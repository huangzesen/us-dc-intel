# PF Explorer — 官方/监管 (Official / Regulatory) — 法属波利尼西亚数据中心枚举方法

日期：2026-08-12。国家：**PF 法属波利尼西亚 (French Polynesia / Polynésie française / Pōrīnetia Farāni)**。
Manifest 条目已核对：`{"country_code":"PF","country_name":"French Polynesia","subnational_type":"country","divisions":["French Polynesia"]}`。即 **subnational_type = country，仅 1 个分区：`French Polynesia`**。

本文件角度：官方/监管/公共部门证据，包括政府门户、法律文本、电信与频率监管、电力、官方采购、运营商官方设施页、海缆官方公告，以及分区级查询模板与 A/B/C 证据分级。

可靠性分级（Reliability grades）：
- **A** = 一手/法定责任来源：法属波利尼西亚政府与 Service Public 页面、Lexpol/JOPF、Légifrance 扩展至 PF 的法律文本、ANFR 关于 PF 频率/电信权限说明、Autorité polynésienne de la concurrence（APC）意见、OPT/Tahiti Nui Telecom/Tahiti Nui Fortress/Vini/TDF 官方页面、EDT 官方页面、Google Cloud 官方海缆博客、官方采购平台 Te Ariari、ISPF 官方统计、RCS/企业官方法律声明。
- **B** = 较强二手来源：署名本地/区域/行业媒体（Tahiti Infos、TNTV、Polynésie La 1ère、La Dépêche de Tahiti、RNZ Pacific、DCD 等）、AFD 项目页、TeleGeography 报告文本、设备/EPC 厂商新闻稿。
- **C** = 弱线索：Baxtel/DataCenterMap/DataCenters.com、海缆地图聚合站、SEO 主机页、离岸 VPS/VPN 营销、社交媒体、无来源目录、只描述 MoU/剪彩且无技术/采购/业主细节的报道。

---

## 0. 市场基线判断（明确结论）

**法属波利尼西亚不是“无市场”。截至 2026-08，可确认至少 2 个本地数据中心/托管设施线索：**

1. **Tahiti Nui Fortress (TNF)** — Tahiti Nui Telecom（Groupe OPT 体系）品牌，官方页面称其为法属波利尼西亚首个 Data Center，提供 cloud、dedicated servers、security 与 colocation/baie/salle informatique 托管；官方法律声明给出 Tahiti Nui Telecom SAS、RCS Papeete、Papenoo PK 16.7 侧山地址。分类：`operator_colo`，存在/服务/地址为 **A**；容量、实际机柜数、PUE、MW 如非官方规格页给出则降 **B/C**。
2. **TDF Pic Rouge / Papeete data center** — TDF 官方 2025-09-18 新闻宣布在 Papeete 上方 Pic Rouge 开放数据中心，2025-06 交付，首批客户包括 Banque de Polynésie 与 Axians Polynésie，2026 有扩容计划，合规审计验证 Tier III level。分类：`commercial_colo` 或 `operator_colo`（TDF 是广播/电信基础设施运营商，按本项目 schema 选择最贴近类别），存在/地点/状态为 **A**；TNTV/DCD 对容量、投资额、扩容到约 40 baies 等描述为 **B**。

市场结论应写为 **“小型已确认市场 / confirmed small market”**，而不是“无市场”。仍需严格区分：
- 数据中心/托管设施：TNF、TDF Pic Rouge。
- 邻近资产：Honotua、NATITUA、Manatua、Google Honomoana/Tabua 等海缆登陆设施、卫星地面站、OneWeb/Galileo 站点、电信 POP、电力设施。
- 公有云区域：AWS / Azure / Google Cloud / OCI 官方区域列表未显示 PF 区域；Google 在 PF 的资产是海缆/登陆基础设施，不是 GCP region。

分类规则：候选对象先分类再入册 —— `commercial_colo` / `operator_colo` / `government_hosting` / `cable_landing_station` / `telecom_exchange` / `hyperscaler_ict_facility` / `enterprise_server_room`。只有 `commercial_colo` 与 `operator_colo` 计入 DC 市场；海缆登陆站和卫星站不得单独升级为 DC。

---

## 1. 官方与法定来源（Government & Legal）

