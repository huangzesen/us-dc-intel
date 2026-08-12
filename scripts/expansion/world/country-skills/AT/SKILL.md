---
name: at-datacenter-methodology
location: scripts/expansion/world/country-skills/AT/SKILL.md
description: |
  Austria (AT) datacenter discovery & audit methodology — how to enumerate, verify, and update Austrian datacenter projects at state (Bundesland) + municipality granularity (9 states in the current manifest). Austria has no national public datacenter permit register: enumeration joins state/municipal building law (Baubewilligung/Bauverfahren/Flächenwidmung), APG + state-DSO grid evidence and EEffG §72a ≥500 kW energy reporting, Auftrag.at/BRZ procurement, cloud-region official pages (Azure Austria East in Vienna; Google Kronstorf in development; no AWS/OCI region), and operator pages (Digital Realty, AtlasEdge, A1, BRZ, LINZ AG, Magenta, VIX) plus the ADCA association. Read this before running AT exploration/audit batches. Routes to explorer-official.md (regulation/energy/permits/procurement/cloud) and explorer-industry.md (operators/associations/IXP/aggregators).
---

# AT · 奥地利数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：奥地利**没有**公开的全国数据中心建设许可注册库（建筑法属州法、市/区执行）；无专用 UVP 清单类型（仅作负向控制）；**EEffG §72a** 要求 IT 电力 ≥500 kW 的数据中心每年公开报告 KPI（能量效率监测点，非设施注册库）。枚举采用“州/市政建筑许可 → APG/州配电运营商电网证据 → 采购/政府 IT → 云区域官方页 → 运营商/IXP”多轨交叉。
> 分区模型：**9 个联邦州（Bundesländer）**（Wien、Niederösterreich、Oberösterreich、Salzburg、Steiermark、Tirol、Vorarlberg、Kärnten、Burgenland）；Wien 为主要产出（Digital Realty/AtlasEdge/A1/BRZ/VIX/Azure），Oberösterreich（Google Kronstorf、LINZ AG）、Steiermark（Magenta Graz）为次集群。
> 已知种子：Azure Austria East（Wien，AZ 支持）、Google Kronstorf（Oberösterreich，建设中）、Digital Realty Wien VIE1/2/VIE13、AtlasEdge VIE001/VIE002、A1（14 座 AT 数据中心、覆盖全部州首府）、BRZ、VIX（Wien 三处）、LINZ AG Linz 1/2、eworx Linz/Perg、Magenta Graz、Nexspace Graz、Citycom、EBRZ。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供奥地利探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：RIS（UVP-G 2000/EEffG/ElWOG/TKG）、Energieeffizienz-Monitoringstelle、E-Control/APG、RTR/Breitbandatlas、州政府与市政建筑许可（Baubewilligung/Bauverfahren/Flächenwidmung）、BRZ/Auftrag.at/BBG/TED 采购、云区域官方页（Azure Austria East、Google Kronstorf、AWS/OCI 负向）、9 州工作流 |
| `explorer-industry.md` | 行业/厂商发现：运营商种子表（Digital Realty/AtlasEdge/A1/BRZ/VIX/LINZ AG/eworx/Magenta/Nexspace/Citycom/EBRZ）、ADCA/ISPA/EuroCloud 协会、ORF/DCD/derStandard 等媒体、DataCenterMap 等目录（C）、VIX/PeeringDB 互连、已知设施证据表 |

## 核心结构事实（框定每次搜索）

