---
name: ae-datacenter-methodology
location: scripts/expansion/world/country-skills/AE/SKILL.md
description: |
  United Arab Emirates (AE) datacenter discovery & audit methodology. No national registry; enumeration joins emirate-level planning (Dubai Municipality / Build in Dubai / DDA / Trakhees; Abu Dhabi DMT/TAMM/Binaa), utility/NOC workflows (DEWA, DoE/TAQA Distribution/EWEC, EtihadWE, SEWA), free-zone/master-developer authorities (DIC/TECOM, DSO/DIEZ, Masdar City, KEZAD/KIZAD, JAFZA), official cloud regions (AWS me-central-1 UAE 3 AZ, Azure UAE North Dubai + UAE Central Abu Dhabi, Oracle me-dubai-1 + me-abudhabi-1), and operator pages (Khazna, G42/Stargate, Equinix, Moro Hub, Gulf Data Hub, Pure DC, du, e&/SmartHub). Division model: 28 municipality/city areas. Read this before running AE exploration/audit batches. Routes to explorer-official.md (planning/utility/regulator/cloud) and explorer-industry.md (press/vendor/Arabic patterns).
---
# AE · 阿联酋数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为阿联酋数据中心枚举提供「酋长国规划许可 + 电力/公用事业 + 自由区 + 云区域 + 运营商官网」五线并联的查询框架。阿联酋**没有全国性数据中心注册库**，许可按**酋长国与管辖机构**高度碎片化：迪拜走 Dubai Municipality / Build in Dubai、DDA（TECOM/DIC 类区域）、Trakhees（PCFC/JAFZA）；阿布扎比走 DMT/TAMM/Binaa 与阿布扎比/阿莱茵/达夫拉三市；北部酋长国走各自市政府门户 + EtihadWE。大型项目**电力常是最佳官方线索**（DEWA、DoE/TAQA/EWEC、EtihadWE、SEWA）。主商业集群在**迪拜与阿布扎比**，次要在沙迦、阿治曼、富查伊拉、哈伊马角。本 skill 汇总两份探索报告（官方管线 + 行业发现），供阿联酋探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：Dubai Municipality/Build in Dubai/DDA/Trakhees、DMT/TAMM/Binaa、DEWA/DoE/TAQA/EWEC/EtihadWE/SEWA、TDRA、官方云区域页（AWS/Azure/Oracle）、运营商官网（Khazna、Equinix、du、e&、UAE-IX/DE-CIX） |
| `explorer-industry.md` | 行业/厂商发现：DCD/W.Media/Construction Week 等贸易媒体、WAM 与各酋长国官方媒体、自由区生态（Masdar、KEZAD、DSO/DIEZ、JAFZA）、英阿双语查询模式、逐分区枚举法 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库**：枚举 = 酋长国规划系统 + 自由区许可 + 公用事业/NOC + 官方开放数据 + 云区域页 + 电信/托管页 + 贸易媒体的联合；许可管辖按酋长国与机构划分（Dubai Municipality vs DDA vs Trakhees vs DIEZ；DMT/TAMM/Binaa 覆盖阿布扎比、阿莱茵、达夫拉）。
2. **电力是最好的官方线索**：迪拜走 DEWA Building NOC 与电力接入；阿布扎比走 DoE（https://www.doe.gov.ae/）、TAQA Distribution（ADDC/AADC 旧称）、EWEC（https://ewec.ae/，阿布扎比水电唯一采购方）；北部酋长国（阿治曼/富查伊拉/哈伊马角/乌姆盖万及部分沙迦）走 EtihadWE（前 FEWA）；沙迦单独走 SEWA。电网容量、自供电、太阳能 PPA 容量、IT 负载**分列四字段**。高价值样例：DoE 的 `Khazna Data Center Limited - SS Licence` PDF 把运营商与发电/自供电许可绑定。
3. **自由区与总开发商是关键路由**：大量设施位于 Dubai Internet City/TECOM、Dubai Production City/IMPZ、Dubai Silicon Oasis、Masdar City、KEZAD/KIZAD、Meydan、JAFZA、Hamriyah、SAIF Zone、RAKEZ、Fujairah SmartHub 等；权威页（DDA、Masdar City、KEZAD/AD Ports、DIEZ、PCFC）常先于普通市政府页暴露项目。
4. **云区域 = 城市级种子，不是物理地址**：AWS `me-central-1` Middle East (UAE) 3 AZ（2022 开放）；Azure UAE North=迪拜 `uaenorth`、UAE Central=阿布扎比 `uaecentral`（受限）；Oracle UAE East 迪拜 `me-dubai-1` + UAE Central 阿布扎比 `me-abudhabi-1`；**Google Cloud 在阿联酋无区域**（附近 `me-central1` 是多哈/卡塔尔），不得把 GCP 算作阿联酋设施证据。
5. **英文+阿拉伯文双语搜索**：阿拉伯文核心词 `مركز بيانات`/`مراكز البيانات`（数据中心）、`تصريح بناء`/`رخصة بناء`/`تصاريح البناء`（建筑许可）、`شهادة إنجاز`（完工证书）、`عدم ممانعة`（NOC）、`كهرباء`（电力）、`محطة فرعية`（变电站）、`ميغاواط`（兆瓦）。阿拉伯文常用于官方媒体转载与酋长国本地公告。
6. **别名归一化**：`e&`/`Etisalat` 旧数据中心资产按时间映射到 Khazna 或 SmartHub；`IMPZ`=Dubai Production City；`DIC`=Dubai Internet City；`KIZAD` 旧品牌可能以 `KEZAD` 出现；`ADWEA/ADWEC/ADDC/AADC` 是阿布扎比能源旧称，现多由 DoE/EWEC/TAQA Distribution 代表。
7. **阶段词与容量陷阱**：`announced`/`MoU`/`land lease`/`secured power`/`groundbreaking`/`under construction`/`launched`/`inaugurated`/`operational`/`campus build-out` 必须原文记录；阿联酋宣传常用整个园区/长期叙事（如 Stargate 5 GW 园区、Khazna 673 MW 组合），当前单楼 IT 负载 ≠ 满配园区容量；电网/自供/太阳能 MWp 与 IT MW 分列。

