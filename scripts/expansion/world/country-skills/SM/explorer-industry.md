# SM Explorer Industry — 圣马力诺数据中心行业侧发现方法

Date verified: 2026-08-12. Country: **SM San Marino（圣马力诺共和国）**. Division model: **municipality / castello**. `world-manifest.jsonl` confirms exactly **9 divisions**: Acquaviva; Chiesanuova; Domagnano; Faetano; Fiorentino; Borgo Maggiore; Citta di San Marino; Montegiardino; Serravalle. Companion file: `explorer-official.md`. 本文件覆盖行业侧发现：运营商/设施扫描、本地媒体、行业媒体、聚合目录、互联目录、托管商、投资促进渠道、云信号、加密/ICT 友好营销证据，以及按 castello 的枚举策略。

Reliability grades: **A** = 官方/运营商/监管/政府媒体；**B** = 可靠行业媒体、本地报纸、厂商/客户案例、强互联证据；**C** = 聚合目录、市场页、转售商声明、社交帖、营销叙事；**U** = 未证实传言。行业研究负责找线索，最终设施记录优先 A/B 佐证。

## 0. 行业发现框架（Industry Discovery Frame）

- 圣马力诺是微型市场：约 61 km2、约 3.4 万人口、一个主要本地电信运营商 SMT/TIM San Marino、一个国有公用事业 AASS、有限工业区和少量本地 IT 供应商。预期产出低，确认质量比数量重要。
- **SMT/TIM San Marino 有公开官方 Data Center/Housing 服务页**。这使“运营商商业 housing/cloud-hosting 服务存在”为 **A**。但官方页面未充分公开机房精确地址、Tier 认证、功率或 castello；这些字段必须另证。
- SMT 官方/并行域可见事实：`smt.sm` 服务入口将 Data Center 与 fixed/mobile/internet 并列；`smt.sm/en/services/easy-data-center` 提供 Easy DATA CENTER；`telecomitalia.sm/business/prodotto/housing/` 描述 IDC/Housing、冗余光纤、MIX Milano、UPS、发电机、消防与 24x7 监控。
- “SMT Tier III / Rovereta / Serravalle”目前只能作为 **U/C search cue**。除非找到 SMT、B.U.、AASS、可靠媒体或 Uptime/认证机构证据，否则不要写成事实。
- 加密/金融科技、SMI 创新、Xago、DLT 监管、在线博彩等是需求侧信号。设施计数必须和政策营销分离。
- 圣马力诺无 hyperscale cloud region；附近云区域在意大利米兰/都灵。任何“San Marino cloud”需核实物理托管地。

## 1. 本地媒体与行业媒体（Local Press and Trade Press）

| Source | URL | Language | 用途 | 分级 |
|---|---|---|---|---|
| San Marino RTV | https://www.sanmarinortv.sm/ | IT | 政府、电信、AASS、ICT、DLT 报道 | B |
| Libertas | https://www.libertas.sm/ | IT | 本地政治/经济/科技新闻 | B |
| San Marino Fixing | https://sanmarinofixing.com/ | IT | 商业、企业、注册、ICT 线索 | B |
| L'Informazione di San Marino | https://www.linformazione.sm/ | IT | 本地新闻线索 | B/C，逐条核验 |
| Corriere Romagna / RiminiToday / Il Resto del Carlino | 各官网 | IT | 里米尼-圣马力诺跨境网络、能源、投资 | B |
| DatacenterDynamics | https://www.datacenterdynamics.com/ | EN | 数据中心行业新闻；SM 预期稀少 | B |
| Capacity Media | https://www.capacitymedia.com/ | EN | 连接性/边缘市场线索 | B |
| CoinDesk / Cointelegraph / Finance Magnates | 各官网 | EN | Ripple/SMI/Xago/crypto 叙事 | B for named company fact; C for hype |

检索模板：

```text
site:sanmarinortv.sm "centro dati"
site:sanmarinortv.sm "data center"
site:libertas.sm "centro dati"
site:libertas.sm "San Marino Telecom" "data center"
site:sanmarinofixing.com "data center"
site:linformazione.sm "centro elaborazione dati"
"San Marino Telecom" "data center"
"TIM San Marino" "Housing" "Data Center"
"San Marino" "data center" Rovereta
"San Marino" "data center" Serravalle
"San Marino" blockchain decreto
"San Marino Innovation" Ripple
Xago "San Marino"
```

