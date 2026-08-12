---
name: se-datacenter-methodology
location: scripts/expansion/world/country-skills/SE/SKILL.md
description: |
  Sweden (SE) datacenter discovery & audit methodology — how to enumerate, verify, and update Sweden datacenter projects at county (län) + municipality (kommun) granularity. Sweden has no national public datacenter facility register: enumeration joins municipal planning/building files (detaljplan, bygglov, marklov, startbesked, slutbesked, council minutes), environmental permitting under miljöbalken (Länsstyrelsen/Miljöprövningsdelegationen, Mark- och miljödomstolen court judgments, Naturvårdsverket-hosted decisions), Svenska kraftnät grid/connection queue context (~7 GW datacenter demand in 2026) plus DSOs and district-heat spillvärme agreements, cloud-region pages (AWS eu-north-1, Azure Sweden Central/South, GCP europe-north2, OCI eu-stockholm-1), PTS/MSB NIS2/Data Act regulatory context, and operator facility pages. Read this before running SE exploration/audit batches. Routes to explorer-official.md (planning/env/court/grid/cloud/regulators) and explorer-industry.md (SweDCI/Business Sweden/trade press/operator portfolios/county matrix).
---

# SE · 瑞典数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：瑞典**没有**全国公开的数据中心设施注册库；枚举是**市政规划/建筑许可（PBL：`detaljplan`/`bygglov`/`startbesked`）+ 环评（`miljöbalken` 第 9 章，Länsstyrelsen/Miljöprövningsdelegationen 决定、Mark- och miljödomstolen 判决）+ 电网（Svenska kraftnät 连接队列约 7 GW 数据中心需求）+ 云区域 + 运营商页** 的多源连接。
> 大型园区的最强早期信号常是**购地/详细规划、电网连接或变电站规划、备用发电机/环评案件**，而非数据中心专用国家许可；备用发电机装机输入功率（`installerad tillförd effekt`）可远大于 IT load，不可混记。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供瑞典探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：市政规划/建筑许可（PBL/Boverket/Lantmäteriet NGP）、环评与法院（Länsstyrelsen/Naturvårdsverket/Domstol.se，含 Equinix SK2、AWS Västerås Kvastbruket 1 660 MW、Google Horndal 实例）、Svenska kraftnät/Ei 电网、PTS Data Act/MSB NIS2、Business Sweden/SweDCI、云区域官方页（AWS/Azure/GCP/OCI）、运营商种子、21 郡路由表、验证与去重规则 |
| `explorer-industry.md` | 行业/厂商发现：SweDCI/Business Sweden/Boverket 流程、运营商官方组合页（Tele2/Bahnhof/atNorth/Conapto/Digital Realty-Interxion/EcoDataCenter/Kolo DC/GleSYS/Equinix/Tietoevry）、超大规模云页（AWS/Azure/GCP/OCI/Meta/CoreWeave）、DCD/Baxtel/DataCenterMap/SVT 等贸易与本地媒体、TED 公共采购、21 郡三遍法（种子→市政→电力/环境）、状态映射与陷阱 |

## 核心结构事实（框定每次搜索）