1. **无全国许可注册库、无专用 UVP 类型**：建设/空间规划为州法、市/区执行；每州必跑建筑许可 + 电网 + 采购三轨；UVP 仅作负向/控制检查（如 Google Kronstorf 无需 UVP 的辩论）。
2. **EEffG §72a 是独特能源信号**：≥500 kW IT 电力数据中心须每年公开 KPI 报告（energieeffizienzmonitoring.at/rechenzentren/）；是寻找新设施/验证 MW 的官方线索，但不是完整注册库。
3. **电网证据最有效**：APG（输电，官方称当前无空闲输电接入容量）+ 各州 DSO（Wiener Netze、Netz NÖ/OÖ、Salzburg Netz、Energienetze Steiermark/Graz Netze、Kärnten Netz、TINETZ、Vorarlberger Energienetze、Netz Burgenland）；搜 `Netzanschluss`、`Umspannwerk`、`große Last`、`Anschlussleistung`、`Abwärme/Fernwärme`。
4. **采购/政府 IT 出官方信号**：BRZ（联邦数据中心）、Auftrag.at/app.auftrag.at（`Rechenzentrum`/`Colocation`/`Housing`/`Serverraum`）、BBG、TED（EU 门槛以上）；区分设备更新与新建设施。
5. **云区域官方页定界**：Azure Austria East（Microsoft Learn 列 Wien，AZ 支持；无具体地址）、Google Kronstorf（2026-04-23 开工，建设中；不等于 GCP 区域）、AWS/OCI 无奥地利区域（负向核验）；`Austria East` 是区域标签不是地址。
6. **互连证据：VIX + PeeringDB**：VIX 自 1996 年运营、Wien 三处位置（A）；PeeringDB 设施页仅作互连线索（C/B），须回查运营商页/许可/媒体。
7. **“Vienna”陷阱**：`Vienna` 常指美国弗吉尼亚州 Vienna（Vienna, VA）；需奥地利上下文（Wien、.at、邮编）才算数；Equinix 无奥地利 IBX。
8. **拼写与语言**：德语 `Rechenzentrum`/`Datenzentrum`/`Serverfarm`/`Colocation`/`Housing`/`Baubewilligung`/`Bauverfahren`/`Flächenwidmung`/`Betriebsanlage`/`Spatenstich`/`Inbetriebnahme`；每州保留德语查询；机构名（BRZ、LINZ AG、Magenta）按原文搜索。

## 查询模式（复制粘贴模板见 explorer-official.md §3 / explorer-industry.md §4）

