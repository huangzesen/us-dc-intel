# CC 官方探索器 - 科科斯（基林）群岛数据中心枚举方法论：澳洲领地政府 / 电信 / 电力 / 采购
# CC Explorer Official - Cocos (Keeling) Islands Datacenter Enumeration via Australian Territory Government, Telecom, Power, and Procurement

Date: 2026-08-12. Scope: Cocos (Keeling) Islands (CC)。Manifest entry verified from `world-manifest.jsonl`: `subnational_type=country`; **唯一清单分区 / only division: `Cocos (Keeling) Islands`**. 细化地点只作证据落位：West Island、Home Island、Direction Island、Unknown CC。

本文是官方来源优先的方法论，不是设施清单。结论需要随执行日期复核；但下列 URL 已在本次评审中确认可访问或可检索。

## 0. 结论基线（Ground Truth）

- **商业数据中心判断 / commercial DC judgment**: 截至 2026-08-12，公开官方来源未发现 CC 存在可验证的商业托管、云区域、超大规模、AI/HPC 或 carrier hotel 市场。
- **关键修正 / key correction**: CC 不是无海缆领地。Oman Australia Cable (OAC) 已投入服务，行业及运营商来源确认其登陆点包括 **West Island, Cocos (Keeling) Islands**。这应记录为电信基础设施 / cable landing station lead，不应自动计为商业数据中心。
- **连接基线 / connectivity baseline**: nbn 官方 Sky Muster 页面确认 Cocos (Keeling) Islands 可通过 Sky Muster 卫星服务接入 nbn；OAC 为国际海缆登陆线索；Telstra/本地运营商/IOTT 相关线索需用官方覆盖、ACMA、AusTender 或运营商页面交叉验证。
- **电力基线 / power baseline**: 可公开证据显示 Home Island 有小规模柴油/风电历史项目，AusTender 存在 CC 电力发电、配电、电缆、控制系统和燃油采购记录。任何 MW 级数据中心主张必须匹配联邦采购、电力接入和建设批准证据。
- **人口/治理基线 / governance baseline**: ABS 2021 QuickStats 显示 CC 常住人口约 593；基础设施部页面确认澳大利亚政府负责 Christmas Island 与 Cocos (Keeling) Islands 两个 Indian Ocean Territories，并通过部门、WA 服务安排或合同交付州级服务。

## 1. 可靠性分级（Reliability Grades）

- **A - 官方/一手来源**: Australian Department of Infrastructure IOT 页面、Shire of Cocos (Keeling) Islands、ABS、DFAT、nbn、Telstra 官方页、ACMA、AusTender、ARENA、官方预算/Portfolio Budget Statements、官方云区域清单、运营商正式新闻稿（如 SUBCO）。
- **B - 强二手来源**: ABC News、Reuters、Oman Observer、iTnews、DCD、SubTel Forum、Capacity Media、TeleGeography/Submarine Cable Map、APH/ANAO 文件。若直接引用一手文件或运营商声明，可作为 A 级结论的佐证；单独使用时仍为 B。
- **C - 弱/聚合来源**: 数据中心目录站、SEO 市场报告、供应商国家下拉页、社交媒体、无引用中英文文章、BGP/故障监控页。只能生成线索，不能计数。

## 2. 已核实官方来源登记册（Verified Official Source Register）

### 2.1 领地政府 / Governance (Grade A)

- Infrastructure IOT portal: `https://www.infrastructure.gov.au/territories-regions/territories/indian-ocean-territories-christmas-island-and-cocos-keeling-islands`
  - 已核实：页面说明 Australian Government 对 Christmas Island 与 Cocos (Keeling) Islands 负责，并通过部门、WA SDA 或合同交付服务。
- Cocos governance page: `https://www.infrastructure.gov.au/territories-regions-cities/territories/indian-ocean-territories/cocos-keeling-islands/governance-administration`
  - 用途：治理结构、法律适用、Administrator/地方政府线索。
- Shire of Cocos (Keeling) Islands: `https://shire.cc/`
  - 已核实：官网有效，菜单含 Tender、Council documents、Major Projects、Home Island/West Island contact pages。
- ABS 2021 QuickStats: `https://www.abs.gov.au/census/find-census-data/quickstats/2021/901021002`
  - 已核实：用于人口、住户和小市场规模基线。
