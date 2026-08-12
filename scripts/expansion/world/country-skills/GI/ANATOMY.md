# GI · Country Anatomy

Datacenter-country knowledge layer for **Gibraltar (GI)**.

## Files

| Layer | File | Status | Note |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present | Merged from the two explorers; entry table, division model, A/B/C/U grading, query templates. |
| Official/regulatory/cloud pipeline | `explorer-official.md` | present | HMGoG government/gazette/statistics/procurement, GRA, GFSC/gambling, GEA power, Gibtelecom/GibFibre telecom, official cloud-region negative checks, division templates and facility seeds, false-positive filters. |
| Industry/trade press/vendor discovery | `explorer-industry.md` | present | Local/trade press (Chronicle, GBC, DCD, Capacity, Computer Weekly), operator/hosting sweep, aggregator and interconnection directories, investment/cloud/local-hosting checks, enumeration matrix and grading rules. |
| Division layer | `divisions/` | — | Single division `Gibraltar`; planned `divisions/Gibraltar/` creation. |

## Division layer (future)

- World manifest (`world-manifest.jsonl`) models GI as `subnational_type: country` with exactly one division: `Gibraltar` (British Overseas Territory).
- All confirmed records must use `division: Gibraltar`. Area labels (Mount Pleasant, Port/North Mole, Europa Point, City Centre, Waterport, Europort, Ocean Village, Bayside/Business Bay, North Front/Airport) are locality anchors only, never division values; Spanish Campo de Gibraltar is cross-border connectivity context only.
- Planned: `divisions/Gibraltar/` with sub-location notes (search buckets only, never divisions), including the facility seeds (Gibtelecom Mount Pleasant operating A/B; Continent 8 inside the Rock operating A; Pelagos near Port announced/planned A; GibFibre claims C; Europa Point cable landing connectivity B) and status discipline (planned/announced never mixed with operating capacity).
