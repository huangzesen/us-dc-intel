# JE · Country Anatomy

Datacenter-country knowledge layer for Jersey (JE).

## Files

| Path | Status | Note |
|---|---|---|
| SKILL.md | present | Country-level skill: 双线方法论（官方/监管/云管线 + 行业/厂商/媒体发现），由两份 explorer 合并而来 |
| explorer-official.md | present | 官方/监管/云管线：gov.je 规划/采购、States Assembly、JFSC 注册处、JCRA 电信牌照、Jersey Electricity 电网、JT/Sure 运营商一手设施页、官方云区域排除表 |
| explorer-industry.md | present | 行业/厂商/媒体发现：JT/Sure/Digital Jersey 种子、目录/聚合源、行业与本地媒体、教区搜索矩阵、核心证据链、容量提取规则 |
| divisions/ | — | division 层未建；规划在 divisions/jersey/ 下建 sub-location 笔记 |

## Division layer (future)

- manifest 已核验：`subnational_type: country`，`divisions: ["Jersey"]`；唯一枚举分区为 Jersey。
- 已确认记录使用 `division: Jersey`；12 个教区（St Helier、St Saviour、St Clement、Grouville、St Martin、Trinity、St John、St Mary、St Ouen、St Peter、St Brelade、St Lawrence）只作 parish/locality 字段（搜索桶），永远不作 division。
- 规划：创建 `divisions/jersey/` 时，在子层笔记中沉淀教区定位矩阵（St Saviour/JT 双设施、St Helier/Sure、Grouville/N3 电力登陆、St Peter 机场工业区、St Brelade/St Ouen 海缆候选）与 Jersey/Guernsey、Jersey/New Jersey 混淆排除纪律。
