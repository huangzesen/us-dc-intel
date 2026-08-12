# VU Explorer Industry — 瓦努阿图数据中心枚举 · 行业/厂商来源

日期: 2026-08-12。范围: 瓦努阿图共和国 (Vanuatu, VU)，全国 6 省 (provinces): Malampa、Penama、Sanma、Shefa、Tafea、Torba（已按 `world-manifest.jsonl` 核对）。角度: 通过行业、运营商、厂商、目录和媒体渠道发现商业数据中心、托管/colo、电信设施、政府 DC 项目和误报。

可靠性分级 (Reliability grades): **A** = 运营商/厂商官方页、监管牌照/命令、政府/DCDT/PMO、国企或公用事业、官方云区域页、官方项目文件；**B** = 可靠行业/本地/区域媒体（具名+日期）、运营商访谈、承包商案例、多边项目页；**C** = 目录站、海缆追踪器、PeeringDB/ASN 聚合、LinkedIn/社交、转售/SEO 页、市场报告片段。C 级仅作线索，须独立锚定后方可升级。

## 0. 已验证行业基线 (Verified Industry Baseline)

- 未发现瓦努阿图存在公开销售的中性机柜托管 (neutral rack colocation) 或超大规模商业数据中心市场。已确认的数据中心信号是 **政府数据中心 (Vanuatu Government Data Centre / VGDC) in Port Vila, Shefa**，不是商业 colo。
- DCDT 官方 brochures 页面列出 `Vanuatu Government Data Center` 与 `Vanuatu Internet Exchange Point`；DCDT VIX 页面说明 VIX housed at the Vanuatu Government Data Centre in Port Vila；PMO 公告确认 Data Centres and Cloud Pilot Project remain property of the State of Vanuatu，并要求 DCDT complete implementation of the VGDC project。
- 行业设施/连接性集中在 **Port Vila / Shefa**: VGDC/VIX、ICN1 维拉港登陆站、TVL/Vodafone、Digicel、Telsat/WanTok、政府/银行/企业服务器房线索。**Santo/Sanma、Malekula/Malampa、Tanna/Tafea** 有 Tamtam cable 覆盖/节点信号，但不是 DC 证据。
- Starlink、Kacific/SES/O3b、移动塔、Wi-Fi、宽带覆盖、海缆登陆站、IXP、NOC 和运营商总部均为连接性或电信资产；除非来源明确描述 data centre、server room、racks、colocation、DR site 或 hosting facility，否则不计为数据中心。
- 检索语言: 英语优先；同时使用法语与 Bislama 变体。术语双拼: `data center` / `data centre` / `datacenter`、`colo` / `colocation` / `co-location`、`hosting` / `hébergement`、`server` / `serveur`、`cable station` / `station d'atterrissement` / `stesen kabel`。

## 1. 行业来源图谱与分级 (Industry Source Map And Grades)

