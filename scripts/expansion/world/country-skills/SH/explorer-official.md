# SH Explorer Official：圣赫勒拿、阿森松与特里斯坦-达库尼亚官方/监管一手来源枚举方法论
# （Saint Helena, Ascension and Tristan da Cunha — Official / Regulatory / Primary-Source Discovery）

日期：2026-08-12。国家：**SH — Saint Helena, Ascension and Tristan da Cunha（圣赫勒拿、阿森松与特里斯坦-达库尼亚）**，英国海外领地（British Overseas Territory）。Manifest 已核对：`world-manifest.jsonl` 第 153 行为 `subnational_type = "geographical region"`，**divisions = Ascension / Saint Helena / Tristan da Cunha**。这些是地理区域而不是统一行政二级；每条设施记录必须同时写 manifest 分区与自然子层（例如 Saint Helena / Jamestown 或 Rupert's，Ascension / Georgetown 或 Cat Hill，Tristan da Cunha / Edinburgh of the Seven Seas）。

本文角度：**官方/监管/一手来源**（政府、公报、法规、采购、电信许可、公用事业、海缆所有方、云厂商官方区域页、公开军事/政府记录）。本市场极小，正确产出通常是“已确认 1 条设施 + 若干连接/卫星/采购线索 + 明确阴性覆盖”，不要用海缆、军事站点或卫星站虚增数据中心。

信度分级（Reliability grades）：**A** = 官方/一手来源直接证明相关主张（SHG/AIG/TDG 官网、公报 Gazette/法律文书、英国 FCDO/NAO/议会记录、Sure St Helena、Connect Saint Helena、Google Equiano 官方页、官方云区域页、认证注册处）。**B** = 具名当事方、日期、地点的可靠媒体/行业报道（SAMS、St Helena Independent、The Sentinel、The Islander、DCD、Developing Telecoms、Capacity Media、Submarine Networks、TechAfrica News 等）。**C** = 目录站、SEO 托管页、承包商作品集、社交帖、活动简介、转引报道、无地址/设施证据的主张。

---

## 0. 已核实国家基线（Verified national baseline）

- **已确认数据中心设施：1 条**。`St Helena Government Main Data Centre, Carnarvon Court, Jamestown`（Saint Helena / Jamestown）已入库；owner = St Helena Government；`status: operational`；`capacity_mw: null`；`evidence_date: 2022-03-07`；A 级。SHG 2022-03-07 发布确认 Schneider Electric 工程师到岛调试关键后备蓄电池，地点包括 “SHG Main Data Centre at Carnarvon Court in Jamestown” 与 Connect Saint Helena 在 Carnarvon Court 的核心设备服务。Gazette EX-GAZ-9 PDF 对工程师隔离豁免形成配套一手证据。
- **官方证据 URL 已核实真实**：
  - `https://www.sainthelena.gov.sh/quarantine-exemption-for-engineers-to-commission-critical-backup-solutions/`
  - `https://www.sainthelena.gov.sh/app/uploads/gazette/EX-GAZ-9-Exemption-from-Isolation-Order-Engineer-S-Leak-R-Jayeesan.pdf`
  - `https://www.sainthelena.gov.sh/shg-invites-expressions-of-interest-for-st-helena-electronic-communications-providers/`
