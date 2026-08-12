---
name: ly-datacenter-methodology
location: scripts/expansion/world/country-skills/LY/SKILL.md
description: |
  Parent-level data-center enumeration methodology for Libya (LY). Libya has no
  single public datacenter register, so enumeration triangulates GACI/CIM
  regulatory records, IANA .LY delegation, LPTIC/LTT subsidiary operator pages,
  municipal building licenses, GECOL power/tender records, free-zone/university/UN
  procurement, hyperscaler region absence checks, industry colo providers, trade
  press and directories across 22 popularates. Read this before running LY
  exploration/audit batches. Routes to explorer-official.md (official/regulatory/
  cloud pipeline) and explorer-industry.md (industry/vendor discovery).
---

# LY · 利比亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：Libya has no single public datacenter register；枚举必须跨 官方监管（GACI/CIM、LPTIC/LTT 子公司页、市政府建筑许可、GECOL 电力/招标、自贸区/大学/UN 采购、超大规模云区域缺失核验）与 行业（colo/云厂商、贸易媒体、协会、目录）多轨三角测量。
> 多轨三角测量：官方轨道产出 A 级监管/项目证据，行业轨道产出 B/C 级线索与状态词汇，两者交叉验证后才可定状态与容量。
> 本 skill 汇总两份探索报告（explorer-official.md / explorer-industry.md）为国家层方法论；批次执行前必读。

## 入口

| 文件 | 内容 | 说明 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线：GACI/CIM、IANA `.LY`、LPTIC/LTT 子公司页、市政府建筑许可、GECOL 电力/招标、自贸区/大学/UNGM-UNDP 采购、超大规模云区域缺失核验、官方/运营商种子清单 | A 级主干与查询模板 |
| explorer-industry.md | 行业/厂商发现：Qabas、Libyan Spider、Digital Cloud、Altaqnya 等厂商页、贸易媒体、协会（LTF/ISOC/LATI/MFZ）、目录升级流程、22 个 popularates 查询矩阵 | B/C 级线索与状态词汇 |

## 核心结构事实（框定每次搜索）

1. **无国家数据中心注册表**：Libya 不存在统一公开的全国数据中心登记；枚举需拼接 GACI/CIM 电信与数字基础设施信号、LPTIC 与子公司页面、市政府建筑许可、GECOL 电力/招标记录、自贸区/大学/政府采购、官方超大规模云区域列表、本地运营商页与贸易媒体/目录。
2. **官方轨迹**：GACI/CIM（`cim.gov.ly`；IANA `.LY` 转移报告确认其依 GNU 部长会议 2022 年第 49 号决议设立并依 985 号决议管理 `.LY`，LTT 为技术联络人）、LPTIC/LTT/Almadar/Libyana/Hatif/LITC/Aljeel Aljadeed 子公司页、市政建筑许可（2018 年第 225 号决定）、GECOL（`gecol.ly`）、自贸区（MFZ）与 UNGM/UNDP 采购。
3. **阿拉伯语优先**：官方检索语言以阿拉伯语为主；云页面、IANA、UNGM、DCD、Telecompaper 与 Libya Herald 用英语。核心词 `مركز بيانات`、`مراكز البيانات`、`مركز استضافة البيانات`、`الحوسبة السحابية`、`استضافة`、`رخصة بناء`、`الشركة العامة للكهرباء`。
4. **地理集中**：高收益城市为 Tripoli、Benghazi、Misrata、Sabha；次级线索在 Murzuq、Derna、Tobruk/Butnan、Sirte、Zawiya、Al-Khums/Murqub 及南部/油田直辖市（出现政府、电信、大学、港口/自贸区、银行、油气、电力控制系统时）。
5. **云语义（含负向控制）**：AWS/Azure/GCP/OCI 官方页面均无 Libya 公有云区域；本地 "cloud" 产品可能托管于本地私有数据中心、电信数据中心或外部超大规模/合作伙伴区域；Qabas/Libyan Spider 的合作伙伴身份不等于超大规模设施。
6. **容量语义**：MW/MVA/机架数仅在被直接声明时使用；不得从泛泛的备用发电机/UPS/冷却/柜描述推断 MW；区分 IT 负载、站点负载、发电容量与电网接入容量。
7. **陷阱**：目录（DataCenterMap 等）默认 C 级；无具名设施的 `digital transformation`/`cloud` 新闻只是线索；政策/计划（如 LPTIC Tripoli/Misrata 计划）≠ 项目容量；服务器机房、DNS 根节点、电信交换局不得按完整数据中心计数。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§5 / explorer-industry.md §1-§6）

