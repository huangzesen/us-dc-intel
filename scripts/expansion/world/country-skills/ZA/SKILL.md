---
name: za-datacenter-methodology
location: scripts/expansion/world/country-skills/ZA/SKILL.md
description: |
  South Africa (ZA) datacenter discovery & audit methodology. No national registry; enumeration is a municipality-first land-use/building-control exercise under SPLUMA with Municipal Planning Tribunals (MPTs), backed by environmental authorisations (DFFE/NEAS/EGIS, provincial departments), power records (Eskom/NERSA/municipal electricity, MVA/substation/wheeling), telecoms (ICASA), official cloud regions (AWS af-south-1 Cape Town, Azure South Africa North/ Johannesburg + West/ Cape Town, Google africa-south1 Johannesburg, OCI af-johannesburg-1), and operator pages (Teraco/Digital Realty, Africa Data Centres/Cassava/Liquid, Equinix JN1 + Cape Town, Vantage JNB1/JNB2, OADC/WIOCC, NTT/Dimension Data, BCX/Telkom, Digital Parks Africa). Division model: province - district/metropolitan municipality (52 divisions). Read this before running ZA exploration/audit batches. Routes to explorer-official.md (planning/environment/power/cloud) and explorer-industry.md (press/vendor/district matrix).
---
# ZA · 南非数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为南非数据中心枚举提供「市镇土地用途/建筑许可 + 环评 + 电力 + 云区域 + 运营商官网」五线并联的查询框架。南非**没有全国性数据中心注册库，也没有全国规划许可库**，枚举本质是**以市镇（municipality）为单位的土地用途/建筑管控作业**：在 SPLUMA（空间规划与土地用途管理法）框架下，市镇须设 Municipal Planning Tribunal（MPT）或同级决策机构，A 级证据通常是市镇议程/审裁报告/决议通知/分区批复/建筑图批复/Site Development Plan/上诉记录。**实际搜索单位是都会区/地方市镇而非省份**；电力（Eskom/NERSA/市镇电力局）是核心过滤器。市场高度集中于**豪登省与西开普省**（约翰内斯堡/Midrand/Isando/Bredell/Waterfall City/Samrand/Centurion、开普敦/Rondebosch/Brackenfell/King Air Industria、德班/Riverhorse Valley）。本 skill 汇总两份探索报告（官方管线 + 行业发现），供南非探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：市镇规划门户（Cape Town Planning Portal/DAMS/MPT、Joburg eServices、eThekwini LUMS、Tshwane NAPS、Ekurhuleni）、DFFE/NEAS/EGIS 环评、Eskom/NERSA/市镇电力、ICASA、官方云区域页、运营商官网 |
| `explorer-industry.md` | 行业/厂商发现：DCD/MyBroadband/TechCentral/ITWeb/Daily Maverick/GroundUp 等媒体、运营商/开发商矩阵、省级与区级枚举矩阵、已知高优先线索 |

## 核心结构事实（框定每次搜索）

