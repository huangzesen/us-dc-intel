# CC 行业探索器 - 科科斯（基林）群岛数据中心枚举方法论：行业 / 贸易媒体 / 供应商发现
# CC Explorer Industry - Cocos (Keeling) Islands Datacenter Enumeration via Industry, Trade Press, and Vendor Discovery

Date: 2026-08-12. Scope: Cocos (Keeling) Islands (CC)。Manifest entry verified from `world-manifest.jsonl`: `subnational_type=country`; **唯一清单分区 / only division: `Cocos (Keeling) Islands`**. 细化地点：West Island、Home Island、Direction Island、Unknown CC。Angle: industry/operator/infrastructure pipeline.

本文用于行业侧发现和误报过滤；最终计数仍以官方、运营商或项目一手证据为准。

## 0. 市场现实（Market Reality）

- **商业托管市场 / commercial colocation**: 截至 2026-08-12，未发现 CC 有公开可验证的商业 colocation、carrier hotel、hyperscale、AI/HPC 或公有云区域。
- **电信基础设施存在 / telecom infrastructure exists**: Oman Australia Cable (OAC) 已经使 Cocos (Keeling) Islands 接入国际海缆，公开报道将 landing point 指向 **West Island**。这会产生 cable landing station / connectivity lead，但不自动产生商业数据中心记录。
- **卫星仍是重要接入层 / satellite access remains relevant**: nbn 官方 Sky Muster 页面列明 Cocos (Keeling) Islands 可通过 Sky Muster satellite providers 使用 nbn-powered plans。用户侧天线、modem 和 nbn 澳大利亚本土 ground stations 不应计为 CC 数据中心。
- **本地运营商线索 / local operator leads**: IOTT、MultiWave、Cocos Communications and IT 等可作为 internet/mobile/IT service leads；除非出现公开的 hosting/rack/colocation/facility 证据，否则不能计数。
- **硬过滤 / hard filters**: 人口约 593、岛屿孤立电力系统、小型电力工程和燃油采购记录，都与 MW 级数据中心主张不匹配。任何大规模设施声称必须有电力、建设、通信许可和采购/投资证据。

## 1. 可靠性分级（Reliability Grades）

- **A - 一手/运营商/官方**: SUBCO、nbn、Telstra、IOTT/本地运营商正式页面、Australian Department of Infrastructure、Shire、AusTender、ACMA、ARENA、ABS、官方云区域清单。
- **B - 权威行业/媒体**: ABC News、Reuters、Oman Observer、iTnews、DCD、SubTel Forum、Capacity Media、TeleGeography/Submarine Cable Map、Submarine Networks、APH/ANAO。用于发现和交叉验证；单独出现时通常不直接计数。
- **C - 弱来源**: 数据中心目录、SEO 市场报告、国家下拉页、社交媒体、供应商泛区域页面、无引用中英文文章、BGP/故障聚合。只能作为 rumor watch。

## 2. 行业来源登记册（Industry Source Register）

### 2.1 海缆与登陆站 / Subsea Cable and CLS

- SUBCO OAC project/news: `https://sub.co/news/australias-first-express-cable-to-emea-has-landed-in-perth-on-track-to-go-live-in-q22022-2`
  - Grade A operator source for OAC project context.
- Oman Observer ready-for-service report: `https://www.omanobserver.om/article/1126098/business/economy/oman-australia-undersea-cable-is-ready-for-service`
  - Grade B+ corroboration quoting SUBCO; confirms OAC live/ready for service and landing points including West Island, Cocos (Keeling) Islands.
- DCD / Reuters / iTnews / SubTel Forum / Submarine Networks:
  - Use for OAC, Diego Garcia spur, Salalah spur, and future Indian Ocean route changes. Treat as B unless linking to primary documents.
- Google Australia Connect / Bosun / Dhivaru:
  - Official Google pages confirm Christmas Island-focused cables/connectivity hubs, not CC facilities unless a source explicitly names Cocos (Keeling) Islands.
  - `https://cloud.google.com/blog/products/infrastructure/bosun-australia-connect-initiative-for-indo-pacific-connectivity`
  - `https://cloud.google.com/blog/products/networking/introducing-dhivaru-new-subsea-cable`

### 2.2 Satellite, Mobile, and Internet Operators

- nbn Sky Muster: `https://www.nbnco.com.au/learn/network-technology/sky-muster-explained`
  - Grade A. Confirms service availability to Cocos (Keeling) Islands; does not locate a CC data center.
- nbn ground equipment: `https://www.nbnco.com.au/corporate-information/media-centre/media-statements/satellite-ground-equipment-contract`
  - Grade A for Sky Muster architecture and ground station context.
- Telstra: `https://www.telstra.com.au/`
  - Grade A for direct Telstra claims. Search coverage, USO, mobile, satellite-to-mobile limitations, and enterprise notices.
