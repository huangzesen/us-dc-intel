---
name: mh-datacenter-methodology
location: scripts/expansion/world/country-skills/MH/SKILL.md
description: |
  Marshall Islands (MH/RMI) datacenter discovery & audit methodology — how to enumerate, verify, and update Marshall Islands datacenter-class facilities at 24-municipality (atoll/single-island) granularity. RMI has no commercial colocation market and no planning-permit registry: enumeration pivots on NTA (National Telecommunications Authority — Majuro/Ebeye facilities, ICANN L-root colocation evidence, HANTRU-1 landing stations), Nitijela legislation (Telecom Reform Act 2025), World Bank Digital Republic project (P171517) and Digital Government Office, US government partners (USTDA Pacific Connect / State Dept / US Army Kwajalein-Reagan Test Site — context only), cloud-region absence checks (no AWS/Azure/GCP/OCI region), and industry/trade press (DCD, Submarine Networks, Marshall Islands Journal). Read this before running MH exploration/audit batches. Routes to explorer-official.md (NTA/Nitijela/World Bank/USG/cable/cloud pipeline) and explorer-industry.md (vendor/trade-press/directory discovery).
---

# MH · 马绍尔群岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：马绍尔群岛（RMI）**没有**商业主机托管市场、没有数据中心牌照类别、没有规划许可数据库——不能按美欧方式直接枚举。
> 现实的设施宇宙只有五类：① NTA 电信/海缆登陆设施（Majuro + Ebeye）；② 政府与捐赠方 ICT（Digital Republic 项目）；③ 银行/金融服务器机房；④ 美军 Kwajalein（Reagan Test Site）受限军事 IT（公开不可枚举）；⑤ 未来海缆登陆站（IOKWE/Pacific Connect/CPC，规划中）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供马绍尔群岛探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：NTA（nta.mh、ICANN L-root、HANTRU-1 登陆站）、Nitijela 立法（Telecom Reform Act 2025/PL 2025-28）、MOTC&IT 与 Digital Government Office、World Bank P171517、USTDA/State Dept/Army Kwajalein、EPA/MIEC/KAJUR 能源、云区域官方页（缺席确认）、24 市镇矩阵、分级规则 |
| `explorer-industry.md` | 行业/厂商发现：NTA 运营者视角、卫星厂商（Starlink/Intelsat/SES/OneWeb，仅连接性）、Google Halaihai/IOKWE 海缆、CDN/超大规模缺席核验、本地 IT/银行机房（C 级）、Kwajalein 军事-工业 IT（上下文）、贸易媒体与目录、分市镇模板 |

## 核心结构事实（框定每次搜索）

1. **微州国**：29 环礁 + 5 单岛，本仓库用 24 市镇（municipality）层；ICT 集中在 Majuro（首都，Delap-Uliga-Djarrit/Laura 走廊）与 Ebeye（Kwajalein 环礁），其余为低人口外环礁。
2. **NTA 是枢纽实体**（A 级）：国有控股电信，Majuro 地址 `NTA, 1169, Main Street, Delap`、Ebeye 地址 `NTA, 5025 Main Street`；**ICANN 2017 公告确认 L-root 节点安装在 Majuro 且 NTA 在其数据中心提供托管（colocation）**——这是全国唯一高置信的在运数据中心级设施；Ebeye/Kwajalein 只算已确认电信/登陆站。
3. **海缆事实锚定每个分区搜索**：HANTRU-1（2010 在运）连接 Kwajalein（Reagan Test Site）至 Guam，含 Majuro/Ebeye 登陆（FCC DA-09-1309A1 为所有权/容量/登陆站条款 A 级源；TeleGeography 为地图登录清单）；未来 IOKWE 支线（NTA 拥有/运营，接入 Google Halaihai/Pacific Connect，Majuro + Ebeye 登陆，约 2029 RFS，B 级）与 Central Pacific Cable（USTDA 可行性，A 级范围）。
4. **监管制度**（A 级立法锚）：National Telecommunications Act 1990 创设 NTA；Bill 66 移除独家条款；Telecommunications (Reform) Act 2025（PL 2025-28，2025-04-21 生效）开放市场；配套 Electronic Transactions / Digital Transformation & Identity Verification / Cybersecurity Act 2025。无 DC 牌照类、无规划许可库——不要搜索全国性 DC 注册表。
5. **政府数字议程**：Digital Republic of the Marshall Islands Project（World Bank，3000 万美元赠款，2021 启动，项目 P171517）资助连接、数字政府、网络安全、数字 ID；Digital Government Office 隶属 Chief Secretary，政府服务器基础设施集中在 Majuro Capitol/Uliga-Delap 区域；World Bank 项目文件是政府机房计划的最佳 A 级源。
6. **云/超大规模缺席**：AWS/Azure/GCP/OCI 均无 MH 区域或本地分区（官方区域页确认）；Starlink/VPS 转售商 ≠ 云区域；Majuro 的 CloudFront 边缘 PoP 声称未经验证（C 级）。Google 在 MH 的足迹是海缆（IOKWE），不是计算设施。
7. **能源硬约束**：柴油孤岛电网（MIEC 供电 Majuro，KAJUR 供电 Kwajalein/Ebeye），无互联电网；任何暗示兆瓦级数据中心的声称都必须强烈怀疑（C 级直到出现电力证据）。
8. **语言**：英语优先即可；加 `site:gov.mh` / `site:rmigov.com` / `site:nta.mh` 范围限定。
9. **噪音规避**：马绍尔船旗注册（全球第二大船籍）会污染检索——加 `-registry` 或用 Majuro/Ebeye/NTA/cable 限定；reseller 营销页（如 atalnetworks.com Majuro）不是设施证据。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§3 / explorer-industry.md §1-§2）

