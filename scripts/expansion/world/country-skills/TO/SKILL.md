---
name: to-datacenter-methodology
location: scripts/expansion/world/country-skills/TO/SKILL.md
description: 汤加数据中心查询方法论（Tonga datacenter discovery & audit methodology）——双线来源（官方/监管/云管线 + 行业/厂商发现）与五分区模型下的设施枚举规则。
---

# TO · 汤加数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：汤加王国（Kingdom of Tonga, TO）——按 `world-manifest.jsonl`，分区（division）必须且仅为：**`'Eua`、`Ha'apai`、`Niuas`、`Tongatapu`、`Vava'u`**。双线方法论：`explorer-official.md`（官方/监管/云管线）与 `explorer-industry.md`（行业/厂商发现），均为 codex 审核定稿。语言：中文为主、英文术语双语；查询模板以英文执行，含少量汤加语（lea faka-Tonga）召回辅助。评审日期：2026-08-12。

## 入口

| 入口 | 管线 | 内容 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线 | 已核实基线（无 DC 注册库/无 DC 专属牌照、CCT 监管、TCC 身份澄清、政府数字化锚点、海缆登陆站默认电信设施、2026 Hawaiki 分支、Niuas 卫星-only）、信度分级、官方来源优先级（CCT/MEIDECC、PMO/DTD/MEIDECC/Finance、国有电信与海缆运营主体、Tonga Power、公司/法人载体、官方云区域缺位）、当前官方种子清单、分区枚举策略、误报与分级规则、来源速查 |
| `explorer-industry.md` | 行业/厂商发现 | 行业基线（无中立机架托管/无 tiered 商业 DC/hyperscale 市场）、信度分级、行业来源地图、厂商与运营商扫描（海缆/TCC/Digicel/Wantok/Starlink/政府 ICT 与银行机房）、汤加语/混合召回、枚举矩阵、玩家矩阵、分级规则、来源速查 |

## 核心结构事实

