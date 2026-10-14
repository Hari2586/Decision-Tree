const { chromium } = require('playwright-core');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  for (const vp of [{width:1440,height:900},{width:390,height:844}]) {
    const page = await browser.newPage({ viewport: vp });
    const errs = []; page.on('pageerror', e => errs.push(e.message)); page.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
    await page.goto('http://127.0.0.1:4500/', { waitUntil: 'networkidle' });
    await page.addScriptTag({ url: 'https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js' });
    const axe = await page.evaluate(async () => { const r = await axe.run(document, { runOnly: ['wcag2a','wcag2aa','best-practice'] }); return r.violations.map(v => v.id + ' (' + v.impact + ') x' + v.nodes.length + ': ' + v.nodes.slice(0,2).map(n => n.target.join(' ')).join(' | ')); });
    const ovf = await page.evaluate(() => { const w = document.documentElement.clientWidth; return [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > w + 1 && getComputedStyle(e).position !== 'fixed' && !e.closest('[data-sc-pan]'); }).slice(0,5).map(e => e.tagName + '.' + e.className); });
    // hybrid plate opacity at act 4 p=0.6
    const op = await page.evaluate(async () => { const a = document.getElementById('room-asset'); const top = a.getBoundingClientRect().top + scrollY; scrollTo(0, top + (a.offsetHeight - innerHeight) * 0.6); await new Promise(r => setTimeout(r, 700)); const pl = [...a.querySelectorAll('.card--navy')]; return pl.map(p => getComputedStyle(p).opacity + ' ' + p.querySelector('[data-sc-count]').textContent); });
    const gauge = await page.evaluate(async () => { const a = document.getElementById('room-asset'); const top = a.getBoundingClientRect().top + scrollY; scrollTo(0, top + (a.offsetHeight - innerHeight) * 0.98); await new Promise(r => setTimeout(r, 700)); return document.querySelector('.shelf__total').getAttribute('data-n') + ' full=' + document.querySelector('.shelf').classList.contains('is-full'); });
    // tab order: first 14 focus stops
    await page.evaluate(() => scrollTo(0, 0)); const stops = [];
    for (let i = 0; i < 14; i++) { await page.keyboard.press('Tab'); stops.push(await page.evaluate(() => { const e = document.activeElement; return e.tagName + (e.className ? '.' + e.className.split(' ')[0] : '') + ':' + (e.textContent.trim().slice(0,18) || e.getAttribute('aria-labelledby') || ''); })); }
    const railOverflow = await page.evaluate(() => document.querySelector('.rail').scrollWidth - innerWidth);
    const sw = await page.evaluate(() => document.documentElement.scrollWidth + '/' + document.documentElement.clientWidth); console.log(JSON.stringify({ vp, errs, axe, sw, gauge, railOverflow }));
    await page.close();
  }
  await browser.close();
})();
