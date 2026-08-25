---
name: The Competitive Fishing League
description: One axis, one canal, one champion.
colors:
  canal-deep: "#08243d"
  canal: "#0d3557"
  canal-lit: "#123f66"
  basin: "#14497a"
  water: "#2a6fa8"
  spray: "#dce9f2"
  marble: "#ece7db"
  gravel: "#cbbfa4"
  hedge: "#1b3a2a"
  hedge-lit: "#2f5c40"
  gilt: "#c0913f"
  gilt-lit: "#e6c179"
  gilt-deep: "#8a6524"
  bronze-ink: "#664611"
  ink-2: "#a8c2d6"
  # Gradient stops and machine-room shades, documented prose values
  marble-highlight: "#fbf8f1"
  marble-shade: "#d5cec0"
  hedge-deep: "#16301f"
  machine-room: "#061c30"
  # The ink under every physical shadow on the page
  umbra: "#000000"
typography:
  scale:
    label-xs: ".62rem"
    label-s: ".63rem"
    label-sm: ".68rem"
    label: ".7rem"
    label-md: ".72rem"
    small: ".86rem"
    caption: ".88rem"
    rank: ".92rem"
    angler: ".94rem"
    body-s: "1rem"
    annotation: "1.02rem"
    plan-figure: "8px"
    close-h: "1.4rem"
    close-h-max: "2.35rem"
  display:
    fontFamily: '"Cinzel", Georgia, "Times New Roman", serif'
    fontSize: "clamp(1.85rem, 1.1rem + 3.5vw, 4.15rem)"
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: "0.11em"
  headline:
    fontFamily: '"Cinzel", Georgia, "Times New Roman", serif'
    fontSize: "clamp(1.35rem, 1rem + 1.7vw, 2.15rem)"
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: "0.16em"
  title:
    fontFamily: '"Cinzel", Georgia, "Times New Roman", serif'
    fontSize: "clamp(1.8rem, 1.2rem + 2.4vw, 2.7rem)"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: "0.14em"
  body:
    fontFamily: '"EB Garamond", Georgia, "Times New Roman", serif'
    fontSize: "clamp(1.0625rem, 0.98rem + 0.38vw, 1.1875rem)"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: '"Cinzel", Georgia, "Times New Roman", serif'
    fontSize: "0.72rem"
    fontWeight: 600
    letterSpacing: "0.34em"
components:
  button-primary:
    backgroundColor: "{colors.gilt}"
    textColor: "{colors.canal-deep}"
    padding: "1.05rem 2.1rem"
  button-primary-hover:
    backgroundColor: "{colors.gilt-lit}"
    textColor: "{colors.canal-deep}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.gilt-lit}"
    padding: "1.05rem 2.1rem"
  button-done:
    backgroundColor: "{colors.hedge-lit}"
    textColor: "{colors.marble}"
---

# Design System: The Competitive Fishing League

## Overview

**Creative North Star: "The Engraved Water Garden"**

The Competitive Fishing League presents itself as an institution laid out like a formal water garden: the league as a great estate whose ground plan is the page. One axis runs its full length — the Grand Canal, drawn in one-point perspective across the first viewport, then continued downward as a single column of rooms, each section a band across the same central line. The voice is an eighteenth-century engraved plan: everything ornamental is drawn as crisp vector geometry — hairline flourishes, rake lines, plan knots, fountain jets — never photographic decoration.

The page deliberately refuses the pro-tour pattern of a hero photograph over a card grid. Its hero is inscriptional: a crest set in a marble cartouche, the league name in engraved capitals beneath, and a vector vista of the canal receding to the horizon between mirrored parterres. Photographs appear only framed as material objects — outing plates inside arched hedge theatres, the champion in a hedge niche (the user asked for the champion image to lead at poster scale, so it runs wide within its apse). The joke is never announced; the straight face is the whole product, and the styling never winks. Density is ceremonial: generous band padding, one idea per band, prose capped at 66ch.

Motion is rationed to a single authored moment — the fountains waking in sequence as the vista and the order come into view — plus quiet state transitions (button fills, theatre lifts, row highlights). Nothing depends on scripting: the markup renders complete without JS, scripting only holds the jets back so the wake can run, and `prefers-reduced-motion` disables it entirely.

**Key Characteristics:**
- One great axis: every section is a band on the same central line, separated by a single gilt hairline rule.
- Four materials, strictly zoned: canal blue ground, clipped-hedge green enclosure, gilt bronze rule-work and controls, marble inscription at fixed points.
- All ornament is vector: flourishes, legend icons, the plan knot, the scale bar, the vista, the fountain jets.
- Engraved type: Cinzel inscriptional capitals for anything that names, ordains, or labels; EB Garamond — often italic — for running prose and annotation.
- Mirrored symmetry: the vista, the plan legend, and the theatre row are strict mirror compositions.
- Built to be sent: one self-contained file, decorative images lazy-loaded, and the share action front and center at the close.

