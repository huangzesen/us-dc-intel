---
name: iq-datacenter-methodology
location: scripts/expansion/world/country-skills/IQ/SKILL.md
description: |
  Iraq (IQ) datacenter discovery & audit methodology — how to enumerate, verify, and update Iraq datacenter projects at governorate granularity (16 search divisions in the current manifest: Anbar, Basra, Babylon, Baghdad, Diyala, Dhi Qar, Karbala, Kirkuk, Kurdistan, Maysan, Muthanna, Najaf, Nineveh, Qadisiya, Saladin, Wasit; Erbil/Sulaymaniyah/Duhok are grouped as Kurdistan). Iraq has no public national datacenter facility register: enumeration joins CMC licensing, MoC/state-company announcements, PMO/Cabinet e-government evidence (National Data Center), NIC and governorate investment licences, municipal/planning permits, Ministry of Electricity/utility and substation evidence, KRG official sources, official cloud-region lists (no Iraq region as of review), and operator/vendor pages (T964, Linkdata). Read this before running IQ exploration/audit batches. Routes to explorer-official.md (regulator/ministry/cloud pipeline) and explorer-industry.md (operator/trade-press/division query execution).
---

# IQ · 伊拉克数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：伊拉克**没有**公开的全国数据中心设施注册库或统一规划许可库（无 FOIA、无 e-permitting 大平台），不能按美欧方式直接枚举。
> 伊拉克枚举靠**多管线交叉三角测量**：CMC 牌照与数字平台监管、MoC/国家公司（GCCI/GCCIT、ITPC、Al-Salam）公告、PMO/内阁电子政务证据（National Data Center）、NIC 与各省投资委员会许可、市政/Amanat Baghdad 规划、电力部/电网与变电站记录、KRG 官方源、官方云区域页（**截至复核无伊拉克区域**）、运营商与厂商页面。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供伊拉克探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：CMC、MoC/PMO/Cabinet、NIC 与省投资委员会、市政/Amanat Baghdad/环境、电力部/变电站、官方云区域页（AWS/Azure/GCP/OCI/Huawei Cloud 均无伊拉克区域）、16 省七步扫掠矩阵与记录 schema |
| `explorer-industry.md` | 行业/厂商发现：运营商与设施种子（T964、Linkdata、MNO/ISP）、厂商 pivot（Nokia/Schneider/Huawei/Uptime）、贸易媒体分级（DCD/IBN/INA/Shafaq/964/Rudaw/Kurdistan24）、英阿双语词表、逐省行业路线、目录对账与去重规则 |

## 核心结构事实（框定每次搜索）

1. **无全国设施注册库**：枚举 = CMC + MoC/国家公司 + PMO 电子政务 + 投资许可 + 规划 + 电力 + KRG + 云区域页 + 运营商/厂商页的联合；CMC 数字平台登记**≠**物理数据中心。
2. **省份边界**：manifest 为 **16 个搜索 division**，其中 Erbil/Sulaymaniyah/Duhok 归入 **Kurdistan**；不得把 manifest 称为"伊拉克全部省份"，覆盖完成 = 16 个 division 全部扫过。
3. **电力是核心验证轴**：MOE（https://moelc.gov.iq/）与输电/配电公司、变电站/馈线、MW/MVA、发电机容量/冗余/燃料存储、可再生/PPA 分开记录；**永远不要把 site power 或 PR 容量换算成 IT load**。
4. **反误报规则**：不得从 CMC 数字平台登记、移动/ISP/VSAT/Starlink/卫星牌照、光纤/IXP/交换局/海缆登陆、`مركز معلومات` 政府信息中心、云销售页、孤立发电机/变电站项目推断数据中心。
5. **商业市场仍小**：Baghdad 与 Kurdistan/Erbil 设施证据最强；Basra 围绕 Al-Faw 是边缘/海缆/石油部门线索区（海缆登陆≠数据中心）；其余省份以负扫掠 + 电信交换局/大学/银行/石油/政府服务核查为主。
6. **阿英双语必须并用**：阿拉伯语用于 CMC/MoC/NIC/省政府与官方媒体；英语用于云厂商、厂商页、投资新闻、海缆/连通性与国际贸易媒体。
7. **记录类型分离**：commercial colo / government DC / telco core / bank / oil-sector / cloud region / edge-POP-IXP-cable / investment pipeline，逐条保留生命周期动词（signed/MoU/licensed/land allocation/under construction/inaugurated/launched/operational）。

