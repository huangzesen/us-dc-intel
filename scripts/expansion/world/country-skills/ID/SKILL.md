---
name: id-datacenter-methodology
location: scripts/expansion/world/country-skills/ID/SKILL.md
description: |
  Indonesia (ID) datacenter discovery & audit methodology. No national facility registry; enumerate by joining five official trails: OSS-RBA / KBLI 63102 business licensing, SIMBG PBG/SLF building permits, AMDALNET environmental approvals, PLN / PLN Batam power agreements (PJBTL, MVA), and Komdigi PSE registration, plus official cloud-region pages (AWS Jakarta ap-southeast-3, Azure Indonesia Central, Google Cloud Jakarta, Alibaba ap-southeast-5) and official colo pages (DCI, NeutraDC/neuCentrIX, NTT, Equinix, STT, PDG, Digital Edge, BDx, DayOne). Division model: 38 provinces / special regions / capital district. Read this before running ID exploration/audit batches. Routes to explorer-official.md (OSS/KBLI, SIMBG, AMDALNET, PLN, PSE, cloud regions) and explorer-industry.md (trade press, province matrix, estate/power pivots).
---
# ID · 印度尼西亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为印度尼西亚数据中心枚举提供「官方许可 + 电力 + 云区域 + 运营商官网」四线并联的查询框架。印尼**没有全国性商业数据中心注册库**，必须把枚举问题拆成 OSS/KBLI 业务许可、SIMBG 建筑许可、AMDALNET 环评、PLN/PLN Batam 电力协议（PJBTL/MVA）、Komdigi PSE 注册五条官方线索，再与云区域页和运营商官网交叉验证。核心商业地理集中在**雅加达、西爪哇（Bekasi/Cikarang/Karawang）、万丹（BSD/Serpong）、廖内群岛（Batam/Nongsa/Kabil）、东爪哇（泗水）**。本 skill 汇总两份探索报告（官方管线 + 行业发现），供印度尼西亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：OSS-RBA & KBLI 63102、SIMBG PBG/SLF、AMDALNET、PLN/PLN Batam PJBTL、Komdigi PSE、官方云区域页（AWS/Azure/GCP/阿里云）、运营商官网设施页 |
| `explorer-industry.md` | 行业/厂商发现：DCD/W.Media/Antara/Bisnis/Kontan/CNBC/DetikInet/Kompas 等贸易媒体、运营商/开发商矩阵、园区与电力枢纽、38 省级逐省查询矩阵 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库**：OSS-RBA（https://oss.go.id/en）是业务许可注册，不是设施注册；KBLI 63102「Aktivitas Penyediaan Infrastruktur Komputasi, Hosting, dan Aktivitas Terkait」的 OSS 描述明确包含云基础设施、机房出租、数据中心托管等，可作为法定经营线索（A），但不能计数设施。
2. **建筑许可走 SIMBG**：大型园区需 PBG（Persetujuan Bangunan Gedung）与 SLF（Sertifikat Laik Fungsi），门户 https://simbg.pu.go.id/；选址兼容性看 OSS RDTR Interaktif / KKPR。DPMPTSP（市县投资与一站式服务局）页面常常比 SIMBG 更易索引。
3. **环评走 AMDALNET**：门户 https://amdalnet.menlhk.go.id/，搜索词 AMDAL / UKL-UPL / Persetujuan Lingkungan / PKPLH / RKL-RPL；小型托管或改造项目不会公开，缺失不等于负面证据。
4. **电力是印尼最强过滤器**：超大规模项目几乎必有 PLN / PLN Batam 供电协议（PJBTL）、MVA 连接容量、变电站工程与 REC 采购；门户 https://web.pln.co.id/、https://layanan.pln.co.id/、https://eproc.pln.co.id/；Batam 搜 `site:plnbatam.com data center PJBTL`。已知标杆：DayOne 与 PLN Batam 的 **511 MVA / 约 450 MW** 协议。
5. **云区域只证明市场存在**：AWS Asia Pacific (Jakarta) `ap-southeast-3` 3 AZ、Azure Indonesia Central 3 AZ、Google Cloud Jakarta、Alibaba `ap-southeast-5`；云区域/AZ 计数 ≠ 物理设施计数，须由许可、PLN、园区或备案佐证坐标。
6. **术语与省属陷阱**：印尼设施常以「计算基础设施、托管、办公楼、工业园区、电信设施、仓库/公用建筑」获批，不一定叫「pusat data」；「Jakarta」宣传名常实际位于西爪哇 Bekasi/Cikarang/Karawang 或万丹 Serpong/BSD，务必从地址/园区解析省份：Cikarang/Cibitung/Karawang/Purwakarta=西爪哇，Serpong/BSD/Pondok Aren=万丹，Kuningan/MT Haryono/TB Simatupang/CBD=雅加达。
7. **单位与状态词**：MVA 与 MW 不互相换算除非来源明确；阶段动词严格区分：`minat investor`/`MoU`/`kerja sama`（意向，C）、`akuisisi lahan`（拿地，B）、`PJBTL`/`kontrak listrik`（强电力信号，A-/B+）、`groundbreaking`/`peletakan batu pertama`/`topping out`（施工，B+）、`diresmikan`/`diluncurkan`/`beroperasi`（运营，须运营商页复核）。

