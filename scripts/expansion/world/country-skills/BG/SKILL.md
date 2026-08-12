---
name: bg-datacenter-methodology
location: scripts/expansion/world/country-skills/BG/SKILL.md
description: |
  Bulgaria (BG) datacenter discovery & audit methodology — how to enumerate, verify, and update Bulgaria datacenter projects across 28 NUTS3 districts / 265 municipalities. Bulgaria is a municipal-permit country: building permits and commissioning certificates live with each municipality / chief architect (главен архитект), not a national planning portal. Enumeration proceeds province → municipality → permit/EIA/grid/operator, triangulating Sofia NAG registers, MOEW/RIEW EIA registers, ESO/distribution grid evidence, CRC operator records, CAIS EOP procurement, Registry Agency filings, cloud/edge pages (no hyperscaler region — Exoscale BG-SOF-1 is the named cloud zone), operator facility pages (Equinix SO1/SO2, Digital Realty/Telepoint, Neterra SDC, Evolink, Daticum, A1, CETIN), and trade press. Read this before running BG exploration/audit batches. Routes to explorer-official.md (official/regulatory/cloud pipeline) and explorer-industry.md (trade press / vendor discovery).
---

# BG · 保加利亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：保加利亚是**市政许可制国家**——建设许可与投产证书由各市 / 总建筑师（главен архитект）持有，**没有**单一全国规划许可搜索门户，不能按英国 LPA 或美国市政统一入口方式直接枚举。
> 枚举按 **省（област）→ 市（община）→ 许可/EIA/电网/运营商** 逐级下钻，三角测量：Sofia NAG 建筑许可登记册、MOEW/RIEW 环评登记册、ESO/配电公司电网证据、CRC 运营商登记、CAIS EOP 公共采购、Registry Agency 公司档案、云/边缘官方页（无超大规模区域）、运营商设施页与行业媒体。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供保加利亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：Sofia NAG 各登记册、市政 `Разрешения за строеж`/`чл.149 ЗУТ`、MOEW/RIEW EIA、ESO/配电公司/EWRC、CRC 运营商、CAIS EOP 采购、Registry Agency/BULSTAT/地籍、云与边缘官方页、28 省逐省矩阵 |
| `explorer-industry.md` | 行业/厂商发现：BIX.BG/DE-CIX Sofia/NetIX/PeeringDB 互联层、运营商与项目种子清单（Sofia/Plovdiv/海岸/Ruse 等分区模板）、DCD/SeeNews/Capital/TechNews 媒体、Baxtel/DataCenterMap/Datacenters.com 目录、逐省四遍扫描法、状态映射与陷阱 |

## 核心结构事实（框定每次搜索）

1. **市政许可制**：同一项目可能以 `център за данни`、`дейта център`、`дата център`、`data center`、`информационен център`、`изчислителен център`、`сървърно помещение`、`колокационен център` 或电信/工业建筑名义出现；Sofia 首选官方登记册为 NAG（https://nag.sofia.bg/pages/render/187），含建筑许可、基础设施许可、投产证书（удостоверение за въвеждане в експлоатация）、设计签证、用途变更与城市规划令。
2. **Sofia 为主市场**，但 Sofia 市与 Sofia 省是两个省：`SDC Stolnik` 在 Sofia 省，不在 Sofia 市；目录常把 Kaspichan/Varna/Sofia 地址错放，须按官方市/地籍地址重新分桶。
3. **28 个 NUTS3 省 / 265 个市**（NSI 2025）：manifest 用省，但许可在市级——查市政页、市政议会纪要、RIEW、工业园区站点，而不是只查省行政页。
4. **大型数据中心在电网/环评/采购/土地/电信记录中证据更强**，泛泛的建筑许可统计弱；用变电站名找隐藏项目（许可标题可能是通用工业/仓库）。
5. **无超大规模公共云区域**：AWS/Azure/GCP/OCI 官方区域页无保加利亚区域（Azure Front Door 有 Sofia 边缘 POP，AWS 最近 Local Zone 为 Athens/Istanbul/Warsaw）——区域/边缘证据 ≠ 设施；Exoscale `BG-SOF-1`（A1 Lift，3 Nedelcho Bonchev St）是具名商用云区，不是超大规模区域。
6. **容量语义**：区分 `installed capacity` / `dedicated power` / `renewable supply` / `rack capacity` / `future expansion` / `grid connection`；保语文章常只报投资额没有 MW；运营商容量多为营销值，须许可/EIA/电网确认。
7. **西里尔文搜索必需**：拉丁（data center/datacenter）与西里尔（дейта център/дата център/център за данни）两种形式都要搜；西里尔文找到许可与地方政府页，英文找到运营商与行业媒体。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§6 / explorer-industry.md §2-§5）

