---
name: th-datacenter-methodology
location: scripts/expansion/world/country-skills/TH/SKILL.md
description: |
  Thailand (TH) datacenter discovery & audit methodology — how to enumerate, verify, and update Thailand datacenter projects across Bangkok, 76 provinces, and Phatthaya (special city). Thailand has no single public planning-permit portal: build the census from BOI (Board of Investment) approvals/promoted companies, NBTC telecom-license registry, ONEP Smart EIA Plus environmental records, local building-control authorities (BMA/DPT/municipalities), EGAT/MEA/PEA/ERC power evidence, official cloud-region pages (AWS ap-southeast-7 launched 2025-01, Google asia-southeast3 Bangkok 2026-01, Azure Thailand South planned, Oracle Alloy/AIS), and operator pages (True IDC, AIS/GSA, NT/CAT, STT GDC, Equinix, CtrlS/NT, Telehouse, SUPERNAP, ETIX, INET, TCC, DayOne/GDS, Bridge, Digital Edge, NTT). Read this before running TH exploration/audit batches. Routes to explorer-official.md (BOI/NBTC/ONEP/power/cloud) and explorer-industry.md (Thai-language queries/trade press/estate pivots).
---

# TH · 泰国数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：泰国**没有**一个能可靠列出所有私有数据中心建筑许可的公共门户；普查需从 **BOI 批准/受促进公司**、**NBTC 电信牌照注册**、**ONEP Smart EIA Plus 环境记录**、**当地建筑主管机关（BMA/DPT/市政）**、**EGAT/MEA/PEA/ERC 电力证据**、**官方云区域页**与**运营商官方页**构建。
> 核心市场：**Bangkok + 大曼谷 + 东部经济走廊（EEC）**——Chon Buri、Rayong、Chachoengsao（BOI 批文反复点名 Bangkok、Chachoengsao、Chonburi、Pathum Thani、Rayong、Samut Prakan）。优先省带：Bangkok、Samut Prakan、Nonthaburi、Pathum Thani、Chon Buri、Rayong、Chachoengsao。
> 泰语与英语都要搜：`data center`/`IDC`/`colocation`/`cloud region` + `ศูนย์ข้อมูล`（数据中心）、`ดาต้าเซ็นเตอร์`、`ศูนย์ดาต้า`、`คลาวด์`（云）、`โคลเคชั่น`、`ศูนย์บริการข้อมูล`。本 skill 汇总两份探索报告（官方管线 + 行业发现），供泰国探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：BOI 批准与受促进公司、NBTC 电信牌照（运营商普查）、BMA/DPT/市政建筑许可、ONEP Smart EIA Plus、EGAT/MEA/PEA/ERC 电力、官方云区域（AWS/Google/Azure/Oracle Alloy-AIS）、运营商官方种子（True IDC/AIS-GSA/NT/STT GDC/Equinix/CtrlS）、分区枚举策略与状态规则 |
| `explorer-industry.md` | 行业/厂商发现：泰语关键词与状态词表、Thai 商业媒体（Bangkok Biz/Prachachat/Thansettakij/The Standard/Bangkok Post）、全球贸易媒体（DCD/W.Media）、运营商/开发商矩阵（STT、True IDC、GSA/AIS/Gulf、DayOne/GDS、Bridge、Digital Edge、NTT、SUPERNAP、Telehouse、ETIX、INET、NT、TCC、Empyrion、DIG、TikTok 等）、工业园/地块 pivot、77 省全扫字符串 |

## 核心结构事实（框定每次搜索）

