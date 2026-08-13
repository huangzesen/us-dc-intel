# Slice 9 — P3 polish: mobile / a11y / OG (plan §7, §8)

**Scope:** `astro/src/pages/index.astro` + new `astro/public/og.png`.
**Build:** `cd astro && npm run build` → passes (1 page, ~1.5 s).

## 0. Regression fixed first: scoped CSS never matched injected DOM

While auditing mobile layout, screenshots showed large parts of the runtime UI
unstyled: the country switch rendered as fat default buttons, the worldwide
country cards and the whole US tile cartogram were default-gray `<button>`s,
registry rows had no cell padding / row borders / status-chip / capacity-bar
styling, map-legend and evidence-key rows lost their layout, and JS-injected
`.en`/`.zh` spans showed **both languages at once** (e.g. the "Countries with
projects有项目的国家" stat label).

Cause: those rules lived in Astro's scoped `<style>` and compiled to
`selector[data-astro-cid-…]`, which can never match nodes created at runtime
via `innerHTML`/`createElement`. (Slice 4 had already moved the chart/modal
rows to the `is:global` block for exactly this reason — these selectors were
missed.)

Fix: moved the affected rules verbatim into the existing `is:global` style
block, with pointer comments left at the old locations:

- `[data-lang="en"] .zh` / `[data-lang="zh"] .en` visibility
- `.countrybar button` (+ `.on`)
- `.geoitem` family (`.gt/.gn/.gv/.gbar`)
- `.tile` family (`.ab/.tv/.sel`) and `.b0`–`.b4` ramp classes
- `.legend .lg` / `.chart-legend .lg` / `.legend .sw`
- registry cells: `td`, `tbody tr:hover`, `td.proj/geo/yr/gr/cap`, `.capv`,
  `.capbar`, `.chip`
- `.evbar i` (reveal animation) and `.evkey .lg/.sw`
- `* { box-sizing: border-box }` (the scoped `*` also compiled to
  `[data-astro-cid]` only)

No values changed — this restores the design that already shipped. Verified
before/after with headless-Chrome screenshots (dark + light, 390 px + 1280 px).

## A. Mobile (§7)

- **§7.3 registry cards (≤680 px):** the table becomes stacked cards —
  `thead` hidden, `table/tbody` display block, each `tr.vrow` a 3-row grid
  (project + operator / capacity bar + right-aligned status chip / geo · year
  · evidence). Card height is pinned at 108 px (overflow hidden) so the §3.1
  virtualizer keeps working; `renderWindow` already adopts the measured row
  height, and the `resize` handler now resets `vMeasured` so crossing the
  breakpoint (rotation) re-measures. Verified at an emulated 390 px viewport:
  `display:grid`, 108 px rows, no horizontal overflow, all 6 fields legible.
- **§7.2 country strip (≤680 px):** collapses to the `⌘K SEARCH` chip + the
  active scope button (`.countrybar button[data-country]:not(.on)` hidden).
  The active button still toggles back to Worldwide, and the palette reaches
  all 241 countries. The `.cmdk` sheet goes full-width on phones.
- **§7.4 map touch:** on coarse pointers one-finger drag is disabled (page
  keeps scrolling; pinch-zoom still works, two fingers pan) and a translucent
  "USE TWO FINGERS TO MOVE THE MAP / 使用双指移动地图" overlay flashes on a
  single-finger drag attempt. Fullscreen re-enables one-finger panning.
  Landscape phones get `min-height: min(70vh, 480px)` for the map.
- **§7.5 tooltips on touch:** emulated mouse events already pin the tooltip
  on tap; added a coarse-pointer `touchstart` listener that dismisses it when
  tapping outside a chart element.
- **§7.6 hero clamp:** floor dropped 56 px → 44 px so the TW figure + unit
  fit 360 px screens.
- Yearbar wraps below 680 px (play/slider/label no longer overflow-cramped);
  ticker was already hidden ≤720 px and under reduced motion — unchanged.
- **Deferred (not "verify and fix" scope):** §7.1 sticky mini-hero is a new
  feature, not a layout fix — left for a future slice.

## B. Accessibility (§8 + audit #10)

- **Focus ring:** global `:where(button, input, select, a, th, tr,
  [tabindex]):focus-visible { outline: 2px solid var(--acc) }`; removed the
  `outline: none` that `.tile`/`.geoitem` set on focus-visible.
- **Dialog focus management:** DC modal and ⌘K palette now trap Tab (cycle
  within the open box), focus their first control on open (close button /
  search input) and return focus to the opener on close. Esc already worked.
  Verified via CDP: Enter on a row opens the modal with focus on close, Tab
  from the last control wraps to the first, Esc restores focus to the row.
- **Live regions:** `aria-live="polite"` on `#fCount`; new visually-hidden
  `#heroLive` span announces the settled hero figure ("2.16 TW tracked") on
  scope changes — the odometer digits stay `aria-hidden`.
- **Keyboard registry:** rows get `tabindex="0"` + Enter/Space opens the same
  detail modal as click; sortable headers get `scope="col"`, `tabindex="0"`,
  Enter/Space sorting, and live `aria-sort` (carets are now `aria-hidden`).
  Non-sortable headers get `scope="col"` too.
- **Mirrored tooltip content:** cartogram tiles get full
  `aria-label` ("Alaska · 14 facilities · 4.79 GW"); wave columns get
  `role="img" tabindex="0"` with the per-status breakdown as the label.
  Funnel rows already state stage/value/count as visible text.
- **Labels:** `aria-label` added to `#mapFull` and `#cmdkInput`; the
  state-filter clear chip gets a descriptive label alongside its "TX x" text.
- **Reduced motion:** audited per §8 — ticker (hidden), odometer (static),
  scrubber autoplay (single-step per press) already honor `noMotion`; no
  changes needed.
- **Contrast:** the plan calls for no specific contrast changes (palette is
  CVD-validated per §10); none made.

## C. Open Graph (§8 social/meta)

- `<head>` now carries `og:type/site_name/title/description/url/image`
  (+width/height/alt), `twitter:card=summary_large_image` +
  title/description/image, and a canonical link. Description is generated
  from the data export (capacity, facilities, countries, sources), so it
  tracks the corpus. Absolute URLs use the deployed origin
  `https://xhelio.ai/datacenters/`.
- `astro/public/og.png` — 1200×630 dark-theme card in the site's control-room
  style (grid texture, amber brand block, glow + dot field, 2.16 TW hero,
  tracked/estimated split bar, stats row). Prerendered with headless Chrome
  from a throwaway HTML card (not checked in); regenerate whenever the hero
  numbers move, or automate at build later per the plan's "generated at
  build" ideal.
- The page `<meta name="description">` was upgraded to the same data-driven
  text (was a static one-liner).

## Verification

1. `npm run build` → pass.
2. Headless-Chrome screenshots (dark + light): desktop country strip, US
   cartogram + legend, registry table with chips/bars restored; 390 px mobile:
   collapsed country strip, wrapped yearbar, hero fits, registry cards.
3. CDP functional checks: focus trap, focus return, keyboard sort, keyboard
   row → modal, live regions, `aria-sort`, wave/tile labels.
4. OG tags verified in `dist/index.html`; `og.png` is 1200×630 and ships in
   `dist/`.
5. `git diff` checked — no internal paths in the change.

## Known non-issues / out of scope

- Some countries display as "CN · CN" (name_en falls back to the code) — data
  export issue, untouched per the no-data-changes contract.
- Leaflet canvas markers remain mouse/touch-only; exposing them to keyboards
  needs a parallel DOM list and is beyond this slice.
