---
name: fr-datacenter-methodology
location: scripts/expansion/world/country-skills/FR/SKILL.md
description: |
  France (FR) datacenter discovery & audit methodology — how to enumerate, verify, and update France datacenter projects across 18 regions + 101 départements, using communes/EPCI as the planning-permit unit. France has no single public facility registry: enumeration joins urbanisme permits (permis de construire, national SITADEL open data), environmental records (ICPE / autorisation environnementale / enquête publique / MRAe opinions / Géorisques), grid evidence (RTE transmission-scale; Enedis distribution-scale ~460 DCs / 1.2 GW), official cloud-region pages (AWS/Azure/GCP/OCI/OVHcloud/Scaleway), and operator facility pages. Read this before running FR exploration/audit batches. Routes to explorer-official.md (permits/environment/grid/cloud) and explorer-industry.md (trade press/vendors/department query table).
---

# FR · 法国数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：法国**没有**统一的数据中心设施注册库；枚举需拼接**城市规划许可（permis de construire）**、**环境/预审文件（ICPE/环境影响授权/公众调查）**、**电网信号（RTE/Enedis）**、**云区域官方页**与**运营商官方页**。
> 最强设施证据往往不是许可本身，而是捆绑的 **enquête publique unique / consultation du public**（同时覆盖 autorisation environnementale/ICPE 与 permis de construire）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供法国探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：SITADEL/SDES 建筑许可开放数据、Géoportail de l'Urbanisme、commune/EPCI 门户、省府 ICPE/公众调查、projets-environnement/MRAe/Autorité environnementale、Géorisques 检查、RTE/Enedis 电网证据、DGE/ARCEP 政策、云区域官方页、运营商种子、18 区域+101 省工作流 |
| `explorer-industry.md` | 行业/厂商发现：Le Monde Informatique/DCD France/DCMag/DataCenter POST 贸易媒体、France Datacenter 协会、按区域运营商种子清单、101 省 prefecture site 查询种子表、法语词汇变体、验证配方与优先级 |

## 核心结构事实（框定每次搜索）

1. **无全国设施注册库**：以 commune/EPCI 为许可单元（建筑许可在当地申报），后经全国 **SITADEL** 开放数据浮出（2013 起非住宅许可月度文件）；SITADEL 可能不显式标 “datacenter”。
2. **环境线索常不以“datacenter”为法律类别**：出现在 **installations classées/ICPE**（rubrique 2910/2925）、备用发电机组、燃油罐、电池、冷却系统、`autorisation environnementale`、`enquête publique`、`consultation du public` 卷宗中；省府页与 MRAe 意见常暴露精确 commune、MW、发电机数、场地与分期。
3. **电网**：RTE（输电级）2016 年以来接入 8 个数据中心、签约 800 MW，但 2024 年底最大消耗仅 120 MW——**签约容量可严重高估建成/使用容量**；Enedis（配电级）约 400-460 个接入数据中心、约 1.2 GW。RTE 管大项目，Enedis 管中小项目。
4. **IDF 特殊审批**：大巴黎区大型项目（>5,000 m² 商业场所）还需区域省长批准（`agrément préfectoral`，Code de l'urbanisme R.510-1/R.510-6）——额外 A 级线索。
5. **云区域=区域存在（A），非地址**：AWS `eu-west-3` Paris；Azure France Central (Paris) / France South (Marseille)；GCP `europe-west9` Paris；OCI `eu-paris-1` / `eu-marseille-1`；OVHcloud Gravelines/Paris/Roubaix/Strasbourg（北方 SecNumCloud 区域）；Scaleway DC2-DC5（DC5 >20 MW IT）。
6. **容量字段必须分离**：`surface_m2`、`it_mw`（仅显式 “puissance IT/IT load”）、`grid_mw`（raccordement/签约功率）、`generator_mw`（备用发电，非 IT load）、`campus_plan_mw`（长期营销规划）、`actual_consumption`。
7. 地理：巴黎/Île-de-France 主导 carrier-neutral 与超大规模；Marseille 是海缆/网络枢纽；北部是 OVHcloud 基地；AI/超大规模向电力与工业用地扩散（Dunkerque/Escaudain/Bouchain、EDF/RTE 邻近地、Essonne/Yvelines）。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§4 / explorer-industry.md §2/§5）