1. **BOI 是最佳官方项目种子**：BOI/OSOS 新闻具名项目公司、省、投资额、有时给 **IT load MW**（例：2025 批 Bangkok/Chonburi/Rayong 三项目 909 亿泰铢、约 350 MW，含 WHA ESIE4 Rayong 的 Beijing Haoyang、Bangkok 的 Empyrion、Chonburi 的 GSA Data Center 02；2026 批 Chachoengsao 的 Skyline 200 MW、Chonburi 的 Bridge Data Centres IIO 134 MW；2025 全年 36 个数据中心项目、7,280 亿泰铢）。**BOI 批准≠建设/运营**，需许可/电力/运营商公告交叉。
2. **NBTC 电信牌照=最佳官方运营商普查**：searchtelecomlicense.nbtc.go.th 暴露公司名/注册号/牌照类型/授权服务（`Data Center`、`Colocation`、`Hosting`、`Cloud`）；非设施级，一个持牌人可运营多站。
3. **规划许可碎片化**：曼谷建筑许可走 BMA（webportal.bangkok.go.th / opencontract.bangkok.go.th），外府走当地市政/区建筑主管机关；工业园（IEAT/私园）与 EEC 当局页另有渠道；不要指望全国在线许可检索。
4. **ONEP Smart EIA Plus（eia.onep.go.th）**：数据中心可能落在建筑/能源/工业园/备用发电/基础设施类别而非独立 `data center` 类；按 SPV/工业园/县/泰英项目名搜；可揭示阶段、地块、发电机/冷却/用水、有时总电力。
5. **电力边界**：**MEA**=Bangkok/Nonthaburi/Samut Prakan；**PEA**=其余 74 府；**EGAT**=发电输电（2026 年强化 EEC 电网支持数据中心投资）；ERC=监管。用电力证据验证大 MW 声明与在建集群。
6. **云区域**（A=区域存在/状态）：AWS Asia Pacific (Thailand) Region `ap-southeast-7` 2025-01-07 上线（3 AZ，>US$5B）；Google Cloud Bangkok `asia-southeast3` 2026-01-21 上线（3 zone）；Azure **Thailand South 计划/意向**（未上线）；Oracle Alloy + AIS 本地超大规模云；TikTok/ByteDance 为 data hosting 批文（非自有设施，除非点名站点）。
7. **容量与去重**：BOI 常给 `IT Load`；运营商可能给 `power capacity`/`critical IT load`/`campus power`/`MVA`/全建 MW——只存阶段特定 MW，园区总规划单列；`Bangkok` 营销名常实际位于 Samut Prakan/Pathum Thani/Nonthaburi/Chonburi/Rayong；GSA 01/02/05、Bridge IIO/III、True IDC 批文、Digital Edge SPV 可能指不同阶段/站点，不合并。泰历（BE）=公历+543。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§4 与 explorer-industry.md §1/§7）

- 泰语核心词：`ดาต้าเซ็นเตอร์` `ดาต้า เซ็นเตอร์` `ศูนย์ข้อมูล` `ศูนย์ข้อมูลคอมพิวเตอร์` `ศูนย์คอมพิวเตอร์` `ศูนย์บริการข้อมูล` `อินเทอร์เน็ตดาต้าเซ็นเตอร์` `ไอดีซี` `IDC` `Data Center` `Data Hosting` `Cloud` `เซิร์ฟเวอร์` `คลาวด์`；状态词：`ขอรับการส่งเสริมการลงทุน`/BOI 申请=管线、`อนุมัติ`/`ไฟเขียว`=BOI 批准（A-）、`ลงนาม`/`MOU`=意向（C）、`เช่าพื้นที่`/`ซื้อที่ดิน`/`ตั้งอยู่ในนิคม`=土地信号（A-/B）、`วางศิลาฤกษ์`/`เริ่มก่อสร้าง`=在建、`เปิดให้บริการ`/`เปิดดำเนินการ`=运营声明。
- BOI：`site:boi.go.th "data center" "IT load" Thailand`、`site:osos.boi.go.th "Data Center" "Chonburi"`、`site:boi.go.th "ศูนย์ข้อมูล" "เมกะวัตต์"`、`site:boi.go.th "GSA Data Center"`。
- 牌照：`site:telecom-license.nbtc.go.th "Data Center" "Colocation"`、`site:nbtc.go.th "รายงานการอนุญาต" "Data Center"`、`searchtelecomlicense.nbtc.go.th "{operator}"`。
- 规划/建筑：`"{company}" "{province}" "ขออนุญาตก่อสร้าง"`、`"{project}" "ใบอนุญาตก่อสร้าง"`、`site:bangkok.go.th "data center" "building permit"`、`site:dpt.go.th "ศูนย์ข้อมูล" "ก่อสร้าง"`。
- 环境：`site:eia.onep.go.th ("ดาต้าเซ็นเตอร์" OR "ศูนย์ข้อมูล")`、`"{company}" "EIA" "นิคมอุตสาหกรรม"`、`"{province}" "ดาต้าเซ็นเตอร์" "รายงานผลกระทบสิ่งแวดล้อม"`。
- 电力：`site:egat.co.th "data center" Thailand`、`site:pea.co.th "ดาต้าเซ็นเตอร์" "ไฟฟ้า"`、`site:mea.or.th "data center" "Samut Prakan"`、`site:erc.or.th "data center" "direct PPA"`、`"{province}" ("สถานีไฟฟ้า" OR "หม้อแปลง" OR "สายส่ง") ("ดาต้าเซ็นเตอร์" OR "ศูนย์ข้อมูล")`。
- 云：`"AWS" Thailand Region "data centers located in Thailand"`、`"asia-southeast3" "Bangkok" site:cloud.google.com`、`"Thailand South" site:learn.microsoft.com azure`、`"AIS Cloud" "Oracle Alloy"`、`"Google" Thailand "Chonburi" "data center" WHA`。
- 媒体：`site:bangkokbiznews.com "ดาต้าเซ็นเตอร์" "IT Load"`、`site:prachachat.net "ดาต้าเซ็นเตอร์" "ชลบุรี" OR "ระยอง"`、`site:datacenterdynamics.com Thailand "{operator}"`、`site:w.media Thailand "{operator}"`。
- 工业园 pivot：`"Amata City Chonburi" ("data center" OR "datacenter")`、`"WHA Eastern Seaboard Industrial Estate 4" ("data center" OR "Haoyang" OR "AWS")`、`"WHA Eastern Seaboard Industrial Estate 5" "GSA Data Center"`、`"Gateway City Industrial Estate" "Skyline Data Center"`、`"Digital Park Thailand" CtrlS "data center"`。

