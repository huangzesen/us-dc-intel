# PF · Country Anatomy

Datacenter-country knowledge layer for French Polynesia (PF).

## Files

| Path | Status | Note |
|---|---|---|
| SKILL.md | present | Country-level skill: 双线方法论（官方/监管管线 + 行业/媒体/厂商发现），小型已确认市场（TNF + TDF Pic Rouge），法语优先，由两份 explorer 合并而来 |
| explorer-official.md | present | 官方/监管管线：政府门户/法律文本、ANFR/APC/ARN 电信监管、RGPD/DSI/SIPF、TNF/TDF/Vini/ONATi、海缆/登陆站/卫星、EDT 电力、Te Ariari 采购、建筑许可/土地/环评、分区查询模板 |
| explorer-industry.md | present | 行业/媒体/厂商发现：行业媒体、运营商/设施/厂商、云区域负向控制、法语查询模板、塔希提语/地名变体、枚举矩阵、按事实分级规则与 PF 特有陷阱 |
| divisions/ | — | division 层未建；规划在 divisions/french-polynesia/ 下建 sub-location 笔记 |

## Division layer (future)

- manifest 已核验：`subnational_type: country`，`divisions: ["French Polynesia"]`；仅 1 个分区 French Polynesia。
- 已确认记录使用 `division: French Polynesia`；岛屿组（Îles du Vent、Îles Sous-le-Vent、Tuamotu-Gambier、Marquises、Australes）与市镇（Papeete、Papenoo、Pirae、Faa'a 等）仅作地理细化层（site/commune 字段），永远不作 division。
- 规划：创建 `divisions/french-polynesia/` 时，在子层笔记中沉淀岛屿组矩阵（Îles du Vent 唯一 DC 线索区、其余默认无 DC）与资产拆分纪律（Papenoo 同场域混合 TNF/Honotua/teleport/Galileo/OneWeb 必须拆资产；NATITUA ≠ Tahiti-Hawaii）。
