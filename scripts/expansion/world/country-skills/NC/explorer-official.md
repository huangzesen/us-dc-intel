# NC Explorer — 官方 / 监管 / 电信 / 电力 勘探方法
# New Caledonia Official / Regulatory / Telecom / Power Discovery Methodology

Date: 2026-08-12. Scope: enumerate New Caledonia (Nouvelle-Calédonie) datacenter facilities and projects from official, regulatory, telecom, power, cable-landing, and procurement sources. Chinese is primary; French/English terms are retained for search precision.

world-manifest verification: `world-manifest.jsonl` lists NC as one manifest division only: `country_code: "NC"`, `subnational_type: "country"`, `divisions: ["New Caledonia"]`. Therefore the delivery coverage unit is **New Caledonia**. The practical scan grid below uses the territory's 3 provinces and 33 communes only as an internal completeness checklist, not as manifest divisions.

Reliability grades: **A** = official/primary source (government, official gazette, regulator/competent authority, operator official page, procurement notice, official filing); **B** = strong secondary or industry source; **C** = aggregator, social/self-published, weak secondary, or unverified lead.

---

## 0. 结构性事实（New Caledonia frame）

- **行政框架**：新喀里多尼亚是法国 `collectivité sui generis`。官方页面确认有 **33 communes**；国家代表页面确认有 **3 provinces**：Province Sud、Province Nord、Province des Îles Loyauté。Open Data NC 的 `communes-nc` 数据集可用于完整 commune 清单，并标注 Poya 横跨 Province Nord 与 Province Sud。
- **市场体量很小**：NC 没有 AWS/Azure/Google Cloud 本地区域。设施级发现应以本地电信/托管、政府 DINUM、银行、矿业工业 IT、教育科研和少量本地服务商为主。任何 MW 级、Tier 级或机柜数声明都必须逐字段分级。
- **电信监管口径**：不要使用不存在或未验证的 `ARCEP-NC` 作为 A 级来源。ANFR 明确说明法国本土 ARCEP 在新喀里多尼亚不具管辖权，电信监管由新喀里多尼亚政府承担。2024 年政府公告显示正在通过 Autorité de la concurrence de la Nouvelle-Calédonie 的技术支持预备独立监管任务。实际检索应使用 `gouv.nc`、JONC/Juridoc、Autorité de la concurrence NC、ANFR、OPT-NC 和采购平台。
- **电力约束**：Enercal 是输电和系统运行核心；配电由 communes 选择 Enercal 或 EEC-Engie。Enercal 官方说明 Grande Terre 公共输电网为 150 kV / 33 kV，输电网由领地所有并委托 Enercal 运营。数据中心候选的 `grid_mw`、`generator_mw`、`it_mw` 必须分开记录。
- **海底光缆约束**：OPT-NC 官方资料确认 GONDWANA-1 于 2008 年连接 Nouméa-Sydney；GONDWANA-2 于 2022 年连接 Nouméa-Suva，并与 PICOT-2 国内光缆一起增强冗余。landing 精确地址通常不公开，除非 OPT/政府/许可文件明确给出。

---

## 1. 高价值官方来源（A 级主干）

### 1.1 政府、法律、公报、行政边界

| Source | URL | 用途 | Grade |
|---|---|---|---:|
| Gouvernement de la Nouvelle-Calédonie | https://gouv.nc | 政府公告、DINUM、数字化、能源、电信政策 | A |
| JONC / Juridoc | https://juridoc.gouv.nc | Journal officiel、公报 PDF、法律/决议/arrêté | A |
| Congrès de la Nouvelle-Calédonie | https://www.congres.nc | 议会审议、能源/电信/预算/特许经营决议 | A |
| Haut-commissariat | https://www.nouvelle-caledonie.gouv.fr | 国家代表、ANFR/无线电、电信国家侧页面、公共调查线索 | A |
| Province Sud | https://www.province-sud.nc | 环境、urbanisme、土地、经济项目；该站可能对 automated HEAD 返回 403，浏览/搜索可用 | A |
| Province Nord | https://www.province-nord.nc | 环境、矿业、能源、aménagement、marchés publics | A |
| Province des Îles Loyauté | https://www.province-iles.nc | 岛屿接入、环境、土地、公共项目 | A |
| Open Data NC | https://data.gouv.nc | communes、fibre deployment、DRH/DINUM job PDFs、采购统计 | A |
| ISEE | https://www.isee.nc | 人口/经济校准；非设施级 | A |
| DITTT / Géorep | https://www.dittt.gouv.nc | 地理、基础设施、地籍/GIS 背景 | A |

