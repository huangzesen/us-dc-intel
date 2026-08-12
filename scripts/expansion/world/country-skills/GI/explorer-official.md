# GI Explorer Official — 直布罗陀数据中心枚举·官方渠道方法论

日期：2026-08-12。国家：**GI Gibraltar（直布罗陀，英国海外领地）**。分区模型已按 `/Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/world/world-manifest.jsonl` 核对：`{"country_code":"GI","country_name":"Gibraltar","subnational_type":"country","divisions":["Gibraltar"]}`。因此官方枚举只有一个分区：**Gibraltar**。全境面积很小，设施定位在同一分区内用片区补充，如 Mount Pleasant、Port / North Mole、Europa Point、City Centre、Waterport、Europort、Ocean Village、Bayside / Business Bay、North Front / Airport。

本文件覆盖官方、监管、电力、电信、采购、云区域和设施种子。行业媒体、聚合目录和商业发现见 `explorer-industry.md`。

可靠性分级（本文件适用）：

- **A** = 一级证据：政府/监管/公报/招标/授予页面、公用事业、运营商自营设施页、官方云区域列表。
- **B** = 强二级证据：可信行业媒体、监管年报中的案例描述、PeeringDB/RIPE、供应商案例、具名公司新闻。
- **C** = 弱线索：聚合目录、市场平台、转售商声明、招商叙事、由公司地址或新闻措辞推断的机房。
- **U** = 未验证传闻或无法回溯来源的说法；仅作检索提示。

分级只适用于来源实际证明的事实。例如，Gibtelecom 自营 Data Centre Solutions 页面证明其提供托管/机房服务是 **A**；GRA 年报和 Privy Council 案件摘要点名 Gibtelecom 在 **Mount Pleasant** 拥有/运营数据中心，可把该设施位置提升为 **A/B**。但聚合目录中的容量、等级、客户数和重复条目，未被运营商或官方记录确认前仍为 **C**。

---

## 0. 已核实结论 (Verified Baseline)

- **分区完整性**：GI 只有 `Gibraltar` 一个分区；不得创建市镇、省份或西班牙边境区分区。西班牙 Campo de Gibraltar 只能作为跨境连接性语境，不能计入 GI 设施。
- **确认运营设施 1：Gibtelecom Data Centre / Mount Pleasant**。Gibtelecom 官网有 Data Centre Solutions、Hosting & Cloud Services、Private Cloud 等服务页；GRA 2019/2020 年报描述了 GibFibre 要求进入“located at Mount Pleasant and belonging to Gibtelecom”的 data centre；2025 年 Privy Council 案件摘要也写明 Gibtelecom owns and operates a data centre at Mount Pleasant where it hosts third party servers。作为设施存在与片区定位，按 **A/B**；容量、Tier、机柜数、具体街址未公开确认时不得升级。
- **确认运营设施 2：Continent 8 Gibraltar Data Centre / inside the Rock**。HM Government of Gibraltar 2024 新闻稿称 Continent 8 在 Rock 内约 500 米深处运营，提供 server hosting、cloud hosting 和 cybersecurity；Continent 8 官网 Gibraltar location 页面称其 Gibraltar data centre 为本地最安全/最互联/认证设施之一。作为设施存在按 **A**（政府+运营商）；详细容量未公开确认。
- **确认政府采购需求：Data Centre Hosting Services**。2022 年 HMGoG Tender Notice 和 Tender Award 均真实存在；Award 页面显示中标方为 Continent 8 Technologies Plc，合同期/金额信息可作为政府托管需求与供应商验证的 **A** 级证据。
- **已公布未来项目：Pelagos Data Centres near the Port of Gibraltar**。2025-09-04 HMGoG 新闻稿与 Pelagos 官网公布 250MW、五期、20,000 m2、近港口、首期计划 2027 年底运营、独立于 Gibraltar 现有电网供电。当前状态应标为 **Announced / planned**，按政府公告为 **A(公告/计划)**，但不是运营设施，不能计入现役容量。
- **Gibfibre 修正**：当前可验证来源显示 GibFibre / GibFibreSpeed 是经 GRA 授权的本地电子通信网络/服务提供者，官网与其他公开来源描述其为私有 full-fibre / FTTH 网络运营商。不要将其描述为政府所有的批发光纤机构。Gibfibre 的数据中心相关内容可作为企业服务/线索，但设施存在仍需独立确认。
- **超大规模云区域负面结论**：AWS、Azure、Google Cloud、Oracle OCI 官方区域列表没有 Gibraltar 区域；最近相关公有云区域在西班牙/马德里或西班牙 Aragón（AWS Europe Spain）。

