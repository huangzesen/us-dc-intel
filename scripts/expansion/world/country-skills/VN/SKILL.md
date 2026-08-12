---
name: vn-datacenter-methodology
location: scripts/expansion/world/country-skills/VN/SKILL.md
description: |
  Viet Nam (VN) datacenter discovery & audit methodology — how to enumerate, verify, and update Vietnamese datacenter projects across 63 province/municipality divisions (manifest; 2025 admin reorg reduced the country to 34 provincial-level units from 2025-07-01 — search old and new names). Viet Nam has no single public datacenter registry: enumeration joins investment-policy approvals (chấp thuận chủ trương đầu tư), investment registration certificates (IRC), construction permits (giấy phép xây dựng) and PCCC acceptance, high-tech / industrial / export-processing zone management boards (SHTP, HEPZA, HHTP, QTSC), EVN power evidence, MIC / VTA telecom and cloud-service regulation (2023 Telecom Law, Decree 163/2024/NĐ-CP, effective 2025-01-01), official cloud footprint pages (AWS Hanoi Local Zone + Direct Connect @ CMC Tower, no Azure/GCP/OCI region), and operator pages (Viettel IDC, VNPT, FPT Fornix, CMC Telecom, STT VNG, NTT/QD.TEK, Edge Centres, VNTT/Becamex, Saigontel, MobiFone). Read this before running VN exploration/audit batches. Routes to explorer-official.md (approvals/zones/power/MIC/cloud) and explorer-industry.md (Vietnamese queries/trade press/province matrix).
---

# VN · 越南数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：越南**没有**单一公开的国家数据中心注册库；枚举需 join **投资政策批准（chấp thuận chủ trương đầu tư）**、**投资登记证书（IRC）**、**建筑许可（giấy phép xây dựng）与 PCCC 消防验收**、**高科技/工业/出口加工区管委会（SHTP、HEPZA、HHTP、QTSC）**、**EVN 电力证据**、**MIC/VTA 电信与云服务监管**（2023 电信法 + 163/2024/NĐ-CP，2025-01-01 生效，数据中心/云服务无外资上限）与**运营商官方页**。
> 商业数据中心集中在 **Ho Chi Minh、Ha Noi、Binh Duong、Da Nang** 及周边高科技/工业区；次级线索在 Dong Nai、Long An、Ba Ria - Vung Tau、Binh Dinh、Khanh Hoa 等电力富余中南部省份。注意 2025 行政重组（63→34 省级单位，2025-07-01 起新政府运作）——输出仍按 manifest 63 名，但检索需新旧名都搜（如 Binh Duong/BR-VT 记录可能出现在扩大的 HCMC 门户）。
> 省级政府数据中心（trung tâm tích hợp dữ liệu tỉnh）多为小型公共设施，与商业 colo/hyperscale 分开标注。本 skill 汇总两份探索报告（官方管线 + 行业发现），供越南探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：投资/规划/建设批准链（UBND/SKHĐT/Sở Xây dựng/管委会）、高科技/工业/出口加工区、EVN 电网、MIC/VTA 电信法登记、官方云足迹（AWS Hanoi Local Zone/Direct Connect@CMC Tower、Azure HCMC POP、无 GCP/OCI 区域）、运营商官方种子（Viettel/VNPT/FPT/CMC/NTT-QD.TEK/STT VNG）、分级工作流与记录清单 |
| `explorer-industry.md` | 行业/厂商发现：越南语关键词与状态词表、行业/贸易媒体（DCD/ITA/VIR/The Investor/VnExpress/VietnamNet/ICTVietnam/Bao Dau Tu/Tuoi Tre/VOV）、运营商/开发商矩阵（Viettel、VNPT、FPT Fornix、CMC、STT VNG、NTT/QD.TEK、Edge Centres、VNTT/Becamex、SAM/VSIP、Saigontel、Gaw、KBC/AIC、G42、MobiFone、True IDC）、区域集群（Hanoi/CMC、HCMC/Tan Thuan/SHTP/Tan Phu Trung、南方工业带、中部海岸）、63 省查询矩阵与通用模板 |

## 核心结构事实（框定每次搜索）

