---
name: gr-datacenter-methodology
location: scripts/expansion/world/country-skills/GR/SKILL.md
description: |
  Greece (GR) data-center enumeration methodology. Division model: 13 first-level administrative regions plus Mount Athos as explicit exclusion/negative-control. No single public datacenter registry; census joins Diavgeia transparency decisions, e-PRM environmental records, e-adeies building permits, ADMIE/HEDNO/RAEEY grid evidence, EETT telecom records, strategic-investment decisions (ependyseis.mindev.gov.gr), OpenBusiness operating notifications (Law 5069/2023 + JMD 96038/2024, effective 2025-03-01; thresholds >=200 kW IT for third-party DCs, >=1,000 kW self-use), GEMH registry, and official operator/cloud pages. Attica is the primary hub (grid-constrained): Microsoft Operations 4733 Hellas three-site strategic investment (Spata 19.2 MW, Koropi Sites 27/28 at 9.6 MW each). Azure Greece Central/Athens announced 2020 but not shown live on current Azure regions list — verify GA every run. Key seeds: Digital Realty/Lamda Hellix Athens campus + HER1 Heraklion, DATA4 Paiania, EDGNEX/Data In Scale Spata, Dromeus/Apto Spata, Serverfarm/ADMIE, OTE/Cosmote Rentis, Grid Telecom/Quadrivium Chania CLS + 20 MW campus, Lancom, Synapsecom, GR-IX Athens/Thessaloniki. Read this before running GR exploration/audit batches. Routes to explorer-official.md (Diavgeia/e-PRM/e-adeies/OpenBusiness playbook) and explorer-industry.md (operator/trade-press/market playbook).
---

# GR · 希腊数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：希腊无单一公共数据中心登记册，普查靠拼接 Diavgeia 透明决定、环境记录（e-PRM）、电子建筑许可（e-adeies）、电网证据（ADMIE/HEDNO/RAEEY）、电信监管记录（EETT）、战略投资决定、运营通知框架（Law 5069/2023 + JMD 96038/2024）与官方运营商/云页面。按事实分级，而非按项目分级。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：Diavgeia/FEK、OpenBusiness 运营通知框架、e-adeies/TEE、YPEN/e-PRM、ADMIE/HEDNO/RAEEY、EETT、GSIS G-Cloud、GRNET/GR-IX、战略投资门户、ΓΕΜΗ、14 分区逐区策略、生命周期词 |
| `explorer-industry.md` | 行业/厂商管线：DCD/Kathimerini/Naftemporiki 等媒体、目录/聚合器、运营商与项目种子表、云区域核查、14 分区行业路由、验证与去重规则 |

## 核心结构事实（框定每次搜索）

