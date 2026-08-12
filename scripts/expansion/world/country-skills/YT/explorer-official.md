# YT Explorer Official — 马约特数据中心官方/监管/一手来源枚举方法论
# Mayotte Datacenter Enumeration via Official, Regulatory, Power, Cable, and Procurement Sources

日期 Date: 2026-08-12. 国家 Country: **YT Mayotte（马约特，法国海外省 / French overseas department and region）**. 分区模型 Division model: `world-manifest.jsonl` 确认为 **subnational_type = country**，且只有 **1 个分区 Division: Mayotte**。本文件采用中文为主、英文补充的双语风格，用于发现和核实马约特境内运营中、在建、规划及机构性数据中心设施。

可靠性分级 Reliability grades: **A** = 官方/一手来源直接证明具体主张（政府、监管机构、公共开发金融机构、运营方官网、采购公告、认证登记、海缆财团或云厂商官方页）。**B** = 具名当事方、日期、地点的可靠媒体/行业媒体。**C** = 目录站、聚合页、SEO 主机页、社交帖、无地址或无设施证据的说法。媒体转述官方表态不得自动升级为 A；需同时保存被转述的一手 URL。

---

## 0. 已核实基线 Verified Baseline

- **分区覆盖 Division coverage**: manifest entry is exactly `{"country_code":"YT","country_name":"Mayotte","subnational_type":"country","divisions":["Mayotte"]}`. 任何记录的 `division` 必须写 **Mayotte**；Mamoudzou、Kaweni、Koungou 等仅作市镇/片区字段。
- **市场结论 Market conclusion**: 马约特并非“无公开数据中心”。本轮核实到 **ITH Center / Information Technology Hosting SAS** 是公开运营的本地 colocation / housing 数据中心，位于 Mamoudzou / Kaweni。除此之外，未确认其他 carrier-neutral 或 hyperscale 数据中心。
- **ITH Center 设施事实 Facility facts**:
  - AFD 项目页确认：`https://www.afd.fr/fr/projets/construction-du-premier-data-center-de-mayotte`，项目为 “construction et exploitation du premier data center de Mayotte”，受益方 ITH Center，位置 Mamoudzou，AFD 融资 3,000,000 EUR，项目起始 2020-11-06。AFD 描述容量为 **420 kW、76 baies informatiques、2 suites privées de 8 baies**，并称 2022-10-21 已 inaugurated。
  - ITH 官方页确认：`https://www.ith.yt/`，称 “1er Datacenter Tier III Neutre dédié à la colocation de la région”，位于 **Zone Industrielle de Kawéni, Mamoudzou**，自 2022 年提供服务，容量口径为 **80 baies**。
  - Banque des Territoires / Caisse des Dépôts 新闻稿确认：`https://www.banquedesterritoires.fr/sites/default/files/2022-10/CP_Inauguration%20Datacenter%20ITH%20Mayotte%20Banque%20des%20Territoires_21102022.pdf`，确认 ITH SAS 运营、总投资近 10M EUR、Banque des Territoires 1.3M EUR fonds propres、AFD 与 Crédit Agricole Réunion-Mayotte 合计 7.5M EUR loans/bridge financing。
  - **Tier III 处理**: 目前找到的是 ITH/AFD/金融机构对 Tier III 或 Uptime-defined Tier III 的描述；未在 Uptime/TIA/EPI 登记中核实到证书 ID。因此记录为 **`tier_claim: "Tier III / conception Tier III"`**，不要写成 `certified Tier III`，除非认证登记给出证书。
  - **容量处理**: `capacity_mw` 可记录 AFD 的 **0.42 MW**，并备注 ITH 官网写 80 bays、AFD 写 76 bays；DataCenterMap 的 0.65 MW 属 C 级补充，不覆盖 AFD/ITH 一手口径。
