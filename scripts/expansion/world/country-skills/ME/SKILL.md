---
name: me-datacenter-methodology
location: scripts/expansion/world/country-skills/ME/SKILL.md
description: |
  Montenegro (ME) datacenter discovery & audit methodology — how to enumerate, verify, and update Montenegro datacenter projects at municipality granularity. Montenegro has no public national datacenter registry: enumeration joins Ministry of Spatial Planning (MUPD) UTU/building-permit indexes, municipal planning/permit pages, public procurement (CEJN/portalujn), EKIP telecom records, REGAGEN/CGES/CEDIS/EPCG energy records, EPA environmental permits, operator pages, official cloud-region lists (no hyperscaler region — negative control), and trade press. Montenegrin/BCS terms first (data centar, građevinska dozvola, urbanističko-tehnički uslovi). Read this before running ME exploration/audit batches. Routes to explorer-official.md (official/regulatory/cloud pipeline) and explorer-industry.md (trade press / vendor discovery).
---

# ME · 黑山数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：黑山**没有**公共全国数据中心注册库；枚举按**市级**粒度，拼接：国家空间规划部（MUPD）UTU/建筑许可索引、市政规划/许可页、公共采购（CEJN/portalujn）、EKIP 电信证据、REGAGEN/CGES/CEDIS/EPCG 能源记录、EPA 环评许可、运营商页、云厂商官方区域表（负向对照）与行业媒体。
> 黑山是**小型电信与政府主导市场**，非超大规模云区域市场；高置信度物理线索集中在电信/政府/公用事业设施：Crnogorski Telekom Data Centar Podgorica、One Montenegro carrier-neutral 数据中心、政府数据中心/容灾规划、EPCG/CEDIS/CGES 在 Nikšić 钢铁厂综合体的 Konsolidovani Data Centar。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供黑山探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：MUPD UTU/建筑许可页、市政许可门户（Podgorica/Bar/Kotor/Nikšić 等）、EPA 环评、REGAGEN/CGES/CEDIS/EPCG 能源与电网、EKIP 电信登记与服务公告、政府可行性研究与采购、云区域负向对照、运营商种子、市级工作流与可靠性规则 |
| `explorer-industry.md` | 行业/厂商发现：运营商扫描（Telekom/One/Telenor/MTEL/BeeNET/Tehnopolis/Cikom）、4iG 国家项目、承包商案例（IBT）、Vijesti/DCD/Balkan Green Energy News 媒体、ICT Cortex/PKCG 协会、目录（C 级）、逐市配方（高/中/低产出）、目录→一级核验工作流、容量与状态提取 |

## 核心结构事实（框定每次搜索）

1. **无全国数据中心注册库**：建筑证据分属国家与市政两级——MUPD 发布 `urbanističko-tehnički uslovi`（UTU）、`građevinske dozvole` 等决定；市政页（Podgorica、Bar、Kotor、Nikšić 尤佳）发布本地 UTU/建筑/使用许可扫描件与年度索引。
2. **黑山语/BCS 优先**：`data centar`、`državni data centar`、`konsolidovani data centar`、`kolokacija`、`server sala`、`računarski centar`、`cloud usluge`、`virtual data centar`、`građevinska dozvola`、`upotrebna dozvola`、`urbanističko-tehnički uslovi`、`trafostanica`、`agregat`、`UPS`、`hlađenje`；英文补充。
3. **生命周期层级**：`prostorni plan/DUP/LSL` < `UTU` < `idejno rješenje/saglasnost glavnog arhitekte` < `građevinska dozvola/odobrenje za građenje` < `prijava radova/izvođenje radova` < `upotrebna dozvola` < `otvoren/pušten u rad/operativan`。
4. **规划记录常写泛称**：`poslovni objekat`、`infrastrukturni objekat`、`telekomunikacioni objekat`、`objekat od opšteg interesa` 而非 `data centar`——按法人实体与地址搜，不只按数据中心词。
5. **无超大规模公共云区域**：AWS/Azure/GCP/OCI 官方区域表无黑山——本地 `cloud`/`virtual data centar`/VPS/转售页仅服务线索，除非官方区域页点名黑山。
6. **容量极少披露 MW**：保留代理指标——m²、机架数、认证标准（ISO 27001/27701）、冗余层级、UPS/发电机/消防范围、项目金额；第三方目录容量（如 Telekom 150 kW）默认 C 直到一级来源确认。
7. **歧义与变体**：`Data centar` 可指公共机构服务器机房/电信网络设施/云产品/真 colo，须记录设施类型；运营商总部地址 ≠ 数据中心地址；Niksic/Nikšić、Žabljak/Zabljak、Kolašin、Plužine、Rožaje、Šavnik、Herceg Novi 及西里尔变体都要搜；市政 PDF 多为扫描件，必要时 OCR。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§4 / explorer-industry.md §1-§4）

