---
name: nc-datacenter-methodology
location: scripts/expansion/world/country-skills/NC/SKILL.md
description: 新喀里多尼亚数据中心双线查询方法论（官方/监管/电信/电力管线 + 行业/媒体/供应商发现），法文优先检索，含 division 模型、来源分级与查询模板；New Caledonia datacenter dual-line discovery methodology (official/regulatory/telecom/power pipeline + industry/media/vendor discovery), French-first search, with division model, source grading and query templates. 运行 NC 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# NC · 新喀里多尼亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为新喀里多尼亚（Nouvelle-Calédonie, NC）数据中心设施与项目枚举批次提供官方与行业双线方法。官方线（explorer-official.md）覆盖政府/公报/议会、电信监管（gouv.nc、JONC/Juridoc、Autorité de la concurrence NC、ANFR、OPT-NC）、电力（Enercal/EEC-Engie）、海缆（GONDWANA/PICOT）与公共采购（marchespublics.nc）；行业线（explorer-industry.md）覆盖已验证行业种子（DSP、OPT-NC、PITA）、本地媒体（LNC、NC La 1ère、CCI）、全球/区域贸易媒体、法文优先查询词库、供应商/业主转向清单与记录验收规则。中文为主，法/英检索词保留用于检索精度；官方来源仍是接纳权威。

## 入口

| 文件 | 职责 | 内容概要 |
|---|---|---|
| explorer-official.md | 官方/监管/电信/电力 | gouv.nc、JONC/Juridoc（juridoc.gouv.nc）、Congrès（congres.nc）、Haut-commissariat（nouvelle-caledonie.gouv.fr）、三省（province-sud.nc、province-nord.nc、province-iles.nc）、Open Data NC（data.gouv.nc）、ISEE、DITTT/Géorep、OPT-NC（opt.nc/office.opt.nc）、ANFR Outre-mer、Autorité de la concurrence NC、Enercal/EEC-Engie、GONDWANA/PICOT 海缆、marchespublics.nc 采购、云负向基线（AWS/Azure/GCP/OVHcloud） |
| explorer-industry.md | 行业/媒体/供应商 | DSP/Data Services Pacific（dsp.nc、CIPAC 扩展文章）、OPT-NC 历史（CITIUS）、PITA 成员、APNIC/bgp.tools/PeeringDB、DataCenterMap/Inflect 目录、本地媒体（LNC、NC La 1ère、CCI、ADECAL、Technopole、Choose NC）、全球/区域贸易媒体（DCD、Capacity、Submarine Networks、TeleGeography、Telecompaper、BW Group）、法文查询词库、厂商/业主转向清单、枚举矩阵与验收规则 |

## 核心结构事实