## 查询模式（复制粘贴模板见 explorer-official.md §6 与 explorer-industry.md §5）

- `"United Arab Emirates" ("data center" OR "data centre" OR datacenter) "{emirate}"` / `"{emirate}" "{division}" "data center" ("MW" OR "MVA" OR "IT load")`
- `site:dm.gov.ae ("data center" OR "مركز بيانات")` / `site:buildindubai.gov.ae "data center"` / `site:dda.gov.ae ("Final Building Permit" OR "Construction Permits") "{operator}"`
- `site:tamm.abudhabi "data center" OR "مركز بيانات"` / `"Binaa" "data center" "Abu Dhabi"` / `site:mediaoffice.abudhabi "data center" "DMT" OR "Binaa"`
- `site:dewa.gov.ae "{operator}" ("NOC" OR "Building NOC" OR "electricity connection")` / `site:doe.gov.ae filetype:pdf Khazna "Data Center" "Licence"` / `site:ewec.ae "data center" "Abu Dhabi"`
- `site:etihadwe.ae ("data center" OR datacenter OR "substation")` / `site:sewa.gov.ae "data center" OR "مركز بيانات"`
- `site:tdra.gov.ae "data center" OR AWS OR cloud` / `site:wam.ae "data center" Khazna OR "Moro Hub"`
- `"مركز بيانات" "الإمارات" "تصريح بناء"` / `"مراكز البيانات" "دبي" "تصاريح البناء"` / `"مركز بيانات" "أبوظبي" "دائرة الطاقة"`
- 阶段词映射（阿拉伯文）：مذكرة تفاهم/اتفاقية=意向（C/B）；تخصيص أرض/تأجير الأرض=拿地（A/B 官方）；وضع حجر الأساس/بدء الأعمال الإنشائية=开工（B/A）；افتتاح/تدشين/إطلاق/دخل الخدمة=运营（须运营商页复核）。

## 官方/监管管线要点（详见 explorer-official.md）

