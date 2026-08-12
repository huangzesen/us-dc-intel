---
name: ps-datacenter-methodology
location: scripts/expansion/world/country-skills/PS/SKILL.md
description: |
  Palestine (PS) parent-level methodology for data-center enumeration at governorate granularity (16
  governorates). No hyperscaler public-cloud region exists in Palestine; nearby Israeli regions
  (AWS il-central-1, Google me-west1, Azure Israel Central, Oracle il-jerusalem-1) must never be mapped to
  PS. Physical facility universe is small: Paltel Data Center Al-Bireh/Ramallah (launched 2019, ~6,000 sq m,
  Uptime Tier III Design, ~USD 10M, second Paltel DC), Paltel first DC at Nablus HQ, and MTIT/MTDE
  Government Computer Center / National Data Center in Ramallah (collocation, DR hosting, government private
  cloud, 17 hosted institutions). DWBG (IDA USD 20M) and 2025 Unified Data Hosting/Cloud Strategy EOI are
  pipeline evidence. Gaza Paltel main data centers/switches are damaged/intermittent (WAFA 2023 fuel
  shutdown, 7amleh 75% damaged) - never normal operational without current primary source. Enumeration
  pivots from MTDE/WAFA/Shiraa procurement/PEX filings/official operator pages; Gaza must be status-checked
  every run. Routes to explorer-official.md (ministry/procurement/government-DC pipeline) and
  explorer-industry.md (operator/trade-press/directory pipeline).
---

# PS · 巴勒斯坦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：巴勒斯坦没有超大规模公共云区域；邻近以色列区域（AWS il-central-1、Google me-west1、Azure Israel Central、Oracle il-jerusalem-1）**绝不映射到 PS 省**。物理设施宇宙很小：Paltel 数据中心 Al-Bireh/Ramallah（2019 年启用，约 6,000 m2，Uptime Tier III Design，约 1,000 万美元，Paltel 第二个 DC）、Paltel 首个 DC（纳布卢斯 HQ）、MTIT/MTDE 政府计算机中心/国家数据中心（拉姆安拉：colo、DR 托管、政府私有云、17 个托管机构）。DWBG（IDA 2,000 万美元）与 2025 统一数据托管/云战略 EOI 为管线证据。**加沙每次运行都必须状态核查**——Paltel 主数据中心/交换机因燃料耗尽关停（WAFA 2023-11-16）、75% 电信基础设施受损（7amleh 2024），未获 2025-2026 主源确认前绝不标 normal operational。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供巴勒斯坦探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：MTDE/MTIT、DWBG、政府计算机中心/NDC、PalCERT、Shiraa 采购、PEX、Paltel 官方、Ooredoo、PCBS/TRA、PIPA/PIEFZA、云区域阴性对照、16 省路由 |
| `explorer-industry.md` | 行业管线：DCD/Bloomberg-DCK/Telecompaper/本地阿拉伯媒体、运营商/厂商种子、目录处理、已确认/弱线索处理、逐省矩阵、验证工作流 |

## 核心结构事实（框定每次搜索）