- IOTT listing: `https://iot-businesses.com.au/directory/indian-ocean-territories-telecom/`
  - Grade B/C business-directory lead unless backed by IOTT-owned page or government/ACMA/AusTender evidence. Useful terms: `IOTT`, `Indian Ocean Territories Telecom`, `Cocos 4G network`, `NBN Sky Muster Plus`.
- MultiWave: `https://multiwavenetworks.com.au/cocos-islands-internet/`
  - Grade B/C provider lead for nbn Sky Muster resale. Not facility evidence.
- Cocos Communications and IT:
  - Use ABN Lookup, AusTender and Shire documents for verification. Social pages are C only.

### 2.3 Power and Civil Infrastructure Context

- AusTender: `https://www.tenders.gov.au/`
  - Grade A for contracts. Relevant discovered terms: `CKI HV 10032223`, `Generator Control System on Cocos (Keeling) Islands`, `Diesel fuel for power generation - Cocos/Keeling Islands`, `Power Infrastructure Structural Inspections`.
- Home Island Power Station and Wind Farm profile: `https://worldofrenewables.com/home_island_power_station_and_wind_farm/`
  - Grade B historical power-capacity source. Use to sanity-check power scale, not as data center evidence.
- Clean Energy Regulator data: `https://cer.gov.au/document/greenhouse-and-energy-information-designated-generation-facility-2023-24`
  - Grade A/B government dataset for generator names and annual generation.

### 2.4 Datacenter and Cloud Directories

- DCD: `https://www.datacenterdynamics.com/`
  - B for real articles; no CC commercial DC found in this review.
- DataCenterMap, Cloud Infrastructure Map, DataCenters.com, Corning/Iron Mountain/Equinix global pages:
  - C unless naming a CC address, operator and facility with corroboration. Country selector hits are false positives.
- Official cloud regions:
  - AWS: `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html`
  - Azure: `https://learn.microsoft.com/en-us/azure/reliability/regions-list`
  - Google Cloud: `https://cloud.google.com/about/locations`
  - Oracle OCI: `https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm`

## 3. 行业查询模板（Industry Query Templates）

海缆 / Subsea:

```text
"Oman Australia Cable" ("Cocos" OR "West Island" OR "Cocos (Keeling) Islands")
site:sub.co ("Oman Australia Cable" OR OAC) (Cocos OR "West Island" OR "ready for service" OR landing)
site:datacenterdynamics.com ("Oman Australia Cable" OR "Cocos Islands" OR "Cocos (Keeling)")
site:subtelforum.com ("Oman Australia Cable" OR "Cocos" OR "West Island")
site:submarinecablemap.com "Cocos (Keeling) Islands"
"Cocos (Keeling) Islands" "cable landing station"
```

卫星、移动、本地 ISP / Satellite, mobile, local ISPs:

```text
site:nbnco.com.au (Cocos OR "Cocos (Keeling) Islands" OR "Indian Ocean Territories") ("Sky Muster" OR satellite OR business OR wholesale OR "ground station")
site:telstra.com.au (Cocos OR "Keeling" OR "Indian Ocean Territories") (mobile OR coverage OR satellite OR exchange OR "data centre" OR "data center")
"Indian Ocean Territories Telecom" OR IOTT (Cocos OR "Cocos 4G" OR "Sky Muster" OR nbn OR hosting OR colocation)
"Cocos Communications and IT" (telecommunications OR ICT OR hosting OR server OR tender)
site:multiwavenetworks.com.au Cocos ("Sky Muster" OR nbn OR business)
```

托管、云、AI/HPC 负面检查 / DC, cloud, AI negative checks:

```text
"Cocos (Keeling) Islands" (colocation OR colo OR "rack space" OR "carrier hotel" OR "internet exchange" OR IX)
"Cocos (Keeling) Islands" ("data centre" OR "data center" OR datacenter) -tourism -diving
"Cocos (Keeling) Islands" (AWS OR Azure OR "Google Cloud" OR Oracle OR OCI OR "cloud region" OR "edge location")
"Cocos (Keeling) Islands" (GPU OR AI OR "artificial intelligence" OR supercomputer OR "high performance computing") (investment OR facility OR campus)
site:datacentermap.com (Cocos OR Keeling)
site:cloudinfrastructuremap.com (Cocos OR Keeling)
```

行业媒体 / Trade press:

```text
site:abc.net.au "Cocos (Keeling) Islands" (cable OR satellite OR internet OR Telstra OR nbn OR digital OR "data centre")
site:reuters.com ("Cocos" OR "Oman Australia Cable" OR "Indian Ocean Territories")
site:itnews.com.au ("Oman Australia Cable" OR "Cocos")
site:capacitymedia.com ("Cocos" OR "Oman Australia Cable" OR "Indian Ocean Territories")
site:datacenterdynamics.com ("Cocos" OR "Keeling" OR "Indian Ocean Territories")
```

中文传闻监视 / Chinese rumor watch:

