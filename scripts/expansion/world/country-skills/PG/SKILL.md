---
name: pg-datacenter-methodology
location: scripts/expansion/world/country-skills/PG/SKILL.md
description: |
  Parent-level data-center enumeration methodology for Papua New Guinea (PG). PNG
  has no public national datacenter registry; enumeration triangulates operator
  pages, SOE announcements (PNG DataCo, KCH, Telikom, Datec), Department of ICT
  GovCloud/digital-government material, NICTA licensing, NPC tenders, subsea
  cable/IXP sources, trade press and directories across 22 provinces. English
  primary with Tok Pisin secondary; data centre/data center both searched. Read
  this before running PG exploration/audit batches. Routes to
  explorer-official.md (official/regulatory/cloud/energy pipeline) and
  explorer-industry.md (industry/vendor/connectivity/province recipes).
---

# PG · 巴布亚新几内亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：PNG has no public national datacenter registry；枚举最佳路径是三角测量 运营商页、国企/SOE 公告（PNG DataCo、KCH、Telikom、Datec）、DICT 数字政府材料、NICTA 牌照语境、NPC 招标/中标、海底光缆/IXP 来源、贸易媒体与目录。
> 多轨三角测量：官方/SOE/运营商轨道产出 A 级证据，电缆/连接性轨道产出 B 级地点线索，目录与社交仅作 C 级发现；云/GovCloud 平台 ≠ 新物理设施。
> 本 skill 汇总两份探索报告（explorer-official.md / explorer-industry.md）为国家层方法论；批次执行前必读。

## 入口

| 文件 | 内容 | 说明 |
|---|---|---|
| explorer-official.md | 官方/监管/云/能源管线：NCDC 建筑许可、DLPP 规划、CEPA 环境许可、NICTA 牌照（含 Ninja Tables AJAX 端点）、DICT GovCloud、PNG DataCo、云区域核验、PNG Power/KCH 电网、种子项目/运营商表、22 省搜索模式 | A 级主干与查询模板 |
| explorer-industry.md | 行业/厂商/连接性/省域配方：运营商与 colo 种子清单、云与主权云扫描（含 Alibaba/CloudSigma）、连接性枢轴（Coral Sea/KSCN/PPC-1/Puk-Puk 1/PNG-IX）、政府/采购与标准扫描、五遍省域配方、证据分级与陷阱 | A/B/C 全谱系 |

## 核心结构事实（框定每次搜索）

1. **无国家数据中心注册表**：PNG 不存在公开的全国数据中心登记；ISOC Pulse 2026 报告列 **2 个活跃数据中心 + 2 个活跃 IXP**——市场语境而非完整设施登记。
2. **地理集中**：硬性设施证据集中在 **National Capital District / Port Moresby** 与 **Madang**；次级观察点：Morobe / Lae、Western Highlands / Mount Hagen、West Sepik / Vanimo、Bougainville、East New Britain / Kokopo-Rabaul、Milne Bay / Alotau、New Ireland / Kavieng、Northern / Popondetta（光缆、电信、政府或省 ICT 节点）。
3. **语言**：官方来源以英语为主；同时搜 `data centre` 与 `data center`（加 `datacentre`）；连接性词汇：`CLS`、`MCLS`、`PPC-1`、`Coral Sea Cable`、`Kumul Submarine Cable`、`Pukpuk`、`Bulikula`、`Hawaiki Nui`、`earth station`、`IXP`；Tok Pisin（`data senta`、`gavman cloud`、`kompiuta senta`）仅作本地媒体/社交二线核验。
4. **省属陷阱**：Port Moresby 属 **National Capital District** 而非 Central 省；Lae 属 Morobe、Madang 镇属 Madang、Mount Hagen 属 Western Highlands、Vanimo 属 West Sepik、Alotau 属 Milne Bay、Popondetta 属 Northern、Kavieng 属 New Ireland、Kokopo/Rabaul 属 East New Britain、Arawa/Buka 属 Bougainville。
5. **云语义（含负向控制）**：AWS/Azure/GCP/OCI/Alibaba 官方区域页均无 PNG 公有云区域（截至 2026-08-12 核验）；PNG 相关云信号是合作伙伴/本地云——Oracle 与 PNG DataCo、Telikom/Datec/CloudSigma 主权 AI 数据中心（2026-03 预发布，A 级公告/B 级物理设施）；Google 通过 Pacific Connect/Bulikula/Pukpuk 海底光缆介入——连接性线索而非云区域证据。
6. **设施分类**：区分 commercial colo、sovereign/government cloud、enterprise/private facility（BSP、银行）、telecom/network facility（Digicel 核心网）、micro-edge（NFA/Zella）、cable landing station（无托管角色不算数据中心）、false positive（call centre、training centre、NOC、资源中心）。
7. **容量语义**：PNG 来源极少公布 MW/机架；不得从 Tier 3、AI、sovereign 措辞或电缆容量推断容量；未声明则 `capacity_mw` 留空。
8. **状态纪律**：`pre-launched`、`MoU`、`partnership`、`roadshow`、`plans to procure` ≠ 运营设施；运营商/SOE 页声明已投产并给出物理地点才算 operational。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§7 / explorer-industry.md §6-§7）

