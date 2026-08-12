---
name: wf-datacenter-methodology
location: scripts/expansion/world/country-skills/WF/SKILL.md
description: 瓦利斯和富图纳数据中心查询方法论：precinct 三分区（Alo/Sigave/Uvea），SPT-WF 电信核心与 Tui Samoa 海缆为最强设施线索，商业 colo/政府 DC 须 A 级具名，法语为主检索。Wallis and Futuna datacenter methodology: three precinct divisions, SPT-WF telecom core and Tui Samoa cable strongest facility leads, commercial colo/government DC need A-grade naming, French-primary search.
---

# WF · 瓦利斯和富图纳数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：合并 explorer-official.md 与 explorer-industry.md 双线方法论，指导对瓦利斯和富图纳（Wallis and Futuna, WF）数据中心候选的发现、分级、归属与误报排除。官方线覆盖国家/领地行政站与 JOWF、Assemblée territoriale、SPT-WF、Légifrance/ARCEP、采购（BOAMP/PLACE）、AFD/欧盟项目、EEWF/ENGIE 电力、官方云区域负向；行业线覆盖运营商/厂商扫描、行业媒体与目录负控、分区枚举矩阵、云区域与主权云扫描。官方检索以法语为主，英文为辅。

## 入口

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | wallis-et-futuna.gouv.fr + JOWF、Assemblée territoriale、SPT-WF、Légifrance（CPCE/énergie）、ARCEP、BOAMP/PLACE、AFD Tui Samoa、欧盟 OCT 页、EEWF/ENGIE、AFNIC、官方云区域负向 |
| explorer-industry.md | 行业/厂商/媒体发现 | SPT-WF 电信核心/接入扫描、OPT-NC 合作辨析、私营 ISP/托管负控、银行/医院/行政/教育机房、卫星/无线连接性、La 1ère/区域媒体、目录负控、枚举矩阵、主权云扫描 |

## 核心结构事实

