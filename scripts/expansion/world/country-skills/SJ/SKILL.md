---
name: sj-datacenter-methodology
location: scripts/expansion/world/country-skills/SJ/SKILL.md
description: 斯瓦尔巴和扬马延数据中心发现与审计方法论（bilingual）。Svalbard and Jan Mayen datacenter discovery & audit methodology: verified negative for commercial DC — enumerate the official/regulatory/cloud pipeline (Sysselmesteren, Longyearbyen Lokalstyre, regjeringen.no white paper, Lovdata ekomloven/datasenterforskriften, Nkom register, Brønnøysund, SSB population, Space Norway Svalbard fibre, Statsforvalteren/Forsvaret/Met.no Jan Mayen, hyperscaler-absence checks) plus industry/trade-press discovery (KSAT SvalSat, UNIS/KHO/EISCAT/SIOS research, Seed Vault, directories). Division model: single repo division Svalbard and Jan Mayen with sub_areas Svalbard/Jan Mayen. Read before running SJ exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# SJ · 斯瓦尔巴和扬马延数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：斯瓦尔巴和扬马延（SJ）截至 2026-08-12 官方与行业双线结论均为 **verified negative**：未发现可验证的商业数据中心、托管数据中心、云区域或 hyperscale 项目。官方渠道能确认的 IT 密集实体是卫星地面站（KSAT SvalSat）、科研/观测设施（UNIS/KHO/EISCAT/SIOS）、政府设施（Seed Vault）、电信与海缆基础设施（Space Norway Svalbard fibre）、扬马延国防/气象/导航站——这些实体一律不得升级为 `commercial_dc`。本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双线交叉验证，以 Nkom 数据中心登记为 A 级负向表面、Sysselmesteren/Lokalstyre/regjeringen/Lovdata 主证。本 skill 汇总两份最终审定的探索报告，作为 SJ 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | Sysselmesteren（总督府）、Longyearbyen Lokalstyre（规划/基建）、regjeringen.no Svalbard white paper、Lovdata（Svalbard 法/ekomloven/datasenterforskriften）、Nkom 数据中心登记、Space Norway Svalbard fibre、SSB 人口、Brønnøysund 企业登记、Statsforvalteren i Nordland/Forsvaret/Met.no（Jan Mayen）、云区域缺失检查 |
| explorer-industry.md | 行业/厂商发现 | KSAT SvalSat/Svalbard Ground Station、Space Norway（含 Nittedal Teleport false-positive 规则）、Telenor Svalbard、UNIS/KHO/EISCAT/SIOS 科研设施、Seed Vault、Nkom/目录站核验流程、中文/挪威语检索模板 |

## 核心结构事实

