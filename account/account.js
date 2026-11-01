/* Kapture account · kaptapp.com/account/
 *
 * Deliberately dependency free. The rest of this site loads no third-party
 * script, and the page that handles sign-in is the worst place to start: a CDN
 * bundle here would be able to read the session it is meant to protect. The
 * Supabase REST and Auth endpoints are plain HTTP, and the handful of calls
 * this page needs are written out below instead.
 *
 * The two values below are public by design. The publishable key identifies
 * the project and grants nothing on its own: what it can read or write is
 * decided entirely by row level security, which is why purchases and
 * entitlements have no client write path at all. No service role key, database
 * password or webhook secret is used here, and none would work from a browser.
 */
(function () {
  'use strict';

  var SUPABASE_URL = 'https://sokcwfqvutnjzzbsuhqm.supabase.co';
  var SUPABASE_PUBLISHABLE_KEY = 'sb_publishable_GqY0_BwdTP4gcnsPBJ-73g_de3r-toA';

  var PRODUCT = 'kapture_pro';
  var STORE_KEY = 'kapture.session';
  var RETURN_TO = 'https://kaptapp.com/account/';

  var main = document.querySelector('.ac');
  var live = document.getElementById('acLive');
  if (!main) return;

  /* ---- session -------------------------------------------------------- */

  var session = null;

  function loadSession() {
    try {
      var raw = localStorage.getItem(STORE_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (e) { return null; }
  }

  function saveSession(s) {
    session = s;
    try {
      if (s) localStorage.setItem(STORE_KEY, JSON.stringify(s));
      else localStorage.removeItem(STORE_KEY);
    } catch (e) { /* private mode: the page still works for this visit */ }
  }

  /* ---- http ----------------------------------------------------------- */

  function api(path, opts) {
    opts = opts || {};
    var headers = { apikey: SUPABASE_PUBLISHABLE_KEY };
    if (opts.body) headers['Content-Type'] = 'application/json';
    if (opts.auth !== false && session && session.access_token) {
      headers.Authorization = 'Bearer ' + session.access_token;
    }
    if (opts.headers) {
      Object.keys(opts.headers).forEach(function (k) { headers[k] = opts.headers[k]; });
    }
    return fetch(SUPABASE_URL + path, {
      method: opts.method || 'GET',
      headers: headers,
      body: opts.body ? JSON.stringify(opts.body) : undefined
    });
  }

  /* A 401 usually means the access token aged out rather than that the person
     is signed out, so try the refresh token once before giving up on them. */
  function apiAuthed(path, opts) {
    return api(path, opts).then(function (res) {
      if (res.status !== 401) return res;
      return refresh().then(function (ok) {
        return ok ? api(path, opts) : res;
      });
    });
  }

  function refresh() {
    if (!session || !session.refresh_token) return Promise.resolve(false);
    return api('/auth/v1/token?grant_type=refresh_token', {
      method: 'POST',
      auth: false,
      body: { refresh_token: session.refresh_token }
    }).then(function (res) {
      if (!res.ok) return false;
      return res.json().then(function (data) {
        if (!data.access_token) return false;
        saveSession({ access_token: data.access_token, refresh_token: data.refresh_token });
        return true;
      });
    }).catch(function () { return false; });
  }

  /* ---- state ---------------------------------------------------------- */

  function setState(name) {
    main.setAttribute('data-state', name);
    main.querySelectorAll('.ac-panel').forEach(function (p) {
      p.setAttribute('aria-hidden', p.getAttribute('data-panel') === name ? 'false' : 'true');
    });
  }

  function say(msg) { if (live) live.textContent = msg; }

  function fail(message) {
    var el = document.getElementById('acErrorText');
    if (el) el.textContent = message || 'We could not load your account.';
    setState('error');
  }

  /* ---- formatting ----------------------------------------------------- */

  var PLATFORMS = {
    macos: 'macOS', windows: 'Windows', linux: 'Linux',
    chrome: 'Chrome', ios: 'iOS', android: 'Android'
  };

  function platformName(p) { return PLATFORMS[p] || 'Device'; }

  function date(iso) {
    if (!iso) return null;
    var d = new Date(iso);
    if (isNaN(d)) return null;
    return d.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' });
  }

  function text(el, value) { el.textContent = value; return el; }

  /* ---- account view --------------------------------------------------- */

  function loadAccount() {
    setState('loading');

    return apiAuthed('/auth/v1/user').then(function (res) {
      if (res.status === 401 || res.status === 403) { signOutLocal(); return null; }
      if (!res.ok) throw new Error('user');
      return res.json();
    }).then(function (user) {
      if (!user) return;
      text(document.getElementById('acEmailShown'), user.email || '');

      // get_my_access() is the same answer the desktop app gets: whether this
      // account is Pro, on which plan, in which state, and the trial dates. The
      // entitlement row is read only for a one-off purchase date. All of it is
      // read-only for a client: row level security returns this person's rows.
      return Promise.all([
        apiAuthed('/rest/v1/rpc/get_my_access', { method: 'POST', body: { p_product_id: PRODUCT } }),
        apiAuthed('/rest/v1/entitlements?select=status,valid_from,valid_until,max_devices,' +
          'products(name),purchases(purchased_at)&status=eq.active&product_id=eq.' + PRODUCT + '&limit=1'),
        apiAuthed('/rest/v1/device_activations?select=device_id,device_name,platform,activated_at' +
          '&deactivated_at=is.null&order=activated_at.asc')
      ]).then(function (rs) {
        if (!rs[0].ok || !rs[1].ok || !rs[2].ok) throw new Error('data');
        return Promise.all([rs[0].json(), rs[1].json(), rs[2].json()]);
      }).then(function (out) {
        render(out[0][0] || null, out[1][0] || null, out[2] || []);
        setState('signed-in');
      });
    }).catch(function () {
      fail('We could not load your account. Please try again.');
    });
  }

  /* What the licence card says, from get_my_access() alone. A trial has an end
     date but no payment method and no renewal, so it is never described as a
     subscription, and "Renews" is shown only for a paid plan that will renew. */
  var PLAN_NAMES = { monthly: 'Subscription, monthly', annual: 'Subscription, annual',
    purchase: 'One-time purchase', manual: 'Licence granted by Kapture' };

  function licenceView(access, entitlement) {
    var a = access || {};
    var paid = a.plan === 'monthly' || a.plan === 'annual';
    var v = { badge: 'Inactive', facts: [], note: '' };

    if (a.pro && a.plan === 'trial') {
      v.badge = 'Free trial';
      v.facts = [['Status', 'Free trial'], ['Type', 'Trial'],
        ['Started', date(a.trial_started_at)], ['Trial ends', date(a.trial_ends_at)]];
    } else if (a.pro && paid) {
      var status = a.state === 'past_due' ? 'Payment due'
        : a.state === 'canceling' ? 'Cancelled, active until the end of the period' : 'Active';
      v.badge = a.state === 'past_due' ? 'Payment due' : 'Active';
      v.facts = [['Status', status], ['Type', PLAN_NAMES[a.plan]],
        [a.state === 'canceling' ? 'Ends' : a.state === 'past_due' ? 'Access until' : 'Renews',
          date(a.access_until)]];
    } else if (a.pro) {
      var purchase = entitlement && entitlement.purchases;
      v.badge = 'Active';
      v.facts = [['Status', 'Active'], ['Type', PLAN_NAMES[a.plan] || 'Licence'],
        ['Purchased', a.plan === 'purchase' ? date(purchase && purchase.purchased_at) : null],
        ['Valid until', a.access_until ? date(a.access_until) : 'No end date']];
    } else if (a.state === 'expired' && a.plan === 'trial') {
      v.facts = [['Status', 'Trial ended'], ['Type', 'Trial'], ['Trial ended', date(a.trial_ends_at)]];
      v.note = 'Your free trial has ended. Your captures and library stay on your computer.';
    } else if (a.state === 'expired' && paid) {
      v.facts = [['Status', 'Ended'], ['Type', PLAN_NAMES[a.plan]], ['Ended', date(a.access_until)]];
      v.note = 'Your subscription has ended. Your captures and library stay on your computer.';
    } else {
      v.note = 'No active Kapture Pro licence on this account. ' +
        'If you have just bought one, it can take a moment to appear.';
    }
    return v;
  }

  function render(access, entitlement, devices) {
    var active = !!(access && access.pro);
    var view = licenceView(access, entitlement);
    var badge = document.getElementById('acStatus');
    badge.textContent = view.badge;
    badge.setAttribute('data-active', active ? 'yes' : 'no');

    var facts = document.getElementById('acFacts');
    facts.innerHTML = '';

    function fact(label, value) {
      if (!value) return;
      var row = document.createElement('div');
      row.appendChild(text(document.createElement('dt'), label));
      row.appendChild(text(document.createElement('dd'), value));
      facts.appendChild(row);
    }

    var note = document.getElementById('acLicenceNote');
    var deviceCard = document.getElementById('acDevices');

    view.facts.forEach(function (f) { fact(f[0], f[1]); });
    note.textContent = redeemedNote || view.note;
    redeemedNote = '';
    showRedeem(access);

    if (!active) {
      deviceCard.hidden = true;
      return;
    }

    // Devices
    deviceCard.hidden = false;
    var seats = access.seats_max || (entitlement && entitlement.max_devices) || 0;
    document.getElementById('acSeats').textContent =
      devices.length + ' of ' + seats + ' in use';

    var list = document.getElementById('acDeviceList');
    list.innerHTML = '';

    if (!devices.length) {
      var empty = document.createElement('li');
      var emptyText = document.createElement('p');
      emptyText.className = 'ac-empty';
      emptyText.textContent =
        'No devices activated yet. Kapture Pro activates this licence when you sign in to the app.';
      empty.appendChild(emptyText);
      list.appendChild(empty);
    }

    devices.forEach(function (d) {
      var li = document.createElement('li');
      li.className = 'ac-device';

      // Built node by node with textContent. A device name is something the
      // user typed on their own machine, so it is never put into innerHTML.
      var info = document.createElement('div');
      var nameEl = document.createElement('p');
      nameEl.className = 'ac-device-name';
      nameEl.textContent = d.device_name || (platformName(d.platform) + ' device');
      var metaEl = document.createElement('p');
      metaEl.className = 'ac-device-meta';
      var when = date(d.activated_at);
      metaEl.textContent = platformName(d.platform) + (when ? ' · activated ' + when : '');
      info.appendChild(nameEl);
      info.appendChild(metaEl);

      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'btn btn-ghost btn-sm';
      btn.textContent = 'Deactivate';
      btn.addEventListener('click', function () { deactivate(d, li, btn); });

      li.appendChild(info);
      li.appendChild(btn);
      list.appendChild(li);
    });

    document.getElementById('acDeviceNote').textContent = devices.length
      ? 'Deactivating frees a seat so you can use Kapture Pro on another machine.'
      : '';
  }

  /* ---- deactivate ------------------------------------------------------
     The RPC is the only write a client may make here: device_activations has
     no insert or update policy, because the seat limit has to be checked and
     taken in one step, which a policy cannot do.

     A successful HTTP status is not proof the row changed. Row level security
     filters rows out silently, so a write that touched nothing comes back
     looking exactly like a write that worked. The list is therefore re-read
     from the database afterwards and the device confirmed gone before the
     person is told anything succeeded. */

  function deactivate(device, li, btn) {
    btn.disabled = true;
    li.setAttribute('data-busy', 'yes');
    say('Deactivating…');

    apiAuthed('/rest/v1/rpc/deactivate_device', {
      method: 'POST',
      body: { p_device_id: device.device_id, p_product_id: PRODUCT }
    }).then(function (res) {
      if (!res.ok) throw new Error('rpc');
      return res.json();
    }).then(function (released) {
      // Re-read the authoritative list rather than trusting the call.
      return apiAuthed('/rest/v1/device_activations?select=device_id&deactivated_at=is.null')
        .then(function (res) {
          if (!res.ok) throw new Error('verify');
          return res.json();
        }).then(function (rows) {
          var stillThere = rows.some(function (r) { return r.device_id === device.device_id; });
          if (stillThere) throw new Error('unchanged');
          say('Device deactivated.');
          return loadAccount();
        });
    }).catch(function (err) {
      btn.disabled = false;
      li.removeAttribute('data-busy');
      var msg = err && err.message === 'unchanged'
        ? 'That device is still active. Nothing was changed, so please try again.'
        : 'We could not deactivate that device. Please try again.';
      say(msg);
      fail(msg);
    });
  }

  /* ---- sign in / out --------------------------------------------------- */

  var form = document.getElementById('acForm');
  var emailInput = document.getElementById('acEmail');
  var emailError = document.getElementById('acEmailError');

  function showEmailError(msg) {
    emailError.textContent = msg;
    emailError.hidden = !msg;
    emailInput.setAttribute('aria-invalid', msg ? 'true' : 'false');
  }

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = (emailInput.value || '').trim();
      if (!email || email.indexOf('@') < 1 || email.indexOf('.') < 0) {
        showEmailError('Enter the email address you use for Kapture.');
        emailInput.focus();
        return;
      }
      showEmailError('');

      var send = document.getElementById('acSend');
      send.disabled = true;
      send.textContent = 'Sending…';

      api('/auth/v1/otp?redirect_to=' + encodeURIComponent(RETURN_TO), {
        method: 'POST',
        auth: false,
        body: { email: email, create_user: true }
      }).then(function (res) {
        send.disabled = false;
        send.textContent = 'Email me a link';
        if (!res.ok) {
          // The most common cause is the sender's hourly limit, and saying so
          // is more useful than a generic failure.
          showEmailError(res.status === 429
            ? 'Too many sign-in emails just now. Please wait a minute and try again.'
            : 'We could not send that link. Please check the address and try again.');
          return;
        }
        document.getElementById('acSentTo').textContent = email;
        setState('link-sent');
        say('Sign-in link sent to ' + email);
      }).catch(function () {
        send.disabled = false;
        send.textContent = 'Email me a link';
        showEmailError('We could not reach the server. Please try again.');
      });
    });
  }

  var another = document.getElementById('acUseAnother');
  if (another) {
    another.addEventListener('click', function () {
      setState('signed-out');
      emailInput.focus();
    });
  }

  function signOutLocal() {
    saveSession(null);
    setState('signed-out');
  }

  var signOut = document.getElementById('acSignOut');
  if (signOut) {
    signOut.addEventListener('click', function () {
      signOut.disabled = true;
      // Revoke server side too, so the refresh token cannot be reused.
      apiAuthed('/auth/v1/logout', { method: 'POST', body: {} })
        .catch(function () { /* local sign-out still happens */ })
        .then(function () {
          signOut.disabled = false;
          signOutLocal();
          say('Signed out.');
        });
    });
  }

  var retry = document.getElementById('acRetry');
  if (retry) {
    retry.addEventListener('click', function () {
      if (session) loadAccount(); else setState('signed-out');
    });
  }

  /* ---- connect Kapture Pro --------------------------------------------
     Kapture Pro signs in through this page (docs/desktop-auth-contract.md in
     the backend repository). The app listens on 127.0.0.1 and opens
     /account/?app=connect&port=…&state=…&platform=…. The request is kept here
     for 15 minutes and the normal emailed link is sent. When that link comes
     back in this browser, the new session is offered to the app instead of
     being kept by this page, and it reaches the app only after a click on
     Connect, as a form POST to the loopback address: a navigation, because
     browsers block fetch() from a public page to 127.0.0.1, and a POST body,
     so the tokens are never in a URL. A session this page already had is left
     alone, and nothing here is logged. */

  var CONNECT_KEY = 'kapture.app_connect';
  var CONNECT_TTL = 15 * 60 * 1000;

  var handoff = null;   // { tokens, req } while the Connect question is on screen

  function validConnect(r) {
    return !!r && typeof r.port === 'number' && r.port % 1 === 0 &&
      r.port >= 1024 && r.port <= 65535 &&
      typeof r.state === 'string' && /^[A-Za-z0-9_-]{43}$/.test(r.state) &&
      (r.platform === 'macos' || r.platform === 'windows');
  }

  // The request the app opened this page with, if any. It is taken out of the
  // address bar at once, valid or not.
  function connectFromQuery() {
    var q = new URLSearchParams(location.search);
    if (q.get('app') !== 'connect') return null;
    history.replaceState(null, '', location.pathname + location.hash);
    var port = q.get('port') || '';
    var req = {
      port: /^[1-9][0-9]{3,4}$/.test(port) ? Number(port) : 0,
      state: q.get('state') || '',
      platform: q.get('platform') || '',
      expires: Date.now() + CONNECT_TTL
    };
    return validConnect(req) ? req : { invalid: true };
  }

  function storeConnect(req) {
    try { localStorage.setItem(CONNECT_KEY, JSON.stringify(req)); return true; }
    catch (e) { return false; }
  }

  function dropConnect() {
    try { localStorage.removeItem(CONNECT_KEY); } catch (e) { /* nothing stored */ }
  }

  // The stored request, only while it is valid and unexpired.
  function loadConnect() {
    var req = null;
    try { req = JSON.parse(localStorage.getItem(CONNECT_KEY) || 'null'); } catch (e) { return null; }
    if (!req) return null;
    if (!validConnect(req) || !(req.expires > Date.now())) { dropConnect(); return null; }
    return req;
  }

  function asBearer(token, opts) {
    opts.auth = false;
    opts.headers = { Authorization: 'Bearer ' + token };
    return opts;
  }

  // Ends a session that was never handed over, so it cannot be used later.
  function endSession(token) {
    api('/auth/v1/logout?scope=local', asBearer(token, { method: 'POST', body: {} }))
      .catch(function () { /* it also expires on its own */ });
  }

  function closeConnect(title, message) {
    document.getElementById('acConnectTitle').textContent = title;
    document.getElementById('acConnectLead').hidden = true;
    document.getElementById('acConnectActions').hidden = true;
    document.getElementById('acConnectHint').textContent = message;
    setState('connect');
    say(title);
  }

  function offerConnect(tokens, req) {
    handoff = { tokens: tokens, req: req };
    setState('loading');
    api('/auth/v1/user', asBearer(tokens.access_token, {})).then(function (res) {
      if (!res.ok) throw new Error('user');
      return res.json();
    }).then(function (user) {
      if (!user || !user.id) throw new Error('user');
      handoff.userId = user.id;
      text(document.getElementById('acConnectEmail'), user.email || 'your account');
      setState('connect');
      document.getElementById('acConnectYes').focus();
    }).catch(function () {
      endSession(tokens.access_token);
      handoff = null;
      fail('We could not check that sign-in, so Kapture Pro was not connected. ' +
        'Request a new link, or start again from the app.');
    });
  }

  // The account a stored session belongs to, read from its own token; null
  // when it cannot be read, which is treated as someone else's session.
  function sessionUserId(s) {
    try {
      var part = s.access_token.split('.')[1].replace(/-/g, '+').replace(/_/g, '/');
      return JSON.parse(atob(part + '===='.slice(part.length % 4 || 4))).sub || null;
    } catch (e) { return null; }
  }

  // So that "Manage Account" in the app finds this browser signed in, keep a
  // second, independent session here when Kapture Pro is connected (the link's
  // own session goes to the app). It never replaces a session for another
  // account, and nothing about connecting the app depends on it: any failure
  // or a slow answer simply leaves this browser as it was.
  function keepBrowserSession(h) {
    var existing = loadSession();
    if (existing && existing.access_token) {
      return Promise.resolve(sessionUserId(existing) === h.userId ? 'already' : 'other-account');
    }
    var controller = typeof AbortController === 'function' ? new AbortController() : null;
    var timer = controller ? setTimeout(function () { controller.abort(); }, 6000) : null;
    return fetch(SUPABASE_URL + '/functions/v1/browser-session', {
      method: 'POST',
      headers: { apikey: SUPABASE_PUBLISHABLE_KEY, Authorization: 'Bearer ' + h.tokens.access_token,
        'Content-Type': 'application/json' },
      body: '{}',
      cache: 'no-store',
      signal: controller ? controller.signal : undefined
    }).then(function (res) {
      if (!res.ok) return 'none';
      return res.json().then(function (s) {
        if (!s || typeof s.access_token !== 'string' || typeof s.refresh_token !== 'string') return 'none';
        if (sessionUserId(s) !== h.userId) return 'none';
        saveSession({ access_token: s.access_token, refresh_token: s.refresh_token });
        return 'signed-in';
      });
    }).catch(function () { return 'none'; }).then(function (result) {
      if (timer) clearTimeout(timer);
      return result;
    });
  }

  var connectYes = document.getElementById('acConnectYes');
  if (connectYes) {
    connectYes.addEventListener('click', function () {
      if (!handoff) return;
      var h = handoff;
      handoff = null;
      // Single use: the request is gone before anything is sent, and it must
      // still be the same, unexpired request the question was asked for.
      var req = loadConnect();
      dropConnect();
      if (!req || req.state !== h.req.state) {
        endSession(h.tokens.access_token);
        closeConnect('Not connected', 'The request from Kapture Pro has expired. Start again from the app.');
        return;
      }
      closeConnect('Connecting Kapture Pro',
        'Your browser is handing the sign-in to Kapture Pro. If it shows an error page instead, ' +
        'Kapture Pro was no longer waiting or this browser blocked the connection: start again from the app.');
      keepBrowserSession(h).then(function () {
        var post = document.createElement('form');
        post.method = 'POST';
        post.action = 'http://127.0.0.1:' + req.port + '/kapture-auth/callback';
        [['state', req.state], ['access_token', h.tokens.access_token],
          ['refresh_token', h.tokens.refresh_token], ['expires_at', h.tokens.expires_at || '']
        ].forEach(function (f) {
          var input = document.createElement('input');
          input.type = 'hidden';
          input.name = f[0];
          input.value = f[1];
          post.appendChild(input);
        });
        document.body.appendChild(post);
        post.submit();
        // The browser has already copied the fields; they do not stay in the page.
        post.remove();
      });
    });
  }

  var connectNo = document.getElementById('acConnectNo');
  if (connectNo) {
    connectNo.addEventListener('click', function () {
      if (!handoff) return;
      var h = handoff;
      handoff = null;
      dropConnect();
      endSession(h.tokens.access_token);
      closeConnect('Not connected', 'Kapture Pro was not connected, and that sign-in has been ended. You can close this tab.');
    });
  }

  /* ---- access code ----------------------------------------------------
     A friends-and-family code gives this account Kapture Pro with no end date
     and nothing to pay; the database decides everything (redeem_access_code).
     A link like /account/?code=RAYFAM fills the code in: it is taken out of
     the address bar at once and kept for an hour, so it survives the emailed
     sign-in link. Redeeming always takes a click. */

  var CODE_KEY = 'kapture.access_code';
  var CODE_TTL = 60 * 60 * 1000;
  var redeemedNote = '';

  function cleanCode(v) { return String(v || '').replace(/\s+/g, '').toUpperCase(); }
  function validCode(v) { return /^[A-Z0-9]{4,32}$/.test(v); }

  function codeFromQuery() {
    var q = new URLSearchParams(location.search);
    if (!q.has('code')) return;
    var code = cleanCode(q.get('code'));
    q.delete('code');
    var rest = q.toString();
    history.replaceState(null, '', location.pathname + (rest ? '?' + rest : '') + location.hash);
    if (!validCode(code)) return;
    try { localStorage.setItem(CODE_KEY, JSON.stringify({ code: code, expires: Date.now() + CODE_TTL })); }
    catch (e) { /* the code can still be typed in */ }
  }

  function storedCode() {
    try {
      var c = JSON.parse(localStorage.getItem(CODE_KEY) || 'null');
      if (c && validCode(c.code) && c.expires > Date.now()) return c.code;
      localStorage.removeItem(CODE_KEY);
    } catch (e) { /* nothing stored */ }
    return '';
  }

  function dropCode() {
    try { localStorage.removeItem(CODE_KEY); } catch (e) { /* nothing stored */ }
  }

  var redeemCard = document.getElementById('acRedeem');
  var redeemForm = document.getElementById('acRedeemForm');
  var codeInput = document.getElementById('acCode');
  var codeError = document.getElementById('acCodeError');
  var redeemBtn = document.getElementById('acRedeemBtn');

  function showCodeError(msg) {
    codeError.textContent = msg;
    codeError.hidden = !msg;
    codeInput.setAttribute('aria-invalid', msg ? 'true' : 'false');
  }

  // Worth offering only while a code could help: no licence, a trial, or a
  // subscription that has been cancelled and will not renew.
  function showRedeem(access) {
    if (!redeemCard) return;
    var a = access || {};
    redeemCard.hidden = !(!a.pro || a.plan === 'trial' || a.state === 'canceling');
    if (!redeemCard.hidden && !codeInput.value) codeInput.value = storedCode();
  }

  var REDEEM_ANSWERS = {
    already_redeemed: 'This account has already redeemed that code.',
    already_has_access: 'This account already has a Kapture Pro licence, so there is nothing to redeem.',
    has_subscription: 'This account has a subscription that renews. Cancel the renewal first, then enter the code again: nothing more will be charged.',
    invalid: 'That code is not valid or is no longer available.',
    rate_limited: 'Too many attempts. Please try again in an hour.'
  };

  if (redeemForm) {
    redeemForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var code = cleanCode(codeInput.value);
      if (!validCode(code)) {
        showCodeError('Enter the code exactly as you received it.');
        codeInput.focus();
        return;
      }
      showCodeError('');
      redeemBtn.disabled = true;
      redeemBtn.textContent = 'Redeeming…';

      apiAuthed('/rest/v1/rpc/redeem_access_code', { method: 'POST', body: { p_code: code } }).then(function (res) {
        if (res.status === 401) { signOutLocal(); return null; }
        if (!res.ok) throw new Error('rpc');
        return res.json();
      }).then(function (answer) {
        redeemBtn.disabled = false;
        redeemBtn.textContent = 'Redeem';
        if (answer === null) return;
        if (answer === 'granted') {
          dropCode();
          codeInput.value = '';
          redeemedNote = 'Code redeemed. Kapture Pro is now active on this account with no end date and nothing to pay. ' +
            'Sign in to Kapture Pro on your computer with this email address to use it.';
          say('Code redeemed. Kapture Pro is active.');
          return loadAccount();
        }
        if (answer !== 'rate_limited' && answer !== 'invalid') dropCode();
        showCodeError(REDEEM_ANSWERS[answer] || 'We could not redeem that code. Please try again.');
      }).catch(function () {
        redeemBtn.disabled = false;
        redeemBtn.textContent = 'Redeem';
        showCodeError('We could not redeem that code. Please try again.');
      });
    });
  }

  /* ---- boot ------------------------------------------------------------ */

  function readHash() {
    if (!location.hash || location.hash.length < 2) return null;
    var p = new URLSearchParams(location.hash.slice(1));
    var token = p.get('access_token');
    var error = p.get('error_description') || p.get('error');
    if (!token && !error) return null;
    // Take the tokens out of the address bar immediately: they should not sit
    // in history, or be read by anything that can see the URL.
    history.replaceState(null, '', location.pathname);
    if (error) return { error: error };
    return { access_token: token, refresh_token: p.get('refresh_token'), expires_at: p.get('expires_at') };
  }

  codeFromQuery();
  if (storedCode()) document.getElementById('acCodeNote').hidden = false;
  var connectAsk = connectFromQuery();
  var fromLink = readHash();
  var pending = fromLink && fromLink.access_token ? loadConnect() : null;

  if (connectAsk && connectAsk.invalid) {
    fail('This request from Kapture Pro is not valid. Start again from the app.');
  } else if (connectAsk) {
    // A sign-in should never arrive together with a new request; end it
    // rather than leave it unused.
    if (fromLink && fromLink.access_token) endSession(fromLink.access_token);
    if (storeConnect(connectAsk)) {
      document.getElementById('acConnectNote').hidden = false;
      setState('signed-out');
    } else {
      fail('This browser is not letting kaptapp.com remember the request from Kapture Pro, so it cannot connect. ' +
        'Allow site data for kaptapp.com or use another browser, then start again from the app.');
    }
  } else if (fromLink && fromLink.error) {
    fail(fromLink.error === 'access_denied' || /expired/i.test(fromLink.error)
      ? 'That sign-in link has expired or was already used. Please request a new one.'
      : 'We could not complete that sign-in. Please request a new link.');
    var back = document.getElementById('acRetry');
    if (back) back.textContent = 'Back to sign in';
  } else if (pending) {
    // Kapture Pro asked for this sign-in: it is offered to the app and never
    // saved here. The website keeps whatever session it already had.
    session = loadSession();
    offerConnect(fromLink, pending);
  } else if (fromLink && fromLink.access_token) {
    saveSession({ access_token: fromLink.access_token, refresh_token: fromLink.refresh_token });
    loadAccount();
  } else {
    session = loadSession();
    if (session && session.access_token) loadAccount();
    else setState('signed-out');
  }
})();
