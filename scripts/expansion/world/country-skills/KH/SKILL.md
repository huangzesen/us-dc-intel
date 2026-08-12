---
name: kh-datacenter-methodology
location: scripts/expansion/world/country-skills/KH/SKILL.md
description: |
  Cambodia (KH) datacenter discovery & audit methodology — how to enumerate, verify, and update Cambodia datacenter projects across Phnom Penh and 24 provinces. Cambodia has no public facility-level datacenter registry and little planning-permit visibility: enumeration triangulates MPTC datacenter licensing (2025-06-09 license notice), TRC telecom-operator lists (51 active operators), MLMUPC construction permits / One Window Service, CDC/QIP/SEZ investment approvals, MoE EIA records, EAC/EDC/MME power evidence, Uptime Institute certifications, operator pages (ByteDC, Chaktomuk PNH1, Telcotech/Royal Group, SINET, MekongNet), PeeringDB, and trade press. Khmer + English search. Read this before running KH exploration/audit batches. Routes to explorer-official.md (official/regulatory/cloud pipeline) and explorer-industry.md (trade press / vendor discovery).
---

# KH · 柬埔寨数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：柬埔寨**没有**公共设施级数据中心注册库，规划许可可见性很低；枚举靠四条通道三角测量：① **电信/数据中心牌照**——MPTC 牌照通知与 TRC 运营商名单确定合法实体；② **投资审批**——CDC 合格投资项目（QIP）公告（投资额、区、就业）；③ **运营商/厂商页**——最具体的设施事实（常缺 MW 与精确容量）；④ **行业媒体+目录**——DCD/W.Media/Khmer Times/Phnom Penh Post/Construction & Property/Uptime/目录补漏。
> 市场**压倒性集中在 Phnom Penh**，Kandal 周边有溢出可能；其余省份多为电信 POP/电子政务机房/云营销。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供柬埔寨探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：MPTC 数据中心牌照（2025-06-09 通知）、TRC 运营商普查、MLMUPC/市政/Khan 建设许可、CDC/QIP/SEZ、MoE/ODC EIA、EDC/EAC/MME 电力、云区域负向对照、设施种子表、8 级逐省策略（Tier1 Phnom Penh/Kandal → Tier2 → Tier3 轻扫）、验证与陷阱 |
| `explorer-industry.md` | 行业/厂商发现：英/柬语查询词表与阶段映射、政府/监管/协会来源表、运营商设施种子清单（ByteDC/Chaktomuk/Telcotech/National DC/Kepstar/Ezecom/SINET/MekongNet/Seatel/DPDC/HT Networks/Metfone/NeocomISP）、云区域检查（含阿里/华为/腾讯）、媒体与目录分级、逐省模板与中文 SEZ 扫描、容量/状态规则、工作流 |

## 核心结构事实（框定每次搜索）