- **无商业 colocation、无超大规模云区域证据**。AWS、Azure、GCP、OCI 官方区域页截至本批次未列 Saint Helena、Ascension 或 Tristan da Cunha。Google 海缆登陆不等于 GCP 区域。
- **Equiano 圣赫勒拿支线是主要数字基础设施事件**。SHG 官方页确认 Saint Helena 分支长约 1,154 km，连接 Equiano 主干；2021-08-26 标志该分支登陆，2021-08-29 在 Rupert's Beach 完成岸端登陆；2023-05-21 至 2023-05-26 完成 Cable Landing Station / SLTE 最终调试，SHG 2023-06-01 称 SLTE 已测试并 live；2023-09-01 SHG 称 Equiano 已 live，并通过 Sure 让公众从 2023-10-01 使用基于海缆的服务。
- **登陆站不是数据中心**。Rupert's Beach / Rupert's Valley 的 Modular Cable Landing Station（MCLS）是连接基础设施；只有出现明确托管、机架、服务器代管或企业 colo 服务证据时才可提升为 DC 设施记录。不得与 Jamestown 的 Carnarvon Court 合并。
- **Connect Saint Helena 官网应使用 `http://www.connect.co.sh/` / `http://www.connect.co.sh/about-us.html`**。本批次发现 www.connect.co.sh 的 HTTPS 形式有 TLS handshake failure，但 HTTP 站点可访问；旧草稿中的 connectsthelena.com 未验证为当前官网。
- **Ascension**：AIG 官网真实；AIG 2025/2026 电信更新确认 Sure South Atlantic 将于 2026-02-28 停止岛上电信服务角色，Omnitouch 将从 2026-03-01 成为 incoming telecommunications service provider。该事实只证明电信运营转换，不证明数据中心。军事/政府通信设施不公开，不能推断 DC。
- **Tristan da Cunha**：TDG 官网真实；2024-09-22 官方新闻确认 Starlink 已到岛，且原有 geostationary satellite VSAT 仍提供 10 Mbps 并承载语音流量。Starlink/VSAT 是卫星连接，不是数据中心。
- 诚实产出预期：**1 条确认设施**（SHG Main Data Centre, Carnarvon Court）+ **连接设施记录/线索**（Equiano MCLS/landing station、Teleport & Data Centre 采购历史、Tristan IT Container/Starlink 连接线索）+ Ascension/Tristan 阴性覆盖。容量无一手来源时一律 `capacity_mw: null`。

---

## 1. 官方与一手来源（Official and primary sources）

### 1.1 St Helena Government（SHG）— 门户、公报、法规、规划、采购

主入口：
- SHG 门户：`https://www.sainthelena.gov.sh/`
- Gazette 公报：通过 SHG 导航 `News -> Gazette` 与 `site:sainthelena.gov.sh/app/uploads/gazette/` 查 PDF；EX-GAZ-9 已核实可访问。
- 法规：SHG 导航下存在 Laws of Ascension / Laws of St Helena / Laws of Tristan da Cunha 入口；枚举时用导航或 `site:sainthelena.gov.sh legislation` 确认当前 URL。
- 规划/建筑：SHG 导航下 `Land Planning and Building Control Division` 与 `Planning & Building` 是机房改造、发电机、冷却、配电、MCLS 附属工程的高信号入口。
- 采购：SHG 新闻/采购/EOI 页面与公报均需查。2020 EOI 明确列 “Teleport & Data Centre on-Island and International Connectivity”，但这是历史采购需求/服务范围，不等同于新商业 DC。

查询模板（EN）：
```text
site:sainthelena.gov.sh ("data centre" OR "data center" OR datacenter OR "server room" OR teleport OR hosting OR UPS OR "backup battery")
site:sainthelena.gov.sh/app/uploads/gazette ("data centre" OR "data center" OR Carnarvon OR telecom OR "landing station")
site:sainthelena.gov.sh (planning OR "development control" OR "building control" OR permission) ("data centre" OR telecom OR generator OR UPS)
"Carnarvon Court" ("data centre" OR "server" OR Schneider OR battery)
site:sainthelena.gov.sh ("expressions of interest" OR EOI OR tender OR procurement) (telecom OR "electronic communications" OR "data centre")
```

### 1.2 电信与许可（Telecom：Sure St Helena、SHG licence/EOI）

