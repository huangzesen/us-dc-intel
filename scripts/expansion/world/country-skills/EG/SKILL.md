---
name: eg-datacenter-methodology
location: scripts/expansion/world/country-skills/EG/SKILL.md
description: |
  Egypt (EG) datacenter discovery & audit methodology — how to enumerate, verify, and update Egypt datacenter projects at 27-governorate granularity. Egypt has no single public national planning register for datacenters: enumeration triangulates NTRA licensing (dedicated Data center + Cloud computing licence categories and licensee PDFs — the strongest national operator/service evidence), MCIT/ITIDA/SIS/cabinet government announcements, governorate/local building-permit services (lgs.gov.eg, digital.gov.eg) and NUCA/new-city authorities (6th of October, New Cairo, New Administrative Capital/ACUD, New Alamein, New Borg El Arab, 10th of Ramadan), GAFI/free-zone and SCZONE special-zone leads (Kemet Sokhna, East Port Said), EETC/EgyptERA/EEHC/Ministry of Electricity power evidence plus NREA/PV Hub renewable leads, EEAA environmental approvals, cloud signals (Huawei Cloud Cairo Region AF-Cairo is the only official Egypt public cloud; AWS/Azure/GCP/OCI have no Egypt region — check official tables), and operator pages. Read this before running EG exploration/audit batches. Routes to explorer-official.md (NTRA/planning/power/cloud/governorate) and explorer-industry.md (operator seeds/trade press/English+Arabic vocabulary/governorate matrix).
---

# EG · 埃及数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：埃及**没有**全国公开的数据中心规划登记库；枚举必须拼接 **NTRA 许可（`Data center` + `Cloud computing` 独立牌照类别，全国最强的运营商/服务证据）+ 政府公告（MCIT/ITIDA/SIS/内阁）+ 省/新城规划许可 + 电网/可再生能源 + 环评 + 云区域 + 运营商页**。
> 阿拉伯语是高召回率的必要条件（`مركز بيانات`/`مراكز البيانات`/`الحوسبة السحابية`/`رخصة بناء`/`محطة محولات`…）；开罗都会区是商业重心，特殊经济区（SCZONE）与新城（新行政首都）是规划重点。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供埃及探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：NTRA 数据中心/云许可框架与持牌人 PDF、MCIT/ITIDA/SIS/内阁/ACUD、lgs.gov.eg/digital.gov.eg/NUCA/新城当局、GAFI/自由区、EETC/EgyptERA/EEHC/NREA/PV Hub 电力、EEAA 环评、云区域核查（Huawei Cloud AF-Cairo 为唯一官方埃及公有云；AWS/Azure/GCP/OCI 无埃及区域）、运营商种子（Telecom Egypt RDH/Raya/GPX/Khazna-Benya/Huawei/Orange）、省枚举策略与状态规则 |
| `explorer-industry.md` | 行业/厂商发现：NTRA 持牌人清单用法、MCIT/ITIDA/SIS/内阁/GAFI/SCZONE/NUCA 政府源、承包商页（Orascom/ECG/Redcon/Raya IT）、运营商/开发商种子（Telecom Egypt/Raya/GPX/Orange/Huawei/Link/e-finance/Cyshield/EGIT/ECC/e&/Benya-Khazna/Hassan Allam-A15/INTRO-Kemet/Income-IGI/Renergy 等）、云区域证据、贸易媒体（DCD/W.Media/Capacity/EnterpriseAM/Zawya）、英阿双语词汇表、27 省矩阵、验证与反误报规则 |

## 核心结构事实（框定每次搜索）

