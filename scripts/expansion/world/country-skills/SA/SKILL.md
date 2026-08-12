---
name: sa-datacenter-methodology
location: scripts/expansion/world/country-skills/SA/SKILL.md
description: |
  Saudi Arabia (SA) datacenter discovery & audit methodology — how to enumerate, verify, and update Saudi datacenter projects at governorate-level granularity (122 divisions, GeoNames admin2: 13 regions → governorates). Saudi enumeration is a regulated digital-infrastructure market plus permit joins: CST Data Center Services Regulation (decision 502/1445, in force 2024-01-01) provider registries, CST cloud-registration classes (Qualifying/Class A/B/C), Balady/MoMRAH municipal permits, NCEC environmental permits, SEC / National Grid SA power evidence, official cloud-region pages (AWS Saudi Arabia Region 2026, Azure Saudi Arabia East Q4-2026, Google Dammam me-central2, Oracle Jeddah/Riyadh/NEOM, Huawei Class C, Alibaba/SCCC), and operator pages (center3/stc, Mobily, Salam, Sahayeb/MIS, QST, DataVolt, TONOMUS/Ezditek, Khazna, EDGNEX/DAMAC, Gulf Data Hub, HUMAIN). Read this before running SA exploration/audit batches. Routes to explorer-official.md (regulator/permits/power/cloud) and explorer-industry.md (trade press/vendors/Arabic+English query patterns).
---

# SA · 沙特阿拉伯数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：沙特**没有**统一的公开数据中心设施注册库；枚举需组合 **CST 数据中心服务注册**（Data Center Services Regulation `502/1445`，2024-01-01 生效）、**CST 云计算注册**（Qualifying/Class A/B/C）、**Balady/MoMRAH 市政许可**、**NCEC 环境许可**、**SEC/National Grid SA 电力证据**、**官方云区域页**与**运营商官方页**。
> 大型公告（1.5 GW / 1 GW / 300 MW / 200 MW）多为**项目或园区级计划容量**，未获许可/通电/年报/运营商规格页前按计划计；Riyadh、Eastern Province（Dammam/Khobar/SPARK）、Jeddah、NEOM/Oxagon 是最高优先级地理。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供沙特探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：CST 数据中心与云注册、MCIT/Vision 2030/SDAIA/SPA、沙特交易所与年报、Balady/MoMRAH 市政许可、NCEC 环境许可、SEC/National Grid 电力、MODON/NEOM/MISA/ECZA/RCJY 工业区、官方云区域页、122 governorate 工作流与分级 |
| `explorer-industry.md` | 行业/厂商发现：DCD/MEED/W.Media/Capacity/Argaam 媒体、运营商/开发商种子表（center3、Mobily、Salam、Zain、NourNet、QST、DataVolt、EDGNEX/DAMAC、GDH、Sahayeb/MIS、Ezditek、Khazna、HUMAIN）、英语+阿拉伯语查询模式、13 区域枚举地图 |

## 核心结构事实（框定每次搜索）

