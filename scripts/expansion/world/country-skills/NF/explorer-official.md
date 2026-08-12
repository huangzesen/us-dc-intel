# NF Explorer Official — 诺福克岛（Norfolk Island）数据中心枚举：政府 / 监管 / 电信 / 电力 / 采购

日期 Date: 2026-08-12
范围 Scope: Norfolk Island（NF）。Manifest 已核验：`{"country_code":"NF","country_name":"Norfolk Island","subnational_type":"country","divisions":["Norfolk Island"]}`。NF 是单一分区，division = `Norfolk Island`。
角度 Angle: 官方/监管口径发现（official/regulatory discovery），用于识别运营中、在建、拟建以及误报（false-positive）的数据中心候选对象。

可靠性分级 Reliability grades（本 explorer 使用）：
- **A** = 一级/官方来源：澳大利亚联邦政府、Norfolk Island Regional Council（NIRC）、监管机构、公共事业、运营商官方页、IANA/登记注册处、官方云厂商区域页、政府采购门户、正式议会/委员会文件。
- **B** = 可信本地/地区/行业媒体或承包商案例，要求具名当事方、日期、可回查的一手事实。
- **C** = 目录站、市场平台、SEO 托管页、VPN/VPS 位置页、无法核实的营销页或无出处转载。C 级只能作为线索或阴性对照，不能用于确立设施存在。

## 0. 已验证国家基线 Verified Country Baseline

- 诺福克岛是澳大利亚外部领地（external Australian territory）。澳大利亚基础设施、交通、区域发展、通信、体育与艺术部（DITRDCSA / Department of Infrastructure, Transport, Regional Development, Communications, Sport and the Arts）官方领地页确认其位于悉尼东北约 1,600 km，ABS 2021 人口为 2,188。官方领地页：https://www.infrastructure.gov.au/territories-regions/territories/norfolk-island
- 当前治理结构以澳大利亚联邦领地管理 + Norfolk Island Regional Council 地方服务为核心。Administrator 官方页确认 Administrator 代表澳大利亚政府并执行相关法定职能；2026-06-01 起任期的 Administrator 为 Fiona McKergow。Administrator 页：https://www.infrastructure.gov.au/territories-regions/territories/norfolk-island/norfolk-island-governance-administration/norfolk-island-administrator
- NIRC 当前官方域名是 `nirc.gov.au`，页面页脚仍使用 `customercare@nirc.gov.nf`、电话 `+6723 22001`。Council 办公地址为 Bicentennial Complex, 39 Taylors Rd, Burnt Pine, Norfolk Island。主页：https://www.nirc.gov.au/Home
- **结论：未发现经核实的商业数据中心市场。** 本轮核验未发现第三方托管/colo、超大规模云区域、本地公共云区域、IXP 或设施级数据中心公告。NF 的真实数字基础设施锚点是 NIRC/Norfolk Telecom 电信网络、卫星 backhaul、历史/当前卫星地球站、NIRC 电力系统与本地政府/企业 IT 机房。
- **重要纠偏：不要把 Gondwana-1 计作诺福克岛登陆。** 已核验的 Gondwana-1 资料显示该系统连接 New Caledonia 与 Australia，RFS 为 2008，主要登陆点为 Nouméa / Sydney 等；未发现 A 级或可靠 B 级来源证明 Gondwana-1 在 Norfolk Island 设有分支或登陆站。Submarine Networks 页面只可作为区域背景：https://www.submarinenetworks.com/en/systems/australia-usa/gondwana-1
- 官方 NIRC 2026-04-02 新闻明确说明 Norfolk Telecom 仍有 Telstra satellite backhaul 服务：2022 年 DITRDCSA 支持两年 `A$7.35 million` 资金以提升卫星连接，NIRC 2023 年经 tender 将 satellite backhaul 合同授予 Telstra，初始合同延续至 2026-01。该页是当前最强的 A 级电信连接证据：https://www.nirc.gov.au/Your-council/News-Articles/Satellite-Backhaul-Service
- 2015 年联邦委托的 Norfolk Island Mobile Network Review 记录 Norfolk Telecom 运营岛上固定/移动基础设施、负责国际/互联网连接；当时国际连接为 O3b IP satellite + C8 backup satellite。该报告还记录 PSTN/ADSL/GSM core、base station shelters、Norfolk Telecom office 可容纳 core network equipment 等事实。PDF：https://www.infrastructure.gov.au/sites/default/files/migrated/territories/publications/files/GQI_Norfolk_Island_Mobile_Network_Review_2015.pdf
- NIRC 电力页面确认 Norfolk Island electricity services 包括 `Power house (including mechanical workshop)` 与 reticulation。电力系统页：https://www.nirc.gov.au/Infrastructure/Electricity-System ，服务页：https://www.nirc.gov.au/Infrastructure/Infrastructure-Services/Electricity
- `.nf` ccTLD IANA 记录显示 manager 为 Norfolk Island Data Services，地址在 Norfolk Island；这是域名/注册服务存在证据，不是本地数据中心证据。IANA 记录：https://www.iana.org/domains/root/db/nf.htm
- 官方记录语言为英语；检索一律使用英文关键词。本文保持中文为主、英文实体名/查询模板保留的 bilingual style。

