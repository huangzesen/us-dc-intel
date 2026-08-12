---
name: nf-datacenter-methodology
location: scripts/expansion/world/country-skills/NF/SKILL.md
description: 诺福克岛数据中心双线查询方法论（官方/监管/电信/电力/采购 + 行业/媒体/目录/误报核验），no-market 领地，预期零商业数据中心；Norfolk Island datacenter dual-line discovery methodology (official/regulatory/telecom/power/procurement + industry/media/directory/false-positive checks), a no-market territory with expected zero commercial datacenters. 运行 NF 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# NF · 诺福克岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为诺福克岛（Norfolk Island, NF）数据中心枚举批次提供官方与行业双线方法，识别运营中、在建、拟建以及误报（false-positive）的数据中心候选对象。官方线（explorer-official.md）覆盖澳大利亚联邦政府、Norfolk Island Regional Council（NIRC）、监管机构、公用事业、运营商官方页、IANA/注册处、官方云厂商区域页与政府采购门户；行业线（explorer-industry.md）覆盖运营商/供应商扫描、海缆/卫星/电信线索、行业媒体与二级来源、目录到一级核验工作流、地点检索配方与容量提取指引。本领地当前结论：无经核实的商业数据中心市场。

## 入口

| 文件 | 职责 | 内容概要 |
|---|---|---|
| explorer-official.md | 官方/监管/电信/电力/采购 | 澳大利亚联邦（DITRDCSA 领地页/Administrator/legislation.gov.au/ABS）、NIRC（Norfolk Telecom、satellite backhaul、Tenders and EOI、Planning、Electricity）、采购与登记（AusTender、Digital Marketplace、ABN Lookup、ASIC）、电信监管与编号（ACMA、DITRDCSA carrier rules、IANA `.nf`）、Norfolk Telecom/NIRC Telecom、电力/公用事业/大型负载、官方云区域缺失检查（AWS/Azure/GCP/OCI） |
| explorer-industry.md | 行业/媒体/目录/误报核验 | 运营商与供应商扫描（Norfolk Telecom、NIRC backhaul/Telstra、O3b/SES、NIDS `.nf` registry、ACMA/DITRDCSA 框架、区域运营商背景）、海缆/卫星/电信线索、行业媒体（ABC、RNZ Pacific、DCD、CommsDay、ITNews/ARN/CRN、Submarine Networks、SubTel Forum、Islands Business、NIRC newsletters）、目录到一级核验工作流、地点检索配方、容量提取指引、枚举矩阵与分级规则 |

## 核心结构事实

