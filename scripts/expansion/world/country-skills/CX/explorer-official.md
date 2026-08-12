# CX Explorer Official（官方/监管路径）— 圣诞岛数据中心枚举方法

日期：2026-08-12（已在线核验）。范围：澳大利亚海外领地圣诞岛（Christmas Island, CX；ISO 3166-1 alpha-2 = CX）。Manifest 分区（divisions）：`["Christmas Island"]`；subnational_type = `country`，因此清单层面只有一个分区。视角：**官方/监管路径 official/regulatory pipeline**。可靠性分级：A = 官方/一手来源，B = 强二手/行业媒体，C = 目录/聚合/营销/传闻类证据。

## 0. 市场判断（Market Judgment）

**截至 2026-08-12，公开一手来源未确认 CX 存在运营中的商业 colocation、云区域、超大规模或 AI/HPC 数据中心。** 但 CX 已不是“仅卫星连接”的空白市场：Vocus 的 Australia Singapore Cable（ASC）已在 Flying Fish Cove 登陆，CiFi 使用 ASC 提供本地宽带/4G LTE，Telstra 提供 4G 移动服务，Google 已宣布多条与 Christmas Island 相关的新海缆。正确枚举结论应区分：

- **已确认电信设施（A）**：Vocus ASC 圣诞岛登陆/landing station、Telstra 4G、CiFi 本地固定无线/4G LTE 与 ASC 回程。
- **规划/审批中的电信基础设施（A/B）**：Google Australia Connect 的 Bosun 与 interlink cable；Google Dhivaru；EPBC referral 中的 Flying Fish Cove cable landing works。
- **未确认数据中心（B/C lead）**：Reuters/ABC/Guardian 等关于 Google 在圣诞岛建设 AI data centre/data hub 的报道与郡议会记录线索。Google 对部分报道有否认/淡化表述；未见同等强度的一手政府批准、Google 数据中心公告、AusTender 或电力接入批准。因此只能作为 `lead`，不能计为已确认 facility。
- **仍为负面（A/B/C）**：无 AWS/Azure/GCP/OCI 官方 CX cloud region；无公开商业托管目录证据；普通服务器房、基站、卫星终端、电缆登陆站本身不等于商业数据中心。

官方枚举目标是找出：电缆登陆站/landing infrastructure、政府或运营商服务器机房、可公开许可的 AI/data-centre 项目，以及全分区 verified-negative 结论。

## 1. 结构事实（Ground Truth）

