# TF 官方渠道探索方法论 — 法属南部领地 (French Southern Territories) 数据中心枚举
# TF Explorer Official — Datacenter Enumeration via Official / Regulatory Sources

Date: 2026-08-12. Scope: **TF / 法属南部领地 French Southern Territories**. Manifest baseline (`world-manifest.jsonl`): `subnational_type: country`, single division **French Southern Territories**. 本方法论不把 TAAF 的内部 district 当作 repo division；只把 **Crozet / Kerguelen / Saint-Paul et Amsterdam / Terre Adelie / Iles Eparses** 用作站内检索与误报排除清单。

可靠性分级 Reliability grades: **A** = 官方/一手来源（TAAF `taaf.fr`, IPEV `institut-polaire.fr`, Legifrance, 法国国家部门、采购/公报、官方云区域页）；**B** = 可信媒体/科研机构报道且有明确日期与主体；**C** = 数据中心目录、SEO 页面、供应商国家下拉菜单、博客/论坛、未核实市场报告。C 级只能作线索或阴性对照，不能确立设施。

## 0. 已验证基线 (Verified Baseline)

- **结构性结论**: TF/TAAF 没有可枚举的商业数据中心市场。官方 TAAF 页面说明该领地由五个 districts 组成，并且是**无常住人口、无民选机构**的特殊法国海外领地；TAAF 的主要职能是主权、科研支持、自然保护与物流。
- **活动形态**: TAAF/IPEV 官方资料显示，Crozet、Kerguelen、Saint-Paul et Amsterdam 主要承载轮换科研、环境监测、气象、地球物理与后勤活动；TAAF 资料还说明法属南方群岛没有港口，补给依赖从 La Reunion 出发的 Marion Dufresne 船期与基地燃油补给。该条件不支持商业托管、云区或多兆瓦数据中心。
- **通信现实**: IPEV 对站上实验室的描述出现近实时科学数据经 INTERMAGNET telecommunication satellites、Argos 等链路传输。这类科研/观测通信记为 `research-communications`，不是数据中心。
- **行业阴性对照**: DataCenterMap 的全球国家列表列出 179 个有数据中心的国家/市场，但没有 TF 条目；Cloudscene 的 France 市场页只列法国本土/常规城市市场（Paris, Marseille, Lyon 等），不构成 TF 设施证据。公开搜索 “French Southern Territories datacenter / Terres australes centre de donnees” 未发现可信运营设施。
- **枚举预期**: `verified-negative`。任何命中必须先按 “科研站 IT / 卫星通信 / 气象或地球物理观测 / 法国本土设施 / 供应商国家选择器噪声” 排除。

## 1. 官方信息源 (Official Source Surfaces)

| 来源 Source | 用途 Use | 等级 |
|---|---|---:|
| TAAF 行政站 `https://taaf.fr/` | 领地结构、行政职责、法规/公报、科研与后勤、补给、招聘、项目公告 | A |
| IPEV `https://institut-polaire.fr/` | Crozet/Kerguelen/Amsterdam/Dumont d'Urville 科研站、实验室、通信与后勤 | A |
| Legifrance `https://www.legifrance.gouv.fr/` | TAAF 法律地位、法规、适用文本 | A |
| 法国政府/部委站点（Outre-mer, diplomatie, ecologie 等） | 法国海外领地背景、主权/环保/科研政策 | A/B |
| 官方采购/公报（TAAF marches publics, BOAMP, PLACE） | 任何 ICT、机房、卫星通信、电力、建筑采购 | A |
| 官方云厂商区域页（AWS/Azure/GCP/OCI） | 云区域缺席核验；法国本土区域不等于 TF | A |

## 2. 官方查询模板 (Official Query Templates)

优先使用法语；英语用于排除国际目录/SEO 噪声。

```text
site:taaf.fr ("centre de données" OR "data center" OR datacenter OR "salle informatique" OR serveur OR hébergement OR colocation)
site:taaf.fr (Kerguelen OR Crozet OR Amsterdam OR "Saint-Paul" OR "Terre Adélie" OR "Iles Eparses") (informatique OR télécommunications OR satellite OR énergie OR "station")
site:taaf.fr ("marché public" OR "appel d'offres" OR consultation) (informatique OR télécommunications OR satellite OR énergie OR "salle serveurs")
site:institut-polaire.fr (Kerguelen OR Crozet OR Amsterdam OR "Dumont d'Urville") ("data center" OR "centre de données" OR informatique OR serveur OR satellite OR "Argos")
site:legifrance.gouv.fr ("Terres australes et antarctiques françaises" OR TAAF) (télécommunications OR informatique OR énergie OR "centre de données")
"French Southern Territories" ("data center" OR "data centre" OR datacenter OR colocation OR hosting)
"Terres australes" ("centre de données" OR datacenter OR "salle serveurs" OR hébergement)
```

