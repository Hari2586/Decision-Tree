# BRIEF: MoneyHoney home page, scroll-craft build

**Self-authored under explicit creative delegation.** The owner asked to
"install this skill and apply on the website". No interview answers exist for
the eight topics, so the decisions below are authored, and each is marked as
such. Evidence (the owner's standing rules from the redesign brief) is
separated from assumptions.

## Hard rules that outrank everything in this file (evidence, owner's words)

- Content lock: "Do not rewrite, shorten, summarize, reorder within a section,
  or 'improve' any text. Keep every headline, paragraph, button label, number,
  link, and form field word for word. Keep all regulatory text verbatim and
  clearly visible."
- Allowed: "change layout, order of sections on a page, typography, color,
  spacing, icons, imagery, and interaction."
- Brand: navy #1B2666, orange #E8511A, logo as is.
- Later rulings: Direction B "Clear Glass" with the flat Direction A buttons,
  "Don't use too much rounded corners", no em dashes.
- Compliance footer on every page.

Consequence for this build: no new sentences, no new numbers, no new links.
Every figure that moves on this page is a figure already printed on it.

## The eight topics

1. **Vibe** (authored): plain, sorted, trustworthy, dense. References: a
   museum wall of object labels; a well-kept index card drawer; the facts page
   of a prospectus. Not a bank ad.
2. **Scroll journey** (authored, section order kept as the source has it):
   title wall and the four facts; the eleven problem labels; the eleven doors
   in Start Here; the five asset-class plates; the eight specialist shelves;
   the colophon with the regulatory text.
3. **Energy curve** (authored): calm open, a steady build through the two
   collections, one full-room change at the asset classes, then quiet to the
   end.
4. **Feeling, stage by stage, and the one moment** (authored): see the
   feeling curve and the peak below.
5. **One thing no site does** (authored): an empty gauge sits on the edge of
   the page from the first screen. It only fills in one room, plate by plate,
   and it lands on the exact total printed on the first screen.
6. **Distance from premium-minimal** (authored): the "dense" family from
   uniqueness.md §5. Information-forward, small type, high count. Light
   ground, one navy room.
7. **One world or distinct scenes** (authored): distinct rooms. A catalog is
   walked, not flown through. Worldflight is wrong for a directory.
8. **Assets** (evidence): the logo SVG only. No photography, no footage, no
   image-generation key in this environment. So no scrub clips and no
   generated stills: the page is typographic and tabular by decision, not by
   fallback, and the gallery grammar allows that.

## Grammar: Gallery / catalog (uniqueness.md §2.6)

Why: the visitor's real question on this page is "what are the options", not
"should I believe you". Every item on it is already a museum label: a name and
a fact ("11 categories, 614 schemes"). The grammar's label schema is the
content's own schema.

Why the other seven lost:
- Filmic one-shot: needs footage and one linear argument. There is no footage
  and the page is an index.
- Chaptered editorial: needs prose. The page has one paragraph.
- Live surface: needs panels that compute. The home page computes nothing.
- Continuous world: needs geography and a flight. A directory has rooms, not
  a route.
- Typographic poster: needs one claim at 40vw. The content lock forbids
  inventing a claim, and the h1 is a category list.
- Split stage: needs two sides in tension. Nothing on this page is "versus".
- Rhythmic cutlist: needs pulse. A distributor's index page should not pulse.

Grammar bans honoured: no kinetic headlines, no spotlight, no magnet, no scrub
at all, no argument-shaped pinned type act, no hero claim.

## Journey (beats)

```
1  Orientation   the title wall and the four facts, already labelled
2  Recognition   eleven problems on a held wall, hung one at a time
3  Breadth       eleven doors travelling sideways under the hand
4  Completeness  five plates land, the gauge fills, the total closes
5  Curiosity     eight specialist shelves read at reading pace
6  Rest          the colophon plate, the gauge docks onto it, nothing moves
```

## Feeling curve (written before the score)

```
1  Orientation   white wall, the h1 at display size, four fact plates whose
                 figures tick up once on arrival (flow + in, count on entry)
2  Recognition   the frame holds and the eleven solution labels wipe onto the
                 wall left to right, one after another (pin + reveal)
3  Breadth       the Start Here rail: eleven labelled doors slide past, each
                 settling as it arrives, tilting under the pointer (pan + tilt)
4  Completeness  the room goes navy; five asset-class plates arrive in turn,
                 each count ticking to its figure, and the edge gauge fills
                 segment by segment until the readout says 1,774 (pin + count
                 + the signature gauge)                                  PEAK
5  Curiosity     back to the light wall; eight theme shelves in a two-column
                 plan, offset, read at reading pace (flow + in)
6  Rest          the colophon: the footer links and the regulatory text set
                 as a label plate on deep navy; the gauge leaves the page edge
                 and docks onto the plate, complete (pin, greet-and-hold)
```

No two adjacent acts share a feeling. Act 5 is deliberately quiet after the
peak: it is the walk back to the door.

## The peak

Act 4. The sentence a visitor would say: "the little gauge on the edge that
was empty the whole time filled up plate by plate, and when the last one
landed it said 1,774, the same number as the first screen."

It gets the largest span on the page (4.0 viewport-heights against 3.2 for
the rail and 2.4 for the solutions wall), the only dark ground on the page,
and the silence before it: the rail's authored tail breath (an empty last
item on the Start Here rail, so the last door clears before the room changes).

