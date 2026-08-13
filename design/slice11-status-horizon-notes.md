# Slice 11 — Status-based COMPUTE HORIZON (and year-scrubber removal)

Date: 2026-08-13

## Why

The `year` field is NULL for all ~9.5k non-US facilities (announcement-year
semantics for US only), so every year-driven view lied outside the US: the
COMPUTE HORIZON card (Slice 10) showed a US-only stacked area labelled as the
scope's total, and the year scrubber (Slice 8) silently hid most of the corpus
while scrubbing. The `status` field is globally populated (operational /
construction / approved / planned / announced, plus rejected / unknown), so
the horizon now reads status, and the scrubber is gone.

## A) COMPUTE HORIZON — commitment staircase

- **Data**: `scopedFunnel()` — the per-country `funnel` array the export
  already emits (`funnel_rows` in `scripts/export_astro_data.py`, keys
  `op/con/app/pla/ann` with `capacity_mw` + `count`). No new export fields
  were needed. Rejected and unknown are excluded upstream: `funnel_rows`
  only emits `STATUS_ORDER`, so they never reach the chart, and the total
  potential figure = op + con + app + pla + ann only.
- **Form**: cumulative staircase. Phases stack in commitment order
  [operational → construction → approved → planned → announced]; band *k* is
  a rect from its step (x = k/5) to the right edge, sitting on the cumulative
  sum of the more-committed bands. The top edge therefore climbs stepwise to
  the "final compute that might come online" total. Y-axis is capacity
  (GW/TW via the existing `fmtMW`), pinned to the all-phases total per scope
  so legend toggles morph bands without rescaling the axis.
- **Headline**: two animated meters — "X GW online now · Y GW total
  potential" (`hznNowNum` / `hznNum`, both count from their previous value
  and survive the GW→TW crossover via `dataset.v`), plus the per-phase
  breakdown chips underneath.
- **Interaction** (all preserved from Slice 10 mechanics):
  - hover/focus a phase column → band highlight + crosshair dot at the
    cumulative top + tooltip (phase capacity, project count, share,
    cumulative potential through that phase);
  - 5 legend toggle chips (`data-hzn-stage`, aria-pressed) — toggling zeroes
    the band and animates the stack; clicking a band/hotspot toggles the
    same phase (this doubles as the "status/phase filter chips" option from
    the task's part B);
  - hotspots keep `tabindex`/`aria-label` mirrors for keyboard/SR users.
- **Colors**: the existing status tokens `--st-op/--st-con/--st-app/
  --st-pla/--st-ann` (already used by the funnel, registry chips, and both
  themes) assigned in fixed commitment order — no new palette introduced.
- **X-axis**: five phase labels (color dot + bilingual label from
  `DATA.status_labels`), replacing the year ticks.

## B) Year scrubber removed

- Markup: `#yearBar` (play button, range input, labels) deleted from the map
  card; `.yearbar`/`.yb-*` CSS and the `.wcol.dim` wave-dim rules removed.
- JS: `scrubYear/scrubTimer/scrubActive/scrubMatch/scrubAggregates/
  scrubProject/setScrubYear/syncScrubUI/scrubStep/startScrubPlay/
  stopScrubPlay/resetScrubDots/syncWaveScrub/syncHorizonScrub/hznIndexFor/
  hznPick` all removed; map items, dot layer, registry filter, and map-side
  panel no longer re-weight by year.
- URL state: `#y=` dropped from `parseUrlState`/`urlStateHash`/init/popstate.
  Other hash params (`c/s/m/w/st/q`) unchanged; an old shared link with
  `y=` simply ignores that param.
- The horizon's click-to-scrub veil (`hznVeil`) went with it.

## C) Untouched

- The BUILDOUT WAVE bar chart (per-year flow columns + cumulative-operational
  overlay) is intact, including its metric tabs — it is explicitly labelled
  as "project signals by year" and remains a US-signal view.
- Funnel, map, operators, registry, evidence slices unchanged (beyond losing
  the scrub re-weighting, which restores full-dataset figures everywhere).

## Export script

One-line hardening in `status_key`: `"operating"` now maps to `op` (it
previously fell through to `unk`). The current DB has no such rows (a prior
normalization pass cleaned them — see `datacenters.db.bak-20260813-status-norm`),
so exported numbers are unchanged; this just keeps future re-imports honest.
`under_construction` was already caught by the `"construct" in s` test;
`coverage` intentionally stays `unk` (not a commitment phase) and is excluded.

## Verification

- `cd astro && npm run build` — passes.
- Headless-Chrome render of `dist` (served under `/datacenters/`):
  world scope shows **684 GW online now · 1.98 TW total potential**
  (op 683.9 / con 277.2 / app 181.7 / pla 646.6 / ann 189.5 GW, y-axis top
  1978.8 GW, ▲ total label at the top edge); `#c=CN` shows
  **74.8 GW online now · 158 GW total potential** with the real CN phase
  split (74.8 / 32.4 / 5.06 / 35.4 / 10 GW; 458/181/32/193/37 projects) —
  a non-US country now renders a truthful horizon instead of an empty one.
- `grep` of the built HTML: zero `yrRange/yearbar/hznVeil` remnants; no
  internal paths in the diff.