1. **行政区划模型**：manifest 已核对 `subnational_type=precinct`，divisions 精确为 **Alo**、**Sigave**、**Uvea**；不得增删分区。Uvea 是首府 Mata-Utu 与主要行政/电信设施所在；Alo 和 Sigave 位于 Futuna 岛，主要预期为接入网、卫星/无线、公共服务机房线索。
2. **注册库现状**：WF 人口约 1.1 万，经济与电网规模很小；未发现公开的数据中心注册表、独立数据中心许可证类别或可公开检索的本地建筑许可数据库。数据中心枚举应从政府采购、SPT-WF、电缆项目、能源证据和官方公报开始。
3. **法律与监管**：官方电信运营主体为 **Service des Postes et Télécommunications de Wallis et Futuna（SPT-WF）**，官网 `spt.wf`；草稿中的 `opt.wf` 未作为当前官方站点确认，使用 `spt.wf` 与国家行政页作主锚点。Légifrance 有适用于 WF 的电子通信法典章节；ARCEP 是法国电子通信、邮政和新闻发行监管机构，ARCEP 检索用于核实监管决定、市场与运营商事项；法律/监管存在性不等于设施证据。
4. **互联与云**：AFD 官方项目页确认 WF 接入 **Tui Samoa** 海底通信电缆项目（起始 2016-11-16，AFD 融资 1300 万欧元，范围包括通往 Wallis 和 Futuna 的分支、终端设备、分支单元与维护）；SPT-WF 官方页面说明 TUI-SAMOA 于 2018 年 4 月有效启用。电缆登陆/终端默认记录为 `telecom_cable_station` 或 `telecom_core`，不是数据中心。国内接入网：SPT-WF 官方页面说明 THD/FTTH 模式覆盖 Wallis 和 Futuna，先服务 grands comptes（行政和企业）再服务公众；首页提到 Futuna 的 Sigave、Vele、Kolia 等光纤部署。AWS/Azure/Google Cloud/Oracle OCI 官方区域页未列出 WF 区域或本地云数据中心；法国本土或区域云不等于 WF 设施。
5. **设施/项目种子**：SPT-WF / Tui Samoa 电缆终端或登陆相关设施（Uvea + Futuna 方向未细分到 Alo/Sigave，运营中连接性项目，SPT-WF 称 2018-04 有效启用，A，`telecom_cable_station`/`telecom_core`，无托管产品证据不记 commercial_colo）；SPT-WF THD/FTTH grands comptes 部署（Uvea/Alo/Sigave，部署/运营接入网，A，`connectivity_only` 或 `telecom_access`，不是 DC）；Manuia/Mauga 移动回传站点（Uvea，2016 站点/移动覆盖线索，A，`tower_edge`/`connectivity_only`，local alimentation shelter 不是 DC）；SPT-WF 服务点：Mata-Utu、Mua、Hihifo、Leava、Ono（Uvea/Sigave/Alo，邮政/电信服务点，A，可作运营商地理锚点，除非出现机房/交换/托管证据否则不作 DC）；EEWF Kafika/Mata-Utu（Uvea，电力运营背景，A，power evidence only，不是 DC）；政府/行政数据中心（Uvea 预期较高、Alo/Sigave 低，未发现官方具名项目，只有 JOWF、采购或项目文件具名时记录 `government_dc`）；商业机柜托管/colo（全部，未发现官方证据，当前基线为无公开证据，需运营商产品页/合同推翻）。
6. **语言与词汇**：官方检索以法语为主，英文为辅；法语关键词：`centre de données`、`salle informatique`、`hébergement`、`serveur`、`câble sous-marin`、`atterrissement`、`fibre`、`télécommunications`、`électricité`、`très haut débit`、`marché public`、`appel d'offres`；状态词：`proposed`、`planned`、`procurement`、`under_construction`、`operational`、`discontinued`、`false_positive`。
7. **可靠性分级**：A=国家/领地官方站点、JOWF 官方公报、Légifrance、ARCEP、SPT-WF 官方站点、官方采购平台、官方云厂商区域页、AFD/欧盟官方项目页；B=可靠本地或地区媒体、承包商案例研究、具名且带日期的行业/公共项目报道；C=目录、地图、SEO/VPS 页面、社交媒体、未署名聚合、泛市场报告。A 级可证明制度、项目、运营商或服务存在，但不自动证明数据中心设施；B 级可支持候选；C 级只作线索或阴性对照。
8. **计数与去重规则**：任何 commercial_colo 或 government_dc 记录必须有 A 级来源明确写出本地物理设施、托管/机柜/数据中心服务或项目；Tui Samoa 是海缆/终端/接入网证据，不是数据中心证据；FTTH/THD、Manuia 4G、Mauga 站点、服务点、邮局、卫星终端均不是数据中心；`Wallis` 常误命中瑞士 Valais/Wallis 州，`Futuna` 常误命中瓦努阿图 Futuna；采购平台常把 WF 作为全国/海外服务地点选项列出，这不证明本地设施；`.wf` 域名可以托管在法国本土或其他地区，不证明 WF 本地服务器；医疗数据 HDS 法规适用于 WF 不等于本地 HDS 数据中心；电力证据只证明可供电性，不证明 DC，任何 >0.5 MW 主张须有 EEWF/领地/采购/AFD 等 A 级电力锚点。

## 常用查询模板