1. **MPTC 数据中心运营牌照是合规基线**：2025-06-09 通知要求面向客户的托管/托管设备/安全/云（IaaS/PaaS/SaaS）等服务的设施须向邮电部申请牌照——这是规则/存在锚点，**不是牌照登记册**；2025-06 前活跃的运营商可能需新授权；牌照证据与设施存在分开记录。
2. **TRC = 运营商普查，非设施登记**：活跃运营商页（51 家，2025-08-11 更新，可下载 PDF）用于种子 ISP/电信实体——Ezecom、SINET、Telcotech、MekongNet、Metfone/Viettel、Seatel、HT Networks、NeocomISP/NTC、Chaktomuk Data Center Co Ltd、ByteDC/Urban Data Center 等；TRC 不给机架数/MW/地址。
3. **建设许可不集中可搜**：MLMUPC 为国家建设主管机关（One Window Service），项目按法律所有人/项目名/地块/街道/Khmer 词路由到 Phnom Penh 首都行政当局/省/区/Khan；大型/高层/特殊项目可能留在 MLMUPC；公开在线覆盖不全，无结果 ≠ 无许可。
4. **Phnom Penh 别名严重**：同一设施可叫 `ByteDC`、`Urban Data Center`、`Global IT Media Hub`、`PPCC`、`G-Tech`；去重按 (最终母公司, 设施/园区, 地址) 键；Telcotech/Royal Group 与 Ezecom/Telcotech/Royal Group 链、MekongNet/Angkor Data Communication 常以多品牌出现。
5. **无超大规模云区域**：AWS/Azure/GCP/OCI/阿里/华为/腾讯官方区域表无柬埔寨（邻近 SG/TH/MY/ID）——`available to Cambodian customers` ≠ 柬埔寨区域；云转售办公室 ≠ 数据中心。
6. **容量语义**：运营商常只公布机架或楼面不公布 MW；区分 `design capacity`、`critical IT load`、`built floor area`、`racks`，不得随意 rack→MW 换算；目录 MW（Baxtel/市场报告）存 B/C 并注明来源；Uptime 记录精确奖项类型——`Tier III Certification of Design Documents` ≠ 运营认证。
7. **语言**：英文用于行业媒体/运营商/外国投资者披露，Khmer（មជ្ឈមណ្ឌលទិន្នន័យ / អាជ្ញាបណ្ណ / សំណង់ / អគ្គិសនី）用于政府/本地媒体；中国投资 SEZ 还要扫中文（金边/西港/波贝/柴桢）；社交媒体仅官方部委/省页 + 文档图才算 C 以上。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§8 / explorer-industry.md §1-§6）

- 牌照/监管：`site:mptc.gov.kh "data center" "license"`、`site:mptc.gov.kh "អាជ្ញាបណ្ណ" "មជ្ឈមណ្ឌលទិន្នន័យ"`、`site:mptc.gov.kh "National Data Center"`、`site:trc.gov.kh "{运营商}" "Operators List"`。
- 建设/投资：`site:mlmupc.gov.kh "{运营商}" "data center"`、`site:mlmupc.gov.kh "សំណង់" "មជ្ឈមណ្ឌលទិន្នន័យ"`、`site:phnompenh.gov.kh "data center"`、`site:cdc.gov.kh "data center"`、`site:cdc.gov.kh "digital industries" "QIP"`、`"Cambodia" "QIP" "data center" "{运营商}"`。
- 环评：`site:moe.gov.kh "data center" Cambodia`、`site:opendevelopmentcambodia.net "data center" "EIA"`、`"{运营商}" "EIA" "Cambodia"`。
- 电力：`site:edc.com.kh "data center"`、`site:eac.gov.kh "{运营商}" "license"`、`site:mme.gov.kh "data center" "electricity"`、`"{项目}" "substation" "Cambodia"`。
- 云负向：`site:aws.amazon.com Cambodia "Region" "Local Zone"`、`site:cloud.google.com Cambodia "region"`、`site:alibabacloud.com Cambodia "region"`、`"Cambodia" ("cloud region" OR "availability zone") (AWS OR Azure OR OCI)`。
- 行业：`site:datacenterdynamics.com Cambodia "data center"`、`site:khmertimeskh.com Cambodia "data center"`、`site:phnompenhpost.com Telcotech "data center"`、`site:construction-property.com "data center" "CDC"`、`site:w.media Cambodia "National Data Center"`。
- Uptime/PeeringDB：`site:uptimeinstitute.com Cambodia "Data Center"`、`site:peeringdb.com Cambodia ("Phnom Penh" OR "data center")`。
- 中文：`"柬埔寨" ("数据中心" OR "云计算中心" OR IDC) ("金边" OR "西港" OR "波贝" OR "柴桢")`。

## 官方/监管管线要点（详见 explorer-official.md）

