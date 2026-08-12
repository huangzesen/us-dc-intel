# SJ 行业渠道探索 - 斯瓦尔巴和扬马延数据中心枚举
# SJ Explorer Industry - Svalbard and Jan Mayen Datacenter Enumeration

日期 Date: 2026-08-12。范围 Scope: 从行业侧发现并核查 Svalbard and Jan Mayen (SJ) 的数据中心线索。所有候选必须与 `explorer-official.md` 交叉核对；行业来源用于发现，官方/运营商一手来源用于定性。

清单确认 Manifest check: SJ 在 `world-manifest.jsonl` 中只有一个分区 `Svalbard and Jan Mayen`。行业记录必须使用该 repo division，并用 `sub_area: Svalbard | Jan Mayen` 做内部拆分。

本文档为中文为主、英文/挪威语关键词为辅的双语方法论（Chinese-primary bilingual）。

## 1. 行业结论（Industry conclusion）

截至 2026-08-12，行业侧未发现可验证的 SJ 商业数据中心、colocation、hyperscale 或公有云区域。真实存在且最容易误报的数据/通信实体是：

- **KSAT SvalSat / Svalbard Ground Station**: 世界级极轨卫星地面站，位于 Svalbard 的 Plataberget/Longyearbyen 附近，含天线、接收、传输、数据处理相关技术空间；分类为 `satellite_ground_station`。
- **Space Norway Svalbard fibre**: Svalbard 至挪威本土双海缆，关键通信基础设施；分类为 `telecom_subsea_fibre` 或 `interconnection`，不是 DC。
- **Jan Mayen station**: Forsvaret/Met.no 站点，含气象、Galileo、通信、地震传感器等；分类为政府/通信/导航设施，不是 DC。
- **UNIS、KHO、EISCAT、SIOS、新奥勒松研究设施**: 科研数据与观测设施；分类为 `research_it`。
- **Seed Vault**: 政府/国际种子保存设施，任何监控系统只记 `government_monitoring`。

可靠性分级 Reliability grades:

- **A 级**: 运营商官方页、Nkom、Lovdata、regjeringen.no、Forsvaret、Space Norway、KSAT、云厂商官方区域页。
- **B 级**: 可靠行业媒体、主流媒体、科研机构页面，具备主体/地点/日期。
- **C 级**: 目录站、市场报告、销售页面、联系表单国家列表。
- **U 级**: 无法打开或无法二次确认。

行业结论不能只靠目录站或市场报告。任何 “Svalbard data center” 线索都必须回答：是否提供面向第三方客户的付费数据中心/托管服务？是否有 Nkom/许可/企业登记/运营商设施页？如果答案是否，则不得计为商业 DC。

## 2. 已核验行业实体图谱（Verified operator/platform map）

| 主体 Operator/platform | 官方/一手来源 Source | 行业定性 Classification |
|---|---|---|
| KSAT - SvalSat / Svalbard Ground Station | https://www.ksat.no/about-us/ ; https://www.ksat.no/news/news-archive/2021/ksat-has-installed-antenna-number-100-at-svalbard-ground-station/ ; https://www.ksat.no/news/news-archive/20152/ksat-svalbard-ground-station-in-mission-impossible2/ | A 级证明地面站存在。1997 建站；2021 年高原第 100 个天线；2025 页面称近 200 天线。不是商业 DC。 |
| KSAT ownership | https://www.ksat.no/about-us/ | A 级。KSAT 由 Space Norway AS 与 Kongsberg Defence & Aerospace AS 各持 50%。 |
| Space Norway - Svalbard fibre | https://spacenorway.com/satellite-connectivity-solutions/fibre-connectivity/svalbard-fibre/ ; https://spacenorway.com/infrastructure/subsea-fibre-cables/fibre-optic-cables/ | A 级互连基础设施。双海缆、约 1400 km、8 对光纤、2004 投运、服务保障至 2028、新方案考虑 Jan Mayen。不是 DC。 |
| Space Norway - Co-location and Hosting | https://spacenorway.com/infrastructure/ground-services/co-location-and-hosting-services/ | A 级主体页，但地点是 Nittedal Teleport（挪威本土），不是 SJ。记录为 SJ false positive。 |
| Nkom register | https://nkom.no/datasenter/oversikt | A 级监管负向表面。2026-08-12 复核未见 Svalbard/Jan Mayen/Longyearbyen/KSAT/Telenor/Space Norway 商业 DC 运营商条目。 |
| Jan Mayen station | https://www.forsvaret.no/jobb/jan-mayen | A 级。17 人常驻工作站，含 Forsvaret、Met.no、Galileo、Telenor Kystradio、地震传感器等。不是商业 DC。 |
| Svalbard telecom/cable policy | https://www.regjeringen.no/en/documents/meld.-st.-26-20232024/id3041130/?ch=4 | A 级。两条现有海缆由 Space Norway 拥有运营，关键基础设施；替代方案在推进。 |
| Longyearbyen energy | https://www.regjeringen.no/en/documents/meld.-st.-26-20232024/id3041130/?ch=4 | A 级。燃煤电厂 2023-10 关闭，转柴油并处于能源转型/冗余建设期；大规模 DC 电力声明必须高度怀疑。 |
| Cloud platforms | AWS/Azure/GCP/OCI 官方区域页 | A 级负向。无 SJ 区域；Azure Norway East/West 属挪威本土，不属于 SJ。 |

