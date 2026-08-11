# Astro Country Dimension Patch Notes

Date: 2026-08-11

## Changed Files

- `scripts/export_astro_data.py`
  - Added country-aware export support with fallback compatibility for DBs that do not yet have `country` and `subnational` columns.
  - Added `countries` to the JSON payload. Each country includes `code`, `name_en`, `name_zh`, `facilities`, `capacity_mw`, `capacity_gw`, `subnationals`, `funnel`, and `years`.
  - Added `totals.countries_explored` from `scripts/expansion/americas/americas-manifest.jsonl` and `totals.countries_with_projects` from distinct countries present in `centers`.
  - Preserved the existing `states`, `funnel`, `years`, `developers`, `evidence`, `centers`, and `status_labels` structures. `centers` keeps the old fields and adds `country` / `subnational` for filtering.

- `astro/src/pages/index.astro`
  - Updated dashboard copy from US-only to Americas scope in English and Chinese.
  - Added a country scope switcher. Default is all Americas; clicking a country focuses that country; clicking it again returns to all Americas.
  - Added geography rendering modes:
    - All Americas: country list sorted by selected metric.
    - US: existing state tile cartogram.
    - Non-US: subnational bar list, independent of `STATE_LAYOUT`.
  - Updated hero totals, geography view, funnel, yearly wave, and registry filters to respect the selected country scope.

- `astro/src/data/datacenters.json`
  - Regenerated with `LINGTAI_RUNTIME_PYTHON scripts/export_astro_data.py`.

## Validation

- Export command:
  - `LINGTAI_RUNTIME_PYTHON scripts/export_astro_data.py`
  - Result: succeeded.

- Data checks:
  - `totals.facilities`: 2731
  - `totals.countries_explored`: 56
  - `totals.countries_with_projects`: 1
  - `countries` length: 1
  - Sum of `countries[].facilities`: 2731
  - Note: local `datacenters.db` does not yet contain `country` / `subnational`, so export used the compatibility fallback and grouped all rows as `US`.

- Build command:
  - `cd astro && npm run build`
  - Result: succeeded.

- Dist leak check:
  - `grep -rE '/Users/|scratch/|daemons/|logs/|token_' dist/`
  - Result: no matches.

## Remaining Notes

- When `datacenters.db` is updated with `country` and `subnational`, rerun the export command. The same code path should then populate multiple country rows, with `countries_with_projects` reflecting the countries present in the DB.
- Country Chinese names are provided for the 56 Americas manifest entries. Unknown country codes fall back to the English/code label rather than failing export.
