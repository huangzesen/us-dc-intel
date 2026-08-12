---
name: sh-datacenter-methodology
location: scripts/expansion/world/country-skills/SH/SKILL.md
description: 圣赫勒拿、阿森松与特里斯坦-达库尼亚数据中心发现与审计方法论（bilingual）。Saint Helena, Ascension and Tristan da Cunha datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (SHG portal/Gazette/legislation/planning/procurement, Sure St Helena, Connect Saint Helena power, Equiano fibre project & MCLS/SLTE landing, AIG Ascension telecom transition, TDG satellite, UK FCDO/NAO/Hansard/Companies House, hyperscaler-absence checks) plus industry/trade-press discovery (SAMS, DCD, Developing Telecoms, Capacity, Submarine Networks, directories). Division model: geographical region with 3 divisions (Ascension, Saint Helena, Tristan da Cunha) plus natural sub-layers. Read before running SH exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# SH · 圣赫勒拿、阿森松与特里斯坦-达库尼亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：SH（英国海外领地）为极小型市场，正确产出通常为「已确认 1 条设施 + 若干连接/卫星/采购线索 + 明确阴性覆盖」。已确认设施：**St Helena Government Main Data Centre, Carnarvon Court, Jamestown**（A 级、operational、容量 null）；Equiano 海缆为连接基建而非本地云区域，Rupert's MCLS/登陆站非 DC；Ascension 与 Tristan da Cunha 的通信设施多为卫星/移动网/军事-广播通信，不得误判为数据中心。本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双线交叉验证，以 SHG/AIG/TDG、Gazette、Sure、Connect、Google Equiano 官方页与云区域缺失检查主证。本 skill 汇总两份最终审定的探索报告，作为 SH 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | SHG 门户/Gazette/法规/规划/采购（含 2020 "Teleport & Data Centre" EOI）、Sure St Helena 电信、Connect Saint Helena 电力、Equiano 海缆项目时间线（Rupert's Beach 登陆/MCLS/SLTE）、Ascension AIG 电信转换、Tristan TDG 卫星连接、UK FCDO/NAO/Hansard/Companies House、官方云区域缺失检查 |
| explorer-industry.md | 行业/厂商发现 | SAMS、St Helena Independent/The Sentinel/The Islander 本地媒体、DCD/Developing Telecoms/Capacity/TechAfrica News/SubTel Forum 行业媒体、Sure/Connect/AIG/TDG 运营商页、Submarine Networks/Submarine Cable Map、OneWeb/卫星地面站线索、目录站（DataCenterMap/datacenters.com/PeeringDB） |

## 核心结构事实

