# BT · Country Anatomy

Datacenter-country knowledge layer for Bhutan (BT).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (GovTech/GDC, DCS, DHI, BICMA, BPC/DGPC/BEA, MoIT/BCTA, GMCA) + industry (press/Bitdeer IR/SATO/directory) pipelines; four asset classes kept separate |
| Official pipeline | `explorer-official.md` | present | Government/regulator/utility/planning/land sources, cloud-region absence, official operator seeds, 20-dzongkhag workflow |
| Industry pipeline | `explorer-industry.md` | present | Trade/local press (DCD/The Bhutanese/Kuensel/BBS), vendor/operator sweep, status watchlist, division templates, validation rules |
| Division layer | `divisions/` | to be added later | 20 dzongkhags; Thimphu/Sarpang/Chhukha priority, 17 low-probability negative sweeps |

## Division layer (future)

- Enumeration granularity: dzongkhag (20 from `world-manifest.jsonl`); evidence usually town/site (dzongkhag → town/site → operator → status → official cross-check).
- Priority divisions: Thimphu (GDC/Neyduetewa, DCS, Thimphu TechPark, btIX, telco/enterprise core); Sarpang (Jigmeling/Bitdeer 500 MW, Gelephu/GMC, SATO LOI); Chhukha (Gedu/Bitdeer 100 MW, Chukha hydro corridor, Phuentsholing industrial leads).
- Planned per-division files: `divisions/{dzongkhag}.md` with seeds, queries, and status per the two explorers' 20-dzongkhag tables.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (20): Paro, Chhukha, Haa, Samtse, Thimphu, Tsirang, Dagana, Punakha, Wangdue Phodrang, Sarpang, Trongsa, Bumthang, Zhemgang, Trashigang, Monggar, Pema Gatshel, Lhuentse, Samdrup Jongkhar, Gasa, Trashi Yangtse.
