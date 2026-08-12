---
name: ye-datacenter-methodology
location: scripts/expansion/world/country-skills/YE/SKILL.md
description: |
  Yemen (YE) parent-level methodology for data-center enumeration at division granularity (22 divisions
  including Western Coast = Al Hudaydah/Hodeidah search space and Sanaa City). Yemen has no national
  data-center registry, no independent telecom regulator, and no open planning-permit database; enumeration
  assembles state operators (PTC/YemenNet, TeleYemen, AdenNet), the National Information Center (NIC),
  dual MTIT ministries (IRG/Aden vs Ansar Allah/Sana'a), cable landing stations, UN/World Bank procurement,
  universities, banks, and press. Dual authority is the master frame: record control-side for every lead.
  War damage and power constraints are material; no MW-class commercial colo evidence as of 2026-08-12.
  No hyperscaler public region. Routes to explorer-official.md (dual ministries/state operators/cables/
  procurement pipeline) and explorer-industry.md (press/operator/directory pipeline).
---

# YE · 也门数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：也门没有国家数据中心登记册、独立电信监管机构或开放式规划许可数据库；枚举必须由国有运营商（PTC/YemenNet、TeleYemen、AdenNet）、国家信息中心（NIC）、双部委（MTIT 亚丁/萨那）、海缆登陆站、联合国/世行采购、大学、银行与媒体拼接。双重政权（IRG/亚丁 vs Ansar Allah/萨那）是最重要的框架——机构（MTIT、NIC、央行甚至 Saba 通讯社）均存在两份，每条线索必须记录控制方。战争破坏与电力约束是实质性的；截至 2026-08-12 无 MW 级商业 colo 证据。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供也门探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：双 MTIT（Aden/Sana'a）、PTC/YemenNet、TeleYemen、AdenNet+RIPE、NIC、CSO、UNGM/世行采购、海缆登陆站、云区域阴性对照、22 区策略 |
| `explorer-industry.md` | 行业管线：行业媒体/本地媒体、运营商与厂商扫库、目录处理、逐区行业矩阵、候选处理范例 |

## 核心结构事实（框定每次搜索）

1. **无登记册/无独立监管**：也门没有国家数据中心登记册、独立电信监管机构或开放式规划许可数据库；MTIT（两个变体）既发牌照又同时运营国有网络（PTC 固话/YemenNet、TeleYemen 网关），无 ARPCE/TDRA 式独立监管；法律基础为 1991 年第 38 号电信法（1996 年第 33 号修订）。
2. **双重政权（主框架）**：自 2014-2015 年存在两个政府——国际承认政府（IRG，亚丁：MTIT、AdenNet、Saba-Aden、央行亚丁分支）与 Ansar Allah（胡塞）事实当局（萨那：MTIT 萨那、YemenNet/PTC 资产、NIC yemennic.net、Masirah/Al-Thawra）；NIC 与央行都存在两份；**每条记录必须标注控制方**，绝不静默合并两套证据。
3. **PTC/YemenNet（萨那）**：YemenNet 运行国家 ADSL/宽带平台；萨那边 Saba 报道 PTC 提供带安全/冷却/机柜的 `DATA CENTER` 托管空间，报告期内托管 69 家公司（saba.ye/ar/news3243831.htm，A）；无 MW/机架数/街道地址披露。
4. **TeleYemen（唯一国际网关，A 锚点实体）**：官方页称自 1971/72 年起为唯一持牌国际电信网关、2004 年起 100% 国有（PTC 75% + 也门邮政 25%）；托管在 TeleYemen 服务器上；总部萨那（26-Sept/Al-Tahreer），分支亚丁/荷台达/穆卡拉/赛永；登陆站：亚丁（Aden-Djibouti、AAE-1）、Al Ghaydah/马哈拉（FALCON）、荷台达（FALCON，状态敏感）。
5. **AdenNet（IRG 4G ISP，亚丁）**：2018-06 由 IRG 创立以对抗胡塞控制的 YemenNet；RIPE 成员记录（Al-Mulla Main Street, Aden，A）、AS204317；二期（2024）扩展 Abyan/Lahij/Hadhramaut；亚丁核心网络/服务器设施是南方最可能的 IRG 侧国家 DC 线索，物理 DC 目前为 **B 线索**。
6. **战争破坏实质化**：世行动态需求评估与 2023 宽带冗余研究、Sana'a Center 部门研究记录了严重电信损坏、制度碎片化、燃料/电力限制与反复的海缆中断风险；前线/重轰炸省（Saada、Western Coast/荷台达、Taiz、Marib、Jouf、Hajjah、Beida）的每条线索都需新鲜状态核查。
7. **电力是约束而非土地**：国家电网输出远低于需求；设施靠柴油发电机、电池与 2015 年后太阳能；不推断 MW 级数据中心，仅当绑定具名设施时记录 kVA/kW。
8. **国际连通性 = 国家战略资产**：世行 2023 研究称 FALCON 与 Aden-Djibouti 为当时唯一活跃海缆，AAE-1 当时未提供活跃冗余；2024-2025 红海海缆事件使状态易变；陆路 al-Wadiyah（沙特）、Haradh（Hajjah）、Shihin（阿曼，不稳定）。
9. **无超大规模区域**：官方 AWS/Azure/GCP/OCI 区域列表均无也门区域（2026-08-12）；本地 `cloud` 声明是国有运营商/银行/大学/小提供商的托管/主权云服务。
10. **语言**：阿拉伯语为主（مركز بيانات/مراكز البيانات/مركز المعلومات/استضافة المواقع/الحوسبة السحابية/غرفة الخوادم/محطة الأرضية/كبل بحري/مذكرة تفاهم=MoU/مناقصة=招标/تدشين=启用）；英语用于 UN/世行、行业媒体、海缆与云页面。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§3、explorer-industry.md §1/§2/§5）

```text
site:sabanew.net "مركز بيانات" OR "data center"
site:saba.ye "مركز بيانات" OR "data center"
site:masirahtv.net "data center" OR "مركز بيانات"
site:yemen.gov.ye "مركز البيانات"
"وزارة الاتصالات" عدن "مركز بيانات"
"وزارة الاتصالات" صنعاء "مركز بيانات"
"YemenNet" "data center" OR "مركز بيانات" OR "غرفة الخوادم"
"المؤسسة العامة للاتصالات" "DATA CENTER"
"المؤسسة العامة للاتصالات" "استضافة موقعة" "السيرفرات"
"TeleYemen" "gateway" Aden OR Sana'a
"TeleYemen" "data center" OR "hosting"
site:teleyemen.com.ye hosting OR webhosting
"AdenNet" "data center" OR "core network" OR "server"
AS204317 "Aden Net"
site:adennet4g.net "مركز" OR "data" OR "خوادم"
site:yemennic.net "مركز بيانات" OR "خوادم" OR "data"
"المركز الوطني للمعلومات" عدن "مركز بيانات"
site:ungm.org Yemen "4G" OR "telecommunications" OR "data" Aden
site:documents.worldbank.org Yemen ICT "data center" OR "e-government"
"{governorate}" "data center" Yemen
"{muhafazah_ar}" "مركز بيانات"
"{muhafazah_ar}" "استضافة المواقع" OR "الحوسبة السحابية"
"FALCON" cable Yemen "Aden" OR "Hodeidah" OR "Ghaydah"
"AAE-1" Yemen Aden "landing"
"اليمن" "مركز بيانات" "هواوي" OR "السعودية" OR "الإمارات"
"Yemen" "data center" "Saudi" OR "UAE" OR "China" OR "Huawei"
site:datacentermap.com/yemen "{operator}"
"Yemen" "AWS Region" site:aws.amazon.com
```

## 官方/监管管线要点（详见 explorer-official.md）

- **双 MTIT**：IRG（亚丁，经 sabanew.net）与 Ansar Allah（萨那，经 saba.ye/yemen.gov.ye/Al-Masirah）；同时是监管者与运营商所有者；PM Bin Brik 2025-06-22 指示紧急亚丁电信现代化计划（B 信号）；提取项目名、省、阶段词（إطلاق/افتتاح/تدشين=运营声明，مذكرة تفاهم=MoU/planned，مناقصة=招标）。
- **PTC/YemenNet**：萨那核心交换与互联网平台设施；A 仅当官方 PTC/YemenNet/Saba/CSO 来源具名设施/服务；CSO 统计年鉴的交换中心/节点/订户数据对统计为 A、对 DC 推断为 C。
- **TeleYemen**：网关/托管/分支事实为 A；海缆登陆事实与 TeleGeography/AAE-1 联合时为 B/A；`capacity_mw` 在官方给出 MW/kVA 前保持 null。
- **AdenNet**：网络级证据为 A（RIPE/ASN/服务页），物理数据中心为 B 线索。
- **NIC/CSO**：NIC 是国家数据托管机构（角色 A，物理设施 B/C）；CSO 是唯一系统性官方基础设施统计来源。
- **采购/捐助者**：UNGM（如 UNGM Notice 228625：OSESGY/UNMHA 在亚丁的 4G 数据服务采购，A 采购证据）、世行 2017 ICT 政策说明与 2023 宽带冗余研究、yemenhr.com（C 除非打开原始文件）。
- **海缆**：登陆站是小型关键设施（B/A 存在、状态需日期）；不把登陆站当商业 DC。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商核心**：Yemen Mobile（国有 CDMA/3G/4G，2019 约 40% 份额，核心萨那，B）、Sabafon（萨那 HQ，Al-Ahmar Group + Batelco，B）、YOU（原 MTN Yemen，Emerald Int'l，MTN 退出，B/C）、Y Telecom（2020 破产、亚丁 4G 重启，C）；均无公开容量规格。
- **银行**：央行亚丁 vs 萨那双份；商业银行/小额信贷（如 National Microfinance Foundation）= 小型服务器机房 C；核心银行/DR 为机构性质 B/C。
- **大学/油气**：大学 IT 中心为机构计算（仅当页面具名 DC/服务器机房时计数）；炼油厂/油田（Marib、Shabwah、Hadhramaut、亚丁）服务器机房为工业计算 C。
- **小托管商**：YemenHosting（萨那 Driving Street）、Sakhr Net = C，确认物理服务器位置后才建记录；Yemen Computer Company（YCC）提供 DC 设计/建设服务 = B/C 集成商线索，不是运营中的 DC。
- **目录纪律**：Inflect 列 "Yemen Net Al Hudaydah" 带功率/冷却声明 = C，需 PTC/YemenNet/Saba/CSO 佐证；升级流程 = 精确名称 → 运营商官方域 → 双 MTIT/Saba/NIC/CSO/UNGM → 无主源保持 C。
- **状态词**：تدشين/افتتاح/إطلاق/inaugurated = 运营声明；مذكرة تفاهم/MoU = planned；مناقصة/tender = 采购；دمار/destroyed = 损坏（对 FALCON 荷台达、AAE-1 亚丁用带日期的证据记录 current status）。

## 来源分级

- **A** = 针对所主张事实的官方/主要来源：MTIT（亚丁或萨那）页面/声明、PTC/YemenNet 官方或 Saba 转引声明、TeleYemen 官方页、AdenNet 官方/RIPE 注册、NIC 页面、CSO 出版物、Saba 官方通讯社（两变体）、UN/世行项目文件、ITU 官方记录、运营商官方设施页、官方云区域页、Uptime 认证记录。
- **B** = 强二级：Sana'a Center 研究、Yemen Monitor/Barran Press/Aden Times（引述官员）、DCD/Capacity Media/Developing Telecoms/Telecompaper/TeleGeography、BuddeComm/市场报告、具名客户与站点的厂商案例、世行/UNDP 国家简报。
- **C** = 弱线索：DataCenterMap/datacenters.com/Cloudscene/Baxtel/Inflect/仅 PeeringDB、维基、社交帖子、招标聚合器（yemenhr.com 除非原始文件）、不可访问片段、仅目录地址、不指明物理服务器位置的泛托管营销。
- 状态语义与控制方标注为必填；`capacity_mw` 仅当来源对精确设施给出 MW/IT 负载；kW/kVA/发电机/太阳能/平方米进 notes。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 YE 记录与种子（PTC/YemenNet DATA CENTER 托管、TeleYemen 网关/托管、AdenNet 核心、NIC、央行核心系统、UN 采购）。
2. 逐区四遍法：①国有运营商 ②政府/采购（双 Saba、UNGM、世行、大学招标）③海缆/连通性（Aden、Al Ghaydah、Al Hudaydah 登陆站，陆路）④能源/背景（PEC 电网现实、现场柴油/太阳能）。
3. 每条记录标注控制方（IRG/亚丁 vs Ansar Allah/萨那）；状态敏感的省（前线/重轰炸）要求带日期的新鲜证据。
4. 输出 schema：`{country_code: YE, country_name: Yemen, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`（notes 必含控制方）；阴性区在完成四遍法后写 `no_projects: true`。
5. 每次批次复查：超大规模区域阴性对照、海缆状态、双政权部委页面、活跃冲突省状态声明。不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] FALCON Al Ghaydah 登陆站：用带日期来源记录当前状态。
- [ ] FALCON Al Hudaydah 与 AAE-1 Aden：获取 2024-2026 修复/中断新鲜状态证据。
- [ ] AdenNet 物理数据中心：寻找官方设施页或采购文件以升级 B 线索。
- [ ] PTC/YemenNet 托管：寻找街道地址/机架/电力的一手披露。
- [ ] PM Bin Brik 亚丁电信现代化计划（2025-06-22）：追踪后续 DC/基础设施项目。
- [ ] NIC（双份）与央行核心银行系统：寻找设施级证据，标注控制方。
- [ ] 云区域阴性对照与红海海缆事件：每次运行复查。