- **迪拜规划/许可**：Dubai Municipality 建筑许可流程 https://www.dm.gov.ae/municipality-business/building-permit-steps/；Build in Dubai https://buildindubai.gov.ae/services（一站式，公开检索有限，但给出权威流程与服务名）；开放数据 https://www.dm.gov.ae/open-data2/ 与 Bayanat 数据集；DDA https://dda.gov.ae/（DIC/DPC/IMPZ 类 TECOM 集群的规划/许可/完工证）；Dubai Internet City https://www.dic.ae/；Trakhees/PCFC https://pcfc.ae/（JAFZA/杰贝阿里特殊区）。
- **阿布扎比规划/许可**：DMT https://www.dmt.gov.ae/en；TAMM 新建建筑许可 https://www.tamm.abudhabi/en/life-events/business/housing-construction/construction/RequestaNewBuildingPermit；Binaa 平台（DMT 数字化建筑许可）；开放数据 https://data.abudhabi/opendata/；Masdar City https://masdarcity.ae/（Khazna 二期 + Emerge 屋顶太阳能协议）；KEZAD/KIZAD https://www.kezadgroup.com/（Taweelah/Khalifa 工业区）。
- **北部酋长国与沙迦**：Sharjah Municipality https://shjmun.gov.ae/servicedirectory/subServices/10（普通建筑许可/变更/完工证/公用事业完工连接证）；Ajman Municipality & Planning Department https://www.ajman.ae/en/servicecatalog/services/3278；RAK SANAD https://sanad.mun.rak.ae/docs/en/building-permits（交叉 RAKEZ）；Fujairah Municipality https://www.fujmun.gov.ae/ + Bayanat 建筑许可数据集；UAQ 市政府（低密度但勿跳过）。
- **监管/政策**：TDRA https://tdra.gov.ae/en/（欢迎 AWS 入阿联酋声明 https://tdra.gov.ae/en/media/press-release/2021/tdra-welcomes-awss-decision-to-open-data-centers-in-the-uae；非设施注册库）；UAE 官方门户 https://u.ae/；Digital Dubai / Data.Dubai；Abu Dhabi/Dubai Media Office（A 级项目公告，设施状态仍须许可/电力佐证）。
- **云区域页**：AWS https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html + https://aws.amazon.com/blogs/aws/now-open-aws-region-in-the-united-arab-emirates-uae/（me-central-1，3 AZ，需 opt-in）；Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list（uaenorth 迪拜 / uaecentral 阿布扎比受限）；Oracle https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm（me-dubai-1 / me-abudhabi-1）；GCP https://cloud.google.com/about/locations（**无阿联酋区域**）。
- **运营商官方页（A 级存在性）**：Khazna https://khaznadatacenters.com/（官方称 30 个在营数据中心、6 个在建项目、673 MW 组合；AUH6 Masdar、Mafraq、AUH4/AUH8；QAJ1 阿治曼 100 MW AI 优化设施，DCD 称由 EtihadWE 供电）；G42/Stargate https://www.g42.ai/resources/news/global-tech-alliance-launches-stargate-uae（阿布扎比 5 GW UAE-US AI Campus 内 1 GW Stargate 集群）；Equinix 迪拜 DX1/DX2/DX3（IMPZ，UAE-IX by DE-CIX）+ 阿布扎比 AD1（Masdar City）；Moro Hub/Digital DEWA https://www.morohub.com/（Dubai Marina、Warsan 绿色数据中心、MBR Solar Park/Saih Al-Dahal）；Gulf Data Hub https://www.gulfdatahub.ae/（DSO 园区、KIZAD/ICAD 项目）；Pure Data Centres https://pure-dc.com/locations/abu-dhabi/（Yas Island）；du（阿布扎比至迪拜五设施成长叙事）；e&/Etisalat SmartHub（富查伊拉+迪拜地理冗余，DE-CIX SmartHub IX）。
- **B 级容量/项目信号**：VOLT UAE/DIEZ（DSO AI-ready 项目）；Siada/Innovation City（哈伊马角主权 AI/GPU 数据中心）；BEEAH Digital/Khazna 沙迦 JV（Kalba Tier 3，SCTA 合作）；XDS Data Centres（沙迦 SRTI Park 1 MW 浸没式）；Pacific Controls（杰贝阿里/TechnoPark 旧资产，状态须核实）；G42/e& 合并（12 个 Etisalat/G42 设施并入 Khazna，用于去重）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **贸易媒体分级**：DCD（B，UAE 标签 https://www.datacenterdynamics.com/en/news/?tag=uae）、W.Media（B）、Construction Week Middle East（B，承包商/工程 award）、MEED/Zawya/AGBI/Arabian Business/Gulf Business/Khaleej Times/The National（B-/C+，常付费墙）、Fast Company ME/TahawulTech/ITP.net/Telecom Review Arabia（B-/C+）。官方媒体：WAM https://www.wam.ae/（A）、Dubai Media Office https://mediaoffice.ae/（A）、Abu Dhabi Media Office https://www.mediaoffice.abudhabi/（A）、Sharjah Government Media Bureau https://sgmb.ae/（A）。
- **运营商/开发商矩阵（按地理）**：阿布扎比=Khazna AUH6 Masdar/Mafraq、G42/Core42/Stargate、Equinix AD1、Pure DC Yas Island、Gulf Data Hub KIZAD/ICAD；迪拜=Moro Hub（Marina/Warsan/Solar Park）、Khazna DIC/DDD/Ibn Battuta/Jebel Ali（DXB2/DXB3/DXB8/DXB9/Etisalat Earth Station）、Gulf Data Hub DSO、Equinix DX1/DX2/DX3、VOLT/DIEZ DSO；沙迦=Khazna/BEEAH/SCTA Kalba、XDS SRTI Park、e& Al Dhaid 模块化 DC；阿治曼=Khazna QAJ1 100 MW；富查伊拉=e& SmartHub 海缆登陆；哈伊马角=Siada Innovation City。
- **自由区/园区锚点**：Masdar City、Yas Island、KIZAD/KEZAD、ICAD/Mussafah、DSO、DPC/IMPZ、DIC、Dubai Design District、Dubai Marina、JAFZA/Jebel Ali、Warsan、MBR Solar Park/Saih Al-Dahal、Fujairah 海缆/SmartHub、Kalba/COMTECH Freezone、SRTI Park、Innovation City/RAK DAO。
- **目录来源（C）**：Data Center Map / Baxtel / Datacenters.com / PeeringDB / Cloudscene 仅作地址/别名交叉；Uptime Institute 认证名单为 A（认证设施名/状态）；DC Byte/Structure Research/CBRE/JLL/Arizton 市场报告仅作聚合语境。
- **去重与验证规则**：云区域/AZ 不单独计为物理设施；IX 会员名单不算数据中心；电厂不算数据中心（除非绑定命名数据中心项目）；电信机房须有设施级托管证据；e&/Etisalat 旧资产与 Khazna 按来源日期去重；`DX1`/`DX2`/`SmartHub`/`AUH8`/`Mafraq`/`Masdar`/`Meydan` 保留为别名。

