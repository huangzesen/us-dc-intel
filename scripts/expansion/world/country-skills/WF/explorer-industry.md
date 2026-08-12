# WF 行业探勘者 - 瓦利斯和富图纳数据中心枚举：行业/供应商来源
# WF Explorer Industry - Wallis and Futuna Datacenter Enumeration via Industry/Vendor Sources

Date: 2026-08-12. Scope: Wallis and Futuna (WF) 数据中心、托管、运营商机房、电缆登陆站、云/卫星误报枚举。Manifest 已核对：`subnational_type=precinct`，分区 divisions 精确为 **Alo**、**Sigave**、**Uvea**。行业检索以法语为主，英文为辅。

可靠性分级 Reliability grading:

- **A** = 运营商/厂商官方页、SPT-WF 官方页、监管/许可来源、官方云区域页、采购/官方项目文件、AFD/欧盟官方项目页。
- **B** = 可信行业媒体、本地/地区媒体、承包商案例研究，要求具名当事方与日期。
- **C** = 数据中心目录、电缆地图、PeeringDB/ASN 聚合、社交媒体、VPS/SEO 页面、国家下拉列表、泛市场报告。

行业来源不得单独把“连接性”升级为数据中心。C 级只能作为线索或阴性对照，必须回溯到 A/B 来源。

## 0. 已验证行业基线 Verified Industry Baseline

- 未发现 WF 有公开销售的中立机柜托管、商业 colocation、hyperscale、cloud region 或 Data Center Dynamics/目录级本地设施信号。
- 官方电信主体不是草稿中的 `opt.wf`，而是 **SPT-WF - Service des Postes et Télécommunications de Wallis et Futuna**，官网见 `spt.wf`。行业检索仍可使用 `OPT-NC`，但那指新喀里多尼亚 OPT 与 SPT-WF 的合作，不是 WF 本地运营商品牌。
- 最强设施线索是 SPT-WF 的电信核心、Tui Samoa 电缆端站/登陆相关设备、Manuia/THD/FTTH 接入网。默认类型为 `telecom_cable_station`、`telecom_core`、`telecom_access` 或 `connectivity_only`。
- AFD 官方项目确认 Tui Samoa 接入融资覆盖通往 Wallis 与 Futuna 的分支、端站设备、分支单元、维护；SPT-WF 页面说明 TUI-SAMOA 于 2018 年 4 月有效启用。该项目不构成 commercial_colo。
- Futuna 的 Alo/Sigave 应重点查接入网、Leava/Ono 服务点、卫星/无线、公共服务机房线索。除非出现具名机房/托管设施，默认 no datacenter project。
- 主要误报：瑞士 Wallis/Valais 的数据中心、Vanuatu 的 Futuna、全球供应商的国家下拉选项、网页托管/VPS SEO 页、法国本土云/托管、卫星服务。

## 1. 行业来源地图 Industry Source Map

| 来源/角色 Source / player | URL | 用途 Use | 等级 |
|---|---|---|---|
| SPT-WF | https://www.spt.wf/ | 本地电信官方主体；ADSL、FTTH/THD、Manuia、服务点、电信设施线索 | A |
| SPT-WF THD project | https://www.spt.wf/555-DSY.html | Tui Samoa 启用、FTTH 模式、grands comptes、部署计划 | A |
| SPT-WF Mauga page | https://www.spt.wf/Mauga.html | Manuia 移动回传/塔站线索；用于 tower/connectivity 排除 | A |
| Services de l'État | https://www.wallis-et-futuna.gouv.fr/ | 行政公告、JOWF、采购、项目锚点 | A |
| Assemblée territoriale | https://www.assembleeterritoriale.wf/ | 议会、délibérations、预算/投资 | A |
| AFD Tui Samoa | https://www.afd.fr/fr/projets/raccorder-wallis-et-futuna-au-cable-sous-marin-de-telecommunications-tui-samoa | 电缆分支与端站设备项目 | A |
| ARCEP | https://www.arcep.fr/ | 监管、市场、频谱/运营商核查 | A |
| EEWF / ENGIE Solutions | https://www.engie-solutions.com/fr/nos-implantations/EEWF-Wallis-et-Futuna-production-distribution-energie-98800 | 电力运营背景与负载交叉验证 | A |
| La 1ère Wallis et Futuna | https://wallisetfutuna.la1ere.fr/ | 本地新闻：断网、Starlink、电力、公共项目 | B |
| Gouvernement de la Nouvelle-Calédonie | https://gouv.nc/actualites/13-08-2020/lopt-et-wallis-et-futuna-lies-par-le-numerique | OPT-NC 与 SPT-WF 合作、Tui Samoa 背景 | B/A for NC official context |
| Outremers360 / Tahiti Infos / LNC / RFI | https://outremers360.com/ ; https://www.tahiti-infos.com/ ; https://www.lnc.nc/ ; https://www.rfi.fr/ | 地区媒体线索；需回溯官方 | B |
| Submarine Networks / Submarine Cable Map | https://www.submarinenetworks.com/ ; https://www.submarinecablemap.com/ | 电缆路由线索；官方来源优先 | C/B |
| DataCenterMap / Cloudscene / PeeringDB | https://www.datacentermap.com/ ; https://cloudscene.com/ ; https://www.peeringdb.com/ | 阴性对照、ASN/目录线索 | C |
| Starlink / Kacific / SES | https://www.starlink.com/ ; https://kacific.com/ ; https://www.ses.com/ | 卫星连接性；不是 DC | A for service availability only |