### 1.1 政府门户、法律文本、统计

已验证/可用入口：
- 法属波利尼西亚政府门户：https://www.presidence.pf/
- Service Public PF：https://www.service-public.pf/
- Lexpol / JOPF 法律数据库：https://lexpol.cloud.pf/ （常见公开入口；`www.lexpol.pf` 可作为发现变体但运行时以可解析域为准）
- ISPF 统计局：https://www.ispf.pf/
- Haut-Commissariat de la République en Polynésie française：https://www.polynesie-francaise.pref.gouv.fr/
- Légifrance PF 适用法律文本：https://www.legifrance.gouv.fr/

用法：
- Lexpol/JOPF/Légifrance 是 **A 级** 法律文本源；用于确认电信授权、建设许可、预算、公共采购、数据保护扩展、政府职责。
- ISPF 只作人口、电力、经济、企业环境上下文；不单独证明设施存在。
- Haut-Commissariat 用于法国国家在 PF 的权限与项目背景，尤其是频率、国家安全、海缆、国家出资项目。

查询模板：
```text
site:presidence.pf ("centre de données" OR datacenter OR "data center" OR "salle serveurs" OR hébergement)
site:service-public.pf ("centre de données" OR datacenter OR "Tahiti Nui Fortress" OR "TDF" OR "Pic Rouge")
site:lexpol.cloud.pf ("centre de données" OR datacenter OR "salle serveurs" OR "hébergement de données")
site:legifrance.gouv.fr "Polynésie française" ("télécommunications" OR "code des postes" OR "données personnelles")
site:ispf.pf (électricité OR énergie OR télécommunications OR numérique)
site:polynesie-francaise.pref.gouv.fr (numérique OR "câble sous-marin" OR datacenter OR "centre de données")
```

### 1.2 电信监管与频率（不要使用不存在的 ARCEP PF）

关键纠正：
- **不存在可用的 `www.arcep.pf` 官方入口；实测不解析。**
- ANFR 的 PF 页面明确说明：法国 CPCE 原则上不适用于 PF，**ARCEP 不主管该领地**；PF 对电信有本地权限，同时国家保留无线电频率等权限，ANFR 在 PF 有法定角色。
- 本地电信授权与规则应回到 **Code des postes et télécommunications de Polynésie française**、Lexpol/JOPF、政府/部长会公告、历史上的 Service des postes et télécommunications / Agence de réglementation du numérique（ARN）线索，以及竞争机构 APC 的正式意见。

一手/强来源：
- ANFR PF 监管说明：https://www.anfr.fr/outre-mer/polynesie-francaise/reglementation
- Code des postes et télécommunications de Polynésie française：经 Lexpol/ANFR 链接进入。
- Légifrance 上的 Loi du pays n° 2011-29：确认公共电信网络和服务需按 PF 法律授权。
- Autorité polynésienne de la concurrence：https://autorite-concurrence.pf/ ，其 2024 电信外部连接意见确认 TNF 所在 Papenoo 站点承载 data center、Honotua、Galileo、OneWeb 等敏感基础设施线索。

查询模板：
```text
site:anfr.fr/outre-mer/polynesie-francaise (télécommunications OR fréquences OR ARCEP OR ANFR)
site:lexpol.cloud.pf ("code des postes et télécommunications" OR "opérateur" OR "autorisation")
site:legifrance.gouv.fr "Polynésie française" "réseaux ouverts au public" télécommunications
site:autorite-concurrence.pf ("télécommunications extérieures" OR "Tahiti Nui Telecom" OR "data center")
"Agence de réglementation du numérique" "Polynésie française" (opérateur OR numérotation OR autorisation)
"Service des postes et télécommunications" "Polynésie française" opérateur
```

### 1.3 数据保护与政府 IT

已验证框架：
- DSI/SIPF 页面确认 RGPD 自 **2019-06-01** 起适用于法属波利尼西亚，并说明法属波利尼西亚政府的 Direction du Système d'Information（DSI）负责行政数字基础设施与服务。
- 不要把草稿中的 “Commission Polynésienne de la Protection des Données Personnelles (CPPDP)” 当作已验证机构；未找到可确认官方入口。默认使用 **CNIL + PF DSI/SIPF** 作为数据保护与政务 IT 上下文。

