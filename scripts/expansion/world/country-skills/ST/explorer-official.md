# ST Explorer Official（官方/监管侧方法论）— 圣多美和普林西比（Sao Tome and Principe）数据中心枚举

国家：**ST Sao Tome and Principe / São Tomé e Príncipe / 圣多美和普林西比**。行政区划来自 `world-manifest.jsonl`，`subnational_type = district/autonomous region`，必须使用 7 个清单拼写：**Agua Grande、Cantagalo、Caue、Lemba、Lobata、Me-Zochi、Principe**。6 个 district 位于圣多美岛；**Principe** 是自治区域。记录设施时必须写清 `division` + 城镇子层（São Tomé、Trindade、Santana、Neves、Guadalupe、Santo Amaro、São João dos Angolares、Santo António 等）。

本文件用于官方/监管/一手来源发现。它不是设施普查结果；它定义如何发现、核验、分级并避免把海缆、政府 IT 服务或电信 PoP 误登记为数据中心。

## 0. 已核验基线（Verified baseline）

- **政府门户**可访问：`https://stp.gov.st/`（HTTP 200）。门户页列出政府地址、官方文档/法律/年度报告/战略入口，以及 Diário da República 链接。
- **INIC（Instituto de Inovação e Conhecimento）**可访问：`https://inic.gov.st/`。INIC 自述为服务国家的信息技术机构，地址在 **Rua Salustino da Graça, Edifício do Gabinete do Primeiro Ministro, Cidade de São Tomé**，即 **Agua Grande / São Tomé**。INIC 官方服务页列出 **Data Center**，并列出 Backup、Pasta Partilhada、Alojamento & VPS、Gestão gov.st、Email Institucional、VPN、Rede e Infraestrutura、Administração de Sistemas 等服务。因此，**INIC government data center / government hosting** 是本国最强 A 级种子；容量、机房面积、认证和精确楼内位置未公开时保持 `capacity_mw: null`。
- **监管机构为 AGER（Autoridade Geral de Regulação / General Regulatory Authority）**：`https://ager.st/` 官方页说明 AGER 监管电信、邮政、水和电力；World Bank P177158 亦说明 AGER 是 2005 年创建的综合公用事业监管机构，负责监督 telecom、post、water、electricity。不要再把 ARST 当作当前默认机构名；仅作为历史/误写检索词。
- **CST** 官方域名可访问：`https://www.cst.st/` 重定向到 `https://cst.st/`（HTTP 200）。CST 是在位运营商；World Bank P177158 将 CST 与 Unitel STP 列为市场运营商，并说明 CST 参与 ACE/STP Cabo。
- **Unitel STP** 官方域名可访问：`https://www.unitel.st/`（HTTP 200）。它是第二移动运营商；DCD/Expansão 报道可作 B 级行业证据，设施主张仍需监管或运营商一手文件。
- **EMAE** 官方域名可访问：`https://www.emae.st/`（HTTP 200）。EMAE 是水电公用事业；电力记录只能佐证供电/大负荷，不能单独证明数据中心。
- **BCSTP** 官方域名可访问：`https://www.bcstp.st/`（HTTP 200）。央行 IT/支付系统机房是机构 lead；只有央行年报、采购、审计或合同明确到机房/托管时才升级。
- **INE-STP** 官方域名可访问：`https://www.ine.st/`（HTTP 200）。World Bank P177158 明确人口普查数据将托管在 INIC national data center；INE/人口普查项目文件是政府数据中心使用场景的强佐证。
- **ACE 海缆**：ACE 官方页 `https://ace-submarinecable.com/en/submarine-cable/` 明确 ACE 于 2012 年 12 月投入使用，并将 Sao Tome & Principe / São Tomé and Príncipe列为 landing station。World Bank P177158 说明 STP 2012 年从卫星切换到 ACE，并通过 STP Cabo 管理登陆站和容量份额。ACE/STP Cabo 是连通性设施；除非有托管/服务器服务证据，不登记为数据中心。
- **São Tomé-Príncipe 岛际连接**：World Bank P177158 说明 Príncipe 依赖两条微波链路，并规划/评估岛际海缆 PPP，可能由 STP Cabo 或类似结构运营。这是 **Principe / Santo António** 电信 PoP/边缘机房 lead 的来源，但不是已确认 DC。
- **2Africa**：官方可用域名为 `https://www.2africacable.net/`。`https://www.2africacable.com/` 返回跳转/lander 页面，不应作为来源。当前官方文本页说明 core system complete/landed in most landing countries，但未在可检索文本中直接点名 ST；因此圣普 2Africa 登陆只能作为 C 级/待复核 lead，必须用 2Africa 官方地图、TeleGeography/Submarine Cable Map 或系统方公告逐次确认，不能写成已确认 A 级事实。
- **超大规模云区域**：AWS、Azure、Google Cloud、OCI 官方区域列表未列出圣普本地区域。转售商、VPS、BuiltWith 或 “customers in Sao Tome” 页面不是云区域证据。

