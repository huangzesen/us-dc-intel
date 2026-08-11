# GRIDWATCH Interactive Map Patch Notes

## Changed Files

- `scripts/export_astro_data.py`
  - Added approximate centroid coordinate tables for Americas country/territory ISO2 codes and US state/DC/PR anchors.
  - Added `lat` and `lng` to exported `countries[]`.
  - Added `lat` and `lng` to each exported country `subnationals[]` row.
  - Added `lat` and `lng` to exported `states[]` while preserving the existing tile `row`/`col` layout.

- `astro/src/data/datacenters.json`
  - Regenerated from the existing SQLite data using `python scripts/export_astro_data.py`.
  - Confirmed 55 countries, 52 US state/DC/PR records, and all subnational rows include `lat`/`lng`.

- `astro/src/pages/index.astro`
  - Added Leaflet 1.9.4 and OpenStreetMap tiles.
  - Added a real interactive map above the existing tile/list geography view.
  - Added country, US state, and other-country subnational marker rendering.
  - Linked the real map to the existing country switcher, map metric tabs, language switcher, and registry filters.
  - Preserved the existing tile cartogram, subnational list, funnel, wave chart, developer ranking, registry, theme toggle, and language toggle.

## Coordinate Sources And Assumptions

- The country coordinate table is an approximate centroid/visual-anchor table, not facility-level geocoding.
- Main country anchors were checked against public coordinate references:
  - United States: approximate geographic center near `[39.8, -98.6]`.
  - Brazil: published country coordinate near `[-14.235, -51.9253]`.
  - Mexico: geography references place Mexico near `[23.6, -102.5]`.
- Remaining Americas country and territory anchors are approximate visual centroids selected for dashboard mapping.
- US state/DC/PR anchors are approximate state centroid coordinates suitable for aggregate state markers.
- Non-US subnational coordinates currently fall back to the country centroid because the source data has no latitude/longitude at the province/state/department level. In the UI, those markers are spread around the centroid in a small deterministic pattern and popup text marks them as approximate anchors.

## How To Verify

- Regenerate data:
  - `python scripts/export_astro_data.py`
- Confirm coordinates are present:
  - `node -e "const d=require('./astro/src/data/datacenters.json'); console.log(d.countries.every(c=>'lat' in c && 'lng' in c), d.states.every(s=>'lat' in s && 'lng' in s));"`
- Build:
  - `cd astro && npm run build`
- Manual browser checks:
  - Open the dashboard and confirm the real map appears in the Geography section.
  - In All Americas mode, country circles should appear across the Americas and clicking a country should focus the dashboard.
  - In US mode, state circles should appear over the United States and clicking a state should sync the registry state filter.
  - In another country mode, subnational circles should appear near the selected country with popups.
  - Toggle Capacity/Facilities, Dark/Light, and EN/中文 and confirm the existing views still update.

## Known Limits

- The map uses aggregate centroid markers, not exact facility coordinates.
- OpenStreetMap tiles and Leaflet assets are loaded from external public URLs at runtime.
- Non-US subnational geography should be upgraded later with a real province/state coordinate table or facility-level geocoding if more precise placement is required.
