---
name: it-datacenter-methodology
location: scripts/expansion/world/country-skills/IT/SKILL.md
description: |
  Italy (IT) datacenter discovery & audit methodology — how to enumerate, verify, and update Italy datacenter projects at region/province/municipality granularity. Italy has no national building-permit or facility registry, but since 2026 a national single authorization procedure (procedimento unico, DL 21/2026 → Law 49/2026) exists for data centers with MASE operational materials; enumeration triangulates the MASE VIA/VAS/AIA portal (va.mite.gov.it, projects surface as Centrali via emergency-generator thermal capacity), the new procedimento unico route, municipal SUE/SUAP and planning variants (PGT/PRG/PAT-PI/PUG/PUC), regional VIA/AIA portals, Terna/DSO grid connections, AGCOM/ACN/AgID/PSN public-cloud layer, cloud-region pages (AWS eu-south-1, Azure Italy North, GCP europe-west8/-west12, OCI eu-milan-1/eu-turin-1), and operator facility pages. Read this before running IT exploration/audit batches. Routes to explorer-official.md (MASE/permits/grid/cloud/regulators) and explorer-industry.md (IDA/trade press/vendors/regional query patterns).
---

# IT · 意大利数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：意大利**没有**全国统一的建筑许可库或设施注册库，但自 2026 年起存在全国性数据中心单一授权程序（`procedimento unico`，DL 21/2026 → Law 49/2026），不能只按单一门户直接枚举，也不能无视新流程。
> 意大利枚举的**官方主线是 MASE 环境评估门户（VA/VIA/AIA）+ 2026 单一授权 + 市政 SUE/SUAP**：数据中心因应急发电机热容量触发而常以 `Centrali` 归类出现在环境文件中（D.D. VA n. 257/2024，>50 MWt 阈值）；电网（Terna ≥10 MW 连接请求）是最强前瞻信号但噪声大。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供意大利探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：MASE VA/VIA/AIA 门户（含 Amazon Rho/Pero、DATA4 MIL1、STACK Siziano、Noviglio 实例）、2026 procedimento unico、市政 SUE/SUAP/规划变体（PGT/PRG/PAT-PI/PUG/PUC）、大区 VIA/AIA、Terna/DSO 电网、AGCOM/ACN/AgID/DTD/PSN、云区域官方页（AWS/Azure/GCP/OCI）、IDA 协会、大区优先路由表 |
| `explorer-industry.md` | 行业/厂商发现：IDA 创始成员、DCD Italy tag 与意大利贸易媒体（CorCom/Agenda Digitale/Key4biz/Il Sole 24 Ore）、DataCenterMap/Baxtel/datacenters.com 目录、运营商种子清单（Aruba/Retelit/Equinix/DATA4/STACK/Noovle-TIM/Vantage/Digital Realty/Rai Way/CyrusOne/CloudHQ/EdgeConneX/Khazna-Eni/A2A/Open Hub Med）、意英查询模板、按证据分级 |

## 核心结构事实（框定每次搜索）

