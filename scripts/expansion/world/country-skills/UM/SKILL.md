---
name: um-datacenter-methodology
location: scripts/expansion/world/country-skills/UM/SKILL.md
description: 美国本土外小岛屿数据中心查询方法论：verified-negative 商业市场，双线执行负面扫描并监控联邦军事/保护区/科研设施以排除误报。United States Minor Outlying Islands datacenter methodology: verified-negative commercial market, disciplined negative sweep plus federal military/refuge/research infrastructure monitoring.
---

# UM · 美国本土外小岛屿数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：合并 explorer-official.md 与 explorer-industry.md 双线方法论，指导对 UM（United States Minor Outlying Islands）的 disciplined negative sweep 与联邦军事/保护区/科研/通信基础设施误报排除。官方线覆盖 USFWS/DOI、DoD/空军、联邦数据库、云区域页；行业线覆盖目录、互联数据、媒体/提案过滤。基线结论：UM 是 verified-negative 商业数据中心市场。

## 入口

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | DOI/USFWS 保护区页、Air Force/PACAF/AFCEC、Federal Register/eCFR/US Code、EPA NEPAccess、USASpending、SAM.gov、FCC ULS/IBFS、NOAA/USCG、IANA、官方云区域页 |
| explorer-industry.md | 行业/厂商/媒体发现 | PeeringDB/DataCenterMap/Cloudscene/Baxtel/Submarine Cable Map、云区域官方页负向、行业媒体、Palmyra OTEC 提案过滤、中文噪声扫描 |

## 核心结构事实

1. **行政区划模型**：manifest division model 为 **geographical unit**，repo divisions 共九个：**Johnston Atoll（约翰斯顿环礁）**、**Midway Islands（中途岛）**、**Navassa Island（纳瓦萨岛）**、**Wake Island（威克岛）**、**Baker Island（贝克岛）**、**Howland Island（豪兰岛）**、**Jarvis Island（贾维斯岛）**、**Kingman Reef（金曼礁）**、**Palmyra Atoll（巴尔米拉环礁）**。
2. **注册库现状**：UM 是一组偏远美国属地，无常住商业市场、无本地电信监管机构、无商业土地市场、无岛级数据中心许可/激励制度；Census Island Areas 不覆盖 UM 商业人口数据集，用官方 refuge/DoD 页面加岛级人员证据而非外推需求。
3. **法律与监管**：DOI/USFWS 管理野生动物保护区与纪念地，DOI OIA 是核心 insular-area 表面；Wake 为特例（民政权经由联邦当局与 Air Force/PACAF 运行）；Midway 已从 Navy 管辖转为 USFWS refuge 管理；Navassa 被 FWS 描述为无人岛。
4. **互联与云**：官方云区域列表（AWS/Azure/Google Cloud/Oracle）无 UM region（A 级负向）；IANA 显示 `.um` 未分配且不在根区，TLD 不能作为 UM 活跃设施证据；当前互联预期为卫星或联邦任务通信，Midway/Wake 历史海缆资产不等于当前 landing/DC 服务。
5. **设施/项目种子**：Wake airfield（AFCEC 8700 万美元现代化、FY2027 PDI fueling/apron）、Johnston runway/logistics、USFWS field camps、NOAA/USCG aids、卫星终端均分类为 `military-infrastructure`/`refuge-operations`/`research-station-it`/`communications`，不是 colocation；Palmyra OTEC/绿色数据中心提案（约 2010-2011）为 `proposal-only`。
6. **语言与词汇**：英文官方材料为主，另有中文噪声扫描查询包；状态词（required status verbs）：`operational`、`under construction`、`planned`、`procurement`、`proposal-only`、`verified-negative`、`decommissioned`。
7. **可靠性分级**：A=一手/官方（USFWS/DOI、Air Force/PACAF/AFCEC、Federal Register、eCFR/US Code/EO、EPA NEPAccess、USASpending、SAM.gov、FCC ULS/IBFS、NOAA/NWS、USCG NavCen、Census、IANA、官方云区域页）；B=强二手（GAO、国会预算材料、Civil Beat、Stars and Stripes、AP/Reuters、DCD、Data Center Knowledge、TeleGeography）；C=仅线索（目录、SEO 落地页、招聘板、厂商联系表单、市场报告、社交帖、未建提案）；U=不可复核传闻。
8. **计数与去重规则**：商业 DC 阳性证据须同时具备 命名运营商 + 命名 UM division 与物理场地 + 服务（colo/racks/hosting/云区域/edge compute/managed DC）+ A 级或运营商一手来源证明运行/建设/许可/合同；跑道/燃料/太阳能/后勤项目、refuge 办公室与野外营地、科研站 IT、气象站、导航助航、历史海缆建筑、`.um` 状态、远程职位招聘、厂商国家下拉菜单一律不算 DC；Palmyra OTEC 保持 proposal-only。