官方查询模板：

```text
site:gouv.nc (datacenter OR "centre de données" OR "centre informatique" OR "salle informatique" OR DINUM)
site:juridoc.gouv.nc (datacenter OR "centre de données" OR "centre informatique" OR "salle informatique" OR "réseau et datacenter")
site:congres.nc (datacenter OR "centre de données" OR télécommunications OR numérique OR énergie)
site:nouvelle-caledonie.gouv.fr (télécommunications OR radiocommunications OR ANFR OR "Nouvelle-Calédonie")
site:data.gouv.nc (datacenter OR DINUM OR "fibre optique" OR "avis de vacances de poste")
"Nouvelle-Calédonie" "33 communes" site:gouv.nc
"Nouvelle-Calédonie" "3 provinces" site:nouvelle-caledonie.gouv.fr
```

### 1.2 电信与政府监管

| Source | URL | 已验证口径 | Grade |
|---|---|---|---:|
| OPT-NC commercial | https://www.opt.nc | OPT-NC 官方商业站；legal mentions 给出 EPIC、RCS Nouméa、Nouméa 地址 | A |
| OPT-NC corporate/news | https://office.opt.nc | 年报、董事会材料、Gondwana/PICOT 新闻、ASN 合同公告 | A |
| Gouvernement NC telecom regulation | https://gouv.nc | 电信监管与独立监管预备公告 | A |
| ANFR Outre-mer regulation | https://www.anfr.fr/outre-mer/reglementation | 明确 ARCEP 不管辖 NC，监管由 NC 政府承担 | A |
| Autorité de la concurrence NC | https://autorite-concurrence.nc | 2024 connectivity opinion、市场结构/竞争材料 | A |
| APNIC Whois | https://wq.apnic.net | AS/RIR 分配，网络存在事实；非设施事实 | A 网络 / C 设施 |

重要修正：

- `arcep.nc` 不作为来源使用；未验证为 NC 官方监管站点。
- `www.arcep.fr` 可作为法国 ARCEP 背景，但对 NC 设施/运营商监管不是直接 A 源。
- 运营商/ISP 清册从政府、JONC、Autorité de la concurrence、OPT-NC、ANFR 和 APNIC/BGP 交叉获得。

电信查询模板：

```text
site:office.opt.nc (datacenter OR "centre de données" OR hébergement OR CITIUS OR "salle informatique" OR cloud)
site:opt.nc (hébergement OR cloud OR entreprise OR "fibre optique")
site:gouv.nc (télécommunications OR "régulation indépendante" OR connectivité OR OPT-NC)
site:autorite-concurrence.nc (OPT OR Offratel OR Citius OR SCCI OR télécommunications OR connectivité)
site:anfr.fr/outre-mer "Nouvelle-Calédonie" télécommunications ARCEP
site:wq.apnic.net "Office des Postes" "New-Caledonia"
"OPT-NC" ("DATACENTER" OR "centre de données" OR CITIUS OR hébergement) (Nouméa OR Nouville OR Ouémo)
```

### 1.3 电力：Enercal / EEC / concession

