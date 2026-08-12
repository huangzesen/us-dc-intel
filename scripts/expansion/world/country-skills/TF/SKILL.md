---
name: tf-datacenter-methodology
location: scripts/expansion/world/country-skills/TF/SKILL.md
description: 法属南部领地数据中心查询方法论（French Southern Territories datacenter discovery & audit methodology）——双线来源（官方/监管/云管线 + 行业/厂商/媒体发现）与 single-division 模型下的 verified-negative 枚举协议。
---

# TF · 法属南部领地数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：枚举法属南部领地（French Southern Territories / Terres australes françaises, TF）的数据中心并核实行业现实。双线方法论：`explorer-official.md`（官方/监管/云管线）与 `explorer-industry.md`（行业/厂商/媒体发现），均为 codex 审核定稿。划分模型（per manifest）：**subnational_type: country**，单一 division **French Southern Territories**。本方法论不把 TAAF 的内部 district 当作 repo division；只把 **Crozet / Kerguelen / Saint-Paul et Amsterdam / Terre Adelie / Iles Eparses** 用作站内检索与误报排除清单。评审日期：2026-08-12。

## 入口

| 入口 | 管线 | 内容 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线 | 已验证基线（无商业数据中心市场、活动形态、通讯现实、行业阴性对照、枚举预期 verified-negative）、官方信息源（TAAF/IPEV/Legifrance/法国内阁/采购/云区域页）、官方查询模板（法语优先）、内部 district 清单、候选记录判定标准、误报过滤、复核节奏 |
| `explorer-industry.md` | 行业/厂商/媒体发现 | 行业现实、目录负向核验、官方/准官方基础设施线索（TAAF/IPEV/CNES/Meteo-France/CEA/采购）、云与运营商核验、候选升级门槛、已知误报清单、推荐检查顺序 |

## 核心结构事实

1. **行政区划模型**：single division **French Southern Territories**（manifest `subnational_type: country`）。所有候选记录的 division 写 French Southern Territories；Crozet/Kerguelen/Saint-Paul et Amsterdam/Terre Adelie/Iles Eparses 只用于定位来源与识别误报，不写入 repo division。
2. **注册库现状**：TF/TAAF **没有可枚举的商业数据中心市场**。官方 TAAF 页面说明该领地由五个 districts 组成，是**无常住人口、无民选机构**的特殊法国海外领地；TAAF 的主要职能是主权、科研支持、自然保护与物流。行业阴性对照：DataCenterMap 全球库列出有数据中心的 179 个国家/市场但没有 TF 条目；Cloudscene 的 France 市场页只列法国本土/常规城市市场（Paris、Marseille、Lyon 等），不构成 TF 设施证据。公开搜索 “French Southern Territories datacenter / Terres australes centre de données” 未发现可信运营设施。枚举预期：**verified-negative**。
3. **法律与监管**：TAAF 法律地位与法规经 Legifrance 核实；官方采购/公报（TAAF marches publics、BOAMP、PLACE）用于发现任何 ICT、机房、卫星通信、电力、建筑采购；法国政府/部委站点（Outre-mer、diplomatie、ecologie）提供海外领地背景、主权/环保/科研政策。
4. **互联与云**：IPEV 对站上实验室的描述出现近实时科学数据经 INTERMAGNET telecommunication satellites、Argos 等链路传输——这类科研/观测通信记为 `research-communications`，不是数据中心。官方云厂商区域页（AWS/Azure/GCP/OCI）均无 TF 区域；法国本土区域不等于 TF。卫星宽带、地球站或科学数据链路只说明连接方式；除非有外部客户托管服务和机房证据，否则不升级为数据中心。
5. **设施/项目种子**：当前无商业种子。真实基础设施形态是科研站 IT、观测设备、卫星/Argos 数据回传、气象与地球物理网络、燃油/微电力后勤——作为 `research-operations` 或 `communications` 记录，不进入数据中心资产表。采购线索（ICT、satellite、serveur、salle informatique、énergie 项目）可记录为政府/科研运营基础设施；只有明确「托管外部客户/商业机柜/云区域」才升级。
6. **语言与词汇**：法语优先；英语用于排除国际目录/SEO 噪声。关键法语词：centre de données、data center/datacenter、salle informatique、salle serveurs、serveur、hébergement、colocation、marché public、appel d'offres、consultation、télécommunications、satellite、énergie、groupe électrogène、liaison satellite。
7. **可靠性分级**：A=官方/一手来源（TAAF `taaf.fr`、IPEV `institut-polaire.fr`、Legifrance、法国国家部门、采购/公报、官方云区域页）；B=可信媒体/科研机构报道且有明确日期与主体（DCD、Data Center Knowledge、Reuters/AP、法国主流媒体）；C=数据中心目录、SEO 页面、供应商国家下拉菜单、博客/论坛、未核实市场报告（C 级只能作线索或阴性对照，不能确立设施）；U=无可复核来源。
8. **计数与去重规则**：候选记录最低正向证据——商业数据中心/托管设施必须有运营商官方页面、政府许可/采购、地址/坐标、服务形态（colo/rack/hosting/cloud）和至少一个独立 A/B 级佐证（当前预期为零）；科研站 IT/观测通信按 `research-station-it`、`observatory`、`communications`、`meteorological-station` 记录，不得计作商业数据中心；法国本土混淆（France/La Reunion/Paris/Marseille 数据中心、法国云区域、供应商 “France” 页面）均不属于 TF，除非页面明确列出 TF 境内物理设施。标准字段：country_code: TF；division: French Southern Territories；internal_location: Crozet | Kerguelen | Saint-Paul et Amsterdam | Terre Adelie | Iles Eparses | unknown；facility_type: commercial-colo | cloud-region | research-station-it | research-communications | observatory | telecom | power/logistics | false-positive；status: operational | planned | procurement | proposal-only | verified-negative | decommissioned；evidence_grade: A | B | C | U。