云区域负面核验：

```text
"French Southern Territories" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR "cloud region")
"Terres australes" ("région AWS" OR "région Azure" OR "Google Cloud" OR "Oracle Cloud")
```

## 3. 内部 District 清单 (Internal District Checklist)

Manifest 只有一个 division，因此所有候选记录的 division 应写 **French Southern Territories**。下列名称只用于定位来源与识别误报：

| 内部地名 Internal name | 官方处理方式 How to treat hits |
|---|---|
| Archipel Crozet | 科研站、气象/地球物理观测、卫星链路；默认非商业 |
| Archipel Kerguelen / Port-aux-Français | 最大后勤/科研基地；服务器、观测数据、CNES/Meteo-France/CEA 线索默认归 `research-operations` 或 `communications` |
| Iles Saint-Paul et Amsterdam / Martin-de-Vivies | 科研站与观测网络；默认非商业 |
| Terre Adelie / Dumont d'Urville | 南极科研站；条约/科研语境，非 TF 商业 DC 市场 |
| Iles Eparses | TAAF 管辖但与印度洋热带岛屿有关；军事/气象/科研通信不是数据中心 |

## 4. 候选记录判定标准 (Candidate Rules)

最低正向证据：

1. **商业数据中心 / 托管设施**: 必须有运营商官方页面、政府许可/采购、地址/坐标、服务形态（colo/rack/hosting/cloud）和至少一个独立 A/B 级佐证。当前预期为零。
2. **科研站 IT / 观测通信**: TAAF/IPEV/CNES/Meteo-France/CEA 等来源可证明站点或仪器存在，但记录类型应为 `research-station-it`, `observatory`, `communications`, `meteorological-station`，不得计作商业数据中心。
3. **采购线索**: ICT、satellite、serveur、salle informatique、energie 项目可记录为政府/科研运营基础设施；只有明确“托管外部客户/商业机柜/云区域”才升级。
4. **法国本土混淆**: France/La Reunion/Paris/Marseille 数据中心、法国云区域、供应商 “France” 页面均不属于 TF，除非页面明确列出 TF 境内物理设施。

标准字段：

```text
country_code: TF
division: French Southern Territories
internal_location: Crozet | Kerguelen | Saint-Paul et Amsterdam | Terre Adelie | Iles Eparses | unknown
facility_or_project_name:
operator:
facility_type: commercial-colo | cloud-region | research-station-it | research-communications | observatory | telecom | power/logistics | false-positive
status: operational | planned | procurement | proposal-only | verified-negative | decommissioned
evidence_grade: A | B | C | U
primary_urls:
notes:
last_checked:
```

## 5. 误报过滤 (False-Positive Filters)

- **供应商国家选择器**: OVHcloud、Iron Mountain、Uptime、工程公司或 SaaS 页面在国家下拉菜单中列出 “Terres australes françaises / French Southern Territories” 不是设施证据。
- **IP 地理定位**: IP2Location、GeoIP、广告分类中出现 TF 或 “data centers” 分类通常是 IP/国家码噪声，不代表本地机房。
- **法国本土设施**: Paris、Marseille、Lyon、Nantes、La Reunion 等法国或海外省设施不得归入 TF。
- **科研数据平台**: 海洋/极地数据门户、Datarmor 等法国本土计算平台可能处理 TAAF 科学数据，但物理设施不在 TF。
- **通信设施**: 卫星终端、Argos/INTERMAGNET 数据回传、气象站、无线电台、科研服务器间均不是商业 DC。

## 6. 复核节奏 (Recheck Cadence)

- **每次运行**: 重跑 TAAF/IPEV 站内查询、英文/法文 datacenter 查询、DataCenterMap/Cloudscene 阴性对照、官方云区域页。
- **每季度**: 检查 TAAF 公报/采购、BOAMP/PLACE、Legifrance 行政地位、电力/通信采购。
- **事件驱动**: 若出现 “Kerguelen/Amsterdam/Crozet data center”, “AI/GPU/edge in TAAF”, “satellite broadband expansion” 等报道，先按科研通信或法国本土误报处理，只有 A 级建设/许可/运营证据齐备才建档。
