# GG · Country Anatomy

Datacenter-country knowledge layer for **Bailiwick of Guernsey (GG)**.

## Files

| Layer | File | Status | Note |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present | Merged from the two explorers; entry table, division model, A/B/C grading, query templates. |
| Official/regulatory/cloud pipeline | `explorer-official.md` | present | States of Guernsey planning (Webmap/Websearch), GCRA licences, JT/Sure operator pages, electricity (Guernsey Electricity / Alderney Electricity), GFSC/ODPA, procurement/government IT, Guernsey Registry, Alderney/Sark/Herm coverage; pitfalls and verified seeds. |
| Industry/trade press/vendor discovery | `explorer-industry.md` | present | JT/Sure operator sweep, MSPs (C5/Civica/Logicalis), trade press (Guernsey Press, Bailiwick Express, BBC CI, DCD, The Register, Channel Eye, Island FM), directories; directory-to-primary workflow, capacity extraction and false-positive rules. |
| Division layer | `divisions/` | — | Single division `Guernsey`; planned `divisions/Guernsey/` creation. |

## Division layer (future)

- World manifest (`world-manifest.jsonl`) models GG as `subnational_type: country` with exactly one division: `Guernsey` (British Crown Dependency; own planning/telecom/electricity/financial-services/data-protection systems).
- All confirmed records must use `division: Guernsey`. The ten parishes (St Peter Port, St Sampson, Vale, Castel, St Saviour, St Andrew, St Martin, St Peter in the Wood, Forest, Torteval) and Alderney/Sark/Herm are `sub_area`/coverage tags only, never division values.
- Planned: `divisions/Guernsey/` with sub-location notes (search buckets only, never divisions), including the coverage matrix (St Peter Port high-probability operator/government rooms; St Sampson/Vale industrial power context; Alderney planned/exploratory EOI; Sark/Herm negative control) and verified seeds (JT, Sure Guernsey Data Centre, government secure DC, Alderney EOI, Digital Greenhouse counter-proof).