## 2. 运营商与供应商扫网 Operator And Vendor Sweep

### 2.1 SPT-WF telecom core / access

SPT-WF 是本地电信探勘的起点。官方站点列出电信服务、ADSL、Manuia、Wallis 和 Futuna 服务点；THD 页面说明 TUI-SAMOA 接入和 FTTH/4G 模式。若发现 centrale、NOC、local technique、station d'atterrissement、équipements d'extrémité，先记录为电信设施。

```text
site:spt.wf (hébergement OR colocation OR "centre de données" OR datacenter OR serveur OR baie OR rack)
site:spt.wf ("Tui Samoa" OR "câble numérique" OR "câble sous-marin" OR atterrissement OR "équipements d'extrémité")
site:spt.wf (Mata-Utu OR Leava OR Ono OR Sigave OR Alo OR Uvea OR Mauga) (fibre OR Manuia OR ADSL OR "très haut débit" OR réseau)
"Service des Postes et Télécommunications de Wallis et Futuna" (hébergement OR colocation OR serveur OR réseau OR fibre)
```

判定：SPT-WF 服务点、FTTH、ADSL、4G、Mauga local alimentation 均不是数据中心。只有官方产品/合同写明机柜、服务器托管或数据中心服务时才升级为 `commercial_colo`。

### 2.2 OPT-NC cooperation

`OPT` 检索很容易混淆。`OPT-NC` 是新喀里多尼亚 Office des Postes et Télécommunications；2020 年新喀里多尼亚政府页面确认 OPT-NC 与 SPT-WF 续签合作，合作从 2017 年 TUI SAMOA 上线准备开始。该来源可支持 SPT-WF 技术合作背景，不证明 OPT-NC 在 WF 运营数据中心。

```text
"OPT-NC" "SPT-WF" ("Tui Samoa" OR "Wallis-et-Futuna" OR fibre OR "très haut débit")
"OPT" "Wallis-et-Futuna" ("Nouvelle-Calédonie" OR "SPT-WF") -VPS
```

### 2.3 私营 ISP / hosting / colocation

当前基线：未发现本地私营 ISP 或商业托管商。任何“Wallis and Futuna VPS / dedicated server / colocation”页面通常是全球 SEO 或国家下拉列表。

```text
"Wallis et Futuna" (FAI OR ISP OR WISP OR hébergeur OR "hébergement web" OR colocation OR datacenter) -SPT
"Wallis and Futuna" ("data center" OR colocation OR "dedicated server" OR VPS OR hosting) -Switzerland -Valais
site:arcep.fr ("Wallis-et-Futuna" OR "Wallis et Futuna") (opérateur OR FAI OR autorisation OR déclaration)
"Wallis et Futuna" (PeeringDB OR "autonomous system" OR ASN OR IXP OR "point d'échange")
```

处理：若命中供应商页面但无 WF 地址、本地实体、牌照或设施页，记录 `false_positive` 或 `discarded_reseller_or_directory_lead`。

### 2.4 银行、医院、行政、教育机房

这些实体可能有内部 server room，但一般不构成商业数据中心。

```text
"Banque de Wallis et Futuna" (informatique OR serveur OR "salle informatique" OR "centre de données" OR PCA OR PRA OR sauvegarde)
"Wallis et Futuna" (hôpital OR "Agence de santé" OR administration OR vice-rectorat OR école) ("salle informatique" OR serveur OR hébergement OR infogérance)
"Wallis et Futuna" ("plan de continuité" OR PCA OR "plan de reprise" OR PRA OR sauvegarde) informatique
```

