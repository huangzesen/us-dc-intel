# NU Explorer Official（官方/监管源）- Niue 数据中心枚举方法

# NU Explorer Official - Niue Datacenter Enumeration via Official / Regulatory Sources

日期 Date: 2026-08-12. 范围 Scope: 纽埃 Niue（NU）。Manifest 已核验 verified manifest entry: `{"country_code":"NU","country_name":"Niue","subnational_type":"country","divisions":["Niue"]}`. 因此本方法只覆盖一个分区：`Niue`（整岛 / whole island）。

可靠性分级 Reliability grades: **A** = 政府、监管、国有企业、官方公司注册处、官方云区域页、官方项目/采购/法律文件、IANA 等主源；**B** = 具名、可追溯日期的区域媒体、行业媒体、承包商案例、多边项目页；**C** = 目录、地图、PeeringDB/ASN 聚合、社交页、SEO 托管页、市场报告摘要。C 级只作线索或负向控制，不得单独确立设施存在。

## 0. 已核验国家基线 Verified Country Baseline

- 纽埃在 manifest 中是单一国家级分区；枚举输出不得拆出省/州级行政分区。村庄名只用于地理定位和误报排查。Niue is a single-division country record for this workflow.
- 公开资料未显示纽埃有数据中心专属监管登记册、DC 牌照类别或在线建设许可检索门户。数据中心发现应从政府项目、电信、能源、公司注册和官方云区域缺失核验入手。
- 设施级通信资产集中在 Alofi / 阿洛菲：Telecom Niue、政府网络、Manatua 海缆登陆相关设施。其他村庄通常只应出现基站、光缆、配电、公共服务 ICT 室或可再生能源资产。
- Manatua 是纽埃关键连接性资产。SubCom 2018 合同公告确认 Manatua 联合体包括 OPT、Avaroa Cable、Telecom Niue、SSCC，并描述 Apia-Toahotu 主线及至 Niue、Aitutaki、Rarotonga、Bora Bora 的登陆/分支。Submarine Networks 记录 Manatua 连接 Samoa、Niue、Cook Islands、French Polynesia，且是 Niue 和 Cook Islands 的首次光纤连接。
- 2026-08 纽埃政府发布 Manatua 故障通报，说明修复由 Manatua Cable partners 协调，Government of Niue 与 Telecom Niue 持续监控。这是 Manatua 当前运营相关性的 A 级政府证据。
- Tui-Samoa 不在纽埃登陆。ADB 项目 47320-001 和 SSCC/Tui-Samoa 资料指向 Samoa-Fiji/Wallis & Futuna/Savai'i 路由；检索到 "Tui Samoa + Niue" 时按区域混淆处理，除非出现 A 级纽埃登陆证据。
- 官方政府项目页显示 Niue Renewable Energy 位于 Hikufenoga, Tamakautoga / near airport，含 2.79 MWp PV、8.19 MWh BESS、电网升级，目标 2026 年 7 月/年中完成后由 Department of Utilities 与 Niue Power Corporation 接收。它是能源上下文，不是数据中心证据。
- 官方 Starlink 状态已更新：2026-05-12 纽埃政府批准 Starlink/SpaceX 12 个月临时 Spectrum and Internet Communications Licence。Starlink 是连接性服务，不是数据中心。
- IANA .NU 委派记录确认 ccTLD manager 为 The IUSN Foundation（Alofi），technical contact 为 The Internet Infrastructure Foundation（Sweden），registration services URL 为 Internetstiftelsen。该记录支持域名基础设施叙事，但不证明纽埃本地数据中心。
- 官方公司注册处为 **Niue Companies Office** `https://www.companies.gov.nu/`。该网站称 Companies Register of Niue 是面向公众的电子注册簿。注册命中只证明法律实体存在。
- 未发现 AWS、Microsoft Azure、Google Cloud、Oracle OCI 在纽埃设有官方公共云区域、Local Zone 或自有数据中心；此结论只能用厂商官方区域页定期复核。

## 1. 官方源优先级 Official Source Priority

### 1.1 政府与法律 Government, Gazette, Legislation

主源 Primary sources:

- Government of Niue: `https://www.gov.nu/`
- Gazette Notices / Notice Board / Media Releases / Projects: 从 gov.nu 导航进入
- Ministry of Finance: `https://mof.gov.nu/`
- Niue ICT quick link: `https://ictniue.nu/`（由 gov.nu quick links 暴露，使用前复核）
- Legislation volumes and supplements: gov.nu Information -> Legislation

