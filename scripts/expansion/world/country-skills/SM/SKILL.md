---
name: sm-datacenter-methodology
location: scripts/expansion/world/country-skills/SM/SKILL.md
description: 圣马力诺数据中心查询方法论（San Marino datacenter discovery & audit methodology）——双线来源（官方/监管/云管线 + 行业/厂商/媒体发现）与 municipality/castello 九堡模型下的设施枚举规则。
---

# SM · 圣马力诺数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：发现圣马力诺（San Marino, SM）境内商业数据中心、电信机房、公共部门 CED/CPD、托管/云、灾备、AI/HPC 及大型服务器机房。双线方法论：`explorer-official.md`（官方/监管/云管线）与 `explorer-industry.md`（行业/厂商/媒体发现），均为 codex 审核定稿。划分模型（per manifest）：**municipality / castello** — 9 个一级划分：Acquaviva、Chiesanuova、Domagnano、Faetano、Fiorentino、Borgo Maggiore、Citta di San Marino、Montegiardino、Serravalle。评审日期：2026-08-12。

## 入口

| 入口 | 管线 | 内容 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线 | 政府门户/法律库/公用事业/运营商设施页/金融与 DLT 监管/采购证据、意大利语检索词汇、官方查询模板、电力与连接性证据、官方云区域负向检查、9 castelli 覆盖矩阵 |
| `explorer-industry.md` | 行业/厂商/媒体发现 | 运营商与托管扫描、本地/行业媒体、聚合目录与互联目录、投资创新渠道、加密/ICT 友好营销证据、分堡枚举矩阵、分级与防误报规则 |

## 核心结构事实

1. **行政区划模型**：municipality / castello，9 个一级划分（见入口表）。manifest 用 ASCII `Citta di San Marino`；检索时同时跑 `Città di San Marino`、`San Marino città`。Serravalle/Dogana/Rovereta 与 Acquaviva/Gualdicciolo 是商业/工业重点，但每个 castello 都必须跑负向检查，不得只扫 Serravalle/Dogana。
2. **注册库现状**：圣马力诺**没有国家级数据中心登记册，也没有独立的数据中心监管机构**（内陆微型国家，约 61 km²，完全被意大利包围，官方语言意大利语；非欧盟成员但使用欧元并与欧盟制度紧密衔接）。官方枚举组合：Bollettino Ufficiale、Consiglio Grande e Generale 法律库、GovSM、AASS 电网/采购、SMT/TIM San Marino 运营商页面、AIF/BCSM/SMI 金融与 DLT 监管、公共采购和本地媒体。
3. **法律与监管**：城市规化与建设许可主要是国家层面材料；Giunte di Castello 是地方行政线索，不应作为主要许可库。AIF（AML/CFT、虚拟资产/VASP）、BCSM（金融监管）、SMI/DLT 法规（2019 Blockchain Decree、2024 DLT framework：Delegated Decree 138 of 29 Aug 2024、Regulation on Register of DLT Operators 001/2024）均为政策/需求侧信号，不直接计入设施。
4. **互联与云**：圣马力诺无海缆登陆站，国际连接依赖经意大利方向的光纤回路；SMT/TIM San Marino Housing 页声称 Data Center 外联使用冗余光纤、主要 10 Gb/s 光承载，并在 MIX Milano 有直接连接（A 级运营商自述）。PeeringDB AS15433（Telecom Italia San Marino）为互联线索；国内 IXP 预期无。官方云区域负向检查（AWS/Azure/GCP/OCI 官方列表）均无 San Marino 区域，最近区域在意大利米兰/都灵（eu-south-1、italynorth、europe-west8、Europe Milan/Turin OCI）——每次扫描重新确认官方列表。
5. **设施/项目种子**：SMT/TIM San Marino 官方页面公开提供 Data Center / Housing / Cloud-Hosting-Housing 服务（smt.sm/en/services/easy-data-center 显示 2,000 m² data center 线索；telecomitalia.sm/business/prodotto/housing/ 描述冗余光纤、MIX Milano、UPS、发电机、消防、24x7 监控）——支持“运营商数据中心服务存在”为 **A**；具体地址/castello 未被设施页点名时不得擅自落位。“SMT Tier III / Rovereta / Serravalle” 只能作为 **U/C 检索线索**，除非找到 SMT、B.U.、AASS 或可靠媒体明确文本。政府/ISS/BCSM/银行/AASS 内部 CED 可能存但敏感未公开，无采购/预算/官方公告/设施地址前不得高于 C。
6. **语言与词汇**：意大利语 primary——`centro dati`、`centro elaborazione dati`、`data center`、`housing`、`hosting`、`cloud`、`cloud sovrano`、`sala server`、`sala macchine`、`CED`、`CPD`、`disaster recovery`、`continuità operativa`、`Tier III/IV`、`MW/MVA`、`cabina elettrica`、`sottostazione`、`gruppo elettrogeno`、`UPS`、`allacciamento`、`media tensione`、`fibra ottica`、`MIX Milano`、`bando di gara`、`aggiudicazione`、`appalto`、`tecnologie basate su registri distribuiti`、`asset virtuali`、`operatori DLT`；英语/中文辅助：`colocation`、`sovereign cloud`、`server room`、`business continuity`、`IXP`、`cross-border fiber`、数据中心、机房、托管、云、灾备、区块链、虚拟资产。
7. **可靠性分级**（按事实逐条打分，不按项目整体打分）：A=一级证据（公共机构、官方公报/法律库、监管登记、公用事业、运营商自有设施/服务页、政府采购记录、官方云区域页）；B=强二级证据（可靠本地/行业媒体、具名高管访谈、厂商案例研究、PeeringDB/RIPE 等互联目录）；C=弱线索（聚合目录、市场页、转售商声明、办公地址推断、招聘广告、投资促进叙事）；U=未证实传言或纯检索提示词。
8. **计数与去重规则**：SMT/TIM San Marino 官方 Housing 页为 A（服务/设施描述），PeeringDB AS15433 为 B（互联种子），“Rovereta Tier III”无可靠来源为 U/C，“San Marino crypto-friendly attracts data centers”为 C（营销、无设施）；同一 SMT/TIM 条目在多个聚合目录重复须去重后再评估；品牌地址 ≠ 机房地址（公司总部、门店、注册地、`.sm` 域名、support address 不能直接落位为 data center）；意大利邻近噪声（Rimini、Bologna、Milan、Turin 项目）检查行政区划与物理地址，不得误归圣马力诺。最终枚举预期：**1 个 A 级运营商 data-center/housing 服务事实（SMT/TIM San Marino）+ 若干 C 级内部机房/政策需求线索**。