1. **行政区划模型**：5 个 manifest 分区：`'Eua`、`Ha'apai`、`Niuas`、`Tongatapu`、`Vava'u`。地域规则：Nuku'alofa/Sopu/Ma'ufanga/Vuna Road 属 Tongatapu；Neiafu 属 Vava'u；Pangai/Lifuka 属 Ha'apai；Niuatoputapu/Niuafo'ou 属 Niuas；`'Eua` 需精确处理撇号和地名（`'Eua` 不等于 Eurasia）。
2. **注册库现状**：未发现汤加有公开的数据中心注册库（data center registry）或数据中心专属牌照。电信监管/通信许可可以确认运营商存在和服务授权，但**许可不等于数据中心设施**。监管/公开登记的当前优先入口是 **Communications Commission Tonga (CCT)**：`https://www.cct.gov.to/publications`——该页列出 public register / licensed operators，包括 Digicel Tonga、Tonga Cable Limited、Tonga Communications Corporation (TCC)、Starlink Tonga、Wantok Tonga、Fiber Pacific，并列出 Annual Report 2024-2025、Strategic Plan 2023-2027、Spectrum Management Framework、Licensing Fees 2024 等文件。`https://www.tcc.to/` 是 **Tonga Communications Corporation (TCC)**（国有电信运营商/服务商），**不是监管机构**——旧稿中把 `tcc.to` 当作监管来源的写法需避免；监管/许可用 `cct.gov.to` 与 `communications.gov.to` 历史 MEIDECC 页面交叉核对。
3. **法律与监管**：监管立法、license rules、gazette notice 与 annual report 下载项按 CCT/MEIDECC 页面实际链接保存。CCT 许可/登记证明服务授权，不证明机房、NOC、交换站或数据中心；运营商网页（TCC/Digicel/Wantok/Fiber Pacific 的 broadband、mobile、enterprise connectivity 页面）不自动产生 DC 候选；Tonga Registry Service（`https://businessregistries.gov.to/corp/search.aspx?lang=en-US`）核实法人存在（A 级法人证据，不是设施证据）。
4. **互联与云**：汤加最强设施级资产是海缆登陆站（cable landing stations），但默认记录为 `telecom_cable_station`，不是零售 colocation / commercial data center；只有 RIO、FAA、服务目录或合同明确支持客户设备接入、机架、托管、互联时，才可附加 `colo_adjacent_telecom`。2026 年新增/完成的第二国际海缆为 **Tonga Hawaiki Cable Branch System**——AIFFP 与澳大利亚外长新闻稿说明该 405 km 分支接入 Vava'u 的既有登陆站，2026-03 landed、2026-05 completed；它增强 Vava'u 电信设施等级，但仍不是数据中心。Tonga Cable / Tonga-Fiji（Nuku'alofa/Sopu, Tongatapu 的国际海缆登陆设施）与 Tonga Domestic Cable Extension（连接 Tongatapu、Ha'apai、Vava'u，锚点 Nuku'alofa、Pangai、Neiafu）均按 `telecom_cable_station` 记录。官方云区域缺位：截至本次核查，未见 AWS/Azure/Google Cloud/Oracle OCI 在 TO 的官方公共云区域、Local Zone 或自有数据中心页（仅用官方区域页核查）；不得把 reseller、edge CDN、satellite internet 或 VPS SEO 页面升级为本地区域。
5. **设施/项目种子**（当前官方种子清单）：**Government Data Center / data centers' upgrade**（Tongatapu 默认，具体场所未披露——PMO/DTD/World Bank 证实存在或升级语境，非商业 colo；PMO 2025-06-10 政府门户澄清声明称政府数据仍托管在汤加 Government Data Center，一手信号但未披露场所、容量、运营模式或可商业托管性；记录为 `government_internal_data_center` 或 `government_data_center_project`，不写容量、不写精确地址）；**Tonga Cable / Tonga-Fiji cable landing facility**（Tongatapu，Nuku'alofa/Sopu 区域，运营中，A/B，`telecom_cable_station`）；**Tonga Domestic Cable landing: Nuku'alofa**（Tongatapu，运营中/国内连接节点，A/B）、**Pangai/Lifuka**（Ha'apai，运营中/国内连接节点，A/B，小型外岛设施）、**Neiafu**（Vava'u，运营中/国内连接节点，2026 Hawaiki branch 接入既有 Vava'u 登陆站，A，Vava'u 最强设施级候选）；**Potential `'Eua` / `'Ohonua` cable or network facility**（`'Eua`，仅作待核线索，需官方工程/RIO/采购文件确认，B/C until verified——旧稿关于 `'Ohonua` 登陆站须降级为待核线索）；**TCC / Tonga Communications Corporation network core, gateway, NOC, hosting**（Tongatapu，国有运营商网络基础设施，设施属性待证——运营商 A、设施 B/C，仅当 TCC 官方或项目文件点名 NOC/server/hosting/colo 时记录）；**Digicel Tonga / Wantok / Fiber Pacific / Starlink**（主要 Tongatapu，Starlink 全国，持牌/登记服务商，A 服务/牌照、非 DC）；**Niuas satellite connectivity**（Niuas，无海缆/无 DC 锚点，A/B 连接、非 DC，`no_facility_found` / satellite-only negative control）。
6. **语言与词汇**：中文为主、英文术语双语；查询模板英文执行；汤加语召回辅助词表（仅召回辅助，不作语言学或设施证据，正式记录仍需英文/官方文件锚点）：fakamatala（数据/信息）、komipiuta（计算机）、initaneti / 'initaneti（互联网）、server / seva / sēvā（服务器）、fetu'utaki / fetu'utaki（通信）、uhila / 'uhila（电力）、vahenga（分区）。
7. **可靠性分级**：A（官方/一手）=CCT official register / public records；MEIDECC/Department of Communications 公告；PMO/DTD 政策、新闻和项目文件；Tonga Communications Corporation、Tonga Cable Limited、Tonga Power Limited 等官方运营主体页面；Tonga Registry Service；World Bank/ADB/AIFFP/DFAT 项目和完成文件；AWS/Azure/Google/Oracle 官方区域页；Digicel Pacific/Telstra、Starlink/Kacific 官方服务页。B（强二级）=Matangi Tonga、RNZ Pacific、Kaniva Tonga、Islands Business、Data Center Dynamics、Capacity Media、Submarine Networks、TeleGeography 等具名、可追溯、日期清楚的报道或行业说明。C（弱/聚合）=Submarine Cable Map、PeeringDB、Cloudscene、DataCenterMap、datacenters.com、LinkedIn、社交媒体转述、SEO VPS/hosting 页、无署名市场报告——只能作线索或负面控制，不得单独确立设施存在。
8. **计数与去重规则**（误报与分级规则）：**登陆站 ≠ 数据中心**——海缆登陆站是设施级电信资产但不是零售数据中心，除非一手来源明确说明 rack/colo/hosting/interconnection 服务；**政府 DC ≠ 商业 DC**——Government Data Center 和 data centers' upgrade 是公共部门内部设施/项目，无商业服务证据时不得列为 colocation provider；**许可 ≠ 设施**；**运营商网页 ≠ 设施**；**卫星/Starlink**——Starlink、Kacific、VSAT、emergency telecom terminals 是连接资产，不记录为数据中心；**VPS/SEO**——`Tonga VPS`、`Nuku'alofa dedicated server`、`Pacific cloud` 等无本地物理场所、无注册/许可锚点时 C 级负面控制；**电力负载**——任何 >0.5 MW 或 “hyperscale/large data center” 声称必须有 Tonga Power、项目融资、环境审批或政府公告证据，否则判为不可信；**拼写污染**——`'Eua` 不等于 Eurasia；`Tonga` 与 Samoa/American Samoa/Fiji 项目严格区分；`TCC` 需区分 regulator 旧称/语境与 Tonga Communications Corporation。升级规则：C 级目录/地图/SEO 线索必须找到 A 或强 B 锚点；B 级报道必须与一手来源或实体页面一致才能升级设施。