- **通信监管**: 马约特适用法国 ARCEP 监管。ARCEP 2025-04-17 新闻稿/PDF确认 3.4-3.8 GHz 牌照授予 **Orange、SRR、Telco OI**，每家 120 MHz，期限 15 年：`https://en.arcep.fr/fileadmin/user_upload/30-25-english-version.pdf`。不要把未由 ARCEP 确认的 “Free Mayotte / Telma Mayotte” 目录说法当作本地 MNO 事实；可作为待核目录噪声。
- **IXP/PoP**: RENATER 官方确认 **MAYOTIX** 是 Mayotte 的 GIX/IXP，hosted in Mamoudzou on the Vice-Rectorate premises：`https://www.renater.fr/en/network/national-and-international/renaterix/`。这是连接/交换点，不是默认数据中心。
- **海缆连接**:
  - **LION2**（不是 FLY-LION2）连接 LION 至 Mayotte 与 Mombasa；Mayotte landing station historically reported at Kaweni/Mamoudzou。官方/行业核实入口：Orange/France Telecom press release archives, Submarine Networks `https://www.submarinenetworks.com/en/systems/asia-europe-africa/lion-2`。
  - **FLY-LION3** 官方 Orange 页确认 Moroni (Grande Comore) 与 Mamoudzou (Mayotte) 之间 400 km cable，landing stations at **Kaweni (Mamoudzou)** and Moroni，consortium includes Orange, SRR and Comores Câbles，planned in-service Q3 2019, capacity 4 Tbps：`https://www.orange.com/fr/communiques/le-cable-sous-marin-tres-haut-debit-fly-lion3-atterrit-a-mayotte-232877`。
  - **Avassa** Huawei Marine/Hengtong 交付新闻确认 Comoros Telecom 与 Mayotte-based carrier STOI 于 2016 签约，260 km system connects Grande Comore, Anjouan and Mayotte：`https://www.huawei.com/en/news/2016/11/avassa-submarine-cable-project`。它是连接设施，非 DC。
- **电力**: EDM 官方站点已核实为 `https://www.electricitedemayotte.com/`；客户门户使用 `https://www.espace-client.edm.yt/`。CRE/ZNI 与 PPE 文件为电力容量、价格、质量的一手监管入口。电厂、发电机、UPS、储能、ICPE 只证明电力/环境设施，不单独证明 DC。
- **官方网站纠正**: Département de Mayotte 官方站点为 `https://www.mayotte.fr/`（页面列有 Marchés publics 入口）；旧 `cd976.fr` 只可作为历史/别名线索。DEALM 官方站点为 `https://www.mayotte.developpement-durable.gouv.fr/`，不是 `deal-mayotte.developpement-durable.gouv.fr`。
- **云区域与认证负向控制**: AWS/Azure/GCP/OCI 官方区域页未列 Mayotte；Uptime/TIA/EPI 本轮未核实到 Mayotte/ITH 的正式证书条目。负向结果要保留刷新日期。

---

## 1. 官方与一手来源 Official and Primary Sources

### 1.1 法律、行政公报、规划许可 Legal and Administrative Records

一手入口 Primary routes:
- Préfecture de Mayotte: `https://www.mayotte.gouv.fr/`
- RAA: `https://www.mayotte.gouv.fr/Publications/Recueil-des-actes-administratifs-R.A.A`
- Légifrance: `https://www.legifrance.gouv.fr/`
- CNIL: `https://www.cnil.fr/`
- DEALM: `https://www.mayotte.developpement-durable.gouv.fr/`
- Géorisques / ICPE: `https://www.georisques.gouv.fr/`

查询模板 Queries:
```text
site:mayotte.gouv.fr/Publications/Recueil-des-actes-administratifs "ITH"
site:mayotte.gouv.fr/Publications/Recueil-des-actes-administratifs "Information Technology Hosting"
site:mayotte.gouv.fr Mayotte ("centre de données" OR "data center" OR datacenter OR "salle informatique")
site:mayotte.developpement-durable.gouv.fr Mayotte (ICPE OR "permis de construire" OR "étude d'impact") ("centre de données" OR "groupe électrogène" OR onduleur)
site:georisques.gouv.fr Mayotte ITH
site:legifrance.gouv.fr Mayotte ("communications électroniques" OR "zone non interconnectée" OR "commande publique")
site:cnil.fr Mayotte (hébergeur OR "hébergement de données" OR ITH)
```

记录字段 Fields to extract: 文本号/日期、发布机关、地址或市镇、主体 SIREN/SIRET、许可/决定类型、是否涉及机房/发电/冷却/燃料、原文 URL/PDF。

### 1.2 公共采购与开发金融 Procurement and Development Finance

高价值官方入口:
- AFD ITH project: `https://www.afd.fr/fr/projets/construction-du-premier-data-center-de-mayotte`
- Banque des Territoires / Caisse des Dépôts press and financing records: `https://www.banquedesterritoires.fr/`
- BOAMP: `https://www.boamp.fr/`
- PLACE: `https://placee.marches-publics.gouv.fr/`
- Département de Mayotte: `https://www.mayotte.fr/` (Marchés publics)
- Data.gouv.fr: `https://www.data.gouv.fr/`
- Annuaire des Entreprises: `https://annuaire-entreprises.data.gouv.fr/`

