# WF 官方探勘者 - 瓦利斯和富图纳数据中心枚举：官方/监管来源
# WF Explorer Official - Wallis and Futuna Datacenter Enumeration via Official/Regulatory Sources

Date: 2026-08-12. Scope: 瓦利斯和富图纳 Wallis and Futuna (WF)，法国海外集体 collectivité d'outre-mer。Manifest 已核对：`subnational_type=precinct`，分区 divisions 精确为 **Alo**、**Sigave**、**Uvea**。本文用于通过官方、监管、采购和多边机构来源发现运营中、规划中或应排除的数据中心候选。官方检索以法语为主，英文为辅。

可靠性分级 Reliability grading:

- **A** = 国家/领地官方站点、JOWF 官方公报、Légifrance、ARCEP、SPT-WF 官方站点、官方采购平台、官方云厂商区域页、AFD/欧盟官方项目页。
- **B** = 可信本地或地区媒体、承包商案例研究、具名且带日期的行业/公共项目报道。
- **C** = 目录、地图、SEO/VPS 页面、社交媒体、未署名聚合、泛市场报告。

规则：A 级可证明制度、项目、运营商或服务存在，但不自动证明数据中心设施；B 级可支持候选；C 级只作线索或阴性对照。任何 commercial_colo 或 government_dc 记录必须有 A 级来源明确写出本地物理设施、托管/机柜/数据中心服务或项目。

## 0. 已验证国家基线 Verified Country Baseline

- 人口与需求：WF 人口约 1.1 万，经济与电网规模很小；未发现公开的数据中心注册表、独立数据中心许可证类别或可公开检索的本地建筑许可数据库。数据中心枚举应从政府采购、SPT-WF、电缆项目、能源证据和官方公报开始。
- 分区覆盖：必须逐一覆盖 **Alo**、**Sigave**、**Uvea**。Uvea 是首府 Mata-Utu、主要行政与电信设施所在；Alo 和 Sigave 位于 Futuna 岛，主要预期为接入网、卫星/无线、公共服务机房线索。
- 官方电信运营主体：官方站点为 **Service des Postes et Télécommunications de Wallis et Futuna (SPT-WF)**，见 `spt.wf`。草稿中的 `opt.wf` 未作为当前官方站点确认；使用 `spt.wf` 与国家行政页作为主锚点。SPT-WF 首页列出电信、ADSL、电话、Manuia 移动网、Wallis/Futuna 服务点，并说明光纤部署正在 Wallis 和 Futuna 进行。
- 监管与法律：Légifrance 有适用于 WF 的电子通信法典章节；ARCEP 是法国电子通信、邮政和新闻发行监管机构，ARCEP 检索用于核实监管决定、市场与运营商事项。法律/监管存在性不等于设施证据。
- 国际连接：AFD 官方项目页确认 WF 接入 **Tui Samoa** 海底通信电缆项目，项目起始日期 2016-11-16、AFD 融资 1300 万欧元，范围包括通往 Wallis 和 Futuna 的分支、端站设备、分支单元与维护。SPT-WF 官方页面说明 TUI-SAMOA 接入及有效启用于 2018 年 4 月。电缆登陆/端站默认记录为 `telecom_cable_station` 或 `telecom_core`，不是数据中心。
- 国内接入网：SPT-WF 官方页面说明 THD/FTTH 模式覆盖 Wallis 和 Futuna，并提到先服务 grands comptes（行政和企业）再服务公众；首页提到 Futuna 的 Sigave、Vele、Kolia 等光纤部署。该证据支持接入网/电信项目，不支持 commercial_colo。
- 电力：Légifrance 能源法典确认 WF 公共电力由国家和集体按职责组织，领地是公共配电特许授予机关。当前运营主体以 **EEWF - Eau et Electricité de Wallis-et-Futuna** 为主，ENGIE Solutions 官方页面给出 EEWF 在 Mata-Utu/Kafika 的地址并指向 EEWF 客户站点。任何 MW 级负载或数据中心电力主张必须有 EEWF、领地、AFD 或采购证据。
- 云区域：AWS、Azure、Google Cloud、Oracle OCI 官方区域页未列出 WF 区域或本地云数据中心；法国本土或区域云不等于 WF 设施。

## 1. 已验证官方来源 Verified Official Source Map

