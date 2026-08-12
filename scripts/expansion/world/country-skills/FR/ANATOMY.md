# FR · Country Anatomy

Datacenter-country knowledge layer for France (FR).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| Province/state division layer | `divisions/` — 18 régions + 101 départements; communes/EPCI as permit unit | to be added later |

## Division layer (future)

- France enumerates region → département → commune/EPCI, with département code as the stable sweep key (101-department prefecture seed table in explorer-industry.md §5.1).
- Planned: per-département (or per-region) skill files covering prefecture sites, MRAe region pages, and grid/heat-reuse contacts.
