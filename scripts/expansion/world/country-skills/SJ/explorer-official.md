# SJ 官方渠道探索 - 斯瓦尔巴和扬马延数据中心枚举
# SJ Explorer Official - Svalbard and Jan Mayen Datacenter Enumeration

日期 Date: 2026-08-12。范围 Scope: 斯瓦尔巴和扬马延（Svalbard and Jan Mayen, SJ）。

清单确认 Manifest check: `world-manifest.jsonl` 中 SJ 的唯一分区为：

```json
{"country_code":"SJ","country_name":"Svalbard and Jan Mayen","subnational_type":"country","divisions":["Svalbard and Jan Mayen"]}
```

因此枚举输出只能使用 `repo_division: Svalbard and Jan Mayen`。方法论内部必须把该分区拆成两个审计子区域：`Svalbard` 与 `Jan Mayen`，分别做正向线索核查与负向枚举。

本文档为中文为主、英文/挪威语关键词为辅的双语方法论（Chinese-primary bilingual）。挪威语检索词保留原文。

## 1. 结论与可靠性（Conclusion and reliability）

核心结论 Core conclusion: 截至 2026-08-12，未发现 SJ 存在可验证的商业数据中心、托管数据中心、云区域或 hyperscale 项目。官方渠道能确认的 IT 密集实体是卫星地面站、科研/观测设施、政府设施、电信与海缆基础设施；这些实体不得升级为 `commercial_dc`。

特别注意 Special note: KSAT 的 SvalSat / Svalbard Ground Station 位于斯瓦尔巴，是世界级卫星地面站，含数据接收、传输与相关机房能力；它是 `satellite_ground_station`，不是商业数据中心。

可靠性分级 Reliability grades:

- **A 级 Grade A**: 官方/一手来源直接证明字段事实，例如 Sysselmesteren、Longyearbyen Lokalstyre、regjeringen.no、Lovdata、Nkom、Space Norway、Svalbard Energi/Longyearbyen energy documents、Statsbygg/Seed Vault、SSB、Statsforvalteren i Nordland、Met.no、Forsvaret、Brønnøysundregistrene。
- **B 级 Grade B**: 具名运营商、科研机构、行业媒体或主流媒体，能说明地点/主体/日期/状态，但未落到监管登记或许可。
- **C 级 Grade C**: 目录站、市场报告、供应商营销页、社交帖；仅作线索。
- **U 级 Unverified**: 页面打不开、无法二次确认，或只来自无法定位的转述。

分级纪律 Grading discipline:

- Nkom 数据中心登记可作为 A 级负向表面，但 Nkom 公表只列商业运营商；企业内部数据中心可能因安全原因不公开名称，且 0.5 MW 以下或不满足法规定义的内部机房不应推断为商业 DC。
- SvalSat、Jan Mayen Galileo ground station、UNIS/KHO/EISCAT/SIOS、Telenor/Space Norway 网络节点、种子库监控系统均不得因存在服务器、天线、NOC、数据传输或机架而计为商业 DC。

## 2. 已核验官方事实（Verified official facts）

### 2.1 行政与人口（Administration and population）

- **Svalbard**: 挪威主权和法律框架由《斯瓦尔巴条约》与《斯瓦尔巴法》构成；斯瓦尔巴总督府（Sysselmesteren på Svalbard）是挪威政府在群岛的代表。官方入口: https://www.sysselmesteren.no/en/ ；政府专题: https://www.regjeringen.no/en/topics/svalbard-and-polar-areas/svalbard/id87046/ ；Lovdata: https://lovdata.no/dokument/NL/lov/1925-07-17-11 与 https://lovdata.no/dokument/TRAKTAT/traktat/1920-02-09-1 。
- **Longyearbyen**: 地方服务、规划和基础设施由 Longyearbyen Lokalstyre 负责，规划面必须在 https://www.lokalstyre.no/ 与会议/规划文件中核查。
- **人口规模**: SSB 的 2026-03-03 Svalbard population 表显示 2026 年上半年 Longyearbyen + Ny-Alesund 为 2,512 人；SSB 页面还给出 Barentsburg/Hornsund 等定居点统计入口。来源: https://www.ssb.no/en/befolkning/folketall/statistikk/befolkningen-pa-svalbard 。
- **Jan Mayen**: Jan Mayen 是挪威极地岛屿，约 1000 km 离本土，几乎全岛为自然保护区；Statsforvalteren i Nordland 是自然保护区管理机构，且该岛不属于 Nordland 郡。来源: https://www.statsforvalteren.no/nordland/miljo-og-klima/nyheter---miljo-og-klima/2021/08/befaring-i-storslatt-og-unikt-landskap/ 。

