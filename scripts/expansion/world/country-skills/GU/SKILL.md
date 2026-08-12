---
name: gu-datacenter-methodology
location: scripts/expansion/world/country-skills/GU/SKILL.md
description: 关岛数据中心双线查询方法论（官方/监管/云管线 + 行业/厂商/媒体发现），含 division 模型、19 villages 覆盖、A/B/C 来源分级与查询模板；English: dual-line datacenter discovery & audit methodology for Guam (official/regulatory/cloud pipeline + industry/vendor/media discovery), with division model, 19-village coverage, A/B/C source grading and query templates. 运行 GU 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# GU · 关岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：为关岛（Guam, GU，美国未建制领地）的数据中心探索与审计提供统一双线方法论。官方/监管线负责确认与定稿，行业/厂商线负责发现与预筛，两线对读后再创建、确认或拒绝设施记录。本文件由 codex 审核定稿的两份 explorer 合并而成，细节以 `explorer-official.md`（官方线）与 `explorer-industry.md`（行业线）为准。

## 入口

| 文件 | 职责 | 内容摘要 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线：验证与定稿 | 关岛政府与公共采购（guam.gov、BSP、DOA/GSA、notices、立法）、GEDA/GPA/PUC/CCU 能源公用事业、FCC 海缆许可/IBFS、运营商官方设施页（GTA/DOCOMO/IT&E/Guam Exchange）、联邦/国防（SAM.gov、NAVFAC、Andersen、Camp Blaz、DISA）、云区域与边缘、19 villages 覆盖、枚举规则与噪声过滤 |
| `explorer-industry.md` | 行业/厂商/媒体发现：线索与预筛 | GTA/GNC/Guam Exchange/DOCOMO/IT&E 运营商扫描、海缆与登陆站、国防与承包商、媒体（DCD、Submarine Networks、Pacific Island Times 等）与目录（DataCenterMap、Baxtel、Inflect 等）、枚举矩阵与去重规则 |

## 核心结构事实