1. **Division 模型**：manifest 已核验 `country_code:"NF"`、`country_name:"Norfolk Island"`、`subnational_type:"country"`、`divisions:["Norfolk Island"]`。NF 是单一分区，division = Norfolk Island；全领地覆盖，地点粒度（Burnt Pine、Kingston、Cascade、Anson Bay 等）仅用于发现 telecom/electricity/government 线索。
2. **国家基线**：诺福克岛是澳大利亚外部领地（external Australian territory），位于悉尼东北约 1,600 km，ABS 2021 人口 2,188（DITRDCSA 官方领地页确认）；当前治理结构以澳大利亚联邦领地管理 + NIRC 地方服务为核心，Administrator 代表澳大利亚政府并执行相关法定职能（2026-06-01 起为 Fiona McKergow）；NIRC 当前官方域名是 nirc.gov.au（页脚仍用 customercare@nirc.gov.nf、电话 +6723 22001），Council 办公地址 Bicentennial Complex, 39 Taylors Rd, Burnt Pine。
3. **当前结论（2026-08-12）**：未发现经核实的商业数据中心市场——无第三方托管/colo、超大规模云区域、本地公共云区域、IXP 或设施级数据中心公告。NF 的真实数字基础设施锚点是 NIRC/Norfolk Telecom 电信网络、卫星 backhaul、历史/当前卫星地球站、NIRC 电力系统与本地政府/企业 IT 机房。行业图景：no-market / pre-commercial datacenter territory。
4. **重要纠偏：不要把 Gondwana-1 计作诺福克岛登陆**：已核验的 Gondwana-1 资料显示该系统连接 New Caledonia 与 Australia，RFS 2008，主要登陆点为 Nouméa/Sydney 等；未发现 A 级或可靠 B 级来源证明 Gondwana-1 在 Norfolk Island 设有分支或登陆站；Submarine Networks 页面只可作区域背景。凡把 `Gondwana-1 + Norfolk Island` 写成登陆设施的结果，标为 `false_positive_or_regional_background`，除非找到 NIRC/NTL/OPT/ASN 一手文件。
5. **电信连接**：官方 NIRC 2026-04-02 新闻明确说明 Norfolk Telecom 仍有 Telstra satellite backhaul 服务：2022 年 DITRDCSA 支持两年 `A$7.35 million` 资金提升卫星连接，NIRC 2023 年经 tender 将 satellite backhaul 合同授予 Telstra，初始合同延续至 2026-01；该页是当前最强的 A 级电信连接证据；2015 年联邦委托的 Norfolk Island Mobile Network Review 记录 Norfolk Telecom 运营岛上固定/移动基础设施、负责国际/互联网连接，当时国际连接为 O3b IP satellite + C8 backup satellite，并记录 PSTN/ADSL/GSM core、base station shelters、Norfolk Telecom office 可容纳 core network equipment 等事实。
6. **电力约束**：NIRC 电力页面确认 Norfolk Island electricity services 包括 Power house（含 mechanical workshop）与 reticulation；电力系统很小，历史上柴油发电为主，近年有 rooftop solar、battery、BESY energy platform 与 tariff review；对 NF，任何数百 kW 或 MW 级数据中心声称都应首先出现电力接入、发电、配电、planning 或 Council meeting 证据；没有电力/规划证据时，应判为误报或未核实线索。
7. **`.nf` ccTLD**：IANA 记录显示 manager 为 Norfolk Island Data Services（NIDS），地址在 Norfolk Island；这是域名/注册服务存在证据，不是本地数据中心证据；NIDS 同时提供 internet/VoIP/NBN/Sky Muster 类服务页面，但注册局/ISP 服务不得自动转化为本地 DC 设施。
8. **可靠性分级**：A = 一级/官方来源（澳大利亚联邦政府、NIRC、监管机构、公用事业、运营商官方页、IANA/注册处、官方云厂商区域页、政府采购门户、正式议会/委员会文件）；B = 可信本地/地区/行业媒体或承包商案例（要求具名当事方、日期、可回查的一手事实）；C = 目录站、市场平台、SEO 托管页、VPN/VPS 位置页、无法核实的营销页或无出处转载——C 级只能作线索或阴性对照，不能用于确立设施存在。
9. **计数与去重规则**：任何 candidate 若缺少以下至少三项中的两项，不能确立商业 DC：具名运营商、物理地点/地址、设施类型声明（data centre/colocation/racks/IT load）、运营状态、规划/电力证据；Norfolk Telecom/NIRC/Telstra satellite backhaul 可证明电信服务和 backhaul，不能自动证明 colocation 或 datacenter；NIDS 与 `.nf` 可证明 registry/ISP/VoIP/Internet service，不能自动证明本地 server hall；Gondwana-1、Sydney、Nouméa、Guam、Auckland、Australia/NZ cloud regions 是区域互联/后备市场背景，不得计入 NF inventory；历史 Pacific Cable Station、Anson Bay telegraph/cable heritage 是历史通信设施，除非来源指向现代运营 telecom site 否则只作历史背景；卫星 backhaul 是连接性不是数据中心容量，backhaul Mbps/Gbps 不得转成 DC MW；电力系统容量不得折算成 DC MW；云厂商在 Australia/NZ 的区域只作 off-island background；目录、SEO、VPN/VPS 结果无论页面说法多明确，未通过 operator/government/planning/electricity 复核前均不得入库存；分类模型：`commercial_datacenter` / `government_server_room` / `telecom_exchange_or_core` / `satellite_earth_station_or_backhaul` / `power_house_or_utility` / `domain_registry_or_isp` / `seo_false_positive`；运营状态至少需要一个 A 级来源；仅 C 级或 SEO 来源时只能为 `false_positive` 或 `unverified_lead`；容量只在来源明确给出 IT load、rack count、building area、UPS/generator capacity 或 telecom bandwidth 时记录，不得把卫星 backhaul 带宽、电力系统容量或云厂商区域背景折算为 `capacity_mw`。