## Colors

The palette is the garden's materials, not an abstract ramp: a family of five blues drenches the ground, two greens clip the hedges, four bronzes do the rule-work, and marble with gravel buff are the only light surfaces — reserved for inscription and the raked parterre. Roles below follow accent-versus-ground; the blue ground is what leads the palette on every screen.

### Primary

- **Gilt Bronze** (#c0913f): The accent — every rule, hairline, flourish stroke, label, rank numeral, and button fill or border. Rules are gilt at graded alpha: the section rule at 38%, order column rules at 45%, order row rules at 14%.
- **Gilt, Lit** (#e6c179): The brighter gilt for emphasis — plate labels, legend terms, order column heads, ghost button text, the scale bar's numerals, and the focus ring.
- **Gilt, Deep** (#8a6524): Dark bronze for engraved shadow lines — the outer rings of cartouche, niche, cameo, and theatres, the basin lip, and the scrollbar thumb.
- **Bronze Ink** (#664611): The ink dark enough to set type on marble — used solely for "Reigning Champion" on the plinth.

### Secondary

- **Canal Deep** (#08243d): The base ground — the page's body background and the deepest water. Also the scrollbar track and the ring surrounding the cartouche.
- **Canal** (#0d3557): The mid ground — the parterre and theatre bands, the vista sky's first stop, and the cameo quote's text.
- **Canal Lit** (#123f66): The horizon light — the sky's last stop and the close's mid-gradient.
- **Basin** (#14497a): The lightest ground stop, reached only at the close's horizon, and stopped there so the gilt controls sitting on it keep their contrast.
- **Water** (#2a6fa8): Lit water — the basin water fill and the vista canal's mid-gradient.
- **Spray** (#dce9f2): Pale jet spray — the order's points numerals, the basin spray strokes, and the jet columns' gradient.

### Tertiary

- **Hedge** (#1b3a2a): Structural enclosure — the bosquet's hedge walls, the theatre frames, the niche shading, and the vista's hedge blocks.
- **Hedge, Lit** (#2f5c40): The lit side of the hedge — gradient tops of the niche and theatres, the vista hedge blocks' stroke, and — as the one sanctioned exception to the green-is-enclosure rule — the share button's "done" fill.

### Neutral

- **Marble** (#ece7db): Inscription ground — the cartouche, the plinth, and the cameo. Shaded to #cfc8b7 and #d5cec0 in its gradients. Reserved; never a general surface.
- **Gravel Buff** (#cbbfa4): The raked parterre — the vista's parterre fill at 20% opacity and its rake lines. The token is declared in `:root` but the vista drawing uses the literal hex.
- **Muted Ink** (--ink-2, #a8c2d6): The annotation voice — the motto's translation, legend smalls, the order's caption, section introductions, and the waterworks copy.

Two honest notes for anyone extending the palette. The vista SVG redeclares palette values as literal hex inside the drawing (#0d3557, #2a6fa8, #cbbfa4, #1b3a2a, #2f5c40, #c0913f, #dce9f2, plus un-tokenized #5f9ec6 and #0a2b47); a palette change must be made in both places. And a `--seal` red (#9d1c26) is declared in `:root` for the crest's own red accent but is unused in the current build — keep it reserved rather than repurposing it.

### Named Rules

**The Four Materials Rule.** Every surface, line, and word answers to one of four materials: canal blue is the ground, clipped hedge is enclosure, gilt bronze is rule-work and controls, marble is inscription. No material crosses its zone — the sole exception is the share button's done state, which fills hedge green as a confirmation.

**The Light Ground Rule.** Only marble is light. No white or near-white surface may appear anywhere else; the page's ground is canal blue end to end, from the terrace to the waterworks.

## Typography

**Display Font:** Cinzel — inscriptional capitals, loaded at weights 400;500;600;700;900 (with `"Cinzel", Georgia, "Times New Roman", serif`)
**Body Font:** EB Garamond — running text and italic annotation, loaded at 400/500/600 plus italics 400/500 (with `"EB Garamond", Georgia, "Times New Roman", serif`)
**Label/Mono Font:** None — labels share the display face.

Both faces load from Google Fonts with `display=swap` (preconnected). Uppercase is applied with `text-transform`, not a small-caps feature.

**Character:** The voice of a cartographer's engraving — Cinzel's chiselled capitals for ceremony and naming, EB Garamond's warm old-style serif for sentences and hand-written annotation. Everything named is carved; everything said is set.

### Hierarchy

- **Display** (Cinzel 700, clamp(1.85rem, 1.1rem + 3.5vw, 4.15rem), line-height 1.14, letter-spacing .11em): The terrace title, "Competitive Fishing League". The article "The" is set as a small block above it at .3em size, weight 500, letter-spacing .52em, in gilt-lit, indented .52em to correct the trailing tracking.
- **Headline** (Cinzel 600, clamp(1.35rem, 1rem + 1.7vw, 2.15rem), line-height 1.14, letter-spacing .16em): The section heads — "At the head of the garden", "The green theatres", "The order of the fountains". The close's "Carry it down the canal" is the weight-700 variant at clamp(1.4rem, 1rem + 1.9vw, 2.35rem).
- **Title** (Cinzel 900, clamp(1.8rem, 1.2rem + 2.4vw, 2.7rem), line-height 1, letter-spacing .14em): The champion's name on the plinth.
- **Body** (EB Garamond 400, clamp(1.0625rem, 0.98rem + 0.38vw, 1.1875rem), line-height 1.65): Running prose, never wider than 66ch (the `.measure` container).
- **Label** (Cinzel 600, .72rem, letter-spacing .34em, uppercase): The plate-label voice — "The plan of the league". The same voice runs through the order's column heads (.63rem, .28em), legend terms (.68rem, .26em), theatre plate numbers (.63rem, .3em), buttons (.72rem, .26em), the plinth's "Reigning Champion" (.7rem, .34em), and the waterworks headings (.62–.68rem, .24–.3em).
- **Annotation:** EB Garamond italic in muted ink — legend smalls, the order caption, the cameo quote, and the colophon.

All h1–h3 are uppercase with `text-wrap: balance`; headings carry no bottom margin, spacing comes from the layout.

### Named Rules

**The Inscription Rule.** Cinzel capitals are reserved for what names, ordains, or labels — headings, names, ranks, plate labels, buttons. Running prose is always EB Garamond, and italic EB Garamond is the annotation voice. Never set a sentence in Cinzel.

## Layout

The page is a single vertical axis. Every section is a full-width band across it, sharing one container — `.axis`, max-width 1180px (`--axis-max`), side padding clamp(1.25rem, 5vw, 2.5rem). The direction contract's "every section a bosquet" landed literally once — the champion's hedge-walled room — and otherwise as banded rooms of a plan: each section is a distinct ground tone, opened and closed by the same hairline rule. The band sequence down the page: terrace (sky gradient from canal-deep through canal to canal-lit), parterre (canal fading to canal-deep at 60%), the champion's bosquet (canal-deep, over the hedge enclosure), cross-vista (canal), fountain chamber (canal-deep), close (canal-deep lightening through canal-lit at 62% to basin), waterworks (#061c30, the machine room, set deliberately darker and tighter).

Vertical rhythm is ceremonial: major bands breathe with clamp(3.75rem, 9vw, 6.5rem) block padding, the parterre at clamp(3.5rem, 9vw, 6rem), the close is the grandest at clamp(4rem, 10vw, 7rem), the waterworks is tight at clamp(2.75rem, 6vw, 4rem). Section content is centered on the axis; prose and captions sit in `.measure` (66ch max), centered under their heads.

The vista (the hero drawing) is a 1600×620 SVG in one-point perspective: horizon at y=150, the Grand Canal tapering from 760 units wide at the foot to 320 at the horizon, mirrored raked parterres with rake lines drawn to the vanishing point, five diminishing pairs of clipped hedge blocks, and six fountains in three mirrored pairs. Pure vector — nothing photographic above the fold except the crest itself.

Mirrored compositions are the only sanctioned departure from centering: the plan legend is a three-column grid (1fr auto 1fr) with mirrored definition lists around a central broderie knot; the theatres run four across (repeat(4,1fr), gap clamp(.75rem, 2vw, 1.4rem)); the order is a single table on the axis. The waterworks columns use repeat(auto-fit, minmax(230px, 1fr)).

Responsive behavior:
- **860px:** the mirrored legend collapses to a single centered column (knot first, then the two beds, rows max 22rem), and the theatres go two-across.
- **560px:** the order drops its basin (jet) column, angler names wrap, the cameo stacks vertically, buttons go full-width, and the title's "The" tightens to .34em tracking.
- Between breakpoints, the axis container and the type clamps absorb the difference; the grid is the only thing that changes shape.

### Named Rules

**The One Axis Rule.** Every section is a band on the same central axis (max 1180px); prose is centered and never exceeds 66ch. Divergence from the axis is only ever a mirrored composition.

**The Hairline Rule.** Section separation is always the single hairline — `--rule`, 1px solid gilt at 38% alpha — as a border-top. No heavier dividers exist anywhere on the page.

## Elevation & Depth

This system carries no UI shadow vocabulary. Depth is drawn, three ways: one-point perspective (the vista), gradient atmosphere (sky and water lighten toward the horizon), and engraved concentric rings. The shadows that do exist are physical umbrae under material objects, not elevation: dark, soft, and cast downward, as if the objects stand on the plan.

### Shadow Vocabulary

- **Marble umbra** (`0 16px 34px -14px rgba(0,0,0,.7)`): Under the plinth and the cameo — marble slabs lifted off the hedge.
- **Niche umbra** (`0 26px 50px -18px rgba(0,0,0,.72)`): Under the champion's alcove, with an inset 0 3px 0 rgba(230,193,121,.22) gilt-lit edge at the top.
- **Theatre umbra** (`0 20px 34px -20px rgba(0,0,0,.8)`): Under the theatre frames; on hover it deepens and lengthens (`0 28px 44px -20px rgba(0,0,0,.85)`) as the frame lifts.
- **Inscription rings** (`0 2px 3px rgba(255,255,255,.28) inset, 0 18px 38px -12px rgba(0,0,0,.62), 0 0 0 5px canal-deep, 0 0 0 6px gilt-deep, 0 0 0 10px canal-deep, 0 0 0 11px rgba(192,145,63,.5)`): The cartouche's engraved ring structure — an inset marble highlight, then alternating canal and gilt rings.
- **Title legibility** (`0 2px 18px rgba(0,0,0,.45)`): A soft text-shadow under the terrace title, so the engraved caps hold over the sky gradient.

### Named Rules

**The Engraved Ring Rule.** Anything honored — the crest, the niche, each theatre — is set in concentric gilt rings, not floating shadows. Depth is drawn, not dropped.

## Shapes

The form language is garden-plan geometry: hard edges and arcs, no generic rounding. Nothing on the page uses ordinary corner radius. The recurring silhouettes:

- **Circles:** the cartouche (a true circle via aspect-ratio 1 and radius 50%), the cameo's 92px photograph inside a 2px gilt-deep ring, the broderie knot's lobes.
- **Arches:** the niche apse and each theatre are round-headed — semicircular tops over square shoulders. The theatre uses border-radius `50% 50% 2px 2px / 12% 12% 2px 2px` with the inner photograph clipped one step tighter; the champion's niche is a wide shallow apse at `50% 50% 6px 6px / 26% 26% 6px 6px` with the photograph at `24%`.
- **Notched clips:** the bosquet's hedge wall is a clip-path polygon with a 3% notch top and bottom between 38% and 62% width — the openings where the axis enters and leaves the room.
- **Hairlines:** flourishes are SVG, stroke-width 1 with non-scaling stroke, a small gilt circle at center; every icon (legend marks, knot, scale) is 1–1.4px gilt stroke on a transparent ground.

### Named Rules

**The Drawn, Not Rounded Rule.** Every ornamental form is vector-drawn geometry. When the build needs a soft corner it uses an arc, an arch, or a notch — never a generic border-radius.

## Components

### Buttons

Engraved controls — inscriptions you can press. Square corners, no radius; 1px solid gilt border; Cinzel 600 at .72rem, letter-spacing .26em, uppercase; padding 1.05rem 2.1rem.

- **Primary (filled gilt):** gilt background, canal-deep text, gilt-lit border. Hover fills gilt-lit and turns the border marble.
- **Ghost (outlined gilt):** transparent background, gilt-lit text, gilt border. Hover fills gilt, turns text canal-deep, and gains a soft shadow (`0 12px 26px -12px rgba(0,0,0,.62)`).
- **Pressed:** translateY(1px).
- **Done (`data-state="done"`):** hedge-lit fill and border, marble text, no shadow — the one green control. Set by script for 2.6s on a successful copy, with the label swapped to "Copied — now send it" (a failed copy shows "Press ⌘C to copy" without the fill).
- **Focus:** the global gilt-lit ring (2px solid, 3px offset).
- All state changes transition at .35s on the garden's ease curve.

### The Terrace Head (first viewport)

The crest sits in a marble cartouche — a true circle, clamp(132px, 20vw, 178px), radial highlight at 34% 28%, ringed canal-deep/gilt-deep/canal-deep/gilt — chosen because the navy-dominant crest (served from `assets/web/crest.webp`) needs a light ground. Beneath it: the display title, all centered, all on the axis — the crest and title alone, so the vista picks up the axis directly. (A motto and its flourish once stood between them; removed by request.)

### The Green Theatres

Each outing is a theatre: an arched hedge frame (hedge-lit fading to hedge at 70%, 1px gilt-deep ring) holding a portrait photograph at aspect-ratio 9/14, object-fit cover, arched top to match, with the plate number beneath ("Plate I" — Cinzel .63rem, .3em tracking, gilt-lit). On hover or keyboard focus-within the frame lifts 6px and its ring brightens to gilt over .5s on the garden's ease. The photographs lazy-load.

### Marble Inscription Surfaces

- **The plinth:** a marble slab (gradient marble to #cfc8b7), 3px gilt top edge, marble umbra; carries the champion's name in the Title role and "Reigning Champion" in bronze ink. Width min(716px, 92vw), matching the niche's footprint.
- **The cameo cartellino:** a marble tablet (gradient marble to #d5cec0), same 3px gilt edge and umbra; a flex row of the 92px circular portrait (2px gilt-deep ring) beside an italic EB Garamond quote in canal. Width min(468px, 92vw). Stacks vertically at 560px.

### The Order of the Fountains

The standings are a ceremonial table: Cinzel column heads (.63rem, .28em tracking, gilt-lit) over gilt rules at 45% alpha, row rules at 14%, Cinzel rank and points with `tabular-nums`, rows highlighting rgba(42,111,168,.16) on hover. Each row's basin is a miniature fountain — an SVG whose jet height encodes the standing (the higher the jet, the better the season): a pale spray arc, a jet column filled with a spray-fade gradient, water at 50% opacity, and a gilt-deep basin lip. Row jets carry their own stagger delays (.00–.63s). The caption underneath declares the placeholder status of the figures.

### The Fountain Wake

The one authored animation in the system. Jets are drawn at full height in the markup; when `<html>` carries the `js` class they are held at rest (scaleY .12 in the vista, .06 in the order) and released to full height — 1.5s in the vista, 1.25s in the order, on the garden's ease — with staggered delays (vista jets .05–.9s, order rows .00–.63s) once their container gains the `woke` class. The class is added by script when any part of `#vista` or `#order` passes the 85% viewport line, position-checked on scroll and resize (rAF-throttled, listeners removed once all are woken) so deep links and fast scrolls still wake every jet. Under `prefers-reduced-motion`, or with scripting off, the jets render at full height — content is never hidden by default, and the motion is fully disabled rather than shortened.

### Named Rules

**The One Waking Rule.** The fountain wake is the only authored animation. Any new motion must be a state transition (hover, focus, active) on the existing ease curve — never a second choreography.

### Plan Furniture

The small recurring furniture of the engraved plan: the **plate label** (Cinzel .72rem, .34em tracking, gilt-lit, centered) that heads the legend; the **legend rows** (38px gilt line-icon, Cinzel term, marble definition with an italic ink-2 small); the **broderie knot** (clamp(94px, 15vw, 150px) gilt line-work over a hedge-tinted bed at 42% opacity) that centers the legend; and the **scale bar** (min(300px, 76vw), gilt segments marked 0/10/20/30 in 8px Cinzel with the caption "Toises") — every plan carries its scale.

## Do's and Don'ts

### Do:

- **Do** keep the fountain wake as the only authored animation; new motion must be a state transition on the garden's ease curve.
- **Do** draw every ornament as inline SVG with 1px gilt strokes (non-scaling), `aria-hidden` when decorative, and a real `aria-label` when it carries meaning (the vista, the scale).
- **Do** keep every section a band on the one axis (max-width 1180px), prose centered and within 66ch; break symmetry only for a mirrored composition.
- **Do** hold jets back only with the `js` class, and always render them full-height without JS and under `prefers-reduced-motion`.
- **Do** keep marble on inscription and fixed points only — cartouche, plinth, cartellino — shaded with the established marble gradients.
- **Do** keep the straight face: the pageantry is played completely seriously; nothing in the styling may wink at the joke.

### Don't:

- **Don't** introduce a hero photograph or a card grid — the tour-site pattern this world exists to refuse.
- **Don't** put hedge green on any control except the sanctioned done confirmation of the share button.
- **Don't** set running prose in Cinzel, or labels in EB Garamond.
- **Don't** add generic corner rounding; arcs, arches, and notched clips are the only corner language.
- **Don't** lighten the ground: white or near-white belongs to marble alone; the page ground stays canal blue from terrace to waterworks.
- **Don't** duplicate the palette again in new inline SVG; if a drawing must use literal hex, keep it in sync with `:root`.
