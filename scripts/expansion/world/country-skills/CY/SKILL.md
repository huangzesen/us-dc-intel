---
name: cy-datacenter-methodology
location: scripts/expansion/world/country-skills/CY/SKILL.md
description: |
  Cyprus data-center discovery reconciles OCECPR/IRIS telecom authorisations, TPH/Hippodamos planning, CERA/CTSO/EAC grid (12 MVA threshold), e-PPS/TED procurement, DLS land records, DSA NIS law, and cloud-region checks with operator evidence (Cyta Nicosia/Limassol + RedMax + LCA1, CL8 LIM, Logosnet, PrimeTel, Cablenet) across six districts, with TRNC/north-Cyprus treatment for occupied areas.
---

# CY · 塞浦路斯数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为塞浦路斯数据中心/托管设施发现与审计提供可持续、可复现的查询方法论。
> 分区模型：6 个区（districts）：Nicosia/Lefkosia；Limassol/Lemesos；Larnaca/Larnaka；Famagusta/Ammochostos；Paphos/Pafos；Kyrenia/Keryneia。
> 已知种子：Cyta 两座自有 DC（Nicosia/Aglantzia、Limassol/Amathounta）、Cyta/RedMax（Latsia）、Cyta/Simplex LCA1（Larnaca）、CloudLayer8 CL8 LIM Phase 1（Uptime 认证）、Logosnet DataFort、PrimeTel、Cablenet、CyIX/JumboIX、三个海缆登陆站。
> 本 skill 汇总两份探索报告：官方/监管管线（explorer-official.md）与行业/厂商发现（explorer-industry.md），字段级 A/B/C/U 分级。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：OCECPR/IRIS、DEC、DSA、CERA/CTSO/EAC、TPH/Hippodamos、DLS、e-PPS/TED、DMRID/gov.cy、Uptime 登记、云区域官方页、Great Sea Interconnector |
| explorer-industry.md | 行业/厂商发现：Cyta/CL8/Logosnet/PrimeTel/Cablenet 运营商页、DCD/Cyprus Mail/CBN/KNews/SubTel Forum 等媒体、目录聚合器、IXP/海缆管道 |

## 核心结构事实（框定每次搜索）

1. 行政覆盖完整为 **6 个区**；Republic of Cyprus（ROC）在政府控制区含 Nicosia/Limassol/Pafos/Larnaka 四区加 Famagusta 与 Keryneia 两个占领区名义区。**分区注记**：ROC 对 Kyrenia 与大部分 Famagusta 无有效控制；ROC 官方来源覆盖 Famagusta 政府控制部分（Ayia Napa、Paralimni、Protaras、Deryneia）；Kyrenia 与占领区 Famagusta 须通过土耳其语/TRNC 来源搜索并以 `north-cyprus` 注记记录，不得混入 ROC 许可/登记覆盖。
2. **无单一公共数据中心登记册**；须从电信授权、无线电授权、规划/建筑申请、土地记录、公司登记、电力/电网记录、采购通知、运营商官方页、Uptime 登记、云区域页、IXP 与海缆登陆记录拼接。语言：希腊语/英语覆盖 ROC；土耳其语为 TRNC/北部搜索必需。
3. 电网路由：**CERA** 确认 12 MVA 以上客户向 CTSO 提交并网申请，12 MVA 及以下走 EAC/DSO——塞浦路斯多数设施低于超大规模，可能只在 EAC/DSO 痕迹中出现。CERA 还确认竞争市场 2025-10-01 起商业运营。
4. 法律锚点：电子通信 N.112(I)/2004（OCECPR 登记）；无线电框架（DEC）；网络安全 NIS 法律 N.89(I)/2020 合并 Law 60(I)/2025（DSA，关键/必要实体语境）；规划 Law 90/1972（TPH/Hippodamos）；土地 DLS。
5. 云区域（2026-08-12）：AWS/Azure/GCP/OCI **均无塞浦路斯公共区域**；本地「cloud」为服务声称，除非官方区域页另有说明。
6. 可靠性规则：`Tier III standard`/`Tier III specifications`/`Tier III design`/`Tier III Constructed Facility` 是不同声称，仅 Uptime Institute 登记条目证明认证；海缆登陆站与 IXP 是数字基础设施锚点非数据中心；目录计数（DataCenterMap/Datacenters.com/Cloudscene/OCOLO/Data Center Platform/UpStack/ColocationM）仅作发现线索；北塞声称 U 级直到 BTHK/Kıb-Tek/TRNC 采购或具名运营商页给出物理设施/地址。
7. 地址优先级：运营商官方页 > 许可/DLS/e-PPS/登记 > PeeringDB（IXP/设施）> 可信贸易媒体 > 目录。
8. 已确认/高置信线索：Cyta Nicosia/Aglantzia 与 Limassol/Amathounta（A）；Cyta/RedMax Latsia 协议（A 级协议/位置，B 级规格：193 Giannou Kranidioti Ave、1,300 sqm、420 racks、2 MW 变电站、640 kWp PV/电池、2027 年初商业阶段）；Cyta/Simplex LCA1 Larnaca（A 收购 + 年报近 1 MW/Tier III 规格）；CL8 LIM Phase 1 Limassol（A 运营商 + Uptime 登记）；Logosnet DataFort Nicosia（A）；PrimeTel 四地共置（A 服务，站点 U/C）；CyIX/JumboIX（IXP 语境）；海缆登陆 Pentaskhinos/Ayia Napa/Yeroskipos（A/B 基础设施）。