- 设施词：`"център за данни"`、`"дейта център"`、`"дата център"`、`"data center" OR "data centre"`、`"колокационен център"`、`"сървърно помещение"`、`"резервен център за данни"`、`HPC OR суперкомпютър`。
- 许可/状态：`"разрешение за строеж" "център за данни" "{省或市}"`、`"съобщение" "чл.149" "ЗУТ" "център за данни"`、`"виза за проектиране"`、`"подробен устройствен план" OR "ПУП"`、`"Акт 16" OR "удостоверение за въвеждане в експлоатация"`。
- 电网/环评：`"присъединяване" "център за данни" "ЕСО"`、`"подстанция" "център за данни"`、`"110 kV" "дейта център"`、`"ОВОС" "център за данни"`、`"инвестиционно предложение" "център за данни"`、`site:riosv* "център за данни"`。
- 采购：`site:app.eop.bg "център за данни"`、`site:app.eop.bg "резервен център за данни"`、`site:app.eop.bg "колокация"`。
- 运营商：`"колокация" "{城市}" България`、`"дейта център" "{城市}" "ISO 27001"`、`"Tier III" София`、`site:{运营商域} "център за данни"`。
- 互联：`site:bix.bg`、`site:de-cix.net Sofia`、`site:peeringdb.com/fac Bulgaria Sofia`、`"Sofia" "cloud on-ramp"`。
- 行业：`site:datacenterdynamics.com Bulgaria "data center"`、`site:seenews.com Bulgaria data centre`、`site:capital.bg "дейта център"`、`site:economic.bg "център за данни"`、`site:technews.bg "дейта център"`。
- 云负向对照：`site:aws.amazon.com Bulgaria Sofia "Local Zone"`、`site:learn.microsoft.com/azure "Bulgaria" "region"`、`site:cloud.google.com/about/locations Bulgaria`、`site:oracle.com/cloud/public-cloud-regions Bulgaria`。

## 官方/监管管线要点（详见 explorer-official.md）