- 法语核心词：`datacenter` `data center` `centre de données` `centre de calcul` `salle informatique` `hébergement informatique` `permis de construire` `ICPE` `autorisation environnementale` `enquête publique` `consultation du public` `arrêté préfectoral` `groupes électrogènes` `rubrique 2910` `poste source` `sous-station` `chaleur fatale` `réseau de chaleur`。
- 规划：`"{commune}" "permis de construire" ("data center" OR datacenter OR "centre de données" OR "centre informatique")`、`site:{commune}.fr "permis de construire" "centre de données"`、`site:statistiques.developpement-durable.gouv.fr SITADEL permis construire locaux non résidentiels`。
- 环境：`site:{departement}.gouv.fr (datacenter OR "centre de données") (ICPE OR "autorisation environnementale" OR "enquête publique" OR "consultation du public")`、`site:projets-environnement.gouv.fr (datacenter OR "centre de données" OR Interxion OR Equinix)`、`site:mrae.developpement-durable.gouv.fr ("data center" OR datacenter) "{region}"`、`site:georisques.gouv.fr (datacenter OR "Amazon Data Services France")`。
- 电网：`site:rte-france.com datacenter raccordement France MW`、`site:enedis.fr datacenter "raccordés"`、`"{commune}" datacenter "poste source" OR "sous-station"`。
- 行业：`site:lemondeinformatique.fr datacenter France {operator}`、`site:datacenterdynamics.com/en/ France datacenter {operator OR commune}`、`site:dcmag.fr datacenter {operator}`。
- 实体 pivot：`"{legal entity}" (site:societe.com OR site:pappers.fr OR site:annuaire-entreprises.data.gouv.fr)`、`"{legal entity}" "SIREN" datacenter`、`"{legal entity}" "rubrique 2910"`。
- 状态词：`projet/annonce/protocole/mémorandum/envisagé`=意向；`permis de construire/PC/ICPE/arrêté préfectoral/enquête publique/avis MRAe`=许可证据；`chantier/travaux/première pierre/livraison/mise en service`=在建；`en exploitation`/运营商页=运营；`recours/suspension/annulation`=被诉/暂停。

## 官方/监管管线要点（详见 explorer-official.md）

- 规划：SITADEL/SDES（按申请人名、commune、面积过滤非住宅许可；BAN 地理编码，省代码为稳定键）；Géoportail de l'Urbanisme（查 PLU/PLUi/SCOT 分区兼容性）；commune/EPCI 门户（permis de construire/arrêté/registre des autorisations d'urbanisme/ADS）。
- 环境：省府站点模式 `https://www.{slug}.gouv.fr/`（Enquêtes publiques/ICPE/autorisation environnementale/arrêté préfectoral）；projets-environnement.gouv.fr（如 Interxion MRS4 Marseille 记录）；MRAe/Autorité environnementale 意见（新设施最佳技术文件）；Géorisques 检查报告（识别运营实体与 ICPE rubriques）。
- 电网/政策：RTE SDDR raccordement 资料（签约 MW、投机性容量预留警告）；Enedis Observatoire/开放数据；DGE/entreprises.gouv.fr 数据中心指南与 2025 落地指南 PDF；ARCEP（SREN/Data Act 下云监管，聚合环境数据，非设施清单）。
- 云/colo 种子：AWS/Azure/GCP/OCI/OVHcloud/Scaleway 官方页；Equinix（PA2-PA13x，Saint-Denis/Pantin）、Digital Realty/Interxion（巴黎 13 个数据中心 86.6k m²，Marseille MRS）、DATA4（Nozay/Marcoussis PAR01-03；Escaudain 700 MW/50 亿欧元计划）、Telehouse（Voltaire/Magny-les-Hameaux）、Global Switch（Clichy）、OpCore、Eclairion（Bruyères-le-Châtel，Mistral AI cluster）、NTT（巴黎外 84 MW 园区）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 贸易媒体：Le Monde Informatique（B，最佳法语 IT 贸易源）、DCD France tag（B，M&A/超大规模/AI）、DCMag（B/C）、DataCenter POST（B/C）、GlobalData 项目追踪（C 片段/B 付费记录）、DC Byte/Structure Research/CBRE-JLL 等（B 市场上下文/C 单项目）。
- 协会：France Datacenter（B，成员/参与者种子）、Data Centre World Paris 合作伙伴（B/C）。
- 聚合器：DataCenterMap/datacenters.com/PeeringDB/Baxtel = C（发现），多聚合器一致时地址交叉核对 B-；容量/状态永不只靠聚合器。
- 区域种子：IDF（Digital Realty/Equinix/DATA4/Global Switch/Telehouse/Scaleway/OpCore/Eclairion/NTT）、PACA-Marseille（MRS5/Digital/OpCore/海缆生态）、Hauts-de-France（OVHcloud Roubaix/Gravelines、DATA4 Escaudain、Etix Lille/Tourcoing）、Grand Est（OVHcloud Strasbourg、UltraEdge）、AURA（OpCore/Etix/nLighten Lyon）、Nouvelle-Aquitaine（Equinix BX1、UltraEdge Bordeaux）、Occitanie（Etix Toulouse/Montpellier）。
- 全国运营商 pivot：Orange Business、SFR/Altice、Bouygues Telecom、Free/Iliad、Colt DCS、CloudHQ、CyrusOne、Prologis、Goodman、SEGRO、Icade、Ecritel、Thales、Worldline、Atos/Eviden、OVHcloud、Scaleway、Outscale。