- **治理 Governance（A）**：圣诞岛与科科斯（基林）群岛合称 Indian Ocean Territories (IOT)。澳大利亚政府通过 Department of Infrastructure, Transport, Regional Development, Communications, Sport and the Arts 负责该海外领地，并通过服务交付安排提供类似州政府的服务。官方入口：https://www.infrastructure.gov.au/territories-regions/territories/indian-ocean-territories-christmas-island-and-cocos-keeling-islands
- **人口 Population（A）**：DITRDCA/ABS census data 显示 2021 年 Christmas Island 总人口为 1,692。来源：https://www.infrastructure.gov.au/territories-regions/territories/indian-ocean-territories-christmas-island-and-cocos-keeling-islands/christmas-island/christmas-island-census-data
- **地方政府 Shire（A）**：Shire of Christmas Island 官网真实可用，含 public notices、annual reports、planning/building、council meetings 等栏目。入口：https://www.shire.gov.cx/
- **电信 Telecom（A/B）**：DITRDCA 2024 Service Delivery Arrangements kit 仍描述 NBN Sky Muster satellite service、本地 broadband service、Vocus spur line 与 CiFi internet distributor；同一文件列出 IOT Administration、IOT Power Service 和 Shire 联系地址。来源：https://www.infrastructure.gov.au/sites/default/files/documents/service-delivery-arrangements-information-kit-indian-ocean-territories-november2024.pdf
- **现有海缆 Existing subsea cable（A）**：Vocus 官方 ASC 页面确认 ASC 于 2018 年 9 月投入服务，4,600 km，Perth-Singapore，经 Christmas Island 和 Indonesia，容量 up to 60 Tbps，由 Vocus 设计、建设并运营。来源：https://www.vocus.com.au/about-vocus/our-network/international/australia-singapore-cable
- **登陆站位置 CLS location（A/B）**：IOT bulletin 2018 称 Vocus 已铺设从 ASC 分出的 Christmas Island cable extension，cable landing station 在 Flying Fish Cove 的 Administration building 旁建设。来源：https://www.infrastructure.gov.au/territories-regions-cities/territories/indian_ocean/iot_bulletins/2018/A52-Reliable-high-speed-internet
- **本地接入 Local access（A）**：CiFi 官方称其为 Christmas Island first and only fibre internet service provider，网络由 Vocus ASC subsea cable network 支撑，并在 Settlement 与 Drumsite 设办公室。来源：https://cifi.com.au/
- **移动 Mobile（A）**：Parks Australia/Christmas Island National Park 官方旅行信息确认岛上有 Telstra 4G GSM Mobile Telephone Service。来源：https://christmasislandnationalpark.gov.au/plan/plan-your-trip/phone-internet-access/
- **电力 Power（A）**：DITRDCA 2024 kit 列出 Indian Ocean Territories Power Service，Power Services Manager 地址为 11-13 Quarry Road, Phosphate Hill。IOT bulletin 2020 确认 IOT Power Service 正在改变 Christmas Island 与 Cocos 的可再生能源接入规则。来源：https://www.infrastructure.gov.au/territories-regions-cities/territories/indian_ocean/iot_bulletins/2020/A025-2020-renewed-solar-opportunities
- **规划环境审批 Environment/planning（A）**：EPBC public portal 存在 “Subsea Fibre Optic Data Cable Systems Installation - Australia West” referral，范围包括 Bosun cable system connecting Christmas Island to Darwin，以及 Madora Bay、Flying Fish Cove、Darwin 等 landing works；还提到未来连接 Christmas Island onwards to Asia 的 cable system。来源：https://epbcpublicportal.environment.gov.au/all-referrals/project-referral-summary/?id=b532fd88-ca9d-f011-bbd2-002248115f4f

## 2. A 级官方/监管来源（Official Source Register）

### 2.1 DITRDCA / Indian Ocean Territories

- IOT 入口：https://www.infrastructure.gov.au/territories-regions/territories/indian-ocean-territories-christmas-island-and-cocos-keeling-islands
- Service Delivery Arrangements kit：https://www.infrastructure.gov.au/sites/default/files/documents/service-delivery-arrangements-information-kit-indian-ocean-territories-november2024.pdf
- IOT bulletins / media releases：用 `site:infrastructure.gov.au/territories-regions-cities/territories/indian_ocean/iot_bulletins Christmas Island` 搜索历史项目。

查询模板：

```text
site:infrastructure.gov.au "Christmas Island" ("data centre" OR "data center" OR server OR ICT OR "subsea cable" OR "landing station")
site:infrastructure.gov.au "Christmas Island" "Vocus" "cable landing station"
site:infrastructure.gov.au "Indian Ocean Territories" ("Power Service" OR electricity OR solar OR telecommunications)
```

提取：IOT governance、service arrangements、IOT Power Service、政府 ICT、海缆登陆站、预算/项目状态。注意部门名称会随内阁组合变化，URL 路径也可能保留旧 `territories-regions-cities`。

### 2.2 Shire of Christmas Island / WA planning

- Shire 官网：https://www.shire.gov.cx/
- Annual reports：https://www.shire.gov.cx/annual-reports
- WA planning information：https://www.wa.gov.au/government/document-collections/shire-of-christmas-island-planning-information

查询模板：