### 2.2 法规与 Nkom 数据中心登记（Regulation and Nkom register）

- 挪威新的《电子通信法》(ekomloven, LOV-2024-12-13-76) 自 2025-01-01 生效，包含数据中心登记要求。Lovdata: https://lovdata.no/lov/2024-12-13-76 。
- `FOR-2024-12-13-3094` 明确规定 ekomloven 适用于 Svalbard，并相应适用于 Jan Mayen；Svalbard 对竞争章节有例外，但数据中心登记/安全框架不应默认排除。Lovdata: https://lovdata.no/dokument/SF/forskrift/2024-12-13-3094 。
- `datasenterforskriften` 自 2025-01-01 生效，规定数据中心运营商登记、安全、风险评估、应急等要求。Lovdata: https://lovdata.no/dokument/SF/forskrift/2024-12-18-3313 ；政府新闻: https://www.regjeringen.no/no/aktuelt/ny-datasenterforskrift/id3080690/ 。
- Nkom 公表说明：商业数据中心必须登记，内部数据中心在订购电力超过 0.5 MW 时登记；为安全与应急原因，内部数据中心名称和细节不公开。Nkom 页面 2026-08-11 更新，列 115 个注册数据中心、61 个商业运营商。来源: https://nkom.no/datasenter/oversikt 。
- 2026-08-12 复核 Nkom 页面和 CSV 时，未见 `Svalbard`、`Jan Mayen`、`Longyearbyen`、`9171`、`9173`、`9178`、`8099`、`KSAT`、`Telenor`、`Space Norway` 条目。记录为 A 级负向表面，不等同于证明所有内部机房不存在。

### 2.3 通信与海缆（Telecom and subsea fibre）

- Svalbard 与本土由两条海底光缆连接；政府 2024 Svalbard white paper 称其为关键基础设施，Space Norway 拥有并运营，2004 年投运，预计技术寿命至 2028 年底；2022 年一条电缆受损后已修复并重新运行。来源: https://www.regjeringen.no/en/documents/meld.-st.-26-20232024/id3041130/?ch=4 。
- Space Norway 官方页确认 Svalbard fibre 为双光缆、约 1400 km、8 对光纤，支持 Longyearbyen、科研、政府和 SvalSat 下行数据传输；当前服务保证至 2028，并正在推进新光缆方案，延伸考虑 Jan Mayen。来源: https://spacenorway.com/satellite-connectivity-solutions/fibre-connectivity/svalbard-fibre/ 与 https://spacenorway.com/infrastructure/subsea-fibre-cables/fibre-optic-cables/ 。
- 这些通信事实是互连基础设施证据，不是商业数据中心证据。

### 2.4 能源约束（Energy constraints）

- Longyearbyen 燃煤电厂已于 2023-10 关闭，随后转向柴油供热/供电；2024 年政府文件记录柴油机问题、军方发电机临时投入、Lunckefjell 旧矿业柴油机接入以提高安全供给，以及长期转向更多可再生能源仍需大量工作。来源: https://www.regjeringen.no/en/documents/meld.-st.-26-20232024/id3041130/?ch=4 。
- 该能源系统为偏远社区级关键基础设施，政府同时强调不应促成需要重大新增基础设施投资的发展。任何 `X MW data center in Svalbard` 声明都必须先用能源规划、Svalbard Energi/Longyearbyen Lokalstyre 文件与政府文件交叉核验。

### 2.5 卫星、科研与政府设施（Satellite, research, government facilities）