## 查询模式（复制粘贴模板见 explorer-official.md §CMC/MoC/NIC/电力 与 explorer-industry.md §词表/逐省模板）

- CMC：`site:cmc.iq "مركز بيانات" OR "مراكز البيانات" OR "استضافة" OR "خدمات سحابية"`、`site:cmc.iq "data center" OR "data centre" OR hosting OR cloud`、`"هيئة الإعلام والاتصالات" "مركز بيانات" OR "مراكز البيانات"`。
- MoC/国家公司：`site:moc.gov.iq "مركز بيانات" OR "مراكز البيانات" OR "الحوسبة السحابية"`、`"Ministry of Communications" Iraq Nokia "data center"`、`"General Company for Communications and Informatics" OR "GCCI" OR "GCCIT" "data center"`、`"Informatics and Telecommunications Public Company" OR "ITPC" Iraq "data center"`。
- 投资：`site:investpromo.gov.iq "data center" OR "data centre" OR "ICT" OR "communications"`、`"National Investment Commission" Iraq "data center"`、`"{governorate} Investment Commission" "data center" OR ICT OR digital`、`"هيئة استثمار {governorate_ar}" "مركز بيانات" OR "تخصيص أرض"`。
- 电力：`site:moelc.gov.iq "مركز بيانات" OR "data center"`、`"وزارة الكهرباء" "مركز بيانات"`、`"{project}" Iraq substation OR feeder OR MVA OR MW`、`"{project}" Iraq solar OR renewable "data center"`。
- 官方云核查：`site:aws.amazon.com Iraq "region" OR "Local Zone"`、`site:learn.microsoft.com Iraq "region"`、`site:cloud.google.com Iraq "region"`、`site:oracle.com Iraq "cloud region"`、`site:huaweicloud.com Iraq`（结论：均无伊拉克区域）。
- 行业：`site:datacenterdynamics.com/en/news Iraq "data center" OR cable OR Nokia OR T964`、`site:iraq-businessnews.com "data centre" OR "data center"`、`site:rudaw.net "data center" OR "Kurdistan"`、`site:capacitymedia.com Iraq "data centre"`。
- 厂商 pivot：`site:nokia.com Iraq "data center" OR "data centre" OR census`、`site:se.com Iraq "data center" OR T964 OR Baghdad`、`site:uptimeinstitute.com Iraq OR Baghdad OR Erbil OR T964 OR Linkdata`。

## 官方/监管管线要点（详见 explorer-official.md）

