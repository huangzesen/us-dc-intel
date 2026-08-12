---
name: mv-datacenter-methodology
location: scripts/expansion/world/country-skills/MV/SKILL.md
description: |
  Maldives (MV) datacenter discovery & audit methodology — how to enumerate, verify, and update Maldives datacenter projects at 21-division (Male, Addu City, atoll rows) granularity. Maldives has no public datacenter register: enumeration joins CAM telecom licensing (operator universe), operator facility pages (Dhiraagu Tier IV Hulhumale / Velidhoo, OMDC, MVIX), government digital infrastructure (MDS — successor of abolished NCIT, MINDCo, HDC/Maxcom co-location project), planning/land/tender records (HDC, Gazette, Maavehi, councils), environmental/energy records (ERA/STELCO/FENAKA generators and substations), cable-landing priority signals (MSC, DSCoM, PEACE, SMW6, IAX), Uptime Institute certification, and hyperscaler region absence checks (no AWS/Azure/GCP/OCI region). Read this before running MV exploration/audit batches. Routes to explorer-official.md (CAM/government/land/energy/cable/cloud pipeline) and explorer-industry.md (operator seeds/trade press/directory verification).
---

# MV · 马尔代夫数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：马尔代夫**没有**公开的数据中心注册表，市场是**电信主导的小市场**——普查从 Dhiraagu、Ooredoo Maldives、MVIX、Maldives Digital Service/MINDCo、HDC/Maxcom、Focus Infocom 等运营者出发，不能按超大规模市场方式枚举。
> 已确认的设施集群集中在三处：**Hulhumale/Male Atoll（Kaafu）**（Dhiraagu Tier IV DC、OMDC、HDC 托管项目、MSC/SMW6/IAX 登陆）、**Male 市**（MVIX、历史 NCIT/MDS 政府 DC 线索、电信/ISP 机房）、**N. Velidhoo/南米拉敦马杜卢环礁（Noonu）**（Dhiraagu 第三 DC）；Kulhudhuffushi 为高优先级 watch 区（PEACE 海缆 2024 登陆，无确认 DC）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供马尔代夫探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：CAM 牌照（运营者宇宙）、MDS/NCIT/MINDCo 政府数字设施、HDC/Gazette/Maavehi/议会土地与招标、ERA/STELCO/FENAKA 环境能源、海缆主源（MSC/DSCoM/PEACE/SMW6/IAX）、超大规模缺席核验、21 分区矩阵、分级规则 |
| `explorer-industry.md` | 行业/厂商发现：运营者种子注册表（Dhiraagu/OMDC/MVIX/NCIT-MDS/HDC-Maxcom/Syntys）、运营者查询配方、贸易媒体（DCD/Telecompaper/Developing Telecoms/Edition/Raajje/PSM/Corporate Maldives）、目录到一手工作流、分区检索矩阵、容量提取规则 |

## 核心结构事实（框定每次搜索）

1. **无公开注册表**：枚举靠拼接电信牌照、运营者页面、土地/招标公告、环评决定、能源记录与海缆登陆点。
2. **关键清单映射修正**：`North Miladhunmadulu` = Shaviyani（Sh.）；`South Miladhunmadulu` = Noonu（N.）——Dhiraagu N. Velidhoo 数据中心属于 **South Miladhunmadulu**，不是 North；`Male` 是城市，`Male Atoll` 是 Kaafu（含 Hulhumale/Maafushi/Guraidhoo），Dhiraagu Hulhumale DC、OMDC、HDC 项目、MSC/SMW6/IAX 登陆记入 Male Atoll。
3. **机构更替**：President's Office 于 2026-01-15 以 Directive No. 4/2026 设立 **Maldives Digital Service（MDS）**并废除 **NCIT**——历史 NCIT 政府数据中心（Male，2005 年建）的当前运营主张必须经 MDS 确认；`https://presidency.gov.mv/Press/Article/36043` 与 `https://www.mds.gov.mv/` 为 A 级锚。
4. **市场三簇**：① Male Atoll/Hulhumale（最高产）：Dhiraagu Hulhumale Tier IV 认证 DC（Uptime 列表 A）、OMDC Hulhumale（2021，Tier III-ready）、HDC/Maxcom 托管项目（2021 EOI，B/C）、MSC/SMW6/IAX 登陆；② Male 市：MVIX（H. Bonthi 5 层，A）、NCIT/MDS 政府 DC（B 历史）、Dhiraagu/Focus/Raajje/SatLink 机房线索；③ N. Velidhoo/Noonu：Dhiraagu 第三 DC（2025-11 启用，Tier III 级/ready，A/B）。
5. **监管与机构**：CAM（cam.gov.mv）定义持牌运营者宇宙——Dhiraagu/Ooredoo 统一电信牌照、Focus Infocom/Starlink Services ISP 牌照、WARF/OCM 国际海缆牌照、HDC Hulhumale 电信基础设施牌照；**牌照 ≠ 物理设施记录**。环境监管现为 ERA（era.gov.mv，旧称 EPA）。
6. **海缆是位置代理，不是设施证明**：MSC（840km 四纤对，Dhiraagu/Ooredoo/Dialog）、DSCoM 国内海缆扩展（Hulhumale/Maafushi/Dhangethi/Maamigili/Velidhoo/Dhuvaafaru/Eydhafushi 节点）、PEACE（2024 登陆 Kulhudhuffushi，B）、SMW6（Hulhumale）——先提升岛屿搜索优先级，出现独立设施记录才升级。
7. **超大规模缺席**：AWS/Azure/GCP/OCI/Alibaba/Huawei 均无 MV 公共云区域（官方区域页核验）；本地 “cloud”/VPS/托管按转售/本地电信服务对待。
8. **容量稀疏**：公开 MW 基本为零——默认 `capacity_mw: null`，用 Tier/认证、状态、地址、机架/面积、连接性作代理；**不得**从 Tier 级别、海缆容量、发电机存在或防洪声称推断 MW。
9. **语言**：运营者/公共部门页用英语；`data centre` 与 `data center` 都要搜；加岛名（环礁标签常歧义）。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§3 / explorer-industry.md §1-§2、§5）