主路线：
- Sure St Helena：`https://www.sure.co.sh/`。官网已核实，页面说明 Sure 提供 Saint Helena 的 broadband、mobile phone、national & international telephone、public Internet、television rebroadcast services；还称 Sure 属 Beyon 集团。该页证明电信服务商事实，**不证明 colo/DC**。
- SHG 许可/服务采购：2020 EOI 页面真实，服务清单包括 Residential/Voice & Data、Business/Government Voice & Data、Teleport & Data Centre、Mobile、TV、Internet（DNS/managed firewall/mail filtering/domain/web hosting/transit）。该页面可作为 C+/历史线索，除非后续合同/设施/地址文件证实。
- Sure 延期与海缆接入：SHG 2023-09-01 “St Helena connects to the Subsea Cable” 说明 SHG 与 Sure 延长许可，并将服务由 satellite-based 转向 cable-based，目标从 2023-10-01 提供新服务；这是电信状态 A 级，不是数据中心证据。

查询模板：
```text
site:sure.co.sh ("landing station" OR Equiano OR "data centre" OR datacenter OR colocation OR teleport OR business)
"Sure St Helena" (Equiano OR "submarine cable" OR "landing station" OR license OR licence)
site:sainthelena.gov.sh Sure ("subsea cable" OR Equiano OR licence OR license OR "1 October 2023")
site:sainthelena.gov.sh "Teleport & Data Centre"
```

### 1.3 电力与公用事业（Power：Connect Saint Helena）

主路线：
- Connect Saint Helena Ltd 当前可访问官网：`http://www.connect.co.sh/`；About 页：`http://www.connect.co.sh/about-us.html`。
- About 页确认 Connect Saint Helena Ltd 为商业化运营公司，负责向 St Helena Island 社区提供多公用事业服务；公司归 St Helena Government 所有，2013-04-01 开始运营；核心服务为 Electricity、Water、Wastewater；受 St Helena Utilities Regulatory Authority 监管。
- 与 DC 枚举有关的信号：Carnarvon Court 核心设备、发电/输配电、电池/UPS、规划许可、发电机和可再生能源项目。不要从发电装机、特许权金额或电价推断数据中心容量。

查询模板：
```text
site:connect.co.sh (generation OR "electricity generation" OR solar OR battery OR "power station" OR outage OR "Carnarvon Court")
site:sainthelena.gov.sh ("Connect Saint Helena" OR "Connect St Helena" OR electricity OR "power station" OR solar OR battery)
"Connect Saint Helena" ("Carnarvon Court" OR generator OR UPS OR "data centre")
```

### 1.4 Equiano / Fibre Optic Cable Project（海缆与登陆站）

已核实官方 URL：
- SHG fibre project hub：`https://www.sainthelena.gov.sh/st-helena/government/portfolios/economic-development-portfolio/sustainable-development/fibre-optic-cable-project/`
- SHG signs contract with Google：`https://www.sainthelena.gov.sh/st-helena-government-signs-contract-with-google-to-land-subsea-cable/`
- MCLS definitions：`https://www.sainthelena.gov.sh/st-helena/government/portfolios/economic-development-portfolio/sustainable-development/fibre-optic-cable-project/fibre-optic-cable-definitions/`
- Equiano CLS commissioning complete：`https://www.sainthelena.gov.sh/equiano-cable-landing-station-commissioning-works-complete/`
- St Helena connects to the subsea cable：`https://www.sainthelena.gov.sh/st-helena-connects-to-the-subsea-cable/`
- Google Equiano announcement：`https://cloud.google.com/blog/products/infrastructure/introducing-equiano-a-subsea-cable-from-portugal-to-south-africa`

核实时间线：

