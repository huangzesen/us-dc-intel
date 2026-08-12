# SM Explorer Official — 圣马力诺数据中心官方口径枚举方法

Date verified: 2026-08-12. Country: **SM San Marino（圣马力诺共和国）**. Division model: **municipality / castello**. `world-manifest.jsonl` confirms exactly **9 divisions**: **Acquaviva; Chiesanuova; Domagnano; Faetano; Fiorentino; Borgo Maggiore; Citta di San Marino; Montegiardino; Serravalle**. Scope: 官方与监管口径方法，用于发现圣马力诺境内商业数据中心、电信机房、公共部门 CED/CPD、托管/云、灾备、AI/HPC 及大型服务器机房。Companion file: `explorer-industry.md`.

Reliability grades（按事实逐条打分，不按项目整体打分）:

- **A** = 一级证据：公共机构、官方公报/法律库、监管登记、公用事业、运营商自有设施/服务页、政府采购记录、官方云区域页。
- **B** = 强二级证据：可靠本地/行业媒体、具名高管访谈、厂商案例研究、PeeringDB/RIPE 等互联目录。
- **C** = 弱线索：聚合目录、市场页、转售商声明、办公地址推断、招聘广告、投资促进叙事。
- **U** = 未证实传言或纯检索提示词。

## 0. 结构事实（Structure Facts）

- 圣马力诺为内陆微型国家，面积约 61 km2，完全被意大利包围，官方语言为意大利语；不是欧盟成员，但使用欧元并与欧盟存在紧密制度衔接。
- 行政区划必须按 manifest 的 9 个 castelli 逐一覆盖。注意 manifest 使用 ASCII `Citta di San Marino`；检索时同时跑 `Città di San Marino`、`San Marino città`、`Citta di San Marino`。
- 圣马力诺没有国家级数据中心登记册，也没有独立的数据中心监管机构。官方枚举应组合：Bollettino Ufficiale、Consiglio Grande e Generale 法律库、GovSM、AASS 电网/采购、SMT/TIM San Marino 运营商页面、AIF/BCSM/SMI 金融与 DLT 监管、公共采购和地方媒体。
- 城市规划与建设许可主要是国家层面材料；Giunte di Castello 是地方行政线索，不应被当作主要许可库。
- 当前可确认的核心设施事实：**SMT / TIM San Marino 官方页面公开提供 Data Center / Housing / Cloud-Hosting-Housing 服务**，并描述 Data Center、光纤冗余、MIX Milano 连接、UPS、发电机、消防、24x7 监控等。这支持“运营商数据中心服务存在”为 **A**；若具体地址或 castello 未由设施页点名，不得擅自落位。
- “SMT Tier III / Rovereta / Serravalle”应作为 **U/C 检索线索**处理，除非找到 SMT、B.U.、AASS 或可靠媒体明确文本。不要把未核实的 Tier 等级、面积、功率、地址写成设施事实。
- “加密/ICT 友好”是政策与营销事实，不等于本地数据中心设施。SMI、DLT 法令、Xago、VASP/AML 监管均应记录为需求侧/政策侧信号，设施归属须另证。

## 1. 已验证官方来源（Official Sources）