- **MPTC（A=牌照要求/已发牌照/国策/政府项目）**：2025-06-09 牌照通知、Digital Government Policy 2022-2035；政府 National Data Center 项目（Phnom Penh/Digital Park 管线，MPTC 部长与日本大使 2025-07 现场考察；DCD/Khmer Times 的 $30m/12 层/Tier IV 主张为 B 直到 MPTC 页确认）。
- **TRC（A=合法运营商存在）**：活跃运营商名单与电信统计；下载最新 PDF 提取 ISP/增值/网络运营商。
- **MLMUPC / 国家以下建设许可（A）**：建设许可、入住证书、楼高/层数、地契/地块、申请人、地址、机关、日期；法律/法规镜像（ODC/EuroCham/DFDL/BNG）仅用于理解路由。
- **CDC/QIP/SEZ（A=具名项目/公司）**：数字产业为激励行业，QIP 可得税务/海关激励，SEZ 提供一站式与公用设施——Telcotech Kampus 式项目的关键来源；投资促进文章仅 B。
- **MoE / EIA（A=批准/报告）**：Sub-Decree 72 流程；数据中心可能不以 `data center` 类别出现——按公司/地主/SEZ/备用发电机/燃料储存/冷却/输电线/道路工程搜；ODC EIA 数据集为公共补充。
- **EDC/EAC/MME（A=具名客户/电网项目/服务区/牌照/关税/并网）**：大型数据中心应留下高压接入、变电站扩容、专用馈线、变压器进口、购电/工业电价、备用发电机许可/EIA 或 SEZ 公用设施升级之一。
- **云**：无柬埔寨超大规模区域（负向对照，每次刷新前复核）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 设施种子（A=官方存在/B=容量）：**National Data Center**（政府，日本赠款，$30m、3 MW 报道——B，MPTC 为 A）、**ByteDC/Urban Data Center**（2023 开园、carrier-neutral Tier III 设计认证、3 MW、1,000 机架、Land 356 Street R-4/Srah Chork/Daun Penh；Uptime A、DCD B、上市公司档案 A）、**Chaktomuk Data Center PNH1**（Tier III Plus 设计认证，官方页/Uptime A，容量不公开）、**Telcotech / Royal Group Elite DC1**（carrier-neutral，AAG/MCT 海缆所有权为认真基建的证据，2025 Tier III 设计公告）、**Telcotech Kampus**（CDC 批准、$27.7m、Monivong/Tonle Bassac/Chamkarmon——已批准/开发中，非运营）、**Kepstar DC1/DC2**（Singtel 顾问、6.5 MW/3.5 MW 报道、~100 km 外 DR 场地——B/C，DC2 省未定，须谨慎）、**Ezecom**（Royal Group ISP/云，设施细节稀疏，种子+交叉核验）、**SINET**（3,000 m² Phnom Penh，B 咨询页）、**MekongNet IDC1/IDC2**（AnAnA/SunCity 楼、Norodom Blvd/Street 370，MW 不公开）、**Seatel**（2 MW 云 DC，容量多为目录衍生）、**Daun Penh Data Center/DPDC**（C）、**HT Networks HTN-IDC**（Street 114/7 Makara，小型）、**Metfone/Viettel Cambodia**（核心网络设施，PeeringDB org 9493——除非明确设施证据否则不计商用 colo）、**NeocomISP/NTC**（C 种子）。
- 媒体（B）：DCD（B+，ByteDC/Kepstar/联合体/MoU 史）、W.Media（B，National DC/Kepstar）、Khmer Times（B，就职/国策）、Phnom Penh Post（B，Telcotech 债券/Royal Group 基建）、Construction & Property Cambodia（B，CDC 批准/开工/公共建筑）、Open Development Cambodia（B/C 聚合）、Knight Frank Cambodia 2024-12 报告（B，市场/运营商列表，逐个核验）。
- 协会（B/C）：柬埔寨商会/EuroCham/AmCham/CAFT——数字经济活动与运营商会员线索；**无**全国数据中心协会，用商会+TRC+ICT 活动替代。
- 目录（C，佐证时 B）：Baxtel、DataCenterMap、DataCenters.com、Cloudscene、DataCenterJournal；PeeringDB（A-/B，活跃互联证据非容量）。