- **Sofia NAG 登记册（A）**：建筑许可、基础设施许可、投产证书、设计签证、用途变更——按运营商/街道/区/地籍标识符检索；其他市政按 `{市} "Разрешения за строеж"` 或 `{市}.egov.bg` 检索，用总建筑师签发机关与生效语言区分草稿与有效许可。
- **MOEW 公共 EIA 登记册 + 16 个 RIEW（A）**：投资提案、筛选决定、柴油发电机数、冷却/水系统、供电描述；优先 RIEW：Sofia、Pernik/Sofia-region、Plovdiv、Stara Zagora、Burgas、Varna、Ruse、Shumen、Haskovo。
- **电网（A）**：ESO EAD（输电网、并网请求、十年输电网发展规划 110/220/400 kV 工程）；配电三区——Electrohold/ERM West（Sofia/西部）、Energo-Pro（东北）、EVN（东南）；EWRC（能源牌照语境，非设施发现）。
- **CRC / КРС（A=运营商地位）**：公共电子通信网络/服务申报登记册，是**运营商侧登记**，非设施登记——用于种子电信/ISP 名称，再逐一 pivot 到市政许可、EIA、官方 colo 页、采购。
- **CAIS EOP / AOP（A=合同）**：政府数据中心升级、供配电/冷却工程、colo/DR 服务、电信招标；只有点名物理场地或托管地域时才作设施证据。
- **公司/土地（A）**：Registry Agency（UIC/EIK、年报、所有权）、BULSTAT、地籍标识符（идентификатор）串联市政许可与 EIA。
- **云管线**：无超大规模区域（负向对照）；Exoscale BG-SOF-1/A1 Lift 为商用云区；Azure Front Door Sofia 为边缘 POP（互联证据，非设施）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Sofia 锚点（A/B）**：Digital Realty/Telepoint（2026-03-02 收购进入保加利亚；两座 Sofia DC，110+ 网络服务商、多云 on-ramp；别名 Telepoint Sofia East/Sofia Centre、122 Ovcho Pole、8 Asen Yordanov、Digital Realty Sofia）；Equinix SO1/SO2（约 35,000 sq ft / 3,215 m²；SO1 在 Druzhba-1，SO2 在 Nedelcho Bonchev）；Neterra/SDC（SDC 1、SDC 2（2022 开园，约 2 MW / 1,400 m²）、SDC Stolnik（Sofia 省）、SDC Ruse）；Evolink（Sofia 1/2 + Plovdiv，Sofia 2 为 carrier-neutral）；Daticum/Sirma（135 Tsarigradsko Shose）；A1（A1 Data Center；Exoscale BG-SOF-1 在其 Lift 设施）；CETIN Serdika DC；BRAIN++/Sofia Tech Park AI Factory（INSAIT，€90M EU AI factory，2026 开工、三年内建成——按公共/HPC 计算设施单列）。
- **Plovdiv（B/C）**：Brinell Compute（Rakovski 工业区/Maritsa，~€30 亿 AI 园区——B 级直到市政/RIEW/建筑备案捕获）、CETIN Trakia DC（A/B）、Evolink Plovdiv、VueNow（2021 MoU，陈旧线索）。
- **海岸（A/B）**：Top Systems Burgas/BOJ（2026 计划开园，2.5 MW、1,200 m²、220 机架、100% 可再生，远期 10 MW / 5,000 m²）、AC DC/AbsCloud Varna 绿色 DC、Varna Data Center；VueNow 边缘仅旧 MoU。
- **其他区域种子**：SDC Ruse（A）、Telepoint Montana（B/C，Digital Realty 收购仅点名两座 Sofia，Montana 按旧设施核验）、Vivacom/Eutelsat Stara Zagora 地面站 mini DC（A，卫星基础设施，非标准 colo）、TSBG Kapitan Andreevo（C）、ESCOM Haskovo（C）。
- **互联层（A/B）**：BIX.BG（首个保国 IXP，跨 10+ Sofia 数据中心）、DE-CIX Sofia（130+ 网络、11 Tbps 连接容量、峰值 1.3 Tbps+、10 个 Sofia 城域 PoP）、NetIX、PeeringDB（Sofia 设施活跃证据，不完整）。
- **媒体**：DCD（B）、SeeNews（B）、Capital.bg/Dnevnik（B）、Economic.bg/TechNews.bg/Computerworld.bg/Investor.bg（B，AI 工厂/运营商扩张/政府云）、BTA/BNR（B；2026 政治性「三份数据中心协议」声明按 C 直到具名投资者/许可出现）；目录 Baxtel/DataCenterMap（C+）、Datacenters.com/Inflect/Cloudscene/OCOLO/DC Atlas（C）。

## 来源分级

