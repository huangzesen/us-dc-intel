# Slice 10 — Interactive stats: the COMPUTE HORIZON chart

**Target:** `astro/src/pages/index.astro` (section `03 BUILDOUT WAVE`) · **Date:** 2026-08-12
**Intent (Jason):** rethink the stats presentation, make it interactive, and show *at a glance the final compute that might come online*.

## What was built

A new **COMPUTE HORIZON** card at the top of section 03, above the existing per-year
stacked bar chart (which is unchanged). It is a **cumulative stacked area chart**:

- **X** = 2018–2030 (the same `years` matrix the bar chart reads — per-year
  `operational_mw` / `construction_mw` / `pipeline_mw` from `export_astro_data.py`;
  no export changes were needed).
- **Y** = cumulative capacity, stacked bottom→top as **operational → construction →
  pipeline**, using the existing CVD-validated status palette (`--st-op`, `--st-con`,
  `--st-app`). Re-validated with the dataviz six-checks validator on both theme
  surfaces: all pass (light-mode green has a 2.74:1 contrast WARN, relieved by the
  direct labels, legend text, and tooltips).
- **The top edge is the answer**: the stack's upper boundary reads as "compute that
  could be online by year X if every dated project lands", and an animated headline
  number (`711 GW` worldwide) restates it in one glance, with a per-stage breakdown
  row underneath.

The two charts complement rather than duplicate: the bars show **flow** (signals per
year, tab-switchable facilities/capacity), the area shows **stock** (cumulative
capacity). The horizon chart is deliberately capacity-only — "final compute" has no
facilities-count reading — so it ignores the FACILITIES/CAPACITY tabs.

## Interactivity

1. **Hover / focus crosshair** — 13 invisible per-year hotspots (also `tabindex=0`
   with full `aria-label` mirrors for keyboard/SR users) drive a dashed crosshair
   with color-coded dots on each stage boundary and the site-standard tooltip:
   cumulative per stage, bold potential total, and a "click to scrub" hint. On
   coarse pointers, taps pin the tooltip (same convention as the wave columns).
2. **Click a year → page-wide cross-filter** — clicking a hotspot calls the existing
   `setScrubYear()`, so the map markers, registry, wave-column dimming, and the year
   slider above the map all follow. In the horizon chart the scrubbed state renders
   as an amber-edged veil (`≤ 2026`) dimming the years beyond, and the headline
   re-counts to the scrub year. Re-clicking the same year clears the scrub. The
   reverse direction also works: dragging the existing slider or pressing ▶ autoplay
   moves the veil and re-counts the headline year by year (hooked via
   `syncWaveScrub → syncHorizonScrub`).
3. **Stage toggle chips** — the legend is three pill buttons (`aria-pressed`); toggling
   one collapses that band to zero thickness with a ~400 ms rAF path morph (the axis
   stays pinned to the all-stages total so comparisons stay honest), fades its
   boundary strokes, and strikes it through in the breakdown row. E.g. toggling
   pipeline off answers "what's real + committed?" (207 GW vs 711 GW).
4. **Animated headline** — eased count-up that re-counts from its previous value (so
   scrub autoplay reads as a continuous meter), with GW→TW auto-unit crossover.
5. **Scope-aware** — country selection rebuilds the chart from that country's `years`
   matrix with a morph transition (piggybacked on `buildWave()`, so every existing
   rebuild path is covered).

All motion respects the existing `noMotion` flag (`prefers-reduced-motion` /
`?noanim`); theming is fully token-driven (verified in dark and light).

## Design decisions & mechanics

- **No chart library** — one stretched SVG (`preserveAspectRatio="none"`) carries the
  fills and `vector-effect="non-scaling-stroke"` boundary lines; everything that must
  not distort (axis ticks, x labels, crosshair, dots, end labels, veil) is
  percentage-positioned HTML overlaid on the plot. Matches the page's zero-dependency
  pattern.
- **Mark specs** per the dataviz method: fills at 0.42 opacity, 2 px solid boundary
  lines with a 4 px surface-colored "cut" stroke beneath each (the 2 px surface gap
  between stacked fills), 2.5 px emphasis on the top edge, selective direct labels at
  the right edge (per-stage 2030 totals, skipped for bands under 7% of the axis,
  hidden below 680 px) plus a `▲ total` label riding the horizon line. Values wear ink
  tokens, never series color.
- **CSS must live in the `is:global` block**, not the scoped `<style>` — most of the
  chart's DOM is injected at runtime via `innerHTML` and never receives Astro's
  scoped-style attribute. (First build had the rules scoped and silently unmatched;
  moved and verified.)
- **Honesty**: only records with a dated milestone signal are counted (711 GW of the
  2.16 TW corpus, worldwide), and the card note says so — consistent with the site's
  existing "records without a dated signal are hidden while scrubbing" convention.
  Scopes with no dated MW (e.g. Brazil today) legitimately show a flat zero.

## Verification

- `cd astro && npm run build` — passes.
- Playwright suite (12/12): paths render, headline > 0, bar chart's 13 columns
  intact, crosshair + tooltip on hover, click→veil + slider follows + headline
  re-counts, toggle morphs paths + `aria-pressed`, re-click clears scrub, no JS
  page errors. Country-scope rebuild verified via `#c=BR` hash restore.
- Screenshots eyeballed in dark and light, default/scrubbed/toggled states, plus the
  full section for cohesion with the bar chart.
- Diff: only `astro/src/pages/index.astro` (+560/−1); no internal paths in the diff.