## 1. 官方来源优先级 Official Sources To Check First

### 1.1 澳大利亚联邦政府与领地行政

主要来源 Primary sources：

- DITRDCSA Norfolk Island 领地页：https://www.infrastructure.gov.au/territories-regions/territories/norfolk-island
- Norfolk Island Administrator：https://www.infrastructure.gov.au/territories-regions/territories/norfolk-island/norfolk-island-governance-administration/norfolk-island-administrator
- Norfolk Island media releases（从领地页进入）：https://www.infrastructure.gov.au/territories-regions/territories/norfolk-island
- Federal Register of Legislation：https://www.legislation.gov.au/
- ABS Norfolk Island / Census 检索：https://www.abs.gov.au/

用法 Use：

- 用 DITRDCSA 确认治理结构、联邦拨款、通信/ICT/能源项目和 Administrator 公告。
- 用 legislation.gov.au 检索 Norfolk Island 相关法律延伸、通信、电力、地方政府、规划与采购授权。
- 若出现政府数据中心/ICT 机房项目，必须能回到 DITRDCSA、NIRC、AusTender 或正式议会/委员会文件。

政府查询模板 Government query templates：

```text
site:infrastructure.gov.au/territories-regions/territories/norfolk-island ("data centre" OR "data center" OR datacenter OR ICT OR "server room" OR cloud)
site:infrastructure.gov.au/territories-regions/territories/norfolk-island ("telecommunications" OR "satellite backhaul" OR "Norfolk Telecom" OR broadband OR "mobile network")
site:infrastructure.gov.au "Norfolk Island" ("grant" OR funding OR tender OR contract) ("telecommunications" OR ICT OR "satellite backhaul" OR electricity)
site:legislation.gov.au "Norfolk Island" ("telecommunications" OR "carrier licence" OR "electricity" OR planning OR procurement)
site:abs.gov.au "Norfolk Island" ("2021 Census" OR population)
```

### 1.2 Norfolk Island Regional Council（NIRC）

主要来源 Primary sources：

- NIRC 主页：https://www.nirc.gov.au/Home
- Norfolk Telecom（NIRC corporate/finance page）：https://www.nirc.gov.au/Corporate-finance/Norfolk-Telecom
- Satellite backhaul news（2026）：https://www.nirc.gov.au/Your-council/News-Articles/Satellite-Backhaul-Service
- Tenders and EOI：https://www.nirc.gov.au/Your-council/Tenders-and-EOI
- Closed opportunities：https://www.nirc.gov.au/Your-council/Tenders-and-EOI/Closed-Opportunities
- Planning and Development（从主页导航）：https://www.nirc.gov.au/Home
- Electricity System：https://www.nirc.gov.au/Infrastructure/Electricity-System
- Electricity services：https://www.nirc.gov.au/Infrastructure/Infrastructure-Services/Electricity
- Electricity forms：https://www.nirc.gov.au/Infrastructure/Infrastructure-Forms/Electricity-Forms