## 常用查询模板

```text
site:infrastructure.gov.au/territories-regions/territories/norfolk-island ("data centre" OR "data center" OR datacenter OR ICT OR "server room" OR cloud)
site:infrastructure.gov.au/territories-regions/territories/norfolk-island ("telecommunications" OR "satellite backhaul" OR "Norfolk Telecom" OR broadband OR "mobile network")
site:infrastructure.gov.au "Norfolk Island" ("grant" OR funding OR tender OR contract) ("telecommunications" OR ICT OR "satellite backhaul" OR electricity)
site:legislation.gov.au "Norfolk Island" ("telecommunications" OR "carrier licence" OR "electricity" OR planning OR procurement)
site:nirc.gov.au ("data centre" OR "data center" OR datacenter OR "server room" OR "computer room" OR cloud OR "managed services")
site:nirc.gov.au ("Norfolk Telecom" OR telecom OR telecommunications OR "satellite backhaul" OR Telstra OR broadband OR "mobile network")
site:nirc.gov.au ("tender" OR "RFT" OR "RFQ" OR "ITT" OR procurement OR "managed services") ("ICT" OR IT OR telecom OR network OR cloud)
site:nirc.gov.au ("development application" OR planning OR "land use" OR "building approval") ("telecommunications" OR "data centre" OR "data center" OR electricity)
site:nirc.gov.au ("Power house" OR "power station" OR electricity OR diesel OR generator OR solar OR battery OR BESY)
site:tenders.gov.au "Norfolk Island" ("ICT" OR "information technology" OR telecommunications OR "satellite backhaul" OR "data centre" OR cloud)
site:digitalmarketplace.gov.au "Norfolk Island"
site:abr.business.gov.au "Norfolk Island" ("data" OR telecom OR hosting OR technology OR internet)
site:asic.gov.au "Norfolk Island" ("data centre" OR "data center" OR hosting OR telecommunications)
site:acma.gov.au "Norfolk Island" ("carrier licence" OR "carrier licensing" OR telecommunications OR radiocommunications OR numbering)
site:acma.gov.au "Norfolk Island" ("Norfolk Telecom" OR "Norfolk Island Regional Council" OR "broadcasting licence")
site:iana.org/domains/root/db/nf "Norfolk Island Data Services"
site:nirc.gov.au "Norfolk Telecom" ("data centre" OR "data center" OR datacenter OR "server room" OR "core network" OR switch OR NOC)
site:nirc.gov.au "Norfolk Telecom" ("satellite backhaul" OR Telstra OR O3b OR C8 OR "international connectivity" OR broadband)
site:ni.net.nf ("data centre" OR "data center" OR datacenter OR hosting OR "server room" OR business OR ADSL OR fibre OR fiber)
"Norfolk Telecom" "Burnt Pine" (office OR exchange OR switch OR "server room" OR "core network")
"Norfolk Island" "Mobile Network Review" "Norfolk Telecom" ("AXE" OR "core network" OR "satellite systems")
site:nirc.gov.au ("solar" OR battery OR BESY OR renewable OR "tariff review" OR "asset management plan")
"Norfolk Island" ("data centre" OR "data center" OR datacenter) (power OR electricity OR generator OR "large load")
site:aws.amazon.com "Norfolk Island" "AWS Region"
site:learn.microsoft.com "Norfolk Island" Azure region
site:cloud.google.com "Norfolk Island" "Google Cloud" region
site:docs.oracle.com "Norfolk Island" "OCI" region
"{locality}" "Norfolk Island" ("data centre" OR "data center" OR datacenter)
"{locality}" "Norfolk Island" ("server room" OR server OR hosting OR colocation OR "co-location" OR "managed services")
"{locality}" "Norfolk Island" ("Norfolk Telecom" OR telecom OR telecommunications OR broadband OR "satellite backhaul" OR "mobile network")
"{locality}" "Norfolk Island" (electricity OR "power station" OR "Power house" OR diesel OR generator OR solar OR battery)
"Burnt Pine" "Norfolk Island" ("Norfolk Telecom" OR office OR exchange OR switch OR "server room" OR "Power house")
"Kingston" "Norfolk Island" (government OR administration OR ICT OR server)
"Cascade" "Norfolk Island" (wharf OR port OR telecom OR cable OR "development application")
"Anson Bay" "Norfolk Island" ("Pacific Cable Station" OR cable OR telegraph)
"Norfolk Island" ("satellite backhaul" OR "Telstra" OR "O3b" OR "C8 satellite" OR "earth station")
"Norfolk Island" "Gondwana-1" OR "Gondwana 1" OR "cable landing station"
site:datacenterdynamics.com "Norfolk Island" OR "Norfolk Telecom"
site:abc.net.au/news "Norfolk Island" (O3b OR satellite OR "Norfolk Telecom" OR internet)
site:submarinenetworks.com "Norfolk Island" OR "Gondwana-1"
"Norfolk Island" ("data centre" OR "data center" OR datacenter) -Sydney -Auckland -Guam
"Norfolk Island" ("colocation" OR "co-location" OR "dedicated server" OR VPS OR "cloud server")
site:datacentermap.com "Norfolk Island"
site:baxtel.com "Norfolk Island"
"Burnt Pine" "data center" OR "data centre" OR hosting OR server OR VPS
".nf" (hosting OR "data center" OR "data centre" OR colocation OR VPS)
```