1. **无全国设施注册库**：枚举以郡（län）+ 市镇（kommun）为操作单元；repo 拼写为 ASCII/英文（Vasterbotten/Scania/Vastra Gotaland…），搜索必须映射瑞典语（Västerbotten/Skåne/Västra Götaland…）。
2. **市政是 PBL 操作层**：`detaljplan`（详细规划：samråd→granskning→antagen→laga kraft）、`bygglov`/`marklov`、`startbesked`/`slutbesked`、`markanvisning`、市议会/建筑委员会纪要；Boverket 是流程权威，Lantmäteriet NGP 只显示已采纳规划的选定信息（发现层，非完整许可库）。
3. **环评是大型项目的强证据**：备用电源、冷却、排水、化学品/燃料储存、噪声触发 `miljötillstånd`/`anmälan om miljöfarlig verksamhet`；官方实例：Equinix SK2（Stockholm MPD 第 9 章许可）、AWS Västerås `Kvastbruket 1`（Nacka 土地环境法院判决，备用电源总装机输入达 660 MW）、Google Horndal（法院附可再生能源/余热条件）。
4. **电网是门控屏**：Svenska kraftnät 2026 公开表显示约 7 GW 数据中心用电请求在队列（全国/区域语境，非项目清单）；`nätutvecklingsplan` 与郡页给出约束；当地 DSO（Ellevio/E.ON/Vattenfall/Göteborg Energi/Jämtkraft/Skellefteå Kraft/Luleå Energi/Borlänge Energi/Falu Energi/Gavle Energi）与供热公司（Stockholm Exergi/Göteborg Energi/Kraftringen 等）暴露 `spillvärme/restvärme` 协议。
5. **云区域=城市/郡级种子（A），非设施地址**：AWS `eu-north-1` Europe (Stockholm) 3 AZ；Azure Sweden Central（Gävle/Sandviken 一带）+ Sweden South（Staffanstorp/Malmö）；GCP `europe-north2` Stockholm（2025）；OCI `eu-stockholm-1` Sweden Central。
6. **PTS/MSB 是监管语境**：PTS 为欧盟 Data Act 主管机构（云服务提供商）；NIS2 经 `cybersäkerhetslagen`（2026-01-15 起）实施；安全敏感设施可能刻意隐藏位置——缺位置≠不存在。
7. **主集群**：Stockholm（colo 密集）、Västmanland（AWS Västerås）、Dalarna（Google Horndal + EcoDataCenter Falun/Borlänge）、Gävleborg（Microsoft Gävle/Sandviken + Ockelbo Valhalla）、Skåne（Microsoft Staffanstorp）、Norrbotten（Meta Luleå + Boden AI/HPC）、Västernorrland（atNorth Sollefteå SWE04 300 MW）、Uppsala（Tierp/Mehedeby 购地线索）。
8. **容量语义**：区分 `ansökt effekt` / `abonnerad effekt` / 备用发电机 `installerad tillförd effekt` / IT load / 场地总功率；瑞典媒体常报园区总功率（含未建阶段）。

## 查询模式（复制粘贴模板见 explorer-official.md §1、§4 / explorer-industry.md §1、§4）

- 瑞语核心词：`datacenter` `data center` `datahall` `serverhall` `datorhall` `colocation` `samlokalisering` `molnregion` `AI-kluster` `HPC` `högpresterande beräkning` `elintensiv verksamhet` `spillvärme` `överskottsvärme` `reservkraft` `dieselaggregat` `ställverk` `fördelningsstation` `nätanslutning`；规划：`detaljplan` `planbesked` `samråd` `granskning` `bygglov` `marklov` `startbesked` `slutbesked` `markanvisning` `markförsäljning`；环评：`miljötillstånd` `miljöprövning` `miljöfarlig verksamhet` `tillståndsplikt B` `verksamhetskod` `installerad tillförd effekt` `kylvatten` `processvatten` `buller`。
- 市政：`"{kommun}" datacenter bygglov`、`"{kommun}" datacenter detaljplan`、`"{kommun}" serverhall bygglov`、`site:{kommun-domain} datacenter bygglov`、`site:{kommun-domain} serverhall OR datorhall`、`"{kommun}" "startbesked" datacenter`。
- 环评/法院：`site:naturvardsverket.se datacenter miljöbalken`、`site:lansstyrelsen.se datacenter miljötillstånd`、`site:lansstyrelsen.se "miljöprövningsdelegationen" datacenter`、`site:domstol.se "Mark- och miljödomstolen" datacenter`、`"{operator}" "{kommun}" reservkraft`。
- 电网：`site:svk.se datacenter anslutningsärenden`、`site:svk.se "{län}" "nätutvecklingsplan"`、`site:ei.se datacenter elnät`、`"{kommun}" datacenter (MW OR MVA OR ställverk OR transformatorstation)`、`"{kommun}" datacenter spillvärme OR restvärme`。
- 英文：`"Sweden" "data center" "building permit"`、`"Gävle" "data center" Microsoft`、`"Luleå" "data center" Meta`、`"Avesta" "Horndal" Google`、`"Västerås" "Amazon Data Services" "reserve power"`。
- 行业：`site:datacenterdynamics.com Sweden "data center" {operator}`、`site:baxtel.com "Sweden" "{operator}"`、`site:datacentermap.com/sweden {city}`、`site:sdia.se {operator}`、TED：`site:ted.europa.eu datacenter "SE"`。
- 状态追踪：`"{kommun}" ("{operator}" OR datacenter) ("antagen" OR "bygglov" OR "startbesked" OR "i drift")`；取消/搁置：`"{project}" (avslag OR överklagad OR stoppad OR uppskjuten)`。

