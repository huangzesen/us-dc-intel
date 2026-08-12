# GRIDWATCH — UI/UX Improvement Plan

**Target:** `astro/src/pages/index.astro` (+ `scripts/export_astro_data.py`) · live at `https://xhelio.ai/datacenters/`
**Date:** 2026-08-12 · **Data basis:** 12,233 facilities · 241 countries with projects · 2,162.7 GW (857.3 tracked + 1,305.4 estimated)
**Goal:** keep the approved "National Grid Operations Room" art direction (see `design-proposal.md`) and push it from *good dashboard* to *"very very cool" instrument* — while fixing the structural problems that the corpus's growth from 2,731 US centers to 12,233 worldwide facilities has created.

---

## 0. Current-state audit (what's working, what broke)

**Working well — keep and build on:**
- The control-room aesthetic: mono numerals, blueprint grid texture, amber signal accent, indexed kickers (`00 GEOGRAPHY` …), count-up hero, energizing bars. This identity is distinctive; nothing below replaces it.
- Full token-driven dark/light theming and the EN/中文 pattern.
- The scope model (All → country → US state → county) with cross-filtering between map, funnel, wave, and table.
- CVD-validated status palette and sequential blue ramp.

**Broken or outgrown — the plan's targets:**

| # | Problem | Evidence | Severity |
|---|---|---|---|
| 1 | **7.7 MB of JSON inlined in one HTML page** — `datacenters.json` (3.9 MB) + `dc-metadata.json` (3.8 MB) are both embedded as `<script type="application/json">` blobs (`index.astro:1630-1631`). First paint waits on the whole payload; mobile users on 4G wait ~10 s+. | `astro/src/data/` file sizes | **P0** |
| 2 | **Registry renders all 10,669 rows to the DOM** — `renderTable()` maps every scoped center into `innerHTML` (`index.astro:2237`), ~65k DOM nodes on load. The footer copy still claims it shows "flagship records" (`index.astro:1624`), which was true at 60 rows, not 10,669. | `index.astro:2228-2245` | **P0** |
| 3 | **Branding says "Americas", data is the world** — title, hero kicker, `allAmericas` labels, footer all say Americas (`index.astro:17,1418,1443`), but the corpus now spans 241 countries incl. non-Americas. The "countries explored" stat tile compares a number to itself (`{countries_explored} / {countries_explored}` = always 100%, `index.astro:1469`). | grep "AMERICAS" | **P0** |
| 4 | **Light OSM raster tiles inside a dark control room** — the Leaflet map uses default OpenStreetMap tiles (`index.astro:1856`) on a hardcoded `#0a0d12` container (`index.astro:483,521`). In dark mode the bright beige map is the single loudest thing on the page and the only element that ignores the theme; in light mode the hardcoded dark container leaks around the tiles. | screenshot of any dark view | **P0** |
| 5 | **Marker colors break the color system** — `markerColor()` uses a blue→green→amber→red capacity scale (`index.astro:1746-1752`). Red collides with `--st-rej` (rejected), green with operational, amber with the chrome accent; and it's hardcoded so light mode gets dark-mode hexes. Violates the proposal's own "color is data" rule. | `index.astro:1746` | **P1** |
| 6 | **Country switcher = 241 buttons in a scroll strip** — `buildCountrySwitch()` emits one button per country (`index.astro:1970-1977`); finding e.g. "Kenya" means scrolling a 30-screen-wide strip. | `index.astro:1446` | **P1** |
| 7 | **Operators panel ignores the country scope** — `buildDevs()` always reads global `DATA.developers` (`index.astro:2162`); select Brazil and the leaderboard still shows the world top-10. Every other section scopes. | `index.astro:2162` | **P1** |
| 8 | **No shareable state** — theme/lang persist, but country/state/metric selections don't survive reload and can't be linked. | `index.astro:1687` | **P1** |
| 9 | Leaflet ships from unpkg CDN (`index.astro:16,1632`) — external dependency, contradicts the "zero external requests" success criterion; also render-blocking CSS. | | P2 |
| 10 | Tooltips are mouse-only; modal has no focus trap; sort carets are the only sort affordance. | `index.astro:1787` | P2 |