---

## 1. 官方政府、公报、统计与采购 (Government, Gazette, Statistics & Procurement)

| 来源 Source | URL | 用途 Use | 分级 Grade |
|---|---|---|---|
| HM Government of Gibraltar | https://www.gibraltar.gov.gi/ | 政府新闻、部门公告、数字/金融/博彩政策、官方搜索入口。 | A |
| Press releases | https://www.gibraltar.gov.gi/press/press-releases | 查数据中心项目、能源、电信、政府访问和项目发布。 | A |
| Official Notices | https://www.gibraltar.gov.gi/press/official-notices | 公告、临时安排、公开通知；含部分 tender 类通知。 | A |
| Tender Notices | https://www.gibraltar.gov.gi/press/tender-notices | 政府招标入口；检索 hosting、cloud、backup、network、server room。 | A |
| Tender Awards | https://www.gibraltar.gov.gi/press/tender-awards | 中标方、金额、授予日期；设施供应商确认优先源。 | A |
| Government Contracts statistics | https://www.gibraltar.gov.gi/statistics/statistics-topic-area/2025/government-contracts | 年度政府合同表；追踪 IT/托管/网络采购。 | A |
| Statistics Office | https://www.gibraltar.gov.gi/statistics | 人口、经济、电力、政府合同等背景指标。 | A |
| Gibraltar Gazette | https://portal.egov.gi/services/gaz 和 https://www.gibraltarlawoffices.gov.gi/administration-office-and-gazette | 法规、公告、招标和授予线索；同时用 Press/Official Notices/Tenders 追踪近期公开通知。 | A |

官方检索模板：

```text
site:gibraltar.gov.gi "data centre"
site:gibraltar.gov.gi "data center"
site:gibraltar.gov.gi "Data Centre Hosting Services"
site:gibraltar.gov.gi "Continent 8"
site:gibraltar.gov.gi "Pelagos Data Centres"
site:gibraltar.gov.gi "Gibtelecom" "data centre"
site:gibraltar.gov.gi "server hosting"
site:gibraltar.gov.gi "cloud hosting"
site:gibraltar.gov.gi "tender" "hosting"
site:gibraltar.gov.gi "tender" "cloud"
site:gibraltar.gov.gi "backup" "disaster recovery"
site:gibraltar.gov.gi "North Mole Power Station" "data centre"
```

采购处理规则：

1. Tender Notice = 需求存在，通常 **A(采购需求)**；尚未授予时不得确认供应商或运营状态。
2. Tender Award = 中标方与金额，通常 **A**；若 award 点名 Gibraltar 内 Tier III facility，可作为设施需求细节证据。
3. 政府访问/新闻稿点名设施与运营商时为 **A**，但营销性容量和未来时间表要保留状态字段。

---

## 2. 监管与合规 (Regulators & Compliance)

