---
name: jo-datacenter-methodology
location: scripts/expansion/world/country-skills/JO/SKILL.md
description: |
  Jordan (JO) datacenter discovery & audit methodology — how to enumerate, verify, and update Jordan datacenter projects at governorate granularity (12 governorates in the current manifest). No public national datacenter registry and no complete open planning-permit portal: enumeration joins operator pages, Uptime Institute certificates, official inaugurations (Royal Court/Petra), EBRD financing (ADH), TRC telecom licensing, MoDEE/NITC government cloud, MOIN/Invest Jordan/ASEZA/JIEC investment & zone routes, GAM/ASEZA permits, Ministry of Environment EIA, NEPCO/JEPCO/IDECO/EDCO power records, and Arabic-first press. High-yield governorates: Amman (Orange, Zain, Umniah), Aqaba (ADH), Balqa (Orange Ain Al-Basha). No hyperscale cloud region. Read this before running JO exploration/audit batches. Routes to explorer-official.md (TRC/MoDEE/investment/permits/environment/power/cloud/facility seeds) and explorer-industry.md (operators/press/Arabic queries/directories/governorate map).
---

# JO · 约旦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：约旦**无**全国数据中心注册库、也无完整开放的建设许可门户；枚举联合运营商页、Uptime 认证、官方启用（皇家法院/Petra）、EBRD 融资（ADH）、TRC 电信许可、MoDEE/NITC 政府云、MOIN/Invest Jordan/ASEZA/JIEC 投资与特区、GAM/ASEZA 许可、环境部 EIA、NEPCO/JEPCO/IDECO/EDCO 电力与阿语优先媒体。
> 分区模型：**12 省（governorates）**（Ajloun, Amman, Aqaba, Balqa, Irbid, Jerash, Karak, Madaba, Ma'an, Mafraq, Tafilah, Zarqa）；高产出为 **Amman、Aqaba、Balqa**，其余多为工业区/大学/政府服务/负面扫。
> 无 AWS/Azure/GCP/OCI 公共云区域（官方列表负面）；本地云须绑定约旦物理设施证据。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供约旦探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：TRC（阿语 ICT 文件/许可）、MoDEE/NITC 数字政策与政府云、MOIN/Invest Jordan/ASEZA/JIEC、GAM/市镇建设许可、环境部 EIA、EMRC/NEPCO/JEPCO/IDECO/EDCO 电力、云区域核查、官方设施种子表、12 省策略与名称变体 |
| `explorer-industry.md` | 行业/厂商发现：运营商/设施种子（ADH、Orange、Zain、Umniah、Kalaam、NITC/MoDEE）、媒体分级（intaj/Petra/Zawya/DCD/Capacity 等）、英阿语发现查询、容量/状态提取、厂商/承包商回填、海缆角度、12 省行业图、目录对账与状态规范化 |

## 核心结构事实（框定每次搜索）

1. **无注册库**：建立记录须联合运营商页、认证、官方启用、融资/投资记录、市政/ASEZA 许可、环评、电力证据；`no_projects` 须有文档化搜索记录。
2. **市场 telco 主导、三地集中**：Amman（Orange Marj Al-Hammam/Hashem、Zain The Bunker、Umniah Dahiyat Al-Rasheed/南 Amman 线索、MoDEE/NITC）、Aqaba（ADH 城市 DC + Mega DC + 海缆/IXP/云）、Balqa（Orange Ain Al-Basha，2025-05-28 启用，设计可扩 500 机架/总容量 5 MW——容量为公告值非交付负荷）。
3. **Uptime 是认证真值（A 限定）**：ADH Data Hall 1 & CLS（TCDD/TCCF Tier III）、Zain Bunker、Umniah Dahiyat Al-Rasheed（Tier III Constructed Facility 主张）、Orange Marj Al-Hammam；认证页证明设施名与证书类型，不证明容量/利用率/地址。
4. **容量纪律**：保存源措辞（`designed to accommodate`、`expandable to`、`up to`、`total capacity`、`phase 1`）；ADH 各文章有厅级/园区级不同数字，不平均不归一；5 MW（Ain Al-Basha）不得当已交付负荷。
5. **阿语陷阱**：`مركز معلومات` 常指行政信息办公室；`مركز تكنولوجيا/منصة` 可能是培训/创业空间；须 DC 基础设施词汇（机架、MW/MVA、Tier、托管/colo、冷却、发电机、NOC/SOC）。
6. **简称陷阱**：EDCO 电力 vs JEDCO 中小企业机构；JIC 已并入 MOIN；NITC vs NTC；ADH vs 健康/医院简称。
7. **云区域陷阱**：本地云不是超规模区域；巴林/阿联酋/以色列/卡塔尔/沙特区域不算约旦设施。
8. **Aqaba/Amman 去重**：ADH（City/Mega/CLS/IXP/云）按物理厅/园区去重，IX/海缆登陆不单列；Amman 的 Orange/Umniah/Zain 按运营商+园区对账。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§3 / explorer-industry.md §3-§4）

