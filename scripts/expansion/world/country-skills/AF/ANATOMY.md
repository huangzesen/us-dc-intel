# AF · Country Anatomy

Datacenter-country knowledge layer for Afghanistan (AF).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (MCIT/ATRA/DABS/NIXA) + industry (operator/directory/press) pipelines |
| Official pipeline | `explorer-official.md` | present | MCIT/ANDC tenders, ATRA, Afghan Telecom, DABS, NIXA, cloud-region negative controls, 34-province official strategy |
| Industry pipeline | `explorer-industry.md` | present | Operator facility pages, trade press, directories, per-province industry workflow, extraction schema |
| Division layer | `divisions/` | to be added later | 34 provinces; Kabul exhaustive, Nangarhar planned, remainder negative-control sweeps |

## Division layer (future)

- Enumeration granularity: province (34 provinces from `world-manifest.jsonl`).
- Priority divisions: Kabul (exhaustive: ANDC, MCIT second-DC tender, MoMP DC, NIXA, DABS/Tarakhil, ALEF, AryanICT, ACG, e& cloud RFP); Nangarhar (MCIT planned second National Data Center).
- Planned per-division files: `divisions/{province}.md` with seeds, queries, and status per the two explorers' 34-province tables.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (34): Badakhshan, Badghis, Baghlan, Balkh, Bamyan, Daykundi, Farah, Faryab, Ghazni, Ghor, Helmand, Herat, Jowzjan, Kabul, Kandahar, Kapisa, Khost, Kunar, Kunduz, Laghman, Logar, Maidan Wardak, Nangarhar, Nimruz, Nuristan, Paktia, Paktika, Panjshir, Parwan, Samangan, Sar-e Pol, Takhar, Urozgan, Zabul.
