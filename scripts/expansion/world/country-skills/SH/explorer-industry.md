# SH Explorer Industry：圣赫勒拿、阿森松与特里斯坦-达库尼亚行业/媒体/厂商发现方法论
# （Saint Helena, Ascension and Tristan da Cunha — Industry / Trade-Press / Vendor Discovery）

日期：2026-08-12。国家：**SH — Saint Helena, Ascension and Tristan da Cunha（圣赫勒拿、阿森松与特里斯坦-达库尼亚）**。Manifest 已核对：`world-manifest.jsonl` 第 153 行，`subnational_type = "geographical region"`，**divisions = Ascension / Saint Helena / Tristan da Cunha**。记录必须使用 manifest 分区拼写，并附自然子层（Jamestown、Rupert's、Georgetown、Edinburgh of the Seven Seas 等）。

本文角度：**行业/运营商/贸易媒体/厂商发现**。行业来源主要用于产生和交叉验证线索；设施晋级仍需 `explorer-official.md` 的一手证据闭环。Saint Helena 有海缆和政府主机房，但没有公开商业 colo 或云区域；Ascension 与 Tristan da Cunha 的通信设施多数是卫星、移动网或军事/广播通信，不应误判为数据中心。

信度分级（Reliability grades）：**A** = 运营方/厂商自控页面、SHG/AIG/TDG 官方页、公报、Google Equiano 官方页、官方云区域页、认证注册处。**B** = 具名当事方、日期、地点的可靠媒体/行业报道（SAMS、St Helena Independent、The Sentinel、The Islander、DCD、Developing Telecoms、Capacity Media、Submarine Networks、TechAfrica News、SubTel Forum 等）。**C** = 目录站、SEO 托管页、承包商作品集、社交帖、活动简介、转引报道、无地址/设施证据的主张。

---

## 0. 市场形态与已核实事实（Market shape and verified facts）

- **确认设施只有 1 条**：St Helena Government Main Data Centre, Carnarvon Court, Jamestown（Saint Helena / Jamestown），A 级，2022-03-07 SHG + Gazette 证据，容量 `null`。
- **Equiano 是连接基础设施，不是本地云区域**：Google 私营 Equiano 海缆从 Portugal 到 South Africa，Saint Helena 为支线登陆点。SHG 2019-12-23 与 Google 签合同；2021-08-29 在 Rupert's Beach 登陆；2023-06-01 SHG 称 SLTE live；2023-09-01 SHG 称 cable live 并由 Sure 面向公众服务。Rupert's MCLS/landing station 默认非 DC。
- **运营商**：Sure St Helena 官网 `https://www.sure.co.sh/` 已核实，说明其提供 broadband、mobile、national/international telephone、public Internet 与 TV rebroadcast services，并属 Beyon group。此为电信服务事实，不证明 colo。
- **电力/公用事业**：Connect Saint Helena 当前官网为 `http://www.connect.co.sh/`，About 页为 `http://www.connect.co.sh/about-us.html`。公司归 St Helena Government 所有，2013-04-01 运营，核心服务为 Electricity、Water、Wastewater，受 St Helena Utilities Regulatory Authority 监管。旧草稿 connectsthelena.com 未作为当前官网保留。
- **Ascension**：AIG 2026 电信转换公告确认 Sure South Atlantic 将于 2026-02-28 停止岛上电信服务角色，Omnitouch 从 2026-03-01 接续并建设/测试含 4G mobile 的系统；无公开 DC 证据。
- **Tristan da Cunha**：TDG 2024-09-22 新闻确认 Starlink 到岛，Starlink 天线在 IT Container（Communications HQ，2022-05 commissioned）屋顶，旧 VSAT 仍提供 10 Mbps 并承载语音。该事实为卫星通信线索，非 DC。
- **云区域缺位**：AWS、Azure、GCP、OCI 官方区域页截至本批次均无 Saint Helena / Ascension / Tristan da Cunha。目录或 VPS 页不得覆盖官方缺位结论。
- 诚实产出预期：**1 条设施 + 若干连接类/通信类线索 + 阴性覆盖**。不要从海缆容量、援助金额、发电容量、军事通信站或卫星互联网推导机架/MW。

---

## 1. 优先运营商与行业扫描（Priority operator and industry sweep）