---

## 1. Priorities at a glance

| Tier | Theme | Items |
|---|---|---|
| **P0 — Foundation** (do first; everything else sits on it) | Performance + correctness | Payload split & lazy data (§6.1-6.3), registry virtualization + search (§3.1), world rebrand (§2.1), dark map tiles (§5.1) |
| **P1 — Instrument feel** (the "cool" core) | Map + interactivity | Themed markers & glow (§5.2), country command palette (§3.2), scoped operators (§4.4), URL state (§3.3), time scrubber (§3.4) |
| **P2 — Wow layer** | Visual & data-viz | Facility dot layer (§5.3), hero upgrade (§2.2), funnel conversion rates (§4.1), ticker strip (§2.4), section scroll-spy (§2.3) |
| **P3 — Polish** | Mobile, a11y, details | §7, §8 |

Effort key: **S** ≤ ½ day · **M** ~1 day · **L** 2-3 days.

---

## 2. Visual design & layout

### 2.1 Rebrand from "Americas" to worldwide (P0 · S)
- Title → `GRIDWATCH — Global Data Center Buildout Intelligence`; brand sub → `GLOBAL DATA CENTER INTEL / 全球数据中心情报`; hero kicker → `TRACKING THE GLOBAL COMPUTE BUILDOUT / 追踪全球算力大基建`; `allAmericas` → `Worldwide / 全球`.
- Fix the self-comparing stat tile (`index.astro:1469`): replace with **`241 countries & territories with projects`** (and keep `countries_explored` only if the exploration denominator becomes meaningful again — otherwise drop the progress bar).
- Rationale: nothing undermines "situational-awareness instrument" faster than the instrument mislabeling what it watches. This is copy-only; zero risk.

### 2.2 Hero: make 2.16 TW feel like 2.16 TW (P2 · M)
The hero number crossed a unit boundary — celebrate it:
- Auto-unit: ≥1,000 GW display as **`2.16 TW`** with a small `= 2,162.7 GW` sub-line. A terawatt reads as an event; 2162.7 reads as a typo.
- Replace the plain-text tracked/estimated split (`index.astro:1452`) with a **two-segment micro-bar** under the big number (solid blue = tracked 857 GW, hatched/40%-alpha blue = estimated 1,305 GW, direct labels). One glance shows both scale *and* epistemic honesty — currently the split is a mumbled parenthetical.
- Odometer-style digit roll for the count-up (each digit column slides; ~30 lines of CSS/JS, respects `prefers-reduced-motion` via the existing `noMotion` path).
- Add one context line that rotates per load between 2-3 precomputed comparisons from the export (e.g. "≈ 2× total US grid summer peak capacity") — comparisons are what make strangers say "whoa"; bake them into the JSON so no client math.

### 2.3 Section rail / scroll-spy (P2 · S)
The `00-06` indexed kickers already exist; surface them as a **fixed right-edge rail** (desktop ≥1240px only): tiny mono `00…06` markers, active section in amber, click to jump. Cheap (IntersectionObserver already on the page), and it makes the page feel like a multi-panel console rather than a scroll of cards.

### 2.4 Signal ticker under the topbar (P2 · M)
A single-line, slowly auto-scrolling mono strip: `▲ ABILENE TX · 1.2 GW · CONSTRUCTION ● NEW: KEEYASK MB · 500 MW ANNOUNCED …` built from the top-N recent/largest rows already in the payload. Pauses on hover, hidden on mobile and under `prefers-reduced-motion`. This is the Bloomberg-terminal signature move and costs one flex row.