## 官方/监管管线要点（详见 explorer-official.md）

- **市政规划/建筑（A）**：市政站/电子服务搜索 `detaljplaner`/`pågående detaljplaner`/`bygglov`/`diarium`/`anslagstavla`/`protokoll`；提取 `fastighetsbeteckning`、许可引用、申请人/SPV、面积、备用电源范围、`startbesked`/`slutbesked`、上诉状态。实例：Avesta 确认 Google 购地 109 公顷（Horndal）并申请 `marklov`。
- **环评/法院（A）**：Länsstyrelsen `miljöprövningsdelegationen`/`kungörelse`；Naturvårdsverket 托管决定 PDF（Equinix SK2、AWS Västerås）；Domstol.se `Mark- och miljödomstolen`（Google Horndal 2021-06 许可）。提取 `verksamhetskod`、`installerad tillförd effekt`、`reservkraftsanläggning`、`kylvatten`、`buller`、`igångsättningstid`。
- **电网（A，语境）**：Svenska kraftnät 连接案例页（`Datacenter` 分类，通常不点名设施）、`Nätutvecklingsplan 2026-2035`、郡页、`Kapacitetskarta`；Ei 网络监管；当地 DSO 项目页/咨询 PDF（A/B）。
- **PTS/MSB（A，监管语境）**：PTS Data Act 页、MSB NIS2/cybersäkerhetslagen 页；不作设施普查。
- **贸易/投资**：Business Sweden / Data Centers by Sweden（B+/A-，投资促进，站点查找器 B）、SweDCI（B，成员生态）、DCD Sweden tag（B）、Datacenter Forum（B）、DatacenterMap/Baxtel/DataCenters.com（C/B-，仅种子）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商官方页（A- 存在/B 容量）**：Digital Realty/Interxion Stockholm（STO1-STO6，Kista/Akalla 25k m2）、atNorth（SWE01 Kista、SWE02 Akalla Q4 2027、SWE04 Sollefteå 规划 300 MW）、Conapto（Stockholm South 5,200 m2/24 MW，Stockholm 4 South 2024 开）、Bahnhof（Pionen/Thule/S:t Erik/Gullan/Sparven/Göteborg Bunker 规划）、EcoDataCenter（Falun EDC1 80 MW、Borlänge EDC2 至 600 MW 2025 开建）、Kolo DC（CapMan，收购 EcoDataCenter 边缘设施）、GleSYS（Stockholm/Västberga + Falkenberg）、Equinix（官方称瑞典三家）、Tele2/Telia/Cygate/Telenor/GlobalConnect/Arelion（运营商种子）、Tietoevry。
- **云/超大规模（A 区域/C 设施）**：AWS Stockholm 区域 + Västerås 市政/环评证据；Microsoft Gävle/Sandviken/Staffanstorp（local.microsoft.com 官方确认）；Google Cloud Stockholm + Horndal/Avesta 自有土地；Oracle Sweden Central；Meta Luleå（datacenters.atmeta.com，87 亿+ SEK）；CoreWeave（经 EcoDataCenter 的 Falun 负载线索）。
- **贸易媒体**：DCD（B，园区/购地/Microsoft/Vantage/EcoDataCenter/atNorth 更新）、Baxtel（B-/C+）、DataCenterMap/DataCenters.com/OCOLO（C+）、Datacenter Forum（B）、SVT 与本地报（GD/Arbetarbladet/Nya Tierps-Posten 等，B，引用市政文件时）、TED（官方招标，多为 IT 刷新非新设施）。
- **状态映射（瑞语）**：`markförvärv`/`markanvisning`/`planbesked`/`samråd`/`granskning`=提议；`antagen detaljplan`/`lagakraftvunnen`=规划已批未建；`bygglov`/`startbesked`/`pågående markarbeten`/`sprängningsarbeten`=在建；`öppnar`/`i drift`/`go live`/`slutbesked`=运营（仍区分壳楼 vs 实际 IT load）。

