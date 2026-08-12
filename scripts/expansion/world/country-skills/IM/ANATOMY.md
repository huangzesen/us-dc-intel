# IM · Country Anatomy

Datacenter-country knowledge layer for Isle of Man (IM).

## Files

| Path | Status | Note |
|---|---|---|
| SKILL.md | present | Country-level skill: 双线方法论（官方/监管/云管线 + 行业/厂商/媒体发现），由两份 explorer 合并而来 |
| explorer-official.md | present | 官方/监管/云管线：马恩岛政府/规划/CURA/Manx Utilities/Companies Registry/GSC/FSA/政府采购/官方云区域缺位确认 |
| explorer-industry.md | present | 行业/厂商/媒体发现：Manx Telecom、Netcetera、Domicilium、Continent 8、Sure、BlueWave、目录/媒体/枚举矩阵与分级入库规则 |
| divisions/ | — | division 层未建；规划在 divisions/isle-of-man/ 下建 sub-location 笔记 |

## Division layer (future)

- manifest 已核验：`subnational_type: country`，`divisions: ["Isle of Man"]`；唯一 division 为 Isle of Man。
- 已确认记录使用 `division: Isle of Man`；Douglas、Ballasalla、Braddan、Onchan、Ramsey、Peel、Castletown、Port Erin、Port St Mary 等城镇/教区仅作 locality 字段（搜索桶），永远不作 division。
- 规划：创建 `divisions/isle-of-man/` 时，在子层笔记中沉淀全岛覆盖流（locality 分层优先级：Douglas → Ballasalla/Ronaldsway/Malew → Braddan/Union Mills/Tromode → 其余低产出 locality 负面覆盖）。