- DFAT: `https://www.dfat.gov.au/`
  - 用途：领地/国际政策背景。未保留未验证的 CC 专页；执行时用 `site:dfat.gov.au "Cocos (Keeling) Islands"` 或相关双边页面检索。

### 2.2 电信 / Telecom (Grade A/B)

- nbn Sky Muster: `https://www.nbnco.com.au/learn/network-technology/sky-muster-explained`
  - 已核实：nbn 明确列出 Cocos (Keeling) Islands 可通过 Sky Muster satellite providers 获得 nbn-powered plans。该证据证明接入服务，不证明本地数据中心。
- nbn satellite ground-equipment release: `https://www.nbnco.com.au/corporate-information/media-centre/media-statements/satellite-ground-equipment-contract`
  - 用途：确认 Sky Muster 体系由澳大利亚境内多个 ground station 支撑；不要把用户侧碟形天线计作设施。
- Telstra official site: `https://www.telstra.com.au/`
  - 用途：覆盖、USO、移动和企业服务线索。Telstra satellite-to-mobile FAQ 明确不覆盖 Australian territorial islands；这说明该特定 LEO 手机短信产品不适用，不等同于 Telstra 无任何 CC 业务。
- ACMA: `https://www.acma.gov.au/`
  - 用途：频谱/广播/无线许可、carrier 记录；必要时查询 Register of Radiocommunications Licences。
- SUBCO OAC release: `https://sub.co/news/australias-first-express-cable-to-emea-has-landed-in-perth-on-track-to-go-live-in-q22022-2`
  - 已核实：SUBCO OAC 官方项目新闻有效，但该页面主要确认 Perth landfall 和项目背景；需配合 OAC ready-for-service 来源确认 West Island landing。
- OAC ready-for-service corroboration: `https://www.omanobserver.om/article/1126098/business/economy/oman-australia-undersea-cable-is-ready-for-service`
  - 已核实：报道引用 SUBCO，说明 OAC live/ready for service，landing points 包括 Perth、West Island Cocos (Keeling) Islands、Muscat。按 B+ 处理，结合 SUBCO 官方项目来源可支撑 `cable landing station lead`。

### 2.3 电力 / Power and Utilities (Grade A/B)

- AusTender search: `https://www.tenders.gov.au/`
  - 已核实可检索到 CC 电力相关记录，例如 `CKI HV 10032223`（安装电缆以支持 CC 配电）、`CN4121171` / amendments（Generator Control System on Cocos (Keeling) Islands）、`CN474105` 与 `CN1233272`（Diesel fuel for power generation - Cocos/Keeling Islands）、`CN4038128`（Power Infrastructure Structural Inspections）。
- Home Island Power Station and Wind Farm profile: `https://worldofrenewables.com/home_island_power_station_and_wind_farm/`
  - B 级历史项目来源：记录 Home Island power station/wind component, four 320 kW diesel generators and 80 kW wind project. 用作容量级别和误报过滤，需以政府/采购记录交叉验证。
- Clean Energy Regulator generation facility data: `https://cer.gov.au/document/greenhouse-and-energy-information-designated-generation-facility-2023-24`
  - 用途：可查 `Cocos Keeling Islands - Home Island Generation` 等发电数据线索。
- ARENA: `https://arena.gov.au/`
  - 本次未发现足以证明 CC 数据中心的项目；保留为 renewable/microgrid 查询入口。

### 2.4 采购 / Procurement (Grade A)

- AusTender advanced search: `https://www.tenders.gov.au/search/cnadvancedsearch`
- AusTender ATM search: `https://www.tenders.gov.au/search/atmadvancedsearch`
- Shire tenders: `https://shire.cc/en/your-council/tender-and-eois.html`

检索时必须保存 notice ID、title、agency、supplier、value、period、category、URL 和 last_checked。普通 IT 服务或电力工程不计为数据中心；只有明确 server room、data centre、cable landing station、telecom exchange、hosting/colocation 时才升为候选。

### 2.5 云区域负面来源 / Official Cloud Region Negatives (Grade A)

仅使用官方清单确认“无本地云区域”：

