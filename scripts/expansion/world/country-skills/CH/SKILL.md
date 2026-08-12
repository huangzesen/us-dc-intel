---
name: ch-datacenter-methodology
location: scripts/expansion/world/country-skills/CH/SKILL.md
description: |
  Switzerland (CH) datacenter discovery & audit methodology — how to enumerate, verify, and update Switzerland datacenter projects at canton + municipality/commune/comune granularity (26 cantons). Switzerland has no single national datacenter facility register and no national building-permit portal: building law and publication practice are cantonal/communal. Enumeration routes through cantonal/municipal permit publication (Baugesuch/Baubewilligung, permis/autorisation de construire, domanda di costruzione/licenza edilizia), official gazettes (Amtsblatt/feuille officielle/foglio ufficiale) and open-data layers (Zurich eBaugesucheZH + current Baugesuche open data, Geneva SAD/SITG, Vaud FAO/CAMAC/GEOVD_CAMAC, Bern eBau, Basel-Stadt Baupublikationen), energy/grid sources (Swissgrid, ElCom, SFOE/BFE studies, local utilities EKS/ewz/EKZ/AEW/BKW/SIG/Romande Energie/IWB/CKW/WWZ), OFCOM telecom context, cloud-region pages (AWS eu-central-2/Zurich, Azure Switzerland North+West, GCP europe-west6, OCI eu-zurich-1), and operator facility pages (Green, STACK/Safe Host, Digital Realty, Equinix, NTT, Swisscom, NorthC). Read this before running CH exploration/audit batches. Routes to explorer-official.md (permit backbone per canton/energy/grid/cloud) and explorer-industry.md (Vigiswiss/trade press/vendors/canton recipes).
---

# CH · 瑞士数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：瑞士**没有**全国公开的数据中心设施注册库，也**没有**全国建筑许可门户；建筑法与公示实践以**州（Kanton）与市镇（Gemeinde/Commune/Comune）**为主——以州为路由单元，再钻取发布 `Baugesuch`/`Baubewilligung`、`permis de construire`、`domanda di costruzione` 公告的市镇。
> 大型项目在**能源/电网文件**中往往比规划摘要更可见（Beringen/Schaffhausen 案例：数据中心可要求新建变电站并成为政治议题）；官方许可是三语（德/法/意）分散发布，须先搜本地语言再搜英文。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供瑞士探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：联邦基线（ch.ch/Boverket 流程、opendata.swiss、RegBL、调和建筑分区）、Zurich eBaugesucheZH/开放数据、Vaud FAO-CAMAC/Geneva SAD-SITG/Bern eBau/Ticino UDC/Basel Baupublikationen、Schaffhausen/Beringen 官方模板（许可 PDF + EKS）、SFOE/BFE 能耗与余热研究、Swissgrid/ElCom/当地电力公司、OFCOM 电信语境、云区域官方页（AWS/Azure/GCP/OCI）、运营商种子、26 州路由表、提取工作流与信心分级 |
| `explorer-industry.md` | 行业/厂商发现：Vigiswiss/asut/SwissICT/Digitalswitzerland 协会、DCD/Netzwoche/inside-it/ICTjournal/Computerworld 等贸易媒体、DataCenterMap/Baxtel/PeeringDB 目录、运营商/开发商种子（Green/Digital Realty-Interxion/Equinix/NTT/Safe Host-STACK/NorthC/Vantage/AtlasEdge/Swisscom/Aspectra/Exoscale 等）、simap.ch 公共采购与 SHAB 公司事实、三语查询包、26 州配方表、快速验证清单 |

## 核心结构事实（框定每次搜索）

