---
name: mp-datacenter-methodology
location: scripts/expansion/world/country-skills/MP/SKILL.md
description: 北马里亚纳群岛（CNMI）数据中心双线查询方法论（官方/监管/云管线 + 行业/厂商/媒体发现），telecom-first、data-center-light，含 division 模型、来源分级与查询模板；CNMI datacenter dual-line discovery methodology (official/regulatory/cloud pipeline + industry/vendor/media discovery), telecom-first and data-center-light, with division model, source grading and query templates. 运行 MP 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# MP · 北马里亚纳群岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为北马里亚纳群岛联邦（Commonwealth of the Northern Mariana Islands, CNMI/MP）数据中心盘点批次提供官方与行业双线方法。官方线（explorer-official.md）覆盖 CNMI 政府与立法/审计/宽带机构、CUC 公用事业、FCC/USAC、美国联邦采购与拨款、海缆登陆许可与云厂商官方区域页；行业线（explorer-industry.md）覆盖运营商产品页、海缆/电信行业媒体、数据中心目录、建设商/供应商线索与云/CDN 官方缺位核验。行业线索必须回连到官方/一手证据后才能建档；结论按设施主张分级，不按网站整体分级。

## 入口

| 文件 | 职责 | 内容概要 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | CNMI 政府（governor.cnmi.gov、cnmileg.net、opacnmi.com、commerce.gov.mp、bpd.cnmi.gov、marianas.edu）、FCC/USAC（ULS/ASR、海缆登陆、Form 477/BDC、Form 499）、CUC 电力（CUC-RFP-25-021 Solar PV+BESS IPP）、联邦采购与拨款（SAM.gov、FPDS、USASpending、Grants.gov、DOI OIA、FEMA、NTIA、GAO）、海缆登陆许可（FCC DA-97-522 MICS、DA-22-762 Atisa、Proa/TPU）、云/CDN 官方缺位核验 |
| explorer-industry.md | 行业/厂商/媒体发现 | DoCoMo Pacific（Data Center Colocation 产品页）、IT&E/Micronesian Telecommunications Corp.（BEAD 受约方）、PTI Pacifica/MICS、海缆厂商/未来连接（NEC ATISA、Google Proa/TPU/Interlink）、卫星/无线接入排除、云/CDN 缺位、贸易媒体与目录（Baxtel、Datacenters.com、DataCenterMap、Cloudscene、ColoMap、WHTop、PeeringDB）、枚举矩阵与分区工作流 |

## 核心结构事实

