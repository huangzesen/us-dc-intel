# Slice 6 — Signal ticker (§2.4) + shareable URL state (§3.3)

Date: 2026-08-12 · File changed: `astro/src/pages/index.astro` (only file touched)

## A) Signal ticker (§2.4)

A single-line, slowly auto-scrolling mono strip directly under the sticky topbar
(`.gw-ticker` / `#tickerTrack`), built entirely from the inline payload — no fetch.

**Content (34 items per copy, in order):**
1. Headline aggregates: `TRACKED CAPACITY 2.16 TW` (auto-TW past 1,000 GW, amber
   accent), `FACILITIES 12,233`, `COUNTRIES & TERRITORIES 241`, `SOURCE URLS 49,495`.
2. Top-5 countries by capacity: `#1 US United States · 1180.2 GW` … `#5 AU`.
3. Top-8 flagship rows by capacity: `▲ CARSON TX US · 17 GW · ANNOUNCED`
   (green ▲, county + state + country locator, status label).

**Mechanics:**
- Track holds **two identical copies** (`.gw-ticker-copy`, each with trailing
  padding equal to the item gap) and animates `translateX(-50%)` linearly for a
  seamless loop; duration scales with content width (~42 px/s, measured 94s) so
  the pace stays constant across languages.
- **Pauses on hover** (`animation-play-state: paused`).
- **Hidden on mobile** (`max-width: 720px`) and **under `prefers-reduced-motion`**
  (CSS `display:none` + the JS `noMotion` flag sets `hidden`, which also covers
  the `?noanim` escape hatch — the §7 reduced-motion audit item for the ticker).
- `aria-hidden="true"`: every figure repeats elsewhere on the page and the loop
  duplicates its own content, so the strip is decorative.
- Rebuilt on language change (`setLang` → `buildTicker()`); zh labels included.
- Reads `DATA.flagship` (not `DATA.centers`) so the strip stays stable when the
  lazy corpus swaps in.
- CSS lives in the existing `<style is:global>` block — the known page quirk is
  that runtime-injected nodes never receive Astro's scope attribute (see
  slice3/slice5 notes), so scoped rules would miss the injected items.

## B) Shareable URL state (§3.3)

**Schema — hash params, defaults omitted** (`#c=BR&m=n` style, per the plan):

| param | meaning | values | default (omitted) |
|-------|---------|--------|-------------------|
| `c`   | country scope | ISO code, validated against `countryByCode` | worldwide |
| `s`   | geo drill | US state abbr (drives `selState` + tile/marker selection) or subnational name for non-US (drives `fState`) | none |
| `m`   | map metric | `mw` \| `n` | `mw` |
| `w`   | wave metric | `n` \| `mw` | `n` |
| `st`  | status tab | `ann`/`pla`/`app`/`con`/`op` (validated) | all |
| `q`   | registry search | free text (URL-encoded) | empty |

**Behavior:**
- Parsed **before the first render pass** (the block sits ahead of the
  `setTheme`/`setLang` init that drives the initial build), so a shared link
  paints the right view directly.
- **Replace-written** on filter/metric changes (single `syncUrl()` hook at the
  end of `renderTable` covers status/state/search/drill; plus `setMapMetric`,
  `setWaveTab`), **push-written** once per scope change (`setCountry` suppresses
  the inner replace via `applyingUrl` and pushes one settled entry), so browser
  **back/forward walk the scope history**; a `popstate` handler re-applies the
  full state and re-renders.
- **Lazy-corpus race handled:** a geo value from the hash may only exist in the
  deferred `centers.json` (flagship rows cover few states/subnationals).
  `urlGeoPending` holds it — `buildFilters` applies it as soon as a matching
  option exists (corpus load re-runs `buildFilters`), and `urlStateHash()`
  includes the pending value so intermediate re-renders can't drop it from the
  URL. User interaction with the geo select or scope clears the pending value.
- Existing `?theme=`/`?lang=`/`?noanim` query params are untouched (state rides
  the hash; `location.search` is preserved on every history write).

## Verification (headless Chromium against the built site, served under `/datacenters/`)

1. `cd astro && npm run build` — **pass** (1 page, no warnings).
2. Ticker renders 34 items ×2 copies with real stats; track measurably moves
   (~42 px/s, `gw-tick` 94s); hidden with `reduced_motion=reduce` and at 420px
   viewport. *(First test run showed no animation + no corpus — artifact of
   serving dist at `/` instead of the configured `base: '/datacenters/'`; both
   pass when mounted correctly.)*
3. Round-trips: clicking BR → `#c=BR`; status+search → `#c=BR&st=con&q=campinas`;
   loading `#c=BR&st=con&q=campinas&m=n&w=mw` restores country button, status
   select, search box, both metric tabs. Loading `#c=US&s=VT` restores the VT
   drill after the corpus lands (`Showing 6 of 2,379`, VT tile selected).
   BR→IN then back → `#c=BR`/BR active; forward → `#c=IN`/IN active.
   Zero page errors.
4. No internal-path leak: repo grep for user/absolute paths in the changed file
   is clean.

## NOT touched
- §4 charts (funnel ratios §4.1, wave overlay §4.2, country chart §4.3),
  §4.4 scoped operators, §3.4 time scrubber, §2.2 hero micro-bar/comparisons,
  §2.3 scroll-spy rail, §2.5 typography, §5 map work beyond what already shipped.
- No data files, no exporter, no other source files; nothing deleted; no
  commit/push/PR.