1. **无全国许可库**：以州为操作单元，26 州各有公开路径；市政公示窗口短，旧公告可能从门户搜索消失——用精确运营商名/街道/市镇/地块名反查。
2. **三语搜索**：德语主导 Zurich/Aargau/Bern/Basel/Zug/Luzern/St. Gallen 等；法语主导 Geneva/Vaud/Neuchatel/Jura/Fribourg/Valais；意语主导 Ticino；Graubünden 可能用德语/罗曼什语。核心词：德 `Rechenzentrum`/`Baugesuch`/`Baubewilligung`/`Netzanschluss`/`Unterwerk`/`Notstrom`/`Abwaerme`；法 `centre de donnees`/`permis de construire`/`mise a l'enquete`/`raccordement electrique`/`chaleur fatale`；意 `centro dati`/`domanda di costruzione`/`licenza edilizia`/`allacciamento elettrico`。
3. **公开路径最强的州**：Zurich（eBaugesucheZH + 近 20 天当前 Baugesuche 开放数据）、Geneva（SAD 状态平台 + SITG 地图 + open data）、Vaud（FAO/CAMAC 公示 + GEOVD_CAMAC 图层）；Bern/Ticino 用 eBau/UDC 流程定位市政公示路径。
4. **能源/电网是大型项目的最佳旁证**：Swissgrid 输电框架、ElCom 监管、BFE 研究（2024 年瑞士数据中心耗电近 2.1 TWh，区分商业 colo/云/超大规模与内部企业 DC）、当地电力公司（EKS/ewz/EKZ/AEW/BKW/SIG/Romande Energie/IWB/CKW/WWZ/AET）暴露连接功率/变电站/余热；备用电源与连接功率 ≠ IT load，须分字段。
5. **Beringen（SH）是官方大型负荷模板**：2021-07-20 州建筑监察许可、未被上诉、法律生效；Amtsblatt 公告（GB Nr. 862、Industriestrasse 6）+ 州政府决策 PDF + EKS 媒体稿揭示运营商（STACK/Safe Host）、MW/负荷与变电站需求——公示短文 + 政府回应/电力公司文件组合是提取关键。
6. **云区域=城市级种子（A），非设施地址**：AWS Europe (Zurich) `eu-central-2` 3 AZ（2022-11-08 开）；Azure Switzerland North=Zurich + Switzerland West=Geneva；GCP `europe-west6` Zurich 3 zones；OCI `eu-zurich-1`。
7. **主集群**：大苏黎世（Zurich/Opfikon-Glattbrugg/Ruemlang/Schlieren/Dielsdorf/Lupfig-AG/Rafz/Beringen-SH）、日内瓦-沃州弧（Geneva/Gland/Lausanne-Renens）、Bern/Zollikofen/Ittigen、Ticino（Lugano/Manno/Melano），以及 Basel/Zug/Luzern/St. Gallen 次级与公共部门/HPC。
8. **facility_type 必须保留**：银行/政府/电信/大学/医院/企业服务器设施是真实数据中心但不一定是商业 colo——用 `commercial_colo`/`hyperscale_cloud`/`telecom`/`public_sector`/`enterprise`/`HPC-research` 分类。

## 查询模式（复制粘贴模板见 explorer-official.md §1、§4 / explorer-industry.md §4、§6）

- 许可：`"{municipality}" "Rechenzentrum" "Baugesuch"`、`"{canton}" "Rechenzentrum" "Amtsblatt"`、`site:{municipality-domain} Rechenzentrum Baugesuch`、`filetype:pdf "Rechenzentrum" "Auflagefrist"`、`"{commune}" "centre de donnees" "mise a l'enquete"`、`site:ge.ch "data center" "autorisation de construire"`、`"{comune}" "centro dati" "domanda di costruzione"`、`site:ti.ch "centro dati" "licenza edilizia"`。
- 能源/电网：`site:bfe.admin.ch Rechenzentren Schweiz Stromverbrauch`、`site:pubdb.bfe.admin.ch Rechenzentren Schweiz`、`site:swissgrid.ch Rechenzentrum Netzanschluss`、`site:elcom.admin.ch Rechenzentrum`、`"{operator}" "{municipality}" "Unterwerk" OR "substation"`、`"{municipality}" "Rechenzentrum" "Notstrom"`、`"{municipality}" "Rechenzentrum" "Abwaerme" OR "Fernwaerme"`、`site:eks.ch Beringen Rechenzentrum Unterwerk`、`site:ewz.ch Rechenzentrum Netzanschluss`。
- 行业：`site:datacenterdynamics.com Switzerland "data center" {operator}`、`site:netzwoche.ch Rechenzentrum Schweiz {operator}`、`site:inside-it.ch Rechenzentrum Schweiz {operator}`、`site:ictjournal.ch "centre de donnees" Suisse {operator}`、`site:datacentermap.com/switzerland {city}`、`site:baxtel.com/data-centers/switzerland {operator}`。
- 采购/公司：`site:simap.ch ("Rechenzentrum" OR "centre de donnees" OR "centro dati") ("Colocation" OR Housing OR Bau)`、`site:shab.ch ("Datacenter" OR Rechenzentrum) Schweiz`。
- 云 pivot：`"AWS" "Europe (Zurich)" "eu-central-2"`、`"Azure" "Switzerland North" "Switzerland West"`、`"Google Cloud" "europe-west6" Zurich`、`"Oracle" "eu-zurich-1"`。
- 取消/上诉：`"{project}" (abgelehnt OR zurueckgezogen OR sistiert OR Beschwerde OR Einsprache OR recours OR sospeso)`。

