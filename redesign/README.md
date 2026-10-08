# MoneyHoney website redesign

Direction: **B, "Clear Glass"** (chosen 8 Oct 2026). Pages rebuilt so far: home, Solutions hub, Child Education, Emergency Fund, EMI Management.

| Path | What it is |
|---|---|
| `site/` | The redesigned site. Deploy this folder. Relative links match the original URL structure. |
| `site/assets/mh.css` | The one stylesheet for every page (design tokens, components, animations). |
| `site/assets/mh.js` | Progressive interactions: reading progress bar, scroll reveal, slider track fill, figure "tick" on change, hiding the sticky result bar while the calculator is on screen, count-up on the home fact tiles, interactive charts (tooltips on hover, tap or focus; legend toggles). Pages are complete without it. |
| `site/index.html` | Home. |
| `site/solutions/index.html` | Solutions hub. |
| `site/solutions/<slug>/index.html` | Solution pages. Their calculator scripts are the originals, untouched. |
| `original/` | The supplied pages, kept for verification, plus the sitemap index. |
| `alternatives/direction-a-ledger/` | Direction A home page, archived. |
| `inventory/*.md` | Phase 1 inventory per page, generated from the originals: every text fragment, link, label and meta tag in order, compliance rows marked. |
| `01-content-inventory.md` | Hand-written home page inventory with the compliance register. |
| `02-design-directions.html` | Phase 2 moodboard with both directions. |
| `03-audit-and-verification.md` | Phase 4 accessibility audit and Phase 5 content verification. |
| `tools/build.py` | Builds a page: keeps the body byte for byte (only the body tag gains a class and the demo notice moves inside the header landmark), swaps the head's embedded CSS for the shared assets. |
| `tools/verify.py` | Content verification: title, meta, JSON-LD, aria-labels, every href in order, the full visible text stream. |
| `tools/inventory.py` | Generates the per-page inventory tables. |

## Rebuilding a page

```
python3 redesign/tools/build.py <original.html> redesign/site/<path>/index.html <asset-prefix> <body-class>
python3 redesign/tools/verify.py <original.html> redesign/site/<path>/index.html
```

Asset prefix is `""` at the root, `../` one level down, `../../` two levels down. Body class is `page-home`, `page-hub` or `page-solution`.

## Content lock

No text was rewritten, reordered within a section, or added. Icons and chevrons are CSS masks on pseudo-elements, not DOM text. Animations start from a visible resting state and are disabled under `prefers-reduced-motion`. Suggestions that would change content are listed at the end of `03-audit-and-verification.md` and were not applied.
