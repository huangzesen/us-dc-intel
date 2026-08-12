---
name: nr-datacenter-methodology
location: scripts/expansion/world/country-skills/NR/SKILL.md
description: |
  Nauru (NR) data-center enumeration methodology. Division model: 14 districts (Aiwo, Anabar, Anetan, Anibare, Baitsi/Baiti, Boe, Buada, Denigomodu, Ewa, Ijuw, Meneng, Nibok, Uaboe, Yaren); treat the country as one market and tag a district only when a primary source gives one. No verified commercial colocation, hyperscale, cloud region, AI/HPC campus, or carrier hotel; realistic official inventory is the EMC Nauru cable landing station, the government ICT Center (Yaren), Cenpac Net/Digicel operator rooms, and future donor-funded national hosting projects. Power is a hard filter: NUC reports ~5-6 MW peak demand (annual report: 11.6 MW firm capacity, 5.3 MW max demand) — any multi-MW DC claim is nationally material. Key facts: EMC landed Nauru 2025-08-09, AUD135m, expected RFS Nov 2025; current law is the Communications and Broadcasting Act 2018 (repealed the 2017 Act). Read this before running NR exploration/audit batches. Routes to explorer-official.md (government/RONLAW/EMC/NUC playbook) and explorer-industry.md (cable/operator/negative-check playbook).
---

# NR · 瑙鲁数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：瑙鲁为约 21 km2 的单岛微型国家，无任何经核实的商业 colo/超大规模/云区域/AI-HPC/运营商中立机房市场。枚举以「政府 ICT + 监管 + 海缆登陆 + 电力」为主，把全国当一个市场，分区标记只在来源给出区/地址时进行。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：政府门户/ICT 部、RONLAW/2018 年通信与广播法、EMC/NFCC 海缆链、AIFFP/DFAT/ADB/WB 项目文件、NUC 电力、云区域负面、14 区逐区策略 |
| `explorer-industry.md` | 行业/厂商管线：海缆行业源、Cenpac/Digicel 运营商、colocation/云/AI 负面核查、贸易媒体、中文谣言观察 |

## 核心结构事实（框定每次搜索）

1. 行政区划：**14 个 repo 分区** = Aiwo、Anabar、Anetan、Anibare、Baitsi/Baiti、Boe、Buada、Denigomodu、Ewa、Ijuw、Meneng、Nibok、Uaboe、Yaren。议会页将 14 区归为 8 个选区（Aiwo；Anabar=Anabar/Anibare/Ijuw；Anetan=Anetan/Ewa；Boe；Buada；Meneng；Ubenide=Baiti/Denigomodu/Nibok/Uaboe；Yaren）。完整核验：https://www.nauru.gov.nr/parliament-of-nauru/about-parliament/who-comprises-parliament.aspx 。搜索须同时用 **Baitsi 与官方拼写 Baiti**。
2. **无核实市场**：无商业 colo 提供商、无超大规模云区域（AWS/Azure/GCP/Oracle OCI 官方区域页未列 NR，2026-08-12）、无 AI/HPC 园区。现实官方盘点 = ① EMC 瑙鲁海缆登陆站；② Yaren 政府 ICT Center/服务器机房；③ Cenpac Net / Digicel 运营商机房；④ 未来捐助国资助的国家数据托管/数字政府云/网络安全项目。
3. **CLS 不是数据中心**：登陆站为电信设施；仅当 NFCC 或运营商在该站点宣传机架/托管/互联服务才加 colocation/互联。CLS 精确区/地块在已审公开来源未披露——不得臆断 Anibare/Yaren/Aiwo，保留 `Unknown NR`。
4. **电力为硬过滤**：NUC 官网称岛上峰值需求约 5-6 MW（近 12 个月）；年报给出 11.6 MW 固有能力、5.3 MW 最大需求。任何多 MW 数据中心声明在国家层面意义重大，需要一手电力/采购证据。NUC 主办公室：Aiwo District Power House；招标门户 https://www.tenderlink.com/nuc/ 。
5. **现行法修正**：现行通信法为 **Communications and Broadcasting Act 2018**（设立 Nauru Communications Authority），废除了 2017 年 Telecommunications and Regulatory Affairs Act。引用现行法用 2018 年法案（RONLAW https://ronlaw.gov.nr/ ；WIPO 镜像 https://www.wipo.int/wipolex/en/text/580197）；2017 年文件仅历史参考。Nauru Cable Corporation Act 2017 设立 NFCC 管理海缆与批发带宽（ADB 文件佐证）。
6. 政府 ICT 基线：ICT 部位于 **ICT Center, Yaren District**（https://www.nauru.gov.nr/government/departments/department-of-telecommunications.aspx），负责全部政府通信与信息系统、运营政府网络/互联网/邮件/Web 服务、26 名员工。A 级政府服务器机房线索，但本身不是公共 DC 计数。国家数字转型战略 PDF（https://www.nauru.gov.nr/media/204028/nndts_final_version_2025.pdf）含数字政府云战略目标，为 planned-policy 证据，非设施。
7. 常见误报：把 CLS 当商业 DC；用已废止的 2017 年法案；把政府 Moodle、学校机房、Meneng 地区处理中心（难民/拘留设施）、酒店、网络意识项目当 DC；把 Starlink/O3b/Kacific/Intelsat 接入当 DC 基建；接受「Unknown Nauru Data Center」类目录页或通用建设/选址营销页（C 级）。

