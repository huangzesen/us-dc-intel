---
name: na-datacenter-methodology
location: scripts/expansion/world/country-skills/NA/SKILL.md
description: |
  Namibia (NA) data-center enumeration methodology. Division model: 14 first-level regions (Erongo, Hardap, //Karas, Kavango East, Kavango West, Khomas, Kunene, Ohangwena, Omaheke, Omusati, Oshana, Oshikoto, Otjozondjupa, Zambezi); Priority 1 = Khomas (Windhoek/Brakwater) and Erongo (Swakopmund/Walvis Bay) — the only regions with confirmed commercial/cable-linked evidence. No single national public register of data centers or building permits; enumeration cross-checks operators/cable evidence, municipal planning/building control, MEFT EIA/ECC, ECB/MME/NamPower/RED power records, CRAN licences, BIPA registry, Gazette and eProcurement. No hyperscaler region listed for NA (Africa/South Africa presence only). Key seeds: Paratus Armada Data Center (Brakwater/Windhoek, launched Aug 2022, N$123m, DC1/DC2 halls), Telecom Namibia Infinitum co-location (Windhoek), Swakopmund cable landing (Equiano 2022 landing, Telecom Namibia CLS activated 2024; WACS/2Africa), Government/National Data Centre (lead only). Read this before running NA exploration/audit batches. Routes to explorer-official.md (municipal/MEFT/power/CRAN/Gazette playbook) and explorer-industry.md (operator/press/market playbook).
---

# NA · 纳米比亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：纳米比亚无全国统一的数据中心或建筑许可公共登记册，枚举靠交叉核验：已知运营商与海缆证据 → 地方当局规划/建筑控制 → MEFT 环评/ECC → ECB/MME/NamPower/RED 电力 → CRAN 牌照与 Gazette → BIPA 法人 → 采购门户。B/C 材料只生成线索，匹配官方页/市政记录/Gazette/监管记录/采购/登记后才升 A。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：地方当局规划与建筑控制、MEFT EIA/ECC、电力与电网（ECB/NamPower/RED）、CRAN、Gazette/BIPA/采购、官方运营商与云区域种子、14 区逐区策略、词汇与去重 |
| `explorer-industry.md` | 行业/媒体/厂商管线：运营商/厂商页、本地与贸易媒体、云区域核查、已知线索处理、查询剧本、14 区矩阵 |

## 核心结构事实（框定每次搜索）

1. 行政区划：**14 个一级区**：Erongo、Hardap、//Karas、Kavango East、Kavango West、Khomas、Kunene、Ohangwena、Omaheke、Omusati、Oshana、Oshikoto、Otjozondjupa、Zambezi。统计口径：Namibia Statistics Agency 区域概况 https://nsa.org.na/document-category/regional-profiles/ 。
2. **无统一登记册**：枚举为交叉核验练习——① 从已知运营商与海缆/登陆证据出发；② 经地方当局规划/建筑控制核实场地事实；③ 查 MEFT 环境记录（柴油储存、备用发电、变电站、水/冷却、电信基建、敏感区建设等列项活动）；④ 查 ECB/MME/NamPower/RED 发电、供电、转供与并网证据；⑤ 查 CRAN 牌照类别与 Gazette 公告；⑥ 用 BIPA 确认项目发起方法人；⑦ 用 Gazette 与公共采购门户抓国家 ICT/DC 项目。
3. 优先地理：**P1 = Khomas（Windhoek/Brakwater）与 Erongo（Swakopmund/Walvis Bay）**——仅有的确认商业/海缆关联证据区；**P2 = Oshana 与 Otjozondjupa**（北部与中部交通/电力/电信走廊）；**P3/观察 = //Karas 与 Hardap**（可再生电力、氢、矿业、港口邻近产业）；**P4 = 其余区**（主要确认缺失并捕获电信/政府 ICT 机房）。
4. **无超大规模云区域**：AWS/Azure/GCP/Oracle 官方区域页仅显示非洲/南非区域，未列纳米比亚。不得从南非区域或 Google Equiano 推断纳米比亚超大规模设施。
5. 海缆登陆站 ≠ 商业 colo：除非来源明确说该处提供 colo/DC/托管/客户机架服务，否则分开记录。
6. 语言：英语 `data centre / data center / datacenter / colocation / co-location / server room / server hall / data hall / hosting facility / cloud services / Tier III / carrier neutral / cable landing station / network facilities licence / backup generator / diesel storage / substation / MVA / MW / environmental clearance certificate / town planning scheme / rezoning / consent use / building line relaxation`；阿非利卡语/德语变体：`data sentrum / rekenaarsentrum / kolokasie / Rechenzentrum`（site:republikein.com.na "data sentrum"、site:az.com.na "Rechenzentrum"）。
7. 去重键：`(operator/legal entity, town/site, project name, capacity)`——同一项目可能以新闻稿、建筑图、环评、电力牌照、CRAN 公告、运营商页多形态出现。

## 查询模式（复制粘贴模板见 explorer-official.md §1-4 与 explorer-industry.md §3-4）

- 市政/建筑：`site:windhoekcc.org.na "data centre"`、`site:windhoekcc.org.na "building plan" "Brakwater"`、`site:swakopmun.com "data centre"`、`site:walvisbaycc.org.na "building plan" "data"`、`"data centre" "rezoning" Namibia`、`"data centre" "consent use" Namibia`、`"server hall" "building plan" Namibia`、`"diesel storage" "data centre" Namibia`。
- 环境：`site:eia.meft.gov.na "data centre"`、`site:eia.meft.gov.na "Paratus"`、`site:eia.meft.gov.na "Telecom Namibia"`、`site:eia.meft.gov.na "cable landing"`、`"environmental clearance certificate" "data centre" Namibia`、`"scoping report" "data centre" Namibia`、`"Swakopmund" "cable landing station" "environmental"`。
- 电力：`site:ecb.org.na "data centre"`、`site:ecb.org.na "generation licence" "Windhoek"`、`site:nampower.com.na "substation" "Brakwater"`、`site:nampower.com.na "substation" "Swakopmund"`、`"NamPower" "data centre" Namibia`、`"Erongo RED" "data centre"`、`"CENORED" "data centre"`、`"NORED" "data centre"`。
- CRAN：`site:cran.na "data centre"`、`site:cran.na "Paratus"`、`site:cran.na "Network Facilities"`、`site:cran.na "cable landing"`、`"CRAN" "Network Facilities Licence" Namibia`、`"CRAN" "public hearing" "Paratus"`。
- Gazette/登记/采购：`site:namiblii.org/gazettes "data centre" Namibia`、`site:eprocurement.gov.na "data centre"`、`site:mfpe.gov.na "Data Centre"`、`site:gov.na "National Data Centre"`、`site:mict.gov.na "National Data Centre"`、`site:nipdb.com "data centre"`、`"Government Data Centre" Namibia procurement`。
- 行业/媒体：`"Paratus" "Armada" "Brakwater"`、`"Paratus to invest N$123m in data centre"`、`"Telecom Namibia" "Infinitum" "co-location"`、`"Equiano" "Swakopmund" "Paratus"`、`"Telecom Namibia inaugurates Equiano cable landing station"`、`site:namibian.com.na "data centre"`、`site:neweralive.na "data centre"`、`site:economist.com.na "data centre"`、`site:datacenterdynamics.com/en/tags/namibia/`、`filetype:pdf "data centre" Namibia`、`filetype:pdf "Paratus" "Armada"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 地方当局规划/建筑控制（A 级）：Local Authorities Act 1992、Town Planning Ordinance 1954（规划方案/改划/同意用途/偏离/建筑线放宽常在 Government Gazette）、Townships and Division of Land Ordinance 1963。入口：City of Windhoek（https://www.windhoekcc.org.na/，Building Control 页、工程图纸提交页）、Swakopmund 市政（https://swakopmun.com/，Design & Building Division）、Walvis Bay 市政（https://www.walvisbaycc.org.na/）、Legal Assistance Centre Gazette PDF（https://www.lac.org.na/index.php/laws/gazettes/）、NamibLII（https://namiblii.org/gazettes/）、司法部 Gazette 门户（https://moj.gov.na/government-gazzete）。提取：地方当局、议会事项/日期、建筑图号、erf/农场/地块、街道/城镇、地主、申请人、运营商、用途类别/分区、面积、发电机/柴油细节、电力需求、水/冷却、异议、批准条件、完工/入住状态。
- MEFT 环评/ECC（A 级，若来自 MEFT/环境专员/Gazette/政府托管的 EIA 记录）：门户 https://www.meft.gov.na/ 、EIA 门户 https://eia.meft.gov.na/（自动抓取可能超时，用浏览器与搜索引擎缓存）、EIA Tracker（https://eia-tracker.org.na/，C/B 线索，须与 MEFT/Gazette 对证）、Environmental Information Service eLibrary（https://the-eis.com/elibrary/，C/B 线索）。触发词：柴油或危险物质储存、备用发电、太阳能/自发电、输电线路/变电站、电信杆塔/光纤/海缆登陆设施、取水、工业建设、沿海/Dorob 敏感区建设。提取：MEFT 申请/文号、发起人、环评从业者、列项活动、坐标/erf/农场、发电机额定、柴油量、并网、水源、公众参与日期、环境专员决定、上诉/续期/转让状态。
- 电力/电网（A 级）：MME（https://www.mme.gov.na/）、ECB（https://www.ecb.org.na/，Licensing 与 Public Notices）、NamPower（https://www.nampower.com.na/）、Erongo RED（https://erongored.com/）、CENORED（https://cenored.com.na/）、NORED（https://www.nored.com.na/）、Windhoek 市电。区域配电图：Khomas=Windhoek 市电/NamPower；Erongo=Erongo RED；Otjozondjupa/Omaheke/部分 Kunene/Oshikoto=CENORED/NamPower；Oshana/Ohangwena/Omusati/Oshikoto/Kavango East/West=NORED + Oshakati Premier Electric（Oshakati）；Hardap//Karas/Zambezi=逐案核验。提取：申请人、牌照类型/状态、MW/MVA/kVA、电网节点/变电站、RED/地方当局、转供/承购、备用发电、太阳能/IPP 联动、Gazette/听证文号、决定日期。
- CRAN（A 级电信牌照证据，非 DC 证明）：https://www.cran.na/ ，Licensing、Telecommunications Licensees、Public Hearings、Notices、Government Gazettes、Infrastructure Sharing。相关类别：Class ECS、ECNS、Comprehensive ECS/ECNS、Network Facilities、个人牌照、频谱牌照、基建共享公告、海缆登陆/网络设施事项。
- 政府/国家数据中心：存在「Data Centre of the Government」与「National Data Centre」采购/媒体引用，但新国家设施须绑定官方战略计划、预算表决、招标、授标、场地或 Gazette 记录，否则保持 C/B。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场形态：小型运营商主导市场；确认的商业/服务证据集中于 Khomas（Windhoek/Brakwater：Paratus Armada、Telecom Namibia Infinitum colo）与 Erongo（Swakopmund/Walvis Bay：海缆登陆基建、Paratus/Telecom Namibia Equiano 活动）。无官方 AWS/Azure/GCP/Oracle/Huawei 区域页点名纳米比亚；「Namibia cloud region/hyperscale/AI DC」声明在匹配官方提供商/许可/电网/Gazette 记录前视为未核实。
- 已知线索：**Paratus Armada Data Center**（Brakwater/Windhoek, Khomas；A 级 Paratus 页确认服务；B 级 DCD 2022 年 8 月启动、N$123m、Brakwater 园区、DC1/DC2 机房与能源中心；官方后续 = Windhoek/Brakwater 规划、MEFT/EIA、ECB/NamPower/市电连接、CRAN、BIPA）；**Telecom Namibia Infinitum colo**（Windhoek；A 级产品/FAQ 页；DataCenterMap 式「Telecom Namibia Datacenter」仅 C；官方后续 = 年报/招标、CRAN 持牌人列表、Windhoek 建筑/电力记录）；**Swakopmund 海缆登陆/DC 基建**（Erongo；Equiano 2022 年经 Paratus/Telecom Namibia 安排登陆，DCD 报 Telecom Namibia 2024 年启用 Swakopmund Equiano 登陆站；2Africa 官网为系统权威但非 colo 证明；WACS/SARSSy 为补充；记录为 cable landing 除非来源明确客户 colo/DC 服务）；**Government/National Data Centre**（lead 状态，需官方战略/预算/招标/授标/场地）；**MTC/Liquid/银行/企业 ICT 机房**（仅相邻运营商线索，需具名设施、colo 产品、招标、建筑记录或电力/环评证据）。
- 本地媒体（B）：The Namibian、New Era、Namibia Economist、Windhoek Express、Windhoek Observer、Namibian Sun、Informante、NBC News、The Brief、Republikein（data sentrum）、Allgemeine Zeitung（Rechenzentrum）。贸易媒体（B）：DCD（Namibia tag）、Submarine Networks、TechCentral、ITWeb Africa、Developing Telecoms、Capacity Media、TechAfrica News、Mobile Europe。聚合器（C）：DataCenterMap、DataCenters.com、GeoCables Swakopmund、D4D Hub/Xalam 市场简报。
- 行业发现聚焦：① 运营商页与年报；② 覆盖 Paratus/Telecom Namibia/Equiano/WACS/2Africa/SARSSy/光纤路由的贸易媒体；③ 本地商业媒体（建设、建筑图、预算、招标、监管故事）；④ 能源/氢/可再生公告（可能成为算力选址线索）；⑤ 聚合器仅作线索生成。

## 来源分级

- **A**：一手——政府部委/机构、监管机构、市政/地方当局、Government Gazette、官方公司/运营商页、官方云区域页、BIPA 登记。
- **B**：强二手——具名运营商/场地/城镇/日期与项目细节的成熟媒体/贸易源。
- **C**：弱线索——聚合器、社交媒体、咨询幻灯片、无来源公告、含糊的「ICT/数据」引用。
- 陷阱与分级规则：电信牌照 ≠ DC；登陆站 ≠ 客户 colo；不推断超大规模区域；MTC/Liquid/银行/政府 ICT 机房无设施证据不升格；聚合器 C；社交帖 C；Gazette/监管/市政事实优先于媒体时间线。

## 使用流程（探索/复核批次）

1. 读本 SKILL.md 与两份 explorer 报告，确定目标区与候选项。
2. 对每个候选：已知运营商/海缆证据起步 → 市政/建筑控制核实 → MEFT/EIA → ECB/MME/NamPower/RED → CRAN → BIPA → Gazette/采购。
3. 每区跑标准扫描（`"data centre" "{region}"`、`"server room" "{main town}"`、`"building plan" "{main town}" "data"`、`"environmental clearance" "{main town}" "data"`、`"substation" "{main town}" "data centre"`、`"CRAN" "{main town}" "licence"`）。
4. 按去重键去重；设施类型区分 commercial colocation / operator POP / cable landing station / government DC / enterprise-server room / power-telecom-only lead；状态区分 rumour/lead、announced、planning/EIA、permitted、under construction、operational、expansion、decommissioned。
5. 记录每条事实的来源分级与 URL；Gazette/监管/市政事实优先。
6. 遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:11Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] Paratus Armada：A 级市政/EIA/电力记录（Windhoek/Brakwater 规划、MEFT/ECC、ECB/NamPower/市电连接）。
- [ ] Telecom Namibia Infinitum：设施级证据（地址、建筑图/ECC/电力、年报或招标）。
- [ ] Swakopmund：Telecom Namibia Equiano 登陆站启用状态、2Africa 系统状态、CRAN/市政/EIA/NamPower-Erongo RED 记录。
- [ ] 待核实：National/Government Data Centre 的官方战略/预算/招标/授标/场地证据。