1. **Division 模型**：manifest 已核验 `country_code:"MP"`、`country_name:"Northern Mariana Islands"`、`subnational_type:"country"`、`divisions:["Northern Mariana Islands"]`。最终输出必须只使用该 division；Saipan 塞班、Tinian 天宁、Rota 罗塔仅作 municipality/island-level 搜索桶用于归位和覆盖检查，不得写成 manifest divisions。
2. **结论速览（2026-08-12）**：CNMI 没有官方证据显示存在 hyperscale cloud region、commercial carrier-neutral colocation campus 或独立的大型数据中心市场；可确认的骨架是电信基础设施、海缆登陆与政府宽带项目。行业图景是 telecom-first, data-center-light。
3. **已确认电信基础设施（Grade A/B）**：FCC 1997 海缆登陆许可确认 Mariana-Guam Cable/MICS 在 Saipan、Tinian、Rota 与 Guam 有登陆点；FCC 2022 public notice 确认 Atisa 覆盖 Saipan、Tinian、Rota、Guam，并说明 MICS/Atisa 均为 interisland traffic 的竞争路由；DoCoMo Pacific 官方稿称 FCC 已批准 Atisa landing license（连接 Guam、Saipan、Rota、Tinian，并在 Rota/Tinian 建设 cable landing stations）；NEC 官方稿确认 ATISA 完成并把 CNMI 连接到 Guam。
4. **已确认宽带项目（Grade A）**：CNMI Broadband Policy and Development Office（BPD）发布 BEAD 文档，页面显示 2026-05-13 与 Micronesian Telecommunications Corp. dba IT&E 签署 BEAD Subgrant Agreement；BEAD 是宽带/last-mile 与 middle-mile 线索，不自动构成数据中心证据。
5. **电力约束（Grade A）**：CUC 2025 RFP `CUC-RFP-25-021` 为 Saipan、Tinian、Rota 全岛 Solar PV + BESS IPP 采购，附各岛 power plant/transmission-distribution maps；CUC 记录是任何数据中心级负载的必要语境——Saipan/Tinian/Rota 的电信/DC 候选应对照 CUC 电厂、馈线、备用发电与 BESS/IPP 材料；CUC RFP 本身不建立数据中心。
6. **云区域缺位（Grade A）**：AWS、Azure、Google Cloud、Oracle OCI 官方区域/位置页未列 CNMI/Saipan/Tinian/Rota 为 cloud region 或 local zone；Google Pacific Connect/Proa 是海缆项目，不是 Google Cloud region；Oracle hospitality/service-region 样式页面把 Northern Mariana Islands 映射到既有外国区域做应用托管，不是 OCI 在 MP 的区域证据。
7. **设施/项目种子（2026-08 证据状态）**：DoCoMo Pacific 有真实官方 `Data Center Colocation` 产品页（Grade A 产品证据，含 24/7 staffing、fencing、mantrap、cameras、keycard scanners 等安全语言），但页面未给出 CNMI 设施地址，不能仅凭产品页把 "DoCoMo Saipan data center" 升级为已验证设施；IT&E 是 BEAD 官方受约方且目录声称 Saipan data center/colo 存在，但无足够一手地址/设施页，按 C 级线索处理；PTI Pacifica/MICS 是已确认海缆/电信设施主体（跨 Saipan/Tinian/Rota/Guam），证明电信基础设施不证明商业数据中心；Atisa/MICS/Google Proa-TPU-Interlink 是 CNMI 最重要的 digital infrastructure leads，作为 cable landing/telecom gateway 处理，除非后续有 rack/power/colo/hosting 证据。
8. **可靠性分级**：A = 官方/一手（governor.cnmi.gov、cnmileg.net/cnmileg.gov.mp、opacnmi.com、commerce.gov.mp、bpd.cnmi.gov、cucgov.org、FCC/USAC 官方系统、SAM.gov、FPDS、USASpending、Grants.gov、DOI OIA、FEMA、NTIA、运营商官方页面/PDF、云厂商官方基础设施页）；B = 强二手（Marianas Variety、Saipan Tribune、Guam Daily Post、Pacific Daily News、KUAM、Pacific Island Times、RNZ Pacific、Submarine Networks、TeleGeography、Data Center Dynamics、Capacity Media——要求有日期、具名主体、可交叉核验）；C = 弱/聚合（DataCenterMap、Cloudscene、Baxtel、Datacenters.com、ColoMap、WHTop、PeeringDB/BGP 目录、LinkedIn、Facebook/Instagram、招聘启事、论坛、转售商/主机目录）。分级针对具体 claim：FCC/USAC 能证明运营商、无线牌照、海缆或 USF 身份；不能单独证明该运营商在 CNMI 运营数据中心；目录站列出 Saipan data center 只能作 C 级线索，必须追到运营商官方页、FCC/ICFS 文件、合同/RFP 或本地许可。
9. **计数与去重规则**：每个 physical facility 至少需要一条 A 级主证，或一条运营商官方产品页加一个独立位置证据，目录站单条不能建档；cable landing station、central office、gateway、FTTP headend、earth station 默认分类为 `operational_telecom`，除非来源明确给出 third-party colocation/hosting/data center/racks/power/cooling；降级规则——`communications facility`、`gateway`、`central office`、`landing station`、`server room`、`IT room`、`fiber internet`、`5G`、`business support office` 都不是数据中心语言，只有 `colocation`、`hosting`、`data center/datacenter`、`racks/cabinets`、`power/cooling/security for customer equipment` 等可触发数据中心候选；不计入：Starlink/Viasat/Kacific 终端、移动基站、FTTP 覆盖、普通 ISP POP、政府办公室 IT、赌场/酒店/写字楼 server room，除非来源明确给出面向第三方的 colocation/hosting/data center/racks/power/cooling；关岛（Guam/GU）与 CNMI 运营商和海缆高度重叠，Guam data centers/landing stations/IXPs 只能作 upstream context，不计入 MP；卫星/无线接入（Starlink、Viasat、Kacific、固定无线、移动宽带、BRS/PCS/LTE/5G 塔、微波）只是连接基础设施，不计数据中心。

## 常用查询模板