- 官方/许可：`site:ncdc.gov.pg ("data centre" OR "data center" OR "cloud") "Port Moresby"`、`"Building Permit" "data centre" "NCDC"`、`"Planning Permission" "data centre" "Papua New Guinea"`、`site:cepa.gov.pg ("data centre" OR "telecommunications" OR "generator")`。
- 监管/牌照：`site:nicta.gov.pg "PNG Dataco Limited" "license"`、`"{licensee}" ("data centre" OR "data center" OR "cloud" OR "colocation") "Papua New Guinea"`。
- 政府云/主权托管：`site:ict.gov.pg ("GovCloud" OR "Government Cloud" OR "Central Electronic Data Repository" OR "Government Private Network")`、`site:pngdataco.com ("data center" OR "Oracle Cloud" OR "Tier 3")`、`"PNG DataCo" ("Caution Bay" OR "Lae SEZ" OR "Highlands" OR "Islands") "data centre"`、`"Sovereign AI Data Centre" "Papua New Guinea" "Telikom" "Datec" "CloudSigma"`。
- 电力/电网：`site:pngpower.com.pg ("data centre" OR "substation" OR "connection") "{city}"`、`site:kch.com.pg ("132kV" OR "Ramu Grid") "{province}"`。
- 贸易/本地媒体：`site:datacenterdynamics.com/en/news/ "Papua New Guinea" "data center"`、`site:businessadvantagepng.com "PNG DataCo" Oracle "data centre"`、`site:developingtelecoms.com "Papua New Guinea" ("data centre" OR "cloud" OR "Oracle")`、`site:apacoutlookmag.com Vodafone PNG "data centre" Lae "Mount Hagen"`。
- 连接性：`"Kumul Submarine Cable Network" "data centres" "Port Moresby" Madang`、`"PPC-1" Madang "data centre" OR CLS`、`"Coral Sea Cable" "Port Moresby" "landing station" OR MCLS`、`"Puk-Puk 1" Vanimo "cable landing" "PNG DataCo"`、`"PNG-IX" "data centre" OR facility`。
- 省域通用模板：`"{province}" "Papua New Guinea" "data centre"`、`"{main town}" PNG colocation OR "co-location" OR hosting`、`"{main town}" PNG "cable landing" OR CLS OR "earth station"`、`site:npc.gov.pg "{province OR town}" "data centre" OR server OR hosting`。

## 官方/监管管线要点（详见 explorer-official.md）