诚实产量预期：全国 **1 条强政府/机构设施种子（INIC Data Center，Agua Grande）+ 0-2 条机构/运营商 lead + 连通性记录**。除 INIC 外，不要把 CST/Unitel/BCSTP/ACE/STP Cabo 自动登记为数据中心。

## 1. 可靠性分级（Reliability grading）

- **A**：政府/监管/多边机构/运营商一手来源直接证明设施、服务、地址、状态或融资。例如 INIC Data Center 服务页、World Bank P177158、AGER 官方页、ACE 官方页、CST/Unitel/BCSTP/EMAE 官方页、AWS/Azure/GCP/OCI 官方区域页。
- **B**：有具名当事方、日期和地点的可靠媒体/行业报道，例如 DCD、Developing Telecoms、Expansão、Lusa、Téla Nón、STP-Press、Capacity Media、TeleGeography 新闻。
- **C**：目录站、SEO 托管页、承包商作品集、社交页、论坛、地图/POI 页面、未匹配一手证据的媒体转载、未给地址/设施证据的营销话术。

分级必须贴到具体主张：INIC 提供 Data Center 服务是 A；INIC 机房容量/等级/冗余是未公开，不得推断。ACE 在 São Tomé 登陆是 A；ACE 登陆站是数据中心则未证实。

## 2. 官方来源清单（Official and primary source roster）

| 来源 | URL | 用途 | 可靠性处理 |
|---|---|---|---|
| Governo STP | `https://stp.gov.st/` | 政府门户、部委、官方文件、Diário da República 入口 | A（门户/文件事实） |
| INIC | `https://inic.gov.st/`；Data Center 服务页 `https://inic.gov.st/ler_mais.php?id=97` | 政府 Data Center、gov.st、备份、VPS、电子邮件、VPN、政府网络 | A（服务存在与机构位置）；容量 null |
| AGER | `https://ager.st/` | 电信/邮政/水/电监管、许可、运营商、服务公告 | A |
| CST | `https://cst.st/` | 在位运营商、网络、企业/托管/光纤、海缆相关公告 | A for CST-controlled claims |
| Unitel STP | `https://www.unitel.st/` | 第二运营商、网络覆盖、设施 lead | A for Unitel-controlled claims；设施需明确证据 |
| EMAE | `https://www.emae.st/` | 电力、供水、变电站、项目与招标 | A for utility facts |
| BCSTP | `https://www.bcstp.st/` | 央行、支付/金融系统、银行名单、采购 lead | A for bank facts；机房需合同/年报 |
| INE-STP | `https://www.ine.st/` | 人口/普查、数字普查数据、需求侧佐证 | A |
| World Bank P177158 | `https://documents1.worldbank.org/curated/en/779811655323104127/txt/Sao-Tome-and-Principe-Digital-Sao-Tome-and-Principe-Project.txt`；procurement `https://documents.worldbank.org/pt/publication/documents-reports/documentdetail/099012824153022685` | Digital STP、INIC national data center、ACE/STP Cabo、Príncipe connectivity、procurement via STEP | A |
| ACE official | `https://ace-submarinecable.com/en/submarine-cable/` | ACE RFS, landing station list, São Tomé landing | A for cable facts |
| 2Africa official | `https://www.2africacable.net/` | 2Africa system status/map | A only where page/map explicitly supports claim；ST text claim not verified |
| Cloud official pages | AWS `regions_az`, Azure `regions-list`, GCP `about/locations`, OCI `regions.htm` | absence of ST cloud region | A |