**Authored silence:** the empty tail item at the end of the Start Here rail,
roughly a third of a viewport of travel with nothing new arriving. It is
intentional and the verification pass should not read it as dead scroll.

## Tell-someone sentence

It's the site where an empty gauge rides the edge of the page the whole way
down, then fills up in the fund-types room and lands exactly on the 1,774
from the first screen.

## Signature move: the shelf gauge

A fixed rail (right edge on desktop, bottom edge on phones) carrying two
things: four room markers that jump to the four collections, and a five-segment
gauge whose segments are proportional to the five asset-class scheme counts
printed on the page (614, 434, 179, 506 and 41 of 1,774). It is empty from the
first screen. In act 4, bespoke page JS reads the act's `--sc-p` and fills each
segment in step with its plate's arrival, and a readout counts the running
total. On the close it docks onto the colophon plate. No engine edit; the
engine only publishes `--sc-p`.

Real numbers only: 614 + 434 + 179 + 506 + 41 = 1,774, which is the figure on
the first plate. Nothing is invented.

## Score table

| Beat | Device | Why this one |
|---|---|---|
| Orientation | `flow` + `in`, `count` on entry, two parallax wall planes | The facts are already labels; they should sit still and tick once |
| Recognition | `pin` + `reveal` per label | Hanging labels on a held wall is a change of state, which is what a wipe is |
| Breadth | `pan` + `tilt` | Lateral travel reads as "options"; this is the widest collection |
| Completeness | `pin` + `count` + the gauge | The frame holds while the room fills; the only act that needs the visitor to stay |
| Curiosity | `flow` + `in` | Administrative range, read at reading pace, not pinned |
| Rest | `pin`, greet-and-hold | The last screen must hold with content on it |

Checks: six device families (flow/in, count, reveal, pin, pan, tilt, plus
parallax on the hero planes). No family twice in a row (flow, pin, pan, pin,
flow, pin). Zero scrub acts. One peak with the largest span. Total planned
length about 12.5 viewport-heights across six acts.

## Fingerprint gate

Registry at `redesign/scrollcraft/FINGERPRINTS.md` is empty. Nothing to clear.
Row appended after shipping.

## Aesthetic

Dense family on the Direction B palette: white and wash grounds, navy ink,
orange only as the mark and the gauge fill, orange-ink #C4410E for the one
accent role, two-stop accent for the navy room (#FFB28F on navy). Manrope for
display, Figtree for text. Radii 4px and 6px. Flat buttons.
