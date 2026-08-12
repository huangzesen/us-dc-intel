# NF Explorer Industry — 诺福克岛（Norfolk Island）数据中心枚举：运营商 / 行业媒体 / 目录 / 误报核验

日期 Date: 2026-08-12
范围 Scope: Norfolk Island（NF）。Manifest 已核验：`subnational_type=country`，`divisions=["Norfolk Island"]`（单一分区）。
角度 Angle: 行业/运营商/媒体口径发现（industry, operator, trade-press and vendor discovery）。任何设施在升级为 `operational` 库存前必须经官方或运营商一级来源核验。

可靠性分级 Reliability grades（本 explorer 使用）：
- **A** = 运营商官方页、公有/公共部门业主页、监管/登记记录、官方采购/会议文件、超大规模厂商官方位置页、IANA/注册处、交易所/公司公告。
- **B** = 可信行业/本地/地区媒体、承包商案例或 cable/telecom 数据库，要求具名当事方、日期、可回查事实。
- **C** = 目录站、市场平台、VPN/VPS 位置页、SEO 托管页、无一级链接转载或无法核实营销页。

## 0. 市场形态与当前结论 Market Shape And Current Conclusion

- **Norfolk Island 是 no-market / pre-commercial datacenter territory。** 本轮未发现任何经核实的第三方托管、commercial colocation、hyperscale、公有云区域、IXP 或设施级 DC 项目。
- 真实运营商景观是小岛电信/卫星/本地电力：Norfolk Telecom（NIRC 体系内）、Telstra satellite backhaul、历史 O3b/C8 satellite systems、NIRC Power house / electricity reticulation、NIDS `.nf` registry / ISP/VoIP/NBN services。
- **行业纠偏：Gondwana-1 不应作为 Norfolk Island landing seed。** 可核验的 Gondwana-1 行业资料把它描述为 New Caledonia-Australia cable，RFS 2008；未发现 Norfolk Island 分支/landing station 证据。凡把 `Gondwana-1 + Norfolk Island` 写成登陆设施的结果，需标为 `false_positive_or_regional_background`，除非找到 NIRC/NTL/OPT/ASN 一手文件。
- 最近的真实商业托管与云市场在 Sydney、Melbourne、Auckland；Nouméa/Guam 可作太平洋互联背景。它们绝不计入 NF inventory。
- 行业页面宣称 `Norfolk Island data center`、`Burnt Pine VPS`、`Norfolk dedicated server`、`NF cloud server` 的，多数是 SEO 国家/城市位置页。无设施地址、运营商、注册/许可、NIRC planning、电力或可信媒体证据时，判为 C 级误报。
- 检索语言使用英文；中文仅用于方法说明。核心关键词：`Norfolk Island`、`Norfolk Telecom`、`NIRC`、`Telstra satellite backhaul`、`O3b`、`.nf`、`Norfolk Island Data Services`、`+6723`、`Burnt Pine`、`Kingston`、`Cascade`、`Anson Bay`。

## 1. 运营商与供应商扫描 Operator And Vendor Sweep

