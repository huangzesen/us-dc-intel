# VU · Country Anatomy — 瓦努阿图（Vanuatu）

VU 节点：country-skills 层级下 VU 的入口文件为 SKILL.md；双 explorer 文件是 codex 审核定稿的方法论来源，SKILL.md 忠实提炼其 6 省 division 模型、来源分级（A/B/C）、设施类型与升级规则。

## Files

| 文件 | 职责 |
|---|---|
| SKILL.md | 合并方法论入口：bilingual frontmatter + 中文正文（入口表 / 核心结构事实 / 常用查询模板 / 官方与行业管线要点 / 维护纪律），供查询执行与审计直接引用 |
| explorer-official.md | 官方/监管/云管线：DCDT/PMO（VGDC/VIX/Cloud Pilot）、TRBR 牌照/UAP/RIO、gov.vu/MIPU/DOFT/ADB、ICN1/Tamtam/VIX、URA/UNELCO/VUI/DOE、规划/环评/注册、官方云区域负向 |
| explorer-industry.md | 行业/厂商/媒体发现：VGDC/VIX 判定、TVL/Vodafone、Digicel、Telsat/WanTok/Canopy、Interchange/ICN1/Tamtam、企业/公共部门机房线索、媒体/目录负控、三语查询、各省枚举矩阵 |
| divisions/ | （未来）按 6 省（Malampa/Penama/Sanma/Shefa/Tafea/Torba）落地的设施记录目录 |

## Division layer (future)

- manifest division model：6 provinces（Malampa、Penama、Sanma、Shefa、Tafea、Torba）。优先级：Shefa 最高（VGDC/VIX/ICN1/运营商总部）、Sanma 中（Tamtam 节点/Luganville/网络节点）、Malampa 与 Tafea 低-中（Tamtam 覆盖节点）、Penama 与 Torba 很低（接入/灾后 ICT）。
- 归属规则：设施须按省归属；未披露地点的 `data centres`（Cloud Pilot Project）保持 `government_dc_project`，不得自动分配到 Santo 或其他省份；邻居国（Fiji/New Caledonia/Solomon）站点不计入。
- 子层建议：`divisions/<province>/records.md`（VGDC、VIX、ICN1、Tamtam 节点、运营商核心、`no_projects` 负面记录 + `source_grade`/`status`）与 `divisions/<province>/queries.md`（EN/FR/BI 三语查询）。

## 相关文件

- 模板来源：`../RW/SKILL.md`、`../AD/ANATOMY.md`（格式模板）。
- 报告：`../../skill-merge-12b-report.txt`（本批 12b 合并验证清单）。