1. **NTRA 在埃及比多数国家更重要**：有专门的数据中心设立/运营与托管/云服务监管框架，许可类别区分 `Data center` 与 `Cloud computing`；`Telecommunication Services Licensees` PDF 点名 Raya Data Center、EGIT、Cyshield、AWS、Link Data Center、e-finance、GPX 等。NTRA 数据中心牌照是 A 级运营商/服务证据，但物理设施仍须规划/电力/环评/承包商源核实；云服务牌照 ≠ 设施记录。
2. **规划分散在多个当局**：普通省/地方政府、新城市（NUCA/newcities.gov.eg）、科技园区（Maadi Technology Park/ITIDA）、自由区（GAFI）、国家大项目（新行政首都/ACUD）——Cairo/Giza/New Cairo/6th of October/Smart Village/10th of Ramadan/New Borg El Arab/East Port Said/New Alamein 不得假设普通省门户是唯一许可当局。
3. **电力是决定性线索**：EETC 并网研究、EgyptERA 许可/直售/wheeling 规则、EEHC/电力部公告、NREA/PV Hub 可再生供应、具名变电站；2026 EETC/Heca Data MoU 是模型线索（贸易媒体→回解电力部原始声明）。可再生项目毗邻 ≠ IT load，除非源文件把二者绑定。
4. **云区域核查**：**Huawei Cloud Cairo Region（`AF-Cairo`，2024-05 上线，Orange 为本地服务伙伴，2026 规划新 AZ）是唯一经官方页确认的埃及公有云**；AWS/Azure/GCP/OCI 官方区域表均无埃及公共区域——Azure Front Door Cairo POP/`CAI`、AWS Outposts/本地区域销售、服务可用性 ≠ 区域/设施。
5. **主集群**：大开罗（Cairo/Giza/New Cairo/Maadi/6th of October/Smart Village/新行政首都）为商业重心；次级：Alexandria/Borg El Arab（Income/IGI 规划 100 MW）、Suez/Ain Sokhna/SCZONE（Kemet Data Center 80 MW 四期）、Port Said 自由区、South Sinai/El Tor（Renergy 绿电）、Matrouh/New Alamein、Dakahlia/Mansoura、Qalyubia 电信交换。
6. **状态语义（英阿双语）**：`MoU`/`usufruct`/`land allocation`/`مذكرة تفاهم`/`حق انتفاع`/`تخصيص أرض`=意向；`licensed`/`approves`/`وافق`/`منح ترخيص`=已许可；`groundbreaking`/`under construction`/`بدء الإنشاء`=在建；`customer-ready`/`inaugurated`/`operational`/`افتتاح`/`تشغيل`=运营。
7. **商业 vs 政府 vs 电信设施必须分类**：政府/主权云中心、电信交换、企业 IT 机房不是商业 colo；目录里的 Telecom Egypt 交换站只是线索。
8. **反误报**：`Cairo POP`/CDN 节点/IX/云接入 ≠ 云区域；NTRA 云服务牌照无地点 ≠ 设施；阿拉伯语 `مركز معلومات`（信息中心）常是普通办公室而非数据中心。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§6 / explorer-industry.md §1、§4-§6）