1. **Division 模型**：manifest 已核验 `country_code: "NC"`、`subnational_type: "country"`、`divisions: ["New Caledonia"]`。交付覆盖单元为 New Caledonia；3 个省份（Province Sud、Province Nord、Province des Îles Loyauté）与 33 个 communes 仅作内部完整性检查网格，不作 manifest divisions。
2. **行政框架**：新喀里多尼亚是法国 `collectivité sui generis`；官方页面确认 33 communes（Open Data NC 的 communes-nc 数据集可用，并标注 Poya 横跨 Province Nord 与 Province Sud）；国家代表页面确认 3 provinces。
3. **市场体量很小**：NC 没有 AWS/Azure/Google Cloud 本地区域；设施级发现以本地电信/托管、政府 DINUM、银行、矿业工业 IT、教育科研和少量本地服务商为主；任何 MW 级、Tier 级或机柜数声明都必须逐字段分级。
4. **电信监管口径（重要修正）**：不要使用不存在或未验证的 `ARCEP-NC` 作 A 级来源；ANFR 明确说明法国本土 ARCEP 在新喀里多尼亚不具管辖权，电信监管由新喀里多尼亚政府承担；2024 年政府公告显示正通过 Autorité de la concurrence de la Nouvelle-Calédonie 的技术支持预备独立监管任务；实际检索使用 gouv.nc、JONC/Juridoc、Autorité de la concurrence NC、ANFR、OPT-NC 与采购平台。
5. **电力约束**：Enercal 是输电和系统运行核心；配电由 communes 选择 Enercal 或 EEC-Engie；Enercal 官方说明 Grande Terre 公共输电网为 150 kV / 33 kV，输电网由领地所有并委托 Enercal 运营；数据中心的 `grid_mw`、`generator_mw`、`it_mw` 必须分开记录——it_mw 仅限明确 IT load；grid_mw 仅限 raccordement/puissance souscrite/poste source/concession 或 technical filing；generator_mw 是应急柴油/自备电，不等于 IT 容量；矿业电厂、金属冶炼负荷与数据中心候选必须分离。
6. **海缆约束**：OPT-NC 官方资料确认 GONDWANA-1 于 2008 年连接 Nouméa-Sydney（2,152 km）；GONDWANA-2 于 2022 年连接 Nouméa-Suva（1,515 km），并与 PICOT-2 国内光缆（Ouémo、Mont-Dore、Nouville、Île des Pins、Yaté、Maré、Lifou 等）一起增强冗余；PICOT-1 为 2008 年国内光缆（Poindimié 至 Ouvéa 和 Lifou）；landing 精确地址通常不公开，除非 OPT/政府/许可文件明确给出；Hawaiki Nui 等仅作 announced/assessed，除非 OPT-NC 或政府确认 NC 登陆与状态。
7. **设施/项目种子（2026-08 证据状态）**：DSP/Data Services Pacific（dsp.nc 官方站，自称 Nouméa 100% 私有托管公司且有 2 个数据中心——A 存在/运营商主张，容量/地址需确认；CIPAC 2025 文章称 DSP 正在扩展第二个数据中心——B 线索）；OPT-NC（官方电信/海缆/数据中心历史与企业服务，A；历史 CITIUS/OPT datacenter 活动需核实现状）；DINUM/Direction du Numérique et de la Modernisation（gouv.nc 地址在 Ouémo，JONC 组织含 "réseau et datacenter"，DRH PDF 提及 cloud/datacenter 角色，A）；DataCenterMap 列 DSP DC1/DC2 与 OPT-NC DC Nouville（C/B 线索）；Inflect 列 Data Services Pacific DC1 in Nouméa（C/B）；Enercal/EEC-Engie（电网/配电/raccordement/concession 语境，A）；Autorité de la concurrence NC（电信/连接性意见与案卷，A）；APNIC（网络证据 A / 设施证据 C）。
8. **可靠性分级**：A = 官方/一级来源（政府、官方公报、监管/主管机关、运营商官方页、采购公告、官方备案）；B = 强二级或行业来源（成熟媒体、贸易媒体、协会、已验证厂商页）；C = 聚合器、社媒/自出版、弱二级或未验证线索。分级只针对具体事实：运营商标注 "service available in New Caledonia" 或 "Sydney/Australia region serves New Caledonia" 不是本地设施证据。
9. **计数与去重规则**：设施/项目存在性最低要求——1 个 A 来源，或 2 个独立 B 来源加一个本地官方线索；位置必须落到 New Caledonia 并尽可能落到省/commune（只有 "Nouméa" 或 "Ouémo/Nouville/Magenta" 时如实记录该粒度）；运营主体用官方法律名称（RCS Nouméa、RIDET、APNIC org、采购中标方）；状态与存在性分开赋值；容量字段（surface_m2、rack_count、it_mw、grid_mw、generator_mw、contracted_power、marketing_capacity、actual_consumption）永不折叠成单一 "MW" 数字；`data center` 短语可能指真正的 colocation 设施，也可能指政府 server room——只计数有设施级证据的记录（具名运营商、物理地点/commune、服务或许可证据、状态、来源 URL）；全球大型 colocation/hyperscale 品牌（Sydney、Melbourne、Auckland、Singapore、法国本土区域）除非有具体 NC 设施备案，否则作为负面/远程证据；历史 CITIUS/OPT datacenter 引用须与当前 OPT/DSP/DINUM 证据对账以避免对合并或退役资产重复计数。