1. **市镇优先（municipality-first）**：SPLUMA 框架下土地用途决定走市镇规划系统；A 级证据=市镇 MPT/委员会议程或决议、分区（rezoning）、subdivision/consolidation、consent use、Site Development Plan、建筑图批复、上诉记录。高产出都会区：Cape Town（Planning Portal https://www.capetown.gov.za/Work%20and%20business/Planning-portal + DAMS + MPT 会议 https://web1.capetown.gov.za/web1/councilhubonline/mptmeetingdetail）、Johannesburg（eServices 建筑图 https://eservices.joburg.org.za/pages/BuildingPlanProgress.aspx）、eThekwini（LUMS adverts https://www.durban.gov.za/page/lums-adverts）、Tshwane（NAPS 2024-12 起线上建筑图）、Ekurhuleni（Isando/Germiston/Bredell 关键）。
2. **环评触发词不含「data centre」类别**：通过土地改造、水、列名活动、柴油储存、备用发电、燃料处理等触发。DFFE https://www.dffe.gov.za/、NEAS https://neas.environment.gov.za/dea_neas/、EGIS https://www.dffe.gov.za/egis；省级环保厅按省（Western Cape DEA&DP、Gauteng GDARDE、KZN EDTEA 等）。环评从业者（EAP）公开参与页是 B+ 线索（Basic Assessment Report/EIA/专家研究），A 级仅限政府签发的授权书或官方托管文件。
3. **电力是核心过滤器**：Eskom https://www.eskom.co.za/ + Data Portal https://www.eskom.co.za/dataportal/ + Transmission Development Plan（TDP，变电站/区域容量语境）；NERSA https://www.nersa.org.za/（发电注册、许可、wheeling、嵌入式发电、电价决定）；都会区市镇电力局（City Power Johannesburg、Cape Town Electricity、eThekwini Electricity、Ekurhuleni Energy）。A 级=NERSA 决定/注册、Eskom 文件、市镇电力报告、电费/连接记录、官方招标点名项目；B 级=「可再生能源将为云区域供电」的新闻（NERSA/Eskom 证据未开时）。**不要把可再生能源电站当作数据中心**。
4. **云区域 = 都会区种子，非精确设施**：AWS Africa (Cape Town) `af-south-1` 3 AZ（2020-04 开放）；Azure South Africa North（约翰内斯堡，AZ 支持）+ South Africa West（开普敦，成对/受限）；Google `africa-south1` 约翰内斯堡（zones a/b/c，非洲首个 GCP 区域）；OCI South Africa Central `af-johannesburg-1`（region key JNB，2022-01）；Huawei Cloud 南非区域（2018 公告，官网细节有限）；Alibaba/BCX 开普敦线索暂为 B。云区域只证明市场存在与地理，不披露具体建筑。
5. **拼写三变体**：南非常用 `data centre` 与 `datacentre`，美式 `data center` 常见于美资厂商页与 DCD，三种都要搜；另搜 `hyperscale`/`carrier-neutral`/`colocation`/`server farm`/`AI data centre`/`data storage centre`/`backup generators`/`diesel generators`/`substation`/`MVA`/`MW`/`critical IT load`/`rezoning`/`consent use`/`land-use application`/`site development plan`/`Municipal Planning Tribunal`。
6. **阿非利卡语用于乡村告示**：`datasentrum`（数据中心）、`hersonering`（分区）、`grondgebruik`（土地用途）、`bouplan`（建筑图）、`munisipale beplanningstribunaal`（市镇规划审裁）；西开普/北开普本地告示有用，商业发现基本不需要。
7. **阶段与单位陷阱**：`announced`/`MoU`/`considering`=线索（C/B-）；`land-use application`/`rezoning`/`tribunal approval`/`environmental authorisation`/`building plans submitted`=许可阶段（A，若为市镇/EIA 记录）；`breaks ground`/`construction starts`=施工（B 除非运营商/市镇确认）；`opened`/`goes live`/`facility page`=运营（A/B）。**开普敦批复是分阶段**：rezoning/subdivision/MPT 批准 ≠ 环评/建筑/运营完成；电力容量（MVA/电网进口/园区满配）与 IT 负载必须原样保留标签，不换算。**约翰内斯堡命名错配**：厂商常把所有豪登设施宣传为 Johannesburg，落 division 前必须解析精确地址属 City of Johannesburg / Ekurhuleni / Tshwane。

## 查询模式（复制粘贴模板见 explorer-official.md §5 与 explorer-industry.md §6）

