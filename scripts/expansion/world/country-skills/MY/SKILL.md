---
name: my-datacenter-methodology
location: scripts/expansion/world/country-skills/MY/SKILL.md
description: |
  Malaysia (MY) datacenter discovery & audit methodology — how to enumerate, verify, and update Malaysia datacenter projects across 13 states + 3 federal territories (Johor, Selangor/Greater KL/Cyberjaya, WP Kuala Lumpur, Penang, Sarawak, Sabah, …). Malaysia has no complete public national datacenter registry: enumeration joins planning approvals (local-authority OSC 3.0 Plus under KPKT, DBKL OSC, Penang ILCS, Johor Fast Lane; PLANMalaysia GPP Pusat Data >1 MVA guideline approved 2024-10-08, Johor State DC Guideline), utility trails (TNB Green Lane Pathway 132/275 kV one-stop with ~12-month connection target; Sarawak Energy and Sabah Electricity for East Malaysia; water/SPAN/Air Selangor/Ranhill SAJ), DOE/EIA environmental records, MCMC ASP(C) cloud-service licensing and ReCPro, MIDA/MDEC/DIO investment facilitation and Malaysia Digital status, Bursa/issuer filings, official cloud-region pages (AWS ap-southeast-5 opened 2024-08-21, Azure Malaysia West + Southeast Asia 3/Johor Bahru intent, Google first Malaysia DC at Elmina/Selangor, Oracle Malaysia West 2/Kulai ap-kulai-2), and operator pages (AirTrunk JHB1-4, YTL, PDG JH1/JH2, Bridge MY06, Vantage JHB1 + Cyberjaya, NTT Cyberjaya, Keppel/Basis Bay, TM/Nxera, AIMS, Equinix). Read this before running MY exploration/audit batches. Routes to explorer-official.md (planning/TNB/MCMC/MIDA/cloud/operator/division strategy) and explorer-industry.md (operator seeds/trade press/IXP/Malay-English vocabulary/state matrix).
---

# MY · 马来西亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：马来西亚**没有**完整的全国数据中心注册库；普查靠拼接**规划审批（地方当局 OSC 3.0 Plus、DBKL OSC、Penang ILCS、Johor Fast Lane）、电力（TNB Green Lane Pathway 132/275 kV 一站式，东马用 Sarawak Energy/Sabah Electricity）、水（SPAN/Air Selangor/Ranhill SAJ）、环评（DOE/EIA）、MCMC ASP(C) 云服务许可、MIDA/MDEC/DIO 投资促进、云区域官方页、运营商页**。
> 规划证据是 PBT（地方当局）特有的：`Kebenaran Merancang`/`Pelan Bangunan`/`Pelan Kerja Tanah`/`CCC` 是施工状态主干；`Greater Kuala Lumpur` 不等于吉隆坡联邦直辖区（多数超大规模用地在雪兰莪）；`Kuala Lumpur`/`Johor Bahru` 营销标签必须解析到物理州/县（Cyberjaya=Selangor，Sedenak/Kulai/Nusajaya=Johor）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供马来西亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：KPKT/OSC 3.0 Plus/DBKL/PBT、PLANMalaysia GPP Pusat Data（>1 MVA，2024-10-08 内阁批准）与 Johor 州指南（JPBD Johor PDF，JPPPDNJ 委员会）、DOE/EIA/SPAN/水司、TNB Green Lane/ST/SEDA 电网、MCMC ASP(C)/ReCPro、MIDA/MDEC/DIO、云区域官方页（AWS ap-southeast-5/Azure Malaysia West+SEA3/Google Elmina/Oracle ap-kulai-2）、运营商种子（AirTrunk/YTL/PDG/Bridge/Vantage/NTT/Keppel-Basis Bay/AIMS/TM-Nxera/Equinix 等）、逐州分层枚举策略（Tier 1-3）与最小记录字段 |
| `explorer-industry.md` | 行业/厂商发现：DIO/MDEC/MIDA/MITI/州投资机构/Bursa 主源、DCD/W.Media/The Edge/Bernama/NST/The Star/BusinessToday/Lowyat/SoyaCincau 等贸易与马媒、MDCA/MyIX/DE-CIX/Penang IX/PeeringDB/Uptime 协会与互连源、英马双语词汇与状态词、运营商/开发商种子（DayOne-GDS/PDG/Vantage-Yondr/AirTrunk/YTL/Bridge/STT-Basis Bay/NTT/Equinix/Digital Realty-CSF/EdgeConneX/TM/AIMS/Open DC/IP ServerOne/Infinaxis/NEXTDC/Google-Sime Darby 等）、云区域处理、16 州/联邦直辖区矩阵、去重与可靠性注意 |