## 常用查询模板

```text
site:gouv.nc (datacenter OR "centre de données" OR "centre informatique" OR "salle informatique" OR DINUM)
site:juridoc.gouv.nc (datacenter OR "centre de données" OR "centre informatique" OR "salle informatique" OR "réseau et datacenter")
site:congres.nc (datacenter OR "centre de données" OR télécommunications OR numérique OR énergie)
site:nouvelle-caledonie.gouv.fr (télécommunications OR radiocommunications OR ANFR OR "Nouvelle-Calédonie")
site:data.gouv.nc (datacenter OR DINUM OR "fibre optique" OR "avis de vacances de poste")
site:office.opt.nc (datacenter OR "centre de données" OR hébergement OR CITIUS OR "salle informatique" OR cloud)
site:opt.nc (hébergement OR cloud OR entreprise OR "fibre optique")
site:autorite-concurrence.nc (OPT OR Offratel OR Citius OR SCCI OR télécommunications OR connectivité)
site:anfr.fr/outre-mer "Nouvelle-Calédonie" télécommunications ARCEP
site:enercal.nc (datacenter OR "centre de données" OR raccordement OR "poste source" OR MW OR "client direct")
site:enercal.nc ("poste HTB/HTA" OR "150 kV" OR "33 kV" OR "carte de l'électricité")
site:eec-engie.nc (raccordement OR "puissance souscrite" OR "Nouméa")
site:marchespublics.nc (datacenter OR "centre de données" OR "salle informatique" OR hébergement OR infogérance OR cloud OR cybersécurité)
site:marchespublics.nc ("réseau et datacenter" OR "infrastructures numériques" OR DINUM OR "cloud interne")
site:marchespublics.province-nord.nc (hébergement OR "salle informatique" OR cybersécurité OR "système d'information")
site:office.opt.nc Gondwana PICOT "câble sous-marin"
site:office.opt.nc "GONDWANA-2" "PICOT-2" "mise en service"
"Gondwana-1" "Nouméa" Sydney "ready for service"
"centre de données" "Nouvelle-Calédonie"
datacenter Nouméa (hébergement OR colocation OR cloud OR "salle informatique")
"permis de construire" ("centre de données" OR datacenter OR "salle informatique") "Nouvelle-Calédonie"
"enquête publique" (datacenter OR "centre de données" OR "groupe électrogène")
"appel d'offres" (datacenter OR hébergement OR "système d'information" OR "infrastructures numériques")
"groupe électrogène" (datacenter OR "salle informatique" OR "centre de données") Nouméa
"puissance souscrite" (DSP OR DINUM OR OPT-NC OR datacenter)
"{commune}" ("centre de données" OR datacenter OR "salle serveurs" OR hébergement) "Nouvelle-Calédonie"
"{entity}" (datacenter OR "data center" OR "centre de données" OR "salle informatique") "Nouvelle-Calédonie"
site:datacenterdynamics.com ("New Caledonia" OR "Nouvelle-Calédonie" OR Hawaiki OR Gondwana)
site:submarinenetworks.com (Gondwana OR "New Caledonia" OR "Nouvelle-Calédonie")
site:lnc.nc (datacenter OR "data center" OR "centre de données" OR "câble sous-marin" OR "fibre optique")
"Data Services Pacific" "Nouvelle-Calédonie"
"DSP" "data center" Nouméa
```

## 官方/监管/电信/电力管线要点（详见 explorer-official.md）

