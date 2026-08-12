---
name: ge-datacenter-methodology
location: scripts/expansion/world/country-skills/GE/SKILL.md
description: |
  Georgia (GE) datacenter discovery & audit methodology — how to enumerate, verify, and update Georgia datacenter projects at top-level unit granularity (12 buckets: Abkhazia, Adjara, Guria, Imereti, K'akheti, Kvemo Kartli, Mtskheta-Mtianeti, Rach'a-Lechkhumi-Kvemo Svaneti, Samtskhe-Javakheti, Shida Kartli, Samegrelo-Zemo Svaneti, Tbilisi). Building control is municipal (Tbilisi City Hall, Batumi/Kutaisi/Rustavi/Poti portals); counting gate is municipal permit/commissioning, NAPR cadastre/company record, MEPA/NEA environmental decision, GSE/DSO connection, GNCC authorization, or a first-party operator facility page. Georgian-language evidence is mandatory for high recall (მონაცემთა ცენტრი). No hyperscale cloud region. Seeds: Cloud9 Tbilisi, Silknet/Silk Cloud Tier III (planned 2 MW), Caucasus Online, NewTelco, G Data, Bank of Georgia/TBC (private), Bitfury historical, Kutaisi Tech Hub (official planned). Read this before running GE exploration/audit batches. Routes to explorer-official.md (permits/registry/environment/power/telecom/FIZ/cloud) and explorer-industry.md (operators/catalogs/certifications/FIZ/press).
---

# GE · 格鲁吉亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：格鲁吉亚建设管控在市镇（Tbilisi 市政厅 + Batumi/Kutaisi/Rustavi/Poti 等自治市门户），无全国建设许可搜索库；计数门槛=市镇许可/投运记录、NAPR 地籍/公司记录、MEPA/NEA 环境决定、GSE/配电公司连接、ComCom 授权或一方式运营商设施页。
> 分区模型：**12 个顶层单元**（2 自治共和国 + 9 大区 + Tbilisi）；**Abkhazia 与南奥塞梯重叠区**无可靠格鲁吉亚官方覆盖，不编造许可/地籍证据。
> 市场小且 Tbilisi 集中：Cloud9（运营）、Silknet/Silk Cloud（规划 2 MW，2026-08 动工报道）、Caucasus Online、NewTelco、G Data（Tier III Design）、银行私有 DC（Bank of Georgia Lilo、TBC TBL-01）、Bitfury 历史设施、Kutaisi 技术中心（官方规划）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供格鲁吉亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：Matsne 法律、TCSA/MS.GOV.GE/Tbilisi 市政许可、NAPR/maps.gov.ge 地籍、ComCom 授权、MEPA/NEA/ei.gov.ge 环境、GNERC/GSE/Telasi/Energo-Pro/ESCO 电力、经济部/GITA/DGA/FIZ 与 Uptime 认证、格鲁吉亚语查询模板、12 单元策略 |
| `explorer-industry.md` | 行业/厂商发现：市场形态、英/格语搜索模式、目录/认证/互联种子、来源分级（A 一方式/B 媒体/C 目录）、玩家与设施线索清单、省际工作流、观察清单与假阳性 |

## 核心结构事实（框定每次搜索）