- 官方域查询：`site:cim.gov.ly "مركز بيانات"`、`site:lptic.ly "data center"`、`site:ltt.ly "استضافة"`、`site:tripoli.gov.ly "رخصة بناء" "مركز"`、`site:gecol.ly "اتصالات" "ك.ف"`、`site:mfzly.com "data hosting"`、`site:ungm.org Libya "data center"`、`site:lana.gov.ly "الهيئة العامة للاتصالات والمعلوماتية" "مركز بيانات"`。
- 运营商查询：`"LTT Internet Data Center" Libya`、`"Almadar Aljadid" "data center" Tripoli Benghazi`、`"Libyan Spider" "data center" Tripoli`、`"Qabas" "data center in Libya"`、`"TransSahara" "Tier 3"`。
- 每行政区骨架：`"{division English}" Libya "data center"`、`"{city Arabic}" "مركز بيانات"`、`"{city Arabic}" "رخصة بناء" "اتصالات"`、`site:gecol.ly "{city Arabic}" "اتصالات"`、`site:libyaherald.com "{city}" "data centre"`、`site:datacentermap.com/libya "{city}"`。
- 云核验：`site:aws.amazon.com Libya "Local Zone"`、`site:learn.microsoft.com Azure Libya "region"`、`site:cloud.google.com Libya "region"`、`site:oracle.com Libya "cloud region"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **GACI/CIM**：A 级监管与网络治理证据（root servers、数字主权、5G、牌照、频谱分配）；IANA 记录给出 GACI 于 Tripoli Telecom Tower/Al Zawia Street，LTT 为 `.LY` 技术联络人。
- **LPTIC 数字转型**：官方页面称将在 **Tripoli 与 Misrata** 设立综合数据中心——A 级计划证据，状态需市政/GECOL/子公司跟进。
- **LTT 数据中心服务**：`ltt.ly/business/Dcenter` 证明 LTT 营销数据中心/托管服务并承担 `.LY` 技术运维；可下钻 LTT IDC、Alshut Road、DDoS 报道。
- **市政建筑许可**：2018 年第 225 号决定定义许可字段（直辖市、许可号、业主、地块/街道、工程事务所、建筑委员会记录）；实际发布的许可证/市政公告/官方建设项目页为 A 级项目证据，许可工作流页面仅证明流程。
- **GECOL**：变电站/高压接入/招标/项目为 A 级电力事实；除非记录点名设施或运营商，数据中心推断为 A-/B 级。
- **自贸区/大学/UN 采购**：MFZ 数据托管中心（华为承建、40km 光纤、机架、双电源、备用能源、冷却、消防/安防）为 B 级待 MFZ 官方页验证；University of Tripoli IT 学院数据中心（Almadar/Huawei 捐赠）为 A 级机构设施；UNGM/UNDP-LBY-00644 覆盖 **Sebha 市-大学数据中心** 与 **Murzuq 数据中心（Fezzan 大学托管）**。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **贸易/本地媒体（B）**：Libya Herald、Libya Observer、Libya Monitor、Libya Review、DCD、Telecompaper；命名倡导方、城市/地点、项目类型、日期与状态且与官方/运营商证据一致时升 B。
- **协会（B）**：Libyan Technology Foundation（`technology.ly`；GACI 2026-02-15 研讨会：监管、认证、供应商注册、云计算条件、网络安全、数据治理）、ISOC Libya、LATI（Tripoli/Benghazi/Misrata 分支，培训实验室勿计为数据中心）、MFZ。
- **目录（C）**：DataCenterMap（快照 Tripoli 3 / Benghazi 1 / Misrata 1 / Sabha 1）、datacenters.com、Cloudscene、ColocationM、PeeringDB（仅互连元数据）；升级需运营商/官方页、采购、许可或电力记录。
- **运营商种子（存在性 A / 容量视证据）**：LTT、Qabas（Tripoli，备用发电机/独立链路/CCTV/消防/云与托管，mid-2025 新设施待证完工）、Libyan Spider（Tripoli，IaaS/托管）、Almadar（Tripoli/Benghazi 根服务器设施，B 级待 GACI/LANA 主源）、TransSahara/Tatweer（Tier 3/Huawei 模块化，目录城市条目 C）、Digital Cloud Libya（Bab Bin Ghashir，集成商）、Altaqnya（集成商）、银行/油气遗留集成商（Agathon 等，B）。

## 来源分级

- **A** = 官方/一手：GACI/CIM 记录、IANA ccTLD 记录/报告、LPTIC/LTT/Almadar/Libyana/Hatif 官方页、市政许可/规划记录、自贸区/大学/政府官方页、GECOL 招标/项目/电力记录、UNGM/UNDP 采购、官方云供应商位置页、官方运营商设施页。
- **B** = 强二手：Libya Herald/Observer/Monitor、DCD、Telecompaper、官方厂商/客户案例、标准/认证页、具名地点与倡导方的国际采购/贸易媒体。
- **C** = 弱线索：目录专页、LinkedIn/社媒、泛市场报告、未实施的 MoU、无具名设施的 "digital transformation/cloud" 新闻。
- **状态词汇（阿拉伯语）**：`توقيع`（签署）、`اتفاق`（协议）、`رؤية مستقبلية`（未来愿景）= 计划/政策信号；`إنشاء`（设立）、`إطلاق`（启动）、`تشغيل`（运行）、`افتتاح`（开业）、`استضافة`（托管）= 更强运行信号但仍需物理地点/运营商验证；`تنظيم القطاع`/`اعتماد المراكز` 是监管证据而非已许可设施。
- **容量规则**：仅直接声明的 MW/MVA/机架数可入 `capacity_mw`；备用发电机/UPS 泛提及不可推断 MW；许可的楼层/面积记入 notes。
- **政策/计划 ≠ 项目容量**：LPTIC 计划、GACI 战略、MFZ 宣传均须以许可/招标/完工/启用证据定状态。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中 `country_code == "LY"` 的条目，按 division 分组（22 个 popularates）。
2. 以本 skill 运营商标记构建种子：LPTIC/LTT/Almadar/Libyana/Hatif/LITC、Qabas、Libyan Spider、TransSahara、MFZ、大学、市政。
3. 官方优先逐省扫描：`cim.gov.ly`、`lptic.ly`、`ltt.ly`、市政府域、`gecol.ly`、自贸区/大学/UNGM/UNDP。
4. 用 GECOL/市政许可/招标将计划与宣传升级为 permitted/construction/operational。
5. 行业回填：贸易媒体（B）发现备选名称，目录（C）仅作索引；对每个设施执行目录升级工作流（精确名称英阿双语 → 运营商/LPTIC/GACI/LANA → 厂商/承包商 → 仍仅目录则保持 C）。
6. 去重键：`(ultimate parent, facility, city, date)`；区分商业 colo/云、电信 IDC、政府/市政数据枢纽、大学/服务器机房、根/DNS 节点、云服务（无实体设施）。
7. 按 world schema 输出：`{country_code: "LY", country_name: "Libya", division, city, name, operator, status, capacity_mw, source_urls, evidence_date, evidence_grade, notes}`；负结果 `no_projects: true` 并注明所搜城市/拼写变体。
8. **NO-DELETION**：不改写 explorer-official.md / explorer-industry.md；复核批次只增补不删行。

## 待办（2026-08-12 02:37Z）

- 两份探索报告已合并为国家层方法论；下一步以本 skill 为国家层参考运行 LY 探索/复核批次（22 省）。
- 需验证：TransSahara/Tatweer Tier 3 设施（Tripoli/Janzur、Benghazi、Misrata、Sabha 目录条目）是否有运营商页/许可/GECOL 证据；MFZ 华为数据托管中心状态；LPTIC Tripoli/Misrata 综合数据中心状态；Qabas mid-2025 Tripoli 新设施是否完工；Almadar Tripoli/Benghazi 根服务器设施以 GACI/LANA 主源定级。
