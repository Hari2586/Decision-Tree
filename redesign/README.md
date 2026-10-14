# MoneyHoney website redesign

Direction: **B, "Clear Glass"** (chosen 8 Oct 2026), revised the same day with Direction A's flat rectangular buttons and smaller corner radii. Pages rebuilt so far: home, Solutions hub, Child Education, Emergency Fund, EMI Management, Scheme Details, Explore Mutual Funds, MF/SIF Screener.

| Path | What it is |
|---|---|
| `site/` | The redesigned site. Deploy this folder. Relative links match the original URL structure. |
| `site/assets/mh.css` | The one stylesheet for every page (design tokens, components, animations). |
| `site/assets/mh.js` | Progressive interactions: reading progress bar, scroll reveal, slider track fill, figure "tick" on change, hiding the sticky result bar while the calculator is on screen, count-up on the home fact tiles, interactive charts (tooltips on hover, tap or focus; legend toggles). Pages are complete without it. |
| `site/index.html` | Home, now the scroll-craft build: a scroll-driven "gallery" page on the Direction B palette. Content verified at 100%. |
| `site/assets/scrollcraft.js`, `scrollcraft.css` | The scroll-craft engine (unmodified) that drives the home page acts. Other pages do not load it. |
| `site/solutions/index.html` | Solutions hub. |
| `site/solutions/<slug>/index.html` | Solution pages. Their calculator scripts are the originals, untouched. |
| `site/mutual-funds/scheme/`, `explore/`, `screener/` | Application pages. Built with `--keep-page-css`: their own CSS stays and resolves through the token compatibility layer in `mh.css`. |
| `original/` | The supplied pages, kept for verification, plus the sitemap index. |
| `alternatives/direction-a-ledger/` | Direction A home page, archived. |
| `inventory/*.md` | Phase 1 inventory per page, generated from the originals: every text fragment, link, label and meta tag in order, compliance rows marked. |
| `01-content-inventory.md` | Hand-written home page inventory with the compliance register. |
| `02-design-directions.html` | Phase 2 moodboard with both directions (historical). |
| `02-design-direction-final.html` | The final design direction and style guide as built: colour, type, buttons, radii, components, motion, compliance, developer handoff. |
| `03-audit-and-verification.md` | Phase 4 accessibility audit and Phase 5 content verification. |
| `04-home-page-versions.html` | Research summary and three alternative home page versions (Night Desk, Bento Board, Split Editorial) for comparison. |
| `versions/` | Alternative home pages: `v0-direction-b-home` (the previous static Direction B home, paths rewritten to `../../site/`), and V1 to V3 built by `tools/versions.py`. All content verified at 100%. |
| `scrollcraft/` | scroll-craft workspace: `FINGERPRINTS.md` (the build registry) and `builds/moneyhoney-home/` with `BRIEF.md`, the page, the engine copy and the contact sheets in `lab/`. |
| `tools/scrollcraft_home.py` | Generates the scroll-craft home from the original: `python3 tools/scrollcraft_home.py original/index.html <head fragment> site/assets/mh.css <out>`. Every string is lifted from the original by regex. |
| `tools/build.py` | Builds a page: keeps the body byte for byte (only the body tag gains a class and the demo notice moves inside the header landmark), swaps the head's embedded CSS for the shared assets. |
| `tools/verify.py` | Content verification: title, meta, JSON-LD, aria-labels, every href in order, the full visible text stream. |
| `tools/inventory.py` | Generates the per-page inventory tables. |

## Rebuilding a page

```
python3 redesign/tools/build.py <original.html> redesign/site/<path>/index.html <asset-prefix> <body-class>
python3 redesign/tools/verify.py <original.html> redesign/site/<path>/index.html
```

Asset prefix is `""` at the root, `../` one level down, `../../` two levels down. Body class is `page-home`, `page-hub`, `page-solution` (plus one of `variant-timeline`, `variant-stress`, `variant-paths`, and `sol-<slug>` for the headline watermark icon), `page-scheme`, `page-explore` or `page-screener`. Add `--keep-page-css` for pages that carry their own CSS after the design-system marker (scheme, explore, screener, calculators); the generator's token names keep working through the compatibility block at the end of `mh.css`.

## scroll-craft home

The skill lives in `.claude/skills/scroll-craft/`. Verify the home page by scrolling it, not by looking at it:

```
cd redesign/scrollcraft/builds/moneyhoney-home
node ../../../../.claude/skills/scroll-craft/scripts/serve.mjs --root . --port 4500 &
SCROLLCRAFT_CHROME=<path to chrome> node ../../../../.claude/skills/scroll-craft/scripts/shoot.mjs --url http://127.0.0.1:4500 --out lab/shots
```

Add `--width 390 --height 844` for the phone pass and `--reduced-motion` for the reduced-motion pass. Each run writes `sheet.png` and `report.json`.

## Content lock

No text was rewritten, reordered within a section, or added. Icons and chevrons are CSS masks on pseudo-elements, not DOM text. Animations start from a visible resting state and are disabled under `prefers-reduced-motion`. Suggestions that would change content are listed at the end of `03-audit-and-verification.md` and were not applied.