查询模板：
```text
site:service-public.pf/dsi (RGPD OR "données personnelles" OR "marchés publics" OR hébergement OR "centre de données")
site:cnil.fr "Polynésie française" RGPD
"Direction du Système d'Information" "Polynésie française" (hébergement OR cloud OR "salle serveurs")
"Service informatique de la Polynésie française" (hébergement OR "centre de données" OR "appel d'offres")
```

---

## 2. 官方设施与运营商（Facilities & Operators）

### 2.1 Tahiti Nui Fortress / Tahiti Nui Telecom / Groupe OPT

一手来源：
- Tahiti Nui Fortress：https://www.tnfortress.pf/
- Datacenter：https://www.tnfortress.pf/datacenter/
- Cloud：https://www.tnfortress.pf/cloud/
- Réseaux & sécurité：https://www.tnfortress.pf/reseaux-et-securite/
- Mentions légales：https://www.tnfortress.pf/mentions-legales/
- Tahiti Nui Telecom：https://www.tahitinuitelecom.pf/
- Groupe OPT：https://groupe.opt.pf/

证据规则：
- TNF 官方 datacenter/service/contact/legal pages 可确认 `operator_colo` 存在、服务类型、品牌、法人、Papenoo PK 16.7 地址，等级 **A**。
- 官方称 Tier3+ 或高安全等级可记录为官方声明；如果需要标准化成 Uptime/TIA/EN 认证，必须找到证书或审计机构证据，否则不要写成认证事实。
- Tahiti Nui Telecom/TNF 站点同时包含海缆登陆、卫星、Galileo/OneWeb 等基础设施；这些是邻近资产，不自动等于可销售 DC 容量。

查询模板：
```text
site:tnfortress.pf (datacenter OR "Data Center" OR colocation OR "baie" OR "salle informatique")
site:tnfortress.pf (cloud OR "serveurs dédiés" OR firewall OR "réseaux")
site:tnfortress.pf ("PK16,7" OR Papenoo OR "Tahiti Nui Telecom" OR RCS)
site:tahitinuitelecom.pf (datacenter OR "Tahiti Nui Fortress" OR cloud OR Papenoo)
site:groupe.opt.pf ("Tahiti Nui Fortress" OR datacenter OR "centre de données")
```

### 2.2 TDF Pic Rouge / Papeete

一手来源：
- TDF 官方新闻：https://www.tdf.fr/en/tdf-inaugure-son-premier-data-center-a-papeete-en-polynesie-francaise/
- TDF data center/edge pages：https://www.tdf.fr/ （站内 Edge Data Center / regional colocation pages）

证据规则：
- TDF 官方新闻可确认：Papeete/Pic Rouge、opening announced 2025-09-18、delivered June 2025、data hosting solutions、first customers、planned 2026 extension、Tier III level compliance audit。等级 **A**。
- TNTV/DCD 可补充“约 40 baies”、“90 million F CFP”等细节，等级 **B**，除非 TDF 或合同/许可文本确认。
- 设施坐标/精确地址若来自目录站，最多 **C**；官方只给 Pic Rouge/Papeete 时，地址精度不应过写。

查询模板：
```text
site:tdf.fr Papeete ("data center" OR datacenter OR "centre de données" OR "Pic Rouge")
"TDF" "Pic Rouge" "Papeete" ("data center" OR datacenter OR "centre de données")
"TDF" "Polynésie française" ("data center" OR "hébergement" OR "Tier III")
```

### 2.3 Vini / ONATi / 其他本地运营商

已验证口径：
- ONATi 是 Groupe OPT 体系内的综合电信运营商，产品主要以 Vini 品牌销售；把 Vini/ONATi 作为电信运营商与客户接入渠道，不要把每个网络 POP 都记为 DC。
- Lycamobile 页面存在“French Polynesia”入口，但未验证其本地数据中心设施；仅作 MNO/网络线索。
- PMT/Vodafone、Viti 等运营商线索需回到 Lexpol/政府授权或官方企业页面确认。

查询模板：
```text
site:onati.pf (datacenter OR "centre de données" OR cloud OR hébergement OR colocation)
site:vini.pf (datacenter OR "centre de données" OR cloud OR "salle serveurs")
"ONATi" "Tahiti Nui Fortress" OR "Data Center"
"Vini" "Polynésie française" (datacenter OR hébergement OR cloud)
"Lycamobile" OR "Vodafone" OR "Viti" "Polynésie française" (datacenter OR "centre de données" OR hébergement)
```