1. **无超大规模区域**：官方 AWS/GCP/Azure/Oracle 列表无巴勒斯坦区域；以色列邻近区域不得映射；本地 `cloud` = Paltel 私有/云服务、MTDE/NDC 政府私有云或小本地 VPS/托管。
2. **16 省**：Bethlehem, Deir El Balah, Gaza, Hebron, Jerusalem, Jenin, Jericho and Al Aghwar, Khan Yunis, Nablus, North Gaza, Qalqilya, Ramallah, Rafah, Salfit, Tubas, Tulkarm。
3. **Paltel Al-Bireh/Ramallah DC（最强私营设施证据）**：Paltel 阿拉伯语公告（p=58225）称 Al-Bireh/Ramallah 设施在建，并确认此前在 **Nablus** 公司总管理总部有 Paltel 数据中心；DCD/Bloomberg-DCK 报 2019 年启用为 Paltel 第二个 DC：约 65,000 sq ft / 6,000 m2、Uptime Tier III Design 认证、约 1,000 万美元；Uptime 奖项页（paltel-data-center--albireh/1115）项目名与运营商指向 Al-Bireh/Ramallah，但位置行写 "Nablus West Bank"——保留该矛盾说明。
4. **MTIT/MTDE 政府计算机中心/NDC（拉姆安拉）**：世行巴勒斯坦数字经济评估称 MTIT 下建有集中政府数据与 IT 中心、政府计算机中心是主要 e-政府基础设施实体、MTIT 计划在拉姆安拉总部建政府全域云 + DR 站点；NDC 页（mtde.online，A- 域注意）确认政府 colocation、DR 站点托管、DCIM 监测、PalCERT 监测、政府私有云、17 个托管政府机构、270 台虚拟服务器、109 个托管政府网站。
5. **管线 ≠ 设施**：DWBG 项目（IDA 2,000 万美元：法律/监管环境、未来 TRA、根 CA、QoS 平台、应急响应/恢复基础设施、全政府数字转型战略、数据基础设施、数字公共平台、e-GP）与 MTDE 2025 统一数据托管/云托管战略 EOI（云卓越中心、Cloud-First）及世行 DWBG 重组（2026 年初启动国家云托管与数据中心战略）——只有后续招标/授予/官方公告具名站点、业主与实施范围才创建 planned/tendered 设施。
6. **加沙状态纪律**：Paltel 主数据中心/交换机 2023-11-16 起因燃料耗尽逐步关停（WAFA A）；2024 年 75% 受损/至少 50% 摧毁（7amleh B）；2026-05-17 PCBS/MTDE/TRA 世界电信日发布（A）仅证明紧急干预维持部分连通（94 个电信站点数据库更新、12 个应急点、2026-04 移动覆盖）——非 DC 调试证据；战前加沙设施 = `damaged`/`intermittent`/`unknown_current_status`。
7. **Power 是门控事实**：西岸设施依赖进口电力 + 本地配电 + 备用系统；加沙依赖受限燃料/电池/太阳能/维修；不推断 MW 规模。
8. **无中央规划许可登记册**：西岸建筑许可归市政；加沙许可不可靠；枚举从官方/运营商公告与采购出发，识别候选站点后才转向市政。
9. **语言**：阿拉伯语为本地启用/招标/厂商案例最高产语言（مركز بيانات/مركز الحاسوب الحكومي/استضافة الخوادم/الحوسبة السحابية/التعافي من الكوارث/عطاء/مناقصة/افتتاح/تدشين/تدمير/تضرر/انقطاع/إعادة إعمار）；英文最强于 Paltel 2019 贸易报道、世行/UN 文件、加沙损毁报道。
10. **排除项**：泛云/VPS/托管/FTTH/网络覆盖/塔站/ISP ASN/学术概念/房地产区/重建愿景无设施证据者拒绝；耶路撒冷附近以色列设施（Atarot、Modi'in、Har Tuv、Beit Shemesh、特拉维夫）不是 PS 设施。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§2/§4、explorer-industry.md §1/§2/§4/§5）

