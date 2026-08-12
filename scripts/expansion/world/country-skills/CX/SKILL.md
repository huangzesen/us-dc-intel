---
name: cx-datacenter-methodology
location: scripts/expansion/world/country-skills/CX/SKILL.md
description: 圣诞岛数据中心发现与审计方法论（bilingual）。Christmas Island datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (DITRDCA Indian Ocean Territories portal & Service Delivery kit, Shire of Christmas Island/WA planning, Vocus ASC cable landing, Google Bosun/Dhivaru & EPBC referral, Telstra/CiFi/nbn/ACMA, AusTender/budget/Home Affairs, IOT Power Service, official cloud-region absence checks) plus industry/trade-press discovery (Reuters/ABC/Guardian/DCD Google AI data-centre lead, Vocus/CiFi/Telstra operator pages, PRL/CIP power/land leads, directories). Division model: country with 1 division (Christmas Island). Read before running CX exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# CX · 圣诞岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：圣诞岛（Christmas Island, CX；澳大利亚海外领地，Indian Ocean Territories）人口 1,692（2021），截至 2026-08-12 公开一手来源未确认运营中的商业 colocation、云区域、超大规模或 AI/HPC 数据中心。但 CX 已不是「仅卫星连接」的空白市场：**Vocus 的 Australia Singapore Cable（ASC）已在 Flying Fish Cove 登陆**，CiFi 使用 ASC 提供本地宽带/4G LTE，Telstra 提供 4G 移动服务，Google 已宣布多条与圣诞岛相关的新海缆。正确枚举结论应区分：**已确认电信设施（A）**——Vocus ASC 登陆/landing station、Telstra 4G、CiFi 本地固定无线/4G LTE 与 ASC 回程；**规划/审批中的电信基础设施（A/B）**——Google Australia Connect 的 Bosun 与 interlink cable、Google Dhivaru、EPBC referral 中的 Flying Fish Cove cable landing works；**未确认数据中心（B/C lead）**——Reuters/ABC/Guardian 等关于 Google 在圣诞岛建设 AI data centre/data hub 的报道与郡议会记录线索（Google 对部分报道有否认/淡化表述，未见同等强度的一手政府批准、Google 数据中心公告、AusTender 或电力接入批准，只能作 lead 不能计已确认 facility）。本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双轨三角验证；本 skill 汇总两份最终审定报告，作为 CX 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | DITRDCA IOT 门户与 Service Delivery Arrangements kit、Shire of Christmas Island（shire.gov.cx）与 WA planning、Vocus ASC 官方、Google Australia Connect/Bosun/Dhivaru + EPBC referral、Telstra/CiFi/nbn/ACMA、AusTender/budget.gov.au/Home Affairs、IOT Power Service、四大云区域缺失检查 |
| explorer-industry.md | 行业/厂商/媒体发现 | Vocus/CiFi/Telstra 运营商页、Google 官方海缆公告与 AI data-centre 报道（Reuters/ABC/Guardian/Capital Brief/DCD）、PRL/CIP 与 IOT Power Service 土地/电力线索、Serco/Home Affairs 受限 ICT、Submarine Networks/TeleGeography、目录（datacentermap/datacenters/cloudscene/peeringdb）、中文/SEO rumor watch |

## 核心结构事实