```text
site:wallis-et-futuna.gouv.fr ("centre de données" OR "data center" OR datacenter OR "salle informatique" OR hébergement OR serveur) "Wallis"
site:wallis-et-futuna.gouv.fr ("câble sous-marin" OR "Tui Samoa" OR atterrissement OR fibre OR télécommunications OR numérique)
site:wallis-et-futuna.gouv.fr ("Journal Officiel de Wallis et Futuna" OR JOWF) (informatique OR télécommunications OR électricité OR "câble sous-marin")
site:wallis-et-futuna.gouv.fr (arrêté OR délibération OR subvention) ("Tui Samoa" OR fibre OR informatique OR "salle informatique")
site:assembleeterritoriale.wf (informatique OR numérique OR fibre OR télécommunications OR budget OR investissement)
site:assembleeterritoriale.wf ("centre de données" OR datacenter OR hébergement OR "salle informatique")
"Assemblée territoriale" "Wallis et Futuna" ("Tui Samoa" OR fibre OR "très haut débit" OR numérique)
site:spt.wf ("centre de données" OR datacenter OR hébergement OR colocation OR serveur OR baie OR rack)
site:spt.wf ("Tui Samoa" OR "câble numérique" OR "câble sous-marin" OR fibre OR "très haut débit" OR FTTH)
site:spt.wf (Mata-Utu OR Leava OR Ono OR Sigave OR Alo OR Uvea) (fibre OR Manuia OR ADSL OR télécommunications)
site:arcep.fr ("Wallis-et-Futuna" OR "Wallis et Futuna") (SPT OR OPT OR opérateur OR fréquences OR décision OR marché)
site:legifrance.gouv.fr "Wallis et Futuna" ("communications électroniques" OR télécommunications OR postes)
site:legifrance.gouv.fr "Wallis et Futuna" ("service public de l'électricité" OR concession OR énergie)
site:boamp.fr "Wallis-et-Futuna" (informatique OR hébergement OR infogérance OR télécommunications OR "centre de données")
site:marches-publics.gouv.fr "Wallis-et-Futuna" (informatique OR hébergement OR infogérance OR télécommunications OR énergie)
"Wallis et Futuna" ("appel d'offres" OR "marché public" OR consultation) (informatique OR hébergement OR "salle informatique" OR fibre)
site:afd.fr "Wallis-et-Futuna" ("Tui Samoa" OR câble OR fibre OR numérique)
site:international-partnerships.ec.europa.eu "Wallis" Futuna (fibre OR numérique OR télémédecine OR "e-learning")
"Wallis et Futuna" "Tui Samoa" (AFD OR "Union européenne" OR SPT OR "mise en service" OR atterrage)
("EEWF" OR "Eau et Electricité de Wallis-et-Futuna" OR ENGIE) ("Wallis-et-Futuna" OR "Wallis et Futuna") (centrale OR réseau OR concession OR électricité)
"Wallis et Futuna" (centrale OR photovoltaïque OR solaire OR "réseau électrique" OR délestage) (Mata-Utu OR Kafika OR Leava OR Futuna)
"Wallis et Futuna" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR hyperscale OR "cloud region")
site:aws.amazon.com "Wallis"
site:learn.microsoft.com/azure "Wallis"
site:cloud.google.com "Wallis"
site:oracle.com/cloud "Wallis"
"{Division}" "Wallis et Futuna" ("centre de données" OR datacenter OR colocation OR hébergement OR "salle informatique" OR serveur OR cloud OR NOC)
"{Division}" "Wallis et Futuna" (SPT OR fibre OR Maniua OR ADSL OR 4G OR satellite OR VSAT OR Starlink)
"{Division}" "Wallis et Futuna" (centrale OR électricité OR solaire OR photovoltaïque OR EEWF)
site:spt.wf (hébergement OR colocation OR "centre de données" OR datacenter OR serveur OR baie OR rack)
site:spt.wf ("Tui Samoa" OR "câble numérique" OR "câble sous-marin" OR atterrissement OR "équipements d'extrémité")
"Service des Postes et Télécommunications de Wallis et Futuna" (hébergement OR colocation OR serveur OR réseau OR fibre)
"OPT-NC" "SPT-WF" ("Tui Samoa" OR "Wallis-et-Futuna" OR fibre OR "très haut débit")
"Wallis et Futuna" (FAI OR ISP OR WISP OR hébergeur OR "hébergement web" OR colocation OR datacenter) -SPT
"Wallis and Futuna" ("data center" OR colocation OR "dedicated server" OR VPS OR hosting) -Switzerland -Valais
"Wallis et Futuna" (PeeringDB OR "autonomous system" OR ASN OR IXP OR "point d'échange")
"Banque de Wallis et Futuna" (informatique OR serveur OR "salle informatique" OR "centre de données" OR PCA OR PRA OR sauvegarde)
"Wallis et Futuna" (hôpital OR "Agence de santé" OR administration OR vice-rectorat OR école) ("salle informatique" OR serveur OR hébergement OR infogérance)
"Wallis et Futuna" ("plan de continuité" OR PCA OR "plan de reprise" OR PRA OR sauvegarde) informatique
"Wallis et Futuna" (Starlink OR Kacific OR SES OR satellite OR VSAT) (internet OR disponibilité OR entreprise OR revendeur)
site:wallisetfutuna.la1ere.fr (Starlink OR satellite OR internet OR câble OR "Tui Samoa" OR numérique)
"Futuna" (satellite OR VSAT OR Starlink OR fibre OR internet) "Wallis et Futuna"
site:wallisetfutuna.la1ere.fr ("centre de données" OR datacenter OR internet OR câble OR fibre OR Starlink OR numérique OR électricité)
site:outremers360.com "Wallis-et-Futuna" (télécom OR câble OR fibre OR numérique OR énergie)
site:tahiti-infos.com "Wallis-et-Futuna" (télécom OR câble OR fibre OR numérique OR énergie)
site:lnc.nc "Wallis-et-Futuna" (télécom OR câble OR fibre OR numérique OR énergie)
site:rfi.fr "Wallis-et-Futuna" (internet OR câble OR numérique OR Starlink)
site:datacenterdynamics.com ("Wallis et Futuna" OR "Wallis and Futuna")
site:datacentermap.com ("Wallis and Futuna" OR "Mata-Utu" OR "Mata Utu")
site:cloudscene.com ("Wallis and Futuna" OR "Mata-Utu" OR "Mata Utu")
site:submarinenetworks.com ("Wallis" "Futuna" "Tui Samoa")
site:submarinecablemap.com ("Wallis" "Futuna" "Tui Samoa")
"Wallis et Futuna" ("cloud souverain" OR "cloud de confiance" OR "data residency" OR "données hébergées en France")
"Wallis et Futuna" (OVHcloud OR Scaleway OR Outscale OR "Orange Business" OR Capgemini OR Atos) (hébergement OR infogérance OR cloud)
```

