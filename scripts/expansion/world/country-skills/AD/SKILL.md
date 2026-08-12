---
name: ad-datacenter-methodology
location: scripts/expansion/world/country-skills/AD/SKILL.md
description: |
  Andorra (AD) datacenter discovery & audit methodology — how to enumerate, verify, and update Andorra datacenter projects at parish granularity (7 parishes in the current manifest). Andorra has no national datacenter registry and no independent datacenter regulator: enumeration triangulates BOPA official gazette & legal acts, Govern and Comu (parish) planning/activity licences, FEDA grid/energy records, Andorra Telecom operator pages, APDA data-protection records, public procurement, and local press. Read this before running AD exploration/audit batches. Routes to explorer-official.md (official/regulatory/cloud pipeline) and explorer-industry.md (industry/trade-press/vendor discovery).
---

# AD · 安道尔数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：安道尔**没有**全国数据中心注册库，也**没有**独立的数据中心监管机构，不能按美国/欧盟方式直接枚举。
> 安道尔枚举靠**官方多轨迹交叉**：BOPA 官方公报/法律文件、Govern 与 Comu（教区）规划与活动许可、FEDA 电网/能源记录、Andorra Telecom 运营商页面、APDA 数据保护记录、公共采购与本地媒体。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供安道尔探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：BOPA、Govern、Comu 教区规划（7 教区矩阵）、FEDA 能源、Andorra Telecom 电信、APDA、公共采购、云区域官方负面清单 |
| `explorer-industry.md` | 行业/厂商发现：本地媒体（El Periòdic/L'Altaveu/BonDia/Diari/RTVS）、运营商与托管商扫描、聚合器（Data Center Map/datacenters.com）、PeeringDB/CATNIX/RIPE、投资促进渠道、加泰语/西语/法语/英语查询模板、教区级策略 |

## 核心结构事实（框定每次搜索）

1. **无国家数据中心注册库/无独立监管机构**：枚举必须拼接 BOPA、Govern/Comu 规划、FEDA 电网、Andorra Telecom 运营商证据、APDA、采购与本地媒体；单一门户查无 ≠ 项目不存在。
2. **行政区划 = 7 教区（parroquies）**：Canillo、Encamp、La Massana、Ordino、Sant Julia de Loria、Andorra la Vella、Escaldes-Engordany；Comu 控制城市规划、工程许可与活动许可，是许可层级。
3. **教区级精度为硬性要求**：新数据中心通常留下三条官方痕迹——Comu 城市/工程/活动许可、FEDA 大用户/并网规划、涉公共实体的 BOPA/采购/法人文件；街址级精度仅在公开且经核实后可选。
4. **市场形态 = 小微型、运营商主导**：唯一 A 级运营商设施是 Andorra Telecom 位于 **La Massana** 的 Data Centre for businesses（运营商页面）；CEO 2026-08-05 访谈称共三个数据中心（La Massana、La Comella、Santa Coloma）——三址说法为 **B** 级，聚合器地址细节仅作线索。
5. **能源是硬约束**：FEDA 为国家电力公司，大量依赖西班牙/法国进口电；FEDA–Endesa 供电协议延至 2037 年，报道讨论过数据中心可能性——仅 **B** 级意图，无场址/容量/获批项目。
6. **云协议 ≠ 本地超大规模区域**：Govern/Andorra Digital 与 Google Cloud（2025-04-01）、AWS（2025-07-18）战略协议为官方云协作（A 级），但对本地物理云区域为**负面证据**。
7. **超大规模负面检查**（每次扫描重查）：AWS、Azure、GCP、OCI 官方区域表均无安道尔区域；最近区域为 AWS `eu-south-2`（西班牙）、Azure `spaincentral`、GCP `europe-southwest1`（马德里）、OCI 西班牙中部/马德里。
8. **预期真实产出 3-6 个设施**：Andorra Telecom 三个站点 + 可能的内部运营商/政府 CPD + 小型私有服务器机房；不得用聚合器数量充数。
9. **语言**：官方记录与本地媒体首选加泰语，西班牙语用于 Endesa/REE，法语用于 RTE/跨境连接，英语用于超大规模与聚合器检查。
10. **来源分级 A/B/C/U**：A=官方/运营商一手证据；B=具名高管访谈/可靠本地媒体/CATNIX-CSUC-RIPE-PeeringDB/厂商案例；C=聚合器/市场页/转售商/投资促进叙述；U=未证实传闻，仅作搜索线索。

## 常用查询模板（详见 explorer-official.md §1-§5 / explorer-industry.md §1、§4、§7）