| 运营商/线索 Operator / lead | 来源 URL | 地点侧重 | 证据用途 | 分级 |
|---|---|---|---|---|
| Norfolk Telecom / NIRC Telecom | https://www.nirc.gov.au/Corporate-finance/Norfolk-Telecom | Burnt Pine / 全领地 | 固定、移动、宽带、国际连接、网络 core/office 线索。可支撑 telecom asset，不支撑 commercial DC。 | A |
| NIRC satellite backhaul / Telstra contract | https://www.nirc.gov.au/Your-council/News-Articles/Satellite-Backhaul-Service | 全领地 | 2026 当前 backhaul 事实：DITRDCSA funding、2023 Telstra tender/contract、服务级别与费用。核心电信连接证据。 | A |
| Norfolk Telecom service pages (`ni.net.nf`) | https://www.ni.net.nf/adsl | 全领地 | ADSL/fixed broadband/phone-line/fibre language；客户服务线索，不等于 DC。 | A/B（运营商页；路径历史性需复核） |
| Telstra satellite / wholesale backhaul | https://www.telstra.com.au/ | Australia/NF backhaul | NIRC 合同相对方；仅在 NIRC/Telstra 明确 NF 服务时使用。 | A（合同事实以 NIRC 为准） |
| O3b / SES historical satellite | https://www.ses.com/ | Norfolk Island historical/current satellite | 2014-2015 O3b satellite backhaul and dishes；当前状态需复核。 | B/A（ABC/联邦报告；运营商页需复核） |
| Norfolk Island Data Services (NIDS) | https://www.norfolkislanddataservices.com/ 与 IANA https://www.iana.org/domains/root/db/nf.htm | `.nf` registry / ISP layer | `.nf` registry、VoIP、NBN/Sky Muster/IT services；hosting/registry 不等于 DC。 | A（registry/official site 存在性） |
| ACMA / DITRDCSA telecom framework | https://www.acma.gov.au/ ; https://www.infrastructure.gov.au/media-communications/internet/rules-carriers-and-service-providers | Regulatory | Carrier/service provider rules、licensing threshold、radiocomms/broadcasting evidence。 | A |
| Sydney/Melbourne DC operators（Equinix, NEXTDC, AirTrunk, CDC, Digital Realty, Global Switch, Macquarie 等） | 各官网 | Australia mainland | 区域后备托管/云接入背景；不得计入 NF。 | A（区域背景） |
| Auckland/NZ operators（Spark, Datacom, CDC NZ, DCI, Chorus 等） | 各官网 | New Zealand | 区域后备托管/云接入背景；不得计入 NF。 | A/B（区域背景） |
| Gondwana-1 / OPT / Submarine Networks | https://www.submarinenetworks.com/en/systems/australia-usa/gondwana-1 | New Caledonia-Australia | 区域 cable 背景；不是 NF landing evidence。 | B 背景；NF landing claim = 不支持 |

运营商搜索模板 Operator search templates：

```text
"{operator}" "Norfolk Island" ("data centre" OR "data center" OR datacenter OR colocation OR "co-location")
"{operator}" "Norfolk Island" (hosting OR "server room" OR rack OR "NOC" OR "core network" OR exchange)
"{operator}" "Norfolk Island" ("satellite backhaul" OR Telstra OR O3b OR C8 OR "earth station" OR "international connectivity")
"{operator}" "Norfolk Island" (construction OR commissioned OR operational OR tender OR contract)
"{operator}" "Burnt Pine" "Norfolk Island"
site:nirc.gov.au "{operator}" ("Norfolk Island" OR "Norfolk Telecom" OR telecommunications OR ICT OR backhaul)
```

## 2. 电信基础设施线索 Cable, Satellite And Telecom Leads

| 线索 Lead | 地点 | 当前解读 | 证据路径 | 可靠性 |
|---|---|---|---|---|
| Telstra satellite backhaul for Norfolk Telecom | Norfolk Island | 运营中的 backhaul 服务；NIRC 2026 年披露合同、成本、服务级别与重谈安排 | NIRC 2026 news/report | A |
| Norfolk Telecom core / exchange / office equipment | Burnt Pine / Norfolk Telecom office | 运营中的电信 core/office/equipment-room 线索；容量未公开；非商业 DC | 2015 Mobile Network Review、NIRC Norfolk Telecom | A（存在性） |
| O3b satellite dishes / historical satellite systems | Norfolk Island | 2014 两个 O3b satellite dishes 建设；2015 O3b IP + C8 backup backhaul；当前状态需复核 | ABC 2014、联邦 2015 report | A/B 历史；当前状态待核 |
| Mobile/base-station shelters and Mt Pitt fibre/backhaul | 多个站点，含 Mt Pitt 相关线索 | 2G/4G radio network support infrastructure；不是 DC | 2015 Mobile Network Review、后续 NIRC/NTL | A/B |
| NIRC Power house / electricity reticulation | Norfolk Island | 小型电网约束与大型负荷核验面；不是 DC | NIRC Electricity pages、tariff/asset docs | A |
| NIDS `.nf` registry / ISP services | Norfolk Island / registry layer | 域名、VoIP、NBN/Sky Muster、IT services；不视为本地 DC | IANA、NIDS official site | A（实体/服务存在性） |
| Gondwana-1 NF landing | N/A | 未核实/不支持；Gondwana-1 是 New Caledonia-Australia cable background | Submarine Networks / cable maps | C if claimed as NF facility |
| Historical Pacific Cable Station | Anson Bay / heritage context | 历史通信遗产；不是现代 DC，也不是当前 telecom landing evidence | heritage/media sources | B/C historical only |