1. **行政区划模型**：manifest 为 `subnational_type: geographical region`，**3 个 division：Ascension / Saint Helena / Tristan da Cunha**——地理区域而非统一行政二级；每条设施记录必须同时写 manifest 分区与自然子层（Saint Helena / Jamestown 或 Rupert's；Ascension / Georgetown 或 Cat Hill；Tristan da Cunha / Edinburgh of the Seven Seas）。记录分区拼写用 `Ascension`/`Saint Helena`/`Tristan da Cunha`，查询可同时用 `St Helena` 与 `Saint Helena`。
2. **注册库现状**：无公开全国数据中心注册库；最接近普查的是 SHG 门户 + Gazette + 规划/采购 + 电信许可 + 公用事业 + 海缆所有方 + 云区域官方页的组合。**已确认设施仅 1 条**：SHG Main Data Centre（Carnarvon Court, Jamestown；owner = St Helena Government；`status: operational`；`capacity_mw: null`；evidence 2022-03-07 Schneider Electric 工程师上岛调试关键后备电池，SHG 发布 + Gazette EX-GAZ-9 配证）。
3. **法律与监管**：SHG Gazette（`site:sainthelena.gov.sh/app/uploads/gazette/` 查 PDF，EX-GAZ-9 已核实可访问）、Laws of Ascension / St Helena / Tristan da Cunha 入口、Land Planning and Building Control Division（机房改造/发电机/冷却/配电/MCLS 附属工程高信号入口）、SHG 采购/EOI 页面（2020 EOI 列 "Teleport & Data Centre on-Island and International Connectivity"——历史采购需求，不等于新商业 DC）；UK 资金链：FCDO/gov.uk、Hansard（hansard.parliament.uk，可能对自动 curl 403）、NAO、Companies House（Connect/Sure 实体注册与账户）。
4. **互联与云**：**Equiano（Google 私营，Portugal→South Africa，SHG 2019-12-23 签合同接入 Phase 1 分支，分支长约 1,154 km；2021-08-26 标记分支登陆、2021-08-29 Rupert's Beach 岸端登陆；2023-05-21 至 05-26 SLTE 安装/集成/测试；2023-06-01 SLTE live；2023-09-01 海缆 live，Sure 从 2023-10-01 面向公众）**——MCLS/Cable Landing Station/SLTE/PFE 默认是连接设施非 DC；Rupert's Beach/Rupert's Valley 与 Carnarvon Court/Jamestown 是不同地点，不得合并；Equiano 主线不经过 Ascension 或 Tristan；**AWS/Azure/GCP/OCI 官方区域页均无 Saint Helena/Ascension/Tristan**——Google 海缆 ≠ GCP 区域。
5. **设施/项目种子（2026-08 证据状态）**：**SHG Main Data Centre**（Saint Helena/Jamestown，A 已确认，容量 null）；**Connect Saint Helena 核心设备**（Carnarvon Court，公用事业核心设备——设备事实 A/DC 线索 C，不单列 DC）；**Equiano MCLS/SLTE**（Saint Helena/Rupert's，连接设施 A 连接事实，非 DC）；**SHG Teleport & Data Centre 服务（2020 EOI）**（历史采购线索 C+，无地址不成 DC）；**AIG 民用电信设施**（Ascension/Georgetown，2026-02-28 Sure South Atlantic 停止岛上电信角色、2026-03-01 Omnitouch 接续含 4G mobile——电信事实 A，无 DC）；**RAF/USSF/BBC 通信设施**（Ascension 军事区，非公开通信，阴性边界，不从基地存在推断 DC）；**Tristan IT Container / Starlink + VSAT**（Edinburgh of the Seven Seas，2024-09-22 TDG 确认 Starlink 到岛、天线在 IT Container（Communications HQ，2022-05 commissioned）屋顶、VSAT 仍提供 10 Mbps 并承载语音——卫星通信事实 A，非 DC）。
6. **语言与词汇**：英语为主——data centre/data center/datacenter、server room、teleport、hosting、colocation、landing station、submarine cable、backup battery、UPS、expressions of interest（EOI）；行政区拼写注意 Ascension/Saint Helena/Tristan da Cunha。
7. **可靠性分级**：A = 官方/一手（SHG/AIG/TDG 官网、Gazette/法律文书、英国 FCDO/NAO/议会记录、Sure St Helena、Connect Saint Helena、Google Equiano 官方页、官方云区域页、认证注册处）；B = 具名当事人/日期/地点的可靠媒体/行业报道（SAMS、St Helena Independent、The Sentinel、The Islander、DCD、Developing Telecoms、Capacity Media、Submarine Networks、TechAfrica News、SubTel Forum 等）；C = 目录站、SEO 托管页、承包商作品集、社交帖、活动简介、转引报道、无地址/设施证据的主张。
8. **计数与去重规则**：**登陆站 ≠ 数据中心**（无机架/托管/客户/运营服务证据不得升格）；**卫星 ≠ 数据中心**（Starlink/VSAT/teleport/earth station 是连接线索）；**军事设施不公开**（Ascension 的 RAF/USSF/BBC 通信资产不因存在而进 DC 清单）；云区域缺失必须复查官方页；容量无明确一手 MW/kW/rack/white-space 来源时写 `capacity_mw: null`，不得从海缆带宽、援助金额、发电容量、军事通信站或卫星互联网推导机架/MW；目录污染（datacenters.com、DataCenterMap、PeeringDB、VPS/hosting SEO 页）只做 C 级种子，必须回到一手域验证；旧 URL 修正——Connect Saint Helena 当前官网按 `http://www.connect.co.sh/`（HTTPS 有 TLS handshake failure，HTTP 可访问），connectsthelena.com 未验证为当前官网。

## 常用查询模板

