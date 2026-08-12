# UM · Country Anatomy — 美国本土外小岛屿（United States Minor Outlying Islands）

UM 节点：country-skills 层级下 UM 的入口文件为 SKILL.md；双 explorer 文件是 codex 审核定稿的方法论来源，SKILL.md 忠实提炼其 division 模型（geographical unit ×9）、来源分级（A/B/C/U）与负向扫描模板。

## Files

| 文件 | 职责 |
|---|---|
| SKILL.md | 合并方法论入口：bilingual frontmatter + 中文正文（入口表 / 核心结构事实 / 常用查询模板 / 官方与行业管线要点 / 维护纪律），供负向扫描与审计直接引用 |
| explorer-official.md | 官方/监管/云管线：DOI/USFWS refuge 页、Air Force/PACAF/AFCEC、Federal Register/eCFR/US Code、EPA NEPAccess、USASpending、SAM.gov、FCC ULS/IBFS、NOAA/USCG、Census、IANA `.um`、官方云区域页负向 |
| explorer-industry.md | 行业/厂商/媒体发现：目录与互联数据库负向核验、云区域官方页、DoD 军事基建管线、USFWS/科研运营管线、行业媒体与 Palmyra OTEC 提案过滤、中文噪声扫描 |
| divisions/ | （未来）按 manifest division（Johnston/Midway/Navassa/Wake/Baker/Howland/Jarvis/Kingman/Palmyra）落地的负面确认与记录目录 |

## Division layer (future)

- manifest division model：`geographical unit`，共九个 repo division。优先级：Wake 与 Johnston 高（联邦军事基建监控面）、Midway 与 Palmyra 中（refuge/科研 + 提案过滤）、Navassa/Baker/Howland/Jarvis/Kingman 极低（verified-negative，refuge-only）。
- 升级门槛统一：命名运营商 + 命名场地 + 服务/功能 + A 级或运营商一手证据；否则保持 `verified-negative` / `proposal-only`。
- 子层建议：`divisions/<division>/records.md`（候选记录字段 + `evidence_grade` + 误报清单）与 `divisions/<division>/queries.md`（该 division 专用查询）。

## 相关文件

- 模板来源：`../RW/SKILL.md`、`../AD/ANATOMY.md`（格式模板）。
- 报告：`../../skill-merge-12b-report.txt`（本批 12b 合并验证清单）。
