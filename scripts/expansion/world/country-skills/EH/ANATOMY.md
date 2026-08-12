# EH · Country Anatomy

Datacenter-country knowledge layer for **Western Sahara (EH)**.

## Files

| Layer | File | Status | Note |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present | Merged from the two explorers; entry table, division model, A/B/C grading, query templates. |
| Official/regulatory/cloud pipeline | `explorer-official.md` | present | Moroccan-administered institutional routes (MTNRA/MMSP, ANRT, CRI, AMDIE, ONEE/MASEN, CNDP, procurement), UN/MINURSO, operators/certifications/cables; per-bucket official enumeration and verification rules. |
| Industry/trade press/vendor discovery | `explorer-industry.md` | present | DCD, Reuters, Ecofin, Medias24/Le360/TelQuel/Yabiladi/MAP, directories, SADR/Polisario-side sources; enumeration matrix and grading/ingestion rules. |
| Division layer | `divisions/` | — | Single division `Western Sahara`; planned `divisions/Western Sahara/` creation. |

## Division layer (future)

- World manifest (`world-manifest.jsonl`) models EH as `subnational_type: country` with exactly one division: `Western Sahara`.
- All confirmed records must use `division: Western Sahara`. Laayoune-Sakia El Hamra, Dakhla-Oued Ed-Dahab, east-of-the-berm, and UN/MINURSO are internal coverage buckets / locality labels only, never division values.
- Planned: `divisions/Western Sahara/` with sub-location notes (search buckets only, never divisions), including the political-sensitivity attribution rules (Moroccan-administered / SADR-Polisario / UN sources).
