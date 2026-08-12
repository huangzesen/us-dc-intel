# TO Explorer Industry - 汤加行业/厂商渠道数据中心枚举方法论
# Tonga (TO) Datacenter Enumeration via Industry / Vendor / Trade Sources

> 范围（Scope）：汤加王国（Kingdom of Tonga, TO）。按 `world-manifest.jsonl`，分区（division）必须且仅为：`'Eua`、`Ha'apai`、`Niuas`、`Tongatapu`、`Vava'u`。
> 视角（Angle）：行业媒体、运营商、海缆、卫星、云/托管厂商和目录站，用于发现商业数据中心、托管/colo、电信设施、海缆着陆站、云信号与误报。
> 语言（Language）：中文为主、英文术语双语；查询模板含英文与少量汤加语（lea faka-Tonga）召回辅助。

## 0. 行业基线（Industry Baseline）

- 未发现汤加有公开销售的中立机架托管（neutral rack colocation）、tiered commercial data center 或 hyperscale capacity 市场。行业枚举重点应放在“是否存在设施级电信/政府机房”，而不是假设有 colo 市场。
- 设施级强信号集中在 Tongatapu/Nuku'alofa/Sopu 与 Vava'u/Neiafu。Tongatapu 有 Tonga-Fiji 国际海缆着陆和政府/运营商核心设施线索；Vava'u 有既有着陆站和 2026 Tonga Hawaiki Cable Branch System；Ha'apai 有 Pangai/Lifuka 国内海缆节点；`'Eua` 相关说法需一手工程/运营资料确认；Niuas 以卫星连接为主。
- 2026 年的 Tonga Hawaiki Cable Branch System 是重要行业更新：AIFFP/澳大利亚外长稿称 405 km 分支接入 Vava'u 既有 cable landing station，并于 2026-05 宣布完成。这是 `telecom_cable_station`/network redundancy 信号，不是 data center。
- PMO/DTD/World Bank 对 Government Data Center / data centers' upgrade 有一手锚点，但它是公共部门内部数字政府基础设施，不是商业 colo 信号。
- Starlink、Kacific、VSAT、移动核心网、塔站、Wi-Fi、submarine landing station 和 broadband/enterprise connectivity 都是连接或电信资产；除非厂商一手资料明确写 rack、colocation、server hosting、DR、compute hosting 或 interconnection facility，否则不计为数据中心。

## 1. 信度分级（Reliability Grades）

- **A（一手/官方/厂商官方）**：CCT public register；MEIDECC/PMO/DTD；Tonga Communications Corporation `tcc.to`；Tonga Cable Limited；Digicel Pacific/Telstra official pages；Starlink/Kacific official service pages；Tonga Power；Tonga Registry Service；World Bank/ADB/AIFFP/DFAT；官方云厂商区域页。
- **B（强二级）**：Matangi Tonga、RNZ Pacific、Kaniva Tonga、Islands Business、Data Center Dynamics、Capacity Media、Submarine Networks、TeleGeography 等具名、日期明确、内容可交叉核验的报道。
- **C（弱/聚合）**：Submarine Cable Map、Cloudscene、DataCenterMap、datacenters.com、PeeringDB、LinkedIn、社交媒体截图、VPS/hosting SEO 页、无署名市场报告。C 级只能生成 lead 或 negative control。

## 2. 行业来源地图（Industry Source Map）