- CAM：`site:cam.gov.mv "Telecom Service Provider Licensees" Maldives`、`site:cam.gov.mv "Dhiraagu" "Ooredoo Maldives" "Focus Infocom"`、`site:cam.gov.mv "Telecommunication Infrastructure Licence" "Housing Development Corporation"`。
- 政府数字设施：`site:mds.gov.mv "data centre" OR "data center" OR "hosting" OR "infrastructure"`、`site:presidency.gov.mv "Maldives Digital Service" "NCIT" "Directive No. 4/2026"`、`site:mindco.mv "data centre" OR "cloud" OR "hosting"`、`"NCIT" "Male" "data centre" "2005" Maldives`。
- 土地/招标：`site:hdc.mv/announcements "data centre" OR "co-location" OR "colocation"`、`site:oldweb.hdc.mv/announcements "co-location" "Hulhumale"`、`site:gazette.gov.mv "data centre" OR "colocation"`、`site:maavehi.gov.mv "data centre" OR "server" OR "generator"`、`"HDC" "Maxcom Technologies" "Co-location Data Centre"`。
- 环境/能源：`site:era.gov.mv "data centre" OR "generator" OR "fuel storage"`、`site:epa.gov.mv "data centre" OR "server farm"`、`"EIA" "Maldives" "data centre" OR "colocation" OR "landing station"`、`site:stelco.com.mv "data centre" OR "substation" OR "Hulhumale"`、`site:fenaka.mv "generator" OR "Velidhoo"`。
- 运营者：`"Dhiraagu" "Hulhumale" "Tier IV" "data centre"`、`site:dhiraagu.com.mv "data center" OR "colocation" OR "cloud"`、`"Dhiraagu" "Velidhoo" "data centre" OR "Tier III"`、`"Ooredoo Maldives Data Centre" OR "OMDC" "Hulhumale"`、`"Ooredoo" "Kulhudhuffushi" "data centre" OR "managed services"`、`"MVIX" "H. Bonthi" OR "Hihfaseyha"`。
- 贸易/目录：`site:datacenterdynamics.com/en/news/ Maldives "data center" OR "data centre"`、`site:telecompaper.com Maldives Dhiraagu Ooredoo`、`site:developingtelecoms.com Maldives "submarine cable"`、`site:submarinenetworks.com Maldives Kulhudhuffushi OR Hulhumale OR Velidhoo`、`site:datacentermap.com/maldives/ Maldives "Syntys" OR "Dhiraagu"`。
- 负控制：`"Maldives cloud region" AWS OR Azure OR Google OR Oracle`、`"underwater data centre" Maldives`、`"Syntys Maldives" site:syntys.com`、`"MMIX" Maldives`。

## 官方/监管管线要点（详见 explorer-official.md）

