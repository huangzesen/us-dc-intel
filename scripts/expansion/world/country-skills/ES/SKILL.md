---
name: es-datacenter-methodology
location: scripts/expansion/world/country-skills/ES/SKILL.md
description: |
  Spain (ES) datacenter discovery & audit methodology — how to enumerate, verify, and update Spain datacenter projects at autonomous-community + province/municipality granularity. Spain has no single national datacenter permit or facility registry: enumeration joins municipal urban-licensing files (licencia de obras/urbanistica), autonomous-community strategic-project regimes (PIGA in Aragon, PSI in Castilla-La Mancha, projecte empresarial estrategic in Catalonia) and environmental files (EIA/DIA/AAU/AAI), BOE + regional gazette notices (often triggered by substations/400-kV lines), Red Electrica/Redeia grid-access evidence, MITECO EU ReportENER energy-efficiency reporting obligations (>500 kW IT demand), PLACSP public procurement for public-sector CPDs, cloud-region pages (AWS eu-south-2/Aragon, Azure Spain Central/Madrid, GCP europe-southwest1/Madrid, OCI Madrid), and operator facility pages. Read this before running ES exploration/audit batches. Routes to explorer-official.md (BOE/gazettes/grid/regions) and explorer-industry.md (SpainDC/trade press/vendors/regional matrix).
---

# ES · 西班牙数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：西班牙**没有**单一的全国数据中心许可/设施注册库；枚举必须拼接**市政城市规划许可、自治区战略项目与环境文件、电网接入证据、BOE/自治区公报、云区域公告、运营商设施页**。
> 大型项目通常**先以能源需求与变电站文件浮出**（BOE 中 `centro de datos`/`CPD`/`subestacion`/`linea`/`acceso y conexion`）；战略项目制度（Aragon `PIGA`、Castilla-La Mancha `PSI`、Catalonia `projecte empresarial estrategic`）是关键官方抓手；MITECO 能源效率页要求 ≥500 kW IT 电力需求的数据中心按欧盟规则年度披露（未来设施级来源）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供西班牙探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：MITECO 能效页与环评、BOE（含 ACS DC LA PUEBLA/Penaflor 400 kV 实例）、REE/Redeia 电网接入、CNMC 电信监管/运营商登记、PLACSP 公共采购、自治区公报与环评门户（Madrid/Aragon/Catalonia/Andalusia/Valencia/Basque/Galicia/Castilla-La Mancha/Castilla y León 等）、云区域官方页（AWS/Azure/GCP/OCI）、colo 运营商种子、每区枚举法、证据与状态规则 |
| `explorer-industry.md` | 行业/厂商发现：SpainDC 协会与报告、DCD Spain/Data Center Market 贸易媒体、区域报、运营商/开发商种子（Digital Realty-Interxion/Equinix/DATA4/Nabiax/Merlin-Edged/Iron Mountain/NTT/Prime/Vantage/QTS/Tillion/AWS/Microsoft/Google/Oracle/Templus/Aire-OASIX/Stackscale/ADI/Solaria/Nostrum 等）、19 个自治区查询矩阵、快速验证清单 |

## 核心结构事实（框定每次搜索）

