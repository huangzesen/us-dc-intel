# GI Explorer Industry — 直布罗陀数据中心行业发现

日期：2026-08-12。国家：**GI Gibraltar（直布罗陀，英国海外领地）**。分区模型已按 `world-manifest.jsonl` 核对：只有一个分区 **Gibraltar**。本文件覆盖行业侧发现：运营商/设施扫描、本地和行业媒体、聚合目录、互联目录、投资项目、云/托管产品、查询模板、枚举矩阵与分级纪律。官方、监管、电力和采购详见 `explorer-official.md`。

可靠性分级：**A** = 运营商/官方/监管/采购一级证明；**B** = 可信媒体、供应商案例、互联目录等强二级；**C** = 聚合目录、市场平台、转售商或未交叉验证公司声明；**U** = 传闻。

---

## 0. 行业发现框架 (Industry Discovery Frame)

- Gibraltar 是微型市场，但不是空白市场。已核实至少有两个现役托管/数据中心设施线索足够强：**Gibtelecom Mount Pleasant Data Centre** 与 **Continent 8 Gibraltar Data Centre inside the Rock**。
- 2025 年新增重大规划项目：**Pelagos Data Centres** 公布 near the Port of Gibraltar 的 250MW、五期、20,000 m2 data centre campus，政府新闻稿与公司官网均可验证；当前只能标为 **announced/planned**，首期目标为 2027 年底运营。
- GibFibre 是本地 private full-fibre/FTTH 运营商和 authorised electronic communications operator；它可能产生 co-location / data-centre 服务线索，但不能按政府所有的批发光纤机构处理。
- 行业需求主要来自 online gambling、金融服务、DLT/VASP、政府托管和跨境低时延连接。需求存在不等于设施存在。
- 预期生产产出：现役设施 **2 个高可信锚点** + **1 个 A 级 planned campus** + 若干 C 级本地 ISP/MSP/内部机房线索。聚合目录声称的 6 facilities 必须逐条回查运营商/监管/采购。

---

## 1. 本地媒体、行业媒体与市场来源 (Local Press, Trade Press & Market Sources)

| 来源 Source | URL | 语言 | 用途 Use | 分级 |
|---|---|---|---|---|
| Gibraltar Chronicle | https://www.chronicle.gi/ | EN | 政府、电信、博彩、规划和商业新闻。 | B |
| GBC News | https://www.gbc.gi/ | EN | 公共广播；政府声明、能源、电信报道。 | B |
| Your Gibraltar TV | https://www.yourgibraltartv.com/ | EN | 本地商业/电信广告、政府转载、活动线索。 | B/C |
| Panorama archive / Gibraltar news blogs | Panorama 已于 2024-04-26 停刊；用 GBC 停刊报道与可访问归档核查旧线索 | EN | 历史政治和商业评论；仅用于旧线索回溯。 | C unless corroborated |
| Gibraltar Magazine | https://thegibraltarmagazine.com/ | EN | 本地商业活动和 Continent 8 等报道转载线索。 | C/B |
| Olive Press / SUR / Cadena SER Radio Algeciras | https://www.olivepress.es/、https://www.surinenglish.com/、https://cadenaser.com/radio-algeciras/ | EN/ES | 西班牙边境侧报道；跨境能源、港口、海缆和 Pelagos 叙事。 | C/B |
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ | EN | 数据中心行业新闻；Continent 8 contract、Pelagos 250MW 等。 | B |
| Capacity Media | https://www.capacitymedia.com/ | EN | 海缆、运营商、连接性、投资新闻。 | B |
| Telecoms.com | https://www.telecoms.com/ | EN | 运营商股权和网络投资新闻。 | B |
| Computer Weekly | https://www.computerweekly.com/ | EN | Pelagos 等大型项目二级核查。 | B |
| PR Newswire | https://www.prnewswire.com/ | EN | 公司公告分发；Pelagos 原始新闻稿副本。 | B/C; use company/HMGoG first |