## 查询模式（复制粘贴模板见 explorer-official.md §2 与 explorer-industry.md §2）

- `"pusat data" "{operator}" "{province_or_city}"` / `"data center" "{operator}" "{province_or_city}"`（印尼语优先，英语用于超大规模云厂与外资托管）
- `"PBG" "pusat data" "{city}"` / `"Sertifikat Laik Fungsi" "data center" "{operator}"` / `site:simbg.pu.go.id "PBG" "pusat data"`
- `site:amdalnet.menlhk.go.id "pusat data"` / `"AMDAL" "data center" "{operator}"`
- `"PJBTL" "data center" "{operator}"` / `site:pln.co.id "data center" "MVA"` / `"PLN" "pasok listrik" "data center" "{city}"`
- `site:pse.komdigi.go.id "{entity}"`（PSE 注册仅证实体，不作设施记录）
- `site:spse.inaproc.id "pusat data"` / `"Pusat Data Nasional" "tender"`（政府采购线）
- 状态词映射：dibangun/membangun=建设；beroperasi/diresmikan/diluncurkan=运营；kontrak listrik/PJBTL=供电协议；beban IT=IT 负载；gardu induk=变电站。

## 官方/监管管线要点（详见 explorer-official.md）

- **OSS-RBA / KBLI / NIB**：https://oss.go.id/en；KBLI 63102 https://oss.go.id/kbli/detail/4be9f0ac-583b-5323-9839-7372e1708032；KBLI 63101 https://oss.go.id/kbli/detail/cb1de852-fa0f-4ef2-adce-a001ad258d0d；RDTR Interaktif https://oss.go.id/en/rdtr-interaktif。用运营商法定名称开局：PT DCI Indonesia Tbk、PT Telkom Data Ekosistem / NeutraDC、PT NTT Global Data Centers Indonesia、PT Equinix Indonesia、PT Princeton Digital Group Data Centres、PT Digital Edge DC、PT BDx Data Centers、PT DayOne Data Centers。
- **SIMBG / PBG / SLF**：https://simbg.pu.go.id/；按设施代码与园区查询（JK1、JK6、JKT3、JKT2A、CGK、H1、H2、Nongsa Digital Park、GIIC、MM2100、Kabil、Ariobimo、Kuningan Barat），提取业主、建筑功能、地址、楼面、许可日期、SLF 状态。
- **AMDALNET**：https://amdalnet.menlhk.go.id/；搜 pusat data / data center / 运营商法定名称 / 园区名 / 变电站名。
- **Komdigi / PSE**：PSE Privat https://pse.komdigi.go.id/、PSE Publik https://pse.layanan.go.id/beranda、Komdigi https://www.komdigi.go.id/；仅作实体发现与受监管服务状态。
- **PLN / 电力**：https://web.pln.co.id/、https://layanan.pln.co.id/、https://eproc.pln.co.id/；高价值证据=PJBTL、MVA 连接容量、分期送电日期、变电站/馈线/变压器工程、REC 采购；西爪哇园区（GIIC、MM2100、KIIC、Karawang）与 Batam（Nongsa、Kabil）是重点。
- **云区域页**：AWS https://aws.amazon.com/local/jakarta/ + https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html（ap-southeast-3，3 AZ）；Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list + 发布 https://news.microsoft.com/id-id/2025/05/27/microsoft-opens-indonesia-central/（Indonesia Central，3 AZ）；GCP https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-in-jakarta-now-open + https://blog.google/intl/id-id/products/cloud/google-cloud-perluas-kapasitas-pusat-data-ai-di-indonesia/；阿里云 https://www.alibabacloud.com/en/global-locations（ap-southeast-5）。
- **运营商官方页（A 级存在性）**：NTT Jakarta 2（9.4 MW）/2A（12 MW）中央雅加达、Jakarta 3 勿加西（IT 负载最高 45 MW）；DCI E1 雅加达 19 MW、E2 泗水 9 MW、H1 Cibitung（含 JK6 36 MW）、H2 Karawang；Equinix JK1 Kuningan Barat（一期 550 cabinets，满配 1,600 cabinets / 5,300 sqm）；NeutraDC Cikarang/Batam/Serpong/Surabaya；neuCentrIX 19 个边缘点（Medan、Pekanbaru、Makassar、Jayapura、Manado、Banjarmasin、Tanjung Karang、Pugeran 等，仅披露机架数时勿推断 MW）。
- **B 级容量信号**：STT GIIC/Cikarang 园区（360 MW 长期叙事）、PDG JC1/JC2 Cibitung + JC3 GIIC Kota Deltamas（12 亿美元 120 MW）+ JC4、Digital Edge EDGE1/EDGE2 雅加达 + CGK 园区（GIIC Bekasi，规划 500 MW）、BDx CGK3 南雅加达 + CGK4 Jatiluhur/Purwakarta、DayOne Batam Nongsa 72 MW + Kabil 扩建（PLN Batam 511 MVA）、Edgnex Cikarang 144 MW（拿地已报）、Bitera 20 MW / 8,600 sqm。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **贸易媒体分级**：DCD（B+，印尼标签 https://www.datacenterdynamics.com/en/news/?tag=indonesia）、W.Media（B）、Antara / Antara Kepri（B+，Batam/BP Batam/PLN Batam 官方引语最强）、Bisnis Indonesia（B）、Kontan（B，Telkom 系）、CNBC Indonesia（B-/C+）、DetikInet（B）、Kompas Tekno（B）。升级为 A 仅当文章内嵌公司发布、股票公告、PLN 合同、BP Batam/Kominfo/协调部声明或设施规格页。
- **运营商/开发商矩阵（按地理）**：雅加达=Equinix JK1、NTT JKT2/JKT2A、DCI E1、Digital Edge EDGE1/EDGE2、BDx CGK3、Bitera、NDC；西爪哇=DCI H1/H2/JK6、STT 园区、PDG JC1-JC4、Digital Edge CGK、Microsoft Karawang、NTT JKT3、NeutraDC Cikarang/Sentul、BDx CGK4；万丹=NeutraDC Serpong、BDx Technopark/BSD、PDG Bintaro/JB1；廖内群岛=DayOne、NeutraDC Nxera Batam、Data Center First、BW Digital、Racks Central、RangeIDC/EGSB、Gaw-Sinar Primera、Matrix NAP、NDC Batam、SEAX；东爪哇=DCI E2、NeutraDC Surabaya、NDC Surabaya；巴厘/北苏门答腊/南苏拉威西等=neuCentrIX 与 NDC 边缘。
- **目录来源（C）**：Data Center Map / Baxtel / OCOLO / Cloudscene / PeeringDB / Inflect 仅用于地址与别名交叉；IDPRO、APJII/IIX 作互联生态线索；Uptime Institute 认证名单（A，认证存在性）覆盖 DCI、NTT、NeutraDC 等命名设施。
- **园区/电力枢纽**：GIIC、Kota Deltamas、MM2100、Jababeka、KIIC、Jatiluhur/Purwakarta、Nongsa Digital Park / KEK Nongsa、Kabil（KIIE）、Batamindo、BSD/Technopark BSD、Kendal Industrial Park、IKN/Sepaku。搜 `site:deltamas.id data center`、`"MM2100" "{operator}" "data center"`、`site:bpbatam.go.id ("data center" OR "pusat data")`。
- **去重规则**：按实体园区去重（Jakarta 宣传名可能是雅加达、勿加西、万丹或 Purwakarta）；当前 IT 负载 ≠ 满配园区容量（500 MW/1 GW 叙事 vs 在建 20-50 MW 单楼）；商业设施 ≠ 政府数据中心（Pusat Data Nasional、省级 Diskominfo、部委机房不算商业托管）；neuCentrIX 边缘点勿推断 MW。