## 常用查询模板

```text
site:cct.gov.to (license OR licence OR licensee OR "official register" OR "public register" OR "annual report")
site:cct.gov.to (Tonga Cable OR "Tonga Communications Corporation" OR Digicel OR Starlink OR Wantok OR "Fiber Pacific")
site:cct.gov.to (RIO OR "reference interconnection offer" OR interconnection OR "facility access" OR "spectrum")
site:communications.gov.to (Starlink OR satellite OR VSAT OR "submarine cable" OR licence OR license OR regulation)
site:pmo.gov.to ("Government Data Center" OR "data centre" OR "data center" OR "data hosting" OR "government portal")
site:digitaltransformation.gov.to ("data center" OR "data centre" OR "G-Cloud" OR "Cloud First" OR "Data Exchange" OR interoperability)
site:meidecc.gov.to ("data center" OR "data centre" OR "digital government" OR ICT OR "e-government")
site:finance.gov.to (tender OR procurement OR RFP OR "data center" OR "data centre" OR server OR ICT)
site:documents.worldbank.org Tonga P154943 ("data center" OR "data centre" OR "G-Cloud" OR "Digital Government")
site:tcc.to (hosting OR server OR cloud OR business OR enterprise OR NOC OR switch OR "data")
site:tongacable.to (landing OR "cable station" OR RIO OR "facility access" OR interconnection OR Nuku'alofa OR Neiafu OR Pangai OR Vava'u)
"Tonga Cable Limited" ("landing station" OR "cable station" OR RIO OR Nuku'alofa OR Sopu OR Neiafu OR Pangai)
"Tonga Hawaiki Cable Branch System" (Vava'u OR "landing station" OR completed OR Tonga Cable)
site:aiffp.gov.au Tonga Hawaiki Vava'u "landing station"
site:tongapower.to ("data center" OR "data centre" OR datacenter OR "large load" OR "large customer" OR industrial OR MW)
"Tonga Power" ("data center" OR "data centre" OR "large load" OR MW OR "connection")
site:businessregistries.gov.to "{CompanyName}"
"{CompanyName}" Tonga (registered OR incorporated OR "business registry" OR "foreign investment")
"Tonga" ("AWS Region" OR "AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "OCI region")
"Tonga Communications Corporation" ("data center" OR "data centre" OR datacenter OR hosting OR colocation OR server OR cloud OR NOC OR gateway)
site:digicelpacific.com Tonga (enterprise OR business OR cloud OR hosting OR network OR "data")
"Digicel Tonga" ("data center" OR "data centre" OR datacenter OR NOC OR switch OR hosting OR cloud OR server OR enterprise)
"Wantok Tonga" (hosting OR server OR "data center" OR "data centre" OR broadband OR ISP)
"Starlink" Tonga (approved OR launch OR licence OR license OR permit OR reseller)
"Kacific" Tonga (Niuas OR Vava'u OR Ha'apai OR satellite OR broadband OR emergency)
"National Reserve Bank of Tonga" OR "Bank of Tonga" OR "Tonga Development Bank" ("data center" OR "data centre" OR "disaster recovery" OR server OR hosting)
Tonga (fakamatala OR komipiuta OR initaneti OR "'initaneti") ("data center" OR "data centre" OR server OR hosting)
```