- **政府、法律、公报、行政边界**：gouv.nc（政府公告、DINUM、数字化、能源、电信政策）、juridoc.gouv.nc（JONC Journal officiel、公报 PDF、法律/决议/arrêté）、congres.nc（议会审议、能源/电信/预算/特许经营决议）、nouvelle-caledonie.gouv.fr（国家代表、ANFR/无线电、电信国家侧页面、公共调查线索）、三省网站（环境、urbanisme、土地、经济项目、矿产、能源、marchés publics）、data.gouv.nc（communes、fibre deployment、DRH/DINUM job PDFs、采购统计）、ISEE（人口/经济基准，非设施级）、dittt.gouv.nc（地理、基础设施、地籍/GIS 背景）。
- **电信与政府监管**：OPT-NC 商业站（opt.nc，legal mentions 给 EPIC、RCS Nouméa、Nouméa 地址）与公司/新闻站（office.opt.nc，年报、董事会材料、Gondwana/PICOT 新闻、ASN 合同公告）为 A；gouv.nc 查电信监管与独立监管预备公告；ANFR Outre-mer 页面确认 ARCEP 不管辖 NC、监管由 NC 政府承担；Autorité de la concurrence NC（2024 connectivity opinion、市场结构/竞争材料）；APNIC Whois 查 AS/RIR 分配（网络存在事实，非设施事实）；`arcep.nc` 不作来源使用；www.arcep.fr 可作法国 ARCEP 背景，但对 NC 设施/运营商监管不是直接 A 源；运营商/ISP 清册从政府、JONC、Autorité de la concurrence、OPT-NC、ANFR 和 APNIC/BGP 交叉获得。
- **电力**：Enercal（生产、输电、配电、postes sources、网络图、年报）、Enercal network 页（150 kV/33 kV、孤立系统、私有网络）、system operation 页（raccordement、系统运行、输电发展）、distribution 页（communes 选择 Enercal/EEC-Engie）、EEC-Engie（选定 communes 的配电特许与客户/电力语境）；电力提取规则：it_mw/grid_mw/generator_mw 分开，矿业只作工业 IT 和供电线索。
- **海缆与 landing 证据**：GONDWANA-1（OPT 说 2008 部署、2,152 km、Nouméa-Sydney，A 路由/年份 + B 独立印证）、PICOT-1（2008 国内光缆，Poindimié 至 Ouvéa/Lifou，A）、GONDWANA-2（2022、1,515 km、Nouméa-Suva，A）、PICOT-2（经 Ouémo、Mont-Dore、Nouville、Île des Pins、Yaté、Maré、Lifou 的国内链路，A）、Hawaiki Nui/其他分支（仅 announced/assessed，B/C 直到官方确认）。
- **公共采购**：marchespublics.nc（统一采购平台，新版自 2022-12-15 上线）、portail.marchespublics.nc（实时跟踪入口，如重定向以 marchespublics.nc 为准）、marchespublics.province-nord.nc（Province Nord 采购室）、PLACE（www.marches-publics.gouv.fr 法国国家采购，仅用于 Haut-commissariat/国家服务项目，不替代 NC 平台）。
- **云负向基线**：AWS/Azure/GCP 官方区域页无 NC 区域（最近实用区域为澳大利亚/新西兰）；OVHcloud 官方数据中心页无 NC datacenter；"service available in New Caledonia" 或 "Sydney/Australia region serves New Caledonia" 不是本地设施证据。
- **覆盖矩阵**：manifest division 覆盖要求为 New Caledonia 一行；内部完整性扫描按 Province Sud（Nouméa、Dumbéa、Le Mont-Dore、Païta 等，人口/经济中心、政府/DINUM、OPT/DSP、银行、海缆登陆、主电网）、Province Nord（Koné、Voh、Pouembout 等，矿业/工业 IT、KNS/Vavouto 语境、东海岸与北部电信站点）、Province des Îles Loyauté（Lifou、Maré、Ouvéa、Tiga，国内光缆登陆、自治能源系统、电信接入点）；只有出现实体/项目信号后才跑完整 commune 扫描，多数 communes 除接入网设备外没有设施。
- **接纳、分级与字段规则**：存在性 1A 或 2B+本地官方线索；位置落到 NC 并尽量省/commune；运营商/法律实体用官方法律名称；状态模型：lead → announced → under review → permitted → under construction → operational → expansion → retired/merged（保留历史但不对重复计数）；容量字段永不折叠。
- **推荐执行顺序**：①确认 manifest division（New Caledonia 一行）②建官方种子（gouv.nc、juridoc、congres、三省、data.gouv.nc、marchespublics.nc）③建电信种子（OPT-NC、CITIUS 历史备案、DINUM、Autorité de la concurrence、ANFR、APNIC/BGP）④建电力/海缆语境（Enercal、EEC-Engie、GONDWANA/PICOT 登陆与路由证据）⑤有信号后跑完整 commune 扫描 ⑥仅当来源分级、状态、业主、位置与容量字段分别得到支持时才升级记录。