1. **行政区划模型**：manifest 为单一 division — `["Guam"]`（subnational_type=country）。枚举先做全岛扫描，再按官方 19 个 villages 做地名扫描：Agana Heights、Agat/Hågat、Asan-Maina、Barrigada、Chalan Pago-Ordot、Dededo、Hagåtña/Hagatna/Agana、Inalåhan/Inarajan、Malesso'/Merizo、Mangilao、Mongmong-Toto-Maite、Piti、Sånta Rita-Sumai/Santa Rita、Sinajana、Talo'fo'fo/Talofofo、Tamuning/Tamuning-Tumon-Harmon/Tumon/Harmon、Humåtak/Umatac、Yigo、Yona；Tumon/Harmon/Upper Tumon 属 Tamuning 语境，不作独立 division 或独立 village 计数。
2. **三类设施分开**：商业托管/colocation（GTA、DOCOMO Pacific、IT&E、Guam Exchange/GNC 等有真实托管/机房或 cable landing station + data center 证据）；海缆登陆站（默认电信基础设施，只有来源明确写 data center/colocation/racks/第三方机柜/电力/冷却才升级为 DC/colo 候选；Piti、Tanguisson Point、Tumon Bay、Alupang/Agat 为关键登陆点）；国防/联邦通信设施（Andersen AFB、Joint Region Marianas、MCB Camp Blaz、NCTS/Guam Telecommunications Site、DISA Pacific 等，计数时单列 `defense/telecom`，不混入商业 colo）。
3. **注册库现状**：无独立国家数据中心登记处；A 级锚点为运营商官方页、FCC（cable landing license/IBFS/public notice）、SAM.gov、DoD/NAVFAC 官方公告、GPA/PUC、官方云区域页；政府采购（server room/DR/cloud migration/network operations/UPS/generator/HVAC/fiber）只有出现地点、运营方/承包方、阶段或采购号时才形成设施候选，泛泛的 cloud/IT modernization 不计数。
4. **法律与监管**：关岛属美国 FCC 管辖 — 海缆登陆许可、license modification、special temporary authority、foreign ownership/Team Telecom 条件以 FCC 和申请方官方材料为 A 级锚点；GPA 是关岛公用电力系统核心（Government of Guam public corporation，费率受 PUC 监管），大型 DC 线索查 GPA procurement/interconnection/substation/feeder/large load/generation adequacy 与 PUC docket；PUC/CCU 确认费率/供电/utility-level approval，电力规模记录原单位（MW/MVA/kW/kWh）不换算成 IT MW。
5. **设施/项目种子（2026-08 复核基线）**：**GTA** — 官方页描述 GU1/GU2 为 Tier 3-designed data centers and cable landing stations（约 11,800 sq ft、2 MW），GU3 规划 32,000+ sq ft、4 MW、Q3 2025 ready for equipment，另有 HMB IX、Alupang 数据中心破土（2022 新闻，约 31,000 sq ft）；**GNC iX / Gateway Network Connections** — Guam 首个 combined neutral Cable Landing Station and Data Center，位于 Piti（行业/转载页：约 11,800 sq ft、250 racks、2 MW、Type 3 designed，容量与完成日期按 B/C，设施存在可由 GTA 官方 GU1/GU2 页交叉确认）；**Guam Exchange** — 官方页提供 colocation 服务，地址 `122 West Harmon Industrial Park Rd Ste. 103, Tamuning, 96913, Guam`（A 级运营方页面；容量/面积若来自 Inflect/DC Byte/Baxtel 按 C 或 B/C；Pacific Island Times 称 Harmon 1 为 open-access, Tier III compliant，B）；**DOCOMO Pacific** — 官方 business 页提供 data center colocation，点名 Agana、Harmon、Piti 三个 secure off-site colocation facilities（99.99% SLA）；**IT&E** — 官方 data services 页写有 co-location and hosting services（A 级服务证据，单点物理设施待交叉核实）；**NAVFAC 2025 $289M communications center upgrades（Guam）** — 官方公告 A 级，是否计作 data center 看 solicitation/award 是否明确；**DCD 2025 报道 US Navy 拟在 Andersen AFB 建 data center** — B 级，必须回 SAM.gov/NAVFAC 原始 solicitation。
6. **语言与词汇**：英语为主；查岛名/村名用规范化的双拼写（Hagatna/Agana/Hagåtña、Agat/Hågat、Inarajan/Inalåhan、Merizo/Malesso'、Umatac/Humåtak、Santa Rita/Sånta Rita-Sumai、Talofofo/Talo'fo'fo）；噪声过滤 `-Guamá -Cuba -vessel -registry -"Guam ship" -"Guam airport" -flight -hotel -resort`（官方线亦有 `-Guamá -ship -registry`）。
7. **可靠性分级（A/B/C）**：A=官方/一手（Government of Guam、DOA/GSA、BSP、GPA、PUC、GEDA、Guam notices、FCC cable landing license/IBFS/public notice、SAM.gov、Defense.gov contracts、NAVFAC/CNIC/JRM/Andersen/Camp Blaz/DISA、运营商或设施运营方官方页、AWS/Azure/GCP/OCI 官方区域页）；B=强二级（Submarine Networks、TeleGeography Submarine Cable Map、DCD、Pacific Island Times、Pacific Daily News、Guam Daily Post、Marianas Business Journal、Guam Business Magazine、PNC、KUAM、具名供应商新闻稿转载）；C=弱线索（DataCenterMap、Cloudscene、Baxtel、Datacenters.com、Inflect、WHTop、PeeringDB、LinkedIn、招聘帖、社媒、主机目录）。分级作用于具体声明（如 NAVFAC 官方授标确认 communications center upgrades 是 A 级合同证据；媒体称其为 data center 时媒体声称本身只按 B）。
8. **计数与去重规则**：商业 colo 需运营方/官方页或一手材料写明 colocation/data center/hosting/racks/power/cooling/security；landing station 默认 `telecom/landing`，明确托管服务或 combined CLS+DC 才列 DC/colo 候选；军事设施归 `defense/telecom`，公开资料不足时用基地/项目名不猜机房坐标；政府 cloud、CDN edge、satellite terminal、零售宽带、基站、FTTH、office IT、大学实验室默认不计 DC；目录只作 C 级线索必须回运营方/FCC/SAM.gov/Defense.gov/NAVFAC 验证；无产出 village 保留负向搜索轨迹；去重 — 规范化村名、Harmon/Tumon/Upper Tumon/Alupang 为 subareas 地址确认后映射、不合并 GTA GU1/GU2/GU3/GNC/Guam Exchange 除非来源证明同一物理站点、海缆系统/登陆站/DC 记录关联但独立、容量字段保留原单位与来源等级（sq ft/racks/MW/kW/MVA 不可互换）、“ready for equipment”或“planned”不等于 operational。