## 官方/监管/电信/电力/采购管线要点（详见 explorer-official.md）

- **澳大利亚联邦与领地行政**：DITRDCSA Norfolk Island 领地页（确认位置/人口/治理/联邦拨款/通信/ICT/能源项目与 Administrator 公告）、Administrator 页、media releases、legislation.gov.au（Norfolk Island 相关法律延伸、通信、电力、地方政府、规划与采购授权）、ABS（2021 Census/人口）。若出现政府数据中心/ICT 机房项目，必须能回到 DITRDCSA、NIRC、AusTender 或正式议会/委员会文件。
- **NIRC**：NIRC 是地方规划、招标、电力服务、Norfolk Telecom 运营信息和 Council IT 采购的一手来源；Tenders and EOI / Closed Opportunities 可直接发现 ICT managed services、telecom、electricity、generator、network、software 等采购（2026 年已出现 `ITT 7/2026 - Managed Services Provider for Information Technology`，这属于政府 IT 服务线索，不等于数据中心设施）；Planning and Development 用于查 development application、land use、large load 或 building works——NF 没有全国性可检索 DC 规划门户，需结合 NIRC 页面、会议 papers、media releases 与站内搜索。
- **澳大利亚采购与公司/登记体系**：AusTender（联邦资助或联邦部门采购）、Digital Marketplace/BuyICT、ABN Lookup、ASIC/ASIC Connect；任何声称在 NF 运营数据中心、hosting、ISP、managed cloud 的公司，需用 ABN/ASIC 核对实体状态和地址——注册地或邮政地址不等于设施所在地。
- **电信监管与编号**：ACMA、DITRDCSA carrier/service provider rules（澳大利亚 carrier 框架要求 carrier 对用于向公众提供通信服务的 network units 持有 ACMA carrier licence——证明监管门槛，不证明设施存在）、IANA `.nf` delegation；2015 Mobile Network Review 说明当时部分 Norfolk Island 频谱事项由 ACMA 管理，之后澳大利亚通信监管框架延伸到 NF 的细节需以当前 ACMA/DITRDCSA 文件复核。
- **Norfolk Telecom / NIRC Telecom**：NIRC Norfolk Telecom 页、2026 satellite backhaul 新闻、Norfolk Telecom 客户/服务页（当前/历史域名 ni.net.nf，如 ADSL）；2015 报告记录 PSTN 使用 copper/some fibre/Ericsson AXE switch、移动网络有 core/BSC/BTS、base station shelters、radio base station backhaul 多为 E1 部分 fibre、国际连接当时为 O3b IP satellite + C8 backup satellite；2026 NIRC 页面记录卫星 backhaul 由 Telstra 合同提供，合同/费用/服务等级正在重谈，Council 明确表示该问题不影响 internet 或 voice connectivity；这些证据支持 telecom_exchange/telecom_core/satellite_backhaul/network_facility 分类，除非来源明确提供 colocation、rack rental、commercial datacenter、facility address 和运营状态，否则不得记为商业 DC。
- **电力、公用事业与大型负载**：NIRC Electricity System、Electricity services、Electricity forms、tariff review 新闻与 asset management plan PDF；NIRC 明确把电力服务拆为 Power house + reticulation；记录大型负载证据是否存在。
- **官方云区域缺失检查**：AWS（无 Norfolk Island region；澳大利亚为 Sydney ap-southeast-2、Melbourne ap-southeast-4；新西兰 ap-southeast-6 而非 ap-southeast-5）、Azure（无 NF region；相关区域为 Australia East/Southeast/Central/Central 2/New Zealand North）、Google Cloud（无 NF region，官方 locations 页截至 2026-07-23 显示 43 regions/130 zones）、OCI（无 NF region；澳大利亚 East Sydney ap-sydney-1、Southeast Melbourne ap-melbourne-1 等）；不得把 CDN edge、VPN location、billing country、marketplace country list、reseller page 误认为本地部署。
- **分区覆盖矩阵**：manifest 单一分区 Norfolk Island，地点粒度仅用于发现线索；Burnt Pine（NIRC offices 39 Taylors Rd、商业中心、Norfolk Telecom/NIRC 服务、power/electricity 线索——中等产出，预期 telecom/utility/IT services 不是商业 DC）、Kingston（Government House、历史/行政地点、政府 ICT 机房线索——低产出）、Cascade（port/wharf、公共工程、可能通信路径误报检查——无已核实现代海缆登陆）、Middlegate（居民/服务区）、Anson Bay（历史 Pacific Cable Station 背景，不得混同为现代 DC）、Emily Bay/Ball Bay/Rocky Point/Steels Point/Headstone/Longridge/Mount Bates/Mt Pitt（居民、旅游、山区/无线站点、base station/电力服务线索；Mt Pitt/Mount Bates 可用于无线/基台复核）；每个地点执行通用查询块并标记 `covered`，阴性结果也保留。
- **官方枚举工作流**：①读 manifest 确认 NF 只有 Norfolk Island 一个 division ②联邦扫描（DITRDCSA/Administrator/media releases/legislation/ABS）③NIRC 扫描（Home/Norfolk Telecom/News/Tenders/EOI/Planning/Electricity/会议 papers）④采购扫描（AusTender/Digital Marketplace/NIRC tenders，关键词 ICT/managed services/telecommunications/satellite backhaul/electricity/generator/cloud）⑤监管扫描（ACMA/DITRDCSA rules/IANA `.nf`/ABN/ASIC）⑥电信扫描（NIRC Norfolk Telecom + 2026 backhaul + 2015 Review + 服务页；satellite backhaul/core switch/office/base-station shelters 作 telecom assets 不自动进入 DC inventory）⑦电力扫描（Power house/reticulation/asset plans/BESY/tariff review）⑧云区域缺失检查（AWS/Azure/GCP/OCI 官方 region pages）⑨对每个候选先分类（commercial_datacenter/government_server_room/telecom_exchange_or_core/satellite_earth_station_or_backhaul/power_house_or_utility/domain_registry_or_isp/seo_false_positive）⑩运营状态至少一个 A 级来源 ⑪容量只在来源明确给出时记录。
- **当前设施与项目种子（2026-08-12）**：Norfolk Telecom satellite backhaul（Telstra contract，运营中，2023 合同初始期至 2026-01，2026 年 NIRC 正在重谈服务级别/费用——A）；Norfolk Telecom core/exchange/network office（Burnt Pine，运营中，容量未公开，非商业 DC——A 存在性，设施细节逐项核实）；O3b satellite earth-station/backhaul facilities（2014-2015 明确建设/运营，当前是否仍主用需 NIRC/Telstra/NTL 复核——A/B 历史存在，当前状态需 A 级更新）；NIRC Power house/electricity reticulation（运营中，小型电网，柴油 + solar/battery 转型——A）；NIDS/`.nf` registry（运营中，不等于 DC——A registry/ISP 存在性）；Gondwana-1 Norfolk landing claim（不成立——B/C 背景，不得入库存）；SEO "Norfolk Island data center/VPS/dedicated server" 页面（排除——C）。

