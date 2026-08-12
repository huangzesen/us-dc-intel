---
name: sk-datacenter-methodology
location: scripts/expansion/world/country-skills/SK/SKILL.md
description: |
  Slovakia（SK）数据中心发现以官方/监管管线（市/区官方公告板 uradna tabula 与建设许可、Enviroportal EIA/SEA 与 IPKZ、Slov-Lex 法律、ORSR/Register UZ 法人登记、CRZ 合同、UVO/IS EPVO 采购、地籍 skgeodesy/katasterportal、电信监管 teleoff、MIRRI/NASES/Government Cloud、URSO/SEPS/ZSE/VSE/SSE 电网）和行业/厂商发现（Slovak Telekom、Orange TechPark、SWAN、VNET/DC Digitalis/SHC III/Datapark 48、SITEL POP1/POP2/POPKE、1 Cloud Lab、eServer、NIX.SK/SIX/PeeringDB、HPC 与新闻源）为主线，按 8 个自治州（Banska Bystrica; Bratislava; Kosice; Nitra; Presov; Trnava; Trencin; Zilina）逐州枚举。
  市场小而 Bratislava 中心化（Košice 为次级枢纽）：政府/研究设施（NASES/Government Cloud、SPP 托管国家容量、SAV/PERUN、NSCC/Košice HPC）须与商业托管分开分类；斯洛伐克为内陆国无海缆登陆站；官方页无超大规模公有云区域，Tier 声明须以认证记录为准。
---

# SK · 斯洛伐克数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：按 8 个自治州（Banska Bystrica; Bratislava; Kosice; Nitra; Presov; Trnava; Trencin; Zilina）枚举斯洛伐克数据中心设施与项目。
> 分区模型：8 个 samospravne kraje（VUC/kraje）加 79 个 okresy；manifest 所需 8 分区与 8 州一一对应。
> 已知种子：Slovak Telekom（Bratislava 服务，Košice 为批发线索）、Orange TechPark（Bratislava）、SWAN、VNET（DC Digitalis、SHC III、Datapark 48 在建）、SITEL（POP1/POP2 Bratislava、POPKE Košice）、1 Cloud Lab、eServer（租用 Digitalis）、NASES/Government Cloud（含 SPP 托管第二 DC）、SAV/PERUN 超算、NSCC/Košice 超算计划、Tatra Supercompute/Tatra AI 计划。
> 本 skill 汇总两份探索报告：官方/监管管线见 explorer-official.md，行业/厂商发现见 explorer-industry.md。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：结构事实（8 州/79 区、无全国统一建设许可库、内陆国、Bratislava 重、政府/研究设施分类）、核心斯洛伐克语词表、A 级官方源路由（行政/公告板、EIA/SEA 与 IPKZ、法律基础、公司/合同/采购/地籍、电信/云/电网/政府 IT）、官方核实设施/项目锚点表、逐州官方策略、计数与状态规则、高危陷阱、复查节奏 |
| explorer-industry.md | 行业/厂商发现：市场框架（小而 Bratislava 中心化、Košice 次级、其余六州低密度）、行业核心查询、官方云区域状态表、运营商与设施种子表、行业发现路由（运营商/扩张大项目/协会与 IXP/新闻源）、逐州行业策略、目录与聚合器处理、已知陷阱与质量控制、复查节奏、优先未决线索 |

## 核心结构事实（框定每次搜索）