| 线索/主体 | 来源路线 | 分区/子层处理 | 等级与动作 |
|---|---|---|---|
| SHG Main Data Centre, Carnarvon Court | SHG 2022-03-07 发布 + Gazette EX-GAZ-9；Schneider Electric 调试 | Saint Helena / Jamestown | **A 已确认**；容量 `null`；勿与 Rupert's 合并 |
| Sure St Helena | `https://www.sure.co.sh/`；SHG 许可/EOI；SHG 2023-09-01 cable service update | Saint Helena / 全岛；Rupert's 连接 | **A** 运营方事实；无 colo/DC 证据时不成设施 |
| Google / Equiano | Google Cloud 官方博客；SHG fibre project hub；SHG 2019 contract；SHG 2023 commissioning/live updates | Saint Helena / Rupert's | **A** 海缆事实；非 GCP region；landing station 非 DC |
| Connect Saint Helena | `http://www.connect.co.sh/` 与 About 页；SHG/URA/Companies House | Saint Helena / Jamestown + 电力全岛 | **A** 公用事业事实；Carnarvon Court core equipment 不单列 DC |
| SHG Teleport & Data Centre services（2020 EOI） | SHG EOI 页面；后续采购/合同搜索 | Saint Helena / 待定位 | **C+/历史线索**；需合同/地址/服务证据晋级 |
| OneWeb / satellite earth-station 机会 | DCD、SHG 文件、EarthStation.sh 等 | Saint Helena / 待定位 | **B/C 线索**；卫星地面站非 DC |
| AIG / Omnitouch telecom transition | `ascension.gov.ac` 公告、tender/public documents | Ascension / Georgetown 或待定位 | **A** 电信事实；无 DC |
| Military/BBC communications on Ascension | UK MoD/USSF/BBC 公开文件；行业报道 | Ascension / Cat Hill、Traveller's Hill、Wideawake、English Bay | 通信边界；无公开 DC 证据 |
| Tristan Starlink / VSAT / IT Container | `tristandc.com` 官方新闻 | Tristan da Cunha / Edinburgh of the Seven Seas | **A** 卫星通信事实；非 DC |
| 目录站和托管 SEO | DataCenterMap、datacenters.com、PeeringDB、VPS/hosting pages | 各分区 | **C** 种子；必须回到一手域验证 |

运营商/主体查询模板：
```text
"Sure St Helena" (Equiano OR "landing station" OR "data centre" OR datacenter OR colocation OR broadband)
site:sure.co.sh ("landing station" OR Equiano OR business OR enterprise OR colocation OR hosting)
"Connect Saint Helena" (electricity OR power OR solar OR battery OR "Carnarvon Court")
site:connect.co.sh (generation OR solar OR "power station" OR battery OR "Carnarvon Court")
"St Helena" (teleport OR "data centre services") (EOI OR "expressions of interest" OR tender)
"Equiano" "St Helena" (Google OR landing OR Rupert OR SLTE OR "ready for service" OR live)
"Ascension Island" (Omnitouch OR Sure OR telecommunications OR "4G mobile")
"Tristan da Cunha" (Starlink OR VSAT OR "IT Container" OR "Communications HQ")
```

---

## 2. 行业与媒体来源（Industry and press sources）

| 来源 | URL / 查找方式 | 用途 | 等级规则 |
|---|---|---|---|
| SHG fibre project hub | `https://www.sainthelena.gov.sh/st-helena/government/portfolios/economic-development-portfolio/sustainable-development/fibre-optic-cable-project/` | Equiano landing、MCLS/SLTE、官方 press-release index | A |
| Google Cloud Equiano blog | `https://cloud.google.com/blog/products/infrastructure/introducing-equiano-a-subsea-cable-from-portugal-to-south-africa` | Equiano 所有方、路线、Google funding、ASN 合同 | A |
| Sure St Helena | `https://www.sure.co.sh/` | 电信服务商事实、业务服务页面 | A 对运营方自述；非 DC 除非明确托管 |
| Connect Saint Helena | `http://www.connect.co.sh/` / `http://www.connect.co.sh/about-us.html` | 电力/水/废水、Carnarvon Court 设备线索 | A 对公司事实 |
| AIG | `https://www.ascension.gov.ac/` | Ascension 电信、采购、public documents | A |
| TDG / Tristan | `https://www.tristandc.com/` | Starlink/VSAT、IT Container、岛政新闻 | A/B（政府站新闻） |
| SAMS | `https://www.sams.sh/` | 圣赫勒拿新闻、海缆、电力、数字战略 | A/B，重大主张回核 SHG |
| St Helena Independent / The Sentinel | 按名称搜索当前站点 | 周报、规划公告、商业/电信报道 | B |
| The Islander | 按名称搜索当前站点 | Ascension 民事新闻 | B |
| Submarine Networks / Submarine Cable Map / TeleGeography | `https://www.submarinenetworks.com/`；`https://www.submarinecablemap.com/` | landing point、branch、RFS、阿森松/特里斯坦阴性复核 | B，若系统页引用所有方则按主张定级 |
| DCD / Developing Telecoms / Capacity / TechAfrica News / SubTel Forum | 行业媒体站内搜索 | Equiano、OneWeb、OT connectivity、数据中心误报排除 | B |
| UK Parliament / NAO / FCDO | Hansard 域名 `hansard.parliament.uk`（可能对自动 curl 返回 403）；`https://www.nao.org.uk/`；`https://www.gov.uk/` | 英国资金、审计、合同背景 | A |
| Companies House | `https://find-and-update.company-information.service.gov.uk/` | Connect/Sure 相关实体注册与账户 | A |
| 目录站 | datacenters.com、DataCenterMap、PeeringDB、colo.exchange | 种子发现和负面控制 | C |