查询模板:
```text
site:afd.fr Mayotte ("data center" OR datacenter OR "centre de données" OR ITH)
site:banquedesterritoires.fr Mayotte ITH datacenter
site:boamp.fr Mayotte ("hébergement" OR "colocation" OR "centre de données" OR "salle informatique" OR infogérance)
site:placee.marches-publics.gouv.fr Mayotte ("hébergement" OR "sauvegarde" OR "plan de reprise" OR "centre de données")
site:mayotte.fr ("marchés publics" OR "appel d'offres") (informatique OR hébergement OR télécommunications)
site:annuaire-entreprises.data.gouv.fr "Information Technology Hosting"
site:annuaire-entreprises.data.gouv.fr "ITH Center"
Mayotte "6311Z" "annuaire-entreprises.data.gouv.fr"
```

处理规则:
- AFD/CDC/ITH 官方资料可确认 ITH Center 存在、位置、融资、容量口径、运营状态。
- BOAMP/PLACE 采购公告可证明客户采购托管、备份、PRA/PCA、机房维护或网络互联需求；不得仅凭“hébergement web”推断物理 DC。
- 企业登记确认法人/地址/APE；不等同于设施运营，除非公司名与设施证据对齐。

### 1.3 电信监管与运营商 Telecom Regulation and Operators

一手入口:
- ARCEP: `https://www.arcep.fr/`
- ARCEP 2025 Mayotte 3.4-3.8 GHz press/PDF: `https://en.arcep.fr/fileadmin/user_upload/30-25-english-version.pdf`
- Orange Mayotte: `https://mayotte.orange.fr/portail/`
- SRR/SFR Mayotte / Altice Outremer: verify through ARCEP and official SFR/Altice pages
- Telco OI / Only: `https://only.yt/` and `https://telco.re/`
- RENATERIX / MAYOTIX: `https://www.renater.fr/en/network/national-and-international/renaterix/`

查询模板:
```text
site:arcep.fr Mayotte (Orange OR SRR OR "Telco OI" OR "Mayotte One") fréquences
site:arcep.fr Mayotte ("observatoire" OR "marché mobile" OR "réseaux fixes" OR "très haut débit")
site:mayotte.orange.fr Mayotte ("centre de données" OR "hébergement" OR cloud OR "salle serveur")
site:only.yt Mayotte ("centre de données" OR hébergement OR réseau OR "station d'atterrissement")
site:telco.re Mayotte ("centre de données" OR hébergement OR réseau OR "station d'atterrissement")
site:renater.fr MAYOTIX Mayotte Mamoudzou
```

处理规则:
- 当前监管事实的最低名单为 **Orange, SRR, Telco OI**。2024 tender 中出现 **Mayotte One** 可记录为监管申请/候选线索；需进一步确认是否商用。
- “Free Mayotte” 与 “Telma Mayotte” 多见于旅游 SIM/号码目录，未在本轮 ARCEP 2025 牌照结果中作为获牌 MNO 出现；除非有 ARCEP 或公司官方证据，不进入已核实运营商名单。
- MAYOTIX 是 IXP/PoP 线索，记录为 connectivity facility，不作为 DC。

### 1.4 数据中心认证与云区域 Certification and Cloud Region Controls

官方入口:
- Uptime Institute awards: `https://uptimeinstitute.com/uptime-institute-awards/list`
- TIA-942 certified data centers / EPI list: `https://www.epi-certification.com/sites/list`
- AWS regions: `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`
- Azure regions: `https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- Google Cloud locations: `https://cloud.google.com/about/locations`
- OCI regions: `https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm`

查询模板:
```text
site:uptimeinstitute.com/uptime-institute-awards Mayotte
site:uptimeinstitute.com/uptime-institute-awards "ITH Center"
site:uptimeinstitute.com/uptime-institute-awards "Information Technology Hosting"
site:epi-certification.com/sites/list Mayotte
site:epi-certification.com/sites/list "ITH"
"ITH Center" ("Uptime Institute" OR "TIA-942" OR certification)
"Mayotte" ("AWS Region" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR "local zone")
```

记录规则:
- 若无登记证书，只能写 `claimed/conception Tier III`，不得写 `certified Tier III`。
- 云厂商区域页无 Mayotte 是 A 级负向事实；本地主机或 cloud resale 不等于 hyperscale region。

### 1.5 电力、能源、环境 Power, Energy, and Environment

一手入口:
- EDM official: `https://www.electricitedemayotte.com/`
- EDM online portal: `https://www.espace-client.edm.yt/`
- CRE: `https://www.cre.fr/`
- EDF SEI: `https://sei.edf.fr/`
- DEALM / Géorisques as above