## 常用查询模板

```text
site:gov.sm "centro dati"
site:gov.sm "centro elaborazione dati"
site:gov.sm "data center"
site:gov.sm "sala server"
site:gov.sm appalto hosting
site:bollettinoufficiale.sm "centro dati"
site:bollettinoufficiale.sm "centro elaborazione dati"
site:bollettinoufficiale.sm "disaster recovery"
site:bollettinoufficiale.sm "gruppo elettrogeno" informatica
site:bollettinoufficiale.sm "tecnologie basate su registri distribuiti"
site:consigliograndeegenerale.sm "asset virtuali"
site:aass.sm "centro dati"
site:aass.sm "allacciamento" "media tensione"
site:smt.sm "data center"
site:smt.sm hosting housing cloud
site:telecomitalia.sm "Data Center" "San Marino"
site:bcsm.sm "continuità operativa"
site:aif.sm "asset virtuali"
site:sanmarinoinnovation.com "operatori DLT"
"centro dati" "San Marino"
"centro elaborazione dati" "San Marino"
"sala server" "San Marino"
"data center" "San Marino"
"housing" "TIM San Marino"
"San Marino Telecom" "data center"
"San Marino" cloud sovrano
"San Marino" colocation
"San Marino" "disaster recovery"
"San Marino" "asset virtuali"
Xago "San Marino"
AASS allacciamento "media tensione"
"San Marino" VPS server dedicato
site:sanmarinortv.sm "centro dati"
site:libertas.sm "centro dati"
site:sanmarinofixing.com "data center"
"San Marino" "data center" Rovereta
"San Marino" "data center" Serravalle
```

