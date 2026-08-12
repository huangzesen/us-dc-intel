---
name: pf-datacenter-methodology
location: scripts/expansion/world/country-skills/PF/SKILL.md
description: 法属波利尼西亚数据中心双线查询方法论（官方/监管管线 + 行业/媒体/厂商发现），小型已确认市场（TNF + TDF Pic Rouge），法语优先检索，含 division 模型、来源分级与查询模板；French Polynesia datacenter dual-line discovery methodology (official/regulatory pipeline + industry/media/vendor discovery), a confirmed small market (TNF + TDF Pic Rouge), French-first search, with division model, source grading and query templates. 运行 PF 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# PF · 法属波利尼西亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为法属波利尼西亚（French Polynesia / Polynésie française, PF）数据中心枚举批次提供官方与行业双线方法。官方线（explorer-official.md）覆盖政府门户与法律文本、电信与频率监管（ANFR/APC/ARN）、数据保护与政府 IT、官方设施与运营商（TNF、TDF Pic Rouge、Vini/ONATi）、海缆/登陆站/卫星连接性资产、电力（EDT）、政府采购（Te Ariari）、建筑许可/土地/环评与分区级查询模板；行业线（explorer-industry.md）覆盖行业媒体与贸易新闻、运营商/设施/厂商、云区域与超大规模负向控制、法语查询模板、塔希提语/地名变体、枚举矩阵、分级规则与推荐流程。保持规则：行业源用于发现与佐证，最终设施存在/地址/状态尽量回挂官方或法定来源。

## 入口

| 文件 | 职责 | 内容概要 |
|---|---|---|
| explorer-official.md | 官方/监管管线 | 政府门户（presidence.pf、service-public.pf）、Lexpol/JOPF、Légifrance、ISPF、Haut-Commissariat、电信与频率监管（ANFR PF、Code des postes et télécommunications de PF、Loi du pays 2011-29、APC、ARN/Service des postes 线索）、数据保护与政府 IT（RGPD 2019-06-01、DSI/SIPF、CNIL）、TNF/Tahiti Nui Telecom/Groupe OPT、TDF Pic Rouge、Vini/ONATi、海缆（Honotua/NATITUA/Manatua/Google Honomoana-Tabua/MANAIA）、电力（EDT）、政府采购（Te Ariari/PLACE）、建筑许可/土地/环评、分区查询模板与负面控制 |
| explorer-industry.md | 行业/媒体/厂商发现 | 行业媒体（Tahiti Infos、TNTV、Polynésie La 1ère、La Dépêche、RNZ Pacific、DCD、AFD、Submarine Networks/TeleGeography、Baxtel/DataCenterMap）、运营商/设施/厂商（TNF、TDF、Banque de Polynésie/Axians、DSI/SIPF、EDT、ASN/NEC/Google/AFD、Schneider/Vertiv/Caterpillar/Cummins）、云区域负向控制、法语查询模板、塔希提语/地名变体、枚举矩阵、按事实分级规则与 PF 特有陷阱 |

## 核心结构事实