查询模板:
```text
site:electricitedemayotte.com Mayotte (Longoni OR centrale OR réseau OR "appel d'offres" OR MVA OR kVA)
site:cre.fr Mayotte ZNI (PPE OR tarif OR capacité OR qualité)
site:mayotte.developpement-durable.gouv.fr Mayotte (ICPE OR "groupe électrogène" OR "stockage d'énergie")
"ITH Center" Mayotte (énergie OR "groupe électrogène" OR onduleur OR PUE OR "420 kW")
```

处理规则:
- 电力/ICPE 记录可佐证 ITH 或其他设施的备用电源、冷却、燃料存储、许可状态。
- Longoni 电厂、EDM 控制中心、SCADA 机房是电力基础设施线索；没有托管/服务器/地址证据前不计为数据中心。

### 1.6 海缆登陆站 Cable Landing Stations

| 系统 System | 已核事实 Verified facts | 来源 Sources | 枚举处理 |
|---|---|---|---|
| **LION2** | LION extension to Mayotte and Mombasa; Mayotte landing historically at Kaweni/Mamoudzou | `https://www.submarinenetworks.com/en/systems/asia-europe-africa/lion-2`; Orange archive/press searches | 连接设施；不要写 FLY-LION2；非 DC |
| **FLY-LION3** | 400 km Moroni-Mamoudzou, landing stations Kaweni and Moroni, consortium Orange/SRR/Comores Câbles, planned service Q3 2019, 4 Tbps | `https://www.orange.com/fr/communiques/le-cable-sous-marin-tres-haut-debit-fly-lion3-atterrit-a-mayotte-232877` | 连接设施；Kaweni 是 ITH/telecom proximity lead |
| **Avassa** | 260 km Comoros-Mayotte system, Comoros Telecom + Mayotte-based STOI contract, delivered 2016 | `https://www.huawei.com/en/news/2016/11/avassa-submarine-cable-project` | 连接设施；非 DC |

查询模板:
```text
("LION2" OR "LION 2") Mayotte Kaweni landing station Orange
"FLY-LION3" Mayotte Kaweni Mamoudzou Orange SRR "Comores Câbles"
"Avassa" Mayotte STOI "Comoros Telecom" Huawei
Mayotte "câble sous-marin" (résilience OR redondance OR Chido OR nouveau)
```

---

## 2. 分区覆盖流程 Division Coverage Workflow

清单分区只有 **Mayotte**。执行枚举时将全岛拆成市镇/片区，确保每个区域都有“已核实项目/线索/未发现”的结果。

| 子位置 Sub-locality | 优先级 | 官方优先路径 | 当前结论 |
|---|---:|---|---|
| **Mamoudzou / Kaweni** | 高 | ITH/AFD/CDC；RAA/DEAL/ICPE；BOAMP/PLACE；Orange/SRR/Telco OI；海缆资料 | **确认 ITH Center**；Kaweni 另有 LION2/FLY-LION3 landing/connectivity leads；MAYOTIX hosted in Mamoudzou |
| **Koungou / Longoni** | 中 | EDM/CRE/DEAL/Géorisques；port/dept procurement | 电力/港口线索；未发现公开 DC |
| **Dzaoudzi / Pamandzi** | 中低 | 机场/旧行政中心采购；DEAL/ICPE；运营商网络 | 电信/机场机房线索；未发现公开 DC |
| **Dembéni / Ouangani / Sada / Chirongui / Bandrélé / Acoua / M'tsangamouji / Mtsamboro / Bandraboua / Tsingoni / Chiconi / Bouéni / Kani-Kéli** | 低 | 市镇采购、DEAL/ICPE、本地媒体 | 未发现公开 DC；逐次刷新采购与规划记录 |

分区通用查询模板:
```text
("Mayotte" OR "976" OR "{commune}") ("centre de données" OR "data center" OR datacenter OR "salle de serveurs" OR "salle informatique")
("Mayotte" OR "{commune}") ("hébergement" OR "colocation" OR "baie informatique" OR "plan de reprise" OR "sauvegarde")
("Mayotte" OR "{commune}") ("station d'atterrissement" OR "câble sous-marin" OR backbone OR NOC OR "point de présence")
site:boamp.fr Mayotte "{commune}" (informatique OR télécommunications OR hébergement OR infogérance)
site:mayotte.gouv.fr "{commune}" (numérique OR informatique OR câble OR marché)
site:mayotte.developpement-durable.gouv.fr "{commune}" (ICPE OR "permis de construire" OR "groupe électrogène")
```

本地变体: Mahoré / Mahorais / Mahoraise, 976, Grande-Terre, Petite-Terre, Kawéni/Kaweni, Dzaoudzi, Pamandzi.

