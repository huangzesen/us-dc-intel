# TZ · Country Anatomy

Datacenter-country knowledge layer for Tanzania (TZ).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (TCRA/NEMC/EWURA-TANESCO/TISEZA/PDPC/eGA/Tausi) + industry (press/operator/cable) pipelines |
| Official pipeline | `explorer-official.md` | present | TCRA licences + TCRA/TS013, NEMC EIA, EWURA/TANESCO, TISEZA/SEZ, PDPC, eGA/NIDC, building permits, cloud-region negative controls, 31-region workflow |
| Industry pipeline | `explorer-industry.md` | present | Trade press (DCD/W.Media/Developing Telecoms/TanzaniaInvest), operator/developer sweep, cable/IXP leads, Swahili search, four-pass region method |
| Division layer | `divisions/` | to be added later | 31 regions (26 mainland + 5 Zanzibar); Dar es Salaam exhaustive, Dodoma/Zanzibar Urban-West government leads, Pwani/Mtwara watch, rest negative sweeps |

## Division layer (future)

- Enumeration granularity: region (31 regions from `world-manifest.jsonl`; Zanzibar official names Mjini Magharibi/Kaskazini Unguja/Kusini Unguja/Kaskazini Pemba/Kusini Pemba).
- Priority divisions: Dar es Salaam (Raxio TZ1, Wingu, NIDC/TTCL, Vodacom, Tigo/Yas, Airtel, Aptus/Flashnet, TIX, cable landings); Dodoma (eGA/government cloud, Vodacom lead); Zanzibar Urban/West (Oman Data Park MoU, ZIPA/Silicon Zanzibar); Coast/Pwani (Kwala SEZ watch); Mtwara (DARE1 future landing).
- Planned per-division files: `divisions/{region}.md` with seeds, queries, and status per the two explorers' 31-region tables.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (31): Arusha, Dar es Salaam, Dodoma, Geita, Iringa, Kagera, Katavi, Kigoma, Kilimanjaro, Lindi, Manyara, Mara, Mbeya, Morogoro, Mtwara, Mwanza, Njombe, Coast/Pwani, Rukwa, Ruvuma, Shinyanga, Simiyu, Singida, Songwe, Tabora, Tanga, Pemba North/Kaskazini Pemba, Pemba South/Kusini Pemba, Zanzibar North/Kaskazini Unguja, Zanzibar South/Kusini Unguja, Zanzibar West/Mjini Magharibi.