- 英文：`"Egypt" ("data center" OR "data centre" OR datacenter) "{governorate}"`、`"{city}" ("colocation" OR "cloud services" OR "Tier III" OR "Rated-4")`、`"{operator}" "{governorate}" ("NTRA" OR "license" OR "cloud computing services")`、`"{operator}" "{city}" ("Uptime" OR "Tier III")`。
- 阿拉伯语核心词：`مركز بيانات` `مراكز البيانات` `مركز حوسبة` `سنتر داتا` `الحوسبة السحابية` `استضافة` `تراخيص مراكز البيانات` `رخصة بناء` `تصريح بناء` `المركز التكنولوجي` `محطة محولات` `ميجاوات` `تقييم الأثر البيئي` `مولدات` `خزانات وقود`。
- NTRA：`site:tra.gov.eg "data center" "cloud computing services"`、`site:tra.gov.eg "{operator}" "Data Center"`、`site:tra.gov.eg "{operator}" "Cloud computing"`、`site:tra.gov.eg "مراكز البيانات" "ترخيص"`、`"NTRA" "data center" "{operator}"`。
- 政府：`site:mcit.gov.eg "data center" OR "مركز بيانات"`、`site:itida.gov.eg "Maadi Technology Park"`、`site:sis.gov.eg "Government Data and Cloud Computing Center"`、`site:cabinet.gov.eg "data center" "SCZONE" OR "Sokhna"`、`site:sczone.eg "data center"`、`site:gafi.gov.eg "data center" "free zone"`、`site:newcities.gov.eg "data center"`。
- 规划：`site:lgs.gov.eg "رخصة بناء" "مركز بيانات"`、`site:nuca.gov.eg "data center" OR "مركز بيانات"`、`"جهاز تنمية مدينة {new-city}" "مركز بيانات"`、`"{operator}" "رخصة بناء" "مركز بيانات"`。
- 电力/环评：`"EETC" "data center" Egypt`、`site:egyptera.org "data center" OR "{operator}"`、`site:eehc.gov.eg "مركز بيانات"`、`site:nrea.gov.eg "data center"`、`site:eeaa.gov.eg "{operator}" "تقييم الأثر البيئي"`、`"data center" "diesel generators" Egypt "EEAA"`。
- 云 pivot：`"Huawei Cloud" "Cairo Region" "Orange" Egypt`、`"Huawei Cloud" Egypt "availability zone" "2026"`、`"Azure Front Door" Cairo Egypt POP`、`site:aws.amazon.com Egypt "Local Zone" OR "Outposts"`。
- 行业：`site:datacenterdynamics.com/en/news Egypt "data center"`、`site:w.media Egypt "data centre" "NTRA"`、`site:capacitymedia.com Egypt "data centre"`、`site:enterprise.news Egypt "data center" SCZONE OR Kemet`、`site:businesswire.com Egypt "Kemet Data Center"`、`site:trade.gov "Egypt Data Centers"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **NTRA（A）**：https://www.tra.gov.eg/ 框架页、审批公告、Licenses Brief PDF、`Telecommunication Services Licensees` PDF、Global Peering 条款；先搜 NTRA 再搜运营商；提取法律实体、牌照类型/时长/签发日期/许可服务、是否点名站点。
- **MCIT/ITIDA/SIS/内阁（A）**：国家战略/政府云/部长级 MoU；ITIDA Maadi Technology Park 官方页声明园区有数据中心并给出 Cairo 地址。
- **规划（A/B）**：lgs.gov.eg/digital.gov.eg 服务术语；NUCA/newcities.gov.eg 新城；ACUD/新行政首都；GAFI/investinegypt.gov.eg 投资区；提取许可号、地块/街区、技术园区/自由区/新城当局、申请人、用途、面积、MVA/MW、发电机、施工/运营日期。
- **电力（A）**：MOEE/EEHC/EETC/EgyptERA/NREA/PV Hub；`site:moee.gov.eg "مركز بيانات"`、`site:egyptera.org "{operator}"`；提取请求/签约 MVA、IT load、电压、变电站/馈线、并网研究状态、wheeling/直售许可、PPA 对手方、可再生 MW、送电日期。
- **环评（A，谨慎）**：EEAA/环境部；埃及 EIA 文件可能不用英文 `data center`，搜备用发电机/燃料/冷却/变电站/技术园区；咨询公司托管 EIA 为 B+，除非含政府批准函。
- **云（A 区域/C 设施）**：Huawei Cloud `AF-Cairo` 为唯一官方埃及区域；AWS/Azure/GCP/OCI 官方表核查后无埃及公共区域——不得创建设施记录。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **NTRA 持牌人 pivot**：Raya Data Center、EGIT、Cyshield、AWS、Link Data Center、e-finance、GPX、Delta Electronic Systems 等 → 官方页/贸易媒体/目录/阿拉伯语搜索定位设施；2026 新增 Hassan Allam Digital Infrastructure / A15 牌照须回 NTRA/MCIT 主源核实。
- **运营商种子（A=存在/B=容量）**：Telecom Egypt RDH/RDH2（Smart Village/西开罗，Tier III 设计认证，海底电缆枢纽）、Raya（6th of October/Maadi/New Cairo，Africa50 新 Tier III）、GPX（Cairo 1/Cairo 2，扩 12 MW/9,000 sqm/1,800 机架）、Orange Egypt/Orange Business（NAC Grifols 客户设施）、Huawei Cloud（Cairo Region，Orange 伙伴）、Link Data Center（Maadi）、e-finance/Cyshield/EGIT（NTRA 云牌照）、Benya/Khazna（Maadi Technology Park 2.5 亿美元超大规模，规划阶段）、Hassan Allam/A15（2026 牌照）、INTRO/Oman Data Park/Kemet（Sokhna 80 MW 四期，A/B）、Income/IGI（Borg El Arab 100 MW，B）、Renergy（El Tor 绿电，B/C）。
- **承包商页（A/B）**：Orascom（NAC 两个数据中心：Tier 3 38k sqm + 133/1,088 机架）、ECG（RDH2 IT load/机架）、Redcon（GPX Cairo 扩）、Raya IT；可给出面积/机架/状态。
- **贸易媒体**：DCD（B，最佳英文项目流）、W.Media（B，RDH 拆分/利用率）、Capacity/Total Telecom/Developing Telecoms/Telecom Review/Mobile Europe/Connecting Africa（B）、EnterpriseAM/Zawya/BusinessWire/Ahram/Daily News Egypt/Egypt Today（B/C，内阁/SCZONE/投资/MoU）、U.S. ITA 市场注记（A-/B+）、Uptime 认证（仅认证本身 A）。
- **目录（C 线索）**：DataCenterMap、Datacenters.com、Baxtel、Inflect、Cloudscene、PeeringDB、Ocolo、ColoMap。

## 来源分级

- **A** = 官方/一手：NTRA 牌照/框架/新闻稿、MCIT/SIS/内阁/SCZONE 发布、运营商官方设施页、官方云区域页、承包商项目页（含范围/地点）、Uptime 认证、电力/土地/许可记录。
- **B** = 强二级：DCD、W.Media、Capacity Media、Developing Telecoms、Mobile Europe、EnterpriseAM、Zawya、BusinessWire、开发银行/投资方公告（点名运营商/站点）。
- **C** = 仅线索：DataCenterMap、Datacenters.com、Baxtel、Inflect、Cloudscene、PeeringDB、Ocolo、ColoMap、社交媒体、市场报告片段、无设施细节的合作伙伴页。
- **容量规则**：区分 `IT load`/`total power`/`utility allocation`/`future campus capacity`/`phase capacity`/`rack count`/`sqm`；无 kW/rack 或总 IT load 时不把机架换算 MW；MoU/许可/土地 ≠ 运营。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=EG，divisions=27 省）。
2. 牌照种子：从最新 NTRA Licensees PDF + 新闻稿提取全部数据中心/云持牌人（英阿双语归一化）。
3. 大开罗运营商扫描：Telecom Egypt RDH/Raya/GPX/Orange-Huawei/Link/EGID/ECC/e&/Cyshield/e-finance/Benya-Khazna/Hassan Allam → 官方页 → DCD/W.Media/目录。
4. 云核查：Huawei Cloud Cairo Region；重查 AWS/Azure/GCP/OCI 官方区域表；edge POP 单独记录。
5. 特殊区/新城扫描：SCZONE/Sokhna/Kemet、NAC/Orascom/Orange/Grifols、Maadi Technology Park/Khazna-Benya、Smart Village/Telecom Egypt、Borg El Arab/Income、Port Said 自由区/WAVZ。
6. 逐省模板扫描（英+阿）；预期 Cairo/Giza/Suez/Alexandria/Port Said/Dakahlia/Qalyubia/Sohag/Qena/South Sinai/Matrouh 线索最强，其余记录阴性结果。
7. 去重：按 (终极运营商 + 园区/名称 + 城市/省 + 阶段)；注意大开罗边界别名（Cairo/Giza/6th of October/Smart Village/New Cairo/Maadi 可能是同一设施）与 NAC 省归属；政府/主权设施明确标记类型。
8. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目 division 写 `no_projects: true`；容量区分 `operational` / `under_construction` / `planned_full_buildout_mw`。
9. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核埃及数据中心（27 省粒度，Greater Cairo 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Khazna-Benya Maadi 超大规模建设状态、Telecom Egypt RDH2 完成度与 RDH 拆分、GPX Cairo 2 扩建成效、Hassan Allam/A15 牌照细节与站点、Kemet/Sokhna 土地与许可、Income/Borg El Arab 100 MW 项目、Renergy/El Tor 绿电项目、Huawei Cloud 2026 新 AZ 设施、Orascom NAC 两数据中心进度。
