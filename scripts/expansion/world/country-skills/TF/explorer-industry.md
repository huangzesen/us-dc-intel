# TF 行业渠道探索方法论 — 法属南部领地 (French Southern Territories) 数据中心枚举
# TF Explorer Industry — Operator / Market / Infrastructure Discovery

Date: 2026-08-12. Scope: **TF / French Southern Territories**. Manifest baseline: single division **French Southern Territories** (`subnational_type: country`). 行业侧目标不是发现常规 colo 市场，而是持续确认 `verified-negative`、监测科研/通信/物流基础设施，并排除 SEO 与法国本土误报。

行业可靠性分级 Industry reliability: **A** = 运营商/政府/科研机构一手来源（TAAF, IPEV, CNES, Meteo-France, CEA, Legifrance, 官方采购、云厂商官方区域页）；**B** = DCD/Data Center Knowledge/Reuters/AP/法国主流媒体等具名报道；**C** = DataCenterMap/Cloudscene/Baxtel/PeeringDB 等目录、市场报告、供应商落地页、IP 地理库、社交媒体；**U** = 无可复核来源。

## 0. 行业现实 (Market Reality)

- **商业市场结论**: 未发现 TF 境内商业托管、批发、hyperscale、edge cloud、IXP 或云区域市场。TAAF 官方说明其无常住人口且以主权、科研、自然保护和后勤为核心职能；这与商业 DC 所需的客户、电网、光纤、施工/运维市场不匹配。
- **真实基础设施形态**: 行业相关信号主要是科研站 IT、观测设备、卫星/Argos 数据回传、气象与地球物理网络、燃油/微电力后勤。它们可作为 `research-operations` 或 `communications` 记录，不进入数据中心资产表。
- **目录阴性对照**: DataCenterMap 全球库列出有数据中心的国家/市场但无 TF；Cloudscene 的 France 数据中心市场集中在法国本土城市（Paris, Marseille, Lyon, Lille 等），不是 TF。目录中若出现 TF，多数是国家选择器、销售覆盖或 IP 地理噪声。
- **分区处理**: repo division 固定为 **French Southern Territories**。行业搜索可按 Kerguelen、Crozet、Saint-Paul et Amsterdam、Terre Adelie、Iles Eparses 扫描，但不要把这些内部地名写成 repo division。

## 1. 行业/目录负面核验 (Industry Negative Checks)

| 表面 Surface | 处理方式 How to use | 预期 |
|---|---|---|
| DataCenterMap | 国家列表与站内搜索 TF/French Southern/TAAF/Kerguelen | 无 TF 市场；C 级阴性对照 |
| Cloudscene | France market + country/metro 搜索 | France 本土市场存在，TF 无独立设施 |
| Baxtel | 国家/岛屿名搜索 | 预期无设施；若有条目需 A/B 级佐证 |
| PeeringDB | facility/IX/net 搜索 TF、TAAF、Kerguelen、Crozet、Amsterdam | 预期无 IXP/colo 设施 |
| Submarine Cable Map / TeleGeography | 现行商业电缆与登陆站搜索 | 预期无 TF 商业海缆登陆市场 |
| Uptime Institute / vendor pages | 认证/客户/国家选择器搜索 | 国家下拉菜单不是设施证据 |

通用查询：

```text
"French Southern Territories" (datacenter OR "data center" OR "data centre" OR colocation OR colo OR hosting OR "carrier hotel" OR IXP)
"Terres australes" (datacenter OR "centre de données" OR colocation OR hébergement OR "salle serveurs")
TAAF (datacenter OR "centre de données" OR colocation OR hosting OR cloud OR edge)
(Kerguelen OR Crozet OR Amsterdam OR "Saint-Paul" OR "Terre Adélie") (datacenter OR "data center" OR "centre de données" OR colocation OR hosting OR cloud)
site:datacenterdynamics.com ("French Southern Territories" OR TAAF OR Kerguelen OR Crozet OR Amsterdam)
site:datacenterknowledge.com ("French Southern Territories" OR TAAF OR Kerguelen OR Crozet OR Amsterdam)
site:datacentermap.com ("French Southern Territories" OR TAAF OR Kerguelen)
site:cloudscene.com ("French Southern Territories" OR TAAF OR Kerguelen)
site:peeringdb.com ("French Southern Territories" OR TAAF OR Kerguelen OR Crozet)
```

## 2. 官方/准官方行业线索 (Operator-Like Infrastructure)

这些来源可能出现“设施”字样，但默认不是数据中心：

- **TAAF / logistics**: bases, ravitaillement, carburant, énergie, ateliers, telecommunications。用途是判断是否有异常建筑/能源项目。
- **IPEV / polar operations**: station labs, observatories, scientific IT, satellite telemetry。可证明科研基础设施，不证明商业服务。
- **CNES / Meteo-France / CEA / IPGP / GEOSCOPE / INTERMAGNET / Argos**: 观测站、数据回传、卫星跟踪、地球物理网络。记录为 `observatory` 或 `research-communications`。
- **采购与合同**: TAAF procurement、BOAMP、PLACE。若出现 `serveurs`, `salle informatique`, `liaison satellite`, `groupe électrogène`, `énergie`，先按政府/科研运营项目处理。

查询模板：

