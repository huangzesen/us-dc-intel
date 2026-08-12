# WF · Country Anatomy — 瓦利斯和富图纳（Wallis and Futuna）

WF 节点：country-skills 层级下 WF 的入口文件为 SKILL.md；双 explorer 文件是 codex 审核定稿的方法论来源，SKILL.md 忠实提炼其 precinct 三分区模型（Alo/Sigave/Uvea）、来源分级（A/B/C）与法语为主查询模板。

## Files

| 文件 | 职责 |
|---|---|
| SKILL.md | 合并方法论入口：bilingual frontmatter + 中文正文（入口表 / 核心结构事实 / 常用查询模板 / 官方与行业管线要点 / 维护纪律），供查询执行与审计直接引用 |
| explorer-official.md | 官方/监管/云管线：国家/领地行政站 + JOWF、Assemblée territoriale、SPT-WF、Légifrance（CPCE/énergie）、ARCEP、BOAMP/PLACE 采购、AFD Tui Samoa、欧盟 OCT 页、EEWF/ENGIE 电力、AFNIC、官方云区域负向 |
| explorer-industry.md | 行业/厂商/媒体发现：SPT-WF 电信核心/接入扫描、OPT-NC 合作辨析、私营 ISP/托管负控、银行/医院/行政/教育机房、卫星/无线连接性、La 1ère/区域媒体、目录负控、枚举矩阵、主权云扫描 |
| divisions/ | （未来）按三分区（Alo/Sigave/Uvea）落地的设施记录目录 |

## Division layer (future)

- manifest division model：`subnational_type=precinct`，divisions 精确为 **Alo**、**Sigave**、**Uvea**；不增删分区。Uvea 优先级最高（SPT-WF 核心/Tui Samoa 终端/EEWF 电力背景），Alo 与 Sigave 默认 connectivity_only（Futuna 接入网/卫星/公共服务机房线索）。
- 归属规则：Tui Samoa 分支到 Futuna 未细分到 Alo/Sigave 时保持总体记录，官方披露站点细化后再细分；瑞士 Wallis、瓦努阿图 Futuna、法国本土托管一律排除。
- 子层建议：`divisions/<division>/records.md`（SPT-WF 核心/服务点、Tui Samoa 终端、Mauga/Manuia 站点、EEWF 电力背景 + `source_grade`/`status`）与 `divisions/<division>/queries.md`（法语为主查询）。

## 相关文件

- 模板来源：`../RW/SKILL.md`、`../AD/ANATOMY.md`（格式模板）。
- 报告：`../../skill-merge-12b-report.txt`（本批 12b 合并验证清单）。