媒体检索模板：

```text
site:chronicle.gi "data centre" Gibraltar
site:gbc.gi "data centre" Gibraltar
site:yourgibraltartv.com "GibFibre" "data centre"
site:datacenterdynamics.com Gibraltar "data center"
site:datacenterdynamics.com "Continent 8" Gibraltar
site:datacenterdynamics.com Pelagos Gibraltar
site:capacitymedia.com Gibraltar "Gibtelecom"
site:telecoms.com Gibraltar "Gibtelecom"
site:cadenaser.com Gibraltar "centro de datos"
```

---

## 2. 运营商、托管与设施扫描 (Operator, Hosting & Facility Sweep)

| 公司/机构 | 关注点 | 最佳验证路径 | 种子分级 |
|---|---|---|---|
| Gibtelecom | Data Centre Solutions、Hosting & Cloud、Private Cloud、PoP、Gibraltar/London/Dublin/Malta/Malaysia footprint、Mount Pleasant facility。 | Gibtelecom 官网；GRA 年报；Privy Council/GRA dispute docs；政府采购。 | A/B |
| Continent 8 Technologies | Gibraltar data centre inside the Rock、server hosting、cloud hosting、gaming/regulated industry hosting、PCI/ISO claims。 | Continent 8 Gibraltar location；HMGoG 2024 visit；HMGoG 2022 tender award；DCD contract report。 | A |
| Pelagos Data Centres | 250MW planned campus near Port of Gibraltar、five phases、power model、planning and construction milestones。 | HMGoG 2025 announcement；Pelagos official announcement；DPC/planning/energy follow-up；DCD/Computer Weekly secondary. | A(announced/planned) |
| GibFibre / GibFibreSpeed | FTTH/full-fibre network、enterprise services、possible co-location/backups/data-centre claims。 | GibFibre site；GRA authorised-operator notices；GRA disputes; company pages. | A(operator)/C(facility until confirmed) |
| u-mee / Broadband Gibraltar / Sapphire | ISP and fiber network, possible business connectivity/hosting. | GRA notices, company site, RIPE/ASN, local press. | C unless facility named |
| Local MSP/hosting firms | VPS, managed hosting, backups, disaster recovery. | Company site + ASN/whois + contract/client case + physical location. | C |
| GFSC-regulated banks/DLT firms | Local hosting/data residency disclosures, DR arrangements. | GFSC register + company compliance docs + supplier cases. | C/B |
| Remote gambling operators | Local data centre hosting, DR, low-latency gaming infrastructure. | Gambling Division/HMGoG + company disclosures + Continent 8/Gibtelecom cases. | C/B |

扫描纪律：只有 **operator + facility/location + status + evidence URL + division=Gibraltar** 齐全才计入设施。若只有“cloud”“hosting”“Gibraltar presence”“office”或“network access point”，保留为服务/连接性线索。

---

## 3. 聚合目录、互联目录与市场平台 (Aggregators, Interconnection Directories & Marketplaces)

| 来源 Source | URL | 用途 Use | 分级 |
|---|---|---|---|
| Data Center Map - Gibraltar | https://www.datacentermap.com/gibraltar/gibraltar/ | 声称 Gibraltar 有 6 facilities；用于种子，不直接入库。 | C |
| Data Center Map - Continent 8 Gibraltar | https://www.datacentermap.com/gibraltar/gibraltar/continent8-gibraltar/ | Continent 8 地址/描述线索；需以 Continent 8/HMGoG 回查。 | C |
| Data Center Map - Pelagos | https://www.datacentermap.com/gibraltar/gibraltar/pelagos-data-centre/ | Pelagos planned campus 市场条目；以 HMGoG/Pelagos 官网为准。 | C |
| datacenters.com | https://www.datacenters.com/ | marketplace 搜 Gibraltar；可能重复或缺少源。 | C |
| PeeringDB | https://www.peeringdb.com/ | org / net / facility 记录，查 Gibtelecom、Continent 8、GibFibre。 | B/C |
| RIPE Database | https://apps.db.ripe.net/db-web-ui/ | ASN、route、organisation、contact；查 GI 网络运营商。 | B |
| IXPDB / Euro-IX | https://ixpdb.euro-ix.net/ | 核查是否有 Gibraltar IXP；当前预期为无公开 IXP。 | B |
| Submarine Cable Map | https://www.submarinecablemap.com/ | Europa Point / Gibraltar cable landing and systems. | B |
| Internet Exchange Map | https://www.internetexchangemap.com/ | 区域 IXP 地理核查；低优先。 | C |