- **CMC**（https://cmc.iq/）：MNO/ISP 牌照、频谱/5G、数字平台/服务登记（2025 框架，Articles 5/6）、卫星宽带、互联争议；当前表单**不证明本地物理设施**。
- **MoC/PMO/国家公司**：MoC（https://moc.gov.iq/）、Cabinet/General Secretariat（https://cabinet.iq/，National Data Center 页可能 JS 渲染）、IraqGov 机构目录（https://iraqgov.com/）；已确认政府设施种子：National Data Center（Baghdad，2023-08 启用，容量未公开，A/B）、MoC/Nokia Intisar 与 al-Rashid/al-Sinak 交换局（Baghdad，2025-09 合同阶段，B+）、Ministry of Planning 普查数据中心（候选）、KRG Government Data Center（Erbil，2022-09 启用，KRG Tier III 声称，A/B）。
- **NIC/省投资委员会**：https://investpromo.gov.iq/ + investor-guide；投资许可仅证明投资决策（A），状态只算 **planned** 直到施工/运营证据出现。
- **规划/市政/环境**：无全国 e-permitting 库；用省市政府、Amanat Baghdad、KRG 规划机构 + 投资委员会查土地划拨/建筑许可/EIA（`"{governorate}" "data center" "building permit" OR "land allocation"`）。
- **电力**：MOE + 输电/配电公司官方渠道、`ميجاواط/MW`、`محطة تحويل`（变电站）、`مولدات`（发电机）；记录电压/馈线/发电机数/燃料/PPA/通电日期。
- **云区域页**：AWS/Azure/GCP/OCI/Huawei Cloud 官方清单截至复核均无伊拉克区域；Outposts/边缘 POP 只算租户线索。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商种子（A=官方存在/B=容量）**：T964/Tech964（Baghdad，官网称 3 MW IT load、Tier III、N+1，**A 运营商声称**；2026 年底前为在建/计划）、Linkdata Erbil DC 1（服务存在 A，Tier/地址/MW 为 C 线索）、National Data Center（政府设施）、KRG DC、MoC/Nokia×2（合同阶段）、MNO/ISP 核心候选（Ooredoo/Asiacell、Zain Iraq、Korek、Earthlink、ScopeSky——需具名设施证据）、GCCI/GCCIT/ITPC/Al-Salam 交换局候选、Data Center Journal 遗留清单（GCCIT/Alamiya/Talia，C 且可能过期）。
- **厂商 pivot 高价值**：Nokia（MoC/普查 DC）、Schneider（T964 供电/制冷）、Huawei（设备/5G 线索非云区域）、Uptime Institute 证书（A 证书状态；商业伙伴公告≠认证）、DIL/Breeze/WorldLink（Al-Faw 海缆/AI 基础设施管道，B/计划）。
- **贸易媒体分级**：DCD Iraq tag（B）、Iraq Business News（B/B+，常引部委）、Iraqi News/INA/Shafaq/964media（B，官方通稿文本可达 A）、Rudaw/Kurdistan24（B，KRG）、Capacity/Telecom Review/Developing Telecoms/W.Media（B）、Reuters（B+）、US ITA（背景 A-/B+）。
- **目录对账**：DataCenterMap/Baxtel/colocationm/PeeringDB/Cloudscene 只做候选创建（C），用城市级近似而非精确地址，随后回填官方/运营商证据。
- **去重**：按 `(operator, facility/campus, physical division, phase)` 而非文章标题；Kurdistan 桶内记录 Erbil/Sulaymaniyah/Duhok 到 `city_district_exchange`；Kirkuk/Nineveh 争议区记录须有物理位置证据才能归入。

## 来源分级

- **A** = 官方/一手/法律可问责：CMC 页面/PDF、MoC、PMO/Cabinet、国家公司公告、NIC/省投资许可、MOE/公用事业记录、KRG 官方页、官方运营商设施页、官方云区域页、官方厂商项目页、Uptime 证书页。
- **B** = 强二级：DCD、Iraq Business News、Iraqi News、INA、Shafaq、964media、Rudaw、Kurdistan24、Capacity、Telecom Review、Developing Telecoms、Reuters、W.Media、开发银行/投资者发布；只升级被引用的官方事实（官方事实可 B+，直到主页面存档）。
- **C** = 仅线索：DataCenterMap、Data Center Journal、Baxtel、colocationm、PeeringDB、Cloudscene、社交帖、市场报告摘要、无物理范围/位置的厂商营销。
- 状态语义：operational=政府/运营商/厂商/认证源有启用或客户就绪证据；under construction=现场施工/设备 award/建设进度证据；planned/contract=已签合同/MoU/投资许可/土地划拨/公告管道；candidate=交换局/POP/海缆登陆/CMC 登记/云服务可用/目录线索。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=IQ，divisions=16 省）。
2. 建种子：已确认设施（National Data Center、KRG DC、MoC/Nokia×2、T964、Linkdata、普查 DC 线索）+ 运营商官方页 + 厂商页（Nokia/Schneider/Huawei/Uptime）。
3. 逐 division 执行七步扫掠：CMC → MoC/国家公司 → 投资委员会 → 电力 → 规划/市政 → 本地媒体 → 连通性上下文；记录负扫掠（日期+查询串）。
4. 验证：A 级设施证据 = 政府/运营商/厂商/认证页面；每条 URL/数据点独立分级；容量按原文保留（IT load、site power、racks、Tier、冗余分列）。
5. 输出 world schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目 division 写 `no_projects: true`。
6. 遵守 NO-DELETION；只新增 SKILL.md 与 ANATOMY.md。

## 待办（2026-08-12 02:58Z）

- [x] explorer-official.md 与 explorer-industry.md 已完成并合并为本 SKILL.md。
- [ ] 下一步：50× codex terra agent 按 16 division 逐省枚举（优先 Baghdad、Kurdistan/Erbil、Basra）。
- [ ] 待核实：T964 2026 年底开张证据；MoC/Nokia 站点施工进展；KRG DC 与普查 DC 的官方主页面存档；云厂商区域列表是否新增伊拉克区域。
