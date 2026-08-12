# AO · Country Anatomy

Datacenter-country knowledge layer for Angola (AO).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (INACOM/MINTTICS/INFOSI/procurement/AIPEX/energy) + industry (press/operator/directory) pipelines; 18 manifest provinces with 21-province reform mapping |
| Official pipeline | `explorer-official.md` | present | INACOM/Observatorio TIC, MINTTICS, INFOSI, Portal Compras Publicas/SNCP, AIPEX/JUI, IRSEA/ENDE/RNTEP, cloud-region absence, official facility watchlist, 18-province matrix |
| Industry pipeline | `explorer-industry.md` | present | Trade/local press (Jornal de Angola/Angop/Expansao/DCD/The Tech Capital), operator/vendor sweep (Angola Cables/Raxio/Paratus/Africell/Unitel), directory handling, province industry matrix, confidence rules |
| Division layer | `divisions/` | to be added later | 18 manifest provinces; Luanda exhaustive, Huila/Lubango planned-DR watch, Benguela/Zaire secondary, remainder negative-by-default |

## Division layer (future)

- Enumeration granularity: province (18 from `world-manifest.jsonl`; map 2024-reform provinces Icolo e Bengo→Luanda/Bengo, Cuando+Cubango→Cuando Cubango, Moxico Leste→Moxico until manifest changes).
- Priority divisions: Luanda (INFOSI Camama + Rangel backup, AngoNAP, Raxio AO1 Cacuaco, Paratus DC1/DC2 + third DC, Africell Kings Tower, Unitel leads, banks, ZEE Viana); Huila (AnyConnect/Visium Lubango planned DR); Benguela (Lobito corridor); Zaire (Soyo oil/gas); Cabinda/North Lunda/South Lunda/Namibe (extractive/port internal leads); Huambo/Bie/Malanje (university/institutional); Bengo/Cuando Cubango/Cunene/North Cuanza/South Cuanza/Moxico/Uige (negative-by-default).
- Planned per-division files: `divisions/{province}.md` with seeds, queries, and status per the two explorers' 18-province matrices.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (18): Bengo, Benguela, Bie, Cabinda, Cuando Cubango, Cunene, North Cuanza, South Cuanza, Huambo, Huila, North Lunda, South Lunda, Luanda, Malanje, Moxico, Namibe, Uige, Zaire. (Official 2024 reform names: Icolo e Bengo, Cuando, Cubango, Moxico Leste; keep as aliases.)
