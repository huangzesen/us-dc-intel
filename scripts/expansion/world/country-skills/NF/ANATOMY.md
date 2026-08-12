# NF · Country Anatomy

Datacenter-country knowledge layer for Norfolk Island (NF).

## Files

| Path | Status | Note |
|---|---|---|
| SKILL.md | present | Country-level skill: 双线方法论（官方/监管/电信/电力/采购 + 行业/媒体/目录/误报核验），no-market 领地、预期零商业数据中心，由两份 explorer 合并而来 |
| explorer-official.md | present | 官方/监管/电信/电力/采购：DITRDCSA/NIRC/ACMA/AusTender/ABN/ASIC、Norfolk Telecom/Telstra satellite backhaul、NIRC 电力、官方云区域缺失检查 |
| explorer-industry.md | present | 行业/媒体/目录/误报核验：运营商与供应商扫描、海缆/卫星/电信线索、行业媒体、目录到一级核验工作流、地点检索配方、容量提取指引、枚举矩阵与分级规则 |
| divisions/ | — | division 层未建；规划在 divisions/norfolk-island/ 下建 sub-location 笔记 |

## Division layer (future)

- manifest 已核验：`subnational_type: country`，`divisions: ["Norfolk Island"]`；NF 为单一分区，全领地覆盖。
- 已确认记录使用 `division: Norfolk Island`；Burnt Pine、Kingston、Cascade、Anson Bay、Middlegate、Mt Pitt 等仅作地点/locality 字段（搜索桶），永远不作 division。
- 规划：创建 `divisions/norfolk-island/` 时，在子层笔记中沉淀地点覆盖矩阵（Burnt Pine 电信/电力服务、Kingston 政府 ICT、Cascade 无现代海缆登陆、Anson Bay 历史 Pacific Cable Station 误报风险）与 Gondwana-1 非登陆纠偏纪律。