## 官方/监管管线要点（详见 explorer-official.md）

- BOI（https://www.boi.go.th/en/index/ + OSOS https://osos.boi.go.th/EN/news/ ）：首批项目种子（A=批准/申请人/省/投资/IT load）；受促进公司库（A-/B+）。
- NBTC（https://www.nbtc.go.th/ + https://searchtelecomlicense.nbtc.go.th/ ）：运营商普查（A=牌照存在/法律运营权），按授权服务词搜；非设施级。
- 规划：BMA（https://www.bangkok.go.th/ + opencontract.bangkok.go.th 建筑检查仪表盘）、DPT（https://www.dpt.go.th/ ）、外府当地市政/区主管机关、IEAT 与私园、EEC 当局；本地许可命中只作状态证据（具名项目/地块/建筑类型/业主时 A）。
- ONEP Smart EIA Plus（https://eia.onep.go.th/ ）：IEE/EIA/EHIA 记录（A=项目存在/位置/环境状态）；缺失不证无项目。
- 电力：EGAT（https://www.egat.co.th/home/en/ ，2026 EEC 电网强化发布）、MEA（https://www.mea.or.th/ ）、PEA（https://www.pea.co.th/en ）、ERC（https://www.erc.or.th/ ）（A=电网就绪/服务区/连接/关税语境）。
- 云区域（A=存在/状态）：AWS `ap-southeast-7`（2025-01-07 GA，3 AZ）、Google `asia-southeast3` Bangkok（2026-01-21 GA，3 zone）、Azure Thailand South（planned）、Oracle Alloy/AIS Cloud（本地超大规模）、Alibaba/Tencent/Huawei（需官方页+BOI/NBTC 验证）。
- 运营商官方页（存在性 A，容量 B）：True IDC（East Bangna/Midtown Ratchada/Midtown Pattanakarn/North Muangthong，官方 150+ MW 全国）、AIS/GSA（GSA Samut Prakan 20+ MW 开工；AIS Data Center 页）、NT Data Center（9 个 DC/8 省：Bangrak、Nonthaburi 1/2、Sriracha、Phra Khanong、Chiang Mai、Khon Kaen、Hat Yai）、STT GDC（3 个 Bangkok DC、49 MW IT load；Hua Mak/STT Bangkok 园区）、Equinix（2024-10 宣布约 US$500M 分阶段进入泰国+Bangkok 购地——planned 直到官方 IBX 页/许可/BOI）、CtrlS/NT（Chonburi 10 英亩/25 rai、设计最高 150 MW、NT 为连接伙伴）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 泰媒：BOI News/OSOS（A）、Bangkok Biz News（B+，BOI 批准与省份额、泰语法人名/IT load）、Prachachat（B+，WHA/Google、BOI 董事会批准、工业园赢家）、Thansettakij（B）、The Standard Wealth（B，TikTok/data hosting 区分与政策）、Bangkok Post（B）、The Nation Thailand/Thai Enquirer（B-/C+）、Manager/Matichon/Thai PBS 地方媒体（C+/B-，反对/水/电/分区/EIA）。
- 全球媒体：DCD（B+，STT/DayOne-GDS/Bridge/True IDC/BOI/TikTok/CtrlS/Empyrion/NTT）、W.Media（B，BOI 批次/Digital Edge-B.Grimm/DIG）、Dgtl Infra/Capacity/Light Reading（B-/C+）、Mongabay（B 报告事实：Chonburi/Rayong 水/电/建集群）、DC Byte/C&W/JLL/CBRE（B/C 市场脉络）、Baxtel/DataCenterMap/Cloudscene/PeeringDB（C，遗留地址/互连站点线索）。
- 运营商/开发商矩阵要点：**Bangkok**（STT Hua Mak/One Bangkok、Telehouse、True IDC、INET、NT/CAT、AIS/CSL、TCC Empire、NIPA/PROEN、Stellar DC）；**Samut Prakan**（True IDC East Bangna、ETIX、GSA、TikTok data hosting、Freyr）；**Pathum Thani/Nonthaburi**（AIS Tellus、OneAsia/One As1a、North Muangthong）；**Chonburi**（Amata City、EECd/Digital Park Thailand、WHA/Amata/Pinthong、DayOne/GDS CTP1/CTP2 1GW 平台、Bridge QH101/IIO、Google/WHA、Digital Edge/B.Grimm BKK1 100MW Q4 2026、NTT Amata、SUPERNAP 2017 起运营、CtrlS、Doma/DIG 1.5GW 平台、Vistas、Datazone、TCC）；**Rayong**（WHA ESIE4/5、CPGC、Amata City Rayong、Map Ta Phut、GSA 05、Stratus、Galaxy Peak 160 MW、Beijing Haoyang 约 96/350 MW 批、AWS 站点传闻）；**Chachoengsao**（Gateway City、Bang Pakong/Ban Pho、Skyline 200 MW、TikTok、DIG）。
- 区域边缘（Chiang Mai、Khon Kaen、Phuket、Hat Yai、Nakhon Ratchasima、Ayutthaya、Nakhon Pathom、Surat Thani）：NT/CAT/AIS/True/INET 遗留 IDC、大学、省政府云；77 省全扫：英语+泰语模板 + BOI/NBTC/ONEP/PEA 检查后才 `no_projects`。