### 2.5 Typography accent (P3 · S)
Keep system mono for all data, but self-host **one subset woff2** (digits + uppercase only, ~15-25 KB — e.g. IBM Plex Mono SemiBold) used solely for the hero figure and stat-tile values. Preload it; `font-display: swap`. The proposal's "no webfonts" rule was about CDN dependence — a subset in `astro/public/` keeps the page self-contained while giving the hero a face that isn't Menlo.

---

## 3. Interactivity

### 3.1 Registry: virtualize, search, paginate (P0 · M)
- **Render a window, not the corpus**: keep `currentRows` (already maintained, `index.astro:2236`) as the full sorted/filtered list, but paint only the first 100 `<tr>` + a `LOAD 100 MORE ▾` row (or IntersectionObserver infinite append). DOM drops from ~65k nodes to ~600; sort/filter latency becomes imperceptible.
- **Add a free-text search input** to the filter bar matching project + developer + county/subnational (the fields are all in memory; a lowercase-includes scan over 10k rows is <5 ms). With 10,669 rows, browse-only is unusable; search makes the registry the page's lookup tool.
- Fix the count/footer copy: `Showing 100 of 10,669 records` and footer "registry shows the full corpus (10,669 records with capacity signal)".
- Add a **developer filter** (or make operator-leaderboard rows clickable → sets the search box) — see §4.4.

### 3.2 Country command palette (P1 · M)
Replace the 241-button strip with:
- The strip keeps only **Worldwide + top 10 by capacity** (covers ~90% of clicks), then one `⌘K SEARCH ALL 241 …` chip.
- The chip (and `⌘K`/`/` hotkey) opens a **command-palette modal**: type-ahead over countries *and* US states *and* the 10k projects; rows show `US · United States · 1,102.4 GW`; Enter selects scope or opens the project modal. Reuse the existing `dc-modal` chrome so it inherits theming.
- This is the single feature that makes power users feel the site is an instrument: everything reachable in two keystrokes. Data is all client-side already — no backend needed.

### 3.3 Shareable URL state (P1 · S)
Serialize `country / state / mapMetric / waveMetric / status / q` into the hash (`#c=BR&m=n`) on change; parse on load before first render. Analysts screenshotting the site today literally cannot link to "Brazil view." ~40 lines; also makes browser back/forward work as scope navigation.

### 3.4 Time scrubber (P1 · L)
The buildout's *story* is temporal, but time lives only in one chart. Add a **year slider (2018 → 2030) above the map**:
- Dragging it filters the wave highlight and re-weights map markers to capacity with year-signal ≤ selected year; a ▶ button auto-plays 2018→2030 over ~8 s (markers grow, counters re-count).
- Requires export work: emit a `years` matrix per state and per country-subnational (the per-country matrix already exists — `export_astro_data.py:645-648`; extend `state_acc`/`county_acc` the same way; ~+80 KB payload if limited to states+countries).
- Watching the map light up year by year is the "very very cool" moment people will screen-record and share. Ship it behind the play button so the default view stays calm.

### 3.5 Micro-interactions (P3 · S)
- Table rows: 2px left border in status color on hover (reinforces the encoding).
- Filter chips animate in/out (100 ms scale+fade).
- `Esc` clears scope selection when no modal is open; `t` toggles theme (documented in a `?` hotkey popover — control-room operators get hotkeys).

---

## 4. Charts & data-viz

### 4.1 Funnel: show the physics, not just the bars (P2 · S)
- Between adjacent bars, print the **stage-to-stage capacity ratio** in muted mono (`→ 41%`), and headline the already-computed planned-vs-live multiple ("a 7.7× wave still to land" framing from the proposal). The funnel currently states magnitudes; conversion is the insight.
- Add a per-bar tracked/estimated split (same hatched treatment as the hero) so the estimate methodology stays visible where it matters most.