用途 Use: 查政府 ICT、数字化、招标、网络、能源、海缆、Starlink 许可、机构职责。政府文件是 A 级项目/监管证据；媒体转述只是 B/C。

```text
site:gov.nu ("data center" OR "data centre" OR datacenter OR "server room" OR server OR hosting OR "e-government" OR digitization OR ICT)
site:gov.nu (tender OR procurement OR RFQ OR RFP OR contract OR award) (ICT OR fibre OR fiber OR cable OR power OR solar OR "data")
site:gov.nu ("Telecom Niue" OR telecommunications OR Starlink OR SpaceX OR spectrum OR licence OR license)
site:gov.nu ("Manatua" OR "submarine cable" OR "landing station" OR "cable fault" OR connectivity)
site:gov.nu ("Niue Power Corporation" OR NPC OR "Department of Utilities" OR BESS OR "battery energy storage" OR "solar farm")
site:mof.gov.nu (budget OR procurement OR ICT OR telecommunications OR energy OR infrastructure)
```

### 1.2 电信与监管 Telecom And Communications

主源 Primary sources:

- Telecom Niue: `https://telecomniue.com/`
- Telecom Niue notices/events: `https://telecomniue.com/support/notices-events/`
- Telecom Niue terms: `https://telecomniue.com/promotions/terms-conditions/`
- Government of Niue Telecom Niue notice board: `https://www.gov.nu/notice-board/telecom-niue`
- Starlink licence release: `https://www.gov.nu/media-releases/government-of-niue-strengthens-national-connectivity-with-temporary-starlink-license`
- PaCSON Telecom Niue profile: `https://pacson.org/node/173`（B/A-adjacent supporting source for SOE status; do not use alone for facilities）

已核验 facts to carry:

- Telecom Niue 官方站有 Personal、Business、Fibre、4G Wireless、ADSL、ICT Services 等导航；未在本次核验中发现公开 colocation / rack hosting / data centre 服务页。
- Telecom Niue 的政府数字化活动页称其作为 project manager，协助各政府部门迁移到新网络；这是政府网络项目线索，不是 DC 设施证据。
- 2026 政府 Starlink 许可页同时称 Telecom Niue 继续升级岛内 fibre-optic network，并在 Alofi、Tuapa 部署新网络站点；这些是通信基础设施，不等于数据中心。

```text
site:telecomniue.com (business OR enterprise OR "ICT Services" OR hosting OR server OR cloud OR NOC OR switch OR colocation OR "data centre" OR "data center")
site:telecomniue.com (Manatua OR cable OR fibre OR fiber OR broadband OR "network site" OR repeater OR Alofi OR Tuapa)
"Telecom Niue" ("data centre" OR "data center" OR colocation OR hosting OR "server room" OR "computer room" OR gateway OR NOC)
"Telecom Niue" (government OR "100%" OR shareholder OR corporatisation OR SOE OR "state owned")
"Starlink" "Niue" (license OR licence OR spectrum OR SpaceX OR "temporary")
```

### 1.3 电力 Power And Utility Load Checks

主源 Primary sources:

- Government Niue Renewable Energy Phase 1: `https://www.gov.nu/projects/niue-renewable-energy`
- Government Niue Renewable Energy Phase 3: `https://www.gov.nu/projects/niue-renewable-energy-phase-3`
- Government Department of Utilities notice board: `https://gov.nu/notice-board/department-of-utilities`
- SPC / PCREEE / PRDR load and project records: `https://www.pcreee.org/`, `https://prdrse4all.spc.int/`
- Pacific Power Association: `https://www.ppa.org.fj/`
- MFAT Niue page and IATI data: `https://www.mfat.govt.nz/en/countries-and-regions/australia-and-pacific/niue`, `https://devdata.mfat.govt.nz/`

记录规则 Record rule: 能源项目只能支持电力可得性或负荷合理性核查。任何 >0.5 MW 数据中心或大型服务器负荷声称，必须有 NPC / Department of Utilities / gov.nu / funder 文件支持；没有电力侧痕迹时默认不可信。

```text
"Niue Power Corporation" OR "Department of Utilities" (load OR demand OR grid OR diesel OR generator OR substation OR outage)
site:gov.nu ("Niue Renewable Energy" OR BESS OR "battery energy storage" OR "solar farm" OR Hikufenoga OR Tamakautoga)
"Niue" (MW OR MWp OR MWh OR "peak load" OR "peak demand") (NPC OR "Niue Power Corporation" OR gov.nu OR SPC OR PPA)
site:mfat.govt.nz Niue (energy OR solar OR BESS OR grid OR electricity OR infrastructure)
site:prdrse4all.spc.int Niue ("Niue Power Corporation" OR load OR solar OR battery)
```