1. **Division 模型**：manifest 已核验 `country_code:"PF"`、`country_name:"French Polynesia"`、`subnational_type:"country"`、`divisions:["French Polynesia"]`。仅 1 个分区 French Polynesia；岛屿组/市镇仅作地理细化层，不改变 manifest division；不要为群岛创建额外 manifest divisions。
2. **市场基线判断（明确结论）**：法属波利尼西亚不是“无市场”。截至 2026-08，可确认至少 2 个本地数据中心/托管设施线索：①**Tahiti Nui Fortress (TNF)**——Tahiti Nui Telecom（Groupe OPT 体系）品牌，官方页称其为法属波利尼西亚首个 Data Center，提供 cloud、dedicated servers、security 与 colocation/baie/salle informatique 托管；官方法律声明给出 Tahiti Nui Telecom SAS、RCS Papeete、Papenoo PK 16.7 侧山地址。分类 `operator_colo`，存在/服务/地址为 **A**；容量、实际机柜数、PUE、MW 若非官方规格页给出则降 **B/C**。②**TDF Pic Rouge / Papeete data center**——TDF 官方 2025-09-18 新闻宣布在 Papeete 上方 Pic Rouge 开放数据中心，2025-06 交付，首批客户包括 Banque de Polynésie 与 Axians Polynésie，2026 有扩容计划，合规审计验证 Tier III level。分类 `commercial_colo` 或 `operator_colo`，存在/地点/状态为 **A**；TNTV/DCD 对容量、投资额、扩容到约 40 baies 等描述为 **B**。市场结论应写为**“小型已确认市场 / confirmed small market”**。
3. **资产分类规则**：候选对象先分类再入册——`commercial_colo` / `operator_colo` / `government_hosting` / `cable_landing_station` / `telecom_exchange` / `hyperscaler_ict_facility` / `enterprise_server_room`；只有 commercial_colo 与 operator_colo 计入 DC 市场；海缆登陆站和卫星站不得单独升级为 DC。邻近资产：Honotua、NATITUA、Manatua、Google Honomoana/Tabua 等海缆登陆设施、卫星地面站、OneWeb/Galileo 站点、电信 POP、电力设施；公有云区域：AWS/Azure/GCP/OCI 官方区域列表未显示 PF 区域；Google 在 PF 的资产是海缆/登陆基础设施，不是 GCP region。
4. **法律与监管（关键纠偏）**：不存在可用的 `www.arcep.pf` 官方入口（实测不解析）；ANFR 的 PF 页面明确说明法国 CPCE 原则上不适用于 PF，**ARCEP 不主管该领地**；PF 对电信有本地权限，同时国家保留无线电频率等权限，ANFR 在 PF 有法定角色；本地电信授权与规则应回到 **Code des postes et télécommunications de Polynésie française**、Lexpol/JOPF、政府/部长会公告、历史上的 Service des postes et télécommunications / Agence de réglementation du numérique（ARN）线索，以及竞争机构 APC 的正式意见（其 2024 电信外部连接意见确认 TNF 所在 Papenoo 站点承载 data center、Honotua、Galileo、OneWeb 等敏感基础设施线索）；Loi du pays n° 2011-29 确认公共电信网络和服务需按 PF 法律授权。数据保护：RGPD 自 2019-06-01 起适用于 PF，DSI/SIPF 负责行政数字基础设施与服务；不要把草案中的 “Commission Polynésienne de la Protection des Données Personnelles (CPPDP)” 当作已验证机构，默认使用 CNIL + PF DSI/SIPF。
5. **设施/项目种子（2026-08 证据状态）**：TNF（operator_colo，A 存在/服务/地址；官方称 Tier3+ 或高安全等级可记为官方声明，如需标准化为 Uptime/TIA/EN 认证必须找到证书或审计机构证据，否则不要写成认证事实）；TDF Pic Rouge（A 存在/地点/状态，Tier III level 合规审计可作 A 级官方声明；TNTV/DCD “约 40 baies”“90 million F CFP” 等细节为 B）；TNF/TDF 站点同时包含海缆登陆、卫星、Galileo/OneWeb 等基础设施——邻近资产，不自动等于可销售 DC 容量。
6. **电力**：Électricité de Tahiti（EDT，edt.pf）为电力一手来源；ISPF 与政府能源页用于电力、发电结构、价格和需求上下文；设施一手页（TNF/TDF 对绿色能源、光伏、热回收、冗余供电的声明）用于佐证；电力来源只证明电力上下文，不证明 DC 设施；新项目搜索 `poste source`、`ligne HT`、`groupe électrogène`、`alimentation électrique`、`photovoltaïque`、`MW`、`Tier III`、`climatisation`。
7. **语言与词汇**：法语优先检索；核心词汇——数据中心：`centre de données`、`datacenter`、`data center`、`centre informatique`、`salle serveurs`、`salle informatique`；托管/云：`hébergement`、`hébergement de données`、`colocation`、`baie`、`cloud`、`serveur dédié`、`infogérance`、`externalisation`；状态：`livré`、`ouvert`、`inauguré`、`mis en service`、`opérationnel`、`extension prévue`、`en construction`；海缆/网络：`câble sous-marin`、`station d'atterrissement`、`point d'atterrissement`、`fibre optique`、`liaison hertzienne`、`station terrienne`；电力/设施：`poste source`、`ligne haute tension`、`groupe électrogène`、`climatisation`、`détection incendie`、`extinction incendie`、`photovoltaïque`；许可/采购：`permis de construire`、`certificat d'urbanisme`、`étude d'impact`、`enquête publique`、`appel d'offres`、`marché public`、`avis d'attribution`；英文与塔希提语只补发现（Pape'ete、Papeno'o、Fa'a'ā、Mo'orea、Ra'iātea、Porapora 等地名变体）。
8. **可靠性分级**：A = 一手/法定责任来源（政府与 Service Public 页面、Lexpol/JOPF、Légifrance 扩展至 PF 的法律文本、ANFR 关于 PF 频率/电信权限说明、APC 意见、OPT/Tahiti Nui Telecom/TNF/Vini/TDF 官方页、EDT 官方页、Google Cloud 官方海缆博客、官方采购平台 Te Ariari、ISPF 官方统计、RCS/企业官方法律声明）；B = 较强二手来源（署名本地/区域/行业媒体 Tahiti Infos、TNTV、Polynésie La 1ère、La Dépêche de Tahiti、RNZ Pacific、DCD 等、AFD 项目页、TeleGeography 报告文本、设备/EPC 厂商新闻稿）；C = 弱线索（Baxtel/DataCenterMap/DataCenters.com、海缆地图聚合站、SEO 主机页、离岸 VPS/VPN 营销、社交媒体、无来源目录、只描述 MoU/剪彩且无技术/采购/业主细节的报道）。按事实分级：主体存在（官方页/法律声明 = A；媒体 = B；目录 = C）；设施存在（业主官方 datacenter page/opening release = A；媒体探访/报道 = B；目录 = C）；地址/边界（官方 contact/legal/许可/环评 = A；媒体地标 = B；目录坐标 = C）；容量 MW/机柜/baies（官方规格/合同/环评 = A；TNTV/DCD 等采访 = B；Baxtel/DCM 锁库或估算 = C）；状态（官方 opened/delivered/RFS = A；媒体 inaugurated = B；planned/MoU = C）；认证/Tier（证书或审计报告 = A；TDF 官方 “Tier III level” 合规审计可作 A 级官方声明；TNF “Tier3+” 若无证书只写 claimed）。
9. **计数与去重规则**：状态语义——`announced`/MoU = 计划线索；`delivered`/`inaugurated`/`opened` = 可记 operational 但需注明来源日期；`extension planned` = 与现有运营容量分开记录；海缆 RFS 与云区域无关，Google cable landing 不等于 Google Cloud region；旧结论已过时——2025 TDF Pic Rouge 之后，PF 不能再写成“无商用数据中心市场”；ARCEP PF 假阳性——不要使用 arcep.pf，法国 ARCEP 也不直接监管 PF 电信市场；NATITUA 误分类——NATITUA 是 Tuamotu/Marquesas 外岛连接项目，不是 Tahiti-Hawaii（Tahiti-Hawaii 是 Honotua 国际段）；Papenoo 多资产混合——TNF data center、Honotua landing、satellite teleport、Galileo/OneWeb 都可能同场域，必须拆资产；目录容量膨胀——Baxtel/DCM 可发现 TDF/TNF，但 MW/机柜数需降级或回证；Google cable ≠ cloud region；官方语言与拼写——法语搜索优先，英文和塔希提语只补发现；单个企业机房默认 `enterprise_server_room`，不计商用 DC。

