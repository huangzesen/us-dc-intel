# Slice 8 — Time scrubber (§3.4) + self-hosted Leaflet (§6.3)

Files touched: `astro/src/pages/index.astro` (only source change), new static
assets under `astro/public/vendor/leaflet/`. No data changes.

## A) Time scrubber (§3.4)

A year bar sits at the top of the GEOGRAPHY card, above the map: a ▶ play
button, a range slider (2018 → 2030 plus a rightmost **ALL** stop), the active
window label (`≤ 2024` / `ALL YEARS`), and a coverage note.

**Which date field it scrubs.** The registry rows carry a single `year` field
(the "year-signal": announced / operational year, whichever the corpus
recorded). The scrubber filters on `year <= selected`, cumulatively, matching
the plan's "capacity with year-signal ≤ selected year" semantics.

When a year is selected:

- **Registry** filters to rows with a year-signal inside the window (composes
  with the existing status/geo/search filters; the "Showing X of Y" line
  reflects it).
- **Map markers** re-weight: aggregates are recomputed client-side from the
  corpus rows for the current scope (countries worldwide, states/counties in
  the US drill, subnationals elsewhere). Marker size and color band follow the
  scrubbed capacity; empty geographies drop out. The map title gains a
  `· ≤ YEAR` suffix and the note explains the filter. Scrub steps rebuild
  markers **in place** (no `flyToBounds`), so the viewport never jumps while
  dragging or during autoplay.
- **Facility dots** (§5.3 layer) rebuild with the same filter when visible.
- **Wave chart** keeps the full timeline but dims columns past the selected
  year (the §3.4 "wave highlight").
- **URL hash** gains `y=YYYY` (plan §3.3 integration): deep links like
  `#c=US&y=2023` restore scope + scrubber; back/forward re-applies it.

**▶ Autoplay** sweeps 2018 → 2030 in ~8 s (13 steps × 615 ms), then stops at
≤ 2030; pressing again restarts from 2018. Under `prefers-reduced-motion` (or
`?noanim`) the button advances one year per press instead of animating (§8
reduced-motion audit). Activating the scrubber triggers the deferred-corpus
fetch (aggregates would otherwise be computed off the 60 flagship rows); when
the corpus lands mid-scrub the map re-weights in place.

### Documented limitation

Only **1,653 of 10,669** rows (~15%) carry a year-signal; the rest cannot be
placed on a timeline, so they are hidden while scrubbing and reappear at ALL.
The year bar's note states this on the page. The plan's fuller fix — exporting
per-state/per-subnational `years` matrices (`export_astro_data.py`) — is
export work, out of scope for this slice ("do not change the data"); the
client-side aggregation used here slots under those matrices unchanged if they
ship later. The hero counters do not re-count during autoplay (the plan's
"counters re-count" flourish) because scoped totals for undated rows cannot be
derived without that export.

## B) Self-hosted Leaflet (§6.3)

- Leaflet 1.9.4 `leaflet.js`, `leaflet.css`, the five `images/` sprites the
  CSS references, and the BSD-2 `LICENSE` now live in
  `astro/public/vendor/leaflet/`. Downloaded files were verified against
  Leaflet's published SRI hashes
  (js `sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=`,
  css `sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=`).
- `index.astro` references them via `BASE_URL` (`vendor/leaflet/…` under the
  `/datacenters/` mount); both unpkg references are gone. Attribution is
  unchanged: the Leaflet prefix plus © OpenStreetMap © CARTO still render in
  the attribution control.
- The plan's lazy-init half of §6.3 ("defer") was not taken in this slice —
  the slice contract scoped B to self-hosting; the script tag keeps the same
  synchronous position as the CDN one did, so behavior is unchanged.
- Only remaining external requests are the CARTO basemap tiles, which §6.3
  explicitly carves out.

## Verification

1. `npm run build` — **pass**.
2. Headless-browser smoke test against `dist/` served under `/datacenters/`
   with **all non-localhost requests blocked** (offline/no-CDN condition):
   Leaflet loads (`window.L`, map pane, attribution present); scrub to 2024 →
   registry "Showing 578 of 10,669 records", hash `#y=2024`, map title
   suffixed, 6 wave columns dimmed, map-side top value 171.1 GW (vs
   1,180.2 GW at ALL); scrub to 2019 → 243 rows / 62.7 GW; reset to ALL
   restores everything and clears the hash; deep link `#c=US&y=2023` restores
   (422 of 2,379 US rows, slider at 2023); autoplay runs ⏸/▶ correctly and
   stops at ≤ 2030. Zero page errors; only blocked hosts were the four
   `basemaps.cartocdn.com` tile subdomains.
3. Built output contains no `unpkg` (or any CDN) reference;
   `dist/vendor/leaflet/` ships js + css + images + LICENSE.
4. One bug was caught and fixed by the smoke test: the slider's `input`
   handler stopped autoplay first, and the stop path's UI sync rewrote the
   slider position from state before the drag value was read — manual drags
   were no-ops. The handler now captures the value first, and the stop path
   early-returns when no autoplay is running.