```text
site:governor.cnmi.gov "data center" OR "server room" OR "cloud" OR "disaster recovery"
site:cnmileg.net OR site:cnmileg.gov.mp "data center" OR "broadband" OR "telecom" OR "CUC"
site:opacnmi.com "data center" OR "server" OR "information systems" OR "CUC"
site:bpd.cnmi.gov "data center" OR "middle mile" OR "BEAD" OR "IT&E"
site:commerce.gov.mp "broadband" OR "telecom" OR "data center"
site:fcc.gov "Northern Mariana Islands" "cable landing"
site:fcc.gov "Saipan" "Tinian" "Rota" "Guam" "submarine cable"
site:fcc.gov "Atisa" OR "MICS" OR "Mariana-Guam Cable"
site:fcc.gov "Proa" "Northern Mariana Islands" "submarine cable"
site:apps.fcc.gov/cgb/form499 "IT&E" OR "DOCOMO PACIFIC" OR "PTI Pacifica"
site:cucgov.org "data center" OR "critical load" OR "backup power" OR "generator"
site:sam.gov "Northern Mariana Islands" "data center" OR hosting OR colocation
site:fpds.gov "Saipan" "518210" OR "541513" OR "data center"
site:usaspending.gov "Northern Mariana Islands" "broadband" OR "data center" OR "IT&E"
site:grants.gov CNMI BEAD OR broadband OR NTIA
site:docomopacific.com "Saipan" "colocation" OR "data center"
site:business.docomopacific.com "Saipan" "data center" OR colocation OR cabinets OR racks
site:ite.net OR site:shop.ite.net "data center" OR colocation OR hosting OR cloud
site:bpd.cnmi.gov "IT&E" "Subgrant Agreement"
"PTI Pacifica" CNMI OR Saipan OR Tinian OR Rota "data center" OR colocation
site:nec.com ATISA CNMI Guam "completed"
site:cloud.google.com/blog "Proa" "CNMI" "TPU" "Interlink"
site:governor.cnmi.gov "Google" "Proa" OR "Pacific Connect"
"Northern Mariana Islands" "data center" OR datacenter OR colocation -casino -hotel
"Saipan" "data center" OR colocation OR "server hosting" -casino -hotel
site:mvariety.com "data center" OR "colocation" OR "server room" OR "broadband"
site:saipantribune.com "data center" OR "colocation" OR "IT&E" OR "DOCOMO"
site:kuam.com CNMI "data center" OR "submarine cable" OR "Google"
"{Municipality}" "Northern Mariana Islands" "data center" OR datacenter OR colocation -casino -hotel
"Saipan" "data center" OR colocation OR "first data center" -casino
"DoCoMo Saipan" "data center" OR colocation -Baxtel -Datacenters.com
"IT&E Saipan" "data center" OR colocation
```

## 官方/监管管线要点（详见 explorer-official.md）

