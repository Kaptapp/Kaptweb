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
    { attr: 'data-mac-pending', title: 'The Kapture Mac app is coming soon' }
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