- 建筑许可：`site:<state-domain> Rechenzentrum Baubewilligung`、`"Rechenzentrum" "<municipality>" "Flächenwidmung"`、`"Betriebsanlage" "Rechenzentrum" "<state>"`、`filetype:pdf "Rechenzentrum" "<municipality>" "Gemeinderat"`。
- 电网/能源：`site:markt.apg.at Rechenzentrum OR Netzanschluss`、`site:<dso-domain> Rechenzentrum`、`"Netzanschluss" "Rechenzentrum" "<state>"`、`"Umspannwerk" "Rechenzentrum" "<municipality>"`、`"Abwärme" "Rechenzentrum" "Fernwärme" "<city>"`。
- 采购/政府 IT：`site:auftrag.at Rechenzentrum`、`site:bbg.gv.at Rechenzentrum OR Cloud OR Housing`、`site:brz.gv.at Rechenzentrum`、`site:ted.europa.eu Austria Rechenzentrum`、`"Rechenzentrum" "Ausschreibung" "<state>"`。
- 云/超大规模：`"Austria East" "Azure" "Vienna"`、`site:datacenters.google "Kronstorf" Austria`、`"Google" "Kronstorf" "Baubewilligung" OR "Baugenehmigung"`、`site:aws.amazon.com Austria "Region"`、`site:docs.oracle.com OCI Austria region`。
- 州级通用：`site:wien.gv.at Rechenzentrum Baupolizei`（Wien）、`site:noe.gv.at Rechenzentrum`、`site:land-oberoesterreich.gv.at Kronstorf Rechenzentrum`、`site:verwaltung.steiermark.at Rechenzentrum`、`"Rechenzentrum" "<provincial capital>"`。
- 行业/互连：`site:datacenterdynamics.com Austria data center OR datacenter`、`site:orf.at Rechenzentrum Kronstorf OR Nickelsdorf OR Graz`、`site:austriandatacenter.org Mitglieder Rechenzentrum`、`site:vix.at members OR Mitglieder`、`"<operator>" "Rechenzentrum" "Österreich"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 入口：RIS 法律（A）→ 州政府首页 + 市政/区当局（Baupolizei，如 Wien MA 37）→ EEffG §72a/Monitoringstelle → APG/E-Control + 州 DSO → BRZ/Auftrag.at/BBG/TED 采购 → Firmenbuch/GISA 法人核验；内陆国，无海缆工作流，改用 VIX/骨干/PeeringDB。
- 电网：APG 输电接入容量现状 + 各州 DSO 搜索为 MW/接入证据；`Betriebsanlage`（Gewerbeordnung 商业运营许可）是市政/区级官方信号。
- 云：Azure Austria East 记 Wien 区域；Google Kronstorf 记建设中；AWS/OCI 负向核验；Equinix 无奥地利 IBX。
- 证据规则：只算 Baubewilligung/Baubeginn/Inbetriebnahme/运营商设施页/采购或电网直接证据为强证据；策略文件、购地、传言、仅 Widmung 记为线索；`Vienna, VA` 假阳性排除。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商种子：Digital Realty Wien VIE1/VIE2/VIE13（A 官方页）、AtlasEdge VIE001+计划 VIE002（A）、A1 Datacenter Services/Exoscale Vienna zone（A；14 座 AT DC、覆盖全部州首府——用于强制 9 州搜索，不用于编造地址）、BRZ（A）、VIX（A）、LINZ AG Linz 1/2（A）、eworx Linz/Perg（A/B）、Data Center Perg（B/A）、Magenta Graz（A，2022 开业）、Nexspace Graz Alte Poststraße 390/376（A/B）、Citycom（C/B，PeeringDB fac/1119）、EBRZ（B/A）。
- 协会：ADCA（2023 成立，成员/新闻可作运营商种子）、ISPA 成员表、EuroCloud Austria、WKO/Österreichs Energie。
- 媒体：ORF 州频道、derStandard、Die Presse、Kurier、Kleine Zeitung、OÖN、Computerwelt、DCD Austria tag、datacenter-insider（B）。
- 目录（C，仅种子）：DataCenterMap Austria（当前 52 设施/36 运营商）、Baxtel、datacenters.com、ocolo、colocationm、datacenterplatform、Herold。
- 生命周期词汇：`Standortsuche` < `Widmung` < `Bauverfahren/Baubewilligung` < `Baubeginn/Spatenstich` < `Inbetriebnahme` < `EEffG-Meldung`（≥500 kW）。

## 已知设施/项目与证据状态

| 设施/项目 | 州 | 状态与证据 |
|---|---|---|
| Microsoft Azure Austria East | Wien | A（Microsoft Learn 列区域，AZ 支持）；具体地址未公开（U） |
| Digital Realty Wien VIE1/VIE2/VIE13 | Wien | A（Digital Realty 官方页）；DCD 报道 40 MW 购地扩建为 B 线索 |
| AtlasEdge VIE001 + 计划 VIE002 | Wien | A（AtlasEdge 官方页）；DCD 收购报道 B |
| A1 奥地利数据中心网络 / Vienna NGDC（Exoscale 区域） | Wien + 各州首府线索 | A（A1/Exoscale 官方声明）；各城地址需单独取证 |
| BRZ 联邦数据中心 | Wien | A（BRZ 官方页） |
| VIX / VIX1-3 | Wien | A（VIX 官方页，三处位置） |
| Google Kronstorf | Oberösterreich | A（Google 官宣 2026-04-23 开工/建设中，~100 直岗、余热就绪）；DCD/ORF 补充 B |
| LINZ AG TELEKOM Data Center Linz 1/Linz 2 | Oberösterreich | A（运营商/新闻稿） |
| eworx Linz/Perg | Oberösterreich | A/B（运营商页声明） |
| Data Center Perg | Oberösterreich | B/A（Technologiezentrum Perg 自身声明） |
| Magenta Graz | Steiermark | A（Magenta newsroom，2022 开业）+ B（ORF/derStandard 技术细节） |
| Nexspace Graz / COOLtec 系设施 | Steiermark | A/B（Nexspace 运营页；Magenta/COOLtec 背景） |
| Citycom Datacenter Graz | Steiermark | C/B（PeeringDB fac/1119 + Citycom 页）；设施细节待运营商页确认 |
| Digital Burgenland / EBRZ | Burgenland | B/A（公共 IT 提供商自述）；设施具体化待证 |
| Nickelsdorf 大型 DC 传言 | Burgenland | U（项目）；B 仅限 ORF 2026-08-03 传言/谈判报道；无运营商/当局确认 |
| Fragmentix Salzburg AI DC | Salzburg | C 线索；运营商/许可/电网确认前不计入 |
| A1 州首府覆盖（St. Pölten/Innsbruck/Bregenz/Klagenfurt/Eisenstadt/Graz/Linz/Salzburg） | 各州 | A（A1 覆盖声明）；各点设施细节 U/C 待取证 |
| 历史 VRZ Dornbirn | Vorarlberg | C 历史记录，非现行设施 |
| Lakeside Park Klagenfurt | Kärnten | B（科技园本身）；U（作为数据中心） |

## 更新节奏

- 每批次：云区域负向核验（Azure/Google/AWS/OCI）、Google Kronstorf 与 Nickelsdorf 进展、DCD Austria tag、ADCA 新闻、Digital Realty/AtlasEdge/A1/Magenta/LINZ AG 页面、EEffG §72a 新申报。
- 季度：Microsoft/AWS/GCP/OCI 官方区域表、DataCenterMap/Baxtel/PeeringDB/VIX 成员刷新、A1/Exoscale、auftrag.at/TED 采购查询。
- 待办（2026-08-12）：两份 explorer 初稿已完成（codex 复核）；下一步 codex terra agent 分批复核（9 州粒度）；本 skill 作为国家层参考注入。
