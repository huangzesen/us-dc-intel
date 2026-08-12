# VA · Country Anatomy — 圣座（Holy See / 梵蒂冈）

VA 节点：country-skills 层级下 VA 的入口文件为 SKILL.md；双 explorer 文件是 codex 审核定稿的方法论来源，SKILL.md 忠实提炼其 division 模型（仅 Holy See）、字段级分级（A/B/C/U）与物理归属排除规则。

## Files

| 文件 | 职责 |
|---|---|
| SKILL.md | 合并方法论入口：bilingual frontmatter + 中文正文（入口表 / 核心结构事实 / 常用查询模板 / 官方与行业管线要点 / 维护纪律），供查询执行与审计直接引用 |
| explorer-official.md | 官方/监管/云管线：vaticanstate.va/vatican.va 官方站、DTSI 访谈、IANA `.va`、官方云区域负向、Fratello Sole 能源背景、采购/安全/AI 治理线索 |
| explorer-industry.md | 行业/厂商/媒体发现：DTSI 优先核验对象、NTT DATA/Vatican Library 数字化、贸易媒体与目录扫描、容量与地址提取规则、枚举矩阵 |
| divisions/ | （未来）唯一分区 `Holy See` 下的设施记录目录 |

## Division layer (future)

- manifest division model：`subnational_type: country`，divisions 仅 `Holy See`；不创建 Rome、Vatican City municipality、Santa Maria di Galeria 等子分区。
- 物理归属规则：梵蒂冈城国边界内才归 `Holy See`；罗马、Santa Maria di Galeria、Castel Gandolfo、Lateran、Santa Maria Maggiore、Bambino Gesù 等治外/意大利地址默认排除。
- 子层建议：`divisions/Holy See/records.md`（DTSI datacenters、Vatican ISP/`.va` DNS、Library/Archive 数字化线索 + `evidence_grade` 字段级标注）与 `divisions/Holy See/queries.md`（英/意/拉/中查询模板）。

## 相关文件

- 模板来源：`../RW/SKILL.md`、`../AD/ANATOMY.md`（格式模板）。
- 报告：`../../skill-merge-12b-report.txt`（本批 12b 合并验证清单）。
