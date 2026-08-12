---
name: gi-datacenter-methodology
location: scripts/expansion/world/country-skills/GI/SKILL.md
description: 直布罗陀数据中心双线查询方法论（官方/监管/云管线 + 行业/厂商/媒体发现），含 division 模型、A/B/C/U 来源分级与查询模板；English: dual-line datacenter discovery & audit methodology for Gibraltar (official/regulatory/cloud pipeline + industry/vendor/media discovery), with division model, A/B/C/U source grading and query templates. 运行 GI 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# GI · 直布罗陀数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：为直布罗陀（Gibraltar, GI，英国海外领地）的数据中心探索与审计提供统一双线方法论。官方/监管/电力/采购线负责验证与定稿，行业/厂商/媒体线负责发现与预筛，两线互为三角验证。本文件由 codex 审核定稿的两份 explorer 合并而成，细节以 `explorer-official.md`（官方线）与 `explorer-industry.md`（行业线）为准。

## 入口

| 文件 | 职责 | 内容摘要 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线：验证与定稿 | HMGoG 政府/公报/统计/采购（Tender Notices/Awards/Contracts）、GRA 监管、GFSC/博彩、GEA 电力、Gibtelecom/GibFibre 电信、官方云区域负向核查、分区模板与设施种子、误报过滤 |
| `explorer-industry.md` | 行业/厂商/媒体发现：线索与预筛 | 本地/行业媒体（Chronicle、GBC、DCD、Capacity、Computer Weekly 等）、运营商/托管扫描、聚合目录与互联目录、投资/云/托管核查、枚举矩阵与分级规则 |

## 核心结构事实

1. **行政区划模型**：manifest 为单一 division — `["Gibraltar"]`（subnational_type=country）。全域面积很小，设施定位在同一 division 内用片区补充：Mount Pleasant、Port/North Mole、Europa Point、City Centre、Waterport、Europort、Ocean Village、Bayside/Business Bay、North Front/Airport；不得创建市镇/省份/西班牙边境分区，西班牙 Campo de Gibraltar 只能作跨境连接性语境。
2. **注册库现状**：无独立国家数据中心登记处；清点组合运营商自述、监管（GRA 年报/许可）、采购、电力、规划（DPC）证据；GFSC 持牌实体/DLT/VASP 名册与博彩许可只证明需求池，不证明 Gibraltar 自有设施。
3. **法律与监管**：GRA（Gibraltar Regulatory Authority）管通信/数据保护（Gibraltar GDPR/DPA）/竞争/广播/邮政/高教/网络安全；GFSC 管金融服务、持牌实体与 DLT/VASP 名册；HMGoG Remote Gambling 管博彩许可；GEA 管电力（North Mole Power Station 约 80MW 装机、100+ 变电站）；规划走 Development and Planning Commission (DPC)。
4. **互联与云**：AWS/Azure/GCP/OCI 官方区域列表均无 Gibraltar（最近区域在西班牙/马德里：AWS eu-south-2、Azure Spain Central/Madrid、GCP europe-southwest1、OCI eu-madrid-1）；Gibtelecom/Continent 8/Pelagos 的本地托管或云产品是本地/行业托管、private/public cloud 或 planned campus，不得描述成 hyperscale cloud region。
5. **设施/项目种子（2026-08 复核基线）**：**Gibtelecom Data Centre / Mount Pleasant** — 运营中，Gibtelecom 官网 Data Centre Solutions + GRA 2019/2020 年报 + 2025 Privy Council 案件摘要（Gibtelecom owns and operates a data centre at Mount Pleasant），A/B；**Continent 8 Gibraltar Data Centre / inside the Rock（前 MoD Operations Centre/Admiralty Tunnel/COMCEN）** — 运营中，HMGoG 2024 部长访问 + Continent 8 官网 Gibraltar location，A；**Pelagos Data Centres / near the Port of Gibraltar** — 2025-09-04 HMGoG 公告 250MW、五期、20,000 m2、首期目标 2027 年底运营、独立于现有电网，当前标 **Announced/planned**（A 公告/计划），不计入现役容量；**政府 Data Centre Hosting Services 采购** — 2022 Tender Notice/Award 真实存在，中标方 Continent 8 Technologies Plc，A；**GibFibre 数据中心/co-location 声称** — 仅 C 线索，物理设施待独立确认；**Europa Point 海缆登陆** — 仅连接性资产，B。
6. **语言与词汇**：英语主检（data centre/colocation/server room/data hall/Tier III/racks/250MW），西班牙语补充（centro de datos、fibra transfronteriza、cable submarino）；歧义词 GDC 可能指 Gibraltar Data Centre 或 Gibraltar Development Corporation，必须先核实法人。
7. **可靠性分级（A/B/C/U）**：A=一级证据（政府/监管/公报/招标/授予页、公用事业、运营商自营设施页、官方云区域列表）；B=强二级（可信行业媒体、监管年报案例描述、PeeringDB/RIPE、供应商案例、具名公司新闻）；C=弱线索（聚合目录、市场平台、转售商声明、招商叙事、由公司地址或新闻措辞推断的机房）；U=未验证传闻或无来源说法，仅作检索提示。分级只适用于来源实际证明的事实（如 Gibtelecom 自营页证明其提供托管/机房服务是 A；目录中的容量/等级/客户数/重复条目在运营商或官方记录确认前仍为 C）。
8. **计数与去重规则**：生产清单只接受六要素齐全条目 — 具名运营商 + division=Gibraltar + 片区/位置 + 证据 URL + 状态 + 分级；未来项目必须保留 `planned/announced/construction/operating` 状态，不得与运营设施混计；电站/变电站（North Mole、BESS、substations）、电信基站、PoP、海缆登陆站不计为数据中心；聚合目录（Data Center Map “6 facilities”等）只做种子逐条回查；Algeciras/La Linea/Estepona/Malaga/Ceuta/Tangier 设施不是 Gibraltar。

