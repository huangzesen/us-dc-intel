---
name: st-datacenter-methodology
location: scripts/expansion/world/country-skills/ST/SKILL.md
description: 圣多美和普林西比数据中心查询方法论（Sao Tome and Principe datacenter discovery & audit methodology）——双线来源（官方/监管/云管线 + 行业/厂商/媒体发现）与 district/autonomous region 七区模型下的设施枚举规则。
---

# ST · 圣多美和普林西比数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：发现圣多美和普林西比（Sao Tome and Principe / São Tomé e Príncipe, ST）的数据中心与托管设施。双线方法论：`explorer-official.md`（官方/监管/一手来源）与 `explorer-industry.md`（行业/媒体/供应商侧），均为 codex 审核定稿。划分模型（per manifest）：**district/autonomous region** — 7 个清单拼写：**Agua Grande、Cantagalo、Caue、Lemba、Lobata、Me-Zochi、Principe**（6 个 district 位于圣多美岛；**Principe** 是自治区城）。记录设施必须写清 `division` + 城镇子层（São Tomé、Trindade、Santana、Neves、Guadalupe、Santo Amaro、São João dos Angolares、Santo António 等）。评审日期：2026-08-12。

## 入口

| 入口 | 管线 | 内容 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线 | 已验证基线、可靠性分级、官方/一手来源清单（GovSTP/INIC/AGER/CST/Unitel/EMAE/BCSTP/INE/World Bank P177158/ACE/2Africa/云官方页）、官方查询模板（葡语优先）、分区覆盖工作流、设施种子与处理规则、决策规则 |
| `explorer-industry.md` | 行业/厂商/媒体发现 | 行业基线、来源分级、优先扫描对象、行业与媒体名单、查询模板（运营商/政府/媒体/海缆/供应商/负向控制）、分区枚举矩阵、目录到一手证据流程、葡语术语表、决策规则 |

## 核心结构事实

