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

      // Entitlements and activations are read-only for a client: row level
      // security returns this person's rows and nobody else's.
      return Promise.all([
        apiAuthed('/rest/v1/entitlements?select=status,valid_from,valid_until,max_devices,' +
          'products(name),purchases(purchased_at)&status=eq.active&product_id=eq.' + PRODUCT + '&limit=1'),
        apiAuthed('/rest/v1/device_activations?select=device_id,device_name,platform,activated_at' +
          '&deactivated_at=is.null&order=activated_at.asc')
      ]).then(function (rs) {
        if (!rs[0].ok || !rs[1].ok) throw new Error('data');
        return Promise.all([rs[0].json(), rs[1].json()]);
      }).then(function (out) {
        render(out[0][0] || null, out[1] || []);
        setState('signed-in');
      });
    }).catch(function () {
      fail('We could not load your account. Please try again.');
    });
  }

  function render(entitlement, devices) {
    var active = !!entitlement;
    var badge = document.getElementById('acStatus');
    badge.textContent = active ? 'Active' : 'Inactive';
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

    if (!active) {
      note.textContent = 'No active Kapture Pro licence on this account. ' +
        'If you have just bought one, it can take a moment to appear.';
      deviceCard.hidden = true;
      return;
    }

    var purchase = entitlement.purchases || null;
    var product = entitlement.products || null;

    fact('Licence', (product && product.name) || 'Kapture Pro');
    fact('Type', entitlement.valid_until ? 'Subscription' : 'One-time purchase');
    fact('Purchased', date(purchase && purchase.purchased_at) || date(entitlement.valid_from));
    if (entitlement.valid_until) fact('Renews', date(entitlement.valid_until));
    note.textContent = '';

    // Devices
    deviceCard.hidden = false;
    var seats = entitlement.max_devices || 0;
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
    return { access_token: token, refresh_token: p.get('refresh_token') };
  }

  var fromLink = readHash();

  if (fromLink && fromLink.error) {
    fail(fromLink.error === 'access_denied' || /expired/i.test(fromLink.error)
      ? 'That sign-in link has expired or was already used. Please request a new one.'
      : 'We could not complete that sign-in. Please request a new link.');
    var back = document.getElementById('acRetry');
    if (back) back.textContent = 'Back to sign in';
  } else if (fromLink && fromLink.access_token) {
    saveSession(fromLink);
    loadAccount();
  } else {
    session = loadSession();
    if (session && session.access_token) loadAccount();
    else setState('signed-out');
  }
})();