1. **无全国许可库**：以自治区（17 + 2 自治市）为官方操作层，市镇掌 urbanística 许可；大项目常跨层出现（BOE + 自治区公报 + 市镇许可）。
2. **能源与电网是最强先行证据**：搜索 BOE/REE/Redeia 的 `subestacion`、`linea`、`acceso y conexion`、`capacidad de acceso`、征用公告；变电站/线路名常在数据中心名公开前出现（如 `SE Penaflor 400 kV` 服务 `Centro de Datos ACS DC LA PUEBLA`）。RD 1183/2020 + CNMC Circular 1/2024 界定 access/connection/request 语义。
3. **战略项目制度**：Aragon `PIGA`（aragon.es/boa.aragon.es）、Castilla-La Mancha `PSI`（urbanismo.castillalamancha.es，Meta campus 即此）、Catalonia `projecte empresarial estrategic`（26 个潜在项目/7 个极点）、其他自治区 `proyecto estrategico`/`interes autonomico`/`utilidad publica`——分类 ≠ 批准，须查最终环评/建筑许可/电网。
4. **MITECO 能效义务（未来 A 级渠道）**：EU ReportENER 要求 ≥500 kW IT 电力需求的数据中心年度披露、>1 MW 总标称能量输入须余热利用或说明；https://www.miteco.gob.es/es/energia/eficiencia/centros-de-datos.html ——现为规则 A 级，设施级数据尚未公开可查。
5. **主集群**：Aragon（AWS `eu-south-2` 3 AZ + Microsoft/QTS/Tillion/Vantage/SAMCA/ACS 园区管线）、Comunidad de Madrid（Azure Spain Central、GCP `europe-southwest1`/Telefonica、OCI Madrid、colo 密集）；次级：Catalonia（Barcelona/Terrassa/edge）、Valencia、Basque、Andalusia、Galicia、Castilla-La Mancha、Castilla y León、Navarra、Murcia、岛屿/边缘。
6. **云区域=城市级证据（A），非设施地址**：AWS Europe (Spain)/`eu-south-2` Aragon；Azure Spain Central（3 AZ）Madrid；GCP `europe-southwest1` Madrid（Telefonica 共建）；OCI `eu-madrid-1`/`eu-madrid-3` Madrid。
7. **多语言搜索**：西语 `centro de datos`/`CPD`/`centro de procesamiento de datos`；加泰语 `centre de dades`；巴斯克语 `datu-zentroa`；加利西亚语 `centro de procesamento de datos`。
8. **容量语义**：优先变电站 MVA/MW、`potencia solicitada`、`capacidad de acceso`、IT load；区分电网连接容量/场地总功率/IT load/营销园区容量；西班牙公告常把 2030/2035 全期聚合，须按阶段分开。

## 查询模式（复制粘贴模板见 explorer-official.md §4 / explorer-industry.md §2、§5）

- 西语核心词：`centro de datos` `data center` `datacenter` `CPD` `centro de procesamiento de datos` `campus de centros de datos` `nube` `region cloud` `hiperescala` `colocation` `sala tecnica`；许可：`licencia de obras` `licencia urbanistica` `declaracion responsable` `licencia de actividad` `primera ocupacion`；环评：`evaluacion de impacto ambiental` `declaracion de impacto ambiental` `evaluacion ambiental simplificada` `autorizacion ambiental integrada` `autorizacion ambiental unificada (AAU)` `informacion publica`；战略：`proyecto de interes general` `PIGA` `proyecto singular de interes` `PSI` `proyecto empresarial estrategico` `proyecto de interes autonomico` `utilidad publica`；电网：`subestacion` `linea electrica` `400 kV` `220 kV` `punto de conexion` `capacidad de acceso` `potencia IT` `MWe` `MVA`。
- 官方：`site:boe.es "centro de datos" "autorizacion administrativa"`、`site:boe.es "centro de datos" "subestacion"`、`site:miteco.gob.es "centro de datos" "evaluacion ambiental"`、`site:ree.es "centro de datos" "acceso"`、`site:redeia.com "centro de datos" "demanda"`、`site:contrataciondelestado.es ("CPD" OR "centro de proceso de datos")`、`site:cnmc.es "registro de operadores" "{company}"`。
- 大区：`site:bocm.es "centro de datos" ("Algete" OR "Getafe" OR "Alcala de Henares")`、`site:aragon.es ("centro de datos" OR AWS) ("PIGA" OR "Plan de Interes General")`、`site:boa.aragon.es "centro de datos" "Amazon Data Services Spain"`、`site:dogc.gencat.cat ("centre de dades" OR "centro de datos")`、`site:juntadeandalucia.es/medioambiente "centro de datos" "Autorizacion Ambiental Unificada"`、`site:dogv.gva.es "centro de datos"`、`site:euskadi.eus ("data center" OR "datu-zentroa") ("autorizacion ambiental" OR "ingurumen")`、`site:urbanismo.castillalamancha.es "Data Center Campus"`、`site:xunta.gal "centro de procesamento de datos"`。
- 行业：`site:datacenterdynamics.com Spain "data center" {operator OR municipio}`、`site:datacentermarket.es "centro de datos" {operator OR comunidad}`、`site:spaindc.com {operator}`、`site:datacentermap.com/spain {municipio}`、`site:baxtel.com "Spain" "{operator}"`。
- 云 pivot：`"{provider}" "España" "region cloud" "centro de datos"`、`"AWS" Aragon "centro de datos" PIGA`、`"Microsoft" "Villamayor de Gallego" "centro de datos"`、`"Google Cloud" "europe-southwest1" Madrid Telefonica`、`"Oracle" "eu-madrid-1" OR "eu-madrid-3"`。
- 状态追踪：`site:{gazette} "{operator}" ("informacion publica" OR "licencia de obras" OR "inicio de obras")`；取消追踪：`"{operator}" "centro de datos" (desistimiento OR retirada OR denegado OR suspension OR caducidad)`。