- AWS Regions: `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html`
- Azure geographies and regions: `https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- Google Cloud locations: `https://cloud.google.com/about/locations`
- Oracle OCI regions: `https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm`

截至 2026-08-12，官方清单未发现 CC 区域。国家下拉框出现 “Cocos (Keeling) Islands” 不等于 cloud region。

## 3. 官方查询模板（Official Query Templates）

政府与领地行政：

```text
site:infrastructure.gov.au ("Cocos (Keeling) Islands" OR "Indian Ocean Territories") (ICT OR digital OR connectivity OR "data centre" OR "data center" OR server OR cloud OR cybersecurity)
site:infrastructure.gov.au "Cocos (Keeling) Islands" ("cable landing" OR submarine OR OAC OR "Oman Australia Cable" OR satellite OR power)
site:shire.cc ("Cocos" OR "Keeling") (tender OR EOI OR ICT OR server OR power OR procurement OR "data centre" OR "data center")
site:dfat.gov.au "Cocos (Keeling) Islands" (governance OR connectivity OR digital OR cable)
```

电信 / Telecom：

```text
site:nbnco.com.au (Cocos OR "Cocos (Keeling) Islands" OR "Indian Ocean Territories") ("Sky Muster" OR satellite OR gateway OR "ground station" OR "point of presence" OR PoP)
site:telstra.com.au (Cocos OR "Keeling" OR "Indian Ocean Territories") (mobile OR coverage OR satellite OR exchange OR "data centre" OR "data center")
site:acma.gov.au (Cocos OR "Keeling") (carrier OR licence OR radiocommunications OR satellite OR spectrum)
site:sub.co ("Cocos" OR "West Island" OR "Oman Australia Cable" OR OAC)
"Oman Australia Cable" "West Island" "Cocos (Keeling) Islands"
"Cocos (Keeling) Islands" "cable landing station"
```

电力与采购 / Power and procurement：

```text
site:tenders.gov.au ("Cocos (Keeling) Islands" OR "Cocos/Keeling" OR "Indian Ocean Territories") (ICT OR server OR "data centre" OR "data center" OR power OR generator OR electricity OR "control system" OR fibre OR cable)
site:arena.gov.au (Cocos OR "Cocos (Keeling) Islands") (solar OR battery OR renewable OR microgrid OR storage)
"Cocos (Keeling) Islands" "power station" (diesel OR MW OR generator OR "Home Island")
"Cocos Keeling Islands - Home Island Generation"
```

云区域、托管、AI/HPC 负面检查：

```text
"Cocos (Keeling) Islands" ("cloud region" OR "edge location" OR AWS OR Azure OR "Google Cloud" OR Oracle OR OCI)
"Cocos (Keeling) Islands" ("data centre" OR "data center" OR datacenter OR colocation OR "rack space" OR "carrier hotel") -tourism -diving
"Cocos (Keeling) Islands" (AI OR GPU OR supercomputer OR "high performance computing") (facility OR investment OR campus)
```

中文传闻监视 / Chinese rumor watch：

```text
("科科斯（基林）群岛" OR "科科斯群岛" OR "科科斯") ("数据中心" OR "服务器" OR "云区域" OR "海缆" OR "算力" OR "电力")
```

## 4. 分区枚举策略（Per-Division Enumeration）

Manifest 只有 1 个分区：`Cocos (Keeling) Islands`。分区覆盖必须是全领地覆盖；West Island、Home Island、Direction Island 只是 sub_location。

| 清单分区 | 细化地点 | 优先级 | 官方检索策略 | 计数规则 |
|---|---:|---|---|---|
| Cocos (Keeling) Islands | Whole territory | High | 跑第 3 节全部模板；覆盖 Infrastructure、Shire、nbn、Telstra、ACMA、SUBCO/OAC、AusTender、云清单。 | 只有命名设施/项目且功能明确时计候选；否则记录 verified-negative。 |
| Cocos (Keeling) Islands | West Island | High | 首府、机场、政府集中区、OAC landing point。检索 West Island + OAC/cable landing/ICT/power/Telstra/nbn。 | OAC landing 可计 telecom facility lead；机场普通通信机房不计 DC。 |
| Cocos (Keeling) Islands | Home Island | Medium | 社区、Shire seat/服务、电力站历史线索。检索 Home Island + power/server/ICT/telecom。 | 电力站不计 DC；若政府 ICT/server room 被命名，只计 lead。 |
| Cocos (Keeling) Islands | Direction Island | Low | 历史 telegraph cable station 误报防护。 | 1901/历史电报站不计现代设施。 |
| Cocos (Keeling) Islands | Unknown CC | High | 来源确认存在设施但不给具体岛屿时使用。 | 不强行落到 West/Home Island。 |