- **CAM（A，运营者身份）**：牌照页 2024-10-16 更新；提取持牌法人、牌照类、岛屿/集团覆盖；不把牌照当物理设施记录。
- **政府数字设施（A 机构/项目）**：MDS/President's Office/MINDCo/DMADD 页面为 A；2005 NCIT 设施贸易报道为 B 直到 MDS 官方设施页确认在运；`"Maldives 2.0"` 国家数据交换计划为线索。
- **规划/土地/招标（A/B）**：HDC 2021 “Development of Co-Location Data Centre in Hulhumale” EOI + HDC-Maxcom 协议（B/C watch）；提取申请人/SPV、地块、岛屿、当局、公告号、招标/租约状态、用地类、面积、发电机/燃料条件、EIA 参考、当前状态。
- **环境/能源（A 项目元素）**：发电机许可、燃料储存、变电站、冷却厂、海缆登陆站、填海开发中找设施；发电机/变电站记录只是支持证据，不是 DC 存在主张。
- **海缆主源（A/B）**：Uptime Institute 列表（Dhiraagu Hulhumale Tier IV TCDD/TCCF，A）、Dhiraagu 官网 Data Center & Cloud 页（A）、MVIX 官方位置页（A）、MSC/DSCoM/PEACE 运营者公告（A/B）。
- **超大规模缺席（A）**：六个云厂商官方区域页季度复核；本地 “cloud” 按转售对待。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **种子注册表**：Dhiraagu Hulhumale DC（A）、Dhiraagu Data Center & Cloud/Cloud IaaS（A）、Dhiraagu Male 遗留核心 DC（B/C，地址待一手确认）、Dhiraagu N. Velidhoo DC（2025-11 启用，A/B，Noonu 映射）、OMDC（A/B，Tier III standard/ready 区分）、MVIX（A，IXP/机房，不算商业批发 DC）、NCIT/MDS 政府 DC（B 历史，MDS 确认才 A）、HDC/Maxcom（B/C watch）、Syntys Maldives 1（C，无 Syntys 官方页）、Focus Infocom/Raajje（C 设施）、IRSP 列表（C 设施）。
- **贸易媒体（B）**：DCD（OMDC/Dhiraagu 启动）、Telecompaper、Developing Telecoms、Edition/Mihaaru、Raajje.mv、PSM News、Corporate Maldives、Adhadhu/Sun/Avas/Atoll Times/See.mv；SubmarineNetworks/SubTel Forum/CableStatus/TeleGeography 海缆事实；PCH 确认 MVIX 活跃（2022-09-28 成立）。
- **目录（C）**：DataCenterMap/Cloudscene/datacenters.com/Baxtel 仅做种子/查重；Syntys Maldives 1 必须 Ooredoo/Syntys 一手确认后才合并。
- **容量提取**：先搜 MW/MVA/kW、机架/面积、Tier/Uptime、发电机/UPS/2N/N+1、投资额；Tier 认证是可靠性/设计信号不是 IT 负载；无公开值写 `capacity_mw: null` 并把代理放 notes。
- **排除项**：度假村服务器机房/私有度假光纤端点不算 DC；Kulhudhuffushi PEACE 登陆是 watch 区不是设施；不在目录城市标签上分配区域。

## 来源分级

- **A** = 官方/一手：CAM 牌照、运营者官方页（Dhiraagu/Ooredoo/MVIX）、Uptime Institute 认证列表、President's Office/MDS/MINDCo 官方页、HDC/议会/Gazette 土地或招标记录、ERA EIA 决定、STELCO/FENAKA/MEA 官方记录、海缆所有者/财团/运营者公告、云厂商官方区域页（缺席）。
- **B** = 强二级：DCD、Telecompaper、Developing Telecoms、Edition/Mihaaru、Raajje.mv、PSM News、Corporate Maldives、Adhadhu/Sun/Atoll Times、SubTel Forum/SubmarineNetworks 摘要（有具名当事方与日期）、PCH。
- **C** = 目录/市场/SEO/社交：DataCenterMap/Cloudscene/Baxtel/datacenters.com（无一手佐证）、通用 VPS/托管页、仅 Facebook/社交帖（除非是官方 HDC/运营者公告的唯一镜像并显式标注）。
- **状态语义**：PEACE 登陆 = 连接性/watch；HDC-Maxcom = pipeline；Syntys = 未验证；历史 NCIT = 历史状态标记；Tier IV 认证 ≠ MW；发电机存在 ≠ IT 负载。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=MV，divisions=21：Male、Addu City + 历史环礁行）。
2. 用 CAM 定义运营者宇宙（Dhiraagu、Ooredoo、Focus/Raajje、Starlink、WARF、OCM、HDC、按岛 IRSP）。
3. 设施搜索：Dhiraagu/Ooredoo/MVIX/MDS/MINDCo/HDC/Gazette/Maavehi/Male City Council/ERA/STELCO/FENAKA 官方域。
4. 按岛先分配位置，再映射 manifest 分区；不依赖目录城市标签；Tier 声称用 Uptime 列表独立核验。
5. 海缆记录提升优先级岛：Hulhumale、Maafushi、Dhangethi、Maamigili、Velidhoo、Dhuvaafaru、Eydhafushi、Kudahuvadhoo、Kulhudhuffushi——仅当出现独立设施记录才升级。
6. 目录到一手：抓目录精确名称/地址/坐标 → 运营者官方域 → 地址+HDC/Maavehi/Gazette/ERA/议会 → Uptime → CAM；无主源则保留 C 并标 `facility_unverified: true`。
7. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无 MW 用 null；低产分区 one-shot 扫描后写 `no_projects: true`。
8. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核马尔代夫数据中心（21 分区粒度，Hulhumale/Male/Velidhoo 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Dhiraagu N. Velidhoo 第三 DC 的 Uptime/官方页证据、NCIT→MDS 政府 DC 当前运营状态、HDC/Maxcom 托管项目运营状态、Syntys Maldives 1 是否存在、Kulhudhuffushi PEACE 后是否出现设施记录、MW 级容量是否被任何一手源公开。