| 来源/参与方（Source / player） | URL | 用途（Use） | 等级 |
|---|---|---|---|
| CCT public register | `https://www.cct.gov.to/publications` | 持牌/登记运营商锚点：Digicel Tonga、Tonga Cable Limited、TCC、Starlink Tonga、Wantok Tonga、Fiber Pacific 等 | A |
| Tonga Communications Corporation (TCC) | `https://www.tcc.to/` | 国有电信运营商；fixed/mobile/internet/business 服务；不要误当监管机构 | A（运营商）/ B-C（设施推断） |
| Tonga Cable Limited | `https://www.tongacable.to/` | Tonga-Fiji、domestic cable、Hawaiki branch 运营线索；站点证书/可访问性需实跑确认 | A if reachable / B with AIFFP-ADB-WB support |
| AIFFP / DFAT | AIFFP project page, Australian Foreign Minister release | 2026 Hawaiki branch、Vava'u landing、completion status | A |
| PMO / Digital Transformation Department | `https://pmo.gov.to/`, `https://digitaltransformation.gov.to/` | Government Data Center、G-Cloud、data exchange、digital government 项目 | A |
| World Bank / ADB | `https://documents.worldbank.org/`, `https://www.adb.org/` | P154943 digital government、Tonga-Fiji/海缆项目文件、采购和完成报告 | A |
| Digicel Pacific / Telstra | `https://www.digicelpacific.com/`, Telstra announcements | 移动/企业连接和 Telstra-Digicel Pacific 所有权背景 | A（运营商）/ B-C（设施推断） |
| Starlink / Kacific | `https://www.starlink.com/`, `https://kacific.com/` | 卫星服务覆盖与外岛连接；负面控制 | A（服务）/ 非 DC |
| Tonga Power | `https://www.tongapower.to/` | 大负荷可行性与电网痕迹核查 | A |
| Matangi Tonga / Kaniva / RNZ Pacific / Islands Business | local/regional media | 电信 outage、海缆、卫星、政府 ICT 新闻 | B |
| DCD / Capacity / Submarine Networks / TeleGeography | industry press | 海缆与区域基础设施报道；DCD 2026 Hawaiki landing 可作行业锚点 | B |
| Submarine Cable Map / Cloudscene / DataCenterMap / PeeringDB | directories | 路由、ASN、目录线索和误报控制 | C |

## 3. 厂商与运营商扫描（Operator And Vendor Sweep）

### 3.1 海缆：Tonga Cable / Hawaiki / Domestic Cable

```text
"Tonga Cable Limited" ("data center" OR "data centre" OR colocation OR hosting OR "facility access" OR RIO OR "landing station" OR "cable station")
"Tonga-Fiji" OR "Tonga Fiji cable" (Nuku'alofa OR Sopu OR Suva) ("landing station" OR RFS OR capacity OR "cable station")
"Tonga Domestic Cable" (Neiafu OR Pangai OR Nuku'alofa OR Lifuka OR Vava'u OR Ha'apai) ("landing station" OR "cable station" OR RFS)
"Tonga Hawaiki Cable Branch System" (Vava'u OR Neiafu OR "landing station" OR completed OR landed)
site:aiffp.gov.au Tonga Hawaiki Vava'u "landing station"
site:datacenterdynamics.com Tonga Hawaiki cable lands Vava'u
```

处理规则：

- Tonga-Fiji / Nuku'alofa-Suva：`telecom_cable_station`，不是 DC。
- Tonga Hawaiki / Vava'u：`telecom_cable_station` 与 resiliency signal，不是 DC。
- Domestic Cable / Pangai / Neiafu / Nuku'alofa：按官方或强二级资料记录；仅有聚合地图时标 C lead。
- `'Eua` / `'Ohonua`：只有找到官方工程/RIO/采购/运营页面后才升级。

### 3.2 TCC / Tonga Communications Corporation

```text
site:tcc.to (hosting OR server OR cloud OR enterprise OR business OR NOC OR switch OR "data" OR backup)
"Tonga Communications Corporation" ("data center" OR "data centre" OR datacenter OR hosting OR colocation OR server OR cloud OR NOC OR gateway)
"TCC" Tonga ("NOC" OR "network operations" OR "gateway" OR "data services" OR hosting)
```

处理规则：

- `tcc.to` 是运营商官网；可确认服务商和业务类型。
- Broadband/mobile/fixed line/enterprise connectivity 不足以确立 DC。
- 只有官方或 B 级来源明确指向 NOC、gateway、server hosting、managed hosting、colo 或 DR facility 时，才建立设施候选；默认地点 Tongatapu/Nuku'alofa。

### 3.3 Digicel Tonga / Telstra Pacific

```text
site:digicelpacific.com Tonga (enterprise OR business OR cloud OR hosting OR network OR "data")
"Digicel Tonga" ("data center" OR "data centre" OR datacenter OR NOC OR switch OR hosting OR cloud OR server OR enterprise)
"Telstra" "Digicel Pacific" Tonga (network OR enterprise OR cloud OR data)
```

处理规则：

- Telstra/Digicel 官方页可确认所有权和服务背景。
- 移动核心网/交换机房只有在来源点名 facilities、hosting 或 colocation 时才升级；否则为 operator infrastructure lead。

### 3.4 Wantok Tonga / Fiber Pacific / One.Tel / 其他 ISP

