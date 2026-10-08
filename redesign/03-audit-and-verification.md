# MoneyHoney redesign: Phase 4 audit and Phase 5 verification

Page: `redesign/site/index.html` (home). Direction: A, "The Ledger". Date: 8 Oct 2026.

## Phase 4: audit

Method: headless Chromium at 390, 768 and 1280px; axe-core 4.10.2 with WCAG 2.0/2.1/2.2 A+AA and best-practice rules; contrast computed per WCAG formula; tap targets measured from the DOM.

| Check | Result |
|---|---|
| Horizontal overflow | None at 390 / 768 / 1280 |
| Tap targets (all 50 links) | All at least 44px tall and 24px wide |
| Focus states | Visible 3px orange ring with white gap on every link; navy-ground variant on header and footer |
| Contrast, body text #141A3B on white | 16.9:1 |
| Contrast, headings #1B2666 on white | 13.9:1 |
| Contrast, meta #5D637C on white / on tint | 5.9:1 / 5.4:1 |
| Contrast, footer identity #C9CFEA on navy | 9.0:1 |
| Contrast, demo strip #B54708 on #FFFAEB | 5.2:1 |
| Contrast, CTA white on orange #E8511A | 3.7:1 (passes AA for large text; CTA set at 19px/700 so it qualifies) |
| Images without alt | 0 (no raster images; logo SVG has role="img" and aria-label) |
| Landmarks | header, nav[Main], main, footer, nav[Footer]; demo notice moved inside header so all content is in a landmark |
| Forms | None on this page |
| Reduced motion | Transitions disabled under prefers-reduced-motion |
| axe-core violations | 0 after fix (1 before: "region" on the demo strip) |
| Mobile performance | No JavaScript; 33 KB HTML; three Google Fonts families with font-display: swap and preconnect; original 57 KB base64 Inter removed |

Fixes applied during audit: demo strip moved into the header landmark; desktop nav redesigned as a full-width second row so nine links wrap predictably; stat values set to nowrap and 24px on phones so "31 Aug 2026" stays on one line.

Not changed because of the content lock (listed as suggestions instead): no "Skip to content" link was added, since it would introduce new visible text.

## Phase 5: content verification

Method: both files parsed with Python's html.parser; style, script and SVG geometry excluded; compared title, lang, meta tags, canonical, JSON-LD, aria-labels, every href in order, and the full visible text stream in order.

| Item | Original | New | Status |
|---|---|---|---|
| `<title>` | 1 | 1 | Match |
| meta + lang + canonical | 15 | 15 (+1 theme-color, not text) | Match |
| JSON-LD | 1 block | 1 block | Match, byte for byte |
| aria-labels (logo link, logo SVG, 2 navs) | 4 | 4 | Match |
| hrefs, in order | 53 | 53 | Match |
| Visible text fragments | 96 | 96 | Match |
| Fragments missing | | 0 | |
| Fragments altered | | 0 | |
| Fragments added | | 0 | |

Result: 100% match. Compliance text (demo notice, lede sentence, footer identity line, both risk warnings, JSON-LD description) is verbatim and rendered at 13px or larger with AA contrast.

Verification script: run `python3 -I verify.py redesign/original/index.html redesign/site/index.html` (script in session scratchpad; copy kept at `redesign/tools/verify.py`).