## 来源分级

- **A** = 官方/一手：运营商设施/发布页、WAM 或酋长国官方媒体、DMT/TAMM/Dubai Municipality/DDA/Trakhees/KEZAD/自由区当局、DEWA/EWE/SEWA/ADDC/AADC、Uptime Institute 认证、官方云区域文档、市政府建筑许可/完工证、公用事业 NOC/连接/许可。
- **B** = 强二级：DCD、W.Media、Construction Week Middle East、The National、Gulf Business、Zawya、MEED、Fast Company Middle East、DC Byte、供应商案例（Schneider/Huawei/Vertiv/Turner & Townsend/承包商），点名运营商/地点/容量。
- **C** = 弱线索：Data Center Map、Baxtel、Datacenters.com、Cloudscene、社交帖、市场报告 PR 摘要、Wikipedia、旧分销商清单。仅作线索。
- 状态语义：operational=运营商页/政府或公用事业公告/Uptime 认证/IX+运营商确认；construction=官方开工/承包商案例/许可 NOC/电力连接证据；planned=MoU 仅当具备开发商+酋长国/自由区+设施类型+至少一项具体地点/容量/土地/电力陈述；云区域只记云区域证据。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=AE，divisions=28 municipality/city areas），按 explorer-industry.md §6 酋长国→自由区/工业区→运营商/媒体扫描→官方/许可/电力交叉→分区映射。
2. 种子：运营商官网（Khazna、G42/Core42、e&/SmartHub、Moro Hub、GDH、Equinix、Pure DC、du、XDS、BEEAH、VOLT、Siada）+ 云区域页（AWS/Azure/Oracle）+ UAE-IX/DE-CIX。
3. 扫描：官方媒体（WAM/各酋长国 Media Office）→ 酋长国规划（Dubai：DM/DDA/Trakhees；AD：DMT/TAMM/Binaa；北部：市政+自由区）→ 电力（DEWA/DoE-TAQA-EWEC/EtihadWE/SEWA，搜 NOC/connection/substation/MW/MVA/self-supply/solar）→ 贸易媒体（B 桥）→ 目录（C）。
4. 验证：A 级设施证据=市政府/自由区许可或完工证、公用事业 NOC/连接/许可、运营商官方设施页、政府媒体项目公告；按 emirate/division/authority/free-zone/operator/grade/evidence type 记录；IT MW、电网 MW/MVA、自供 MW、太阳能 MWp、园区 GW 分列。
5. 输出：按 world schema 写结果，附证据日期与分级；分区映射仅在命名区域/自由区/地标可支持时落 division，否则保留酋长国级不确定并标注映射置信度。
6. 无项目判定：乌姆盖万、Manama、Masfut、Dibba、Al Madam、Al Batayih、Milehah 等低密度分区需显式负面搜索记录（含英文变体与阿拉伯文），设 no_projects: true 需官方+媒体+运营商三面无信号。
7. 遵守 NO-DELETION；本 skill 与两份 explorer 均为只读输入，只新增 SKILL.md 与 ANATOMY.md。

## 待办（2026-08-12 02:24Z）

- [x] explorer-official.md 与 explorer-industry.md 已完成并合并为本 SKILL.md。
- [ ] 下一步：每批 50× codex terra agents，注入本 skill 后按 28 分区逐区枚举（优先 Abu Dhabi - Abu Dhabi Municipality、Dubai Sectors 1-9、Sharjah、Ajman、Fujairah、Ras Al Khaimah）。
- [ ] 待核实：Stargate UAE 5 GW 园区的 DMT/DoE/EWEC 许可与地块证据；Khazna 673 MW 组合的设施级分解（AUH1/AUH4/AUH6/AUH8 各址状态）；Moro Hub Warsan 与 MBR Solar Park 设施的 DEWA 电力记录；GCP 阿联酋无区域结论随时间更新。