| 来源/参与者 | URL | 用途 | 等级 |
|---|---|---|---|
| DCDT / digital.gov.vu | https://dcdt.gov.vu/ ; https://digital.gov.vu/ | VGDC、VIX、数字化项目、政府 DC 官方锚点。 | A |
| PMO | https://pmo.gov.vu/ | COM 决定、Tamtam/data centres/government broadband/cloud pilot 国家所有权。 | A |
| TRBR Vanuatu | https://www.trbr.vu/ | 持牌服务商、UAP、年度报告、RIO、监管状态。 | A |
| Vodafone Vanuatu / TVL | https://vodafone.com.vu/ | 在位电信商；固定/移动/企业网络线索；TVL 旧域可用作历史线索。 | A（官方存在）；B/C（设施推断） |
| Digicel Vanuatu | https://www.digicelpacific.com/mobile/vu | 移动/家庭/企业服务线索；Port Vila office/address 可作运营商存在。 | A（官方存在）；B/C（设施推断） |
| Telsat Broadband | 当前以目录、社交和 WanTok/Telsat references 为主；历史邮箱/域 `telsatbb.vu` | 卫星/无线 ISP 和远程连接；设施证据不足。 | B/C |
| WanTok Pacific / WanTok Tonga | https://wantok.to/ | 2020 press page claims WanTok acquired Telsat Broadband and offers ICT/networking/colocation menu items; must verify Vanuatu physical facility before upgrade. | B（公司公告）；C/B（facility） |
| Interchange | https://interchange.vu/subsea-cables/ | ICN1、planned ICN2/ICN3、Port Vila-Suva cable、Santo/Tanna connectivity background。 | A（官方海缆） |
| ADB Tamtam | https://www.adb.org/projects/59142-005/main | Tamtam 第二国际海缆项目、节点/融资/status。 | A/B |
| URA / DOE / UNELCO / VUI | https://ura.gov.vu/ ; https://doe.gov.vu/ ; https://unelco.engie.com/ | 电力约束；Port Vila/UNELCO, Santo/VUI；拒绝无电力证据的大负荷 DC。 | A |
| VFSC / Investment / VNSO | https://www.vfsc.vu/ ; https://investvanuatu.vu/ ; https://vnso.gov.vu/ | 法人、投资、统计背景；法律存在不等于设施存在。 | A |
| Data Center Dynamics | https://www.datacenterdynamics.com/ | 行业媒体；已检索到澳大利亚资助 Vanuatu data centers 报道，但需以 DCDT/PMO/PDF 锚定。 | B |
| Vanuatu Daily Post / VBTC / RNZ / Islands Business | https://dailypost.vu/ ; https://vbtc.vu/ ; https://www.rnz.co.nz/pacific ; https://islandsbusiness.com/ | 本地/区域报道、地震/海缆/政府项目/运营商状态。 | B |
| DataCenterMap / Cloudscene / Inflect / Connectbase / Datacenters.com | 各目录站 | 负控与线索；若点名 VGDC、VIX、运营商或地址，必须回到官方来源核实。 | C |

## 2. 运营商、设施与厂商扫描 (Operator, Facility And Vendor Sweep)

### 2.1 Vanuatu Government Data Centre / VIX

已验证行业相关性:

- DCDT brochures 页面列 `Vanuatu Government Data Center` 和 `Vanuatu Internet Exchange Point`，对应 PDF 链接分别为 `/images/brochures/VGDC.pdf` 与 `/images/brochures/VIX.pdf`。
- DCDT events 页面说明 VIX housed at the Vanuatu Government Data Centre in Port Vila。
- PMO COM 公告说明 Data Centres and Cloud Pilot Project remain property of the State of Vanuatu，并指示 DCDT complete implementation of VGDC project with Australian Government support。
- DCD/目录类来源可补充机架数、近 Meteo Department Building、redundant smaller DC 等线索，但这些细节必须用 DCDT PDF、采购或 PMO/DOFT 文件复核后才能作为 A 级字段。

查询:

```text
"Vanuatu Government Data Centre" OR "Vanuatu Government Data Center" "Port Vila"
site:dcdt.gov.vu VGDC OR "Government Data Center" OR "Government Data Centre"
site:digital.gov.vu VIX "Government Data Centre" "Port Vila"
site:pmo.gov.vu "Data Centres" "Cloud Pilot Project" "State of Vanuatu"
site:datacenterdynamics.com Vanuatu "data centers" "Port Vila" "Australia"
```

判定:

- 可登记 `Vanuatu Government Data Centre, Port Vila, Shefa` 为 `government_dc`。
- `VIX` 作为 `ixp_inside_government_dc` 属性或相关设施，不作为独立商业 DC。
- 未披露地点的 “data centres” 保持 `government_dc_project`，不得自动分配到 Sanma。

### 2.2 TVL / Vodafone Vanuatu

已验证行业相关性:

- 官方域 https://vodafone.com.vu/ 可用；TVL 为历史/法律名称线索。
- TRBR UAP 页面点名 Telecom Vanuatu Ltd 与 Digicel、Telsat 为 UAP players。
- 交换/网关/NOC/主机设施线索预计在 Port Vila；消费级网页、SIM、宽带和 webmail 不足为 DC 证据。