1. **行政区划模型**：manifest 为 `subnational_type: country`，**单一 repo division `Svalbard and Jan Mayen`**；输出只能使用该 division，方法论内部分拆为两个审计子区域 `sub_area: Svalbard | Jan Mayen`，分别做正向线索核查与负向枚举；定居点字段 settlement_or_site：Longyearbyen | Ny-Alesund | Barentsburg | Plataberget | Olonkinbyen 等。
2. **注册库现状**：**挪威新《电子通信法》（ekomloven, LOV-2024-12-13-76）自 2025-01-01 生效，含数据中心登记要求**；`FOR-2024-12-13-3094` 明确 ekomloven 适用于 Svalbard 并相应适用于 Jan Mayen（竞争章节有例外，但数据中心登记/安全框架不默认排除）；**datasenterforskriften（FOR-2024-12-18-3313）自 2025-01-01 生效**，规定运营商登记、安全、风险评估、应急要求。**Nkom 公表（nkom.no/datasenter/oversikt，2026-08-11 更新）列 115 个注册数据中心、61 个商业运营商；商业 DC 必须登记，内部 DC 在电力订购超 0.5 MW 时登记且名称/细节可能因安全原因不公开**；2026-08-12 复核页面与 CSV 未见 `Svalbard`/`Jan Mayen`/`Longyearbyen`/`9171`/`9173`/`9178`/`8099`/`KSAT`/`Telenor`/`Space Norway` 条目——记录为 A 级负向表面，不等同于证明所有内部机房不存在。
3. **法律与监管**：Svalbard 主权与法律框架由《斯瓦尔巴条约》与《斯瓦尔巴法》构成；Sysselmesteren（sysselmesteren.no）是挪威政府在群岛的代表；Longyearbyen Lokalstyre（lokalstyre.no）负责地方服务、规划和基础设施——规划面必须在其中核验；Lovdata：Svalbard Act、Svalbard Environmental Protection Act、Svalbard Treaty、ekomloven、datasenterforskriften；Jan Mayen 由 Statsforvalteren i Nordland 管理自然保护、Forsvaret 运行站点（常年 17 人：15 Forsvaret + 2 Meteorologisk institutt），站点含气象观测、Galileo 地面站、地震传感器、Telenor Kystradio 基站。
4. **互联与云**：**Svalbard 与本土由两条海底光缆连接**——政府 2024 Svalbard white paper 称之为关键基础设施，Space Norway 拥有并运营，2004 年投运，技术寿命预计至 2028 年底；Space Norway 官方页确认双光缆、约 1400 km、8 对光纤，支持 Longyearbyen/科研/政府/SvalSat 下行数据传输，正在推进新光缆方案并延伸考虑 Jan Mayen——互联基础设施证据，非商业 DC 证据；**AWS/Azure/GCP/OCI 官方区域页均无 Svalbard**——Azure 仅列 Norway East/West（挪威本土，不属于 SJ）。
5. **设施/项目种子（2026-08 证据状态）**：**KSAT SvalSat / Svalbard Ground Station**（Plataberget/Longyearbyen 附近；1997 年建站，2021 年高原第 100 个天线，2025 年近 200 个天线；KSAT 由 Space Norway AS 与 Kongsberg Defence & Aerospace AS 各持 50%）——`satellite_ground_station`，即使出现 "commercial ground station"/"data downloading" 也只表示商业卫星地面站服务，非商业 DC；**Space Norway Svalbard fibre**——`interconnection`/`telecom_subsea_fibre`；**Space Norway Co-location and Hosting 页**——地点是 Nittedal Teleport（挪威本土），对 SJ 记 false positive；**Jan Mayen station**——Forsvaret/Met.no 站点（国防/气象/Galileo/通信/地震监测/燃料应急），`commercial_dc: absent`，出现 ground station/Galileo/Kystradio/meteorological data 词归政府/导航/通信设施；**UNIS/KHO/EISCAT/SIOS**——`research_it`；**Seed Vault**——`government_monitoring`；**Telenor Svalbard**——仅 `telco_room`/`telecom_operator_lead`（卫星业务交易报道不得自动等同于 Telenor Svalbard 转让）。
6. **语言与词汇**：挪威语检索词保留原文——datasenter、serverhall、datahall、kolokasjon、byggetillatelse、byggesak、arealplan、reguleringsplan、møteprotokoll、kritisk infrastruktur、satellitt；中文监控：斯瓦尔巴（数据中心/托管/机房/卫星地面站/海缆/光缆）、朗伊尔城（数据中心）、扬马延（数据中心）、北极（数据中心 斯瓦尔巴）；NACE 63.11/61/62 + Svalbard 邮编 9171/9173/9178/9172 用于 Brønnøysund 企业扫描。
7. **可靠性分级**：A = 官方/一手（Sysselmesteren、Longyearbyen Lokalstyre、regjeringen.no、Lovdata、Nkom、Space Norway、Svalbard Energi/Longyearbyen energy documents、Statsbygg/Seed Vault、SSB、Statsforvalteren i Nordland、Met.no、Forsvaret、Brønnøysundregistrene、运营商官方页、云厂商官方区域页）；B = 具名运营商/科研机构/行业媒体/主流媒体，能说明地点/主体/日期/状态但未落到监管登记或许可；C = 目录站、市场报告、供应商营销页、社交帖——仅作线索；U = 页面打不开、无法二次确认或只来自无法定位的转述。
8. **计数与去重规则**：**asset_class 精确**（commercial_dc、satellite_ground_station、research_it、government_monitoring、telco_room、cloud_region、false_positive、absent）；SvalSat/Jan Mayen ground station/科研设施/电信机房/种子库监控不得因存在服务器、天线、NOC、数据传输或机架而计为商业 DC；Nkom 公表只列商业运营商，企业内部 DC 可能因安全不公开名称且 0.5 MW 以下或不满足法规定义的内部机房不应推断为商业 DC；目录站只作 C 级线索（常见误报：国家下拉框、Space Norway Nittedal、挪威本土北极营销项目 Lefdal/Glomfjord/Tydal/Tromso）；任何 "X MW data center in Svalbard" 声明必须先用能源规划、Svalbard Energi/Longyearbyen Lokalstyre 文件与政府文件交叉核验。

## 常用查询模板