### 4.2 Wave: cumulative operational overlay (P2 · M)
Overlay a thin amber **cumulative operational-GW line** (SVG polyline over the existing column div stack) on the 2018-2030 chart. The stacked columns show flow per year; the line shows the stock actually energized — the gap between the pipeline stack and the line *is* the story. Amber is correct here: it's the "power actually flowing" signal, not a data series that competes with the status palette.

### 4.3 Country strip-chart in the geography panel (P2 · M)
When `Worldwide` is selected, the `countrygrid` bar-list (`index.astro:1998-2013`) is the weakest visual on the page (241 near-identical cards). Replace the top of it with a **capacity-ranked horizontal bar chart of the top 15 countries** (reusing the operator-leaderboard component, single-hue ramp, direct labels, tracked/est split), followed by a collapsed `SHOW ALL 241 ▾` grid. Ranked comparison is the question visitors actually have ("who's #2 after the US?"); a wall of cards can't answer it at a glance.

### 4.4 Operators: scope + drill (P1 · M)
- Export per-country top-10 developers (`dev_acc` scoped inside `country_acc`, `export_astro_data.py:653`) and make `buildDevs()` read the scoped list — fixes audit item #7.
- Make each operator row **clickable → filters the registry** to that developer (sets the §3.1 search box). The leaderboard becomes navigation, consistent with "map click = cross-filter."
- Optional (P3): 13-point sparkline per operator (year-signal counts) rendered as a tiny inline SVG — export a `years_n` array per top developer.

### 4.5 Evidence strip: make the receipts scoped and honest (P3 · S)
Scope the evidence bar to the selected country (needs per-country `evidence_acc` in the export), and annotate the hero micro-bar's "estimated" segment with a link that scrolls to a one-line method note ("missing capacities filled with country-mean; see split everywhere it matters").

---

## 5. Map experience (the biggest cool-per-effort wins)

### 5.1 Dark-matter basemap, theme-synced (P0 · S)
Swap OSM raster for **CARTO basemap tiles** and bind them to the theme toggle:
- Dark: `https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png` · Light: `…/light_all/…` (both free with attribution, `{r}` gives retina).
- On `setTheme()`, swap the tile layer URL; fix the two hardcoded `#0a0d12` backgrounds (`index.astro:483,521`) to `var(--bg)`.
- Effect: the map stops being a beige hole in the console and becomes the console's main screen — glowing markers on a near-black world map is 80% of the "NORAD wall" fantasy for ~20 lines of code. This is the highest cool-per-line change in the whole plan.

### 5.2 Marker system: one encoding, with glow (P1 · M)
- Replace the ad-hoc red/amber/green scale (`index.astro:1746`) with the **sequential blue capacity ramp** (`--b1…--b4` tokens, theme-aware) — size already encodes the active metric, color now encodes capacity band coherently with the tile cartogram legend.
- Reserve **amber** for exactly one thing: the currently-selected geography's marker (selection = energized).
- Add glow: render markers on a `L.canvas()` renderer with a soft radial shadow (`shadowBlur` ≈ radius, same hue). Canvas also future-proofs marker count for §5.3.
- Popup polish: mono digits, status-colored top-3 list, and a `FOCUS →` button (today clicking the marker both opens the popup and re-scopes, which is jumpy; make scope-change explicit).

### 5.3 Facility dot layer at high zoom (P2 · L)
Today the map bottoms out at county centroids. Add a **facility-level dot layer** (one dot per registry row) that fades in past zoom ~7:
- Coordinates: reuse county centroid + deterministic golden-angle jitter (the pattern already exists for subnational anchors, `index.astro:1874-1881`); export `lat/lng` per center (county lookup is already in `export_astro_data.py:557`). Mark them "approximate" in the popup, consistent with existing honesty conventions.
- Render on the canvas renderer (10k circle marks is fine on canvas; it is *not* fine as SVG/DOM).
- Dot color = **status palette** (at facility grain, status is the interesting variable; capacity ramps stay at aggregate grain). Click → the existing DC detail modal.
- Payload cost: ~2 floats × 10k ≈ 160 KB pre-gzip in the lazy `centers` chunk (§6.2) — acceptable.