```text
site:taaf.fr (informatique OR serveur OR "salle informatique" OR télécommunications OR satellite OR énergie OR carburant) (Kerguelen OR Crozet OR Amsterdam OR "Terre Adélie" OR "Iles Eparses")
site:institut-polaire.fr (informatique OR server OR serveur OR satellite OR telemetry OR "near-real time" OR Argos) (Kerguelen OR Crozet OR Amsterdam)
site:cnes.fr (Kerguelen OR "Terres australes" OR TAAF) (station OR satellite OR "data center" OR "centre de données")
site:meteofrance.com OR site:meteofrance.fr (Kerguelen OR Crozet OR Amsterdam OR "Terre Adélie") (station OR données OR serveur)
site:boamp.fr (TAAF OR "Terres australes") (informatique OR télécommunications OR satellite OR serveur OR énergie)
site:marches-publics.gouv.fr (TAAF OR "Terres australes") (informatique OR télécommunications OR satellite OR serveur OR énergie)
```

## 3. 云与运营商核验 (Cloud / Operator Checks)

官方云区域页才可作为云设施证据；当前预期全部为无：

| Provider | 官方页 | TF 处理 |
|---|---|---|
| AWS | `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/` | 无 TF 区域/Local Zone/Wavelength Zone |
| Microsoft Azure | `https://learn.microsoft.com/en-us/azure/reliability/regions-list` | 无 TF 公共区域 |
| Google Cloud | `https://cloud.google.com/about/locations` 和 `https://datacenters.google/locations/` | 无 TF 区域/自有 DC |
| Oracle OCI | `https://www.oracle.com/cloud/public-cloud-regions/` | 无 TF 公共区域 |

运营商/互连检索：

```text
"French Southern Territories" (AWS OR Azure OR "Google Cloud" OR Oracle OR OCI OR "cloud region" OR "edge location")
"Terres australes françaises" (AWS OR Azure OR "Google Cloud" OR Oracle OR "région cloud")
"Kerguelen" (Starlink OR Intelsat OR Viasat OR satellite OR "earth station" OR "ground station")
"Crozet" (Starlink OR Intelsat OR Viasat OR satellite OR "earth station")
"Amsterdam Island" (Starlink OR Intelsat OR Viasat OR satellite OR "earth station")
```

卫星宽带、地球站或科学数据链路只说明连接方式；除非有外部客户托管服务和机房证据，否则不升级为数据中心。

## 4. 候选升级门槛 (Escalation Rules)

把一个 TF 线索升级为商业数据中心候选前，必须同时满足：

1. 运营主体明确，不是政府科研/气象/军事/保护区运营部门；
2. 明确提供 colocation、rack、hosting、cloud region、GPU/compute rental 或 carrier-neutral interconnection；
3. 物理位置明确在 TF/TAAF 境内，而非 France mainland、La Reunion、French Polynesia 或处理 TAAF 数据的法国本土中心；
4. 有 A 级许可/采购/官方运营页，或运营方官方页 + 独立 A/B 级佐证；
5. 电力、连接、物流规模与声称用途一致。

未满足时记录为：

```text
facility_type: false-positive | research-station-it | research-communications | observatory | telecom | power-logistics | proposal-only
status: verified-negative | operational | procurement | proposal-only
evidence_grade: A | B | C | U
```

## 5. 误报清单 (Known False Positives)

- **France market pages**: Cloudscene、DataCenterMap、DCD 或运营商页面中的 France/Paris/Marseille/Lyon 数据中心不是 TF。
- **国家选择器**: 供应商联系表列出 “French Southern Territories / Terres australes françaises” 是国家码覆盖，不是部署地。
- **IP/GeoIP 页面**: IP2Location 等出现 TF 的 IP 分类或 “data centers” 标签，不代表本地设施。
- **科研数据中心在法国本土**: 法国海洋、极地、气象或科研数据平台可处理 TAAF 数据，但物理位置通常在法国本土；不得归入 TF。
- **站内服务器/观测站**: Kerguelen、Crozet、Amsterdam、Dumont d'Urville 的观测服务器、卫星终端、气象站和实验室网络都是科研运营基础设施。
- **旅游/地图/百科页面**: “base”, “station”, “infrastructure” 需逐项解释；没有托管服务即非 DC。

## 6. 推荐检查顺序 (Recommended Sweep Order)

1. **官方基线**: TAAF presentation/research/logistics 页面与 IPEV station/logistics 页面，确认无常住人口、科研/后勤属性、通信形态。
2. **目录阴性**: DataCenterMap、Cloudscene、Baxtel、PeeringDB、Submarine Cable Map，记录 TF 无独立设施或 IXP。
3. **云阴性**: AWS/Azure/GCP/OCI 官方区域页，确认无 TF 区域。
4. **内部地名扫面**: Kerguelen、Crozet、Saint-Paul et Amsterdam、Terre Adelie、Iles Eparses 分别跑 data center / centre de donnees / server / satellite / energy 模板。
5. **采购监测**: TAAF、BOAMP、PLACE 中 ICT/telecom/energy 项目；把科研/后勤基础设施与商业 DC 明确分开。
6. **误报归档**: 对 France mainland、La Reunion、French Polynesia、国家选择器、IP 地理噪声做 `false-positive` 注记，避免未来重复调查。

每次运行的默认结论应为：**TF = verified-negative for commercial datacenter market**。只有出现官方建设/许可/运营证据时才改变该结论。