## 2. 运营商、托管与设施扫描（Operator, Hosting and Facility Sweep）

| 公司/机构 | 查找目标 | 最佳核实路径 | 种子分级 |
|---|---|---|---|
| SMT / TIM San Marino | Data Center/Housing/Cloud/Hosting 产品、设施技术、地址、容量、SLA | `smt.sm`, `telecomitalia.sm`, B.U., AASS, PeeringDB, RIPE | A for service existence; location/capacity as evidenced |
| AASS | SCADA/utility CED、电力大用户接入、机电采购 | AASS pages, Autorità Energia, B.U. | C until named |
| GovSM / UITEDS / public administration | e-government CED、digital identity、cloud/hosting tenders | GovSM, B.U., procurement | C |
| BCSM and banks | Internal CED/DR, outsourcing, business continuity | BCSM, bank reports, supplier cases | C |
| ISS | Healthcare/social security IT rooms | ISS procurement/news | C |
| San Marino Innovation ecosystem | DLT operators, high-tech firms, incubators | SMI, Registro Imprese, press | B/C for companies; U/C for facilities |
| Xago and crypto/fintech firms | Company presence, infrastructure claims, ASN/IP | company pages, AIF/BCSM, RIPE, hosting traces | B for company; U/C for facility |
| Online gaming/license holders | Regulated IT demand | B.U., regulator/government, industry media | C |
| UniRSM | Research/teaching server rooms | university pages/procurement | C |
| Local IT/MSP/hosting providers | VPS/cloud/hosting claims | ASN, terms, support address, facility address | C |

扫描纪律：`<company> "centro dati"`, `<company> CED`, `<company> "sala server"`, `<company> cloud`, `<company> hosting`, `<company> "disaster recovery"`。无物理地址/castello 与运营状态前，不得把公司计为设施。

## 3. 聚合目录与互联目录（Aggregators and Interconnection Directories）

| Source | URL | 用途 | 分级 |
|---|---|---|---|
| Data Center Map | https://www.datacentermap.com/san-marino/ | 国家页种子；可能列 SMT 或空结果 | C |
| datacenters.com | https://www.datacenters.com/ | 站内 San Marino / Rimini / Milan 查询 | C |
| Baxtel | https://www.baxtel.com/ | 站内 San Marino 查询 | C |
| Cloudscene / colocation marketplaces | 各官网 | 市场线索，易复用 HQ 地址 | C |
| PeeringDB AS15433 | https://www.peeringdb.com/net/8514 | Telecom Italia San Marino ASN、traffic/interconnection | B |
| RIPE DB | https://apps.db.ripe.net/db-web-ui/ | ASN、route、organisation、contacts | B |
| IXPDB | https://ixpdb.euro-ix.net/ | 国内 IXP 负向检查 | B |
| MIX Milano | https://www.mix-it.net/en/exchange/milano/ | SMT/TIM San Marino 官方页提到的 Milan peering 目的地 | A/B |

聚合目录只作发现工具。容量、Tier、地址、运营状态未经运营商、官方、AASS、B.U. 或强二级来源确认，不得高于 C。重复的 SMT/TIM San Marino 条目需要去重。

## 4. 连接性、海缆与边缘信号（Connectivity, Cable and Edge Signals）

- 圣马力诺无海缆登陆站；国际连接依赖经意大利方向的光纤回程。
- SMT/TIM San Marino Housing 页面称 Data Center 外联使用冗余光纤，主要 10 Gb/s 光承载，并在 MIX Milano 有直接连接。这是 A 级运营商自述，可作为连接性事实。
- PeeringDB 显示 Telecom Italia San Marino / AS15433，可作为 ASN 与互联线索；设施位置字段仍需逐条核实。
- 常见公开 IXP 目录中预期无圣马力诺国内 IXP。季度复查 IXPDB、PeeringDB、Internet Exchange Map。
- `.sm` ccTLD、域名托管、邮件服务不等于本地机房。

检索模板：