## 查询模式（复制粘贴模板见 explorer-official.md §3-§5 / explorer-industry.md §1-§6）

- 电信/无线电授权：`site:ocecpr.ee.cy "Μητρώο" "Ηλεκτρονικών Επικοινωνιών" "{operator}"`；`site:iris.cy "{operator}"`；`site:dec.dmrid.gov.cy "{operator}" OR "{area}"`
- 规划（TPH/Hippodamos）：`site:moi.gov.cy/moi/tph "κέντρο δεδομένων" OR "πολεοδομική άδεια"`；`site:hippodamus.tph.moi.gov.cy "{operator}" OR "{address}"`
- 电力（CERA/EAC）：`site:cera.org.cy "data centre" OR "κέντρο δεδομένων" OR "12 MVA"`；`site:eac.com.cy "substation" OR "υποσταθμός" "{area}"`
- 采购：`site:eprocurement.gov.cy "data centre" OR "κέντρο δεδομένων" OR colocation OR hosting`；`site:ted.europa.eu Cyprus "data centre" OR colocation`
- 政府 IT/云：`site:gov.cy/dmrid "data centre" OR "cloud" OR "κυβερνητικό νέφος"`
- 云区域核验：`site:docs.aws.amazon.com/global-infrastructure "Cyprus"`；`site:learn.microsoft.com/en-us/azure/reliability/regions-list "Cyprus"`；`site:cloud.google.com/about/locations "Cyprus"`；`site:docs.oracle.com/iaas "Cyprus"`
- 运营商：`site:cyta.com.cy "data center" OR "RedMax" OR "LCA1"`；`"RedMax" "Giannou Kranidioti" "data center"`；`site:cl8.com Limassol`；`site:logosnet.cy.net data-centre`；`site:primetel.com.cy colocation`；`site:cablenet.com.cy "data center"`
- 贸易媒体：`site:datacenterdynamics.com/en/news/ Cyprus "data center" OR Cyta OR RedMax`；`site:cyprus-mail.com "data centre" OR RedMax`；`site:cbn.com.cy "data centre" OR "Cyta"`；`site:subtelforum.com Cyprus "submarine cable" OR "UGARIT 2"`
- IXP/海缆：`site:peeringdb.com Cyprus CyIX OR JumboIX OR Kermia`；`site:pulse.internetsociety.org/en/ixp-tracker/country/CY Cyprus`；`"Pentaskhinos" OR "Ayia Napa" OR "Yeroskipos" "cable landing"`；`"UGARIT 2" "Pentaskhinos" "CYTA"`
- 土耳其语/TRNC（占领区）：`site:bthk.org "veri merkezi" OR "barındırma"`；`"KKTC" "veri merkezi" "Girne" OR "Gazimağusa"`；`"Kıb-Tek" "veri merkezi" OR "trafo"`
- 希腊语本地清扫：`"κέντρο δεδομένων" "{district}" "Κύπρος"`；`"πολεοδομική άδεια" "κέντρο δεδομένων" "{district}"`

## 官方/监管管线要点（详见 explorer-official.md）