| 来源 | Verified URL | 用途 | 分级与备注 |
|---|---|---|---|
| GovSM 政府门户 | https://www.gov.sm/ | 政府机构、公共服务、Giunte di Castello、采购/政策入口 | **A**；简单 HEAD 可能返回 403，网页可检索 |
| Bollettino Ufficiale | https://www.bollettinoufficiale.sm/ | 法律、decreti、bandi、aggiudicazioni | **A**；根 URL 重定向到 `/on-line/home.html` |
| Consiglio Grande e Generale | https://www.consigliograndeegenerale.sm/ | 议会、法律/规范文本、PDF 附件 | **A** |
| Ufficio Informatica, Tecnologia, Dati e Statistica / Statistica | https://www.statistica.sm/ | 人口、企业、能源/ICT 背景 | **A**；GovSM/Magnolia 页面可能限制 HEAD |
| AASS | https://www.aass.sm/site/home.html | 电力、水、气及公用事业采购/资料 | **A** |
| AASS 电力信息页 | https://www.aass.sm/site/home/elettricita/informazioni-generali.html | 电力进口与 132 kV 接入背景 | **A**；页面说明电力通过 132,000 V 高压线路进入圣马力诺 |
| San Marino Telecom / SMT | https://www.smt.sm/ | 运营商服务、企业 Data Center 产品 | **A** |
| SMT Easy DATA CENTER | https://www.smt.sm/en/services/easy-data-center | Cloud / Hosting / Housing 服务、数据中心面积线索 | **A**；官方搜索结果显示 2,000 m2 data center in San Marino |
| TIM San Marino Housing | https://www.telecomitalia.sm/business/prodotto/housing/ | Housing/IDC 设施描述、冗余光纤、MIX、UPS、发电机 | **A**；同一运营体系的官方旧/并行域 |
| AIF | https://www.aif.sm/ | AML/CFT、virtual assets/VASP 监管线索 | **A** |
| BCSM | https://www.bcsm.sm/ | 金融监管、银行/支付机构材料 | **A** |
| San Marino Innovation | https://www.sanmarinoinnovation.com/ | 创新、DLT、区块链登记/规则 | **A**（机构/自有声明） |
| Garante Privacy | https://www.garanteprivacy.sm/ | 数据保护、跨境数据/云合规背景 | **A** |
| Camera di Commercio / Agenzia Sviluppo Economico | https://www.camcom.sm/ | 企业服务、行业/投资促进 | **A/B** |
| Registro Imprese | https://registroimprese.cc.sm/ | 公司登记检索入口 | **A/B**；部分内容可能需登录/付费 |
| Autorità Energia | https://www.autoritaenergia.sm/ | 能源监管、PEN、年度报告 | **A** |

不要再把 `https://www.cc.sm/` 作为主 URL；当前可用入口是 `camcom.sm`，注册查询入口为 `registroimprese.cc.sm`。

## 2. 官方检索词汇表（Search Vocabulary）

意大利语 primary:

```text
centro dati
centro elaborazione dati
data center
datacenter
housing
hosting
cloud
cloud sovrano
sala server
sala macchine
CED
CPD
disaster recovery
continuità operativa
Tier III
Tier IV
Uptime
MW
MVA
cabina elettrica
sottostazione
trasformatore
gruppo elettrogeno
UPS
alimentazione elettrica
allacciamento
media tensione
fibra ottica
MIX Milano
bando di gara
aggiudicazione
appalto
tecnologie basate su registri distribuiti
tecnologia blockchain
asset virtuali
valuta virtuale
fornitori di servizi relativi ad asset virtuali
operatori DLT
```

英语 / 中文辅助：`data center`, `datacentre`, `colocation`, `sovereign cloud`, `server room`, `business continuity`, `IXP`, `cross-border fiber`, 数据中心, 机房, 托管, 云, 灾备, 区块链, 虚拟资产。

## 3. 官方查询模板（Official Query Templates）

```text
site:gov.sm "centro dati"
site:gov.sm "centro elaborazione dati"
site:gov.sm "data center"
site:gov.sm "sala server"
site:gov.sm "cloud"
site:gov.sm appalto hosting
site:gov.sm appalto CED
site:bollettinoufficiale.sm "centro dati"
site:bollettinoufficiale.sm "centro elaborazione dati"
site:bollettinoufficiale.sm "data center"
site:bollettinoufficiale.sm "sala server"
site:bollettinoufficiale.sm "disaster recovery"
site:bollettinoufficiale.sm "gruppo elettrogeno" informatica
site:bollettinoufficiale.sm "tecnologie basate su registri distribuiti"
site:consigliograndeegenerale.sm "asset virtuali"
site:consigliograndeegenerale.sm "tecnologie basate su registri distribuiti"
site:aass.sm "centro dati"
site:aass.sm "allacciamento" "media tensione"
site:aass.sm "cabina elettrica"
site:smt.sm "data center"
site:smt.sm hosting housing cloud
site:telecomitalia.sm "Data Center" "San Marino"
site:bcsm.sm "continuità operativa"
site:bcsm.sm "asset virtuali"
site:aif.sm "asset virtuali"
site:sanmarinoinnovation.com "operatori DLT"
site:camcom.sm "servizi digitali"
site:registroimprese.cc.sm informatica
```

## 4. 电力与公用事业证据（Energy and Utility Evidence）