## 来源分级

- **A** = 一手/法律可追责：MPTC 牌照通知或已发牌照证据、TRC 运营商名单/统计、MLMUPC 或国家以下建设许可/入住证书、CDC/QIP/SEZ 记录、MoE EIA 批准、EDC/EAC/MME 电力记录、云厂商官方区域页、运营商官方设施页、Uptime Institute 证书、上市公司披露。
- **B** = 强二级：DCD、W.Media、Khmer Times、Cambodia Investment Review、Construction & Property Cambodia、Knight Frank/CBRE 等经纪报告（引述具名运营商）、引述柬法规的律所笔记、供应商/承包商项目页。
- **C** = 弱线索：Baxtel、DataCenterMap、DataCenters.com、PeeringDB（单独时）、招聘广告、社交帖、市场规模报告、SEO 目录；仅用于发现。
- 状态映射：`MoU`/数字中心雄心 = C 意向；`CDC/QIP 批准` = A-/B+（已批准，非运营）；`MPTC 牌照` = A（法律资格，非建成设施）；`Uptime TCDD/Tier III 设计认证` = A（设计认证，非在线服务）；`运营商 launched/inaugurated/服务页/PeeringDB 设施` = A-/B+（运营在场，容量可能仍 B/C）；`approved` / `construction`（开工/合同/供应商案例/官方进展）/ `operational` / `planned`（MoU/公告/市场管线）按此归类。
- **容量与去重**：Uptime 记录精确奖项类型；政府设施区分国家电子政务基础设施与商用 colo；目录过度计数（同名多条目/POP 混入）默认 C；5-10+ MW 声明应有 EDC/EAC/变电站/发电机/EIA/进口/建设痕迹。
- **政策/声明 ≠ 项目容量**：`largest data center` 声明、数字中心目标、无许可/建设的 MoU 不得计设施。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=KH，divisions=Phnom Penh + 24 省）。
2. 下载最新 TRC 运营商 PDF，提取全部 ISP/增值/网络运营商；以 Uptime + 运营商官方页 + DCD/Khmer Times/Knight Frank 建 Phnom Penh 设施种子（National DC、ByteDC、Chaktomuk PNH1、Telcotech/Elite DC1、Kampus、SINET、Kepstar、DPDC、Ezecom、Seatel、MekongNet、NeocomISP）。
3. 对每个法律名与 Khmer 名搜 MPTC 牌照通知/后续页；搜 MLMUPC/Phnom Penh/Kandal 许可 + CDC/QIP/SEZ 建设/投资证据；搜 EAC/EDC/MME 电力/服务区验证。
4. 逐省扫描：Tier1 Phnom Penh（Daun Penh/Srah Chak/Boeung Kak/Russey Keo…）与 Kandal（Techo 机场/KTI/Takhmao/Kandal Stueng/Ang Snuol 等溢出）；Tier2 Siem Reap/Battambang/Preah Sihanouk/Banteay Meanchey/Svay Rieng（SEZ/边境/旅游/DR 用例）；Tier3 其余 18 省轻扫（含中文 SEZ 扫描）。
5. 每次运行复核云厂商官方区域页；按 §7 层级核验容量/状态后写记录；无项目 division 写 `no_projects: true`（分支 POP/网络机房/电信交换单列）。
6. 遵行 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:55Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：探索/复核批次按省分桶（Phnom Penh 优先 → Kandal 溢出 → Tier2 → Tier3 轻扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：National Data Center 建设/移交时间线（MPTC/日本援助源）；Telcotech Kampus 开工与运营商开园证据；Kepstar DC1/DC2 状态与 DC2 确切省；MPTC 2025 牌照通知后各运营商的许可状态；Chaktomuk/MekongNet/Seatel 的 MW 与地址一级证据。