### 5.4 Map/table layout upgrade (P3 · M)
At ≥1240px, offer a `⛶ EXPAND` layout state (short of fullscreen) where the map grows to ~70vh with the registry docked beside it as a synced list — an "operations view." The fullscreen button exists (`index.astro:1492`); this is the windowed middle state that keeps context visible.

---

## 6. Performance (P0 — prerequisite for everything feeling cool)

Fast *is* the aesthetic: a control room that stutters is a broken prop. Current worst case: ~7.7 MB HTML + render-blocking unpkg CSS + 65k-node table ⇒ multi-second first paint, worse on mobile.

### 6.1 Evict `dc-metadata.json` from the page (S · −3.8 MB)
It's only read in `openDcDetail()` (`index.astro:2263`). Have the export write **per-slug files** `astro/public/dc/<slug>.json` (write_dc_metadata already has the map; emit files instead of one blob) and `fetch()` on modal open with a 150 ms skeleton state + in-memory cache. Nobody notices modal data arriving 80 ms late; everybody notices 3.8 MB up front.

### 6.2 Split the main payload: aggregates inline, corpus deferred (M · −3.5 MB initial)
- Keep inline (~150-250 KB): `totals`, `countries` (with funnel/years/subnationals), `states`, `funnel`, `years`, `developers`, `evidence`, `flagship` (60 rows), `status_labels`. Hero, cartogram, funnel, wave, operators, and a 60-row registry paint immediately.
- Defer `centers` (10,669 rows) + `counties` to `astro/public/data/centers.json`, fetched after `DOMContentLoaded` (or on first registry interaction); table shows flagship rows with a shimmer until it lands, then `renderTable()` re-runs.
- In the deferred chunk, **shorten keys** (`project→p, developer→d, capacity_mw→mw, …`) and drop per-row `country` redundancy by grouping — roughly −35% pre-gzip.

### 6.3 Self-host + defer Leaflet (S)
Copy leaflet 1.9.4 css/js into `astro/public/vendor/` (kills unpkg dependency + its DNS/TLS round-trips; restores the "zero external requests" criterion except map tiles). Lazy-init the map via the existing IntersectionObserver when `#realMap` approaches the viewport — Leaflet stops blocking first paint entirely.

### 6.4 Ship compressed (S)
Ensure the host serves precompressed assets: emit `.br`/`.gz` siblings at build (astro-compress or a 5-line postbuild script). JSON compresses ~6-8×; combined with §6.1-6.2 the first-load transfer goes from ~8 MB to **≈ 250-400 KB**.

**Budget after this section:** first paint < 1 s on 4G, interactive < 2 s, Lighthouse perf ≥ 90 mobile. Verify with `npx lighthouse` before/after and record numbers in the patch notes.

---

## 7. Mobile responsiveness (P2-P3)