1. 行政划分：**13 个一级行政区 + 阿索斯山（Mount Athos/Άγιο Όρος）作为明确排除/阴性对照分区**。13 区：Eastern Macedonia & Thrace、Central Macedonia、Western Macedonia、Epirus、Thessaly、Ionian Islands、Western Greece、Central Greece、Attica、Peloponnese、North Aegean、South Aegean、Crete。
2. **无单一公共登记册**：以 Diavgeia（https://diavgeia.gov.gr，含 API/导出端点）强制公开决定（环境批准、市政决定、采购、公共部门 DC 项目）、FEK 法律（https://www.et.gr）、e-adeies 建筑许可（https://eadeies.gov.gr）、e-PRM 环境登记（https://eprm.ypen.gr）、ADMIE（https://www.admie.gr，TYNDP）、HEDNO/DEDDIE、RAEEY（https://www.raaey.gr）、EETT（https://www.eett.gr）、GSIS G-Cloud、GRNET/GR-IX、ΓΕΜΗ 商业登记（https://www.businessregistry.gr）为骨架。
3. **新数据中心运营框架是真实的许可路径（A 级）**：Law 5069/2023 + JMD **96038/2024**，自 **2025 年 3 月 1 日** 生效（OpenBusiness 公告 https://openbusiness-portal.mindev.gov.gr/oloklirothike-to-thesmiko-plaisio-gia-ta-data-centers/）。门槛：第三方服务 DC **≥200 kW IT 设备标称电功率**、自用 DC **≥1,000 kW**。环境批准仍独立（Law 5069/96038 不替代环境、建筑、消防、用地、并网许可）。
4. **Attica 为主枢纽但电网受限**：官方战略投资记录确认 **Microsoft Operations 4733 Hellas S.M.S.A.** 在 Attica 的三数据中心战略投资：Spata-Artemida Site 6 19.2 MW、Koropi/Kropia Sites 27/28 各 9.6 MW（https://ependyseis.mindev.gov.gr/en/stratigikes/erga/investment-in-data-centres-in-greece-2）。ADMIE 规划与 2025-2026 能源媒体描述大规模并网申请压力；并网申请 ≠ 建成容量。
5. **云区域页是种子而非设施登记册**：微软 2020 年正式宣布希腊数据中心区域；Azure 区域列表（https://learn.microsoft.com/en-us/azure/reliability/regions-list）2026-08-12 未显示 Greece Central，而微软全球基建页仍显示 Greece Central/Athens 为 coming soon——无当前 Azure CLI/API 或 GA 证据不得标记为上线。AWS/GCP/Oracle/IBM 无希腊官方区域。
6. **连通性为选址信号而非设施证据**：GR-IX（雅典/塞萨洛尼基）、DE-CIX、Grid Telecom、海缆登陆站、电信 PoP 指向潜在托管市场；登陆站 ≠ DC，除非来源明确说其位于或配属数据中心园区。
7. **希腊语优先**：`κέντρο δεδομένων / κέντρα δεδομένων / Κέντρα Δεδομένων / data center / datacenter / υποδομή νέφους / φιλοξενία εξοπλισμού / οικοδομική άδεια / άδεια δόμησης / γνωστοποίηση λειτουργίας / ΑΕΠΟ / ΜΠΕ / στρατηγική επένδυση / υποσταθμός / όροι σύνδεσης / ΑΔΑ`。
8. 容量规则：IT load MW / installed electrical power / grid connection MVA-MW / total site power / marketing campus capacity 分开字段；不得把欧元、公顷、机架或平方米换算成 MW；岛屿与克里特须先交叉核对电网/互联容量与地方环境批准。

## 查询模式（复制粘贴模板见 explorer-official.md §2 与 explorer-industry.md §3）

- 官方全希：`site:diavgeia.gov.gr "κέντρο δεδομένων" OR "data center"`、`site:diavgeia.gov.gr "data center" "οικοδομική άδεια"`、`site:diavgeia.gov.gr "data center" "γνωστοποίηση λειτουργίας"`、`site:diavgeia.gov.gr "{SPV or operator}" "data center"`、`site:eprm.ypen.gr "data center" OR "κέντρο δεδομένων"`、`site:eadeies.gov.gr "data center" "{municipality}"`、`site:et.gr "5069/2023" "κέντρα δεδομένων"`、`site:et.gr "96038/2024" "Κέντρα Δεδομένων"`、`site:admie.gr "data center" OR "όροι σύνδεσης"`、`site:raaey.gr "data center"`、`site:grnet.gr "data center" OR "Daidalos" OR "GR-IX"`。
- 项目级：`"{operator}" "{SPV}" "ΑΔΑ"`、`"{operator}" "{municipality}" "ΑΕΠΟ"`、`"{operator}" "{municipality}" "ΜΠΕ"`、`"{operator}" "{municipality}" "οικοδομική άδεια"`、`"{project name}" "στρατηγική επένδυση" "data center"`、`"{site name}" "ισχύς" "MW" "data center"`。SPV/运营商 pivot：`MICROSOFT OPERATIONS 4733 HELLAS`、`DATA IN SCALE`、`EDGNEX`、`DAMAC`、`PPC/ΔΕΗ`、`LAMDA HELLIX`、`Digital Realty`、`DATA4`、`Dromeus`、`Apto`、`Serverfarm`、`Grid Telecom`、`Quadrivium`、`Lancom`、`Synapsecom`、`OTE`、`COSMOTE`、`Vodafone`、`Nova`、`GRNET`。
- 行业/目录：`site:datacenterdynamics.com/en/tags/greece/`、`site:kathimerini.gr "data center"`、`site:naftemporiki.gr "data center"`、`site:ot.gr "data center"`、`site:businessdaily.gr "data center"`、`site:energypress.gr "data center"`、`site:datacentermap.com/greece/athens/`、`site:baxtel.com/data-center/athens`、`site:peeringdb.com/ix/347`（GR-IX Athens：Digital Realty ATH1/2/3 为本地设施）、`site:submarinecablemap.com Greece`。
- 云/超大规模 pivot：`"Azure" "Greece Central" "coming soon" OR "available" OR "GA"`、`site:learn.microsoft.com "Greece Central"`、`"Microsoft Operations 4733 Hellas" "data center"`、`"AWS" Greece "region" OR "local zone"`、`"Oracle Cloud" Greece "public cloud region"`。
- 连接/IXP/海缆 pivot：`"GR-IX" Athens "Digital Realty" OR "facility"`、`"GR-IX" Thessaloniki members facility`、`"Chania" "data center" "cable landing station"`、`"Heraklion" "HER1" "Digital Realty"`、`"Tympaki" "2Africa" "Vodafone"`、`"BlueMed" Chania "data center"`。
- 状态词：意图/土地 = `MoU / memorandum / plans / πρόθεση / μνημόνιο / ανακοίνωση / συμφωνία`；许可证据 = `ΑΕΠΟ / ΜΠΕ / οικοδομική άδεια / γνωστοποίηση λειτουργίας / pre-approval`；在建 = `groundbreaking / under construction / έναρξη εργασιών / κατασκευή / εργοτάξιο`；运营 = `opened / launched / operational / live / λειτουργεί / θέση σε λειτουργία` + 接受 colo 订单的设施页或活跃 PeeringDB 本地设施。