## 常用查询模板

```text
site:fws.gov/refuge "{division}" ("data center" OR "data centre" OR datacenter OR server OR cloud OR "special use permit" OR construction)
site:fws.gov/refuge "{division}" ("not accessible" OR permit OR "closed to public visitation")
site:doi.gov/oia ("United States Minor Outlying Islands" OR "Palmyra Atoll" OR "Wake Island")
site:papahanaumokuakea.gov Midway permit OR "Midway Atoll"
site:af.mil "Wake Island" ("airfield" OR "modernization" OR "data center" OR server)
site:pacaf.af.mil "Wake Island" ("airfield" OR "mission" OR "contractor" OR "data center")
site:afcec.af.mil "Wake Island" ("construction" OR "modernization" OR "environmental")
site:comptroller.war.gov "Wake Island" ("PDI" OR "fueling" OR "aircraft parking" OR "data center")
site:war.gov "Wake Island" ("contract" OR "airfield" OR "data center")
site:federalregister.gov "Wake Island"
site:federalregister.gov ("Wake Island" OR "Midway Atoll" OR "Johnston Atoll" OR "Palmyra Atoll" OR "Navassa Island")
site:nepaccess.epa.gov ("Wake Island" OR "Johnston Atoll" OR "Midway Atoll" OR "Palmyra Atoll") ("data center" OR server OR compute)
site:usaspending.gov ("Wake Island" OR "Johnston Atoll" OR "Midway Atoll" OR "Palmyra Atoll") ("data center" OR "IT" OR satellite OR construction)
site:sam.gov ("Wake Island" OR "Johnston Atoll" OR "Midway Atoll" OR "Palmyra Atoll") ("data center" OR server OR construction)
site:fcc.gov ("Wake Island" OR "Midway" OR "Johnston" OR "Palmyra") ("earth station" OR IBFS OR cable)
"United States Minor Outlying Islands" (colocation OR colo OR "rack space" OR "carrier hotel" OR "internet exchange")
"Wake Island" ("data center" OR datacenter OR colocation OR hosting OR "internet exchange")
"Midway Atoll" ("data center" OR datacenter OR colocation OR hosting OR cable)
"Johnston Atoll" ("data center" OR datacenter OR colocation OR hosting)
"Palmyra Atoll" ("data center" OR datacenter OR colocation OR hosting OR OTEC)
site:peeringdb.com ("United States Minor Outlying" OR "Wake Island" OR Palmyra OR Midway)
site:datacentermap.com ("United States Minor Outlying" OR "Wake Island" OR Palmyra OR Midway)
site:cloudscene.com ("United States Minor Outlying" OR "Wake Island" OR Palmyra OR Midway)
site:baxtel.com ("United States Minor Outlying" OR "Wake Island" OR Palmyra OR Midway)
site:comptroller.war.gov ("Wake Island" OR "Johnston Atoll") ("PDI" OR "MILCON" OR "data center")
site:sam.gov ("Wake Island" OR "Johnston Atoll") ("data center" OR "information technology" OR satellite OR generator OR construction)
site:usaspending.gov ("Wake Island" OR "Johnston Atoll") ("data center" OR IT OR satellite OR construction)
"Palmyra Atoll Research Station" (server OR satellite OR "data center" OR communications)
"Midway Atoll" ("server" OR "communications" OR satellite OR "data center")
site:datacenterdynamics.com (Wake OR Midway OR Johnston OR Palmyra OR "Minor Outlying")
site:datacenterknowledge.com (Wake OR Midway OR Johnston OR Palmyra OR "Minor Outlying")
site:civilbeat.org ("Wake Island" OR "Johnston Atoll") ("runway" OR "military" OR "data center")
site:stripes.com ("Wake Island" OR "Johnston Atoll") ("runway" OR "military" OR "data center")
"Palmyra" (OTEC OR "ocean thermal" OR "green data center" OR datacenter)
"美国本土外小岛屿" ("数据中心" OR "算力" OR "云" OR "托管" OR "机房")
"威克岛" ("数据中心" OR "算力" OR "美军" OR "机场" OR "能源")
"中途岛" ("数据中心" OR "海底电缆" OR "机房" OR "保护区")
"约翰斯顿环礁" ("数据中心" OR "跑道" OR "太平洋威慑")
"巴尔米拉环礁" ("数据中心" OR "绿色" OR "海洋温差" OR OTEC)
```