用法 Use：

- NIRC 是地方规划、招标、电力服务、Norfolk Telecom 运营信息和 Council IT 采购的一手来源。
- Tenders and EOI 可直接发现 ICT managed services、telecom、electricity、generator、network、software 等采购。2026 年已出现 `ITT 7/2026 - Managed Services Provider for Information Technology`，这类属于政府 IT 服务线索，不等于数据中心设施。
- Planning and Development 用于查 `development application`、land use、large load 或 building works。NF 没有发现全国性可检索 DC 规划门户，需结合 NIRC 页面、会议 papers、media releases 与站内搜索。

NIRC 查询模板 NIRC query templates：

```text
site:nirc.gov.au ("data centre" OR "data center" OR datacenter OR "server room" OR "computer room" OR cloud OR "managed services")
site:nirc.gov.au ("Norfolk Telecom" OR telecom OR telecommunications OR "satellite backhaul" OR Telstra OR broadband OR "mobile network")
site:nirc.gov.au ("tender" OR "RFT" OR "RFQ" OR "ITT" OR procurement OR "managed services") ("ICT" OR IT OR telecom OR network OR cloud)
site:nirc.gov.au ("development application" OR planning OR "land use" OR "building approval") ("telecommunications" OR "data centre" OR "data center" OR electricity)
site:nirc.gov.au ("Power house" OR "power station" OR electricity OR diesel OR generator OR solar OR battery OR BESY)
site:nirc.gov.au/files "Norfolk Telecom" ("satellite" OR backhaul OR Telstra OR "mobile network" OR broadband)
```

### 1.3 澳大利亚采购与公司/登记体系

主要来源 Primary sources：

- AusTender：https://www.tenders.gov.au/
- Digital Marketplace / BuyICT：https://www.digitalmarketplace.gov.au/
- ABN Lookup：https://abr.business.gov.au/
- ASIC：https://asic.gov.au/ 与 ASIC Connect：https://connectonline.asic.gov.au/

用法 Use：

- 联邦资助或联邦部门采购可能进入 AusTender；NIRC 地方采购主要在 NIRC Tenders and EOI。
- 任何声称在 NF 运营数据中心、hosting、ISP、managed cloud 的公司，需用 ABN/ASIC 核对实体状态和地址。注册地或邮政地址不等于设施所在地。

采购/登记查询模板 Procurement & registry queries：

```text
site:tenders.gov.au "Norfolk Island" ("ICT" OR "information technology" OR telecommunications OR "satellite backhaul" OR "data centre" OR "data center" OR cloud)
site:tenders.gov.au "Norfolk Island" (electricity OR generator OR diesel OR solar OR battery OR "power station")
site:digitalmarketplace.gov.au "Norfolk Island"
site:abr.business.gov.au "Norfolk Island" ("data" OR telecom OR hosting OR technology OR internet)
site:asic.gov.au "Norfolk Island" ("data centre" OR "data center" OR hosting OR telecommunications)
"Norfolk Island" ("AusTender" OR tender OR RFT OR RFQ OR procurement) ("telecommunications" OR ICT OR "satellite backhaul")
```

### 1.4 电信监管与编号

主要来源 Primary sources：

- ACMA：https://www.acma.gov.au/
- DITRDCSA carrier/service provider rules：https://www.infrastructure.gov.au/media-communications/internet/rules-carriers-and-service-providers
- ACMA carrier licensing guide：https://www.acma.gov.au/
- IANA `.nf` delegation：https://www.iana.org/domains/root/db/nf.htm

已验证信号 Verified signals：