1. **批准链是主证据链**：投资政策批准 → IRC → 建筑许可/动工通知（thông báo khởi công）→ 竣工验收（nghiệm thu）→ PCCC/环境（ĐTM）→ 运营；`khởi công`/`khánh thành`/`đưa vào vận hành` 是状态词；`MOU`/`biên bản ghi nhớ`/`ký kết hợp tác` 只是 C/B 线索，直到 IRC/土地/动工/电力出现。
2. **园区管委会是最可靠精确定位**：SHTP（Saigon Hi-Tech Park）、HEPZA（Tan Thuan 出口加工区）、HHTP（Hoa Lac）、Tan Phu Trung 工业园、QTSC——地块号（如 Lô VA02C-03A）比泛城市名可靠；工业园所在常是最好 locator。
3. **监管**：2023 电信法把 `dịch vụ trung tâm dữ liệu` 与 `dịch vụ điện toán đám mây` 纳入电信框架（2025-01-01 生效），163/2024/NĐ-CP 为关键实施法令，数据中心/云无外资上限；MIC/VTA 证明服务类别与注册，通常不揭示地址/MW/建设状态。
4. **云足迹**：AWS **Hanoi Local Zone（2026-06 GA）** + **AWS Direct Connect @ CMC Tower, Hanoi（2025-12）**；Azure 官方列表无越南区域（仅 HCMC Front Door POP）；GCP/OCI 无越南区域（CMC 提供 OCI FastConnect 连接）。云区域/边缘=服务证据，非建筑证据。
5. **容量字段分开**：`công suất thiết kế`（设计容量）vs `công suất IT`（IT 容量）vs `công suất điện`（受电）vs `rack`/`máy chủ`/`diện tích sàn`（机房面积）；越南文章常把未来全园区 MW 当当前容量；`MW IT` 与总电力分开记。
6. **假阳性**：省级 `trung tâm tích hợp dữ liệu`/`trung tâm dữ liệu tỉnh` 多为小型公共设施（政府采购 muasamcong.mpi.gov.vn 可见，A=买家/包件/市政设施证据，非商业 MW）；`Trung tâm Dữ liệu quốc gia` 指公安部国家公共平台，会淹没商业搜索；`IDC` 可能指工业开发公司；越南语有声调，`trung tâm dữ liệu` 与 `trung tam du lieu` 都要搜。
7. **去重**：按 `(最终母公司, 越南 SPV, 园区/工业园, 省)` 匹配；STT VNG HCMC1（原 VNG Data Center）与 HCMC2 区分；NTT HCMC1/QD.TEK=SHTP 6 MW；KBC/AIC 200 MW 为 MoU；2025-2026 hyperscale 项目需 IRC/官方运营商发布/园区管委会公告/动工证据之一才标 `approved`/`construction`。

## 查询模式（复制粘贴模板见 explorer-official.md §1 与 explorer-industry.md §6）

- 越南语核心词：`trung tâm dữ liệu` `TTDL` `IDC` `Internet Data Center` `trung tâm tích hợp dữ liệu` `trung tâm dữ liệu tỉnh` `siêu trung tâm dữ liệu` `trung tâm dữ liệu AI` `điện toán đám mây` `hạ tầng số` `nhà máy dữ liệu` `server farm`。
- 状态词：`khởi công`/`động thổ`=动工；`khánh thành`/`khai trương`/`đưa vào vận hành`/`chính thức vận hành`/`đi vào hoạt động`=运营；`được phê duyệt`/`chủ trương đầu tư`/`giấy chứng nhận đăng ký đầu tư`/`IRC`=批准；`MOU`/`biên bản ghi nhớ`/`ký kết hợp tác`/`đề xuất dự án`/`khảo sát địa điểm`=意向；`quỹ đất`/`khu công nghiệp`/`khu công nghệ cao`/`khu chế xuất`/`khu kinh tế`=土地/园区信号。
- 投资/建设：`"trung tâm dữ liệu" "chấp thuận chủ trương đầu tư" "{province}"`、`"trung tâm dữ liệu" "giấy chứng nhận đăng ký đầu tư" "{province}"`、`"trung tâm dữ liệu" "giấy phép xây dựng" "{province}"`、`site:{province-domain}.gov.vn "trung tâm dữ liệu"`、`site:{dpi-domain}.gov.vn "trung tâm dữ liệu"`。
- 园区：`"trung tâm dữ liệu" "Khu Công nghệ cao TP.HCM"`、`"trung tâm dữ liệu" "Khu chế xuất Tân Thuận"`、`"trung tâm dữ liệu" "Khu Công nghệ cao Hòa Lạc"`、`site:shtp.hochiminhcity.gov.vn OR site:hepza.hochiminhcity.gov.vn OR site:hhtp.gov.vn "trung tâm dữ liệu"`。
- 电力：`"trung tâm dữ liệu" "EVN" "{province}"`、`"trung tâm dữ liệu" "trạm biến áp" "{province}"`、`site:evn.com.vn OR site:evnhcmc.vn OR site:evnhanoi.vn "trung tâm dữ liệu"`。
- 监管：`site:mic.gov.vn "dịch vụ trung tâm dữ liệu"`、`"Nghị định 163/2024/NĐ-CP" "dịch vụ trung tâm dữ liệu"`、`site:vnta.gov.vn "trung tâm dữ liệu" "đăng ký cung cấp dịch vụ viễn thông"`。
- 云：`"AWS Local Zone" Hanoi Vietnam "CMC Tower"`、`"AWS Direct Connect" Hanoi "CMC Tower"`、`"Azure Front Door" "Ho Chi Minh City" "Vietnam"`、`"Viettel Cloud" "data center" "Hà Nội" "Hồ Chí Minh"`、`"CMC Cloud" "AWS Direct Connect" "CMC Tower"`。
- 媒体：`site:datacenterdynamics.com Vietnam "data center" "{operator}"`、`site:vietnamnet.vn "trung tâm dữ liệu" "{operator}"`、`site:vnexpress.net "trung tâm dữ liệu" "{province}"`、`site:ictvietnam.vn OR site:baodautu.vn OR site:tuoitre.vn OR site:vov.vn "trung tâm dữ liệu" "{province}"`。
- 降级/取消：`"{project}" ("chậm tiến độ" OR "tạm dừng" OR "dừng triển khai" OR "thu hồi" OR "hủy bỏ")`、`"{project}" ("vướng mắc" OR "thiếu điện" OR "môi trường" OR "khiếu nại")`。