1. **Sticky mini-hero** (S): on scroll past the hero, compact the topbar to `⚡ 2.16 TW · 12,233 FACILITIES` in mono — keeps the headline number on screen (it's the brand) and doubles as scroll-to-top.
2. **Countrybar → palette** (S): below 680px the top-10 strip collapses to a single `🔍 WORLDWIDE ▾` button opening the §3.2 palette full-screen (bottom sheet). 241-button horizontal scroll on a phone is the current worst mobile interaction.
3. **Registry cards** (M): below 680px render rows as **stacked cards** (project + status chip on line 1, mono capacity + bar line 2, geo + year muted line 3) instead of an 820px-wide horizontal-scroll table (`index.astro:1046`). Cards also give bigger tap targets for the detail modal.
4. **Map interactions** (S): keep `scrollWheelZoom: false`, add two-finger-pan hint overlay ("use two fingers to move the map", standard Leaflet gesture-handling pattern) so the map stops hijacking page scroll on touch; bump `min-height` to `min(70vh, 480px)` in landscape.
5. **Tooltip → tap** (S): on coarse pointers, `mousemove` tooltips (`index.astro:2041`) never fire usefully — switch wave columns/tiles to tap-to-toggle a pinned tooltip that a second tap dismisses.
6. **Hero clamp** (S): `clamp(56px, 9vw, 104px)` leaves the TW figure cramped on 360px screens once the micro-bar (§2.2) is added — drop the floor to 44px and let the unit wrap under.

---

## 8. Polish, accessibility, credibility (P3 unless noted)

- **A11y — modal** (S): focus-trap the DC modal + palette (focus first control on open, return focus on close); add `role="dialog"` keyboard cycling. Esc already works.
- **A11y — live regions** (S): `aria-live="polite"` on `#fCount` and the hero counter block so scope changes are announced.
- **A11y — keyboard tooltips** (S): tiles/wave columns are buttons/divs with hover-only info; mirror tooltip content into `aria-label` (data already at hand in the render loops).
- **Reduced-motion audit** (S): the ticker (§2.4), odometer (§2.2), and scrubber autoplay (§3.4) must all check the existing `noMotion` flag.
- **Empty/edge states** (S): a country with 1 facility currently shows a full funnel of zeros — collapse zero rows to a muted one-liner ("no pipeline recorded beyond N announced").
- **Number craft** (S): consistent `fmtMW` everywhere (the wave y-axis mixes `1.2k` and GW forms); tabular-nums is implicit via mono but add `font-variant-numeric: tabular-nums` for the sans fallbacks.
- **Social/meta** (P2 · S): add OpenGraph/Twitter tags + a generated dark-mode OG image (hero number + map glow screenshot at build). Every share of this site currently unfurls as a bare URL — for a site whose job is to impress, the unfurl is the first impression.
- **Print/PDF stylesheet** (S): light theme, no animations, map replaced by cartogram — analysts will paste this into decks.
- **Footer** (S): add corpus methodology link + "built from N sources" wording already present; fix stale "registry shows flagship records" line (see §3.1).

---

## 9. Suggested sequencing

| Wave | Contents | Effect |
|---|---|---|
| **1 (≈2 days)** | §6.1-6.4 payload/perf · §3.1 table virtualization+search · §2.1 world rebrand · §5.1 dark tiles | Site feels instant; map finally matches the art direction; copy stops lying |
| **2 (≈2-3 days)** | §5.2 marker system · §3.2 command palette · §3.3 URL state · §4.4 scoped operators · §4.3 top-15 country chart | Instrument-grade interactivity; every view reachable and shareable |
| **3 (≈3-4 days)** | §3.4 time scrubber · §5.3 facility dots · §2.2 hero upgrade · §2.4 ticker · §4.1-4.2 chart upgrades | The "screen-record and share" layer |
| **4 (≈1-2 days)** | §7 mobile · §8 polish/a11y/OG | Ship-quality everywhere |

Per the design contract in `design/SKILL.md`: prototype each wave's visual changes in `design-mockup.html` (or a variant) first, update `design-proposal.md` sections that drift, then port to `astro/`.

## 10. Success criteria

- First-load transfer ≤ 400 KB compressed; first paint < 1 s on 4G; Lighthouse mobile perf ≥ 90.
- A stranger understands "the world is building ~2.2 TW of data centers, here's where and who" in < 10 s.
- Any view (country/state/metric/filter/search) is one URL; any of 241 countries or 10k projects reachable in ≤ 2 keystrokes via ⌘K.
- Dark map + glow markers + year-scrubber autoplay produce at least one moment per session where the user says "whoa."
- All color encodings stay CVD-validated; every animated element respects `prefers-reduced-motion`; modal and palette fully keyboard-operable.