1. 斯洛伐克为小型、Bratislava 中心化的托管与主机市场：最强集群在 Bratislava（Telekom、Orange TechPark、SWAN、VNET/DC Digitalis/SHC、SITEL、1 Cloud Lab、eServer-in-Digitalis、NASES/GovCloud、SPP、PERUN）；Košice 为次级枢纽（SITEL POPKE 是唯一确认的商业托管锚点）；Trnava/Trencin/Nitra/Zilina/Banska Bystrica/Presov 低密度，主要搜公共部门机房、医院/大学采购、工业企业 IT、灾备与未来 AI 工厂申报。
2. 无全国统一公共建设许可库：建设许可与占用/投运决定通常在市政或区级官方公告板（uradna tabula / verejna vyhlaska），可能仅 PDF 且索引差；文件可能避开 `datove centrum` 而用 `technologicka budova`、`serverovna`、`strojovna chladenia`、`trafostanica`、`nahradny zdroj`、`datova sala` 描述。
3. 斯洛伐克为内陆国：无海缆登陆站；IXP、陆路光缆、网络 PoP、云边缘节点与 peering 点仅作连通性证据，不算数据中心。
4. 政府与研究设施是真实基础设施但须与商业托管分开分类：NASES/Government Cloud（sk.cloud）、SPP 托管的州 DC 容量、SAV/PERUN 超算（2025-12-18 交付 Bratislava，public_HPC_research）、NSCC/Košice 国家超算（MIRRI 计划路线）。
5. 超大规模缺席须每周期在官方页复查：2026-08-12 核对 AWS/Azure/GCP/OCI 官方位置页均无斯洛伐克公有云区域/本地区。
6. 斯洛伐克语词表为核心（datove/dátové centrum、datacentrum、serverovňa、kolokácia/housing、vladny cloud、superpočítač、stavebné povolenie、kolaudačné rozhodnutie、EIA/zisťovacie konanie、IPKZ、rezervovaný výkon、rozvodňa/trafostanica、nahradný zdroj、verejné obstarávanie/zmluva）；带与不带变音符都要搜。
7. 分级按所支持事实：A 官方/一手（部委、市/州、Enviroportal EIA/SEA 或 IPKZ 记录、Slov-Lex 法律页、CRZ 合同、UVO/IS EPVO 通知、ORSR/Register UZ、运营商官方设施页、云官方区域清单、官方机构页、官方电网/电信监管源）；B 强二级（斯洛伐克/国际媒体、政府贸易指南、厂商案例、投资机构文章、未识别许可/精确设施/当前运营的运营商公告）；C 弱线索（目录、市场页、地图、仅 PeeringDB 设施记录、社媒、SEO 页、市场报告、无一手支持的能力声明）。

## 查询模式（复制粘贴模板见 explorer-official.md §1 / explorer-industry.md §3）