- 澳大利亚 carrier/service provider 框架要求 carrier 对用于向公众供应通信服务的 network units 持有 ACMA carrier licence。该事实证明监管门槛，不证明设施存在。
- 2015 Mobile Network Review 说明当时部分 Norfolk Island 频谱事项由 ACMA 管理；之后澳大利亚通信监管框架延伸到 NF 的细节需以当前 ACMA/DITRDCSA 文件复核。
- `.nf` 由 Norfolk Island Data Services 管理；NIDS 同时提供 internet/VoIP/NBN/Sky Muster 类服务页面，但注册局/ISP 服务不得自动转化为本地 DC 设施。

监管查询模板 Regulatory queries：

```text
site:acma.gov.au "Norfolk Island" ("carrier licence" OR "carrier licensing" OR telecommunications OR radiocommunications OR numbering)
site:acma.gov.au "Norfolk Island" ("Norfolk Telecom" OR "Norfolk Island Regional Council" OR "broadcasting licence")
site:infrastructure.gov.au/media-communications "Norfolk Island" ("carrier" OR telecommunications OR "service provider")
site:iana.org/domains/root/db/nf "Norfolk Island Data Services"
"Norfolk Island" ("+6723" OR "+672 3" OR numbering OR "telephone numbers")
"Norfolk Island Data Services" ("hosting" OR "data centre" OR "data center" OR server OR DNS OR VoIP OR NBN)
```

### 1.5 Norfolk Telecom / NIRC Telecom

主要来源 Primary sources：

- NIRC Norfolk Telecom：https://www.nirc.gov.au/Corporate-finance/Norfolk-Telecom
- NIRC satellite backhaul 2026：https://www.nirc.gov.au/Your-council/News-Articles/Satellite-Backhaul-Service
- Norfolk Telecom customer/service pages, current/historic domain observed at `ni.net.nf`，例如 ADSL：https://www.ni.net.nf/adsl
- 2015 Mobile Network Review PDF：https://www.infrastructure.gov.au/sites/default/files/migrated/territories/publications/files/GQI_Norfolk_Island_Mobile_Network_Review_2015.pdf

已验证信号 Verified signals：

- Norfolk Telecom 是岛上关键电信网络运营主体，提供 fixed/mobile/broadband/international connectivity。NIRC 页面是当前最高优先级入口。
- 2015 报告记录：PSTN 使用 copper / some fibre / Ericsson AXE switch；移动网络有 core/BSC/BTS、base station shelters；radio base station backhaul 多为 E1，部分 fibre；国际连接当时为 O3b IP satellite + C8 backup satellite。
- 2026 NIRC 页面记录：卫星 backhaul 由 Telstra 合同提供，合同/费用/服务等级正在重谈；Council 明确表示该问题不影响 internet 或 voice connectivity。
- 这些证据支持 `telecom_exchange / telecom_core / satellite_backhaul / network_facility` 分类；除非来源明确提供 colocation、rack rental、commercial datacenter、facility address 和运营状态，否则不得记为商业 DC。

NTL 查询模板 Norfolk Telecom queries：

```text
site:nirc.gov.au "Norfolk Telecom" ("data centre" OR "data center" OR datacenter OR "server room" OR "core network" OR switch OR NOC)
site:nirc.gov.au "Norfolk Telecom" ("satellite backhaul" OR Telstra OR O3b OR C8 OR "international connectivity" OR broadband)
site:ni.net.nf ("data centre" OR "data center" OR datacenter OR hosting OR "server room" OR business OR ADSL OR fibre OR fiber)
"Norfolk Telecom" "Burnt Pine" (office OR exchange OR switch OR "server room" OR "core network")
"Norfolk Telecom" (satellite OR O3b OR Telstra OR backhaul OR "earth station" OR "two satellite dishes")
"Norfolk Island" "Mobile Network Review" "Norfolk Telecom" ("AXE" OR "core network" OR "satellite systems")
```

### 1.6 电力、公用事业与大型负荷

主要来源 Primary sources：

