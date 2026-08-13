# Slice 2 — Payload split (§6.1 + §6.2) — patch notes

Date: 2026-08-12. Implements `design/ui-improvement-plan.md` §6.1 (evict dc-metadata
from the page) and §6.2 (aggregates inline, corpus deferred). No other plan items
touched.

## Files changed

- `scripts/export_astro_data.py` — payload split + per-slug metadata emission.
- `astro/src/pages/index.astro` — lazy fetch of the deferred corpus and modal metadata.
- Diff: 274 lines (127 insertions, 19 deletions across the two source files).

Generated outputs (new, under `astro/public/`, copied verbatim into `dist/`):

- `astro/public/data/centers.json` — deferred chunk `{centers: [10,669], counties: [1,156]}`.
- `astro/public/dc/<slug>.json` — 2,860 per-slug DC detail files (slug names are
  filtered to `[A-Za-z0-9._-]+` before writing).

`astro/src/data/dc-metadata.json` is no longer written or imported; the stale file
remains on disk untouched (no-deletion contract) and is now unreferenced.

## Before / after sizes

| Artifact | Before | After |
|---|---|---|
| `dist/index.html` (first-paint HTML) | 7.3 MB | **828 KB** (847,391 B; ~94 KB gzip −9) |
| Inline `datacenters.json` | 3,928,759 B | 811,467 B |
| Inline `dc-metadata.json` | 3,781,820 B | 0 (evicted → 2,860 lazy files) |
| `dist/data/centers.json` (deferred) | — | 3,117,315 B (~427 KB gzip −9) |

The inline payload is 811 KB rather than the plan's 150–250 KB estimate because
`countries` alone (241 countries with subnationals/funnel/years, which §6.2 says to
keep inline for first paint) is 776 KB pre-gzip. Post-gzip the HTML is ~94 KB, inside
the §6.4 first-load budget once precompression (§6.4, not in this slice) ships.

## Fetch strategy

**Deferred corpus (`data/centers.json`, §6.2).** The inline JSON now carries
aggregates only; at boot the client sets `DATA.centers = DATA.flagship` (60 rows) and
`DATA.counties = []`, so hero, cartogram, funnel, wave, operators, and a 60-row
registry paint immediately. `loadCorpus()` fetches the chunk via
`requestIdleCallback` (2.5 s timeout; `setTimeout` 900 ms fallback) after init. While
pending, a pulsing `SYNCING FULL REGISTRY…` note (bilingual, reduced-motion-safe)
shows in the registry filter row. On arrival it swaps in the full arrays, rebuilds
`rowBySlug` / `countiesByState`, re-runs `buildFilters()` + `renderTable()`, and
re-renders the Leaflet layer only when the current scope is the US-state county
drilldown (the sole map view fed by deferred data — avoids yanking the viewport
otherwise). On fetch failure the note hides, the flagship rows remain usable, and any
registry filter interaction retries the load. All URLs are base-aware via a
`data-base={import.meta.env.BASE_URL}` attribute (site mounts at `/datacenters/`).

**Modal metadata (`dc/<slug>.json`, §6.1).** `openDcDetail()` renders the modal
instantly from the registry-row fields with a `Loading detail record…` note (this is
the skeleton state), fetches the per-slug file, and swaps in the full record when it
resolves — only if the modal is still open on the same slug. Results (including
404/`null`) are cached in an in-memory `Map`, so reopening is instant and rows
without a detail file show the existing "No detail record" note exactly as before.

Because the footer previously printed `data.centers.length`, the exporter now emits
`totals.registry_rows` (same number, 10,669) for the server-rendered footer line.

## Build + verification

1. `python3 scripts/export_astro_data.py` → OK (sizes above). `cd astro && npm run build` → **pass** (1 page, no warnings).
2. Inline-leak grep on `dist/index.html`: known corpus projects (e.g. "DAF AI Data Center - Clear Space Force Station", "GCI Anchorage Data Center") — **0 matches** inline, present in `dist/data/centers.json`.
3. End-to-end smoke via Playwright (chromium headless against `astro preview`):
   flagship-first paint 60 rows → lazy note hides → table re-renders 10,669 rows
   ("Showing 10669 of 10669 … full corpus: 12,233"); modal opens with skeleton and
   swaps to full detail (owner/developer/sources render); US country switch → 2,379
   rows, 52 cartogram tiles, 52 state filter options; **zero console errors**.
4. Path-leak check: diff and generated JSON clean of `/Users/`, `scratch/`, `daemons/`, `logs/`, `token_`.

Pre-existing quirk (not a regression, data untouched): `usdc-0153-fermi-america-…`
has a dict-valued `capacity_mw` in its detail record, so the modal shows "NaN MW" —
identical behavior with the old inline blob.

## Explicitly not touched

- §6.3 (self-host/defer Leaflet — still unpkg), §6.4 (precompressed assets), §3.x
  (registry virtualization/search), §5.x, and all P1/P2/P3 items.
- Data contents: byte-identical rows, just relocated. The §6.2 key-shortening idea
  (`project→p`, ~−35% pre-gzip) was deliberately deferred — this slice's contract
  forbids changing data contents, and gzip already takes the deferred chunk to
  ~427 KB; revisit alongside §6.4.
- No commits, pushes, or deletions; DB and gathering pipeline untouched.