聚合目录处理规则：

- 聚合目录可能把 planned facility、运营设施、总部地址、PoP、网络节点放在同一国家页。
- Data Center Map 的 Gibraltar “6 facilities”是待拆分清单，不是确认数量。
- 地址如 `William's Way`、`Neil Pinero Road`、`inside the Rock` 等，只在运营商或官方来源支持时用于生产记录。
- 若 aggregator 与官方/运营商冲突，以官方/运营商为准；保留 aggregator URL 作为 discovery note。

---

## 4. 已核实设施与项目线索 (Verified Facility & Project Leads)

| Lead | Division | Area | Status | Evidence | Grade | Handling |
|---|---|---|---|---|---|---|
| Gibtelecom Data Centre | Gibraltar | Mount Pleasant | Operating | Gibtelecom Data Centre Solutions; GRA Annual Report 2019/2020; Privy Council case summary | A/B | 现役设施锚点；容量/Tier 未公开时留空。 |
| Continent 8 Gibraltar Data Centre | Gibraltar | inside the Rock / former MoD facility | Operating | Continent 8 Gibraltar location; HMGoG 2024 visit; HMGoG 2022 award | A | 现役设施锚点；政府合同需求可关联。 |
| Pelagos Data Centres | Gibraltar | near Port of Gibraltar | Announced/planned | HMGoG 2025 announcement; Pelagos official announcement; DCD secondary | A(announcement) | 不计入运营设施；追踪 planning, land, power, construction, commissioning。 |
| GibFibre data-centre/co-location claims | Gibraltar | Unknown | Lead | GibFibre site/search snippets; GRA authorised-operator context | C | 必须找 physical facility、operator page 或 contract 才能升级。 |
| Government Data Centre Hosting Services | Gibraltar | Tender specified Gibraltar; facility supplied by contractor | Procurement demand / awarded service | HMGoG 2022 tender notice and award to Continent 8 | A | 证明政府采购托管需求和供应商，不必单独建政府设施。 |
| Europa Point cable landing | Gibraltar | Europa Point | Connectivity asset | Submarine cable directories / cable maps | B | 只作连接性；不等于 data centre。 |

---

## 5. 连接性、海缆与边缘信号 (Connectivity, Cable & Edge Signals)

- Gibtelecom 官网称其 data centre footprint includes Gibraltar, London, Dublin, Malta and Malaysia；新闻页还提到与 London and Gibraltar data centres 的 core private network 连接。这是跨境托管 footprint 的 **A** 级运营商声明。
- Continent 8 官网称其全球网络有 data centres and strategic PoPs，Gibraltar 是其 EMEA location 之一；其行业定位偏 iGaming、managed hosting、cloud、cybersecurity。
- Gibraltar 连接性发现应关注 Europa Point、跨境 Spain fiber、carrier diversity、private MPLS/backbone、gaming latency，而不是寻找大型公共 IXP。公开 IXP 目录若无 Gibraltar，不应因此否定私有互联或运营商 PoP。
- Edge/cloud gateway/5G core/PoP 只有在点名“data centre/facility/data hall/colocation”的情况下才转为设施候选。

连接性检索模板：

```text
"Gibtelecom" "Data Centres in London and Gibraltar"
"Gibtelecom" "Points of Presence" "Gibraltar"
"Continent 8" "Gibraltar" "private network"
"Continent 8" "Gibraltar" "carrier"
"Gibraltar" "Europa Point" "submarine cable"
"Gibraltar" "cross-border fibre" Spain
"Gibraltar" "PeeringDB"
"Gibraltar" "IXP"
```

