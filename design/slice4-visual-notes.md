# Slice 4 — P1 visual layer notes (§5.2 marker system + §2.2 hero)

**Date:** 2026-08-12 · **Files changed:** `astro/src/pages/index.astro` only (this notes file aside).
**Build:** `cd astro && npm run build` → **pass** (1 page, no warnings). Headless-browser smoke tests (Playwright/Chromium against the built `dist/`) → all pass, zero page errors.

---

## §5.2 Marker system

### Ramp mapping (color = capacity band, coherent with the tile cartogram)

The ad-hoc `markerColor()` blue→green→amber→red scale is gone. Markers (country, US state, US county, subnational) now use the sequential blue capacity ramp:

| Band | Threshold (`MW_BINS`, same as cartogram legend) | Fill token | Stroke token | fillOpacity |
|---|---|---|---|---|
| 0 | < 1 GW | `--b0` | `--b1` | 0.50 |
| 1 | 1–5 GW | `--b1` | `--b2` | 0.59 |
| 2 | 5–15 GW | `--b2` | `--b3` | 0.68 |
| 3 | 15–45 GW | `--b3` | `--b4` | 0.77 |
| 4 | ≥ 45 GW | `--b4` | `--b4` | 0.86 |

- Band = `binOf(item.capacity_mw, MW_BINS)` — the exact bins/tokens behind the US tile cartogram and its `<1 GW … 45+ GW` legend, so map and cartogram now speak one color language.
- **Size still encodes the active metric** (capacity/facilities, unchanged `markerRadius`); **color + opacity encode the capacity band** (higher band = deeper blue, more opaque). Stroke is the next-lighter ramp step for a lit rim.
- Tokens resolve via `getComputedStyle` at render time (`markerPalette()`), so light mode gets the light ramp instead of hardcoded dark hexes (fixes audit item #5).
- **Amber (`--acc`) is reserved for exactly one thing:** the currently-selected geography's marker (selected US state / selected subnational) — amber fill+stroke, weight 3 ("selection = energized"). The old white selection stroke is gone.

### Glow + renderer

- Markers draw on a custom canvas renderer (`GlowCanvas`, an `L.Canvas.extend`) whose `_updateCircle` pass wraps the parent draw in `shadowBlur = max(6, radius)` / `shadowColor = fillColor` — a soft same-hue radial glow, per spec. `padding: 0.5` keeps the glow from clipping at redraw-tile edges. Canvas also future-proofs marker counts for the §5.3 facility layer (not implemented here).
- **Theme flips restyle markers in place** (`syncMarkerTheme()` from `setTheme()`): styles are recomputed from the new tokens and applied via `setStyle`, no re-render, no viewport jump. Verified: dark shows `#0d366b…#86b6ef`, one click to light swaps to `#cde2fb…#0d366b`.

### Behavior preserved

- Click-to-focus unchanged (same handler: worldwide click → country scope, US state click → drilldown, etc.). Smoke test: firing a click on the BR marker sets `selCountry = "BR"`.
- Popups still bound; popup content/format untouched.
- Hover feedback kept (and now explicit, since canvas has no CSS `:hover`): mouseover bumps weight +1 / fillOpacity +0.18, mouseout restores the exact base style. Verified restore-idempotent.

## §2.2 Hero — TW odometer counter

- **Auto-unit:** ≥ 1,000 GW renders as TW with 2 decimals (`2.16 TW`); below that, GW with 1 decimal (country scopes). The unit label (`#heroUnit`) switches TW/GW live.
- **Honest sub-line:** in TW mode a mono `= 2,162.7 GW` line (`#heroEq`, hidden when empty) sits above the existing tracked/estimated split. The number is always the real `capacity_gw` from the payload — only the presentation animates.
- **Odometer:** each digit is a clipped column (`clip-path: inset(0)` — chosen over `overflow:hidden` because clip-path preserves the flow baseline, keeping the unit baseline-aligned) holding a 0–9 strip. The same cubic-ease count-up as before drives the value; each strip gets `translateY(-d × 1.02em)` (one `.big` line-height per digit) with a 90 ms transform transition, so discrete digit changes read as a roll — low digits spin, high digits glide. Leading digits zero-pad during the roll, odometer-style.
- **Re-animation:** runs on load, on scope change (`updateHero`), on language switch (`setLang → updateHero`), and on theme switch (`setTheme`, guarded by `heroRendered` so init doesn't double-fire). A token (`heroAnimToken`) cancels superseded animations.
- **Honesty + a11y + motion:** `#heroGW` carries `aria-label="2.16 TW"` with digit internals `aria-hidden`; the existing `noMotion` path sets final digits instantly (and the global reduced-motion CSS kills the strip transition).
- Verified in-browser: load → columns land on `2.16`, eq line `= 2,162.7 GW`; scope to US → re-rolls to `1.18` TW with `= 1,180.2 GW`.

## Explicitly NOT touched

- §5.3 facility dot layer, §3.2 command palette, §3.3 URL state, §3.4 time scrubber, §4 chart upgrades (funnel ratios, wave overlay, country strip-chart, scoped operators), §2.2's micro-bar and rotating comparison line (P2 items beyond this slice's counter scope), popup `FOCUS →` button (would change the click-to-focus contract this slice was told to preserve).
- No data, export-script, or payload changes; `markerRadius` sizing math unchanged; no new dependencies.

## Verification detail

1. `npm run build` — pass; new CSS present in the emitted stylesheet (`:global()` used for runtime-injected odometer nodes), inline script parses (`new Function` check).
2. Headless smoke (built site served under `/datacenters/`): 149 worldwide markers, all on the canvas renderer with `glow: true`, 5 distinct band fills matching theme tokens in both themes, opacity ramp 0.50→0.86; amber selected marker confirmed via BR → Rio Grande do Sul.
3. Hero odometer asserted digit-by-digit in both worldwide and US scopes; zero page errors across all runs.
4. Diff contains no internal paths (grep for user/machine paths in the modified file: 0 hits).