1. **CST 是核心监管者**：Communications, Space and Technology Commission（前 CITC）发布《Provision of Data Centers Services Regulation》（decision `502/1445`，2023-08-22 发布，2024-01-01 生效），维护公开的**注册数据中心服务商**与**注册云计算服务商**列表——最佳 A 级运营商/设施种子；分类 Qualifying/Limited/Standard/Advanced，Qualifying 可能意味着在建。
2. **云计算单独注册**：CST 云注册类别 Qualifying/Class A/B/C（Class A 需 Tier 2/ISO 27001；Class B/C 需 Tier 3 建设+运营可持续证书）；Google Cloud 文档称 CST 授予其 Dammam 区域 Class C 许可。用云注册找设施级合作伙伴与主权限制，再转向数据中心服务商注册与运营商页。
3. **规划证据碎片化**：Balady 与 MoMRAH 提供建筑许可/完工证书，但公开检索常需 Nafath 登录或许可证号——先有运营商页/承包商/招标给出 plot 或许可证号再验证。
4. **环境证据归 NCEC**：National Center for Environmental Compliance 的 eCompliance/环境许可服务；柴油发电机、燃料储罐、电池、冷水机组、用水、废水、电子废物、施工影响都可能触发许可。
5. **电力常是决定性证据**：Saudi Electricity Company / Saudi Energy 全资子公司 **National Grid SA** 负责输电；围绕已知园区搜 EHV 变电站、大负荷用户接入、110/132/380 kV 工程、SEC 招标（Etimad）。
6. **超大/AI 公告常分阶段**：1.5 GW（国家战略目标）/ 1 GW / 300 MW / 200 MW 按**项目或园区计划容量**处理，除非许可、通电、年报或运营商规格页把容量分配到具体站点与阶段。
7. **地理**：Riyadh（Ar Riyad/Ad Dir\`iyah：center3、Sahayeb、Ezditek、DataVolt MODON、HUMAIN）；Eastern（Dammam/Khobar/Jubayl/Ahsa\`：Google `me-central2`、Azure East、Khazna、Mobily、QST SPARK）；Makkah（Jeddah/Makkah/Rabigh：Oracle Jeddah、center3、海缆）；Tabuk（Duba\`/Haql：NEOM/OXAGON/DataVolt/Oracle NEOM）；Medina（Madinah/Yanbu）；Qassim（Unaizah）。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§6 与 explorer-industry.md §4/§5）

- 英文核心词：`"data center"` `datacenter` `"data centre"` `"cloud region"` `"AI factory"` `"building permit"` `"environmental permit"` `"National Grid"` `"Saudi Electricity Company"` `substation` `MW` `racks`。
- 阿拉伯语核心词：`مركز بيانات`（数据中心）、`مراكز البيانات`（复数）、`مركز بيانات سحابي`（云数据中心）、`رخصة بناء`（建筑许可）、`تصريح بيئي`（环境许可）、`محطة تحويل`（变电站）、`الشركة السعودية للكهرباء`（沙特电力公司）、`مدن`（MODON 工业城）、`نيوم`/`أوكساجون`（NEOM/OXAGON）。
- 监管：`site:cst.gov.sa "Data Centers Service Providers" "{city}"`、`site:cst.gov.sa "Cloud Computing Services Providers" "Class C"`、`site:cst.gov.sa "مراكز البيانات" "الرياض"`。
- 许可/土地：`site:balady.gov.sa "مركز بيانات" "رخصة بناء"`、`site:modon.gov.sa "DataVolt" "data center"`、`site:neom.com "data center" "DataVolt"`、`site:rcjy.gov.sa "data center" "Yanbu"`、`site:momah.gov.sa "data center" "building permit"`。
- 电力：`site:se.com.sa "380 kV" "data center"`、`"National Grid SA" "data center" "Dammam"`、`site:etimad.sa "data center"`。
- 云区域：`"Google Cloud" "me-central2" "Dammam" "CNTXT"`、`"Oracle Cloud" "Riyadh Region" "center3"`、`"Microsoft" "Saudi Arabia East" "Eastern Province"`、`"AWS" "Saudi Arabia Region" "Availability Zones"`。
- 行业：`site:datacenterdynamics.com "Saudi Arabia" "data center" "MW"`、`site:meed.com "Saudi" "data centre" "Riyadh"`、`site:argaam.com "مراكز البيانات" "المعمر"`、`site:spa.gov.sa "data center" "LEAP"`。
- 容量/状态：`"{project}" (MW OR megawatt OR MVA OR racks OR "under construction")`、`"{project}" (launched OR opened OR operational)`、`"{project_ar}" (توقيع OR ترسية OR افتتاح OR قيد الإنشاء OR تشغيل)`。
- 法名变体：`center3 OR "Digital Centers for Data and Telecommunications Company" OR "سنتـ3"`；`Mobily OR "Etihad Etisalat" OR "موبايلي"`；`Sahayeb OR "Sahayeb Data Park" OR "سحايب"`；`QST OR "Quantum Switch Tamasuk" OR "كوانتم سويتش تاماسك"`；`SCCC OR "Saudi Cloud Computing Company" OR "الشركة السعودية للحوسبة السحابية"`。

## 官方/监管管线要点（详见 explorer-official.md）

- CST 数据中心注册页（A）：https://www.cst.gov.sa/en/knowledge-center/digital-knowledge/data-center/data-centers-providers ；云注册页：https://www.cst.gov.sa/en/knowledge-center/digital-knowledge/cloud-computing/cloud-computing-providers 。逐设施抓 provider/设施名/城市/类别/状态；注册服务 15 天处理期，经商业门户+Nafath。
- MCIT/SDAIA/Vision 2030/SPA（A 公告级）：MCIT LEAP 2023 $580M 数据中心公告、HUMAIN 项目页、SDAIA 国家数据与 AI 战略、SPA 新闻流；ITA 贸易摘要为 **B**。
- 沙特交易所/年报（A）：stc 2022 年报称 center3 拥有集团数字基础设施资产（数据中心+海缆）、容量基数最高 125 MW、计划提至 300 MW；stc 2023 年报称 center3 完成 Riyadh Khurais 9.6 MW 扩展；MIS 官网称 Sahayeb 在 Riyadh/Dammam 有 6 个数据中心、初始 24 MW、可扩展 120 MW。
- 市政/环境：Balady（https://balady.gov.sa/en/services/issuing-building-permit ）、MoMRAH 许可查询、NCEC/eCompliance（https://ecompliance.ncec.gov.sa/ ）。
- 电力/工业区：SEC/National Grid SA、Etimad/MOF/NCGR 政府采购、MODON（Riyadh First Technology Park/First Industrial City）、NEOM/OXAGON（DataVolt 协议，首期预计 2028 运营）、RCJY（Jubail/Yanbu）、MISA、ECZA。
- 云区域（A=区域/城市存在，非精确地址）：AWS 2026 Saudi Arabia Region（3 AZ、>US$5.3B，选址未公开）；Azure Saudi Arabia East Q4-2026 可用（Eastern Province，3 AZ）；Google Dammam `me-central2`（Class C，经 CNTXT）；Oracle Jeddah 2020 + Riyadh（center3 为宿主）+ NEOM 计划；Huawei Cloud Riyadh Class C（合规页）；Alibaba/SCCC（stc 2022 与 Alibaba Cloud/eWTP Arabia/SCAI/SITE 合资）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：DCD（B，center3/QST/DataVolt/Oracle/Khazna/DAMAC/GDH 最佳英文贸易源）、MEED（B，海湾工程状态）、W.Media/Capacity Media（B）、Argaam（B+，沙特上市公司 MIS/Sahayeb 阿英双语）、SPA（A-/B+ 官方活动源）、S&P Global（B，市场框架：Riyadh/Dammam/Jeddah 为主选地，点名 Center3/DAMAC/QST/DataVolt/ZeroPoint/HUMAIN）。
- 运营商种子（存在性 A-，容量另证）：center3/stc（Riyadh/Jeddah/Dammam，DCD 报目标 300 MW by 2027 / 1 GW by 2030）、Mobily（Riyadh/Jeddah/Dammam/Unaizah）、Salam/ITC（Riyadh/Jeddah/Khobar 6 个 DC）、Zain KSA（Riyadh/Jeddah 电信云/边缘）、NourNet（Riyadh 北部 Tier-3、4,500 m²、450 机架、10 MVA）、QST（300 MW 计划=6×50 MW，首站 Dammam SPARK 9 MW）、DataVolt（Riyadh MODON First Technology Park 55,000 m² + Yanbu + NEOM Oxagon 1.5 GW AI 园区）、EDGNEX/DAMAC（Dammam/Riyadh，DCD 报 20 MW→55 MW 扩展）、GDH（Jeddah/Dammam）、Sahayeb/MIS（6 DC、24→120 MW）、Ezditek（RUH01 公主努拉大学、多城 170 MW 计划）、Khazna（Dammam 首站、最高 200 MW AI-ready）、HUMAIN（PIF，MIS 合同 + AirTrunk 合作 Riyadh 园区）、ZeroPoint（NEOM 管线）。
- 承包商回填：Group AMANA（QST Dammam）、EAMFCO/ABL（EDGNEX/DAMAC）、LG/Shaker（DataVolt/NEOM 冷却）、Vertiv（GDH 案例）、Alekhtiar（Mobily 设施工程）。
- 目录源（C/B-）：DataCenterMap、Baxtel、Datacenters.com、DC Byte、Reboot Monkey——仅作线索与别名图，不作 MW 终源。

## 来源分级

- **A** = 官方/一手：CST 注册列表与条例、Balady/MoMRAH 许可与完工证书、NCEC 环境许可、SEC/National Grid SA 记录、MCIT/SPA/Vision 2030/SDAIA/NEOM/MODON 官方公告、沙特交易所/年报、运营商官方设施页（存在/城市）、Uptime 证书查询、官方云区域页（区域存在）。
- **B** = 强二级：DCD/MEED/W.Media/Capacity/Argaam/S&P/Total Telecom/Developing Telecoms/Telecom Review、承包商 EPC 组合页、供应商案例。
- **C** = 弱/未验证：DataCenterMap/Baxtel/Datacenters.com/DC Byte、LinkedIn/社媒、市场报告摘要、无出处博客。
- 状态语义：`signed/MoU/land lease/investment plan`=意向（planned）；`financing secured/contract awarded/EPC/design and build`=planned/construction；`breaks ground/under construction`=在建；`launched/opened/go-live/available`+CST 非 Qualifying 注册=运营（区分整园区 vs 一期）。云区域页只证**云服务区域存在**，非建筑归属；物理设施需宿主/运营商/城市证据且不重复计数。
- 去重：按 `(最终母公司, 园区/设施别名, 城市/governorate, 阶段)` 归一化；Riyadh/Riyad、Jeddah/Jiddah、Khobar/Al Khubar、Madinah/Medina、Khurais/Khurays、Malga/Malqa、Duba/Duba\`、NEOM/Oxagon/Port of NEOM、center3/stc 均需别名消歧；Hijri 日期需转公历记录。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=SA，divisions=122 governorates，GeoNames admin2：13 区域 → governorates）。
2. **CST 扫描**：抓取注册数据中心服务商与云服务商；把每个 city/设施映射到 governorate（Riyadh→Ar Riyad；Dammam/Industrial City 2→Ad Dammam；Khobar→Al Khubar；Jeddah→Jiddah；Yanbu→Yanbu\` al Bahr；Duba\`/OXAGON→Duba\`；Unaizah→Qassim）。
3. **官方云扫描**：AWS Saudi Arabia Region、Azure Saudi Arabia East、Google Dammam、Oracle Jeddah/Riyadh/NEOM、Huawei Riyadh、Alibaba/SCCC——作为区域/城市种子，出现设施证据前不计为设施；不把多个 AZ 拆成多个设施。
4. **运营商官方扫描**：center3/stc、Mobily、Salam、Sahayeb/MIS、QST、DataVolt、TONOMUS/Ezditek、Khazna、EDGNEX/DAMAC、GDH、Equinix（LEAP 2025 $1B 承诺，尚无官方设施页→B）。
5. **许可/电力 join**：Balady/MoMRAH、当地 Amanah、NCEC/eCompliance、MODON/NEOM/RCJY/MISA/ECZA、SEC/National Grid/Etimad；对每个候选设施跑阿拉伯语+英语模板。
6. **年报/证书验证**：沙特交易所、年报、Uptime、ISO、承包商 EPC 引用；容量按原文单位记录并区分 IT load 与受电容量/MVA；输出 world 同 schema，无项目 division 写 `no_projects: true`。
7. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:15Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核沙特数据中心（122 governorates）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：center3 1 GW/300 MW 分阶段容量、QST 300 MW 各站点（SPARK 9 MW 首期）、Khazna Dammam 200 MW 当前状态、Equinix LEAP 2025 $1B/100 MW 承诺（无官方设施页）、Azure Saudi Arabia East 三个站点位置、AWS 区域选址（Riyadh/Eastern/Jeddah 证据搜索）。
