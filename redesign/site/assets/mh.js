/* MoneyHoney · shared interactions. Everything here is progressive: without it the
   page is complete and readable. It never changes any text except to count a figure
   up to the exact string that was already there. */
(function () {
  'use strict';
  var motion = !(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
  var io = 'IntersectionObserver' in window;

  /* 1. Reading progress bar (decorative) */
  var bar = document.createElement('div');
  bar.className = 'mh-progress'; bar.setAttribute('aria-hidden', 'true');
  document.body.appendChild(bar);
  function progress() {
    var h = document.documentElement, max = h.scrollHeight - h.clientHeight;
    bar.style.setProperty('--p', max > 0 ? Math.min(1, h.scrollTop / max).toFixed(4) : 0);
  }
  addEventListener('scroll', progress, { passive: true }); addEventListener('resize', progress); progress();

  /* 2. Scroll reveal, staggered within each group */
  if (motion && io) {
    document.documentElement.classList.add('mh-anim');
    var groups = ['.linkgrid', '.ledger', '.pcards', '.steps', '.pdfs', '.facts', '.res-grid', '.close-steps', '.faq', '.sol-links'];
    groups.forEach(function (sel) {
      document.querySelectorAll(sel).forEach(function (g) {
        Array.prototype.forEach.call(g.children, function (el, i) { el.classList.add('reveal'); el.style.setProperty('--i', Math.min(i, 8)); });
      });
    });
    document.querySelectorAll('.headline, .vb-main > section > h2, main > h2, .page-home .section__head, .nextstep, .site-foot__warn').forEach(function (el) { el.classList.add('reveal'); });
    var seen = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); seen.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    document.querySelectorAll('.reveal').forEach(function (el) { seen.observe(el); });
    /* anything already above the fold shows at once */
    requestAnimationFrame(function () {
      document.querySelectorAll('.reveal').forEach(function (el) {
        var r = el.getBoundingClientRect(); if (r.top < innerHeight && r.bottom > 0) el.classList.add('is-in');
      });
    });
  }

  /* 3. Range sliders: paint the filled part of the track */
  function paint(sl) {
    var lo = +sl.min || 0, hi = +sl.max || 100, v = +sl.value;
    sl.style.setProperty('--p', (hi > lo ? (v - lo) / (hi - lo) * 100 : 0).toFixed(2) + '%');
  }
  document.querySelectorAll('input[type=range]').forEach(function (sl) {
    paint(sl);
    sl.addEventListener('input', function () { paint(sl); });
    var box = sl.dataset.for && document.getElementById(sl.dataset.for);
    if (box) { box.addEventListener('input', function () { paint(sl); }); box.addEventListener('change', function () { paint(sl); }); }
  });
  document.querySelectorAll('[data-presets] button, [data-picker] button').forEach(function (b) {
    b.addEventListener('click', function () { setTimeout(function () { document.querySelectorAll('input[type=range]').forEach(paint); }, 0); });
  });

  /* 4. A figure that changes gets a brief colour tick */
  if (motion && 'MutationObserver' in window) {
    var tick = new MutationObserver(function (ms) {
      ms.forEach(function (m) {
        var el = m.target.nodeType === 3 ? m.target.parentElement : m.target;
        el = el && el.closest('.stat__value, .m');
        if (!el) return;
        el.classList.remove('is-tick'); void el.offsetWidth; el.classList.add('is-tick');
      });
    });
    document.querySelectorAll('.stat__value, .m').forEach(function (el) { tick.observe(el, { characterData: true, childList: true, subtree: true }); });
  }

  /* 5. The sticky result bar stays out of the way while the calculator itself is on screen */
  var gap = document.querySelector('.gapbar'), rail = document.getElementById('where-you-stand');
  if (gap && rail && io) {
    var watch = new IntersectionObserver(function (es) { gap.classList.toggle('is-hidden', es[0].isIntersecting); }, { threshold: 0.15 });
    watch.observe(rail);
  }

  /* 6. Home page fact tiles count up to the exact figure already printed */
  if (motion && io) {
    document.querySelectorAll('.page-home .facts .stat__value').forEach(function (el) {
      var final = el.textContent, n = final.replace(/,/g, '');
      if (!/^\d+$/.test(n)) return;
      var end = +n, obs = new IntersectionObserver(function (es) {
        if (!es[0].isIntersecting) return;
        obs.disconnect();
        var t0 = performance.now();
        (function step(t) {
          var k = Math.min(1, (t - t0) / 900), v = Math.round(end * (1 - Math.pow(1 - k, 3)));
          el.textContent = k < 1 ? v.toLocaleString('en-IN') : final;
          if (k < 1) requestAnimationFrame(step);
        })(t0);
      });
      obs.observe(el);
    });
  }
})();