```text
"San Marino Telecom" PeeringDB
"Telecom Italia San Marino" AS15433
"San Marino Telecom" RIPE
"TIM San Marino" MIX Milano
"San Marino Telecom" "fibra ottica" "Data Center"
"San Marino" IXP
"San Marino" internet exchange
"San Marino" "cross-border fiber"
```

## 5. 投资、创新与经济发展渠道

| Source | URL | 用途 | 分级 |
|---|---|---|---|
| San Marino Innovation | https://www.sanmarinoinnovation.com/ | DLT/innovation companies, incubators, certified operators | A for institution; B/C for promoted projects |
| SMI DLT page | https://www.sanmarinoinnovation.com/eng-blockchain | DLT Operators Register regulation 001/2024 and Decree 138/2024 cue | A |
| Camera di Commercio / ASE | https://www.camcom.sm/ | Business setup, sector clusters, investment signals | A/B |
| Registro Imprese | https://registroimprese.cc.sm/ | company existence and addresses | A/B |
| Ministry/GovSM foreign/economic pages | https://www.esteri.sm/ and https://www.gov.sm/ | international cooperation, investment policy | A/B |
| Visit San Marino / brand pages | https://www.visitsanmarino.com/ | background only | C |

投资促进声明不是设施证据。真实数据中心项目通常还应出现在 SMT、B.U.、AASS 电网规划、建设/采购裁决或可靠设施报道中。

## 6. 加密/ICT 友好定位证据（Crypto/ICT-Friendly Marketing Evidence）

| 证据 | 当前核实结果 | 分级 |
|---|---|---|
| SMI innovation hub | 官方站点在线，定位为数字技术/创新枢纽 | A |
| 2019 Blockchain Decree | SMI 2019 press release online；B.U. PDF 搜索结果显示 blockchain decree text；常见编号为 Decreto Delegato 23 maggio 2019 n.86 | A when B.U. PDF captured |
| 2024 DLT framework | SMI `eng-blockchain` 页面引用 Regulation on the Register of DLT Operators 001/2024 under Delegated Decree No. 138 of 29 Aug 2024, in force 2 Oct 2024 | A |
| Ripple / SMI / Xago narrative | 多由加密/金融媒体和公司材料转述；需交叉 Registro Imprese/AIF/BCSM | B for company facts; C for market narrative |
| Virtual assets AML/VASP | AIF、BCSM、Consiglio/B.U. 法律文本可核验 `asset virtuali` 与服务商定义 | A/B |
| Crypto Summit / metaverse / low-tax setup marketing | SMI/consultancy/press pages可作为营销信号 | B/C |

判读规则：

1. 政策友好不等于本土算力供给。
2. 加密/金融科技公司存在不等于在圣马力诺运行机房。
3. 核查每家公司 ASN、IP 地理、托管条款、支持地址、客户案例。
4. 只有具名圣马力诺境内设施证据才进入设施清单；其他放入 demand/policy signal。

## 7. Query Templates（含 Castello 变体）

意大利语：

```text
"centro dati" "San Marino"
"centro elaborazione dati" "San Marino"
"sala server" "San Marino"
"data center" "San Marino"
"housing" "TIM San Marino"
"Easy DATA CENTER" "San Marino"
"San Marino Telecom" "data center"
"Telecom Italia San Marino" "Housing"
"San Marino" cloud sovrano
"San Marino" colocation
"San Marino" "disaster recovery"
"San Marino" CED governo
"San Marino" "asset virtuali"
"San Marino" "operatori DLT"
Xago "San Marino"
AASS "centro dati"
AASS allacciamento "media tensione"
"San Marino" hosting aziende
"San Marino" VPS server dedicato
"San Marino" gioco online server
```

英语/中文：

```text
"San Marino" data center investment
"San Marino" colocation
"San Marino" sovereign cloud
"San Marino Telecom" data centre
"San Marino" crypto exchange hosting
"San Marino" blockchain-friendly
圣马力诺 数据中心
圣马力诺 机房 托管
圣马力诺 区块链 加密
```

## 8. 分区枚举矩阵（Enumeration Matrix per Division）

