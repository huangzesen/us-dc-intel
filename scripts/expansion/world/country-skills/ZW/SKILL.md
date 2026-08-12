---
name: zw-datacenter-methodology
location: scripts/expansion/world/country-skills/ZW/SKILL.md
description: |
  Zimbabwe data-center discovery merges official/regulatory enumeration (POTRAZ licensing and data protection, ZERA/ZETDC/ZESA power, ZIDA investment, PRAZ/eGP procurement, Ministry of ICT, EMA, councils) with industry/operator discovery (TelOne, Econet, Liquid, Dandemutande, ZOL, ZINX/IXP, trade press). Ten-province sweep with field-level A/B/C/U grading and explicit no-confirmed-facility records.
---

# ZW · 津巴布韦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为津巴布韦数据中心/托管设施发现与审计提供可持续、可复现的查询方法论。
> 分区模型：10 个省（Bulawayo；Harare；Manicaland；Mashonaland Central；Mashonaland East；Mashonaland West；Matabeleland North；Matabeleland South；Midlands；Masvingo）。
> 已知种子：TelOne Harare/Mazowe/Bulawayo、Econet EDC、Liquid Zimbabwe、Dandemutande、ZOL、National Data Centre、ZINX。
> 本 skill 汇总两份探索报告：官方/监管管线（explorer-official.md）与行业/厂商发现（explorer-industry.md），字段级 A/B/C/U 分级。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：POTRAZ/DPA、ZERA/ZETDC/ZESA、ZIDA、PRAZ/eGP、Ministry of ICT/National Data Centre、EMA、councils、CIPZ、云区域/Uptime 核验 |
| explorer-industry.md | 行业/厂商发现：TelOne/Econet/Liquid/Dandemutande/ZOL 运营商、DCD/Ecofin/Techzim/Herald 等贸易媒体、PeeringDB/PCH/IX-F、协会与展会 |

## 核心结构事实（框定每次搜索）

1. 津巴布韦**没有公开的国家数据中心登记册**，也没有统一规划许可库；枚举必须拼接多个官方表面（POTRAZ、ZERA/ZETDC、ZIDA、PRAZ/eGP、Ministry of ICT、EMA、council）。
2. 行政区划为 **10 个省**（含 Bulawayo、Harare 两个城市省）；政府门户使用省导航结构，第三方资料一致。Harare 为行政与商业中心（Sunway City 工业园），Bulawayo 为工业/交通枢纽。
3. 监管基础：电信由 **POTRAZ**（Postal and Telecommunications Act [Chapter 12:05]）监管；电力由 **ZERA**（Energy Regulatory Authority Act）监管，**ZETDC** 为 ZESA 集团输配电公司；规划分散在 Regional, Town and Country Planning Act [Chapter 29:12] 与 Urban Councils Act；投资通过 **ZIDA**；公共采购通过 **PRAZ/eGP**。
4. 数据保护：**Cyber and Data Protection Act [Chapter 12:07] of 2021** 指定 POTRAZ 为 Data Protection Authority；S.I. 155 of 2024（数据控制者许可）已在 ZimLII/Veritas 上线；DPA 门户 dclicensing.potraz.zw 登录受限——不可因无法搜索而推断未注册。
5. **电力是门槛过滤器**：津巴布韦电网受限，ZERA/ZETDC/ZESA、自备发电、太阳能、UPS、发电机、燃料储存、供电协议证据具有决定性；单位必须原样保留（IT MW / facility MW / MVA / kVA / generator kVA / solar MW）。
6. 已确认设施省份：**Harare**（TelOne Runhare House、Econet EDC、Liquid/Dandemutande/ZOL 线索、National Data Centre 语境）、**Bulawayo**（TelOne Bulawayo DC）、**Mashonaland Central**（TelOne Mazowe Earth Station DC）；其余 7 省记录为 `no confirmed facility found`。
7. 津巴布韦为内陆国，无海底电缆登陆站；国际回程经坦桑/南非陆地路由——电缆/回程证据仅作可行性语境，不计数为设施。
8. 无 AWS/Azure/GCP/Oracle 津巴布韦公有云区域（最近在南非）；Uptime 认证清单中未找到津巴布韦设施——`Tier 3`/`Tier 3 Designed` 措辞不等于 Uptime 认证。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§9 / explorer-industry.md §1-§7）

