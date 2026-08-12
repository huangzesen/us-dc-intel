---
name: rw-datacenter-methodology
location: scripts/expansion/world/country-skills/RW/SKILL.md
description: 卢旺达数据中心发现与审计方法学（bilingual）。Rwanda datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (RURA licensing/statistics, MINICT/RISA/NCSA/NDPB, RPPA UMUCYO e-procurement, RDB investment/KIC, REG/REMA energy, cloud-region absence checks) plus industry/trade-press discovery (local press, DCD/trade press, operator pages, RINEX/PeeringDB, aggregators). Division model: city/province with 5 divisions (City of Kigali, Eastern, Northern, Western, Southern). Read before running RW exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# RW · 卢旺达数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：卢旺达无公开全国数据中心注册库、无可靠的可机检全国建设/EIA 许可数据库，且为小型但政策进取的市场——截至 2026-08 运营托管证据单薄（TrAC 营销声称 + 聚合目录条目），管线/线索为 PAIX Kigali、ADC Kigali（2022 宣布、状态不明）、Otech/BSC（2026 MoU）与仅聚合目录的 Raxio RW1/Paratus；本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双轨三角验证（registry-status / triangulation approach），以 RURA/MINICT/RISA/NCSA/RPPA/RDB 主证与强行业媒体为准，聚合目录仅作发现。本 skill 汇总两份最终审定的探索报告，作为 RW 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | RURA（牌照/ICT 统计/RINEX）、MINICT（政策）、RISA（实施，Smart Rwanda、RDAP）、NCSA（cyber.gov.rw）、数据保护法 058/2021 与 DPO、RPPA UMUCYO 电子采购、RDB 投资/KIC/经济特区、REG/EUCL/EDCL 与 REMA（能源/环境）、云区域缺失检查 |
| explorer-industry.md | 行业/厂商发现 | 本地媒体（The New Times、IGIHE、KT Press）、非洲/国际行业媒体（DCD、Connecting Africa、Agence Ecofin、The Stack、Datacentre Magazine）、运营商/厂商页（TrAC、PAIX、ADC、Raxio、MTN、Airtel、Liquid、BSC、Paratus、AOS）、RINEX/PeeringDB 互联、聚合目录 |

## 核心结构事实