电缆/卫星/电信查询 Cable/satellite/telecom queries：

```text
"Norfolk Island" ("satellite backhaul" OR "Telstra" OR "O3b" OR "C8 satellite" OR "earth station")
"Norfolk Telecom" ("satellite backhaul" OR Telstra OR O3b OR C8 OR "international connectivity" OR "earth station")
"Norfolk Island" "two satellite dishes" O3b
"Norfolk Island" "Mobile Network Review" ("core network" OR AXE OR "base station" OR "satellite systems")
"Norfolk Telecom" ("AXE" OR switch OR "core network" OR "server room" OR exchange)
"Norfolk Island" "Gondwana-1" OR "Gondwana 1" OR "cable landing station"
site:submarinenetworks.com "Norfolk Island"
site:submarinecablemap.com "Norfolk Island"
```

解释规则：

- Satellite backhaul is connectivity, not datacenter capacity.
- Cable maps are geography/background tools, not sufficient facility proof for NF.
- `earth station` / `satellite dishes` may be recordable as telecom assets if inventory scope includes telecom infrastructure; otherwise keep as context.
- Do not convert backhaul Mbps/Gbps into DC MW.

## 3. 行业媒体与二级来源 Trade Press And Secondary Sources

| 来源 Source | URL | NF 用途 | 分级 |
|---|---|---|---|
| ABC News | https://www.abc.net.au/news | 2014 O3b satellite dishes/backhaul story；credible regional media. | B |
| RNZ Pacific | https://www.rnz.co.nz/international/pacific-news | Norfolk governance/telecom/energy policy background. | B |
| Data Center Dynamics（DCD） | https://www.datacenterdynamics.com/ | 检索是否有 DC/edge/telecom proposal；预期阴性。 | B |
| CommsDay | https://www.commsday.com/ | 澳新电信/监管报道；paywall 结果需回查一级来源。 | B |
| ITNews Australia / ARN / CRN Australia | https://www.itnews.com.au/ ; https://www.arnnet.com.au/ ; https://www.crn.com.au/ | 澳洲 ICT procurement/managed services/vendor context. | B |
| Submarine Networks | https://www.submarinenetworks.com/ | Cable background and negative check；Gondwana-1 does not establish NF landing. | B/C depending fact |
| SubTel Forum / TeleGeography submarine cable map | https://subtelforum.com/ ; https://www.submarinecablemap.com/ | Cable map cross-check; use as background/negative control. | B/C |
| Islands Business / Pacific regional outlets | https://islandsbusiness.com/ | Pacific connectivity and government digital context. | B |
| Local NIRC newsletters / media releases | https://www.nirc.gov.au/Your-council/Media-releases | Council telecom/electricity/IT updates; if official NIRC, grade A. | A |
| Baxtel / DataCenterMap / Cloudscene / Datacenters.com | 各目录站 | DC directory negative control; expected empty or mislocated results. | C |
| VPS/VPN/location SEO pages | 各营销站 | False-positive capture only. | C |

行业查询示例 Trade query examples：

```text
site:datacenterdynamics.com "Norfolk Island" OR "Norfolk Telecom"
site:itnews.com.au "Norfolk Island" ("Norfolk Telecom" OR satellite OR Telstra OR ICT)
site:arnnet.com.au "Norfolk Island" ICT OR telecom OR Telstra
site:abc.net.au/news "Norfolk Island" (O3b OR satellite OR "Norfolk Telecom" OR internet)
site:rnz.co.nz "Norfolk Island" (telecom OR internet OR electricity OR "Norfolk Telecom")
site:submarinenetworks.com "Norfolk Island" OR "Gondwana-1"
"Norfolk Island" ("data centre" OR "data center" OR datacenter) -Sydney -Auckland -Guam
"Norfolk Island" ("colocation" OR "co-location" OR "dedicated server" OR VPS OR "cloud server")
```

## 4. 目录到一级核验工作流 Directory-To-Primary Verification Workflow

