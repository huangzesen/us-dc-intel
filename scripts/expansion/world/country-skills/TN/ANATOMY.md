# TN · Country Anatomy

Datacenter-country knowledge layer for Tunisia (TN).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (INTT/MTC/ANCS/CNI-ATI/INPDP/TIA/STEG-ANME/permits) + industry (press/operator/directory) pipelines |
| Official pipeline | `explorer-official.md` | present | INTT, MTC, ANCS, CNI/ATI, INPDP, TIA, urbanism/ANPE, STEG/ANME, cloud-region negative controls, operator anchors, 24-governorate matrix |
| Industry pipeline | `explorer-industry.md` | present | Trade press (DCD/We Are Tech/Webmanagercenter/ilboursa/Tekiano/THD), operator sweep, directory handling, governorate industry matrix, candidate examples |
| Division layer | `divisions/` | to be added later | 24 governorates; Tunis/Sousse/Bizerte high priority, Sfax deep-scan, remainder negative checklists |

## Division layer (future)

- Enumeration granularity: governorate (24 from `world-manifest.jsonl`; ISO/government spelling set).
- Priority divisions: Tunis (TT Carthage DC, Ooredoo La Charguia 1, ATI, CNI private cloud, CCK HPC, ministries/BCT); Sousse (Orange Kalaa Kebira, EO/Meninx Enfidha, Sousse technopole); Bizerte (SoleCrypt planned AI DC, Medusa/Orange landing station); Ariana (El Ghazala/Topnet lead); Sfax (technopole, deep scan, likely negative).
- Planned per-division files: `divisions/{governorate}.md` with seeds, queries, and status per the two explorers' governorate matrices.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (24): Ariana, Beja, Ben Arous, Bizerte, Gabes, Gafsa, Jendouba, Kairouan, Kasserine, Kebili, Le Kef, Mahdia, Manouba, Medenine, Monastir, Nabeul, Sfax, Sidi Bouzid, Siliana, Sousse, Tataouine, Tozeur, Tunis, Zaghouan.