- OCECPR/IRIS 为注册电子通信提供商（Cyta、PrimeTel、Cablenet、Epic、Logosnet、NetShop）授权 A 级来源，非 DC 清单；DEC 无线电授权用于无线回程/频谱关联基础设施。
- DSA NIS 法律（N.89(I)/2020 + Law 60(I)/2025）确认网络安全法律状态；数据中心可能作为数字基础设施/必要实体相关，但 DSA 页不应被期待发布站点地址。
- TPH/Hippodamos 为规划申请/许可官方路线（按宗地/地址/运营商检索）；DLS 为已知地址后的土地/权属核验；高负载项目另查 EIA/环境部通知。
- 12 MVA 阈值：>12 MVA 应有 CTSO 痕迹；较小共置可能只有 EAC/DSO 或无公开负载痕迹。
- e-PPS/TED 搜政府共置/云/托管/备份/UPS/发电机/DR 招标；DMRID/gov.cy 为数字政策/云政策/政府 IT/数据主权信号（爬虫可能 403，保留 URL 与证据日期）。
- Uptime 登记确认 `CL8 LIM Data Center, Phase 1`（Limassol，Cloudlayer8 Limited）——A 级认证；Great Sea Interconnector（1,000 MW、1,208 km、500 kV、希塞段在建）为电网语境。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场小型、服务商主导：Nicosia 与 Limassol 为主集群；Larnaca 因 LCA1/Pentaskhinos 重要；Famagusta/Paphos 主要为海缆语境；Kyrenia 需 TRNC/北塞处理。
- **Cyta**：官方业务数据中心/服务器托管页确认两座 DC（Nicosia/Aglantzia、Limassol/Amathounta）、Tier III-standard 与 ISO 27001 声称（A 级运营商声称，非 Uptime 认证）。
- **RedMax/RedOne（Latsia Industrial Area）**：Cyta 2026-07-15 新闻 A 级收购/扩建协议；DCD/Cyprus Mail/KNews B 级规格与 2027 年初分阶段运营。
- **Simplex LCA1**：Cyta 2025-05-07 新闻 + 2024 年报（近 1 MW、Tier III 规格）A 级；DCD/CBN 叙事 B 级。
- **CloudLayer8 CL8 LIM**：运营商页 + Uptime 登记 A 级；目录地址 Faleas 1, Agios Athanasios 为 C 级直到运营商/登记确认。
- **Logosnet DataFort**：运营商页确认 Nicosia 运营商中立 DataFort、功能、500 kVA 柴油发电机声称与地址（A）。
- **PrimeTel**：四地共置服务 A 级；各站点/区细节 U/C。**Cablenet**：公司/办公室地址 A；设施清单/地址 C 直到设施页/许可/DLS/OCECPR 记录确认。**NetShop**：目录/营销 C；用 OCECPR/IRIS 与 DLS/TPH 确认。**Logicom**：集成/设计服务 A 级，非自有/运营数据中心。
- 假阳性控制：本地 VPS/云营销非公共云区域；IXP 与海缆登陆站非数据中心；Logicom 除非单独证明自有设施否则为集成商；Cablenet 办公室地址非设施证据；北塞托管页需一级 TRNC/运营商证据与物理地址。
- **Khazna/G42 塞浦路斯 MoU**：国家层面投资线索（gov.cy 页爬虫可能 403）；仅作 MoU/投资意向，非站点。
- 事件驱动观察：RedMax 商业运营里程碑、LCA1 整合、CL8 认证变化、Medusa/UGARIT 2 登陆/RFS、Great Sea Interconnector 变化、Khazna/G42 或其他外资数据中心站点公告、TRNC 电子政务/数据中心采购。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| Cyta DC Nicosia/Aglantzia | Nicosia | 运营中；Cyta 官方服务页 A |
| Cyta DC Limassol/Amathounta | Limassol | 运营中；Cyta 官方服务页 A |
| Cyta/RedMax（RedOne）Latsia | Nicosia | 收购/扩建协议（A）；规格/2027 初运营 B |
| Cyta/Simplex LCA1 | Larnaca | Cyta 收购；近 1 MW/Tier III 规格（年报 A；DCD/CBN B） |
| CloudLayer8 / CL8 LIM Phase 1 | Limassol | 运营中运营商中立设施；Uptime 登记 A；目录地址 C |
| Logosnet DataFort | Nicosia | 运营中；运营商页 A |
| PrimeTel 共置（四地） | 多区 | 服务 A；站点 U/C |
| Cablenet Engomi/Nicosia | Nicosia | 办公室地址 A；设施 C |
| NetShop ISP 塞浦路斯 DC | Larnaca/Nicosia/Paphos | 目录/营销 C |
| Logicom Solutions | Nicosia | 集成服务 A；无自有设施 |
| CyIX | Nicosia | 运营 IXP（PeeringDB/ISOC B/A 语境） |
| JumboIX / IPTP Kermia | Limassol | 运营 IXP/设施语境（B/A） |
| Pentaskhinos / Ayia Napa / Yeroskipos 登陆站 | Larnaca/Famagusta ROC/Paphos | 运营海缆登陆站（A/B 基础设施，非 DC） |
| Medusa 塞浦路斯登陆 | 区未决 | 海缆系统语境（A/B，非 DC） |
| UGARIT 2（Pentaskhinos-Tartous） | Larnaca | 2026-08-11 宣布（B；需 Cyta/项目一级页） |
| AWS/Azure/GCP/OCI 塞浦路斯公共区域 | n/a | 无（A 级官方页负面核验） |
| 北塞 / Kyrenia DC | Kyrenia/占领区 | 无一级设施确认（U）；BTHK 仅授权机构 |

## 更新节奏

- 月度：Cyta、CL8、PrimeTel、Cablenet、Logosnet、NetShop 新闻页；DCD、Cyprus Mail、CBN、KNews、SubTel Forum、Telecompaper、Capacity Media。
- 季度：OCECPR/IRIS、DEC、PeeringDB、ISOC Pulse、Uptime 登记、AWS/Azure/GCP/OCI 官方位置、DataCenterMap/Datacenters.com/Cloudscene/Data Center Platform。
- 半年：TPH/Hippodamos、DLS、CERA/CTSO/EAC、e-PPS/TED、Cytaglobal/Submarine Networks/TeleGeography。
- 事件驱动：RedMax 商业运营、LCA1 整合、CL8 认证变化、Medusa/UGARIT 2、Great Sea Interconnector、Khazna/G42 站点公告、TRNC 采购。
- 待办（2026-08-12）：RedMax 规格/2027 时间线官方确认；CL8 街道地址确认；PrimeTel 站点解析；Cablenet 设施页/许可；UGARIT 2 一级页；Khazna/G42 MoU 官方页可达性；codex terra agent 分批复核后按本方法论推进。