## 常用查询模板

```text
# 关岛政府/采购
site:guam.gov "data center" OR "datacenter" OR "server room" OR "disaster recovery"
site:gsa.doa.guam.gov "data center" OR "server" OR "UPS" OR "generator"
site:notices.guam.gov "data center" OR "telecommunications"
site:guamlegislature.org "data center" OR "submarine cable" OR "broadband"
# 能源/公用事业
site:guampowerauthority.com "data center" OR "large load" OR "substation" OR "interconnection"
site:guampuc.com "data center" OR "large load" OR "rate case"
site:investguam.com "data center" OR "digital infrastructure" OR "submarine cable"
# 海缆许可/运营商
site:fcc.gov Guam "cable landing license" OR "IBFS"
site:submarinenetworks.com "Guam" "cable landing station"
site:gta.net "GU1" OR "GU2" OR "GU3" OR "data center" OR "cable landing station"
site:business.docomopacific.com "Data Center Colocation" OR Agana OR Harmon OR Piti
site:guamexchange.com "colocation" OR "data center" OR "Harmon"
site:shop.ite.net/business "co-location" OR "colocation" OR "hosting"
# 国防/联邦
site:sam.gov "Guam" "data center" OR "communications center"
site:navfac.navy.mil Guam "communications center" OR "data center"
site:andersen.af.mil "36th Communications Squadron"
site:datacenterdynamics.com Guam "data center" OR "Andersen"
# 云/边缘
site:cloud.google.com/blog Guam Proa OR Taihei OR Bulikula OR Halaihai
site:blog.cloudflare.com Guam "deployment"
# 全岛/村庄
"Guam" "data center" OR "colocation" OR "server hosting" -Guamá -ship -registry
"{village}" "Guam" "data center" OR "colocation" OR "server room"
"{village}" "Guam" "landing station" OR "central office" OR "exchange" OR "gateway"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **关岛政府/采购**：`guam.gov`、BSP（`bsp.guam.gov`）、DOA（`doa.guam.gov`）、GSA procurement（`gsa.doa.guam.gov`，含 Invitation for Bid）、`notices.guam.gov`、Guam Legislature（`guamlegislature.org`）、法院/法典入口；政府 ICT 项目只有出现地点/运营方/阶段/采购号才形成候选。
- **GEDA/GPA/PUC**：GEDA/Invest Guam（`investguam.com`）数据中心招商/激励/QOZ 材料通常是项目背景或政策线索；GPA（`guampowerauthority.com`）与 OpenGovGuam bids（`go.opengovguam.com/bids/available/gpa`）查大型负载/变电站/feeder；PUC（`guampuc.com`）、CCU（`guamccu.org`）、Guam Energy Office（`guamenergy.com`）确认费率与 utility 批准。
- **FCC 海缆许可**：`fcc.gov/international`、`docs.fcc.gov`、IBFS（`licensing.fcc.gov/myibfs`）为 A 级锚点；已核实关键登陆站/项目 — Tanguisson（CUCN/AAG/AJC/Guam-Philippines）、Tumon Bay（TPC-5/AJC/Pacrim West）、Tata Piti（TGN-Pacific/TGN-IA/PPC-1）、GTA Piti-I/GNC iX（SEA-US/JGA South/JGA North/HK-G/SxS）、ATISA（DOCOMO Pacific 官方确认 FCC 批准）、Google Proa/Taihei/Bulikula/Halaihai（海缆/连接性线索，不是 Google Cloud region）。
- **联邦/国防**：SAM.gov、Defense.gov Contracts、DISA、NAVFAC/NAVFAC Pacific、JRM/CNIC、Andersen AFB、MCB Camp Blaz、USACE Honolulu、Guam National Guard；NAVFAC 2025 $289M communications center upgrades 是 A 级；DCD Andersen AFB 报道是 B 级需回原始 solicitation。
- **云区域与边缘**：官方 region/location 列表无 Guam 时记 A 级负向证据（AWS/Azure/GCP/OCI 均无）；Cloudflare Guam deployment 是官方边缘节点证据（记 CDN/edge PoP 线索，不扩展为独立商业 DC）；Google 海缆只证明 connectivity/subsea landing。
- **高优先级地名**：Piti（GNC iX、Tata Piti、GPA/Cabras/Piti 电力）、Tamuning/Harmon/Tumon（Guam Exchange、Tanguisson/Tumon Bay 周边）、Hagåtña/Agana（政府 ICT、DOCOMO label）、Yigo/Andersen AFB（空军通信）、Dededo/Finegayan（Camp Blaz、NCTS）、Santa Rita/Agat（Naval Base Guam、新海缆登陆点）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商**：GTA（GU1/GU2/GU3/HMB IX 官方页 + Alupang 破土新闻）、GNC/RTI（GNC iX 为 combined CLS+DC，Piti，行业/转载 B/C 容量）、Guam Exchange（官方 colocation 页 + Harmon 地址 + PIT 报道 Tier III compliant B）、DOCOMO Pacific（Agana/Harmon/Piti 三处 colocation + carrier services + ATISA FCC 新闻）、IT&E（co-location and hosting 服务页；meet-me points/fiber/transport 不单独计 DC）、NetLabs（`netlabsguam.com` 不可靠，仅弱线索，不列入 A 级运营商清单）。
- **海缆/登陆站**：TeleGeography/Submarine Networks 用于系统名/登陆点/RFS/状态/运营方线索，FCC 或运营方材料用于 A 级确认；Piti 与 GNC/GTA 设施有 DC/colo 语言是 DC 候选重点；Tanguisson/Tumon Bay/Tata Piti 只有 landing station 语言默认 `telecom/landing`；Google Proa/Taihei/Bulikula/Halaihai 只作 future/active cable landing 与 connectivity 线索。
- **国防/承包商**：DCD 报道必须回 SAM.gov/NAVFAC 原始 tender；Camp Blaz/Finegayan/前 Naval Base Guam Telecommunications Site 需用 NAVFAC PA memo、SAM.gov、Defense.gov 分辨是普通营建、telecommunications 还是可计 data center。
- **媒体与目录**：媒体用于时间线/项目名/承包商/容量线索必须回填一手源；目录常把市场统一标为 Hagatna/Guam、地址和 village 可能错误，不要直接采用目录地名；PeeringDB 用于网络/ASN/IX 上下文，不作为设施存在证据。
- **诚实结论**：关岛存在真实商业托管、海缆登陆站+数据中心组合设施与国防通信/数据中心项目；核心不是“是否有 DC”而是避免把不同类型混在一起；AWS/Azure/GCP/OCI 无 Guam 云区域；Google 海缆与 Cloudflare edge 不等同云区域或可枚举 DC。

## 维护注意（更新纪律）

- **更新节奏**：事件驱动 + 定期 — GTA GU3/Alupang（`ready for equipment`/commissioned）、Guam Exchange 新设施、DOCOMO colocation 更新、IT&E 服务页、FCC Guam 海缆许可（Bulikula/Proa/Taihei/Halaihai）、SAM.gov/Defense.gov/NAVFAC 新合同、GPA/PUC 大型负载 docket、Google 海缆进度；无产出 village 保留负向搜索轨迹。
- **来源核验**：每设施候选必含规范名、别名、运营方/业主、村庄或可定位地址、设施类别、状态、证据 URL、证据等级；官方页/一手材料写 colocation/data center/hosting/racks/power/cooling/security 才计商业 colo；目录条目必须回运营方/FCC/SAM.gov/Defense.gov/NAVFAC 验证；“ready for equipment”或“planned”除非后续官方页确认运营否则不算 operational。
- **不删除纪律**：本目录只允许新增/更新文件，禁止删除或移动任何文件；不合并 GTA GU1/GU2/GU3/GNC/Guam Exchange 除非来源证明同一物理站点；不把 communications facility/gateway/central office/earth station/edge server 当 data center。
