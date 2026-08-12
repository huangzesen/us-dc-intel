# FO · Country Anatomy

Datacenter-country knowledge layer for **Faroe Islands (FO)**.

## Files

| Layer | File | Status | Note |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present | Merged from the two explorers; entry table, division model, A/B/C/U grading, query templates. |
| Official/regulatory/cloud pipeline | `explorer-official.md` | present | Official registers (Skráseting, Lógasavn, Fjarskiftiseftirlitið, SEV, Umhvørvisstovan, Dátueftirlitið), Keypsportal procurement, planning/EIA, government IT, hyperscaler region check; 6 coverage areas, grading and confirmed-facility table. |
| Industry/trade press/vendor discovery | `explorer-industry.md` | present | Elektron/Nema/FT/NET operators, Farice/SHEFA cables, PeeringDB/Pulse/BGP databases, trade and local press, aggregators; enumeration matrix and caution rules. |
| Division layer | `divisions/` | — | Single division `Faroe Islands`; planned `divisions/Faroe Islands/` creation. |

## Division layer (future)

- World manifest (`world-manifest.jsonl`) models FO as `subnational_type: country` with exactly one division: `Faroe Islands` (autonomous territory under the Danish Realm, 1948 home rule; not an EU member).
- All confirmed records must use `division: Faroe Islands`. The six coverage areas (Streymoy, Eysturoy, Norðoyar, Vágar, Sandoy, Suðuroy) and the 29 municipalities are internal coverage/locality labels only, never division values.
- Planned: `divisions/Faroe Islands/` with sub-location notes (search buckets only, never divisions), including coverage-completion standard (each area carries confirmed facilities or dated negative/watch records) and the operator leads (Elektron, Nema Húsing, government datacenter B, FT/NET).
