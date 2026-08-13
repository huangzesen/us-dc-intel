# Slice 1 notes — §2.1 world rebrand + §5.1 dark CARTO basemap

**Date:** 2026-08-12 · **File changed:** `astro/src/pages/index.astro` only (30 insertions, 22 deletions)

## 1. Changed lines (before → after)

### A) §2.1 Rebrand "Americas" → worldwide (copy-only)

| Line (orig) | Before | After |
|---|---|---|
| 13 | `<meta name="description" content="GRIDWATCH Americas data center buildout intelligence dashboard." />` | `…"GRIDWATCH global data center buildout intelligence dashboard."…` |
| 17 | `<title>GRIDWATCH — Americas Data Center Buildout Intelligence</title>` | `<title>GRIDWATCH — Global Data Center Buildout Intelligence</title>` |
| 1418-1419 | brand sub `AMERICAS DATA CENTER INTEL` / `全美洲数据中心情报` | `GLOBAL DATA CENTER INTEL` / `全球数据中心情报` |
| 1443-1444 | hero kicker `TRACKING THE AMERICAS COMPUTE BUILDOUT` / `追踪全美洲算力大基建` | `TRACKING THE GLOBAL COMPUTE BUILDOUT` / `追踪全球算力大基建` |
| 1469-1471 | self-comparing stat tile `{countries_explored} / {countries_explored}` + label `Countries explored · Americas / 已探索国家 · 全美洲` + `<div class="bar100"><i></i></div>` fake 100% progress bar | single honest stat `{data.totals.countries_with_projects}` (= 241) + label `Countries & territories with projects / 有项目的国家与地区`; progress bar removed |
| 1645 | i18n key `allAmericas: ["All Americas", "全美洲"]` | `worldwide: ["Worldwide", "全球"]` (usage at orig. 1973 updated to `L(I18N.worldwide)`) |
| 1657-1660 | i18n key `americasSub: ["Data-center buildout across the Americas, grouped by {countries_explored} explored countries and territories.", "覆盖全美洲…"]` | `worldwideSub: ["Global data-center buildout across {countries_with_projects} countries and territories with projects.", "覆盖全球 … 个有项目国家与地区的数据中心建设总盘。"]` (usage at orig. 1989 updated) |
| 1954 | map panel title `"Americas country highlights"` / `"全美洲国家亮点"` | `"Worldwide country highlights"` / `"全球国家亮点"` |
| 2011-2012 | cartogram note `"Countries across the Americas, sorted by magnitude…"` / `"全美洲国家列表…"` | `"Countries worldwide, sorted by magnitude…"` / `"全球国家列表…"` |

Note on the stat tile: the data field `countries_explored` is now 56 while `countries_with_projects` is 241 — the old tile was doubly wrong (self-comparison *and* the wrong denominator concept). The new tile reads `countries_with_projects` from the payload rather than hardcoding 241, so it stays honest as the corpus grows.

### B) §5.1 Dark CARTO basemap, theme-synced

| Line (orig) | Before | After |
|---|---|---|
| 483 | `.realmap { … background: #0a0d12; }` | `background: var(--bg);` |
| 521 | `.leaflet-container { background: #0a0d12; … }` | `background: var(--bg);` |
| 1698 (after) | — | added `let realTileLayer = null;` next to `realMapLayer` |
| 1758 (before `setTheme`) | — | added helper `cartoTileUrl(theme)` → `https://{s}.basemaps.cartocdn.com/{dark_all\|light_all}/{z}/{x}/{y}{r}.png` and `syncMapTiles()` which calls `realTileLayer.setUrl(...)` (Leaflet `setUrl` redraws the layer by default) |
| 1758-1765 | `setTheme()` body | now ends with `syncMapTiles();` so toggling theme swaps the basemap live |
| 1856-1859 | `window.L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", { maxZoom: 18, attribution: '© OpenStreetMap contributors' })` | `realTileLayer = window.L.tileLayer(cartoTileUrl(<current theme>), { maxZoom: 18, subdomains: "abcd", attribution: '© OpenStreetMap © CARTO' })` (attribution keeps both links) |

`syncMapTiles()` guards on `realTileLayer` being non-null, so the `setTheme()` calls that run at boot (before the map is lazily initialized) are no-ops; `initRealMap()` reads the current `data-theme` when creating the layer, so the map always starts on the right basemap.

## 2. Build result

**PASS** — `cd astro && npm run build`: 1 page built, no errors or warnings (657 ms).

## 3. Remaining "Americas" strings

**None.** `grep -in 'americas\|美洲' astro/src/pages/index.astro` returns zero matches — internal identifiers (`allAmericas`, `americasSub`) were renamed to `worldwide`/`worldwideSub` along with the copy.

## 4. What was NOT touched

- §6 payload split, §3 registry virtualization/search, and all P1/P2/P3 items — untouched.
- `scripts/`, `data/`, `export_astro_data.py`, `astro/src/data/*.json` — untouched.
- No file deleted, no commit/push/PR made; changes left in the working tree.
- Marker colors (`markerColor()`, §5.2), Leaflet unpkg CDN (§6.3), and the `.bar100` CSS rules (now unused by the hero tile but still harmless) — deliberately left for their own slices.
- Diff verified free of internal paths (`/Users/`, `scratch/`, `daemons/`, `logs/`, `token_`).
