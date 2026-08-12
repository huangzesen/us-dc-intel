# TF · Country Anatomy

法属南部领地（French Southern Territories / Terres australes françaises）country-skills 节点结构：双线 explorer 方法论（官方/监管/云管线 + 行业/厂商/媒体发现）与合并后的 SKILL.md 查询方法论。划分模型（per manifest）：**subnational_type: country** — 单一 division：French Southern Territories。

## Files

| 文件 | 状态 | 职责 |
|---|---|---|
| `SKILL.md` | Present · merged | 合并双线方法论：frontmatter（bilingual）+ 中文正文（入口表/核心结构事实/常用查询模板/官方管线要点/行业发现要点/维护注意），保留 single-division 模型、来源分级（A/B/C/U）、verified-negative 协议与误报过滤 |
| `explorer-official.md` | Present · codex 定稿 | 官方/监管/云管线：已验证基线（无商业市场、活动形态、通讯现实、行业阴性对照）、官方信息源（TAAF/IPEV/Legifrance/法国内阁/采购/云区域页）、官方查询模板（法语优先）、内部 district 清单、候选记录判定标准、误报过滤、复核节奏 |
| `explorer-industry.md` | Present · codex 定稿 | 行业/厂商/媒体发现：行业现实、目录负向核验（DataCenterMap/Cloudscene/Baxtel/PeeringDB/海缆图/供应商）、官方/准官方基础设施线索（TAAF/IPEV/CNES/Meteo-France/CEA/采购）、云与运营商核验、候选升级门槛、已知误报清单、推荐检查顺序 |
| `divisions/` | To be added later | 单一 division（French Southern Territories）；内部地名（Crozet/Kerguelen/Saint-Paul et Amsterdam/Terre Adelie/Iles Eparses）仅作定位与误报排除，不写入 repo division |

## Division layer (future)

- manifest division model: `country`（单 division：French Southern Territories）。
- 子层规划：单一 division 节点；internal_location 字段枚举 Crozet / Kerguelen / Saint-Paul et Amsterdam / Terre Adelie / Iles Eparses / unknown。
- 相关文件：`SKILL.md`（方法论）、`explorer-official.md`/`explorer-industry.md`（阴性对照与基础设施线索）。