## 来源分级

- **A** = 官方/一手：SITADEL/SDES 许可数据、commune/EPCI 许可令与议会纪要、省府 ICPE/enquête publique/autorisation environnementale、projets-environnement/MRAe/Autorité environnementale、Géorisques 检查、RTE/Enedis（电网聚合）、ARCEP/DGE/Business France（政策）、云区域官方页（区域存在）、运营商官方设施页（存在/位置 A-，容量 B）。
- **B** = 强二级：贸易媒体（DCD、Le Monde Informatique、DCMag、Banque des Territoires、地方经济媒体）、France Datacenter 会员/活动材料、市场报告（DC Byte/Structure Research/CBRE-JLL 等，仅市场上下文）。
- **C** = 弱/未验证：聚合器地图、活动家地图、社交媒体/论坛、泛泛的 DC 地图、GlobalData 片段；仅作线索。
- 验收规则：设施记录需 ≥1 个 A 源或 2 个独立 B 源+本地官方线索；commune/département 已解析；运营商/法人已解析；状态已标；容量字段分离且分级。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=FR，divisions=18 区域+101 省；commune/EPCI 为许可单元）。
2. 全国种子：SITADEL 月度文件 + 官方云/colo 页 + DGE/ARCEP/RTE/Enedis 聚合源。
3. 区域扫：区域省府、MRAe 区域页、区域发展署、能源/余热词、主要 metropole 门户。
4. 省扫：对每省 `site:{slug}.gouv.fr` 查 datacenter/centre de données/ICPE/公众调查（101 省种子表见 explorer-industry.md §5.1；slug 失效时用 `"Préfecture {department}" datacenter`）。
5. commune/EPCI 深挖：许可令、土地交易、议会纪要、PLU 修改、供热网与电网审议（`poste source`/`raccordement`/`chaleur fatale`）。
6. 运营商/实体 pivot：法人名/SIREN/SIRET（annuaire-entreprises.data.gouv.fr/Pappers/Societe.com）重跑官方查询。
7. 电网校验：每个大候选查 RTE/Enedis/本地变电站；grid MW 与 IT load 分开记录。别名处理：Interxion=Digital Realty；Online/Iliad/Scaleway/OpCore 相关但实体不同；”Paris” 常指 91/92/93/94/95 而非 75。输出 world 同 schema；无项目 division 写 `no_projects: true`。
8. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:08Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核法国数据中心（region→département→commune）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：DATA4 Escaudain 700 MW、NTT 84 MW 园区、Eclairion/Mistral Bruyères-le-Châtel 等 AI 项目的许可/电力进度；ARCEP 聚合环境数据发布；海外省（971-976）仅计设施级证据。