```text
site:cct.gov.to (Wantok OR "Fiber Pacific" OR "One.Tel" OR licensee OR licence OR license)
"Wantok Tonga" (hosting OR server OR "data center" OR "data centre" OR broadband OR ISP)
"Fiber Pacific" Tonga (hosting OR server OR "data center" OR "data centre" OR broadband OR ISP)
"One.Tel" Tonga ("data center" OR "data centre" OR hosting OR server OR broadband OR mobile)
```

处理规则：

- 先用 CCT register 确认服务商身份。
- ISP、wireless、tower、retail internet 不推断为 DC。
- 如果官网不可访问或只有社交页，最多 C/B lead，需注册/许可和设施页双锚点。

### 3.5 Starlink / Kacific / Satellite

```text
site:communications.gov.to (Starlink OR satellite OR VSAT OR "temporary permit" OR approval)
site:cct.gov.to (Starlink OR satellite OR VSAT)
"Starlink" Tonga (approved OR launch OR licence OR license OR permit OR reseller)
"Kacific" Tonga (Niuas OR Vava'u OR Ha'apai OR satellite OR broadband OR emergency)
```

处理规则：

- Starlink 在汤加的监管许可/批准是 A 级连接服务证据。
- Kacific/VSAT/ETC emergency telecom 是连接/韧性资产。
- 对 Niuas 特别有用，但不产生 data center/colo 设施。

### 3.6 政府 ICT 与银行/企业机房

```text
"Government Data Center" Tonga (PMO OR DTD OR "Digital Transformation Department" OR "data hosting")
"Tonga Digital Government Support Project" ("data center" OR "data centres" OR "G-Cloud" OR "data centers' upgrade")
"National Reserve Bank of Tonga" OR "Bank of Tonga" OR "Tonga Development Bank" ("data center" OR "data centre" OR "disaster recovery" OR server OR hosting)
"Tonga" bank ("data center" OR "data centre" OR "disaster recovery" OR backup OR server room) Nuku'alofa
```

处理规则：

- 政府数据中心：A 级公共部门设施/项目，可记录但不得写为商业 colo。
- 银行/企业 server room、DR、backup 只有一手报告或采购文件时进入候选；一般为 Tongatapu。

## 4. 汤加语/混合召回（Tongan / Mixed-Language Recall）

> 汤加语词表仅为召回辅助，不作为语言学或设施证据。正式记录仍需英文/官方文件锚点。

| 中文 | English | Tongan / mixed recall |
|---|---|---|
| 数据/信息 | data / information | fakamatala |
| 计算机 | computer | komipiuta |
| 互联网 | internet | initaneti / ʻinitaneti |
| 服务器 | server | server / seva / sēvā |
| 通信 | communications | fetu'utaki / fetuʻutaki |
| 电力 | electricity / power | uhila / ʻuhila |
| 分区 | division | vahenga |

```text
Tonga (fakamatala OR komipiuta OR initaneti OR "ʻinitaneti") ("data center" OR "data centre" OR server OR hosting)
Tonga (fetu'utaki OR fetuʻutaki) (server OR hosting OR "cable station" OR "landing station")
Nuku'alofa OR Neiafu OR Pangai OR Sopu (fakamatala OR initaneti OR server OR "data centre" OR "data center")
```

## 5. 枚举矩阵（Enumeration Matrix）

| 分区（Division） | 媒体/行业产出 | 厂商官方页产出 | 目录/聚合产出 | 预期设施级候选 |
|---|---|---|---|---|
| Tongatapu | 高：政府门户、TCC/Tonga Cable、outage、银行/企业 ICT | 高：TCC、Tonga Cable、Digicel、PMO/DTD | 中：Tonga-Fiji cable、ASN/PeeringDB、SEO VPS | Government Data Center；Nuku'alofa/Sopu cable landing；运营商核心设施线索 |
| Vava'u | 中：Hawaiki branch、Neiafu cable、outage/repair | 中：Tonga Cable/AIFFP/DFAT | 中：Hawaiki/Domestic cable maps | Neiafu/Vava'u cable landing station |
| Ha'apai | 低：Pangai/Lifuka domestic cable、outage | 低 | 低 | Pangai/Lifuka domestic cable node |
| `'Eua` | 极低：需具体 `'Ohonua`/`'Eua` 官方锚点 | 极低 | 低，易误报 | 待核网络设施；无锚点时 `no_facility_found` |
| Niuas | 低：Starlink/Kacific/VSAT/emergency comms | 低：satellite providers | 极低 | 无 DC；satellite-only negative control |

覆盖检查（Coverage check）：矩阵恰好覆盖 manifest 的 5 个分区各一次。

## 6. 玩家矩阵（Player Matrix）