## 常用查询模板

```text
# 政府/采购
site:gibraltar.gov.gi "data centre"
site:gibraltar.gov.gi "Data Centre Hosting Services"
site:gibraltar.gov.gi "Continent 8"
site:gibraltar.gov.gi "Pelagos Data Centres"
site:gibraltar.gov.gi "tender" "hosting"
# 监管
site:gra.gi "data centre"
site:gra.gi "Mount Pleasant" "Gibtelecom"
site:fsc.gi "DLT Providers"
site:gibraltar.gov.gi "remote gambling" "data centre"
# 电信/运营商
site:gibtele.com "Data Centre"
site:gibtele.com "Mount Pleasant"
site:gibfibre.com "data centre"
# 电力
site:gea.gi "data centre"
site:gibraltar.gov.gi "Pelagos" "grid"
site:gibraltar.gov.gi "North Mole Power Station" "Pelagos"
# 行业
"data centre" "Gibraltar"
"Gibtelecom" "Mount Pleasant" "data centre"
"Continent 8" "inside the Rock" "Gibraltar"
"Pelagos Data Centres" "Gibraltar"
site:datacenterdynamics.com Gibraltar "data center"
site:capacitymedia.com Gibraltar "Gibtelecom"
# 西语
"centro de datos" "Gibraltar"
"Gibraltar" "cable submarino" "Europa Point"
# 连接性
"Gibraltar" "Europa Point" "submarine cable"
"Gibraltar" "IXP"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **HMGoG 政府/公报/统计/采购**：`gibraltar.gov.gi` 的 Press Releases、Official Notices、Tender Notices、Tender Awards、Government Contracts statistics、Statistics Office、Gibraltar Gazette 均 A 级；Tender Notice=需求存在（A 采购需求，未授予前不得确认供应商/运营状态）；Tender Award=中标方与金额（A）；政府访问/新闻稿点名设施与运营商为 A，但营销性容量和未来时间表要保留状态字段。
- **GRA**：通信/数据保护/竞争监管；Communications Notices 查 Gibtelecom、GibFibreSpeed、Sapphire/u-mee 等授权/设施权；Annual Reports 里含数据中心接入纠纷（如 GibFibre 要求进入 Mount Pleasant 数据中心案）——A/B。
- **电力（GEA）**：`gea.gi` 供电资产与电网语境（North Mole 约 80MW）；电网很小，任何 1MW+ 新项目/电网接入/变电站/LNG/可再生能源自发电应在政府/GEA/DPC 或规划文件中留痕；电站/BESS/变电站不是数据中心。
- **电信与连接性**：Gibtelecom（incumbent，Data Centre Solutions、Hosting & Cloud、Private Cloud、PoP、Gibraltar/London/Dublin/Malta/Malaysia footprint）；GibFibre（本地 private full-fibre/FTTH ISP 与 authorised operator，勿按政府所有的批发光纤机构处理）；Submarine Cable Map（B）、PeeringDB（B/C）、RIPE（B）查 ASN/路由/组织。
- **官方云区域负向核查**：每次执行记录日期（本轮 2026-08-12）；AWS/Azure/GCP/OCI 官方区域表均无 Gibraltar。
- **片区锚点**：Mount Pleasant（Gibtelecom 重点片区）、inside the Rock/前 MoD Ops Centre（Continent 8）、Port/North Mole（Pelagos + 电力语境）、Europa Point（海缆/连接性）、Europort/City Centre/Westside/Ocean Village/Bayside（金融/博彩/专业服务内部机房线索区）、North Front/Airport（通信基础设施，产出低）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **本地/行业媒体**：Gibraltar Chronicle、GBC News、Your Gibraltar TV、Gibraltar Magazine（C/B）、Olive Press/SUR/Cadena SER Algeciras（西边境侧 C/B）、DCD、Capacity Media、Telecoms.com、Computer Weekly、PR Newswire（优先公司/HMGoG 原文）；Panorama 已停刊（2024-04-26），仅用可访问归档回查旧线索。
- **运营商/托管扫描**：Gibtelecom（A/B）、Continent 8（A：Gibraltar location + HMGoG 2024 访问 + 2022 中标 + DCD 合同报道）、Pelagos（A announced/planned，跟踪 DPC/规划/能源/施工/调试）、GibFibre（A 运营商角色 / C 设施直到确认）、u-mee/Broadband Gibraltar/Sapphire（C）、本地 MSP/hosting（C）、GFSC 持牌银行/DLT 企业（C/B，查本地托管/数据驻留披露）、博彩运营商（C/B）。
- **聚合/互联目录**：Data Center Map（Gibraltar “6 facilities” 是待拆分清单，非确认数量）、datacenters.com、PeeringDB（B/C）、RIPE（B）、IXPDB/Euro-IX（预期无公开 IXP）、Submarine Cable Map（B）、Internet Exchange Map（C）；地址（William's Way、Neil Pinero Road、inside the Rock 等）仅在运营商或官方来源支持时用于生产记录；聚合与官方冲突时以官方/运营商为准。
- **诚实结论**：2 个高可信现役锚点 + 1 个 A 级 planned campus + 若干 C 级本地 ISP/MSP/内部机房线索；需求（博彩/金融/DLT/政府托管/跨境低时延）存在不等于设施存在；本地 hosting/VPS 供应商可能部署在 Spain/UK/Isle of Man/Malta，必须查 ASN、IP 地理定位、条款、支持地址与设施运营商。

## 维护注意（更新纪律）

- **更新节奏**：事件驱动 — Pelagos 后续（DPC agendas/minutes、环评文件、土地转让/租赁、发电许可、施工采购、本地反对意见）、Gibtelecom/Continent 8 产品页与地址确认、政府 tender 发布/授予、GRA/法院文件；定期 — 每轮执行记录官方云区域核查日期、每半年复查超大规模区域页。
- **来源核验**：生产清单只接受六要素齐全条目；容量/Tier/机柜数/客户数未被运营商或官方记录确认前一律不升级；Pelagos 保持 announced/planned，出现 commissioning/customer launch/live data hall 或监管/公用事业验收证据前不计 operating；250MW 标注为规划目标并记录 `first phase targeted late 2027`、`independent of existing grid` 的未来性。
- **不删除纪律**：本目录只允许新增/更新文件，禁止删除或移动任何文件；GibFibre 数据中心声称保持 C 直到找到物理设施、运营商页或合同；不把 London/Dublin/Malta/Malaysia/Isle of Man/Spain 托管节点归入 Gibraltar。