## 常用查询模板

```text
site:presidence.pf ("centre de données" OR datacenter OR "data center" OR "salle serveurs" OR hébergement)
site:service-public.pf ("centre de données" OR datacenter OR "Tahiti Nui Fortress" OR "TDF" OR "Pic Rouge")
site:lexpol.cloud.pf ("centre de données" OR datacenter OR "salle serveurs" OR "hébergement de données")
site:legifrance.gouv.fr "Polynésie française" ("télécommunications" OR "code des postes" OR "données personnelles")
site:ispf.pf (électricité OR énergie OR télécommunications OR numérique)
site:polynesie-francaise.pref.gouv.fr (numérique OR "câble sous-marin" OR datacenter OR "centre de données")
site:anfr.fr/outre-mer/polynesie-francaise (télécommunications OR fréquences OR ARCEP OR ANFR)
site:autorite-concurrence.pf ("télécommunications extérieures" OR "Tahiti Nui Telecom" OR "data center")
site:service-public.pf/dsi (RGPD OR "données personnelles" OR "marchés publics" OR hébergement OR "centre de données")
site:tnfortress.pf (datacenter OR "Data Center" OR colocation OR "baie" OR "salle informatique")
site:tnfortress.pf (cloud OR "serveurs dédiés" OR firewall OR "réseaux")
site:tnfortress.pf ("PK16,7" OR Papenoo OR "Tahiti Nui Telecom" OR RCS)
site:tahitinuitelecom.pf (datacenter OR "Tahiti Nui Fortress" OR cloud OR Papenoo)
site:groupe.opt.pf ("Tahiti Nui Fortress" OR datacenter OR "centre de données")
site:tdf.fr Papeete ("data center" OR datacenter OR "centre de données" OR "Pic Rouge")
"TDF" "Pic Rouge" "Papeete" ("data center" OR datacenter OR "centre de données" OR "baies")
site:onati.pf (datacenter OR "centre de données" OR cloud OR hébergement OR colocation)
site:vini.pf (datacenter OR "centre de données" OR cloud OR "salle serveurs")
site:groupe.opt.pf (Honotua OR NATITUA OR Manatua OR MANAIA OR "câble sous-marin")
site:afd.fr Natitua "French Polynesia" OR "Polynésie française"
site:cloud.google.com/blog/products/infrastructure (Honomoana OR Tabua OR Bulikula OR Halaihai) "French Polynesia"
site:edt.pf (datacenter OR "centre de données" OR "poste source" OR "ligne HT" OR MW)
site:service-public.pf/marchespublics (datacenter OR "centre de données" OR "salle serveurs" OR hébergement OR cloud)
site:ecole.teariari.gov.pf (datacenter OR "centre de données" OR "salle serveurs" OR hébergement OR cloud)
site:lexpol.cloud.pf ("appel d'offres" OR "marché public" OR "avis d'attribution") (datacenter OR "centre de données" OR "salle serveurs")
site:marches-publics.gouv.fr "Polynésie française" (datacenter OR "centre de données" OR "salle serveurs" OR hébergement)
"Papenoo" "PK16,7" ("Tahiti Nui Fortress" OR "Tahiti Nui Telecom" OR datacenter)
"Pic Rouge" Papeete TDF ("permis de construire" OR "travaux" OR datacenter)
"French Polynesia" ("data center" OR "data centre" OR datacenter OR colocation)
"Polynésie française" ("centre de données" OR datacenter OR "salle serveurs" OR hébergement)
"Tahiti" ("data center" OR "centre de données" OR colocation OR "salle informatique")
"Tahiti Nui Fortress" (datacenter OR cloud OR colocation OR "baie" OR "Tier3+" OR "Tier 3")
"TDF" "Polynésie française" ("data center" OR "Pic Rouge" OR "Tier III" OR "photovoltaïque")
site:tntvnews.pf ("data center" OR datacenter OR "centre de données" OR "Pic Rouge" OR "Tahiti Nui Fortress")
site:tahiti-infos.com ("data center" OR datacenter OR "centre de données" OR "Tahiti Nui Fortress")
site:la1ere.francetvinfo.fr/polynesie ("data center" OR datacenter OR "centre de données" OR "Pic Rouge")
site:ladepeche.pf (datacenter OR "centre de données" OR "câble sous-marin")
"French Polynesia" ("cloud region" OR "availability zone" OR "edge location")
site:aws.amazon.com "French Polynesia" "Region"
site:azure.microsoft.com "French Polynesia" "Region"
site:cloud.google.com/about/locations "French Polynesia"
"Tahiti" colocation (Equinix OR NTT OR "Digital Realty" OR Interxion)
"Polynésie française" "étude d'impact" (datacenter OR "centre de données" OR "salle serveurs")
"{commune}" "permis de construire" (datacenter OR "centre de données" OR "salle informatique")
"Honotua" OR "NATITUA" OR "Manatua" OR "Honomoana" OR "Tabua" atterrissement
"Pape'ete" OR Papeete (datacenter OR "centre de données" OR "Pic Rouge")
Papenoo OR "Papeno'o" ("Tahiti Nui Fortress" OR "Tahiti Nui Telecom" OR datacenter)
```

