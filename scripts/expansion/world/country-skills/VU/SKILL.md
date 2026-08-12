---
name: vu-datacenter-methodology
location: scripts/expansion/world/country-skills/VU/SKILL.md
description: 瓦努阿图数据中心查询方法论：6 省模型，Shefa 维拉港 VGDC 政府数据中心为唯一设施级确认，商业 colo 未证实，海缆/IXP/连接性资产不自动升级。Vanuatu datacenter methodology: 6-province model, Port Vila VGDC government DC the only facility-level confirmation, commercial colo unconfirmed, cable/IXP/connectivity assets not auto-promoted.
---

# VU · 瓦努阿图数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：合并 explorer-official.md 与 explorer-industry.md 双线方法论，指导对瓦努阿图（Vanuatu, VU）数据中心候选的发现、分级、归属与误报排除。官方线覆盖 DCDT/PMO、TRBR、政府门户/MIPU/采购、海缆互联（ICN1/Tamtam/VIX）、电力（URA/UNELCO/VUI）、规划与环境、官方云区域负向；行业线覆盖运营商/厂商扫描、目录负控、三语查询与各省枚举矩阵。核心事实以双语标注，所有条目按可靠性分级并保留来源状态动词。

## 入口

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | DCDT/PMO（VGDC/VIX/Cloud Pilot）、TRBR 牌照/UAP/RIO、gov.vu/MIPU/DOFT/ADB、ICN1/Tamtam/VIX、URA/UNELCO/VUI/DOE、规划/环评/注册、官方云区域负向 |
| explorer-industry.md | 行业/厂商/媒体发现 | VGDC/VIX 判定、TVL/Vodafone、Digicel、Telsat/WanTok/Canopy、Interchange/ICN1/Tamtam、企业/公共部门机房线索、媒体/目录负控、三语查询、各省枚举矩阵 |

## 核心结构事实

