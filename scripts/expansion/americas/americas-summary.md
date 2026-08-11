# Americas Second-Level Administrative Division Manifest

Manifest: `/Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/americas/americas-manifest.jsonl`

This manifest contains one JSON object per Americas country or dependent territory. Each object has:

- `country_code`: ISO 3166-1 alpha-2 country or territory code.
- `country_name`: English country or territory name.
- `subnational_type`: Administrative unit type used for exploration.
- `divisions`: Canonical English division names, sorted alphabetically.

## Counts

- Total countries/territories: 56
- Total divisions: 778

## Region Breakdown

| Region | Countries/Territories | Divisions |
| --- | ---: | ---: |
| North America | 6 | 115 |
| Central America | 7 | 97 |
| Caribbean | 28 | 321 |
| South America | 15 | 245 |

## Regional Membership

- North America: Bermuda, Canada, Greenland, Mexico, Saint Pierre and Miquelon, United States.
- Central America: Belize, Costa Rica, El Salvador, Guatemala, Honduras, Nicaragua, Panama.
- Caribbean: Anguilla, Antigua and Barbuda, Aruba, Bahamas, Barbados, Bonaire, Sint Eustatius and Saba, British Virgin Islands, Cayman Islands, Cuba, Curacao, Dominica, Dominican Republic, Grenada, Guadeloupe, Haiti, Jamaica, Martinique, Montserrat, Puerto Rico, Saint Barthelemy, Saint Kitts and Nevis, Saint Lucia, Saint Martin, Saint Vincent and the Grenadines, Sint Maarten, Trinidad and Tobago, Turks and Caicos Islands, United States Virgin Islands.
- South America: Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Falkland Islands, French Guiana, Guyana, Paraguay, Peru, South Georgia and the South Sandwich Islands, Suriname, Uruguay, Venezuela.

## Authority Notes

- Sovereign-state lists use standard first-order administrative divisions: states, provinces, departments, regions, districts, or equivalent capital/federal districts.
- Canada, Mexico, Brazil, Argentina, Chile, Colombia, Peru, Bolivia, Paraguay, Uruguay, Venezuela, Ecuador, Guyana, Suriname, and Central American countries follow their widely used national admin-1 structures.
- Caribbean sovereign states use parish, district, region, municipality, or dependency structures commonly used by national statistical or government references.
- Dependent territories use their official ISO 3166-1 alpha-2 codes. Where a territory has no meaningful internal admin-1 structure for datacenter exploration, the territory itself is listed as the division.
- Small territories with practical internal geography but weak formal admin-1 hierarchy use best-known districts, parishes, islands, municipalities, communes, or arrondissements to keep exploration granular.
- Names are normalized to ASCII English spellings for JSONL portability in the pipeline.
