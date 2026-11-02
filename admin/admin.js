/* Private analytics page. Uses the session the account page keeps in this
   browser and calls public.admin_dashboard, which decides on the server who
   may see the figures. This file holds no secret and grants nothing: a
   session for any other account gets 403. Every value is written with
   textContent, never as HTML. */
(function () {
  'use strict';

  var SUPABASE_URL = 'https://sokcwfqvutnjzzbsuhqm.supabase.co';
  var SUPABASE_PUBLISHABLE_KEY = 'sb_publishable_GqY0_BwdTP4gcnsPBJ-73g_de3r-toA';
  var STORE_KEY = 'kapture.session';

  var main = document.querySelector('.ad');
  var body = document.getElementById('adBody');
  var meta = document.getElementById('adMeta');
  var days = 30;

  /* ---- session (shared with /account/) -------------------------------- */

  function loadSession() {
    try { var raw = localStorage.getItem(STORE_KEY); return raw ? JSON.parse(raw) : null; }
    catch (e) { return null; }
  }
  function saveSession(s) {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(s)); } catch (e) { /* keep going */ }
  }

  function call(session) {
    return fetch(SUPABASE_URL + '/rest/v1/rpc/admin_dashboard', {
      method: 'POST',
      headers: {
        apikey: SUPABASE_PUBLISHABLE_KEY,
        Authorization: 'Bearer ' + session.access_token,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ p_days: days })
    });
  }

  function refresh(session) {
    if (!session.refresh_token) return Promise.resolve(null);
    return fetch(SUPABASE_URL + '/auth/v1/token?grant_type=refresh_token', {
      method: 'POST',
      headers: { apikey: SUPABASE_PUBLISHABLE_KEY, 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh_token: session.refresh_token })
    }).then(function (res) {
      if (!res.ok) return null;
      return res.json().then(function (d) {
        if (!d.access_token) return null;
        var s = { access_token: d.access_token, refresh_token: d.refresh_token };
        saveSession(s);
        return s;
      });
    }).catch(function () { return null; });
  }

  function load() {
    var session = loadSession();
    if (!session || !session.access_token) { main.setAttribute('data-state', 'signed-out'); return; }
    main.setAttribute('data-state', 'loading');
    call(session).then(function (res) {
      if (res.status !== 401) return res;
      return refresh(session).then(function (s) { return s ? call(s) : res; });
    }).then(function (res) {
      if (res.status === 401) { main.setAttribute('data-state', 'signed-out'); return; }
      if (res.status === 403) { main.setAttribute('data-state', 'denied'); return; }
      if (!res.ok) { main.setAttribute('data-state', 'error'); return; }
      return res.json().then(function (data) { render(data); main.setAttribute('data-state', 'ready'); });
    }).catch(function () { main.setAttribute('data-state', 'error'); });
  }

  /* ---- rendering ------------------------------------------------------- */

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined && text !== null) e.textContent = String(text);
    return e;
  }
  function num(v) { return v === null || v === undefined ? '0' : String(v); }
  function money(cents, cur) {
    var n = (Number(cents) || 0) / 100;
    try { return new Intl.NumberFormat('en-GB', { style: 'currency', currency: cur }).format(n); }
    catch (e) { return n.toFixed(2) + ' ' + cur; }
  }
  function classes(o) {
    if (!o) return '';
    var parts = [];
    ['unmarked', 'internal', 'test', 'unknown'].forEach(function (k) { if (o[k]) parts.push(o[k] + ' ' + k); });
    return parts.join(' · ');
  }
  function pairs(o) {
    if (!o) return '';
    return Object.keys(o).sort().map(function (k) { return label(k) + ' ' + o[k]; }).join(' · ');
  }
  function label(k) { return { macos: 'macOS', windows: 'Windows', chrome: 'Chrome' }[k] || k; }

  function section(title, note) {
    var s = el('section', 'ad-section');
    s.appendChild(el('h2', null, title));
    if (note) s.appendChild(el('p', 'ad-note', note));
    body.appendChild(s);
    return s;
  }
  function cards(parent, items) {
    var dl = el('dl', 'ad-cards');
    items.forEach(function (it) {
      var c = el('div', 'ad-card');
      c.appendChild(el('dt', null, it[0]));
      var dd = el('dd', /^[£$€]?[\d.,<]+$/.test(String(it[1])) ? null : 'ad-text', it[1]);
      if (it[2]) dd.appendChild(el('span', 'ad-sub', it[2]));
      c.appendChild(dd);
      dl.appendChild(c);
    });
    parent.appendChild(dl);
  }
  function table(parent, heads, rows, empty) {
    if (!rows.length) { parent.appendChild(el('p', 'ad-empty', empty)); return; }
    var wrap = el('div', 'ad-scroll');
    var t = el('table', 'ad-table');
    var tr = el('tr');
    heads.forEach(function (h) { tr.appendChild(el('th', h.n ? 'n' : null, h.t)); });
    var thead = el('thead'); thead.appendChild(tr); t.appendChild(thead);
    var tb = el('tbody');
    rows.forEach(function (r) {
      var row = el('tr');
      r.forEach(function (v, i) { row.appendChild(el('td', heads[i].n ? 'n' : null, v)); });
      tb.appendChild(row);
    });
    t.appendChild(tb); wrap.appendChild(t); parent.appendChild(wrap);
  }
  function sub(parent, title) {
    var d = el('div'); d.appendChild(el('h3', null, title)); parent.appendChild(d); return d;
  }

  function render(d) {
    while (body.firstChild) body.removeChild(body.firstChild);
    var gen = new Date(d.generated_at);
    meta.textContent = 'Last ' + d.days + ' days · updated ' + gen.toLocaleString('en-GB') +
      ' · collection: anonymous ' + (d.switches.aggregate ? 'on' : 'off') + ', opt-in ' + (d.switches.usage ? 'on' : 'off');

    /* Overview */
    var a = d.accounts, t = d.trials, s = d.subscriptions, dv = d.devices;
    var rev = (d.revenue || []).reduce(function (m, r) {
      m[r.currency] = m[r.currency] || { all: 0, win: 0 };
      m[r.currency].all += Number(r.all_cents) || 0; m[r.currency].win += Number(r.window_cents) || 0; return m;
    }, {});
    var revCur = Object.keys(rev);
    var o = section('Overview',
      'Exact counts from operational records. Accounts are people with a Kapture account; devices are licensed computers; ' +
      'activations are events (one device can activate more than once). "test" = billing test allowlist, "internal" = owner or ' +
      'internal grant, "unmarked" = no marker either way, so not necessarily a customer.');
    cards(o, [
      ['Registered accounts', num(a.registered), '+' + num(a.registered_in_window) + ' in period · ' + classes(a.by_class)],
      ['Confirmed accounts', num(a.confirmed)],
      ['Active trials', num(t.active), num(t.started_in_window) + ' started in period · ' + classes(t.by_class)],
      ['Active subscriptions (live)', num(s.active_live), pairs(s.active_live_by_plan) + (s.active_live ? ' · ' + classes(s.active_live_by_class) : '')],
      ['Revenue (live, all time)', revCur.length ? revCur.map(function (c) { return money(rev[c].all, c); }).join(' + ') : '£0.00',
        revCur.length ? revCur.map(function (c) { return money(rev[c].win, c) + ' in period'; }).join(' · ') : 'No live payments yet'],
      ['Device activations', num(dv.activations_in_window), 'events in period · ' + classes(dv.activations_in_window_by_class)],
      ['Active licensed devices', num(dv.active_in_window), 'seen in period · ' + classes(dv.active_in_window_by_class)]
    ]);
    if ((d.revenue || []).length) {
      table(o, [{ t: 'Revenue by account class' }, { t: 'Payments', n: 1 }, { t: 'All time', n: 1 }, { t: 'In period', n: 1 }],
        d.revenue.map(function (r) { return [r['class'] + ' (' + r.currency + ')', r.payments, money(r.all_cents, r.currency), money(r.window_cents, r.currency)]; }), '');
    }
    var extra = [];
    if (s.set_to_cancel) extra.push(s.set_to_cancel + ' set to cancel');
    if (s.past_due) extra.push(s.past_due + ' past due');
    if (s.test_mode_active) extra.push(s.test_mode_active + ' test-mode subscription(s) excluded');
    if (extra.length) o.appendChild(el('p', 'ad-note', 'Subscriptions: ' + extra.join(' · ') + '.'));

    /* Platforms */
    var p = section('Platforms', 'Devices are licensed computers; licence checks are events.');
    cards(p, [
      ['Active seats', pairs(dv.active_seats) || '0', 'activated and not deactivated'],
      ['Seen in period', pairs(dv.active_in_window_by_platform) || '0', 'devices with a licence check'],
      ['Trials by platform', pairs(t.by_platform) || '0', 'all time']
    ]);
    var g = el('div', 'ad-grid2'); p.appendChild(g);
    table(sub(g, 'App versions (devices seen in period)'), [{ t: 'Platform' }, { t: 'Version' }, { t: 'Devices', n: 1 }],
      dv.versions.map(function (r) { return [label(r.platform), r.version, r.devices]; }), 'No devices seen in this period.');
    table(sub(g, 'Licence checks (events)'), [{ t: 'Platform' }, { t: 'Outcome' }, { t: 'Checks', n: 1 }],
      d.licence_checks.map(function (r) { return [label(r.platform), r.outcome.replace(/_/g, ' '), r.checks]; }), 'No licence checks in this period.');
    table(sub(g, 'Activations by day (events)'), [{ t: 'Day' }, { t: 'Platform' }, { t: 'Activations', n: 1 }],
      dv.activations_by_day.map(function (r) { return [r.day, label(r.platform), r.n]; }), 'No activations in this period.');

    /* Product usage */
    var u = section('Product usage',
      'Anonymous totals have no identifier and count active days and actions, not people. Opted-in figures count installs ' +
      'that chose "Share statistics". Figures from 1 to 4 show as <5.');
    var g2 = el('div', 'ad-grid2'); u.appendChild(g2);
    table(sub(g2, 'Active (anonymous): DAU yesterday · WAU last full week · MAU last full month'),
      [{ t: 'App' }, { t: 'Platform' }, { t: 'DAU', n: 1 }, { t: 'WAU', n: 1 }, { t: 'MAU', n: 1 }, { t: 'First launches', n: 1 }],
      d.anonymous.activity.map(function (r) { return [r.app === 'kapture_pro' ? 'Kapture Pro' : 'Chrome', label(r.platform), r.dau, r.wau, r.mau, r.first_launches]; }),
      d.switches.aggregate ? 'Waiting for the first anonymous totals. Apps send them within about a day of opening.' : 'Anonymous collection is off.');
    table(sub(g2, 'Opted-in installs: DAU · WAU · MAU'),
      [{ t: 'Platform' }, { t: 'DAU', n: 1 }, { t: 'WAU', n: 1 }, { t: 'MAU', n: 1 }],
      d.opt_in.installs.map(function (r) { return [label(r.platform), r.dau, r.wau, r.mau]; }),
      'No opted-in installs yet.');
    table(sub(u, 'Feature use in period (anonymous totals, actions)'), [{ t: 'Platform' }, { t: 'Event' }, { t: 'Total', n: 1 }],
      d.anonymous.features.map(function (r) { return [label(r.platform), r.event.replace(/_/g, ' '), r.total]; }),
      'No feature totals in this period yet.');
    var g3 = el('div', 'ad-grid2'); u.appendChild(g3);
    table(sub(g3, 'Feature adoption (opted-in, last full week)'), [{ t: 'Platform' }, { t: 'Event' }, { t: 'Installs using', n: 1 }],
      d.opt_in.adoption.map(function (r) { return [label(r.platform), r.event.replace(/_/g, ' '), r.percent + '% of ' + r.of]; }),
      'Shown once at least 5 opted-in installs are active in a week.');
    table(sub(g3, 'Retention (opted-in weekly cohorts)'), [{ t: 'Cohort week' }, { t: 'Size', n: 1 }, { t: 'Week', n: 1 }, { t: 'Active', n: 1 }],
      d.opt_in.retention.map(function (r) { return [r.cohort_week, r.size, r.week, r.percent + '%']; }),
      'Shown once a weekly cohort has at least 5 opted-in installs.');
    table(sub(u, 'Versions, OS and languages (anonymous active days in period)'),
      [{ t: 'Platform' }, { t: 'Version' }, { t: 'OS' }, { t: 'Language' }, { t: 'Active days', n: 1 }],
      d.anonymous.versions.map(function (r) { return [label(r.platform), r.version, r.os, r.locale, r.active_days]; }),
      'No anonymous activity in this period yet.');

    var i = d.ingest;
    body.appendChild(el('p', 'ad-note ad-section', 'Collection in period: ' + i.requests + ' requests, ' + i.batches_aggregate +
      ' anonymous and ' + i.batches_usage + ' opt-in batches, ' + i.entries + ' entries, ' + i.limited + ' rate-limited.'));
  }

  /* ---- controls -------------------------------------------------------- */

  main.querySelectorAll('.ad-window button').forEach(function (b) {
    b.addEventListener('click', function () {
      days = Number(b.getAttribute('data-days'));
      main.querySelectorAll('.ad-window button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      load();
    });
  });

  load();
}());