- **NCDC（国家首都区委员会）**：Port Moresby 最有用的公共规划来源；仅当实际规划/建筑公告、申请、招标或董事会通知点名场地/项目时为 A 级存在/状态证据；门户多为表格与政策页，网络搜索优于浏览。
- **DLPP（国土与物理规划部）**：Physical Planning Act 1989 管辖——A 级法律路径而非设施枚举门户；省物理规划委员会与市当局用于 NCD 以外省份。
- **CEPA（环保局）**：Environment (Permits) Regulation 2002 要求接受/授予许可的公告；许可公告点名项目为 A，仅报纸公告无许可号为 B/C；可揭示柴油发电、冷却水、废弃物排放与建设足迹。
- **NICTA**：官方 ICT 监管机构，最佳运营商普查来源；已注册持牌人含 PNG Dataco、Datec、Telikom、Digicel、Vodafone PNG、Global Internet、Kumul Communications、Comserv、Niugini Comtech、Digitec ICT、Daltron、Speedcast 等；牌照证明运营商存在/权威（A），不证明数据中心。
- **DICT / GovCloud**：GovCloud 基础设施服务、Central Electronic Data Repository、Government Private Network 以 PNG DataCo 为实施伙伴且含数据主权要求——A 级国家政府云管线；Draft Government Cloud Policy 2023 与 Government Cloud Standards PDF 为政策/标准语境。
- **PNG DataCo**：`pngdataco.com` 数据中心服务页描述 Tier 3/ISO 认证、PNG 数据驻留、冗余电力/冷却与 24/7 监控（A 级服务存在）；Business Advantage PNG 2026 访谈称 DataCo 在 **Port Moresby 与 Madang** 有数据中心，并考虑 **Kumul Petroleum Caution Bay SEZ、Lae SEZ、Islands、Highlands**（B 级，逐个站点以 NCDC/DLPP/CEPA/PNG Power/招标验证）。
- **电力/电网**：PNG 供电分散且可靠性受限；KCH 2026 年 Tari-Hagen-Yonki (Ramu) 132kV 投运强化 Highlands/Ramu 走廊（Eastern Highlands、Chimbu、Jiwaka、Western Highlands、Southern Highlands、Hela、Enga、Morobe、Madang 的电力可行性优先序）；PNG Power 门户为变电站/连接查询。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商种子（存在性 A / 容量视证据）**：PNG DataCo（A，POM 主设施 + Madang CLS/DR）、Telikom（SOE 伙伴，2026 主权 AI DC）、Datec PNG（A 服务页：云、设备 colo、DR、BCP）、CloudSigma（伙伴，物理托管站点待证）、Digitec/Vodafone PNG（APAC Outlook：Port Moresby 主数据中心 + Lae 后 Mount Hagen 区域中心计划，B）、Digicel（网络核心，非公共 colo，仅明确托管/colo/DR 功能时计数）、Online South Pacific（声称 Port Moresby 两个 colo 数据中心，验证前 ≤B/C）、Daltron（集成商）、APCS（DICT DTS 提及，待官方确认）、BSP（RPS 项目页 A 级企业设施）、Huawei 承建政府国家数据中心（约 2018 年启用，DCD 2020 报道重大安全/维护问题，现状态以 DICT/GovCloud 文档核验）、NFA/Zella（微边缘，非 colo）。
- **贸易/本地媒体（B）**：DCD（PNG 标签）、Business Advantage PNG、Developing Telecoms、APAC Outlook、PNG Business News、NBC PNG、EMTV、FM100、Post-Courier、The National；命名运营商/项目/地点/日期时升 B。
- **目录/互连（C/B-）**：DataCenterMap（PNG DataCo POM + Madang CLS）、Inflect（Datec POM）、Cloudscene、PeeringDB、PCH、IXP Tracker、ISOC Pulse（2 DC + 2 IXP）、SubmarineNetworks/TeleGeography/SubTel Forum（电缆着陆线索）。
- **连接性枢轴**：Coral Sea Cable（Sydney-Port Moresby-Honiara，4,700 km）、KSCN（连 14 省与 POM/Madang 两个国家数据中心）、PPC-1（Madang CLS）、Puk-Puk 1（Vanimo，连 Jayapura）、Google/Pukpuk（澳洲防务条约下三条新缆）、PNG-IX（首个中立 IXP）——着陆站与 IXP 仅证明互连存在。