## 常用查询模板

```text
site:taaf.fr ("centre de données" OR "data center" OR datacenter OR "salle informatique" OR serveur OR hébergement OR colocation)
site:taaf.fr (Kerguelen OR Crozet OR Amsterdam OR "Saint-Paul" OR "Terre Adélie" OR "Iles Eparses") (informatique OR télécommunications OR satellite OR énergie OR "station")
site:taaf.fr ("marché public" OR "appel d'offres" OR consultation) (informatique OR télécommunications OR satellite OR énergie OR "salle serveurs")
site:institut-polaire.fr (Kerguelen OR Crozet OR Amsterdam OR "Dumont d'Urville") ("data center" OR "centre de données" OR informatique OR serveur OR satellite OR "Argos")
site:legifrance.gouv.fr ("Terres australes et antarctiques françaises" OR TAAF) (télécommunications OR informatique OR énergie OR "centre de données")
site:cnes.fr (Kerguelen OR "Terres australes" OR TAAF) (station OR satellite OR "data center" OR "centre de données")
site:meteofrance.com OR site:meteofrance.fr (Kerguelen OR Crozet OR Amsterdam OR "Terre Adélie") (station OR données OR serveur)
site:boamp.fr (TAAF OR "Terres australes") (informatique OR télécommunications OR satellite OR serveur OR énergie)
site:marches-publics.gouv.fr (TAAF OR "Terres australes") (informatique OR télécommunications OR satellite OR serveur OR énergie)
"French Southern Territories" ("data center" OR "data centre" OR datacenter OR colocation OR hosting)
"Terres australes" ("centre de données" OR datacenter OR "salle serveurs" OR hébergement)
TAAF (datacenter OR "centre de données" OR colocation OR hosting OR cloud OR edge)
(Kerguelen OR Crozet OR Amsterdam OR "Saint-Paul" OR "Terre Adélie") (datacenter OR "data center" OR "centre de données" OR colocation OR hosting OR cloud)
site:datacenterdynamics.com ("French Southern Territories" OR TAAF OR Kerguelen OR Crozet OR Amsterdam)
site:datacenterknowledge.com ("French Southern Territories" OR TAAF OR Kerguelen OR Crozet OR Amsterdam)
site:datacentermap.com ("French Southern Territories" OR TAAF OR Kerguelen)
site:cloudscene.com ("French Southern Territories" OR TAAF OR Kerguelen)
site:peeringdb.com ("French Southern Territories" OR TAAF OR Kerguelen OR Crozet)
"French Southern Territories" (AWS OR Azure OR "Google Cloud" OR Oracle OR OCI OR "cloud region" OR "edge location")
"Kerguelen" (Starlink OR Intelsat OR Viasat OR satellite OR "earth station" OR "ground station")
```

云区域负面核验：`"French Southern Territories" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region" OR "cloud region")`、`"Terres australes" ("région AWS" OR "région Azure" OR "Google Cloud" OR "Oracle Cloud")`。

## 官方/监管管线要点（详见 explorer-official.md）