记录规则：必须具名站点、物理房间/设施、用途和来源等级。否则作为 enterprise_server_room_lead，不计入 DC 清单。

### 2.5 卫星与无线连接性

Starlink、Kacific、SES、VSAT、Wi-Fi/4G 均为连接性，不是数据中心。卫星新闻可解释 Alo/Sigave 连接背景，但不得支持 colo。

```text
"Wallis et Futuna" (Starlink OR Kacific OR SES OR satellite OR VSAT) (internet OR disponibilité OR entreprise OR revendeur)
site:wallisetfutuna.la1ere.fr (Starlink OR satellite OR internet OR câble OR "Tui Samoa" OR numérique)
"Futuna" (satellite OR VSAT OR Starlink OR fibre OR internet) "Wallis et Futuna"
```

## 3. 行业媒体、目录与阴性对照 Trade Press, Directories, Negative Controls

高价值媒体：

```text
site:wallisetfutuna.la1ere.fr ("centre de données" OR datacenter OR internet OR câble OR fibre OR Starlink OR numérique OR électricité)
site:outremers360.com "Wallis-et-Futuna" (télécom OR câble OR fibre OR numérique OR énergie)
site:tahiti-infos.com "Wallis-et-Futuna" (télécom OR câble OR fibre OR numérique OR énergie)
site:lnc.nc "Wallis-et-Futuna" (télécom OR câble OR fibre OR numérique OR énergie)
site:rfi.fr "Wallis-et-Futuna" (internet OR câble OR numérique OR Starlink)
```

数据中心/电缆目录：

```text
site:datacenterdynamics.com ("Wallis et Futuna" OR "Wallis and Futuna")
site:datacentermap.com ("Wallis and Futuna" OR "Mata-Utu" OR "Mata Utu")
site:cloudscene.com ("Wallis and Futuna" OR "Mata-Utu" OR "Mata Utu")
site:submarinenetworks.com ("Wallis" "Futuna" "Tui Samoa")
site:submarinecablemap.com ("Wallis" "Futuna" "Tui Samoa")
```

目录处理：

- 瑞士 Wallis/Valais 结果直接 `false_positive`.
- 只有国家下拉列表或全球服务覆盖，不记录设施。
- 目录缺席只是弱阴性信号；最终仍以官方/运营商/采购来源为准。

## 4. 分区行业枚举 Per-Division Industry Enumeration

| 分区 Division | 预期行业发现 | 供应商路径 Vendor route | 决策规则 |
|---|---|---|---|
| Uvea | Mata-Utu 行政/电信核心、SPT-WF 服务点、Tui Samoa 端站线索、EEWF 电力背景、银行/医院内部机房线索 | SPT-WF、AFD、JOWF、Assemblée、ARCEP、EEWF、La 1ère、采购、目录阴性对照 | 电缆/核心记录为 telecom；commercial_colo/government_dc 需 A 级具名；Mauga/Manuia 为 tower/connectivity |
| Alo | Ono/Mala'e 等 Futuna 南部服务点、接入网、卫星/无线、村级公共设施 | SPT-WF、La 1ère、卫星厂商、JOWF、采购 | 默认 no commercial DC；只有具名机房/项目才升级 |
| Sigave | Leava、Vele、Kolia 等 Futuna 北部服务点、接入网、卫星/无线、公共服务 | SPT-WF、La 1ère、卫星厂商、JOWF、采购 | 默认 no commercial DC；Leava 服务点不是 DC |

覆盖检查：本表恰好覆盖 manifest 中 3 个分区各一次：Alo、Sigave、Uvea。

通用分区查询：

```text
"{Division}" "Wallis et Futuna" ("centre de données" OR datacenter OR colocation OR hébergement OR "salle informatique" OR serveur OR cloud OR NOC)
"{Division}" "Wallis et Futuna" (SPT OR fibre OR Manuia OR ADSL OR 4G OR satellite OR VSAT OR Starlink)
"{Division}" "Wallis et Futuna" (centrale OR électricité OR solaire OR photovoltaïque OR EEWF)
```

## 5. 云区域和主权云 Cloud Region Sweep

官方页面：

- AWS Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/

已核实处理：这些官方页面没有 WF/Wallis/Futuna 匹配。法国本土区域、欧洲区域、亚太区域或 cloud de confiance 供应商（OVHcloud、Scaleway、Outscale、Orange Business、Capgemini、Atos 等）均不构成 WF 本地设施，除非采购文件明确要求 WF 本地物理托管。