## 官方/监管管线要点（详见 explorer-official.md）

- 投资/规划：省级 UBND、Sở Kế hoạch và Đầu tư（SKHĐT）、Sở Xây dựng、Sở Thông tin và Truyền thông；国家行政程序门户 dichvucong.gov.vn；建设部 moc.gov.vn。
- 园区管委会：SHTP（https://shtp.hochiminhcity.gov.vn/ ）、HEPZA（https://hepza.hochiminhcity.gov.vn/ ）、HHTP/Hoa Lac（https://hhtp.gov.vn/ ）、QTSC；`khu công nghệ thông tin tập trung`（集中 IT 园）是未来集群关键词。
- EVN 电力（A=电力/变电站/电网事实，非设施普查）：EVN 集团（https://www.evn.com.vn/ ）、EVN HCMC（https://evnhcmc.vn/ ）、EVN Hanoi（https://evnhanoi.vn/ ）、国家输电公司（https://www.npt.evn.vn/ ）；`cấp điện`/`trạm biến áp`/`110kV`/`220kV`。
- MIC/VTA（A=服务类别/注册）：https://mic.gov.vn/ 、https://english.mic.gov.vn/ 、cspl.mic.gov.vn、vnta.gov.vn；2023 电信法+163/2024/NĐ-CP。
- 云足迹：AWS Hanoi Local Zone（2026-06）+ Direct Connect @ CMC Tower（2025-12）；Azure 仅 HCMC Front Door POP；GCP/OCI 无区域——连接性线索。
- 运营商官方页（存在性 A，容量 A-/B）：Viettel IDC（Hoa Lac 30 MW/2,400+ 机架、Binh Duong、HCMC Hoang Hoa Tham、Da Nang、Tan Phu Trung 140 MW/~10,000 机架/4 ha、首期 2026）、VNPT IDC（8 个 DC：Hoa Lac/Tan Thuan/Cau Giay/Da Nang/HCMC）、FPT Fornix（HN01/HN02/HCM01/HCM02；HCM02 3,600 机架/10,000 m²@SHTP）、CMC Telecom（CMC Tower Hanoi、Tan Thuan、SHTP 120 MW hyperscale 2025 获批）、NTT/QD.TEK HCMC1@SHTP（官方页 6 MW critical IT load/3,100 m²）、STT VNG HCMC1 运营 + HCMC2 计划 60 MW（Tan Thuan）、Edge Centres EC51 HCMC、VNTT/Becamex（Binh Duong eDatacenter）、Saigontel（Long An Nam Tan Tap/Tan Phu Trung）、MobiFone（Hai Phong/Da Nang/Dong Nai 等）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：DCD Vietnam tag（B+，Viettel/CMC/FPT/STT VNG/NTT/Gaw/Saigontel）、ITA market intelligence（B+，41 个活跃商业 DC/221 MW/12 投资者种子）、Viet Nam Government Portal（A-/B+）、MIC/MOST 英文页（A-/B）、VIR/The Investor（B，KBC/AIC、CMC、G42、电价争议）、VietnamPlus/VNA（B+）、VnExpress（B）、VietnamNet/ICTNews（B，电价/政策/运营商列表）、ICT Vietnam（B）、Bao Dau Tu（B）、Tuoi Tre/VOV（B，BR-VT Digital Hub、Long An、省公告）、W.Media/Dgtl Infra/Light Reading（B/C+）、CBRE/C&W/Savills/JLL/Arizton/Mordor（B 聚合/C 付费摘要）、DataCenterMap/Baxtel/PeeringDB（C，PeeringDB 对精确地址互连设施可 B-）。
- 区域集群：**Ha Noi/Hoa Lac/北方**（Viettel Hoa Lac、VNPT Hoa Lac/Cau Giay、FPT HN01/HN02、CMC Tower+AWS DX、Hanoi Telecom/HTC、Thang Long IP、北宁/北江/兴安/海阳电子走廊）；**HCMC**（Tan Thuan/District 7、SHTP/Thu Duc、Tan Phu Trung/Cu Chi、QTSC/District 12；Viettel TPT、STT VNG、CMC、NTT、FPT HCM02、KBC/AIC 200 MW MoU、Evolution/Hathor、Edge Centres、Gaw、True IDC、MobiFone、Saigontel）；**Binh Duong/Dong Nai/Long An/BR-VT**（SAM DigitalHub VSIP 3 150 MW/~50 ha、Viettel BD、VNTT/Becamex、Saigontel+P&G Tech、BR-VT Digital Hub/DCH Chau Duc 海缆站）；**Da Nang/中部**（VNPT An Don、Viettel Da Nang、MobiFone、Hoa Khanh、Nhon Hoi EZ、Khanh Hoa Van Phong、Quang Nam Chu Lai）；Mekong 与其余省多为省级集成数据中心（`trung tâm tích hợp dữ liệu`）、IOC/智慧城市控制中心、企业机房——逐省查询（矩阵表 explorer-industry.md §5）。
- 目录源（C）：Baxtel/DataCenterMap/Datacenters.com/OCOLO/Cloudscene——仅线索，需运营商/政府确认。