---

## 6. 投资、云与经济促进渠道 (Investment, Cloud & Economic Development)

| 来源 | URL | 用途 | 分级 |
|---|---|---|---|
| Pelagos Data Centres | https://pelagosdata.com/ | 250MW planned campus、容量、阶段、能源、PUE/Tier 目标。 | A(自身声明) |
| HMGoG Pelagos announcement | https://www.gibraltar.gov.gi/press-releases/pelagos-data-centres-unveils-ambitious-plan-for-new-250mw-facility-near-the-port-of-gibraltar-6412025-11196 | 政府背书、项目规模、位置和时间表。 | A(公告/计划) |
| Gibraltar Finance | https://www.gibraltarfinance.gi/ | 金融、DLT、VASP、预测市场和招商需求。 | A(机构)/C(设施线索) |
| GFSC DLT Providers | https://www.fsc.gi/regulated-entities/dlt-providers-38 | DLT/VASP 企业需求池。 | A |
| HMGoG Remote Gambling | https://www.gibraltar.gov.gi/finance-gaming-and-regulations/remote-gambling | 博彩监管入口和许可需求池。 | A |
| Gibraltar Chamber of Commerce | https://www.gibraltarchamberofcommerce.com/ | 本地商业活动与企业线索。 | B/C |
| DCD / Computer Weekly / local Spanish press | see §1 | Pelagos 和大型项目二级报道。 | B/C |

投资项目处理：

1. Pelagos 当前为 announced/planned；记录 `first phase targeted late 2027`、`250MW by 2033`、`near Port of Gibraltar`、`independent of existing grid`，并标注未来性。
2. 后续复查 Development and Planning Commission (DPC) agendas/minutes、environmental impact documents、land transfer/lease、power generation permits、construction procurement、local objections。
3. “AI hub”“digital gateway”“largest infrastructure initiative”等表述是招商叙事；不替代容量投运证据。

---

## 7. 云与本地托管核查 (Cloud & Local Hosting Checks)

- Hyperscale cloud region：AWS/Azure/GCP/OCI 官方列表均无 Gibraltar；最近可用区域多在 Spain/Madrid 或 AWS Europe (Spain)。
- Gibtelecom 和 Continent 8 的 cloud 产品是本地/私有/行业云和托管服务，不是 AWS/Azure/GCP/OCI region。
- 本地 hosting/VPS 供应商常可能部署在 Spain/UK/Isle of Man/Malta；必须检查 ASN、IP geolocation、terms、support address、facility operator。

托管检索模板：

```text
"Gibraltar" "managed hosting"
"Gibraltar" "VPS"
"Gibraltar" "data residency" hosting
"Gibraltar" "locally hosted cloud"
"Gibraltar" "disaster recovery" hosting
"Gibraltar" "business continuity" "data centre"
"Gibraltar" "Tier III" "racks"
"Gibraltar" "server migration" "data centre"
```

---

## 8. 查询模板大全 (Query Templates)

英语主检索：

```text
"data centre" "Gibraltar"
"data center" "Gibraltar"
"Gibraltar" "colocation"
"Gibraltar" "co-location"
"Gibraltar" "server room"
"Gibraltar" "data hall"
"Gibraltar" "Tier III"
"Gibraltar" "racks" "data centre"
"Gibtelecom" "data centre"
"Gibtelecom" "Mount Pleasant"
"Continent 8" "Gibraltar" "data centre"
"Continent 8" "inside the Rock"
"Pelagos Data Centres" "Gibraltar"
"Gibraltar" "250MW" "data centre"
"GibFibre" "data centre"
"GibFibre" "co-location"
"Europa Point" "submarine cable" "Gibraltar"
```

西班牙语补充：