## 官方/监管管线要点（详见 explorer-official.md）

- Diavgeia/FEK/e-PRM/e-adeies/OpenBusiness 决定为 A 级（设施/项目存在、法律发起人、地点、许可阶段、法定路径）。战略投资门户/部委项目页为 A 级（战略投资状态、实施实体、预算、官方站点/市镇与所列功率）。ADMIE/HEDNO/RAEEY 官方材料为 A 级（电网路径、连接约束、能源监管语境——不得从连接需求推断建成 DC）。EETT 运营商登记/决定为 A 级（公司/运营商地位，非设施数或容量）。云提供商官方页：区域公告/状态 A 级；物理设施数/地点 B 级除非有场地级公共记录。
- 状态规则：**operational** 仅当有运营通知/许可、运营商在用设施页、Uptime/认证绑定在用场地、活跃 PeeringDB/IX 证据或云区域 GA 证据；**under construction** 仅当建筑许可 + 承包商/运营商开工证据；**approved/planned** = 战略投资批准、AEPO、建筑许可/预批或官方运营商公告（与在用容量分开）。`μνημόνιο / πρόθεση / αναμένεται`、投资总额、GW 级汇总申请均视为非运营管线。
- 去重键：`legal SPV/proponent + municipality + campus/site name + permit/AEO/AEEP number + Diavgeia ADA + operator facility code`。重复陷阱：微软云区域 vs 三个 Attica 站点；`Microsoft` vs `Microsoft Operations 4733 Hellas`；EDGNEX vs DAMAC vs PPC vs `Data In Scale`；Lamda Hellix vs Digital Realty vs ATH1-5；登陆站 vs DC；政府/研究基建 vs 商业 colo；DEDDIE/ADMIE 连接申请 vs 建成设施。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场形态：无成熟全国行业协会或行业登记册；三角定位 = 官方运营商页 + 云区域页 + DCD/希腊贸易媒体 + GR-IX/DE-CIX/PeeringDB + 海缆公告 + 官方许可。主枢纽 Attica（东 Attica/Mesogeia：Koropi、Spata-Artemida、Paiania、Markopoulo、雅典市区）；次级 Thessaloniki/Central Macedonia 与 Crete；Volos/Thessaly 在市场报告管线列表但需一手确认。市场报告数字（Arizton、DataCenterMap、Baxtel、Datacenters.com、Mordor）仅线索。
- 项目种子表：**Microsoft Azure / Microsoft Operations 4733 Hellas**（Attica Spata 19.2 MW + Koropi 9.6 MW×2；战略投资页 A；区域公告 A；非 GA 不标记上线）；**Digital Realty / Lamda Hellix 雅典园区**（Koropi；Lamda Hellix 旧名并入 Digital Realty 去重；ATH1-5 按运营商页/许可/PeeringDB 核验）；**Digital Realty HER1**（Crete/Heraklion；官方设施页与 2025 新闻稿确认；DCD 报初始 1 MW IT 负荷可扩至 5 MW，Hill 报至 6.5 MW——容量按来源与字段记录）；**DATA4 Athens/Peania-Paiania 园区**（官方页 Agiou Louka 33；DCD 报奠基，Hill 报 DC1 5,200 m2/15 MW——计数 under-construction/未来容量前核验许可）；**EDGNEX (DAMAC 55% + PPC 45%) / Data In Scale**（Attica/Spata；PPC 官方稿确认 JV 与新项目；DCD 报 12.5-15.5 MW；计数前核验 Diavgeia/e-adeies/OpenBusiness）；**Dromeus Capital + Apto**（Spata 工业区；希腊/国际媒体强线索，需 Diavgeia/e-PRM/e-adeies 确认）；**Serverfarm + ADMIE/IPTO**（合作意向公告，监管 TSO 参与可能受 RAEEY 限制——A/B 公告，C 设施）；**OTE/COSMOTE**（Renti：Uptime 列 Rentis Data Center，Aktor 描述 OTE Renti 改造 1,500 m2/124 机架/500 m2 机房；目录其余站点 C+）；**Lancom**（Athens/Marousi、Thessaloniki/Balkan Gate、Heraklion 线索）；**Synapsecom**（Ano Liosia/Athens + Kalochori/Thessaloniki colo 页）；**Grid Telecom + Quadrivium**（Crete/Chania：新 Chania CLS 托管于 Quadrivium 20 MW Interconnection DC 园区内——CLS 与园区分开计数，园区状态经许可/运营商页核验）；**Sparkle/TIM**（Chania BlueMed/数据中心线索 B）；**Vodafone Greece**（Tympaki 登陆、Milos 路由——登陆非 DC 证据）；**Nova/United Group**（电信托管线索 B/C）；**GRNET/G-Cloud/Daidalos**（公共/研究基建，非商业 colo）。