媒体/行业查询模板：
```text
site:sams.sh ("data centre" OR Equiano OR "submarine cable" OR "landing station" OR teleport OR electricity)
site:datacenterdynamics.com ("St Helena" OR "Saint Helena" OR Equiano OR OneWeb)
site:developingtelecoms.com ("St Helena" OR "Saint Helena" OR Equiano)
site:capacitymedia.com ("St Helena" OR Equiano OR Ascension)
site:submarinenetworks.com ("St Helena" OR "Saint Helena" OR Equiano)
site:subtelforum.com ("St Helena" OR "Saint Helena" OR Equiano)
"St Helena" "data centre" (2020 OR 2021 OR 2022 OR 2023 OR 2024 OR 2025 OR 2026)
"Ascension Island" "data centre" OR datacenter
"Tristan da Cunha" "data centre" OR datacenter OR internet
```

---

## 3. 目录到一手工作流（Directory-to-primary workflow）

1. 目录/SEO/hosting 页面只取种子。对 “St Helena data center/hosting/VPS” 默认 C，因为常见误报包括 Napa, California 的 St. Helena、卫星地面站、泛非 hosting SEO 页面。
2. 对种子执行一手回核：`sainthelena.gov.sh`、`sure.co.sh`、`connect.co.sh`、`ascension.gov.ac`、`tristandc.com`、`gov.uk`、`nao.org.uk`、`hansard.parliament.uk`、Companies House。
3. 地址必须能落到 manifest 分区 + 自然子层。无地址、无设施名、无运营方自控证据时保持 lead。
4. 状态必须有 commissioning、operational、licence、service launch、planning approval、procurement award 等证据；海缆 live 或 satellite live 只证明连接状态。
5. 容量只接受一手 MW/kW/rack/white-space/认证注册证据；否则 `capacity_mw: null`。

负面控制查询：
```text
"St Helena" (colocation OR colo OR "carrier-neutral" OR "tier 3" OR "tier 4") -"St Helena Sound" -"Napa"
"St Helena" (VPS OR "cloud hosting" OR "dedicated server") -"Saint Helena Island"
"Ascension Island" (AWS OR Azure OR "Google Cloud" OR OCI OR GCP)
"St Helena" (AWS OR Azure OR "Google Cloud" OR GCP) ("region" OR "availability zone")
"SH" "data center" -"St Helena" -"Ascension" -"Tristan"
```

---

## 4. 三分区枚举矩阵（Enumeration matrix）

| 分区 | 官方/运营商（A 路由） | 连接/海缆（A/B 路由） | 行业媒体（B 路由） | 目录/社交（C 路由） | 当前期望产出 |
|---|---|---|---|---|---|
| **Ascension** | AIG、Omnitouch/Sure 转换公告、AIG procurement/public documents | 无公开新海缆；卫星/移动通信；军事通信不公开 | The Islander、UK MoD/BBC/USSF 公开报道 | 目录多为误标 | 阴性为主；电信转换记录为通信事实；无 DC |
| **Saint Helena** | SHG + Gazette、Sure、Connect、Companies House | Equiano / MCLS / SLTE / Rupert's landing | SAMS、DCD、Developing Telecoms、Capacity、SubTel Forum | 目录/SEO 作种子 | 1 条确认 DC；Equiano landing station 连接记录；Teleport/earth-station 线索 |
| **Tristan da Cunha** | TDG/tristandc.com | Starlink + VSAT；无海缆 | 极少量外部报道 | 目录误标 | 阴性；IT Container/Starlink 是通信线索，非 DC |

### 4.1 Ascension 查询配方
```text
"Ascension Island" ("data centre" OR "data center" OR datacenter OR "server room" OR hosting OR colocation)
site:ascension.gov.ac (telecom OR telecommunications OR communications OR "data" OR tender OR procurement)
site:ascension.gov.ac (Omnitouch OR Sure OR "4G mobile" OR "telecommunications provider")
"Ascension Island" ("submarine cable" OR "landing station" OR fibre OR satellite)
"Ascension" (USSF OR "Space Force" OR RAF OR BBC) (communications OR "earth station" OR satellite)
```

