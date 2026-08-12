# GU · Country Anatomy

Datacenter-country knowledge layer for **Guam (GU)**.

## Files

| Layer | File | Status | Note |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present | Merged from the two explorers; entry table, division model, 19-village coverage, A/B/C grading, query templates. |
| Official/regulatory/cloud pipeline | `explorer-official.md` | present | Government of Guam and public procurement, GEDA/GPA/PUC/CCU utilities, FCC cable-landing licensing/IBFS, carrier official facility pages, federal/defense (SAM.gov, NAVFAC, Andersen, Camp Blaz, DISA), cloud-region/edge checks, 19-village coverage, enumeration rules and noise filters. |
| Industry/trade press/vendor discovery | `explorer-industry.md` | present | GTA/GNC/Guam Exchange/DOCOMO/IT&E operator sweep, subsea/landing stations, defense vendors, media (DCD, Submarine Networks, Pacific Island Times et al.) and directories (DataCenterMap, Baxtel, Inflect), enumeration matrix and dedup rules. |
| Division layer | `divisions/` | — | Single division `Guam`; planned `divisions/Guam/` creation. |

## Division layer (future)

- World manifest (`world-manifest.jsonl`) models GU as `subnational_type: country` with exactly one division: `Guam` (US unincorporated territory).
- All confirmed records must use `division: Guam`. The 19 official villages are secondary coverage search buckets only, never division values; Tumon/Harmon/Upper Tumon belong to the Tamuning context.
- Planned: `divisions/Guam/` with sub-location notes (search buckets only, never divisions), including the three-class separation (commercial colo / cable landing infrastructure / defense-federal telecom), high-priority localities (Piti, Tamuning-Harmon-Tumon, Hagåtña, Yigo/Andersen, Dededo/Finegayan, Santa Rita/Agat), and facility seeds (GTA GU1/GU2/GU3, GNC iX, Guam Exchange, DOCOMO Pacific, IT&E, NAVFAC communications center, Andersen data center lead).