## 查询模式（复制粘贴模板见 explorer-official.md §2 与 explorer-industry.md §3）

- 政府/法律：`site:nauru.gov.nr ("data centre" OR "data center" OR datacenter OR "server room")`、`site:nauru.gov.nr (tender OR procurement OR contract OR gazette) (ICT OR server OR cloud OR cybersecurity)`、`site:ronlaw.gov.nr ("Communications and Broadcasting Act" OR "Nauru Communications Authority" OR "Nauru Fibre Cable Corporation")`。
- 海缆/CLS：`"Nauru" "cable landing station"`、`"Nauru" "beach manhole"`、`site:eastmicronesiacable.com Nauru`、`site:naurufibrecable.com (Nauru OR Naoero) (landing OR "ready for service" OR wholesale OR backhaul)`、`site:aiffp.gov.au Nauru "East Micronesia Cable"`、`site:dfat.gov.au "East Micronesia Cable" Nauru`、`filetype:pdf "East Micronesia Cable" Nauru (BMH OR "beach manhole" OR "landing station")`。
- 电力/许可：`site:nuc.com.nr ("Power Demand" OR MW OR diesel OR solar OR BESS OR "large customer")`、`site:tenderlink.com/nuc Nauru (substation OR generator OR transformer)`、`"Aiwo District Power House" Nauru (MW OR generator OR load)`。
- 开发金融/变化检测：`site:adb.org Nauru (ICT OR cable OR broadband OR "digital government")`、`site:worldbank.org Nauru (digital OR ICT OR connectivity)`、`site:aiffp.gov.au Naoero OR Nauru (digital OR cable)`、`"Nauru" ("data centre" OR "data center") (China OR 中国 OR 数据中心)`。
- 运营商：`site:cenpac.net.nr (hosting OR server OR DNS OR colocation OR "data centre")`、`"Cenpac Net" Nauru (server OR hosting OR colocation OR Aiwo OR "Civic Centre")`、`site:digicelpacific.com Nauru ("data centre" OR switch OR core OR LTE OR cable)`。
- 负面核查：`"Nauru" (colocation OR "colo" OR "rack space" OR "carrier hotel" OR "internet exchange")`、`"Nauru" (AWS OR Azure OR "Google Cloud" OR Oracle OR OCI OR "cloud region")`、`"Nauru" (GPU OR AI OR supercomputer)`、`site:datacentermap.com Nauru`、`site:cloudinfrastructuremap.com Nauru`。
- 太平洋贸易媒体（B）：`site:datacenterdynamics.com Nauru "East Micronesia Cable"`、`site:rnz.co.nz Nauru (cable OR internet OR Digicel OR Cenpac)`、`site:abc.net.au Nauru (cable OR internet)`、`site:pacificislandtimes.com Nauru (cable OR datacenter)`、`site:loopnauru.com Nauru (ICT OR cable)`。中文：`"瑙鲁" ("数据中心" OR "云" OR "算力" OR "海底光缆" OR "通信")`——中文/SEO 命中一律 C 级，除非 NFCC/瑙鲁政府/AIFFP/DFAT/ADB/WB/具名运营商佐证。

## 官方/监管管线要点（详见 explorer-official.md）

