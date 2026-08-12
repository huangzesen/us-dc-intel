---
name: nu-datacenter-methodology
location: scripts/expansion/world/country-skills/NU/SKILL.md
description: 纽埃数据中心双线查询方法论（官方/监管源 + 行业/厂商源），单 division 整岛覆盖，预期零商业托管市场，含 Manatua 海缆/Starlink/.NU 误判排除与查询模板；Niue datacenter dual-line discovery methodology (official/regulatory + industry/vendor sources), single-division whole-island coverage, expected zero commercial colocation market, with Manatua cable/Starlink/.NU false-positive exclusions and query templates. 运行 NU 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# NU · 纽埃数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为纽埃（Niue, NU）数据中心枚举批次提供官方与行业双线方法。官方线（explorer-official.md）覆盖政府/公报/立法、电信与通信监管、电力与负荷核验、Manatua 海缆登陆、公司注册、.NU/IUSN/DNS 基础设施与官方云区域缺失核验；行业线（explorer-industry.md）覆盖运营商/厂商扫描（Telecom Niue、Manatua、IUSN、Starlink、企业/公共部门机房线索、供应商/承包商）、目录与负向控制、枚举矩阵与最终分级规则。C 级只作线索或负向控制，不得单独确立设施存在；本领地负向先验很强，任何 "Niue VPS/cloud/dedicated server" 都必须先按 SEO/海外托管误报处理。

## 入口

| 文件 | 职责 | 内容概要 |
|---|---|---|
| explorer-official.md | 官方/监管源 | Government of Niue（gov.nu、Gazette/Notice Board/Media Releases/Projects）、Ministry of Finance、立法卷宗、Telecom Niue（telecomniue.com）、Starlink 2026 临时许可、PaCSON、电力（Niue Renewable Energy Phase 1/3、Department of Utilities、SPC/PCREEE/PRDR、PPA、MFAT/IATI）、Manatua 海缆（SubCom 合同 PDF、故障通报、Submarine Networks、ADB 47320-001 Tui-Samoa 误报控制、SSCC）、Niue Companies Office、.NU/IUSN/DNS（IANA、IUSN、Internet Niue、Internetstiftelsen）、官方云区域缺失（AWS/Azure/GCP/OCI） |
| explorer-industry.md | 行业/厂商源 | 行业基线（无公开中性托管市场）、Telecom Niue 扫描（业务/ICT/fibre/4G/ADSL/NOC 机房线索）、Manatua 海缆与 cable-adjacent 线索（facility access/RIO/FAA/wholesale interconnect）、IUSN/.NU registry、Starlink 与卫星供应商、企业/公共部门 server-room 线索（政府、医院、学校、机场、银行、BCN/TV）、供应商/承包商（SubCom、Sunergise、Fortinet/Cisco/Huawei/Alepo 等）、目录与负向控制、枚举矩阵与最终分级规则 |

## 核心结构事实

