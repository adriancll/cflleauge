# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Single self-contained `index.html` at the repo root, with CSS in a `<style>` block and
images referenced from `assets/`. Chosen by the user for shareability: the page's whole job
is to be sent to people, so it must open by double-click and deploy to Netlify/GitHub Pages
or a plain static host with no build step.

## Users

People who are sent a link to it — friends of the crew, prospective members, and the members
themselves. They arrive curious and uncommitted, usually from a phone, with no prior idea of
what CFL is. They are not looking to complete a task; they are deciding in a few seconds
whether this is funny, real, and worth caring about.

## Product Purpose

The Competitive Fishing League (CFL) is a friends' fishing league. This site exists to spread
it: to make the league feel like an institution, give the crew a place to point at, and make
a stranger want in. Success is someone reaching the bottom, grinning, and sending it on.

## Positioning

CFL is a mates' league that carries itself with the full ceremony of a professional tour —
crest, season, standings, a reigning champion. The joke is never announced; the straight face
is the whole product. A generic "fishing club" page could not copy this, because the humour
lives in the gap between the pageantry and the fact that it is a handful of friends.

## Operating Context

Seasons, individual outings, and an eventual champion. Members already have a crest/logo, a
champion portrait, and photos from outings. The league is social and self-organised — there
is no governing body, entry fee, venue contract, or prize purse.

## Capabilities and Constraints

- Not a product or service. Nothing to buy, book, or sign up for through the site.
- Species and water type are deliberately unspecified: the copy must never name a species,
  venue, or water type, because the real answer is mixed and unconfirmed.
- The reigning champion may be identified as **Liam**. No statistics, weights, dates, or
  achievements may be attributed to him beyond the title itself.
- All other angler names, standings figures, and season results are **placeholders** and must
  be labelled as such for the user to replace.
- **Undecided / not to be invented:** season dates, number of members, league founding year,
  locations, rules, scoring system, social links, contact details.

## Brand Commitments

- Name: Competitive Fishing League, abbreviated CFL.
- The crest (`assets/logoalpha.png`, transparent) is the identity anchor and must appear at
  the top of the page. It is a predominantly dark navy circular crest with red and white
  accents (~72% dark pixels), so it requires a light ground for contrast.
- Blue is the league's colour and must lead the palette. Red is available as the crest's
  own accent.
- The user asked for a "normal", non-modern website — traditional web furniture over
  contemporary app-style layout.

## Evidence on Hand

Real assets in `assets/`:

- `logoalpha.png` (2000×2000, transparent) — crest. Primary mark.
- `logo.png` (2000×2000, opaque) — same crest on a solid ground.
- `cflchampion.png` (340×332) — champion image, designated by the user as the main poster.
  Low resolution: initially capped at ~340px; in Aug 2026 the user asked for the champion to
  display large, so the site now renders it at ~716px from a Lanczos-upscaled and sharpened
  derivative (`assets/web/champion-big.webp`, 680×664). A higher-resolution source would
  replace it cleanly if one appears.
- `liamcfl.png` (338×332) — champion/member image. Low resolution, same constraint.
- `fishingpicture1–4.png` (all portrait, ~1024×1535 to 941×1672) — outing photos. Portrait
  orientation drives any gallery layout.

Absent, and not to be fabricated: real standings, real results, sponsors, press, testimonials,
member counts, or dates.

## Product Principles

1. **Straight face, always.** The pageantry is played completely seriously. Winking at the
   joke kills it.
2. **Ceremony over information.** The visitor is here to feel the league's weight, not to
   look anything up. Structure exists to confer status.
3. **Never claim what isn't true.** Invented rosters and figures are permitted as clearly
   marked placeholder material; facts about real people, places, and results are not.
4. **Built to be sent.** One file, fast on a phone, and legible in a link preview.

## Accessibility & Inclusion

No product-specific standard established. Default expectation: legible contrast on the blue
ground, real alt text on every asset, and full keyboard reachability.
