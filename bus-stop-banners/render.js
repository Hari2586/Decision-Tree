// Renders each banner to a preview PNG and a true-size print PDF.
// Usage: node render.js   (needs playwright; banners use 100px = 1 foot)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const FILES = ['front-15x4', 'side-left-4x4', 'side-right-4x4', 'backdrop-12x4'];
const PX_PER_FT = 100;
const CSS_PX_PER_IN = 96;

(async () => {
  const browser = await chromium.launch();
  fs.mkdirSync(path.join(__dirname, 'print'), { recursive: true });
  fs.mkdirSync(path.join(__dirname, 'preview'), { recursive: true });
  for (const name of FILES) {
    const url = 'file://' + path.join(__dirname, name + '.html');
    const page = await browser.newPage({ deviceScaleFactor: 2, viewport: { width: 1600, height: 500 } });
    await page.goto(url, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const banner = page.locator('.banner');
    await banner.screenshot({ path: path.join(__dirname, 'preview', name + '.png') });

    const { w, h } = await page.evaluate(() => ({ w: +document.body.dataset.w, h: +document.body.dataset.h }));
    const inW = (w / PX_PER_FT) * 12;
    const inH = (h / PX_PER_FT) * 12;
    const zoom = (inW * CSS_PX_PER_IN) / w;
    await page.emulateMedia({ media: 'print' });
    await page.addStyleTag({ content: `@page { size: ${inW}in ${inH}in; margin: 0 } .banner { zoom: ${zoom}; }` });
    await page.pdf({ path: path.join(__dirname, 'print', name + '.pdf'), width: `${inW}in`, height: `${inH}in`,
      printBackground: true, pageRanges: '1' });
    console.log(name, `${inW}x${inH}in`, 'zoom', zoom.toFixed(2));
    await page.close();
  }
  await browser.close();
})();