- TRC：`site:trc.gov.jo "data center" OR "مركز بيانات" OR "مراكز البيانات"`、`site:trc.gov.jo "استضافة" OR "الحوسبة السحابية" OR "cloud"`。
- MoDEE/NITC：`site:modee.gov.jo "data center" OR "مركز بيانات"`、`site:modee.gov.jo "السحابة الوطنية" OR "السحابة الحكومية"`、`"National Cloud" Jordan "data center"`。
- 投资/特区：`site:moin.gov.jo "data center" OR "مركز بيانات"`、`site:aseza.jo "data center" OR "مركز العقبة الرقمي" OR "كابل بحري"`、`site:jiec.com "data center" OR "استضافة"`。
- 许可：`"رخصة أبنية" "مركز بيانات" الأردن`、`site:amman.jo "مركز بيانات" OR "data center" OR "رخصة أبنية"`、`"بلدية" "مركز بيانات" "رخصة أبنية" إربد OR الزرقاء`。
- 环境：`site:moenv.gov.jo "مركز بيانات" OR "مراكز البيانات"`、`"تقييم الأثر البيئي" "مركز بيانات" الأردن`、`"مولدات ديزل" "مركز بيانات"`。
- 电力：`site:nepco.com.jo "data center" OR "Aqaba Digital Hub"`、`site:jepco.com.jo "مركز بيانات" OR "محطة تحويل"`、`"NEPCO" "data center" Jordan connection`。
- 行业（英/阿）：`"Jordan" ("data center" OR datacenter) (MW OR racks OR colocation OR inaugurated OR "under construction")`、`"مركز بيانات" الأردن ("ميغاواط" OR "رفوف" OR "استضافة" OR "افتتاح" OR "قيد الإنشاء")`、`"أورنج الأردن" "مركز بيانات" OR "عين الباشا"`、`"زين الأردن" "ذا بنكر"`、`"أمنية" "مركز بيانات" OR "ضاحية الرشيد" OR "جنوب عمان"`。
- 媒体/认证：`site:petra.gov.jo Jordan "data center" OR "مركز بيانات"`、`site:intaj.net "data center" Jordan Orange OR Zain OR Umniah`、`site:uptimeinstitute.com Jordan OR "Aqaba Digital Hub" OR "Hashem Data Center" OR "The Bunker"`。

## 官方/监管管线要点（详见 explorer-official.md）