- **A** = 官方/一手/可追责：NAG 或官方市政域的建筑许可/基础设施许可/投产证书、MOEW/RIEW EIA 决定或投资提案、ESO/配电公司并网文件或具名变电站工程、CRC 运营商登记（运营商地位，非设施）、CAIS EOP 采购记录（点名场地时）、Registry Agency/BULSTAT、运营商官方设施页（存在/位置 A，容量 B）、云厂商官方区域/边缘页（区域/边缘在场）、政府/EuroHPC/INSAIT/Sofia Tech Park 官方发布。
- **B** = 强二级：DCD、SeeNews、Capital.bg/Dnevnik、Economic.bg/TechNews.bg、BTA/BNR（引述政府/运营商文件时）、可信本地媒体；CMS 等仅作流程参考。
- **C** = 弱/未验证：DataCenterMap、Datacenters.com、Baxtel、Inflect、Cloudscene、OCOLO、DC Atlas、社交帖、市场摘要、旧 MoU（如 VueNow 2021）；聚合库默认 C。
- 状态语义（保语）：`виза за проектиране`/`ПУП`/`инвестиционно предложение` = 早期规划；`разрешение за строеж`/`одобрен инвестиционен проект` = 已许可（未必开工）；`откриване на строителна площадка`/`започва строителство`/`първа копка` = 开工；`Акт 15`/`Акт 16`/`удостоверение за въвеждане в експлоатация` = 投产/运营就绪；`открит`/`в експлоатация`/`работещ`/`operational` = 运营（仍用投产记录/运营商页核验）。
- **陷阱**：采购中的 `център за данни` 常指办公楼内企业服务器机房，非商用 colo；`дата център` 为非正式拼写也要搜；`Cloud Виртуален център за данни` 采购除非是机房建设/装修/运营/供电/冷却/机架工程，否则不算物理设施；医院/大学/市政/卫星地面站服务器房不计商用 colo；Telepoint 收购后不得双重计数；Exoscale BG-SOF-1 不是超大规模区域；边缘 POP/on-ramp 仅作互联证据。
- **政策/声明 ≠ 项目容量**：部长/政治声明、MoU、投资备忘录须有具名投资者+场地+许可才计 C 以上；Brinell、VueNow 等按此处理。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=BG，divisions=28 省 → 265 市）。
2. 种子已知设施与运营商：Equinix SO1/SO2、Digital Realty/Telepoint、Neterra SDC 1/2/Stolnik/Ruse、Evolink Sofia 1/2、Daticum、A1/Exoscale、CETIN Serdika/Trakia、Vivacom/A1 区域 colo、Top Systems Burgas、AC DC/AbsCloud Varna、BRAIN++。
3. Sofia 官方核验：对每个种子搜 NAG 建筑许可/基础设施许可/设计签证/投产证书（按运营商、街道、区、地籍标识符）；Sofia 溢出区扫 Sofia 省与 Pernik（Столник、Божурище、Елин Пелин、Костинброд、Перник、подстанция、110 kV）。
4. EIA 扫描：MOEW 公共登记册 + RIEW 页；电网扫描：ESO 并网/十年规划 + 配电公司公告，用变电站名找隐藏项目。
5. CRC 运营商扩展：从公共电子通信登记建电信/ISP 宇宙，逐一 pivot；采购补漏：CAIS EOP（公共数据中心、colo、供配电/冷却、DR）。
6. 行业媒体 delta 监控：DCD/SeeNews/Capital/BTA/公司新闻稿，仅在许可/EIA/运营商页确认后升级。
7. 去重：按地址/地籍 ID/变电站/运营商图谱匹配；注意品牌名、法人实体、街道地址、电信节点名四套标识。输出 world 同 schema；无设施级证据输出 `no_projects: true`。
8. 遵行 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:40Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：探索/复核批次按 28 省分桶（省 → 市）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Brinell Compute（Maritsa/Rakovski）市政/RIEW/建筑备案进度；Top Systems Burgas 2026 投产；Digital Realty/Telepoint 收购后 Sofia East/Centre 的现行官方页；BRAIN++ 开工时间表；Telepoint Montana 现行状态。