1. **行政区划模型**：district/autonomous region，7 个清单拼写：Agua Grande、Cantagalo、Caue、Lemba、Lobata、Me-Zochi、Principe。不使用清单外拼写作为行政层；每条记录叠加城镇子层（São Tomé、Trindade、Santana、Neves、Guadalupe、Santo Amaro、São João dos Angolares、Santo António 等）。
2. **注册库现状**：圣普**没有国家级数据中心登记册**。官方枚举以政府门户（stp.gov.st，HTTP 200）、INIC（inic.gov.st，信息与创新机构，地址 Rua Salustino da Graça, Edifício do Gabinete do Primeiro Ministro, Cidade de São Tomé = Agua Grande / São Tomé）、AGER（ager.st，2005 年创建的综合公用事业监管机构，监管电信/邮政/水/电；不要再把 ARST 当作当前默认机构名，仅作历史/误写检索词）、CST（cst.st，在位运营商，参与 ACE/STP Cabo）、Unitel STP（unitel.st，第二移动运营商）、EMAE（emae.st，水电公用事业）、BCSTP（bcstp.st，央行）、INE-STP（ine.st，人口普查）及 World Bank P177158（Digital STP 项目）组合。
3. **法律与监管**：AGER 监管电信/邮政/水/电，许可证与运营商验证走 AGER 官方公告；建设/招标走 Diário da República 与政府采购（concurso público/licitação）；设备采购金额（World Bank/AfDB 贷款、海缆投资）不能换算 MW/rack/面积/Tier——融资/采购 ≠ 容量。
4. **互联与云**：ACE 海缆 2012 年 12 月投入使用，将 Sao Tome & Principe 列为 landing station；STP 2012 年从卫星切换到 ACE，STP Cabo（PPP/SPV）管理登陆站与容量份额，股份主要由 CST/Unitel 持有。Príncipe 依赖两条微波链路，World Bank P177158 规划/评估岛际海缆 PPP——这是 **Principe / Santo António** 电信 PoP/边缘机房 lead 的来源，不是已确认 DC。2Africa 官方可用域名是 `https://www.2africacable.net/`（`.com` 返回跳转页，不可引用）；当前官方文本未直接点名 ST，圣普 2Africa 登陆只能作 **C 级/待复核 lead**，须用 2Africa 官方地图、TeleGeography/Submarine Cable Map 或系统方公告逐次确认。AWS/Azure/GCP/OCI 官方区域列表均未列出圣普本地区域；转售商、VPS、BuiltWith 或 “customers in Sao Tome” 页面不是云区域证据。
5. **设施/项目种子**：**INIC Data Center / government hosting**（Agua Grande / São Tomé，**A 级最强种子**——官方服务页列出 Data Center、Backup、Pasta Partilhada、Alojamento & VPS、Gestão gov.st、Email Institucional、VPN、Rede e Infraestrutura、Administração de Sistemas；容量/机房面积/认证/精确楼内位置未公开时保持 `capacity_mw: null`）；CST core network room/NOC（lead，仅 CST/AGER 文件说 room/NOC/DC 才 A，否则 C/B）；Unitel STP switching center（technical-launch lead，B 来自 Expansão；“Centro de Comutação” 是电信交换设施 lead 不等同 DC）；BCSTP IT/payment-system room（C lead 直到 BCSTP 采购/年报）；ACE/STP Cabo landing station（Agua Grande / São Tomé，A for cable/landing，non-DC 连通性记录）；Government digital platform/Portal Único（demand-side lead，与 INIC national data center 交叉核验）；Príncipe PoP/inter-island cable endpoint（Principe / Santo António，A/B for connectivity，C for DC）；2Africa ST landing（未确认，C lead）。
6. **语言与词汇**：葡萄牙语优先，同时跑无重音英文拼写；葡语术语：centro de dados / centro de processamento de dados / Data Center、sala de servidores（服务器机房）、alojamento / hospedagem / VPS（托管/主机）、colocação（主机托管）、gestão gov.st（政府门户管理）、cópia de segurançca / backup、fibra óptica、cabo submarino、estação de aterragem / estação de cabos（登陆站）、centro de comutação（交换中心）、centro de operações de rede（NOC）、gerador / grupo gerador、UPS / fonte de alimentação ininterrupta、subestação（变电站）、concurso público / licitação（招标）、chave na mão（交钥匙）。
7. **可靠性分级**：A=政府/监管/多边机构/运营商一手来源直接证明设施、服务、地址、状态或融资（INIC Data Center 服务页、World Bank P177158、AGER 官方页、ACE 官方页、CST/Unitel/BCSTP/EMAE 官方页、AWS/Azure/GCP/OCI 官方区域页、2Africa 官方 `.net` 仅在地图/文本明确支持主张时）；B=有具名当事方、日期和地点的可靠媒体/行业报道（DCD、Developing Telecoms、Expansão、Lusa、Téla Nón、STP-Press、Capacity Media、TeleGeography 新闻、TechAfrica News）；C=目录站、SEO 托管页、承包商作品集、社交页、论坛、地图/POI 页面、未匹配一手证据的媒体转载、未给地址/设施证据的营销话术。分级必须贴到具体主张：INIC 提供 Data Center 服务是 A；INIC 机房容量/等级/冗余未公开不得推断；ACE 在 São Tomé 登陆是 A；ACE 登陆站是数据中心则未证实。
8. **计数与去重规则**：Data Center 服务 vs 数据中心设施——INIC 服务页足以证明政府提供 Data Center/hosting 类服务；若普查 schema 要求物理设施字段，地址先用 INIC 官方地址，容量和认证保持 null，并标注 “exact server-room/building details not public”。海缆登陆站 ≠ 数据中心（ACE/STP Cabo 只建连通性记录，无托管/服务器服务证据时不创建 DC facility）；电信核心网/交换中心 ≠ 数据中心（CST/Unitel 的 NOC、switching center、MSC、PoP 是电信设施 lead，只有出现 “centro de dados / data center / hosting / colocation / sala de servidores” 且能落到站点时才升级）；融资/采购 ≠ 容量；云区域缺位只引用 AWS/Azure/GCP/OCI 官方区域页，任何本地代理、CDN 用户、VPS 客户页面均为假阳性；2Africa 谨慎处理（`.net` 可用、`.com` 无效，ST landing 必须由官方地图/TeleGeography/系统方公告直接确认）；无法核验的 CST/BCSTP/2Africa/Príncipe lead 不删除，降级并写明缺证类型。诚实产量预期：全国 **1 条强政府/机构设施种子（INIC Data Center，Agua Grande）+ 0-2 条机构/运营商 lead + 连通性记录**。