1. **行政区划模型**：manifest 为 **city/province**，恰好 **5 个 division**：**City of Kigali、Eastern、Northern、Western、Southern**（对应基加利市 + 4 省；区/akarere 为第二层检索与地址解析）：City of Kigali（Gasabo、Kicukiro、Nyarugenge——唯一商业/电信集群；Kacyiru 的 Telecom House 驻 TrAC、RINEX、NCSA）；Eastern（Bugesera、Gatsibo、Kayonza、Kirehe、Ngoma、Nyagatare、Rwamagana——Mwulire 卢旺达航天局遥测站；布格塞拉机场在建；坦桑尼亚边境光纤走廊）；Northern（Musanze/Rubavu 旅游走廊，低产出）；Western（基伍湖甲烷气电厂=能源背景；Goma/Rubavu 边境）；Southern（Huye 卢旺达大学、Kamonyi 的 MTN 5G 扩展站点）。Kinyarwanda 名称用于检索召回：Umujyi wa Kigali、Intara y'Iburasirazuba（东）、Intara y'Amajyaruguru（北）、Intara y'Iburengerazuba（西）、Intara y'Amajyepfo（南）。
2. **注册库现状**：无公开全国数据中心注册库；无可靠在线建设许可检索（City of Kigali 与各区发布规划材料但无统一可机检数据库；REMA 为环境主管机构 rema.gov.rw）；最接近普查的是 **RURA ICT 市场统计与牌照 + RPPA UMUCYO 电子采购通告 + RDB 投资公告 + RISA 项目页**的组合；云区域官方列表为超大规模设施的**负向证据**。
3. **法律与监管**：RURA（2013-04-08 第 09/2013 号法设立；牌照普查与市场统计源，**牌照≠设施**）；MINICT（ICT 政策领导）；**RISA**（2017 年设立，协调 Smart Rwanda 总体规划与数字基建，RDAP 实施机构）；**NCSA**（网络安全/数据保护监督；站点为 **cyber.gov.rw（非 ncsa.gov.rw）**，地址 Telecom House 5 楼 8 KG 7 St, Kacyiru；《国家网络安全战略 2024–2029》）；**数据保护法 058/2021**（2021-10-13 通过、10-15 宪报；DPO dpo.gov.rw；**无全面本地化规则**，但个人数据出境须授权——法律为监管/需求背景，非设施证据）。**历史执法上下文**：2017 年 RURA 因 MTN 在境外运营 IT 服务违反牌照处以约 USD 8.5M 罚款——证明监管层推动受监管工作负载境内托管。
4. **互联与云（负向）**：**RINEX**（RURA 2009 年设立，Telecom House KG 7 Kacyiru，AS329521，2025 年底约 15 成员）为运营中 IXP，是互联锚点**非 DC 容量**；RICTA 管理 .rw 与 RINEX；IremboGov 为政府平台运营证据（托管地点未核实）；**无 AWS/Azure/GCP/OCI 卢旺达区域**（最近约翰内斯堡/开普敦）；Starlink 2023-02 起在卢旺达运营（连通性非设施）；卢旺达为内陆国、无海缆登陆（经肯尼亚/坦桑尼亚登陆点 TEAMS/SEACOM/EASSy 陆地光纤）。
5. **设施/项目种子（2026-08 证据状态）**：**TrAC Kigali 数据中心**（TransAfrica Communications；Telecom House, 8 KG 7 Ave, Kacyiru；trac.africa 营销云与 tier 3 托管——A 级营销声称、C 级物理细节、U 级 Uptime Tier III 认证）；**PAIX Kigali**（KIC 内 3 MW 载波中立目录条目——C 聚合/U 状态；PAIX 官方与 Africa50 强调加纳/肯尼亚资产）；**AOS Ltd**（Kigali Business Centre, KN 5 Rd；本地 IT 服务商托管，C，2023-06 更新）；**Raxio RW1**（仅聚合目录；Raxio 官方页**未列卢旺达**——U/C 直至官方确认）；**ADC Kigali**（2022-11 宣布 2 MW、2023 Q1 动工；B 宣布/U 当前状态；DCD 2026-06 称项目状态不明）；**Otech（Omantel）× Broadband Systems Corporation**（2026-06-03 AI-ready Tier III 共投 MoU；B MoU/U 场地）；**MTN Rwanda 核心/5G**（B 网络/C DC；MTN Centre Kigali PeeringDB fac 11839；2025-06 起 5G，含南部省 Kamonyi 站点）；**Airtel Rwanda**（B 运营商/C DC）；**Liquid Intelligent Technologies Rwanda**（2013 年收购 Rwandatel 资产；B 光纤存在/U 本地 DC）；**BSC**（2010 年成立基加利 ISP，全国光纤/无线；Otech MoU 伙伴）；**Paratus Rwanda**（B 连通性/C-U DC 目录；官方数据中心菜单列安哥拉/纳米比亚/赞比亚而非卢旺达）；**卢旺达航天局遥测站（Mwulire, Rwamagana, Eastern）**（2025-07 商业天线启用；边缘/电信设施记录，非商业数据中心）。
6. **语言与词汇**：卢旺达三语（Kinyarwanda/英语/法语），**英语与法语召回最佳**（centre de données、centre de traitement de données、hébergement、colocation、salle des serveurs、point de présence、fibre optique、appel d'offres、mise en service）；Kinyarwanda 低产出但用于区级政府帖（ikigo cy'imyirondoro、ububiko bw'amakuru、itsinda rya serveurs、ikoranabuhanga）。捕获生命周期动词：projet/étude/MoU（意向）、appel d'offres/AMI/tender/awarded（采购）、construction/travaux/groundbreaking（在建）、mise en service/opérationnel/inaugurated/go-live（运营）。
7. **可靠性分级**：A = 官方/主源（RURA 牌照/统计/决定/法令、MINICT/RISA/NCSA/NDPB 文件与招标、RPPA UMUCYO 通告、RDB 投资材料、政府所有运营商页、官方云区域列表、政府渠道核实的原始新闻）；B = 强二手（DCD、Connecting Africa、Agence Ecofin、The Stack、Datacentre Magazine、The New Times/IGIHE/KT Press 引用官方材料、PeeringDB 互联元数据、ISOC IXP 追踪、世行/UNECA 项目文件）；C = 仅线索（DataCenterMap、datacenters.com、datacenterplanet、Baxtel、Inflect、无具名场地的厂商营销、旧 MoU、LinkedIn/社媒、无源博客）；U = 未验证（仅聚合或单一弱源，升级前复查）。**分级只覆盖该源实际支撑的事实**：已核实 MoU（B）不使设施运营；已核实服务页（A）不证明物理站点地址。
8. **计数与去重规则**：设施存在须源同时点名基础设施**与**位置（足以区分物理站点）；已营销托管/云服务无具名站点 = 提供商级服务线索（另列）；`facility_type` 精确（commercial_colocation、telco_core、ixp、government_hosting、planned_commercial_dc、edge_ground_station、registry_infrastructure、lead_only）；`status` 精确（operational、marketed_service、announced、mou、procurement、under_construction、unknown、negative）；**容量字段（MW/机架）无官方/运营商/招标源则保持 null**（PAIX 3 MW、ADC 2 MW 来自目录/宣布，按此引用）；**Telecom House 为一栋楼、多运营商（TrAC/RINEX/NCSA）——按运营商分别记录，不得合并**；ICT 办公室/网吧/电脑实验室/NGO 服务器机房/GIS 室/软件平台一律不计。