| 来源 Source | URL | 已核实用途 Verified use | 等级 |
|---|---|---|---|
| Services de l'État et du Territoire | https://www.wallis-et-futuna.gouv.fr/ | 国家/领地行政、JOWF、公报、公共项目、服务目录 | A |
| JOWF 官方栏目 | https://www.wallis-et-futuna.gouv.fr/Publications/Publications-administratives/Journal-Officiel-de-Wallis-et-Futuna-JOWF | Journal Officiel de Wallis et Futuna 下载入口；用于 arrêté、délibération、补贴与项目公告 | A |
| Assemblée territoriale | https://www.assembleeterritoriale.wf/ | 领地议会、délibérations、预算/投资线索；站点首页已核实 | A |
| SPT-WF | https://www.spt.wf/ | 邮政与电信官方运营主体；光纤、Manuia、ADSL、电话、服务点 | A |
| SPT-WF THD 项目 | https://www.spt.wf/555-DSY.html | TUI-SAMOA 2018-04 启用、THD/FTTH、grands comptes、融资与部署说明 | A |
| SPT-WF 部署进展 | https://www.spt.wf/Mauga.html | Manuia/移动与本地无线站点线索；Mauga 为 telecom/tower，不是 DC | A |
| AFD Tui Samoa 项目 | https://www.afd.fr/fr/projets/raccorder-wallis-et-futuna-au-cable-sous-marin-de-telecommunications-tui-samoa | AFD/欧盟支持的 Tui Samoa 接入；分支到 Wallis 与 Futuna、端站设备、维护 | A |
| Légifrance CPCE | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006071191/LEGISCTA000044950342/ | WF 电子通信适用章节 | A |
| Légifrance énergie | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000023983208/LEGISCTA000031059800/ | WF 电力公共服务组织与领地特许授权 | A |
| ARCEP | https://www.arcep.fr/ | 法国电子通信/邮政监管资料、决定、市场数据 | A |
| BOAMP | https://www.boamp.fr/pages/recherche/ | 国家采购公告，可按 986/Wallis-et-Futuna 过滤 | A |
| PLACE | https://www.marches-publics.gouv.fr/ | 国家采购平台；避免把全国性海外清单误判为 WF 本地设施 | A |
| European Commission OCT page | https://international-partnerships.ec.europa.eu/countries/wallis-and-futuna_fr | 欧盟对 WF 数字/光纤、远程医疗/远程学习支持背景 | A |
| EEWF / ENGIE Solutions | https://www.engie-solutions.com/fr/nos-implantations/EEWF-Wallis-et-Futuna-production-distribution-energie-98800 | 电力/水务运营主体与 Mata-Utu 地址线索 | A |
| AFNIC | https://www.afnic.fr/ | .wf 域名背景；域名存在不等于本地托管 | A |

## 2. 官方设施/项目种子 Current Official Facility / Project Seeds

| 候选 Candidate | 分区 | 状态 | 等级 | 记录方式 |
|---|---:|---|---|---|
| SPT-WF / Tui Samoa 电缆端站或登陆相关设施 | Uvea + Futuna 方向未细分到 Alo/Sigave | 运营中连接性项目；SPT-WF 称 2018-04 有效启用 | A | `telecom_cable_station` / `telecom_core`；无托管产品证据，不记 commercial_colo |
| SPT-WF THD/FTTH grands comptes 部署 | Uvea, Alo, Sigave | 部署/运营接入网 | A | `connectivity_only` 或 `telecom_access`; 不是 DC |
| Manuia/Mauga 移动回传站点 | Uvea | 2016 站点/移动覆盖线索 | A | `tower_edge` / `connectivity_only`; local alimentation shelter 不是 DC |
| SPT-WF 服务点：Mata-Utu, Mua, Hihifo, Leava, Ono | Uvea, Sigave, Alo | 邮政/电信服务点 | A | 可作运营商地理锚点；除非出现机房/交换/托管证据，否则不作 DC |
| EEWF Kafika/Mata-Utu | Uvea | 电力运营背景 | A | power evidence only；不是 DC |
| 政府/行政数据中心 | Uvea 预期较高；Alo/Sigave 低 | 未发现官方具名项目 | 未定 | 只有 JOWF、采购或项目文件具名时记录 `government_dc` |
| 商业机柜托管/colo | 全部 | 未发现官方证据 | 无 | 当前基线为无公开证据；需运营商产品页/合同推翻 |

## 3. 官方枚举流程 Official Enumeration Workflow

