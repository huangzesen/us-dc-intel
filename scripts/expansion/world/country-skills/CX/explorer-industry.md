# CX Explorer Industry（行业/厂商路径）— 圣诞岛数据中心枚举方法

日期：2026-08-12（已在线核验）。范围：澳大利亚海外领地圣诞岛（Christmas Island, CX；ISO 3166-1 alpha-2 = CX）。Manifest 分区（divisions）：`["Christmas Island"]`（单分区）。视角：**行业/运营商/厂商路径 industry/operator/vendor pipeline**。可靠性分级：A = 运营商/厂商/政府一手来源，B = 权威行业媒体/主流媒体，C = 目录/聚合/营销/社交传闻。

## 0. 行业判断（Market Reality）

**CX 是海缆登陆与边缘连接节点，不是已确认的商业数据中心市场。** 截至 2026-08-12，一手来源确认 Vocus ASC 已在 Christmas Island/Flying Fish Cove 登陆、CiFi 使用 ASC 提供本地互联网与 4G LTE、Telstra 提供 4G、Google 已宣布连接 Christmas Island 的 Bosun、interlink cable 与 Dhivaru 海缆。但一手来源尚未确认运营中的 CX colocation、cloud region、AI/HPC data centre 或 carrier hotel。

行业枚举要保持三层：

- **A 级已确认**：Vocus ASC landing / cable system；CiFi local ISP/fixed wireless/4G LTE；Telstra 4G mobile；Google official subsea cable projects。
- **B 级重点 lead**：Reuters/ABC/Guardian/DCD/Submarine Networks 关于 Google Christmas Island AI data centre/data hub 的报道；这些报道可触发 Shire minutes、planning、EPBC、AusTender、电力与 Google 官方检索。
- **C 级/负面**：data center directories、VPS/offshore hosting 营销、社交媒体转述、未给地址/运营商的“Christmas Island data center”页面。

结论写法：`no confirmed commercial datacenter; confirmed telecom/cable infrastructure; monitor Google data-centre lead`。

## 1. 行业结构事实（Industry Baseline）

- **Vocus（A）**：Vocus 官方确认 Australia Singapore Cable (ASC) 是 4,600 km、up to 60 Tbps、Perth-Singapore，经 Christmas Island 和 Indonesia，2018 年 9 月投入服务，由 Vocus 设计、建设并运营。URL：https://www.vocus.com.au/about-vocus/our-network/international/australia-singapore-cable
- **ASC landing（A/B）**：DITRDCA IOT bulletin 2018 说 cable landing station 正在 Flying Fish Cove Administration building 旁建设；ABC 2019 报道 Vocus staff inspected a new cable landing station on Christmas Island。官方优先，ABC 作为 B 级交叉。URLs：https://www.infrastructure.gov.au/territories-regions-cities/territories/indian_ocean/iot_bulletins/2018/A52-Reliable-high-speed-internet ，https://www.abc.net.au/news/2019-02-08/new-underwater-cable-gives-christmas-island-high-speed-internet/10666312
- **CiFi（A）**：CiFi 官方称其为 Christmas Island first and only fibre internet service provider，网络 exclusively supported by Vocus ASC subsea cable network，提供 home/business/4G mobile internet，办公室在 Settlement 与 Drumsite。URL：https://cifi.com.au/
- **Telstra（A/B）**：Parks Australia 官方旅行页确认 Telstra 4G GSM Mobile Telephone Service；ARN/Telecompaper 2022 报道 Vocus 与 Telstra 使用 ASC backhaul 升级 Christmas Island mobile connectivity、将 2G 升级为 4GX。官方旅行页为服务确认，行业媒体为项目背景。URL：https://christmasislandnationalpark.gov.au/plan/plan-your-trip/phone-internet-access/
- **nbn / satellite（A）**：DITRDCA 2024 Service Delivery kit 仍描述 NBN Sky Muster satellite service 与本地 broadband service；卫星服务是连接性，不是 data centre。URL：https://www.infrastructure.gov.au/sites/default/files/documents/service-delivery-arrangements-information-kit-indian-ocean-territories-november2024.pdf
- **Google cable systems（A）**：Google Cloud 官方宣布 Australia Connect：Bosun cable connects Darwin to Christmas Island, with onward connectivity to Singapore；另有 Melbourne-Perth-Christmas Island interlink cable。Google 还宣布 Dhivaru cable connects Maldives, Christmas Island and Oman。URLs：https://cloud.google.com/blog/products/infrastructure/bosun-australia-connect-initiative-for-indo-pacific-connectivity ，https://cloud.google.com/blog/products/networking/introducing-dhivaru-new-subsea-cable
- **EPBC referral（A）**：Australian EPBC public portal “Subsea Fibre Optic Data Cable Systems Installation - Australia West” 覆盖 Bosun cable system、Flying Fish Cove landing works，并提到 future cable system connecting Christmas Island onwards to Asia。URL：https://epbcpublicportal.environment.gov.au/all-referrals/project-referral-summary/?id=b532fd88-ca9d-f011-bbd2-002248115f4f
- **Google AI/data-centre lead（B/C）**：Reuters 2025 报道（经 ABC/Guardian/Capital Brief 等转载/跟进）称 Google 在 Christmas Island 筹划 AI data centre/data hub；同时有报道指出 Google 否认或淡化“data centre”说法，称项目属于 subsea cable/digital resilience work。缺少一手 data-centre approval 或 Google facility announcement 前，不能升级为 A。