- TRC（A 电信/ICT 监管状态，非注册库）：ICT 部门阿语文件、电信许可、频谱/型式批准/编号门户；缺席不证明不存在。
- MoDEE/NITC（A 政策/政府云）：数字转型战略 2026-2028、e-Government 项目；设施细节通常不公开。
- 投资/特区：MOIN、Invest Jordan（省际投资图）、ASEZA（Aqaba 单一窗口/激励）、JIEC（低产出省工业区）；均不证明设施。
- 许可：GAM e-services/ChkLand 跟踪（需已知标识符）、ASEZA（Aqaba 项目走 ASEZA 而非普通市政假设）；许可记录 A 当有具体编号/地块/业主/用途。
- 环境：环境部 EIA——数据中心可能不单列类别，搜触发活动（柴油发电机、燃油库、电池、冷却、取水、变电站）。
- 电力：EMRC（监管/电价）、NEPCO（输电/单一买方）、JEPCO（Amman/Zarqa/Madaba/Balqa）、IDECO（北部 Irbid 等）、EDCO（南部/东部 Aqaba 等）；大 DC 的电网证据具决定性。
- 推荐管线：Uptime 页 → 运营商官方页 → 融资/启用（EBRD/皇家法院/Petra/intaj）→ Amman/Aqaba/Balqa 深潜（GAM/ASEZA/JEPCO/EDCO/NEPCO/环境/阿语）→ 其余 9 省模板扫 → 云核查 → 目录对账。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商种子：ADH（adh.jo：City DC 2020 起、Mega DC、EBRD JOD 10m 贷款、EU 支持二厅 fit-out；A 官方/融资/Uptime）、Orange Jordan（Marj Al-Hammam A、Hashem B+ 2025-03 Tier III Design、Ain Al-Basha B+/A- 500 机架/5 MW）、Zain The Bunker（A 官方页，KHBP）、Umniah（A 官方 colo/DC + Uptime；南 Amman 新项目 A-/B）、Kalaam（C/B，区域服务不证明约旦设施）、NITC/MoDEE（A 政策/B-C 设施）。
- 媒体：intaj.net（B/B+ 运营商新闻稿）、Petra（A/B）、Zawya/MENAFN（B）、Jordan Times/Roya/Al-Mamlaka/Al-Ghad（B）、DCD/Capacity/Telecom Review/Developing Telecoms/W.Media（B）、The Fast Mode/SAMENA/Intelligent CIO（B）、Uptime（A 认证）、EBRD/EU（A 项目/融资）。
- 目录（C）：DataCenterMap Amman、datacenters.com、colocationm、datacentercatalog、Cloudscene、PeeringDB、Baxtel、ocolo——仅别名/地址/隐藏阶段线索。
- 状态规范化：`strategy/MoU/partnership/platform`=规划/上下文；`financing/fit-out/second hall`=扩展/在建；`commenced construction/EPC awarded`=在建；`inaugurated/opened/launched/hosting customers`=运营；运营商 Tier 声明须 Uptime 匹配。

## 已知设施/项目与证据状态

| 设施/项目 | 省 | 状态与证据 |
|---|---|---|
| Aqaba Digital Hub（City DC / Mega DC / Data Hall 1 & CLS） | Aqaba | 运营/扩展（A adh.jo/EBRD/Uptime；容量按来源与阶段分别存储）；City DC 2020 起 Tier III 主张 |
| Orange Jordan – Ain Al-Basha DC | Balqa | 2025-05-28 启用（B+/A- intaj/FANA）；500 机架/5 MW 为公告容量；Orange 主源/JEPCO/许可待补 |
| Orange Jordan – Marj Al-Hammam DC | Amman | 运营（A 官方托管/DC 手册 + Uptime）；目录容量 C |
| Orange Jordan – Hashem DC | Amman | Tier III Design（B+ 2025-03 报道/SAMENA）；Uptime 状态复核；目录地址/容量 C |
| Zain Jordan – The Bunker | Amman/KHBP | 运营（A 官方页 + Uptime 页）；99.982% 可用性主张；目录 2 MW 为 C |
| Umniah – Dahiyat Al-Rasheed colo room | Amman | 运营（A 官方 + Uptime 列表）；容量未公开 |
| Umniah – South Amman 新项目 | Amman | A-/B 线索（官方页 + Trismart）；状态与去重待验 |
| NITC / MoDEE 政府托管/国家云 | Amman（待验） | A 政策/B-C 设施；按政府/机构分类 |
| Kalaam Telecom | 未验证 | C/B 线索；约旦设施页/认证/许可前不计数 |
| Zain Amman DC 2（目录） | Amman | C 候选；官方/Uptime/许可前不单列 |

## 更新节奏

- 每批次：云区域负面核查、Uptime 国家/客户页（Orange/ADH/Zain/Umniah）、ADH 扩展（EBRD/EU、第二厅）、Ain Al-Basha 许可回填、Umniah 南 Amman 状态、Kalaam 约旦设施证据。
- 季度：12 省负面扫回顾（阿语优先）、海缆/AqabaIX 相邻设施、CBJ/银行/大学机构级线索、目录别名去重（Al Mirnaah/35D/ADH、Marj Al-Hamam 变体）。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（12 省粒度）；本 skill 作为国家层参考注入。