分区通用扫描（`{Division}` 替换为 manifest 精确值）：`"{Division}" Tonga ("data centre" OR "data center" OR datacenter OR colocation OR hosting OR "server room" OR "cable station" OR "landing station" OR fibre OR fiber OR broadband OR ICT)`；`site:cct.gov.to "{Division}" (telecommunications OR internet OR broadband OR cable OR electricity)`；`site:tongapower.to "{Division}" (grid OR power OR generation OR substation)`。

## 官方/监管管线要点（详见 explorer-official.md）

- **监管与许可（CCT / MEIDECC Communications）**：优先入口 CCT public records `https://www.cct.gov.to/publications` 与 Department of Communications / MEIDECC 历史监管公告 `https://communications.gov.to/`；用途：枚举持牌电信/ISP/卫星/海缆运营者、确认 Starlink/Tonga Cable/TCC/Digicel 等合法服务状态、查找 RIO、facility access、interconnection、spectrum、licensing fee、annual statistics 等与设施接入相关的文件。任何 `tcc.to` 命中应先判断是否为 Tonga Communications Corporation 运营商页面，不要当监管证据。
- **政府数字化（PMO / DTD / MEIDECC / Finance）**：Digital Transformation Department (DTD, Prime Minister's Office) 发布 Digital Government Strategic Framework、Tonga Enterprise Architecture Framework、Tonga Data Exchange Policy、National Cybersecurity Framework、Cloud First Policy 等；World Bank `Tonga Digital Government Support Project (P154943)` ICR 提到 Component 4 从 secure government network / data center / G-Cloud 设计调整为 whole-of-government integration platform and data centers' upgrade。Cloud First Policy 明确要求政府新 IT 投资优先考虑云，并限制各实体新建独立 data center/server/storage/network/UPS 基础设施——这支持「集中/共享政府基础设施」而非分散商业 DC 市场。
- **国有电信与海缆运营主体**：TCC `https://www.tcc.to/`、Tonga Cable Limited `https://www.tongacable.to/`（站点可访问性/证书状态需实跑确认，若证书异常用 CCT register、AIFFP、ADB/WB、Submarine Networks 交叉核对）、AIFFP Tonga Hawaiki page、Australian Foreign Minister 2026-05-26 release；TCC 运营商核心网、交换、NOC、hosting/enterprise 服务只有在一手资料点名设施时记录。
- **电力与大负荷核查（Tonga Power）**：`https://www.tongapower.to/` 与 downloads/annual reports；汤加岛屿电网规模较小，任何 >0.5 MW 或 “hyperscale/large data center” 声称必须找到 Tonga Power、项目融资、环境审批或政府公告证据；太阳能、BESS、substation、grid upgrade 是能源资产不是 DC，除非明确服务数据中心负荷。
- **分区枚举策略**：Tongatapu——最高（PMO/DTD Government Data Center、CCT register、TCC/TongaTel/Tonga Cable、Tonga-Fiji/Nuku'alofa landing、Tonga Power、registry；Nuku'alofa/Sopu/Ma'ufanga/Vuna Road/St George Building 等默认 Tongatapu，政府/运营商总部默认 Tongatapu 除非源另有地点）；Vava'u——中（AIFFP/DFAT/Tonga Cable Hawaiki branch、Neiafu/Vava'u landing、CCT、Tonga Power；Neiafu 是唯一强非 Tongatapu 设施级候选，Hawaiki branch 只增强电信冗余不升级为 DC）；Ha'apai——低（Pangai/Lifuka 登陆站可作小型 `telecom_cable_station`，无 hosting/DC 证据时不记录数据中心）；`'Eua`——极低到低（仅在官方工程/采购/RIO 证据出现时核实 `'Ohonua` 或其他网络设施）；Niuas——极低（Niuatoputapu、Niuafo'ou 连接线索不产生设施，默认 `no_facility_found`）。覆盖检查：上表恰好覆盖 manifest 的 5 个分区各一次。
- **刷新说明**：每次实跑前重新核对 CCT register/publications、MEIDECC communications 公告、PMO/DTD digital government 页面、World Bank P154943 最新 ICR/采购文件、Tonga Cable/TCC 官网、Tonga Power 年报和官方云区域页；只有来源升级后才改变设施状态。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **行业基线**：未发现汤加有公开销售的中立机架托管（neutral rack colocation）、tiered commercial data center 或 hyperscale capacity 市场。行业枚举重点应放在「是否存在设施级电信/政府机房」，而不是假设有 colo 市场。设施级强信号集中在 Tongatapu/Nuku'alofa/Sopu 与 Vava'u/Neiafu。Starlink、Kacific、VSAT、移动核心网、塔站、Wi-Fi、submarine landing station 和 broadband/enterprise connectivity 都是连接或电信资产；除非厂商一手资料明确写 rack、colocation、server hosting、DR、compute hosting 或 interconnection facility，否则不计为数据中心。
- **厂商与运营商扫描**：海缆（Tonga Cable/Hawaiki/Domestic Cable——Tonga-Fiji/Nuku'alofa-Suva 与 Hawaiki/Vava'u 均 `telecom_cable_station` 非 DC；`'Eua`/`'Ohonua` 只有找到官方工程/RIO/采购/运营页面后才升级）；TCC（`tcc.to` 是运营商官网可确认服务商和业务类型，broadband/mobile/fixed line/enterprise connectivity 不足以确立 DC，只有官方或 B 级来源明确指向 NOC、gateway、server hosting、managed hosting、colo 或 DR facility 时才建立设施候选，默认地点 Tongatapu/Nuku'alofa）；Digicel Tonga/Telstra Pacific（官方页可确认所有权和服务背景，移动核心网/交换机房只有来源点名 facilities、hosting 或 colocation 时才升级）；Wantok Tonga/Fiber Pacific/One.Tel（先用 CCT register 确认服务商身份，ISP/wireless/tower/retail internet 不推断为 DC，官网不可访问或只有社交页时最多 C/B lead，需注册/许可和设施页双锚点）；Starlink/Kacific/卫星（Starlink 在汤加的监管许可/批准是 A 级连接服务证据，Kacific/VSAT/ETC emergency telecom 是连接/韧性资产，对 Niuas 特别有用但不产生 data center/colo 设施）；政府 ICT 与银行/企业机房（政府数据中心 A 级公共部门设施/项目可记录但不得写为商业 colo；银行/企业 server room、DR、backup 只有一手报告或采购文件时进入候选，一般为 Tongatapu）。
- **玩家矩阵**：Government Data Center/DTD（公共部门内部 ICT，Tongatapu 默认，A 存在/项目、地址容量未披露，`government_internal_data_center` 非 commercial colo）；Tonga Cable Limited（国际/国内海缆运营，Tongatapu/Vava'u/Ha'apai，A/B，`telecom_cable_station`，Hawaiki branch 更新 Vava'u）；TCC（国有电信运营商，Tongatapu，A 运营商/B-C 设施，仅点名 NOC/hosting/gateway 时记录设施）；Digicel Tonga/Telstra Pacific（移动/企业连接，Tongatapu，A 运营商/B-C 设施，不从移动核心网推断 DC）；Wantok Tonga/Fiber Pacific/One.Tel（ISP/连接，Tongatapu 为主，A 登记/牌照、C/B 设施，需官网+设施证据双锚点）；Starlink/Kacific（卫星连接，全国含 Niuas，A 服务/许可、非 DC，负面控制）；Tonga Power（公用事业，各供电岛，A 电力，用于否定无电力痕迹的大负荷声称）；境外 VPS/云转售（reseller/SEO，无，C，负面控制）。
- **分级规则**：升级规则（C→A/强 B；B→一手一致）；登陆站规则（默认 `telecom_cable_station`，有 RIO/FAA/facility access/colo 文档才加 `colo_adjacent_telecom`）；政府规则（Government Data Center 可作公共部门设施记录但不可扩写成商业托管或云区域）；运营商规则（运营商存在、牌照、移动核心网、企业连接、IP transit 不证明数据中心）；电力规则（>0.5 MW 声称需要 Tonga Power、项目融资、环境/建设许可或政府公告，无痕迹时降级/否定）；地域规则（见核心结构事实第 1 条）；云区域规则（官方 AWS/Azure/Google/OCI 页未列 TO 时，任何 “Tonga cloud region” 第三方页面按 C 级误报处理）。

## 维护注意（更新纪律）

- 不删除/移动任何既有文件；双 explorer 文件是 codex 审核定稿，SKILL.md 忠实提炼其内容，细则差异以 explorer 原文件为准。
- 每次实跑前重新核对过去 12 个月的 CCT register/publications、MEIDECC Starlink/VSAT 和海缆公告、Tonga Cable/TCC 官网、Hawaiki branch 状态、PMO/DTD 政府数据中心说明、World Bank/ADB 项目文件、Tonga Power 年报，以及官方云区域页。
- 默认规则：登陆站/卫星/移动核心网/宽带连接不是数据中心；许可不等于设施；政府 DC 不等于商业 colo；>0.5 MW 声称必须有电力/融资/审批/政府公告痕迹。