1. 先核对 manifest：`Alo`、`Sigave`、`Uvea` 必须各跑一次，不增删分区。
2. 跑国家/领地官方站点与 JOWF：查 `centre de données`、`salle informatique`、`hébergement`、`serveur`、`informatique`、`câble sous-marin`、`fibre`、`télécommunications`、`électricité`。
3. 跑 SPT-WF：确认电信设施、光纤/Manuia/回传/端站；特别区分接入网、塔、端站与可销售托管。
4. 跑采购：BOAMP、PLACE、JOWF、Assemblée délibérations。采购结果若只是软件/SaaS/法国本土托管，记录为 non-local hosting，不计入 WF。
5. 跑电力：EEWF/ENGIE、Légifrance、AFD、JOWF；任何数据中心负载必须能和电力容量、连接申请或建筑/能源公告互相印证。
6. 跑官方云区域页：仅用于缺席核查。云厂商在法国本土或亚太其他地区存在，不构成 WF 设施。
7. 对每个候选给出 `facility_type` 与 `basis_for_status`；没有物理设施证据时保留为 lead 或 false_positive。

## 4. 查询模板 Query Templates

官方站点：

```text
site:wallis-et-futuna.gouv.fr ("centre de données" OR "data center" OR datacenter OR "salle informatique" OR hébergement OR serveur) "Wallis"
site:wallis-et-futuna.gouv.fr ("câble sous-marin" OR "Tui Samoa" OR atterrissement OR fibre OR télécommunications OR numérique)
site:wallis-et-futuna.gouv.fr ("Journal Officiel de Wallis et Futuna" OR JOWF) (informatique OR télécommunications OR électricité OR "câble sous-marin")
site:wallis-et-futuna.gouv.fr (arrêté OR délibération OR subvention) ("Tui Samoa" OR fibre OR informatique OR "salle informatique")
```

议会与领地：

```text
site:assembleeterritoriale.wf (informatique OR numérique OR fibre OR télécommunications OR budget OR investissement)
site:assembleeterritoriale.wf ("centre de données" OR datacenter OR hébergement OR "salle informatique")
"Assemblée territoriale" "Wallis et Futuna" ("Tui Samoa" OR fibre OR "très haut débit" OR numérique)
```

SPT-WF：

```text
site:spt.wf ("centre de données" OR datacenter OR hébergement OR colocation OR serveur OR baie OR rack)
site:spt.wf ("Tui Samoa" OR "câble numérique" OR "câble sous-marin" OR fibre OR "très haut débit" OR FTTH)
site:spt.wf (Mata-Utu OR Leava OR Ono OR Sigave OR Alo OR Uvea) (fibre OR Manuia OR ADSL OR télécommunications)
```

监管与法律：

```text
site:arcep.fr ("Wallis-et-Futuna" OR "Wallis et Futuna") (SPT OR OPT OR opérateur OR fréquences OR décision OR marché)
site:legifrance.gouv.fr "Wallis et Futuna" ("communications électroniques" OR télécommunications OR postes)
site:legifrance.gouv.fr "Wallis et Futuna" ("service public de l'électricité" OR concession OR énergie)
```

采购：

```text
site:boamp.fr "Wallis-et-Futuna" (informatique OR hébergement OR infogérance OR télécommunications OR "centre de données")
site:marches-publics.gouv.fr "Wallis-et-Futuna" (informatique OR hébergement OR infogérance OR télécommunications OR énergie)
"Wallis et Futuna" ("appel d'offres" OR "marché public" OR consultation) (informatique OR hébergement OR "salle informatique" OR fibre)
```

电缆/多边项目：

```text
site:afd.fr "Wallis-et-Futuna" ("Tui Samoa" OR câble OR fibre OR numérique)
site:international-partnerships.ec.europa.eu "Wallis" Futuna (fibre OR numérique OR télémédecine OR "e-learning")
"Wallis et Futuna" "Tui Samoa" (AFD OR "Union européenne" OR SPT OR "mise en service" OR atterrage)
```

电力：

```text
("EEWF" OR "Eau et Electricité de Wallis-et-Futuna" OR ENGIE) ("Wallis-et-Futuna" OR "Wallis et Futuna") (centrale OR réseau OR concession OR électricité)
"Wallis et Futuna" (centrale OR photovoltaïque OR solaire OR "réseau électrique" OR délestage) (Mata-Utu OR Kafika OR Leava OR Futuna)
```

云区域缺席：

```text
"Wallis et Futuna" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR hyperscale OR "cloud region")
site:aws.amazon.com "Wallis"
site:learn.microsoft.com/azure "Wallis"
site:cloud.google.com "Wallis"
site:oracle.com/cloud "Wallis"
```

## 5. 分区官方枚举 Per-Division Official Enumeration

