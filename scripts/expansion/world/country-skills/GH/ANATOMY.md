# GH · Country Anatomy

Datacenter-country knowledge layer for Ghana (GH).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (NCA/Energy Commission/EPA/MMDA/DPC/NITA/GIPC) + industry (operator/connectivity/press/directory) pipelines; status ladder enforced |
| Official pipeline | `explorer-official.md` | present | NCA licensing/landing stations, Energy Commission permits + Bulk Customer Register, EPA/EIA, MMDA planning permits, DPC/NITA/ministry, GIPC/GFZA/RGD, cloud-region absence, 16-region coverage map, verification recipe |
| Industry pipeline | `explorer-industry.md` | present | Operator/facility census (Equinix AC1, Onix Accra #1, PAIX, NITA, ADC/Onix pipeline), hyperscaler status, subsea/IXP evidence, trade press feeds, directory rules, per-region discovery map |
| Division layer | `divisions/` | to be added later | 16 regions; Greater Accra commercial core, Ashanti government DC (Kumasi), rest negative with query/date notes |

## Division layer (future)

- Enumeration granularity: region (16 from `world-manifest.jsonl`; `subnational_type = region`).
- Priority divisions: Greater Accra (Equinix AC1/MDXi Appolonia, Onix Accra #1, PAIX Accra, ADC/Onix pipeline, NITA Accra, telco DCs, cable landings, IXPs); Ashanti (NITA Ghana E-Gov Cloud Data Center Kumasi - government DC present, commercial colo unconfirmed); Western (Takoradi oil/gas enterprise rooms); Northern (Tamale government/UN/telco rooms); remaining 12 regions negative-by-default.
- Planned per-division files: `divisions/{region}.md` with seeds, queries, and status per the two explorers' 16-region maps.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (16): Ahafo, Ashanti, Bono, Bono East, Central, Eastern, Greater Accra, North East, Northern, Oti, Savannah, Upper East, Upper West, Volta, Western, Western North.
