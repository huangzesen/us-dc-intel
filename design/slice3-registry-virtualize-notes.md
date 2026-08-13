# Slice 3 — Registry virtualization + search (§3.1)

**Date:** 2026-08-12 · **File changed:** `astro/src/pages/index.astro` only (165 insertions, 16 deletions) · **Build:** `cd astro && npm run build` → PASS

## Windowing approach

The registry table no longer materializes the corpus. `renderTable()` still computes
`currentRows` (scope → status → state/subnational → search filter, then sort) over the
full 10,669-row corpus in memory, but painting is delegated to a windowed renderer:

- `.tblwrap` became the scroll viewport: `max-height: min(70vh, 640px); overflow-y: auto`,
  with a sticky `thead` so the column headers (and their sort carets) stay visible.
- Fixed-height row model: every rendered row is `tr.vrow` at **57px** (CSS-pinned;
  `td.proj b` / `.own` get block+ellipsis so no row can wrap taller). On the first paint
  the code measures one real row via `getBoundingClientRect()` and adopts the measured
  height if collapsed-border rounding shifts it, so spacer math stays exact.
- `renderWindow()` computes `first = floor(scrollTop / ROW_H) − OVERSCAN` and paints
  `ceil(viewportH / ROW_H) + 2·OVERSCAN` rows (OVERSCAN = 8), framed by **two spacer
  rows** (`tr.vpad`, one `<td colspan=6>` each) whose heights are `first · ROW_H` and
  `(total − first − count) · ROW_H`. The scrollbar therefore represents the full corpus
  (scrollHeight ≈ 10,669 × 57 = 608k px) while the DOM holds only the window.
- Scroll events are rAF-throttled and re-render only when the `(first, count)` window
  actually changes; window resize invalidates the window. Filter/sort changes reset
  `scrollTop` to 0.
- Row identity: each `tr.vrow` carries `data-i` (absolute index into `currentRows`).
  The row-click → DC-detail-modal handler was switched from DOM-position indexing
  (which spacers/recycling would break) to `data-i`, so click-to-open-detail behaves
  exactly as before. Row markup/content is unchanged.

**Measured DOM bound (headless Chromium, 1280×720):** 25 rows in the DOM at rest
(9 visible + 16 overscan), 17 at the clamped bottom edge, +1–2 spacer rows — bounded
by `ceil(viewportH/57) + 16` regardless of corpus size (~29 at the 640px viewport cap,
~50 worst-case on a very tall fullscreen viewport). Down from ~10,669 `<tr>` / ~65k nodes.

## Search behavior

- New `#fSearch` input in the registry filter bar (mono styling matching the selects,
  lang-aware placeholder EN/中文).
- Case-insensitive substring match over **project name, developer, county,
  subnational/state, and country** — country matches the code *and* both display names
  (`"brazil"` finds `BR` rows via the inline countries aggregate). Haystacks are
  lowercased once per row and cached (`c._q`), so a keystroke is a single `includes`
  scan over ≤10,669 strings (<5 ms).
- Composes with the existing filters: country switch → status tab → state/subnational
  drill → search, all AND-ed, then sorted; the virtualized window renders the subset.
- Result count: `#fCount` now reads `Showing N of M records` (the stale "flagship
  records" copy is gone, per §3.1's copy fix; footer likewise now says the registry
  lists the full corpus).
- Clear: a `✕ clear search` chip appears while a query is active (alongside the
  existing state-clear chip); clicking clears and refocuses the input. An empty-result
  query renders a muted "No records match the current filters." row.
- Typing also triggers `loadCorpus()` (same lazy-load nudge the selects already had),
  so searching before the deferred corpus arrives still upgrades from flagship rows.

## Astro scoping caveat (discovered, worked around, NOT fixed)

Astro scopes the page's `<style>` (`sel[data-astro-cid-…]`), but all registry rows —
and in fact all of the page's `innerHTML`-generated content (geoitems, chips, funnel
rows…) — never receive the scoping attribute, so scoped rules silently miss them.
This pre-dates this slice (visible in the deployed slice-2 build: dynamic `td` renders
with 1px default padding). The new virtualization-critical rules are therefore written
with `:global(...)` so they demonstrably reach runtime rows; the pre-existing scoped
rules were left untouched. **Recommend a follow-up slice audits scoped-vs-dynamic CSS
page-wide** (likely `is:global` on the style block).

## Verification run (headless Chromium against `dist/`, served under `/datacenters/`)

- Build: PASS (`astro build`, 1 page).
- Worldwide, corpus loaded: `Showing 10,669 of 10,669 records`; 25 `tr.vrow` in DOM;
  scroll to middle → window starts at `data-i` 5326; bottom → last `data-i` 10668.
- Search `vantage` → 79 rows, every visible row matches; `brazil` → 96 rows (matches
  via country name → BR); clear chip restores 10,669.
- US scope + status `op` + search `texas` → 60 of 2,379; all visible rows in TX.
- Subnational drill (fState) still filters (6 of 2,379 for the first state).
- Row click opens the DC detail modal (`Meta Altoona Data Center`).
- No internal-path leak in the diff (`git diff` grep for user/home paths: clean).

## Not touched

§3.2 command palette, §3.3 URL state, §4 charts, §5.2 marker system, §6.3 leaflet
self-host (unpkg tags untouched), §6.4 compression, all P1/P2 items, the data files,
and the deploy pipeline. No files deleted; no commit/push. The registry `h2` still says
"Flagship projects" — heading copy wasn't in §3.1's copy-fix bullet; flagging it for
the next copy pass.