---

## 3. 海缆、登陆站、卫星（Connectivity Assets）

一手/强来源：
- Groupe OPT NATITUA 新闻：NATITUA 由 OPT 与 Alcatel Submarine Networks 合作，连接 Tahiti 与 Tuamotu/Marquises 多岛，容量声明 10 Tbps 级。
- AFD NATITUA 项目页：确认 2018 起项目、20 个 Tuamotu/Marquesas 岛屿、OPT 受益方、AFD 600 万欧元融资。
- Google Cloud South Pacific Connect：https://cloud.google.com/blog/products/infrastructure/honomoana-and-tabua-subsea-cables-connect-south-pacific
- Google Cloud Bulikula/Halaihai：https://cloud.google.com/blog/products/infrastructure/introducing-bulikula-and-halaihai-subsea-cables-to-connect-the-central-pacific
- APC 2024 电信外部连接意见：确认 Honotua、Manatua、Natitua、Google South Pacific Connect 对 PF 电信市场的意义。

事实口径：
- **Honotua**：Tahiti-Hawaii 国际连接，并有 Tahiti、Moorea、Huahine、Raiatea、Bora Bora 国内段；APC/OPT/海缆源均可作为线索。登陆站不等于 DC。
- **NATITUA**：不是 Tahiti-Hawaii 国际海缆；它是连接 Tuamotu/Marquesas 外岛的国内/区域扩展项目。草稿中的 “NATITUA：Tahiti-Hawaii” 应删除。
- **Manatua**：连接 PF、Cook Islands、Niue、Samoa；在 PF 国际冗余中重要，应纳入查询。
- **Google Honomoana / Tabua / interlink**：Google 官方说会在 Fiji 与 French Polynesia 建设物理多样化登陆站并以 interlink cable 连接；在官方 RFS 前按 `planned`/`under_construction` 或 `near_completion_unverified`，不得当作 Google Cloud region。
- **MANAIA / Hawaiki Nui**：以媒体/行业线索为主，需回挂 OPT/Google/政府/法律文本；无官方 RFS 时不得记为 operational。

查询模板：
```text
site:groupe.opt.pf (Honotua OR NATITUA OR Manatua OR MANAIA OR "câble sous-marin")
site:service-public.pf/dgen (Honotua OR NATITUA OR Manatua OR "câble sous-marin")
site:afd.fr Natitua "French Polynesia" OR "Polynésie française"
site:cloud.google.com/blog/products/infrastructure (Honomoana OR Tabua OR Bulikula OR Halaihai) "French Polynesia"
site:autorite-concurrence.pf (Honotua OR Manatua OR Honomoana OR Tabua OR "télécommunications extérieures")
"Papenoo" ("Honotua" OR "Tahiti Nui Telecom" OR "station d'atterrissement")
```

---

## 4. 电力（Power）

一手来源：
- Électricité de Tahiti（EDT）：https://www.edt.pf/
- ISPF 与政府能源页面：用作电力、发电结构、价格和需求上下文。
- 设施一手页：TNF/TDF 对绿色能源、光伏、热回收、冗余供电的声明。

用法：
- 电力来源只证明电力上下文，不证明 DC 设施。
- 若发现新项目，搜索 `poste source`、`ligne HT`、`groupe électrogène`、`alimentation électrique`、`photovoltaïque`、`MW`、`Tier III`、`climatisation`。

查询模板：
```text
site:edt.pf (datacenter OR "centre de données" OR "poste source" OR "ligne HT" OR MW)
site:edt.pf ("groupe électrogène" OR photovoltaïque OR solaire OR stockage OR batterie)
"Tahiti Nui Fortress" (énergie OR solaire OR "énergies vertes" OR MW)
"TDF" "Pic Rouge" (photovoltaïque OR "récupération de chaleur" OR "Tier III")
"Polynésie française" électricité (datacenter OR "centre de données" OR "grand consommateur")
```

---

## 5. 政府采购与招标（Procurement）

