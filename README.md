# GRIDWATCH · US + Americas Datacenter Buildout Intelligence

Tracked datacenter / data-center / server-farm facilities and projects across the United States and the Americas (Canada, Brazil, Mexico, Argentina, Chile, Colombia, and 48 more countries/territories).

## What's inside

- **`datacenters.db`** — SQLite database of tracked facilities/projects. `centers` table has a `country` column (ISO 3166-1 alpha-2, e.g. `US`, `BR`, `MX`) and a `subnational` column (state / province / department / division).
- **`astro/`** — production Astro static site (GRIDWATCH board): state/country switching, light/dark themes, EN/中文, capacity + project views.
- **`scripts/`** — exploration contracts, batch files, and merge pipelines:
  - `scripts/expansion/americas/` — 101 web-exploration batches (one per country/territory), results as JSONL, plus `explore-brief.md` (the evidence contract).
  - `scripts/merge_americas.py` — idempotently merges Americas exploration results into `datacenters.db` (adds `country`/`subnational` columns).
  - `scripts/export_astro_data.py` — exports `datacenters.db` → `astro/src/data/datacenters.json` (with `countries` aggregate array).
- **`merge-output/americas-summary.json`** — last merge run summary (per-country facility/capacity counts).

## Current totals (2026-08-11 merge)

- 3,409 tracked centers: US 2,731 + 678 Americas rows from 101 exploration batches
- 54 countries/territories with at least one project
- Top Americas markets by facility count: BR 95, MX 60, CA 53, CO 47, AR 45, CL 39

## Data & evidence

Exploration follows the contract in `scripts/expansion/americas/explore-brief.md`: every division is searched; real facilities/projects get project rows with source-backed evidence; divisions with no credible public evidence get explicit `no_project` coverage rows. Status/confidence notes are carried per row in the JSONL results.

## Rebuild & deploy

See `astro/SKILL.md` for the maintenance contract (data flow, rebuild steps, leak checks, deployment boundary). Live board: <https://xhelio.ai/datacenters/>

## 相关文件

- `SKILL.md`（顶层方法论/路由）· `ANATOMY.md`（结构地图）
- `scripts/SKILL.md`（管线）· `astro/SKILL.md`（正式站）· `design/SKILL.md`（设计）· `kanban/SKILL.md`（旧看板）
- `datacenters.db`（主库）· `merge-output/americas-summary.json`（最近汇总）

---

Built with the LingTai agent network (https://github.com/Lingtai-AI/lingtai) for Jason/Zesen.