采购模板：`site:bollettinoufficiale.sm "bando di gara" informatica`、`site:bollettinoufficiale.sm "aggiudicazione" informatica`、`site:bollettinoufficiale.sm "climatizzazione" informatica`、`site:bollettinoufficiale.sm "continuità operativa"`、`site:aass.sm bando informatica`、`site:iss.sm "sala server"`。分堡通用模板：`"{castello}" ("centro dati" OR "data center" OR "sala server" OR CED OR hosting)`，并对每个 castello 跑 `site:libertas.sm "{castello}"` 与 `site:sanmarinortv.sm "{castello}"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **核心官方源**：GovSM（gov.sm，简单 HEAD 可能返回 403，网页可检索）、Bollettino Ufficiale（重定向到 /on-line/home.html）、Consiglio Grande e Generale、Statistica、AASS（电力/水/气公用事业，132 kV 高压线路接入背景）、SMT（smt.sm）、TIM San Marino Housing（telecomitalia.sm）、AIF、BCSM、San Marino Innovation、Garante Privacy、Camera di Commercio（camcom.sm——不再用 cc.sm 作主 URL）、Registro Imprese（registroimprese.cc.sm）、Autorità Energia。
- **电力与公用事业**：AASS 电力信息页是关键背景——电力通过多条 132 kV 高压线路接入并由 AASS 配电；对任何新增数据中心负荷寻找 `allacciamento`、`media tensione`、`cabina`、`sottostazione`、`trasformatore`、`potenza disponibile`、`gruppo elettrogeno`、`UPS`、`raffreddamento`；AASS 年报/采购中的电网升级、大用户接入、机电维护合同。
- **9 castelli 官方覆盖矩阵**：Acquaviva（Gualdicciolo 边境工业/SMT 联系地址线索）、Domagnano（SMI 地址与创新企业）、Fiorentino（工业区/企业 IT）、Borgo Maggiore（商业/银行/TIM corporate/store 地址）、Citta di San Marino（政府/议会/BCSM/Garante 内部 CED）、Serravalle（Dogana/Rovereta/Galazzano/Ciarulla 工业商业区，SMT Tier/Rovereta 传言须核实）；Chiesanuova/Faetano/Montegiardino 低密度低预期。每轮结果表必须列出 9 个 castelli，即使结果为 negative checked。
- **记录格式**：每个候选设施至少记录 `name`、`operator`、`service type`（housing/cloud/internal CED/DR/edge/HPC）、`castello`（未知时写 `unknown within SM`，不要推断）、`address evidence`（source URL + 引文摘要）、`power/cooling/connectivity evidence`、`customer-facing?`、`grade per fact`、`negative checks`。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **本地/行业媒体**：San Marino RTV、Libertas、San Marino Fixing、L'Informazione di San Marino、Corriere Romagna/RiminiToday/Il Resto del Carlino（里米尼-圣马力诺跨境网络/能源/投资）、DCD、Capacity Media、CoinDesk/Cointelegraph/Finance Magnates（Ripple/SMI/Xago/crypto 叙事，公司事实 B、炒作 C）。
- **运营商/托管扫描**：SMT/TIM San Marino（A for service existence，location/capacity as evidenced）、AASS（C until named）、GovSM/UITEDS（C）、BCSM 与银行（C）、ISS（C）、SMI 生态（B/C 公司，U/C 设施）、Xago 与加密/fintech（B 公司，U/C 设施）、在线博彩牌照持有者（C）、UniRSM（C）、本地 IT/MSP/hosting（C）。扫描纪律：`<company> "centro dati"`、`<company> CED`、`<company> "sala server"`、`<company> cloud`、`<company> hosting`；无物理地址/castello 与运营状态前不得把公司计为设施。
- **聚合目录与互联目录**：Data Center Map、datacenters.com、Baxtel、Cloudscene 等仅作发现工具，容量/Tier/地址/运营状态未经运营商、官方、AASS、B.U. 或强二级来源确认不得高于 C；PeeringDB AS15433、RIPE DB、IXPDB（国内 IXP 负向检查）、MIX Milano（A/B）为互联证据。
- **加密/ICT 友好定位**：SMI 创新枢纽（A）、2019 Blockchain Decree（Decreto Delegato 23 maggio 2019 n.86，A when B.U. PDF captured）、2024 DLT framework（A）、Ripple/SMI/Xago 叙事（B 公司事实/C 市场叙事）、虚拟资产 AML/VASP（A/B）。判读规则：政策友好 ≠ 本土算力供给；加密/fintech 公司存在 ≠ 在圣马力诺运行机房；核验每家公司 ASN、IP 地理、托管条款、支持地址、客户案例；只有具名圣马力诺境内设施证据才进入设施清单，其他放入 demand/policy signal。

## 维护注意（更新纪律）

- 不删除/移动任何既有文件；双 explorer 文件是 codex 审核定稿，SKILL.md 忠实提炼其内容，细则差异以 explorer 原文件为准。
- 功率、等级、PUE、机房面积、机柜数、冗余等级只有在运营商页面、AASS/B.U. 文件或厂商案例明确时才记录为 A/B；聚合目录和媒体数字默认为 C。
- 云区域负向检查每次扫描重新确认 AWS/Azure/GCP/OCI 官方列表；季度复查 SMT/TIM San Marino、AASS、B.U.、GovSM、SMI、AIF、BCSM、本地媒体、PeeringDB、IXPDB、聚合目录。
- 不要用聚合目录或加密营销把全国设施数放大；“San Marino cloud/sovereign cloud”营销须核实物理托管地，不得误判为本地 hyperscale region。