## 官方/监管管线要点（详见 explorer-official.md）

- **联邦基线（A）**：ch.ch 许可流程说明、opendata.swiss（州建筑申请/Geneva 授权/Zurich 建筑申请/建筑分区/RegBL 数据集发现枢纽）、RegBL/RBD（EGID/地址校验）、调和建筑分区数据集（用地兼容性，非设施证明）。
- **Zurich（最高优先级）**：eBaugesucheZH、stadt-zuerich.ch、近 20 天当前建筑申请开放数据（WMS/WFS/API）、UVP 页；优先市镇 Zurich/Opfikon-Glattbrugg/Ruemlang/Schlieren/Dielsdorf/Rafz/Wallisellen/Winterthur/Dietikon。
- **Vaud/Geneva（罗曼地）**：Vaud FAO/CAMAC 公示、ACTIS-CAMAC 问卷平台、GEOVD_CAMAC 图层、Geneva SAD 状态平台、SITG 地图（`locautorisationconstruire`）；优先 Gland/Lausanne/Renens/Ecublens/Nyon/Yverdon、Geneva/Vernier/Meyrin/Plan-les-Ouates。
- **Bern/Ticino/Basel 等**：Bern eBau（2022 起电子提交，公开细节仍走市镇）、Ticino UDC 流程与 Lugano `albo comunale`、Basel-Stadt Baupublikationen/e-Kantonsblatt、Basel-Landschaft Bauinspektorat、Schwyz Amtsblatt。
- **能源/监管**：BFE 研究（A-/B+ 聚合）、UVEK 政策稿（A）、Swissgrid 连接框架（A 流程）、ElCom（A 监管）、当地电力公司（A/B，连接/变电站/余热）；OFCOM/BAKOM（A 电信语境，非设施登记）。
- **simap.ch（A 公共采购）**：公共部门数据中心建设/colo/迁移招标；SHAB（A 公司事实）：新 DC 子公司/并购/地址变更，用于法律实体别名。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **协会**：Vigiswiss（B，瑞士数据中心协会，成员/政策语境）、asut（B-/C+，电信）、SwissICT/Digitalswitzerland（C+）、S-GE/州经济促进（C+/B-）。
- **贸易媒体**：DCD（B，最佳国际来源）、Netzwoche（B，德语）、inside-it.ch（B）、ICTjournal（B，法语，罗曼地关键）、Computerworld.ch（B-/C+）、Le Temps/TDG/24 heures/RTS（B-/C+，日内瓦/沃州规划与争议）、NZZ/Handelszeitung/Aargauer Zeitung（B-/C+）、Datacenter-Insider（B，德系运营商扩展）、Telecompaper/Capacity（C+/B-）。
- **目录（C+ 线索）**：DataCenterMap、Baxtel、Datacenters.com、PeeringDB（B-/C+，运营交叉核对）、Cloudscene/Inflect/OCOLO（C）。
- **运营商种子（A=存在/B=容量）**：Green（Lupfig/Zurich West + Dielsdorf + 两个新增 Metro-Campus Zurich 2025 开建）、Digital Realty/Interxion（ZUR1/ZUR2/ZUR3 Glattbrugg）、Equinix（瑞士五家，Zurich+Geneva）、NTT（Zurich 1 Ruemlang，10,500+ m2/20 MW IT load）、Safe Host/STACK（Geneva/Gland SH1-SH3 + ZUR01/Rafz、ZUR02/Beringen、ZUR03）、NorthC（Muenchenstein/Biel 收购）、Vantage（Zurich 线索）、AtlasEdge（Zurich）、Swisscom（Bern/Wankdorf 等，电信设施）、Aspectra/EveryWare/ti&m（中小企业托管）、Exoscale（云逻辑区，非设施）、T Cloud Public（Bern/Zollikofen）、CKW/WWZ/Datacenter Zug/CONVOTIS/Datasource/Moresi/BancaDati（Zug/Ticino）。
- **状态语义（三语）**：`Absicht`/`Planung`/`projet`/`intention`=意向；`Baugesuch`/`Baupublikation`/`mise a l'enquete`/`domanda di costruzione`=申报/公示；`Baubewilligung`/`permis delivre`/`licenza edilizia`/`rechtskraeftig`/`entree en force`=已许可法律生效；`Spatenstich`/`Baustart`/`debut chantier`/`inizio lavori`=在建；`Inbetriebnahme`/`mise en service`/`messa in esercizio`/`eroeffnet`=运营；`abgelehnt`/`zurueckgezogen`/`sistiert`/`recours`/`sospeso`=拒绝/撤回/暂停/上诉。