| 分区 Division | 覆盖重点 | 必跑查询 | 预期处理 |
|---|---|---|---|
| Uvea | Mata-Utu、Hahake/Hihifo/Mua、SPT-WF 总部/核心网、政府/银行/EEWF、电缆端站线索 | `Uvea`, `Wallis`, `Mata-Utu`, `Hihifo`, `Mua`, `Kafika`, `Mauga` + 数据中心/电信/电力关键词 | 最高优先；可记录 telecom_core/cable/access、电力背景；government_dc 或 colo 需 A 级具名 |
| Alo | Futuna 南部、Ono/Mala'e、公共服务点、接入网/卫星/无线 | `Alo`, `Ono`, `Mala'e`, `Futuna` + fibre/satellite/telecommunications | 默认 connectivity_only；只有具名机房/项目才升级 |
| Sigave | Futuna 北部、Leava、SPT Futuna 服务点、光纤部署 | `Sigave`, `Leava`, `Vele`, `Kolia`, `Futuna` + fibre/satellite/telecommunications | 默认 connectivity_only；Leava 服务点不是 DC |

覆盖检查：本节恰好覆盖 manifest 中 3 个分区各一次：Alo、Sigave、Uvea。

## 6. 记录字段 Capture Fields

```text
name:
operator_or_owner:
division: Alo | Sigave | Uvea
village_or_site:
coordinates_or_address:
source_url:
source_date:
source_grade: A|B|C
facility_type: commercial_colo | government_dc | telecom_cable_station | telecom_core | telecom_access | enterprise_server_room | tower_edge | connectivity_only | false_positive
status: proposed | planned | procurement | under_construction | operational | discontinued | false_positive
basis_for_status:
capacity_or_power_claim:
power_evidence:
license_or_registry_anchor:
notes:
```

## 7. 判定规则 Decision Rules

- `commercial_colo`: 需要 SPT-WF 或其他官方/合同来源明确写出在 WF 本地提供 colocation、baie/rack、hébergement serveur physique 或同等服务。
- `government_dc`: 需要国家、领地、AFD/欧盟或采购文件具名“centre de données / data center / centre de traitement de données / salle serveurs”及站点或项目状态。
- `telecom_cable_station`: Tui Samoa 分支、端站设备、登陆/aterrage、运营商传输设施。除非出现托管/互联服务证据，不升级为数据中心。
- `telecom_access` / `connectivity_only`: FTTH、ADSL、4G/Manuia、Wi-Fi、卫星、塔、回传站点、终端设备。
- `enterprise_server_room`: 银行、医院、行政系统、学校等内部机房；须有物理房间/站点和用途证据，不按商业 DC 计数。
- `false_positive`: 瑞士 Wallis/Valais、Vanuatu Futuna、泛“Wallis and Futuna”下拉国家列表、全球供应商市场页、VPS SEO 页面、法国本土云/托管。

## 8. 常见陷阱 Pitfalls

- `opt.wf` 不应作为当前主站点；使用 `spt.wf`、国家行政页和 JOWF 核实 SPT-WF。
- Tui Samoa 是海底电缆/端站/接入网证据，不是数据中心证据。
- FTTH/THD、Manuia 4G、Mauga 站点、服务点、邮局、卫星终端均不是数据中心。
- `Wallis` 常误命中瑞士 Valais/Wallis 州；`Futuna` 常误命中瓦努阿图 Futuna。
- 采购平台常把 WF 作为全国/海外服务地点选项列出；这不证明本地设施。
- `.wf` 域名可以托管在法国本土或其他地区，不证明 WF 本地服务器。
- 医疗数据 HDS 法规适用于 WF 不等于本地 HDS 数据中心。

## 9. 来源速查 Source Quick List

- Services de l'État: https://www.wallis-et-futuna.gouv.fr/
- JOWF: https://www.wallis-et-futuna.gouv.fr/Publications/Publications-administratives/Journal-Officiel-de-Wallis-et-Futuna-JOWF
- Assemblée territoriale: https://www.assembleeterritoriale.wf/
- SPT-WF: https://www.spt.wf/
- SPT-WF THD: https://www.spt.wf/555-DSY.html
- AFD Tui Samoa: https://www.afd.fr/fr/projets/raccorder-wallis-et-futuna-au-cable-sous-marin-de-telecommunications-tui-samoa
- ARCEP: https://www.arcep.fr/
- Légifrance CPCE WF: https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006071191/LEGISCTA000044950342/
- Légifrance énergie WF: https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000023983208/LEGISCTA000031059800/
- BOAMP: https://www.boamp.fr/pages/recherche/
- PLACE: https://www.marches-publics.gouv.fr/
- EEWF/ENGIE: https://www.engie-solutions.com/fr/nos-implantations/EEWF-Wallis-et-Futuna-production-distribution-energie-98800
- European Commission WF: https://international-partnerships.ec.europa.eu/countries/wallis-and-futuna_fr
- Cloud absence checks: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google https://cloud.google.com/about/locations ; Oracle https://www.oracle.com/cloud/public-cloud-regions/