1. **2026 全国单一授权程序**：DL 21/2026（Gazzetta Ufficiale 26G00041）→ Law 49/2026；MASE 2026-07 发布操作材料（申请表、所需授权清单、公开通知模板、电子提交规范）。新项目自 2026 年中起走此线；过渡期旧市政/大区 VIA/SUAP 记录与新文件并存。
2. **MASE VA/VIA/AIA 门户是全国最佳公共项目库（A 级）**：https://va.mite.gov.it/ 搜索 `Ricerca Progetti - VIA`、`Ricerca Installazioni - AIA`；数据中心常以 `Centrali` 归类（应急发电机热容量触发）；D.D. VA n. 257/2024 为 >50 MWt 应急发电机的数据中心专用 VIA 指南。
3. **电网是最强前瞻信号但噪声大**：Terna 主管高/超高压连接（尤其 ≥10 MW），连接申请是流程第一步；Terna Lightbox 与贸易媒体报大量投机性连接请求——聚合 GW 是管线压力，不是项目。
4. **伦巴第是主集群且唯一有成熟专项制度的地区**：DGR XII/2629（2024-06-24）市政指南 + L.R. 11/2026 区域选址制度 + `Sportello regionale per i centri dati`；Milan 西/南物流-电力走廊（Settala、Peschiera Borromeo、Melegnano、Siziano、Vellezzo Bellini、Cornaredo、Vittuone、Pavia/Bornasco/Certosa、Bergamo/Ponte San Pietro）。
5. **市政是操作单元，规划计划名称因地区而异**：SUE（建筑）/SUAP（生产活动）/impresainungiorno.gov.it；`PGT`（伦巴第）、`PRG/PRGC`（皮埃蒙特等）、`PAT/PI`（威尼托）、`PUG`（艾米利亚-罗马涅/普利亚）、`PUC`（坎帕尼亚）、`Piano Operativo`（托斯卡纳）。
6. **云区域=城市级证据（A），非设施地址**：AWS `eu-south-1`（Milan，3 AZ）；Azure Italy North（Milan）；GCP `europe-west8` Milan + `europe-west12` Turin（信号）；OCI `eu-milan-1` + `eu-turin-1`（Turin 由 TIM Enterprise 托管）。
7. **容量语义**：环境文件常披露应急发电机热容量（MWt）优于 IT load；区分 `IT load MW` / 电网导入 MVA / 发电机电气 MW / 发电机热 MWt / Terna 请求连接容量 / 已授权电网工程。
8. **优先级地理**：Milan 大都会/伦巴第 → Lazio/Rome（Aruba、PSN、Namex、Areti）→ Piemonte/Turin（OCI/Google/TIM）→ Toscana/Arezzo → Veneto、Emilia-Romagna（CINECA/INFN 非商业除外）、Sicilia/Palermo（Open Hub Med）→ 其余大区低基线。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§4 / explorer-industry.md §2、§5）

- 意语核心词：`data center` `datacenter` `centro dati` `centri dati` `centro elaborazione dati` `CED` `server farm` `colocation` `housing` `cloud region` `polo strategico nazionale` `infrastruttura digitale`；许可：`permesso di costruire` `SCIA` `DIA` `variante urbanistica` `piano attuativo` `SUAP` `SUE` `albo pretorio` `delibera` `determinazione` `conferenza di servizi`；环评：`VIA` `verifica di assoggettabilita` `AIA` `AUA` `gruppi elettrogeni` `potenza termica nominale`；电网：`cabina primaria` `stazione elettrica` `connessione alla rete` `allacciamento Terna` `alta tensione`；运营：`CPI` `agibilita` `messa in esercizio`。
- 官方：`site:va.mite.gov.it "data center" "{regione}"`、`site:va.mite.gov.it "{operator}" "data center"`、`site:mase.gov.it "data center" "procedimento unico"`、`"{comune}" "data center" "permesso di costruire"`、`site:{comune-domain} "data center" "albo pretorio"`、`site:{comune-domain} "data center" "delibera"`、`filetype:pdf "centro elaborazione dati" "agibilita" "{comune}"`、`site:{regione-domain} "VIA" "data center"`。
- 电网：`site:terna.it "data center" "connessione"`、`"{comune}" "data center" "stazione elettrica"`、`"{comune}" "data center" "cabina primaria"`、`"{comune}" "data center" "e-distribuzione"`、`"{comune}" "data center" "Areti" OR "Unareti" OR "A2A" OR "IRETI"`。
- 行业：`site:datacenterdynamics.com/en/ Italy "data center" {operator OR comune}`、`site:italiandatacenter.com {operator}`、`"{operator}" "{comune}" (MW OR MVA OR "metri quadrati" OR "IT load")`、`"{operator}" "{comune}" ("inizio lavori" OR "inaugura" OR "apre" OR "autorizzato")`。
- 云 pivot：`"AWS" "eu-south-1" "Milan"`、`"Microsoft" "Italy North" Settala Bornasco`、`"Google Cloud" "europe-west12" Turin`、`"Oracle" "eu-turin-1" TIM Enterprise`、`"Polo Strategico Nazionale" "data center" TIM Leonardo Sogei`。
- 双语文种（Trentino-Alto Adige）：`"Rechenzentrum Bozen"`、`"Datacenter Bolzano"`、`"centro dati Trento"`。
- 取消追踪：`"{operator}" "{comune}" data center (respinto OR ritirato OR sospeso OR opposizione)`。