已验证入口：
- 当前官方采购门户说明页为 Service Public PF 的 **Te Ariari**：https://www.service-public.pf/marchespublics/
- 该页链接到市场室/平台 `ecole.teariari.gov.pf`。实测域名可访问但证书链可能导致命令行校验失败；浏览器可按实际证书状态复核。
- `www.marches-publics.pf` 实测不解析，不应作为主入口；保留为历史/错误变体搜索即可。
- 法国国家 PLACE：https://www.marches-publics.gouv.fr/ 可补充国家服务在 PF 的采购。

用法：
- 招标、采购人、地点、金额、中标公告为 **A**。
- 对政府/半官方托管、SIPF/DSI 外包、TDF/TNF 公共客户、海缆运维、发电/空调/消防升级，应优先查 Te Ariari、Service Public PF、Lexpol/JOPF、PLACE。

查询模板：
```text
site:service-public.pf/marchespublics (datacenter OR "centre de données" OR "salle serveurs" OR hébergement OR cloud)
site:ecole.teariari.gov.pf (datacenter OR "centre de données" OR "salle serveurs" OR hébergement OR cloud)
site:lexpol.cloud.pf ("appel d'offres" OR "marché public" OR "avis d'attribution") (datacenter OR "centre de données" OR "salle serveurs")
site:marches-publics.gouv.fr "Polynésie française" (datacenter OR "centre de données" OR "salle serveurs" OR hébergement)
"Service informatique de la Polynésie française" "appel d'offres" hébergement
"Direction du Système d'Information" "Polynésie française" "marchés publics"
```

---

## 6. 建筑许可 / 土地 / 环评（Building, Land, Environment）

重点：
- PF manifest 没有省/州级 division；建筑许可仍需按市镇与岛屿搜索：Papeete、Pirae、Faa'a、Punaauia、Arue、Mahina、Hitiaa O Te Ra/Papenoo、Moorea-Maiao、Uturoa、Bora-Bora、Rangiroa、Nuku Hiva、Tubuai。
- TNF 的官方法律声明给出 Papenoo PK 16.7 侧山；TDF 官方给出 Pic Rouge/Papeete。更精确边界需建筑许可、环评或业主资料。
- 环评、消防、城市规划、土地记录为 **A**；目录坐标为 **C**。

查询模板：
```text
"Papenoo" "PK16,7" ("Tahiti Nui Fortress" OR "Tahiti Nui Telecom" OR datacenter)
"Pic Rouge" Papeete TDF ("permis de construire" OR "travaux" OR datacenter)
"{commune}" "permis de construire" (datacenter OR "centre de données" OR "salle informatique")
site:lexpol.cloud.pf ("permis de construire" OR urbanisme OR "étude d'impact") (datacenter OR "centre de données")
"Polynésie française" "étude d'impact" (datacenter OR "centre de données" OR "salle serveurs")
```

---

## 7. 分区查询模板（Per-Division Query Templates）

Manifest 中 PF 仅 **1 个分区：French Polynesia**。分区级模板即全国级模板；岛屿组/市镇仅作地理细化层，不改变 manifest division。

### 7.1 Division 01 — French Polynesia

```text
"French Polynesia" ("data center" OR "data centre" OR datacenter OR colocation)
"Polynésie française" ("centre de données" OR datacenter OR "salle serveurs" OR hébergement)
"Tahiti" ("data center" OR "centre de données" OR colocation OR "salle informatique")
"Tahiti Nui Fortress" OR "tnfortress" OR "Tahiti Nui Telecom" datacenter
"TDF" "Papeete" "Pic Rouge" datacenter
site:{official-domain} ("centre de données" OR datacenter OR hébergement OR "salle serveurs")
site:{official-domain} ("câble sous-marin" OR "station d'atterrissement" OR Honotua OR NATITUA OR Manatua OR Honomoana OR Tabua)
site:{official-domain} ("appel d'offres" OR "marché public") (datacenter OR "centre de données" OR hébergement)
site:{official-domain} ("permis de construire" OR "étude d'impact") (datacenter OR "centre de données")
```