## 常用查询模板

```text
site:rura.rw licence internet OR operator OR "service provider" Rwanda
site:rura.rw "centre de donnees" OR "data center" OR hebergement OR cloud OR RINEX
"RURA" Rwanda "data center" OR "centre de donnees" OR colocation
site:minict.gov.rw ("data centre" OR "data center" OR hosting OR RDAP OR "Smart Rwanda")
site:risa.gov.rw (RDAP OR "data centre" OR hosting OR tenders OR AMBAS)
site:cyber.gov.rw ("data centre" OR "data center" OR hosting OR "critical infrastructure")
site:rppa.gov.rw tender OR "avis d'appel d'offres" OR UMUCYO ICT
"UMUCYO" Rwanda tender ("data centre" OR "data center" OR serveurs OR hebergement OR cloud)
site:rdb.rw ("data centre" OR "data center" OR KIC OR "innovation city" OR SEZ)
"Kigali Innovation City" data centre OR datacenter
site:reg.rw OR site:eucl.rw ("data centre" OR "data center" OR serveurs OR "grand client")
site:rema.gov.rw EIA "centre de donnees" OR telecom OR fibre
"Gasabo" OR Kacyiru OR "Telecom House" Rwanda ("data centre" OR colocation OR serveurs)
"Kigali" ("data centre" OR "data center" OR colocation OR hebergement OR "Tier III")
site:trac.africa ("data centre" OR colocation OR hosting OR cloud)
site:paix.io (Kigali OR Rwanda) ; site:raxiogroup.com Rwanda
site:africadatacentres.com (Kigali OR Rwanda)
"Broadband Systems Corporation" Rwanda fibre OR "data centre"
"Paratus" Rwanda "data centre" OR Kigali
site:datacenterdynamics.com Rwanda OR Kigali data center
site:newtimes.co.rw Rwanda ("data centre" OR colocation OR hosting)
site:en.igihe.com Rwanda ("data centre" OR serveurs OR fibre)
"Rwanda" ("centre de donnees" OR "data center") (tender OR "appel d'offres") 2025 OR 2026
"RINEX" OR "Rwanda Internet Exchange" members facilities Kigali
site:peeringdb.com Kigali Rwanda facility
"Rwanda" AWS OR Azure OR "Google Cloud" OR OCI region - absence check
site:uptimeinstitute.com Rwanda ("certified" OR "Tier III") - negative control
"Rwamagana" OR Mwulire Rwanda (teleport OR ground station OR satellite)
```

## 官方/监管管线要点（详见 explorer-official.md）

