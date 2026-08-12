# NU · Country Anatomy

Datacenter-country knowledge layer for Niue (NU).

## Files

| Path | Status | Note |
|---|---|---|
| SKILL.md | present | Country-level skill: 双线方法论（官方/监管源 + 行业/厂商源），单 division 整岛覆盖、预期零商业托管市场，由两份 explorer 合并而来 |
| explorer-official.md | present | 官方/监管源：gov.nu/MOF/立法、Telecom Niue、Starlink 临时许可、电力与负荷核验、Manatua 海缆、Niue Companies Office、.NU/IUSN/DNS、官方云区域缺失核验 |
| explorer-industry.md | present | 行业/厂商源：Telecom Niue 扫描、Manatua cable-adjacent 线索、IUSN/.NU registry、Starlink/卫星、企业/公共部门机房线索、供应商/承包商、目录与负向控制、枚举矩阵与最终分级规则 |
| divisions/ | — | division 层未建；规划在 divisions/niue/ 下建 sub-location 笔记 |

## Division layer (future)

- manifest 已核验：`subnational_type: country`，`divisions: ["Niue"]`；输出恰好一个 division key：Niue。
- 已确认记录使用 `division: Niue`；村庄（Alofi、Avatele、Hakupu、Tuapa、Tamakautoga 等）仅作地点/位置字段（搜索桶），永远不作 division。
- 规划：创建 `divisions/niue/` 时，在子层笔记中沉淀村庄策略（Alofi 唯一设施级枢纽、非 Alofi 默认 no_projects、Hikufenoga/Tamakautoga 能源项目语境）与误判排除纪律（Manatua 登陆站 ≠ DC、Tui-Samoa 不登陆纽埃、.NU/DNS 技术联系在瑞典）。