| 日期 | 事件 | 等级与说明 |
|---|---|---|
| 2019-06-28 | Google 发布 Equiano：从 Portugal 到 South Africa，沿途 branching units；Google fully funded；ASN 建设合同 Q4 2018 | A（Google 官方） |
| 2019-07 | SHG 签 Letter of Intent，保留 Equiano Phase 1 branch | A（SHG 2019-12 合同公告回溯） |
| 2019-12-23 | SHG 与 Google 签合同，将 St Helena 接入 Equiano Phase 1，提供第一条对外 fibre optic connectivity | A（SHG） |
| 2021-08-26 / 2021-08-29 | SHG project hub 称 2021-08-26 标志分支登陆；2021-08-29 在 Rupert's Beach 完成岸端登陆 | A（SHG；两日期均保留，记录具体事件时注明口径） |
| 2023-05-21 至 2023-05-26 | Telecom Egypt subcontractual deployment team 完成 Equiano SLTE 安装、集成、测试 | A（SHG） |
| 2023-06-01 | SHG 称 SLTE working as intended，meaning it is now live | A（SHG） |
| 2023-09-01 | SHG 称 Equiano subsea cable is live，并公布 Sure 从 2023-10-01 面向公众的新服务安排 | A（SHG） |
| 2023-10 | SHG project hub 称 verification and commissioning document 于 2023 年 10 月签署 | A（SHG hub） |

决策规则：
- MCLS / Cable Landing Station / SLTE / PFE 默认是连接设施，不是 DC。
- Rupert's Beach/Rupert's Valley 与 Carnarvon Court/Jamestown 是不同地点。
- Equiano 主线不经过 Ascension 或 Tristan da Cunha；每批次仍用 `submarinecablemap.com` / TeleGeography / Submarine Networks 复核是否出现新海缆或 landing point。

查询模板：
```text
site:sainthelena.gov.sh Equiano (cable OR "landing" OR Rupert OR "submarine" OR SLTE OR MCLS)
site:sainthelena.gov.sh "Cable Landing Station" "St Helena"
"Equiano" "St Helena" (landing OR Rupert OR "ready for service" OR "1 October 2023")
"St Helena" "landing station" (Equiano OR Rupert) ("data centre" OR colocation OR hosting)
site:submarinenetworks.com ("St Helena" OR "Saint Helena" OR Equiano)
site:submarinecablemap.com ("Ruperts Bay" OR "Saint Helena")
```

### 1.5 Ascension — AIG 与公开电信/军事边界

主入口：
- AIG：`https://www.ascension.gov.ac/`
- AIG telecommunications partnership：`https://www.ascension.gov.ac/aig-announces-telecommunications-partnership`
- AIG telecom advisor/tender/public documents：通过 `site:ascension.gov.ac telecommunications tender procurement` 与 AIG Public Documents 查。

已核实基线：
- AIG 2026 转换公告确认 Sure South Atlantic Ltd 将于 2026-02-28 停止 on-island telecommunications provider 角色；Omnitouch 从 2026-03-01 接续，并设计、安装、测试含 4G mobile 的新系统。该证据为 A 级电信运营状态，**无 DC/colo/机房证据**。
- RAF Ascension、US/Space Force 站点、BBC Atlantic Relay 等为军事/政府/广播通信设施；公开资料不足以枚举为 DC。只有 MoD/AIG/BBC/USSF 一手文件明确设施性质、地址、状态时才记录，且通常仍是通信/地面站而非数据中心。

查询模板：
```text
site:ascension.gov.ac ("data centre" OR "data center" OR datacenter OR "server room" OR telecom OR communications OR tender OR procurement)
site:ascension.gov.ac (Omnitouch OR Sure OR "telecommunications provider" OR "4G mobile")
"Ascension Island" ("data centre" OR datacenter OR "server room" OR colocation)
"Ascension Island" ("submarine cable" OR "landing station" OR fibre OR satellite)
"Ascension Island" (RAF OR USSF OR "Space Force" OR BBC) (communications OR "earth station" OR satellite)
```

### 1.6 Tristan da Cunha — TDG（卫星连接，预期阴性）

主入口：
- TDG / Tristan da Cunha Government：`https://www.tristandc.com/`
- Starlink update：`https://www.tristandc.com/government/news-2024-09-22-starlink.php`