1. **市镇级许可为主干**：Tbilisi 市政厅（tbilisi.gov.ge）、Batumi/Kutaisi/Rustavi/Poti/Zugdidi/Gori/Telavi 等 `*.gov.ge` 门户；TCSA（国家建设监督）与 ms.gov.ge 为过程指针；Matsne（matsne.gov.ge）提供空间规划/建设法典。
2. **NAPR 是法人/地籍决胜关**：公司身份、法律形式、地籍地块与不动产用途；NAPR 证明所有权/场地，不证明运营。
3. **格鲁吉亚语强制**：`მონაცემთა ცენტრი`（数据中心）、`სერვერული`（服务器房）、`კოლოკაცია`、`სამშენებლო ნებართვა`（建设许可）、`ექსპლუატაციაში მიღება`（投运）、`გარემოზე ზემოქმედების შეფასება`（环评）、`თავისუფალი ინდუსტრიული ზონა`（FIZ）；注意 `მონაცემთა ცენტრი` 也可指信息/统计/客服中心——必须核实 IT/服务器设施。
4. **环境证据高价值**：ei.gov.ge 公开听证/EIA/环境决定；提取备用发电机数及 kW/MW、燃油量、水/冷却需求、噪声/空气模型。
5. **电力与电网**：GNERC（监管）、GSE（输电连接，Grid Code II 章）、Telasi（Tbilisi DSO）、Energo-Pro（区域 DSO）、ESCO；具名 DC 客户的电网记录才算证据。
6. **无超规模云区域**：AWS/Azure/GCP/OCI 官方列表无格鲁吉亚（国家）；警惕美国佐治亚州（Georgia, USA）页面。
7. **Uptime 认证分级**：Tier Design 认证=规划/设计证书，不等于运营；Constructed Facility 证明已建，但银行/政府私有 DC 属非商业上下文。
8. **Abkhazia/占领区**：加密货币/矿场报道属 de-facto 处理，不得混入格鲁吉亚官方枚举。

## 查询模式（复制粘贴模板见 explorer-official.md §2 / explorer-industry.md §1）