- 加泰语：`"centre de dades" Andorra`、`"centre de processament de dades" Andorra`、`"centre de dades" "La Massana"`、`"centre de dades" "La Comella"`、`"centre de dades" "Santa Coloma"`、`Andorra licitacio "centre de dades"`、`FEDA "centre de dades"`、`"sala de servidors" Andorra`、`Andorra "nuvol sobira"`。
- 西班牙语：`"centro de datos" Andorra`、`Endesa FEDA Andorra "centro de datos"`、`Andorra "nube soberana"`。
- 法语：`Andorre "centre de donnees"`、`Andorre "cloud souverain"`。
- 英语：`Andorra data center investment`、`Andorra Telecom data centre La Massana`、`Andorra sovereign cloud`。
- 官方站内：`site:govern.ad "Google Cloud" Andorra`、`site:govern.ad "Amazon Web Services" Andorra`、`site:andorra-digital.com "cloud sobira"`、`site:elperiodic.ad "centre de dades"`、`site:all-andorra.com "Andorra Telecom" "data centres"`。
- 云 pivot：`"Andorra Telecom" CATNIX 20 Gbps`、`Aitek Andorra cloud`、`Tecnoland Andorra "centre de dades"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 国家级：Govern（法律/公告/云协议）、BOPA（官方公报：法律、法令、招标、裁决、公营企业行为）、Portal Juridic（LGOTU 合并法）、Tramit（电子行政程序）、Andorra Digital（云协议与认证云目录）、APDA（数据保护）、Estadistica（能源/ICT 数据集）、Andorra Business（投资机构，仅作线索源）。
- 教区级：七个 Comu 全部覆盖（Canillo、Encamp、La Massana、Ordino、Sant Julia de Loria、Andorra la Vella、Escaldes-Engordany），搜索 `llicencia d'activitat`/`llicencia urbanistica`/`llicencia d'obres`/`pla d'urbanisme`/`adjudicacio` + 候选设施名。
- 能源：FEDA + FEDA 透明门户 + FEDA Solucions；术语 `gran consumidor`、`potencia`、`subestacio`、`ETR`、`transformador`、`connexio`、`adjudicacio`。
- 电信/互联：Andorra Telecom 官方设施页（A）、CATNIX/CSUC 升级新闻（B）、PeeringDB ASN 种子（B/C）、RIPE（B）、IXPDB（B）；无国内 IXP 记录，跨境光纤经西班牙/法国。
- 采购：BOPA 招标词 `"centre de dades"`、CPD、`"sala de servidors"`、`backup`、`recuperacio de desastres`、`grup electrogen informatica`。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 本地媒体 B 级源：El Periòdic、L'Altaveu、BonDia、Diari d'Andorra、Cadena SER Andorra、RTVS、VilaWeb Andorra、all-andorra.com（具名高管访谈）；DCD/Capacity Media 对安道尔覆盖稀疏。
- 运营商/托管种子：Andorra Telecom（A/B）、Tecnoland“DataCenter Andorra”（B/C，需核实物理教区与 ASN）、Aitek Souverain Cloud（公司/服务 B，设施 U，注意与法国 `aitek.fr` 区分）、银行与公共机构内部 CPD（C）。
- 聚合器纪律：Data Center Map/datacenters.com/colocationm 仅作发现工具，容量/层级/SLA/地址/状态不得高于 **C** 进入清单，除非官方/运营商源确认。
- 状态动词区分：`announced`/`MoU`/`land acquired`/`construction`/`launched`/`operational`；FEDA/Endesa 讨论、投资者兴趣、1 MW AI-DC 概念只能记为带日期线索。

## 来源分级

- **A** = 公共机构/官方公报/公用事业/采购记录/运营商自有设施页/云官方区域页；例如 Andorra Telecom Data Centre 页面（La Massana 服务）。
- **B** = 具名高管访谈、可靠本地媒体、CATNIX/CSUC/RIPE/PeeringDB、厂商案例、足够细节的贸易媒体；例如 CEO 三数据中心陈述。
- **C** = 聚合器目录、市场页、转售商声明、无具名场址的投资促进叙述、由公司办公地址推断、社交帖子或招聘广告。
- **U** = 未证实传闻；仅作搜索线索。分级只针对该来源所证明的事实。
- **意图 ≠ 项目**：云协议（Google Cloud/AWS）为官方协作但不构成设施证据；超大规模区域列表为权威负面证据，每次扫描重查并记录检查日期。

## 维护注意（更新纪律）

- **更新节奏**：季度重查——本地媒体、BOPA、Comu 议程/会议纪要、FEDA 新闻、Andorra Telecom 页面、PeeringDB、CATNIX、Andorra Digital、云厂商官方区域表；每次扫描记录云负面检查日期。
- **来源验证**：聚合器地址/容量必须回链官方或运营商一手源；CEO 访谈等 B 级陈述需后续文件（BOPA/Comu/FEDA/运营商页面）升级；不得虚构 NRT/法人编号。
- **不删除纪律（NO-DELETION）**：只创建自己的结果文件与 skill 文件，不修改/删除 explorer 源文件与其他工作产物；发现更优来源时以新增记录 + 更高分级并存，不覆盖旧证据。