## 行业/媒体/目录/误报核验要点（详见 explorer-industry.md）

- **市场形态与当前结论**：Norfolk Island 是 no-market / pre-commercial datacenter territory；本轮未发现任何经核实的第三方托管、commercial colocation、hyperscale、公有云区域、IXP 或设施级 DC 项目；真实运营商景观是小岛电信/卫星/本地电力：Norfolk Telecom（NIRC 体系内）、Telstra satellite backhaul、历史 O3b/C8 satellite systems、NIRC Power house/electricity reticulation、NIDS `.nf` registry/ISP/VoIP/NBN services。
- **运营商与供应商扫描**：Norfolk Telecom/NIRC Telecom（A，可支撑 telecom asset 不支撑 commercial DC）、NIRC satellite backhaul/Telstra 合同（A，核心电信连接证据）、Norfolk Telecom service pages ni.net.nf（A/B 运营商页，客户服务线索不等于 DC）、Telstra satellite/wholesale backhaul（仅在 NIRC/Telstra 明确 NF 服务时使用，合同事实以 NIRC 为准）、O3b/SES 历史卫星（B/A，当前状态需复核）、NIDS（A registry/official site 存在性）、ACMA/DITRDCSA telecom framework（A 监管）、Sydney/Melbourne DC 运营商（Equinix、NEXTDC、AirTrunk、CDC、Digital Realty、Global Switch、Macquarie——A 区域背景，不得计入 NF）、Auckland/NZ 运营商（Spark、Datacom、CDC NZ、DCI、Chorus——A/B 区域背景）、Gondwana-1/OPT/Submarine Networks（B 背景；NF landing claim 不支持）。
- **海缆/卫星/电信线索**：Telstra satellite backhaul（运营中，A）；Norfolk Telecom core/exchange/office equipment（运营中电信 core/office/equipment-room 线索，容量未公开，非商业 DC，A 存在性）；O3b satellite dishes/历史卫星系统（2014 两个 O3b dishes 建设，2015 O3b IP + C8 backup backhaul，当前状态待核，A/B 历史）；mobile/base-station shelters 与 Mt Pitt fibre/backhaul（2G/4G radio network 支持基础设施，不是 DC，A/B）；NIRC Power house/electricity reticulation（小型电网约束与大型负载核验面，不是 DC，A）；NIDS `.nf` registry/ISP 服务（域名/VoIP/NBN/Sky Muster/IT services，不视为本地 DC，A 实体/服务存在性）；Gondwana-1 NF landing（未核实/不支持，C if claimed as NF facility）；历史 Pacific Cable Station（Anson Bay heritage，B/C 仅历史）。解释规则：satellite backhaul is connectivity, not datacenter capacity；cable maps 是地理/背景工具，不足以作为 NF 设施证明；earth station/satellite dishes 在库存范围含电信基础设施时可记作 telecom assets，否则作语境；不把 backhaul Mbps/Gbps 转成 DC MW。
- **行业媒体与二级来源**：ABC News（2014 O3b 报道，B）、RNZ Pacific（治理/电信/能源政策背景，B）、DCD（预期阴性，B）、CommsDay（澳新电信/监管报道，paywall 结果需回查一级来源，B）、ITNews Australia/ARN/CRN（澳洲 ICT 采购/managed services/vendor 语境，B）、Submarine Networks（海缆背景与负向检查；Gondwana-1 不建立 NF landing，B/C 按事实）、SubTel Forum/TeleGeography（海缆图交叉检查，背景/负向控制，B/C）、Islands Business（太平洋连接与政府数字语境，B）、NIRC newsletters/media releases（官方则 A）、Baxtel/DataCenterMap/Cloudscene/Datacenters.com（目录负向控制，预期空或错位结果，C）、VPS/VPN/location SEO 页（误报捕获，C）。
- **目录到一级核验工作流**：①官方/运营商扫描优先，目录扫描只作补充或阴性对照 ②若目录声称 Norfolk Island data center，必须回查运营商官网、物理地址、ABN/ASIC、ACMA/licensing、NIRC planning/tender/electricity 证据、可信媒体 ③检查是否只是服务国家列表、VPN endpoint、VPS checkout location、billing country、IP geolocation、CDN PoP 或 SEO doorway page ④检查是否实际设施在 Sydney/Melbourne/Auckland/Guam/Nouméa 或其它区域市场 ⑤无一级证据时记录为 seo_false_positive / directory_false_positive，不得创建设施 ⑥对 `.nf` 和 NIDS：registry/DNS/VoIP/NBN/Sky Muster/IT support 仅证明服务，不证明 server hall 或 colocation。
- **地点检索配方与覆盖矩阵**：单一分区 + 领地内地点变体；每个地点执行通用块并标记 covered；覆盖清单——Norfolk Island（全覆盖）、Burnt Pine（中 telecom/utility/IT services，低 DC）、Kingston（低-中 government ICT，低 DC）、Cascade（低-中 port/infrastructure，低 DC，现代 cable landing 说法需严格核验）、Anson Bay（历史通信背景，低现代设施，Pacific Cable Station heritage false-positive risk）、Middlegate（低）、Mt Pitt/Mount Bates（低-中 radio/base station）、Emily Bay/Ball Bay/Rocky Point/Steels Point/Headstone/Longridge（极低-低，只需阴性覆盖）。
- **容量提取指引**：当前无任何 NF commercial data center 可记录 MW/机架/建筑面积；Norfolk Telecom/NIRC 电信设施除非来源明确给出 UPS、generator、rack、IT load、floor area 或 telecom room specs，否则 `capacity_mw: null`；卫星 backhaul 记录为 connectivity capacity（Mbps/monthly cost/SLA），不得折算为 DC 容量；电力记录只说明电网约束与大型负载可行性；云区域只作 off-island background。
- **枚举矩阵与分级规则**：Telstra satellite backhaul（telecom_backhaul，operational/合同重谈中，A）；Norfolk Telecom core/exchange/office equipment（telecom_exchange_or_core，operational，容量未知，A）；O3b satellite dishes/历史地球站（satellite_earth_station_or_backhaul，历史确认，当前角色需更新，A/B）；NIRC Power house/electricity reticulation（power_utility，operational，A）；NIDS/`.nf` registry 与 ISP/VoIP 服务（registry_isp_service，operational service，作为 DC 排除，A）；Gondwana-1 NF landing（false_positive_or_regional_background，排除，C for NF facility claim）；SEO "Norfolk Island data center/VPS" 页（seo_false_positive，排除，C）；Sydney/Melbourne/Auckland/Nouméa/Guam 设施（regional_background，从 NF 排除，A/B 仅 off-island context）。分级规则：A 级来源证明其实际陈述的事实（如 NIRC satellite backhaul 证明 backhaul 服务，不证明 DC）；只有 A 级来源或直接引用/链接一手文件的 B 级报道可确立 `operational`；电信、电力、历史 cable heritage 与商业 DC 严格区分；区域 cable map/market directory 如无 NF landing/physical-address proof 只能作背景或误报；目录、SEO、VPN/VPS 结果未通过 operator/government/planning/electricity 复核前均不得入库存。
- **预期枚举结果**：极小且保守的清单——Norfolk Telecom/NIRC satellite backhaul、Norfolk Telecom core/exchange/office equipment、历史/当前 satellite earth-station assets、NIRC Power house/electricity reticulation、NIDS `.nf` registry/ISP services，以及若干 C 级 SEO/目录误报；预期不会出现任何经证实的商业数据中心；若未来出现 NF data center 声称，必须具备具名运营商、明确地点、设施类型、运营状态以及 NIRC/电力/规划/采购或监管证据后才能进入库存。

## 维护注意（更新纪律）

- **更新节奏**：批次运行时以检索当日为准更新证据日期与状态；O3b 历史卫星系统与 Gondwana-1 相关声明每次复查；2026 satellite backhaul 重谈结果跟踪 NIRC 新闻。
- **来源核验**：只有 A 级来源或直接引用/链接一手文件的 B 级报道可确立 operational；目录/SEO/VPN/VPS 结果未通过 operator/government/planning/electricity 复核前不得入库存；对极小领地，阴性证据同样重要——记录已扫过的 official pages、tenders、cloud region pages 和目录误报，防止重复误判。
- **不删除纪律**：本目录只新增/更新 SKILL.md、ANATOMY.md 与探索产物，禁止删除/移动任何现有文件（explorer-official.md、explorer-industry.md 与历史证据保留为原始记录）。