## 官方/监管管线要点（详见 explorer-official.md）

- **BOE（A）**：全国授权、公共信息公告、土地/公共领域影响、电力基础设施；按变电站/线路名+数据中心名双向搜索（实例 `SE Penaflor 400 kV` → `ACS DC LA PUEBLA`）。
- **REE/Redeia（A，流程/容量声明）**：`site:ree.es "centro de datos" "acceso"`；RD 1183/2020 + CNMC Circular 1/2024 判定 access/connection/request 阶段。
- **MITECO（A，规则）**：能效页（ReportENER 500 kW/1 MW 阈值）+ 国家环评搜索（sede.miteco.gob.es，`centro de datos`/`CPD`/`subestacion`/`linea 400 kV`）。
- **CNMC（A，公司/市场语境）**：运营商登记（Law 11/2022 预先通知）、data portal 省级电信指标；非设施级。
- **PLACSP/OpenPLACSP（A，公共采购事实）**：公共部门 CPD、变电站、设计/冷却/UPS 工程招标。
- **自治区环评/规划（A）**：Madrid BOCM/CONEX、Aragon PIGA/BOA/INAGA、Catalonia DOGC/tramits/govern.cat、Andalusia BOJA/AAU-AAI、Valencia DOGV/mediambient（`Data Center "El Lobo"` Monforte del Cid 实例）、Basque BOPV（`Data Center Euskadi S.L.` Abanto-Zierbena 实例）、Galicia DOG/cmatv、Castilla-La Mancha DOCM、Castilla y León BOCYL。
- **市政许可（A/B）**：市镇 `licencia de obras`/`declaracion responsable`/`primera ocupacion`/e-sede；Madrid/Barcelona 大都会市镇门户比全国搜索更重要。
- **法律主体 pivot**：BOE/公报中的商业名称、SPV（`Amazon Data Services Spain`、`Microsoft 7724 Spain`、`Data Center Euskadi`、`ACS DC` 等）→ 市政文件核实。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **协会**：SpainDC（B，行业词汇/年报/成员种子，非设施注册表）、DCD SpainDC 档案、Datacloud/Data Centre World 活动。
- **贸易媒体**：DCD Spain tag（B，最佳英文来源）、Data Center Market（B，西语行业媒体）、El Economista/Cinco Dias/Expansion/El Pais（B-/C+）、区域报（Heraldo de Aragon/La Vanguardia/Valencia Plaza 等，B-/C+，常首发市政/许可阶段/反对）；工程/法律/地产（EjePrime/Iberian Property/DLA Piper/Sener/IDOM/AECOM，B/C）。
- **目录（C/C+ 线索源）**：DataCenterMap、Datacenters.com、Baxtel、PeeringDB；须运营商页/市政/官方核实。
- **运营商/开发商种子（A=存在/B=容量）**：Digital Realty/Interxion（Madrid MAD1-5/Julian Camarillo）、Equinix（Madrid MD + Barcelona BA1/BA2）、DATA4（Alcobendas/San Agustin del Guadalix）、Nabiax（Alcala/Julian Camarillo/Terrassa）、Merlin/Edged（Getafe/Barcelona/Bilbao-Arasur/Extremadura，CNMV 披露 A 级）、Iron Mountain（San Fernando de Henares MAD-1，旧名 XData）、NTT、Prime（Alcobendas MAD01）、Vantage（Aragon/Villanueva de Gallego）、QTS/Blackstone（Calatorao）、Tillion/Azora（Zaragoza）、AWS/Microsoft/Google/Oracle 区域、Templus（Malaga/Sevilla/Ceuta）、Aire/OASIX/Stackscale（Madrid/Malaga/Toledo/Canarias）、ADI Data Center Euskadi、Solaria（电网需求公告）、Nostrum/Ingenostrum（Badajoz/Caceres/Guadalajara/Galicia）。
- **状态语义（西语）**：`anuncia`/`previsto`/`reserva de suelo`/`MOU`=意向；`informacion publica`=已申报未批准；`aprobacion inicial/definitiva`/`licencia de obras`/`DIA`/`PIGA`/`PSI`=已许可（须区分战略分类与最终许可）；`inicio de obras`/`primera piedra`/`adjudicacion`=在建；`inaugura`/`operativo`/`en servicio`/运营商页上线/Uptime/PeeringDB 活跃/云区域 GA=运营；`desistimiento`/`denegado`/`suspension`/`caducidad`=取消/过期。

