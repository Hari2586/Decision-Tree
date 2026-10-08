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

  /* 7. Interactive charts: hover, tap or focus a bar to read its value; click a legend item to hide a series.
        Values come from the page's own calculator (window.mhCalc) and from each chart's aria-label,
        so nothing is invented. */
  var tip = document.createElement('div');
  tip.className = 'mh-tip'; tip.setAttribute('role', 'tooltip'); tip.hidden = true;
  document.body.appendChild(tip);
  function tipShow(title, rows, x, y) {
    tip.textContent = '';
    if (title) { var b = document.createElement('b'); b.textContent = title; tip.appendChild(b); }
    rows.forEach(function (r) {
      var line = document.createElement('span');
      if (r[2]) { var sw = document.createElement('i'); sw.style.background = r[2]; line.appendChild(sw); }
      var l = document.createElement('em'); l.textContent = r[0]; line.appendChild(l);
      var v = document.createElement('strong'); v.textContent = r[1]; line.appendChild(v);
      tip.appendChild(line);
    });
    tip.hidden = false;
    var w = tip.offsetWidth, h = tip.offsetHeight, pad = 8;
    var left = Math.min(Math.max(x, w / 2 + pad), innerWidth - w / 2 - pad);
    var top = y - h - 12; if (top < pad) top = y + 18;
    tip.style.left = left + 'px'; tip.style.top = top + 'px';
    requestAnimationFrame(function () { tip.classList.add('is-show'); });
  }
  function tipHide() { tip.classList.remove('is-show'); tip.hidden = true; }
  addEventListener('scroll', tipHide, { passive: true }); addEventListener('resize', tipHide);
  document.addEventListener('pointerdown', function (e) { if (!e.target.closest('svg')) tipHide(); });
  function inr(v) { var n = Math.floor(Math.abs(v) + 0.5); return (v < 0 && n ? '-' : '') + '₹' + n.toLocaleString('en-IN'); }
  function centerTop(el) { var b = el.getBoundingClientRect(); return [b.left + b.width / 2, b.top]; }

  /* 7a. Story charts */
  document.querySelectorAll('svg.schart').forEach(function (svg) {
    var items = (svg.getAttribute('aria-label') || '').split('; ').map(function (p) {
      var parts = p.split(': '); var v = parts.pop(); return [parts.pop() || '', v];
    });
    var bars = svg.querySelectorAll('rect.chbar, rect.cbar');
    if (bars.length !== items.length) return;
    bars.forEach(function (r, i) {
      r.setAttribute('tabindex', '0'); r.setAttribute('role', 'img'); r.setAttribute('aria-label', items[i][0] + ': ' + items[i][1]);
      function on() { svg.classList.add('is-hover'); r.classList.add('is-on'); var c = centerTop(r); tipShow(items[i][0], [['', items[i][1]]], c[0], c[1] - (r.classList.contains('cbar') ? 26 : 0)); }
      function off() { svg.classList.remove('is-hover'); r.classList.remove('is-on'); tipHide(); }
      r.addEventListener('pointerenter', on); r.addEventListener('pointerleave', off);
      r.addEventListener('focus', on); r.addEventListener('blur', off);
      r.addEventListener('click', function (e) { e.stopPropagation(); if (tip.hidden) on(); else off(); });
    });
  });

  /* 7b. The calculator's chart in the rail: one hit zone per year, rebuilt after every recalculation */
  var chart = document.getElementById('chart');
  if (chart && window.mhCalc) {
    var legend = Array.prototype.map.call(chart.parentNode.querySelectorAll('.legend > span'), function (s) { return s.textContent.trim(); });
    var colors = ['var(--chart-3)', 'var(--chart-1)'];
    var yearHead = (function () { var th = document.querySelector('#ytab thead th'); return th ? th.textContent.trim() : 'Year'; })();
    function wire(r) {
      var old = chart.querySelector('.mh-hits'); if (old) old.remove();
      var bars = r.bars || []; if (!bars.length) return;
      var vb = chart.viewBox.baseVal, x0 = 8, slot = (vb.width - 8 - x0) / bars.length;
      var rects = chart.querySelectorAll(':scope > rect');
      var g = document.createElementNS('http://www.w3.org/2000/svg', 'g'); g.setAttribute('class', 'mh-hits');
      bars.forEach(function (b, k) {
        var h = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        h.setAttribute('x', (x0 + k * slot).toFixed(1)); h.setAttribute('y', 0); h.setAttribute('width', slot.toFixed(1)); h.setAttribute('height', vb.height);
        h.setAttribute('tabindex', '0'); h.setAttribute('role', 'img');
        h.setAttribute('aria-label', yearHead + ' ' + b[0] + ': ' + legend[0] + ' ' + inr(b[1]) + ', ' + legend[1] + ' ' + inr(b[2]));
        function on() {
          chart.classList.add('is-hover');
          [rects[2 * k], rects[2 * k + 1]].forEach(function (x) { if (x) x.classList.add('is-on'); });
          var tall = rects[2 * k + 1] || rects[2 * k] || h, c = centerTop(tall);
          tipShow(yearHead + ' ' + b[0], [[legend[0], inr(b[1]), colors[0]], [legend[1], inr(b[2]), colors[1]]], c[0], c[1]);
        }
        function off() { chart.classList.remove('is-hover'); chart.querySelectorAll('.is-on').forEach(function (x) { x.classList.remove('is-on'); }); tipHide(); }
        h.addEventListener('pointerenter', on); h.addEventListener('pointerleave', off);
        h.addEventListener('focus', on); h.addEventListener('blur', off);
        h.addEventListener('click', function (e) { e.stopPropagation(); if (tip.hidden) on(); else off(); });
        g.appendChild(h);
      });
      chart.appendChild(g);
    }
    try { wire(window.mhCalc({})); } catch (e) {}
    document.addEventListener('mh-calc', function (e) { wire(e.detail); });
    /* legend items toggle their series */
    chart.parentNode.querySelectorAll('.legend > span').forEach(function (sp, i) {
      sp.setAttribute('role', 'button'); sp.setAttribute('tabindex', '0'); sp.setAttribute('aria-pressed', 'true');
      function toggle() {
        var hidden = chart.classList.toggle(i ? 'hide-b' : 'hide-a');
        sp.setAttribute('aria-pressed', hidden ? 'false' : 'true');
      }
      sp.addEventListener('click', toggle);
      sp.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
    });
  }

  /* 8. Landmarks, names and keyboard reach for generated pages. Nothing visible changes:
        ARIA roles and names are taken from text already on the page, and scrollable
        panels become focusable so keyboard users can scroll them. */
  (function () {
    var body = document.body, h1 = document.querySelector('h1'), n = 0;
    function idOf(el) { if (!el.id) el.id = 'mh-lm-' + (++n); return el.id; }
    if (!document.querySelector('main, [role="main"]')) {
      var main = Array.prototype.find.call(body.children, function (el) { return el.matches('div.wrap') && el.querySelector('section'); });
      if (main) main.setAttribute('role', 'main');
    }
    Array.prototype.slice.call(body.children).forEach(function (el) {
      if (el.matches('header, nav, main, aside, footer.site-foot, script, style, [role], [hidden], [aria-hidden="true"], .mh-progress, .mh-tip') || !el.textContent.trim()) return;
      if (el.querySelector('main, aside, [role="main"]')) return;               /* already holds the main or a sidebar landmark */
      if (getComputedStyle(el).display === 'none') return;
      if (el.matches('.secnav')) {                                                /* section links: a navigation named after the page */
        el.setAttribute('role', 'navigation'); if (h1) el.setAttribute('aria-labelledby', idOf(h1)); return;
      }
      var label = el.querySelector('h1, h2, h3, h4, b, .t'); if (!label) return;
      if (el.tagName === 'FOOTER') {                                              /* a page footer cannot be a region itself: wrap it */
        var box = document.createElement('div'); box.setAttribute('role', 'region'); box.setAttribute('aria-labelledby', idOf(label));
        el.parentNode.insertBefore(box, el); box.appendChild(el); el.setAttribute('role', 'group'); return;
      }
      el.setAttribute('role', 'region'); el.setAttribute('aria-labelledby', idOf(label));
    });
    function enhance(root) {
      /* compare checkboxes drawn by the screener and explorer get the row's scheme name as their label */
      root.querySelectorAll('input[type=checkbox]:not([aria-label]):not([id])').forEach(function (box) {
        if (box.closest('label')) return;
        var row = box.closest('tr, .card, .nfo-card'), nm = row && row.querySelector('.nm, a, td'), cmp = document.querySelector('.cmpbar b');
        if (nm) box.setAttribute('aria-label', (cmp ? cmp.textContent.trim() + ' ' : '') + nm.textContent.trim());
      });
      /* panels that scroll sideways or inside themselves are reachable with the keyboard */
      root.querySelectorAll('.scrollx, .chart-wrap, .table-wrap, .ledger-scroll, .gw, .sx, .vlist').forEach(function (el) {
        if (!el.hasAttribute('tabindex')) el.setAttribute('tabindex', '0');
      });
    }
    enhance(document);
    var app = document.getElementById('app') || document.getElementById('list');
    if (app && 'MutationObserver' in window) new MutationObserver(function () { enhance(app); }).observe(app, { childList: true, subtree: true });
  })();
})();