## 官方/监管管线要点（详见 explorer-official.md）

- **MASE VA/VIA/AIA 门户（A）**：搜索 `data center`/`centro dati`/`CED`/运营商名；同时打开 `Info` 与 `Documentazione`（附录 PDF 含市政文件）；提取 MASE ID（ID_VIP/ID_MATTM、Codice procedura）作稳定去重键；`istruttoria tecnica` ≠ 批准。实例：Amazon Data Services Italy Rho/Pero（ID 11344）、DATA4 MIL1 Settimo Milanese/Cornaredo（ID 11512）、STACK/Supernap Siziano（Doc 7938/15674）、Noviglio Mxp I（ID 9499）。
- **2026 procedimento unico**：DL 21/2026 → Law 49/2026；查询 `"procedimento unico" "data center" "{comune}"`、`site:mase.gov.it "procedimento unico" "centri dati"`、`"avviso al pubblico" "centro dati"`。
- **市政 SUE/SUAP**：impresainungiorno.gov.it（流程路由 A，提交文件常不公开）；`albo pretorio`/`amministrazione trasparente`/市议会决议/规划门户；规划计划名称按大区变体。
- **大区 VIA/VAS/AIA 门户**：低于全国阈值的项目走大区线；`site:{regione-domain} "Verifica di assoggettabilita" "data center"`。
- **电网**：Terna 连接流程（A，流程）/Lightbox 数据中心分析（A-/B+）；按地区查 DSO：Unareti/A2A（米兰）、IRETI（都灵/艾米利亚）、AGSM AIM（维罗纳）、Areti（罗马）、e-distribuzione（全国）、Hera；Terna 连接请求 ≠ 可建项目，分开记录。
- **云/公共部门监管**：ACN 云资质目录（A，PA 云供应商种子）、AgID PA Cloud、Strategia Cloud Italia、PSN（A/B，需用许可核实设施）、AGCOM（市场语境）。
- **法律主体 pivot**：Registro Imprese/Telemaco 解析 SPV 与母公司（品牌 ≠ 法律实体）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **IDA（Italian Datacenter Association，B）**：创始成员 Microsoft、Equinix Italy、Rai Way、DATA4、STACK、Digital Realty、Vantage、CBRE；会员/新闻页是生态种子，非设施注册表。
- **贸易媒体**：DCD Italy tag（B，英文交易/建设信息最佳）、Agenda Digitale（B，政策法规）、CorCom/Key4biz/Il Sole 24 Ore/Industria Italiana（B）、本地报（la Provincia Pavese/Il Giorno/MilanoToday/RomaToday 等，C+/B-，常首发市政计划/抗议/购地）。
- **目录（C+ 线索源）**：DataCenterMap、Datacenters.com、Baxtel（超大规模园区线索好）、Datacenterplatform/DC Atlas；须运营商页或许可核实。
- **运营商种子（A=存在/B=容量）**：Aruba（Ponte San Pietro/Bergamo、Arezzo IT1/IT2、Rome IT3/IT4）、Retelit/Irideos（Milan/Corsico/Avalon）、Equinix（Milan ML）、DATA4（Cornaredo MIL01/Vittuone MIL2）、STACK（Siziano/Supernap 系）、Noovle/TIM（Santo Stefano Ticino、Pomezia、Turin、PSN）、Vantage（Milan I/Melegnano 64 MW + Castelletto 32 MW）、Digital Realty、Rai Way（Rome 大项目已批）、CyrusOne（Milan 外首个破土，Segrate）、CloudHQ（MXP4/MXP5）、EdgeConneX（2026 战略利益）、Khazna/Eni（Ferrera Erbognone AI 园区，B 级待许可）、A2A/Redelfi/Magnora/Solaria（能源开发商进入，管线）、Open Hub Med（Palermo/Carini 海底电缆）。
- **状态语义（意语）**：`accordo`/`protocollo`/`manifestazione di interesse`/`studio di fattibilita`=意向；`permesso di costruire`/`VIA`/`AIA`/`AUA`/`provvedimento autorizzatorio`/`delibera`=已许可；`inizio lavori`/`posa della prima pietra`/`cantiere`=在建；`inaugurato`/`operativo`/`messo in esercizio`/运营商页=运营。