优先来源：AASS、Autorità Energia、B.U.、GovSM。AASS 电力信息页是关键背景：圣马力诺电力通过多条 132 kV 高压线路接入并由 AASS 配电。对任何新增数据中心负荷，应尝试寻找：

- `allacciamento`, `media tensione`, `cabina`, `sottostazione`, `trasformatore`, `potenza disponibile`, `gruppo elettrogeno`, `UPS`, `raffreddamento`.
- AASS 年报/透明度/采购中的电网升级、大用户接入、机电维护合同。
- B.U. 中有关发电机、消防、建设许可、公共 ICT 采购的法令或裁决。

电力纪律：功率、等级、PUE、机房面积、机柜数、冗余等级只有在运营商页面、AASS/B.U. 文件或厂商案例明确时才能记录为 A/B。聚合目录和媒体数字默认为 C。

## 5. 电信与连接性证据（Telecom and Connectivity Evidence）

| 来源 | URL | 用途 | 分级 |
|---|---|---|---|
| SMT / San Marino Telecom | https://www.smt.sm/ | 当前运营商品牌、企业服务入口 | A |
| SMT Easy DATA CENTER | https://www.smt.sm/en/services/easy-data-center | Data Center / Cloud / Hosting / Housing 官方服务页 | A |
| TIM San Marino Housing | https://www.telecomitalia.sm/business/prodotto/housing/ | IDC/Housing 技术描述：冗余光纤、MIX、UPS、发电机、消防、24x7 监控 | A |
| PeeringDB AS15433 | https://www.peeringdb.com/net/8514 | Telecom Italia San Marino ASN、流量与互联线索 | B |
| RIPE DB | https://apps.db.ripe.net/db-web-ui/ | ASN/route/organisation/contact 核验 | B |
| MIX Milano | https://www.mix-it.net/en/exchange/milano/ | SMT 页面提到的 Milan peering 目的地背景 | A/B |
| IXPDB | https://ixpdb.euro-ix.net/ | 国内 IXP 负向检查 | B |

SMT/TIM San Marino 的 Housing 页面可支持“商业 housing/colocation 服务存在”。但页面页脚地址或公司总部地址不自动等于机房地址；设施 castello 需要页面正文、采购、AASS 或可靠媒体明确定位。

## 6. 金融、ICT、DLT 与加密友好证据

本节记录政策/需求侧信号，不能直接计入设施。

| 事实 | Verified source / query | 分级 |
|---|---|---|
| San Marino Innovation 是官方创新/数字技术机构 | https://www.sanmarinoinnovation.com/ | A |
| 2019 Blockchain/DLT 法规营销 | SMI press release `Al Via il Decreto Blockchain della Repubblica di San Marino` | A（SMI 自有发布）/ A if B.U. PDF cited |
| 2019 Decreto Delegato Blockchain | B.U. PDF 搜索结果显示 `NORME SULLA TECNOLOGIA BLOCKCHAIN PER LE IMPRESE`；常见引文为 Decreto Delegato 23 maggio 2019 n.86 | A，逐次拉取 PDF 核实编号 |
| 2024 DLT 框架 | SMI DLT page cites Regulation on the Register of DLT Operators 001/2024 under Delegated Decree No. 138 of 29 Aug 2024 | A |
| Virtual assets / VASP AML changes | Consiglio/B.U. PDFs and AIF materials; search `asset virtuali`, `fornitori di servizi relativi ad asset virtuali` | A/B |
| BCSM financial supervision | https://www.bcsm.sm/ | A |
| Xago / Ripple / crypto exchange claims | Industry/press + company pages only unless official registration is found | B for company/policy; U/C for facilities |

判读规则：区块链法令、SMI 入驻、金融科技公司注册、低税率宣传只说明政策环境或潜在需求。只有出现圣马力诺境内具名机房、运营商设施页、AASS 电网记录、B.U. 采购/许可或可靠设施报道，才可进入设施表。

## 7. 采购证据（Procurement Evidence）

公共采购入口以 B.U. 和各机构站点为主；不要假设有统一完整电子采购平台。检索重点：