```text
"centro de datos" "Gibraltar"
"Gibraltar" "centro de datos" "puerto"
"Gibraltar" "250 MW" "centro de datos"
"Gibraltar" "fibra transfronteriza"
"Gibraltar" "cable submarino" "Europa Point"
```

站内检索：

```text
site:gibraltar.gov.gi "data centre"
site:gibraltar.gov.gi "Pelagos"
site:gibraltar.gov.gi "Continent 8"
site:gibraltar.gov.gi "Data Centre Hosting Services"
site:gra.gi "data centre"
site:gra.gi "GibFibre" "Gibtelecom"
site:gibtele.com "data centre"
site:continent8.com "Gibraltar"
site:gibfibre.com "data centre"
site:datacenterdynamics.com "Gibraltar" "data center"
```

---

## 9. 枚举矩阵 (Enumeration Matrix)

渠道 × 对象：

| Channel | Gibtelecom | Continent 8 | Pelagos | GibFibre / ISPs | Government | Finance/Gaming | Aggregator/IX |
|---|---|---|---|---|---|---|---|
| Official / tender | Procurement links, regulator | Tender award, gov visit | HMGoG announcement | GRA notices | Hosting/cloud tenders | license-driven demand | — |
| Operator pages | DC/cloud/PoP | Gibraltar location | project specs | fiber/enterprise services | — | case studies | — |
| Regulator/courts | GRA dispute, Mount Pleasant | procurement/gov | planning follow-up | authorised operator | data protection | GFSC/Gambling | — |
| Industry media | network/ownership | contract/cases | 250MW coverage | ISP claims | procurement | gaming demand | market counts |
| Aggregators | duplicate facility seeds | address/description seed | planned entry | weak service seed | — | — | facility/IX seed |
| Connectivity DB | ASN/PoP | network/facility | future network | ASN/routes | — | — | PeeringDB/RIPE/IXPDB |

地理片区 × 预期产出：

| Area | Main objects | Expected yield | Grade cap |
|---|---|---|---|
| Mount Pleasant | Gibtelecom data centre | 1 operating anchor | A/B |
| inside the Rock / former MoD facility | Continent 8 data centre | 1 operating anchor | A |
| Port / North Mole | Pelagos planned campus; power/port context | 1 planned project; no operating until commissioned | A(planned) |
| Europa Point | cable landing/connectivity | landing/connectivity only | B unless facility named |
| Europort / City Centre / Westside | finance, government, offices | 0-2 internal/DR leads | C/B |
| Ocean Village / Bayside | gaming/professional services offices | 0-1 service/DR lead | C |
| North Front / Airport | logistics/telecom equipment | low yield | C |

---

## 10. 分级规则与误报过滤 (Grading & False Positives)

- **A**：运营商自营设施页、政府新闻/采购/授予、监管决定或法院摘要中点名的设施。Gibtelecom service existence、Continent 8 facility、Pelagos announced project 均可按其事实范围给 A。
- **B**：DCD/Computer Weekly/Capacity/Telecoms.com、本地可信媒体、PeeringDB/RIPE、供应商案例。用于补强，不替代运营商/官方。
- **C**：Data Center Map、datacenters.com、company.gi、migration vendors、advertorials、招聘、转售商。只作发现入口。
- **U**：社媒、论坛、无法追溯“stc/Batelco/Pelagos expansion”传闻。

误报过滤：

- 不把 Pelagos 计为 operating，除非出现 commissioning、customer launch、live data hall 或 regulator/utility acceptance 证据。
- 不把 Data Center Map 的数量当作国家设施总数。
- 不把 North Mole Power Station、BESS、substations、telecom masts、PoPs 计为数据中心。
- 不把 GibFibre 的 fiber network 或 enterprise broadband 自动推断成 data centre；找不到物理设施则保持 C。
- 不把 London、Dublin、Malta、Malaysia、Isle of Man 或 Spain 托管节点归入 Gibraltar。
- 不把 Gibraltar office、licence、tax residency 或 gaming licence 当作 facility proof。