## 来源分级

- **A** = 官方/一手：MASE VA/VIA/AIA 或 procedimento unico 记录、Gazzetta Ufficiale 法律、大区/市政许可与规划文件、Terna/DSO 官方连接或电网工程文件、运营商官方设施页（存在/位置）、ACN 云资质目录、MIMIT `interesse strategico nazionale` 公告。
- **B** = 强二级：IDA/协会页、贸易媒体（DCD 等）、法律客户简报、市场报告、有出处的投资/电网新闻（点名运营商/地点/MW 但无主许可）。
- **C** = 弱/未验证：通用数据中心地图、经纪列表、抓取目录、社交媒体、无出处投资声明、SEO 页；目录默认 C，除非官方页/权威记录/披露核实。
- **容量规则**：优先 IT load MW；否则标注为 generator thermal MWt / MVA 连接容量；规划总容量与一期分开；大项目须 ≥2 条证据链（许可+运营商，或许可+电网/环评，或运营商+MASE）；应急发电机热容量与 IT load 不可直接换算。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=IT，divisions=大区/省/市镇）。
2. 建种子：MASE 门户搜索 + 云区域（AWS/Azure/GCP/OCI/PSN）+ 运营商官方页（Aruba/Retelit/Equinix/DATA4/STACK/Noovle/Vantage/Digital Realty/Rai Way/CyrusOne/CloudHQ/EdgeConneX/Open Hub Med）+ DCD Italy tag + IDA 成员。
3. 对每个 division 执行漏斗：全国官方扫描（MASE）→ 2026 单一程序公告 → 云/colo 种子 → 电网（Terna/DSO，请求容量与许可容量分开）→ 大区 VIA/AIA → 市镇 SUE/SUAP/albo/delibere → 法律主体 pivot（Registro Imprese）。
4. 优先地区：Lombardia/Milan 大都会（MASE + Regione Lombardia 页 + 市政 PGT/SUE）→ Lazio/Rome（PSN/Namex/Areti）→ Piemonte/Turin（OCI/Google/TIM）→ Toscana/Arezzo → Veneto/Emilia-Romagna → 南部与岛屿（海底电缆/边缘/IXP 线索）。
5. 去重键：(运营商/法律实体 + 市镇 + 园区/项目名 + MASE ID/程序码 + 地块/地址)；注意品牌 vs SPV（STACK vs Supernap Italia vs Infrastructure Italia Land）、DATA4 campus vs 单体建筑、云区域 vs 宿主伙伴、MASE 附录中的市政文件。
6. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目 division 写 `no_projects: true`；容量区分 `operational` / `under_construction` / `planned_full_buildout_mw`。
7. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核意大利数据中心（大区/省/市镇粒度，Lombardy 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Khazna/Eni Ferrera Erbognone 许可状态、EdgeConneX 战略利益公告细节、CyrusOne Milan 破土与许可、Vantage Castelletto 二期、Microsoft Bornasco/Settala 建设进度、Google `europe-west12` Turin 是否上线、2026 procedimento unico 首批申请记录。
