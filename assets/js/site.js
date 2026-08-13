/* Muneris — progressive enhancement only. The site works fully without JS. */
(function () {
  'use strict';

  /* Mobile navigation ----------------------------------------------------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-nav');

  function setNav(open) {
    if (!nav || !toggle) return;
    nav.hidden = !open;
    toggle.setAttribute('aria-expanded', String(open));
  }

  function syncNavForViewport() {
    if (!nav) return;
    var isMobile = window.matchMedia('(max-width: 820px)').matches;
    if (isMobile) {
      setNav(false);
    } else {
      nav.hidden = false;
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
    }
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      setNav(nav.hidden);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !nav.hidden) {
        setNav(false);
        toggle.focus();
      }
    });
    window.addEventListener('resize', syncNavForViewport);
    syncNavForViewport();
  }

  /* Current year in the footer -------------------------------------------- */
  var year = document.querySelector('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());

  /* Reveal on scroll ------------------------------------------------------- */
  var targets = document.querySelectorAll('.reveal');
  if (!targets.length) return;

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced || !('IntersectionObserver' in window)) {
    targets.forEach(function (el) { el.classList.add('is-visible'); });
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });

  targets.forEach(function (el) { observer.observe(el); });
})();