## 3. 行业搜索模板（Search templates）

### 3.1 运营方与设施发现（Operator and facility discovery）

```text
"KSAT" Svalbard ("SvalSat" OR "Svalbard Ground Station" OR antenna OR downlink OR "data")
"Svalbard Satellite Station" (antennas OR expansion OR capacity OR "data processing")
site:ksat.no (Svalbard OR SvalSat OR "Svalbard Ground Station")
"Space Norway" "Svalbard fibre" OR "Svalbard fiber"
site:spacenorway.com Svalbard (fibre OR fiber OR cable OR "co-location" OR hosting)
"Telenor Svalbard" (fiber OR fibre OR mobile OR network OR "Space Norway")
"Svalbard Undersea Cable" (capacity OR outage OR repair OR "fiber pairs" OR "fibre pairs")
"UNIS" Svalbard ("server" OR "data" OR "IT" OR "computing")
"Kjell Henriksen Observatory" ("data" OR server OR instruments)
"EISCAT" Svalbard ("data" OR processing OR radar)
"SIOS" Svalbard ("data management" OR storage OR infrastructure)
```

### 3.2 商业 DC 与项目状态（Commercial DC and project status）

```text
"Svalbard" ("data center" OR datacenter OR "server hall" OR serverhall OR datahall)
"Svalbard" (colocation OR "co-location" OR hosting OR "cloud region" OR hyperscale)
"Longyearbyen" ("data center" OR datacenter OR colocation OR hosting)
"Jan Mayen" ("data center" OR datacenter OR colocation OR hosting OR serverhall)
site:datacenterdynamics.com Svalbard
site:datacenterdynamics.com "Jan Mayen"
site:datacentermap.com Svalbard
site:baxtel.com Svalbard
site:cloudscene.com Svalbard
site:datacenters.com "Svalbard and Jan Mayen"
```

### 3.3 中文检索（Chinese-language searches）

```text
斯瓦尔巴 数据中心
斯瓦尔巴 托管 机房
斯瓦尔巴 卫星地面站 数据
斯瓦尔巴 海缆 光缆
朗伊尔城 数据中心
扬马延 数据中心
北极 数据中心 斯瓦尔巴
挪威 斯瓦尔巴 光缆 扬马延
```

### 3.4 云区域核查（Cloud-region checks）

```text
site:aws.amazon.com/about-aws/global-infrastructure "Svalbard"
site:learn.microsoft.com/en-us/azure/reliability/regions-list "Svalbard"
site:cloud.google.com/about/locations "Svalbard"
site:oracle.com/cloud/public-cloud-regions "Svalbard"
"Svalbard" "availability zone" OR "cloud region"
"Jan Mayen" "cloud region" OR "availability zone"
```

## 4. 重点实体处理规则（Entity handling rules）

### 4.1 KSAT SvalSat / Svalbard Ground Station

处理结论: `asset_class: satellite_ground_station`。

KSAT 的 Svalbard 站点是行业侧最强实体，也是最常见误报来源。官方/运营商来源确认其天线规模、卫星下行、数据传输和 Svalbard fibre 依赖关系，但没有证明它提供通用商业数据中心、colo、cloud region 或企业托管服务。即使页面出现 “commercial ground station” 或 “data downloading”，也只表示商业卫星地面站服务，不表示商业 DC。

建议记录字段:

```text
facility_name: SvalSat / Svalbard Ground Station
operator_legal_name: Kongsberg Satellite Services AS
repo_division: Svalbard and Jan Mayen
sub_area: Svalbard
settlement_or_site: Plataberget / Longyearbyen area
asset_class: satellite_ground_station
source_grade: A
status: operational
commercial_dc_status: absent / not a colocation data center
```

### 4.2 Space Norway fibre and hosting

处理结论:

- Svalbard fibre: `interconnection` / `telecom_subsea_fibre`
- Space Norway co-location page: `false_positive_for_SJ` unless a page explicitly places hosting in Svalbard or Jan Mayen