## 3. 官方查询模板（Official query templates）

使用葡语优先，并同时跑无重音英文拼写。搜索引擎中 OR 组必须加括号。

```text
site:inic.gov.st ("Data Center" OR "centro de dados" OR "Alojamento" OR VPS OR Backup OR "gov.st")
site:inic.gov.st ("São Tomé" OR "Sao Tome") ("Data Center" OR "centro de dados" OR "centro de processamento de dados")
site:stp.gov.st ("centro de dados" OR "data center" OR INIC OR "governo digital" OR "Portal Único")
site:ager.st (CST OR Unitel OR "STP Cabo" OR "cabo submarino" OR licença OR autorização)
site:cst.st ("centro de dados" OR "data center" OR hosting OR alojamento OR fibra OR "cabo submarino")
site:unitel.st ("centro de dados" OR "data center" OR fibra OR cobertura OR "centro de comutação")
site:emae.st ("centro de dados" OR "grande consumidor" OR subestação OR MVA OR kVA OR concurso)
site:bcstp.st ("servidores" OR "centro de dados" OR "data center" OR informática OR pagamento)
site:ine.st ("censo" OR recenseamento) ("INIC" OR "centro de dados" OR servidores)
site:documents.worldbank.org ("Sao Tome and Principe" OR "São Tomé") ("national data center" OR INIC OR "data center" OR "inter-island cable" OR "STP Cabo")
```

采购/公报查询：

```text
("São Tomé e Príncipe" OR "Sao Tome and Principe") (concurso público OR licitação OR empreitada OR "aviso de concurso") ("centro de dados" OR servidores OR informática OR telecom OR fibra)
("Diário da República" "São Tomé e Príncipe") ("centro de dados" OR INIC OR telecomunicações OR AGER OR CST OR Unitel)
site:stp.gov.st/documentos ("centro de dados" OR "transformação digital" OR "governo digital" OR INIC)
```

海缆/连通性查询：

```text
("São Tomé" OR "Sao Tome") ("landing station" OR "cabo submarino" OR "estação de aterragem" OR "estação de cabos")
ACE ("São Tomé" OR "Sao Tome") (landing OR "cabo submarino" OR "STP Cabo")
"STP Cabo" ("landing station" OR "cabo submarino" OR ACE OR capacidade)
("São Tomé" OR "Sao Tome") ("Príncipe" OR Principe) ("microwave link" OR "inter-island cable" OR "cabo inter-ilhas" OR fibra)
2Africa ("São Tomé" OR "Sao Tome" OR "São Tomé e Príncipe") (landing OR "planned landing" OR "cable landing station")
```

## 4. 分区覆盖工作流（Division coverage workflow）

每个清单分区必须有结论：已确认设施、lead、连通性记录，或“未发现公开项目”。默认不要为县政府、电信基站、发电站或海缆登陆站创建 DC 记录。

| Manifest division | 城镇子层 | 官方优先路线 | 当前覆盖结论 |
|---|---|---|---|
| **Agua Grande** | São Tomé | INIC Data Center；政府门户/公报；CST/Unitel 总部与核心网；BCSTP；ACE/STP Cabo；AGER；EMAE | **最高优先级**。INIC 是 A 级政府 Data Center 种子；CST/Unitel/BCSTP 为 lead；ACE/STP Cabo 为连通性记录 |
| **Lobata** | Guadalupe、Santo Amaro | 县许可、EMAE、CST/Unitel 覆盖、沿海基础设施 | 未发现公开 DC；只保留电信/电力 lead |
| **Lemba** | Neves | 县许可、港口/燃油区电力、运营商覆盖 | 未发现公开 DC |
| **Me-Zochi** | Trindade、Madalena | 县许可、政府机构/学校/卫生网络、EMAE | 未发现公开 DC；政府机构机房仅 C 级 lead，除非一手合同 |
| **Cantagalo** | Santana | 县许可、运营商覆盖、EMAE | 未发现公开 DC |
| **Caue** | São João dos Angolares | 县许可、运营商覆盖、EMAE | 未发现公开 DC |
| **Principe** | Santo António | Governo Regional do Príncipe、World Bank inter-island connectivity、CST/Unitel PoP | 未发现公开 DC；Príncipe connectivity/PoP 是 lead |