## 来源分级

- **A** = 官方/一手：运营商官方设施页/发布、省级人民委员会/厅页（具名项目/位置/状态）、投资登记证书、高科技/工业园管委会页、云提供商官方基础设施页、EVN 电力/变电站文档、MIC/VTA 官方页、政府采购记录（muasamcong.mpi.gov.vn，买家/包件证据）、运营商维护的 PeeringDB 精确互连地址。
- **B** = 强二级：DCD、ITA、VIR、The Investor、VietnamPlus/VNA、VnExpress、VietnamNet、ICTVietnam、Tuoi Tre、VOV、Bao Dau Tu、CBRE/C&W/Savills/JLL 具名项目报告、官方伙伴/承包商案例、行业协会。
- **C** = 弱线索：Baxtel/DataCenterMap/Datacenters.com/OCOLO/Cloudscene 单独引用、LinkedIn/社媒、付费市场报告摘要、无原始源的转载、只说省在招商的投资吸引文章、无后续的 MoU。
- 状态语义：`planned/announced`（MOU/意向）→ `approved`（投资政策批准/IRC/管委会批准）→ `construction`（动工/建筑许可/管委会公告/动工证据）→ `operational`（khánh thành/đưa vào vận hành/运营商页接受服务/云 GA）。
- 去重/标注：省级集成数据中心与商业 colo/hyperscale 分开；`MW IT` vs `công suất thiết kế` vs `công suất điện` 分开；2025 重组后新旧省名都检索，输出记旧 manifest 名、notes 记当前官方名；容量按阶段存储，未来全园区 MW 不当前容量。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=VN，divisions=63 省/直辖市；检索新旧名）。
2. **种子运营商宇宙**：Viettel IDC、VNPT、FPT Fornix、CMC、STT VNG、NTT/QD.TEK、Edge Centres、Hanoi Telecom、VNTT/Becamex、Gaw、Saigontel、SAM/VSIP、VNG、MobiFone。
3. **Tier 1 省全工作流**：Ho Chi Minh（SHTP/HEPZA/Tan Phu Trung/QTSC）、Ha Noi（Hoa Lac/Cau Giay/CMC Tower）、Binh Duong、Da Nang——官方+运营商+电力。
4. **Tier 2 工业/能源线索**：Dong Nai、Long An、BR-VT、Binh Dinh、Khanh Hoa、北部电子带（Bac Ninh/Hai Phong/Thai Nguyen 等）。
5. **Tier 3 省政府数据中心扫**：`trung tâm dữ liệu tỉnh`/`trung tâm tích hợp dữ liệu`/Sở TTTT/招标（muasamcong.mpi.gov.vn）——小公共设施单独标注。
6. **验证**：IRC/官方运营商发布/园区管委会/动工或建设证据后才升 approved/construction；容量按字段分开；输出 world 同 schema，无项目 division 写 `no_projects: true`。
7. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:15Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核越南数据中心（63 divisions，新旧省名映射）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Viettel Tan Phu Trung 140 MW 首期 2026 状态、CMC SHTP hyperscale 120 MW 获批后动工、STT VNG HCMC2 60 MW、SAM DigitalHub VSIP 3 150 MW 是否有 IRC/建设、KBC/AIC 200 MW 是否走出 MoU、AWS 越南后续（Local Zone→区域？）、G42/FPT 主权 AI 云项目载体与投资证书、Evolution/Hathor SHTP 项目。