负面控制（cloud / hyperscaler）：
```text
"French Polynesia" "cloud region"
"Tahiti" ("cloud region" OR "availability zone")
site:docs.aws.amazon.com/global-infrastructure/latest/regions "French Polynesia"
site:azure.microsoft.com/en-us/explore/global-infrastructure "French Polynesia"
site:cloud.google.com/about/locations "French Polynesia"
site:oracle.com/cloud/public-cloud-regions "French Polynesia"
```

### 7.2 岛屿组 / 市镇分层（可选）

| 岛屿组（Îles） | 主要地点 | 预期 |
|---|---|---|
| Îles du Vent（Tahiti / Mo'orea） | Papeete、Pic Rouge、Papenoo、Pirae、Faa'a、Punaauia、Arue、Mahina、Moorea-Maiao | 唯一现实 DC 类线索区；TNF 与 TDF 均在 Tahiti |
| Îles Sous-le-Vent | Uturoa、Tahaa、Huahine、Bora-Bora | 海缆/电信节点；默认无 DC |
| Tuamotu-Gambier | Rangiroa、Manihi、Hao、Makemo、Mangareva | NATITUA/通信节点；默认无 DC |
| Marquises | Nuku Hiva、Hiva Oa | NATITUA/通信节点；默认无 DC |
| Australes | Tubuai、Rurutu | 通信/电力上下文；默认无 DC |

岛屿模板：
```text
"{île}" (datacenter OR "centre de données" OR "salle serveurs" OR hébergement)
"{commune}" (datacenter OR "centre de données") ("permis de construire" OR "marché public")
"{île}" ("câble sous-marin" OR atterrissement OR Honotua OR NATITUA OR Manatua)
```

---

## 8. 证据分级与状态语义

| 事实 | A 级证据 | B/C 降级条件 |
|---|---|---|
| 设施存在 | TNF/TDF 官方设施页、法律声明、采购/许可/环评 | 媒体为 B；目录站为 C |
| 地址/边界 | 官方 contact/legal page、许可、环评 | 目录坐标、社交媒体地址为 C |
| 容量 | 官方规格、合同、环评、采购文件 | 媒体引用为 B；Baxtel/DCM 数字为 C |
| 状态 | 官方 opening/RFS/operational 页面 | MoU/规划新闻为 C，媒体投运为 B |
| 认证/Tier | 证书或官方审计说明 | 营销性 “Tier3+” 只能记为 claimed |

状态语义：
- `announced` / MoU = 计划线索。
- `delivered` / `inaugurated` / `opened` = 可记 operational，但需注明来源日期。
- `extension planned` = 与现有运营容量分开记录。
- 海缆 RFS 与云区域无关；Google cable landing 不等于 Google Cloud region。

## 9. 快速 URL 索引（已复验口径）

- 政府：https://www.presidence.pf/ ；https://www.service-public.pf/
- 法律：https://lexpol.cloud.pf/ ；https://www.legifrance.gouv.fr/
- 采购：https://www.service-public.pf/marchespublics/ ；市场室链接 `ecole.teariari.gov.pf`
- 电信/监管上下文：https://www.anfr.fr/outre-mer/polynesie-francaise/reglementation ；https://autorite-concurrence.pf/
- 运营商/设施：https://www.tnfortress.pf/ ；https://www.tahitinuitelecom.pf/ ；https://groupe.opt.pf/ ；https://www.tdf.fr/
- 电力：https://www.edt.pf/
- 海缆：https://cloud.google.com/blog/products/infrastructure/honomoana-and-tabua-subsea-cables-connect-south-pacific

## 10. 常见陷阱

- **ARCEP PF 是假入口**：不要把 `www.arcep.pf` 或法国 ARCEP 当 PF 本地监管源；以 ANFR/PF 法律/政府/ARN/APC 为准。
- **NATITUA 不是 Tahiti-Hawaii**：Tahiti-Hawaii 是 Honotua 国际段；NATITUA 连接 Tuamotu/Marquesas 外岛。
- **登陆站 ≠ 数据中心**：Papenoo 同时有 TNF、海缆、卫星站；必须按资产类别拆分。
- **“Tier3+” 与 “Tier III level” 要分开**：官方营销声明、合规审计、正式认证不是同一事实。
- **目录站容量谨慎**：Baxtel/DataCenterMap 可用于发现 TNF/TDF，但容量/坐标须降级。
- **PF 只有一个 manifest division**：不要为群岛创建额外 manifest divisions。