## 来源分级

- **A** = 官方/一手：市政建筑/规划门户或 PDF、Länsstyrelsen/MPD 环评决定、Domstol.se/Mark- och miljödomstolen 判决、Naturvårdsverket 托管决定、Svenska kraftnät/Ei/PTS/MSB 官方页、运营商官方设施页（存在/位置）、云区域官方文档（区域存在）、Lantmäteriet 官方地籍/地理数据。
- **B** = 强二级：Business Sweden/SweDCI、DCD、Datacenter Forum、引用市政文件的本地新闻、运营商页容量（未独立核实）。
- **C** = 弱/未验证：DataCenterMap、Baxtel、DataCenters.com、CloudInfrastructureMap、LinkedIn/社交、抓取目录、市场报告片段；仅作搜索种子，须官方页/市政/环评/运营商核实。
- **容量规则**：备用发电机 `installerad tillförd effekt` ≠ IT load；`detaljplan` 允许数据中心用途是场地容量记录，只有附加具名运营商/申请人、建筑许可、环评、施工或运营时才计为设施；安全敏感设施缺地址属预期。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=SE，divisions=21 郡，repo 拼写映射瑞典语）。
2. 建种子：云区域（AWS/Azure/GCP/OCI/Meta）+ 运营商官方页（Digital Realty/atNorth/Conapto/Bahnhof/EcoDataCenter/Equinix/GleSYS 等）+ 已知园区（Västerås/Horndal/Gävle-Sandviken/Staffanstorp/Luleå/Sollefteå/Tierp）。
3. 对每个郡：列出市镇，跑市政域 + lansstyrelsen.se 查询包；三遍法：①运营商/云种子 ②市政规划（detaljplan/planbesked/bygglov/datahall/elintensiv）③电力/环境（svk.se/ei.se/DSO/供热 spillvärme）。
4. 对每个命中捕获最强生命周期文件（官方设施页/详细规划/建筑许可/环评决定/电网记录/带日期的开业发布），容量至少与一个独立来源交叉核对。
5. 去重：按 (母公司/瑞典 SPV/申请人名 + 园区名 + 设施码 SWE01/STO6 + 市镇 + 郡) 归一化；注意 Kista/Akalla 跨 Interxion→Digital Realty 旧名与 Stockholm Data Parks 品牌；`elintensiv verksamhet` ≠ 数据中心除非文档明说。
6. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目 division 写 `no_projects: true`；容量区分 `operational` / `under_construction` / `planned_full_buildout_mw`。
7. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核瑞典数据中心（21 郡粒度，Stockholm/Västmanland/Dalarna/Gävleborg/Skåne/Norrbotten 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Google Horndal 建设进度、AWS Västerås 各期、Microsoft Gävle-Sandviken/Staffanstorp 许可状态、atNorth SWE02/SWE04 时间表、EcoDataCenter Borlänge EDC2 开工、Conapto/CoreWeave 扩张、Tierp/Mehedeby 大项目、Vantage 瑞典线索、Svenska kraftnät 队列中具名项目（通常不公开）。