- 政府 ICT：政府门户 https://www.nauru.gov.nr/ ；ICT 部页（ICT Center/Yaren、政府通信系统范围、管理联系）；EMC 光纤项目页（历史 RFI 与早期范围）；数字转型战略页/PDF；政府名录 2025 PDF（https://www.nauru.gov.nr/media/202632/govt_directory_2025.pdf）；GIO 媒体发布/公报/公告页（ICT 采购、土木工程通知、任命、项目仪式、捐助公告）。设施解释：政府服务器机房/ICT 运营线索，非商业 DC。
- EMC 链（A 级）：EMC 官网（https://www.eastmicronesiacable.com/，项目页：2022 年开工四年项目、2025 年底交付、各登陆点建登陆站、2,250 km Tarawa-Pohnpei 主干、分支至 Nauru 与 Kosrae、连接 HANTRU-1、单纤对频谱共享、每国初始 100 Gbps、系统能力 10 Tbps、陆上设施含 CLS/海滩人孔/管道/近站回传）；NFCC 官网（https://www.naurufibrecable.com/，治理页指 NFCC 立法；登陆文章确认 2025-08-09 登陆、AUD135m、预计 2025 年 11 月 RFS）；AIFFP 投资页（AUD135m、最高 AUD65m 赠款、100% 赠款、Naoero Fibre Cable、经 Pohnpei 接 HANTRU-1）；AIFFP 土木工程文章（2024-11-01 开工：海滩人孔、管道、登陆站基础结构，目标 2025 年 12 月交付）；DFAT 里程碑三篇；ADB/WB 项目文件（设计/机构/成本/陆上基建史实；无公共区/地块，不得据此断言 Anibare/Yaren/Aiwo）。
- 电力：NUC（https://www.nuc.com.nr/）与年报（11.6 MW 固有能力、5.3 MW 最大需求）、tenderlink 门户。
- 云负面：AWS/Azure/GCP/Oracle 官方区域页，带日期记录。
- 候选处理：计数前最少 = 一个点名设施/项目及其功能的 A 级源，或运营商/政府官方页 + 一个独立 A/B 源；区级标记需来源地址/区或文档化的影像/地理编码步骤。预期记录：EMC Nauru CLS（NFCC/EMC，landed 2025-08-09，RFS 2025-11 待当期核验，division Unknown NR）；ICT Center（Yaren，运营中政府 ICT，非商业 DC）；Cenpac Net Inc/Nauru Internet Centre（Aiwo Civic Centre 地址，运营商/服务器机房线索）；Digicel Nauru（运营商线索，无 colo 公开证据，Unknown NR）；云区域/超大规模/colo（verified-negative）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场现实：无核实商业 colocation/DC 市场；Data Center Map 国家页为负面核查源；声称「Unknown Nauru Data Center」或通用建设/选址服务的条目为 C 级营销线索。
- 海缆行业源：EMC/NFCC（A）；nem Australasia 为 AIFFP 承包的项目协调单位（B+，优先 NFCC/AIFFP/EMC 的 A 级事实）；NEC 供应商稿（https://www.nec.com/en/press/202306/global_20230606_02.html，B+）；Submarine Cable Map / Submarine Networks（B/C）；DCD/SubTel Forum/Pacific Islands Times（B，仅当复制一手项目文件）。
- 运营商：Cenpac Net Inc（A 运营商身份/地址：ISP since 1998、.nr 注册局角色、Civic Centre, Aiwo District；ITU 2017 国家概况确认 Digicel+Cenpac 双结构、政府西侧光纤骨干；APNIC/BGP 为 B 网络元数据非设施）；Digicel Nauru（A/B 运营商在场；无 colo 证据；假设存在移动核心/交换基建但无公开 DC/colo 场地）。
- 扫描顺序：① EMC/CLS 状态（NFCC→AIFFP→EMC→nem→NEC→DFAT，确认 2025 年 11/12 月 RFS 是否达成或延迟）；② CLS 位置钉定（ADB/WB/ESIA PDF 与 NFCC/GIO 媒体，否则 Unknown NR）；③ Cenpac（官网→APNIC/BGP→托管/DNS/域名页→Aiwo 地址确认）；④ Digicel（官方页→海缆新闻→政府/Telstra 源→交换/核心位置证据）；⑤ 官方重叠（ICT 部与数字转型战略）；⑥ 电力过滤（NUC 页/年报/招标）；⑦ 14 区全扫（含 Baitsi/Baiti）；⑧ 每轮记录云/colo/AI-HPC/目录负面。

## 来源分级

- **A**：官方/一手——nauru.gov.nr、stats.gov.nr、RONLAW/官方法案文本、naurufibrecable.com、eastmicronesiacable.com、AIFFP/DFAT/ADB/WB 项目文件、NUC 官方页与年报、ITU、官方云区域页。
- **B**：强二手或项目侧——nem Australasia（EMC 项目协调单位）、NEC、SubTel Forum、海缆参考文献、DCD、APNIC/PeeringDB/BGP 工具（网络元数据）、RNZ/ABC/PACNEWS/Loop/Pacific Islands Times（引用具名官员或项目文件时）。
- **C**：弱/聚合——数据中心目录、通用厂商服务页、SEO 市场报告、社交媒体、无引用的中文/英文文章、BGP/断网监控（仅作路由线索）。

## 使用流程（探索/复核批次）

1. 读 ICT 部与数字转型战略 PDF，提取政府托管/云/网络安全/采购术语。
2. 跑 EMC/CLS 链：EMC 项目页 → NFCC 新闻 → AIFFP 投资/土木/登陆页 → DFAT 里程碑 → ADB/WB 设计文件；确认 RFS 状态。
3. 位置钉定仅在来源或影像流程确立地块/区之后；否则 division 保持 `Unknown NR`。
4. 查 NUC 电力需求/容量与大型客户/变电站工程。
5. 搜 RONLAW 现行通信/数据/网络/公用事业/土地/采购法。
6. 用表格扫全部 14 区（含 Baitsi/Baiti 两种拼写）。
7. 每轮记录云区域/colo/AI-HPC/目录负面，便于后续 diff。遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:09Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] 确认 EMC 瑙鲁 RFS：2025 年 11/12 月目标是否达成/延迟（NFCC/AIFFP 当期页）。
- [ ] CLS 区级钉定：ADB/WB/ESIA PDF、NFCC/GIO 媒体、影像流程。
- [ ] Cenpac：托管/机架/互联服务公开证据（升格或保持运营商机房线索）。
- [ ] 待核实：Digicel Nauru 交换/核心场地位置证据。