```text
site:shire.gov.cx "data centre" OR "data center" OR "Google"
site:shire.gov.cx ("planning approval" OR "building approval" OR "development application") ("Christmas Island" OR Google OR cable OR telecommunications)
site:shire.gov.cx ("server" OR ICT OR IT OR "cyber" OR "network")
site:wa.gov.au "Shire of Christmas Island" ("local planning scheme" OR "structure plan")
```

提取：任何 Google/data hub 土地租赁、airport area、light industrial area、Phosphate Hill、Flying Fish Cove/Fish Cove、building approval、council minutes。Shire 会议记录是数据中心传闻的关键核查入口；没有审批/会议记录时不得从媒体报道升级。

### 2.3 Vocus ASC / cable landing

- Vocus ASC 官方：https://www.vocus.com.au/about-vocus/our-network/international/australia-singapore-cable
- IOT bulletin 2018 landing-station 线索：https://www.infrastructure.gov.au/territories-regions-cities/territories/indian_ocean/iot_bulletins/2018/A52-Reliable-high-speed-internet
- TeleGeography map（B+ 线索）：https://www.submarinecablemap.com/submarine-cable/australia-singapore-cable-asc

查询模板：

```text
site:vocus.com.au "Christmas Island" "Australia Singapore Cable"
"Flying Fish Cove" "cable landing station" "Christmas Island"
"Australia Singapore Cable" "Flying Fish Cove" Vocus
```

计数规则：ASC landing station 是 `telecom/cable landing infrastructure`，不是 colocation，除非 Vocus/CiFi/政府明确公开机架托管或互联服务。

### 2.4 Google / EPBC / Australia Connect

- Google Australia Connect / Bosun 官方：https://cloud.google.com/blog/products/infrastructure/bosun-australia-connect-initiative-for-indo-pacific-connectivity
- Google Dhivaru 官方：https://cloud.google.com/blog/products/networking/introducing-dhivaru-new-subsea-cable
- EPBC referral：https://epbcpublicportal.environment.gov.au/all-referrals/project-referral-summary/?id=b532fd88-ca9d-f011-bbd2-002248115f4f

查询模板：

```text
site:cloud.google.com "Christmas Island" "Bosun"
site:cloud.google.com "Christmas Island" "Dhivaru"
site:epbcpublicportal.environment.gov.au "Christmas Island" "Flying Fish Cove" "subsea"
"Christmas Island" "Google" ("data centre" OR "data center" OR "data hub") site:shire.gov.cx
```

规则：Google 官方目前核实的是海缆/连接项目，不是 CX 数据中心。EPBC referral 也核实 cable systems and landings，不等于 data centre approval。媒体所称 Google AI/data hub 必须等待 Google 官方、澳政府审批、Shire planning approval 或电力/土地文件交叉确认。

### 2.5 Telstra / CiFi / nbn / ACMA

- CiFi 官方：https://cifi.com.au/
- Telstra 4G 官方旅行/政府确认：https://christmasislandnationalpark.gov.au/plan/plan-your-trip/phone-internet-access/
- nbn：https://www.nbnco.com.au/
- ACMA：https://www.acma.gov.au/

查询模板：

```text
site:cifi.com.au "Christmas Island" ("data centre" OR "data center" OR hosting OR colocation OR "carrier grade")
site:telstra.com.au "Christmas Island" (4G OR 4GX OR "data centre" OR exchange OR backhaul)
site:nbnco.com.au "Christmas Island" ("Sky Muster" OR satellite OR outage OR "data centre")
site:acma.gov.au "Christmas Island" (carrier OR licence OR spectrum OR radiocommunications)
```

规则：CiFi/Telstra/nbn 网络设施只按电信设施或 server-room lead 记录；零售宽带、4G 基站、Wi-Fi hotspot 和卫星终端不计为数据中心。

### 2.6 AusTender / budget / Home Affairs / power

- AusTender：https://www.tenders.gov.au/
- Budget：https://budget.gov.au/
- Home Affairs：https://www.homeaffairs.gov.au/
- IOT Power Service bulletin：https://www.infrastructure.gov.au/territories-regions-cities/territories/indian_ocean/iot_bulletins/2020/A025-2020-renewed-solar-opportunities