```text
site:bollettinoufficiale.sm "bando di gara" informatica
site:bollettinoufficiale.sm "aggiudicazione" informatica
site:bollettinoufficiale.sm "centro elaborazione dati"
site:bollettinoufficiale.sm "sala server"
site:bollettinoufficiale.sm "disaster recovery"
site:bollettinoufficiale.sm "continuità operativa"
site:bollettinoufficiale.sm "climatizzazione" informatica
site:bollettinoufficiale.sm "gruppo elettrogeno"
site:gov.sm appalti cloud
site:aass.sm bando informatica
site:smt.sm gara appalto
site:iss.sm "sala server"
site:bcsm.sm "continuità operativa"
```

政府、ISS、BCSM、银行和 AASS 内部 CED 可能存在，但敏感且未必公开。没有采购、预算、官方公告或设施地址前，不得高于 C。

## 8. 官方云区域负向检查（Official Cloud-Region Negative Checks）

Verified 2026-08-12:

| Provider | Official source | San Marino result | Nearest/relevant Italy region |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No San Marino region | Europe (Milan) `eu-south-1` |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No San Marino region | Italy North `italynorth`, physical location Milan |
| Google Cloud | https://docs.cloud.google.com/compute/docs/regions-zones and https://cloud.google.com/about/locations | No San Marino region | Milan `europe-west8`; Turin `europe-west12` also appears in Google/Oracle interconnect context |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No San Marino region | Italy Northwest (Milan), Italy North (Turin) |

每次扫描重新确认官方列表。云区域负向检查用于防止把“San Marino cloud/sovereign cloud”营销误判为本地 hyperscale region。

## 9. Division Coverage Matrix（9 Castelli）

| Castello per manifest | 官方扫描重点 | 查询模板 | 预期 |
|---|---|---|---|
| Acquaviva | Gualdicciolo/边境工业与 SMT 联系地址线索；需区分办公/节点/机房 | `Acquaviva "centro dati"`; `Gualdicciolo "data center"`; `site:smt.sm Gualdicciolo` | 0-1，需 A/B 定位 |
| Chiesanuova | 小型住宅/本地公共设施 | `Chiesanuova "centro dati"`; `Chiesanuova CED` | 0 |
| Domagnano | SMI 地址与创新企业；公司存在不等于设施 | `Domagnano "centro dati"`; `site:sanmarinoinnovation.com Domagnano` | 0-1 C |
| Faetano | 低密度区域 | `Faetano "centro dati"`; `Faetano "sala server"` | 0 |
| Fiorentino | 工业区/企业 IT | `Fiorentino "centro dati"`; `Fiorentino "zona industriale" informatica` | 0-1 C |
| Borgo Maggiore | 商业、银行、TIM San Marino corporate/store addresses | `"Borgo Maggiore" "centro dati"`; `"Borgo Maggiore" banca CED`; `site:telecomitalia.sm "Borgo Maggiore"` | 0-1 C unless facility located |
| Citta di San Marino | 政府、议会、BCSM、Garante | `"Città di San Marino" "centro elaborazione dati"`; `BCSM "continuità operativa"`; `gov.sm CED` | 0-1 B/C internal |
| Montegiardino | 最小 castello，低预期 | `Montegiardino "centro dati"`; `Montegiardino CED` | 0 |
| Serravalle | Dogana/Rovereta/Galazzano/Ciarulla 工业与商业区；SMT Tier/Rovereta 传言须核实 | `Serravalle "data center"`; `Rovereta "data center"`; `Dogana "centro dati"`; `"San Marino Telecom" Rovereta` | 0-2，未证实前 C/U |

覆盖规则：每轮结果表必须列出 9 个 castelli，即使结果为 negative checked。不得只扫描 Serravalle/Dogana。

## 10. 记录格式（Evidence Capture）

每个候选设施至少记录：

- `name`, `operator`, `service type`（housing/cloud/internal CED/DR/edge/HPC）
- `castello`（未知时写 `unknown within SM`，不要推断）
- `address evidence`（source URL + 引文摘要）
- `power/cooling/connectivity evidence`
- `customer-facing?`
- `grade per fact`
- `negative checks`（AASS/B.U./SMT/PeeringDB/RIPE/aggregators）

最终枚举预期：**1 个 A 级运营商 data-center/housing 服务事实（SMT/TIM San Marino），加若干 C 级内部机房/政策需求线索**。不要用聚合目录或加密营销把全国设施数放大。
