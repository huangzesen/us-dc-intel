# Slice 7 — Chart upgrades (§4.1/§4.2) + scoped operators (§4.4)

Scope: `astro/src/pages/index.astro` only. No data changes, no export changes.
Build: `cd astro && npm run build` → **pass** (1 page, no warnings).

## §4.1 Funnel

- **Stage-to-stage conversion ratios** between adjacent bars, in muted mono
  (`→ 341%`, `→ 28%`, `→ 153%`, `→ 247%` on the worldwide view). Rendered as a
  `.fratio` row that mirrors the `.frow` grid so the ratio sits under the bar
  column; `title` attribute explains "capacity vs previous stage" (bilingual).
- **Planned-vs-live multiple headline**: the funnel `<h2>` now ends with
  "— a 1.9× wave still to land" (zh: "还有 1.9× 的浪潮待落地"), computed as
  (all non-operational stages) / operational capacity. Skipped when a scoped
  country has zero operational capacity (no divide-by-zero, no "∞").
- **Per-bar hover tooltips** (existing `#tip` component): stage name, capacity,
  project count, and share of all-stage capacity.
- **Not done — per-bar tracked/estimated hatched split**: the funnel aggregate
  (`DATA.funnel` / `country.funnel`) only carries `key/count/capacity_mw/label`;
  there is no per-stage tracked/est split in the exported data, and this slice
  is barred from changing data or the exporter. Needs a small `export_astro_data.py`
  addition in a later slice.

## §4.2 Wave

- **Cumulative operational overlay**: a thin amber (`var(--acc)`) SVG polyline
  over the column stack — the running stock of energized capacity/facilities,
  flat through the 2027-2030 pipeline years, which is the story (flow vs stock).
  Implemented as a percent-coordinate `viewBox="0 0 100 100"` +
  `preserveAspectRatio="none"` overlay with `vector-effect: non-scaling-stroke`,
  so it tracks the responsive column layout with no resize handler.
- **One shared axis** (no dual-axis): the y-scale stretches to
  `max(tallest year stack, final cumulative value)`; the line is drawn in the
  active metric (GW in CAPACITY mode, facility count in FACILITIES mode) so the
  units always match the columns.
- **Axis fixes**: y-ticks were rendered inverted (0 at the top, max at the
  baseline); they now read max→0 top-down, and FACILITIES-mode ticks round to
  whole facilities (was "153.25"). Tooltip gains a "Cumulative operational /
  累计运营" line. Legend gains an amber line swatch entry ("Cumulative
  operational (stock)" / "累计运营（存量）").
- The capacity-vs-facility toggle and per-column hover tooltips already existed
  from earlier slices; this slice extends both to cover the overlay.

## §4.4 Scoped operators

- **Detail modal**: the Developer field is now a button styled as an amber
  dotted-underline link. Clicking it runs `scopeToOperator(name)`: closes the
  modal, clears any country scope (worldwide), sets the §3.1 registry search box
  to the operator name, re-renders, and scrolls to the registry. The §3.3 URL
  hash picks it up automatically (`#q=Scala+Data+Centers`), so the scoped view
  is shareable. The `owner` field stays plain text on purpose — the registry
  haystack indexes `developer`, not `owner`, so an owner search would 0-match.
- **Operator leaderboard**: every named row is clickable (plus `role="button"`,
  `tabindex="0"`, Enter/Space) through the same `scopeToOperator`, making the
  leaderboard navigation per the plan. The "Unknown operator" bucket is excluded
  — it is an aggregate label, not a searchable developer string.
- **Not done — per-country top-10 developers** (`dev_acc` scoped inside
  `country_acc`): requires the exporter change named in §4.4 bullet 1; out of
  contract for this slice (no data changes).

## Pre-existing defect found & fixed in passing (same file, chart-critical)

The page has two `<style>` blocks: the main one is Astro-**scoped** (selectors
compile to `.x[data-astro-cid-…]`), and a `<style is:global>` block whose own
comment says runtime-injected nodes "never receive Astro's scoped-style
attribute". All funnel/wave/operator/modal-field rows are injected via
`innerHTML`, so their rules in the scoped block never matched: funnel bars were
invisible (stuck at `width: 0`), wave columns stacked top-down in the wrong
order (`column-reverse` lost), operator rows and modal `dt/dd` lost their grid,
and tooltip title lines lost their weight. Verified against a clean build of
HEAD (`git stash` → build → computed `display: block` on `.wcol`/`.drow`), so
this predates slice 7. Fix: moved those rule groups **verbatim** (funnel `.frow…`,
wave `.wcol/.wseg/.wtot/.wx span`, operators `.drow…`, `#tip .t1/.t2`,
`.estbadge`, `.dc-modal-body dt/dd/a`, `.dc-note`, and their three media-query
overrides) into the existing global block, following the repo's established
pattern (cmdk + ticker styles already live there for exactly this reason).
New slice-7 rules were written straight into the global block. Other injected
UI outside this slice's charts (registry rows, country grid, evidence key, map
side panels) may have the same class of issue — worth an audit slice.

## Verification

1. `npm run build` — pass.
2. Playwright (chromium) against the built site served under the `/datacenters/`
   base: funnel bars + ratios + tooltip render; wave columns bottom-anchored
   with amber cumulative line (13 points), y-axis 613→0, tooltip shows
   cumulative; all checked in light/en and dark/zh, `?noanim`, zero page errors.
3. Operator flow: leaderboard "Microsoft" click → search box `Microsoft`,
   "Showing 185 of 10,669 records", hash `q=Microsoft`. From a Brazil-scoped
   view, modal Developer link "Scala Data Centers" → scope cleared, 17 records
   worldwide, hash `q=Scala+Data+Centers`.
4. `git diff` grep — no internal path leaks; only `astro/src/pages/index.astro`
   modified (+ this notes file; screenshots in `scratch/slice7-*.png`).

## Observed, not touched

- One detail record renders "NaN MW" capacity in the modal (e.g. the Fermi
  America record) — the value arrives non-numeric from the per-slug JSON; the
  capacity render path is untouched by this slice. Data-side fix.