### 1.4 海缆登陆 Cable Landing: Manatua, Not Tui-Samoa

主源和高可信源 Primary and high-confidence sources:

- SubCom Manatua contract-in-force PDF: `https://www.subcom.com/documents/Manatua-CIF-SubCom-final-19NOV2018.pdf`
- SubCom / Manatua cable lay complete PDF: `https://www.subcom.com/documents/2020/Manatua_Consortium_Confirms_Cable_Lay_Ops_Complete-FINAL-APPROVED_FOR_RELEASE-17FEB2020.pdf`
- Government of Niue Manatua fault update: `https://www.gov.nu/media-releases/government-updates-public-on-the-internet-service-disruption`
- Submarine Networks Manatua profile: `https://www.submarinenetworks.com/en/systems/australia-usa/manatua`（B）
- ADB Samoa Submarine Cable Project 47320-001: `https://www.adb.org/projects/47320-001/main`（Tui-Samoa 背景 / false-positive control）
- SSCC: `https://www.ssccsamoa.com/`（Tui-Samoa/Samoa-side context）

记录规则 Record rule: Manatua Alofi 登陆站记录为 `telecom_cable_station`。只有 Telecom Niue / Manatua consortium / RIO / FAA / official facility-access 文件明确支持客户设备接入、互连、托管或类托管服务时，才升级为 `colo_adjacent_telecom`。

```text
"Manatua" Niue (Alofi OR landing OR "landing station" OR "cable station" OR "ready for service" OR RFS OR fault OR repair)
"Manatua" ("Telecom Niue" OR "Avaroa Cable" OR OPT OR SSCC OR SubCom) (consortium OR cable OR landing OR capacity)
site:subcom.com Manatua Niue
site:gov.nu Manatua (fault OR cable OR landing OR Telecom)
"Tui Samoa" OR "Tui-Samoa" Niue (landing OR spur OR branch)  # false-positive control
site:adb.org "Samoa Submarine Cable Project" "47320-001"
site:adb.org "Tui-Samoa"
```

### 1.5 公司注册 Company / Entity Verification

主源 Primary source:

- Niue Companies Office: `https://www.companies.gov.nu/`

用途 Use: 核实 Telecom Niue、Niue Power Corporation、IUSN、Starlink 本地许可实体/代理、承包商或项目 SPV 的法律名称。注册处证据为 A 级法律存在证据，但不是设施证据。

```text
site:companies.gov.nu ("Telecom Niue" OR "Niue Power" OR "IUSN" OR "Internet Users Society" OR Starlink OR SpaceX)
"Niue Companies Office" ("Telecom Niue" OR "Niue Power Corporation" OR IUSN OR Starlink)
"Registrar of Companies" Niue (telecom OR power OR ICT OR hosting OR "data")
```

### 1.6 .nu / IUSN / DNS Infrastructure

主源 Primary sources:

- IANA .NU delegation: `https://www.iana.org/domains/root/db/nu.html`
- IUSN Foundation: `https://iusn.org/`
- Internet Niue: `https://internetniue.nu/`
- Internetstiftelsen registry information: `https://www.internetstiftelsen.se/`

记录规则 Record rule: .nu ccTLD、DNS、Wi-Fi funding 和域名争议是连接性/数字经济背景。IANA 明确技术联系在瑞典，不支持本地 DC 结论。即使发现本地 DNS/server 设备，也按 `dns_registry_infrastructure` 或 `public_wifi_infrastructure` 处理，不计商业数据中心。

```text
"IUSN" OR "Internet Users Society" Niue (registry OR ".nu" OR DNS OR server OR infrastructure OR WiFi OR "free internet")
site:iana.org/domains/root/db/nu
site:iusn.org Niue (server OR DNS OR registry OR internet OR WiFi)
site:internetniue.nu Niue (network OR WiFi OR server OR infrastructure)
```

### 1.7 官方云区域缺失性核验 Cloud Region Absence

只使用厂商官方页面做 A 级缺失性结论。