| 玩家（Player） | 类型 | 主分区 | 设施证据 | 处理方式 |
|---|---|---|---|---|
| Government Data Center / DTD | 公共部门内部 ICT | Tongatapu（默认） | A（存在/项目），地址容量未披露 | `government_internal_data_center`；非 commercial colo |
| Tonga Cable Limited | 国际/国内海缆运营 | Tongatapu / Vava'u / Ha'apai | A/B | `telecom_cable_station`；Hawaiki branch 更新 Vava'u |
| Tonga Communications Corporation (TCC) | 国有电信运营商 | Tongatapu | A（运营商），B/C（设施） | 仅点名 NOC/hosting/gateway 时记录设施 |
| Digicel Tonga / Telstra Pacific | 移动/企业连接 | Tongatapu | A（运营商），B/C（设施） | 不从移动核心网推断 DC |
| Wantok Tonga / Fiber Pacific / One.Tel | ISP/连接 | Tongatapu 为主 | A（登记/牌照），C/B（设施） | 需官网+设施证据双锚点 |
| Starlink / Kacific | 卫星连接 | 全国，含 Niuas | A（服务/许可），非 DC | 负面控制 |
| Tonga Power | 公用事业 | 各供电岛 | A（电力） | 用于否定无电力痕迹的大负荷声称 |
| 境外 VPS/云转售 | reseller/SEO | 无 | C | 负面控制 |

## 7. 分级规则（Grading Rules）

- **升级规则**：C 级目录/地图/SEO 线索必须找到 A 或强 B 锚点；B 级报道必须与一手来源或实体页面一致，才能升级设施。
- **着陆站规则**：landing station 默认 `telecom_cable_station`；有 RIO/FAA/facility access/colo 文档才加 `colo_adjacent_telecom`。
- **政府规则**：Government Data Center 可作为公共部门设施记录，但不可扩写成商业托管或云区域。
- **运营商规则**：运营商存在、牌照、移动核心网、企业连接、IP transit 不证明数据中心。
- **电力规则**：>0.5 MW 声称需要 Tonga Power、项目融资、环境/建设许可或政府公告；无痕迹时降级/否定。
- **地域规则**：Nuku'alofa/Sopu/Ma'ufanga/Vuna Road 属 Tongatapu；Neiafu 属 Vava'u；Pangai/Lifuka 属 Ha'apai；Niuatoputapu/Niuafo'ou 属 Niuas；`'Eua` 需精确处理撇号和地名。
- **云区域规则**：官方 AWS/Azure/Google/OCI 页未列 TO 时，任何 “Tonga cloud region” 第三方页面按 C 级误报处理。

## 8. 来源速查（Source Quick List）

- 官方/监管：CCT `https://www.cct.gov.to/publications`；MEIDECC Communications `https://communications.gov.to/`；PMO `https://pmo.gov.to/`；DTD `https://digitaltransformation.gov.to/frame-works-and-policy/`。
- 运营商/厂商：TCC `https://www.tcc.to/`；Tonga Cable `https://www.tongacable.to/`；Digicel Pacific `https://www.digicelpacific.com/`；Starlink `https://www.starlink.com/`；Kacific `https://kacific.com/`。
- 项目/行业：World Bank Documents `https://documents.worldbank.org/`；ADB `https://www.adb.org/`；AIFFP Tonga Hawaiki project；DFAT / Australian Foreign Minister 2026 completion release；Submarine Networks；TeleGeography；Data Center Dynamics；Capacity Media。
- 本地/地区媒体：Matangi Tonga `https://matangitonga.to/`；Kaniva Tonga `https://kanivatonga.co.nz/`；RNZ Pacific `https://www.rnz.co.nz/pacific`；Islands Business `https://islandsbusiness.com/`。
- 目录/负面控制：Submarine Cable Map、Cloudscene、DataCenterMap、datacenters.com、PeeringDB、LinkedIn、VPS SEO pages。
- 注册/电力：Tonga Registry Service `https://businessregistries.gov.to/corp/search.aspx?lang=en-US`；Tonga Power `https://www.tongapower.to/`。

刷新说明（Refresh instruction）：每次实跑前重新核对过去 12 个月的 CCT register/publications、MEIDECC Starlink/VSAT 和海缆公告、Tonga Cable/TCC 官网、Hawaiki branch 状态、PMO/DTD 政府数据中心说明、World Bank/ADB 项目文件、Tonga Power 年报，以及官方云区域页。