## 2. 关键行业参与方（Operator/Vendor Register）

### 2.1 Vocus / ASC

用途：确认现有海缆、登陆点、容量、运营商、维护状态。

```text
site:vocus.com.au "Australia Singapore Cable" "Christmas Island"
site:vocus.com.au "Christmas Island" (landing OR "cable landing" OR "data centre" OR "data center")
"Australia Singapore Cable" "Flying Fish Cove" "landing station"
site:submarinecablemap.com "Australia-Singapore Cable" "Christmas Island"
```

计数：ASC/CLS = telecom infrastructure。若 Vocus 页面只提供 wholesale capacity，不代表岛上有商业 colocation。

### 2.2 CiFi

用途：确认本地 ISP、固定无线、4G LTE、ASC 回程和可能的 network room/PoP 线索。

```text
site:cifi.com.au "Christmas Island" ("4G" OR LTE OR "fixed wireless" OR "Vocus ASC" OR "carrier grade")
site:cifi.com.au ("data centre" OR "data center" OR hosting OR colocation OR "server")
"CiFi" "Christmas Island" (tower OR "network" OR PoP OR backhaul)
```

计数：CiFi 网络与办公室是运营商基础设施 lead；只有官方公开命名 server room/PoP/hosting 服务时才计入设施。

### 2.3 Telstra

用途：Telstra 4G/4GX、移动基站、ASC backhaul 项目、历史网络。

```text
site:telstra.com.au "Christmas Island" (4G OR 4GX OR mobile OR backhaul OR exchange)
"Vocus" "Telstra" "Christmas Island" "4GX"
"Telstra" "Christmas Island" ("data centre" OR "exchange" OR "backhaul")
```

计数：4G/4GX = mobile telecom infrastructure，不是 DC。仅运营商 exchange/server-room 一手证据可升级为 facility lead。

### 2.4 Google / Australia Connect / Dhivaru

用途：新海缆、landing infrastructure、可能的数据中心 lead。

```text
site:cloud.google.com "Christmas Island" "Bosun"
site:cloud.google.com "Christmas Island" "Dhivaru"
"Google" "Christmas Island" ("data centre" OR "data center" OR "data hub" OR AI) -Kiritimati
"Google" "Christmas Island" "Shire" "airport"
"Google" "Christmas Island" ("power" OR diesel OR renewable OR "phosphate")
```

计数：Google 官方 cable announcement = A 级 cable project。Google data centre = B/C lead，直到 Google 或政府审批明确“data centre/facility/site/IT load/power”。

### 2.5 PRL / Christmas Island Phosphates (CIP) / power

用途：矿业土地、电力、可能的数据中心能源/土地 lead。

```text
"Christmas Island Phosphates" (Google OR "data centre" OR "data center" OR power OR solar OR lease)
site:prlgroup.com.au "Christmas Island" (solar OR power OR Google OR data)
"Phosphate Hill" "Christmas Island" ("data centre" OR Google OR power OR ICT)
```