## 常用查询模板

```text
site:inic.gov.st ("Data Center" OR "centro de dados" OR "Alojamento" OR VPS OR Backup OR "gov.st")
site:stp.gov.st ("centro de dados" OR "data center" OR INIC OR "governo digital" OR "Portal Único")
site:ager.st (CST OR Unitel OR "STP Cabo" OR "cabo submarino" OR licença OR autorização)
site:cst.st ("centro de dados" OR "data center" OR hosting OR alojamento OR fibra OR "cabo submarino")
site:unitel.st ("centro de dados" OR "data center" OR fibra OR cobertura OR "centro de comutação")
site:emae.st ("centro de dados" OR "grande consumidor" OR subestação OR MVA OR kVA OR concurso)
site:bcstp.st ("servidores" OR "centro de dados" OR "data center" OR informática OR pagamento)
site:ine.st ("censo" OR recenseamento) ("INIC" OR "centro de dados" OR servidores)
site:documents.worldbank.org ("Sao Tome and Principe" OR "São Tomé") ("national data center" OR INIC OR "data center" OR "inter-island cable" OR "STP Cabo")
("São Tomé e Príncipe" OR "Sao Tome and Principe") (concurso público OR licitação OR empreitada OR "aviso de concurso") ("centro de dados" OR servidores OR informática OR telecom OR fibra)
("São Tomé" OR "Sao Tome") ("landing station" OR "cabo submarino" OR "estação de aterragem" OR "estação de cabos")
"STP Cabo" ("landing station" OR "cabo submarino" OR ACE OR capacidade)
2Africa ("São Tomé" OR "Sao Tome" OR "São Tomé e Príncipe") (landing OR "planned landing" OR "cable landing station")
site:datacenterdynamics.com ("São Tomé" OR "Sao Tome" OR "CST" OR "Unitel")
site:developingtelecoms.com ("São Tomé" OR "Sao Tome" OR CST OR Unitel)
site:telanon.info ("centro de dados" OR telecom OR CST OR Unitel OR fibra OR "cabo submarino")
site:stp-press.st ("centro de dados" OR telecom OR energia OR concurso OR INIC)
(Huawei OR ZTE OR Ericsson OR Nokia) "São Tomé e Príncipe" (telecom OR rede OR "core network" OR fibra OR 4G OR 5G)
(Schneider OR Vertiv OR ABB OR Caterpillar OR Cummins OR Siemens) "São Tomé e Príncipe" (gerador OR UPS OR energia OR "data center" OR "centro de dados")
"São Tomé e Príncipe" (AWS OR Azure OR "Google Cloud" OR OCI) ("data center" OR region OR região)
```

