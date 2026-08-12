# TV · Country Anatomy — 图瓦卢（Tuvalu）

图瓦卢节点：country-skills 层级下 TV 的入口文件为 SKILL.md；双 explorer 文件是 codex 审核定稿的方法论来源，SKILL.md 忠实提炼其 division 模型、来源分级与查询模板。

## Files

| 文件 | 职责 |
|---|---|
| SKILL.md | 合并方法论入口：bilingual frontmatter + 中文正文（入口表 / 核心结构事实 / 常用查询模板 / 官方与行业管线要点 / 维护纪律），供查询执行与审计直接引用 |
| explorer-official.md | 官方/监管/云管线：政府部委（ICT/Finance）、TTC、TEC、立法、AIFFP/World Bank/JICA、采购字段、最低阳性证据、官方云区域页负向核验 |
| explorer-industry.md | 行业/厂商/媒体发现：海缆媒体、目录负向检查、运营商/厂商种子、项目状态 watchlist、hyperscaler 负向核验、输出规范 |
| divisions/ | （未来）按 manifest division（Funafuti/Niutao/Nukufetau/Nukulaelae/Nanumea/Nanumaga/Nui/Vaitupu）落地的设施记录目录 |

## Division layer (future)

- manifest division 模型：`subnational_type: town council/island council`；Funafuti 为 P0（Vaka landing/临时生产、TTC server room、在途 micro DC、Starlink gateway、可能 cache），Vaitupu P2（4G+Starlink），其余外岛 P3（仅接入，负向 DC 检查）。
- Niulakita 未列 manifest：并入外岛负预期备注，不新增 division。
- 子层建议：`divisions/<division>/records.md`（资产记录 + `evidence_grade_by_field` + `not_dc_reason`）与 `divisions/<division>/queries.md`（该 division 专用查询）。

## 相关文件

- 模板来源：`../RW/SKILL.md`、`../AD/ANATOMY.md`（格式模板）。
- 报告：`../../skill-merge-12b-report.txt`（本批 12b 合并验证清单）。