```text
"Wallis et Futuna" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR "cloud region" OR hyperscale)
"Wallis et Futuna" ("cloud souverain" OR "cloud de confiance" OR "data residency" OR "données hébergées en France")
"Wallis et Futuna" (OVHcloud OR Scaleway OR Outscale OR "Orange Business" OR Capgemini OR Atos) (hébergement OR infogérance OR cloud)
```

## 6. 枚举矩阵 Enumeration Matrix

| 设施类型 Facility type | Uvea | Alo | Sigave |
|---|---|---|---|
| `commercial_colo` | 低；当前无公开证据 | 无预期 | 无预期 |
| `government_dc` | 低-中；需采购/JOWF/项目文件 | 很低 | 很低 |
| `telecom_cable_station` | 中；Tui Samoa 端站/登陆线索 | 低；AFD 提到 Futuna 分支但需站点细分 | 低；同左 |
| `telecom_core` | 中；SPT-WF 主设施/核心网线索 | 低；服务点/接入网 | 低；Leava/Futuna 服务点/接入网 |
| `telecom_access` | 高；FTTH/4G/ADSL | 高；FTTH/卫星/无线 | 高；FTTH/卫星/无线 |
| `enterprise_server_room` | 低-中；银行/医院/行政 | 低 | 低 |
| `tower_edge` | 中；Mauga/Manuia | 低 | 低 |
| `connectivity_only` | 高 | 高 | 高 |

## 7. 升级/降级规则 Grading And Classification Rules

- 升级到 `commercial_colo`: 必须有 A 级来源明确写出本地机柜、rack/baie、server hosting、colocation 或可租用物理空间。
- 升级到 `government_dc`: 必须有官方项目/采购/JOWF 具名数据中心、机房工程或 CTD，并给出状态。
- 保持 `telecom_cable_station`: 电缆分支、登陆、端站设备、传输设备、海缆维护。
- 保持 `telecom_access` 或 `connectivity_only`: FTTH、ADSL、4G、Wi-Fi、Starlink/Kacific/SES/VSAT、服务点、用户接入。
- 降级为 `false_positive`: 仅国家下拉列表、VPS SEO、瑞士 Wallis、Vanuatu Futuna、泛云区域页面、法国本土托管。
- 电力证据只证明可供电性，不证明 DC；任何 >0.5 MW 主张须有 EEWF/领地/采购/AFD 等 A 级电力锚点。

## 8. 命中记录字段 Capture Fields

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

## 9. 实跑检查清单 Run Checklist

- Confirm manifest divisions: Alo, Sigave, Uvea.
- Run SPT-WF official queries first; treat `opt.wf` as unverified/deprecated unless it becomes reachable and linked by official sources.
- Search AFD/JOWF/Assemblée for Tui Samoa, THD, FTTH, grands comptes, terminal equipment, atterrage.
- Search BOAMP/PLACE/JOWF for hosting, infogérance, salle informatique, centre de données.
- Search EEWF/ENGIE and energy law for any large-load claim.
- Search La 1ère and regional media for outages, Starlink/satellite, cable repair or new cable/Futuna extension.
- Search DCD/DataCenterMap/Cloudscene/PeeringDB only as negative controls and lead generators.
- For each positive, assign facility type conservatively and record the exact source URL.

## 10. 来源速查 Source Quick List

- SPT-WF: https://www.spt.wf/
- SPT-WF THD: https://www.spt.wf/555-DSY.html
- SPT-WF Mauga/Manuia line: https://www.spt.wf/Mauga.html
- Services de l'État: https://www.wallis-et-futuna.gouv.fr/
- JOWF: https://www.wallis-et-futuna.gouv.fr/Publications/Publications-administratives/Journal-Officiel-de-Wallis-et-Futuna-JOWF
- Assemblée territoriale: https://www.assembleeterritoriale.wf/
- AFD Tui Samoa: https://www.afd.fr/fr/projets/raccorder-wallis-et-futuna-au-cable-sous-marin-de-telecommunications-tui-samoa
- ARCEP: https://www.arcep.fr/
- EEWF/ENGIE: https://www.engie-solutions.com/fr/nos-implantations/EEWF-Wallis-et-Futuna-production-distribution-energie-98800
- La 1ère WF: https://wallisetfutuna.la1ere.fr/
- OPT-NC cooperation context: https://gouv.nc/actualites/13-08-2020/lopt-et-wallis-et-futuna-lies-par-le-numerique
- BOAMP: https://www.boamp.fr/pages/recherche/
- PLACE: https://www.marches-publics.gouv.fr/
- Cloud checks: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google https://cloud.google.com/about/locations ; Oracle https://www.oracle.com/cloud/public-cloud-regions/