## 来源分级

- **A** = 官方/一手：BOI 批准发布/受促进公司库、NBTC 牌照注册、ONEP Smart EIA Plus、BMA/省/市政/DPT/工业园许可、EGAT/MEA/PEA/ERC 官方记录、官方云区域页（存在/状态）、运营商官方页/新闻（存在/位置/状态）、SET 上市公司文件/年报。
- **B** = 强二级：Bangkok Biz/Prachachat/Thansettakij/The Standard/Bangkok Post 具名项目事实、DCD/W.Media/Dgtl Infra、法律/监管分析（解释 NBTC/BOI 规则变化）、工业园开发商公告（Amata/WHA 官方）。
- **C** = 弱线索：Baxtel/DataCenterMap/Datacenters.com/Cloudscene/PeeringDB 单独引用、LinkedIn/社媒、聚合器、当地促销 MoU、无出处转载、经纪人报告摘要。
- 状态语义：`approved`（BOI 批准或官方许可，无建设证据）→ `construction`（官方动工/建筑许可/公用事业施工/运营商建设更新/EIA 文件）→ `operational`（官方开业/云 GA/运营商设施页接受服务/认证/事故报告具名/公用事业证据）；`planned/announced`=公司意向/购地/MOU/市场进入公告。
- 去重：按 `(最终母公司, 泰国 SPV, 园区/工业园, 省)` 匹配；云区域可能有多处未披露 AZ 设施——云区域记一条 cloud-infrastructure 记录，不拆成多个物理 DC；BOI data hosting 项目可能跨省安装服务器，仅官方点名省级站点才拆分。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=TH，divisions=78：Bangkok + 76 府 + Phatthaya）。
2. **BOI 扫描**：抓 BOI/OSOS 的 `data center`/`data hosting`/`IT load`/`MW` 及泰语等价词；建 SPV/省/投资/IT load/日期种子。
3. **NBTC 运营商扫描**：对每个 SPV/运营商与服务关键词查 searchtelecomlicense.nbtc.go.th；补牌照记录与别名。
4. **运营商/云扫描**：AWS、Google、Azure、Oracle/AIS、True IDC、AIS/GSA、NT、STT GDC、Equinix、CtrlS/NT 官方设施/区域页。
5. **许可/EIA 扫描**：ONEP Smart EIA Plus、BMA/地方当局/DPT、工业园页、EEC 页。
6. **电力验证**：EGAT/MEA/PEA/ERC 查省/站点；用供电辖区检验大 MW 声明。
7. **省负扫**：低信号省跑泰语+英语查询（BOI/NBTC/ONEP/PEA/地方）后才 `no_projects: true`；输出 world 同 schema。
8. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:15Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核泰国数据中心（78 divisions）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：AWS 泰国区域物理站点（Rayong 传闻，需 BOI/工业园/许可）、Google Chonburi/WHA 首个 DC 落地、Azure Thailand South 进展、Equinix 泰国进入（$500M）是否已有 IBX/许可、STT Bangkok 2（Q4 2026 服务）、DayOne/GDS 1GW 平台 vs CTP1/CTP2 阶段、Bridge IIO 134 MW 与 QH101 关系、DIG/Doma 1.5GW 平台状态、TikTok data hosting 与自有设施区分。