- **CNMI 政府与公共机构**：governor.cnmi.gov（政府目录）、cnmileg.net/cnmileg.gov.mp（立法会）、opacnmi.com（公共审计官 OPA 报告/财务审计）、commerce.gov.mp（商务部）、bpd.cnmi.gov（宽带政策与开发办公室，BEAD 文档）、marianas.edu（北马里亚纳学院，机构 IT/采购线索）；政府来源可用于发现 government data center/disaster recovery/server room/hosting RFP，但只有出现专用设施语言时才建档；普通 IT system、software、website、helpdesk、network equipment purchase 不能升级为数据中心。
- **FCC/USAC 电信监管通道**：CNMI 属美国 telecom/FCC 体系；FCC ULS/ASR 证明无线、微波、地球站、tower/antenna 设施位置；FCC/ICFS 海缆（MICS、Atisa、未来 Proa/TPU/Interlink 等）的 landing authorization 与 landing points；Broadband Data Collection/Form 477 是 ISP 与覆盖枚举入口（不是数据中心证据，2022 后宽带部署数据迁移出 Form 477）；Form 499/USAC 是 USF 申报人与服务商法人名录（不是设施证据）；不要复述未经核实的“FCC 自 2009 年才取得 CNMI 电信管辖权”——2009 是 CNMI immigration/border federalization 节点，不是本方法论的 DC 监管锚点。
- **CUC 电力与公用事业**：cucgov.org 与 procurement/RFP 文档（cucgov.org/cuc_content/uploads/ 下）用于电力可行性；`CUC-RFP-25-021`（Saipan/Tinian/Rota 全岛 Solar PV + BESS IPP，2025-08）附各岛电厂/输配电图；U.S. DOE CNMI energy profile（energy.gov/oe/...）为老化基础设施/石油依赖语境。
- **联邦采购与拨款**：SAM.gov、FPDS、USASpending、Grants.gov、DOI OIA、FEMA、NTIA BroadbandUSA、GAO bid protests；用 place of performance 过滤（MP/CNMI/Saipan/Tinian/Rota）+ NAICS 过滤：518210（Computing Infrastructure Providers, Data Processing, Web Hosting）、541513（Computer Facilities Management）、541519、517111（Wired Telecom Carriers）、237130（Power and Communication Line Construction）、221122（Electric Power Distribution）。
- **海缆登陆**：FCC DA-97-522 授予 GST Telecom 权限建设 Mariana-Guam Cable/MICS（Guam 与 Saipan、Tinian、Rota 登陆点）；FCC DA-22-762 说明 Atisa 与 MICS 服务同一批岛屿；DoCoMo Pacific 2017 官方稿（FCC 批准 Atisa landing license，Rota/Tinian 新建 landing stations）；NEC 2017 官方稿（ATISA 完成并连接 CNMI 到 Guam）；Google Cloud 2024 官方博客（Proa 连接 Japan、CNMI 与 Guam，TPU 延伸至 CNMI——规划/宣布中的海缆连接，不是云区域或数据中心）。
- **云与 CDN 官方缺位核验**：AWS/Azure/GCP/OCI/Cloudflare/Akamai 官方网络页每次做时效性结论前重查；若页面只把 Northern Mariana Islands 映射到某服务区域（如 billing/service availability geography），不能写成 CNMI data center/region。
- **分区覆盖/市政桶**：单一 manifest division `Northern Mariana Islands`，三个市政桶（Saipan/Tinian/Rota）各自官方优先路径——Saipan（FCC/ICFS cable + ULS/ASR、BPD/BEAD、Governor/Legislature/OPA、CUC Saipan 电力图、SAM/FPDS place-of-performance Saipan：可记录 Atisa/MICS/未来 Proa landing、运营商 office/POP、政府/机构机房线索，只有有主证时建 government_related_dc 或 commercial_colocation）；Tinian（FCC cable + ULS、CUC Tinian、SAM/FPDS：已有 cable landing/service 线索，默认无商业 DC，军事/机场基建只作背景避免细节化）；Rota（同 Tinian，默认无商业 DC）。覆盖完整 = 三个市政桶都有检索痕迹，但最终记录仍在单一 manifest division 下。
- **枚举规则**：①先跑 FCC/ICFS + BDC/Form 477 + USAC 499 建运营商和海缆骨架，再跑 BPD/BEAD、CUC、SAM/FPDS/USASpending 建政府/电力项目骨架 ②每个 physical facility 至少一条 A 级主证或运营商官方产品页加一个独立位置证据 ③cable landing station/central office/gateway/FTTP headend/earth station 默认 operational_telecom ④DoCoMo Pacific 官方 colocation 产品页是真实 A 级产品证据但当前无 CNMI 地址 ⑤Google Pacific Connect/Proa/TPU/Interlink 是 subsea cable lead，不得作 Google Cloud region/edge PoP/DC 证据 ⑥Saipan/Tinian/Rota 未找到主证的候选输出 no_projects: true 或 telecom_only: true，保留查询、日期、source tier ⑦Guam 只作 upstream context。
- **噪声过滤**：排除 -casino -gambling -"Imperial Pacific" -"Tinian Dynasty" -hotel -resort -tourism -cruise；-Guam（仅排除非 CNMI 设施时使用，海缆上游查询可保留 Guam）；-"Marianas Trench" -"Mariana Islands"（海洋/地理泛称）-NMI（歧义缩写）；优先锚词：`"Northern Mariana Islands"`、`CNMI`、`Saipan MP 96950`、`Tinian MP`、`Rota MP`、`Commonwealth of the Northern Mariana Islands`。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **行业结论**：CNMI 可验证行业图景是 telecom-first, data-center-light。
- **DoCoMo Pacific**：Data Center Colocation 产品页（business.docomopacific.com/data-center-colocation）为 Grade A 产品证据（公司提供 colocation，含 24/7 staffing、fencing、mantrap、cameras、keycard scanners 安全语言）；该页不证明 CNMI 设施位置；support 页列 Guam 与 Saipan 商务服务地点，但 office/contact 地点不是数据中心；任何 `DoCoMo Saipan` 目录条目按 Grade C 处理，直到匹配到 DoCoMo 官方地址、FCC/ICFS 文件、本地许可、合同或可信的带日期媒体报告。
- **IT&E / Micronesian Telecommunications Corp.**：BPD 在 BEAD 文件中具名（2026-05-13 Subgrant Agreement），且目录声称 Saipan data-center/colo 存在，是高优先级线索；不得把 IT&E Saipan 分类为 commercial_colocation，除非 IT&E 官方页、合同、许可或强本地报道确认设施地址与 colocation/hosting/rack 服务；BEAD 光纤部署可能产生 central offices、splice huts、cabinets、network rooms，除非明确客户 colocation 或数据中心用途，否则仍是 telecom/FTTP 资产；线索含 Tekken Street/Susupe 地址（排除目录站核实）。
- **PTI Pacifica / MICS**：FCC DA-22-762（MICS 监管分类）与 DA-97-522（Mariana-Guam Cable 登陆许可）确认 PTI/MICS 是跨 Saipan/Tinian/Rota/Guam 的海缆/电信基础设施线索；Guam 侧 PTI/affiliate 数据中心或登陆站只作 upstream context，不计入 MP；企业/政府/私人运营商经 MICS 的服务按电信服务处理，除非具名设施含 DC/colo 语言。
- **海缆厂商/未来连接**：Atisa/MICS 是运营中的电信海缆系统；Proa/TPU/Interlink 是规划中或进行中的国际海缆线索，最终设施状态前须在 FCC/ICFS 复查；cable landing 不等于 data center，分类为 operational_telecom 或 planned_telecom，除非来源明确描述登陆站的客户 colocation/hosting。
- **卫星/无线接入**：Starlink、Viasat、Kacific、固定无线、移动宽带、BRS/PCS/LTE/5G 塔、微波站点只是连接基础设施；用 FCC ULS/ASR 与提供商可用性页理解覆盖，不计数据中心。
- **云/CDN 缺位**：每次提取前重查 AWS/Azure/GCP/OCI/Cloudflare/Akamai 官方页；当前结论：无 CNMI official cloud region/local zone/edge PoP。
- **贸易媒体与目录**：B 级——Marianas Variety、Saipan Tribune、Pacific Daily News、Guam Daily Post、KUAM、Pacific Island Times、RNZ Pacific、Submarine Networks、TeleGeography、DCD、Capacity Media；C 级线索——Baxtel（列 DoCoMo Saipan 与 IT&E Saipan）、Datacenters.com、DataCenterMap、Cloudscene、ColoMap、WHTop、PeeringDB、ARIN；目录若给出街道地址、电力、机柜、面积或运营商，须先对运营商官方页、FCC 文件、建筑许可、采购记录或直接本地媒体验证；目录缺席只是弱负面信号。
- **枚举矩阵**：commercial colocation（运营商官方页 → 本地许可/合同/媒体 → 目录；设施地址 + colocation/rack/power/cooling/customer equipment 语言；A/B 印证后才 commercial_colocation）；operator data center product（产品语言只证明产品不证明 CNMI 设施，planned_telecom_colocation 或线索直到地址证实）；cable landing station（FCC/ICFS + 运营商发布 + Saipan/Tinian/Rota 登陆点与运营商/持牌人 → operational_telecom 或 planned_telecom）；central office/POP（operational_telecom，不是 DC）；government/institutional DC（BPD/gov/RFP/OPA/SAM/FPDS 中明确 data center/server room/DR/hosting + 位置 → government_related_dc）；cloud region/CDN PoP（官方网络页具名 CNMI → 目前缺位）；satellite gateway（operational_telecom，不是 DC）。
- **分区工作流**：Saipan（最高可能性：运营商 office/POP、cable landing/gateway、可能的目录 colo 线索；升级只需 A/B 位置证据）；Tinian（海缆/电信接入、可能 landing station、DC 概率很低；默认 telecom_only/no_projects）；Rota（同 Tinian）。
- **监视清单（最终提取前重跑）**："Saipan" data center/colocation/"first data center" -casino；"DoCoMo Saipan"；"IT&E Saipan"；site:business.docomopacific.com Saipan colocation；site:ite.net Saipan；site:bpd.cnmi.gov IT&E subgrant middle mile；site:fcc.gov Proa CNMI cable landing；site:governor.cnmi.gov Google cable landing Saipan。未来来源若具名设施，入库前要求：operator、确切岛屿/市政、facility type、operational/planned 状态、至少一条 A/B 印证来源。

## 维护注意（更新纪律）

- **更新节奏**：每次做时效性结论前重查云/CDN 官方页；每次最终提取前重跑监视清单；Proa/TPU/Interlink 最终设施状态前在 FCC/ICFS 复查。
- **来源核验**：每个 physical facility 至少一条 A 级主证或运营商官方产品页 + 独立位置证据；目录独有条目保持 C 直到一手印证；B 级媒体要求有日期、具名主体、可交叉核验；未来设施入库要求 operator、确切岛/市政、facility type、状态与 A/B 印证。
- **不删除纪律**：本目录只新增/更新 SKILL.md、ANATOMY.md 与探索产物，禁止删除/移动任何现有文件（explorer-official.md、explorer-industry.md 与历史证据保留为原始记录）。