| 来源 Source | URL | 用途 Use | 分级 Grade |
|---|---|---|---|
| Gibraltar Regulatory Authority (GRA) | https://www.gra.gi/ | 通信、数据保护、竞争、广播、邮政、高等教育、网络安全监管。 | A |
| GRA Communications | https://www.gra.gi/communications | 电子通信监管范围、授权运营商、咨询和决定。 | A |
| GRA Communications Notices | https://www.gra.gi/communications/documents/notices | 查 Gibtelecom、GibFibreSpeed、Sapphire/u-mee 等授权/设施权。 | A |
| GRA Data Protection | https://www.gra.gi/data-protection | Gibraltar GDPR / DPA 合规、数据保护监管。 | A |
| GRA Annual Reports | https://www.gra.gi/ 站内 Annual Report / uploads | 监管纠纷、市场结构、数据中心接入案例。 | A/B |
| GFSC | https://www.fsc.gi/ | 金融服务监管、持牌实体、DLT/VASP 名录。 | A |
| GFSC Regulated Entities | https://www.fsc.gi/regulated-entities | 银行、保险、支付、DLT 等持牌实体枚举。 | A |
| GFSC DLT Providers | https://www.fsc.gi/regulated-entities/dlt-providers-38 | DLT/数字资产持牌机构，本地托管需求线索。 | A |
| HMGoG Remote Gambling | https://www.gibraltar.gov.gi/finance-gaming-and-regulations/remote-gambling | Gambling Division 入口；博彩许可与监管需求语境。 | A |
| Gibraltar Finance | https://www.gibraltarfinance.gi/ | 金融/数字资产招商语境，不等于设施证据。 | A(自身)/C(项目线索) |

监管检索模板：

```text
site:gra.gi "data centre"
site:gra.gi "Mount Pleasant" "Gibtelecom"
site:gra.gi "GibFibre" "data centre"
site:gra.gi "authorised operator" "GibFibre"
site:fsc.gi "data centre"
site:fsc.gi "data residency"
site:fsc.gi "DLT Providers"
site:gibraltar.gov.gi "remote gambling" "data centre"
```

合规语境：金融、DLT/VASP 和在线博彩是本地托管需求的主要来源，但“持牌机构存在”只证明需求池，不证明其在 Gibraltar 有自营机房。持牌机构披露 local hosting / Gibraltar data residency 可作为 **B**；设施仍需运营商、采购或监管文件确认。

---

## 3. 电力与公用事业 (Power & Utilities)

| 来源 Source | URL | 用途 Use | 分级 Grade |
|---|---|---|---|
| Gibraltar Electricity Authority (GEA) | https://www.gea.gi/ | 电力机构、供电资产、电网语境。 | A |
| GEA Who We Are | https://www.gea.gi/gea/who-we-are | North Mole Power Station，约 80MW 装机，100+ substations。 | A |
| HMGoG energy / outage releases | https://www.gibraltar.gov.gi/press/press-releases | North Mole、BESS、供电中断、能源政策和大负荷项目语境。 | A |
| Pelagos HMGoG announcement | https://www.gibraltar.gov.gi/press-releases/pelagos-data-centres-unveils-ambitious-plan-for-new-250mw-facility-near-the-port-of-gibraltar-6412025-11196 | 250MW planned data centre 声称独立于现有电网供电。 | A(公告/计划) |
| HMGoG Continent 8 visit | https://www.gibraltar.gov.gi/press-releases/minister-feetham-visits-continent-8-technologies-datacentre-402024-9569 | 政府点名 Continent 8 Datacentre 位于 Admiralty Tunnel / COMCEN site。 | A |

电力判断：

1. Gibraltar 电网很小；现役设施一般不会公开 MW 级容量。任何 1MW+ 新项目、grid connection、substation、LNG/renewables self-generation，都应在政府、GEA、DPC 或规划文件中留下痕迹。
2. GEA 电站、North Mole、BESS、变电站不是数据中心；只作供电能力语境。
3. Pelagos 这类 250MW 规划明显超过本地公用电网常规语境，应核查“independent of Gibraltar’s existing grid”、燃料/电源、规划许可、环评和土地安排。

电力检索模板：

```text
site:gea.gi "data centre"
site:gea.gi "large user"
site:gibraltar.gov.gi "data centre" "grid"
site:gibraltar.gov.gi "Pelagos" "grid"
site:gibraltar.gov.gi "North Mole Power Station" "Pelagos"
site:gibraltar.gov.gi "substation" "data centre"
site:gibraltar.gov.gi "battery energy storage" "North Mole"
```