分区模板：

```text
("{district}" OR "{town}") ("São Tomé e Príncipe" OR "São Tomé" OR "Sao Tome") ("data center" OR "centro de dados" OR "sala de servidores" OR colocation OR alojamento)
("{district}" OR "{town}") (telecom OR fibra OR "cabo submarino" OR "landing station" OR "centro de comutação" OR "network operations")
("{district}" OR "{town}") (gerador OR UPS OR subestação OR energia OR "grupo gerador")
("{district}" OR "{town}") (licenciamento OR obras OR concurso OR licitação OR empreitada) (servidores OR telecom OR informática)
site:cst.st ("{district}" OR "{town}") (fibra OR cobertura OR "centro de dados")
site:unitel.st ("{district}" OR "{town}") (fibra OR cobertura OR "centro de comutação")
site:emae.st ("{district}" OR "{town}") (subestação OR energia OR eletricidade)
```

## 5. 设施种子与处理规则（Seeds and handling）

| 种子 | Division / town | 状态 | 等级 | 处理 |
|---|---|---|---|---|
| **INIC Data Center / government hosting** | Agua Grande / São Tomé | 官方服务存在；设施细节未公开 | **A** for service and institution location | 可作为设施种子；容量/面积/等级 null；补采地址、服务范围、采购/建设文件 |
| CST core network room / NOC | Agua Grande / São Tomé | lead | A only if CST/AGER file says room/NOC/DC; otherwise C/B | 不因运营商存在自动登记为 DC |
| Unitel STP switching center | Agua Grande / São Tomé（核实） | technical-launch lead | B from Expansão; A if Unitel/AGER confirms | “Centro de Comutação” 是电信交换设施 lead，不等同 DC |
| BCSTP IT/payment-system room | Agua Grande / São Tomé | lead | C until BCSTP procurement/annual report | 机构机房需明确证据 |
| ACE / STP Cabo landing station | Agua Grande / São Tomé | connectivity facility | A for cable/landing; non-DC | 单独连通性记录；仅有托管/服务器证据才升级 |
| Government digital platform / Portal Único | Agua Grande / São Tomé（核实托管） | demand-side lead | A for project; not facility unless hosting named | 与 INIC national data center 交叉核验 |
| Príncipe PoP / inter-island cable endpoint | Principe / Santo António | lead | A/B for connectivity; C for DC | 只作 PoP/edge lead |
| 2Africa ST landing | 未确认 | weak lead | C until system/source names ST | 不得写成已确认登陆站 |

## 6. 决策规则（Decision rules）

- **Data Center 服务 vs 数据中心设施**：INIC 服务页足以证明政府提供 Data Center/hosting 类服务；若普查 schema 要求物理设施字段，地址先用 INIC 官方地址，容量和认证保持 null，并标注“exact server-room/building details not public”。
- **海缆登陆站 != 数据中心**：ACE/STP Cabo 是连通性基础设施。无托管/服务器服务证据时，不创建 DC facility，只创建 cable/landing connectivity record。
- **电信核心网/交换中心 != 数据中心**：CST/Unitel 的 NOC、switching center、MSC、PoP 是电信设施 lead；只有出现 “centro de dados / data center / hosting / colocation / sala de servidores” 且能落到站点时才升级。
- **融资/采购 != 容量**：World Bank/AfDB 贷款额、海缆投资、设备采购金额不能换算 MW、rack、面积或 Tier。
- **云区域缺位**：只引用 AWS/Azure/GCP/OCI 官方区域页；任何本地代理、CDN 用户、VPS 客户页面均为假阳性。
- **2Africa 谨慎处理**：官方 `.net` 是可用来源；`.com` 不是有效来源。ST landing 必须由官方地图/TeleGeography/系统方公告直接确认。
- **保留旧 lead 但降级**：无法核验的 CST/BCSTP/2Africa/Príncipe lead 不删除，降级并写明缺证类型。
