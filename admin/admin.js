/* Private analytics dashboard (V2).
   Uses the session the account page keeps in this browser and calls
   public.admin_dashboard_v2, which decides on the server who may see the
   figures: any other account gets 403. Filters are sent to the server and
   change the queries. Every value is written with textContent or as SVG
   attributes, never as HTML. Class names use the kd- prefix on purpose. */
(function () {
  'use strict';

  var SUPABASE_URL = 'https://sokcwfqvutnjzzbsuhqm.supabase.co';
  var SUPABASE_PUBLISHABLE_KEY = 'sb_publishable_GqY0_BwdTP4gcnsPBJ-73g_de3r-toA';
  var STORE_KEY = 'kapture.session';
  var PREFS_KEY = 'kapture.dashboard';
  var SVGNS = 'http://www.w3.org/2000/svg';
  var VIEWS = ['overview', 'customers', 'devices', 'usage', 'health'];

  var main = document.querySelector('.kd');
  var body = document.getElementById('kdBody');
  var meta = document.getElementById('kdMeta');
  var chips = document.getElementById('kdChips');
  var form = document.getElementById('kdFilters');
  var data = null;
  var inflight = 0;

  /* ---- preferences (per browser only) --------------------------------- */

  var prefs = { period: '30', from: '', to: '', platform: 'all', klass: 'all', plan: 'all' };
  try { var saved = JSON.parse(localStorage.getItem(PREFS_KEY) || 'null'); if (saved) Object.keys(prefs).forEach(function (k) { if (saved[k]) prefs[k] = saved[k]; }); }
  catch (e) { /* defaults */ }
  function savePrefs() { try { localStorage.setItem(PREFS_KEY, JSON.stringify(prefs)); } catch (e) { /* optional */ } }

  /* ---- session (shared with /account/) -------------------------------- */

  function loadSession() {
    try { var raw = localStorage.getItem(STORE_KEY); return raw ? JSON.parse(raw) : null; }
    catch (e) { return null; }
  }
  function saveSession(s) { try { localStorage.setItem(STORE_KEY, JSON.stringify(s)); } catch (e) { /* keep going */ } }

  function call(session, args) {
    return fetch(SUPABASE_URL + '/rest/v1/rpc/admin_dashboard_v2', {
      method: 'POST',
      headers: { apikey: SUPABASE_PUBLISHABLE_KEY, Authorization: 'Bearer ' + session.access_token, 'Content-Type': 'application/json' },
      body: JSON.stringify(args)
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

  /* ---- dates ------------------------------------------------------------ */

  function iso(d) { return d.toISOString().slice(0, 10); }
  function utcToday() { var n = new Date(); return new Date(Date.UTC(n.getUTCFullYear(), n.getUTCMonth(), n.getUTCDate())); }
  function range() {
    var today = utcToday();
    if (prefs.period === 'custom' && prefs.from && prefs.to) return { from: prefs.from, to: prefs.to };
    var days = Number(prefs.period) || 30;
    var from = new Date(today); from.setUTCDate(from.getUTCDate() - (days - 1));
    return { from: iso(from), to: iso(today) };
  }
  function fmtDay(s, opts) { return new Date(s + 'T00:00:00Z').toLocaleDateString('en-GB', Object.assign({ day: 'numeric', month: 'short', timeZone: 'UTC' }, opts || {})); }

  /* ---- load --------------------------------------------------------------- */

  function load() {
    var session = loadSession();
    if (!session || !session.access_token) { main.setAttribute('data-state', 'signed-out'); return; }
    var r = range();
    var args = { p_from: r.from, p_to: r.to, p_platform: prefs.platform, p_class: prefs.klass, p_plan: prefs.plan };
    var mine = ++inflight;
    main.setAttribute('data-state', data ? 'refreshing' : 'loading');
    call(session, args).then(function (res) {
      if (res.status !== 401) return res;
      return refresh(session).then(function (s) { return s ? call(s, args) : res; });
    }).then(function (res) {
      if (mine !== inflight) return;
      if (res.status === 401) { main.setAttribute('data-state', 'signed-out'); return; }
      if (res.status === 403) { main.setAttribute('data-state', 'denied'); return; }
      if (res.status === 400) { showError('Those filters are not valid. Choose a period of up to a year, ending today or earlier.'); return; }
      if (!res.ok) { showError('The figures could not be loaded.'); return; }
      return res.json().then(function (d) { data = d; main.setAttribute('data-state', 'ready'); render(); });
    }).catch(function () { if (mine === inflight) showError('The figures could not be loaded. Check the connection and try again.'); });
  }
  function showError(msg) { document.getElementById('kdError').textContent = msg; main.setAttribute('data-state', 'error'); }

  /* ---- small DOM helpers ----------------------------------------------- */

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined && text !== null) e.textContent = String(text);
    return e;
  }
  function svg(tag, attrs) {
    var e = document.createElementNS(SVGNS, tag);
    Object.keys(attrs || {}).forEach(function (k) { e.setAttribute(k, attrs[k]); });
    return e;
  }
  function tip(text) {
    var w = el('span', 'kd-tip');
    var b = el('button', null, 'i'); b.type = 'button'; b.setAttribute('aria-label', 'About this metric: ' + text);
    w.appendChild(b); w.appendChild(el('span', 'kd-tip-body', text));
    return w;
  }
  function n(v) { var x = Number(v); return isFinite(x) ? x : 0; }
  function int(v) { return n(v).toLocaleString('en-GB'); }
  function isSupp(v) { return v === '<5'; }
  function money(cents, cur) {
    try { return new Intl.NumberFormat('en-GB', { style: 'currency', currency: cur || 'GBP' }).format(n(cents) / 100); }
    catch (e) { return (n(cents) / 100).toFixed(2) + ' ' + cur; }
  }
  var PLATFORM = { macos: 'macOS', windows: 'Windows', chrome: 'Chrome', other: 'Unknown', unknown: 'Unknown' };
  function plat(k) { return PLATFORM[k] || k; }
  function words(s) { return String(s).replace(/_/g, ' '); }
  function cap(s) { s = String(s); return s.charAt(0).toUpperCase() + s.slice(1); }

  /* A filter that does not apply to a group of metrics is named, so an
     unfiltered figure is never presented as filtered. */
  function scope(groups) {
    var notes = [];
    var f = data.filters, ap = data.applies;
    if (f.platform !== 'all' && groups.some(function (g) { return ap.platform.indexOf(g) < 0; })) notes.push('platform');
    if (f['class'] !== 'all' && groups.some(function (g) { return ap['class'].indexOf(g) < 0; })) notes.push('account class');
    if (f.plan !== 'all' && groups.some(function (g) { return ap.plan.indexOf(g) < 0; })) notes.push('plan');
    return notes.length ? 'Not filtered by ' + notes.join(' or ') : '';
  }

  /* ---- components ------------------------------------------------------- */

  var periodLabel = function () { return data.period.days + ' days'; };

  /* Comparison with the previous equal period. A percentage needs a base of
     at least 5; below that only the absolute difference is meaningful. */
  function delta(cur, prev) {
    cur = n(cur); prev = n(prev);
    var d = cur - prev;
    var s = el('span');
    if (prev >= 5) {
      var pct = Math.round(100 * d / prev);
      s.textContent = (pct > 0 ? '▲ ' : pct < 0 ? '▼ ' : '') + Math.abs(pct) + '% vs previous ' + periodLabel();
    } else {
      s.textContent = (d > 0 ? '+' : d < 0 ? '−' : '±') + Math.abs(d) + ' vs ' + prev + ' in previous ' + periodLabel();
    }
    if (d > 0) s.className = 'kd-up'; else if (d < 0) s.className = 'kd-down';
    return s;
  }

  function kpi(parent, label, value, foot, help) {
    var c = el('div', 'kd-kpi');
    var l = el('div', 'kd-kpi-label', label);
    if (help) l.appendChild(tip(help));
    c.appendChild(l);
    var v = el('div', 'kd-kpi-value', value);
    if (!/^[£$€−+]?[\d.,%<]+$/.test(String(value))) v.className += ' is-text';
    c.appendChild(v);
    if (foot) { var f = el('div', 'kd-kpi-foot'); if (typeof foot === 'string') f.textContent = foot; else f.appendChild(foot); c.appendChild(f); }
    parent.appendChild(c);
    return c;
  }
  function kpis(parent) { var g = el('div', 'kd-kpis'); parent.appendChild(g); return g; }

  function panel(grid, span, title, sub, help) {
    var p = el('section', 'kd-panel kd-span-' + span);
    var h = el('h2', null, title);
    if (help) h.appendChild(tip(help));
    p.appendChild(h);
    if (sub) p.appendChild(el('p', 'kd-panel-sub', sub));
    grid.appendChild(p);
    return p;
  }
  function grid(parent) { var g = el('div', 'kd-grid'); parent.appendChild(g); return g; }
  function empty(parent, text) { parent.appendChild(el('div', 'kd-empty', text)); }

  /* Daily bars. Values may be numbers or "<5" (suppressed): those draw as a
     short grey bar so the day is visibly non-zero without a false height. */
  function bars(parent, series, keys, opts) {
    opts = opts || {};
    var vals = series.map(function (p) { return keys.map(function (k) { return p[k]; }); });
    var total = function (row) { return row.reduce(function (s, v) { return s + (isSupp(v) ? 0 : n(v)); }, 0); };
    var anySupp = vals.some(function (r) { return r.some(isSupp); });
    var max = Math.max.apply(null, vals.map(total).concat([anySupp ? 4 : 0]));
    if (!max) { empty(parent, opts.empty || 'Nothing recorded in this period.'); return; }
    var W = Math.max(260, Math.round(parent.clientWidth - 36) || 640), H = 150, pad = { l: 30, b: 20, t: 6 }, iw = W - pad.l, ih = H - pad.b - pad.t;
    var bw = iw / series.length, gap = Math.min(4, bw * 0.25);
    var s = svg('svg', { viewBox: '0 0 ' + W + ' ' + H, role: 'img', 'aria-label': opts.label || 'Daily chart' });
    var top = niceMax(max);
    [0, 0.5, 1].forEach(function (f) {
      var y = pad.t + ih - f * ih;
      s.appendChild(svg('line', { x1: pad.l, x2: W, y1: y, y2: y, 'class': 'kd-grid-line' }));
      if (f === 0.5 && (opts.money ? (top / 2) % 100 : (top / 2) % 1)) return;  // no rounded half labels
      var t = svg('text', { x: pad.l - 6, y: y + 4, 'text-anchor': 'end', 'class': 'kd-axis' }); t.textContent = fmtAxis(top * f, opts.money); s.appendChild(t);
    });
    series.forEach(function (p, i) {
      var x = pad.l + i * bw + gap / 2, y0 = pad.t + ih;
      keys.forEach(function (k, j) {
        var v = p[k], h;
        if (isSupp(v)) h = Math.max(2, ih * (2 / top));
        else h = ih * (n(v) / top);
        if (!h) return;
        var r = svg('rect', { x: x, y: y0 - h, width: Math.max(1, bw - gap), height: h, rx: Math.min(2, bw / 4),
                              'class': 'kd-bar' + (isSupp(v) ? ' is-supp' : j ? ' is-b' : '') });
        var t = svg('title'); t.textContent = fmtDay(p.day, { weekday: 'short' }) + ' · ' + (opts.names ? opts.names[j] + ': ' : '') +
          (isSupp(v) ? '<5 (suppressed)' : opts.money ? money(v) : int(v));
        r.appendChild(t); s.appendChild(r);
        y0 -= h;
      });
    });
    var idx = series.length > 2 ? [0, Math.floor((series.length - 1) / 2), series.length - 1] : series.map(function (_, i) { return i; });
    idx.forEach(function (i, k) {
      var t = svg('text', { x: pad.l + i * bw + bw / 2, y: H - 4, 'text-anchor': k === 0 && idx.length > 1 ? 'start' : k === idx.length - 1 && idx.length > 1 ? 'end' : 'middle', 'class': 'kd-axis' });
      t.textContent = fmtDay(series[i].day); s.appendChild(t);
    });
    var c = el('div', 'kd-chart'); c.appendChild(s); parent.appendChild(c);
    if (opts.names && opts.names.length > 1 || anySupp) {
      var lg = el('div', 'kd-legend');
      (opts.names || []).forEach(function (nm, j) { if (opts.names.length > 1) lg.appendChild(el('span', j ? 'is-b' : '', nm)); });
      if (anySupp) lg.appendChild(el('span', 'is-supp', 'fewer than 5 (exact figure withheld)'));
      parent.appendChild(lg);
    }
  }
  function niceMax(v) { if (v <= 4) return 4; var p = Math.pow(10, Math.floor(Math.log10(v))); var m = v / p; return (m <= 1 ? 1 : m <= 2 ? 2 : m <= 5 ? 5 : 10) * p; }
  function fmtAxis(v, isMoney) { return isMoney ? '£' + Math.round(v / 100).toLocaleString('en-GB') : Math.round(v).toLocaleString('en-GB'); }

  /* Ranked horizontal bars for categories. */
  function hbars(parent, rows, emptyText) {
    if (!rows.length) { empty(parent, emptyText); return; }
    var max = Math.max.apply(null, rows.map(function (r) { return isSupp(r.value) ? 4 : n(r.value); })) || 1;
    var ul = el('ul', 'kd-hbars');
    rows.forEach(function (r) {
      var li = el('li');
      li.appendChild(el('span', 'kd-hb-label', r.label));
      li.appendChild(el('span', 'kd-hb-value', r.display !== undefined ? r.display : r.value));
      var tr = el('span', 'kd-hb-track'), f = el('span', 'kd-hb-fill');
      f.style.width = Math.max(2, Math.round(100 * (isSupp(r.value) ? 2 : n(r.value)) / max)) + '%';
      tr.appendChild(f); li.appendChild(tr); ul.appendChild(li);
    });
    parent.appendChild(ul);
  }

  function stats(parent, items) {
    var dl = el('dl', 'kd-stats');
    items.forEach(function (it) { var d = el('div'); d.appendChild(el('dt', null, it[0])); d.appendChild(el('dd', null, it[1])); dl.appendChild(d); });
    parent.appendChild(dl);
  }

  function table(parent, heads, rows, summary) {
    if (!rows.length) return;
    var det = el('details', 'kd-details');
    det.appendChild(el('summary', null, summary || 'Show table'));
    var wrap = el('div', 'kd-scroll'), t = el('table', 'kd-table'), tr = el('tr');
    heads.forEach(function (h) { tr.appendChild(el('th', h.n ? 'n' : null, h.t)); });
    var th = el('thead'); th.appendChild(tr); t.appendChild(th);
    var tb = el('tbody');
    rows.forEach(function (r) { var row = el('tr'); r.forEach(function (v, i) { row.appendChild(el('td', heads[i].n ? 'n' : null, v)); }); tb.appendChild(row); });
    t.appendChild(tb); wrap.appendChild(t); det.appendChild(wrap); parent.appendChild(det);
  }
  function dailyTable(parent, keys, names, isMoney) {
    table(parent, [{ t: 'Day' }].concat(names.map(function (x) { return { t: x, n: 1 }; })),
      data.series.filter(function (p) { return keys.some(function (k) { return isSupp(p[k]) || n(p[k]); }); }).reverse()
        .map(function (p) { return [fmtDay(p.day, { year: 'numeric' })].concat(keys.map(function (k) { return isSupp(p[k]) ? '<5' : isMoney ? money(p[k]) : int(p[k]); })); }),
      'Show daily figures');
  }

  /* ---- views ------------------------------------------------------------- */

  function revenueTotals() {
    var cur = 0, prev = 0, ccy = 'GBP';
    data.kpi.revenue.forEach(function (r) { if (r.currency === 'GBP' || data.kpi.revenue.length === 1) { cur += n(r.cur); prev += n(r.prev); ccy = r.currency; } });
    return { cur: cur, prev: prev, ccy: ccy, other: data.kpi.revenue.filter(function (r) { return r.currency !== ccy; }) };
  }

  function viewOverview(v) {
    var k = data.kpi, rv = revenueTotals();
    var g = kpis(v);
    kpi(g, 'Live revenue', money(rv.cur, rv.ccy), delta(rv.cur / 100, rv.prev / 100),
      'Completed live Stripe payments in the period, all account classes unless filtered. Test-mode payments are excluded.');
    kpi(g, 'Active subscriptions', int(k.active_subscriptions), 'live, now',
      'Live subscriptions currently active or trialing. Test-mode subscriptions are excluded.');
    kpi(g, 'New accounts', int(k.new_accounts.cur), delta(k.new_accounts.cur, k.new_accounts.prev),
      'Kapture accounts created in the period. An account is not necessarily a paying customer.');
    kpi(g, 'Trials started', int(k.trials_started.cur), delta(k.trials_started.cur, k.trials_started.prev),
      'Kapture Pro trials started in the period. Each account can start one trial.');
    kpi(g, 'Active licensed devices', int(k.active_devices), 'seen in the last ' + periodLabel(),
      'Computers with an active seat that checked their licence during the period. A device is not a user.');
    kpi(g, 'Device activations', int(k.activations.cur), delta(k.activations.cur, k.activations.prev),
      'Activation events. One computer can be activated more than once, so this is not a count of devices or people.');
    var sc = scope(['payments', 'accounts', 'subscriptions']);
    if (sc) v.appendChild(el('p', 'kd-scope', 'Revenue, subscriptions and new accounts: ' + sc.toLowerCase() + '.'));

    var gr = grid(v);
    var p1 = panel(gr, 8, 'Accounts, trials and activations', 'Per day, ' + fmtDay(data.period.from) + ' – ' + fmtDay(data.period.to));
    bars(p1, data.series, ['registrations', 'trials'], { names: ['New accounts', 'Trials'], label: 'New accounts and trials per day', empty: 'No new accounts or trials in this period.' });
    dailyTable(p1, ['registrations', 'trials', 'activations'], ['New accounts', 'Trials', 'Activations']);
    var p2 = panel(gr, 4, 'Live revenue per day', rv.other.length ? 'GBP shown; other currencies in Customers' : null);
    bars(p2, data.series, ['revenue_cents'], { money: true, label: 'Live revenue per day', empty: 'No live payments in this period.' });
    var p3 = panel(gr, 6, 'Anonymous active days', 'Days on which an install was used, from anonymous totals',
      'Each install counts once per day it is used. With no identifier, this cannot show how many different people used Kapture.');
    bars(p3, data.series, ['anonymous_active'], { label: 'Anonymous active days per day',
      empty: data.switches.aggregate ? 'Waiting for anonymous totals. Apps send them within about a day of being opened.' : 'Anonymous statistics are switched off.' });
    var p4 = panel(gr, 6, 'Licences issued', 'Per day', 'Successful licence checks from the apps. These are events, not devices.');
    bars(p4, data.series, ['licence_issued'], { label: 'Licences issued per day', empty: 'No licences issued in this period.' });
  }

  function viewCustomers(v) {
    var c = data.customers;
    var sc = scope(['accounts', 'trials', 'subscriptions', 'payments']);
    if (sc) v.appendChild(el('p', 'kd-scope', sc + '.'));
    var g = kpis(v);
    kpi(g, 'Accounts', int(c.accounts_total), int(c.confirmed_total) + ' confirmed', 'All Kapture accounts in the selected class. Unmarked accounts have no test or internal marker; that does not prove they are customers.');
    kpi(g, 'New accounts', int(data.kpi.new_accounts.cur), delta(data.kpi.new_accounts.cur, data.kpi.new_accounts.prev));
    kpi(g, 'Trials active', int(c.trials_active), int(c.trials_started) + ' started · ' + int(c.trials_ended) + ' ended in period');
    var conv = c.conversion;
    kpi(g, 'Trial conversion', conv.eligible >= 5 ? Math.round(100 * conv.converted / conv.eligible) + '%' : int(conv.converted) + ' of ' + int(conv.eligible),
      conv.eligible ? 'trials started 21+ days ago' : 'no trial is 21 days old yet',
      'Trials that became a live subscription within 21 days of starting, for trials started at least 21 days ago. A percentage is shown from 5 eligible trials.');
    kpi(g, 'New subscriptions', int(c.subscriptions_new), int(c.subscriptions_cancelled) + ' cancelled in period');
    kpi(g, 'Set to cancel', int(c.subscriptions_set_to_cancel), c.subscriptions_test_mode ? int(c.subscriptions_test_mode) + ' test-mode active (excluded)' : 'live subscriptions');

    var gr = grid(v);
    var p1 = panel(gr, 6, 'Live subscriptions', 'By plan and status', 'Live Stripe subscriptions only. Use the Plan filter to narrow it.');
    hbars(p1, c.subscriptions.map(function (r) { return { label: cap(r.plan) + ' · ' + words(r.status), value: r.n, display: int(r.n) }; }), 'No live subscriptions for these filters.');
    var p2 = panel(gr, 6, 'Payments', 'Completed Stripe payments by mode and account class',
      'Live payments are real money; test-mode payments come from Stripe test mode. Internal payments come from the owner or internal accounts.');
    var pays = c.payments;
    if (!pays.length) empty(p2, 'No completed payments for these filters.');
    else {
      hbars(p2, pays.map(function (r) { return { label: cap(r.mode) + ' · ' + r['class'], value: n(r.cents_all), display: money(r.cents_all, r.currency) + ' all time' }; }), '');
      table(p2, [{ t: 'Mode' }, { t: 'Class' }, { t: 'In period', n: 1 }, { t: 'Payments', n: 1 }, { t: 'All time', n: 1 }, { t: 'Payments', n: 1 }],
        pays.map(function (r) { return [r.mode, r['class'], money(r.cents_period, r.currency), int(r.count_period), money(r.cents_all, r.currency), int(r.count_all)]; }));
    }
    if (c.failed_payments) p2.appendChild(el('p', 'kd-panel-sub', int(c.failed_payments) + ' failed live payment(s) in the period'));

    var p3 = panel(gr, 8, 'New accounts per day', null);
    bars(p3, data.series, ['registrations'], { label: 'New accounts per day', empty: 'No new accounts in this period.' });
    var p4 = panel(gr, 4, 'Trials started by platform', 'In the period');
    hbars(p4, Object.keys(c.trials_by_platform).map(function (k) { return { label: plat(k), value: c.trials_by_platform[k], display: int(c.trials_by_platform[k]) }; }), 'No trials started in this period.');

    var p5 = panel(gr, 12, 'Account classes', 'Always shows all three classes, whatever the filter',
      'Classes come from existing records only: test = billing test allowlist, internal = owner or internal access grant, unmarked = neither (not verified as a customer).');
    table(p5, [{ t: 'Class' }, { t: 'Accounts', n: 1 }, { t: 'Active trials', n: 1 }, { t: 'Live subscriptions', n: 1 }, { t: 'Live revenue', n: 1 }, { t: 'Active seats', n: 1 }],
      c.segments.map(function (s) { return [cap(s['class']), int(s.accounts), int(s.trials_active), int(s.subscriptions_live), money(s.revenue_live_cents), int(s.devices_active)]; }), 'Show by class');
    hbars(p5, c.segments.map(function (s) { return { label: cap(s['class']), value: s.accounts, display: int(s.accounts) + ' accounts · ' + money(s.revenue_live_cents) + ' live' }; }), '');
  }

  function viewDevices(v) {
    var d = data.devices;
    var sc = scope(['devices', 'licence_checks']);
    if (sc) v.appendChild(el('p', 'kd-scope', sc + '.'));
    if (data.filters.platform === 'chrome') v.appendChild(el('p', 'kd-scope', 'Kapture for Chrome has no licence or licensed devices; these figures are for Kapture Pro on macOS and Windows.'));
    var sum = function (o) { return Object.keys(o).reduce(function (s, k) { return s + n(o[k]); }, 0); };
    var by = function (o) { return Object.keys(o).sort().map(function (k) { return plat(k) + ' ' + int(o[k]); }).join(' · ') || 'none'; };
    var g = kpis(v);
    kpi(g, 'Active seats', int(sum(d.active_seats)), by(d.active_seats), 'Activated and not deactivated. Seats are licensed computers, not people.');
    kpi(g, 'Seen in period', int(sum(d.seen_in_period)), by(d.seen_in_period), 'Active seats that checked their licence in the period.');
    kpi(g, 'Activations', int(data.kpi.activations.cur), delta(data.kpi.activations.cur, data.kpi.activations.prev), 'Activation events; one computer can activate more than once.');
    kpi(g, 'Deactivations', int(d.deactivations_in_period), 'in the period');
    kpi(g, 'Licence checks', int(data.kpi.licence_checks.cur), delta(data.kpi.licence_checks.cur, data.kpi.licence_checks.prev), 'Licence requests from the apps (events).');

    var gr = grid(v);
    var p1 = panel(gr, 8, 'Activations per day', 'macOS and Windows');
    bars(p1, data.series, ['activations_macos', 'activations_windows'], { names: ['macOS', 'Windows'], label: 'Activations per day by platform', empty: 'No activations in this period.' });
    dailyTable(p1, ['activations_macos', 'activations_windows'], ['macOS', 'Windows']);
    var p2 = panel(gr, 4, 'Platforms', 'Active seats');
    hbars(p2, Object.keys(d.active_seats).map(function (k) { return { label: plat(k), value: d.active_seats[k], display: int(d.active_seats[k]) }; }), 'No active seats.');
    var p3 = panel(gr, 6, 'App versions', 'Devices seen in the period, by the version they last reported');
    hbars(p3, d.versions.map(function (r) { return { label: plat(r.platform) + ' ' + r.version, value: r.devices, display: int(r.devices) }; }), 'No devices seen in this period.');
    var p4 = panel(gr, 6, 'Licence check outcomes', 'In the period', '"Unknown" means the request did not say which platform it came from.');
    hbars(p4, d.licence_outcomes.map(function (r) { return { label: plat(r.platform) + ' · ' + words(r.outcome), value: r.checks, display: int(r.checks) }; }), 'No licence checks in this period.');
    var p5 = panel(gr, 12, 'Licence checks per day', 'Licences issued per day');
    bars(p5, data.series, ['licence_issued'], { label: 'Licences issued per day', empty: 'No licences issued in this period.' });
    dailyTable(p5, ['licence_issued', 'licence_checks'], ['Issued', 'All checks']);
  }

  function viewUsage(v) {
    var u = data.usage;
    var sc = scope(['anonymous', 'opt_in']);
    if (sc) v.appendChild(el('p', 'kd-scope', sc + ': anonymous and opted-in statistics are not linked to accounts.'));
    var g = kpis(v);
    var act = u.activity;
    var pick = function (key) { return act.length ? act.map(function (r) { return plat(r.platform) + ' ' + r[key]; }).join(' · ') : '—'; };
    kpi(g, 'DAU', act.length === 1 ? act[0].dau : pick('dau'), 'yesterday (UTC)', 'Anonymous: installs active yesterday. Without an identifier this counts installs, not people.');
    kpi(g, 'WAU', act.length === 1 ? act[0].wau : pick('wau'), 'last full week', 'Anonymous: installs active in the last full ISO week (Monday–Sunday), each counted once.');
    kpi(g, 'MAU', act.length === 1 ? act[0].mau : pick('mau'), 'last full month', 'Anonymous: installs active in the last full calendar month, each counted once.');
    kpi(g, 'First launches', u.first_launches, 'in the period', 'Anonymous: installs opened for the first time.');
    var oi = u.optin_installs;
    kpi(g, 'Opted-in installs', oi.length ? oi.map(function (r) { return plat(r.platform) + ' ' + r.mau; }).join(' · ') : '0', 'active in 30 days',
      'Installs that chose “Share statistics”. These carry a random ID, so they can be counted over time.');

    var gr = grid(v);
    var p1 = panel(gr, 6, 'Anonymous active days', 'Per day', 'Each install counts once per day it is used.');
    bars(p1, data.series, ['anonymous_active'], { label: 'Anonymous active days per day',
      empty: data.switches.aggregate ? 'Waiting for anonymous totals. Apps send them within about a day of being opened.' : 'Anonymous statistics are switched off.' });
    var p2 = panel(gr, 6, 'Opted-in active installs', 'Per day', 'Distinct opted-in installs active each day.');
    bars(p2, data.series, ['optin_active'], { label: 'Opted-in active installs per day',
      empty: data.switches.usage ? 'No opted-in installs yet. They appear once users choose “Share statistics”.' : 'Opt-in statistics are switched off.' });
    var p3 = panel(gr, 8, 'Most used features', 'Anonymous totals in the period, top 20', 'Counts of actions (events), not people. Figures from 1 to 4 show as <5.');
    hbars(p3, u.features.map(function (r) { return { label: words(r.event) + ' · ' + plat(r.platform), value: r.total, display: r.total }; }),
      data.switches.aggregate ? 'No feature totals in this period yet.' : 'Anonymous statistics are switched off.');
    var p4 = panel(gr, 4, 'Feature adoption', 'Opted-in installs, last full week', 'Share of active opted-in installs that used each feature. Shown from 5 active installs.');
    hbars(p4, u.adoption.map(function (r) { return { label: words(r.event) + ' · ' + plat(r.platform), value: r.percent, display: r.percent + '% of ' + r.of }; }),
      'Shown once at least 5 opted-in installs are active in a week.');
    var p5 = panel(gr, 6, 'Retention', 'Opted-in weekly cohorts', 'Share of each weekly cohort of new opted-in installs active N weeks later. Shown for cohorts of 5 or more.');
    if (!u.retention.length) empty(p5, 'Shown once a weekly cohort has at least 5 opted-in installs.');
    else {
      hbars(p5, u.retention.map(function (r) { return { label: 'Week of ' + fmtDay(r.cohort_week) + ' · week ' + r.week, value: n(r.percent), display: r.percent + '% of ' + r.size }; }), '');
    }
    var p6 = panel(gr, 6, 'Versions, systems and languages', 'Anonymous active days in the period');
    hbars(p6, u.environments.slice(0, 12).map(function (r) { return { label: plat(r.platform) + ' ' + r.version + ' · ' + words(r.os) + ' · ' + r.locale, value: r.active_days, display: r.active_days }; }),
      'No anonymous activity in this period yet.');
  }

  function viewHealth(v) {
    var h = data.health, i = h.ingest;
    v.appendChild(el('p', 'kd-scope', 'System figures are not affected by the platform, class or plan filters.'));
    var g = kpis(v);
    kpi(g, 'Anonymous collection', data.switches.aggregate ? 'On' : 'Off', 'switch aggregate');
    kpi(g, 'Opt-in collection', data.switches.usage ? 'On' : 'Off', 'switch usage');
    kpi(g, 'Requests', int(i.requests), int(h.ingest_today.requests) + ' today', 'Statistics requests that reached the database in the period.');
    kpi(g, 'Batches accepted', int(n(i.batches_aggregate) + n(i.batches_usage)), int(i.batches_aggregate) + ' anonymous · ' + int(i.batches_usage) + ' opt-in');
    kpi(g, 'Rate-limited', int(i.limited), int(h.ingest_today.limited) + ' today', 'Requests refused because a daily limit was reached.');
    kpi(g, 'Licence errors', int(h.licence_errors), 'unavailable or error outcomes');

    var gr = grid(v);
    var p1 = panel(gr, 8, 'Collection per day', 'Accepted batches per day');
    var ser = h.ingest_series.map(function (p) { return { day: p.day, accepted: n(p.batches_aggregate) + n(p.batches_usage) }; });
    bars(p1, ser, ['accepted'], { label: 'Accepted batches per day', empty: 'No statistics batches in this period.' });
    table(p1, [{ t: 'Day' }, { t: 'Requests', n: 1 }, { t: 'Anonymous', n: 1 }, { t: 'Opt-in', n: 1 }, { t: 'Duplicates', n: 1 }, { t: 'Limited', n: 1 }],
      h.ingest_series.filter(function (p) { return n(p.requests); }).reverse().map(function (p) { return [fmtDay(p.day, { year: 'numeric' }), int(p.requests), int(p.batches_aggregate), int(p.batches_usage), int(p.duplicates), int(p.limited)]; }),
      'Show daily figures');
    var p2 = panel(gr, 4, 'Rejections', null, 'Invalid requests (unknown events, free text, oversized bodies, credentials) are refused by the endpoint before the database and are only logged.');
    stats(p2, [['Rejected requests', 'Not recorded'], ['Duplicates', int(i.duplicates)], ['New installs', int(i.new_installs)], ['Forget requests', int(i.forgets)], ['Entries stored', int(i.entries)]]);

    var p3 = panel(gr, 6, 'Scheduled jobs', 'Most recent run');
    if (!h.jobs) empty(p3, 'Job status is unavailable.');
    else if (!h.jobs.length) empty(p3, 'No scheduled jobs.');
    else stats(p3, h.jobs.map(function (j) {
      return [j.name + ' · ' + j.schedule + (j.active ? '' : ' (paused)'),
              j.last_status ? cap(j.last_status) + ', ' + new Date(j.last_start).toLocaleString('en-GB', { dateStyle: 'short', timeStyle: 'short' }) : 'Not run yet'];
    }));
    var p4 = panel(gr, 6, 'Limits and freshness');
    var fr = h.freshness, lim = h.limits;
    var day = function (s) { return s ? fmtDay(String(s).slice(0, 10), { year: 'numeric' }) : 'none yet'; };
    stats(p4, [['Last statistics request', day(fr.last_ingest_day)], ['Last anonymous data', day(fr.last_anonymous_day)], ['Last opt-in data', day(fr.last_optin_day)],
      ['Last licence check', day(fr.last_licence_check_day)], ['Last device contact', day(fr.last_device_contact)],
      ['Requests per day', int(lim.requests_per_day)], ['Entries per day', int(lim.entries_per_day)], ['New installs per day', int(lim.new_installs_per_day)],
      ['Batches per install per day', int(lim.batches_per_install_day)]]);
  }

  var RENDER = { overview: viewOverview, customers: viewCustomers, devices: viewDevices, usage: viewUsage, health: viewHealth };

  function currentView() { var h = location.hash.replace('#', ''); return VIEWS.indexOf(h) >= 0 ? h : 'overview'; }

  function render() {
    if (!data) return;
    var view = currentView();
    main.setAttribute('data-view', view);
    document.querySelectorAll('#kdTabs a').forEach(function (a) {
      if (a.getAttribute('data-view') === view) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    while (body.firstChild) body.removeChild(body.firstChild);
    var v = el('div', 'kd-view');
    body.appendChild(v);   // attached first, so charts can measure their width
    RENDER[view](v);

    meta.textContent = fmtDay(data.period.from, { year: 'numeric' }) + ' – ' + fmtDay(data.period.to, { year: 'numeric' }) +
      ' · compared with the previous ' + data.period.days + ' days · updated ' +
      new Date(data.generated_at).toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' });
    while (chips.firstChild) chips.removeChild(chips.firstChild);
    [['Anonymous', data.switches.aggregate], ['Opt-in', data.switches.usage]].forEach(function (c) {
      chips.appendChild(el('span', 'kd-chip' + (c[1] ? ' is-on' : ''), c[0] + ' ' + (c[1] ? 'on' : 'off')));
    });
  }

  /* ---- controls ---------------------------------------------------------- */

  function syncForm() {
    form.period.value = prefs.period; form.platform.value = prefs.platform; form['class'].value = prefs.klass; form.plan.value = prefs.plan;
    var r = range(); form.from.value = prefs.from || r.from; form.to.value = prefs.to || r.to;
    var max = iso(utcToday()); form.from.max = max; form.to.max = max;
    form.classList.toggle('is-custom', prefs.period === 'custom');
  }
  form.addEventListener('change', function (e) {
    var t = e.target;
    if (t.name === 'period') {
      prefs.period = t.value;
      if (t.value === 'custom') { var r0 = range(); prefs.from = prefs.from || r0.from; prefs.to = prefs.to || r0.to; }
    } else if (t.name === 'from' || t.name === 'to') {
      prefs[t.name] = t.value;
      if (!prefs.from || !prefs.to || prefs.from > prefs.to) { syncForm(); return; }
    } else if (t.name === 'class') prefs.klass = t.value;
    else prefs[t.name] = t.value;
    savePrefs(); syncForm(); load();
  });
  form.addEventListener('submit', function (e) { e.preventDefault(); });
  window.addEventListener('hashchange', render);
  var lastWidth = innerWidth, resizeTimer = 0;
  window.addEventListener('resize', function () {
    if (Math.abs(innerWidth - lastWidth) < 40) return;
    lastWidth = innerWidth; clearTimeout(resizeTimer); resizeTimer = setTimeout(render, 200);
  });

  /* Keep an open tooltip inside the viewport: shift it sideways if needed. */
  function placeTip(e) {
    var t = e.target.closest && e.target.closest('.kd-tip');
    if (!t) return;
    var tb = t.querySelector('.kd-tip-body');
    tb.style.marginLeft = '0px';
    requestAnimationFrame(function () {
      var r = tb.getBoundingClientRect(), pad = 12, shift = 0;
      if (r.right > innerWidth - pad) shift = innerWidth - pad - r.right;
      if (r.left + shift < pad) shift = pad - r.left;
      tb.style.marginLeft = shift + 'px';
    });
  }
  body.addEventListener('mouseover', placeTip);
  body.addEventListener('focusin', placeTip);
  document.getElementById('kdRetry').addEventListener('click', load);

  syncForm();
  load();
}());