### 4.2 Saint Helena 查询配方
```text
("Saint Helena" OR "St Helena") ("data centre" OR "data center" OR datacenter OR "server room" OR hosting OR colocation OR teleport)
("Saint Helena" OR "St Helena") (Equiano OR "submarine cable" OR "landing station") (Rupert OR Google OR Sure OR SLTE OR MCLS)
site:sainthelena.gov.sh ("data centre" OR Equiano OR teleport OR "submarine cable" OR electricity OR UPS)
site:sure.co.sh (business OR enterprise OR "landing station" OR Equiano OR hosting OR colocation)
site:connect.co.sh (generation OR solar OR battery OR "power station" OR "Carnarvon Court")
"Carnarvon Court" ("data centre" OR Schneider OR battery OR backup)
```

### 4.3 Tristan da Cunha 查询配方
```text
"Tristan da Cunha" ("data centre" OR "data center" OR datacenter OR server OR hosting OR colocation)
"Tristan da Cunha" (internet OR satellite OR VSAT OR Starlink OR broadband OR telecom)
site:tristandc.com (internet OR satellite OR VSAT OR Starlink OR telecom OR "IT Container" OR "Communications HQ")
```

---

## 5. 种子记录（Seed records to validate during enumeration）

| 种子 | 状态 | 容量 | 开发/运营主体 | 等级 | 使用来源 |
|---|---|---|---|---|---|
| SHG Main Data Centre, Carnarvon Court, Jamestown | operational；2022-03-07 调试证据 | null | St Helena Government | **A** | SHG 发布 + Gazette EX-GAZ-9 |
| Connect Saint Helena core equipment at Carnarvon Court | operational utility core equipment | null | Connect Saint Helena | A 对设备事实；C 对 DC | SHG 2022 Schneider 页面；Connect 官网 |
| Equiano MCLS / Cable Landing Station / SLTE, Rupert's | landed 2021；SLTE live 2023 | null | SHG/Google/Sure/Telecom Egypt/ASN 等 | A 连接事实；非 DC | SHG fibre hub、SHG commissioning、Google blog |
| SHG Teleport & Data Centre services（2020 EOI） | historical procurement/service requirement | null | SHG | C+/A 对 EOI 存在 | SHG EOI 页面；后续采购搜索 |
| OneWeb / satellite earth-station lead | lead | null | OneWeb/Sure/SHG（需回核） | B/C | DCD/SHG 文件；非 DC |
| AIG / Omnitouch telecom transition | service transition 2026 | null | AIG / Omnitouch / Sure | A 电信事实；非 DC | AIG announcement |
| Ascension military/BBC communications | non-public communications | null | UK/US/BBC | 阴性边界 | 不作 DC，除非一手证据明确 |
| Tristan IT Container / Starlink + VSAT | satellite communications | null | TDG / SpaceX Starlink / existing VSAT provider | A 通信事实；非 DC | TDG 2024 Starlink update |

---

## 6. 容量与信度提取（Capacity & reliability extraction）

记录字段优先级：设施名、运营/所有主体、地址、manifest 分区、自然子层、状态、evidence_date、证据 URL、是否连接/登陆站、是否云区域、容量/认证。

不得从以下内容推导容量：
- Equiano 带宽、Google/EDF/FCDO 资金、海缆建设成本。
- Connect Saint Helena 发电规模、PPP/公用事业资产价值、电价。
- Starlink/VSAT 带宽、mobile 4G 覆盖。
- “world class”、“digital economy”、“teleport”、“hosting service” 等营销语句。

容量查询模板：
```text
("Saint Helena" OR "St Helena") ("data centre" OR datacenter) (rack OR racks OR MW OR kW OR capacity OR Tier)
"Carnarvon Court" (capacity OR racks OR MW OR kW OR battery OR Schneider)
"St Helena" teleport (capacity OR racks OR MW OR colocation)
"Equiano" "St Helena" (capacity OR bandwidth OR landing)
```

分级规则：
- **A**：证明设施/地址/状态/合同/许可的官方、运营方、厂商自控页或认证注册处。
- **B**：可靠媒体/行业报道，适合补足时间线与线索，但设施入库仍需一手回核。
- **C**：目录、社交、SEO、无地址托管页、无法回核的承包商作品集。

陷阱：
- Rupert's landing station 与 Jamestown Carnarvon Court 是两个地点。
- Google 海缆不等于 GCP 区域。
- Ascension 军事/广播/卫星设施不等于 DC。
- Tristan Starlink/VSAT/IT Container 不等于 DC。
- 小市场宁可明确阴性，也不要把通信节点扩展成数据中心。
