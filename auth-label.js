/* Header account button: "Sign in" when signed out, "My Account" when signed
   in. Signed in means the account page has a session stored in this browser
   (localStorage "kapture.session", written and removed only by /account/).
   This script is loaded directly after the button, so the label is set
   before the header is first painted: no flash, no layout shift. It only
   chooses a label; it grants nothing. */
(function () {
  'use strict';

  function signedIn() {
    try {
      var s = JSON.parse(localStorage.getItem('kapture.session') || 'null');
      return !!(s && (s.refresh_token || s.access_token));
    } catch (e) { return false; }
  }

  function apply() {
    var on = signedIn();
    var links = document.querySelectorAll('a[data-label-in][data-label-out]');
    for (var i = 0; i < links.length; i++) {
      var text = links[i].getAttribute(on ? 'data-label-in' : 'data-label-out');
      if (links[i].textContent !== text) links[i].textContent = text;
    }
  }

  apply();
  if (!window.kaptureAuthLabel) {
    window.kaptureAuthLabel = apply;
    // Signing in or out in another tab, and pages restored from the back-forward cache.
    window.addEventListener('storage', function (e) { if (e.key === null || e.key === 'kapture.session') apply(); });
    window.addEventListener('pageshow', apply);
  }
}());