- NTA：`site:nta.mh "data center" OR "server" OR "hosting" OR "colocation"`、`site:nta.mh "Contact Us" "5025 Main Street" "Ebeye"`、`site:nta.mh "cable" OR "landing" OR "HANTRU" OR "fiber"`、`site:facebook.com/mhnta "Ebeye" OR "Majuro" OR "outage" OR "upgrade"`、`"NTA" "L-root" "Majuro"`、`site:icann.org "Marshall Islands" "root server"`。
- 立法/政府：`site:rmiparliament.org telecommunications`、`site:worldbank.org Marshall Islands digital government P171517`、`site:documents.worldbank.org "Digital Republic" Marshall Islands`、`"Digital Government Office" Marshall Islands Chief Secretary`、`site:gov.mh OR site:rmigov.com MOTC OR "Transportation, Communications" ICT`。
- 海缆：`"IOKWE" OR "Halaihai" OR "Central Pacific Cable" Marshall Islands`、`site:submarinenetworks.com IOKWE`、`site:datacenterdynamics.com "Marshall Islands"`、`site:ustda.gov Marshall Islands Pacific Connect`。
- 通用分区：`"{Division}" "Marshall Islands" ("data center" OR "datacenter" OR "server room" OR "server" OR "telecom" OR "cable landing" OR "earth station")`、`"{Division}" atoll NTA (fiber OR satellite OR microwave OR tower)`、`site:nta.mh "{Division}"`。
- 行业/规避：`"Marshall Islands" ("data center" OR datacenter OR colocation OR "server hosting") -registry`、`"Kwajalein" ("data center" OR "network operations" OR "IT services") Army contract`、`site:datacentermap.com Marshall Islands OR Majuro`、`"Starlink" "Marshall Islands" availability`。

## 官方/监管管线要点（详见 explorer-official.md）