```text
site:sainthelena.gov.sh ("data centre" OR "data center" OR datacenter OR "server room" OR teleport OR hosting OR UPS OR "backup battery")
site:sainthelena.gov.sh/app/uploads/gazette ("data centre" OR Carnarvon OR telecom OR "landing station")
site:sainthelena.gov.sh (planning OR "development control" OR permission) ("data centre" OR telecom OR generator OR UPS)
"Carnarvon Court" ("data centre" OR "server" OR Schneider OR battery)
site:sainthelena.gov.sh ("expressions of interest" OR EOI OR tender OR procurement) (telecom OR "electronic communications" OR "data centre")
site:sure.co.sh ("landing station" OR Equiano OR "data centre" OR colocation OR teleport OR business)
"Sure St Helena" (Equiano OR "submarine cable" OR "landing station" OR licence OR license)
site:sainthelena.gov.sh "Teleport & Data Centre"
site:connect.co.sh (generation OR "electricity generation" OR solar OR battery OR "power station" OR "Carnarvon Court")
"Connect Saint Helena" ("Carnarvon Court" OR generator OR UPS OR "data centre")
site:sainthelena.gov.sh Equiano (cable OR "landing" OR Rupert OR "submarine" OR SLTE OR MCLS)
"Equiano" "St Helena" (landing OR Rupert OR "ready for service" OR "1 October 2023")
site:submarinenetworks.com ("St Helena" OR "Saint Helena" OR Equiano)
site:ascension.gov.ac ("data centre" OR datacenter OR "server room" OR telecom OR tender OR procurement)
"Ascension Island" ("data centre" OR datacenter OR "server room" OR colocation) ; "Ascension Island" ("submarine cable" OR "landing station")
site:tristandc.com ("data centre" OR "data center" OR datacenter OR server OR "server room")
"Tristan da Cunha" ("data centre" OR datacenter OR hosting OR colocation) ; "Tristan da Cunha" (Starlink OR VSAT OR "IT Container")
site:gov.uk "St Helena" (cable OR telecom OR digital OR "data centre" OR Equiano)
site:hansard.parliament.uk "St Helena" (cable OR telecom OR digital OR Equiano)
site:nao.org.uk "St Helena" (cable OR telecom OR airport OR infrastructure)
site:find-and-update.company-information.service.gov.uk "Connect Saint Helena"
site:sams.sh ("data centre" OR Equiano OR "submarine cable" OR "landing station" OR teleport OR electricity)
site:datacenterdynamics.com ("St Helena" OR "Saint Helena" OR Equiano OR OneWeb)
site:developingtelecoms.com OR site:capacitymedia.com ("St Helena" OR Equiano)
"St Helena" (colocation OR colo OR "carrier-neutral" OR "tier 3") -"St Helena Sound" -"Napa"
"St Helena" (VPS OR "cloud hosting" OR "dedicated server") -"Saint Helena Island"
"St Helena" (AWS OR Azure OR "Google Cloud" OR GCP) ("region" OR "availability zone")
("Saint Helena" OR "St Helena") ("data centre" OR datacenter) (rack OR racks OR MW OR kW OR capacity OR Tier)
"Ascension Island" (AWS OR Azure OR "Google Cloud" OR OCI OR GCP)
```

## 官方/监管管线要点（详见 explorer-official.md）