---

## 4. 电信与连接性 (Telecom & Connectivity)

| 来源 Source | URL | 用途 Use | 分级 Grade |
|---|---|---|---|
| Gibtelecom | https://www.gibtele.com/ | incumbent operator；企业连接、托管、云、PoP、新闻。 | A |
| Gibtelecom Data Centre Solutions | https://www.gibtele.com/business/hosting-and-cloud-services/data-centre-solutions | 托管/机房服务存在性。 | A |
| Gibtelecom Hosting & Cloud Services | https://www.gibtele.com/business/hosting-and-cloud-services | 数据中心 footprint：Gibraltar、London、Dublin、Malta、Malaysia 等。 | A |
| Gibtelecom Private Cloud | https://www.gibtele.com/business/hosting-and-cloud-services/private-cloud | private/public cloud 产品；需确认是否落地本地机房。 | A(产品) |
| Gibtelecom Points of Presence | https://www.gibtele.com/business/hosting-and-cloud-services/points-of-presence | PoP 与跨境/国际数据中心 footprint。 | A |
| GibFibre | https://gibfibre.com/ | 本地 private full-fibre/FTTH ISP 与企业连接线索。 | A(运营商角色) |
| GibFibre About | https://gibfibre.com/about/ | FTTH 时间线、SMB/enterprise 服务。 | A(自身声明) |
| GRA authorised-provider notices | https://www.gra.gi/communications/documents/notices | 授权运营商与设施权；核对 GibFibre/Gibtelecom/u-mee/Sapphire 等。 | A |
| Submarine Cable Map | https://www.submarinecablemap.com/ | 海缆和登陆点核查；Europa Point / Gibraltar 连接性语境。 | B |
| PeeringDB | https://www.peeringdb.com/ | ASN、设施、组织和互联线索；需账号/页面逐项核查。 | B/C |
| RIPE Database | https://apps.db.ripe.net/db-web-ui/ | ASN、路由对象、组织和联系人。 | B |

连接性检索模板：

```text
site:gibtele.com "Data Centre"
site:gibtele.com "Mount Pleasant"
site:gibtele.com "Gibraltar" "Data Centres in London and Gibraltar"
site:gibtele.com "co-location"
site:gibfibre.com "data centre"
site:gibfibre.com "co location"
site:gra.gi "Gibtelecom" "data centre"
site:gra.gi "GibFibre" "Mount Pleasant"
"Europa Point" "submarine cable" Gibraltar
"Gibraltar" "PeeringDB" "Gibtelecom"
"Gibraltar" "IXP"
```

---

## 5. 官方云区域负面核查 (Official Cloud-Region Negative Checks)

每次执行记录日期。本轮核查日期：2026-08-12。

| Provider | 官方来源 Official source | Gibraltar 结果 | 最近相关区域 |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | 官方区域表无 Gibraltar。 | Europe (Spain) `eu-south-2`。 |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | 官方区域表无 Gibraltar。 | Spain Central / Madrid。 |
| Google Cloud | https://cloud.google.com/about/locations 和 https://docs.cloud.google.com/compute/docs/regions-zones | 官方区域/zone 表无 Gibraltar。 | Madrid `europe-southwest1`。 |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ 和 https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | 官方区域表无 Gibraltar。 | Spain Central (Madrid) `eu-madrid-1`。 |

不要把 Gibtelecom/Continent 8/Pelagos 的本地托管或云产品描述成 hyperscale cloud region。它们是本地/行业托管、private/public cloud 或 planned campus 线索。

---

## 6. 分区查询模板与设施种子 (Division Templates & Facility Seeds)

唯一分区：**Gibraltar**。