- 公告板/建设许可：`site:{municipality-domain} "datove centrum" "stavebne povolenie"`、`site:{municipality-domain} "dátové centrum" "verejná vyhláška"`、`site:{municipality-domain} "datacentrum" "rozhodnutie o stavebnom zámere"`、`site:{municipality-domain} "serverovňa" "kolaudačné rozhodnutie"`、`site:{borough-domain} "{operator}" "stavebné povolenie"`、`filetype:pdf "dátové centrum" "Bratislava" "stavebné povolenie"`、`"{legal_entity}" "úradná tabuľa" "dátové centrum"`。
- EIA/IPKZ：`site:enviroportal.sk/eia-sea "dátové centrum"`、`site:enviroportal.sk "datacentrum" "zisťovacie konanie"`、`site:enviroportal.sk "technologická budova" "UPS"`、`site:enviroportal.sk "{operator}" "dátové centrum"`、`site:enviroportal.sk/ipkz "integrované povolenie" "dieselagregát"`、`"okresný úrad" "{municipality}" "dátové centrum" "EIA"`。
- 采购/合同/法人/地籍：`site:crz.gov.sk "dátové centrum" "{operator}"`、`site:crz.gov.sk "datacentrum" "NASES"`、`site:crz.gov.sk "kolokácia" "server"`、`site:uvo.gov.sk "dátové centrum"`、`site:evo.isepvo.sk "kolokácia"`、`site:orsr.sk "{legal_entity}" "{ICO}"`、`site:registeruz.sk "{legal_entity}"`、`site:skgeodesy.sk "{address}" OR "{parcel}"`。
- 电网/电信/政府 IT：`site:urso.gov.sk "dátové centrum" OR "datacentrum"`、`site:seps.sk "dátové centrum" OR "rezervovaný výkon"`、`site:zse.sk "dátové centrum" "pripojenie"`、`site:vse.sk "dátové centrum" "pripojenie"`、`site:sse.sk "dátové centrum" "pripojenie"`、`"{operator}" "rezervovaný výkon" OR "požadovaný príkon"`、`site:teleoff.gov.sk "{operator}" "dátové centrum"`、`site:mirri.gov.sk "vládny cloud" "dátové centrum"`、`site:nases.gov.sk "dátové centrum" OR "Govnet"`。
- 行业核心：`Slovakia "data center" Bratislava`、`Slovakia datacenter Košice`、`Slovensko "dátové centrum" "kolokácia"`、`"datacentrum" Bratislava operator`、`"serverhousing" Bratislava Slovensko`、`"AI factory" Slovakia "data center"`、`"Tatra Supercompute" OR "Tatra AI"`、`"superpočítač" Bratislava Košice PERUN`。
- 运营商：`"{operator}" "dátové centrum" "Bratislava"`、`"{operator}" "datacentrum" "Košice"`、`"{operator}" "housing" "Slovensko"`、`"{operator}" "virtualne datove centrum"`、`"{operator}" "TIER 3" "Slovakia"`、`"{operator}" "IČO" "dátové centrum"`。
- 扩张/大项目：`"dátové centrum" "postaví" Slovensko`、`"datacentrum" "otvorí" Bratislava OR Košice`、`"AI továreň" Slovensko`、`"Tatra AI" "dátové centrum"`、`"Slovakia" "data center" "MW"`、`"superpočítač" "Košice" "MIRRI"`、`"PERUN" "superpočítač" "SAV"`。
- IXP/协会：`site:nix.sk "Bratislava" "datacentrum"`、`site:six.sk "Košice" OR "Bratislava"`、`site:peeringdb.com "Sitel Bratislava"`、`site:itas.sk "dátové centrum"`、`site:kosiceitvalley.sk "dátové centrum" OR "superpočítač"`。
- 新闻：`site:zive.aktuality.sk "dátové centrum" Slovensko`、`site:trend.sk "datacentrum" OR "dátové centrum"`、`site:forbes.sk "VNET" "dátové centrum"`、`site:hnonline.sk "dátové centrum" "Slovensko"`、`site:datacenterdynamics.com Slovakia "data center"`、`site:trade.gov Slovakia "data center" "Tatra Supercompute"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 行政/公告板路由：8 州官方门户（bratislavskykraj.sk、trnavskykraj.sk、tsk.sk、unsk.sk、zilinskykraj.sk、bbsk.sk、psk.sk、kosickykraj.sk）加主城市门户（bratislava.sk 及各 borough）；先查市政/区公告板取许可；提取申请人、法人/ICO、案号、地块 ID、地籍区、项目名、许可类型、机构、决定日期、发电机/燃油存储/变压器容量、是否仅为楼内机房。
- EIA/SEA 与 IPKZ：Enviroportal（enviroportal.sk/eia-sea、/ipkz、/ipkz/register-prevadzok-a-povoleni）；旧 `/sk/ippc` 路由已过期；大型 AI/HPC/超大规模线索须有 EIA、地方许可、战略投资决定、用地或电网记录才可标 `planned` 超过 B。
- 法律基础：建筑法 2025 年第 25 号（2025-04-01 生效）、EIA 2006 年第 24 号、IPKZ/IPPC 2013 年第 39 号、能源法 2012 年第 251 号、电子通信 2021 年第 452 号、个人数据 2018 年第 18 号、网络安全 2018 年第 69 号、战略投资 2024 年第 142 号（重大计算/DC 园区项目可能相关，但政策页非设施证据，除非点名投资者/地点/项目）。
- 公司/合同/采购/地籍：Obchodny register SR（orsr.sk）、Register uctovnych zavierok（registeruz.sk）、CRZ（crz.gov.sk/zmluvy.gov.sk，DC/云/托管/机房/Govnet 合同）、UVO/IS EPVO（uvo.gov.sk、evo.isepvo.sk）、地籍（skgeodesy.sk、katasterportal.sk、kataster.vugk.sk）；CRZ/UVO 证据 A 证采购或合同，仅当文件识别场地/宿主设施/机房才 A 证物理设施。
- 电信/云/电网/政府 IT：teleoff.gov.sk 电信监管；MIRRI（mirri.gov.sk）信息化/Government Cloud/HPC；NASES（nases.gov.sk）州网络与电子政务运营商；Government Cloud（sk.cloud）；URSO（urso.gov.sk）能源监管；SEPS（seps.sk）输电系统运营商（发展规划与并网语境）；ZSE/VSE/SSE 配电区域；电网事实与设施状态分开记录（requested_connection_MW_or_MVA、connection_point、DSO、grid_status 等）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商种子：Slovak Telekom（官方服务页称 DC 近 Bratislava 中心；批发材料称 Bratislava 与 Košice 均有 DC，Košice 须一手材料证实）；Orange TechPark（官方页描述 1,026+ 平米总面积、680 平米客户厅、housing 与虚拟 DC，Bratislava telecom_colocation/云锚点）；SWAN（官方 DC 服务页，法律席位 Landererova 12）；VNET（DC Digitalis Trnavska cesta 110/B、1,000 平米数据厅、SHC III Namestie hraniciarov、Datapark 48 coming soon 不计运营）；SITEL（POP1/POP2 Bratislava、POPKE Košice，最强中立托管多站点种子）；1 Cloud Lab（2000 年起运营，Bratislava DC/托管/公有云）；eServer（SK 托管位于 Digitalis，不另建设施记录）；WebSupport（托管品牌，Bratislava 办公室，无物理 DC 页，仅提供商线索）。
- HPC/政府：NASES/Government Cloud（government_or_public_sector 类，经 CRZ/MIRRI/NASES 映射组成物理 DC）；NASES 第二 DC 位于 SPP Bratislava DC（2021 年底起，A/B，需 CRZ 合同）；SAV/PERUN（2025-12-18 交付 Bratislava，public_HPC_research）；NSCC/Košice 超算（MIRRI 计划方向 A，媒体技术对比 B）；Tatra Supercompute/Tatra AI（西部斯洛伐克，精确分区未公开，B 级计划线索，无 EIA/许可/用地/电网证据前不计入）。
- IXP/协会：NIX.SK（Bratislava 中立 IX，2015 年起运作，A 证 IXP 存在）；SIX（STU Bratislava 与 Košice 技术大学运营，A 证 IXP 非 DC）；PeeringDB（Sitel Bratislava、Digitalis 等 C/B 种子）；ITAS（协会会员非设施证据）；SAPIE（创新经济/AI 政策线索）；Košice IT Valley（东部集群线索）。
- 目录处理：DataCenterMap、Baxtel、datacenters.com、Cloudscene/OCOLO/Inflect/colomap、PeeringDB 均 C 级种子；升级工作流：捕获名称/声称地址/运营商/城市/容量→搜运营商域→搜公告板/Enviroportal/CRZ/UVO/地籍→搜认证记录→无一手/强二级源则保持 C 并从设施总数排除。
- 陷阱：Datacube/Perpetuus 目录大条目与旧州 DC 报道提及 Devínska Nová Ves 的 Perpetuus 私人 DC，保持线索；eServer 与 Digitalis 不重复计数；Orange TechPark 精确街道/许可/认证另证；Telekom Košice 目录片段不得升 A；IXP/peering 在场不是 DC；超大规模无 SK 区域每季度复查。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| Slovak Telekom 数据中心服务 | Bratislava；Košice 批发线索 | 运营中服务；A（官方服务页 telekom.sk）；个别地址 B/C 直至一手地址证明；Košice 需一手设施证据 |
| Orange Slovensko TechPark | Bratislava | 运营中服务；A（orange.sk 官方设施/服务页，1,026+ 平米/680 平米客户厅）；认证/位置细节需另证（Petržalka 许可、Uptime 证书） |
| SWAN 数据中心 | Bratislava | 运营中服务；A（swan.sk 官方服务页）；物理 DC 场地待确认；搜 CRZ 公共部门托管/云合同 |
| VNET DC Digitalis | Bratislava（Trnavska cesta 110/B） | 运营中；A（vnet.sk/dcdigitalis.sk，1,000 平米数据厅）；确认地籍地块与许可 |
| VNET SHC III | Bratislava（Namestie hraniciarov） | 运营中；A；确认精确门牌/地块 |
| VNET Datapark 48 | Bratislava | coming soon/计划中；A（运营商列出，未运营）；搜 Cernysevskeho/Petržalka 许可与电网，投运证据前不计运营 |
| SITEL POP1 / POP2 | Bratislava | 运营中；A（sitel.sk）；确认地址/许可；PeeringDB fac 465 仅 C/B 支持 |
| SITEL POPKE | Kosice | 运营中；A；唯一确认的 Košice 商业托管锚点；经 Košice 公告板与 VSE 确认 |
| 1 Cloud Lab 数据中心 | Bratislava | 运营中；A（1cloudlab.sk）；验证地址与规格 |
| eServer Bratislava 托管 | Bratislava（位于 Digitalis） | 运营中服务；A（服务）；Tier 声明 C/B；非独立设施 |
| NASES / Government Cloud | Bratislava / 州产业 | 运营中国家云；A（sk.cloud、mirri.gov.sk、nases.gov.sk）；政府/公共部门基础设施，非商业托管 |
| NASES 第二 DC（SPP 场地） | Bratislava | 运营/迁移完成（2021 年底目标后）；A/B（MIRRI 官方）；需 CRZ 合同与 SPP 场地细节 |
| PERUN 超算（SAV/CSČ SAV） | Bratislava | 已交付/安装调试至运营 HPC；A（sav.sk 2025-12-18 交付）；public_HPC_research |
| 国家超算 Košice 组件 | Kosice | 计划/项目路线；A（MIRRI 决策方向）；B（媒体技术对比）；跟踪采购/安装地点/市政许可/VSE |
| Tatra Supercompute / Tatra AI | 西部斯洛伐克，精确分区未公开 | 计划线索；B（官方项目页 tatrasupercompute.com、trade.gov 指南）；无 EIA/许可/用地/电网证据前不计入 |
| AWS/Azure/GCP/OCI 公有云区域 | 无 | 官方位置页无 SK 区域/本地区；A（负向检查）；每季度复查 |

## 更新节奏

- 月度：Tatra Supercompute/Tatra AI、MIRRI、SARIO、经济部战略投资通知、Enviroportal EIA 搜索、斯洛伐克科技/商业媒体。
- 季度：AWS/Azure/GCP/Oracle 官方位置页；NIX.SK/SIX/PeeringDB 设施变化；Uptime 认证搜索。
- 半年：全部 8 州加重点市政公告板扫掠；CRZ/UVO/IS EPVO 搜 `dátové centrum`、`datacentrum`、`serverovňa`、`housing`、`kolokácia`、`vládny cloud`；目录刷新去重。
- 年度：所有计数地址的地籍校验；高负载站点电网语境；目录对一手源去重。
- 优先未决线索：Tatra Supercompute 精确站点/分区/许可/EIA/电网；Telekom Košice 一手设施证据；Datacube/Perpetuus 当前运营商与官方状态；VNET Datapark 48 启动/许可/地址；Orange TechPark 精确地址与认证；SITEL POP1/POP2/POPKE 精确地址与许可/地籍；SWAN 物理场地；WebSupport 物理托管地点；NSCC Košice 机器安装站点与运营状态。
- 待办（2026-08-12）：SK 属 batch-10 已复核国家；后续按本方法论推进 8 州枚举，codex terra agent 分批复核后更新证据分级。