1. **行政区划模型**：全国 6 省（provinces）：**Malampa、Penama、Sanma、Shefa、Tafea、Torba**（已按 world-manifest.jsonl 核对）；地名归一化：Efate/Efate Island、Port Vila/Vila、Espiritu Santo/Santo、Luganville、Malekula/Lakatoro、Tanna/Lenakel/Isangel、Ambae/Saratamata、Vanua Lava/Sola。
2. **注册库现状**：未发现瓦努阿图有公开的数据中心登记册或数据中心专属牌照类别；设施枚举必须交叉使用 DCDT/PMO、TRBR、采购、海缆、电力和媒体来源。官方已确认的设施级信号集中在 **Shefa 省 / 维拉港（Port Vila, Efate）**：DCDT 的 `Vanuatu Government Data Center` 官方资料、PMO 关于 Tamtam submarine cable / data centres / government broadband network 的 COM 公告、以及 DCDT 页面说明 Vanuatu Internet Exchange (VIX) housed at the Vanuatu Government Data Centre in Port Vila。
3. **法律与监管**：TRBR（`trbr.vu`）为电信监管机构，牌照/RIO/年度报告/Universal Access Policy（UAP 点名 Telecom Vanuatu Ltd、Telsat Broadband Ltd、Digicel Vanuatu Ltd）是运营商存在与监管状态的 A 级证据但不是数据中心证据；先列电信/ISP 参与者，再回 DCDT、运营商官方页、采购和媒体核实 data centre / colocation / server room / gateway facility。规划/建筑/环评：Port Vila / Luganville 市政在线许可检索未发现，用 `site:gov.vu`、市政公告和媒体兜底；DEPC/环境走 `environment.gov.vu`、`gov.vu`、ADB/World Bank E&S 文件；VFSC、investvanuatu.vu 作法人/投资背景。
4. **互联与云**：官方连接性资产包括 ICN1 维拉港国际海缆（2014 完成，Port Vila–Suva, Fiji，接入 Southern Cross）、VIX、Tamtam 第二国际海缆项目（ADB 项目 `59142-005`，连接 Lifou, New Caledonia 与 Vanuatu，提升 Santo/Malekula/Efate/Tanna 连接）；海缆登陆站、IXP、NOC、交换机房默认不是商业数据中心，只有来源明确点名 data centre / colocation / racks / hosting facility 才升级；AWS/Azure/Google Cloud/Oracle OCI 官方区域清单未列 VU，不将 VPS、Starlink、Kacific/SES/O3b、云转售或托管广告提升为本地设施。
5. **设施/项目种子**：Vanuatu Government Data Centre, Port Vila（Shefa）——官方确认存在，DCDT 列 VGDC brochure（`/images/brochures/VGDC.pdf`），DCDT VIX 页说明 VIX housed at VGDC，PMO 2025-11-26 COM 指示 complete implementation，A 级，登记为 `government_dc`（地址细节、机架数、冗余站点用 VGDC PDF/采购/后续公告复核，不登记为商业 colo）；Data Centres / Cloud Pilot Project（State property，地点未披露，行政上优先查 Shefa，登记 `government_dc_project`，未披露地点不可分配到 Santo 或其他省份）；VIX at VGDC（Shefa，`ixp_inside_government_dc` / `colo_adjacent_interconnection` 属性，VIX 本身非商业 DC）；ICN1 Port Vila landing/cable station（Shefa，`telecom_cable_station` 非 DC，有 RIO/设备接入证据可加 `colo_adjacent_telecom`）；Tamtam 节点/登陆点（Sanma/Malampa/Shefa/Tafea，`telecom_cable_station_project` / `connectivity_project` 非 DC）；TVL/Vodafone、Digicel、Telsat/WanTok 网络设施（Shefa 为主、Luganville/Santo 可能有网络节点，牌照/存在 A，设施推断 C/B，`telecom_core_lead` 不得无证升级为 DC）。
6. **语言与词汇**：英语优先，辅以法语与 Bislama；术语双拼：`data center` / `data centre` / `datacenter`、`colo` / `colocation` / `co-location`、`hosting` / `hébergement`、`server` / `serveur`、`cable station` / `station d'atterrissement` / `stesen kabel`；状态词：`proposed`、`planned`、`procurement`、`implementation`、`under_construction`、`operational`、`discontinued`、`false_positive`；没有状态证据时不写运营中。
7. **可靠性分级**：A=政府、监管机构、国企/法定机构、公用事业监管、官方公司页、官方云区域页、立法文本、多边机构项目文件；B=具名来源与日期的可靠本地/区域/行业媒体、承包商案例、运营商访谈、多边项目页面；C=目录站、海缆追踪器、PeeringDB/ASN 聚合、社交页面、SEO/转售页面、无出处聚合，C 级仅作线索或负控，不得用于确立设施。
8. **计数与去重规则**：`government_dc` 必须有 DCDT/PMO/采购/项目文件点名政府数据中心和地点或清楚归属；`commercial_colo` 必须有运营商官方产品页、合同、资费或设施页明示在瓦努阿图提供 colocation、rack、data centre hosting、disaster recovery site；`telecom_cable_station` 海缆登陆站/节点可登记为电信设施但非 DC；`connectivity_only` 覆盖 Starlink、Kacific、SES/O3b、移动塔、VSAT、Wi-Fi、学校 ICT、社区互联网、海缆覆盖；`false_positive` 指泛 SEO 的 “Port Vila data center services / VPS / dedicated server” 页（无本地设施、运营商、地址或监管锚点）；邻居国 Fiji Suva、New Caledonia Lifou/Noumea、Solomon Honiara 的海缆/运营商名称易混淆，仅统计瓦努阿图境内站点；电力资产（UNELCO/VUI 柴油、水电、太阳能、风电、BESS、变电站）是可行性背景不是数据中心；任何 MW 级数据中心在瓦努阿图小电网中都必须有电力证据（UNELCO/VUI/URA/DOE）。

## 常用查询模板