## 来源分级

- **A** = 官方/一手：州/市镇许可与公报（Amtsblatt/FAO/Foglio）、官方地图/开放数据（eBaugesucheZH/SAD/SITG/CAMAC）、官方电力公司/政府文件、运营商官方设施页（存在/位置）、云区域官方文档（区域存在）、simap.ch 采购、SHAB 公司事实、BFE/UVEK/Swissgrid/ElCom/OFCOM 官方页。
- **B** = 强二级：权威国家/贸易媒体或协会/投资机构（点名运营商/地点/容量）、运营商页容量（未独立核实）、EKS 等电力公司媒体稿（B+/A-）。
- **C** = 弱/未验证：商业数据中心地图、经纪页、抓取目录、无出处市场报告；目录默认 C，须官方/运营商/PeeringDB 核实。
- **容量规则**：优先运营商 IT MW 或许可电气导入；`MVA/kVA` 为视在功率需注明；备用电源 MVA/MW、`Anschlussleistung`、年耗电、冷却/水、余热交付与供热伙伴分字段存储；聚合研究（如 BFE 2.1 TWh）不作设施计数。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=CH，divisions=26 州）。
2. 建种子：运营商/云官方页（AWS/Azure/GCP/OCI/Green/STACK/Digital Realty/Equinix/NTT/Swisscom/NorthC）+ 已知园区（Beringen/Lupfig/Dielsdorf/Glattbrugg/Ruemlang/Gland/Renens/Zollikofen/Lugano）。
3. 对每个州跑三遍：①官方许可（州门户/公报/市镇/开放数据）②能源电网（当地电力公司/变电站/余热）③运营商/云+贸易媒体，回到许可。
4. 对每个候选捕获：州、市镇、地址、地块/GB/CAMAC/SAD/许可号、法律实体与品牌、项目/设施码、`source_status`（application/public_inquiry/permit_granted/legally_binding/construction/operational/expansion）、发布日期、许可机关、source_urls、电网 MW/IT load MW/应急发电/冷却水/余热、信心等级。
5. 去重：Interxion→Digital Realty、Safe Host→STACK、Netrics/NorthC/NTS 旧名、Zurich/Geneva 营销名（可能位于 Glattbrugg/Opfikon/Dielsdorf/Lupfig、Plan-les-Ouates/Gland/Meyrin/Vernier）；云区域与 AZ 数不产生设施记录。
6. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`（含 `facility_type` 字段）；无项目 division 写 `no_projects: true`；容量区分 `operational` / `under_construction` / `planned_full_buildout_mw`。
7. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核瑞士数据中心（26 州粒度，Zurich/AG/SH/GE/VD 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：STACK Beringen/Rafz 许可与建设状态、Green Lupfig/Dielsdorf/Metro-Campus 各期、Digital Realty ZUR 各期、NTT Zurich 1 扩建、NorthC Muenchenstein/Biel、Vantage/AtlasEdge 瑞士线索、Azure Switzerland West 设施、simap.ch 近期公共部门 DC 招标、BFE 未来设施级披露。