查询:

```text
site:vodafone.com.vu (hosting OR server OR cloud OR enterprise OR business OR NOC OR switch OR gateway OR "data centre" OR "data center")
"Telecom Vanuatu" OR "Vodafone Vanuatu" ("Port Vila" OR Tagabe OR Erakor OR Nambatu) (gateway OR switch OR NOC OR server OR hosting OR "data centre" OR "data center")
site:trbr.vu "Telecom Vanuatu" OR TVL OR Vodafone
```

### 2.3 Digicel Vanuatu

已验证行业相关性:

- 官方瓦努阿图页面: https://www.digicelpacific.com/mobile/vu；联系页列 Corporate Address: Ellouk Plateau, PMB 9103, Port-Vila, Vanuatu。
- Digicel 是 TRBR/UAP 参与者；核心网络设施存在为合理电信推断，但设施级证据仍需官方/监管/采购/媒体点名。

查询:

```text
site:digicelpacific.com/mobile/vu (enterprise OR business OR network OR cloud OR hosting OR "data centre" OR "data center")
"Digicel Vanuatu" ("data center" OR "data centre" OR NOC OR switch OR hosting OR cloud OR server OR gateway)
site:trbr.vu "Digicel Vanuatu" OR Digicel
"Digicel Vanuatu" "Ellouk Plateau" "Port-Vila"
```

### 2.4 Telsat Broadband / WanTok / Canopy / smaller ISPs

已验证行业相关性:

- TRBR UAP 页面点名 Telsat Broadband Ltd；目录和社交资料显示 Telsat 位于 Port Vila，但目录只给 B/C 级线索。
- WanTok page `https://wantok.to/wantok-network-announces-acquisition-of-telsat-broadband/` 已验证存在，2020-07-10 press item says WanTok Network entered agreement to acquire Telsat Broadband. 站点页脚/菜单出现 ICT、Networking、Website Hosting、Colocation 等服务词，但站点主体是 WanTok Tonga/Pacific；不能据此证明 Vanuatu colo facility。
- Canopy Vanuatu 需要用官方域、TRBR 或本地媒体重新锚定；仅从旅游/覆盖指南出现不可登记。

查询:

```text
"Telsat Broadband" Vanuatu ("Port Vila" OR office OR head-end OR server OR NOC OR "data centre" OR "data center")
site:trbr.vu Telsat OR "Telsat Broadband"
site:wantok.to Telsat Vanuatu acquisition colocation hosting
"WanTok" Vanuatu (server OR hosting OR NOC OR network OR Digicel OR acquisition OR colocation)
"Canopy" Vanuatu (fiber OR fibre OR broadband OR server OR NOC OR "Port Vila" OR Luganville)
```

判定:

- Telsat/WanTok/Canopy 默认 `isp_or_connectivity_lead`。
- WanTok 的 `Colocation` 菜单项是跨国服务/营销线索；只有点名 Vanuatu site/address/racks 时才升级。

### 2.5 Interchange / ICN1 / Tamtam

已验证行业相关性:

- Interchange 官方页面说明 ICN1 于 2014 年完成，连接 Port Vila 到 Suva, Fiji，并接入 Southern Cross。
- PMO/ADB 已确认 Tamtam 第二海缆项目，连接 Lifou, New Caledonia 到 Vanuatu，改善 Santo、Malekula、Efate、Tanna 连接。
- 海缆、登陆站和 IXP 可以支撑互联/延迟/冗余背景，但不自动构成商业 DC。

查询:

```text
site:interchange.vu (ICN1 OR ICN2 OR ICN3 OR cable OR capacity OR "Port Vila" OR Suva OR Santo OR Tanna)
"ICN1" Vanuatu ("Port Vila" OR Suva OR capacity OR outage OR upgrade OR landing)
"Tamtam Submarine Cable" Vanuatu (Santo OR Malekula OR Efate OR Tanna OR Lifou OR Prima OR ADB)
site:adb.org "Tamtam Submarine Cable Project" "Vanuatu"
```