## 来源分级

- **A** = 官方/一手/法定可追责：印尼政府门户、OSS/KBLI/NIB、SIMBG PBG/SLF、RDTR/KKPR、AMDALNET、PLN/PLN Batam 供电协议、官方云区域页、运营商官方设施页、上市公司公告、官方园区/SEZ 页。
- **B** = 强二级：Antara、主要印尼商业媒体、Data Center Dynamics、运营商合作方发布、可信工程/地产来源（点名项目）。
- **C** = 弱线索：聚合目录、社交媒体、顾问摘要、过期营销页、项目传闻、仅 MOU 的投资报道。
- 状态语义：planned/permitting/construction/operational/expansion/cancelled 按证据日期与来源分级记录；云 AZ 与 PSE 注册不单独计为设施。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=ID，divisions=38 provinces / special regions / capital district），按 explorer-industry.md §6 省级矩阵逐省枚举。
2. 种子：云区域页 + 运营商官网设施页（DCI、NeutraDC/neuCentrIX、NTT、Equinix、STT、PDG、Digital Edge、BDx、DayOne、NDC、SM+）。
3. 扫描：每候选按「运营商页 → PLN/PJBTL → SIMBG/DPMPTSP → AMDALNET → PSE/OSS → 贸易媒体（B 桥）→ 聚合目录（C）」顺序验证（explorer-official.md §9）。
4. 验证：以官方证据落 A 级事实；单位 MVA/MW 分列；用园区名+设施代码解析真实省份，避免把 Bekasi/Banten 站点归入 Jakarta。
5. 输出：按 world schema 写结果，附证据日期与分级；province/city 粒度。
6. 无项目判定：仅当省/市政府门户、LPSE/SPSE/SIRUP、Telkom/neuCentrIX 位置页、本地新闻均无信号时设 no_projects: true。
7. 遵守 NO-DELETION；本 skill 与两份 explorer 均为只读输入，只新增 SKILL.md 与 ANATOMY.md。

## 待办（2026-08-12 02:23Z）

- [x] explorer-official.md 与 explorer-industry.md 已完成并合并为本 SKILL.md。
- [ ] 下一步：每批 50× codex terra agents，注入本 skill 后按 38 省逐省枚举（Tier 1：Jakarta、West Java、Banten、Riau Islands、East Java）。
- [ ] 待核实：Microsoft Indonesia Central 物理园区位置（Karawang/GIIC 报道需 PBG/PLN 佐证）；DayOne 511 MVA 协议的 PLN Batam 官方文源；PDG JC4 与 Edgnex Cikarang 144 MW 的许可/电力证据。