1. **行政区划模型**：manifest 为 **country**，恰好 **1 个 division：`Christmas Island`**；sub_location 标注地点：**Flying Fish Cove / Settlement**（高——ASC landing station、Google cable landing works、政府/港口/运营商设施）、**Phosphate Hill / Quarry Road**（高——IOT Power Service、CIP/PRL、可能 data hub 电力/土地线索）、**Airport / XCH / YPXM**（高用于传阅——Google 报道土地/data hub 线索）、**Kampong / Jalan Pantai**（中——IOT Administration ICT）、**Drumsite**（中——CiFi 办公室/本地网络）、**North West Point**（中/受限——拘留中心 ICT 合同）、**Silver City / Poon Saan / Kampong 住宅区**（低——verified-negative）、**Phosphate mine / PRL / CIP**（中——企业 IT/电力）。
2. **注册库现状**：无公开数据中心注册库；官方枚举目标 = 电缆登陆站/landing infrastructure、政府或运营商服务器机房、可公开许可的 AI/data-centre 项目，以及全分区 verified-negative 结论；无审批/会议记录时不得从媒体报道升级。
3. **法律与监管**：圣诞岛与科科斯（基林）群岛合称 Indian Ocean Territories（IOT）；澳大利亚政府经 DITRDCA（Department of Infrastructure, Transport, Regional Development, Communications, Sport and the Arts）负责，经服务交付安排提供类似州政府的服务；Shire of Christmas Island（shire.gov.cx）处理地方规划/建筑审批，WA planning 提供本地规划方案；电信经 ACMA；采购经 AusTender。
4. **互联与云（负向+例外）**：**Vocus ASC**（A 级：2018-09 投运，4,600 km、up to 60 Tbps、Perth-Singapore 经圣诞岛与印尼，Vocus 设计/建设/运营）；landing station 在 **Flying Fish Cove** 的 Administration building 旁（DITRDCA IOT bulletin 2018 + ABC 2019 交叉）；**CiFi** 自称岛上唯一 fibre ISP、网络完全由 Vocus ASC 支撑、办公室在 Settlement 与 Drumsite；**Telstra 4G**（Parks Australia 官方旅行页确认；ARN/Telecompaper 2022 报道 Vocus/Telstra 用 ASC backhaul 升级 2G→4GX）；**Google Bosun**（Darwin-Christmas Island + 通往新加坡，官方 A）与 **Dhivaru**（Maldives-Christmas Island-Oman，官方 A）+ interlink cable（Melbourne-Perth-Christmas Island）；**EPBC referral**「Subsea Fibre Optic Data Cable Systems Installation - Australia West」覆盖 Bosun 与 Flying Fish Cove landing works（A）；官方 AWS/Azure/GCP/OCI 区域页无 CX（A 级缺失；澳大利亚大陆区域不覆盖圣诞岛本地设施）；无公开商业托管目录证据。
5. **设施/项目种子（2026-08 证据状态）**：**ASC cable landing station（Flying Fish Cove）**——A/B，telecom/cable landing infrastructure，非 colocation；**CiFi 本地 ISP/fixed wireless/4G LTE**——A，网络运营商 lead，不计 colo；**Telstra 4G/4GX**——A/B，移动电信设施，不计 DC；**Google Bosun/interlink cable**——A/B，planned/approval，planned cable/landing project；**Google Dhivaru**——A，planned subsea cable connectivity；**Google AI data centre/data hub**——B/C lead（Reuters 2025 经 ABC/Guardian/Capital Brief 转述；Google 否认/淡化，称属 subsea cable/digital resilience；缺一手 data-centre approval 或 Google facility 公告前不得升级 A）；**政府/Shire server rooms**——A lead（仅命名项目时计）；**PRL/CIP 企业 IT/电力**——B/C，不计 DC 除非命名 facility；**North West Point 拘留中心 ICT**——A/B lead，只记合同层面；**商用 colo/云区域**——verified negative。
6. **语言与词汇**：英文为主；**Kiritimati 混淆防护**——「Christmas Island」也是基里巴斯 Kiritimati，所有查询必须加 Australia / Indian Ocean / CX 或 `-Kiritimati -Kiribati`；**.cx 域名滥用**——`.cx` 被商业滥用，优先 shire.gov.cx、cifi.com.au、gov.au，不用裸 `site:.cx` 当证据；中文/SEO rumor watch 词：圣诞岛 数据中心/算力/AI 数据中心（默认 C）。
7. **可靠性分级**：A = 运营商/厂商/政府一手（Vocus、CiFi、Telstra、Google 官方、DITRDCA/Shire/WA/EPBC/AusTender/budget/Home Affairs、官方云区域页）；B = 权威行业/主流媒体（Reuters/ABC/Guardian/DCD/Submarine Networks/ARN/Telecompaper/Capital Brief——具名文件或官员）；C = 目录/聚合/营销/社交传阅（datacentermap/datacenters/cloudscene/peeringdb、VPS/offshore hosting 营销、无来源转述）。**升级标准**：A 级 facility = 一手来源命名设施/项目+功能+地点，或官方/运营商来源 + 许可/规划/采购来源交叉确认；B 级 lead = 媒体点名文件或官员但缺公开一手审批/运营商设施页；C 级 ignore/rumor = 目录、SEO、社交、无来源转述，仅作二次搜索词。
8. **计数与去重规则**：电缆登陆站 ≠ 商业 DC（ASC landing station 与 Google cable landing works 是电信基础设施，无机架/托管/互联产品时不计 colocation）；卫星/4G/Wi-Fi ≠ DC（Sky Muster、Telstra 4G、CiFi fixed wireless、Starlink、机场 Wi-Fi 都是连通性）；电力设施 ≠ DC（IOT Power Service、柴油机组、太阳能/BESS、PRL/CIP energy plans 只作可行性/否定或支撑材料）；拘留中心受限（North West Point ICT 只记录公开合同或官方文件，不推断内部机房）；云区域缺位（澳大利亚大陆区域≠CX 本地设施）；Google data centre rumor——2025 媒体与 Shire 线索值得追踪，但 Google 官方公开材料核实的是海缆，报道被公司否认/淡化时可靠性保持 B/C lead；目录即使出现 Christmas Island 条目也降为 C 直至有地址、运营商和一手来源。

