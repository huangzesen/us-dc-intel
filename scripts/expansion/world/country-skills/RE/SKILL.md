---
name: re-datacenter-methodology
location: scripts/expansion/world/country-skills/RE/SKILL.md
description: 留尼汪数据中心发现与审计方法论（bilingual）。Reunion datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (prefecture/ICPE & DREAL planning, ARCEP telecom regulator, EDF SEI/CRE power, BOAMP/PLACE procurement, SAFE/LION/METISS cable-landing context, REUNIX IXP, certification registries, hyperscaler-absence checks) plus industry/trade-press discovery (Omega 1 operator, SFR Business NETCENTER, Zeop/Oceinde, Orange Reunion, local media, directories). Division model: single division Reunion with commune-level sweeps (Le Port highest priority). Read before running RE exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# RE · 留尼汪数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：留尼汪（RE，法国海外省/大区 DROM）无公开全国数据中心注册库，是小型但真实的托管/colo 市场——核心已核实设施为 **Omega 1 / Omega One（Le Port，Groupe Oceinde/Zeop 生态）**，另有 SFR Business Reunion NETCENTER 托管服务、Zeop Entreprise hosting、Orange Reunion 运营商线索；本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双线交叉验证，以地方政府/ICPE、ARCEP、EDF SEI/CRE、BOAMP/PLACE 与运营商一手页主证，目录站仅作 C 级发现；SAFE/LION/METISS 海缆与 REUNIX IXP 只作连接背景。本 skill 汇总两份最终审定的探索报告，作为 RE 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | Prefecture `reunion.gouv.fr`/ICPE/DREAL 规划许可、Region/Departement/TCO/mairie 地方政府、ARCEP 电信监管、EDF SEI/CRE 电力、BOAMP/PLACE 采购、SAFE/LION/LION2/METISS 海缆登陆背景、REUNIX IXP、Uptime/EPI/TIA 认证注册表、AWS/Azure/GCP/OCI 官方云区域负向检查 |
| explorer-industry.md | 行业/厂商发现 | Omega 1 运营商站点、SFR Business Reunion NETCENTER、Zeop/Oceinde、Orange Reunion/Orange Business、本地媒体（clicanoo/linfo/zinfos974/imazpress 等）、DataCenterMap/Baxtel/Cloudscene 目录、REUNIX/PeeringDB、海缆源（Submarine Networks/TeleGeography） |

## 核心结构事实

1. **行政区划模型**：manifest 为 `subnational_type: country`，**单一 division `Reunion`**——所有记录 division 必填 `Reunion`，不得自建省/大区细分；市镇（commune）为第二层检索与地址解析字段（Le Port、Saint-Denis/Sainte-Clotilde/Le Chaudron、Saint-Paul、La Possession、Saint-Pierre、Le Tampon、Saint-Louis、Saint-André、Saint-Benoît、Sainte-Marie、Sainte-Suzanne）。
2. **注册库现状**：无统一可机检数据中心注册库；最接近普查的是 Prefecture/ICPE（`Installations classées`，含发电机/燃烧类别）、BOAMP/PLACE 采购、地方政府规划材料与运营商一手的组合；大型设施应有 permit/ICPE 痕迹。
3. **法律与监管**：RE 为法国 DROM——国家数字政策 DINUM（`numerique.gouv.fr`）、Prefecture 与 DREAL 管 ICPE/规划，ARCEP（`arcep.fr`）验证运营商与市场（Orange Reunion、SRR/SFR、Outremer Telecom/Mobius、Zeop/Oceinde、Idom、Mediaserv/Canalbox）——**电信授权 ≠ 设施注册表**；EDF SEI（`edf-sei.fr`）与 CRE 支持电网连接/约束/PPE 背景。
4. **互联与云**：**SAFE 登陆 Saint-Paul**、**LION/LION2** 连接马达加斯加/留尼汪/毛里求斯并延伸马约特/肯尼亚、**METISS** 见 TeleGeography 元数据——均为 connectivity 记录，非 DC；**REUNIX 为 2026-08 唯一活跃 IXP**（ISOC Pulse 1 个），PeeringDB 需复查；**AWS/Azure/GCP/OCI 官方区域清单均无留尼汪区域**——Azure France South 是马赛/法国本土，不得当留尼汪证据；本地云/托管按本地/运营商服务处理。
5. **设施/项目种子（2026-08 证据状态）**：**Omega 1 / Omega One**（Le Port；TCO 2023-05-04 奠基报道 + `omegaone.re` 运营商站核实存在/地点；宣称留尼汪/印度洋首个等效 Tier 3，ISO 27001 + HDS 徽章；1 MW / 120 机架为 B 级报道值；A 级存在/地点，认证与容量待注册表核实）；**SFR Business Reunion NETCENTER/托管**（`sfrbusiness.re` 一手托管页证明服务存在；目录地址 3 avenue Theodore Drouhet, Le Port 为 C 级，待一手/许可/采购证据匹配）；**Zeop Entreprise hosting/data-center 服务**（`entreprise.zeop.re`，属 Oceinde 生态——先核实是否就是 Omega 1 再建独立设施，防重复）；**Orange Reunion / Orange Business**（运营商/采购枢纽，本遍未核实留尼汪专属 DC 设施页——保持 lead）；**SAFE 登陆站**（Saint-Paul，B 级连接记录）；**REUNIX**（Saint-Denis 大概率，PeeringDB 核实后 B/A，IXP 非 DC）。
6. **语言与词汇**：法语为主、官方法语检索最佳——`centre de données`/`centre de traitement de données`/`datacenter`/`hébergement`/`colocation`/`salle de serveurs`/`permis de construire`/`enquête publique`/`groupe électrogène`/`poste source`/`onduleur`/`climatisation`/`station d'atterrissement`/`câble sous-marin`/`cloud souverain`/`infogérance`/`appel d'offres`；中文监控：留尼汪（数据中心/云计算/托管/海底光缆）。
7. **可靠性分级**：A = 官方/一手（运营商页、政府/地方当局页、监管决定、公开采购、规划/ICPE 文件、公用事业记录、认证注册表、官方云区域页、一手海缆/IXP 证据）；B = 可靠行业/本地媒体或厂商源且具名方/日期/地点；C = 目录、SEO 托管页、社交页、聚合器或未署名市场声明。**逐字段分级**：设施可有 A 级存在、B 级上线细节、C 级容量。
8. **计数与去重规则**：**单 division**，市镇单列；**不重复建 Omega 1**（Zeop/Oceinde 同生态，Zeop 托管引用 Omega 1 前不得另建）；**海缆登陆站不是 DC**（除非源明确把登陆站与 colo/托管绑定）；电信牌照非设施、电力仅佐证；容量不得从海缆带宽、变压器规模、营销形容词或岛市规模推导；"equivalent Tier 3" 与 Uptime Tier III 认证分开存储，需注册表证据；低产出市镇显式记录负向扫描而非删除覆盖。

