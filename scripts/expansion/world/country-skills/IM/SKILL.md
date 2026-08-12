---
name: im-datacenter-methodology
location: scripts/expansion/world/country-skills/IM/SKILL.md
description: 马恩岛数据中心双线查询方法论（官方/监管/云管线 + 行业/厂商/媒体发现），含 division 模型、来源分级与查询模板；Isle of Man datacenter dual-line discovery methodology (official/regulatory/cloud pipeline + industry/vendor/media discovery) with division model, source grading and query templates. 运行 IM 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# IM · 马恩岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为马恩岛（Isle of Man, IM）数据中心枚举/审计批次提供官方与行业双线发现方法。官方线（explorer-official.md）覆盖政府、规划、监管与云管线；行业线（explorer-industry.md）覆盖运营商、厂商、媒体与目录发现。两线交叉核验，按 A/B/C 分级入库；本文件是运行批次前的路由与纪律入口。

## 入口

| 文件 | 职责 | 内容概要 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | 马恩岛政府（gov.im）、Department for Enterprise、Digital Isle of Man、规划检索（services.gov.im/planning-applications、pabc.gov.im）、CURA 电信/频谱监管、Manx Utilities 电力、Companies Registry、GSC/FSA、政府采购（In-Tend IOMG）、官方云区域缺位确认 |
| explorer-industry.md | 行业/厂商/媒体发现 | 优先运营商/设施扫描（Manx Telecom、Netcetera The Dataport、Domicilium、Continent 8、Sure、BlueWave、Wi-Manx/Noventre）、行业媒体（DCD、Capacity、CommsUpdate、Telecompaper、IOM Today、Manx Radio、BBC IoM）、目录/经纪人（DataCenterMap、Data Center Platform、Colo-X 等）、枚举矩阵与分级入库规则 |

## 核心结构事实

1. **Division 模型**：manifest 已核验 `subnational_type: country`，`divisions: ["Isle of Man"]`。唯一 division 为 Isle of Man；所有设施记录必须落到 locality 字段（Douglas、Ballasalla、Braddan、Onchan、Ramsey、Peel、Castletown、Port Erin、Port St Mary 等城镇/教区），不存在下级行政区清单。
2. **政治与市场形态**：马恩岛是英国王冠属地（Crown Dependency），自治议会为 Tynwald；按本地政府/监管/许可系统处理，不套用英国地方规划或 Ofcom/Companies House 流程。市场为小型离岸托管/colo，需求由 e-gaming、金融服务、云/托管、灾备与本地企业 IT 驱动；无 hyperscale campus 或 AWS/Azure/GCP/OCI 公共云区域。
3. **规划检索**：全岛集中式，官方入口为 Isle of Man Government Online Services planning search（services.gov.im/planning-applications/）与 Planning & Building Control（pabc.gov.im），不是 planningportal.co.uk；`planning.gov.im` 不是主要当前入口。
4. **法律与监管**：通讯与公用事业监管机构为 Communications and Utilities Regulatory Authority（CURA，cura.im），负责电信/广播/公用事业监管并发布 licence information；公司核验使用 Isle of Man Government Companies Registry（gov.im/services.gov.im），不是 Companies House；博彩监管由 Isle of Man Gambling Supervision Commission（GSC，isleofmangsc.com）独立负责，FSA 监管金融服务，spread betting 例外归 FSA——GSC 与 FSA 未合并。
5. **电力与互联**：Manx Utilities（manxutilities.im）负责电力连接、大型负载与开发商信息；现有 60 MW interconnector 与新的互联/开发商咨询背景；机房具体用电仍需项目文件或规划附件。
6. **设施/项目种子（2026-08 证据状态）**：Manx Telecom twin datacentres（Douglas North/Greenhill 待地址核验，A）；Netcetera The Dataport（Ballasalla/Malew，A）；Domicilium / The Isle of Man Datacentre（Ballasalla / Ronaldsway Industrial Estate，A/B）；Continent 8 Isle of Man data centre（Douglas / Pulrose Road，A）；Sure Isle of Man data centre services（地址待核验，A 服务）；Wi-Manx/Noventre Heywood House（历史线，B/C）；BlueWave Communications（通信运营商、非确认岛内 DC，官方 bwc.im，colo 由 UK sister company aql 提供）；e-gaming/金融需求方（Microgaming、PokerStars 等）为需求方而非设施。
7. **语言与词汇**：搜索以英文为主，关键词含 "data centre"/"datacentre"/"data center"、colocation、server room、standby generator、backup generator、substation、MVA/MW、interconnector、planning application、registered office；注意 "cloud platform"/"managed hosting"/"remote hands" 需确认是否有岛内物理设施。
8. **可靠性分级**：A = 官方/监管/许可/运营商一手来源（gov.im、pabc.gov.im、services.gov.im、cura.im、manxutilities.im、isleofmangsc.com、legislation.gov.im、运营商现行官方设施页、官方公司注册记录、官方云区域页）；B = 强二级来源（DCD、Capacity Media、CommsUpdate、Telecompaper、IOM Today、Manx Radio、BBC IoM、Manx Technology Group 等含地址的技术/市场文章）；C = 目录/聚合/经纪人/SEO/社媒（DataCenterMap、Datacenters.com、Cloudscene、Data Center Platform、Colo-X、Colomap、Upstack）。
9. **计数与去重规则**：facility_type/status 需精确；CURA licence = A 级运营商身份但不等于数据中心设施；运营商总部/registered office 不是机房地址（Douglas 办公地址易误标）；目录地址 + 运营商官方设施页 = 可记 A/B 混合但地址字段需标来源；运营商官方 "services" 页无地址 = A 级服务证据不等于 A 级设施地址证据；不得入库：云转售、运营商总部、e-gaming 公司办公室、network PoP、radio mast、substation、仅发电机规划记录；BlueWave 与 UK aql colocation、美国 Bluewave.net、百慕大 bluewave.bm 需区分。