---

## 3. 设施种子清单 Facility Seed List

| 种子 Seed | 分区/子位置 | 状态 | 等级 | 容量处理 | 最佳证据路径 |
|---|---|---|---|---|---|
| **ITH Center / Information Technology Hosting SAS** | Mayotte — Mamoudzou / Kaweni | 运营中 colocation/housing data center；inaugurated 2022-10-21 | **A** for existence/location/operator/financing/capacity from AFD/ITH/CDC; **Tier certification not independently verified** | AFD: 0.42 MW, 76 bays + 2 suites; ITH: 80 bays; DCM: 0.65 MW is C only | ITH `https://www.ith.yt/`; AFD project; Banque des Territoires PDF; Annuaire Entreprises |
| **MAYOTIX** | Mayotte — Mamoudzou, Vice-Rectorate premises | IXP/GIX, not DC | A for IXP fact | null | RENATERIX official page |
| **LION2 landing / Kaweni** | Mayotte — Mamoudzou / Kaweni | Submarine cable landing/connectivity facility | A/B depending source; not DC | null | Orange archives; Submarine Networks |
| **FLY-LION3 landing / Kaweni** | Mayotte — Mamoudzou / Kaweni | Submarine cable landing/connectivity facility | A | cable capacity 4 Tbps, not DC capacity | Orange FLY-LION3 press release |
| **Avassa landing / STOI lead** | Mayotte — Mamoudzou/Kaweni to verify | Submarine cable connectivity facility | A/B | null | Huawei/Hengtong delivery; TeleGeography/GeoCables |
| **Orange / SRR / Telco OI network rooms** | Mayotte | Telecom PoP/NOC leads | A for operator spectrum; C until facility proof | null | ARCEP decisions; operator official pages; BOAMP |
| **EDM control/SCADA rooms and Longoni plant** | Mayotte — Mamoudzou/Koungou | Power infrastructure leads, not DC | A for power facts; C as DC lead | not DC capacity | EDM/CRE/DEAL/Géorisques |
| **Government/hospital/municipal hosting procurements** | Mayotte, mainly Mamoudzou | Customer/use-case leads | A if BOAMP/PLACE or official procurement; not a facility unless address/operator known | null | BOAMP/PLACE, mayotte.fr, mayotte.gouv.fr |
| **AWS/Azure/GCP/OCI local region** | — | Negative: no Mayotte region found | A negative | null | official region pages |
| **Uptime/TIA/EPI certified facility** | — | Negative/unchecked certificate ID for ITH | A negative when registry searched | null | official certification registries |

---

## 4. 陷阱与决策规则 Pitfalls and Decision Rules

- **不要重复草稿错误**: Mayotte 已有公开 ITH Center；不能再写“未确认任何公开数据中心”。同时，LION2 不是 FLY-LION2。
- **Tier III 诚实写法**: ITH/AFD/CDC 可支持 “Tier III / conception Tier III / defined by Uptime Institute” 的主张；未找到证书 ID 前不要写 “Uptime certified”。
- **容量冲突要保留来源口径**: AFD 420 kW/76 bays 是 A 级项目资料；ITH 官网 80 bays 是 A 级运营方资料；DataCenterMap 0.65 MW 是 C 级目录补充。
- **海缆与 IXP 不是 DC**: LION2、FLY-LION3、Avassa、MAYOTIX 都是连接设施/PoP 线索；只有出现服务器托管/colo/机房运营证据才可升级。
- **运营商名单以 ARCEP 为准**: 2025 年 3.4-3.8 GHz 牌照为 Orange, SRR, Telco OI。Free/Telma 目录说法应降级为噪声，除非有 ARCEP 或公司官方证据。
- **法国海外省监管链**: Légifrance/Préfecture RAA/ARCEP/CRE/DEAL/BOAMP/PLACE 是主要官方链条；不要寻找独立 Mayotte regulator。
- **公共采购高价值**: BOAMP/PLACE 的 hosting, sauvegarde, PRA/PCA, colocation, salle informatique 公告可能揭示 ITH 客户、政府机房迁移或新项目。
- **电力证据的边界**: 发电机、UPS、冷却、PUE、ICPE 能佐证设施属性，但单独的电力设施不等于 DC。
- **刷新项**: 每次更新重查 ITH 官方、AFD/CDC、Uptime/TIA/EPI、AWS/Azure/GCP/OCI、ARCEP、BOAMP/PLACE、DEAL/Géorisques、Mayotte 2024-2026 cyclone recovery/submarine cable resilience news。