```text
("科科斯（基林）群岛" OR "科科斯群岛" OR "科科斯") ("数据中心" OR "云区域" OR "海缆" OR "算力" OR "服务器" OR "托管")
"Cocos (Keeling) Islands" ("data centre" OR "data center" OR cloud OR ICT) (China OR Chinese OR Huawei OR HMN OR "China Harbour")
```

## 4. 枚举矩阵（Enumeration Matrix）

| 候选类型 | 主要来源 | 优先级 | 何时升级计数 |
|---|---:|---|---|
| OAC cable landing / CLS | SUBCO (A), Oman Observer/iTnews/DCD/SubTel (B), ACMA/AusTender if found (A) | High | 明确命名 West Island/CC landing station、operator、status；计 telecom facility lead，不计 commercial DC。 |
| nbn Sky Muster access | nbn (A), providers (B/C) | High | 只证明服务；仅当 nbn/ACMA 命名本地 PoP、gateway、shelter 或 exchange 时计设施候选。 |
| Telstra/IOTT mobile or internet infrastructure | Telstra/IOTT official (A/B), ACMA/AusTender (A), local media (B/C) | High | 命名本地交换、hub、shelter、backhaul facility 或 hosting product。 |
| Government/Shire server room | Infrastructure/Shire/AusTender (A) | Medium | 采购或审计命名 server room/data centre；仍标 `lead`，不可当商业设施。 |
| Local ISP/reseller hosting | Operator pages, ACMA, AusTender, ABN, media | Medium | 明确提供 CC 本地 rack/hosting/colocation，并有地址/设施证据。 |
| Commercial colocation/cloud/AI-HPC | Official cloud lists (A), operator announcements (A), DCD/Reuters (B) | Low | 需要一手运营商或官方区域/设施公告；目录站永不单独计数。 |
| Power infrastructure | AusTender/CER (A), project profiles (B) | Filter | 只作容量和可行性过滤；不计 DC。 |

## 5. 候选必填字段（Required Fields）

```text
country_code: CC
division: Cocos (Keeling) Islands
sub_location: West Island | Home Island | Direction Island | Unknown CC
facility_or_project_name:
operator: SUBCO | nbn | Telstra | IOTT | Cocos Communications and IT | Australian Government (IOT) | Shire of Cocos (Keeling) Islands | other
facility_type: cable landing station | satellite access service | satellite ground station | telecom exchange | mobile/backhaul site | government server room | colocation | cloud region | AI/HPC | other
status: operational | ready-for-service | under construction | planned | lead | verified-negative
capacity_or_scale: Tbps | MW | racks | users | unknown
evidence_grade: A | B | C
primary_urls:
secondary_urls:
connectivity: Oman Australia Cable | nbn Sky Muster satellite | Telstra/IOTT mobile | unknown
power: isolated island grid | diesel generation | wind/renewable component | unknown
site_address:
coordinates:
notes:
last_checked: 2026-08-12
```

最低计数标准：一个 A 级设施/项目来源，或运营商官方来源加一个独立 A/B 级佐证；细化地点必须有来源明确命名、地址、坐标或可复核的地理编码过程。

## 6. 已验证负面与误报（Verified Negatives and False Positives）

- **Commercial colocation**: 未发现 CC 本地商业托管供应商。IOTT/MultiWave 属连接服务线索，不等于机架托管。
- **Cloud regions**: AWS/Azure/Google Cloud/Oracle OCI 官方区域清单无 CC region。
- **OAC/CLS**: West Island cable landing 是电信设施线索；除非出现公开 colocation/caching/hosting 产品，不计 commercial DC。
- **Google Christmas Island hubs**: Google Australia Connect/Bosun/Dhivaru 目前指向 Christmas Island、Mandurah、Maldives、Thailand/Oman 等；不要外推到 Cocos (Keeling) Islands。
- **Satellite service**: Sky Muster、Starlink、O3b/SES、Optus satellite availability 是连接上下文，不构成本地数据中心。
- **Power projects**: Home Island power station、wind/solar/battery、generator controls、电力电缆不是数据中心。
- **Historical Direction Island cable station**: 历史电报设施不计现代设施。
- **SEO/directory artifacts**: `Unknown Cocos Data Center`、供应商国家下拉框、市场规模页面、中文泛文章默认 C 级。

## 7. 推荐扫描顺序（Recommended Sweep Order）

1. OAC/SUBCO sweep: 确认 OAC West Island landing、RFS、operator、landing-station evidence and whether any colocation/caching product exists.
2. nbn/Telstra/IOTT sweep: 区分 access service、mobile site、exchange/hub、hosting product。
3. AusTender/ACMA sweep: 查 telecom, ICT, generator, fibre, cable landing, server, data centre terms；记录 notice IDs。
4. Power filter: 用 AusTender、CER、Home Island project records 检查任何设施主张的电力可行性。
5. Cloud/directories negative sweep: 官方云区域清单 + DCD/DataCenterMap/CloudInfrastructureMap/中文搜索。
6. Location sweep: West Island high priority for OAC/airport/government; Home Island for power/Shire; Direction Island for historical false positives; otherwise `Unknown CC`。
