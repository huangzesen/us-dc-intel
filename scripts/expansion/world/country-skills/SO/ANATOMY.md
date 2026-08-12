# SO · Country Anatomy

Datacenter-country knowledge layer for Somalia (SO).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (NCA/MOCT/NIRA/SOMINVEST/donors/power) + industry (press/operator/interconnection) pipelines; admin attribution mandatory |
| Official pipeline | `explorer-official.md` | present | NCA licensing, MOCT federal NDC, NIRA/ABIS, Somaliland sources (govsomaliland/moiid/TaiwanICDF), Puntland (mof.pl.so), investment/donor records, power (BECO/SESRP), cloud-region absence, 18-region strategy |
| Industry pipeline | `explorer-industry.md` | present | DCD/Bloomberg/Techpoint/SONNA/Goobjoog/Garowe press, operator sweep (Hormuud/Somtel/Telesom/Golis/NationLink/Wingu/SomaliREN/Somcable), directory/IXP/subsea handling, Somali/Arabic search, four-pass region method |
| Division layer | `divisions/` | to be added later | 18 regions; Banaadir and Northwest (Woqooyi Galbeed) priority clusters, Puntland low-medium, rest negative |

## Division layer (future)

- Enumeration granularity: region (18 from `world-manifest.jsonl`; Northwest = Woqooyi Galbeed incl. Sahil/Berbera note; Togdheer/Awdal Somaliland; Sanaag/Sool contested; Bari/Nugaal/Mudug Puntland).
- Priority divisions: Banaadir (federal NDC, Hormuud portfolio, NationLink, SomaliREN, NIRA/ABIS, SoIXP, DARE1 landing); Northwest/Woqooyi Galbeed (Somaliland NDC Hargeisa, Wingu Berbera SL01, Telesom, Somtel, Somcable 2Africa, EGS/S-Road); Bari (Golis HQ Bosaso); Nugaal (Garowe/Puntland e-services); Mudug (Galkayo/Golis nodes).
- Planned per-division files: `divisions/{region}.md` with seeds, queries, admin-attribution notes, and status per the two explorers' 18-region tables.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (18): Awdal, Bakool, Banaadir, Bari, Bay, Galguduud, Gedo, Hiiraan, Middle Juba, Lower Juba, Mudug, Nugaal, Sanaag, Middle Shabelle, Lower Shabelle, Sool, Togdheer, Northwest.
