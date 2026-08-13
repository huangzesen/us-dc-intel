# Slice 5 notes — facility dot layer (§5.3) + command palette (§3.2)

Date: 2026-08-12 · Files changed: `astro/src/pages/index.astro` only (+339/−3).

## A) Facility dot layer (§5.3)

**Coordinates.** The lazy corpus rows (`astro/public/data/centers.json`, 10,669 rows)
carry **no lat/lng** — the task brief said they do, but they don't; only the
`counties` array (1,156 US counties) and the inline country/state aggregates have
coordinates. So, per the §5.3 spec ("reuse county centroid + deterministic
golden-angle jitter"), each dot anchors to:

1. its US county centroid (`counties` in the lazy chunk), spread ±0.045°;
2. fallback US state centroid (inline `states`), spread ±0.4°;
3. fallback country centroid (inline `countries`), spread ±0.8°.

Within an anchor group, dot *i* sits at golden-angle `i × 2.399963` rad on a ring
`spread × (0.25 + 0.75·√((i mod 64)/64))` — fully deterministic, no RNG. The hover
tooltip says "Approximate position (county/country anchor)" per the site's honesty
conventions. No data files were touched.

**Rendering.** One `L.circleMarker` per row on the existing §5.2 canvas renderer
(`realCanvas`), collected in a `layerGroup` built lazily on first show. Radius is
capacity-scaled (1.8–7 px, √MW). Color rides the same §5.2 blue ramp
(`--b0…--b4` via `markerPalette()`), but re-binned to facility grain
(`DOT_BINS = [30, 100, 300, 1000]` MW, picked from corpus quantiles — the
aggregate `MW_BINS` start at 1 GW and would flatten ~99% of facilities into band
0). Glow is off for dots (10k shadow-blurred arcs would hurt canvas frame time).
Theme flips restyle dots in place via the extended `syncMarkerTheme()`.

**Interactions.** Hover → site tooltip (`showTip`) with project name, location,
capacity, approximate-position note; click → the existing facility modal
(`openDcDetail(slug, row)`); mouseover style bump mirrors the aggregate markers.

**Visibility / degradation.** Dots are hidden until the lazy corpus lands
(`corpusReady`); until then the toggle chip is `hidden` too. After load a subtle
"● 10,669 FACILITIES" pill (bottom-left of the map, `.dotchip`) appears. The
layer attaches only past `DOT_MIN_ZOOM = 6` (spec: "fades in past zoom ~7"; 6
makes dots appear on country focus, whose flyTo caps at zoom 6). The chip
toggles the layer; enabling it below the zoom gate nudges the map to zoom 6 so
the toggle never appears to do nothing. `zoomend` drives attach/detach.

## B) Command palette (§3.2)

- **Open:** `Cmd/Ctrl+K` (window-level keydown, `preventDefault`), or the new
  "⌘K SEARCH" chip at the head of the country strip (delegated
  `data-cmdk-open`). Opening also calls `loadCorpus()` so facility search warms
  up; before the corpus lands only flagship rows match (graceful).
- **Search:** reuses §3.1 logic — `countrySearchNames` for countries,
  `rowHaystack(c)` (cached lowercase haystack) for facilities. Empty query shows
  top-10 countries by capacity; a query shows ≤6 countries + ≤12 facilities,
  both capacity-ranked. Rows render `SCOPE | US · United States | 1,102.4 GW`
  and `SITE | project · county, area, CC | MW`.
- **Keyboard:** ↑/↓ move the active row (wrapping), Enter selects, ESC closes
  (checked before the dc-modal in the shared keydown handler), backdrop click
  closes. Enter on a country calls `setCountry()` (guarded against the toggle
  behavior) and scrolls the map into view; Enter on a facility opens the
  existing detail modal.
- **Chrome:** markup reuses the `dc-modal` backdrop/z-index scheme with a
  compact top-aligned box; bilingual labels use the codebase's `langIndex()`
  ternary convention for runtime strings.

## Gotchas found while building

1. **Script-order crash:** the inline script runs before end-of-body, so palette
   markup placed after it made `getElementById("cmdk")` null and killed the whole
   script. The palette markup now sits just before the `gw-data` script tag.
2. **Pre-existing site-wide bug (NOT fixed here, worth a future slice):** the
   page's `<style>` is Astro-scoped (`[data-astro-cid-…]` on every selector
   part), but most of the UI is injected at runtime via `innerHTML` and never
   gets the scope attribute — so countrybar buttons, dev rows, table rows,
   `.en/.zh` toggling inside dynamic HTML etc. render **unstyled, on the live
   production site too** (verified against xhelio.ai/datacenters: countrybar
   buttons compute as default Arial). One-line candidate fix: `is:global` on the
   main style block. I did not apply it globally (out of slice scope); the new
   palette styles live in their own `<style is:global>` block instead, and both
   new runtime labels use `langIndex()` ternaries instead of `.en/.zh` spans.

## Verification

- `cd astro && npm run build` → **pass** (1 page, no warnings).
- Headless Chromium (Playwright) against the built site served under
  `/datacenters/`: corpus loads (10,669), toggle chip appears; dots visibly
  render/clear on toggle (screenshot-diffed) with capacity-banded blue dots over
  Brazil focus at zoom 6; dot hover tooltip shows name/location/capacity +
  approximate note; dot click opens the facility modal. Ctrl+K opens the
  palette; "prince william" → 12 SITE rows; ↓↓ + Enter opens that facility's
  modal; "brazil" + Enter re-scopes to BR (hero updates); ESC closes. Zero page
  errors across all runs.
- Diff check: only `astro/src/pages/index.astro` changed; no internal paths in
  the diff.

## Not touched

§4 charts (funnel/wave/operators), §3.3 URL state, §3.4 time scrubber, §6.x
performance items, the country strip contents (still full 241 + Worldwide; only
the ⌘K chip was prepended — the §3.2 "top-10 only" strip cut was not in this
slice's scope), the export pipeline, and all data files. No commits/pushes.
