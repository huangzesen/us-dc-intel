# SE · Country Anatomy

Datacenter-country knowledge layer for Sweden (SE).

## Files

| Layer | File | Status |
|---|---|---|
| Country-level skill | `SKILL.md` | present (merged from the two explorers) |
| Official / regulatory / cloud pipeline | `explorer-official.md` | present |
| Industry / trade press / vendor discovery | `explorer-industry.md` | present |
| County division layer | `divisions/` — 21 län (repo ASCII spellings map to Swedish names: Vasterbotten=Västerbotten, Scania=Skåne, Vastra Gotaland=Västra Götaland, …) | to be added later |

## Division layer (future)

- Sweden enumerates county-first with municipality drill-down; the manifest uses ASCII/English county names that must be mapped to Swedish (län/kommun) for searching.
- Planned: per-county (or per-division) skill files covering municipal planning/building portals (detaljplan/bygglov/startbesked patterns), county Länsstyrelsen environmental permitting, DSO/grid operators (Ellevio, E.ON, Vattenfall, Göteborg Energi, Jämtkraft, Skellefteå Kraft, …), and district-heating spillvärme partners per county.
