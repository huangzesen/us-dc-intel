# World Manifest Granularity Notes

Updated the world expansion manifest from first-level administrative divisions to a mixed second-level strategy for large countries and major markets.

## Summary

- Countries/regions in `world-manifest.jsonl`: 192
- Divisions before: 3062
- Divisions after: 5674
- Batch chunk size: 10
- Batches before: 406
- Batches after: 668
- US handling: absent from the world manifest; `make_batches.py` still skips US and Americas coverage dynamically.

## Upgraded Countries

| Country | Previous count | New count | New granularity | Source |
| --- | ---: | ---: | --- | --- |
| CN | 34 | 360 | Prefecture-level divisions with province-level prefix | GeoNames `admin2Codes.txt`; cross-checked against public China prefecture-level counts. |
| IN | 36 | 763 | Districts with state/UT prefix | GeoNames `admin2Codes.txt`; cross-checked against India IGOD state-wise district directory. |
| DE | 16 | 403 | Kreis/Landkreis and urban districts with state prefix | Wikipedia `List of districts of Germany` table. |
| FR | 18 | 101 | Departments | Wikipedia `List of French departments` table; excludes Lyon Metropolis to keep department count at 101. |
| GB | 13 | 185 | County, unitary authority, council area, or local government district with country prefix | GeoNames `admin2Codes.txt`; cross-checked against ONS county/unitary authority dataset description. |
| KR | 17 | 229 | Si/gun/gu with province/metropolitan city prefix | GeoNames `admin2Codes.txt`; cross-checked against public South Korea administrative division counts. |
| AU | 8 | 540 | Local government areas with state/territory prefix | GeoNames `admin2Codes.txt`. |
| AE | 7 | 28 | Municipality/city areas with emirate prefix | GeoNames `admin2Codes.txt`. |
| SA | 13 | 122 | Governorates with region prefix | GeoNames `admin2Codes.txt`. |
| ZA | 9 | 52 | District and metropolitan municipalities with province prefix | GeoNames `admin2Codes.txt`. |

## Retained Countries

JP remains at 47 prefectures; this is already a stable, commonly used market planning layer and avoids expanding to roughly 1700 municipalities.

RU remains at 83 federal subjects; BR and MX are handled through Americas coverage outside this manifest. ID, TR, and NG remain at province/state level for this pass because their current granularity is sufficient for major-market routing and keeps the world batch count inside the 600-800 target range.

## Source URLs

- GeoNames admin2 dump: https://download.geonames.org/export/dump/admin2Codes.txt
- GeoNames admin1 names: https://download.geonames.org/export/dump/admin1CodesASCII.txt
- China prefecture-level reference: https://en.wikipedia.org/wiki/Prefecture-level_divisions_of_China
- India district directory: https://igod.gov.in/sg/district/states
- Germany districts reference: https://en.wikipedia.org/wiki/List_of_districts_of_Germany
- France departments reference: https://en.wikipedia.org/wiki/List_of_French_departments
- UK county/unitary authority dataset reference: https://www.data.gov.uk/dataset/79b1ab91-4fb9-4a66-abc7-ddfba7027c73/county-and-unitary-authority-december-2024-names-and-codes-in-the-uk
- South Korea administrative divisions reference: https://en.wikipedia.org/wiki/Administrative_divisions_of_South_Korea
