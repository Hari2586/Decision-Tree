# MoneyHoney redesign: Phase 4 audit and Phase 5 verification

Chosen direction: B, "Clear Glass". Final page: `redesign/site/index.html`. Direction A is archived at `redesign/alternatives/direction-a-ledger/index.html`. Both share the same HTML body; only the stylesheet and font link differ. Date: 8 Oct 2026.

Direction B results: no overflow at 390/768/1280; all 50 links at least 44px tall; 0 axe-core violations; fonts Manrope and Figtree loaded; content verification 100% match (same 96 fragments, 53 hrefs, identical head). Card icons are CSS-only masked SVGs on pseudo-elements, so no text or DOM nodes were added.

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

Verification script: run `python3 -I redesign/tools/verify.py redesign/original/index.html redesign/site/index.html` (script in session scratchpad; copy kept at `redesign/tools/verify.py`).

---

## Batch 2: Solutions hub and three solution pages (8 Oct 2026)

Method as above, plus a scripted read-through at phone and desktop widths with wheel scrolling so the scroll-reveal animations are exercised, and JavaScript error capture.

| Page | Overflow | Targets under 44px | axe violations | JS errors | Content match |
|---|---|---|---|---|---|
| Home (moved to shared assets) | None | 0 | 0 | 0 | 100% (96 fragments, 53 hrefs) |
| Solutions hub | None | 0 | 0 | 0 | 100% (52 fragments) |
| Child Education | None | 0, excluding inline citation markers | 0 | 0 | 100% (337 fragments) |
| Emergency Fund | None | 0, excluding inline citation markers | 0 | 0 | 100% (370 fragments) |
| EMI Management | None | 0, excluding inline citation markers | 0 | 0 | 100% (395 fragments) |

Citation markers such as [1] are inline links inside sentences. WCAG 2.2 target size exempts in-text links; their tap area was still enlarged from about 12 by 13px to 22 by 29px with padding.

Fixes applied in this batch: breadcrumb links raised to 44px; "Illustration" and "Matches Your Numbers" badges recoloured to 5.3:1 on their tint; demo notice moved inside the header landmark on every page (layout move, text unchanged); segmented buttons fill their row when they wrap on phones.

Body identity: for the hub and the three solution pages the body markup is byte-identical to the original apart from the body tag's class and the demo-notice move (asserted by `tools/build.py`). Calculator scripts, form fields, ids and data attributes are therefore unchanged and the calculators work as before.

Interactions and animation added, all progressive and reduced-motion aware: reading progress bar; staggered scroll reveal for cards, steps, FAQs and documents; filled slider tracks; a colour tick on any figure that recalculates; the headline figure count-up and chart draw-in from the original scripts, restyled; a floating result bar on phones that hides while the calculator is on screen; hover lifts and animated chevrons; the matching goal-table row highlighted with an orange edge and a popping badge.

### Interactive charts (added 8 Oct 2026)

- **Calculator chart in the rail.** One invisible hit zone per year. Hover, tap or keyboard-focus a year to see a tooltip with the year and both series, named from the chart's own legend and valued from the page's own calculator (`window.mhCalc`). The hovered year's bars keep full colour with an orange outline while the others fade. Zones rebuild after every recalculation. Each legend item is a toggle button that hides or shows its series.
- **Story charts.** Each bar is focusable with an accessible name taken from the chart's existing aria-label (label and value). Hover, tap or focus turns the bar orange, fades the rest and shows the label and value in a tooltip. All 13 charts across the three pages were checked: aria items and bars line up one to one.
- Tooltips are built with DOM text nodes, never HTML strings, and hide on scroll, resize, or a tap outside the chart. No visible page text was added; the tooltips compose existing legend labels, table headers and the figures already shown in the year-by-year table.
- Re-audit after the change: 0 axe violations on all three pages, no JavaScript errors, content match 100%.

---

## Batch 3: Scheme Details, Explore Mutual Funds, MF/SIF Screener (8 Oct 2026)

These are application pages whose markup is largely drawn by their own scripts (filters, result cards, a 476-column grid, interactive NAV and return charts). Their bodies and scripts are kept byte for byte. Their own page CSS is kept too, and now resolves through a compatibility layer in `assets/mh.css` that maps every original design token to the Clear Glass palette, type and radii. On top of that, body-class-scoped overrides restyle the identity band, NAV panel, fact tiles, section nav, tabs, period pills, calculator output, filter rail, result cards, compare bar, screener toolbar, grid header and boot screen.

| Page | Body size | Overflow | axe violations after fixes | JS errors | Content match |
|---|---|---|---|---|---|
| Scheme Details (360 ONE Flexicap Fund) | 312 KB | None | 2, both pre-existing markup (see below) | 0 | 100% |
| Explore Mutual Funds | 867 KB | None | 1, pre-existing markup | 0 | 100% |
| MF/SIF Screener | 774 KB | None | 0 | 0 | 100% |

Fixes applied at runtime by `assets/mh.js`, with no visible change: the main content wrapper gets the main landmark where a page has none; the identity band, page head and section nav become named landmarks using the page's own h1; page-level disclaimer footers are wrapped as named regions so the site footer stays the only contentinfo; compare checkboxes drawn by the scripts get an accessible name from their row's scheme name; scrollable tables, ledgers and chart panels are keyboard focusable with a visible focus ring. Fixes in CSS: loss figures darkened to 5.9:1 on white and AA on the highlighted row; the active performance tab now has white text on its navy pill (the page CSS had overridden it); the info button beside Instant Redemption enlarged to 32px; pills, collection chips and filter buttons reach 44px on touch devices.

Pre-existing markup items not fixed because the body is locked (listed as suggestions): the lumpsum returns table has an empty first header cell; the calculator headings are h4 directly under h2 on the scheme page, and the filter group headings are h4 under h1 on Explore. Small targets that remain are inline scheme-name links inside table rows and cards, which WCAG exempts as in-text links, and 36px period pills inside the pill groups on mouse devices (44px on touch).

---

## Revision: Ledger-style buttons and smaller radii (8 Oct 2026)

Per your direction, Clear Glass keeps its layout, colour and type, but buttons now follow Direction A: flat and rectangular with 4px corners, orange fill with white text for the primary action, white with a navy outline for the secondary (filling navy on hover), and a plain navy text link for the tertiary. Corner radii were reduced throughout: controls 4px, chips, inputs and segmented groups 6px, cards 8px, panels 10px. No pill shapes remain; only status dots and slider thumbs are circular. Shadows were softened to match.

Re-audit after the revision on all eight pages: no overflow, 0 axe violations on six pages and only the three pre-existing markup items on the scheme and Explore pages, no JavaScript errors, content match 100% everywhere. The "Edit Your Numbers" button in the phone result bar was raised to 44px.