- 官方：`site:gov.me/mdup "data centar"`、`site:gov.me/mdup "građevinska dozvola" "data centar"`、`site:gov.me "Državni data centar"`、`site:podgorica.me "data centar"`、`site:{市政域} "građevinske dozvole" "{运营商}"`、`site:{市政域} "upotrebne dozvole" "data centar"`。
- 环评：`site:epa.org.me "data centar"`、`site:epa.org.me "procjena uticaja" "data centar"`、`site:sekretarijat-za-ppor.podgorica.me "data centar"`。
- 能源：`site:cedis.me "Konsolidovani Data Centar"`、`site:epcg.com "Konsolidovani Data Centar"`、`site:cges.me "trafostanica" "Nikšić"`、`site:regagen.co.me "zatvoreni distributivni sistem" "data centar"`、`"data centar" "trafostanica" "Crna Gora"`。
- 电信：`site:ekip.me "Data Centar Podgorica"`、`site:ekip.me "kolokacija" "Crnogorski Telekom"`、`site:ekip.me "Registrovani operatori elektronskih komunikacija"`。
- 采购：`site:cejn.gov.me "data centar" OR "serverska sala" OR "kolokacija"`、`site:portalujn.gov.me "Data Centar"`、`site:gov.me "javna nabavka" "data centar"`、`site:gov.me "Studija izvodljivosti" "Državni data centar"`。
- 运营商 pivot：`"{运营商}" "data centar" "Podgorica"`、`"{运营商}" "kolokacija servera"`、`"{运营商}" "MTKC" OR "Moskovska" OR "Bulevar Svetog Petra Cetinjskog"`。
- 行业：`site:vijesti.me "data centar" "Crnogorski Telekom"`、`site:datacenterdynamics.com Montenegro "data center"`、`site:balkangreenenergynews.com Montenegro "data center"`、`site:4ig.hu "Montenegro"`。
- 云负向：`site:aws.amazon.com/about-aws/global-infrastructure/ Montenegro`、`site:cloud.google.com/about/locations Montenegro`。

## 官方/监管管线要点（详见 explorer-official.md）

- **MUPD（A）**：UTU 与建筑许可页（请求/签发/拒绝/中止/中断状态）；eParcela 仅服务路由证据，具体许可回 MUPD/市政记录核验。提取：机关、文号、日期、申请/投资人、设计/审查、市、地籍市、宗地/UP、计划/DUP/LSL、地址、工程描述、面积、用途、变电/发电引用、状态链。
- **市政门户（A）**：Podgorica 规划/许可秘书处（Građevinske dozvole、Upotrebne dozvole、Odobrenje za građenje、UTU 年度索引）、Bar（建筑/使用/UTU/公共利益对象决定/合法化）、Kotor 年度索引（2025/2024/2023…）、Nikšić PDF API（`api.niksic.me/uploads/...`，搜 `Željezara`/`KDC`/`EPCG`/`CEDIS`/`CGES`/`data centar`）。
- **EPA / 市政环评（A）**：`elaborat procjene uticaja`、EIA 研究/决定、综合许可；发电机数/燃料、UPS/电池、冷却、变压器/变电站、用水、噪声与空气排放条件。
- **能源（A）**：REGAGEN（能源监管、牌照登记、封闭配电系统）、CGES（TSO：十年输电网发展规划 PDF、变电站工程、TSO 数据中心/DR 提及）、CEDIS（DSO；官方公告——**Konsolidovani Data Centar 位于 Željezara Nikšić 工业综合体**，未来可服务其他机构/企业）、EPCG。
- **EKIP（A=电信监管/运营商登记）**：运营商登记决定（Crnogorski Telekom、One Crna Gora、MTEL、Telemach、Domena/DoMEn、Čikom、Logate、Data Design 及 ISP）；`Data Centar Podgorica` 施工服务公告（A/B 运营证据）。
- **政府/采购（A=意向，非状态）**：State Data Center + State DR Center 可行性研究（要求 Tier3+ 标准，gov.me/wapi.gov.me PDF）；CEJN 公共采购、portalujn.gov.me 遗留记录；采购词 `Data Centar`、`server sala`、`UPS`、`agregat`、`hlađenje`、`virtualizacija`。
- **云**：无超大规模区域（负向对照）；运营商/集成商线索（Schneider/Vertiv/Huawei/Cisco/Nutanix/VMware/HP）可补设施服务证据。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 已确认/高值运营商种子：**Crnogorski Telekom**——Data Centar Podgorica（官方开园页，2020-07-06 与 EKIP 领导共同开园；MTKC 2019 年施工招标；`kolokacija servera` 官方页）+ **Bijelo Polje DR 中心**（2011 开园，Deutsche Telekom 标准）——均为 A/B；**One Montenegro**（前 Telenor；2015 建设、780 m²、ISO 27001/27701 语境，carrier-neutral 官方页，A/B）；**Tehnopolis Nikšić**（孵化器/创新中心官方设施页，A，小型研发设施非批发 colo）；**EPCG/CEDIS/CGES KDC**（Željezara Nikšić，2025 宣布，计划中——官方 CEDIS 公告 A，行业版 B）；**4iG 国家 Tier III 数据中心**（4iG 公司项目页 A，DCD/行业 B，具体市/场地未公开——Podgorica 占位，计划中）；MTEL Virtual Data Centar（服务线索 B/C）；BeeNET（未验证服务/设施线索）；Cikom/央行 Žabljak DR 微型数据中心（B 企业级 DR，非商用 colo）；IBT 承包商案例（Telenor THQ 消防/安全工程 B/C、Pljevlja 工作包 C/B）。
- 媒体（B）：Vijesti（Telekom Podgorica/Bijelo Polje、One/Telenor 认证、Cikom/央行、项目公告的最佳本地来源）、DCD（4iG/匈牙利协议——**未披露地点/容量，不得据此建设施**）、Balkan Green Energy News（KDC、绿色数据中心政策）、Montenegro Business（B/C，实体名/日期有用，须一级核验）、CDM/Bankar.me/Investitor.me/Pobjeda/RTCG。
- 协会（B/C）：ICT Cortex（黑山 ICT 协会成员生态）、PKCG 商会（`data centar`/`digitalna infrastruktura`/`cloud` 语境）。
- 目录（C）：DataCenterMap Montenegro（Podgorica/Bijelo Polje，含 Victoria Group 旧条目——可能已停用）、Data Center Catalog、Inflect（Telekom CG TGD01 地址/电力种子）、Cloudscene、PeeringDB、Colomap。