查询模板：

```text
site:tenders.gov.au "Christmas Island" (ICT OR "data centre" OR "data center" OR server OR cable OR satellite OR power OR Google)
site:budget.gov.au "Christmas Island" ("subsea cable" OR "data centre" OR "digital" OR telecommunications)
site:homeaffairs.gov.au "Christmas Island" (ICT OR "North West Point" OR detention OR Serco)
"Christmas Island" "IOT Power Service" (capacity OR generator OR solar OR battery OR "data centre")
```

提取：政府 ICT、拘留中心合约、电力升级、海缆建设、土地/机场/安全项目。拘留中心 ICT 公开性受限；只记录合约层面的 ICT lead。

### 2.7 云厂商官方区域页（Verified Negative）

| 厂商 | 官方页面 | CX 状态 |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | 无 CX region/local zone |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | 无 CX region |
| Google Cloud | https://cloud.google.com/about/locations | 无 CX cloud region；Google CX 官方来源仅确认 subsea cables |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | 无 CX region |

## 3. 分区枚举流程（Per-Division Workflow）

Manifest divisions：**`["Christmas Island"]`**。清单层面不得拆成多个 division；可在 `sub_location` 中标注地点。

| sub_location | 优先级 | 预期产出 | 官方路径 | 计数规则 |
|---|---:|---|---|---|
| Flying Fish Cove / Settlement | High | ASC landing station；Google cable landing works；政府/港口/运营商设施 | DITRDCA bulletin、Vocus、EPBC、Shire planning | 电缆登陆站计 telecom facility；无托管产品不得计 colo |
| Kampong / Jalan Pantai | Medium | IOT Administration / Office of Administrator ICT lead | DITRDCA Service Delivery kit、AusTender | 只在采购/文件命名机房时计 lead |
| Phosphate Hill / Quarry Road | High | IOT Power Service；CIP/PRL；可能 data hub power/land lead | DITRDCA kit、IOT Power Service、Shire、PRL/CIP、EPBC | 电力设施不计 DC；若 Google power lease 有一手文件则升级 lead |
| Drumsite | Medium | CiFi office/local network lead；小型商业/住宅 | CiFi、Shire planning | 网络办公室/基站不计 DC |
| Silver City / Poon Saan / Kampong residential | Low | verified-negative | Shire planning + broad web | 无证据则 no_projects |
| North West Point | Medium/Restricted | detention centre ICT contracts | Home Affairs、AusTender、Serco | 只记合约层面，不枚举内部机房 |
| Airport / XCH / YPXM | High for rumors | Google reported land/data hub lead; airport comms | Shire minutes/planning、EPBC、AusTender、Google official | 媒体报道仅 B/C lead；需一手审批或公司公告 |
| Phosphate mine / PRL / CIP | Medium | enterprise IT/power lead | PRL/CIP official、Shire、EPBC | 企业 IT 机房通常不计，除非专用 facility 公开命名 |

通用模板：

```text
"{Place}" "Christmas Island" Australia ("data centre" OR "data center" OR "server room" OR server OR telecom OR "cable landing" OR Google)
"{Place}" "Christmas Island" (Vocus OR CiFi OR Telstra OR "Bosun" OR Dhivaru OR "Australia Singapore Cable")
site:shire.gov.cx "{Place}" (Google OR cable OR planning OR "data centre" OR "data center" OR telecommunications)
```

执行要求：

1. 先跑全分区 `Christmas Island Australia -Kiritimati` 模板，再跑上表地点。
2. 对 Flying Fish Cove、Airport、Phosphate Hill 必须追加 Google/Vocus/EPBC/Shire 查询。
3. 对媒体中的 Google data centre/data hub，只能建 `status: lead`，除非出现 Google 官方 data-centre 页面、Shire development approval、EPBC non-cable data-centre referral、AusTender/Defence contract 或电力接入文件。
4. 负面结论要写入 `verified-negative`，不要为填表把普通基站、Wi-Fi、办公室服务器柜提升为数据中心。