与 `world-manifest.jsonl` 的 9 个 castelli 严格对齐。圣马力诺体量小，Serravalle/Dogana/Rovereta 与 Acquaviva/Gualdicciolo 是商业/工业重点，但每个 castello 都必须跑负向检查。

| Castello | 特征/重点 | 查询模板 | 预期 |
|---|---|---|---|
| Acquaviva | Gualdicciolo 边境工业/SMT 联系地址线索；确认办公 vs 设施 | `Acquaviva "centro dati"`; `Gualdicciolo hosting`; `Gualdicciolo "data center"`; `site:smt.sm Gualdicciolo` | 0-1 C/A if official |
| Chiesanuova | 住宅/低密度 | `Chiesanuova "centro dati"`; `Chiesanuova "sala server"` | 0 |
| Domagnano | SMI/创新企业地址线索 | `Domagnano "centro dati"`; `Domagnano "startup innovativa"`; `site:sanmarinoinnovation.com Domagnano` | 0-1 C |
| Faetano | 农村/低密度 | `Faetano "centro dati"`; `Faetano CED` | 0 |
| Fiorentino | 工业区/企业 IT | `Fiorentino "centro dati"`; `Fiorentino data center`; `Fiorentino "zona industriale" informatica` | 0-1 C |
| Borgo Maggiore | 商业、银行、TIM corporate/store addresses | `"Borgo Maggiore" "centro dati"`; `"Borgo Maggiore" banca server`; `"TIM San Marino" "Borgo Maggiore"` | 0-1 C unless facility located |
| Citta di San Marino | 政府、议会、BCSM、Garante | `"Città di San Marino" "centro elaborazione dati"`; `"San Marino città" CED`; `BCSM "centro dati"` | 0-1 B/C internal |
| Montegiardino | 最小 castello | `Montegiardino "centro dati"`; `Montegiardino CED` | 0 |
| Serravalle | Dogana/Rovereta/Galazzano/Ciarulla 工业商业区；SMT Tier/Rovereta rumor needs proof | `Rovereta "data center"`; `Dogana "centro dati"`; `Serravalle hosting`; `"San Marino Telecom" Rovereta` | 0-2 C/U until verified |

通用模板：`"{castello}" ("centro dati" OR "data center" OR "sala server" OR CED OR hosting)`；并对每个 castello 跑 `site:libertas.sm "{castello}"` 与 `site:sanmarinortv.sm "{castello}"`。

## 9. 分级规则（Grading Rules）

- **A**：SMT/TIM San Marino 官方 Data Center/Housing 页面、B.U./采购/裁决、AASS 官方文件、监管登记、官方云区域页。
- **B**：RTV/Libertas/Fixing/Corriere Romagna 等可靠本地媒体、DCD/Capacity 等行业媒体、具名高管访谈、PeeringDB/RIPE、厂商案例。
- **C**：Data Center Map/datacenters.com/Baxtel/Cloudscene、市场页、转售商/HQ 地址推断、营销叙事、加密博客、社交帖、招聘广告。
- **U**：未证实传言，仅作检索提示词。

示例：SMT/TIM San Marino 官方 Housing 页面为 **A**（service/facility description）；PeeringDB AS15433 为 **B**（connectivity seed）；“Rovereta Tier III”若无可打开来源为 **U/C**；“San Marino crypto-friendly attracts data centers”为 **C**（marketing, no facility）。

## 10. 防误报（False Positives）

- 政策/营销 ≠ 设施：SMI、DLT 法令、Xago、元宇宙宣传、低税率、在线博彩牌照都不构成本地机房证据。
- 品牌地址 ≠ 机房地址：公司总部、门店、注册地、`.sm` 域名、support address 不能直接落位为 data center。
- 意大利邻近噪声：Rimini、Bologna、Milan、Turin 项目容易被误归圣马力诺；检查行政区划和物理地址。
- 聚合目录重复：同一 SMT/TIM 条目可能在多个目录重复；去重后再评估。
- Tier/认证：Tier III/Tier IV 必须由 Uptime/运营商/可靠建设案例明确支持。
- 季度复查：SMT/TIM San Marino、AASS、B.U.、GovSM、SMI、AIF、BCSM、本地媒体、PeeringDB、IXPDB、聚合目录、AWS/Azure/GCP/OCI 官方区域列表。
