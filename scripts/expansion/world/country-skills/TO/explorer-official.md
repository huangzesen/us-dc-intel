# TO Explorer Official - 汤加官方/监管渠道数据中心枚举方法论
# Tonga (TO) Datacenter Enumeration via Official / Regulatory Sources

> 范围（Scope）：汤加王国（Kingdom of Tonga, TO）。按 `world-manifest.jsonl`，分区（division）必须且仅为：`'Eua`、`Ha'apai`、`Niuas`、`Tongatapu`、`Vava'u`。
> 视角（Angle）：官方、监管、国有企业、采购和多边项目文件，用于发现运营中、规划中和误报（false positive）的数据中心/电信设施候选。
> 语言（Language）：中文为主、英文术语双语；查询模板（query templates）以英文执行。

## 0. 已核实基线（Verified Baseline）

- 未发现汤加有公开的数据中心注册库（data center registry）或数据中心专属牌照。电信监管/通信许可可以确认运营商存在和服务授权，但**许可不等于数据中心设施**。
- 监管/公开登记的当前优先入口是 **Communications Commission Tonga (CCT)**：`https://www.cct.gov.to/publications`。该页列出 public register / licensed operators，包括 Digicel Tonga、Tonga Cable Limited、Tonga Communications Corporation (TCC)、Starlink Tonga、Wantok Tonga、Fiber Pacific，并列出 Annual Report 2024-2025、Strategic Plan 2023-2027、Spectrum Management Framework、Licensing Fees 2024 等文件。
- `https://www.tcc.to/` 是 **Tonga Communications Corporation (TCC)**，即国有电信运营商/服务商，不是监管机构。旧稿中把 `tcc.to` 当作监管来源的写法需避免；监管/许可用 `cct.gov.to` 与 `communications.gov.to` 历史 MEIDECC 页面交叉核对。
- 政府数字化存在明确官方/多边文件锚点。Digital Transformation Department (DTD, Prime Minister's Office) 发布 Digital Government Strategic Framework、Tonga Enterprise Architecture Framework、Tonga Data Exchange Policy、National Cybersecurity Framework、Cloud First Policy 等；World Bank `Tonga Digital Government Support Project (P154943)` ICR 提到 Component 4 从 secure government network / data center / G-Cloud 设计调整为 whole-of-government integration platform and data centers' upgrade。
- PMO 2025-06-10 关于政府门户的澄清声明称政府数据仍托管在汤加 Government Data Center；这是一手信号，但未披露场址、容量、运营模式或可商业托管性。记录时使用 `government_data_center_project` / `government_internal_data_center`，默认分区为 Tongatapu，除非官方文件给出不同地点。
- 汤加最强设施级资产是海缆着陆站（cable landing stations），但默认记录为 `telecom_cable_station`，不是零售 colocation / commercial data center。只有 RIO、FAA、服务目录或合同明确支持客户设备接入、机架、托管、互联时，才可附加 `colo_adjacent_telecom`。
- 2026 年新增/完成的第二国际海缆为 **Tonga Hawaiki Cable Branch System**。AIFFP 与澳大利亚外长新闻稿说明该 405 km 分支接入 Vava'u 的既有着陆站，2026-03 landed、2026-05 completed。它增强 Vava'u 电信设施等级，但仍不是数据中心。
- Niuas 未见海缆着陆或官方数据中心/机房项目锚点；主要按卫星/应急连接（satellite-only connectivity）处理，预期无设施级候选。

## 1. 信度分级（Reliability Grades）

- **A（官方/一手）**：CCT official register / public records；MEIDECC/Department of Communications 公告；PMO/DTD 政策、新闻和项目文件；Tonga Communications Corporation、Tonga Cable Limited、Tonga Power Limited 等官方运营主体页面；Tonga Registry Service；World Bank/ADB/AIFFP/DFAT 项目和完成文件；AWS/Azure/Google/Oracle 官方区域页。
- **B（强二级）**：Matangi Tonga、RNZ Pacific、Kaniva Tonga、Islands Business、Data Center Dynamics、Submarine Networks、TeleGeography 等具名、可追溯、日期清楚的报道或行业说明。
- **C（弱/聚合）**：Submarine Cable Map、PeeringDB、Cloudscene、DataCenterMap、datacenters.com、LinkedIn、社交媒体转述、SEO VPS/hosting 页、无署名市场报告。只能作线索或负面控制；不得单独确立设施存在。

## 2. 官方来源优先级（Official Source Priority）

### 2.1 监管与许可：CCT / MEIDECC Communications

优先入口：

- CCT public records：`https://www.cct.gov.to/publications`
- Department of Communications / MEIDECC 历史监管公告：`https://communications.gov.to/`
- 监管立法、license rules、gazette notice 与 annual report 下载项按 CCT/MEIDECC 页面实际链接保存。

用途：

- 枚举持牌电信/ISP/卫星/海缆运营者；确认 Starlink、Tonga Cable、TCC、Digicel 等合法服务状态。
- 查找 RIO、facility access、interconnection、spectrum、licensing fee、annual statistics 等与设施接入相关的文件。
- 任何 `tcc.to` 命中应先判断是否为 Tonga Communications Corporation 运营商页面，不要当监管证据。

```text
site:cct.gov.to (license OR licence OR licensee OR "official register" OR "public register" OR "annual report")
site:cct.gov.to (Tonga Cable OR "Tonga Communications Corporation" OR Digicel OR Starlink OR Wantok OR "Fiber Pacific")
site:cct.gov.to (RIO OR "reference interconnection offer" OR interconnection OR "facility access" OR "spectrum")
site:communications.gov.to (Starlink OR satellite OR VSAT OR "submarine cable" OR licence OR license OR regulation)
"Communications Commission Tonga" ("data centre" OR "data center" OR datacenter OR hosting OR colocation OR IXP)
```

### 2.2 政府数字化：PMO / DTD / MEIDECC / Finance

优先入口：

- PMO：`https://pmo.gov.to/`
- Digital Transformation Department：`https://digitaltransformation.gov.to/frame-works-and-policy/`
- MEIDECC：`https://www.meidecc.gov.to/` 与 `https://communications.gov.to/`
- Ministry of Finance：`https://www.finance.gov.to/`
- World Bank Documents：`https://documents.worldbank.org/`

用途：

- 查找 Government Data Center、data centers' upgrade、G-Cloud、secure government network、data exchange、interoperability、backup/DR、procurement 等证据。
- PMO/DTD/World Bank 可确立公共部门内部数据中心线索；但在缺少地址、机房属性、容量和运营主体时，不应写成商业 colo。
- Cloud First Policy 明确要求政府新 IT 投资优先考虑云，并限制各实体新建独立 data center/server/storage/network/UPS 基础设施；这支持“集中/共享政府基础设施”而非分散商业 DC 市场。

```text
site:pmo.gov.to ("Government Data Center" OR "data centre" OR "data center" OR "data hosting" OR "government portal")
site:digitaltransformation.gov.to ("data center" OR "data centre" OR "G-Cloud" OR "Cloud First" OR "Data Exchange" OR interoperability)
site:meidecc.gov.to ("data center" OR "data centre" OR "digital government" OR ICT OR "e-government")
site:finance.gov.to (tender OR procurement OR RFP OR "data center" OR "data centre" OR server OR ICT)
site:documents.worldbank.org Tonga P154943 ("data center" OR "data centre" OR "G-Cloud" OR "Digital Government")
```

### 2.3 国有电信与海缆运营主体

优先入口：

- Tonga Communications Corporation：`https://www.tcc.to/`
- Tonga Cable Limited：`https://www.tongacable.to/`（站点可访问性/证书状态需实跑确认；若证书异常，用 CCT register、AIFFP、ADB/WB、Submarine Networks 等交叉核对）
- CCT register 中的 Tonga Cable / TCC 条目
- AIFFP Tonga Hawaiki page：`https://www.aiffp.gov.au/investments/investment-list/expanding-digital-connectivity-tonga-second-international-undersea-cable`
- Australian Foreign Minister 2026-05-26 release：`https://www.foreignminister.gov.au/minister/penny-wong/media-release/strengthening-tongas-connectivity-second-international-undersea-cable-complete`

用途：

- Tonga Cable / Tonga-Fiji：Nuku'alofa/Sopu, Tongatapu 的国际海缆着陆设施，记录为 `telecom_cable_station`。
- Tonga Domestic Cable Extension：连接 Tongatapu、Ha'apai、Vava'u；常见官方/项目文件锚点为 Nuku'alofa、Pangai、Neiafu。若出现 `'Eua`/`'Ohonua` 国内连接说法，必须用官方运营商、采购或工程文件核实后再记录。
- Tonga Hawaiki Cable Branch System：Vava'u 既有着陆站的第二国际海缆接入，记录为 `telecom_cable_station` / redundancy signal。
- TCC 运营商核心网、交换、NOC、hosting/enterprise 服务只在一手资料点名设施时记录。

```text
site:tcc.to (hosting OR server OR cloud OR business OR enterprise OR NOC OR switch OR "data")
site:tongacable.to (landing OR "cable station" OR RIO OR "facility access" OR interconnection OR Nuku'alofa OR Neiafu OR Pangai OR Vava'u)
"Tonga Cable Limited" ("landing station" OR "cable station" OR RIO OR Nuku'alofa OR Sopu OR Neiafu OR Pangai)
"Tonga Hawaiki Cable Branch System" (Vava'u OR "landing station" OR completed OR Tonga Cable)
site:aiffp.gov.au Tonga Hawaiki Vava'u "landing station"
```

### 2.4 电力与大负荷核查：Tonga Power

优先入口：

- Tonga Power：`https://www.tongapower.to/`
- Tonga Power downloads / annual reports：`https://www.tongapower.to/downloads`

用途：

- 汤加岛屿电网规模较小，任何 >0.5 MW 或“hyperscale/large data center”声称必须找到 Tonga Power、项目融资、环境审批或政府公告证据。
- 太阳能、BESS、substation、grid upgrade 是能源资产，不是 DC；除非明确服务数据中心负荷。

```text
site:tongapower.to ("data center" OR "data centre" OR datacenter OR "large load" OR "large customer" OR industrial OR MW)
site:tongapower.to (Nuku'alofa OR Neiafu OR Pangai OR "'Ohonua" OR Tongatapu OR Vava'u OR Ha'apai OR "'Eua") (grid OR power OR generation OR substation)
"Tonga Power" ("data center" OR "data centre" OR "large load" OR MW OR "connection")
```

### 2.5 公司与项目载体核实（Company / Legal Entity）

优先入口：

- Tonga Registry Service entity search：`https://businessregistries.gov.to/corp/search.aspx?lang=en-US`

用途：

- 核实声称在汤加运营的 hosting、ICT、telecom、foreign investment 项目载体。
- 注册处命中是法人存在 A 级证据，不是设施证据。

```text
site:businessregistries.gov.to "{CompanyName}"
"{CompanyName}" Tonga (registered OR incorporated OR "business registry" OR "foreign investment")
"Tonga Registry Service" ("Tonga Cable" OR "Tonga Communications Corporation" OR Digicel OR hosting OR "data center")
```

### 2.6 官方云区域缺位（Cloud Region Absence）

仅使用官方区域页核查：

- AWS regions / Local Zones：`https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`
- Azure regions：`https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- Google Cloud locations：`https://cloud.google.com/about/locations` 与 `https://datacenters.google/locations/`
- Oracle OCI public regions：`https://www.oracle.com/cloud/public-cloud-regions/`

```text
"Tonga" ("AWS Region" OR "AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "OCI region")
site:aws.amazon.com Tonga "Local Zone"
site:learn.microsoft.com Tonga "Azure region"
site:cloud.google.com Tonga "region"
site:oracle.com Tonga "cloud region"
```

截至本次核查，未见 AWS/Azure/Google Cloud/Oracle OCI 在 TO 的官方公共云区域、Local Zone 或自有数据中心页。不得把 reseller、edge CDN、satellite internet 或 VPS SEO 页面升级为本地云区域。

## 3. 当前官方种子清单（Official Seed List）

| 候选（Candidate） | 分区（Division） | 状态（Status） | 等级（Grade） | 记录方式（How to record） |
|---|---|---|---|---|
| Government Data Center / data centers' upgrade | Tongatapu（默认；具体场址未披露） | PMO/DTD/World Bank 证实存在或升级语境；非商业 colo | A（存在/项目） | `government_internal_data_center` 或 `government_data_center_project`；不写容量、不写精确地址，除非后续官方披露。 |
| Tonga Cable / Tonga-Fiji cable landing facility | Tongatapu（Nuku'alofa/Sopu 区域） | 运营中 | A/B | `telecom_cable_station`；TCL/项目文件为锚点；不默认 retail DC。 |
| Tonga Domestic Cable landing: Nuku'alofa | Tongatapu | 运营中/国内连接节点 | A/B | `telecom_cable_station`；用 Tonga Cable、ADB/WB、CCT 或工程文件核实。 |
| Tonga Domestic Cable landing: Pangai/Lifuka | Ha'apai | 运营中/国内连接节点 | A/B | `telecom_cable_station`；小型外岛设施。 |
| Tonga Domestic Cable landing: Neiafu | Vava'u | 运营中/国内连接节点；2026 Hawaiki branch 接入既有 Vava'u 着陆站 | A | `telecom_cable_station`；Vava'u 最强设施级候选。 |
| Potential `'Eua` / `'Ohonua` cable or network facility | `'Eua` | 仅作待核线索，需官方工程/RIO/采购文件确认 | B/C until verified | 不因聚合地图或未署名文本直接入库；确认后才列 `telecom_cable_station`。 |
| TCC / Tonga Communications Corporation network core, gateway, NOC, hosting | Tongatapu | 国有运营商网络基础设施；设施属性待证 | 运营商 A；设施 B/C | 仅当 TCC 官方或项目文件点名 NOC/server/hosting/colo 时记录。 |
| Digicel Tonga / Wantok / Fiber Pacific / Starlink | 主要 Tongatapu；Starlink 全国 | 持牌/登记服务商 | A（服务/牌照）；非 DC | 连接服务与网络资产；不推断数据中心。 |
| Niuas satellite connectivity | Niuas | 无海缆/无 DC 锚点 | A/B（连接）；非 DC | `no_facility_found` / satellite-only negative control。 |

## 4. 分区枚举策略（Per-Division Strategy）

通用扫描（`{Division}` 替换为 manifest 精确值）：

```text
"{Division}" Tonga ("data centre" OR "data center" OR datacenter OR colocation OR hosting OR "server room" OR "cable station" OR "landing station" OR fibre OR fiber OR broadband OR ICT)
site:cct.gov.to "{Division}" (telecommunications OR internet OR broadband OR cable OR electricity)
site:communications.gov.to "{Division}" (telecommunications OR internet OR broadband OR cable OR Starlink OR satellite)
site:digitaltransformation.gov.to "{Division}" (ICT OR digital OR "data center" OR "data centre" OR hosting)
site:finance.gov.to "{Division}" (tender OR procurement OR ICT OR "data center" OR "data centre")
site:tongapower.to "{Division}" (grid OR power OR generation OR substation)
```

| 分区（Division） | 预期产出 | 官方优先路线 | 归属规则 |
|---|---|---|---|
| Tongatapu | 最高 | PMO/DTD Government Data Center；CCT register；TCC/TongaTel/Tonga Cable；Tonga-Fiji/Nuku'alofa landing；Tonga Power；registry | Nuku'alofa、Sopu、Ma'ufanga、Vuna Road、St George Building 等默认 Tongatapu；政府/运营商总部默认 Tongatapu，除非源另有地点。 |
| Vava'u | 中 | AIFFP/DFAT/Tonga Cable Hawaiki branch；Neiafu/Vava'u landing；CCT；Tonga Power | Neiafu 是唯一强非 Tongatapu 设施级候选；Hawaiki branch 只增强电信冗余，不升级为 DC。 |
| Ha'apai | 低 | Tonga Domestic Cable Pangai/Lifuka；CCT/MEIDECC outage/project notices；Tonga Power | Pangai/Lifuka 着陆站可作为小型 `telecom_cable_station`；无 hosting/DC 证据时不记录数据中心。 |
| `'Eua` | 极低到低 | 仅在官方工程/采购/RIO 证据出现时核实 `'Ohonua` 或其他网络设施；Tonga Power | 旧稿关于 `'Ohonua` 着陆站须降级为待核线索，除非找到一手锚点。 |
| Niuas | 极低 | CCT/MEIDECC satellite/Starlink/Kacific/VSAT；Tonga Power 外岛电力 | Niuatoputapu、Niuafo'ou 连接线索不产生设施；默认 `no_facility_found`。 |

覆盖检查（Coverage check）：上表恰好覆盖 manifest 的 5 个分区各一次。

## 5. 误报与分级规则（False Positives And Grading Rules）

- **着陆站 ≠ 数据中心**：海缆着陆站是设施级电信资产，但不是零售数据中心；除非一手来源明确说明 rack/colo/hosting/interconnection 服务。
- **政府 DC ≠ 商业 DC**：Government Data Center 和 data centers' upgrade 是公共部门内部设施/项目；无商业服务证据时不得列为 colocation provider。
- **许可 ≠ 设施**：CCT 许可/登记证明服务授权，不证明机房、NOC、交换站或数据中心。
- **运营商网页 ≠ 设施**：TCC/Digicel/Wantok/Fiber Pacific 的 broadband、mobile、enterprise connectivity 页面不自动产生 DC 候选。
- **卫星/Starlink**：Starlink、Kacific、VSAT、emergency telecom terminals 是连接资产；不记录为数据中心。
- **VPS/SEO**：`Tonga VPS`、`Nuku'alofa dedicated server`、`Pacific cloud` 等无本地物理场址、无注册/许可锚点时为 C 级负面控制。
- **电力负荷**：任何 >0.5 MW 声称必须有 Tonga Power、政府项目、环境审批或多边融资证据；否则判为不可信。
- **拼写污染**：`'Eua` 不等于 Eurasia；`Tonga` 与 Samoa/American Samoa/Fiji 项目严格区分；`TCC` 需区分 regulator 旧称/语境与 Tonga Communications Corporation。

## 6. 来源速查（Source Quick List）

- CCT public register / publications：`https://www.cct.gov.to/publications`
- MEIDECC Department of Communications：`https://communications.gov.to/`
- Prime Minister's Office：`https://pmo.gov.to/`
- Digital Transformation Department policies：`https://digitaltransformation.gov.to/frame-works-and-policy/`
- World Bank Documents：`https://documents.worldbank.org/`（重点 `Tonga Digital Government Support Project P154943`）
- Tonga Communications Corporation：`https://www.tcc.to/`
- Tonga Cable Limited：`https://www.tongacable.to/`
- AIFFP Tonga Hawaiki project：`https://www.aiffp.gov.au/investments/investment-list/expanding-digital-connectivity-tonga-second-international-undersea-cable`
- Australian Foreign Minister completion release：`https://www.foreignminister.gov.au/minister/penny-wong/media-release/strengthening-tongas-connectivity-second-international-undersea-cable-complete`
- Tonga Power：`https://www.tongapower.to/` and `https://www.tongapower.to/downloads`
- Tonga Registry Service：`https://businessregistries.gov.to/corp/search.aspx?lang=en-US`

刷新说明（Refresh instruction）：每次实跑前重新核对 CCT register/publications、MEIDECC communications 公告、PMO/DTD digital government 页面、World Bank P154943 最新 ICR/采购文件、Tonga Cable/TCC 官网、Tonga Power 年报和官方云区域页；只有来源升级后才改变设施状态。