## 4. 候选记录模板（Extraction Schema）

```text
country_code: CX
division: Christmas Island
sub_location: Flying Fish Cove | Settlement | Kampong | Phosphate Hill | Drumsite | Airport | North West Point | Unknown CX
facility_or_project_name:
operator_or_owner: Vocus | CiFi | Telstra | Google | Australian Government (IOT) | Shire of Christmas Island | Home Affairs | PRL/CIP | other
facility_type: cable landing station | telecom PoP | mobile/backhaul facility | government server room | enterprise server room | data centre | colocation | cloud region | AI/HPC | power facility | other
status: operational | planned | under construction | approval/referral | lead | verified-negative
capacity_or_scale: Tbps/Gbps/MW/racks/unknown
power_connection: IOT Power Service isolated grid | dedicated generation | solar/BESS | unknown
connectivity: Vocus ASC | Google Bosun planned | Google Dhivaru planned | Telstra 4G | nbn Sky Muster | CiFi fixed wireless/4G | unknown
evidence_grade: A | B | C
primary_urls:
secondary_urls:
site_address:
coordinates:
notes:
last_checked: 2026-08-12
```

最低升级标准：

- **A 级 facility**：一手来源命名设施/项目、功能和地点；或官方/运营商来源 + 许可/规划/采购来源交叉确认。
- **B 级 lead**：Reuters/ABC/DCD/Guardian 等点名文件或官员，但缺少公开一手审批/运营商设施页。
- **C 级 ignore/rumor**：目录、SEO、社交媒体、无来源转载；仅作二次搜索词。

## 5. 误报与降级规则（Pitfalls）

- **Kiritimati 混淆**：“Christmas Island” 也是基里巴斯 Kiritimati。所有查询必须加 Australia / Indian Ocean / CX 或 `-Kiritimati -Kiribati`。
- **.cx 域名噪声**：`.cx` 被商业滥用。优先 `shire.gov.cx`、`cifi.com.au`、`gov.au`；不要用裸 `site:.cx` 当证据。
- **电缆登陆站 != 商业 DC**：ASC landing station 与 Google cable landing works 是电信基础设施；无机架/托管/互联产品时不计 colocation。
- **Google data centre rumor**：2025 媒体报道与 Shire 线索值得追踪，但 Google 官方公开材料核实的是海缆。报道被公司否认/淡化时，可靠性保持 B/C lead。
- **卫星/4G/Wi-Fi != DC**：Sky Muster、Telstra 4G、CiFi fixed wireless、Starlink、机场 Wi-Fi 都是连接性。
- **电力设施 != DC**：IOT Power Service、柴油机组、太阳能/BESS、PRL/CIP energy plans 只能作为可行性/否定或支撑材料。
- **拘留中心受限**：North West Point ICT 只记录公开合同或官方文件，不推断内部机房。
- **云区域缺席**：澳大利亚大陆区域（Sydney/Melbourne 等）不等于 CX 本地设施。

## 6. 建议首轮扫描顺序（Recommended Sweep）

1. Manifest 确认：`CX` 只有 `Christmas Island` 一个 division。
2. 官方入口：DITRDCA IOT + Service Delivery kit + Shire + WA planning。
3. 已有电信设施：Vocus ASC + DITRDCA 2018 landing station bulletin + CiFi + Telstra/Parks Australia。
4. 新海缆：Google Bosun + Dhivaru + EPBC referral + Shire planning。
5. 数据中心传闻：Reuters/ABC/Guardian/DCD lead → Shire council minutes/planning → EPBC/AusTender/Home Affairs/Defence/Google 官方交叉。
6. 电力过滤：IOT Power Service、Phosphate Hill、PRL/CIP energy claims。
7. 云/colo/目录负面：官方云区域页 + datacentermap/datacenters/cloudscene。
8. 写入候选：A 级设施、B/C 级 lead、verified-negative 分开记录。
