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

  /* ---- Store CTAs: unavailable until each destination exists ----
     The markup ships no fake links. `data-store-pending` covers the Chrome Web
     Store listing, `data-mac-pending` the unreleased Mac app. Both render as
     disabled controls that announce why. */
  var pendingStates = [
    { attr: 'data-store-pending', title: 'Kapture is in Chrome Web Store review' },
    { attr: 'data-mac-pending',   title: 'The Kapture Mac app is coming soon' }
  ];

  pendingStates.forEach(function (state) {
    var nodes = document.querySelectorAll('[' + state.attr + ']');
    Array.prototype.forEach.call(nodes, function (el) {
      el.setAttribute('aria-disabled', 'true');
      el.setAttribute('title', state.title);
      el.addEventListener('click', function (event) {
        // Let the final CTA anchor scroll to its own explanatory note; block the rest.
        if (el.getAttribute('href') === '#cta' && el.closest('.cta-band')) {
          event.preventDefault();
        }
      });
    });
  });

  /* ---- Hero mock: one desktop composition, scaled to fit ----
     Kapture only runs on the desktop, so the mock never reflows into a phone
     layout. It is laid out at its design width and scaled down as a unit, the
     way a real screenshot of a desktop window would be. */
  var scaler = document.querySelector('.product-scaler');
  var mock = scaler && scaler.querySelector('.window');

  if (scaler && mock) {
    var DESIGN_WIDTH = 1040;
    var fitMock = function () {
      var available = scaler.clientWidth;
      if (!available) return;
      var factor = Math.min(1, available / DESIGN_WIDTH);
      mock.style.transform = factor === 1 ? 'none' : 'scale(' + factor + ')';
      // offsetHeight is the untransformed layout height, so scale it too.
      scaler.style.height = Math.round(mock.offsetHeight * factor) + 'px';
    };

    fitMock();
    window.addEventListener('resize', fitMock);
    window.addEventListener('orientationchange', fitMock);
    window.addEventListener('load', fitMock);
  }

  /* ---- Hero panel demo: alternate the extension's light and dark themes ---- */
  var panelDemo = document.getElementById('panelDemo');
  var stillMotion = window.matchMedia
    ? window.matchMedia('(prefers-reduced-motion: reduce)')
    : { matches: false };

  if (panelDemo && !stillMotion.matches) {
    window.setInterval(function () {
      panelDemo.classList.toggle('is-dark');
    }, 4200);
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
