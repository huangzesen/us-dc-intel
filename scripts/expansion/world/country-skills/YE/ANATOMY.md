# YE · Country Anatomy

Datacenter-country knowledge layer for Yemen (YE).

## Files

| Layer | File | Status | Notes |
|---|---|---|---|
| Country-level skill | `SKILL.md` | present-merged | Merged methodology: official (dual MTIT, PTC/YemenNet, TeleYemen, AdenNet, NIC, CSO, UN/World Bank, cables) + industry (press/operator/directory) pipelines; dual-authority control-side notes mandatory |
| Official pipeline | `explorer-official.md` | present | Dual ministries, PTC/YemenNet, TeleYemen, AdenNet+RIPE, NIC, CSO, UNGM/World Bank procurement, cable landing stations, cloud-region absence, 22-division strategy |
| Industry pipeline | `explorer-industry.md` | present | Trade/local press, operator and vendor sweep, directory handling, governorate industry matrix, candidate handling examples |
| Division layer | `divisions/` | to be added later | 22 divisions; Sanaa City/Aden/Hadhramaut/Mahra/Western Coast/Taiz priority, Marib/Shabwah southern corridor, remainder negative searches |

## Division layer (future)

- Enumeration granularity: 22 manifest divisions (Western Coast = Al Hudaydah/Hodeidah search space; Sanaa City = Amanat Al Asimah).
- Priority divisions: Sanaa City (PTC/YemenNet DATA CENTER hosting, TeleYemen HQ/gateway, NIC, mobile cores, CBY Sana'a); Aden (AdenNet core/4G, TeleYemen gateway + Aden-Djibouti/AAE-1 landing, CBY Aden, UN missions); Hadhramaut (AdenNet Phase 2, TeleYemen Mukalla/Seiyun, oil); Mahra (FALCON Al Ghaydah); Western Coast (FALCON Hudaydah, status-sensitive); Taiz/Marib (war-status-sensitive institutional leads).
- Planned per-division files: `divisions/{division}.md` with seeds, queries, control-side notes, and status per the two explorers' 22-division tables.

## Cross-references

- Parent folder: `scripts/expansion/world/country-skills/` (per-country SKILL.md/ANATOMY.md conventions mirror IN/DE/GB/FR/KR and batches 2-7).
- Division names (22): Abyan, Aden, Amran, Beida, Dhale, Dhamar, Hadhramaut, Hajjah, Western Coast, Ibb, Jouf, Lahij, Marib, Mahra, Mahwit, Raymah, Sanaa City, Saada, Shabwah, Sanaa, Socotra, Taiz.