1. **Division 模型**：manifest 已核验 `country_code:"NU"`、`country_name:"Niue"`、`subnational_type:"country"`、`divisions:["Niue"]`。本法只覆盖一个分区 Niue（整岛）；枚举输出不得拆出省/州级行政区；村庄名只用于地理定位和误报排查。覆盖完成 = 输出中恰好一个 division key：`Niue`。
2. **国家基线**：公开资料未显示纽埃有数据中心专属监管登记册、DC 牌照类别或在线建设许可检索门户；数据中心发现应从政府项目、电信、能源、公司注册和官方云区域缺失核验入手。设施级通信资产集中在 Alofi（Telecom Niue、政府网络、Manatua 海缆登陆相关设施）；其他村庄通常只应出现基站、光缆、配电、公共服务 ICT 室或可再生能源资产。
3. **Manatua 海缆（关键连接性资产）**：SubCom 2018 合同公告确认 Manatua 联合体包括 OPT、Avaroa Cable、Telecom Niue、SSCC，并描述 Apia-Toahotu 主线及至 Niue、Aitutaki、Rarotonga、Bora Bora 的登陆/分支；Submarine Networks 记录 Manatua 连接 Samoa、Niue、Cook Islands、French Polynesia，且是 Niue 和 Cook Islands 的首次光纤连接；2026-08 纽埃政府发布 Manatua 故障通报，说明修复由 Manatua Cable partners 协调、Government of Niue 与 Telecom Niue 持续监控——这是 Manatua 当前运营相关性的 A 级政府证据。
4. **Tui-Samoa 不在纽埃登陆（误报控制）**：ADB 项目 47320-001 和 SSCC/Tui-Samoa 资料指向 Samoa-Fiji/Wallis & Futuna/Savai'i 路由；检索到 "Tui Samoa + Niue" 时按区域混淆处理，除非出现 A 级纽埃登陆证据；Tui-Samoa、SSCC、Apia、Tuasivi、SamoaTel、Digicel Samoa、Vodafone Samoa 属萨摩亚/Fiji/Wallis 区域语境，不得计入 NU。
5. **电力与负荷**：官方政府项目页显示 Niue Renewable Energy 位于 Hikufenoga, Tamakautoga（near airport），含 2.79 MWp PV、8.19 MWh BESS、电网升级，目标 2026 年 7 月/年中完成后由 Department of Utilities 与 Niue Power Corporation 接收——能源上下文，不是数据中心证据；任何 >0.5 MW 数据中心或大型服务器负荷声称必须有 NPC/Department of Utilities/gov.nu/funder 文件支持，没有电力侧痕迹时默认不可信。
6. **Starlink 状态（2026-05-12 更新）**：纽埃政府批准 Starlink/SpaceX 12 个月临时 Spectrum and Internet Communications Licence；Starlink 是连接性/韧性服务，不是数据中心；更早的未授权使用报道必须按时间范围处理。
7. **.NU / IUSN / DNS 基础设施**：IANA .NU 委派记录确认 ccTLD manager 为 The IUSN Foundation（Alofi），technical contact 为 The Internet Infrastructure Foundation（Sweden），registration services URL 为 Internetstiftelsen；该记录支持域名基础设施叙事但不证明纽埃本地数据中心；.nu ccTLD、DNS、Wi-Fi funding 和域名争议是连接性/数字经济背景；即使发现本地 DNS/server 设备，也按 `dns_registry_infrastructure` 或 `public_wifi_infrastructure` 处理，不计商业数据中心。
8. **设施/项目种子（2026-08 证据状态）**：Manatua/Alofi cable landing facility（A 海缆项目与政府运营相关性，B 公共海缆库细节——记 `telecom_cable_station`，无 facility-access/interconnect 证据不得计 DC 或 colo）；Telecom Niue core network 与政府网络服务（A 运营商/服务存在性，设施细节未证实——记 `telecom_network_lead`）；Starlink 临时许可服务（A 2026 政府许可——`connectivity_service`）；Niue Renewable Energy PV/BESS（A——`power_context`，仅支持负荷合理性）；.NU/IUSN/Internetstiftelsen（A DNS 委派——`dns_registry_context`）；AWS/Azure/GCP/OCI 公共云区域在 NU 均无（A 负向——`cloud_absence`）。
9. **可靠性分级**：A = 政府、监管、国有企业、官方公司注册处、官方云区域页、官方项目/采购/法律文件、IANA 等主源；B = 具名、可追溯日期的区域媒体、行业媒体、承包商案例、多边项目页；C = 目录、地图、PeeringDB/ASN 聚合、社交页、SEO 托管页、市场报告摘要——C 级只作线索或负向控制，不得单独确立设施存在。
10. **计数与去重规则**：cable landing station != datacenter；电信运营商存在、ICT service、fibre、4G site、network site、repeater != colocation；Starlink、Kacific、SES、Intelsat 等卫星/批发容量是连接性资产不是本地数据中心；.nu 域名、DNS、Wi-Fi nation 故事不是数据中心（IANA 技术联系在 Sweden）；海外 "Niue VPS"、"Alofi dedicated server"、"Niue cloud hosting" SEO 页面默认 C 级，没有纽埃本地地址、运营商主源或公司注册锚定时不建档；任何大型电力或容量声称必须能解释在纽埃小岛电网中的负荷来源并由 NPC/gov.nu/MFAT/SPC 主源支持；A 级可单独确立 entity/project/negative cloud-region 事实但 facility status 仍必须与来源措辞一致；B 级可佐证事件、供应商案例或媒体线索，不能单独把 "network upgrade" 升级为 DC；C 级永远不能单独建档；License/registration/service page != facility；任何从 lead 到 facility 的升级必须引用 source URL、观察日期、原文措辞、运营商、位置以及为何该记录属于单一 division `Niue`。