## 来源分级

- **A** = 官方/一手：运营商自有设施/服务页、政府/SOE 公告点名数据中心、数据中心工程采购/合同、承包商项目页（交付设施）、官方云区域列表（公有云地理）、NICTA 牌照记录、NCDC/DLPP/CEPA 具名项目记录。
- **B** = 强二手：DCD、Business Advantage PNG、Developing Telecoms、APAC Outlook、NBC/EMTV/FM100/PNG Business News（具名运营商/项目/地点）、含物理交付细节的厂商案例。
- **C** = 弱线索：目录、Mapcarta/OSM/Google Maps、社交帖、LinkedIn 声明、市场报告、泛云/ICT 活动文本、电缆地图。
- **状态词汇**：`RFI`/`EOI`/`RFP`/`tender`/`contract awarded` = 采购阶段；`pre-launch`/`MoU`/`partnership`/`roadshow`/`plans to procure` = announced/planned；`launch`/`pre-launched`/`commissioned`/`operational` = 更强信号但仍需物理地点。
- **容量规则**：MW/kVA/机架/柜/平方米仅直接声明时记录；Tier 评级、电缆容量、电信网络规模不可推断容量。
- **弱线索过滤器**：`"data centre" "Papua New Guinea" -"call centre" -"training centre"`；仅 `server room`/`ICT resource centre`/`NOC`/`digital service platform` 时不计为数据中心。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中 `country_code == "PG"` 的条目，按 division 分组（22 省/自治区）。
2. 以本 skill 运营商标记构建种子：PNG DataCo、Datec、Telikom、CloudSigma、Vodafone/Digitec、Digicel、Online South Pacific、Daltron、APCS、BSP/Huawei 政府设施。
3. 确认公有云缺失：检查 AWS/Azure/GCP/OCI/Alibaba 官方区域页，记录无 PNG 公有区域（除非官方列表变化）。
4. NCD + Madang 深扫：运营商页、目录、IXP/PeeringDB/PCH、光缆着陆源、政府云/采购、本地媒体。
5. 区域观察扫描：Lae/Morobe、Mount Hagen/Western Highlands、Vanimo/West Sepik、Bougainville、Kokopo/Rabaul、Alotau、Kavieng、Popondetta——电缆/运营商/本地媒体词。
6. 每条线索以一手来源验证并归类：commercial colo、sovereign/government cloud、enterprise/private、telecom/network、micro-edge、CLS、false positive。
7. 按 world schema 输出：`{country_code: "PG", country_name: "Papua New Guinea", division, city, name, operator, status, capacity_mw, source_urls, evidence_date, evidence_grade, notes}`；服务被确认但无建筑的记录为 cloud/hosting service lead 而非物理数据中心；负结果 `no_projects: true` 注明所搜词与日期。
8. **NO-DELETION**：不改写 explorer-official.md / explorer-industry.md；复核批次只增补不删行。

## 待办（2026-08-12 02:39Z）

- 两份探索报告已合并为国家层方法论；下一步以本 skill 为国家层参考运行 PG 探索/复核批次（22 省）。
- 需验证：Sovereign AI Data Centre（Telikom/Datec/CloudSigma）是新建物理站点、既有 Datec/Telikom 设施还是境内托管云栈；PNG DataCo Madang 设施与 PPC-1 CLS 以 DataCo 官方页确认；Vodafone PNG Lae/Mount Hagen 区域中心现状；Huawei 政府国家数据中心当前状态（DICT/GovCloud 文档）；Online South Pacific 两个 POM 设施所有权与地址；NFA/Zella 微边缘地点（NCD 或其他省）。