## 来源分级

- **A** = 官方/一手：MUPD 或市政 UTU/建筑/使用许可、EPA 或市政 EIA 决定、REGAGEN/CGES/CEDIS/EPCG 官方项目或许可记录、EKIP 监管记录、运营商官方数据中心/开园/招标页、政府会议材料或官方采购文件、云厂商官方区域页。
- **B** = 强二级：DCD、Balkan Green Energy News、Vijesti、RTCG、Mina、引述具名方的可靠本地商业媒体、具名场地的承包商案例研究、具名方但非原始来源的公司/交易所公告。
- **C** = 弱/未验证：DataCenterMap、Inflect、Datacenters.com、Cloudscene、Colomap、LinkedIn、SEO 托管页、转售 `cloud` 页、泛泛虚拟服务器产品。
- **状态语义**：政府可行性研究与政策声明对「意向」是 A 级，对「运营状态」不是——须有许可、招标、建设、移交或开园证据；`planned` 直到采购/政府验收/运营商开园/场地建设证据出现。
- **容量规则**：披露什么存什么（m²、机架、ISO、Tier、UPS/发电机/消防范围、项目金额），不编 MW；`capacity_mw: null` 并记代理指标。
- **政策/声明 ≠ 项目容量**：匈牙利基础设施协议、绿色数据中心国策、KDC 意向书——无具名场地+许可/招标/开园不计设施；老建筑程序记录（`odobrenje za građenje`）不得丢弃。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=ME，divisions=市：Podgorica、Nikšić、Bar、Budva、Kotor、Tivat、Bijelo Polje、Pljevlja、Herceg Novi、Ulcinj、Cetinje、Danilovgrad 及北部/小市）。
2. 每市执行：MUPD UTU/许可页 → 市政规划/许可年度索引 → EKIP 运营商与服务公告 → REGAGEN/CGES/CEDIS/EPCG 电网/变电站/封闭配电 → EPA/市政环评 → CEJN/portalujn 采购。
3. 高产出市：Podgorica（电信总部、政府项目、4iG、BeeNET/m:tel/One/Telekom）、Nikšić（Tehnopolis、KDC/Željezara）、Bijelo Polje（Telekom DR）、Pljevlja（Telenor 承包商线索）、Žabljak（央行/Cikom DR）；沿海市（Bar/Budva/Kotor/Tivat/Herceg Novi/Ulcinj）须排除旅游/房地产/电缆假阳性。
4. 运营商 pivot：EKIP 持牌运营商 → 官方设施/招标/许可/采购；目录种子（DataCenterMap/Data Center Catalog/Inflect）→ 官方域精确串 → 本地媒体开园/认证史 → CEJN 采购 → GOV.ME 部委 → 仍仅目录则记 C 并点名缺什么证明。
5. 容量/状态提取：保留代理指标；KDC 与 4iG 保持 `planned`；Tehnopolis/Cikom 按小型研发/企业内部设施归类。输出 world 同 schema；无项目 division 写 `no_projects: true`。
6. 遵行 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:50Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：探索/复核批次按市分桶；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：EPCG/CEDIS/CGES KDC 在 Željezara Nikšić 的许可/采购/建设进度；4iG 国家 Tier III 数据中心确切场地；One Montenegro 现行设施页与地址；MTEL/BeeNET 物理设施证据；Telekom Data Centar Podgorica 与 Bijelo Polje DR 的当前运营状态与容量。