## 官方/监管管线要点（详见 explorer-official.md）

- **政府门户、法律文本、统计**：presidence.pf、service-public.pf、Lexpol/JOPF（lexpol.cloud.pf，www.lexpol.pf 可作发现变体但运行时以可解析域为准）、ISPF（只作人口/电力/经济/企业环境上下文，不单独证明设施存在）、Haut-Commissariat（polynesie-francaise.pref.gouv.fr，法国国家在 PF 的权限与项目背景，尤其频率、国家安全、海缆、国家出资项目）、Légifrance（legifrance.gouv.fr，A 级法律文本源，用于确认电信授权、建设许可、预算、公共采购、数据保护扩展、政府职责）。
- **电信监管与频率（不要使用不存在的 ARCEP PF）**：不存在可用的 www.arcep.pf 官方入口；ANFR 的 PF 页面明确 ARCEP 不主管该领地，PF 对电信有本地权限、国家保留无线电频率权限、ANFR 在 PF 有法定角色；本地电信授权与规则回到 Code des postes et télécommunications de PF、Lexpol/JOPF、政府/部长会公告、历史 Service des postes et télécommunications / ARN 线索与 APC 正式意见；Loi du pays n° 2011-29 确认公共电信网络和服务需按 PF 法律授权。
- **数据保护与政府 IT**：RGPD 自 2019-06-01 起适用 PF；DSI/SIPF 负责行政数字基础设施与服务；不要使用草案中的 CPPDP，默认 CNIL + PF DSI/SIPF。
- **官方设施与运营商**：TNF 官方 datacenter/service/contact/legal pages 可确认 operator_colo 存在、服务类型、品牌、法人、Papenoo PK 16.7 地址（A）；官方称 Tier3+ 或高安全等级可记录为官方声明，标准化认证需证书或审计机构证据；Tahiti Nui Telecom/TNF 站点同时包含海缆登陆、卫星、Galileo/OneWeb 等基础设施——邻近资产不自动等于可销售 DC 容量；TDF 官方新闻可确认 Papeete/Pic Rouge、opening announced 2025-09-18、delivered June 2025、data hosting solutions、first customers、planned 2026 extension、Tier III level compliance audit（A）；TNTV/DCD 可补充“约 40 baies”“90 million F CFP”等细节（B）；设施坐标/精确地址若来自目录站最多 C，官方只给 Pic Rouge/Papeete 时地址精度不应过写；ONATi 是 Groupe OPT 体系内综合电信运营商、产品以 Vini 品牌销售——把 Vini/ONATi 作电信运营商与客户接入渠道，不要把每个网络 POP 都记为 DC；Lycamobile “French Polynesia” 入口未验证其本地数据中心设施，仅作 MNO/网络线索；PMT/Vodafone、Viti 等运营商线索需回到 Lexpol/政府授权或官方企业页面确认。
- **海缆、登陆站、卫星（连接性资产）**：Groupe OPT NATITUA 新闻（OPT 与 Alcatel Submarine Networks 合作，连接 Tahiti 与 Tuamotu/Marquises 多岛，容量声明 10 Tbps 级）；AFD NATITUA 项目页（2018 起项目、20 个 Tuamotu/Marquesas 岛屿、OPT 受益方、AFD 600 万欧元融资）；Google Cloud South Pacific Connect（Honomoana/Tabua 连接 South Pacific）；Google Cloud Bulikula/Halaihai；APC 2024 电信外部连接意见确认 Honotua、Manatua、Natitua、Google South Pacific Connect 对 PF 电信市场的意义。事实口径：**Honotua** = Tahiti-Hawaii 国际连接并有 Tahiti、Moorea、Huahine、Raiatea、Bora Bora 国内段，登陆站不等于 DC；**NATITUA** = 不是 Tahiti-Hawaii 国际海缆，而是连接 Tuamotu/Marquesas 外岛的国内/区域扩展项目（草稿中的 “NATITUA：Tahiti-Hawaii” 应删除）；**Manatua** = 连接 PF、Cook Islands、Niue、Samoa，在 PF 国际冗余中重要；**Google Honomoana/Tabua/interlink** = Google 官方说会在 Fiji 与 French Polynesia 建设物理多样化登陆站并以 interlink cable 连接，在官方 RFS 前按 planned/under_construction 或 near_completion_unverified，不得当作 Google Cloud region；**MANAIA/Hawaiki Nui** = 以媒体/行业线索为主，需回挂 OPT/Google/政府/法律文本，无官方 RFS 时不得记为 operational。
- **电力**：EDT 为电力一手来源；电力来源只证明电力上下文不证明 DC 设施；新项目搜索 poste source/ligne HT/groupe électrogène/alimentation électrique/photovoltaïque/MW/Tier III/climatisation。
- **政府采购与招标**：当前官方采购门户说明页为 Service Public PF 的 **Te Ariari**（service-public.pf/marchespublics/），链接到市场室/平台 ecole.teariari.gov.pf（实测域名可访问但证书链可能导致命令行校验失败，浏览器按实际证书状态复核）；www.marches-publics.pf 实测不解析，不应作主入口，保留为历史/错误变体搜索即可；法国国家 PLACE（marches-publics.gouv.fr）可补充国家服务在 PF 的采购；招标、采购人、地点、金额、中标公告为 A；对政府/半官方托管、SIPF/DSI 外包、TDF/TNF 公共客户、海缆运维、发电/空调/消防升级，应优先查 Te Ariari、Service Public PF、Lexpol/JOPF、PLACE。
- **建筑许可/土地/环评**：PF manifest 没有省/州级 division，建筑许可仍需按市镇与岛屿搜索：Papeete、Pirae、Faa'a、Punaauia、Arue、Mahina、Hitiaa O Te Ra/Papenoo、Moorea-Maiao、Uturoa、Bora-Bora、Rangiroa、Nuku Hiva、Tubuai；TNF 官方法律声明给 Papenoo PK 16.7 侧山，TDF 官方给 Pic Rouge/Papeete，更精确边界需建筑许可、环评或业主资料；环评、消防、城市规划、土地记录为 A，目录坐标为 C。
- **分区查询模板与负面控制**：manifest 仅 1 个分区 French Polynesia，分区级模板即全国级模板；岛屿组/市镇分层——Îles du Vent（Tahiti/Mo'orea：唯一现实 DC 类线索区，TNF 与 TDF 均在 Tahiti）、Îles Sous-le-Vent（海缆/电信节点，默认无 DC）、Tuamotu-Gambier（NATITUA/通信节点，默认无 DC）、Marquises（NATITUA/通信节点，默认无 DC）、Australes（通信/电力上下文，默认无 DC）；负面控制查询："French Polynesia" cloud region / "Tahiti" availability zone / site:docs.aws.amazon.com / site:azure.microsoft.com / site:cloud.google.com/about/locations / site:oracle.com/cloud/public-cloud-regions。
- **证据分级与状态语义**：设施存在（TNF/TDF 官方设施页、法律声明、采购/许可/环评 = A；媒体 = B；目录 = C）；地址/边界（官方 contact/legal/许可/环评 = A；目录坐标、社交媒体地址 = C）；容量（官方规格、合同、环评、采购文件 = A；媒体引用 = B；Baxtel/DCM 数字 = C）；状态（官方 opening/RFS/operational 页 = A；MoU/规划新闻 = C，媒体投运 = B）；认证/Tier（证书或官方审计说明 = A；营销性 "Tier3+" 只能记为 claimed）；状态语义：announced/MoU = 计划线索；delivered/inaugurated/opened = 可记 operational 但需注明来源日期；extension planned = 与现有运营容量分开记录；海缆 RFS 与云区域无关。