## 常用查询模板

```text
site:gov.nu ("data center" OR "data centre" OR datacenter OR "server room" OR server OR hosting OR "e-government" OR digitization OR ICT)
site:gov.nu (tender OR procurement OR RFQ OR RFP OR contract OR award) (ICT OR fibre OR fiber OR cable OR power OR solar OR "data")
site:gov.nu ("Telecom Niue" OR telecommunications OR Starlink OR SpaceX OR spectrum OR licence OR license)
site:gov.nu ("Manatua" OR "submarine cable" OR "landing station" OR "cable fault" OR connectivity)
site:gov.nu ("Niue Power Corporation" OR NPC OR "Department of Utilities" OR BESS OR "battery energy storage" OR "solar farm")
site:mof.gov.nu (budget OR procurement OR ICT OR telecommunications OR energy OR infrastructure)
site:telecomniue.com (business OR enterprise OR "ICT Services" OR hosting OR server OR cloud OR NOC OR switch OR colocation OR "data centre" OR "data center")
site:telecomniue.com (Manatua OR cable OR fibre OR fiber OR broadband OR "network site" OR repeater OR Alofi OR Tuapa)
"Telecom Niue" ("data centre" OR "data center" OR colocation OR hosting OR "server room" OR "computer room" OR gateway OR NOC)
"Telecom Niue" (government OR "100%" OR shareholder OR corporatisation OR SOE OR "state owned")
"Starlink" "Niue" (license OR licence OR spectrum OR SpaceX OR "temporary")
"Niue Power Corporation" OR "Department of Utilities" (load OR demand OR grid OR diesel OR generator OR substation OR outage)
site:gov.nu ("Niue Renewable Energy" OR BESS OR "battery energy storage" OR "solar farm" OR Hikufenoga OR Tamakautoga)
"Niue" (MW OR MWp OR MWh OR "peak load" OR "peak demand") (NPC OR "Niue Power Corporation" OR gov.nu OR SPC OR PPA)
"Manatua" Niue (Alofi OR landing OR "landing station" OR "cable station" OR "ready for service" OR RFS OR fault OR repair)
"Manatua" ("Telecom Niue" OR "Avaroa Cable" OR OPT OR SSCC OR SubCom) (consortium OR cable OR landing OR capacity)
site:subcom.com Manatua Niue
site:gov.nu Manatua (fault OR cable OR landing OR Telecom)
"Tui Samoa" OR "Tui-Samoa" Niue (landing OR spur OR branch)
site:adb.org "Samoa Submarine Cable Project" "47320-001"
site:companies.gov.nu ("Telecom Niue" OR "Niue Power" OR "IUSN" OR "Internet Users Society" OR Starlink OR SpaceX)
"IUSN" OR "Internet Users Society" Niue (registry OR ".nu" OR DNS OR server OR infrastructure OR WiFi OR "free internet")
site:iana.org/domains/root/db/nu
"Niue" ("AWS Region" OR "AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR hyperscale)
"Niue" ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR "server room" OR "cable station" OR "landing station")
"Alofi" Niue (server OR hosting OR "data centre" OR "data center" OR NOC OR switch OR fibre OR cable OR colocation)
"{Village}" Niue ("data center" OR "data centre" OR server OR hosting OR fibre OR broadband OR ICT OR power OR solar)
"Manatua" ("facility access" OR FAA OR colocation OR interconnect OR "customer equipment" OR "meet me" OR "landing station access")
"Telecom Niue" (Fortinet OR Cisco OR Huawei OR Alepo OR vendor OR upgrade OR "government network")
"Niue" (Sunergise OR BESS OR "solar farm" OR "battery energy storage") (project OR contractor OR completion OR NPC)
"Government of Niue" (server OR "server room" OR "computer room" OR "data centre" OR "data center" OR backup OR DR)
"Niue" ("data center" OR "data centre" OR datacenter OR colocation OR "dedicated server" OR VPS OR "cloud hosting") -Starlink -"free wifi"
site:datacentermap.com Niue OR Alofi
site:peeringdb.com Niue OR "Telecom Niue"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **政府与法律**：Government of Niue（gov.nu，Gazette Notices/Notice Board/Media Releases/Projects）、Ministry of Finance（mof.gov.nu）、Niue ICT quick link（ictniue.nu，由 gov.nu quick links 暴露，使用前复核）、立法卷宗与增补（gov.nu Information → Legislation）；政府文件是 A 级项目/监管证据，媒体转述只是 B/C。
- **电信与通信监管**：Telecom Niue（telecomniue.com）官方站有 Personal、Business、Fibre、4G Wireless、ADSL、ICT Services 等导航；本次核验未发现公开 colocation/rack hosting/data centre 服务页；Telecom Niue 的政府数字化活动页称其作为 project manager 协助各部门迁移到新网络——政府网络项目线索，不是 DC 设施证据；2026 政府 Starlink 许可页同时称 Telecom Niue 继续升级岛内 fibre-optic network，并在 Alofi、Tuapa 部署新网络站点——通信基础设施，不等于数据中心；PaCSON profile（B/A-adjacent 支持 SOE 状态，不单独用于设施）。
- **电力与公用事业负荷核验**：Government Niue Renewable Energy Phase 1/3、Department of Utilities notice board、SPC/PCREEE/PRDR（pcreee.org、prdrse4all.spc.int）、Pacific Power Association（ppa.org.fj）、MFAT Niue 页与 IATI 数据（mfat.govt.nz、devdata.mfat.govt.nz）；能源项目只能支持电力可得性或负荷合理性核验；任何 >0.5 MW 数据中心或大型服务器负荷声称必须有 NPC/Department of Utilities/gov.nu/funder 文件支持。
- **海缆登陆：Manatua，不是 Tui-Samoa**：SubCom Manatua contract-in-force PDF（2018-11-19）、SubCom cable lay complete PDF（2020-02-17）、Government of Niue Manatua fault update、Submarine Networks Manatua profile（B）、ADB Samoa Submarine Cable Project 47320-001（Tui-Samoa 背景/误报控制）、SSCC（Tui-Samoa/Samoa-side 语境）；记录规则：Manatua Alofi 登陆站记录为 `telecom_cable_station`；只有 Telecom Niue/Manatua consortium/RIO/FAA/official facility-access 文件明确支持客户设备接入、互联、托管或类托管服务时，才升级为 `colo_adjacent_telecom`。
- **公司注册**：Niue Companies Office（companies.gov.nu）——Companies Register of Niue 是面向公众的电子注册簿；核实 Telecom Niue、Niue Power Corporation、IUSN、Starlink 本地许可实体/代理、承包商或项目 SPV 的法律名称；注册处证据是 A 级法律存在证据但不是设施证据。
- **.NU / IUSN / DNS**：IANA .NU delegation、IUSN Foundation（iusn.org）、Internet Niue（internetniue.nu）、Internetstiftelsen（internetstiftelsen.se）；记录规则：.nu ccTLD、DNS、Wi-Fi funding 和域名争议是连接性/数字经济背景；IANA 明确技术联系在瑞典，不支持本地 DC 结论。
- **官方云区域缺失核验**：只用厂商官方页面做 A 级缺失性结论——AWS Regions/Local Zones、Azure、Google Cloud（cloud.google.com/about/locations、datacenters.google/locations）、Oracle OCI 官方页均无 NU region/Local Zone/自有数据中心；每次刷新复查。
- **分区覆盖与村庄策略**：覆盖完成 = 输出恰好一个 division key `Niue`；村庄级检索只用于定位：Alofi/Alofi North/Alofi South、Avatele、Hakupu、Vaiea、Liku、Lakepa、Mutalau、Namukulu、Hikutavake、Toi、Tuapa、Makefu、Tamakautoga；Alofi 是唯一预期设施级枢纽，Tuapa 可能出现在 2026 网络站点工程中，Hikufenoga/Tamakautoga 出现在机场附近可再生能源项目；所有非 Alofi 村庄命中默认 `no_projects`，除非 A/B 来源具名与电信、能源、政府 ICT 或海缆登陆相关的物理设施。
- **刷新清单**：①确认 manifest 仍为 divisions:["Niue"] ②重跑 gov.nu ICT/Telecom Niue/Starlink/Manatua/采购/能源检索 ③重跑 Telecom Niue 站点 hosting/data centre/ICT services/NOC/fibre/Manatua 检索 ④复查 companies.gov.nu ⑤复查 IANA .NU 委派与 IUSN/Internet Niue 页 ⑥复查 Manatua 与 Tui-Samoa 路由证据（SubCom/ADB/SSCC/Submarine Networks）⑦复查 AWS/Azure/GCP/OCI 官方区域页 ⑧确认每条输出记录映射到单一 division `Niue`。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **行业基线**：本次核验未发现纽埃公开销售中性机架托管、商业 colocation、tiered datacenter、云区域或 hyperscale 容量；设施级行业信号集中在 Telecom Niue 与 Manatua；负向先验很强——人口和小岛电网规模使商业 DC 市场概率极低，任何 "Niue VPS/cloud/dedicated server" 都必须先按 SEO/海外托管误报处理。
- **Telecom Niue**：唯一本地有意义的运营商线索；官方站有 business services 和 ICT 措辞，政府发布将其与光纤升级和新网络站点关联；未验证到公开 colocation 服务；记录规则——Telecom Niue 页面可确立运营商/服务存在性；datacenter/colo 记录要求明确语言（"data centre"、"colocation"、"rack"、"hosting"、"facility access"、"customer equipment"、"NOC"）并带物理站点或服务边界；查询含 Fortinet/Cisco/Huawei/Alepo/vendor/upgrade/"government network" 转向。
- **Manatua 海缆与 cable-adjacent 线索**：Manatua 是 `telecom_cable_station` 线索，默认不是 colocation 设施；升级前搜索 facility-access 证据、RIO/FAA 条款、批发互联或客户设备接入（"facility access" OR FAA OR colocation OR interconnect OR "customer equipment" OR "meet me" OR "landing station access"）。
- **IUSN / .NU Registry**：.NU 造就了知名的 Niue 互联网故事，但不暗示本地托管；IANA 显示 Alofi manager 与 Sweden 技术联系/名称服务器基础设施；记录为 `dns_registry_context` 或 `public_wifi_context`，除非主源具名向第三方提供托管/colo/计算的本地设施。
- **Starlink 与卫星供应商**：Starlink 2026 年正式获临时 12 个月试验许可；更早的未授权使用报道按时间范围处理；卫星信号只作韧性/连接性语境；查询含 Kacific/SES/Intelsat 容量/合同/宽带/备份/冗余。
- **企业/公共部门 server-room 线索**：潜在内部机房线索包括政府部门、Niue Foou Hospital、学校、机场、公用事业、银行/金融办公室、BCN/TV Niue、较大酒店——通常为内部 IT 房，不得进入 DC 列表；仅当来源具名物理房间/站点时记录为 `enterprise_server_room_lead`；除非来源描述第三方托管/colo 或国家指定政府 DC，否则不计为数据中心。
- **供应商/承包商扫描**：高价值供应商——SubCom（Manatua）；Sunergise（2026 Hikufenoga/Tamakautoga solar/BESS 项目）；Telecom Niue/政府网络升级中的安全/网络供应商（如 Fortinet case study 证据）；厂商案例为 B 级，除非与运营商/政府主证据配对。
- **目录与负向控制**：datacentermap.com、cloudscene.com、datacenters.com、peeringdb.com、submarinecablemap.com 作为负向控制运行；C 级目录缺位不是证明，但有助于捕捉明显的市场声称；海外 VPS/hosting 提供视为 `seo_false_positive`，除非给出物理纽埃地址并独立锚定到 Telecom Niue、Companies Office 或政府/公用事业来源。
- **枚举矩阵**：commercial colo/hosting（A 级接纳：Telecom Niue 或其他官方本地运营商页具名 colo/hosting/racks，或政府许可/项目具名 DC；无 A/B 物理证据 = `no_market`）；cable landing（A：Telecom Niue/gov.nu/SubCom/联合体官方证据；升级仅在有 facility-access/customer-equipment 证据时）；telecom core（A：Telecom Niue/gov.nu 官方服务与网络页；`telecom_network_lead`，不是 DC）；cloud providers（官方区域页，官方缺位 = `cloud_absence`，营销页忽略）；energy/load（NPC/gov.nu/MFAT/SPC/PPA，仅能源语境，大型负荷合理性必需）；enterprise IT rooms（官方机构文档，仅线索除非第三方设施服务明确）；.NU/IUSN/DNS（IANA/IUSN/Internetstiftelsen，DNS/registry 语境，不是 DC）。
- **分区覆盖**：每条保留记录必须使用 division: "Niue"；村庄/位置可分开存储用于地理，但 division 不得超出 manifest；村庄搜索集含 Alofi、Alofi North/South、Avatele、Hakupu、Vaiea、Liku、Lakepa、Mutalau、Namukulu、Hikutavake、Toi、Tuapa、Makefu、Tamakautoga、Hikufenoga/Tamakautoga near airport；非 Alofi 默认 no_projects。
- **最终分级规则**：A 级可单独确立 entity/project/negative cloud-region 事实，但 facility status 仍必须与来源措辞一致；B 级可佐证事件、供应商案例或媒体线索，不能单独把 "network upgrade" 升级为 DC；C 级永远不能单独建档；License/registration/service page != facility；Cable landing != datacenter；Satellite != datacenter；DNS registry != datacenter；公共云缺位必须从官方提供商页面刷新；任何从 lead 到 facility 的升级必须引用 source URL、观察日期、原文措辞、运营商、位置以及为何该记录属于单一 division `Niue`。

## 维护注意（更新纪律）

- **更新节奏**：每次刷新按清单重跑 gov.nu/Telecom Niue/Companies Office/IANA/Manatua-Tui-Samoa 路由/云区域页；公共云缺位从官方提供商页面刷新；Starlink 许可状态按时间范围处理。
- **来源核验**：升级必须引用 source URL、观察日期、原文措辞、运营商、位置与 division 归属；C 级只作线索或负向控制；对极小岛市场，负向证据与村庄级 no_projects 记录同样重要。
- **不删除纪律**：本目录只新增/更新 SKILL.md、ANATOMY.md 与探索产物，禁止删除/移动任何现有文件（explorer-official.md、explorer-industry.md 与历史证据保留为原始记录）。