- POTRAZ/数据保护：`site:potraz.gov.zw "data centre" OR "data center"`；`site:dclicensing.potraz.zw "data controller" OR "register"`；`"Cyber and Data Protection" "S.I. 155 of 2024" Zimbabwe`
- 电力（ZERA/ZETDC/ZESA）：`site:zera.co.zw "{operator}" OR "data centre" OR "licence"`；`site:zetdc.co.zw "{operator}" "substation" OR "MVA" OR "33kV" OR "66kV" OR "132kV"`；`"{project}" "power supply agreement" OR "PPA" OR "captive power" Zimbabwe`
- 投资（ZIDA）：`site:zidainvest.com "data centre" OR "ICT" OR "cloud" OR "digital"`；`"ZIDA" "special economic zone" "ICT" OR "data" Zimbabwe`
- 采购（PRAZ/eGP）：`site:egp.praz.org.zw "data centre" OR "DATACENTR" OR "server" OR "cloud"`；已核实线索：OPC/DATACENTR/D/10/2025（Tender Id 42451，Munhumutaba Building，GoZ 财政，A 级采购证据/政府设施线索）
- 部委/委员会/EMA：`site:ictministry.gov.zw "data centre" OR "National Data Centre"`；`site:ema.co.zw "data centre" OR "generator" OR "fuel storage"`；`site:hararecity.co.zw "data centre" OR "TelOne" OR "building plan"`
- 公司注册（CIPZ）：`"CIPZ" OR "Companies and Intellectual Property" "{operator}" Zimbabwe`（注册局在线端点本轮不可达，U 级）
- 运营商：`"{operator}" Zimbabwe "data centre" OR "colocation"`；`"{operator}" Zimbabwe "MW" OR "MVA" OR "racks" OR "kVA"`；`"{operator}" "POTRAZ" OR "ZERA" OR "ZIDA" OR "EMA" Zimbabwe`
- 贸易媒体：`site:techzim.co.zw "data centre" OR "data center" Zimbabwe`；`site:datacenterdynamics.com Zimbabwe "data center"`；`site:itweb.africa Zimbabwe "data centre" OR "IT park"`
- 网络/IXP：`"ZINX" OR "Zimbabwe Internet Exchange" members OR peers`；`site:peeringdb.com Zimbabwe "Harare" OR "ZINX"`（网络证据不等于设施）
- 省级清扫：`"{province}" "data centre" OR "data center" Zimbabwe`；`"{capital}" "data centre" OR "server room" OR "hosting" Zimbabwe`；`site:zim.gov.zw "{province}" "ICT" OR "digital" OR "data"`
- 云区域/Uptime（年度）：`site:aws.amazon.com Zimbabwe "Region"`；`site:uptimeinstitute.com Zimbabwe "TelOne" OR "Econet"`

## 官方/监管管线要点（详见 explorer-official.md）