- **核心官方源**：TAAF 行政站 `taaf.fr`（领地结构、行政职责、法规/公报、科研与后勤、补给、招聘、项目公告）、IPEV `institut-polaire.fr`（Crozet/Kerguelen/Amsterdam/Dumont d'Urville 科研站、实验室、通信与后勤）、Legifrance（TAAF 法律地位、法规、适用文本）、法国政府/部委站点（Outre-mer、diplomatie、ecologie 等）、官方采购/公报（TAAF marches publics、BOAMP、PLACE）、官方云厂商区域页。
- **内部 district 清单处理**：Archipel Crozet——科研站、气象/地球物理观测、卫星链路，默认非商业；Archipel Kerguelen / Port-aux-Français——最大后勤/科研基地，服务器、观测数据、CNES/Meteo-France/CEA 线索默认归 `research-operations` 或 `communications`；Iles Saint-Paul et Amsterdam / Martin-de-Vivies——科研站与观测网络，默认非商业；Terre Adelie / Dumont d'Urville——南极科研站，条约/科研语境，非 TF 商业 DC 市场；Iles Eparses——TAAF 管辖但与印度洋热带岛屿有关，军事/气象/科研通信不是数据中心。
- **复核节奏**：每次运行重跑 TAAF/IPEV 站内查询、英/法文 datacenter 查询、DataCenterMap/Cloudscene 阴性对照、官方云区域页；每季度检查 TAAF 公报/采购、BOAMP/PLACE、Legifrance 行政地位、电力/通信采购；事件驱动——若出现 “Kerguelen/Amsterdam/Crozet data center”、”AI/GPU/edge in TAAF”、”satellite broadband expansion” 等报道，先按科研通信或法国本土误报处理，只有 A 级建设/许可/运营证据齐备才建档。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **行业现实**：未发现 TF 境内商业托管、批发、hyperscale、edge cloud、IXP 或云区域市场。TAAF 官方说明其无常住人口且以主权、科研、自然保护和后勤为核心职能——与商业 DC 所需的客户、电网、光纤、施工/运维市场不匹配。
- **目录负向核验**：DataCenterMap（无 TF 市场，C 级阴性对照）、Cloudscene（France 本土市场存在，TF 无独立设施）、Baxtel（预期无设施，若有条目需 A/B 级佐证）、PeeringDB（预期无 IXP/colo 设施）、Submarine Cable Map/TeleGeography（预期无 TF 商业海缆登陆市场）、Uptime Institute/vendor pages（国家下拉菜单不是设施证据）。
- **官方/准官方基础设施线索**：TAAF/logistics（bases、ravitaillement、carburant、énergie、ateliers、telecommunications——判断是否有异常建筑/能源项目）、IPEV/polar operations（station labs、observatories、scientific IT、satellite telemetry——可证明科研基础设施，不证明商业服务）、CNES/Meteo-France/CEA/IPGP/GEOSCOPE/INTERMAGNET/Argos（观测站、数据回传、卫星跟踪、地球物理网络——记录为 `observatory` 或 `research-communications`）、采购与合同（TAAF procurement、BOAMP、PLACE——出现 `serveurs`、`salle informatique`、`liaison satellite`、`groupe électrogène`、`énergie` 先按政府/科研运营项目处理）。
- **候选升级门槛**（升为商业数据中心候选前必须同时满足）：1) 运营主体明确，不是政府科研/气象/军事/保护区运营部门；2) 明确提供 colocation、rack、hosting、cloud region、GPU/compute rental 或 carrier-neutral interconnection；3) 物理位置明确在 TF/TAAF 境内，而非 France mainland、La Reunion、French Polynesia 或处理 TAAF 数据的法国本土中心；4) 有 A 级许可/采购/官方运营页，或运营方官方页 + 独立 A/B 级佐证；5) 电力、连接、物流规模与声称用途一致。未满足时记录为 false-positive | research-station-it | research-communications | observatory | telecom | power-logistics | proposal-only。
- **已知误报**：France market pages（Cloudscene/DataCenterMap/DCD 或运营商页面中的 France/Paris/Marseille/Lyon 数据中心不是 TF）；国家选择器（供应商联系表列出 “French Southern Territories” 是国家码覆盖，不是部署地）；IP/GeoIP 页面（IP2Location 等出现 TF 的 IP 分类或 “data centers” 标签不代表本地设施）；科研数据中心在法国本土（法国海洋、极地、气象或科研数据平台可处理 TAAF 数据，但物理位置通常在法国本土，不得归入 TF）；站内服务器/观测站（Kerguelen、Crozet、Amsterdam、Dumont d'Urville 的观测服务器、卫星终端、气象站和实验室网络都是科研运营基础设施）；旅游/地图/百科页面（“base”、“station”、“infrastructure” 需逐项解释，没有托管服务即非 DC）。

## 维护注意（更新纪律）

- 不删除/移动任何既有文件；双 explorer 文件是 codex 审核定稿，SKILL.md 忠实提炼其内容，细则差异以 explorer 原文件为准。
- 每次运行的默认结论应为：**TF = verified-negative for commercial datacenter market**；只有出现官方建设/许可/运营证据时才改变该结论。
- 对 France mainland、La Reunion、French Polynesia、国家选择器、IP 地理噪声做 `false-positive` 注记，避免未来重复调查。
- 按推荐检查顺序执行：官方基线 → 目录阴性 → 云阴性 → 内部地名扫描 → 采购监测 → 误报归档。
