# PS · Country Anatomy

Datacenter-country knowledge layer for Palestine (PS).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (MTDE/NDC/Shiraa/PEX/WAFA/World Bank) + industry (operator/trade-press/directory) pipelines; Gaza status discipline mandatory |
| Official pipeline | `explorer-official.md` | present | MTDE/MTIT + DWBG, Government Computer Center/NDC, PalCERT, Shiraa procurement, PEX, Paltel official, Ooredoo, PCBS/TRA, PIPA/PIEFZA, cloud-region absence, 16-governorate routing |
| Industry pipeline | `explorer-industry.md` | present | DCD/Bloomberg-DCK/Telecompaper/local Arabic press, operator/vendor seeds (Paltel/Jawwal/Hadara/Ooredoo/Zone/Digital Communication), directory handling, confirmed/weak lead handling, governorate matrix, verification workflow |
| Division layer | `divisions/` | to be added later | 16 governorates; Ramallah/Nablus priority, Gaza five status-sensitive, remainder negative |

## Division layer (future)

- Enumeration granularity: governorate (16 from `world-manifest.jsonl`).
- Priority divisions: Ramallah (Paltel Al-Bireh Tier III DC, Government Computer Center/NDC, Zone C lead, operator HQ/server rooms); Nablus (Paltel first DC at general-management HQ, An-Najah leads); Hebron (municipal/vendor C/B lead, Tarqumiya zone future); Gaza/North Gaza/Deir El Balah/Khan Yunis/Rafah (damage/recovery status discipline; historical Paltel main DCs; Al-Aqsa academic concept; Rafah Egypt connectivity); Jerusalem (filter Israeli facilities/cloud regions); Bethlehem/Jenin (downgrade Paltel directory claims to C); Jericho and Al Aghwar (JAIP/solar future leads); Tulkarm/Qalqilya/Salfit/Tubas (negative).
- Planned per-division files: `divisions/{governorate}.md` with seeds, queries, and status per the two explorers' 16-governorate matrices.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (16): Bethlehem, Deir El Balah, Gaza, Hebron, Jerusalem, Jenin, Jericho and Al Aghwar, Khan Yunis, Nablus, North Gaza, Qalqilya, Ramallah, Rafah, Salfit, Tubas, Tulkarm.
