# NC · Country Anatomy

Datacenter-country knowledge layer for New Caledonia (NC).

## Files

| Path | Status | Note |
|---|---|---|
| SKILL.md | present | Country-level skill: 双线方法论（官方/监管/电信/电力管线 + 行业/媒体/供应商发现），法文优先检索，由两份 explorer 合并而来 |
| explorer-official.md | present | 官方/监管/电信/电力：gouv.nc/JONC/Congrès/三省、OPT-NC、ANFR/Autorité de la concurrence NC、Enercal/EEC-Engie、GONDWANA/PICOT 海缆、marchespublics.nc、云负向基线 |
| explorer-industry.md | present | 行业/媒体/供应商：DSP/Data Services Pacific、OPT-NC 历史（CITIUS）、PITA、APNIC/bgp.tools/PeeringDB、本地与贸易媒体、法文查询词库、厂商/业主转向清单、验收规则 |
| divisions/ | — | division 层未建；规划在 divisions/new-caledonia/ 下建 sub-location 笔记 |

## Division layer (future)

- manifest 已核验：`subnational_type: country`，`divisions: ["New Caledonia"]`；交付覆盖单元为 New Caledonia。
- 已确认记录使用 `division: New Caledonia`；3 个省份（Province Sud、Province Nord、Province des Îles Loyauté）与 33 个 communes 仅作内部完整性检查网格（搜索桶），永远不作 division。
- 规划：创建 `divisions/new-caledonia/` 时，在子层笔记中沉淀省/commune 扫描网格（Province Sud 主设施区、Province Nord 矿业 IT、Province des Îles Loyauté 国内光缆登陆）与电信监管口径（ARCEP 不管辖 NC、监管由 NC 政府承担）。
