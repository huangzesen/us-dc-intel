# PH · Country Anatomy

Datacenter-country knowledge layer for Philippines (PH).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (LGU/NTC/DICT-GovCloud/DENR-EMB/energy/PEZA-BOI/NPC/cloud-official) + industry (operator/interconnection/press/directory) pipelines; 18 PSGC regions incl. NIR |
| Official pipeline | `explorer-official.md` | present | PSA PSGC 18-region coverage, NTC (DTIP RA 12234/VAS/SRF exemption), DICT/GovCloud/NGDC, DENR-EMB ECC/CNC Online, DOE/ERC/NGCP/utilities, PEZA/BOI/SIPP, NPC, official cloud checks, division strategy, minimum schema, red flags |
| Industry pipeline | `explorer-industry.md` | present | Operator landscape (VITRO/ePLDT, STT GDC, Equinix, Converge, DITO, SpaceDC, EdgeConneX, Flow/A-Flow, DAMAC/EDGNEX), hyperscaler/cloud status, interconnection ecosystem (IXPs/cables), DCAP, trade press, region strategy, workflow |
| Division layer | `divisions/` | to be added later | 18 PSGC regions; NCR/CALABARZON/Central Luzon Tier 1, Central Visayas/Davao/NIR/Western Visayas/Ilocos-CAR/Cagayan Valley/Northern Mindanao Tier 2, remainder Tier 3 |

## Division layer (future)

- Enumeration granularity: region (18 PSGC regions as of 31 Jul 2025; NIR from RA 12000 - Negros Occidental incl. Bacolod, Negros Oriental, Siquijor; do not use the older 17-region list).
- Tier 1 divisions: NCR (VITRO Makati/Pasig/Parañaque, Equinix MN1-MN3, STT GDC Makati/Fairview, Converge Pasig, AWS Local Zone/Direct Connect ecosystem); CALABARZON (VITRO Sta. Rosa, SpaceDC MNL1/Cainta, STT Cavite, Flow/A-Flow, DAMAC/EDGNEX Laguna leads, Batangas/Nasugbu); Central Luzon (DITO Clark Super Core, New Clark City/BCDA, Subic, Bataan/AFAB, Baler/Aurora landing).
- Tier 2: Central Visayas (VITRO Cebu 1/2, Cebu IT Park, VECO); Davao (STT Davao, Bifrost/Digos Apricot, Davao Light); NIR (Bacolod/Dumaguete edge-BPO); Western Visayas (Iloilo/MORE Power); Ilocos-CAR (La Union landings, North Luzon Data Center/Baguio); Cagayan Valley (Claveria/TPU); Northern Mindanao (CDO/CEPALCO, Phividec).
- Tier 3: Bicol, Eastern Visayas, Zamboanga Peninsula, Soccsksargen, Caraga, BARMM, Mimaropa (government/telco edge/DR/cable/energy leads).
- Planned per-division files: `divisions/{region}.md` with seeds, queries, and status per the two explorers' region strategies.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (18): NCR, CAR, Region I Ilocos, Region II Cagayan Valley, Region III Central Luzon, Region IV-A CALABARZON, Mimaropa (IV-B), Region V Bicol, Region VI Western Visayas, NIR Negros Island Region, Region VII Central Visayas, Region VIII Eastern Visayas, Region IX Zamboanga Peninsula, Region X Northern Mindanao, Region XI Davao, Region XII Soccsksargen, Region XIII Caraga, BARMM.