### 2.6 企业与公共部门服务器机房线索

潜在线索: Reserve Bank of Vanuatu、ANZ、BSP、NBV、BRED、财政/海关/统计/移民、Vanuatu Airports、USP Emalus、National University of Vanuatu、医院、酒店/航空/港口系统。通常是内部服务器房或云消费者。

```text
"Reserve Bank of Vanuatu" OR RBV ("data centre" OR "data center" OR "disaster recovery" OR server OR IT)
"National Bank of Vanuatu" OR "ANZ Vanuatu" OR "BSP Vanuatu" ("data centre" OR "data center" OR "disaster recovery" OR server)
"USP Emalus" OR "University of the South Pacific" Vanuatu (server OR "data centre" OR network OR hosting)
"Airports Vanuatu" OR AVL (server OR ICT OR "data centre" OR "data center" OR network)
"Vanuatu" (ministry OR government OR department) ("server room" OR "data centre" OR "data center" OR "disaster recovery")
```

仅当来源点名物理设施、地点和功能时计入；否则标记 `enterprise_server_room_lead` 或忽略。

## 3. 行业媒体、目录与负控 (Trade Press, Directories, And Negative Controls)

高价值媒体/目录:

- Vanuatu Daily Post: https://dailypost.vu/
- VBTC: https://vbtc.vu/
- RNZ Pacific: https://www.rnz.co.nz/pacific
- Islands Business: https://islandsbusiness.com/
- Data Center Dynamics: https://www.datacenterdynamics.com/ （Cloudflare 可能阻挡直接抓取；可用搜索片段和二次来源，但最终字段回锚 DCDT/PMO）
- Submarine Networks: https://www.submarinenetworks.com/ 和 submarinecablemap.com/cablestatus/geocables 仅作海缆 B/C 线索
- Inflect / Connectbase / Datacenters.com / DataCenterMap / Cloudscene 仅作 C 级目录线索

搜索模板:

```text
"Vanuatu" ("data center" OR "data centre" OR datacenter OR colocation OR "co-location" OR "server hosting" OR "managed hosting") -proxy -VPS
"Port Vila" ("data center" OR "data centre" OR server OR hosting OR colocation OR "landing station" OR "cable station" OR VIX)
"Luganville" OR "Santo" ("landing station" OR "cable station" OR server OR internet OR telecom OR fibre OR fiber)
"Vanuatu Government Data Centre" OR "Vanuatu Government Data Center"
"Vanuatu" "Tamtam" "data centre" OR "government broadband"
site:dailypost.vu ("data centre" OR "data center" OR internet OR broadband OR cable OR Starlink OR digital OR telecom)
site:datacenterdynamics.com Vanuatu OR "Port Vila"
site:datacentermap.com Vanuatu OR "Port Vila"
site:cloudscene.com Vanuatu OR "Port Vila"
site:connectbase.com "Vanuatu Government Datacenter"
site:inflect.com "Vanuatu Government Datacenter"
```

目录处理规则:

- 目录点名 `Vanuatu Government Datacenter`、`No2 Area`、`Port Vila`、`VIX` 等: 回到 DCDT/PMO/VGDC PDF 核实，目录字段保持 C。
- “data center consulting in Port Vila / dedicated server / VPS / edge location” 无本地运营商、地址、设施页或监管锚点: `discarded_reseller_or_directory_lead`。
- DataCenterMap/Cloudscene 无条目是弱负信号，不证明无政府或企业服务器房。

## 4. 三语查询模板与各省枚举矩阵 (Tri-lingual Query Templates & Per-Province Enumeration Matrix)

通用清扫 (Generic sweep, EN/FR/BI):