1. 官方/运营商扫描优先；目录扫描只作补充或阴性对照。
2. 若目录声称 Norfolk Island data center，必须回查运营商官网、物理地址、ABN/ASIC、ACMA/licensing、NIRC planning/tender/electricity evidence、可信媒体。
3. 检查是否只是服务国家列表、VPN endpoint、VPS checkout location、billing country、IP geolocation、CDN PoP 或 SEO doorway page。
4. 检查是否实际设施在 Sydney、Melbourne、Auckland、Guam、Nouméa 或其它区域市场。
5. 无一级证据时记录为 `seo_false_positive` / `directory_false_positive`；不得创建设施。
6. 对 `.nf` 和 NIDS：registry、DNS、VoIP、NBN、Sky Muster、IT support 仅证明服务，不证明 server hall 或 colocation。

目录/误报查询 Directory/false-positive queries：

```text
site:datacentermap.com "Norfolk Island"
site:datacenters.com "Norfolk Island"
site:cloudscene.com "Norfolk Island"
site:baxtel.com "Norfolk Island"
site:peeringdb.com "Norfolk Island"
"Norfolk Island" ("dedicated server" OR VPS OR "cloud server" OR "bare metal" OR "VPN server")
"Burnt Pine" "data center" OR "data centre" OR hosting OR server OR VPS
"Kingston" "Norfolk Island" "data center" OR hosting OR VPS
".nf" (hosting OR "data center" OR "data centre" OR colocation OR VPS)
```

## 5. 地点检索配方与覆盖矩阵 Locality Search Recipes And Coverage Matrix

单一分区（Norfolk Island）+ 领地内地点变体。每个地点执行通用块并标记 `covered`，即使结果为阴性。

通用地点扫描块 Universal locality sweep：

```text
"{locality}" "Norfolk Island" ("data centre" OR "data center" OR datacenter)
"{locality}" "Norfolk Island" (server OR "server room" OR hosting OR colocation OR "co-location" OR VPS)
"{locality}" "Norfolk Island" ("satellite backhaul" OR O3b OR Telstra OR "earth station" OR "Norfolk Telecom")
"{locality}" "Norfolk Island" (telecom OR internet OR broadband OR "mobile network" OR "base station")
"{locality}" "Norfolk Island" (power OR electricity OR "Power house" OR "power station" OR generator OR diesel OR solar OR battery)
"{locality}" "Norfolk Island" (tender OR procurement OR "development application" OR planning)
```

覆盖清单 Coverage checklist：

| 地点 | 行业可能性 | 分配说明 |
|---|---|---|
| Norfolk Island | 全覆盖 | Manifest 唯一 division；所有 official/operator/cloud/目录查询都以全领地执行。 |
| Burnt Pine | 中（telecom/utility/IT services）；低（DC） | NIRC offices、商业中心、Norfolk Telecom/NIRC 服务线索；无 commercial DC 证据。 |
| Kingston | 低-中（government ICT）；低（DC） | Government House/行政历史地点；政府机房线索无公开设施证据。 |
| Cascade | 低-中（port/infrastructure）；低（DC） | Port/wharf/public works；现代 cable landing 说法需严格核验，当前无 NF cable landing 证据。 |
| Anson Bay | 历史通信背景；低（现代设施） | Pacific Cable Station heritage false-positive risk；只作历史背景。 |
| Middlegate | 低 | 居民/服务区；电信/电力服务公告。 |
| Mt Pitt / Mount Bates | 低-中（radio/base station） | 可能出现 base station、radio、telecom backhaul 线索；不是 DC。 |
| Emily Bay / Ball Bay / Rocky Point / Steels Point / Headstone / Longridge | 极低-低 | 居民/农地/旅游地点；只需阴性覆盖。 |

高产出地点变体 High-yield locality variants：

```text
"Burnt Pine" "Norfolk Island" ("Norfolk Telecom" OR exchange OR switch OR "core network" OR "server room")
"Burnt Pine" "Norfolk Island" ("data centre" OR "data center" OR datacenter OR hosting)
"Kingston" "Norfolk Island" (government OR administration OR ICT OR server)
"Cascade" "Norfolk Island" (wharf OR port OR telecom OR cable OR "landing station")
"Anson Bay" "Norfolk Island" ("Pacific Cable Station" OR cable OR telegraph)
"Mt Pitt" "Norfolk Island" ("base station" OR radio OR telecom OR fibre OR fiber)
```