| Provider | Official URL | NU result |
|---|---|---|
| AWS Regions | `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/` | No NU region found |
| AWS Local Zones | `https://aws.amazon.com/about-aws/global-infrastructure/localzones/` | No NU Local Zone found |
| Microsoft Azure | `https://learn.microsoft.com/en-us/azure/reliability/regions-list` | No NU region found |
| Google Cloud | `https://cloud.google.com/about/locations`; `https://datacenters.google/locations/` | No NU region / Google-owned DC found |
| Oracle OCI | `https://www.oracle.com/cloud/public-cloud-regions/` | No NU region found |

```text
"Niue" ("AWS Region" OR "AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR hyperscale)
"Niue" ("cloud region" OR "sovereign cloud" OR "data residency" OR "public cloud")
```

## 2. Division Coverage And Village Strategy

Manifest coverage is complete when the output contains exactly one division key: `Niue`.

村庄级检索只用于定位：Alofi / Alofi North / Alofi South, Avatele, Hakupu, Vaiea, Liku, Lakepa, Mutalau, Namukulu, Hikutavake, Toi, Tuapa, Makefu, Tamakautoga. Alofi is the only expected facility-grade hub. Tuapa may appear in 2026 network-site work. Hikufenoga/Tamakautoga appears for the renewable-energy project near the airport.

```text
"Niue" ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR "server room" OR "cable station" OR "landing station")
"Alofi" Niue (server OR hosting OR "data centre" OR "data center" OR NOC OR switch OR fibre OR cable OR colocation)
"{Village}" Niue ("data center" OR "data centre" OR server OR hosting OR fibre OR broadband OR ICT OR power OR solar)
```

For all non-Alofi village hits, default to `no_projects` unless an A/B source names a physical facility relevant to telecom, energy, government ICT, or cable landing.

## 3. 当前官方种子清单 Current Official Seed List

| Candidate | Location | Evidence grade | Record as | Notes |
|---|---|---:|---|---|
| Manatua / Alofi cable landing facility | Alofi / Niue | A for cable project and government operational relevance; B for public cable database details | `telecom_cable_station` | Do not count as DC or colo without facility-access / interconnect evidence. |
| Telecom Niue core network and government network services | Alofi-focused, island-wide access network | A for operator/services; facility details currently unproven | `telecom_network_lead` | Business ICT/fibre services exist; no public colo page verified. |
| Starlink temporary licensed service | Island-wide | A for 2026 government licence | `connectivity_service` | Satellite service; not DC. |
| Niue Renewable Energy PV/BESS | Hikufenoga, Tamakautoga / near airport | A | `power_context` | 2.79 MWp PV, 8.19 MWh BESS; supports load plausibility only. |
| .NU / IUSN / Internetstiftelsen | Alofi admin contact; Sweden technical contact | A for DNS delegation | `dns_registry_context` | Not DC evidence; beware overseas registry infrastructure. |
| AWS/Azure/GCP/OCI public cloud regions | None in NU | A negative | `cloud_absence` | Recheck official region pages on each refresh. |

## 4. False Positives And Honest Grading

- 海缆登陆站不等于数据中心。Cable landing station != datacenter.
- 电信运营商存在、ICT service、fibre、4G site、network site、repeater 不等于 colocation。
- Starlink、Kacific、SES、Intelsat 等卫星/批发容量是连接性资产，不是本地数据中心。
- .nu 域名、DNS、Wi-Fi nation 故事不是数据中心；IANA 当前记录显示技术联系在 Sweden。
- 海外 "Niue VPS", "Alofi dedicated server", "Niue cloud hosting" SEO 页面默认 C 级；没有纽埃本地地址、运营商主源或公司注册锚定时不建证。
- Tui-Samoa、SSCC、Apia、Tuasivi、SamoaTel、Digicel Samoa、Vodafone Samoa 属萨摩亚/Fiji/Wallis regional context，不得计入 NU。
- 任何大型电力或容量声称必须能解释在纽埃小岛电网中的负荷来源，并由 NPC / gov.nu / MFAT / SPC 主源支持。

## 5. Refresh Checklist

1. Confirm manifest still says `divisions:["Niue"]`.
2. Re-run gov.nu searches for ICT, Telecom Niue, Starlink, Manatua, procurement, energy.
3. Re-run Telecom Niue site searches for hosting, data centre, ICT services, NOC, fibre, Manatua.
4. Recheck Niue Companies Office at `companies.gov.nu`.
5. Recheck IANA .NU delegation and IUSN/Internet Niue pages.
6. Recheck Manatua and Tui-Samoa route evidence via SubCom/ADB/SSCC/Submarine Networks.
7. Recheck AWS/Azure/GCP/OCI official region pages.
8. Confirm every output record maps to the single division `Niue`.