```text
EN: "{Province}" Vanuatu ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR "server room" OR cloud OR "landing station" OR "cable station" OR NOC OR switch OR fibre OR fiber OR broadband)
EN: "{Province}" Vanuatu (VGDC OR VIX OR Tamtam OR TVL OR "Vodafone Vanuatu" OR Digicel OR Telsat OR WanTok OR Canopy OR Interchange OR Starlink)
FR: "{Province}" Vanuatu ("centre de données" OR "salle de serveurs" OR hébergement OR colocation OR "station d'atterrissement" OR opérateur OR fibre OR FAI)
BI: "{Province}" Vanuatu ("stesen kabel" OR "kompani blong internet" OR "serbis blong internet" OR server OR internet OR letrik OR telikom)
```

| 省份 | 预期行业发现 | 厂商路线 | 判定规则 |
|---|---|---|---|
| Shefa | VGDC/VIX、ICN1 Port Vila、运营商总部/核心、银行/政府服务器房、目录命中 | DCDT/PMO、Interchange、TRBR、Vodafone/Digicel、Telsat/WanTok、DCD/目录回锚 | 可登记 VGDC 为 `government_dc`；ICN1 为 `telecom_cable_station`；其余运营商设施不无证升级。 |
| Sanma | Santo/Luganville Tamtam 节点、运营商覆盖、VUI 电力、旅游/企业连接 | ADB/PMO Tamtam、TRBR、Digicel/Vodafone/Canopy 搜索、URA/VUI | Tamtam 是连接项目；无 data centre 词和地点证据则不计 DC。 |
| Malampa | Malekula Tamtam 覆盖、UAP/移动/卫星连接 | ADB/PMO、TRBR UAP、运营商覆盖 | 仅 `connectivity_project` 或 `no_projects`。 |
| Tafea | Tanna Tamtam 覆盖、旅游 ICT、卫星/离网电力 | ADB/PMO、TRBR UAP、Starlink/卫星线索 | 连接性/离网电力为负控；除非命名设施，记 `no_projects`。 |
| Penama | Ambae/Pentecost/Maewo 连接、灾后重建 ICT | TRBR UAP、媒体、政府数字项目 | 灾后/教育 ICT 不是 DC；无命名设施则 `no_projects`。 |
| Torba | Torres/Vanua Lava/Sola 小型连接、政府 ICT 房间 | TRBR UAP、媒体、卫星/移动覆盖 | 小型接入设施不计 DC；无命名设施则 `no_projects`。 |

覆盖检查: 上表恰好覆盖全部 6 省各一次。

## 5. 云、卫星与连接性扫描 (Cloud, Satellite, And Connectivity Sweep)

官方云缺失检查:

```text
"Vanuatu" ("AWS region" OR "AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "OCI region")
"Vanuatu" ("cloud region" OR hyperscale OR "public cloud" OR "sovereign cloud" OR "data residency")
```

仅用官方清单: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google Cloud https://cloud.google.com/about/locations ; Oracle OCI https://www.oracle.com/cloud/public-cloud-regions/ 。截至 2026-08-12 未见 VU 区域。

卫星/连接性规则:

- Starlink、Kacific、SES/O3b、VSAT、社区 Wi-Fi、移动覆盖、学校 CLICC/telemedicine 设备均为 `connectivity_only`。
- Tamtam、ICN1、VIX 是互联/连接资产；只在 DCDT/PMO 点名 VGDC 时才支撑政府 DC。
- 数据驻留/主权数据主张需回到 DCDT、CERT VU、Data Protection legislation 和 PMO COM 决定。

## 6. 命中捕获字段 (Capture Fields For Any Hit)

```text
name:
operator_or_owner:
province:
town_or_site:
coordinates_or_address:
source_url:
source_date:
source_grade: A|B|C
facility_type: commercial_colo | government_dc | government_dc_project | ixp_inside_government_dc | telecom_cable_station | telecom_core | enterprise_server_room | tower_edge | connectivity_only | false_positive
status: proposed | planned | procurement | implementation | under_construction | operational | discontinued | false_positive
basis_for_status:
capacity_or_power_claim:
power_evidence:
license_or_registry_anchor:
notes:
```

升级规则:

- 升级为 `commercial_colo` 仅当存在运营商页面、资费/产品页、设施页或合同明示在瓦努阿图提供 colocation/机架/数据中心服务。
- 升级为 `government_dc` 仅当 DCDT/PMO/采购/多边文件点名政府数据中心和地点；VGDC Port Vila 已满足存在条件。
- 海缆站保持 `telecom_cable_station`；IXP 保持 `ixp_inside_government_dc` 或 `interconnection`.
- Starlink、铁塔、Wi-Fi、VSAT、宽带覆盖、Tamtam 覆盖、省级 UAP rollout 保持 `connectivity_only`。

## 7. 陷阱 (Pitfalls)

- SEO 托管页常推销 “Vanuatu VPS / Port Vila dedicated server / data center consulting”，无实体设施；按 C 级忽略。
- WanTok/Telsat/Canopy 的 hosting、ICT、networking 或 colocation 字样可能是跨国服务或营销菜单；必须要求 Vanuatu 物理站点证据。
- 运营商总部在维拉港不等于数据中心；在设施/功能核验前使用 `telecom_core_lead`。
- 海缆站、VIX、网关可以与数据中心同址，但不能相互替代；分类应保留设施功能差异。
- 邻国 Fiji Suva、New Caledonia Lifou/Noumea、Solomon Honiara 的海缆/运营商名称易混淆；仅统计瓦努阿图境内站点。
- 电力资产（UNELCO/VUI 柴油、水电、太阳能、风电、BESS、变电站）是可行性背景，不是数据中心。

## 8. 来源速查表 (Source Quick List)

- DCDT / VGDC / VIX: https://dcdt.gov.vu/ ; https://dcdt.gov.vu/index.php/media-files/brochures ; https://dcdt.gov.vu/images/brochures/VGDC.pdf ; https://dcdt.gov.vu/images/brochures/VIX.pdf ; https://digital.gov.vu/index.php/media-files/events
- PMO COM decision: https://pmo.gov.vu/en/public-information/press-release/1145-council-of-ministers-approves-key-recommendation-on-the-tamtam-submarine-cable%2C-data-centre-and-government-broadband-network.html
- TRBR: https://www.trbr.vu/ ; https://www.trbr.vu/contact-us ; https://www.trbr.vu/telecom-industry/universal-access/universal-access-policy
- Operators: https://vodafone.com.vu/ ; https://www.digicelpacific.com/mobile/vu ; https://www.digicelpacific.com/mobile/vu/contact-us ; https://wantok.to/wantok-network-announces-acquisition-of-telsat-broadband/
- Interchange/ICN1: https://interchange.vu/subsea-cables/
- ADB Tamtam: https://www.adb.org/projects/59142-005/main ; https://www.adb.org/sites/default/files/project-documents/59142/59142-005-iee-en.pdf
- Power: https://ura.gov.vu/ ; https://ura.gov.vu/en/electricity/whom-do-we-regulate/unelco ; https://ura.gov.vu/en/electricity/whom-do-we-regulate/vanuatu-utilities-infrastructure-limited ; https://doe.gov.vu/ ; https://unelco.engie.com/
- Registry/statistics/investment: https://www.vfsc.vu/ ; https://investvanuatu.vu/ ; https://vnso.gov.vu/
- Media/directories: https://dailypost.vu/ ; https://vbtc.vu/ ; https://www.rnz.co.nz/pacific ; https://islandsbusiness.com/ ; https://www.datacenterdynamics.com/ ; https://www.submarinenetworks.com/ ; https://inflect.com/ ; https://www.connectbase.com/
- Cloud absence: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google Cloud https://cloud.google.com/about/locations ; OCI https://www.oracle.com/cloud/public-cloud-regions/

刷新指令: 再次运行时先重跑 DCDT VGDC/VIX、PMO COM/Tamtam、TRBR license/UAP/RIO、Interchange/ADB Tamtam、URA/DOE power、运营商官方页、本地媒体和官方云区域清单，再变更瓦努阿图设施状态。