```text
site:dcdt.gov.vu ("Government Data Center" OR "Government Data Centre" OR VGDC OR "data centre" OR "data center" OR VIX)
site:digital.gov.vu ("Government Data Center" OR "Government Data Centre" OR VIX OR "Data Centre" OR "Port Vila")
site:pmo.gov.vu ("data centre" OR "data centres" OR "data center" OR Tamtam OR "Cloud Pilot" OR "Government Broadband Network")
"Vanuatu Government Data Centre" OR "Vanuatu Government Data Center" "Port Vila"
"Vanuatu Internet Exchange" "Government Data Centre" "Port Vila"
site:trbr.vu ("data center" OR "data centre" OR datacenter OR "server room" OR IXP OR hosting OR colocation OR gateway)
site:trbr.vu (licensee OR licence OR license OR "public register") (TVL OR Vodafone OR Digicel OR Telsat OR WanTok OR Interchange)
site:trbr.vu RIO OR "Reference Interconnection Offer" OR interconnection OR gateway
site:trbr.vu "annual report" OR "telecommunications sector report"
site:trbr.vu "Universal Access Policy" (Tanna OR Malekula OR Santo OR Maewo OR Ambae OR Torres OR Efate)
site:gov.vu ("data centre" OR "data center" OR "Government Data Centre" OR "Cloud Pilot" OR "Digital Transformation")
site:pmo.gov.vu (Tamtam OR "submarine cable" OR "data centre" OR "government broadband")
site:doft.gov.vu (tender OR procurement OR contract OR budget) ("data centre" OR ICT OR server OR Tamtam OR broadband)
site:mipu.gov.vu (telecommunications OR broadband OR "submarine cable" OR Tamtam OR ICT)
site:adb.org Vanuatu 59142-005 OR Tamtam OR "submarine cable"
site:interchange.vu (ICN1 OR ICN2 OR ICN3 OR "Port Vila" OR Suva OR Santo OR Tanna OR "Subsea Cables")
"ICN1" "Port Vila" "Suva" "Interchange"
site:pmo.gov.vu Tamtam "data centre" "government broadband"
site:adb.org "Tamtam Submarine Cable Project" "59142-005"
"Vanuatu Internet Exchange" OR VIX "Government Data Centre" "Port Vila"
site:ura.gov.vu UNELCO "Port Vila" electricity concession
site:ura.gov.vu VUI Santo Luganville electricity
site:doe.gov.vu (UNELCO OR VUI OR electricity OR "large customer" OR substation) ("data centre" OR "data center" OR ICT OR server)
"Vanuatu" ("data centre" OR "data center" OR "large load" OR MW) (UNELCO OR VUI OR electricity OR grid)
"Port Vila" "building permit" ("data centre" OR "data center" OR telecommunications OR server)
"Luganville" "building permit" ("data centre" OR "data center" OR telecommunications OR server)
"Vanuatu" DEPC OR EIA ("data centre" OR "data center" OR telecommunications OR "submarine cable")
site:vfsc.vu ("Telecom Vanuatu" OR Digicel OR Telsat OR WanTok OR Interchange OR "data centre")
site:investvanuatu.vu (telecommunications OR ICT OR "data centre" OR "data center" OR Interchange)
"Vanuatu" ("AWS Region" OR "AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "OCI region")
"Vanuatu" ("cloud region" OR hyperscale OR "data residency" OR "sovereign cloud")
"{Province}" Vanuatu ("data center" OR "data centre" OR datacenter OR colocation OR "server room" OR "Government Data Centre" OR "cable station" OR "landing station" OR ICT)
site:dcdt.gov.vu "{Province}" ("data centre" OR "data center" OR VIX OR broadband OR Tamtam)
site:pmo.gov.vu "{Province}" (Tamtam OR "data centre" OR "data center" OR broadband OR digital)
site:trbr.vu "{Province}" (telecommunications OR internet OR broadband OR cable OR "Universal Access")
site:ura.gov.vu "{Province}" (UNELCO OR VUI OR electricity OR concession)
"Vanuatu" ("data center" OR "data centre" OR datacenter OR colocation OR "co-location" OR "server hosting" OR "managed hosting") -proxy -VPS
"Port Vila" ("data center" OR "data centre" OR server OR hosting OR colocation OR "landing station" OR "cable station" OR VIX)
"Luganville" OR "Santo" ("landing station" OR "cable station" OR server OR internet OR telecom OR fibre OR fiber)
"Vanuatu Government Data Centre" OR "Vanuatu Government Data Center"
"Vanuatu" "Tamtam" "data centre" OR "government broadband"
site:dailypost.vu ("data centre" OR "data center" OR internet OR broadband OR cable OR Starlink OR digital OR telecom)
site:datacenterdynamics.com Vanuatu OR "Port Vila"
site:datacentermap.com Vanuatu OR "Port Vila"
site:cloudscene.com Vanuatu OR "Port Vila"
site:connectbase.com "Vanuatu Government Datacenter"
site:inflect.com "Vanuatu Government Datacenter"
site:vodafone.com.vu (hosting OR server OR cloud OR enterprise OR business OR NOC OR switch OR gateway OR "data centre" OR "data center")
"Telecom Vanuatu" OR "Vodafone Vanuatu" ("Port Vila" OR Tagabe OR Erakor OR Nambatu) (gateway OR switch OR NOC OR server OR hosting OR "data centre" OR "data center")
site:digicelpacific.com/mobile/vu (enterprise OR business OR network OR cloud OR hosting OR "data centre" OR "data center")
"Digicel Vanuatu" ("data center" OR "data centre" OR NOC OR switch OR hosting OR cloud OR server OR gateway)
"Digicel Vanuatu" "Ellouk Plateau" "Port-Vila"
"Telsat Broadband" Vanuatu ("Port Vila" OR office OR head-end OR server OR NOC OR "data centre" OR "data center")
site:wantok.to Telsat Vanuatu acquisition colocation hosting
"WanTok" Vanuatu (server OR hosting OR NOC OR network OR Digicel OR acquisition OR colocation)
"Canopy" Vanuatu (fiber OR fibre OR broadband OR server OR NOC OR "Port Vila" OR Luganville)
site:interchange.vu (ICN1 OR ICN2 OR ICN3 OR cable OR capacity OR "Port Vila" OR Suva OR Santo OR Tanna)
"ICN1" Vanuatu ("Port Vila" OR Suva OR capacity OR outage OR upgrade OR landing)
"Tamtam Submarine Cable" Vanuatu (Santo OR Malekula OR Efate OR Tanna OR Lifou OR Prima OR ADB)
"Reserve Bank of Vanuatu" OR RBV ("data centre" OR "data center" OR "disaster recovery" OR server OR IT)
"National Bank of Vanuatu" OR "ANZ Vanuatu" OR "BSP Vanuatu" ("data centre" OR "data center" OR "disaster recovery" OR server)
"USP Emalus" OR "University of the South Pacific" Vanuatu (server OR "data centre" OR network OR hosting)
"Airports Vanuatu" OR AVL (server OR ICT OR "data centre" OR "data center" OR network)
"Vanuatu" (ministry OR government OR department) ("server room" OR "data centre" OR "data center" OR "disaster recovery")
"{Province}" Vanuatu ("centre de données" OR "salle de serveurs" OR hébergement OR colocation OR "station d'atterrissement" OR opérateur OR fibre OR FAI)
"{Province}" Vanuatu ("stesen kabel" OR "kompani blong internet" OR "serbis blong internet" OR server OR internet OR letrik OR telikom)
"Vanuatu" ("AWS region" OR "AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "OCI region")
"Vanuatu" ("cloud region" OR hyperscale OR "public cloud" OR "sovereign cloud" OR "data residency")
```