```text
site:sysselmesteren.no (datasenter OR serverhall OR datahall OR kolokasjon)
site:sysselmesteren.no (byggetillatelse OR byggesak OR arealplan OR tillatelse) (data OR server OR telekom OR satellitt)
site:lokalstyre.no (datasenter OR serverhall OR datahall OR kolokasjon)
site:lokalstyre.no (arealplan OR reguleringsplan OR byggesak OR møteprotokoll) (data OR IT OR telekom OR næring)
site:regjeringen.no Svalbard (datasenter OR ekomloven OR fiber OR satellitt OR "kritisk infrastruktur")
site:nkom.no Svalbard (datasenter OR ekomloven)
site:brreg.no OR site:data.brreg.no (Longyearbyen OR "9171" OR "9173" OR "9178") ("63.11" OR databehandling OR hosting OR datasenter)
site:statsforvalteren.no/nordland "Jan Mayen" (forvaltning OR naturreservat OR tillatelse OR inngrep)
site:forsvaret.no "Jan Mayen" (stasjon OR kommunikasjon OR Galileo OR Telenor OR Kystradio)
site:met.no "Jan Mayen" (meteorologisk OR værstasjon OR Olonkinbyen)
"Jan Mayen" (datasenter OR "data center" OR serverhall OR hosting OR colocation)
"KSAT" Svalbard ("SvalSat" OR "Svalbard Ground Station" OR antenna OR downlink OR "data")
site:ksat.no (Svalbard OR SvalSat OR "Svalbard Ground Station")
"Space Norway" "Svalbard fibre" OR "Svalbard fiber" ; site:spacenorway.com Svalbard (fibre OR cable OR "co-location" OR hosting)
"Svalbard Undersea Cable" (capacity OR outage OR repair OR "fiber pairs") ; "Telenor Svalbard" (fiber OR network)
"UNIS" Svalbard ("server" OR "data" OR "IT" OR "computing") ; "Kjell Henriksen Observatory" ("data" OR server)
"EISCAT" Svalbard ("data" OR processing OR radar) ; "SIOS" Svalbard ("data management" OR storage)
"Svalbard" ("data center" OR datacenter OR "server hall" OR serverhall OR datahall)
"Svalbard" (colocation OR "co-location" OR hosting OR "cloud region" OR hyperscale)
"Longyearbyen" ("data center" OR datacenter OR colocation OR hosting) ; "Jan Mayen" ("data center" OR hosting)
site:datacenterdynamics.com Svalbard ; site:datacenterdynamics.com "Jan Mayen"
site:datacentermap.com Svalbard ; site:baxtel.com Svalbard ; site:cloudscene.com Svalbard
site:datacenters.com "Svalbard and Jan Mayen"
斯瓦尔巴 数据中心 ; 斯瓦尔巴 托管 机房 ; 斯瓦尔巴 卫星地面站 数据 ; 斯瓦尔巴 海缆 光缆
朗伊尔城 数据中心 ; 扬马延 数据中心 ; 北极 数据中心 斯瓦尔巴
site:aws.amazon.com/about-aws/global-infrastructure "Svalbard" ; site:learn.microsoft.com/en-us/azure/reliability/regions-list "Svalbard"
site:cloud.google.com/about/locations "Svalbard" ; site:oracle.com/cloud/public-cloud-regions "Svalbard"
"Svalbard" "availability zone" OR "cloud region" ; "Jan Mayen" "cloud region" OR "availability zone"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **行政与人口**：Sysselmesteren（`sysselmesteren.no/en/`）为总督府入口；Longyearbyen Lokalstyre（`lokalstyre.no`）负责地方服务/规划/基建，规划面必须在其会议/规划文件中核验；regjeringen.no Svalbard white paper（meld. St. 26 2023-2024）为政府文件主源；SSB Svalbard 人口表（2026-03-03：2026 上半年 Longyearbyen + Ny-Alesund 2,512 人；Barentsburg/Hornsund 等定居点统计入口）；Brønnøysundregistrene（`brreg.no` / `data.brreg.no`）企业登记——Svalbard 邮编 9171/9173/9178/9172 + NACE 63.11/61/62。
- **法规与 Nkom 登记**：ekomloven（LOV-2024-12-13-76）2025-01-01 生效含数据中心登记；FOR-2024-12-13-3094 将 ekomloven 适用于 Svalbard/Jan Mayen；datasenterforskriften（FOR-2024-12-18-3313）2025-01-01 生效（登记/安全/风险评估/应急）；Nkom `nkom.no/datasenter/oversikt` 为 A 级负向表面——每批次记录页面更新日期、商业运营商表是否有 Svalbard/Jan Mayen 地址或已知主体；公表只列商业运营商，内部 DC 0.5 MW 以上登记但名称可能不公开。
- **通信与海缆**：Svalbard 双海缆为关键基础设施（Space Norway 拥有运营，2004 投运，服务保障至 2028，新方案在推进并考虑 Jan Mayen）；2022 年一条电缆受损后已修复重新运行——通信事实是互联基建证据，不是商业 DC 证据。
- **能源约束**：Longyearbyen 燃煤电厂 2023-10 关闭，转柴油供热/供电；2024 政府文件记录柴油机问题、军方发电机临时投入、Lunckefjell 旧矿业柴油机接入提高安全供给、长期转更多可再生能源仍需大量工作——偏远社区级关键基础设施，政府同时强调不应促成需重大新增基建投资的发展；任何 MW 级声明必须先交叉核验能源规划/Svalbard Energi/Lokalstyre 与政府文件。
- **云区域缺失**：每批次重查 AWS/Azure/GCP/OCI 官方区域页；2026-08-12 复核均无 `Svalbard`；Azure 仅列 Norway East/West（挪威本土，不属 SJ）；SaaS 可用性、CDN edge、卫星链路、客户所在地支持、国家下拉框均不能推断为云区域或本地数据中心。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **已验证实体图谱**：KSAT SvalSat/Svalbard Ground Station（A 级地面站存在，1997 建站/2021 第 100 天线/2025 近 200 天线；所有权 Space Norway 50% + Kongsberg 50%；分类 satellite_ground_station，记录字段含 facility_name/operator_legal_name: Kongsberg Satellite Services AS/sub_area: Svalbard/settlement: Plataberget）；Space Norway Svalbard fibre（A 级互联基建）；Space Norway co-location 页（A 级主体页但地点 Nittedal Teleport，SJ false positive）；Nkom register（A 级监管负向）；Jan Mayen station（A 级，17 人常驻）；Telenor Svalbard（仅 telco_room/lead，除非出现明确 SJ 托管服务、Nkom 登记或设施页）。
- **搜索与核验**：任何 "Svalbard data center" 线索必须回答：是否提供面向第三方客户的付费数据中心/托管服务？是否有 Nkom/许可/企业登记/运营商设施页？答案是否则不得计为商业 DC；每个候选先定位坐标/行政归属，不在 Svalbard 或 Jan Mayen 的直接排除；对 SJ 内候选要求至少一条官方/运营商一手来源支持 `commercial_dc`，否则按实际资产类别记录；输出使用唯一 repo division `Svalbard and Jan Mayen` 并填 `sub_area`。
- **目录站处理**：只作 C 级线索；若只有国家页/联系表单国家项/市场报告国家列表，标 C 并定性 `no facility evidence`；若有设施名，查运营商官网、Nkom、Brønnøysund、Sysselmesteren/Lokalstyre；若设施实际是 KSAT/SvalSat、Space Norway fibre、科研站、种子库、Nittedal/挪威本土 DC，标 `false_positive`。
- **诚实结论（2026-08）**：`commercial_dc: absent`；同时保留 SvalSat/SGS、Space Norway fibre、Jan Mayen station、科研/政府/电信设施的非 DC 分类记录，防止重复误报。

## 维护注意（更新纪律）

- **更新节奏**：每季度——Nkom 登记页/CSV（是否新增 Svalbard/Jan Mayen 主体）、Brønnøysund Svalbard 地址 + NACE 63.11/61/62 新公司、Sysselmesteren/Lokalstyre 建设/许可、云区域清单；每半年——regjeringen white paper/能源转型文件（Longyearbyen 柴油/可再生状态、是否有新增大负荷许可）、Space Norway Svalbard fibre 状态（2028 后替代/新缆项目、是否涉及 Jan Mayen）、SvalSat 新天线/新机房/扩建授权；每年——复查全部 C/U 级目录条目；事件驱动——任何 "Svalbard data center" 项目声明、新海缆、Jan Mayen 设施变化为最大变化。
- **来源核验**：逐一点击 A 级 URL；区分 Nkom 公表（商业运营商）与内部 DC（安全原因不公开名称）；Space Norway `Co-location and Hosting` 页面必须核对地点（Nittedal ≠ SJ）；挪威本土北极营销项目（Lefdal、Glomfjord、Tydal、Tromso）不得映射到 SJ。
- **不删除纪律（no-deletion）**：已核实记录不得删除；状态变化改标并保留原始证据链；无支撑条目降级为 C/U 保留而非移除；负向检索（商业 DC 缺失）须如实记录而非跳过。