## 5. 候选抽取模板（Candidate Schema）

```text
country_code: CC
division: Cocos (Keeling) Islands
sub_location: West Island | Home Island | Direction Island | Unknown CC
facility_or_project_name:
operator_or_owner: SUBCO | nbn | Telstra | IOTT | Australian Government (IOT) | Shire of Cocos (Keeling) Islands | Island Power Co | other
consent_or_authorisation: ACMA licence | AusTender notice | federal budget | Shire tender | operator announcement | none found
site_address:
coordinates:
status: operational | ready-for-service | under construction | planned | lead | verified-negative
facility_type: cable landing station | satellite access terminal/service | satellite ground station | telecom exchange | government server room | colocation | cloud region | AI/HPC | power station | other
it_load_mw:
power_connection: isolated island grid | diesel generation | wind/renewable component | unknown
connectivity: Oman Australia Cable | nbn Sky Muster satellite | Telstra/IOTT mobile | unknown
evidence_grade: A | B | C
primary_urls:
secondary_urls:
notes:
last_checked: 2026-08-12
```

## 6. 当前候选与负面状态（Current Candidate State）

- **Oman Australia Cable landing - West Island**: telecom/cable landing station lead; status operational/ready-for-service; owner/operator SUBCO; evidence B+ with SUBCO official project source plus Oman Observer ready-for-service report. Not a commercial data center unless colocation/hosting is explicitly offered at CC.
- **nbn Sky Muster service - whole territory**: access service verified by nbn official page; user premises equipment and mainland ground stations are not CC data centers.
- **Telstra / IOTT mobile and internet services**: telecom service leads only. Count a facility only if ACMA, AusTender, Telstra/IOTT official materials, or Shire documents name a local exchange, shelter, hub, or hosting product.
- **Home Island power generation**: power infrastructure lead/constraint. Do not count as DC.
- **Government/Shire server rooms**: plausible but unverified. Count only if a procurement, audit, asset plan, or official notice names a server room/data centre.
- **Commercial colocation / cloud region / AI-HPC**: verified negative as of this review.

## 7. 常见误报（False Positives）

- 把 OAC cable landing station 当作商业数据中心。
- 把 nbn Sky Muster 用户侧天线、modem 或澳大利亚本土 ground station 当作 CC 本地数据中心。
- 把 Telstra/IOTT 基站、4G 覆盖或卫星回程当作 carrier hotel。
- 把 Home Island power station、wind/solar/battery 项目、电缆配电工程当作数据中心。
- 把 Direction Island 历史电报站当作现代通信设施。
- 把 Google/AWS/Azure/Oracle 国家下拉框、billing country、marketing country 当作 cloud region。
- 把 Corning/Iron Mountain/Equinix 等全球供应商页面中的国家列表当作 CC 设施。
- 把普通机场、学校、诊所、酒店或 Shire 办公室 IT 设备计为设施。

## 8. 首轮执行工作流（Recommended Workflow）

1. 从 Infrastructure IOT、Shire、ABS 固定治理和规模基线。
2. 用 nbn、Telstra、ACMA、SUBCO/OAC 查询连接；OAC West Island landing 单独记录为 telecom facility lead。
3. 在 AusTender 搜 `Cocos`, `Cocos/Keeling`, `Indian Ocean Territories`, `Oman Australia Cable`, `Generator Control System`, `ICT`, `server`, `data centre`。
4. 用 Home Island power station / CER / AusTender 建立电力容量过滤条件。
5. 跑官方云区域清单，记录 CC cloud-region negative。
6. 对 West Island、Home Island、Direction Island 做细化地点扫描；没有来源时使用 `Unknown CC`。
7. 每条候选保留 URL、notice ID、来源等级、摘录日期和“不计数原因”。
