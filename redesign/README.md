# MoneyHoney website redesign

Chosen direction: **B, "Clear Glass"** (picked 8 Oct 2026).

| Path | What it is |
|---|---|
| `site/index.html` | Final home page, Direction B. Deploy this. |
| `original/index.html` | The supplied original, kept for verification. |
| `alternatives/direction-a-ledger/index.html` | Direction A, archived. Same HTML body, different stylesheet. |
| `01-content-inventory.md` | Phase 1 inventory, every string and link, compliance register. |
| `02-design-directions.html` | Phase 2 moodboard with both directions. |
| `03-audit-and-verification.md` | Phase 4 accessibility audit and Phase 5 content verification. |
| `tools/verify.py` | Content verification script. `python3 -I redesign/tools/verify.py <original> <new>` |

## Applying the design to sub-pages

The design is the `<style>` block and the Google Fonts `<link>` in `site/index.html`. Every sub-page keeps its own content and the same header, nav and compliance footer. Card icons are chosen by `href` in CSS, so new product links get the default four-square icon until a rule is added.

Content lock: no text was rewritten, reordered within a section, or added. Suggestions that would change content are listed at the end of `03-audit-and-verification.md` and were not applied.