## 核心结构事实（框定每次搜索）

1. **规划=地方当局主导**：半岛开发申请通常走 KPKT 下 **OSC 3.0 Plus Online**（osc3plus.kpkt.gov.my），KL 有独立 DBKL OSC 门户，Penang 历史上用 ILCS 等本地系统，Johor 用 **Johor Fast Lane** 与州数据中心协调流程；PLANMalaysia **GPP Pusat Data**（>1 MVA，2024-10-08 内阁批准）是统一参考；Johor 州有独立官方指南（jpbd.johor.gov.my PDF，路由 PBT OSC/Johor Fast Lane + JPPPDNJ 委员会）。
2. **电力证据异常强**：TNB 为数据中心建 **Green Lane Pathway**（132/275 kV 高压供电、一站式、连接期从 36-48 个月压缩至约 12 个月）；ESA（供电协议）、MVA/MW、`pencawang masuk utama` 变电站、馈线工程、送电日期是高价值证据；东马必须用 **Sarawak Energy**/**Sabah Electricity**，不得套用半岛 TNB 证据。
3. **云区域=区域证据（A），非设施地址**：AWS Asia Pacific (Malaysia) `ap-southeast-5` 3 AZ（2024-08-21 开）；Azure Malaysia West（Greater KL，3 AZ）+ 已宣布 Southeast Asia 3（Johor Bahru）；Google 首个马来西亚 DC + 云区域（Elmina Business Park/Shah Alam/Selangor，Sime Darby Property 共建租约）；Oracle Malaysia West 2 (Kulai) `ap-kulai-2`（2026-02-02）；Alibaba 也在 Johor。AZ 数不推断地址。
4. **MCMC ASP(C) 轻触云服务许可**：本地存在或经本地 DC 提供云服务者落入 Applications Service Provider Class Licence (ASP(C)) 框架——法律实体/受规管服务种子，非设施证明；ReCPro 查布线/网络设施提供商。
5. **MIDA/MDEC/DIO（A，投资批准/状态）**：MIDA 2021-2023 数据中心/云服务批准投资 RM114.7 亿（聚合值不作设施计数）；Malaysia Digital Status、Data Centre Task Force、按运营商与州搜 MIDA（常镜像/转载运营商公告）。
6. **主集群**：Johor（Sedenak Tech Park/Kulai、Iskandar Puteri/Nusajaya、JB/Plentong/Gelang Patah/Senai/Pasir Gudang/Tanjung Langsat/Muar——AirTrunk JHB1-4、YTL Green DC Park 500 MW、PDG JH1/JH2、Bridge MY06、Vantage JHB1 300 MW、Keppel DC Johor 1、Microsoft SEA3、Oracle Kulai、TM Nxera IPDC）；Selangor/Greater KL（Cyberjaya/Sepang、Elmina/Shah Alam、Kajang-Bangi、Subang、MRANTI——Vantage KUL1/KUL2、NTT Cyberjaya 1-6、Equinix KL1/KL2、Google Elmina、TM KVDC、Basis Bay/STT、Digital Realty/CSF、AIMS）；WP KL（Menara AIMS carrier hotel、CBD/金融、Bukit Jalil）；Penang（Bayan Lepas/Batu Kawan/Perai，ILCS）；Kedah（Kulim Hi-Tech/Open DC D8-1）；Sarawak/Sabah（水电/州云/边缘，较小且政府/电信主导）。
7. **容量语义**：区分 `critical IT load`/`facility load`/`power supply`/`powered land`/`campus buildout`；AirTrunk JHB1 150+ MW/JHB2 270+ MW/JHB3-4 280 MW、PDG JH1 150 MW（官方披露 200/300 MW 概念）、Vantage JHB1 300 MW+、YTL 公园 500 MW 概念——全期 vs 一期分开。
8. **反误报**：`pusat data nasional`/部委数据中心/州整合数据中心常是公共部门 IT 机房；`Greater KL` ≠ KL 联邦直辖区；MIDA 聚合 ≠ 设施；OSC 详情可能登录受限（用公开会议标题/市议员报告/新闻恢复申请号）；数据中心可被批准为工业/商业/公用事业/ICT/仓库/办公/混合用途，不总是 `pusat data`。

## 查询模式（复制粘贴模板见 explorer-official.md §1、§9 / explorer-industry.md §1、§7）

- 英/马混合拼写：`"data centre" "{operator}" "{state_or_city}"`、`"data center"`、`"pusat data"`、`"pusat data raya"`、`"pusat data AI"`、`"pusat kolokasi"`、`"ladang pelayan"`、`"cloud region"`、`"carrier hotel"`、`"disaster recovery centre"`。
- 规划：`"pusat data" "kebenaran merancang" "{PBT}"`、`"data centre" "OSC" "{PBT}"`、`"pusat data" "pelan bangunan"`、`"pusat data" "pelan kerja tanah"`、`"data centre" "CCC" Malaysia`、`site:osc3plus.kpkt.gov.my/pbt "pusat data"`、`site:osc.dbkl.gov.my "data centre"`、`site:jpbd.johor.gov.my "data centre"`、`"Johor Fast Lane" "pusat data"`。
- 电力/水：`site:tnb.com.my "{operator}" "data centre"`、`site:tnb.com.my "{operator}" "MVA"`、`site:tnb.com.my "Green Lane Pathway" "data centre"`、`site:tnb.com.my "pencawang" "pusat data"`、`"{operator}" "132kV" OR "275kV" Malaysia`、`site:sarawakenergy.com "data centre"`、`site:sabah-electricity.com.my "data centre"`、`site:span.gov.my "data centre"`、`site:airselangor.com "data centre"`、`site:ranhillsaj.com.my "data centre"`、`"data centre" "recycled water" "Johor"`。
- 环评/监管/投资：`site:doe.gov.my "data centre" "EIA"`、`site:mcmc.gov.my "cloud services" "ASP(C)"`、`site:recpro.mcmc.gov.my "{operator}"`、`site:mida.gov.my "data centre" "{operator}"`、`site:mdec.my "Malaysia Digital Status" "data centre"`、`site:mydigitalinvestment.gov.my "Data Centre & Cloud"`、`site:bursamalaysia.com "data centre" "{issuer}"`。
- 云 pivot：`"ap-southeast-5" Malaysia "Availability Zones"`、`"Malaysia West" "Greater Kuala Lumpur"`、`"Southeast Asia 3" "Johor Bahru" Microsoft`、`"Google data center" "Elmina Business Park"`、`"Pearl Computing Malaysia"`、`"ap-kulai-2" "Kulai" Oracle`、`"Alibaba Cloud" Malaysia Johor`。
- 行业：`site:datacenterdynamics.com Malaysia "{operator}"`、`site:theedgemalaysia.com "data centre" "{operator}"`、`site:thestar.com.my "data centre" Johor OR Cyberjaya`、`site:bernama.com "pusat data" Malaysia`、`site:w.media Malaysia "data center"`、`"MyIX" "{operator}" Cyberjaya OR "Kuala Lumpur"`、`"Penang IX" "data centre"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **规划（A）**：OSC 3.0 Plus/DBKL/PBT 页（先定 PBT：Cyberjaya=MPSepang、Elmina=MBSA、Petaling Jaya=MBPJ、Kajang=MPKj、Subang=MBSJ、Klang=MPKlang、JB=MBJB、Kulai=MPKu、Iskandar Puteri=MBIP）；提取申请号/申请人/业主/地段/mukim/区/提案/计划类型/会议日期/决定/公告；`Kebenaran Merancang`、`Pelan Bangunan`、`Pelan Kerja Tanah`、`Pelan Jalan dan Parit`、`CCC` 为主要状态链。
- **PLANMalaysia/Johor 指南（A，框架）**：GPP Pusat Data 筛选分区/缓冲/1 MVA 工作流；州采用通告与地方计划公示；指南本身不产生设施。
- **环境/水（A）**：DOE EIA Report Status/Executive Summary（按运营商/地主/工业园/发电/备用燃料/取水触发，`data centre` 不是干净的 prescribed activity 类别）；SPAN/Air Selangor/Ranhill SAJ（马来西亚近期关注水耗/中水/饮用水约束）。
- **电力（A）**：TNB Green Lane/ESA/MVA/132-275 kV/变电站/送电日期 + GET/CRESS/太阳能-BESS-区域冷却；Sarawak Energy/Sabah Electricity 用于东马；ST/SEDA 监管语境。
- **MCMC（A，许可）**：ASP(C) 云服务许可、Network Facilities Provider、ReCPro 布线/网络设施生态。
- **MIDA/MDEC/DIO（A/B）**：批准投资、Malaysia Digital Status、项目促进、州/站点提示；聚合统计不作设施。
- **行业**：DCD（B+）、The Edge Malaysia（B+）、Bernama/NST/The Star/Malay Mail（B）、BusinessToday/DNA/Lowyat/SoyaCincau（B-/C+）、承包商（Gamuda/IJM/Sime Darby Property/JCorp/Mah Sing/Paragon Globe，B）、MDCA（B-/C+）、MyIX/DE-CIX/Penang IX（A-/B，互连节点）、Uptime（A 认证）、Baxtel/DataCenterMap/Cloudscene/PeeringDB（C，有时 B-）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商/开发商种子（A=存在/B=容量）**：DayOne/GDS（Nusajaya Tech Park NTP1-3 + Kempas）、PDG（JH1 Sedenak 150 MW 一期交付、JH2 16 km 外）、Vantage/Yondr（JHB1 300 MW+，收购保持历史名+现名）、Vantage Cyberjaya（KUL1 运营、KUL2 436 MW 相邻园区）、AirTrunk（JHB1 150+ MW/JHB2 270+ MW/JHB3-4 280 MW，TNB 150 MW ESA、中水、屋顶光伏）、YTL（Green Data Center Park Kulai 275 英亩/500 MW 概念 + NVIDIA/Sea/AI Cloud）、Bridge/Chindata/Bain（MY06 Sedenak/ByteDance、Cyberjaya）、STT/Basis Bay（KL1 + Cyberjaya DC.1/DC.2 + Johor NCIP）、NTT（Cyberjaya 1-6，CBJ5/CBJ6 12 MW 级；Johor Gelang Patah 购地管线）、Equinix（KL1/JH1，KL2/JH2 扩张）、Digital Realty/CSF（Cyberjaya TelcoHub 收购，旧名防重复）、EdgeConneX（Cyberjaya/KL）、TM/TM Global/Nxera（KVDC Cyberjaya、IPDC Iskandar Puteri 280 MW TNB）、AIMS（Menara AIMS/KL carrier hotel + Cyberjaya）、Open DC（CJ1 Cyberjaya、JB1/JB2、D8-1 Kedah、PE1/PE2 Penang，官方称六家）、IP ServerOne（CJ1 Tier 3）、Infinaxis（Cyberjaya 新兴，多为目录线索）、NEXTDC（KL1 65 MW Tier IV，注意实际物理位置）、Google/Sime Darby（Elmina 破土）。
- **状态词（英/马）**：`announces/launches/opens/ready for service/commercial operation/operational/groundbreaking/breaks ground/topped out/land acquisition/built-to-suit lease/power secured`；马 `dilancarkan/beroperasi/pecah tanah/dibina/kebenaran merancang/pelan bangunan/kelulusan`；`Malaysia Digital status`/`approved digital investment`=批准语境 A 非设施；`MoU/exploring/potential/expected to attract`=C；`land acquisition/power secured/water agreement`=A-/B+；`ready for service/opens/go-live`=运营证据。

## 来源分级

- **A** = 官方/一手：PLANMalaysia/KPKT 指南与通告、OSC/PBT 规划记录、州指南（Johor）、DOE/EIA、SPAN/水司、TNB/ST/Sarawak Energy/Sabah Electricity、MCMC 许可/登记、MIDA/MDEC/DIO 官方发布、云区域官方页、运营商官方设施页、Bursa/年报披露、Uptime 认证、工业园开发商官方页。
- **B** = 强二级：Bernama、The Edge Malaysia、The Star、DCD、AP/FT、承包商新闻稿、可信律所/工程笔记（点名法定流程或项目）、W.Media。
- **C** = 弱线索：目录、经纪页、社交帖、招聘广告、未验证地图、无申请号的社区反对。
- **容量/状态规则**：`critical IT load`/`facility load`/`power supply`/`powered land`/`campus buildout` 分开存单位；云区域 ≠ 设施；MIDA 聚合 ≠ 设施；Google/AWS/Azure/Oracle 区域名是高等级云服务证据但建筑需规划/运营商/土地/公用事业证明。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=MY，divisions=13 州 + 3 联邦直辖区）。
2. 建种子：云区域（AWS/Azure/Google/Oracle/Alibaba）+ 运营商官方页（AirTrunk/YTL/PDG/Bridge/Vantage/NTT/Keppel-Basis Bay/TM-Nxera/Equinix/STT/AIMS/Open DC/NEXTDC）+ MIDA/MDEC/DIO。
3. 归一化实体：马 SPV ≠ 全球品牌（从运营商发布/Bursa/MIDA/承包商合同取公司/法律名）；解析营销标签到物理州/县/PBT（`Greater KL`、`Kuala Lumpur`=Cyberjaya/Selangor、`Johor Bahru`=周边县）。
4. 拉规划链：OSC 3.0 Plus/DBKL/市议会页搜 `kebenaran merancang`/`pelan bangunan`/`pelan kerja tanah`/`Mesyuarat OSC`/`CCC`。
5. 拉电力链：TNB Green Lane/ESA/MVA/132-275 kV/变电站；东马 Sarawak Energy/Sabah Electricity；拉水/环评链：DOE EIA/SPAN/水司/中水/冷却/发电机；拉监管链：MCMC ASP(C)/网络许可/ReCPro/MDEC Malaysia Digital。
6. 逐州矩阵：先 Johor + Selangor/Cyberjaya（Tier 1），再 KL/Penang（Tier 1），Sarawak/Putrajaya/Labuan 与 Negeri Sembilan/Melaka/Perak/Kedah（Tier 2），Sabah/Pahang/Terengganu/Kelantan/Perlis（Tier 3）；贸易媒体只补缺。
7. 去重：JHB1 可能指 AirTrunk 或 Vantage/Yondr（存运营商特定园区码+来源日期）；GDS→DayOne；Vantage→Yondr；CSF→Digital Realty；Cyberjaya 被国际页标为 Kuala Lumpur；政府 DC 与商业 colo 分类。
8. 输出最小记录字段：facility_name/operator_brand/legal_entity/state/district-PBT/mukim-park/source_status（planned|approved|under construction|energized|operating|cancelled）/planning_evidence/power_evidence/water_environment_evidence/cloud_or_operator_evidence/confidence_grade/notes；无项目 division 写 `no_projects: true`；容量区分 `operational` / `under_construction` / `planned_full_buildout_mw`。
9. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核马来西亚数据中心（州/联邦直辖区粒度，Johor + Selangor/Cyberjaya 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：AirTrunk JHB3/JHB4 与 Vantage JHB1 建设状态、YTL Green DC Park 各 JDC 期、PDG JH2 与 Bridge MY06 许可、Oracle ap-kulai-2 物理设施、Microsoft SEA3 Johor Bahru 进展、Google Elmina 数据中心完工、NTT Johor 购地管线、TM Nxera IPDC 280 MW、TNB Green Lane 各项目连接时间表、Alibaba Johor 区域设施。