已核实基线：
- TDG 2024-09-22 新闻确认 Starlink 已投入使用；Starlink 天线在 IT Container（Communications HQ，2022-05 commissioned）屋顶，位置在 Administration building 旁；原 VSAT geostationary satellite 仍提供 10 Mbps，语音流量仍走该路线。
- 该信息证明 **satellite/communications HQ**，不是数据中心。IT Container 可作为通信线索（C+/A 对通信事实），不得当作 DC 设施，除非后续 TDG 一手文件明确服务器托管/机房功能。

查询模板：
```text
site:tristandc.com ("data centre" OR "data center" OR datacenter OR server OR "server room")
site:tristandc.com (internet OR satellite OR VSAT OR Starlink OR telecom OR "IT Container" OR "Communications HQ")
"Tristan da Cunha" ("data centre" OR datacenter OR hosting OR colocation)
"Tristan da Cunha" ("Edinburgh of the Seven Seas") (telecom OR internet OR electricity)
```

### 1.7 英国资金链、审计与公司注册

主路线：
- FCDO/gov.uk：`https://www.gov.uk/`
- UK Parliament Hansard：用 `hansard.parliament.uk` 域名检索（该站可能对自动 curl 返回 403）
- NAO：`https://www.nao.org.uk/`
- Companies House：`https://find-and-update.company-information.service.gov.uk/`
- SHG audit PDF（Fibre Optic Cable Network Project performance audit）：`https://www.sainthelena.gov.sh/documents/ASH-Performance-Audit.pdf`

用途：
- 核实 Equiano 支线资金、合同、审计结论、采购延误、PPP/公用事业实体与股权事实。
- 金额与合同值可作为融资/项目背景，不可推导 MW、机架、面积或 DC 规模。

查询模板：
```text
site:gov.uk "St Helena" (cable OR telecom OR digital OR "data centre" OR Equiano)
site:hansard.parliament.uk "St Helena" (cable OR telecom OR digital OR Equiano)
site:nao.org.uk "St Helena" (cable OR telecom OR airport OR infrastructure)
site:find-and-update.company-information.service.gov.uk "Connect Saint Helena"
site:sainthelena.gov.sh/documents "Fibre Optic Cable" audit
```

### 1.8 云区域缺位核验（Official cloud-region absence checks）

每批次必查官方页，并把缺位作为“已核实检查项”：
- AWS：`https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`
- Azure：`https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- GCP：`https://cloud.google.com/about/locations`
- OCI：`https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm`

截至本批次，四家官方页检索 Saint Helena / St Helena / Ascension / Tristan 均无 SH 区域。目录站或本地 VPS/hosting 页面只能作为 C 级服务线索。

---

## 2. 分区覆盖工作流（Division coverage workflow）

必须逐一覆盖 manifest 三分区；每个分区要么分配项目/线索，要么显式写 “no public data-centre project found”。

### 2.1 Ascension

| 子层 | 优先级 | 官方优先路线 | 当前结论 |
|---|---:|---|---|
| Georgetown / Two Boats | 中 | AIG 新闻、采购、公共文件、电信转换公告 | 电信服务转换已证实；无 DC |
| Cat Hill / Traveller's Hill / Wideawake / English Bay | 低 | UK/US/BBC 一手公开记录 | 通信/军事/广播站点不公开；无公开 DC 证据 |

```text
"Ascension" ("data centre" OR "data center" OR datacenter OR "server room" OR hosting OR colocation)
site:ascension.gov.ac ("data centre" OR telecom OR communications OR tender OR procurement)
"Ascension Island" ("submarine cable" OR "landing station" OR fibre OR satellite)
```

### 2.2 Saint Helena

| 子层/定居点 | 优先级 | 官方优先路线 | 当前结论 |
|---|---:|---|---|
| Jamestown / Carnarvon Court | 高 | SHG、Gazette、Connect、规划/采购 | SHG Main Data Centre 已确认 A；容量 null |
| Rupert's Beach / Rupert's Valley | 高（连接） | SHG fibre project、MCLS/SLTE、Sure | Equiano MCLS/landing station 已确认连接设施；非 DC |
| Longwood、Half Tree Hollow、Blue Hill、Sandy Bay、Prosperous Bay Plain | 中低 | SHG 规划/建筑、电力、机场 ICT | 无公开 DC；机构机房仅 C 线索 |

