# CF · Country Anatomy

Datacenter-country knowledge layer for Central African Republic (CF).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (ARCEP/gouv.cf/AfDB CAB-CAR/SOCATEL-IANA/World Bank PGNSP/energy) + industry (press/operator/vendor/directory) pipelines; 17 manifest divisions, Bangui-centric |
| Official pipeline | `explorer-official.md` | present | ARCEP, government portal/ministry domains, AfDB CAB-CAR, SOCATEL/.cf IANA, World Bank PGNSP, Huawei/Cybastion/ECCAS-PIDA, ENERCA, cloud-region absence, candidate handling table, 17-division matrix |
| Industry pipeline | `explorer-industry.md` | present | Trade/local press (Agence Ecofin/Radio Ndeke Luka/Digital Business Africa/DCD), operator/vendor sweep (GreenLine/Cybastion/Orange/Telecel/Moov/DEVEAG), directory handling, lead verification recipes, division matrix |
| Division layer | `divisions/` | to be added later | 17 manifest divisions; Bangui high-yield, Ombella-Mpoko/Haute-Sangha-Mambere-Kadei context, rest negative |

## Division layer (future)

- Enumeration granularity: division (17 from `world-manifest.jsonl`; current CAR is 20 prefectures + Bangui after 2020/2021 reform - normalize to manifest, keep current names in notes).
- Normalization notes: Haute-Sangha/Mambere-Kadei = current Mambere-Kadei/Berberati corridor; Sangha = Sangha-Mbaere; Kemo-Gribingui = Kemo/Nana-Grebizi legacy; Gribingui = Nana-Grebizi. Do not create new manifest divisions (Mambere, Lim-Pende, Ouham-Fafa, Nana-Grebizi, Kemo).
- Priority divisions: Bangui (CAB-CAR national datacentre + Digital Training Centre, GreenLine/SOCATEL Tier 3, Huawei Tier III, Cybastion, Orange core, ARCEP HQ, SOCATEL Rue Guerillot, University of Bangui); Ombella-Mpoko (Boali/ENERCA power, peri-Bangui); Haute-Sangha/Mambere-Kadei (CAB Cameroon link); remainder negative-by-default.
- Planned per-division files: `divisions/{division}.md` with seeds, queries, and status per the two explorers' 17-division matrices.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (17): Ouham, Bamingui-Bangoran, Bangui, Basse-Kotto, Haute-Kotto, Haut-Mbomou, Haute-Sangha/Mambere-Kadei, Gribingui, Kemo-Gribingui, Lobaye, Mbomou, Ombella-Mpoko, Nana-Mambere, Ouham-Pende, Sangha, Ouaka, Vakaga.