- `"{municipality}" "data centre"` / `"{municipality}" datacentre` / `"{municipality}" "data center"`（三种拼写）
- `"{municipality}" "data centre" "Municipal Planning Tribunal"` / `"data centre" +"rezoning"` / `"data centre" +"site development plan"` / `"data centre" +"building plan"`
- `site:capetown.gov.za "data centre"` / `site:web1.capetown.gov.za "data centre"` / `site:joburg.org.za "data centre"` / `site:durban.gov.za "data centre"` / `site:ekurhuleni.gov.za "data centre"` / `site:tshwane.gov.za "data centre"`
- `"data centre" "environmental authorisation" "South Africa"` / `"data centre" "Basic Assessment Report"` / `"data centre" "diesel" "environmental authorisation"` / `site:dffe.gov.za "data centre"`
- `"{operator}" "Eskom" "data centre"` / `"{project}" "MVA"` / `"{project}" "substation" "data centre"` / `site:nersa.org.za "{operator}" "generation"`
- `site:icasa.org.za "rapid deployment" "data centre"` / `site:icasa.org.za "{operator}" "Electronic Communications Service"`
- `"datasentrum" ("Kaapstad" OR "Johannesburg")` / `"datasentrum" ("hersonering" OR "grondgebruik")`（阿非利卡语）
- 阶段词映射：announced/MoU=线索（C/B-）；rezoning/tribunal approval/EA/building plans submitted=许可（A 市镇/EIA 记录）；breaks ground=施工（B）；opened/goes live=运营（A/B）。

## 官方/监管管线要点（详见 explorer-official.md）

