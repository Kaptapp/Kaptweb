/* Kapture site · kaptapp.com
   Minimal progressive enhancement. The page is fully readable without this file. */

(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.add('js');

  /* ---- Current year in the footer ---- */
  var year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

  /* ---- Header gets a background once the page is scrolled ---- */
  var header = document.getElementById('siteHeader');
  if (header) {
    var setStuck = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    setStuck();
    window.addEventListener('scroll', setStuck, { passive: true });
  }

  /* ---- Unreleased destinations ----
     The Chrome extension is live, so those buttons are ordinary links. The Mac
     app is not released, so `data-mac-pending` still renders it as a disabled
     control that announces why. */
  var pendingStates = [
    { attr: 'data-mac-pending', title: 'The Kapture Mac app is coming soon' },
    { attr: 'data-win-pending', title: 'The Kapture Windows app is coming soon' }
  ];

  pendingStates.forEach(function (state) {
    var nodes = document.querySelectorAll('[' + state.attr + ']');
    Array.prototype.forEach.call(nodes, function (el) {
      el.setAttribute('aria-disabled', 'true');
      /* The aria-label is already localised in the markup, so the tooltip uses
         it rather than the English fallback baked in above. */
      el.setAttribute('title', el.getAttribute('aria-label') || state.title);
      el.addEventListener('click', function (event) {
        // Let the final CTA anchor scroll to its own explanatory note; block the rest.
        if (el.getAttribute('href') === '#cta' && el.closest('.cta-band')) {
          event.preventDefault();
        }
      });
    });
  });

  /* ---- Kapture for Chrome: replay the real capture workflow ----
     One composition, six phases. Full page is selected, Capture page runs the
     sweep, the file is kept; then the panel switches to Select area, a region
     is dragged, and only that region is captured. */
  var cap = document.getElementById('capDemo');
  var capPoints = document.getElementById('capPoints');

  /* The two points below the composition name the state it is in. Colour only,
     so stepping the animation never moves anything. */
  var capMark = function (name) {
    if (!capPoints) return;
    var mode = (name === 'area' || name === 'draw' || name === 'crop') ? 'area' : 'full';
    Array.prototype.forEach.call(capPoints.querySelectorAll('li[data-mode]'), function (li) {
      li.classList.toggle('is-active', li.getAttribute('data-mode') === mode);
    });
  };

  if (cap) {
    var capStill = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var capPhases = [
      { name: 'full', hold: 2000 },
      { name: 'scan', hold: 2300 },
      { name: 'kept', hold: 1500 },
      { name: 'area', hold: 1900 },
      { name: 'draw', hold: 2100 },
      { name: 'crop', hold: 2000 }
    ];

    if (capStill) {
      // No sweep and no drag: hold the finished Select area state, which still
      // shows both the panel and what it produced.
      cap.setAttribute('data-phase', 'crop');
      capMark('crop');
    } else {
      var capAt = 0;
      var capStep = function () {
        capAt = (capAt + 1) % capPhases.length;
        cap.setAttribute('data-phase', capPhases[capAt].name);
        capMark(capPhases[capAt].name);
        window.setTimeout(capStep, capPhases[capAt].hold);
      };
      capMark(capPhases[0].name);
      window.setTimeout(capStep, capPhases[0].hold);
    }
  }

  /* ---- Kapture Pro: the six controls switch the app to a real state ----
     Each control names a state; the component re-renders to it. No overlay,
     no highlight box: the screen itself changes. */
  var kp = document.getElementById('kpDemo');
  var kpPoints = document.getElementById('kpPoints');

  if (kp && kpPoints) {
    var kpItems = Array.prototype.slice.call(kpPoints.querySelectorAll('li[data-state]'));
    var kpStill = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var kpTimer = null;
    var kpAt = 2;   // start on the plain library

    var kpShow = function (i) {
      kpAt = i;
      kp.setAttribute('data-state', kpItems[i].getAttribute('data-state'));
      kpItems.forEach(function (li, n) { li.classList.toggle('is-active', n === i); });
    };
    var kpCycle = function () {
      if (kpStill) return;
      kpTimer = window.setInterval(function () { kpShow((kpAt + 1) % kpItems.length); }, 4200);
    };
    var kpHold = function () { window.clearInterval(kpTimer); kpTimer = null; };

    kpItems.forEach(function (li, i) {
      var t = li.querySelector('button') || li;
      ['mouseenter', 'focus', 'click'].forEach(function (evt) {
        t.addEventListener(evt, function () { kpHold(); kpShow(i); });
      });
    });
    kpPoints.addEventListener('mouseleave', function () { if (!kpTimer) kpCycle(); });

    kpShow(kpAt);
    kpCycle();
  }

  /* ---- Smart: one workspace, five tools ----
     The app keeps a single indicator that travels between segments, measured
     rather than assumed so a translated label of any width still fits. Only
     the region under the description swaps; the shell never moves. */
  var sm = document.getElementById('smDemo');
  var smTabs = document.getElementById('smTabs');
  var smPoints = document.getElementById('smPoints');

  if (sm && smTabs && smPoints) {
    var smSegs = Array.prototype.slice.call(smTabs.querySelectorAll('b[data-tool]'));
    var smThumb = smTabs.querySelector('.sm-thumb');
    var smStill = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var smTimer = null;
    var smAt = 0;

    var smPlace = function () {
      var on = smSegs[smAt];
      if (!on || !smThumb) return;
      smThumb.style.setProperty('--sm-w', on.offsetWidth + 'px');
      smThumb.style.setProperty('--sm-x', on.offsetLeft - smTabs.scrollLeft + 'px');
      if (!smTabs.classList.contains('sm-ready')) {
        window.requestAnimationFrame(function () { smTabs.classList.add('sm-ready'); });
      }
    };

    var smShow = function (i) {
      smAt = i;
      var name = smSegs[i].getAttribute('data-tool');
      sm.setAttribute('data-tool', name);
      smSegs.forEach(function (b, n) { b.classList.toggle('is-on', n === i); });
      Array.prototype.forEach.call(smPoints.querySelectorAll('li[data-tool]'), function (li) {
        li.classList.toggle('is-active', li.getAttribute('data-tool') === name);
      });
      smPlace();
    };

    var smCycle = function () {
      if (smStill) return;
      smTimer = window.setInterval(function () { smShow((smAt + 1) % smSegs.length); }, 4200);
    };
    var smHold = function () { window.clearInterval(smTimer); smTimer = null; };

    Array.prototype.forEach.call(smPoints.querySelectorAll('li[data-tool]'), function (li, i) {
      var t = li.querySelector('button') || li;
      ['mouseenter', 'focus', 'click'].forEach(function (evt) {
        t.addEventListener(evt, function () { smHold(); smShow(i); });
      });
    });
    smPoints.addEventListener('mouseleave', function () { if (!smTimer) smCycle(); });

    smShow(0);
    // Measure once the webfont has settled, so the indicator matches the drawn text.
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(smPlace);
    window.addEventListener('load', smPlace);
    if ('ResizeObserver' in window) new ResizeObserver(smPlace).observe(smTabs);
    smCycle();
  }

  /* ---- Languages: the selector changes the interface around it ----
     The words themselves live in CSS custom properties, so switching language
     is one attribute change and the whole interface crossfades as one group,
     the way the apps do it. Nothing here is translated by the website. */
  var lg = document.getElementById('lgDemo');
  var lgPick = document.getElementById('lgPick');

  if (lg && lgPick) {
    var lgItems = Array.prototype.slice.call(lgPick.querySelectorAll('li[data-lang]'));
    var lgStill = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var lgTimer = null, lgFade = null, lgAt = 0;

    var lgShow = function (i) {
      lgAt = i;
      var code = lgItems[i].getAttribute('data-lang');
      lgItems.forEach(function (li, n) { li.classList.toggle('is-active', n === i); });
      if (lgStill) { lg.setAttribute('data-lang', code); return; }
      // Out, swap, back in: the interface never shows two languages at once.
      lg.classList.add('is-turning');
      window.clearTimeout(lgFade);
      lgFade = window.setTimeout(function () {
        lg.setAttribute('data-lang', code);
        lg.classList.remove('is-turning');
      }, 220);
    };

    var lgCycle = function () {
      if (lgStill) return;
      lgTimer = window.setInterval(function () { lgShow((lgAt + 1) % lgItems.length); }, 3600);
    };
    var lgHold = function () { window.clearInterval(lgTimer); lgTimer = null; };

    lgItems.forEach(function (li, i) {
      var t = li.querySelector('button') || li;
      ['mouseenter', 'focus', 'click'].forEach(function (evt) {
        t.addEventListener(evt, function () { lgHold(); lgShow(i); });
      });
    });
    lgPick.addEventListener('mouseleave', function () { if (!lgTimer) lgCycle(); });

    lgShow(0);
    lgCycle();
  }

  /* ---- Common questions: progressive enhancement into an accordion ----
     The markup ships as eight plain question and answer pairs, so the answers
     are in the static HTML for anyone reading it without scripting, and for
     search and answer engines. This upgrades that markup in place: the heading
     text becomes a real button, the answer becomes a labelled region, and the
     pair collapses. Nothing is fetched, injected or removed from the DOM. */
  var faq = document.querySelector('#faq .faq');

  if (faq) {
    var faqItems = Array.prototype.slice.call(faq.querySelectorAll('.faq-q'));
    var faqStill = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var faqOpen = null;

    var faqSet = function (item, open) {
      item.classList.toggle('is-open', open);
      item.querySelector('.faq-btn').setAttribute('aria-expanded', open ? 'true' : 'false');
    };

    faqItems.forEach(function (item, i) {
      var h = item.querySelector('h3');
      var a = item.querySelector('p');
      if (!h || !a) return;

      var qId = 'faq-q' + (i + 1);
      var aId = 'faq-a' + (i + 1);

      // The heading keeps its level and its text; the button sits inside it, so
      // the document outline is unchanged and the control is still a control.
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'faq-btn';
      btn.id = qId;
      btn.setAttribute('aria-expanded', 'false');
      btn.setAttribute('aria-controls', aId);
      while (h.firstChild) btn.appendChild(h.firstChild);

      var mark = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      mark.setAttribute('class', 'i faq-mark');
      mark.setAttribute('aria-hidden', 'true');
      var use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
      use.setAttribute('href', '#i-caret');
      mark.appendChild(use);
      btn.appendChild(mark);
      h.appendChild(btn);

      // A wrapper the answer can be measured against, so the reveal animates
      // without anyone having to know how tall the text is.
      var panel = document.createElement('div');
      panel.className = 'faq-a';
      panel.id = aId;
      panel.setAttribute('role', 'region');
      panel.setAttribute('aria-labelledby', qId);
      var inner = document.createElement('div');
      inner.className = 'faq-a-in';
      a.parentNode.insertBefore(panel, a);
      inner.appendChild(a);
      panel.appendChild(inner);

      btn.addEventListener('click', function () {
        var isOpen = btn.getAttribute('aria-expanded') === 'true';
        // One at a time: opening a question closes whichever was open.
        if (faqOpen && faqOpen !== item) faqSet(faqOpen, false);
        faqSet(item, !isOpen);
        faqOpen = isOpen ? null : item;
      });
    });

    // Only now, once every pair has been upgraded, does the CSS start
    // collapsing them. Without this the answers would vanish for the moment
    // between first paint and this script running.
    faq.setAttribute('data-acc', faqStill ? 'still' : 'on');
  }

  /* ---- Reveal sections on scroll ---- */
  var reveals = document.querySelectorAll('.reveal');

  if (!('IntersectionObserver' in window)) {
    Array.prototype.forEach.call(reveals, function (el) {
      el.classList.add('is-visible');
    });
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });

  Array.prototype.forEach.call(reveals, function (el) {
    observer.observe(el);
  });

  /* Failsafe: reveal anything still hidden shortly after load, so a stalled
     observer can never leave the page looking blank. */
  window.addEventListener('load', function () {
    window.setTimeout(function () {
      Array.prototype.forEach.call(reveals, function (el) {
        el.classList.add('is-visible');
      });
    }, 1200);
  });
})();