计数：矿业企业 IT/power 不计 DC；若与 Google data hub 的 land/power deal 被一手文件确认，则计 `planned/lead`。

### 2.6 Serco / Home Affairs / restricted government ICT

用途：North West Point detention centre ICT 合约。

```text
site:tenders.gov.au "Christmas Island" "North West Point" ICT
site:homeaffairs.gov.au "Christmas Island" (ICT OR "data centre" OR "data center" OR Serco)
"Serco" "Christmas Island" (ICT OR server OR "data centre")
```

计数：只记录公开合约/服务范围；不推断内部机房。

## 3. 行业媒体与目录（Media/Directory Register）

高价值 B 级：

- Data Center Dynamics：https://www.datacenterdynamics.com/ — Google cables/data-centre lead, cable context.
- ABC News：https://www.abc.net.au/ — Christmas Island cable landing、Google uncertainty/local impacts.
- Reuters（通过可信转载或 Reuters 页面）— Google data centre/data hub lead；需注意 Google 否认/淡化。
- Guardian / Capital Brief / The Australian / iTnews / ARN / Telecompaper — 项目与运营商交叉线索。
- Submarine Networks：https://www.submarinenetworks.com/ — Bosun、Dhivaru、ASC、Google data-centre rumors。作为行业二手，不能替代一手审批。
- TeleGeography Submarine Cable Map：https://www.submarinecablemap.com/submarine-cable/australia-singapore-cable-asc — landing-point map，B+ 线索。

目录 C 级负面：

```text
site:datacentermap.com "Christmas Island"
site:datacenters.com "Christmas Island"
site:cloudscene.com "Christmas Island" OR "Flying Fish Cove"
site:peeringdb.com "Christmas Island" OR "CX"
```

规则：目录缺席是弱负信号；目录出现也只是 C 级，必须找运营商、地址、许可或采购记录。

## 4. 行业查询模板（Industry Sweep）

通用数据中心/托管：

```text
"Christmas Island" Australia ("data centre" OR "data center" OR datacenter OR colocation OR "rack space" OR "carrier hotel") -Kiritimati -Kiribati
"Christmas Island" Australia ("AI data centre" OR "AI data center" OR "data hub" OR GPU OR HPC) Google -Kiritimati
"Flying Fish Cove" ("data centre" OR "data center" OR datacenter OR "cable landing" OR "landing station")
```

连接/海缆：

```text
"Christmas Island" (Vocus OR ASC OR "Australia Singapore Cable" OR "Bosun" OR Dhivaru OR "Australia Connect") -Kiritimati
"Christmas Island" "subsea cable" ("landing" OR "Flying Fish Cove" OR EPBC OR Vocus OR Google)
site:datacenterdynamics.com "Christmas Island"
site:submarinenetworks.com "Christmas Island" (Bosun OR Dhivaru OR "data center" OR "data centre")
```

本地运营商：

```text
"Christmas Island" (CiFi OR "Christmas Island Fibre Internet" OR Telstra OR 4GX OR "fixed wireless")
"Christmas Island" "Vocus ASC" CiFi
"Christmas Island" "Telstra 4G" "Vocus"
```

政府/审批二次核查：

```text
site:shire.gov.cx "Google" "Christmas Island"
site:shire.gov.cx ("data centre" OR "data center" OR "data hub" OR "cable")
site:epbcpublicportal.environment.gov.au "Christmas Island" "subsea"
site:tenders.gov.au "Christmas Island" (Google OR "data centre" OR "data center" OR ICT OR cable)
```

中文/SEO rumor watch（默认 C）：

```text
"圣诞岛" "数据中心" Google 澳大利亚 -基里巴斯
"Christmas Island" "AI 数据中心" OR "算力"
```

## 5. 枚举矩阵（Enumeration Matrix）