- **SHG**：门户 `sainthelena.gov.sh`；Gazette 通过导航 News→Gazette 与 `site:sainthelena.gov.sh/app/uploads/gazette/` 查 PDF（EX-GAZ-9 已核实）；法规入口 Laws of Ascension/St Helena/Tristan da Cunha；`Land Planning and Building Control Division` 与 `Planning & Building` 为机房改造/发电机/冷却/配电/MCLS 附属工程高信号入口；采购/EOI 页面与公报均需查（2020 EOI 列 Teleport & Data Centre 服务清单，含 DNS/managed firewall/mail filtering/domain/web hosting/transit——C+/历史线索，除非后续合同/设施/地址文件证实）。
- **电信许可**：Sure St Helena `sure.co.sh` 官方页核实（broadband、mobile phone、national & international telephone、public Internet、television rebroadcast；属 Beyon 集团）——证明电信服务商事实，**不证明 colo/DC**；SHG 2023-09-01 "St Helena connects to the Subsea Cable" 说明许可延长、服务由 satellite-based 转向 cable-based——电信状态 A 级，非 DC 证据。
- **电力/公用事业**：Connect Saint Helena `connect.co.sh`（HTTP；About 页核实：商业运营公司、归 SHG 所有、2013-04-01 开始运营、核心服务 Electricity/Water/Wastewater、受 St Helena Utilities Regulatory Authority 监管）——Carnarvon Court 核心设备、发电/输配电、电池/UPS、规划许可、发电机与可再生能源项目为 DC 枚举相关信号；**不得从发电装机、特许权金额或电价推断数据中心容量**。
- **Equiano 海缆**：SHG fibre project hub、SHG-Google 合同、MCLS definitions、CLS commissioning 完成、St Helena connects to the subsea cable、Google Cloud 官方博客均 A 级；时间线 2019-06-28 发布 → 2019-12-23 合同 → 2021-08-26/29 登陆 → 2023-05-21 至 05-26 SLTE → 2023-06-01 SLTE live → 2023-09-01 cable live → 2023-10 验证文件签署；每批次用 submarinecablemap.com/TeleGeography/Submarine Networks 复查 Ascension/Tristan 是否出现新海缆。
- **Ascension/Tristan 官方**：AIG `ascension.gov.ac`（2026 电信转换公告 A 级；军事/政府通信设施不公开，不能推断 DC）；TDG `tristandc.com`（2024-09-22 Starlink 更新确认卫星连接与 IT Container 通信线索，非 DC）。
- **云区域缺失**：每批次必查 AWS/Azure/GCP/OCI 官方页并把缺失作为「已核实检查项」；目录站或本地 VPS/hosting 页只能作 C 级服务线索。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **优先运营商/主体扫描**：SHG Main Data Centre（A 已确认，容量 null，勿与 Rupert's 合并）；Sure St Helena（A 运营商事实，无 colo/DC 证据时不成立设施）；Google/Equiano（A 海缆事实，非 GCP region，landing station 非 DC）；Connect Saint Helena（A 公用事业事实，Carnarvon Court 核心设备不单列 DC）；SHG Teleport & Data Centre 服务 2020 EOI（C+/历史线索，需合同/地址/服务证据升级）；OneWeb/卫星地面站机会（B/C 线索，卫星地面站非 DC）；AIG/Omnitouch 电信转换（A 电信事实，无 DC）；Tristan Starlink/VSAT/IT Container（A 卫星通信事实，非 DC）。
- **行业与媒体来源**：SAMS（`sams.sh`，A/B，重大主张回核 SHG）、St Helena Independent/The Sentinel（周报/规划公告，B）、The Islander（Ascension 民事新闻，B）、DCD/Developing Telecoms/Capacity/TechAfrica News/SubTel Forum（行业站内搜索，B，用于 Equiano/OneWeb/OT connectivity 与 DC 误报排除）、Submarine Networks/Submarine Cable Map/TeleGeography（landing point/branch/RFS，B，若系统页引用所有方则按主证定级）、UK Parliament/NAO/FCDO（A）、Companies House（A）。
- **目录到一手工作流**：目录/SEO/hosting 页面只取种子——"St Helena data center/hosting/VPS" 默认 C（常见误报：Napa, California 的 St. Helena、卫星地面站、泛非 hosting SEO 页）；对种子执行一手回核（sainthelena.gov.sh、sure.co.sh、connect.co.sh、ascension.gov.ac、tristandc.com、gov.uk、nao.org.uk、hansard.parliament.uk、Companies House）；地址必须能落到 manifest 分区 + 自然子层，无地址/设施名/运营商自控证据时保持 lead；状态必须有 commissioning/operational/licence/service launch/planning approval/procurement award 证据，海缆 live 或卫星 live 只证明连接状态；容量只接受一手 MW/kW/rack/white-space/认证注册证据，否则 `capacity_mw: null`。
- **诚实结论（2026-08）**：1 条确认设施（SHG Main Data Centre）+ Equiano 连接记录/登陆站 + Teleport/earth-station 线索 + Ascension/Tristan 阴性覆盖；小市场宁肯明确阴性，也不要把通信节点扩展成数据中心。

## 维护注意（更新纪律）

- **更新节奏**：每季度——SHG Gazette/新闻/采购/EOI 扫描（"data centre"/"teleport"/"Carnarvon"/"landing station"）、Sure/Connect 官网状态（含 connect.co.sh HTTPS 是否恢复）、AIG/TDG 新闻、云区域清单复核；每半年——Equiano 相关 SHG hub/Google 发布、NAO/Hansard 审计线索、海缆地图复查 Ascension/Tristan 新 landing；每年——复查全部 C 级目录条目与容量线索、OneWeb/卫星地面站状态；事件驱动——任何 Ascension/Tristan 海缆或超大规模云区域声明、Omnitouch 设施公告为最大变化。
- **来源核验**：逐一点击 A 级 URL；Hansard 对自动 curl 可能 403（用浏览器/搜索）；Connect Saint Helena 用 HTTP 站点；SAMS 重大主张回核 SHG；目录容量不得继承运营商存在声明的等级。
- **不删除纪律（no-deletion）**：已核实记录不得删除；状态变化改标并保留原始证据链；无支撑条目降级为 C/lead 保留而非移除；负向覆盖（Ascension/Tristan "no public data-centre project found"）须显式记录而非跳过。
