# SA · Country Anatomy

Datacenter-country knowledge layer for Saudi Arabia (SA).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — 13 regions → 122 governorates (GeoNames admin2) | to be added later |

## Division layer (future)

- Saudi Arabia enumerates at region → governorate granularity (122-division manifest, e.g. `Riyadh Region - Ar Riyad`, `Eastern Province - Ad Dammam`, `Mecca Region - Jiddah`, `Tabuk Region - Duba'`), with English/Arabic transliteration aliases mapped per division (alias table in explorer-industry.md §5).
- Planned: per-governorate (or per-region) skill files covering CST registration routing, Balady/NCEC/SEC permit surfaces, and local Amanah / municipality portals per region.