- NIRC Electricity System：https://www.nirc.gov.au/Infrastructure/Electricity-System
- NIRC Electricity services：https://www.nirc.gov.au/Infrastructure/Infrastructure-Services/Electricity
- NIRC Electricity forms：https://www.nirc.gov.au/Infrastructure/Infrastructure-Forms/Electricity-Forms
- NIRC electricity tariff review news：https://www.nirc.gov.au/Your-council/News-Articles/Independent-Review-of-Electricity-Tariff
- NIRC public exhibition / asset management plan PDFs（站内检索）

已验证信号 Verified signals：

- NIRC 明确把电力服务拆为 Power house + reticulation。电力系统很小，历史上柴油发电为主，近年来有 rooftop solar、battery、BESY energy platform 与 tariff review。
- NIRC 2024 newsletter 记录 rooftop solar/battery uptake 与 diesel displacement 进展；这些是电力约束/可再生能源背景，不是 DC 证据。
- 对 NF，任何多百 kW 或 MW 级数据中心宣称都应首先出现电力接入、发电、配电、planning 或 Council meeting 证据。没有电力/规划证据时，应判为误报或未核实线索。

电力查询模板 Power queries：

```text
site:nirc.gov.au ("Power house" OR "power station" OR electricity OR diesel OR generator OR reticulation OR transformer)
site:nirc.gov.au ("solar" OR battery OR BESY OR renewable OR "tariff review" OR "asset management plan")
site:nirc.gov.au ("large load" OR "new connection" OR "supply of electricity" OR "electrical contractor")
"Norfolk Island" ("power station" OR "Power house" OR electricity OR diesel OR generator OR solar OR battery)
"Norfolk Island" ("data centre" OR "data center" OR datacenter) (power OR electricity OR generator OR "large load")
```

### 1.7 官方云区域缺失检查 Official Cloud Region Absence Checks

仅用于确认超大规模厂商是否在 NF 设有公有云区域/本地区/边缘区。不得把 CDN edge、VPN location、billing country、marketplace country list、reseller page 误认为本地部署。

| Provider | 官方来源 Official source | NF 结果（截至 2026-08-12） |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ 与 https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | 无 Norfolk Island region。官方文档列出 Australia: Sydney `ap-southeast-2`, Melbourne `ap-southeast-4`; New Zealand 为 `ap-southeast-6`（不是 `ap-southeast-5`）。 |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list 与 https://azure.microsoft.com/en-au/explore/global-infrastructure/geographies | 无 Norfolk Island region。相关区域为 Australia East / Australia Southeast / Australia Central / Australia Central 2 / New Zealand North。 |
| Google Cloud | https://cloud.google.com/about/locations 与 https://docs.cloud.google.com/compute/docs/regions-zones | 无 Norfolk Island region。Google Cloud 官方 locations 页截至 2026-07-23 显示 43 regions / 130 zones；Australia/NZ 区域需从官方表核对。 |
| Oracle Cloud Infrastructure | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm 与 https://www.oracle.com/cloud/public-cloud-regions/ | 无 Norfolk Island region。官方表列 Australia East (Sydney) `ap-sydney-1`、Australia Southeast (Melbourne) `ap-melbourne-1` 等。 |

云查询模板 Cloud absence queries：

```text
site:aws.amazon.com "Norfolk Island" "AWS Region"
site:docs.aws.amazon.com "Norfolk Island" "ap-"
site:learn.microsoft.com "Norfolk Island" Azure region
site:cloud.google.com "Norfolk Island" "Google Cloud" region
site:docs.oracle.com "Norfolk Island" "OCI" region
```

## 2. 分区覆盖矩阵 Division Coverage Matrix

Manifest 给出单一分区 **Norfolk Island**。因此分区覆盖 = 全领地覆盖；地点粒度仅用于发现 telecom/electricity/government 线索。每个地点执行通用查询块并标记 `covered`，阴性结果也保留。