```text
("Saint Helena" OR "St Helena") ("data centre" OR "data center" OR datacenter OR "server room" OR hosting OR colocation) (Jamestown OR Rupert OR Longwood)
("Carnarvon Court" OR "Rupert's" OR "Ruperts") ("data centre" OR teleport OR "landing station" OR telecom OR UPS)
site:sainthelena.gov.sh ("Saint Helena" OR Jamestown OR Rupert) ("data centre" OR telecom OR electricity OR planning)
```

### 2.3 Tristan da Cunha

| 子层 | 优先级 | 官方优先路线 | 当前结论 |
|---|---:|---|---|
| Edinburgh of the Seven Seas / Administration building | 低 | TDG news、Starlink/VSAT、IT Container | 卫星连接与 IT Container 通信线索；无 DC |

```text
"Tristan da Cunha" ("data centre" OR "data center" OR datacenter OR "server" OR hosting OR colocation)
site:tristandc.com (telecom OR internet OR satellite OR VSAT OR Starlink OR "IT Container")
```

---

## 3. 设施种子清单（Facility seed list for enumerators）

| 种子 | 建议归属（分区/子层） | 状态 | 等级 | 处理 |
|---|---|---|---|---|
| SHG Main Data Centre, Carnarvon Court, Jamestown | Saint Helena / Jamestown | operational；evidence 2022-03-07 | **A** | 已确认设施；容量 `null`；使用 SHG 发布 + Gazette PDF |
| Connect Saint Helena core equipment, Carnarvon Court | Saint Helena / Jamestown | operational core utility equipment | A（设备事实）/ C（DC 线索） | 不单列 DC，除非后续文件证明独立机房/托管 |
| Equiano Modular Cable Landing Station / SLTE, Rupert's | Saint Helena / Rupert's | connected/live 2023 | A（连接事实） | 连接设施；非 DC；可做海缆/landing record |
| SHG Teleport & Data Centre services（2020 EOI） | Saint Helena / 待定位 | historical procurement lead | C+/A 对 EOI 存在 | 复查是否再招标/合同；无地址不成 DC |
| AIG civil telecom facilities | Ascension / Georgetown 或待定位 | telecom lead | C 至 A（按来源） | 无公开 DC 证据 |
| RAF/USSF/BBC communications facilities | Ascension / 军事区 | non-public communications | 阴性边界 | 不从基地存在推断 DC |
| Tristan IT Container / Starlink + VSAT | Tristan da Cunha / Edinburgh of the Seven Seas | satellite communications | A（TDG 通信事实）/ 非 DC | 记录连接线索；非 DC |

---

## 4. 陷阱与决策规则（Pitfalls and decision rules）

- **manifest 拼写**：记录分区必须用 `Ascension` / `Saint Helena` / `Tristan da Cunha`；查询可同时用 `St Helena` 与 `Saint Helena`。
- **登陆站 != 数据中心**：MCLS、SLTE、PFE、shore end、landing station 都是连接基础设施；没有机架/托管/客户/运营服务证据时不得升格。
- **卫星 != 数据中心**：Starlink、VSAT、teleport、earth station 是连接线索；不自动产生 DC。
- **军事设施不公开**：Ascension 的 RAF/USSF/BBC 通信资产不因存在而进入 DC 清单。
- **云区域缺位**：四大云官方区域页缺位必须复查；Google Equiano 不等于 GCP region。
- **容量保守**：无明确一手 MW/kW/rack/white-space 来源时写 `capacity_mw: null`。
- **目录污染**：datacenters.com、DataCenterMap、PeeringDB、VPS/hosting SEO 页只做 C 级种子，必须回到一手域验证。
- **旧 URL 修正**：Connect Saint Helena 当前官网按 `http://www.connect.co.sh/` 使用；若 HTTPS 未来恢复再更新。