## 常用查询模板

```text
site:gov.im "data centre" "Isle of Man"
site:services.gov.im/planning-applications "data centre"
site:pabc.gov.im "data centre" "Douglas"
"Isle of Man" "planning application" "generator" "data centre"
site:cura.im "licence" "Manx Telecom"
site:cura.im "frequency allocations" "Manx Telecom"
site:manxutilities.im "interconnector" "MW"
"Manx Utilities" "{operator}" "substation"
site:gov.im/categories/business-and-industries/companies-registry "{operator}"
"{operator} Limited" "registered office" "Isle of Man"
site:isleofmangsc.com "licence holders" "online gambling"
site:in-tendhost.co.uk/iomg "data centre"
"{locality}" "Isle of Man" "data centre"
"{locality}" "Isle of Man" colocation
site:pabc.gov.im "{locality}" "data centre"
site:digitalisleofman.com "{operator}" "Datacentre"
site:datacenterdynamics.com "Isle of Man" "data center"
site:iomtoday.co.im "data centre" OR "datacentre"
site:datacentermap.com/isle-of-man "{operator}"
"Isle of Man" "AWS region" -aws.amazon.com
"Isle of Man" "Azure region" -microsoft.com -azure.microsoft.com
"Manx Telecom headquarters" "data centre"
"e-gaming" "Isle of Man" "data centre" "office"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **政府与议会**：site:gov.im / site:tynwald.org.im 查 "data centre"、"Cabinet Office"、"Digital Isle of Man"；提取政府部门、采购/议题日期、设施名、承包商、locality、预算/合同额、是否仅为云/托管采购。
- **规划与建筑控制**：services.gov.im/planning-applications/ 与 pabc.gov.im 按地址/规划号/日期检索；提取 application reference、状态、申请人/业主/代理、locality、完整地址、园区、用途描述（data hall、server room、UPS、battery room、cooling、fuel storage、standby generator）、条件（噪音/排放/消防/交通/电力）；规划记录可将设施/扩建/发电机证据提升为 A。
- **通讯监管（CURA）**：查运营商牌照/频谱（Manx Telecom、Sure、Domicilium、BlueWave）；CURA 只能证明通讯许可身份，须与运营商官方设施页/规划/目录地址交叉。
- **电力（Manx Utilities）**：site:manxutilities.im 查 data centre/large load/substation/interconnector，用于容量、接入、变电站与大型负载佐证。
- **公司与牌照**：Companies Registry（gov.im/services.gov.im）核验实体存在/注册名/注册地址/filing（注册地址≠设施地址）；GSC 查 e-gaming 牌照（需求方背景）；FSA 查金融服务实体（除 spread betting 外不把 online gambling 归入 FSA）；legislation.gov.im 查 Online Gambling Regulation Act 2001。
- **政府采购**：In-Tend IOMG（in-tendhost.co.uk/iomg）查 data centre hosting/WAN/DR 合同；注意 bot/登录限制，记录入口可用性、检索日期、能否打开 tender documents。
- **云区域缺位确认（negative control）**：AWS/Azure/GCP/OCI 官方区域页均无 Isle of Man region；本地 AWS marketing/partner/cloud resale 不能算 AWS region。
- **覆盖流程**：全岛覆盖但按 locality 分层——Douglas（Manx Telecom、Continent 8、Sure、政府 IT、e-gaming/金融需求方）、Ballasalla/Ronaldsway/Malew（Netcetera、Domicilium、机场/工业区）、Braddan/Union Mills/Tromode、Onchan、Ramsey、Peel/Castletown/Port Erin/Port St Mary 低产出负面覆盖；每个 locality 至少跑 "{locality}" + data centre/datacentre/colocation/server room/standby generator + pabc/planning 检索。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **优先运营商/设施扫描**（按序）：Manx Telecom Datacentre（官方 A，Tier 3，two datacentres，isleofmandatacentre.com）→ Netcetera The Dataport（官方 A，Tier 3/3+，Ballasalla/Malew）→ Domicilium The Isle of Man Datacentre（官方 A/B，Ronaldsway Industrial Estate，Digital Isle of Man 目录给出地址 IM9 2RS）→ Continent 8（官方 A，Tier-3 Douglas/Pulrose Road，legal 页注册办公室）→ Sure（官方 offshore data centres 服务页覆盖 IoM + IOM terms PDF；Spring 2026 opening 的社媒信号仅作 C/B 种子）→ BlueWave（bwc.im，通信运营商；colo/data centre 由 UK aql 提供，不作已确认岛内设施）→ Wi-Manx/Noventre（Heywood House 历史线）→ Manx Technology Group（2026 市场文章，"all four Isle of Man datacentres" 线索，B）。
- **行业媒体与二级来源**：DCD（Manx Telecom datacentre unit、Wi-Manx 2010 历史项目、面积/机柜线索）、Manx Technology Group 文章（ASN 列表、市场覆盖）、Capacity Media（海缆/网络基础设施）、CommsUpdate/Telecompaper（Manx Telecom/Sure/BlueWave/Domicilium 电信事件）、IOM Today、Manx Radio、BBC IoM（本地商业/规划/政府 IT）、LinkedIn/社媒（新开业/招聘/项目节奏，C，个别公司官方账号可作 B 种子）。
- **目录与经纪人**：DataCenterMap（当前显示 Isle of Man 6 facilities / Douglas 4 / Ballasalla 2，逐条回查）、Data Center Platform、Colo-X、Datacenters.com、Cloudscene、Inflect、ColocationM——只用于播撒设施名、地址和市场覆盖，不得单独给 A。
- **目录到一手核验流程**：目录记录 facility/operator/address/locality → 搜运营商官网同名设施或 "owns and operates" → 用 planning services/pabc 查地址/发电机/改建/用途变更 → 用 CURA 查通讯许可、Companies Registry 查法律实体 → 若只有目录和经纪人页面，记录为 C 并标明缺失的一手证据。
- **分级与入库**：A 级设施 = 运营商官网明确 owns/operates/located on Isle of Man 或规划/政府/监管文件确认物理设施；A 级服务但非地址 = 运营商官网确认 data-centre/colo 服务但无具体地址，facility_address_confidence 需低或 unknown；B 级设施线索 = DCD/Manx Technology Group/本地媒体给出设施名/规模/地址，需一手回查；C 级 = 目录/聚合/经纪人/社媒/SEO，只播撒不单独确认；不得入库：云转售、总部、办公室、PoP、radio mast、substation、仅发电机规划记录。
- **枚举矩阵与负面控制**：Douglas 与 Ballasalla/Ronaldsway 逐设施回查，其余 locality 通用扫描 + negative log；低产出 locality 的命中必须至少一个一手来源或两个独立 B 来源才可入库；negative log 记录检索日期、查询式、未发现内容（no hyperscale public region、BlueWave 指向 UK aql DCs、公司仅办公室等）。
- **执行顺序**：①官方页建 A/B 种子 ②目录补地址标 C ③planning 查地址/发电机/用途 ④CURA + Companies Registry 核验 ⑤GSC 与本地媒体解释需求不把办公室当设施 ⑥官方云区域页确认 hyperscale 缺位 ⑦Douglas/Ballasalla 深扫、其余 locality 通用扫描。

## 维护注意（更新纪律）

- **更新节奏**：批次运行时以检索当日为准更新证据日期与状态；历史设施（Government Data Centre、Manx Data Centre、Wi-Manx）需核实现状，不得默认仍在运营。
- **来源核验**：每个设施条目保留一手来源 URL 与分级；目录地址需回查运营商官网/规划；社媒信号必须回查官网或规划后才可提升。
- **不删除纪律**：本目录只新增/更新 SKILL.md、ANATOMY.md 与探索产物，禁止删除/移动任何现有文件（explorer-official.md、explorer-industry.md 与历史证据保留为原始记录）。