Space Norway 官方站同时有 Svalbard fibre 页面和 Nittedal Teleport 的 co-location/hosting 页面。核查者必须保持地点约束：Nittedal 位于挪威本土，不属于 SJ。不要把 Space Norway 的本土 teleport hosting 服务映射到 Svalbard。

### 4.3 Jan Mayen

处理结论: `commercial_dc: absent`。

Forsvaret 官方页显示 Jan Mayen 是小型工作站社会，含国防、气象、Galileo、通信、地震监测、燃料/应急功能。行业侧如果出现 “ground station”、“Galileo”、“Telenor Kystradio”、“meteorological data” 等词，应归入政府/导航/通信设施，而不是 DC。

### 4.4 Telenor Svalbard

处理结论: `telco_room` or `telecom_operator_lead` only。

行业搜索会出现 Telenor Svalbard、Telenor Satellite 与 Space Norway 的相关消息。2026-08-12 复核可确认：

- Space Norway 拥有/运营 Svalbard fibre（政府白皮书与 Space Norway 官方页）。
- Telenor/Space Norway 的卫星业务交易相关报道不可自动等同于 Telenor Svalbard 被转让。
- 未见 Nkom 商业 DC 登记中出现 Telenor Svalbard 或 Space Norway 的 SJ 数据中心条目。

如需记录 Telenor，必须只作为本地电信/网络机房线索，除非出现明确的 SJ 托管服务、Nkom 登记或设施页。

## 5. 云区域事实（Cloud-region facts）

2026-08-12 复核官方区域页:

- AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ - 无 Svalbard/Jan Mayen。
- Microsoft Azure: https://learn.microsoft.com/en-us/azure/reliability/regions-list - 无 Svalbard/Jan Mayen；Norway East/West 是挪威本土区域，不属于 SJ。
- Google Cloud: https://cloud.google.com/about/locations - 无 Svalbard/Jan Mayen。
- Oracle OCI: https://www.oracle.com/cloud/public-cloud-regions/ - 无 Svalbard/Jan Mayen。

规则: SaaS 可用性、CDN edge、卫星链路、客户所在地支持、国家下拉框均不能推断为云区域或本地数据中心。

## 6. 目录站与市场报告处理（Directories and market reports）

目录站核查顺序:

1. 记录站点 URL、检索日期、是否有具体设施名。
2. 若只有国家页、联系表单国家项或市场报告国家列表，标 `C` 并定性为 `no facility evidence`。
3. 若有设施名，查运营商官网、Nkom、Brønnøysund、Sysselmesteren/Lokalstyre。
4. 若设施实际是 KSAT/SvalSat、Space Norway fibre、科研站、种子库、Nittedal/挪威本土 DC，标 `false_positive`。

常见 false positives:

- “Svalbard and Jan Mayen” 出现在全球供应商表单国家列表。
- Space Norway “Co-location and Hosting” 位于 Nittedal Teleport，不在 SJ。
- “Svalbard data” 指卫星数据下行或科研数据门户。
- “Arctic data center” 指挪威本土或北欧其他地点。
- “Norway data center” 市场报告把 Norway 与 SJ 混用。

## 7. 行业工作流（Workflow）

1. 从 KSAT、Space Norway、Forsvaret、Nkom、云厂商官方页开始，记录 A 级正/负向事实。
2. 用第 3 节模板跑英文、挪威语、中文检索，捕获任何新增设施名。
3. 每个候选先定位坐标/行政归属；不在 Svalbard 或 Jan Mayen 的候选直接排除。
4. 对 SJ 内候选要求至少一条官方/运营商一手来源支持 `commercial_dc`，否则按实际资产类别记录。
5. 对 SvalSat/Jan Mayen ground station/科研设施/电信机房保留非 DC 记录，防止重复误报。
6. 输出时使用唯一 repo division `Svalbard and Jan Mayen`，并填 `sub_area`。

## 8. 最终判断模板（Bottom-line wording）

可用于枚举报告的结论:

```text
No verified commercial data center, colocation facility, hyperscale campus, or public cloud region was found in the SJ manifest division (Svalbard and Jan Mayen) as of 2026-08-12. Verified IT-intensive infrastructure consists of satellite ground stations (notably KSAT SvalSat), subsea fibre/telecom infrastructure (Space Norway Svalbard fibre), research IT/observatories, government monitoring facilities, and the Jan Mayen defence/meteorological/navigation station. These are classified outside commercial_dc.
```

中文结论:

```text
截至 2026-08-12，SJ 分区（Svalbard and Jan Mayen）未发现可验证商业数据中心、托管设施、hyperscale 园区或公有云区域。已核验的 IT 密集基础设施包括 KSAT SvalSat 卫星地面站、Space Norway 斯瓦尔巴海缆/通信基础设施、科研观测设施、政府监控设施，以及扬马延国防/气象/导航站点；这些均不得计入 commercial_dc。
```