| Source | URL | 用途 | Grade |
|---|---|---|---:|
| Enercal | https://www.enercal.nc | production, transport, distribution, postes sources, network map, annual reports | A |
| Enercal network pages | https://www.enercal.nc/lelectricite-en-nouvelle-caledonie/les-reseaux/ | 150 kV / 33 kV network, isolated systems, private networks | A |
| Enercal system operation | https://www.enercal.nc/lelectricite-en-nouvelle-caledonie/la-gestion-du-transport-et-du-systeme-electrique/ | raccordement, system operator, transport development | A |
| Enercal distribution | https://www.enercal.nc/lelectricite-en-nouvelle-caledonie/la-distribution/ | communes choosing Enercal/EEC-Engie distribution; 2025 distribution figures | A |
| EEC-Engie | https://www.eec-engie.nc | distribution concession in selected communes, customer/power context | A-/B |

电力查询模板：

```text
site:enercal.nc (datacenter OR "centre de données" OR raccordement OR "poste source" OR MW OR "client direct")
site:enercal.nc ("poste HTB/HTA" OR "150 kV" OR "33 kV" OR "carte de l'électricité")
"Enercal" ("poste source" OR raccordement OR puissance) (Nouméa OR Dumbéa OR Païta OR Koné OR Voh)
"concession" "Enercal" électricité "Nouvelle-Calédonie"
site:eec-engie.nc (raccordement OR "puissance souscrite" OR "Nouméa")
("SLN" OR "KNS" OR "Prony Resources") ("centrale" OR "MW" OR "réseau privé") "Nouvelle-Calédonie"
```

电力提取规则：

- `it_mw` 仅限明确 IT load / puissance informatique。
- `grid_mw` 仅限 raccordement、puissance souscrite、poste source、concession 或 technical filing。
- `generator_mw` 是应急柴油/自备电，不等于 IT 容量。
- 矿业电厂、金属冶炼负荷和 data center 候选必须分离；矿业只是工业 IT 和供电线索。

### 1.4 海底光缆与 landing evidence

| Cable/system | Verified facts | Sources | Grade |
|---|---|---|---:|
| GONDWANA-1 | OPT-NC says deployed in 2008; 2,152 km; Nouméa-Sydney | OPT-NC network security page; SCN/TeleGeography corroboration | A route/year from OPT; B independent |
| PICOT-1 | OPT-NC says 2008 domestic cable; Poindimié to Ouvéa and Lifou | OPT-NC | A |
| GONDWANA-2 | OPT-NC says 2022; 1,515 km; Nouméa-Suva, Fiji | OPT-NC | A |
| PICOT-2 | OPT-NC says domestic links via Ouémo, Mont-Dore, Nouville, Île des Pins, Yaté, Maré, Lifou | OPT-NC press materials | A |
| Hawaiki Nui / other branches | Treat only as announced/assessed unless OPT-NC or government confirms NC landing and status | DCD/Telecompaper/BW Digital/TeleGeography | B/C until official |

Cable queries:

```text
site:office.opt.nc Gondwana PICOT "câble sous-marin"
site:office.opt.nc "GONDWANA-2" "PICOT-2" "mise en service"
site:office.opt.nc "station d'atterrissement" OR atterrage OR Ouémo OR Nouville OR "Mont-Dore"
"Gondwana-1" "Nouméa" Sydney "ready for service"
"Hawaiki Nui" ("New Caledonia" OR "Nouvelle-Calédonie") OPT
site:submarinecablemap.com "New Caledonia"
```

### 1.5 公共采购 / procurement

| Source | URL | 用途 | Grade |
|---|---|---|---:|
| Marchés publics de la Nouvelle-Calédonie | https://marchespublics.nc | 统一采购平台；政府公告称新版自 2022-12-15 上线 | A |
| Portal path mentioned by government | https://portail.marchespublics.nc | 实时跟踪入口；如重定向，以 `marchespublics.nc` 为准 | A |
| Province Nord e-procurement | https://marchespublics.province-nord.nc | Province Nord public procurement room; also says notices are on `marchespublics.nc` | A |
| PLACE state procurement | https://www.marches-publics.gouv.fr | 法国国家采购，仅用于 Haut-commissariat/国家服务项目；不要替代 NC 平台 | A when relevant |

