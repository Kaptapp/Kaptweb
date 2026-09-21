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
      el.setAttribute('title', state.title);
      el.addEventListener('click', function (event) {
        // Let the final CTA anchor scroll to its own explanatory note; block the rest.
        if (el.getAttribute('href') === '#cta' && el.closest('.cta-band')) {
          event.preventDefault();
        }
      });
    });
  });

  /* ---- Six benefits, spotlit on the real library screenshot ----
     Each point carries the region it describes as data-spot="x,y,w,h" in
     percentages of that capture. Hover or focus takes over; otherwise it
     cycles. Nothing moves when the visitor prefers reduced motion. */
  var spotlight = document.getElementById('proSpotlight');

  if (spotlight) {
    var box = spotlight.querySelector('.spotlight-box');
    var items = Array.prototype.slice.call(spotlight.querySelectorAll('li[data-spot]'));
    var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var timer = null;
    var at = 0;

    var light = function (i) {
      at = i;
      var parts = items[i].getAttribute('data-spot').split(',');
      box.style.left = parts[0] + '%';
      box.style.top = parts[1] + '%';
      box.style.width = parts[2] + '%';
      box.style.height = parts[3] + '%';
      spotlight.classList.add('is-lit');
      items.forEach(function (li, n) { li.classList.toggle('is-active', n === i); });
    };

    var cycle = function () {
      if (still) return;
      timer = window.setInterval(function () { light((at + 1) % items.length); }, 3200);
    };
    var hold = function () { window.clearInterval(timer); timer = null; };

    items.forEach(function (li, i) {
      var trigger = li.querySelector('button') || li;
      trigger.addEventListener('mouseenter', function () { hold(); light(i); });
      trigger.addEventListener('focus', function () { hold(); light(i); });
      trigger.addEventListener('click', function () { hold(); light(i); });
    });
    spotlight.addEventListener('mouseleave', function () { if (!timer) cycle(); });

    light(0);
    cycle();
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