- **KSAT/SvalSat**: KSAT 官方历史页确认 Svalbard Satellite Station 于 1997 年建立，KSAT 由 Space Norway AS 与 Kongsberg Defence & Aerospace AS 各持 50%。来源: https://www.ksat.no/about-us/ 。KSAT 新闻显示 2021 年 Svalbard Ground Station 装上高原第 100 个天线；2025 年相关页面称站点接近 200 个天线。来源: https://www.ksat.no/news/news-archive/2021/ksat-has-installed-antenna-number-100-at-svalbard-ground-station/ 与 https://www.ksat.no/news/news-archive/20152/ksat-svalbard-ground-station-in-mission-impossible2/ 。
- **SvalSat 扩张**: 2024 Svalbard white paper 称 SvalSat 未来数年有每年扩 10-15 个天线的目标，扩建需相关主管机关授权。来源: https://www.regjeringen.no/en/documents/meld.-st.-26-20232024/id3041130/?ch=4 。
- **Jan Mayen station**: Forsvaret 官方页确认 Jan Mayen 有一个小型站点，常年 17 人，其中 15 人为 Forsvaret，2 人为 Meteorologisk institutt；站点包含天气观测、Galileo 地面站、地震传感器、Telenor Kystradio 基站等。来源: https://www.forsvaret.no/jobb/jan-mayen 。
- **Seed Vault**: Svalbard Global Seed Vault 官方页为种子长期储存设施入口；若出现监控、安防、数据记录系统，只能记 `government_monitoring`。来源: https://www.seedvault.no/ 。

## 3. 官方入口与查询模板（Official surfaces and query templates）

### 3.1 Svalbard 官方面（Official surfaces）

优先入口:

- Sysselmesteren: https://www.sysselmesteren.no/ 与 https://www.sysselmesteren.no/en/
- Longyearbyen Lokalstyre: https://www.lokalstyre.no/
- Regjeringen Svalbard white paper/topic: https://www.regjeringen.no/en/documents/meld.-st.-26-20232024/id3041130/ 与 https://www.regjeringen.no/en/topics/svalbard-and-polar-areas/svalbard/id87046/
- Lovdata: Svalbard Act, Svalbard Environmental Protection Act, Svalbard Treaty, ekomloven, datasenterforskriften
- Nkom register: https://nkom.no/datasenter/oversikt
- Space Norway Svalbard fibre: https://spacenorway.com/satellite-connectivity-solutions/fibre-connectivity/svalbard-fibre/
- SSB Svalbard population: https://www.ssb.no/en/befolkning/folketall/statistikk/befolkningen-pa-svalbard
- Brønnøysundregistrene: https://www.brreg.no/ and https://data.brreg.no/enhetsregisteret/oppslag

查询模板:

```text
site:sysselmesteren.no (datasenter OR serverhall OR datahall OR kolokasjon)
site:sysselmesteren.no (byggetillatelse OR byggesak OR arealplan OR tillatelse) (data OR server OR telekom OR satellitt)
site:lokalstyre.no (datasenter OR serverhall OR datahall OR kolokasjon)
site:lokalstyre.no (arealplan OR reguleringsplan OR byggesak OR møteprotokoll) (data OR IT OR telekom OR næring)
site:regjeringen.no Svalbard (datasenter OR ekomloven OR fiber OR satellitt OR "kritisk infrastruktur")
site:nkom.no Svalbard (datasenter OR ekomloven)
site:brreg.no OR site:data.brreg.no (Longyearbyen OR "9171" OR "9173" OR "9178") ("63.11" OR databehandling OR hosting OR datasenter)
```

### 3.2 Jan Mayen 官方面（Official surfaces）

优先入口:

- Statsforvalteren i Nordland Jan Mayen: https://www.statsforvalteren.no/nordland/
- Forsvaret Jan Mayen: https://www.forsvaret.no/jobb/jan-mayen
- Meteorologisk institutt: https://www.met.no/
- Lovdata Jan Mayen administration/nature reserve: https://lovdata.no/dokument/SF/forskrift/1980-11-21-12 与 https://lovdata.no/dokument/SFE/forskrift/2010-11-19-1456

查询模板:

```text
site:statsforvalteren.no/nordland "Jan Mayen" (forvaltning OR naturreservat OR tillatelse OR inngrep)
site:forsvaret.no "Jan Mayen" (stasjon OR kommunikasjon OR Galileo OR Telenor OR Kystradio)
site:met.no "Jan Mayen" (meteorologisk OR værstasjon OR Olonkinbyen)
"Jan Mayen" (datasenter OR "data center" OR serverhall OR hosting OR colocation)
```

## 4. 分区枚举策略（Per-division enumeration strategy）

### 4.1 Repo division: Svalbard and Jan Mayen

输出中只能保留一个仓库分区字段:

```text
repo_division: Svalbard and Jan Mayen
sub_area: Svalbard | Jan Mayen
```

最小字段 Minimum fields:

```text
facility_name
operator_legal_name
org_number
repo_division: Svalbard and Jan Mayen
sub_area: Svalbard | Jan Mayen
settlement_or_site: Longyearbyen | Ny-Alesund | Barentsburg | Plataberget | Olonkinbyen | other
asset_class: commercial_dc | satellite_ground_station | research_it | government_monitoring | telco_room | cloud_region | false_positive | absent
source_grade: A | B | C | U
source_url
source_date
status: proposed | permitted | under_construction | operational | dormant | withdrawn | absent
power_mw_type / power_mw_value
notes
```

### 4.2 Svalbard 子区域

预期结果: 商业 DC 负向；地面站/科研/政府/电信正向分类。

步骤:

1. 查 Nkom register 和 CSV，过滤 Svalbard/Longyearbyen/postcodes/已知主体。
2. 查 Brønnøysund：地址 `9171 Longyearbyen`, `9173 Ny-Alesund`, `9178 Barentsburg`, `9172 Sveagruva`；NACE 63.11、61、62。
3. 查 Sysselmesteren 和 Longyearbyen Lokalstyre 的规划、建筑、环境许可。
4. 对 SvalSat/KSAT、Space Norway fibre、UNIS、KHO、EISCAT、SIOS、Seed Vault、Telenor/电信节点逐条分类。
5. 用能源与海缆官方事实检查任何 MW、容量、可靠性或新建声明。

### 4.3 Jan Mayen 子区域

预期结果: 纯负向控制（negative control）。

步骤:

1. 用 Statsforvalteren、Forsvaret、Met.no、Lovdata 确认设施面只涉及自然保护区管理、气象、国防/通信/导航、应急。
2. 检索数据中心/服务器/托管/云关键词。
3. 若出现 Galileo/Telenor Kystradio/地震传感器/气象系统，分类为 `government_monitoring`、`telco_room` 或 `satellite_ground_station`，不得计为 commercial DC。

## 5. 云区域与目录站负向核查（Cloud and directory negative checks）

官方云区域页每次运行都要重查:

```text
site:aws.amazon.com/about-aws/global-infrastructure "Svalbard"
site:learn.microsoft.com/en-us/azure/reliability/regions-list "Svalbard"
site:cloud.google.com/about/locations "Svalbard"
site:oracle.com/cloud/public-cloud-regions "Svalbard"
```

2026-08-12 复核结果: AWS、Azure、Google Cloud、Oracle OCI 官方区域页均无 `Svalbard`；Azure 仅列 Norway East/West，位于挪威本土，不属于 SJ。官方区域页:

- AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud: https://cloud.google.com/about/locations
- Oracle OCI: https://www.oracle.com/cloud/public-cloud-regions/

目录站只作 C 级线索:

```text
site:datacentermap.com Svalbard
site:baxtel.com Svalbard
site:cloudscene.com Svalbard
site:datacenters.com "Svalbard and Jan Mayen"
```

常见误报:

- 联系表单国家下拉项含 “Svalbard and Jan Mayen” 不代表有设施。
- Space Norway `Co-location and Hosting` 指 Nittedal Teleport（挪威本土），不是 SJ。
- Norway 北部/北极营销项目如 Lefdal、Glomfjord、Tydal、Tromso 不得映射到 SJ。

## 6. 最终核查清单（Final checklist）

每次枚举运行前后记录以下结果:

1. Manifest: `divisions` 是否仍为 `["Svalbard and Jan Mayen"]`。
2. Nkom: 页面更新日期、商业运营商表是否有 Svalbard/Jan Mayen 地址或已知主体。
3. Brønnøysund: Svalbard 地址 + NACE 63.11/61/62 是否出现新公司。
4. Sysselmesteren/Lokalstyre: 是否有数据中心、serverhall、datahall、telekom、satellitt 相关建设/许可。
5. SvalSat: 新天线/新机房/扩建是否仍属地面站授权。
6. Space Norway: Svalbard fibre 当前状态、2028 后替代/新缆项目、是否涉及 Jan Mayen。
7. Energy: Longyearbyen 能源转型、柴油/可再生状态、是否有新增大负荷许可。
8. Cloud: AWS/Azure/GCP/OCI 官方区域是否仍无 SJ。
9. Jan Mayen: Forsvaret/Met.no/Statsforvalteren 是否仍仅显示国防、气象、导航/通信、自然保护区管理。
10. False positives: 地面站、科研机房、政府监控、种子库、电信机房、挪威本土北极项目是否被错误计为 DC。

底线 Bottom line: SJ 的官方枚举结果应为 `commercial_dc: absent`，同时保留 SvalSat/SGS、Space Norway fibre、Jan Mayen station、科研/政府/电信设施的非 DC 分类记录。