| 地点 Locality | 覆盖状态 | 预期产出 / 官方路径 |
|---|---:|---|
| Norfolk Island（manifest division） | 必查 | 全领地通用搜索、联邦/NIRC/ACMA/AusTender/云区域缺失检查。 |
| Burnt Pine | 必查 | NIRC offices at 39 Taylors Rd、商业中心、Norfolk Telecom/NIRC 服务、power/electricity 线索。中等产出；预期为 telecom/utility/IT services，不是商业 DC。 |
| Kingston | 必查 | Government House、历史/行政地点；政府 ICT 机房线索。低产出。 |
| Cascade | 必查 | port/wharf、公共工程、可能通信路径误报检查。无已核实现代海缆登陆。 |
| Middlegate | 覆盖 | 居民/服务区；电力、电信服务公告。低产出。 |
| Anson Bay | 覆盖 | 历史 Pacific Cable Station 背景；不得混同为现代 DC。 |
| Emily Bay / Ball Bay / Rocky Point / Steels Point / Headstone / Longridge / Mount Bates / Mt Pitt | 覆盖 | 居民、旅游、山区/无线站点、base station/电力服务线索。低产出。Mt Pitt/Mount Bates 可用于无线/基地台复核。 |

通用地点查询块 Universal locality query block：

```text
"{locality}" "Norfolk Island" ("data centre" OR "data center" OR datacenter)
"{locality}" "Norfolk Island" ("server room" OR server OR hosting OR colocation OR "co-location" OR "managed services")
"{locality}" "Norfolk Island" ("Norfolk Telecom" OR telecom OR telecommunications OR broadband OR "satellite backhaul" OR "mobile network")
"{locality}" "Norfolk Island" (electricity OR "power station" OR "Power house" OR diesel OR generator OR solar OR battery)
"{locality}" "Norfolk Island" (tender OR procurement OR "development application" OR planning)
site:nirc.gov.au "{locality}" ("Norfolk Telecom" OR electricity OR tender OR ICT OR planning OR "satellite backhaul")
```

高产出地点变体 High-yield locality variants：

```text
"Burnt Pine" "Norfolk Island" ("Norfolk Telecom" OR office OR exchange OR switch OR "server room" OR "Power house")
"Burnt Pine" "Norfolk Island" ("data centre" OR "data center" OR datacenter OR hosting)
"Kingston" "Norfolk Island" (government OR administration OR ICT OR server)
"Cascade" "Norfolk Island" (wharf OR port OR telecom OR cable OR "development application")
"Anson Bay" "Norfolk Island" ("Pacific Cable Station" OR cable OR telegraph)
"Mt Pitt" OR "Mount Pitt" "Norfolk Island" ("base station" OR telecom OR radio OR fibre OR fiber)
```

## 3. 官方枚举工作流 Official Enumeration Workflow

1. 读取 manifest，确认 NF 只有 `Norfolk Island` 一个 division。
2. 联邦扫描：DITRDCSA Norfolk Island 领地页、Administrator、media releases、legislation.gov.au、ABS。
3. NIRC 扫描：Home、Norfolk Telecom、News Articles、Tenders and EOI、Closed Opportunities、Planning and Development、Electricity pages、Council meeting papers/PDFs。
4. 采购扫描：AusTender、Digital Marketplace、NIRC tenders；关键词包括 ICT、managed services、telecommunications、satellite backhaul、electricity、generator、cloud。
5. 监管扫描：ACMA、DITRDCSA carrier/service provider rules、IANA `.nf`、ABN/ASIC。
6. 电信扫描：NIRC Norfolk Telecom + 2026 satellite backhaul + 2015 Mobile Network Review + Norfolk Telecom service pages。将 satellite backhaul / core switch / office / base-station shelters 作为 telecom assets，不自动进入 DC inventory。
7. 电力扫描：NIRC Power house / reticulation / asset plans / BESY / tariff review；记录大型负荷证据是否存在。
8. 云区域缺失检查：AWS / Azure / Google Cloud / OCI 官方 region pages。
9. 对每个候选先分类：`commercial_datacenter` / `government_server_room` / `telecom_exchange_or_core` / `satellite_earth_station_or_backhaul` / `power_house_or_utility` / `domain_registry_or_isp` / `seo_false_positive`。
10. 运营状态至少需要一个 A 级来源；仅 C 级或 SEO 来源时只能为 `false_positive` 或 `unverified_lead`。
11. 容量只在来源明确给出 IT load、rack count、building area、UPS/generator capacity 或 telecom bandwidth 时记录；不得把卫星 backhaul 带宽、电力系统容量或云厂商区域背景折算为 `capacity_mw`。