| 类别 | 状态 | 证据路径 | 等级 | 处理 |
|---|---|---|---|---|
| Vocus ASC cable landing station | operational | Vocus official + DITRDCA IOT bulletin + TeleGeography/ABC | A/B | 计 `telecom/cable landing infrastructure` |
| CiFi local ISP / fixed wireless / 4G LTE | operational | CiFi official + DITRDCA kit | A | 计 network operator lead；不计 colo |
| Telstra 4G/4GX | operational | Parks Australia + ARN/Telecompaper | A/B | 计 mobile telecom infrastructure；不计 DC |
| Google Bosun / interlink cable | planned/approval | Google official + EPBC + DCD | A/B | 计 planned cable/landing project |
| Google Dhivaru | planned | Google official | A | 计 planned subsea cable connectivity |
| Google AI data centre/data hub | unconfirmed lead | Reuters/ABC/Guardian/Capital Brief + Shire minutes search | B/C | 不计 confirmed；需一手审批/公告 |
| Government/Shire server rooms | likely small lead | DITRDCA/Shire/AusTender | A lead | 仅命名项目时计 lead |
| PRL/CIP enterprise IT/power | lead | PRL/CIP/Shire/media | B/C | 不计 DC，除非命名 facility |
| North West Point detention ICT | restricted lead | Home Affairs/AusTender/Serco | A/B lead | 只记录合约层面 |
| Commercial colo/cloud region | no confirmed projects | cloud official pages + directories | A/C negative | verified-negative |

## 6. 候选记录模板（Required Fields）

```text
country_code: CX
division: Christmas Island
sub_location: Flying Fish Cove | Settlement | Drumsite | Phosphate Hill | Airport | North West Point | Unknown CX
facility_or_project_name:
operator: Vocus | CiFi | Telstra | Google | Australian Government (IOT) | Shire of Christmas Island | PRL/CIP | Serco/Home Affairs | other
facility_type: cable landing station | planned subsea landing | ISP PoP | mobile backhaul | government server room | enterprise server room | colocation | cloud region | AI/HPC data centre | other
status: operational | planned | under construction | approval/referral | lead | verified-negative
capacity_or_scale: Tbps/Gbps/MW/racks/unknown
connectivity: Vocus ASC | Google Bosun | Google Dhivaru | Telstra 4G/4GX | CiFi fixed wireless/4G | nbn Sky Muster | unknown
power: IOT Power Service isolated grid | dedicated generation | solar/BESS | unknown
evidence_grade: A | B | C
primary_urls:
secondary_urls:
site_address:
coordinates:
notes:
last_checked: 2026-08-12
```

升级标准：

- A：运营商/厂商/政府官方页面或审批文件明确设施、地点、功能。
- B：行业媒体或主流媒体点名文件、官员、公司回应，但缺少公开一手审批。
- C：目录、SEO、社交媒体、无来源转载；只作为搜索词，不计设施。

## 7. 误报与可靠性规则（False Positives）

- **Kiritimati**：所有搜索加 Australia / Indian Ocean / CX 或 `-Kiritimati -Kiribati`。
- **Cable != DC**：Vocus ASC、Google Bosun/Dhivaru 是 connectivity。登陆站可计电信基础设施，不能自动计商业 DC。
- **Google rumor handling**：Reuters/ABC/Guardian/DCD lead 值得追踪；Google 官方和 EPBC 当前只确认 cable work。无 Shire development approval/Google facility announcement 前不能列为 confirmed data centre。
- **CiFi/Telstra/nbn**：4G、fixed wireless、Sky Muster、Wi-Fi hotspot、基站、运营商办公室都不是 colocation。
- **Power**：IOT Power Service、diesel/solar/BESS、PRL/CIP energy plans 是可行性证据，不是 DC 证据。
- **Cloud regions**：AWS/Azure/GCP/OCI 官方区域页无 CX；澳大利亚大陆区域不覆盖圣诞岛本地设施。
- **Directories**：DatacenterMap/Cloudscene 等即使出现 Christmas Island 条目也必须降为 C，直至有地址、运营商和一手来源。

## 8. 推荐扫描顺序（Recommended Sweep）

1. Vocus ASC + Flying Fish Cove landing station。
2. CiFi + Telstra + nbn/Sky Muster，确认运营商网络但避免误计。
3. Google official cables + EPBC referral。
4. Google AI/data-centre lead：Reuters/ABC/DCD/Guardian/Capital Brief → Shire minutes/planning → AusTender/EPBC/Home Affairs/Defence/Google official。
5. PRL/CIP 与 IOT Power Service，核查土地/电力线索。
6. 云区域和商业托管负面检查。
7. 输出时分开写 `confirmed telecom infrastructure`、`unconfirmed data-centre lead`、`verified-negative commercial DC/cloud/colo`。