## 行业/媒体/厂商发现要点（详见 explorer-industry.md）

- **行业格局判断**：法属波利尼西亚是小型已确认数据中心市场，不是空白市场；已验证线索集中在 Tahiti——TNF（operator_colo，Papenoo PK 16.7）、TDF Pic Rouge/Papeete（commercial_colo 或 operator_colo）、政府/机构托管需求（DSI/SIPF、市镇、银行、大学、医疗、媒体是本地客户/招标线索，单个企业机房默认 enterprise_server_room）、海缆/卫星邻近资产（Honotua、NATITUA、Manatua、Google Honomoana/Tabua、OneWeb/Galileo 站点可解释连接性与站点聚集，但不得替代 DC 证据）。核心结论写法：**confirmed small market / marché local confirmé mais très petit**；容量通常不公开，必须避免从目录站过度采信 MW/机柜数。
- **行业媒体与贸易新闻**：TDF 官方新闻（A）、Tahiti Nui Fortress 官方（A）、Tahiti Infos（B）、TNTV News（B，TDF Pic Rouge 采访、扩容/baies/投资额、SIPF 招标线索）、Polynésie La 1ère（B）、La Dépêche de Tahiti（B）、RNZ Pacific（B）、DCD（B，TDF launch/Google/海缆/目录交叉核验）、AFD（B，接近 A 但非设施业主）、Submarine Networks/TeleGeography map（B/C 海缆系统名、landing point 初筛）、Baxtel/DataCenterMap/DataCenters.com（C）；使用要点：捕获动词与日期——`annoncé`、`livré`、`inauguré`、`ouvert`、`opérationnel`、`extension prévue`、`accueille ses premiers clients`，把 "planned extension 2026" 与当前 operational 容量分开。
- **运营商、设施与厂商**：TNF datacenter/cloud/legal-contact 页（A）、Tahiti Nui Telecom（A，OPT 子公司、satellite/cable/cloud/fortress 品牌）、Groupe OPT（A，母集团、海缆、NATITUA、公共运营商背景）、ONATi/Vini（A 电信，DC 需回挂 TNF/TNT）、TDF（A）、Banque de Polynésie/Axians Polynésie（A/B，TDF 首批客户，不等于自营 DC）、DSI/SIPF（A 政府上下文）、EDT（A）、ASN/NEC/Google/AFD（A/B，海缆供应链与项目事实）、Schneider/Vertiv/Caterpillar/Cummins 等（C 起，除非合同/业主确认 UPS/冷却/发电机线索）。
- **云区域与超大规模**：PF 无已确认公有云 region/availability zone；官方全球位置页作负面控制（AWS/Azure/GCP/OCI）；Google 在 PF 的相关资产是 subsea cable/landing infrastructure，不是 Google Cloud region；负面控制模板含 "Tahiti" colocation (Equinix OR NTT OR "Digital Realty" OR Interxion)。
- **法语查询模板与塔希提语/地名变体**：见上“语言与词汇”；塔希提语主要用於地名规范和本地社区媒体，官方文件以法语为主；地名变体（Pape'ete、Papeno'o、Fa'a'ā、Mo'orea、Ra'iātea、Porapora）用于发现，设施事实仍需法语/官方/业主源确认。
- **枚举矩阵**：TNF operator colo/cloud（Papenoo/Hitiaa O Te Ra/Tahiti，tnfortress.pf/tahitinuitelecom.pf/groupe.opt.pf，A）；TDF Pic Rouge data center（Papeete/Pic Rouge/Tahiti，tdf.fr + TNTV/DCD，A/B）；政府/机构托管（Papeete/Tahiti，service-public.pf/dsi、Te Ariari、Lexpol，A）；企业/银行机房（Tahiti 都市区，Banque de Polynésie、Socredo、UPF、医疗机构 + salle serveurs，C 起）；海缆登陆站（Papenoo、Bora Bora、Moorea、Tuamotu、Marquesas，Honotua/NATITUA/Manatua/Honomoana/Tabua，A/B）；云区域/超大规模（全境，官方云区域负面控制，A 负面控制）；电力设施（Tahiti + 外岛，EDT、poste source、MW、groupe électrogène，A）；卫星/teleport（Papenoo，OneWeb、Galileo、station terrienne，A/B）。岛屿组矩阵：Îles du Vent（确认市场核心；TNF/TDF）；Îles Sous-le-Vent（海缆/电信为主；无独立 DC）；Tuamotu-Gambier（NATITUA 通信节点；无 DC）；Marquises（NATITUA 通信节点；无 DC）；Australes（无 DC，保留通信/电力上下文）。
- **按事实分级与 PF 特有陷阱**：主体/设施/地址/容量/状态/认证按上节逐项分级；PF 特有陷阱——旧结论过时（2025 TDF Pic Rouge 之后 PF 不能再写成“无商用数据中心市场”）、ARCEP PF 假阳性（不要使用 arcep.pf）、NATITUA 误分类（是 Tuamotu/Marquesas 外岛连接项目不是 Tahiti-Hawaii）、Papenoo 多资产混合（TNF data center、Honotua landing、satellite teleport、Galileo/OneWeb 同场域必须拆资产）、目录容量膨胀（Baxtel/DCM MW/机柜数需降级或回证）、Google cable ≠ cloud region、官方语言与拼写（法语优先，英文/塔希提语只补发现）。
- **推荐流程**：①官方设施种子（TNF datacenter/cloud/contact/legal pages；TDF Pic Rouge official release）②官方/法定回证（Service Public PF、Lexpol/JOPF、ANFR PF、APC、Te Ariari、PLACE）③媒体补充（TNTV/Tahiti Infos/DCD/La 1ère 捕获采访、客户、扩容、投资额）④容量严控（官方规格优先；媒体容量为 B；目录容量为 C）⑤海缆拆分（Honotua/NATITUA/Manatua/Honomoana/Tabua 落 cable_landing_station 或 connectivity context）⑥云负面控制（AWS/Azure/GCP/OCI 官方区域页确认无 PF region/AZ）⑦地理去重（manifest division 固定为 French Polynesia；site/commune 字段用 Papeete/Pic Rouge/Papenoo 等细化）⑧监控频率（月度 TDF/TNF/Service Public/TNTV；季度 Lexpol/Te Ariari/APC；海缆按 Google/OPT/RFS 公告更新）。

## 维护注意（更新纪律）

- **更新节奏**：月度 TDF/TNF/Service Public/TNTV；季度 Lexpol/Te Ariari/APC；海缆按 Google/OPT/RFS 公告更新；每次做时效性结论前重查 AWS/Azure/GCP/OCI 官方区域页。
- **来源核验**：行业源用于发现与佐证，最终设施存在/地址/状态尽量回挂官方或法定来源；容量以官方规格优先，媒体为 B、目录为 C；状态按 delivered/inaugurated/opened 等动词捕获并注明来源日期；extension planned 与当前运营容量分开；Tier 认证必须区分官方声明与正式认证。
- **不删除纪律**：本目录只新增/更新 SKILL.md、ANATOMY.md 与探索产物，禁止删除/移动任何现有文件（explorer-official.md、explorer-industry.md 与历史证据保留为原始记录）。