## 来源分级

- **A** = 官方/一手：BOE/自治区公报公共信息与环评决定、电网/变电站授权、市镇许可文件、MITECO/REE/Redeia/CNMC 官方规则与登记、云区域官方页（区域存在）、运营商官方设施页（存在/位置）、CNMV 上市公司披露。
- **B** = 强二级：运营商页容量（未独立核实）、SpainDC/协会、DCD/Data Center Market/Cinco Dias/El Economista/区域报（有出处）、市场报告、工程任命（项目现实性 B/A-）。
- **C** = 弱/未验证：聚合器、地图、LinkedIn、地产宣传册、无出处投资声明；目录默认 C，除非官方/运营商/PeeringDB/Uptime 核实。
- **容量规则**：优先运营商 IT MW；`MWe`/总电气 MW/`MVA`/园区上限分开标注，不换算；>20 MW 项目须至少一条电网接入/变电站/公报/运营商/投资者证据才计入；支持设施（装配、物流、AI 服务器维修、水项目、变电站、污水处理）与数据厅分开记录。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=ES，divisions=自治区/省/市镇）。
2. 建种子：云区域（AWS/Azure/GCP/OCI）+ colo 运营商页（Equinix/Digital Realty/Global Switch/Iron Mountain/Nabiax/Telefonica/Templus 等）+ SpainDC 成员 + DCD/Data Center Market 首扫。
3. 对每个 division：识别法律主体/SPV → BOE + 自治区公报搜索（`centro de datos`/`CPD`/运营商名）→ 自治区环评门户（EIA/AAU/AAI/战略项目）→ 市政许可搜索（精确地块/工业园区）→ REE/Redeia + BOE 电网（变电站/线路）→ PLACSP 公共 CPD → 贸易媒体补缺并回解到官方文件。
4. 优先地区：Madrid（Azure/GCP/OCI + colo 密度，BOCM/市政）→ Aragon（AWS/Microsoft/QTS/Tillion/Vantage，PIGA/BOA）→ Catalonia（Barcelona/DOGC/战略项目分类）→ Basque/Andalusia/Valencia → 其余自治区按矩阵。
5. 去重：按 (运营商/法律实体 + 市镇 + 园区/设施名 + 变电站/线路 + 许可号) 聚类；注意品牌 vs SPV（Interxion→Digital Realty、bitNAP→Templus、XData→Iron Mountain、Telefonica→Nabiax）；Madrid/Barcelona 品牌可能位于周边市镇（Alcobendas/Alcala de Henares/Getafe/L'Hospitalet/Terrassa）。
6. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目 division 写 `no_projects: true`；容量区分 `operational` / `under_construction` / `planned_full_buildout_mw`。
7. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核西班牙数据中心（自治区/省/市镇粒度，Madrid+Aragon 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：AWS Aragon 扩展各园区许可（PIGA 阶段）、Microsoft Aragon 园区（Villamayor de Gallego）、Meta/Talavera PSI 许可进度、Merlin/Edged 各园区（Getafe/Barcelona/Bilbao）许可、Nostrum Evergreen Badajoz 与 CC Green Cáceres、ADI Data Center Euskadi、Solaria 电网需求公告对应的实际项目、MITECO ReportENER 设施级数据是否公开。
