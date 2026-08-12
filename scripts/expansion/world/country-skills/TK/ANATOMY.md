# TK · Country Anatomy

托克劳（Tokelau）country-skills 节点结构：双线 explorer 方法论（官方/监管/云管线 + 行业/厂商发现）与合并后的 SKILL.md 查询方法论。划分模型（per manifest）：**单一 division：`Tokelau`**；环礁 Atafu/Nukunonu/Fakaofo 只作 sub_location 标签（Unknown TK 默认桶）。

## Files

| 文件 | 状态 | 职责 |
|---|---|---|
| `SKILL.md` | Present · merged | 合并双线方法论：frontmatter（bilingual）+ 中文正文（入口表/核心结构事实/常用查询模板/官方管线要点/行业发现要点/维护注意），保留 single-division 模型、来源分级（A/B/C）、verified-negative 基线、环礁 sub_location 规则与误报过滤 |
| `explorer-official.md` | Present · codex 定稿 | 官方/监管/云管线：官方地面真值（政治/行政地位、治理地理、人口/需求、能源约束、连接性修正、无商业 DC 市场基线）、官方来源登记表、官方负项证据（云区域/政府域检查）、按 division 枚举策略、候选 schema、常见误报、变化检测触发器、复核清单 |
| `explorer-industry.md` | Present · codex 定稿 | 行业/厂商发现：行业现实（verified-negative 基线、Southern Cross NEXT、Teletok、微尺度需求与电力）、运营商与基础设施来源、互联 pivots、云/托管/IXP 负检查、`.tk` 域名噪声、能源与可建性、按环礁行业枚举、候选字段、误报与升级、复核清单 |
| `divisions/` | To be added later | 单一 division（Tokelau）；sub_location 字段枚举 Atafu / Nukunonu / Fakaofo / Unknown TK |

## Division layer (future)

- manifest division model: 单一 division `Tokelau`（subnational_type 无子划分）。
- 子层规划：单一 division 节点；sub_location 枚举 Atafu（低优先级）、Nukunonu（中——Southern Cross NEXT/海缆节点线索）、Fakaofo（中——Teletok/IANA `.tk` 管理者身份）、Unknown TK（高——未定位线索默认桶）。
- 相关文件：`SKILL.md`（方法论）、`explorer-official.md`/`explorer-industry.md`（阴性对照与基础设施线索）。