## 行业/媒体/供应商发现要点（详见 explorer-industry.md）

- **已验证行业种子**：DSP/Data Services Pacific（dsp.nc 官方站——最强私有种子，自称 Nouméa 100% 私有托管公司、2 个数据中心；A 存在/运营商主张、B 营销语言、容量/地址需确认）；CIPAC 2025 文章（DSP 正在扩展第二个数据中心，B 线索）；DataCenterMap（列 DSP DC1/DC2 与 OPT-NC DC Nouville，C/B 线索，谨慎抓取并交叉核对）；Inflect（列 Data Services Pacific DC1 in Nouméa，C/B）；OPT-NC（官方电信/海缆/数据中心历史与企业服务，A）；Autorité de la concurrence NC（案卷提及 OPT、Offratel、CITIUS 与连接性市场结构，A 法律/市场事实）；PITA（成员名单含 OPT-NC，B 协会/成员线索）；APNIC（网络证据 A、设施证据 C）；bgp.tools/PeeringDB（B/C，永不单独作设施接纳）。DSP 检索词：`DSP`、`Data Services Pacific`、`Le Cube`、`210 rue Gervolino`、`34 rue du général Gallieni`、`Nouméa`、`Magenta`。
- **本地媒体与经济来源**：LNC（les Nouvelles Calédoniennes，电信/海缆/能源/商业项目，B）、NC La 1ère（公共服务新闻、社会/经济语境，B）、CCI NC（企业目录、本地 IT 公司、经济杂志 PDF，B）、ADECAL（投资/经济发展线索，B）、Technopole NC（创新与数字生态线索，B）、Choose New Caledonia（投资促进、电信/经济背景，B）、LinkedIn/Facebook/公司社媒（招聘、照片、扩展暗示，C 除非官方公司账号并交叉核验）。
- **全球/区域贸易媒体**：DCD（太平洋数据中心/海缆公告、Hawaiki Nui 语境，B）、Capacity Media（海缆与运营商市场，B）、Submarine Cable Networks（海缆系统与登陆路由，B）、TeleGeography Submarine Cable Map（海缆图、RFS、登陆点，A/B 路由证据）、Telecompaper（电信/海缆公告，B）、BW Group/BW Digital（Hawaiki Nui 业主/开发商公告——业主公告 A；NC 设施除非确认 NC 登陆否则 B/C）。
- **法文优先查询词库**：设施与服务（"centre de données" "Nouvelle-Calédonie"、datacenter Nouméa hébergement/colocation/cloud/"salle informatique"、"hébergement de données"、"salle serveurs" banque/administration/université/mine、"centre informatique" OPT-NC/DINUM/DSP）；生命周期/状态（permis de construire、enquête publique、appel d'offres、mise en service、extension）；电力/冷却（groupe électrogène、onduleurs、climatisation、puissance souscrite、poste source）；网络/海缆（câble sous-marin atterrage/atterrissement/débarquement、GONDWANA-1/2、PICOT-2、station d'atterrissement）。
- **厂商/业主转向清单**：电信/在位者（OPT-NC、OPT、Office des Postes et Télécommunications de Nouvelle-Calédonie、Helia by OPT-NC、CITIUS、Offratel）；私有托管（DSP、Data Services Pacific、Le Cube、Nouméa data center、Magenta data center）；政府（DINUM、Direction du Numérique et de la Modernisation、Amadéo、Service des infrastructures numériques、section réseau et datacenter）；金融（BCAL、BNP Paribas NC、Société Générale Calédonienne de Banque、Banque de Nouvelle-Calédonie）；矿业/工业（SLN、ERAMET、Koniambo Nickel SAS/KNS、Prony Resources NC、Goro、Doniambo、Vavouto）；教育/科研（UNC、IRD NC、CRESICA）；电力（Enercal、EEC-Engie、poste source、raccordement、puissance souscrite）。
- **枚举矩阵**：运营商官方页（A/B，服务存在性/业主主张，容量另验）；采购（A，政府/受监管项目强）；JONC/Juridoc/Congrès（A，状态与法律业主强）；省/commune 记录（A，最强的本地位置/状态证据）；Enercal/EEC（A，MW 声明必需）；本地媒体（B，除非与 A 源配对否则是线索）；贸易媒体（B，海缆路由可支持官方证据）；行业协会（B，实体种子）；APNIC/BGP/PeeringDB（A/B 网络、C 设施，永不足以单独计数）；聚合器（C/B，确认前只作线索）；社媒/招聘（C，仅线索）。
- **记录验收与分级**：存在性——A 官方业主页具名/采购/许可/JONC 记录/政府备案；B 成熟媒体或协会具名；C 聚合器/抓取/社媒/无来源报告。容量——A 许可/能源/raccordement 文档/技术附录/官方规格表；B 运营商手册或信誉贸易文章；C 聚合器值/销售数据库/无来源估计。状态——尽量用确切日期；operational 需要当前服务/官方列表或等效运营证据；expansion 保留基础设施状态并单独分级扩展证据；历史 CITIUS/OPT 引用与当前 OPT/DSP/DINUM 证据对账。必需字段：name、operator、legal_entity、status、status_date、province、commune、address_or_area、source_urls、evidence_grade_existence、evidence_grade_capacity、it_mw、grid_mw、generator_mw、rack_count、notes。
- **快速优先顺序**：①dsp.nc 加 DSP 手册/下载，然后通过许可、采购或本地记录验证 DSP DC1/DC2 地址与扩展 ②office.opt.nc 年报与董事会 PDF 查 CITIUS/OPT 数据中心历史并对账现状 ③gouv.nc/data.gouv.nc/JONC 查 DINUM "réseau et datacenter"、云/内部基础设施与 Ouémo 引用 ④marchespublics.nc 与省采购室查托管、云、网安、基础设施、UPS/发电机/冷却招标 ⑤Enercal/EEC 查任何电力或 MW 字段 ⑥海缆路由扫描（OPT GONDWANA/PICOT 优先，TeleGeography/SCN/DCD 其次）⑦本地媒体与社媒/招聘仅用于发现名称、日期与术语。

## 维护注意（更新纪律）

- **更新节奏**：批次运行时以检索当日为准更新证据日期与状态；每次做时效性结论前重查云负向基线（AWS/Azure/GCP/OVHcloud 官方页）；Hawaiki Nui 等海缆在官方确认前保持 announced/assessed。
- **来源核验**：B/C 线索提升前必须查官方页、JONC/Juridoc、采购、Enercal/EEC 或业主备案；存在性与容量/状态分开分级；历史 CITIUS/OPT 记录与当前证据对账防重复计数。
- **不删除纪律**：本目录只新增/更新 SKILL.md、ANATOMY.md 与探索产物，禁止删除/移动任何现有文件（explorer-official.md、explorer-industry.md 与历史证据保留为原始记录）。