- **市镇规划/土地用途（A 级）**：Cape Town Planning Portal + Building-plan applications https://www.capetown.gov.za/City-Connect/Apply/Planning-building-and-development/Building-plan-applications + MPT meeting https://web1.capetown.gov.za/web1/councilhubonline/mptmeetingdetail + Planning By-law；Johannesburg eServices/BuildingPlanProgress；eThekwini https://www.durban.gov.za/（LUMS adverts、议会决议、电力年报）；Tshwane/Ekurhuleni/Nelson Mandela Bay/Mangaung/Buffalo City 直接扫。从市镇包提取：申请号、erf/farm/portion、街道/街区、所申请分区、申请人/地主/运营商、楼面、机房数、MVA/MW 电力需求、备用发电与柴油储存、水/冷却、环评触发、反对/上诉、决定日期与条件。已知高产出样例：2026 年开普敦 MPT 报道批准 King Air Industria（近开普敦国际机场）两座超大规模数据中心土地用途申请，媒体关联 Equinix；MPT 记录为 A，GroundUp/Business Day/News24/IOL 报道为 B 线索。
- **环评（A 级授权书）**：DFFE/NEAS/EGIS + 省级环保厅；搜索词 `data centre`+`environmental authorisation`/`Basic Assessment Report`/`NEMA`/`diesel`/`public participation`；提取 DFFE/省级参考号、列名活动、项目发起人、坐标/erf、柴油储量、发电机组数/额定、水源、污水方案、生物多样性约束、上诉状态。
- **电力（A 级）**：Eskom/NERSA/市镇电力；`"{operator}" "Eskom" "data centre"`、`"{project}" "MVA"`、`"{project}" "substation"`、`"{operator}" "NERSA" "generation registration"`、`site:eskom.co.za "data centre"`、`site:nersa.org.za "data centre"`；132kV/88kV 连接、wheeling、嵌入式发电、太阳能+NERSAA。
- **ICASA（电信语境，非设施注册库）**：https://www.icasa.org.za/（授权、公众咨询、频谱/站点、快速部署法规 2026 草案含被动基础设施 GIS 申报）；用于向数据中心周边光纤/网络商 pivoting：Openserve/Telkom、DFA、Liquid、Vodacom Business、MTN、Frogfoot、Vumatel/Dark Fibre Africa、Seacom、WIOCC/OADC。
- **云区域页**：AWS https://aws.amazon.com/local/africa/ + https://aws.amazon.com/local/africa/cape-town/ + https://aws.amazon.com/blogs/aws/now-open-aws-africa-cape-town-region/（af-south-1）；Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list（SA North JHB / SA West CPT 成对受限）；GCP https://cloud.google.com/about/locations + https://docs.cloud.google.com/compute/docs/regions-zones + https://cloud.google.com/blog/products/infrastructure/heita-south-africa-new-cloud-region（africa-south1）；OCI https://www.oracle.com/news/announcement/oracle-cloud-johannesburg-region-2022-01-19/ + https://docs.oracle.com/iaas/releasenotes/changes/8b70bb98-9542-4dae-92d9-8d3f05cc8417/index.htm（af-johannesburg-1，JNB）；Huawei https://www.huawei.com/en/news/2018/11/huawei-cloud-south-africa-connected-intelligent。
- **运营商官方页（A 级存在性）**：Teraco/Digital Realty https://www.teraco.co.za/data-centre-locations/（JB Isando/Bredell、CT Rondebosch/Brackenfell、DB Riverhorse Valley；NAPAfrica/ACX 生态）；Africa Data Centres/Cassava/Liquid https://www.africadatacentres.com/（Midrand/Samrand、CT CPT1/CPT2 2024 年新增 6 MW、DB）；Vantage JNB1/JNB2 Waterfall City https://vantage-dc.com/data-center-locations/emea/johannesburg-i-south-africa/（JNB1 满配信号最高 120 MW critical load）；Equinix JN1 https://www.equinix.com/data-centers/europe-colocation/south-africa-colocation/johannesburg-data-centers/jn1（308 Brollo Road Germiston/Isando）+ 开普敦 King Air Industria 提案（2026-07 MPT 批准广泛报道，须 DAMS/MPT 记录核实）；OADC/WIOCC https://openaccessdc.net/（Parklands、Bryanston、Isando；2026 收购 7 个 NTT SA 设施）；NTT DATA/Dimension Data/Internet Solutions https://services.global.ntt/...south-africa-data-centers（Parklands、Bryanston、Umhlanga、Bloemfontein、East London、Port Elizabeth/Gqeberha、Bree、Belville——部分已归 OADC，计数前核实现任业主）；BCX/Telkom https://www.bcx.co.za/solutions/services/managed-infrastructure-and-cloud-services/（官方称自有 12 个数据中心）；Digital Parks Africa https://www.dpa.host/（Samrand/Centurion/Pretoria/JHB/CT）；xneelo https://xneelo.co.za/；MTN/Vodacom 电信设施（区分商业托管与内部网络设施）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **贸易媒体分级**：DCD（B，https://www.datacenterdynamics.com/en/news/?tag=south-africa，Teraco/Vantage/Equinix/ADC 扩张最佳）、MyBroadband（B，本地容量/水电争议/Azure 本地化）、TechCentral（B，超大规模投资/法律挑战）、ITWeb（B，本地企业/电信）、Daily Maverick/GroundUp（B，开普敦土地用途批复/反对/审裁日期）、W.Media/Data Centre Magazine/Capacity Media/Dgtl Infra（B/C）、Business Day/Engineering News/Polity/IOL/Moneyweb/News24（B/C 早期线索）。
- **运营商/开发商矩阵（按地理）**：豪登=Teraco（Isando/Bredell）、Equinix JN1（Germiston/Isando）、Vantage JNB1/JNB2（Waterfall City）、ADC/Liquid（Midrand/Samrand）、OADC（Parklands/Bryanston/Isando）、NTT/Dimension Data、BCX/Telkom（Centurion）、Digital Parks Africa（Samrand）；西开普=Teraco CT1/CT2（Rondebosch/Brackenfell）、ADC CPT1/CPT2（Diep River）、Equinix King Air Industria 提案、OADC、AWS/azure 云区域；夸祖鲁-纳塔尔=Teraco DB1（Riverhorse Valley）、NTT Umhlanga、ADC、eThekwini 2026 韩资 AI 数据中心 MOA 线索（MOA 仅 C，须土地/环评/电力/规划记录）；自由邦=OADC Bloemfontein（BFN1）、NTT Bloemfontein；东开普=NTT East London 与 Gqeberha 官方列名、Coega SEZ/ELIDZ；北开普=可再生能源/wheeling 高相关（勿把电站当 DC）。
- **目录来源（C/B）**：DataCenterMap/Baxtel/Cloudscene/DC Atlas/datacenters.com/PeeringDB 仅作遗留电信/边缘设施地址；Uptime Institute 证书为 B/A（认证设施身份）；法律/环评顾问（Pinsent Masons Out-Law、Clyde & Co、Enviroworks EAP PDF）为 B 分析、托管 EIA/BID 告示时 A。
- **去重与陷阱**：Johannesburg 命名错配（豪登设施未必属 JHB 市）；开普敦批复分阶段；电力容量 vs IT 负载标签保留；可再生能源电站≠数据中心；目录可能重复列出旧 NTT/IS/OADC 名称（确认现任业主避免重复计数）；市镇/电信「data centre」可能是内部机房（仅计符合项目范围的设施，否则标 internal/edge 容量未知）。