采购查询模板：

```text
site:marchespublics.nc (datacenter OR "centre de données" OR "salle informatique" OR hébergement OR infogérance OR cloud OR cybersécurité)
site:marchespublics.nc ("réseau et datacenter" OR "infrastructures numériques" OR DINUM OR "cloud interne")
site:marchespublics.province-nord.nc (hébergement OR "salle informatique" OR cybersécurité OR "système d'information")
site:gouv.nc "plateforme des marchés publics" "marchespublics.nc"
site:www.marches-publics.gouv.fr "Nouvelle-Calédonie" (hébergement OR informatique OR datacenter)
```

---

## 2. 云与排除性基线（cloud negative evidence）

| Vendor | Official URL | NC fact | Grade |
|---|---|---|---:|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | region list includes Sydney `ap-southeast-2`; no NC region | A |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | public Azure region list has Australia regions; no NC region | A |
| Google Cloud | https://cloud.google.com/about/locations | official locations page; no NC region; nearest practical regions are Australia/NZ | A |
| OVHcloud | https://www.ovhcloud.com/en/datacenter/ | official datacenter page lists countries/regions elsewhere; no NC datacenter | A |

Rule: "service available in New Caledonia" or "Sydney/Australia region serves New Caledonia" is **not** local facility evidence.

---

## 3. 已验证种子实体（seed entities）

| Category | Entity | Evidence to use | Typical grade |
|---|---|---|---:|
| Incumbent telecom | OPT-NC / Office des Postes et Télécommunications de Nouvelle-Calédonie | official sites, annual reports, board PDFs, APNIC ASNs, cable pages | A |
| Historical OPT datacenter activity | CITIUS / OPT datacenter activity | OPT annual reports and competition authority filings mention CITIUS and datacenter activity; verify current status before counting | A historical / B current unless updated |
| Government IT | DINUM / Direction du Numérique et de la Modernisation | gouv.nc address at Ouémo; JONC organization includes "réseau et datacenter"; DRH PDFs mention cloud/datacenter roles | A |
| Private colocation | DSP / Data Services Pacific | official `dsp.nc` says private hosting company in Nouméa and unique actor with 2 data centers; aggregators give addresses/capacity only as B/C until official/permit confirmation | A existence / B-C capacity |
| Power/system | Enercal, EEC-Engie | grid, distribution, raccordement and concession context | A |
| Competition/market | Autorité de la concurrence NC | telecom/connectivity opinions and case files | A |
| Network evidence | APNIC / bgp.tools / PeeringDB | ASN/IP/peering seeds; non-facility unless tied to a named site | A network / C facility |

---

## 4. 覆盖矩阵（manifest division + internal scan grid）

Manifest division coverage requirement:

```text
New Caledonia
```

Internal completeness scan:

| Province | Communes to sweep | Priority rationale |
|---|---|---|
| Province Sud | Nouméa, Dumbéa, Le Mont-Dore, Païta, Boulouparis, La Foa, Sarraméa, Farino, Moindou, Bourail, Thio, Yaté, Île des Pins, south Poya | population/economy center, government/DINUM, OPT/DSP, banking, cable landings, main grid |
| Province Nord | Koné, Voh, Pouembout, Koumac, Poum, Bélep, Ouégoa, Pouébo, Hienghène, Touho, Poindimié, Ponérihouen, Houaïlou, Kouaoua, Canala, north Poya, Kaala-Gomen | mining/industrial IT, KNS/Vavouto context, east coast and northern telecom sites |
| Province des Îles Loyauté | Lifou, Maré, Ouvéa, Tiga where referenced in provincial/cable records | domestic cable landings, autonomous energy systems, telecom access sites |