分区模板（对每个清单分区）：`("{district}" OR "{town}") ("São Tomé e Príncipe" OR "São Tomé" OR "Sao Tome") ("data center" OR "centro de dados" OR "sala de servidores" OR colocation OR alojamento)`；`("{district}" OR "{town}") (telecom OR fibra OR "cabo submarino" OR "landing station" OR "centro de comutação" OR "network operations")`；`("{district}" OR "{town}") (gerador OR UPS OR subestação OR energia OR "grupo gerador")`；`("{district}" OR "{town}") (licenciamento OR obras OR concurso OR licitação OR empreitada) (servidores OR telecom OR informática)`；并跑 `site:cst.st`、`site:unitel.st`、`site:emae.st` 的分区变体。负向控制：`"Sao Tome" "data center" -"São Tomé e Príncipe"`、`"STP" "data center" -"São Tomé"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **核心官方源**：Governo STP（stp.gov.st）、INIC（inic.gov.st，Data Center 服务页 ler_mais.php?id=97）、AGER（ager.st）、CST（cst.st）、Unitel STP（unitel.st）、EMAE（emae.st）、BCSTP（bcstp.st）、INE-STP（ine.st）、World Bank P177158（Digital STP 项目，INIC national data center/ACE/STP Cabo/Príncipe connectivity/procurement via STEP）、ACE official、2Africa official `.net`、云官方页。
- **分区覆盖工作流**：每个清单分区必须有结论——已确认设施、lead、连通性记录，或“未发现公开项目”。Agua Grande（São Tomé）最高优先级：INIC 是 A 级政府 Data Center 种子，CST/Unitel/BCSTP 为 lead，ACE/STP Cabo 为连通性记录；Lobata（Guadalupe、Santo Amaro）、Lemba（Neves）、Me-Zochi（Trindade、Madalena）、Cantagalo（Santana）、Caue（São João dos Angolares）未发现公开 DC，只保留电信/电力 lead（Me-Zochi 政府机构机房仅 C 级 lead 除非一手合同）；Principe（Santo António）走 Governo Regional do Príncipe、World Bank inter-island connectivity、CST/Unitel PoP——未发现公开 DC，PoP/edge 是 lead。默认不要为县政府、电信基站、发电站或海缆登陆站创建 DC 记录。
- **决策规则**：INIC 服务页足以证明政府 Data Center/hosting 服务（地址用 INIC 官方地址，容量/认证 null 并标注 “exact server-room/building details not public”）；海缆登陆站 != 数据中心；电信核心网/交换中心 != 数据中心；融资/采购 != 容量；云区域缺位只引用官方区域页；2Africa 谨慎处理；旧 lead 不删除、降级并写明缺证类型。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **优先扫描对象**：INIC Data Center / government hosting（A，首要设施种子，补地址/服务范围/建设采购文件，容量 null）；CST core network / hosting lead（B/C until official DC service，不因 4G/光纤自动升级）；Unitel STP switching center（B lead，“Centro de Comutação” 标 telecom facility lead，找官方地址/许可）；STP Cabo / ACE landing station（A connectivity，只有托管/服务器证据才升级）；BCSTP IT/payment systems（C lead，需央行一手文件）；商业银行服务器房（C lead，机构机房不公开不登记）；Príncipe PoP / inter-island endpoint（B/C lead，只记 telecom/edge lead 非 DC）；2Africa possible ST landing（C lead，未点名 ST 前不得确认）。
- **行业与媒体**：INIC/CST/Unitel/AGER/World Bank/ACE/2Africa 官方为 A；DCD、Developing Telecoms、Expansão（Unitel STP launch 与 Centro de Comutação）、Téla Nón/STP-Press/Lusa（本地政治/电信/采购/电力）、Submarine Cable Map/Submarine Networks（海缆状态交叉核验，B unless system-owner source）、目录（Datacenters.com、DataCenterMap、PeeringDB、BuiltWith、VPS lists，C 只作种子发现）。
- **目录到一手证据流程**：1) 目录只取种子；2) 对每个种子回查 inic.gov.st、cst.st、unitel.st、ager.st、stp.gov.st、bcstp.st、World Bank、ACE/2Africa official；3) 要求至少一个一手证据落到设施/服务/地址/状态，否则保留 C 级 lead；4) 海缆、PoP、交换中心、基站、发电机、变电站默认不是 DC；5) 字段中始终记录 division 的 manifest spelling，城镇写在 locality/town 字段；6) 无一手容量时 `capacity_mw: null`、`racks: null`、`area_sqm: null`、`tier: null`。

## 维护注意（更新纪律）

- 不删除/移动任何既有文件；双 explorer 文件是 codex 审核定稿，SKILL.md 忠实提炼其内容，细则差异以 explorer 原文件为准。
- 容量/Tier/机柜数必须留空，除非找到明确文件；融资/采购金额不能换算设施规格。
- 2Africa ST landing 必须用 `.net` 官方地图、TeleGeography 或系统方公告确认后才能升级；分区覆盖要完整，7 个 manifest divisions 均需记录已查来源和未发现公开 DC 的负向结论。