## 官方/监管管线要点（详见 explorer-official.md）

- DCDT/PMO 是政府数据中心的 A 级锚点：DCDT `dcdt.gov.vu` + 镜像 `digital.gov.vu`，brochures 页列出 `Vanuatu Government Data Center`（VGDC.pdf）与 `Vanuatu Internet Exchange Point`（VIX.pdf）；DCDT events 页说明 VIX 于 2012 年由政府与五家网络运营商 MOU 建立，housed at VGDC in Port Vila；PMO COM 公告（2025-11-26）提及 Tamtam cable、new data centres、government broadband network，指示 DCDT complete implementation of the VGDC project（Australian Government support），并说明 Data Centres and Cloud Pilot Project remain State property。`Vanuatu Government Data Centre, Port Vila` 可登记为 `government_dc` / `operational_or_implementation`，但机架数、冗余站点、精确地址和状态细节需从 VGDC PDF、采购文件或后续官方公告复核。
- TRBR 用法：牌照、RIO、年度报告是运营商存在和监管状态的 A 级证据但不是数据中心证据；先列出电信/ISP 参与者再回 DCDT、运营商官方页、采购和媒体核实是否有 data centre / colocation / server room / gateway facility。
- 政府门户/MIPU/采购/多边：政府数据中心建设、云试点、Tamtam、政府宽带网、采购和预算以 PMO/DCDT/DOFT/ADB 为 A 级；ADB 项目 `59142-005` 证实 Tamtam 是第二国际海缆项目，节点/登陆站可作 `telecom_cable_station_project` 但不等于数据中心；采购、合同授予、EIA 和预算可验证状态（planned / procurement / under_construction / operational），没有状态证据时不写运营中。
- 海缆、登陆站与互联：ICN1（2014 完成，Port Vila–Suva，接入 Southern Cross，Interchange 官方页）为 `telecom_cable_station`（Shefa），若仅来源海缆图/追踪器则降为 C；Tamtam 节点覆盖 Santo/Sanma、Malekula/Malampa、Efate/Shefa、Tanna/Tafea，为 `connectivity_project` 不记为 DC；VIX 为 `ixp_inside_government_dc`，只支撑 Port Vila 政府 DC 和互联属性。
- 电力、公用事业与大负荷约束：URA（`ura.gov.vu`）验证 UNELCO 继续运营 Port Vila electricity concession 至 2031-12-31、VUI 自 2010 年起为 Santo electricity service provider；DOE（`doe.gov.vu`）涉及 VUI/UNELCO/能源项目；任何 MW 级数据中心在瓦努阿图小电网中都必须有电力证据，没有 UNELCO/VUI/URA/DOE 证据的 MW、hyperscale、AI DC 主张按 C 级或误报处理。
- 规划、建筑、环评、公司注册：Port Vila / Luganville 市政在线许可检索未发现，用 `site:gov.vu`、市政公告和媒体兜底；DEPC/环境走 `environment.gov.vu`、`gov.vu`、ADB/World Bank E&S 文件；VFSC（`vfsc.vu`）、VIPA/投资（`investvanuatu.vu`）作背景，法律存在不等于设施存在；VNSO（`vnso.gov.vu`）仅作统计背景。
- 官方云区域缺失检查：仅使用官方页面做 A 级存在/缺失判断；AWS/Azure/Google Cloud/OCI 官方区域清单未列 VU。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 已验证行业基线：未发现瓦努阿图存在公开销售的中性机柜托管（neutral rack colocation）或超大规模商业数据中心市场；已确认的数据中心信号是政府数据中心（VGDC）in Port Vila, Shefa，不是商业 colo；行业设施/连接性集中在 Port Vila / Shefa；Santo/Sanma、Malekula/Malampa、Tanna/Tafea 有 Tamtam cable 覆盖/节点信号但不是 DC 证据；Starlink、Kacific/SES/O3b、移动塔、Wi-Fi、宽带覆盖、海缆登陆站、IXP、NOC 和运营商总部均为连接性或电信资产。
- 运营商、设施与厂商扫描：VGDC/VIX（登记 `government_dc` + `ixp_inside_government_dc` 属性，未披露地点的 “data centres” 保持 `government_dc_project` 不得自动分配到 Sanma）；TVL/Vodafone（`vodafone.com.vu`，A 官方存在/B-C 设施推断，消费级网页、SIM、宽带和 webmail 不足为 DC 证据）；Digicel（`digicelpacific.com/mobile/vu`，Corporate Address: Ellouk Plateau, PMB 9103, Port-Vila，核心网络设施存在为合理电信推断但设施级证据仍需官方/监管/采购/媒体点名）；Telsat/WanTok/Canopy（默认 `isp_or_connectivity_lead`，WanTok 2020-07-10 press 称收购 Telsat Broadband，站点出现 ICT/Networking/Website Hosting/Colocation 菜单词但站点主体是 WanTok Tonga/Pacific，不能据此证明 Vanuatu colo facility，只有点名 Vanuatu site/address/racks 才升级；Canopy 需官方域、TRBR 或本地媒体重新锚定）；Interchange/ICN1/Tamtam（海缆、登陆站和 IXP 可支撑互联/延迟/冗余背景但不自动构成商业 DC）；企业/公共部门服务器房线索（Reserve Bank of Vanuatu、ANZ/BSP/NBV/BRED、财政/海关/统计/移民、Vanuatu Airports、USP Emalus、National University、医院、酒店/航空/港口系统——通常内部机房或云消费者，仅当来源点名物理设施、地点和功能时计入，否则标 `enterprise_server_room_lead` 或忽略）。
- 行业媒体、目录与负控：高价值媒体/目录——Vanuatu Daily Post、VBTC、RNZ Pacific、Islands Business、Data Center Dynamics（Cloudflare 可能挡直接抓取，可用搜索片段和二次来源但最终字段回锚 DCDT/PMO）、Submarine Networks / submarinecablemap 仅作海缆 B/C 线索、Inflect/Connectbase/Datacenters.com/DataCenterMap/Cloudscene 仅作 C 级目录线索；目录点名 `Vanuatu Government Datacenter`、`No2 Area`、`Port Vila`、`VIX` 等回 DCDT/PMO/VGDC PDF 核实，目录字段保持 C；`data center consulting in Port Vila / dedicated server / VPS / edge location` 无本地运营商、地址、设施页或监管锚点 → `discarded_reseller_or_directory_lead`；DataCenterMap/Cloudscene 无条目是弱负信号，不证明无政府或企业服务器房。
- 三语查询与各省枚举矩阵：通用清扫 EN/FR/BI 三语模板；Shefa 可登记 VGDC 为 `government_dc`、ICN1 为 `telecom_cable_station`，其余运营商设施不无证升级；Sanma（Santo/Luganville Tamtam 节点、运营商覆盖、VUI 电力）Tamtam 是连接项目，无 data centre 词和地点证据则不计 DC；Malampa/Tafea 仅 `connectivity_project` 或 `no_projects`；Penama/Torba 灾后/教育 ICT 不是 DC，无命名设施则 `no_projects`。
- 捕获字段：`name`、`operator_or_owner`、`province`、`town_or_site`、`coordinates_or_address`、`source_url`、`source_date`、`source_grade`（A|B|C）、`facility_type`（commercial_colo / government_dc / government_dc_project / ixp_inside_government_dc / telecom_cable_station / telecom_core / enterprise_server_room / tower_edge / connectivity_only / false_positive）、`status`（proposed / planned / procurement / implementation / under_construction / operational / discontinued / false_positive）、`basis_for_status`、`capacity_or_power_claim`、`power_evidence`、`license_or_registry_anchor`、`notes`。升级规则：`commercial_colo` 仅当存在运营商页面、资费/产品页、设施页或合同明示在瓦努阿图提供 colocation/机架/数据中心服务；`government_dc` 仅当 DCDT/PMO/采购/多边文件点名政府数据中心和地点（VGDC Port Vila 已满足）；海缆站保持 `telecom_cable_station`；IXP 保持 `ixp_inside_government_dc` 或 `interconnection`；Starlink、铁塔、Wi-Fi、VSAT、宽带覆盖、Tamtam 覆盖、省级 UAP rollout 保持 `connectivity_only`。
- 陷阱：SEO 托管页常推销 “Vanuatu VPS / Port Vila dedicated server / data center consulting”，无实体设施按 C 级忽略；WanTok/Telsat/Canopy 的 hosting/ICT/networking 或 colocation 字样可能是跨国服务或营销菜单，必须要求 Vanuatu 物理站点证据；运营商总部在维拉港不等于数据中心，设施/功能核验前使用 `telecom_core_lead`；海缆站、VIX、网关可以与数据中心同址但不能相互替代，分类应保留设施功能差异；邻居国站点名易混淆，仅统计瓦努阿图境内站点；电力资产是可行性背景不是数据中心。

## 维护注意（更新纪律）

- 再次运行时先重跑 DCDT VGDC/VIX、PMO COM/Tamtam、TRBR license/UAP/RIO、Interchange/ADB Tamtam、URA/DOE power、运营商官方页、本地媒体和官方云区域清单，再变更瓦努阿图设施状态。
- 状态动词驱动：任何 `commissioned`、`RFS`、`ready for service`、`awarded`、`installed`、`accepted` 字样触发重新分级；VGDC 的机架数/冗余站点/精确地址出现官方披露时立即补录并升为 A 级字段。
- 电力与建设证据联动：MW 级/AI/hyperscale 主张必须能回锚 UNELCO/VUI/URA/DOE 或 EIA 文件，否则保持 C 或 false_positive。
