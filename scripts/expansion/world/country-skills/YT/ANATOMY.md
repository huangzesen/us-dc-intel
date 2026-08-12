# YT · Country Anatomy — 马约特（Mayotte）

YT 节点：country-skills 层级下 YT 的入口文件为 SKILL.md；双 explorer 文件是 codex 审核定稿的方法论来源，SKILL.md 忠实提炼其唯一分区模型（Mayotte）、来源分级（A/B/C）与容量/Tier 多来源口径纪律。

## Files

| 文件 | 职责 |
|---|---|
| SKILL.md | 合并方法论入口：bilingual frontmatter + 中文正文（入口表 / 核心结构事实 / 常用查询模板 / 官方与行业管线要点 / 维护纪律），供查询执行与审计直接引用 |
| explorer-official.md | 官方/监管/云管线：Préfecture/RAA/Légifrance/CNIL/DEALM/Géorisques、AFD ITH 项目/Banque des Territoires/BOAMP/PLACE、ARCEP/Orange/SRR/Telco OI/RENATERIX、Uptime/TIA/EPI + 云区域负向、EDM/CRE/EDF SEI、LION2/FLY-LION3/Avassa |
| explorer-industry.md | 行业/厂商/媒体发现：ITH Center/MAYOTIX 优先扫描、运营商（Orange/SRR/Telco OI/Mayotte One）、目录到一手工作流、媒体（Mayotte Hebdo/Le Journal/La 1ère/Linfo.re）、容量/可靠性/命名规则、分区查询模式 |
| divisions/ | （未来）唯一分区 Mayotte 下的设施记录目录（含 sub_locality 市镇/片区） |

## Division layer (future)

- manifest division model：`subnational_type: country`，divisions 仅 **Mayotte**；Mamoudzou、Kaweni、Koungou 等为 sub_locality 字段，不建子 division。
- 覆盖优先级：Mamoudzou/Kaweni 最高（ITH Center、LION2/FLY-LION3 landing、MAYOTIX、运营商 PoP）；Koungou/Longoni 中（EDM/Longoni 电力背景）；Dzaoudzi/Pamandzi 中低（机场/旧行政中心电信机房）；其余 13 市镇低（no public DC 默认）。
- 子层建议：`divisions/Mayotte/records.md`（ITH Center 主记录 + MAYOTIX/海缆 landing/运营商 PoP/EDM 背景，字段含 `tier_claim`/`tier_certified`/`capacity_mw_alt_c`）与 `divisions/Mayotte/queries.md`（官方/行业/分区查询模板）。

## 相关文件

- 模板来源：`../RW/SKILL.md`、`../AD/ANATOMY.md`（格式模板）。
- 报告：`../../skill-merge-12b-report.txt`（本批 12b 合并验证清单）。