## 6. 容量提取指引 Capacity Extraction Guidance

- 当前无任何 NF commercial data center 可记录 MW/机架/建筑面积。
- Norfolk Telecom / NIRC 电信设施：除非来源明确给出 UPS、generator、rack、IT load、floor area 或 telecom room specs，否则 `capacity_mw: null`。
- Satellite backhaul：记录为 connectivity capacity（例如 Mbps/monthly cost/SLA），不得折算为 DC 容量。
- Electricity：NIRC Power house / reticulation / tariff review / asset plan 只说明电网约束和大型负荷可行性，不得折算成 DC MW。
- Cloud regions：AWS/Azure/GCP/OCI 在 Australia/NZ 的区域只作 off-island background，不给 NF facility capacity。

容量查询 Capacity queries：

```text
"Norfolk Island" ("data centre" OR "data center" OR datacenter) (MW OR racks OR "Tier III" OR Uptime OR "square metres")
"Norfolk Telecom" (rack OR UPS OR generator OR "server room" OR "core network" OR hosting)
"Norfolk Island" ("satellite backhaul" OR Telstra OR O3b) (Mbps OR Gbps OR bandwidth OR SLA OR capacity)
"Norfolk Island" ("Power house" OR "power station" OR electricity) (capacity OR MW OR kW OR diesel OR generator)
site:nirc.gov.au ("capacity" OR MW OR kW OR generator OR "asset management plan") ("electricity" OR "Power house")
```

## 7. 枚举矩阵与分级规则 Enumeration Matrix And Grading Rules

| 候选 | 类型 | 建议状态（截至 2026-08-12） | 证据路径 | 分级 |
|---|---|---|---|---|
| Telstra satellite backhaul for Norfolk Telecom | telecom_backhaul | operational / contract under renegotiation | NIRC 2026-04-02 official news/report | A |
| Norfolk Telecom core / exchange / office equipment | telecom_exchange_or_core | operational; capacity unknown | NIRC Norfolk Telecom + 2015 federal review | A |
| O3b satellite dishes / historical earth-station systems | satellite_earth_station_or_backhaul | historical confirmed; current role needs update | ABC 2014 + 2015 federal review; NIRC 2026 satellite context | A/B |
| NIRC Power house / electricity reticulation | power_utility | operational | NIRC electricity pages | A |
| NIDS / `.nf` registry and ISP/VoIP services | registry_isp_service | operational service; exclude as DC | IANA + NIDS official site | A |
| Gondwana-1 NF landing | false_positive_or_regional_background | exclude; no NF landing proof | Gondwana-1 cable pages list New Caledonia-Australia | C for NF facility claim |
| SEO “Norfolk Island data center/VPS” pages | seo_false_positive | exclude | no primary evidence | C |
| Sydney/Melbourne/Auckland/Nouméa/Guam facilities | regional_background | exclude from NF | operator/cloud official pages | A/B only as off-island context |

分级规则 Grading rules：

- A 级来源证明其实际陈述的事实；例如 NIRC satellite backhaul 证明 backhaul 服务，不证明 DC。
- 只有 A 级来源或直接引用/链接一手文件的 B 级报道可确立 `operational`。
- 电信、电力、历史 cable heritage 与商业 DC 严格区分。
- 区域 cable map/market directory 如无 NF landing/physical-address proof，只能作背景或误报。
- 目录、SEO、VPN/VPS 结果无论页面说法多明确，未通过 operator/government/planning/electricity 复核前均不得入库。

## 8. 预期枚举结果 Expected Enumeration Outcome

预期输出是极小且保守的清单：Norfolk Telecom / NIRC satellite backhaul、Norfolk Telecom core/exchange/office equipment、历史/当前 satellite earth-station assets、NIRC Power house/electricity reticulation、NIDS `.nf` registry/ISP services，以及若干 C 级 SEO/目录误报。**预期不会出现任何经证实的商业数据中心。** 若未来出现 NF data center 宣称，必须具备具名运营商、明确地点、设施类型、运营状态以及 NIRC/电力/规划/采购或监管证据后才能进入库存。