- POTRAZ 对运营商牌照/服务类别/数据控制者注册语境为 A 级；除非文件点名物理站点或数据中心服务，否则不算设施证据。
- 电力是真实设施与主机/云营销说法的**最佳官方判别器**；MVA/kVA 不得换算为 MW/IT 负载。
- ZIDA 季度报告可发现 ICT/能源/基础设施/SEZ 项目（含 Sunway City、Harare 机场工业/IT 园区概念）但不等同于设施完工。
- eGP 的 OPC/DATACENTR/D/10/2025 是 A 级采购证据与政府设施线索，但不作独立商业共置设施计数。
- Ministry of ICT 项目页 + National Broadband Plan 2023-2030 将 National Data Centre 作为政策/项目语境（A 级语境）；具体启用细节（2017 TelOne 首期、2021-02 总统启用）为 B 级。
- EMA 用于 EIA/项目简报/发电机/燃料储存/变电站通知；council 建筑/规划记录搜索性不一致。
- CIPZ/DCIP 仅用于确认法人/SPV/注册地址；在线端点本轮不可达（U 级）。
- 红旗：无超大规模云官方页的云区域说法；无 Uptime 列出的 Tier 3 认证升级；目录地址无运营商/council 支持；MoU 当作在建；Mazowe 误归 Harare；因搜索无命中而遗漏省份。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **TelOne Harare**：官方页列 Data Centre & Cloud Services、Colocation、DRaaS、Rack Space Rental，地址 Runhare House, 107 Kwame Nkrumah Avenue, Causeway，Harare，措辞 `Tier 3 Data Centre Environment`（A 级服务/地址，非 Uptime 认证）；Techzim 称 2017-03 Harare 启用为 National Data Centre 首期（B）。
- **TelOne Mazowe Earth Station DC**（Mashonaland Central）：DCD 报道 2022-03 启用、第四个 TelOne DC、34 racks、1,300 sqm；TechnoMag 称 US$1m 扩建（B 级容量/成本；目录 C 级；需官方设施页）。
- **TelOne Bulawayo DC**：DCD/Ecofin/Techzim/263Chat/Herald 报道 2022-04 启用、120 racks、400 kVA 或 400 kW（依来源措辞）、`Tier 3 Designed`（B 级容量/措辞；目录地址 C 级）。
- **Econet Data Centre (EDC)**：2025-06 下旬起企业入驻的 5 MW Harare 数据中心，与 Africa Data Centres 姊妹能力设计/建设，计划翻倍至 10 MW 应对 AI（B 级，需 Econet 自有页或官方文件确认）。
- **Econet InfraCo 机场工业/IT 园区**：Harare 机场附近 300 ha、100 MW 太阳能、大型数据中心概念（B/C 级 planned/MoU-intent；无许可/选址/供电/施工证据前不计数）。
- **Liquid Zimbabwe**：官方国家页确认 Borrowdale, Piers Road 办公室与批发 data/voice/IP 服务（A 级存在/地址）；目录所称 Liquid Zimbabwe DC/Tier 3/PUE 为 C 级，需 Liquid/ADC 设施页确认。
- **Dandemutande/Utande**：运营商存在 A 级；DCD 2025-02 报道 US$15m Tier III 运营商中立项目（ITU Partner2Connect，目标 2026-06），地点/规格未披露（B 级计划；完工未确认）。
- **National Data Centre**：Ministry 项目语境 A 级；2017/2021 启用细节 B 级。
- 不计数：NetOne、Telecel、Powertel、IMC/Starlink、ZINX/HIX、CDN/cache 节点、光纤节点、POTRAZ Digital Centres、云转售、银行服务器房、矿场控制室、大学服务器房。
- 保留的降级：Econet 5 MW/10 MW（B）、机场园区（B/C planned）、Dandemutande 完工（未确认）、Liquid 规格（C）、ZOL/Liquid Home 遗留共置说法（U/B）。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| TelOne Harare Data Centre / Runhare House | Harare | 运营中；官方服务/地址页 A 级，2017 启用 B 级；无 Uptime 认证 |
| TelOne Mazowe Earth Station DC | Mashonaland Central | 运营中（2022-03 启用）；DCD/TechnoMag B 级（34 racks、1,300 sqm、US$1m）；目录 C 级 |
| TelOne Bulawayo DC | Bulawayo | 运营中（2022-04 启用）；120 racks、400 kVA/kW、Tier 3 designed 均为 B 级；地址 C 级 |
| Econet Data Centre (EDC) | Harare | 2025 年报道运营/入驻中；5 MW、10 MW 扩张意图 B 级；需 Econet 官方确认 |
| Econet InfraCo 机场工业/IT 园区 + DC | Harare | planned/MoU-intent（B/C）；需 ZIDA/ZERA/ZETDC/council/EMA/施工证据 |
| Liquid Zimbabwe DC 线索 | Harare | 办公室/服务 A 级；设施规格 C 级线索 |
| Dandemutande 现有共置 | Harare | 运营线索；公司 A 级、目录/社交 C 级；需当前官方共置页 |
| Dandemutande US$15m Tier III DC | 未披露（可能 Harare） | planned/在建，目标 2026-06 未确认（B/C） |
| Government National Data Centre | Harare（预期） | 政策/项目语境 A；启用细节 B |
| ZOL / Liquid Home 遗留 DC/共置说法 | Harare | 线索（U/B）；需当前 Liquid/ZOL 自有数据中心页 |
| ZINX / Zimbabwe Internet Exchange | Harare | 网络/IXP（B），非设施 |
| NetOne / Telecel / Powertel 核心设施 | 全国 | 仅线索，无数据中心证据 |
| 超大规模云公有区域 | n/a | 津巴布韦无（A 级官方页确认）；年度复核 |
| Uptime 认证设施 | n/a | 未找到（A 级清单表面）；年度复核 |

## 更新节奏

- POTRAZ 牌照/DPA/行业报告：季度。
- ZIDA 报告与投资牌照：季度。
- PRAZ/eGP 采购（`data centre`、`DATACENTR`、`cloud`、`server`、`hosting`、`DR`、`backup`）：月度。
- EMA/council（Harare/Bulawayo 月度，其余季度/触发式）；ZERA/ZETDC/ZESA：季度。
- Ministry of ICT/National Data Centre/e-government：月度。
- 云区域与 Uptime 认证：年度及任何津巴布韦云区域/Tier 认证声明时。
- 运营商页：季度；Econet EDC/InfraCo、Dandemutande 月度直至状态落定。
- 媒体：Techzim/NewZimbabwe/Bulawayo24/263Chat/Herald 每周；DCD/ITWeb Africa/Developing Telecoms/Connecting Africa/Capacity 每月。
- 目录：季度并与运营商/官方页对账；PeeringDB/PCH/IX-F/ZISPA：季度。
- 待办（2026-08-12）：Econet EDC 5 MW/10 MW 的 Econet 自有页或官方文件；Dandemutande 2026-06 完工核实；Mazowe/Bulawayo 容量官方确认；CIPZ 在线端点可达性；codex terra agent 分批复核后按本方法论推进。