## 来源分级

- **A** = 官方/一手：市镇 MPT/议会/建筑图/土地用途记录、政府签发的环评授权书、Eskom/NERSA/市镇电力文件、ICASA 咨询/监管文件、官方云区域页（区域存在性）、运营商官方设施页（声称的设施存在性）。
- **B** = 强二级：Data Center Dynamics、MyBroadband、TechCentral、ITWeb、Engineering News、GroundUp、News24、Business Day、IOL、母公司托管的公司发布、工程顾问项目页；作线索与佐证，官方记录存在时不作最终证明。
- **C** = 弱线索：DataCenterMap、Baxtel、Datacenters.com、LinkedIn、社交媒体、请愿、无设施细节的营销声明、MOU/签约仪式文章、顾问臆测。
- 状态语义：见核心结构事实 §7；云区域不推断精确建筑；可再生能源项目不计数为数据中心。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=ZA，divisions=52 province - district/metropolitan municipality），按 explorer-industry.md §6 每个 division：拆分 province/district-metro/关键地方市镇与城镇。
2. 种子：运营商官网（Teraco、ADC/Liquid、Vantage、Equinix、OADC/WIOCC、NTT、BCX/Telkom、Digital Parks Africa）+ 云区域页（AWS/Azure/GCP/OCI）+ Uptime/PeeringDB 兜底。
3. 扫描：市镇 MPT/规划门户（`data centre`/`datacentre`/`data center`+rezoning/SDP/building plan）→ 环评（operator/erf/工业园+province）→ 电力（Eskom/NERSA/市镇电力 MVA/MW/substation/wheeling）→ 贸易媒体（B 桥）→ 目录（C）。
4. 验证：以 A 级官方记录落事实；三拼写全搜；把精确地址映射到 City of Johannesburg / Ekurhuleni / Tshwane / City of Cape Town 等再落 division；阶段不确定显式记录（announced/MOA、land-use approved、building-plan approved、environmental authorised、under construction、operational、expansion）。
5. 输出：按 world schema 写结果，附证据日期与分级；字段含 province/municipality/place/precinct/facility_or_project_name/operator/planning_reference/environmental_reference/power_reference_or_MVA_MW/cloud_or_colo_seed/status。
6. 无项目判定：低概率分区（Limpopo/Mpumalanga/North West/Northern Cape 大部、东开普/自由邦乡村区）需显式负面搜索（运营商+城镇+目录/证书兜底），三面无信号才设 no_projects: true。
7. 遵守 NO-DELETION；本 skill 与两份 explorer 均为只读输入，只新增 SKILL.md 与 ANATOMY.md。

## 待办（2026-08-12 02:26Z）

- [x] explorer-official.md 与 explorer-industry.md 已完成并合并为本 SKILL.md。
- [ ] 下一步：每批 50× codex terra agents，注入本 skill 后按 52 分区逐区枚举（优先 Gauteng：City of Johannesburg/Ekurhuleni/Tshwane；Western Cape：City of Cape Town；KZN：eThekwini）。
- [ ] 待核实：Equinix King Air Industria 提案的 Cape Town DAMS/MPT 记录与决定文件；OADC 收购 7 个 NTT SA 设施的交易确认与各址现任业主；Vantage JNB2 与 Waterfall City 二期（Attacq JV）的市镇管辖（JHB vs Ekurhuleni）与电力证据；eThekwini 韩资 AI 数据中心 MOA 是否已有土地/环评/规划记录。