## 官方/监管管线要点（详见 explorer-official.md）

- 官方来源表：Services de l'État et du Territoire（`wallis-et-futuna.gouv.fr`，A）、JOWF 官方栏目（A）、Assemblée territoriale（`assembleeterritoriale.wf`，A）、SPT-WF（`spt.wf`，A）、SPT-WF THD 项目页（`spt.wf/555-DSY.html`，A）、SPT-WF 部署进展（`spt.wf/Mauga.html`，A；Mauga 为 telecom/tower 不是 DC）、AFD Tui Samoa 项目页（A）、Légifrance CPCE 章节（A）、Légifrance énergie（A，WF 公共电力由国家与集体按职责组织，领地为公共配电特许授予机关）、ARCEP（A）、BOAMP（A，可按 986/Wallis-et-Futuna 过滤）、PLACE（A，避免把全国性海外清单误判为 WF 本地设施）、欧盟 OCT 页（A，数字/光纤/远程医疗/远程学习支持背景）、EEWF/ENGIE Solutions（A，Mata-Utu/Kafika 地址与客户站点）、AFNIC（A，`.wf` 域名背景；域名存在不等于本地托管）。
- 官方枚举流程：先核对 manifest（Alo/Sigave/Uvea 各跑一次，不增删分区）→ 跑国家/领地官方站与 JOWF（查 centre de données/salle informatique/hébergement/serveur/informatique/câble sous-marin/fibre/télécommunications/électricité）→ 跑 SPT-WF（确认电信设施、光纤/Manuia/回传/终端；特别区分接入网、塔、终端与可销售托管）→ 跑采购（BOAMP/PLACE/JOWF/Assemblée délibérations；采购结果若只是软件/SaaS/法国本土托管，记录为 non-local hosting，不计入 WF）→ 跑电力（EEWF/ENGIE、Légifrance、AFD、JOWF；任何数据中心负载必须能和电力容量、连接申请或建筑/能源公告互相印证）→ 跑官方云区域页（仅用于缺失核验；云厂商在法国本土或亚太其他地区存在不构成 WF 设施）→ 对每个候选给出 `facility_type` 与 `basis_for_status`，没有物理设施证据时保留为 lead 或 false_positive。
- 官方设施/项目种子表：SPT-WF/Tui Samoa 电缆终端（Uvea+Futuna，A，telecom_cable_station/telecom_core）；THD/FTTH grands comptes 部署（Uvea/Alo/Sigave，A，connectivity_only/telecom_access）；Manuia/Mauga 回传站点（Uvea，A，tower_edge/connectivity_only）；SPT-WF 服务点 Mata-Utu/Mua/Hihifo/Leava/Ono（A，运营商地理锚点）；EEWF Kafika/Mata-Utu（A，power evidence only）；政府/行政数据中心（未发现官方具名项目，未定）；商业机柜托管/colo（全部，无官方证据）。
- 判定规则：`commercial_colo` 需要 SPT-WF 或其他官方/合同来源明确写出在 WF 本地提供 colocation、baie/rack、hébergement serveur physique 或同等服务；`government_dc` 需要国家、领地、AFD/欧盟或采购文件具名“centre de données / data center / centre de traitement de données / salle serveurs”及站点或项目状态；`telecom_cable_station` 覆盖 Tui Samoa 分支、终端设备、登陆/aterrage、运营商传输设施，除非出现托管/互联服务证据不升级为数据中心；`telecom_access`/`connectivity_only` 覆盖 FTTH、ADSL、4G/Manuia、Wi-Fi、卫星、塔、回传站点、终端设备；`enterprise_server_room` 覆盖银行、医院、行政系统、学校等内部机房，须有物理房间/站点和用途证据，不按商业 DC 计数；`false_positive` 覆盖瑞士 Wallis/Valais、瓦努阿图 Futuna、泛“Wallis and Futuna”下拉国家列表、全球供应商市场页、VPS SEO 页面、法国本土云/托管。
- 常见陷阱：`opt.wf` 不应作为当前主站点，用 `spt.wf`、国家行政页和 JOWF 核实 SPT-WF；Tui Samoa 是海底电缆/终端/接入网证据不是数据中心证据；FTTH/THD、Manuia 4G、Mauga 站点、服务点、邮局、卫星终端均不是数据中心；`Wallis` 常误命中瑞士 Valais/Wallis 州、`Futuna` 常误命中瓦努阿图 Futuna；采购平台常把 WF 作为全国/海外服务地点选项列出；`.wf` 域名可托管在法国本土或其他地区；HDS 法规适用不等于本地 HDS 数据中心。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 已验证行业基线：未发现 WF 有公开销售的中性机柜托管、商业 colocation、hyperscale、cloud region 或 DCD/目录级本地设施信号；官方电信主体不是草稿中的 `opt.wf` 而是 SPT-WF（`spt.wf`）；行业检索仍可使用 `OPT-NC` 但那指新喀里多尼亚 OPT 与 SPT-WF 的合作，不是 WF 本地运营商品牌；最强设施线索是 SPT-WF 的电信核心、Tui Samoa 电缆终端/登陆相关设备、Manuia/THD/FTTH 接入网，默认类型为 `telecom_cable_station`、`telecom_core`、`telecom_access` 或 `connectivity_only`；Futuna 的 Alo/Sigave 重点查接入网、Leava/Ono 服务点、卫星/无线、公共服务机房线索，除非出现具名机房/托管设施，默认 no datacenter project。
- 主要误报：瑞士 Wallis/Valais 的数据中心、瓦努阿图的 Futuna、全球供应商的国家下拉选项、网页托管/VPS SEO 页、法国本土云/托管、卫星服务。
- 运营商与供应商扫描：SPT-WF 电信核心/接入（起点；若发现 centrale、NOC、local technique、station d'atterrissement、équipements d'extrémité 先记录为电信设施；服务点、FTTH、ADSL、4G、Mauga local alimentation 均不是数据中心，只有官方产品/合同写明机柜、服务器托管或数据中心服务时才升级为 commercial_colo）；OPT-NC 合作（2020 年新喀里多尼亚政府页面确认 OPT-NC 与 SPT-WF 续签合作、自 2017 年 TUI SAMOA 上线准备开始；该来源可支持 SPT-WF 技术合作背景，不证明 OPT-NC 在 WF 运营数据中心）；私营 ISP/hosting/colocation（当前基线未发现本地私营 ISP 或商业托管商，任何“Wallis and Futuna VPS / dedicated server / colocation”页面通常是全球 SEO 或国家下拉列表，若命中供应商页面但无 WF 地址、本地实体、牌照或设施页，记录 false_positive 或 discarded_reseller_or_directory_lead）；银行/医院/行政/教育机房（可能有内部 server room，一般不构成商业数据中心，必须具名站点、物理房间/设施、用途和来源等级，否则作为 enterprise_server_room_lead 不计入 DC 清单）；卫星与无线连接性（Starlink、Kacific、SES、VSAT、Wi-Fi/4G 均为连接性不是数据中心，卫星新闻可解释 Alo/Sigave 连接背景但不得支持 colo）。
- 行业媒体、目录与阴性对照：高价值媒体——La 1ère Wallis et Futuna、Gouvernement de la Nouvelle-Calédonie（OPT-NC 合作背景）、Outremers360、Tahiti Infos、LNC、RFI（B 级，需回溯源官方）；Submarine Networks / Submarine Cable Map（C/B 海缆路由线索，官方来源优先）；DataCenterMap/Cloudscene/PeeringDB（C 级阴性对照/ASN 线索）；Starlink/Kacific/SES（仅服务可用性 A）。目录处理：瑞士 Wallis/Valais 结果直接 false_positive；只有国家下拉列表或全球服务覆盖不记录设施；目录缺失只是弱阴性信号，最终仍以官方/运营商/采购来源为准。
- 分区行业枚举矩阵：Uvea（Mata-Utu 行政/电信核心、SPT-WF 服务点、Tui Samoa 终端线索、EEWF 电力背景、银行/医院内部机房线索——电缆/核心记录为 telecom；commercial_colo/government_dc 需 A 级具名；Mauga/Manuia 为 tower/connectivity）；Alo（Ono/Mala'e 等 Futuna 南部服务点、接入网、卫星/无线、村级公共设施——默认 no commercial DC，只有具名机房/项目才升级）；Sigave（Leava/Vele/Kolia 等 Futuna 北部服务点、接入网、卫星/无线、公共服务——默认 no commercial DC，Leava 服务点不是 DC）。
- 升级/降级规则：升级到 commercial_colo 必须有 A 级来源明确写出本地机柜、rack/baie、server hosting、colocation 或可租用物理空间；升级到 government_dc 必须有官方项目/采购/JOWF 具名数据中心、机房工程或 CTD 并给出状态；保持 telecom_cable_station：电缆分支、登陆、终端设备、传输设备、海缆维护；保持 telecom_access 或 connectivity_only：FTTH、ADSL、4G、Wi-Fi、Starlink/Kacific/SES/VSAT、服务点、用户接入；降级为 false_positive：仅国家下拉列表、VPS SEO、瑞士 Wallis、瓦努阿图 Futuna、泛云区域页面、法国本土托管；电力证据只证明可供电性不证明 DC，任何 >0.5 MW 主张须有 EEWF/领地/采购/AFD 等 A 级电力锚点。
- 捕获字段：`name`、`operator_or_owner`、`division`（Alo | Sigave | Uvea）、`village_or_site`、`coordinates_or_address`、`source_url`、`source_date`、`source_grade`（A|B|C）、`facility_type`（commercial_colo | government_dc | telecom_cable_station | telecom_core | telecom_access | enterprise_server_room | tower_edge | connectivity_only | false_positive）、`status`（proposed | planned | procurement | under_construction | operational | discontinued | false_positive）、`basis_for_status`、`capacity_or_power_claim`、`power_evidence`、`license_or_registry_anchor`、`notes`。
- 实践检查清单：确认 manifest divisions（Alo/Sigave/Uvea）→ 先跑 SPT-WF 官方查询（`opt.wf` 视为未验证/弃用，除非可达并被官方来源链接）→ 搜 AFD/JOWF/Assemblée（Tui Samoa、THD、FTTH、grands comptes、terminal equipment、atterrage）→ 搜 BOAMP/PLACE/JOWF（hosting、infogérance、salle informatique、centre de données）→ 搜 EEWF/ENGIE 与能源法（任何大负载主张）→ 搜 La 1ère 与区域媒体（断网、Starlink/卫星、海缆维修或新电缆/Futuna 延伸）→ DCD/DataCenterMap/Cloudscene/PeeringDB 仅作阴性对照与线索生成 → 每个阳性保守分配设施类型并记录精确来源 URL。

## 维护注意（更新纪律）

- 每次运行先跑 SPT-WF 官方查询，再跑 AFD/JOWF/Assemblée、采购、电力、媒体与云区域清单，最后才变更 WF 设施状态。
- 状态动词驱动：任何 `commissioned`、`mise en service`、`RFS`、`awarded`、`installed`、`accepted` 字样触发重新分级；Tui Samoa 分支到 Futuna 的站点细化（Alo/Sigave 细分）出现官方披露时立即补录。
- 电力与建设证据联动：>0.5 MW 或大负载主张必须能回锚 EEWF/领地/采购/AFD 或能源公告，否则保持 C 或 false_positive。