```text
site:mtde.gov.ps "data center" OR "data infrastructure" OR "cloud"
site:mtde.gov.ps "مركز بيانات" OR "الحوسبة السحابية" OR "استضافة"
site:mtde.online "مركز البيانات الوطني" OR "PalCERT"
site:wafa.ps "مركز البيانات" OR "بالتل" OR "التحول الرقمي"
site:english.wafa.ps "Paltel" "data centers" OR "Digital West Bank"
site:shiraa.gov.ps "مركز بيانات" OR "data center" OR "خوادم" OR "الحوسبة السحابية"
site:pex.ps PALTEL "Annual Report"
site:paltelgroup.ps "مركز البيانات" OR "data center" OR "Uptime"
site:pcbs.gov.ps "telecommunications" "Gaza"
"Palestine" "data center" Paltel Ramallah Al-Bireh
"Paltel" "Tier III" "Uptime" Palestine
"Paltel" "data center" "Nablus" OR "Al-Bireh"
"Zone Technologies" Ramallah "data center" OR "cloud"
"Ooredoo Palestine" "data center" OR "cloud"
"Gaza" "data centers" Paltel damage OR fuel OR batteries
"غزة" "مراكز البيانات" "بالتل" OR "انقطاع"
"مناقصة" "مركز بيانات" فلسطين
"فلسطين" "مركز البيانات الوطني"
"{division}" "data center" Palestine
"{Arabic governorate}" "مركز بيانات" OR "استضافة" OR "خوادم"
"Palestine" "cloud region" OR "availability zone"
site:datacentermap.com/palestine "{division}"
"Paltel Data Center" Bethlehem OR Jenin OR Gaza
"Al-Aqsa University" "Gaza Data Centre"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **MTDE/MTIT**（mtde.gov.ps，A）：电信与数字经济部（原 MTIT）；DWBG 项目页（IDA 2,000 万美元，A）与统一数据托管/云托管战略 EOI（2025，A 高信号：云卓越中心、Cloud-First、数据托管基础设施评估、公私合作）。
- **NDC/政府计算机中心**（mtde.online/national-data-center/，A- 域注意）：政府 colo/DR/私有云服务；PalCERT（mtde.online/palcert/，A-）为政府 SOC，非独立 DC；状态：运营（机构政府 DC 服务），新云/DC 战略组件保持 planned/tendered。
- **Shiraa 采购门户**（shiraa.gov.ps，A）：ProcurementView 通知（示例：教育部数据中心归档系统采购招标）；镜像站点（palestinetenders.com 等）为 C 直到链接 Shiraa/MTDE/世行原始文件。
- **PEX/上市公司**（pex.ps，A）：Paltel Group 年报搜索 data center/مركز البيانات/Gaza/impairment/capex/cloud。
- **Paltel 官方**（paltelgroup.ps/paltel.ps/jawwal.ps，A）：Al-Bireh 公告（四光纤路径、三电力路径、冷却设计、colo/安全管理/虚拟服务器/IaaS-PaaS-SaaS/存储）；Uptime 奖项页（A 认证身份，位置行矛盾保留）。
- **Ooredoo Palestine**：运营商身份 A；集团级 DC 扩张/Iron Mountain 伙伴关系为区域信号，不构成 PS 设施证据；本回合未验证到 A 级巴勒斯坦设施页。
- **PCBS/TRA**：官方统计 A；2026-05-17 发布为韧性/背景证据。
- **PIPA/PIEFZA**：投资促进材料 A；Bethlehem 工业园区、Jericho 农工园、Jenin 自由工业区、Tarqumiya/Hebron 为未来选址线索。
- **云区域阴性对照**：AWS/GCP/Azure/Oracle 官方列表（A），以色列区域不得映射。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Paltel Al-Bireh**：记录为 operational、division Ramallah、capacity_mw null、面积 6,000 m2（DCD/Bloomberg）、Tier III Design（Uptime/DCD）、服务 colo/DR/VPS/IaaS-PaaS-SaaS/存储。
- **Paltel 首个 DC - Nablus**：Paltel 公告确认存在，但公共容量/Tier/当前状态细节有限；置信度低于 Al-Bireh；无 MW/Tier/公共 HQ 以外地址。
- **Zone Technologies（Ramallah）**：DataCenterMap 列 Masrouji Building/Al Madaen Street "Zone Data Center"；zone.ps 营销云/VPS/云存储——C+/B- 线索，缺设施规格/电力/调试/许可。
- **需降级的弱记录**：`Paltel Data Center - Bethlehem`（C，仅目录/弱三方）、`Paltel Data Center - Jenin`（C）、`Digital Communication Gaza`（C，不得覆盖战争损毁证据）、`New Gaza redevelopment data centres`（概念）、`Hebron Municipality data center`（C/B 厂商材料）、`Al-Aqsa University Gaza Data Centre`（学术/NSDI 概念）。
- **媒体分级**：DCD（B+）、Bloomberg/DCK（B，1,000 万美元拉姆安拉故事）、Telecompaper/SAMENA（B）、Al Jazeera（B，加沙冗余/战时运营）、WAFA（A/B）、7amleh（B）、PCBS（A）、PITA（B-/C）、本地阿拉伯媒体 Palsawa/QudsNet/Maan/Bnews/Hadf（B-/C）。
- **状态词**：افتتاح/إطلاق/تدشين = launched/operational；يتم انشاؤه/قيد الإنشاء = under construction；اتفاقية/مذكرة تفاهم = planned；عطاء/مناقصة = tendered；انقطاع/توقف/تضرر/تدمير = outage/damaged；إعادة إعمار = 重建概念（无授予/站点则非项目）。

## 来源分级

- **A** = 主要来源：MTDE/PA 部委、WAFA 官方通讯社（政府/运营商声明）、Shiraa 公共采购门户、世行/UN/EU 项目或损毁报告、PCBS、PEX 申报/年报、Uptime Institute 认证、具名设施或服务的运营商官方页。
- **B** = 强佐证：DCD、Bloomberg/Data Center Knowledge、Telecompaper、Al Jazeera/NYT/Reuters/Access Now/7amleh（引述具名运营商或已发布评估时）、行业协会材料。
- **C** = 仅线索：DataCenterMap、Inflect、Data Center Platform、Datacenter Catalog、经纪页面、LinkedIn/社交帖子、无物理站点的云/托管营销页、不暴露原始买方通知的招标镜像。
- 接受阈值：运营设施 = 运营商/政府启用声明/官方设施页/Uptime 认证+佐证/政府或世行文本点名现存 DC；招标/规划 = Shiraa/MTDE/世行采购具名 DC/云/数据托管实施；损毁设施 = Paltel/WAFA/UN/世行/PCBS/7amleh 证据——绝不静默保留战前加沙站点为 operational。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 PS 记录与种子（Paltel Al-Bireh、Paltel Nablus、NDC/政府计算机中心、Zone、Gaza Paltel 设施、Ooredoo、DWBG 管线）。
2. 验证工作流：行业/目录/阿拉伯语媒体播种 → 精确名称+阿拉伯语变体 → 运营商官方站/PEX/注册表验证身份 → 运营商公告/Uptime/政府来源/Shiraa/市政/可信贸易文章验证物理站点 → 验证状态（启用=运营；协议/MoU/战略=planned；招标=tendered；加沙战前项需当前损毁/恢复状态）→ 验证省与市（不映射以色列设施/云区域）→ 仅来源陈述时提取规模 → 记录置信度说明。
3. 加沙五省（Gaza、North Gaza、Deir El Balah、Khan Yunis、Rafah）每次运行状态核查：PCBS/MTDE/WAFA/UN-RDNA 2026 + 运营商最新声明。
4. 边界规则：市场文案可能把 Al-Bireh、Beitunia 或 Nablus 相关资产标为 "Ramallah"；可用市政/坐标时用之，否则按最强来源记录仓省并保留说明。
5. 输出 schema：`{country_code: PS, country_name: Palestine, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目省 `no_projects: true`。不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] Paltel Nablus 首个 DC：寻找当前 Paltel 页面/申报确认规格与状态。
- [ ] NDC：用 mtde.gov.ps/世行/WAFA 交叉核对 mtde.online 最终坐标与服务计数。
- [ ] DWBG 国家云托管与数据中心战略：追踪 2026 早期启动活动与后续招标/授予。
- [ ] Zone Ramallah：用 Zone/市政/客户合同/电信许可验证设施规格、电力、调试。
- [ ] Gaza：用 2025-2026 运营商或官方来源确认各 Paltel 设施当前状态。
- [ ] Ooredoo Palestine：寻找巴勒斯坦具名设施证据（如有）。
- [ ] 云区域阴性对照（含以色列区域排除）：每次运行复查。