## 常用查询模板

```text
# 官方
site:infrastructure.gov.au "Christmas Island" ("data centre" OR "data center" OR server OR ICT OR "subsea cable" OR "landing station")
site:infrastructure.gov.au "Christmas Island" "Vocus" "cable landing station"
site:infrastructure.gov.au "Indian Ocean Territories" ("Power Service" OR electricity OR solar OR telecommunications)
site:shire.gov.cx ("data centre" OR "data center" OR Google OR "planning approval" OR "building approval" OR "development application")
site:shire.gov.cx ("server" OR ICT OR IT OR cyber OR network)
site:wa.gov.au "Shire of Christmas Island" ("local planning scheme" OR "structure plan")
# 海缆/运营商
site:vocus.com.au "Christmas Island" "Australia Singapore Cable"
"Flying Fish Cove" "cable landing station" "Christmas Island" ; "Australia Singapore Cable" "Flying Fish Cove" Vocus
site:cifi.com.au "Christmas Island" ("data centre" OR hosting OR colocation OR "carrier grade")
site:telstra.com.au "Christmas Island" (4G OR 4GX OR "data centre" OR exchange OR backhaul)
site:nbnco.com.au "Christmas Island" ("Sky Muster" OR satellite OR outage) ; site:acma.gov.au "Christmas Island" (carrier OR licence OR spectrum)
# Google
site:cloud.google.com "Christmas Island" ("Bosun" OR Dhivaru)
site:epbcpublicportal.environment.gov.au "Christmas Island" "Flying Fish Cove" "subsea"
"Christmas Island" "Google" ("data centre" OR "data center" OR "data hub") site:shire.gov.cx
"Google" "Christmas Island" ("AI data centre" OR "data hub" OR GPU OR HPC) -Kiritimati
# 采购/电力/受限
site:tenders.gov.au "Christmas Island" (ICT OR "data centre" OR "data center" OR server OR cable OR satellite OR power OR Google)
site:budget.gov.au "Christmas Island" ("subsea cable" OR "data centre" OR digital OR telecommunications)
site:homeaffairs.gov.au "Christmas Island" (ICT OR "North West Point" OR detention OR Serco)
"Christmas Island" "IOT Power Service" (capacity OR generator OR solar OR battery OR "data centre")
"Christmas Island Phosphates" (Google OR "data centre" OR power OR solar OR lease)
"Serco" "Christmas Island" (ICT OR server OR "data centre")
# 云/目录负面
site:datacentermap.com "Christmas Island" ; site:datacenters.com "Christmas Island" ; site:cloudscene.com "Christmas Island" OR "Flying Fish Cove"
site:peeringdb.com "Christmas Island" OR "CX"
"Christmas Island" Australia ("data centre" OR datacenter OR colocation OR "rack space" OR "carrier hotel") -Kiritimati -Kiribati
# 中文/SEO rumor watch（默认 C）
"圣诞岛" "数据中心" Google 澳大利亚 -基里巴斯 ; "Christmas Island" "AI 数据中心" OR "算力"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **DITRDCA / IOT**：IOT 门户（注意部门名称随内阁组合变化，URL 路径可能保留旧 `territories-regions-cities`）；Service Delivery Arrangements kit（2024-11 PDF）描述 NBN Sky Muster、本地宽带、Vocus spur line 与 CiFi，并列出 IOT Administration、IOT Power Service 和 Shire 联系地址；IOT bulletins 检索历史项目。
- **Shire/WA planning**：Shire 官网真实可用（public notices、annual reports、planning/building、council meetings）；**Shire 会议记录是数据中心传阅的关键核查入口**——没有审批/会议记录时不得从媒体报道升级；WA planning 提供本地规划方案。
- **Vocus ASC**：官方页确认 2018-09 投运、4,600 km、60 Tbps、Perth-Singapore；IOT bulletin 2018 确认 landing station 建在 Flying Fish Cove Administration building 旁；ASC landing station 是 telecom/cable landing infrastructure，除非 Vocus/CiFi/政府明确公开机架托管或互联服务否则不计 colocation。
- **Google/EPBC**：Google 官方核实的目前是海缆/连接项目（Bosun 连接 Darwin 与 Christmas Island 并通往新加坡、interlink cable、Dhivaru 连接 Maldives/Christmas Island/Oman），不是 CX 数据中心；EPBC referral 核实 cable systems and landings，不等于 data centre approval；媒体所称 Google AI/data hub 必须等待 Google 官方、澳政府审批、Shire planning approval 或电力/土地文件交叉确认。
- **Telstra/CiFi/nbn/ACMA**：CiFi/Telstra/nbn 网络设施只按电信设施或 server-room lead 记录；零售宽带、4G 基站、Wi-Fi hotspot 和卫星终端不计为数据中心；ACMA 查 carrier/licence/spectrum。
- **AusTender/budget/Home Affairs/power**：提取政府 ICT、拘留中心合同（North West Point，公开性受限，只记录合同层面的 ICT lead）、电力升级、海缆建设、土地/机场/安全项目；IOT Power Service（11-13 Quarry Road, Phosphate Hill）与 2020 bulletin（太阳能接入规则变化）作电力过滤。
- 首轮扫描顺序：manifest 确认（CX 单分区）→ DITRDCA IOT + Service Delivery kit + Shire + WA planning → 已有电信（Vocus ASC + 2018 landing bulletin + CiFi + Telstra/Parks Australia）→ 新海缆（Google Bosun + Dhivaru + EPBC referral + Shire planning）→ 数据中心传阅（Reuters/ABC/Guardian/DCD lead → Shire minutes/planning → EPBC/AusTender/Home Affairs/Defence/Google 官方交叉）→ 电力过滤（IOT Power Service、Phosphate Hill、PRL/CIP）→ 云/colo/目录负面（官方云区域页 + datacentermap/datacenters/cloudscene）→ 写入候选时 A 级设施、B/C 级 lead、verified-negative 分开记录。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 行业判断：**CX 是海缆登陆与边缘连接节点，不是已确认的商业数据中心市场**；行业枚举保持三层：A 级已确认（Vocus ASC landing、CiFi 本地 ISP、Telstra 4G、Google 官方海缆项目）；B 级重点 lead（Reuters/ABC/Guardian/DCD/Submarine Networks 关于 Google Christmas Island AI data centre/data hub 的报道——可触发 Shire minutes、planning、EPBC、AusTender、电力与 Google 官方检索）；C 级/负面（数据中心目录、VPS/offshore hosting 营销、社交转述、未给地址/运营商的「Christmas Island data center」页面）。
- 结论写法：`no confirmed commercial datacenter; confirmed telecom/cable infrastructure; monitor Google data-centre lead`。
- 枚举矩阵：Vocus ASC CLS（operational，A/B，计 telecom/cable landing infrastructure）；CiFi（operational，A，计 network operator lead 不计 colo）；Telstra 4G/4GX（operational，A/B，计 mobile telecom infrastructure 不计 DC）；Google Bosun/interlink（planned/approval，A/B，计 planned cable/landing project）；Google Dhivaru（planned，A，计 planned subsea cable connectivity）；Google AI data centre/data hub（unconfirmed lead，B/C，不计 confirmed，需一手审批/公告）；政府/Shire server rooms（A lead，仅命名项目时计）；PRL/CIP 企业 IT/电力（B/C，不计 DC 除非命名 facility）；North West Point（A/B lead，只记合同层面）；商用 colo/云区域（A/C negative，verified-negative）。
- 诚实结论（2026-08）：无已确认商业数据中心；已确认电信/海缆基础设施；监控 Google data-centre lead。

## 维护注意（更新纪律）

- **更新节奏**：每季度——DITRDCA IOT bulletins/Service Delivery kit、Shire 会议记录/规划、Vocus ASC 状态、CiFi/Telstra/nbn 页面、ACMA、AusTender/budget/Home Affairs、Google Bosun/Dhivaru 与 EPBC referral 状态、官方云区域页、目录负面检查；事件驱动——任何 Google data-centre 一手公告（Google 官方 facility 页、Shire development approval、EPBC 非海缆 data-centre referral、AusTender/Defence 合同或电力接入文件）为最大变化信号。
- **来源核验**：逐一点击 A 级 URL；Google data-centre 报道被公司否认/淡化时保持 B/C lead；EPBC referral 只证明 cable works；Kiritimati 混淆与 .cx 域名滥用持续防护；媒体与官方材料分开引用。
- **不删除纪律（no-deletion）**：已核实记录不得删除；状态变化改标（planned → approval/referral → under construction → operational）并保留原始证据链；无支撑条目降级为 C/U 保留而非移除；负向检索（verified-negative / cloud-region absence）须如实记录而非跳过。
