# MO · Country Anatomy

Datacenter-country knowledge layer for Macao (MO).

## Files

| Path | Status | Note |
|---|---|---|
| SKILL.md | present | Country-level skill: 双线方法论（官方/监管/云管线 + 行业/厂商/媒体发现），含 division 模型、四语检索词、来源分级与查询模板，由两份 explorer 合并而来 |
| explorer-official.md | present | 官方/监管/云管线：gov.mo/GCS/SAFP 政府云、CTT 电信监管与数据中心授权（Reg. 13/2024、CTM 授权 1/2024 续期）、DSEDT、CTM、CEM、DICJ、网安/GPDP/AMCM、公报/采购/工务、云区域官方页、博彩承批公司披露 |
| explorer-industry.md | present | 行业/厂商/媒体发现：四语检索词、CTM 主运营商管线、其他电信运营商、政府与集成商、博彩承批公司、超大规模云缺位、贸易与本地媒体、互联/IXP/海缆、聚合目录、分区枚举矩阵 |
| divisions/ | — | division 层未建；规划在 divisions/macao/ 下建 sub-location 笔记 |

## Division layer (future)

- manifest 已核验：`subnational_type: country`，`divisions: ["Macao"]`；所有记录使用 `division: Macao`。
- 已确认记录使用 `division: Macao`；澳门半岛、氹仔、路氹、路环、新填海区仅作 area 字段（搜索桶），教区（Sé、Fátima 等）仅作 parish 辅助字段，永远不作 division；横琴/珠海为 CN 司法辖区，从澳门计数排除。
- 规划：创建 `divisions/macao/` 时，在子层笔记中沉淀分区枚举矩阵（澳门半岛政府 DC/云、氹仔 CTM 线索、路氹 casino_internal_it 分开计数、路环电力语境、新填海区管线）与四语检索纪律（繁中/葡/英/简中）。