## 官方/监管管线要点（详见 explorer-official.md）

- 官方来源表面：DOI OIA islands portal + Palmyra 页、Pacific Islands Refuges and Monuments Office、Pacific Remote Islands Marine National Monument / Papahanaumokuakea、9 个 FWS refuge 页；Air Force/PACAF/AFCEC 新闻与采购；Federal Register Wake Island Code、National Archives EO 11048；Federal Register/eCFR/EPA NEPAccess/FCC ULS+IBFS/USASpending/SAM.gov/NOAA/NWS/USCG NavCen/Census Island Areas/IANA `.um`；官方云区域页（AWS/Azure/GCP/OCI）。
- 已验证官方事实：Wake airfield 为军事加油/训练/导弹测试/备降/后勤机场；AFCEC 报告 8700 万美元 Wake airfield 现代化（灯光/接地/道面标识/C-17 任务支持）；FY2027 DoD 预算含 Wake PDI fueling/停机坪基础设施——都是 `military-infrastructure`。
- 提取规则：页面描述准入/保护/科研/人员/refuge 设施只记官方背景；除非来源点名计算/托管设施及其运营商，否则不建 DC 记录。
- 每轮运行清单：核对 9 个 manifest division → 逐 division 扫 FWS → Wake/Johnston 扫空军/DoD 预算 → 扫联邦数据库 → 云区域负向 → IANA `.um` → 开放网络扫 UM/division + DC 词 → 任何阳性须 A 级土地/许可/合同或运营商证据才能离开 `verified-negative`。
- 每月：FWS refuge 页/新闻、Federal Register、DoD/PACAF/AFCEC Wake 与 Johnston 更新、SAM.gov、USASpending；每季：云区域页、IANA `.um`、FCC ULS/IBFS、PeeringDB/目录；事件驱动：任何 UM 算力/AI/云/跑道/能源/电缆头条或公告/立法/保护区边界变更。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场现实五重过滤：需求过滤（无城市/企业市场）、电力过滤（岛电为任务级微网/发电机/太阳能，非商用多 MW 电网服务）、互联过滤（卫星或联邦任务通信为主）、土地用途过滤（多为受限 refuge/纪念地）、云过滤（官方区域页无 UM region，不因美国区可用性推断 edge/云存在）。
- 目录与互联数据库仅作误报检测与负向确认，不能单独证明设施：PeeringDB、DataCenterMap、Cloudscene、Baxtel、Submarine Cable Map、TeleGeography、IANA `.um`；目录返回泛化国家页或远程职位标记为 `C false-positive`。
- 行业媒体/提案监控：DCD、Data Center Knowledge、Civil Beat、Stars and Stripes、AP/Reuters；Palmyra OTEC/green DC 报道（约 2010-2011）为已知 `proposal-only` 误报家族，除非当前 NEPA/许可/建设/运营商证据支持。
- 候选记录字段：`country_code`、`division`（九选一或 Unknown UM）、`facility_or_project_name`、`operator`、`facility_type`（military-infrastructure/refuge-operations/research-station-it/communications-earth-station/historical-cable-station/commercial-colo/cloud-region/proposal-only/verified-negative）、`status`、`capacity_or_scale`、`power`、`connectivity`、`evidence_grade`、`primary_urls`、`secondary_urls`、`site_address`、`coordinates`、`notes`、`last_checked`。
- 已验证负面清单：商业 colo/hosting 无验证提供商；云区域无 UM region；`.um` 未分配且不在根区；招聘板多为远程职位或抓取列表；厂商国家下拉菜单是市场覆盖表单；军事项目、科研/refuge IT、历史海缆建筑、Palmyra OTEC 提案均非 DC。
- 扫描顺序：确认 division → 商业关键词扫描 → 云官方页 → 目录与互联 → IANA → Wake/Johnston 联邦面 → FWS 全 refuge 页 → 行业媒体最后且未支持项降级 C/U。

## 维护注意（更新纪律）

- 每月：Wake/Johnston DoD 项目面、FWS 新闻、Federal Register、SAM.gov、USASpending。
- 每季：云区域页、IANA `.um`、PeeringDB/目录、FCC ULS/IBFS、Submarine Cable Map。
- 事件驱动：任何 UM 算力/AI/数据中心头条、Palmyra OTEC 复活、新的 Wake/Johnston 能源或通信授标、保护区/纪念地法律变更；任何阳性外观条目在升级前必须过 A 级门槛。