## 4. 当前设施与项目种子 Current Facility And Project Seeds

以下是枚举校验种子；入库前逐项重新核实，且按资产类型保守分类。

| Seed | 地点 | 类型 | 当前状态（截至 2026-08-12） | 最佳证据 | 可靠性 |
|---|---|---|---|---|---|
| Norfolk Telecom satellite backhaul（Telstra contract） | Norfolk Island | 电信 backhaul / satellite connectivity | 运营中；2023 合同初始期至 2026-01，2026 年 NIRC 正在重谈服务级别/费用 | NIRC 2026-04-02 news + tabled report | A |
| Norfolk Telecom core / exchange / network office | Burnt Pine / Norfolk Telecom office（具体设施位置需 NIRC/NTL 文件确认） | 电信 core / exchange / internal equipment room | 运营中；容量未公开；非商业 DC | 2015 Mobile Network Review、NIRC Norfolk Telecom page | A（存在性）；设施细节需逐项核实 |
| O3b satellite earth-station/backhaul facilities | Norfolk Island | 卫星地球站 / telecom facility | 2014-2015 明确建设/运营；当前是否仍主用需以 NIRC/Telstra/NTL 复核 | ABC 2014、2015 Mobile Network Review | A/B 历史存在；当前状态需 A 级更新 |
| NIRC Power house / electricity reticulation | Norfolk Island（NIRC electricity system） | 公用电力设施 | 运营中；小型电网，柴油 + solar/battery 转型 | NIRC electricity pages、asset/tariff docs | A |
| Norfolk Island Data Services / `.nf` registry | Norfolk Island / registry layer | ccTLD registry / ISP/VoIP service | 运营中；不等于 DC | IANA `.nf`、NIDS official site | A（registry/ISP 存在性） |
| Gondwana-1 Norfolk landing claim | N/A | 误报/区域背景 | 不成立；未发现 NF landing A/B 证据 | Submarine Networks Gondwana-1 lists New Caledonia-Australia system | B/C 背景；不得入库 |
| SEO “Norfolk Island data center/VPS/dedicated server” pages | N/A | false positive | 排除 | 目录/营销页，无设施证据 | C |

## 5. 可靠性与排除规则 Reliability And Exclusion Rules

- `Norfolk Telecom`、`NIRC`、`Telstra satellite backhaul` 可证明电信服务和 backhaul；不能自动证明 colocation 或 datacenter。
- `Norfolk Island Data Services` 与 `.nf` 可证明 registry/ISP/VoIP/Internet service；不能自动证明本地 server hall。
- `Gondwana-1`、Sydney、Nouméa、Guam、Auckland、Australia/NZ cloud regions 是区域互联/后备市场背景；不得计入 NF inventory。
- 历史 `Pacific Cable Station`、Anson Bay telegraph/cable heritage 是历史通信设施；除非来源指向现代运营 telecom site，否则只作历史背景。
- 任何 candidate 若缺少以下至少三项中的两项，不能确立商业 DC：具名运营商、物理地点/地址、设施类型声明（data centre / colocation / racks / IT load）、运营状态、规划/电力证据。
- 对极小领地，阴性证据同样重要：记录已扫过的 official pages、tenders、cloud region pages 和目录误报，防止重复误判。
