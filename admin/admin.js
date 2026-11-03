/* Private analytics dashboard.
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
  function addDays(s, k) { var d = new Date(s + 'T00:00:00Z'); d.setUTCDate(d.getUTCDate() + k); return iso(d); }
  function range() {
    var today = utcToday();
    if (prefs.period === 'custom' && prefs.from && prefs.to) return { from: prefs.from, to: prefs.to };
    var days = Number(prefs.period) || 30;
    var from = new Date(today); from.setUTCDate(from.getUTCDate() - (days - 1));
    return { from: iso(from), to: iso(today) };
  }
  function fmtDay(s, opts) { return new Date(String(s).slice(0, 10) + 'T00:00:00Z').toLocaleDateString('en-GB', Object.assign({ day: 'numeric', month: 'short', timeZone: 'UTC' }, opts || {})); }
  function fmtLong(s) { return fmtDay(s, { weekday: 'short', year: 'numeric' }); }
  function fmtTime(s) { return new Date(s).toLocaleString('en-GB', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit', timeZone: 'UTC' }) + ' UTC'; }
  function daysAgo(s) { return Math.round((utcToday() - new Date(String(s).slice(0, 10) + 'T00:00:00Z')) / 864e5); }
  function relDay(s) { var k = daysAgo(s); return k === 0 ? 'today' : k === 1 ? 'yesterday' : k + ' days ago (' + fmtDay(s) + ')'; }

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
  /* Phosphor Fill, the only icon weight on this page (assets/icons/phosphor-fill). */
  function icon(name, cls) {
    var i = el('i', 'kd-i ph-fill ph-' + name + (cls ? ' ' + cls : ''));
    i.setAttribute('aria-hidden', 'true');
    return i;
  }
  function add(parent) { for (var i = 1; i < arguments.length; i++) if (arguments[i]) parent.appendChild(typeof arguments[i] === 'string' ? document.createTextNode(arguments[i]) : arguments[i]); return parent; }
  /* Information button: focusable, named, and described by its tooltip text. */
  var tipCount = 0;
  function tip(text) {
    var w = el('span', 'kd-tip'), id = 'kd-tip-' + (++tipCount);
    var b = el('button'); b.type = 'button'; b.setAttribute('aria-label', 'More information'); b.setAttribute('aria-describedby', id);
    b.appendChild(icon('info'));
    var body = el('span', 'kd-tip-body', text); body.id = id; body.setAttribute('role', 'tooltip');
    w.appendChild(b); w.appendChild(body);
    return w;
  }
  function n(v) { var x = Number(v); return isFinite(x) ? x : 0; }
  function int(v) { return isSupp(v) ? 'fewer than 5' : n(v).toLocaleString('en-GB'); }
  function short(v) { return isSupp(v) ? '<5' : n(v).toLocaleString('en-GB'); }
  function isSupp(v) { return v === '<5'; }
  function money(cents, cur) {
    try { return new Intl.NumberFormat('en-GB', { style: 'currency', currency: cur || 'GBP' }).format(n(cents) / 100); }
    catch (e) { return (n(cents) / 100).toFixed(2) + ' ' + cur; }
  }
  function plural(k, one, many) { return n(k) === 1 ? one : (many || one + 's'); }
  var PLATFORM = { macos: 'macOS', windows: 'Windows', chrome: 'Chrome', other: 'Unknown', unknown: 'Unknown' };
  var PLATFORM_ICON = { macos: 'apple-logo', windows: 'windows-logo', chrome: 'google-chrome-logo' };
  function plat(k) { return PLATFORM[k] || k; }
  function cap(s) { s = String(s); return s.charAt(0).toUpperCase() + s.slice(1); }
  function words(s) { return cap(String(s).replace(/[_-]+/g, ' ')); }

  /* Sum values that may include "<5". A hidden small count is at least 1, so
     the result is a floor, shown as "7+" rather than a made-up exact number. */
  function sumVals(vals) {
    var total = 0, hidden = 0;
    vals.forEach(function (v) { if (isSupp(v)) hidden++; else total += n(v); });
    if (!hidden) return { value: total, text: total.toLocaleString('en-GB'), exact: true };
    if (!total && hidden === 1) return { value: 2, text: '<5', exact: false };
    return { value: total + hidden, text: (total + hidden).toLocaleString('en-GB') + '+', exact: false };
  }

  /* Account types, in plain words. Classes come from existing records only. */
  var CLASS = {
    internal: { name: 'Internal', icon: 'buildings', about: "Kapture's own accounts: the owner account and accounts given internal access." },
    test: { name: 'Test', icon: 'flask', about: 'Accounts explicitly marked for billing tests.' },
    unmarked: { name: 'Unmarked', icon: 'question', about: 'Neither internal nor test. Not proof of a real customer.' }
  };

  /* A filter that does not apply to a group of metrics is named, so an
     unfiltered figure is never presented as filtered. */
  function scope(groups) {
    var notes = [];
    var f = data.filters, ap = data.applies;
    if (f.platform !== 'all' && groups.some(function (g) { return ap.platform.indexOf(g) < 0; })) notes.push('platform');
    if (f['class'] !== 'all' && groups.some(function (g) { return ap['class'].indexOf(g) < 0; })) notes.push('account type');
    if (f.plan !== 'all' && groups.some(function (g) { return ap.plan.indexOf(g) < 0; })) notes.push('plan');
    return notes.length ? 'not filtered by ' + notes.join(' or ') : '';
  }

  /* ---- components ------------------------------------------------------- */

  function periodLabel() { return data.period.days + ' days'; }

  function notice(parent, iconName, parts, cls) {
    var d = el('div', 'kd-notice' + (cls ? ' ' + cls : ''));
    d.appendChild(icon(iconName));
    var t = el('div'); parts.forEach(function (p) { if (p) t.appendChild(typeof p === 'string' ? document.createTextNode(p) : p); });
    d.appendChild(t); parent.appendChild(d); return d;
  }

  /* Comparison with the previous equal period. A percentage needs a base of
     at least 5; below that the previous figure is stated as it is. */
  function delta(cur, prev, fmt) {
    cur = n(cur); prev = n(prev); fmt = fmt || function (x) { return x.toLocaleString('en-GB'); };
    var d = cur - prev, s = el('span', 'kd-delta'), text;
    if (!cur && !prev) { text = 'None in the previous ' + periodLabel() + ' either'; }
    else if (!prev) { text = 'None in the previous ' + periodLabel(); }
    else if (prev >= 5) { var pct = Math.round(100 * d / prev); text = (pct ? Math.abs(pct) + '% ' + (pct > 0 ? 'more' : 'less') : 'Same') + ' than the previous ' + periodLabel(); if (!pct) text = 'Same as the previous ' + periodLabel(); }
    else { text = fmt(prev) + ' in the previous ' + periodLabel(); }
    if (cur && d > 0) { s.className += ' is-up'; s.appendChild(icon('arrow-up')); }
    else if (d < 0) { s.className += ' is-down'; s.appendChild(icon('arrow-down')); }
    else s.appendChild(icon('minus'));
    s.appendChild(document.createTextNode(text));
    return s;
  }

  function kpi(parent, o) {
    var c = el('div', 'kd-kpi kd-tone-' + (o.tone || 'quiet'));
    var top = el('div', 'kd-kpi-top');
    var b = el('span', 'kd-badge'); b.appendChild(icon(o.icon)); top.appendChild(b);
    var l = el('div', 'kd-kpi-label'); l.appendChild(el('span', 'kd-kpi-title', o.label));
    if (o.help) l.appendChild(tip(o.help));
    top.appendChild(l); c.appendChild(top);
    var v = el('div', 'kd-kpi-value', o.value);
    if (o.text || !/^[£$€−+<]?[\d.,%<+]+$/.test(String(o.value))) v.className += ' is-text';
    c.appendChild(v);
    if (o.sub) { var s = el('div', 'kd-kpi-sub'); if (typeof o.sub === 'string') s.textContent = o.sub; else s.appendChild(o.sub); c.appendChild(s); }
    var uf = unfiltered(o.group); if (uf) { var ufw = el('div', 'kd-kpi-sub'); ufw.appendChild(uf); c.appendChild(ufw); }
    if (o.delta) { var f = el('div', 'kd-kpi-foot'); f.appendChild(o.delta); c.appendChild(f); }
    parent.appendChild(c);
    parent.setAttribute('data-n', Math.min(4, parent.children.length));
    return c;
  }
  /* A row of KPI cards. Featured rows hold the screen's headline figures;
     the column count follows the number of cards (see data-n in the CSS). */
  function kpis(parent, featured) { var g = el('div', 'kd-kpis' + (featured ? ' is-hero' : '')); parent.appendChild(g); return g; }

  function block(parent, title, iconName, help) {
    var b = el('section', 'kd-block');
    if (title) {
      var h = el('h2', 'kd-section-head');
      if (iconName) h.appendChild(icon(iconName));
      h.appendChild(document.createTextNode(title));
      if (help) h.appendChild(tip(help));
      b.appendChild(h);
    }
    parent.appendChild(b);
    return b;
  }

  function panel(grid, span, title, o) {
    o = o || {};
    var p = el('section', 'kd-panel kd-span-' + span + (o.cls ? ' ' + o.cls : ''));
    var head = el('div', 'kd-panel-head');
    var h = el('h3');
    if (o.icon) h.appendChild(icon(o.icon));
    h.appendChild(document.createTextNode(title));
    if (o.help) h.appendChild(tip(o.help));
    head.appendChild(h);
    var uf = unfiltered(o.group); if (uf) head.appendChild(uf);
    p.appendChild(head);
    p.head = head;
    if (o.sub) p.appendChild(el('p', 'kd-panel-sub', o.sub));
    grid.appendChild(p);
    return p;
  }
  function grid(parent) { var g = el('div', 'kd-grid'); parent.appendChild(g); return g; }

  /* Compact empty state: an icon, what is missing and why, in one or two lines. */
  function empty(parent, iconName, title, why) {
    var d = el('div', 'kd-empty');
    d.appendChild(icon(iconName || 'circle-dashed'));
    var t = el('div'); t.appendChild(el('strong', null, title)); if (why) t.appendChild(document.createTextNode(why));
    d.appendChild(t); parent.appendChild(d);
  }

  /* Segmented control that redraws one panel's chart. */
  function switcher(p, options, draw) {
    var holder = el('div');
    var seg = el('div', 'kd-seg'); seg.setAttribute('role', 'group'); seg.setAttribute('aria-label', 'Choose what the chart shows');
    var btns = options.map(function (o, i) {
      var b = el('button', null, o.label); b.type = 'button'; b.setAttribute('aria-pressed', i ? 'false' : 'true');
      b.addEventListener('click', function () {
        btns.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        while (holder.firstChild) holder.removeChild(holder.firstChild);
        draw(holder, o);
      });
      seg.appendChild(b); return b;
    });
    p.head.appendChild(seg);
    p.appendChild(holder);
    draw(holder, options[0]);
  }

  /* ---- charts ------------------------------------------------------------- */

  var hover = el('div', 'kd-hover'); hover.setAttribute('aria-hidden', 'true'); document.body.appendChild(hover);
  function showHover(x, y, day, rows) {
    while (hover.firstChild) hover.removeChild(hover.firstChild);
    hover.appendChild(el('div', 'kd-hover-day', fmtLong(day) + (day === iso(utcToday()) ? ' · today, so far' : '')));
    rows.forEach(function (r) {
      var row = el('div', 'kd-hover-row'); var a = el('span', r.sw, r.name); row.appendChild(a); row.appendChild(el('span', null, r.value)); hover.appendChild(row);
    });
    hover.classList.add('is-on');
    var w = hover.offsetWidth, h = hover.offsetHeight;
    var left = Math.min(innerWidth - w - 12, Math.max(12, x + 14)), top = y - h - 14;
    if (top < 8) top = y + 18;
    hover.style.left = left + 'px'; hover.style.top = top + 'px';
  }
  function hideHover() { hover.classList.remove('is-on'); }

  /* Daily bars, stacked. defs: [{ key, name, c }] where c is the colour slot
     1–5. Values may be "<5": those draw as a dashed outline so the day is
     visibly non-zero without a made-up height. */
  function bars(parent, series, defs, o) {
    o = o || {};
    var anySupp = false;
    var totals = series.map(function (p) { return defs.reduce(function (s, d) { if (isSupp(p[d.key])) { anySupp = true; return s + 2; } return s + n(p[d.key]); }, 0); });
    var max = Math.max.apply(null, totals.concat([0]));
    if (!max) { empty(parent, o.emptyIcon, o.empty || 'Nothing recorded in this period.', o.emptyWhy); return false; }
    var c = el('div', 'kd-chart'); parent.appendChild(c);   // measured before drawing
    var W = Math.max(280, Math.round(c.clientWidth) || 640), H = o.height || 170;
    var pad = { l: o.money ? 40 : 30, r: 2, b: 22, t: 8 }, iw = W - pad.l - pad.r, ih = H - pad.b - pad.t;
    var bw = iw / series.length, gap = Math.min(5, bw * 0.28), top = niceMax(max, o.money);
    var s = svg('svg', { viewBox: '0 0 ' + W + ' ' + H, role: 'img', 'aria-label': o.label || 'Daily chart' });
    [0, 0.5, 1].forEach(function (f) {
      var y = pad.t + ih - f * ih;
      s.appendChild(svg('line', { x1: pad.l, x2: W - pad.r, y1: y, y2: y, 'class': 'kd-grid-line' }));
      var v = top * f; if (f === 0.5 && (o.money ? v % 100 : v % 1)) return;
      var t = svg('text', { x: pad.l - 7, y: y + 4, 'text-anchor': 'end', 'class': 'kd-axis' }); t.textContent = fmtAxis(v, o.money); s.appendChild(t);
    });
    var today = iso(utcToday());
    series.forEach(function (p, i) {
      var x = pad.l + i * bw, y0 = pad.t + ih;
      var hit = svg('rect', { x: x, y: pad.t, width: bw, height: ih, 'class': 'kd-hit' });
      s.appendChild(hit);
      defs.forEach(function (d) {
        var v = p[d.key], h = isSupp(v) ? Math.max(3, ih * (2 / top)) : ih * (n(v) / top);
        if (!h) return;
        s.appendChild(svg('rect', { x: x + gap / 2, y: y0 - h, width: Math.max(1.5, bw - gap), height: h, rx: Math.min(3, bw / 4),
                                    'class': 'kd-bar ' + (isSupp(v) ? 'is-supp' : 'kd-c' + d.c), 'pointer-events': 'none' }));
        y0 -= h;
      });
      var rows = defs.map(function (d) { return { name: d.name, sw: 'kd-sw-' + d.c, value: isSupp(p[d.key]) ? 'fewer than 5' : o.money ? money(p[d.key]) : int(p[d.key]) }; });
      var t = svg('title'); t.textContent = fmtLong(p.day) + ': ' + rows.map(function (r) { return r.name + ' ' + r.value; }).join(', '); hit.appendChild(t);
      hit.addEventListener('pointerenter', function () { hit.classList.add('is-on'); });
      hit.addEventListener('pointerleave', function () { hit.classList.remove('is-on'); hideHover(); });
      hit.addEventListener('pointermove', function (e) { showHover(e.clientX, e.clientY, p.day, rows); });
      if (p.day === today && series.length > 1) {
        s.appendChild(svg('line', { x1: x, x2: x, y1: pad.t, y2: pad.t + ih, 'class': 'kd-today-line', 'pointer-events': 'none' }));
      }
    });
    // Date labels: at most six (fewer on narrow charts), counted back from the last day so it is always labelled.
    var step = Math.max(1, Math.ceil(series.length / Math.max(2, Math.min(6, Math.floor(iw / 72)))));
    series.forEach(function (p, i) {
      if ((series.length - 1 - i) % step) return;
      var cx = pad.l + i * bw + bw / 2, anchor = cx < pad.l + 24 ? 'start' : cx > W - 24 ? 'end' : 'middle';
      var t = svg('text', { x: anchor === 'start' ? pad.l : anchor === 'end' ? W - pad.r : cx, y: H - 5, 'text-anchor': anchor, 'class': 'kd-axis' });
      t.textContent = p.day === today ? 'Today' : fmtDay(p.day); s.appendChild(t);
    });
    c.appendChild(s);
    if (defs.length > 1 || anySupp) {
      var lg = el('div', 'kd-legend');
      if (defs.length > 1) defs.forEach(function (d) { lg.appendChild(el('span', 'kd-sw-' + d.c, d.name)); });
      if (anySupp) lg.appendChild(el('span', 'is-supp', 'Fewer than 5 (exact figure hidden for privacy)'));
      parent.appendChild(lg);
    }
    return true;
  }
  function niceMax(v, isMoney) {
    if (isMoney) { var pounds = niceMax(v / 100); return pounds * 100; }
    if (v <= 4) return 4;
    var p = Math.pow(10, Math.floor(Math.log10(v))), m = v / p;
    return (m <= 1 ? 1 : m <= 2 ? 2 : m <= 5 ? 5 : 10) * p;
  }
  function fmtAxis(v, isMoney) { return isMoney ? '£' + Math.round(v / 100).toLocaleString('en-GB') : Math.round(v).toLocaleString('en-GB'); }

  /* Money per day. With only a few payment days a bar chart is mostly
     empty and suggests a trend that is not there, so those days are listed. */
  function moneyDays(parent, series, key, label) {
    var paid = series.filter(function (p) { return n(p[key]) > 0; });
    if (!paid.length) { empty(parent, 'receipt', 'No payments in this period.', ' Payments appear here on the day they are received.'); return; }
    if (paid.length <= 4 || paid.length < series.length / 5) {
      var ul = el('ul', 'kd-days');
      paid.slice().reverse().forEach(function (p) { var li = el('li'); li.appendChild(el('b', null, money(p[key]))); li.appendChild(el('small', null, fmtDay(p.day, { weekday: 'short' }))); ul.appendChild(li); });
      parent.appendChild(ul);
      parent.appendChild(el('p', 'kd-panel-sub', 'Payments on ' + paid.length + ' of ' + series.length + ' days. Most days had no transactions, so there is no daily trend to read yet.'));
      return;
    }
    bars(parent, series, [{ key: key, name: label || 'Received', c: 3 }], { money: true, label: (label || 'Revenue') + ' per day' });
  }

  /* Ranked horizontal bars for categories. rows: { label, value, display, icon, fill, tags } */
  function hbars(parent, rows, emptyArgs, o) {
    o = o || {};
    if (!rows.length) { empty.apply(null, [parent].concat(emptyArgs)); return; }
    var max = Math.max.apply(null, rows.map(function (r) { return isSupp(r.value) ? 4 : n(r.value); })) || 1;
    var ul = el('ul', 'kd-hbars');
    rows.forEach(function (r) {
      var li = el('li');
      var lab = el('span', 'kd-hb-label'); if (r.icon) lab.appendChild(icon(r.icon)); lab.appendChild(el('span', null, r.label));
      if (r.tags) r.tags.forEach(function (t) { lab.appendChild(t); });
      li.appendChild(lab);
      li.appendChild(el('span', 'kd-hb-value', r.display !== undefined ? r.display : short(r.value)));
      if (!o.noBars) {
        var tr = el('span', 'kd-hb-track'), f = el('span', 'kd-hb-fill ' + (isSupp(r.value) ? 'is-supp' : r.fill || ''));
        f.style.width = Math.max(2, Math.round(100 * (isSupp(r.value) ? 2 : n(r.value)) / max)) + '%';
        tr.appendChild(f); li.appendChild(tr);
      }
      ul.appendChild(li);
    });
    parent.appendChild(ul);
  }
  function tag(text, cls, iconName) { var t = el('span', 'kd-tag' + (cls ? ' ' + cls : '')); if (iconName) t.appendChild(icon(iconName)); t.appendChild(document.createTextNode(text)); return t; }

  function stats(parent, items) {
    var dl = el('dl', 'kd-stats');
    items.forEach(function (it) {
      var d = el('div'), dt = el('dt', null, it[0]);
      if (it[2]) dt.appendChild(tip(it[2]));
      var dd = el('dd', null, it[1]); if (it[3]) dd.appendChild(el('small', null, it[3]));
      d.appendChild(dt); d.appendChild(dd); dl.appendChild(d);
    });
    parent.appendChild(dl);
    return dl;
  }

  function details(parent, summary, cls) { var d = el('details', 'kd-details' + (cls ? ' ' + cls : '')); d.appendChild(el('summary', null, summary)); parent.appendChild(d); return d; }
  function table(parent, heads, rows) {
    var wrap = el('div', 'kd-scroll'), t = el('table', 'kd-table'), tr = el('tr');
    heads.forEach(function (h) { tr.appendChild(el('th', h.n ? 'n' : null, h.t)); });
    var th = el('thead'); th.appendChild(tr); t.appendChild(th);
    var tb = el('tbody');
    rows.forEach(function (r) { var row = el('tr'); r.forEach(function (v, i) { var td = el('td', heads[i].n ? 'n' : null); if (v && v.nodeType) td.appendChild(v); else td.textContent = v; row.appendChild(td); }); tb.appendChild(row); });
    t.appendChild(tb); wrap.appendChild(t); parent.appendChild(wrap);
  }
  function dailyTable(parent, keys, names, isMoney, summary) {
    var rows = data.series.filter(function (p) { return keys.some(function (k) { return isSupp(p[k]) || n(p[k]); }); }).reverse();
    if (!rows.length) return;
    table(details(parent, summary || 'Daily figures'), [{ t: 'Day' }].concat(names.map(function (x) { return { t: x, n: 1 }; })),
      rows.map(function (p) { return [fmtLong(p.day)].concat(keys.map(function (k) { return isSupp(p[k]) ? '<5' : isMoney && isMoney[k] ? money(p[k]) : int(p[k]); })); }));
  }

  /* Today / yesterday / last 7 days from the daily series. Only shown when the
     selected period ends today, since that is the only time those days are in it. */
  function recentWindow(series) {
    var s = series || data.series, today = iso(utcToday());
    if (!s.length || s[s.length - 1].day !== today) return null;
    return { today: s[s.length - 1], yesterday: s.length > 1 ? s[s.length - 2] : null, week: s.length >= 7 ? s.slice(-7) : null };
  }
  function recentTable(parent, rows, series) {
    var w = recentWindow(series);
    if (!w) {
      empty(parent, 'calendar-blank', 'Today and yesterday are outside this period.', ' Choose a period that ends today to compare them.');
      return;
    }
    var t = el('table', 'kd-recent'), hr = el('tr');
    var head = function (title, sub, cls) { var th = el('th', cls, title); th.scope = 'col'; th.appendChild(el('small', null, sub)); return th; };
    var blank = el('th'); blank.scope = 'col'; blank.appendChild(el('span', 'kd-sr', 'Measure'));
    hr.appendChild(blank);
    hr.appendChild(head('Today', fmtDay(w.today.day) + ', so far', 'is-today'));
    if (w.yesterday) hr.appendChild(head('Yesterday', fmtDay(w.yesterday.day)));
    if (w.week) hr.appendChild(head('Last 7 days', fmtDay(w.week[0].day) + ' – ' + fmtDay(w.today.day)));
    var th = el('thead'); th.appendChild(hr); t.appendChild(th);
    var tb = el('tbody');
    rows.forEach(function (r) {
      var tr = el('tr'), name = el('th'); name.scope = 'row';
      name.appendChild(icon(r.icon)); name.appendChild(document.createTextNode(r.name)); if (r.help) name.appendChild(tip(r.help));
      var uf = unfiltered(r.group); if (uf) { uf.classList.add('kd-row-tag'); name.appendChild(uf); }
      tr.appendChild(name);
      var cell = function (points, cls) {
        var v = r.sum(points), td = el('td', cls, v.text);
        // Apps report a day late, so an empty today is "not reported yet", not zero.
        if (r.late && cls === 'is-today' && !v.value) { td.textContent = '—'; td.title = 'Not reported yet'; }
        if (!v.value) td.classList.add('is-zero');
        tr.appendChild(td);
      };
      cell([w.today], 'is-today');
      if (w.yesterday) cell([w.yesterday]);
      if (w.week) cell(w.week);
      tb.appendChild(tr);
    });
    t.appendChild(tb);
    var sc = el('div', 'kd-scroll'); sc.appendChild(t); parent.appendChild(sc);
    parent.appendChild(el('p', 'kd-panel-sub', 'Days run midnight to midnight UTC. Today is still in progress' + (rows.some(function (r) { return r.late; }) ? '; — means not reported yet.' : '.')));
  }
  function sumKey(key, isMoney) {
    return function (points) {
      if (isMoney) { var c = points.reduce(function (s, p) { return s + n(p[key]); }, 0); return { value: c, text: money(c) }; }
      return sumVals(points.map(function (p) { return p[key]; }));
    };
  }

  /* Which account types the figures on this screen include. */
  function classNotice(parent) {
    var k = data.filters['class'];
    if (k === 'all') {
      var segs = (data.customers && data.customers.segments) || [];
      var mix = el('span', 'kd-mix');
      ['unmarked', 'internal', 'test'].forEach(function (c) {
        var s = segs.filter(function (x) { return x['class'] === c; })[0];
        var sp = el('span'); sp.appendChild(icon(CLASS[c].icon)); sp.appendChild(document.createTextNode(CLASS[c].name + ': ' + int(s ? s.accounts : 0) + ' ' + plural(s ? s.accounts : 0, 'account')));
        mix.appendChild(sp);
      });
      notice(parent, 'flask', [el('strong', null, 'Includes internal and test accounts. '),
        'Choose Account type → Unmarked only to leave them out. Unmarked accounts are not proven customers.', mix], 'is-warn');
    } else if (k === 'unmarked') {
      notice(parent, 'question', [el('strong', null, 'Unmarked accounts only. '), 'Internal and test accounts are left out. Unmarked accounts are not proven customers.']);
    } else {
      notice(parent, CLASS[k].icon, [el('strong', null, CLASS[k].name + ' accounts only. '), CLASS[k].about + ' These figures are not customer activity.']);
    }
  }
  /* A figure the current filters cannot narrow (licence checks and usage
     statistics are recorded without an account) says so where it is shown. */
  function unfiltered(group) {
    var sc = group ? scope([group]) : '';
    if (!sc) return null;
    var t = tag(cap(sc), 'is-warn', 'info'); t.title = 'Recorded without an account, so this figure includes every account type.';
    return t;
  }
  function scopeNote(parent, groups, what) {
    var sc = scope(groups);
    if (sc) notice(parent, 'info', [what + ' ' + sc + '.']);
  }

  /* ---- shared figures ------------------------------------------------------ */

  function revenueTotals() {
    var cur = 0, prev = 0, ccy = 'GBP';
    data.kpi.revenue.forEach(function (r) { if (r.currency === 'GBP' || data.kpi.revenue.length === 1) { cur += n(r.cur); prev += n(r.prev); ccy = r.currency; } });
    return { cur: cur, prev: prev, ccy: ccy, other: data.kpi.revenue.filter(function (r) { return r.currency !== ccy; }) };
  }

  /* Friendly names for the events in the analytics registry (events.v1.json). */
  var EVENTS = {
    app_active: ['App used', 'pulse'], app_opened: ['App opened', 'rocket-launch'], app_updated: ['App updated', 'arrows-clockwise'],
    milestone_reached: ['Milestone reached', 'seal-check'], error_shown: ['Error message shown', 'warning-circle'],
    setting_changed: ['Setting changed', 'gear-six'], analytics_enabled: ['Statistics sharing turned on', 'chart-bar'],
    state_snapshot: ['Library snapshot', 'stack'], onboarding_progressed: ['Onboarding step completed', 'check-circle'],
    screen_viewed: ['Screen viewed', 'squares-four'], library_scan: ['Library scanned', 'magnifying-glass'],
    captures_indexed: ['Captures indexed', 'stack'], screenshots_source_changed: ['Screenshot folder changed', 'folder-plus'],
    project_created: ['Project created', 'folder-plus'], project_renamed: ['Project renamed', 'note-pencil'],
    project_appearance_changed: ['Project appearance changed', 'note-pencil'], project_deleted: ['Project deleted', 'trash'],
    collection_created: ['Collection created', 'stack'], collection_updated: ['Collection updated', 'stack'],
    collection_deleted: ['Collection deleted', 'trash'], collection_membership_changed: ['Added to or removed from a collection', 'stack'],
    capture_organised: ['Capture organised', 'folder-plus'], capture_opened: ['Capture opened', 'image-square'],
    tag_changed: ['Tags edited', 'tag'], note_changed: ['Note edited', 'note-pencil'], metadata_changed: ['Details edited', 'note-pencil'],
    search_performed: ['Search', 'magnifying-glass'], view_changed: ['View changed', 'squares-four'],
    duplicates_checked: ['Duplicates checked', 'copy'], duplicates_resolved: ['Duplicates resolved', 'copy'],
    rule_saved: ['Rule saved', 'list'], rule_changed: ['Rule changed', 'list'], rules_applied: ['Rules applied', 'lightning'],
    sign_in: ['Signed in', 'user-check'], trial_started: ['Trial started', 'hourglass-medium'], access_changed: ['Access changed', 'shield-check'],
    checkout_opened: ['Checkout opened', 'credit-card'], portal_opened: ['Billing page opened', 'credit-card'],
    device_deactivated: ['Device deactivated', 'monitor'], capture_completed: ['Screenshot captured', 'camera'],
    capture_failed: ['Capture failed', 'warning-circle'], capture_cancelled: ['Capture cancelled', 'x-circle'],
    history_used: ['Capture history used', 'clock-counter-clockwise'], pro_banner: ['Pro banner', 'sparkle'], link_opened: ['Link opened', 'link-simple']
  };
  function eventName(e) { return (EVENTS[e] || [words(e)])[0]; }
  function eventIcon(e) { return (EVENTS[e] || [])[1] || 'lightning'; }

  /* Feature totals grouped by event across platforms, in rank order. */
  function featureRows() {
    var by = {}, order = [];
    data.usage.features.forEach(function (r) {
      if (!by[r.event]) { by[r.event] = []; order.push(r.event); }
      by[r.event].push(r);
    });
    return order.map(function (e) {
      var parts = by[e], tot = sumVals(parts.map(function (p) { return p.total; }));
      return { event: e, total: tot, parts: parts };
    });
  }

  /* ---- views ------------------------------------------------------------- */

  function viewOverview(v) {
    var k = data.kpi, rv = revenueTotals();
    var top = block(v);
    classNotice(top);

    var hero = kpis(top, true);
    kpi(hero, { icon: 'currency-gbp', tone: 'money', label: 'Revenue received', value: money(rv.cur, rv.ccy),
      sub: 'Real (live) payments in the last ' + periodLabel() + (rv.other.length ? '. Other currencies are on Customers.' : ''),
      delta: delta(rv.cur, rv.prev, function (x) { return money(x, rv.ccy); }),
      help: 'Money actually paid through Stripe in live mode during the period. Stripe test-mode payments are never included.' });
    kpi(hero, { icon: 'credit-card', tone: 'money', label: 'Active subscriptions', value: int(k.active_subscriptions),
      sub: 'Live subscriptions right now',
      help: 'Live Stripe subscriptions that are active or in a Stripe trial at this moment, whatever period is selected. Test-mode subscriptions are excluded.' });

    var g = kpis(top);
    kpi(g, { icon: 'users', tone: 'grow', label: 'New sign-ups', value: int(k.new_accounts.cur), sub: 'Kapture accounts created',
      delta: delta(k.new_accounts.cur, k.new_accounts.prev), help: 'Accounts created in the period. A sign-up is not necessarily a paying customer.' });
    kpi(g, { icon: 'hourglass-medium', tone: 'grow', label: 'Trials started', value: int(k.trials_started.cur), sub: 'Free Kapture Pro trials',
      delta: delta(k.trials_started.cur, k.trials_started.prev), help: 'Kapture Pro free trials started in the period. Each account can start one trial.' });
    kpi(g, { icon: 'monitor', tone: 'device', label: 'Devices using Kapture', value: int(k.active_devices), sub: 'Licensed computers that checked in',
      help: 'Computers with an active licence that checked in during the period. A device is a computer, not a person: one person can use several.' });
    kpi(g, { icon: 'plugs-connected', tone: 'device', label: 'Device activations', value: int(k.activations.cur), sub: 'Computers signed in to Kapture Pro',
      delta: delta(k.activations.cur, k.activations.prev),
      help: 'How many times a computer was activated. One computer can activate more than once (for example after reinstalling), so this is not a count of devices, people or new customers.' });
    scopeNote(top, ['payments', 'accounts', 'subscriptions'], 'Revenue, subscriptions and sign-ups are');

    // What changed recently.
    var gr = grid(block(v, 'Recent activity', 'calendar-check'));
    var pr = panel(gr, 12, 'Today, yesterday and the last 7 days');
    recentTable(pr, [
      { name: 'New sign-ups', icon: 'users', sum: sumKey('registrations') },
      { name: 'Trials started', icon: 'hourglass-medium', sum: sumKey('trials') },
      { name: 'Payments received', icon: 'currency-gbp', sum: sumKey('revenue_cents', true), help: 'Live payments only, in GBP.' },
      { name: 'Device activations', icon: 'plugs-connected', sum: sumKey('activations') },
      { name: 'Daily app activity', icon: 'pulse', sum: sumKey('anonymous_active'), late: true, group: 'anonymous',
        help: 'Anonymous: each install counts once for each day it is used. Apps send these totals about once a day, so today and yesterday fill in later.' }
    ]);

    // Trends.
    var tb = block(v, 'Over the period', 'chart-line-up');
    var g2 = grid(tb);
    var p1 = panel(g2, 8, 'Growth per day', { sub: fmtDay(data.period.from) + ' – ' + fmtDay(data.period.to) + ' · hover a day for details' });
    switcher(p1, [
      { label: 'Sign-ups and trials', defs: [{ key: 'registrations', name: 'New sign-ups', c: 1 }, { key: 'trials', name: 'Trials started', c: 2 }], empty: 'No sign-ups or trials in this period.' },
      { label: 'Device activations', defs: [{ key: 'activations_macos', name: 'macOS', c: 4 }, { key: 'activations_windows', name: 'Windows', c: 2 }], empty: 'No device activations in this period.' }
    ], function (h, o) {
      bars(h, data.series, o.defs, { label: o.label + ' per day', empty: o.empty, emptyIcon: 'chart-bar' });
    });
    var p2 = panel(g2, 4, 'Revenue received per day', { icon: 'currency-gbp', help: 'Live payments on the day they were received. GBP only.' });
    moneyDays(p2, data.series, 'revenue_cents', 'Received');

    var p3 = panel(g2, 6, 'Daily app activity', { icon: 'pulse', group: 'anonymous', help: 'Anonymous totals: each install counts once for each day it is used. Without an identifier this cannot say how many different people used Kapture.' });
    bars(p3, data.series, [{ key: 'anonymous_active', name: 'Active installs', c: 2 }], { height: 130, label: 'Daily app activity',
      emptyIcon: 'pulse', empty: data.switches.aggregate ? 'No app activity has arrived yet.' : 'Anonymous statistics are switched off.',
      emptyWhy: data.switches.aggregate ? ' Apps send anonymous totals about once a day after they are opened.' : '' });
    var p4 = panel(g2, 6, 'Most used features', { icon: 'cursor-click', group: 'anonymous', sub: 'Top actions in the period. Counts actions, not people.' });
    var fr = featureRows().filter(function (r) { return r.event !== 'app_opened'; }).slice(0, 5);
    hbars(p4, fr.map(function (r) { return { label: eventName(r.event), icon: eventIcon(r.event), value: r.total.exact ? r.total.value : (r.total.text === '<5' ? '<5' : r.total.value), display: r.total.text, fill: 'kd-f2' }; }),
      ['cursor-click', data.switches.aggregate ? 'No feature activity yet.' : 'Anonymous statistics are switched off.', data.switches.aggregate ? ' It appears once apps send their daily totals.' : '']);
    if (fr.length) { var a = el('a', 'kd-panel-sub', 'See all features on Product usage →'); a.href = '#usage'; p4.appendChild(a); }
  }

  function viewCustomers(v) {
    var c = data.customers, k = data.kpi, rv = revenueTotals();
    var top = block(v);
    classNotice(top);
    scopeNote(top, ['accounts', 'trials', 'subscriptions', 'payments'], 'These figures are');

    var hero = kpis(top, true);
    kpi(hero, { icon: 'users', tone: 'grow', label: 'Total accounts', value: int(c.accounts_total), sub: 'All time, for the selected account type',
      help: 'Every Kapture account of the selected type, whenever it was created.' });
    kpi(hero, { icon: 'credit-card', tone: 'money', label: 'Active subscriptions', value: int(k.active_subscriptions), sub: 'Live subscriptions right now',
      help: 'Live Stripe subscriptions that are active or in a Stripe trial at this moment. Test-mode subscriptions are excluded.' });
    kpi(hero, { icon: 'currency-gbp', tone: 'money', label: 'Revenue received', value: money(rv.cur, rv.ccy), sub: 'Real (live) payments in the last ' + periodLabel(),
      delta: delta(rv.cur, rv.prev, function (x) { return money(x, rv.ccy); }),
      help: 'Money actually paid through Stripe in live mode during the period. Stripe test-mode payments are never included.' });

    var g = kpis(top);
    kpi(g, { icon: 'user-plus', tone: 'grow', label: 'New sign-ups', value: int(k.new_accounts.cur), sub: 'Accounts created', delta: delta(k.new_accounts.cur, k.new_accounts.prev) });
    kpi(g, { icon: 'user-check', tone: 'grow', label: 'Confirmed accounts', value: int(c.confirmed_total), sub: int(c.confirmed_in_period) + ' confirmed in the period',
      help: 'Accounts whose email address has been confirmed, all time.' });
    kpi(g, { icon: 'hourglass-medium', tone: 'grow', label: 'Active trials', value: int(c.trials_active), sub: int(c.trials_started) + ' started · ' + int(c.trials_ended) + ' ended in the period',
      help: 'Kapture Pro free trials running right now.' });
    var conv = c.conversion;
    if (!n(conv.eligible)) {
      kpi(g, { icon: 'chart-line-up', tone: 'quiet', label: 'Trial conversion', value: 'Not enough history yet', text: true,
        sub: 'No trials have reached the conversion measurement window.',
        help: 'Share of trials that became a paid live subscription within 21 days. Only trials started at least 21 days ago count, and a percentage is shown from 5 such trials.' });
    } else {
      kpi(g, { icon: 'chart-line-up', tone: 'grow', label: 'Trial conversion',
        value: conv.eligible >= 5 ? Math.round(100 * conv.converted / conv.eligible) + '%' : int(conv.converted) + ' of ' + int(conv.eligible), text: conv.eligible < 5,
        sub: conv.eligible >= 5 ? int(conv.converted) + ' of ' + int(conv.eligible) + ' trials became paid within 21 days' : 'Trials that became paid within 21 days. A percentage is shown from 5 trials.',
        help: 'Share of trials that became a paid live subscription within 21 days. Only trials started at least 21 days ago count.' });
    }

    // Subscriptions.
    var sb = block(v, 'Subscriptions', 'arrows-clockwise');
    var gs = kpis(sb);
    kpi(gs, { icon: 'credit-card', tone: 'money', label: 'New subscriptions', value: int(c.subscriptions_new), sub: 'Live, started in the period',
      help: 'Live Stripe subscriptions created in the period.' });
    kpi(gs, { icon: 'calendar-blank', tone: c.subscriptions_set_to_cancel ? 'warn' : 'quiet', label: 'Ending soon', value: int(c.subscriptions_set_to_cancel), sub: 'Set to cancel at period end',
      help: 'Active live subscriptions that are set to cancel at the end of their current billing period.' });
    kpi(gs, { icon: 'x-circle', tone: 'quiet', label: 'Ended', value: int(c.subscriptions_cancelled), sub: 'Live subscriptions ended in the period' });
    if (c.subscriptions_test_mode) notice(sb, 'flask', [int(c.subscriptions_test_mode) + ' active test-mode ' + plural(c.subscriptions_test_mode, 'subscription') + ' left out of every figure here.']);

    // Over the period.
    var ob = block(v, 'Over the period', 'chart-line-up');
    var og = grid(ob);
    var p1 = panel(og, 8, 'Sign-ups and trials per day', { sub: fmtDay(data.period.from) + ' – ' + fmtDay(data.period.to) + ' · hover a day for details' });
    switcher(p1, [
      { label: 'Both', defs: [{ key: 'registrations', name: 'New sign-ups', c: 1 }, { key: 'trials', name: 'Trials started', c: 2 }] },
      { label: 'Sign-ups', defs: [{ key: 'registrations', name: 'New sign-ups', c: 1 }] },
      { label: 'Trials', defs: [{ key: 'trials', name: 'Trials started', c: 2 }] }
    ], function (h, o) { bars(h, data.series, o.defs, { label: o.label + ' per day', empty: 'No sign-ups or trials in this period.', emptyIcon: 'users' }); });
    var col = el('div', 'kd-span-4 kd-col'); og.appendChild(col);
    var STATUS = { active: 'active', trialing: 'in Stripe trial', past_due: 'payment overdue', canceled: 'cancelled', unpaid: 'unpaid', incomplete: 'incomplete', incomplete_expired: 'expired', paused: 'paused' };
    var p2 = panel(col, 12, 'Subscriptions by plan', { icon: 'credit-card', help: 'Live Stripe subscriptions in any status. The Plan filter narrows this.' });
    hbars(p2, c.subscriptions.map(function (r) {
      return { label: cap(r.plan) + ' · ' + (STATUS[r.status] || words(r.status)), value: r.n, display: int(r.n), fill: r.plan === 'annual' ? 'kd-f3' : 'kd-f2',
               icon: r.status === 'active' || r.status === 'trialing' ? 'check-circle' : 'minus' };
    }), ['credit-card', 'No live subscriptions for these filters.', '']);
    var p3 = panel(col, 12, 'Trials by platform', { icon: 'devices', help: 'Trials started in the period.' });
    hbars(p3, Object.keys(c.trials_by_platform).map(function (key) { return { label: plat(key), icon: PLATFORM_ICON[key], value: c.trials_by_platform[key], display: int(c.trials_by_platform[key]), fill: key === 'windows' ? 'kd-f2' : 'kd-f4' }; }),
      ['hourglass-medium', 'No trials started in this period.', '']);

    // Revenue: real money and test money never share a panel.
    var r = block(v, 'Revenue', 'currency-gbp', 'Revenue is money actually paid in the period. It is not recurring subscription value: an annual plan pays once a year, a monthly plan once a month.');
    var gr = grid(r);
    var live = c.payments.filter(function (x) { return x.mode === 'live'; }), test = c.payments.filter(function (x) { return x.mode !== 'live'; });
    var className = function (x) { return (CLASS[x['class']] || { name: cap(x['class']) }).name; };
    var pl = panel(gr, 8, 'Real payments received', { icon: 'wallet', sub: 'Live Stripe payments by account type' });
    hbars(pl, live.map(function (x) {
      return { label: className(x), icon: (CLASS[x['class']] || {}).icon || 'question', value: n(x.cents_period), display: money(x.cents_period, x.currency), fill: x['class'] === 'unmarked' ? 'kd-f3' : 'kd-f5',
               tags: [tag(int(x.count_period) + ' in period'), tag(money(x.cents_all, x.currency) + ' all time')] };
    }), ['receipt', 'No live payments for these filters.', '']);
    if (live.some(function (x) { return x['class'] === 'internal' || x['class'] === 'test'; }))
      pl.appendChild(el('p', 'kd-panel-sub', 'Internal and test accounts paid real money in live mode. That money is real, but it is not customer revenue.'));
    if (c.failed_payments) notice(pl, 'warning-circle', [int(c.failed_payments) + ' live ' + plural(c.failed_payments, 'payment') + ' failed in the period.'], 'is-warn');
    var pt = panel(gr, 4, 'Test payments', { icon: 'flask', cls: 'is-test', sub: 'Stripe test mode. Not real money, never counted as revenue.' });
    hbars(pt, test.map(function (x) { return { label: className(x), icon: 'flask', value: n(x.count_all), display: int(x.count_all) + ' · ' + money(x.cents_all, x.currency) }; }),
      ['flask', 'No test payments for these filters.', ''], { noBars: true });
    var ph = panel(gr, 12, 'Revenue received per day', { icon: 'currency-gbp', sub: 'Live payments, GBP' });
    moneyDays(ph, data.series, 'revenue_cents', 'Received');
    dailyTable(ph, ['revenue_cents'], ['Received'], { revenue_cents: true }, 'Payment history by day');
    if (rv.other.length) ph.appendChild(el('p', 'kd-panel-sub', 'Also received in other currencies: ' + rv.other.map(function (o) { return money(o.cur, o.currency); }).join(', ') + '.'));

    // Account types: always all three, whatever the filter.
    var ct = block(v, 'Account types', 'identification-card', 'Account types come from existing records only. They are never guessed from behaviour. This section always shows all three types, whatever the filter.');
    var cg = kpis(ct);
    ['unmarked', 'internal', 'test'].forEach(function (key) {
      var s = c.segments.filter(function (x) { return x['class'] === key; })[0] || {};
      var card = kpi(cg, { icon: CLASS[key].icon, tone: key === 'unmarked' ? 'grow' : 'quiet', label: CLASS[key].name, value: int(s.accounts), sub: CLASS[key].about });
      var f = el('div', 'kd-kpi-foot'); card.appendChild(f);
      stats(f, [['Active trials', int(s.trials_active)], ['Live subscriptions', int(s.subscriptions_live)], ['Live payments, all time', money(s.revenue_live_cents)]]).className += ' is-compact';
    });
  }

  function cmpVersion(a, b) {
    var pa = String(a).split('.').map(Number), pb = String(b).split('.').map(Number);
    for (var i = 0; i < Math.max(pa.length, pb.length); i++) { var x = pa[i] || 0, y = pb[i] || 0; if (isNaN(x) || isNaN(y)) return String(a).localeCompare(String(b)); if (x !== y) return x - y; }
    return 0;
  }
  var OUTCOME = {
    issued: ['Licence issued', 'good'], device_limit: ['Device limit reached', 'quiet'], not_signed_in: ['Not signed in', 'quiet'],
    invalid_request: ['Request not valid', 'warn'], invalid_platform: ['Unsupported platform', 'warn'],
    unavailable: ['Licence service unavailable', 'bad'], error: ['Check failed', 'bad']
  };

  function viewDevices(v) {
    var d = data.devices, k = data.kpi;
    var top = block(v);
    scopeNote(top, ['devices'], 'Device figures are');
    if (data.filters.platform === 'chrome') notice(top, 'google-chrome-logo', ['Kapture for Chrome has no licence or licensed devices. These figures are for Kapture Pro on macOS and Windows.']);
    var sum = function (o) { return Object.keys(o).reduce(function (s, x) { return s + n(o[x]); }, 0); };
    var by = function (o) { return Object.keys(o).sort().map(function (x) { return plat(x) + ' ' + int(o[x]); }).join(' · ') || 'None yet'; };
    var checks = d.licence_outcomes.reduce(function (s, r) { return s + n(r.checks); }, 0);
    var issued = d.licence_outcomes.filter(function (r) { return r.outcome === 'issued'; }).reduce(function (s, r) { return s + n(r.checks); }, 0);
    var failed = d.licence_outcomes.filter(function (r) { return OUTCOME[r.outcome] && OUTCOME[r.outcome][1] === 'bad'; }).reduce(function (s, r) { return s + n(r.checks); }, 0);

    var hero = kpis(top, true);
    kpi(hero, { icon: 'monitor', tone: 'device', label: 'Licensed devices', value: int(sum(d.active_seats)), sub: 'Activated right now · ' + by(d.active_seats),
      help: 'Computers activated for Kapture Pro and not deactivated, right now. One licence can cover more than one device, and a device is not a person.' });
    kpi(hero, { icon: 'clock-counter-clockwise', tone: 'device', label: 'Connected devices', value: int(sum(d.seen_in_period)), sub: 'Checked in during the period · ' + by(d.seen_in_period),
      help: 'Licensed devices that checked their licence at least once in the period.' });
    var g = kpis(top);
    kpi(g, { icon: 'plugs-connected', tone: 'device', label: 'Device activations', value: int(k.activations.cur), sub: 'Computers signed in to Kapture Pro',
      delta: delta(k.activations.cur, k.activations.prev),
      help: 'How many times a computer was activated. One device can activate more than once, and an activation is not a new customer.' });
    kpi(g, { icon: 'x-circle', tone: 'quiet', label: 'Deactivated', value: int(d.deactivations_in_period), sub: 'Devices removed from a licence',
      help: 'Devices removed from a licence in the period, by the user or automatically.' });
    kpi(g, { icon: 'shield-check', tone: failed ? 'warn' : 'good', label: 'Licence checks', value: int(k.licence_checks.cur), group: 'licence_checks',
      sub: !checks ? 'None in this period' : checks >= 20 ? Math.round(100 * issued / checks) + '% issued a licence' : int(issued) + ' of ' + int(checks) + ' issued a licence',
      delta: delta(k.licence_checks.cur, k.licence_checks.prev),
      help: 'Background checks the apps make to confirm a licence. They are not user sessions, and one device checks many times.' });

    // Recent activity.
    var rg = grid(block(v, 'Recent activity', 'calendar-check'));
    var pr = panel(rg, 12, 'Today, yesterday and the last 7 days');
    recentTable(pr, [
      { name: 'Activations on macOS', icon: 'apple-logo', sum: sumKey('activations_macos') },
      { name: 'Activations on Windows', icon: 'windows-logo', sum: sumKey('activations_windows') },
      { name: 'Licences issued', icon: 'shield-check', sum: sumKey('licence_issued'), group: 'licence_checks' }
    ]);

    // macOS and Windows.
    var pg = grid(block(v, 'macOS and Windows', 'devices'));
    var pp = panel(pg, 12, 'Platforms side by side', { sub: 'Kapture Pro devices. The split bar is drawn from 10 devices, so a tiny sample does not look like a trend.' });
    var wrap = el('div', 'kd-platforms');
    [['macos', 'is-mac'], ['windows', 'is-win']].forEach(function (pl) {
      var key = pl[0], col = el('div', 'kd-platform ' + pl[1]), h = el('div', 'kd-platform-head');
      h.appendChild(icon(PLATFORM_ICON[key])); h.appendChild(document.createTextNode(plat(key))); col.appendChild(h);
      stats(col, [['Licensed', int(d.active_seats[key] || 0)], ['Connected', int(d.seen_in_period[key] || 0)], ['Activations', int((d.activations_in_period || {})[key] || 0)]]);
      var vs = d.versions.filter(function (r) { return r.platform === key; }).map(function (r) { return r.version; }).sort(cmpVersion).reverse();
      var tags = el('div', 'kd-tags');
      if (!vs.length) tags.appendChild(tag('No versions reported in this period'));
      vs.forEach(function (x) { tags.appendChild(tag(x === 'unknown' ? 'Version unknown' : 'v' + x)); });
      col.appendChild(tags);
      wrap.appendChild(col);
    });
    pp.appendChild(wrap);
    var mac = n(d.active_seats.macos), win = n(d.active_seats.windows);
    if (mac + win >= 10) {
      var split = el('div', 'kd-split'); split.setAttribute('role', 'img');
      split.setAttribute('aria-label', 'Licensed devices: macOS ' + Math.round(100 * mac / (mac + win)) + '%, Windows ' + Math.round(100 * win / (mac + win)) + '%');
      var sm = el('span', 'is-mac'), sw = el('span', 'is-win'); sm.style.width = (100 * mac / (mac + win)) + '%'; sw.style.width = (100 * win / (mac + win)) + '%';
      split.appendChild(sm); split.appendChild(sw); pp.appendChild(split);
      var lg = el('div', 'kd-legend'); lg.appendChild(el('span', 'kd-sw-4', 'macOS ' + Math.round(100 * mac / (mac + win)) + '%')); lg.appendChild(el('span', 'kd-sw-2', 'Windows ' + Math.round(100 * win / (mac + win)) + '%')); pp.appendChild(lg);
    }

    // Over the period.
    var og = grid(block(v, 'Over the period', 'chart-line-up'));
    var pa = panel(og, 8, 'Activations per day', { sub: fmtDay(data.period.from) + ' – ' + fmtDay(data.period.to) + ' · hover a day for details' });
    switcher(pa, [
      { label: 'Activations', defs: [{ key: 'activations_macos', name: 'macOS', c: 4 }, { key: 'activations_windows', name: 'Windows', c: 2 }], empty: 'No activations in this period.' },
      { label: 'Licence checks', group: 'licence_checks', defs: [{ key: 'licence_issued', name: 'Licence issued', c: 1 }, { key: 'other_checks', name: 'Other answers', c: 5 }], empty: 'No licence checks in this period.' }
    ], function (h, o) {
      var uf = unfiltered(o.group); if (uf) { var ufp = el('p', 'kd-panel-sub'); ufp.appendChild(uf); h.appendChild(ufp); }
      var ser = data.series.map(function (p) { return Object.assign({}, p, { other_checks: Math.max(0, n(p.licence_checks) - n(p.licence_issued)) }); });
      bars(h, ser, o.defs, { label: o.label + ' per day', empty: o.empty, emptyIcon: 'plugs-connected' });
    });
    dailyTable(pa, ['activations_macos', 'activations_windows', 'licence_issued', 'licence_checks'], ['macOS activations', 'Windows activations', 'Licences issued', 'All licence checks']);
    var po = panel(og, 4, 'Licence checks', { icon: 'shield-check', group: 'licence_checks', sub: 'Answers in the period' });
    var grouped = {};
    d.licence_outcomes.forEach(function (r) { grouped[r.outcome] = (grouped[r.outcome] || 0) + n(r.checks); });
    hbars(po, Object.keys(grouped).sort(function (a, b) { return grouped[b] - grouped[a]; }).map(function (o) {
      var m = OUTCOME[o] || [words(o), 'quiet'];
      return { label: m[0], value: grouped[o], display: int(grouped[o]), icon: m[1] === 'good' ? 'check-circle' : m[1] === 'bad' ? 'x-circle' : m[1] === 'warn' ? 'warning-circle' : 'minus',
               fill: m[1] === 'good' ? 'kd-f-good' : m[1] === 'bad' ? 'kd-f-bad' : 'kd-f5' };
    }), ['shield-check', 'No licence checks in this period.', '']);
    if (d.licence_outcomes.length) {
      po.appendChild(el('p', 'kd-panel-sub', '“Not signed in” and “Device limit reached” are normal answers, not faults.'));
      table(details(po, 'Raw outcomes by platform'), [{ t: 'Platform' }, { t: 'Shown as' }, { t: 'Raw status' }, { t: 'Checks', n: 1 }],
        d.licence_outcomes.map(function (r) { var c = el('code', null, r.outcome); return [plat(r.platform), (OUTCOME[r.outcome] || [words(r.outcome)])[0], c, int(r.checks)]; }));
    }

    // Supporting: versions.
    var vg = grid(block(v, 'App versions', 'stack', '“Newest reported” is the highest version these devices reported. It may not be the latest release, so older versions are not necessarily out of date.'));
    var pv = panel(vg, 12, 'Versions in use', { sub: 'Connected devices, by the version they last reported' });
    var newest = {};
    d.versions.forEach(function (r) { if (r.version !== 'unknown' && (!newest[r.platform] || cmpVersion(r.version, newest[r.platform]) > 0)) newest[r.platform] = r.version; });
    var vrows = d.versions.slice().sort(function (a, b) { return a.platform === b.platform ? cmpVersion(b.version, a.version) : a.platform < b.platform ? -1 : 1; });
    hbars(pv, vrows.map(function (r) {
      var isNew = newest[r.platform] === r.version;
      return { label: plat(r.platform) + ' ' + (r.version === 'unknown' ? '(version unknown)' : r.version), icon: PLATFORM_ICON[r.platform], value: r.devices,
               display: int(r.devices) + ' ' + plural(r.devices, 'device'), fill: r.platform === 'windows' ? 'kd-f2' : 'kd-f4',
               tags: [isNew ? tag('Newest reported', 'is-good') : r.version === 'unknown' ? null : tag('Older version')].filter(Boolean) };
    }), ['stack', 'No devices connected in this period.', ' Versions appear when licensed devices check in.']);
  }

  function viewUsage(v) {
    var u = data.usage, act = u.activity, oi = u.optin_installs;
    var top = block(v);
    scopeNote(top, ['anonymous', 'opt_in'], 'Usage statistics are not linked to accounts, so they are');
    var noAgg = !data.switches.aggregate, noUse = !data.switches.usage;

    var today = utcToday();
    var lastMonth = new Date(Date.UTC(today.getUTCFullYear(), today.getUTCMonth() - 1, 1)).toLocaleDateString('en-GB', { month: 'long', timeZone: 'UTC' });
    var wkEnd = new Date(today); wkEnd.setUTCDate(wkEnd.getUTCDate() - ((wkEnd.getUTCDay() + 6) % 7) - 1);
    var wkStart = new Date(wkEnd); wkStart.setUTCDate(wkStart.getUTCDate() - 6);
    var combined = function (key) {
      var s = sumVals(act.map(function (r) { return r[key]; }));
      var split = act.length > 1 ? act.map(function (r) { return plat(r.platform) + (r.app && r.app !== 'pro' ? ' (' + r.app + ')' : '') + ' ' + short(r[key]); }).join(' · ') : '';
      return { value: act.length ? s.text : '—', split: split };
    };

    // Everyone: anonymous totals (installs, not people).
    if (noAgg) notice(top, 'toggle-left', [el('strong', null, 'Anonymous statistics are switched off. '), 'The figures below are not being collected.']);
    else if (!act.length) notice(top, 'clock', [el('strong', null, 'No app activity has arrived yet. '), 'Apps send anonymous totals about once a day after they are opened, so a dash means “no data yet”, not zero use.']);
    var hero = kpis(top, true);
    var d1 = combined('dau'), w1 = combined('wau'), m1 = combined('mau');
    kpi(hero, { icon: 'sun', tone: 'use', label: 'Active yesterday', value: d1.value, sub: d1.split || fmtDay(iso(new Date(today - 864e5))) + ' (UTC)',
      help: 'Anonymous: installs used yesterday (' + fmtDay(iso(new Date(today - 864e5))) + ', UTC), each counted once. Installs, not people. Yesterday is used because apps report with a delay.' });
    kpi(hero, { icon: 'calendar-blank', tone: 'use', label: 'Active last week', value: w1.value, sub: w1.split || fmtDay(iso(wkStart)) + ' – ' + fmtDay(iso(wkEnd)),
      help: 'Anonymous: installs used at least once in the last full week, Monday to Sunday (' + fmtDay(iso(wkStart)) + ' – ' + fmtDay(iso(wkEnd)) + '). Each install counts once.' });
    kpi(hero, { icon: 'calendar-check', tone: 'use', label: 'Active in ' + lastMonth, value: m1.value, sub: m1.split || 'Last full calendar month',
      help: 'Anonymous: installs used at least once in ' + lastMonth + '. Each install counts once.' });
    kpi(hero, { icon: 'rocket-launch', tone: 'grow', label: 'First launches', value: isSupp(u.first_launches) ? '<5' : !act.length && !n(u.first_launches) ? '—' : int(u.first_launches), sub: 'New installs in the period',
      help: 'Anonymous: installs opened for the first time in the period.' });

    // Sharing devices: opted in, counted by a random install ID.
    var sb = block(v, 'Sharing devices', 'chart-bar', 'Installs whose user chose “Share statistics”. They carry a random ID, so each device is counted once. This is a small, self-selected group, separate from the anonymous totals above.');
    if (noUse) notice(sb, 'toggle-left', ['Detailed statistics are switched off.']);
    var gb = kpis(sb);
    var oiSum = function (key) { return oi.length ? sumVals(oi.map(function (r) { return r[key]; })).text : noUse ? '—' : '0'; };
    var oiSplit = function (key) { return oi.length > 1 ? oi.map(function (r) { return plat(r.platform) + ' ' + short(r[key]); }).join(' · ') : ''; };
    kpi(gb, { icon: 'devices', tone: 'device', label: 'Last 30 days', value: oiSum('mau'), sub: oiSplit('mau') || 'Sharing devices active', help: 'Distinct opted-in devices used at least once in the last 30 days.' });
    kpi(gb, { icon: 'calendar-blank', tone: 'device', label: 'Last 7 days', value: oiSum('wau'), sub: oiSplit('wau') || 'Sharing devices active', help: 'Distinct opted-in devices used at least once in the last 7 days.' });
    kpi(gb, { icon: 'sun', tone: 'device', label: 'Yesterday', value: oiSum('dau'), sub: oiSplit('dau') || 'Sharing devices active', help: 'Distinct opted-in devices used yesterday (UTC).' });

    // Recent activity.
    var rg = grid(block(v, 'Recent activity', 'calendar-check'));
    var pr = panel(rg, 12, 'Today, yesterday and the last 7 days', { sub: 'Apps send totals about once a day, so today and yesterday usually fill in a day later.' });
    recentTable(pr, [
      { name: 'Daily app activity', icon: 'pulse', sum: sumKey('anonymous_active'), late: true, help: 'Anonymous: installs used that day, each counted once. Over 7 days the days are added, so this is not unique installs or people.' },
      { name: 'Sharing devices active', icon: 'devices', sum: sumKey('optin_active'), late: true, help: 'Distinct opted-in devices used that day. Over 7 days the days are added, so one device can count more than once.' }
    ]);

    // Over the period.
    var og = grid(block(v, 'Over the period', 'chart-line-up'));
    var pd = panel(og, 8, 'Daily app activity', { sub: fmtDay(data.period.from) + ' – ' + fmtDay(data.period.to) + ' · hover a day for details' });
    switcher(pd, [
      { label: 'Everyone', defs: [{ key: 'anonymous_active', name: 'Installs active', c: 2 }],
        empty: noAgg ? 'Anonymous statistics are switched off.' : 'No daily activity yet.', why: noAgg ? '' : ' Apps send totals about once a day after they are opened.' },
      { label: 'Sharing devices', defs: [{ key: 'optin_active', name: 'Sharing devices active', c: 4 }],
        empty: noUse ? 'Detailed statistics are switched off.' : 'No sharing devices yet.', why: noUse ? '' : ' They appear once someone chooses “Share statistics”.' }
    ], function (h, o) { bars(h, data.series, o.defs, { label: o.label + ' per day', empty: o.empty, emptyWhy: o.why, emptyIcon: 'pulse' }); });
    dailyTable(pd, ['anonymous_active', 'optin_active'], ['Installs active', 'Sharing devices active']);
    var pe = panel(og, 4, 'Versions and systems', { icon: 'stack', sub: 'Daily app activity, by environment' });
    if (!u.environments.length) empty(pe, 'stack', 'No app activity yet.', '');
    else {
      hbars(pe, u.environments.slice(0, 5).map(function (r) { return { label: plat(r.platform) + ' ' + r.version + ' · ' + words(r.os) + ' · ' + r.locale, icon: PLATFORM_ICON[r.platform], value: r.active_days, display: short(r.active_days), fill: 'kd-f2' }; }), []);
      if (u.environments.length > 5) table(details(pe, 'All ' + u.environments.length + ' environments'), [{ t: 'Platform' }, { t: 'Version' }, { t: 'System' }, { t: 'Language' }, { t: 'Active days', n: 1 }],
        u.environments.map(function (r) { return [plat(r.platform), r.version, words(r.os), r.locale, short(r.active_days)]; }));
    }

    // Most used features: full width, the screen's main list.
    var fg = grid(block(v, 'Most used features', 'cursor-click', 'Anonymous totals of actions in the period, from every install. They count actions, not people. Figures from 1 to 4 show as <5.'));
    var pf = panel(fg, 12, 'What people do in Kapture', { sub: 'Actions in the last ' + periodLabel() + ', top 20. Comparison with the previous period is not available yet.' });
    var fr = featureRows();
    hbars(pf, fr.map(function (r, i) {
      var tags = r.parts.map(function (p) { return tag(plat(p.platform) + ' ' + short(p.total), null, PLATFORM_ICON[p.platform]); });
      return { label: eventName(r.event), icon: eventIcon(r.event), value: r.total.text === '<5' ? '<5' : r.total.value, display: r.total.text + (r.total.text === '<5' ? '' : ' ' + plural(r.total.value, 'time')),
               fill: i < 3 ? 'kd-f2' : 'kd-f5', tags: tags };
    }), ['cursor-click', noAgg ? 'Anonymous statistics are switched off.' : 'No feature activity in this period yet.', noAgg ? '' : ' Actions appear once apps send their daily totals.']);
    if (fr.length) table(details(pf, 'Raw event names'), [{ t: 'Shown as' }, { t: 'Event' }, { t: 'Platform' }, { t: 'Total', n: 1 }],
      u.features.map(function (r) { return [eventName(r.event), el('code', null, r.event), plat(r.platform), short(r.total)]; }));

    // Adoption and return: one compact note while neither has enough data.
    var ab = block(v, 'Adoption and return', 'arrow-counter-clockwise');
    if (!u.adoption.length && !u.retention.length) {
      var pn = panel(grid(ab), 12, 'Not enough sharing devices yet');
      pn.appendChild(el('p', 'kd-panel-sub', 'Feature adoption needs at least 5 sharing devices active in a week. “Are people coming back?” needs a week in which at least 5 devices started sharing, followed by a complete week. Both stay hidden until then, so no one can be singled out.'));
      return;
    }
    var ag = grid(ab);
    var pa = panel(ag, 6, 'Tried each feature', { icon: 'cursor-click', sub: 'Share of sharing devices active last week that used each feature.',
      help: 'Of the opted-in devices active in the last full week, the share that used each feature at least once. Shown from 5 active devices.' });
    hbars(pa, u.adoption.map(function (r) { return { label: eventName(r.event) + ' · ' + plat(r.platform), icon: eventIcon(r.event), value: n(r.percent), display: r.percent + '% of ' + short(r.of), fill: 'kd-f4' }; }),
      ['users', 'Not enough sharing devices last week.', ' At least 5 must be active in a week.']);
    var pc = panel(ag, 6, 'Are people coming back?', { icon: 'arrow-counter-clockwise', sub: 'Share of each week’s new sharing devices used again in later weeks.',
      help: 'Devices that started sharing statistics in the same week form a group. For each later week, this shows the share of that group used again. Only groups of 5 or more are shown.' });
    if (!u.retention.length) empty(pc, 'arrow-counter-clockwise', 'Not enough history yet.', ' This needs a week in which at least 5 devices started sharing, followed by a complete week.');
    else {
      var cohorts = {}, weeks = 0;
      u.retention.forEach(function (r) { (cohorts[r.cohort_week] = cohorts[r.cohort_week] || { size: r.size, w: {} }).w[r.week] = r.percent; weeks = Math.max(weeks, r.week); });
      var heads = [{ t: 'Started week of' }, { t: 'Devices', n: 1 }];
      for (var i = 1; i <= weeks; i++) heads.push({ t: 'Week ' + i, n: 1 });
      table(pc, heads, Object.keys(cohorts).sort().map(function (ck) {
        var row = [fmtDay(ck), short(cohorts[ck].size)];
        for (var j = 1; j <= weeks; j++) row.push(cohorts[ck].w[j] === undefined ? '' : cohorts[ck].w[j] + '%');
        return row;
      }));
      pc.appendChild(el('p', 'kd-panel-sub', 'Week 1 is the week after a device started. Blank cells are weeks that have not finished yet.'));
    }
  }

  /* Scheduled jobs, by the names they have in the database. */
  var JOBS = { 'analytics-adoption': 'Daily analytics summary', 'analytics-purge': 'Old data cleanup', 'kapture-stripe-reconcile': 'Payment reconciliation' };
  function jobName(j) { return JOBS[j] || (/reconcil/.test(j) ? 'Payment reconciliation' : words(j)); }
  /* Next run, only for the simple "minute hour * * *" and "minute * * * *" forms. */
  function nextRun(expr) {
    var m = /^(\d{1,2}) (\d{1,2}|\*) \* \* \*$/.exec(String(expr).trim());
    if (!m) return null;
    var now = new Date(), t = new Date(now);
    t.setUTCSeconds(0, 0); t.setUTCMinutes(Number(m[1]));
    if (m[2] === '*') { if (t <= now) t.setUTCHours(t.getUTCHours() + 1); }
    else { t.setUTCHours(Number(m[2])); if (t <= now) t.setUTCDate(t.getUTCDate() + 1); }
    return t;
  }
  function every(expr) { var m = /^(\d{1,2}) (\d{1,2}|\*) \* \* \*$/.exec(String(expr).trim()); if (!m) return ''; return m[2] === '*' ? 'Hourly' : 'Daily ' + ('0' + m[2]).slice(-2) + ':' + ('0' + m[1]).slice(-2); }

  function viewHealth(v) {
    var h = data.health, i = h.ingest, fr = h.freshness;
    var top = block(v);
    var jobs = h.jobs, active = (jobs || []).filter(function (j) { return j.active; });
    var failedJobs = active.filter(function (j) { return j.last_status === 'failed'; });
    var anyOn = data.switches.aggregate || data.switches.usage;
    var last = fr.last_ingest_day;

    // Status first: the same card as every other screen, with the status as the value.
    var st = kpis(top);
    var status = function (tone, iconName, label, word, sub, help) { kpi(st, { icon: iconName, tone: tone, label: label, value: word, text: true, sub: sub, help: help }); };
    status(data.switches.aggregate ? 'good' : 'quiet', data.switches.aggregate ? 'toggle-right' : 'toggle-left', 'Anonymous analytics', data.switches.aggregate ? 'On' : 'Off', 'Daily totals from every install',
      'Whether the apps are allowed to send anonymous daily totals. On does not by itself mean data is arriving: see Data collection.');
    status(data.switches.usage ? 'good' : 'quiet', data.switches.usage ? 'toggle-right' : 'toggle-left', 'Detailed statistics', data.switches.usage ? 'On' : 'Off', 'Only from people who chose to share');
    if (!anyOn) status('quiet', 'circle-dashed', 'Data collection', 'Not collecting', 'Both switches are off');
    else if (!last) status('quiet', 'clock', 'Data collection', 'Waiting', 'No report has arrived yet');
    else if (daysAgo(last) <= 1) status('good', 'check-circle', 'Data collection', 'Receiving', 'Last report ' + relDay(last));
    else status('quiet', 'clock', 'Data collection', 'Quiet', 'Last report ' + relDay(last), 'No reports recently. This can simply mean no one opened the apps; it is not by itself a fault.');
    if (jobs === null) status('quiet', 'question', 'Scheduled jobs', 'Unavailable', 'The job log could not be read');
    else if (failedJobs.length) status('bad', 'warning-circle', 'Scheduled jobs', 'Needs attention', failedJobs.length + ' failed on the last run');
    else if (!active.some(function (j) { return j.last_status; })) status('quiet', 'clock', 'Scheduled jobs', 'Not yet run', 'No job has run yet');
    else status('good', 'check-circle', 'Scheduled jobs', 'Healthy', active.some(function (j) { return !j.last_status; }) ? 'Every job that ran succeeded' : 'All succeeded on their last run');

    // Needs attention: real problems only, never zero activity on its own.
    var issues = [];
    failedJobs.forEach(function (j) { issues.push(['bad', 'x-circle', jobName(j.name) + ' failed', 'Last run ' + (j.last_start ? fmtTime(j.last_start) : '') + '. Details are under Technical details.']); });
    if (n(h.licence_errors)) issues.push(['bad', 'shield-check', 'Licence checks failed ' + int(h.licence_errors) + ' ' + plural(h.licence_errors, 'time'), 'The licence service was unavailable or returned an error in the period.']);
    if (n(i.limited)) issues.push(['warn', 'prohibit', int(i.limited) + ' analytics ' + plural(i.limited, 'request was', 'requests were') + ' limited', 'A daily limit was reached, so some reports were refused.']);
    if (jobs) active.filter(function (j) { return j.last_status === 'succeeded' && j.last_start && /^\d{1,2} \d{1,2} \* \* \*$/.test(j.schedule) && Date.now() - new Date(j.last_start) > 2 * 864e5; })
      .forEach(function (j) { issues.push(['warn', 'clock', jobName(j.name) + ' has not run for two days', 'It runs daily. Last run ' + fmtTime(j.last_start) + '.']); });
    var ab = block(v, 'Needs attention', 'warning-circle');
    if (!issues.length) notice(ab, 'check-circle', [el('strong', null, 'Nothing needs attention. '), 'No failed jobs, licence errors or limited requests in the period.'], 'is-good');
    else {
      var ul = el('ul', 'kd-attn');
      issues.forEach(function (x) { var li = el('li', 'is-' + x[0]); li.appendChild(icon(x[1])); var t = el('div', null, x[2]); t.appendChild(el('small', null, x[3])); li.appendChild(t); ul.appendChild(li); });
      ab.appendChild(ul);
    }

    // Collection activity.
    var cb = block(v, 'Collection activity', 'tray-arrow-down');
    if (data.filters.platform !== 'all' || data.filters['class'] !== 'all') notice(cb, 'info', ['System figures are not affected by the platform or account type filters.']);
    var cg = kpis(cb);
    kpi(cg, { icon: 'tray-arrow-down', tone: 'use', label: 'Reports received', value: int(n(i.batches_aggregate) + n(i.batches_usage)), sub: int(i.batches_aggregate) + ' anonymous · ' + int(i.batches_usage) + ' detailed',
      help: 'A report is one delivery of statistics from an app, accepted and stored. Apps send about one a day.' });
    kpi(cg, { icon: 'arrows-clockwise', tone: 'use', label: 'Analytics requests', value: int(i.requests), sub: int(h.ingest_today.requests) + ' today',
      help: 'Every call the apps made to the analytics service that reached the database, including duplicates and limited ones.' });
    kpi(cg, { icon: 'database', tone: 'use', label: 'Statistics recorded', value: int(i.entries), sub: 'Individual counts stored', help: 'The individual counts stored from accepted reports.' });
    kpi(cg, { icon: 'prohibit', tone: n(i.limited) ? 'warn' : 'quiet', label: 'Requests limited', value: int(i.limited), sub: int(h.ingest_today.limited) + ' today',
      help: 'Requests refused because a daily limit was reached.' });
    var ser = h.ingest_series.map(function (p) { return Object.assign({}, p, { reports: n(p.batches_aggregate) + n(p.batches_usage) }); });
    var rg = grid(cb);
    var pr = panel(rg, 12, 'Today, yesterday and the last 7 days');
    recentTable(pr, [
      { name: 'Reports received', icon: 'tray-arrow-down', sum: sumKey('reports') },
      { name: 'Analytics requests', icon: 'arrows-clockwise', sum: sumKey('requests') },
      { name: 'Requests limited', icon: 'prohibit', sum: sumKey('limited') }
    ], ser);
    var pc = panel(rg, 12, 'Reports received per day', { sub: 'An empty day means no app sent a report, not that collection failed.' });
    bars(pc, ser, [{ key: 'batches_aggregate', name: 'Anonymous', c: 2 }, { key: 'batches_usage', name: 'Detailed', c: 4 }],
      { label: 'Reports received per day', emptyIcon: 'tray-arrow-down', empty: anyOn ? 'No reports in this period.' : 'Collection is switched off.', emptyWhy: anyOn ? ' Reports arrive when people open the apps.' : '' });

    // Scheduled jobs.
    var jg = grid(block(v, 'Scheduled jobs', 'clock'));
    var pj = panel(jg, 12, 'Automatic tasks', { sub: 'Times are UTC.' });
    if (jobs === null) empty(pj, 'question', 'Job status is unavailable.', ' The job log could not be read.');
    else if (!jobs.length) empty(pj, 'clock', 'No scheduled jobs.', '');
    else {
      var jl = el('ul', 'kd-jobs');
      jobs.forEach(function (j) {
        var ok = j.last_status === 'succeeded', bad = j.last_status === 'failed', li = el('li', 'kd-tone-' + (!j.active ? 'quiet' : bad ? 'bad' : ok ? 'good' : 'quiet'));
        var b = el('span', 'kd-badge'); b.appendChild(icon(bad ? 'x-circle' : ok ? 'check-circle' : 'clock')); li.appendChild(b);
        var name = el('div', 'kd-job-name'); name.appendChild(el('b', null, jobName(j.name))); name.appendChild(el('small', null, every(j.schedule))); li.appendChild(name);
        var nx = j.active ? nextRun(j.schedule) : null;
        var runs = el('div', 'kd-job-runs');
        runs.appendChild(el('span', null, j.last_start ? 'Last ' + fmtTime(j.last_start) : 'Not run yet'));
        if (nx) runs.appendChild(el('span', null, 'Next ' + fmtTime(nx)));
        li.appendChild(runs);
        li.appendChild(tag(!j.active ? 'Paused' : bad ? 'Failed' : ok ? 'Succeeded' : j.last_status ? cap(j.last_status) : 'Not run yet', bad ? 'is-bad' : ok ? 'is-good' : ''));
        jl.appendChild(li);
      });
      pj.appendChild(jl);
    }

    // Technical details, collapsed.
    var td = details(v, 'Technical details', 'is-section');
    var lim = h.limits, day = function (s) { return s ? fmtLong(String(s).slice(0, 10)) : 'None yet'; };
    td.appendChild(el('h4', 'kd-sub-head', 'Other counters in the period'));
    stats(td, [['Duplicate reports ignored', int(i.duplicates), 'Reports sent twice, for example after a retry. They are recognised and not counted again.'],
      ['New sharing installs', int(i.new_installs), 'Installs that shared detailed statistics for the first time.'],
      ['Data deletion requests', int(i.forgets), 'Requests from apps to delete their detailed statistics.']]);
    td.appendChild(el('h4', 'kd-sub-head', 'Data freshness'));
    stats(td, [['Last statistics request', day(fr.last_ingest_day)], ['Last anonymous data', day(fr.last_anonymous_day)], ['Last detailed data', day(fr.last_optin_day)],
      ['Last licence check', day(fr.last_licence_check_day)], ['Last device contact', fr.last_device_contact ? fmtTime(fr.last_device_contact) : 'None yet']]);
    td.appendChild(el('h4', 'kd-sub-head', 'Daily limits'));
    stats(td, [['Requests per day', int(lim.requests_per_day)], ['Statistics per day', int(lim.entries_per_day)], ['New installs per day', int(lim.new_installs_per_day)],
      ['Reports per install per day', int(lim.batches_per_install_day)], ['Statistics per install per day', int(lim.entries_per_install_day)]]);
    if (jobs && jobs.length) {
      td.appendChild(el('h4', 'kd-sub-head', 'Jobs'));
      table(td, [{ t: 'Shown as' }, { t: 'Job name' }, { t: 'Schedule (cron, UTC)' }, { t: 'Active' }, { t: 'Last status' }, { t: 'Last start' }, { t: 'Last end' }],
        jobs.map(function (j) { return [jobName(j.name), el('code', null, j.name), el('code', null, j.schedule), j.active ? 'yes' : 'no', j.last_status || '—', j.last_start ? fmtTime(j.last_start) : '—', j.last_end ? fmtTime(j.last_end) : '—']; }));
    }
    var rows = h.ingest_series.filter(function (p) { return n(p.requests); }).reverse();
    if (rows.length) {
      td.appendChild(el('h4', 'kd-sub-head', 'Daily counters'));
      table(td, [{ t: 'Day' }, { t: 'Requests', n: 1 }, { t: 'Anonymous reports', n: 1 }, { t: 'Detailed reports', n: 1 }, { t: 'Duplicates', n: 1 }, { t: 'Limited', n: 1 }],
        rows.map(function (p) { return [fmtLong(p.day), int(p.requests), int(p.batches_aggregate), int(p.batches_usage), int(p.duplicates), int(p.limited)]; }));
    }
    td.appendChild(el('p', 'kd-panel-sub', 'Requests that are not valid (unknown events, free text, oversized bodies) are refused by the endpoint before they reach the database. They are only in the function logs, so they are not counted here.'));
  }

  var RENDER = { overview: viewOverview, customers: viewCustomers, devices: viewDevices, usage: viewUsage, health: viewHealth };

  function currentView() { var h = location.hash.replace('#', ''); return VIEWS.indexOf(h) >= 0 ? h : 'overview'; }

  function render() {
    if (!data) return;
    hideHover();
    var view = currentView();
    main.setAttribute('data-view', view);
    document.querySelectorAll('#kdTabs a').forEach(function (a) {
      if (a.getAttribute('data-view') === view) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    while (body.firstChild) body.removeChild(body.firstChild);
    var v = el('div', 'kd-view');
    body.appendChild(v);   // attached first, so charts can measure their width
    RENDER[view](v);

    while (meta.firstChild) meta.removeChild(meta.firstChild);
    var range1 = el('span'); range1.appendChild(icon('calendar-blank')); range1.appendChild(document.createTextNode(' ' + fmtDay(data.period.from, { year: 'numeric' }) + ' – ' + fmtDay(data.period.to, { year: 'numeric' }) + ' (UTC)'));
    add(meta, range1, el('span', null, 'compared with the previous ' + data.period.days + ' days'),
      el('span', null, 'updated ' + new Date(data.generated_at).toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' })));
    while (chips.firstChild) chips.removeChild(chips.firstChild);
    [['Anonymous analytics', data.switches.aggregate], ['Detailed statistics', data.switches.usage]].forEach(function (c) {
      var ch = el('span', 'kd-chip' + (c[1] ? ' is-on' : '')); ch.appendChild(icon(c[1] ? 'toggle-right' : 'toggle-left'));
      ch.appendChild(document.createTextNode(c[0] + ' ' + (c[1] ? 'on' : 'off'))); chips.appendChild(ch);
    });
  }

  /* ---- controls ---------------------------------------------------------- */

  document.querySelectorAll('#kdTabs a[data-icon]').forEach(function (a) { a.insertBefore(icon(a.getAttribute('data-icon')), a.firstChild); });
  document.querySelectorAll('[data-tip]').forEach(function (s) { s.parentNode.replaceChild(tip(s.getAttribute('data-tip')), s); });

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
  window.addEventListener('scroll', hideHover, { passive: true });
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
  main.addEventListener('mouseover', placeTip);
  main.addEventListener('focusin', placeTip);
  // Escape closes an open tooltip, as it would any other popup.
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && document.activeElement && document.activeElement.closest && document.activeElement.closest('.kd-tip')) document.activeElement.blur();
  });
  document.getElementById('kdRetry').addEventListener('click', load);

  syncForm();
  load();
}());
