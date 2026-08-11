# GRIDWATCH US County Map Notes

## Data Source

- County centroid source: U.S. Census Bureau 2024 Gazetteer county national file, `2024_Gaz_counties_national.zip`.
- Source URL: `https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2024_Gazetteer/2024_Gaz_counties_national.zip`
- Generated local data file: `scripts/expansion/us-county-coords.json`.
- The generated coordinate file contains 3,222 rows with `county`, `state`, `lat`, and `lng`.

## Coverage

- Current export produces 1,164 US county/state aggregates in `datacenters.json`.
- All exported county aggregates have `lat` and `lng`.
- 1 aggregate, `Northern Indiana`, does not map to a Census county-equivalent name and uses the Indiana state centroid fallback.
- The current database has 2,731 US center rows. Its raw county/state text includes some full state names and multi-county labels; after normalizing state names to USPS abbreviations and preserving raw county labels, the dashboard county export contains 1,164 county/state aggregates.

## Matching Rules

- Normal county names remove the `County` suffix to match the project database style, for example `Loudoun County` becomes `Loudoun`.
- Louisiana `Parish` and Puerto Rico `Municipio` suffixes are normalized for lookup.
- Alaska `Borough`, `Census Area`, `Municipality`, and `City and Borough` suffixes are normalized for lookup while display names remain source-compatible.
- Independent city labels are preserved when present, for example `Baltimore city` and `St. Louis city`, to avoid collisions with same-named counties.
- Multi-county labels split on `/`, `;`, `,`, and `&` for coordinate lookup. If no part matches, the state centroid is used.

## Frontend Interaction

- Americas view remains country-level.
- US view starts with state-level Leaflet markers and the existing state tile cartogram.
- Clicking a US state marker or tile sets the state filter, flies the Leaflet map to that state, and renders county-level markers for counties with projects in that state.
- County marker radius follows the active map metric, capacity or facilities. Marker color remains capacity-banded.
- County popups show county name, state, facility count, and capacity.

## Known Limits

- County points are centroids, not polygons, so this is a point-detail drilldown rather than a county choropleth.
- Multi-county project labels are represented by the first matched county centroid when possible.
- Non-US country behavior is unchanged and still uses existing subnational anchors.