Commune/province query pattern:

```text
site:{province-or-commune-domain} (datacenter OR "centre de données" OR "salle informatique" OR "centre informatique")
site:{province-or-commune-domain} ("permis de construire" OR urbanisme OR "enquête publique" OR "conseil municipal") ("centre de données" OR datacenter OR "poste source")
"{commune}" ("centre de données" OR datacenter OR "salle serveurs" OR hébergement) "Nouvelle-Calédonie"
"{commune}" ("poste source" OR raccordement OR "puissance souscrite") (Enercal OR EEC)
```

---

## 5. 接纳、分级与字段规则

Minimum acceptance:

- Facility/project existence: 1 A source, or 2 independent B sources plus one local official clue.
- Location: must resolve to New Caledonia and preferably commune/province; if only "Nouméa" or "Ouémo/Nouville/Magenta" is given, record that granularity honestly.
- Operator/legal entity: use official legal name where possible (`RCS Nouméa`, `RIDET`, APNIC org, procurement awardee).
- Status: assign separately from existence.

Status model:

- `lead`: only trade/aggregator/social clue.
- `announced`: named owner/project but no permit or service evidence.
- `under review`: enquête publique, procurement, deliberation, or study stage.
- `permitted`: permit/arrêté/délibération issued.
- `under construction`: permit plus works/contract/official construction evidence.
- `operational`: official service page, annual report, regulator/authority filing, active procurement/service evidence, or confirmed live facility.
- `expansion`: existing facility has an extension, phase, or capacity upgrade.
- `retired/merged`: historical facility or corporate vehicle no longer independent; keep history but do not double count.

Capacity fields:

- `surface_m2`
- `rack_count`
- `it_mw`
- `grid_mw`
- `generator_mw`
- `contracted_power`
- `marketing_capacity`
- `actual_consumption`

Never collapse these fields into a single "MW" number.

---

## 6. 推荐执行顺序（recommended pipeline）

1. Confirm manifest division: one delivery row for `New Caledonia`.
2. Build official seeds: `gouv.nc`, `juridoc.gouv.nc`, `congres.nc`, provinces, `data.gouv.nc`, `marchespublics.nc`.
3. Build telecom seeds: OPT-NC, CITIUS historical filings, DINUM, Autorité de la concurrence, ANFR, APNIC/BGP.
4. Build power/cable context: Enercal, EEC-Engie, GONDWANA/PICOT landing and route evidence.
5. Run full commune sweep only after an entity/project signal appears; most communes will have no facility beyond access-network equipment.
6. Promote a record only when source grade, status, owner, location, and capacity fields are separately supported.

---

## 7. Source index

- Government: https://gouv.nc
- JONC/Juridoc: https://juridoc.gouv.nc
- Congrès: https://www.congres.nc
- Haut-commissariat: https://www.nouvelle-caledonie.gouv.fr
- Province Sud: https://www.province-sud.nc
- Province Nord: https://www.province-nord.nc
- Province des Îles Loyauté: https://www.province-iles.nc
- Open Data NC: https://data.gouv.nc
- ISEE: https://www.isee.nc
- DITTT: https://www.dittt.gouv.nc
- OPT-NC commercial: https://www.opt.nc
- OPT-NC corporate/news: https://office.opt.nc
- ANFR outre-mer regulation: https://www.anfr.fr/outre-mer/reglementation
- Autorité de la concurrence NC: https://autorite-concurrence.nc
- Enercal: https://www.enercal.nc
- EEC-Engie: https://www.eec-engie.nc
- Marchés publics NC: https://marchespublics.nc
- Province Nord procurement: https://marchespublics.province-nord.nc
- APNIC Whois: https://wq.apnic.net
- TeleGeography Submarine Cable Map: https://www.submarinecablemap.com
- AWS regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- OVHcloud datacenters: https://www.ovhcloud.com/en/datacenter/