```text
"data centre" "Gibraltar"
"data center" "Gibraltar"
"Gibraltar" "colocation"
"Gibraltar" "co-location"
"Gibtelecom" "Data Centre Solutions"
"Gibtelecom" "Mount Pleasant" "data centre"
"Continent 8" "Gibraltar" "data centre"
"Continent 8" "inside the Rock" "Gibraltar"
"Pelagos Data Centres" "Gibraltar"
"Gibraltar" "Data Centre Hosting Services" "Tender"
"Gibraltar" "Tier III" "data hall" "racks"
"Gibraltar" "server hosting" "cloud hosting"
"GibFibre" "data centre" "Gibraltar"
"Europa Point" "cable landing" "Gibraltar"
```

片区锚点：

- **Mount Pleasant**：Gibtelecom data centre 重点片区。
- **Inside the Rock / former MoD Operations Centre**：Continent 8 重点片区；公开资料通常不提供街址。
- **Port / North Mole**：Pelagos planned campus、GEA/North Mole 电力语境；电站不能误计为机房。
- **Europa Point**：海缆登陆/连接性语境，只有另有证据时才计为数据中心。
- **Europort / City Centre / Westside / Ocean Village / Bayside**：金融、博彩、专业服务和办公类内部机房线索区。
- **North Front / Airport**：通信基础设施、物流和园区语境，预期产出低。

设施种子清单：

| 设施/线索 Facility / lead | 分区 Division | 片区 Area | 状态 Status | 当前最佳证据 Best evidence | 分级 Grade |
|---|---|---|---|---|---|
| Gibtelecom Data Centre | Gibraltar | Mount Pleasant | Operating | Gibtelecom Data Centre Solutions；GRA 2019/2020 年报；Privy Council GibFibre v GRA 摘要 | A/B |
| Continent 8 Gibraltar Data Centre | Gibraltar | inside the Rock / former MoD facility | Operating | HMGoG 2024 Minister visit；Continent 8 Gibraltar location | A |
| Pelagos Data Centres | Gibraltar | near the Port of Gibraltar | Announced / planned; first phase targeted late 2027 | HMGoG 2025 announcement；Pelagos official announcement | A(计划) |
| GibFibre data-centre / co-location service claims | Gibraltar | 未公开确认 | Lead only | GibFibre site/searchable pages and GRA authorised-operator context; verify physical facility independently | C until facility confirmed |
| Government data centre hosting need | Gibraltar | 未指定；tender required Gibraltar | Procurement demand, supplier awarded | HMGoG 2022 Tender Notice/Award to Continent 8 | A(采购/需求) |
| Europa Point cable landing / submarine systems | Gibraltar | Europa Point | Connectivity asset | Submarine Cable Map / TeleGeography style sources; verify per cable system | B(landing/connectivity only) |

生产清单只接受五要素齐全条目：**具名运营商 + division=Gibraltar + 片区/位置 + 证据 URL + 状态 + 分级**。未来项目必须保留 `planned/announced/construction/operating` 状态，不得与运营设施混计。

---

## 7. 误报过滤 (False-Positive Filters)

- **Gibfibre ownership**：按 private/authorised ISP 与 fiber operator 处理，不按政府所有的批发光纤机构处理。
- **GDC 歧义**：GDC 可能指 Gibraltar Data Centre，也可能指 Gibraltar Development Corporation；必须先核实法人。
- **聚合目录重复**：Data Center Map 的“6 facilities”可作种子，不可直接入库；常复制运营商文本或把 planned 项目与运营站点混排。
- **电站/变电站误报**：North Mole Power Station、BESS、substations 不等于数据中心。
- **云产品误报**：private cloud、public cloud、DR、PoP、core network 不是云区域，也不必然是单独设施。
- **跨境误报**：Algeciras、La Linea、Estepona、Malaga、Ceuta、Tangier 设施不是 Gibraltar；只能作为网络路径或替代托管语境。
- **未来项目误报**：Pelagos 当前是 announced/planned，除非规划、施工或运营证据更新，不得计入现役设施容量。