- 官方（格语）：`site:ms.gov.ge "მონაცემთა ცენტრი"`、`site:tbilisi.gov.ge "სამშენებლო ნებართვა" "{operator}"`、`site:{municipality}.gov.ge "სერვერული"`、`site:napr.gov.ge "{operator}" "{company_id}"`、`site:maps.gov.ge "{cadastral}"`、`site:ei.gov.ge "{operator}" "გარემოზე ზემოქმედების შეფასება"`、`site:gse.com.ge "მონაცემთა ცენტრი"`、`site:comcom.ge "{operator}" "ავტორიზაცია"`。
- 英语：`"Georgia" "data center" "building permit" Tbilisi -Atlanta -USA`、`"Tbilisi" "data center" colocation`、`"Silk Cloud" "data center" Georgia`、`"Cloud9" "Dinamo Arena" "data center"`、`"NewTelco Georgia" "neutral data center"`、`"Kutaisi Technology Hub" "data center"`。
- 格语行业：`მონაცემთა ცენტრი თბილისი`、`სილქნეთი მონაცემთა ცენტრი`、`სილქ ქლაუდი მონაცემთა ცენტრი`、`ქუთაისის ტექნოლოგიური ჰაბი მონაცემთა ცენტრი`、`კოლოკაცია საქართველო`。
- 低产出单元扫：`"{division}" "მონაცემთა ცენტრი"`、`"{main_town}" "data center" colocation Georgia`、`site:bm.ge "{division}" "მონაცემთა ცენტრი"`。
- 目录/认证：`site:datacentermap.com/georgia "Data Centers"`、`site:uptimeinstitute.com Georgia Tbilisi`、`site:peeringdb.com/fac Tbilisi Georgia`、`site:cloudscene.com "Georgia" "data center"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 许可：Tbilisi/自治市门户 → TCSA → NAPR/地籍；提取许可号/日期/发证机构/申请人/法人 ID/地籍码/用途/面积/投运状态。
- 电信：ComCom 授权证明行业身份，不证明设施；`{operator} + ავტორიზაცია`。
- 环境：ei.gov.ge（当前高价值门户）、MEPA、NEA；环境评估法典 + 环评许可法。
- 电力：GSE 输电连接 + 配电公司（Telasi/Energo-Pro）；提取连接协议/技术条件号、电压、变电站、MW/MVA、DSO/TSO。
- 投资/FIZ：经济部（Kutaisi Tech Hub）、GITA、DGA（州 ICT，勿把服务器房当 DC）、Revenue Service、Tbilisi/Kutaisi/Poti FIZ（居民身份≠设施）。
- 计数规则：市镇许可/投运/地籍用途/官方项目页/一方式设施页=countable；一方式服务页无许可=operating 但 `permit_unverified`；Design 认证=planned；目录=候选不计数；加密矿场/历史 Bitfury 需当前运营证据；政府/银行 DC 为上下文。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 一方式（A）：Cloud9（cloud9.ge，Dinamo Arena，2 Akaki Tsereteli Ave Gate 5，3 路独立供电/630 kVA 备用/ N+N）、Caucasus Online（co.ge/en/426）、NewTelco（newtelco.com，中性 DC 自 2016-02）、Silknet/Silk Cloud（Tier 3 计划）、GDKHOST（自有小 DC，Zugdidi 待验）、Uptime GE 页、经济部 Kutaisi 页、FIZ 页、Bitfury 历史出售 PDF。
- 媒体（B）：BM.ge（Silknet 动工 2026-08、2 MW、2027 投运预期）、Georgia Today、Forbes Georgia、DCD（Bitfury 历史）、ENOG 演示（NewTelco）、Internet Society IXP tracker。
- 目录（C）：DataCenterMap（5 设施 2 市场 Tbilisi/Batumi）、Cloudscene、DC Hub、Inflect（NewTelco，Politkovskaia 街）、datacenters.com、PeeringDB fac/8513（Caucasus Online）、Baxtel、colo.exchange。
- 假阳性：美国佐治亚州（Atlanta/Douglas/Effingham/Georgia Power）；`მონაცემთა ცენტრი` 指信息中心；企业服务器房；IX/CDN/POP/登陆站；目录重复；注册办公地址；矿场当商业 colo；Design 认证当运营；FIZ 居民当运营。

## 已知设施/项目与证据状态

| 设施/项目 | 区/市 | 状态与证据 |
|---|---|---|
| Cloud9 Dinamo Arena | Tbilisi | 运营（A 一方式页；地址/供电细节）；目录容量 0.5 MW 为 C |
| Silknet / Silk Cloud Tier III DC | Tbilisi | 规划/在建（A 计划页 + B 2026-08 动工报道；2 MW，2027 预期）；许可/NAPR/电网/Uptime 待补 |
| Caucasus Online colocation | Tbilisi | 运营候选（A 服务页）；地址/许可/地籍待补 |
| NewTelco Georgia | Tbilisi | 运营中性 DC（A/B 集团页 + ENOG）；法人/许可/地址待验；目录 3 MW 为 C |
| G Data Data-Center #1 | Tbilisi | Tier III Design 认证（A Uptime）；仅设计认证，不推断运营/容量 |
| Bank of Georgia Main DC (Lilo) | Tbilisi/Lilo | Uptime Design + Constructed Facility（A）；私有银行 DC，非商业 colo |
| TBC Bank TBL-01 | Tbilisi | Uptime Constructed Facility（A）；私有 |
| Bitfury Gldani/TFZ 矿场 DC | Tbilisi/Gldani | 历史 40-60 MW（A/B 历史）；当前运营/所有权未决，不计为现役商业 colo |
| Bitfury Gori 矿场 DC | Shida Kartli/Gori | 历史 ~20 MW（B/C）；无官方许可/地籍 |
| Kutaisi Technology Hub 数据中心组件 | Imereti/Kutaisi | 官方规划（A 经济部）；无 MW/运营商/商业 colo |
| Cloud9 Batumi Arena | Adjara/Batumi | 目录 C（在建声称）；Batumi 许可/一方式确认前不计数 |
| GDKHOST.NET 小 DC | Samegrelo-Zemo Svaneti/Zugdidi（待验） | A 服务声称；市镇/法人/许可待验 |

## 更新节奏

- 每批次：云区域负面核查（勿用美国佐治亚页）、Silk Cloud（许可/地址/Uptime/投运）、Cloud9/Batumi、NewTelco 法人/地址、G Data 从 Design 到 Constructed/投运。
- 季度：Bitfury Gldani/Gori 当前所有者与运营；Kutaisi Tech Hub 采购/进度；FIZ 新 IT/HPC/矿场租户；Uptime GE 页。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（12 单元粒度）；本 skill 作为国家层参考注入。