## 常用查询模板

```text
site:reunion.gouv.fr "centre de données" OR datacenter OR "salle de serveurs" OR "Omega 1"
site:reunion.gouv.fr ICPE "centre de données" OR datacenter OR "groupe électrogène"
site:tco.re "Omega 1" OR datacenter OR "centre de données"
site:regionreunion.com OR site:departement974.fr "datacenter" OR "hébergement" OR "salle serveurs"
"permis de construire" "La Réunion" "centre de données" OR datacenter OR "Omega 1"
site:arcep.fr Réunion Orange SFR Zeop Oc éinde "cahier des charges" OR autorisation
site:edf-sei.fr Réunion "centre de données" OR datacenter OR "Omega 1" OR "poste source"
"Omega 1" "La Réunion" MW OR kVA OR "groupe électrogène" OR "photovoltaïque"
site:boamp.fr "La Réunion" "centre de données" OR hébergement OR "cloud" OR infogérance
site:boamp.fr "La Réunion" datacenter OR "sauvegarde" OR PRA OR PCA
"La Réunion" "appel d'offres" "cloud souverain" OR "centre de données"
"Saint-Paul" Réunion SAFE OR METISS "landing station" OR "station d'atterrissement"
"Le Port" OR "Saint-Paul" Réunion "câble sous-marin" OR "landing station"
"REUNIX" OR "Réunion IX" OR "Reunion Internet Exchange" PeeringDB
"Omega 1" OR "Omega One" "La Réunion" "data center" OR "centre de données"
"Omega 1" "Le Port" "ISO 27001" OR HDS OR "Tier 3" OR "120 racks" OR "1 MW"
"SFR Business Réunion" NETCENTER OR datacenter OR "hébergement" OR PRA OR PCA
"SFR Le Port" "3 avenue Théodore Drouhet" OR "Theodore Drouhet" datacenter
"Zeop entreprise" hébergement OR datacenter OR "data-center"
"Orange Réunion" "centre de données" OR datacenter OR hébergement OR cloud
site:datacenterdynamics.com Reunion OR "La Réunion" "Omega 1" OR datacenter
site:imazpress.com OR site:zinfos974.com "Omega 1" OR "centre de données"
site:clicanoo.re OR site:linfo.re Réunion datacenter OR "centre de données" OR cloud
"La Réunion" "cloud souverain" OR "cloud de confiance" OR "data center"
留尼汪 数据中心 OR 云计算 OR 托管 OR 海底光缆
"La Réunion" "AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region" ; "France South" Azure Marseille "La Réunion"
"{commune}" Réunion "centre de données" OR datacenter OR "salle de serveurs" OR hébergement OR colocation
"{commune}" Réunion "groupe électrogène" OR "poste source" OR onduleur OR climatisation
site:datacentermap.com "{commune}" Réunion ; "{commune}" "data center" "permis de construire"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **规划/ICPE/DREAL**：Prefecture `reunion.gouv.fr`、Region `regionreunion.com`（可能 Cloudflare 拦截）、Departement `departement974.fr`、TCO `tco.re`、Saint-Denis `saintdenis.re`、DINUM `numerique.gouv.fr`；用地方政府/规划记录证明市镇、地块、许可、建设日期、发电机/UPS/冷却范围与公共部门用途；含发电机/燃料储运的数据中心查 DREAL/ICPE。高价值源：TCO 文章与 Oceinde 新闻资料 PDF（`tco.re/wp-content/uploads/2023/05/dp-omega1-04-05-2023.pdf`）。
- **ARCEP**：验证运营商与市场（Orange Reunion、SRR/SFR、Outremer Telecom、Zeop/Oceinde、Idom、Mediaserv/Canalbox、频率授予、海外观察站材料）；不得从电信授权推断数据中心。
- **EDF SEI / CRE**：`edf-sei.fr`、`cre.fr`、PPE 文件支持电网连接、电气约束、可再生能源供给、发电机/UPS/变压器规模与孤岛电网约束；电力文件单独不能创建 DC 记录。
- **采购**：BOAMP `boamp.fr`、PLACE `marches-publics.gouv.fr`、TCO/Region/Departement/mairie 采购页为政府托管/云/灾备/服务器机房迁移的 A 级线索；除非招标或中标点名设施/地址，位置保持 null、状态 `lead/procurement`。
- **认证注册表**：Uptime Institute awards、EPI/TIA-942 certified sites、TIA——"equivalent Tier 3" 不等于 Uptime Tier III 认证；ISO 27001/HDS 声明须含颁发机构/注册表/证书号，否则按运营商声明存；国家选择器列出 Reunion 不是认证证据。
- **云区域负向**：AWS/Azure/GCP/OCI 官方页每次刷新复查；当前结论为无留尼汪区域；转售托管、CDN edge、本地伙伴页、"France South" 与法国本土区域均不得当留尼汪区域证据。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **优先运营商扫描**：Omega 1（`omegaone.re` + TCO 文章/PDF + DCD + Imaz Press + Zinfos974 + DataCenterMap + Baxtel）——存在/运营商站/Le Port 地点为 A，上线叙事与技术值（1 MW/120 racks）为 B，认证字段须注册表核实；SFR Business Reunion NETCENTER（`sfrbusiness.re/entreprises-et-collectivites/hebergement/`，目录地址 C 级）；Zeop Entreprise（`entreprise.zeop.re`，含 Hébergement 路径——先解清与 Omega 1 关系，避免重复设施）；Orange Reunion/Orange Business（`reunion.orange.fr`、`orange-business.com`——仅运营商/监管背景，设施保持 lead）。
- **行业媒体与目录**：本地媒体集 clicanoo.re、linfo.re、zinfos974.com、ipreunion.com、freedom.re、lequotidien.re、la1ere.francetvinfo.fr/reunion/（具名/日期/地点则 B）；行业 DCD、Imaz Press、Capacity、Telecom Review；目录 DataCenterMap（Omega 1 + SFR Le Port 两条种子）、Baxtel、Cloudscene、Datacenters.com——C 级种子，只有一手/官方源证明同一设施/字段才升级为 A。
- **目录到一手工作流**：目录只提供名字/运营商/地址/容量种子 → 匹配一手域（omegaone.re、oceinde.com、entreprise.zeop.re、sfrbusiness.re、reunion.orange.fr、arcep.fr、tco.re、reunion.gouv.fr、boamp.fr、marches-publics.gouv.fr）→ 谨慎分配市镇（Omega 1 = Le Port；SFR 目录地址 = Le Port 待核实；Sainte-Clotilde/Le Chaudron = Saint-Denis；SAFE 登陆 = Saint-Paul）→ 若服务页只证明托管而无具名物理设施，建服务/lead 注记而非完整设施记录。
- **诚实结论（2026-08）**：Omega 1 为唯一已核实本地 DC；SFR/Zeop/Orange 为服务/lead 层；海缆与 IXP 为连接背景；超大规模云区域为 verified negative；Uptime/EPI/TIA 留尼汪认证本遍为负向。

## 维护注意（更新纪律）

- **更新节奏**：每季度——Omega 1 状态/认证核实（`omegaone.re`、Uptime/EPI/TIA 注册表）、BOAMP/PLACE 采购扫描（"centre de données"/"hébergement"/"cloud"/"infogérance"）、SFR Le Port 目录地址匹配一手证据；每半年——Prefecture/ICPE 与 DREAL 记录、ARCEP 市场材料、EDF SEI/CRE/PPE 电网文件、云区域清单复核；每年——复查全部 C/U 级条目（SFR 地址、Zeop 关系、目录容量）、海缆/IXP 状态；事件驱动——任何留尼汪超大规模云区域声明或新 ICPE 申请为最大变化。
- **来源核验**：逐一点击 A 级 URL；`regionreunion.com` 与 ISOC Pulse 可能返回 Cloudflare/机器人检查——记录访问限制并用另一主源/可靠源交叉核对；TeleGeography Submarine Cable Map 可能 JS/机器人保护——用搜索摘要/API 可见元数据并交叉 Submarine Networks 或运营商发布。
- **不删除纪律（no-deletion）**：已核实记录不得删除；状态变化改标并保留原始证据链；无支撑条目降级为 U/C 保留而非移除；低产出市镇显式记录 "no public DC evidence found on run date" 而非跳过。