- **NTA（A）**：nta.mh 联系页为 Majuro/Ebeye 地址 A 级源；ICANN L-root 公告是全国唯一的直接“数据中心托管”陈述；NTA Facebook 是故障/升级/CTE 状态证据（2021-2023 HANTRU-1 升级）。提取：地址、传输/DDF 机房、地球站、CTE 升级、服务环礁（卫星馈电机房）。
- **Nitijela 立法（A）**：Telecom Reform Act 2025 告诉你牌照类（无 DC 类）与监管机构（现称 Office of the Telecommunications Regulator，B 级）；2025 公共法索引确认配套数字法。
- **World Bank P171517（A）**：项目文件确认 2025 电信改革、Starlink 2025-06-10 本地开通、2023 年底美国政府 4000 万美元 Majuro/Ebeye 全屋光纤承诺；提取政府数据中心/主机托管组件、数字政府平台、网络安全、数字 ID、数据保护立法计划。
- **美方伙伴（A/B）**：USTDA Pacific Connect 可行性（A）；State Dept 2026-02 檀香山投资峰会 1.32 亿美元承诺页当前为 technical-difficulties 壳（保留 B 级）；US Army Kwajalein/Reagan Test Site 为上下文（B/C），不枚举受限军用机房；FCC DA-09-1309A1 为 HANTRU-1 登陆站条款（A）。
- **能源/环境（薄但可查）**：EPA 柴油机组许可（实际无公开 DC 发电机许可）、MIEC/KAJUR 无 DC 级连接公开记录。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **NTA 是唯一真正的设施拥有者/运营者**：无公开 colo 产品页——任何 NTA 托管都按内部/电信处理，除非出现主源服务页；CEO Dr. Yukiko Muller 是公告检索锚点。
- **卫星厂商 = 连接性，不是 DC**：Starlink（2025-06-10 本地开通，World Bank 文档确认）、Intelsat（60 个外岛小基站 + 卫星枢纽，命名网络类型供证据识别）、SES O3b mPOWER / OneWeb（无确认终端）；不记容量。
- **Google Halaihai / IOKWE（B）**：Submarine Networks 命名 NTA 为拥有/运营者，DCD 确认规划支线；登陆站建筑是最可能的未来 DC 邻近资产，但现在是规划基础设施。
- **贸易媒体（B）**：DCD、Submarine Networks、Subsea Cables News、APNIC、telecoms.com、Reuters、Pacific Island Times、RNZ Pacific、Marshall Islands Journal（本地记录报：Bill 66、故障、Digital Republic）。
- **目录（C）**：DataCenterMap/Datacenters.com/Cloudscene——MH 几乎总缺席，缺席是弱负信号而非证明；cablestatus/GeoCables 的 RFS 日期按 C 级对待。
- **本地机房（C）**：Pacific International Inc.、Majuro Digital Solutions、BOMI、CMI 等企业/银行服务器机房不是本管线 DC，除非主源描述专用机房（电力/机架）。

## 来源分级

- **A** = 官方/一手：NTA 官方页/公告、ICANN L-root 公告、Nitijela 立法 PDF/索引、World Bank 项目文件、USTDA/State Dept 发布、US Army/USAKA 官方页、FCC 公告、海缆运营者官方登陆站记录、云厂商官方区域页（用于缺席确认）。
- **B** = 强二级：DCD、Submarine Networks、Subsea Cables News、APNIC、telecoms.com、Reuters、Marshall Islands Journal、Pacific Island Times、RNZ Pacific、Intelsat/Broadband Commission 外岛部署故事、Wikipedia（仅线索生成/交叉核对）。
- **C** = 弱/聚合：DataCenterMap/Datacenters.com/Cloudscene、专用服务器营销页（atalnetworks.com）、未验证的 CloudFront 边缘 PoP 声称、cablestatus/GeoCables 追踪器、社交媒体轶事。
- **状态语义**：Starlink 可用性/Intelsat 小站/NTA 零售互联网 = 连接性（不记 DC）；IOKWE/CPC = 规划基础设施（不记运营 DC）；登陆站可能未来容纳小型 DDF/colo 机房——建设后重新评估；企业服务器机房默认 C 或 no_projects。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=MH，divisions=24 市镇）。
2. 建种子：NTA 官网/Facebook + ICANN + FCC/TeleGeography 海缆记录 + World Bank P171517 + rmigov.com；归一化拼写（Ebeye=Kwajalein 分区，Uliga/Delap/Rita=Majuro，Jabor=Jaluit，Enewetak/Ujelang 变体）。
3. 对每个分区跑通用模板（英语）；Majuro/Kwajalein 追加 NTA/政府/海缆深度查询（§1.1、§1.4、§1.5）。
4. 核对海缆声称：登陆站对照 FCC/USG 文件与 TeleGeography；IOKWE 按规划基础设施记录（RFS 日期按 C 级）。
5. 去重：HANTRU-1 是一条海缆两个 MH 登陆（Majuro + Ebeye），不得双计；Kwajalein 分区民用（Ebeye）与军事（基地）两条轨道分开。
6. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无证据分区写 `no_projects: true`（完整性优先）。
7. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核马绍尔群岛数据中心（24 市镇粒度，Majuro 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：IOKWE 登陆站开工与 2029 RFS、State Dept 132M 承诺页恢复（当前 B）、CloudFront Majuro PoP 官方确认、Digital Government Office/Capitol 服务器机房证据、NTA colo 产品页是否存在。