## 来源分级

- **A**：官方/一手（该具体事实）：Diavgeia/FEK 决定、e-PRM 记录、e-adeies 建筑许可、OpenBusiness 运营通知、战略投资门户/部委项目页、ADMIE/HEDNO/RAEEY、EETT 登记/决定、云提供商官方区域页（区域公告/状态）、运营商设施专属页（存在性 A-）、ΓΕΜΗ。
- **B**：强二手/贸易/法律分析或部分确认事实的官方源：DCD、Kathimerini、Naftemporiki、OT.gr、Business Daily、energypress、The Tech Capital、Capacity、TeleGeography、Submarine Networks；运营商页容量/时间（未投运/未许可时）；Uptime 记录。
- **C**：目录、市场报告、本地推广文章、投机媒体：DataCenterMap、Datacenters.com、Baxtel、Arizton、Mordor、Cushman & Wakefield 语境。

## 使用流程（探索/复核批次）

1. 从官方云/运营商页与战略投资门户播种具名项目。
2. 经战略投资页、FEK/Diavgeia、ΓΕΜΗ 解析法律发起人/SPV。
3. 在 Diavgeia 搜 SPV、市镇、希腊生命周期词与 ΑΔΑ。
4. 在 e-PRM/YPEN 搜环境记录并匹配 Diavgeia AEO/AEEP 决定。
5. 在 e-adeies/TEE 与市政页搜建筑许可与预批。
6. 在 OpenBusiness 搜 Law 5069/JMD 96038 门槛以上设施的运营通知证据。
7. 查 ADMIE/HEDNO/RAEEY 连接与电网约束，申请/批准连接单独记录。
8. 查 EETT 运营商合法性与 GR-IX/PeeringDB 活跃互联证据。
9. 官方表面穷尽后才用行业/贸易媒体补漏，未核实事实降为 B 或 C。
10. 显式跑 14 分区表（含 Mount Athos 阴性对照与低优先岛屿区）。遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:14Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] Azure Greece Central：每轮核验 Azure 区域列表/API GA 状态。
- [ ] Microsoft 三站点：Diavgeia/e-adeies/OpenBusiness 逐站许可与运营证据。
- [ ] Digital Realty HER1 与 DATA4 Paiania：容量字段按来源核验，许可阶段确认。
- [ ] 待核实：EDGNEX/Data In Scale、Dromeus/Apto、Serverfarm/ADMIE 的许可与在建证据；Chania Quadrivium 20 MW 园区状态。