- **RURA**：牌照普查与市场统计源（Q2 2025 报告：2 个 MNO、4 个 ISP、1 个批发网络服务商、2 个网络设施商、23 个零售 ISP——2025 结构）；RINEX 2009 年设立；ICT 统计决定运营商份额与结构。
- **RPPA UMUCYO**：全国电子采购系统（umucyo.gov.rw；勿用 umuganda.rdb.rw）；政府 ICT/数字招标全部经其或部委门户；OCDS 开放承包数据 data.open-contracting.org/en/publication/145。
- **RDB/KIC**：RDB 一站式投资与激励；Kigali Innovation City（GoR+Africa50+BADEA，60 公顷，动工公告；MINECOFIN US$20M 基础设施融资）为 PAIX 目录声称所在园区——园区存在不证明 PAIX 运营。
- **能源/规划/环境**：REG（2014-07 成立政府控股，EUCL/EDCL 子公司）电网背景（2025-07 底全国通电率 84.6%：59.6% 电网 + 约 25% 离网；水电/基伍湖甲烷气/泥炭/光伏/进口）；REMA EIA 记录；City of Kigali 许可（勿假设可检索完整性）；大型电力声称须与 REG/EUCL 连接或变电站证据交叉核对。
- 每轮枚举须覆盖全部 5 个 division，真无活动则记 `no_projects: true`；预期高度集中于 Kigali：City of Kigali（所有已识别候选）、Eastern（Mwulire 遥测站 + Bugesera/Rwamagana 检索）、Northern/Western/Southern（大学/电信边缘/光纤 PoP，商业 DC 预期负向）。
- 来源优先检查表：RURA → MINICT/MINECOFIN → RISA/RDAP → NCSA/NDPB/DPO → RPPA UMUCYO → RDB → REG/RURA 能源 + REMA + City of Kigali 许可 → 世行项目文件（RDAP P175437）+ UNECA/D4D Hub 市场简报 → 运营商官方页 → ISOC/PeeringDB → 行业媒体（B 佐证）→ 聚合目录（C/U 发现）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 本地媒体：The New Times（最高价值英语媒体；Liquid 数据主权、MTN 5G）、IGIHE（MTN 5G 含 Kamonyi、RDAP）、KT Press（Irembo 历史）、RwandaTechNews（KIC、IremboGov）、CNBC Africa（MTN 罚款、Starlink 启动）；行业媒体：DCD（ADC 2022、Otech/BSC 2026；DCD 页可能对 curl 403 但浏览器/搜索可开）、Connecting Africa、Agence Ecofin、Datacentre Magazine（Raxio US$380M 2026-07）、The Stack（Raxio 确认科特迪瓦/坦桑尼亚而非卢旺达）。
- 验证规则：A 运营设施 = 官方/运营商/捐赠方源点名站点+位置+基础设施功能；B 运营设施 = 强媒体点名站点/位置并最好引官方；C 线索 = 聚合/社媒/转售/无本地物理证据服务页；U = 仅聚合或单一弱源（Raxio RW1、Paratus 目录、PAIX 状态、ADC 现状、TrAC Uptime Tier III、AOS）；提供商级服务 = 官方托管/云/服务器服务但无具名设施（TrAC hosting、Liquid cloud、MTN 服务）；计划/管线 = ADC/Otech-BSC/PAIX 一律保持非运营直至招标/建设/揭牌证据。
- 诚实结论（2026-08）：运营托管证据单薄（TrAC 营销 + 聚合列表）；RURA/MINICT/RISA/NCSA/RPPA/RDB 主证与强行业媒体之外的一切保持 U/C 直至复核。

## 维护注意（更新纪律）

- **更新节奏**：每季度——RURA ICT 统计与牌照页、RPPA UMUCYO 招标扫描（“data centre”/“hosting”/“serveurs”/“cloud”）、复核 ADC Kigali/Otech-BSC/PAIX Kigali/Raxio RW1/Paratus Rwanda 状态（运营商站 + DCD Rwanda tag）；每半年——MINICT/RISA/NCSA 政策与项目页（RDAP 里程碑、网络安全战略行动、数据保护规则）、REG 电网/能源报告（电力可行性变化）；每年——复核全部 U 级聚合条目（TrAC Tier III 声称、PAIX 3 MW、AOS、Raxio RW1、Paratus）、确认 Uptime Institute 认证状态（2026-08 卢旺达无已验证认证）；事件驱动——任何卢旺达云区域宣布（AWS/Azure/GCP/OCI）为最大变化，监视官方区域页。
- **来源核验**：复核层逐个点击 A 级 URL；NCSA 站点为 cyber.gov.rw（非 ncsa.gov.rw）；DCD 页 curl 403 不算死链（用浏览器/搜索）；PeeringDB 条目为互联元数据（B/C）非设施证明。
- **不删除纪律（no-deletion）**：已复核记录不得删除；状态变化改标（announced/mou → procurement → under_construction → operational）并保留原始证据链；无支撑条目降级为 U/C 保留而非移除；负向检索（无项目）须如实记录而非跳过。
