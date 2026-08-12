---
name: sd-datacenter-methodology
location: scripts/expansion/world/country-skills/SD/SKILL.md
description: |
  Sudan (SD) datacenter discovery & audit methodology — how to enumerate, verify, and update Sudan datacentre facilities at 18-state granularity. Sudan has no public planning-permit or facility registry: enumeration joins TPRA telecom licensing (incl. a third-class cloud-via-private-data-center SaaS licence class), MTDT digital-transformation programs (3x3 plan, Baladna, CONSOLEX), NIC/NDC national data infrastructure and SIXP IXP records, SUNA official reporting, operator official pages (Sudatel/Sudani — Khartoum DC, two Tier III DCs group statement, Port Sudan/SAS1 lead), cable-consortium records (EASSy/SAS1/SAS2 at Port Sudan), energy/grid context, and cloud-region absence checks (no AWS/Azure/GCP/OCI region). War context is mandatory for grading: since April 2023 Khartoum facilities were occupied/damaged (Feb 2024 shutdown), SAF recaptures in March/May 2025, and the 1,300 m2 state data centre was rehabilitated 9 Oct 2025 — every status claim must be date-stamped. Read this before running SD exploration/audit batches. Routes to explorer-official.md (TPRA/MTDT/NIC/energy/cloud/state pipeline) and explorer-industry.md (press/vendor/interconnection/state sweep).
---

# SD · 苏丹数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：苏丹**没有**公共设施注册表与建筑电子许可门户；枚举靠拼接 **TPRA 电信牌照**（含“通过自有数据中心提供云计算服务、限 SaaS”的三类牌照）、**MTDT 数字化转型公告**（3x3 计划、Baladna、CONSOLEX）、**NIC/NDC/SIXP 国家信息基础设施**、**SUNA 官方报道**、**运营者官方页**（主要是 Sudatel/Sudani）与 IXP/网络注册表。
> 商业市场极小且 **Sudatel/Sudani 主导**：官方页描述 Khartoum Sudatel Data Center（14,000 m2、四个机房各近 1,000 台服务器、DC 页称 Tier IV 标准）且集团页称运营**两座 Tier III 数据中心**（含 Port Sudan/SAS1 线索）；NIC 国家数据中心 + 1,300 m2 国家数据中心于 **2025-10-09 修复重启**。
> **战争语境是分级必备**（2023-04-15 起 SAF vs RSF）：Khartoum 设施 2023-2025 被占领/破坏（2024-02 全国断网），政府战时在 Port Sudan 运作——任何 Khartoum 状态声称必须带日期并复核。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供苏丹探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：TPRA（2019 牌照条例、三类云/SaaS 牌照、Sudan CERT）、MTDT/SUNA（3x3/Baladna/CONSOLEX/国家 DC 重启）、NIC/NDC/SIXP（nic.gov.sd、PeeringDB ix 2320、2026 更名线索）、能源/电网（SETCo/电力部）、云区域缺席核验、运营者种子表、18 州矩阵与优先级、分级去重规则 |
| `explorer-industry.md` | 行业/厂商发现：媒体源（DCD/Dabanga/Sudan Tribune/Actum SUNA）、运营者/厂商扫描（Sudatel/Zain/MTN/NIC/Canar/EBS/SUDASAT）、官方转轨渠道、英/阿语检索模式、18 州四遍法、超大规模处理、苏丹特定陷阱 |

## 核心结构事实（框定每次搜索）

1. **Sudatel/Sudani 是唯一有当前官方公共 colo/托管/DC 服务页的运营者**（A）：Khartoum SDC 页（14,000 m2、四机房各近 1,000 服务器、Tier IV 标准声称）+ 业务页（集团运营两座 Tier III DC、PaaS/SaaS）+ cloud.sudani.sd；服务：colo、专用/虚拟服务器、SAN、备份/灾备、防火墙、IaaS/云托管；地址/联系页在 Sinkat Street, Khartoum。**Tier 声称是运营者自称**，除非出现 Uptime/独立认证。
2. **Sudatel 第二座 DC / Port Sudan（A 集团级，C 街道级）**：集团业务页列 EASSy/SAS1/SAS2 连接、FY2025 披露 Tier III+ DC 基础设施；聚合器（C）给 Dim Al-Nour Street/SAS1——Port Sudan 街道/容量/状态由 Sudatel/SUNA/海缆运营者确认前保持 C。
3. **NIC/NDC/国家数据中心（A）**：NIC（宪法法令 363/1999 设立，National Information Center Act 2010 重组，MTDT 附属）负责国家信息网络/骨干与数据中心基础设施；Khartoum NDC + 政府托管/VPS；**2025-10-09 部长 Ahmed Dardiri 经 SUNA 宣布 1,300 m2 主国家数据中心修复重启**（含云计算/数据保护/AI 支持系统）——SUNA/部长 A，Actum 英文综合 B；当前运营状态单独分级并复核。
4. **SIXP（B 级历史/陈旧线索）**：PeeringDB ix 2320 列 NIC 组织、Khartoum、4 个对等（PCH AS42/AS3856、Sudatel AS15706、Zain AS36998），最后更新 **2020-01-22**；PCH 目录标 **Defunct** 且无设施/交换机——不得当当前运营证明，经 NIC/SIXP/PeeringDB 更新/实时路由服务器/运营者确认后再用。
5. **NIC 更名线索（2026-05，本地媒体 C/B）**：报道 NIC 转型为“苏丹数据与人工智能管理局（هيئة البيانات والذكاء الاصطناعي السودانية）”——nic.gov.sd/mtdt.gov.sd/法令/SUNA 确认前不得用新名作 A。
6. **战争状态时间线（分级必备）**：2023-04-15 开战；2023-04 至 2025-03 Khartoum 大部被 RSF 控制；RSF 占领 ISP 数据中心引发 **2024-02 全国断网**；2025 无人机/战斗破坏 Khartoum 电力/电信；2025-03 SAF 夺回关键站点、2025-05 宣称 Khartoum 州无 RSF；2025-10-09 国家 DC 重启。
7. **监管 TPRA（A）**：Telecommunications and Post Regulating Act 2018 + 2019 Licensing Regulation；三类牌照 = 通过自有数据中心提供云服务（限 SaaS）——苏丹最接近公共 DC/云授权制度；牌照证明**授权**，不证明具名设施或数量（一牌可盖多设施）。Sudan CERT（tpra3.onespace.sd，2010-01）用于网络事件语境。
8. **政府“数据中心”歧义**：Baladna/3x3/CONSOLEX/州 ICT 计划是计划证据不是设施记录，除非点名站点/运营者；阿拉伯语 `مركز بيانات` 常指政府 IT 室/档案中心/电信交换局——要求计算/托管功能+运营者+地点。
9. **云缺席（A 负）**：AWS/Azure/GCP/OCI 官方区域表无苏丹区域；本地云（Sudani cloud.sudani.sd、NIC 服务）映射到 Sudatel/NIC 站点；聚合器“无直连 on-ramp（2025-09，最近枢纽 Marseille/Nairobi）”按 C 语境。
10. **语言**：阿拉伯语为主（مركز بيانات、مركز البيانات الوطني、استضافة、خوادم/سيرفرات、سحابة/الحوسبة السحابية、التحول الرقمي）+ 英语（data centre/data center/datacentre）；TPRA/MTDT/Sudatel/NIC 页用英语。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§7 / explorer-industry.md §1-§5）

- TPRA：`site:tpra.gov.sd "data centre"`、`site:tpra.gov.sd "cloud" "licence"`、`site:tpra.gov.sd "Licensing Regulation" "2019"`、`site:tpra.gov.sd "third-class" "cloud"`、`site:tpra.gov.sd Sudatel OR Zain OR MTN OR Sudani`。
- MTDT/SUNA：`site:mtdt.gov.sd "data centre" OR "data center"`、`site:mtdt.gov.sd "مركز البيانات"`、`site:suna-sd.net "مركز البيانات"`、`site:suna-sd.net "data centre" OR "digital transformation"`、`"إعادة تأهيل" "مركز البيانات" السودان`。
- NIC/SIXP：`site:nic.gov.sd "data centre" OR "مركز البيانات"`、`site:nic.gov.sd "شبكة المعلومات القومية"`、`"National Data Centre" Sudan NIC`、`site:peeringdb.com/ix/2320`、`"SIXP" Sudan "National Information Center"`、`"المركز القومي للمعلومات" "مركز البيانات"`。
- 运营者：`"Sudatel" "data centre" "Sinkat" OR "Port Sudan"`、`site:sudatel.sd OR site:sudani.sd "data centre" OR "data center"`、`site:cloud.sudani.sd "data center"`、`"Zain" OR "MTN" Sudan "data centre" "كهرب"`。
- 能源：`"data centre" "substation" Sudan OR Khartoum OR "Port Sudan"`、`"power supply agreement" "data centre" Sudan`、`site:setco.sd OR site:moep.gov.sd "data centre"`、`"انقطاع الكهرباء" "مركز بيانات" السودان`。
- 州模板（英/阿）：`Khartoum Sudan "data centre" OR "data center"`、`"Port Sudan" OR "Red Sea" Sudan "data centre"`、`الخرطوم "مركز بيانات"`、`"بورتسودان" OR "البحر الأحمر" "مركز بيانات"`、`"شمال كردفان" OR "جنوب كردفان" OR "غرب كردفان" "مركز بيانات"`、Darfur 五州阿语+`مركز بيانات`。
- 媒体：`site:datacenterdynamics.com/en/news/ Sudan "data centre"`、`site:dabangasudan.org "data centre" OR "مركز بيانات" OR "internet shutdown"`、`site:sudantribune.com "data centre" OR "التحول الرقمي"`、`site:actumsudan.substack.com Sudan data centre`。
- 云：`"cloud region" Sudan AWS OR Azure OR Google OR Oracle`、`site:cloud.sudani.sd "data center"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **TPRA（A 授权）**：提取牌照类/持有人/服务范围（SaaS/云/colo）/牌照号日期/法人（Sudatel Telecom Group、Zain Sudan Ltd、MTN Sudan、EBS…）；牌照不是设施计数。
- **MTDT/SUNA（A 计划/公告）**：3x3 数字化转型计划/CONSOLEX API 网关（e-government 计划证据）；Baladna 平台（2025-10，Khartoum 试点，租户/需求信号非设施）；SUNA 为政府 DC/ICT 公告主渠道。
- **NIC/NDC（A）**：nic.gov.sd 托管/VPS 服务、国家信息网络职责、NDC 存在证据（ITU 2016 议程、SIXP 流量研究）；SIXP 现状 B/C（PCH Defunct）；2026 更名 C/B。
- **能源（A 佐证）**：SETCo 输变电、电力部、变电站/发电机/柴油/水电（Nile）；战时停电语境（2025 无人机打击，B）；电力证据不得单独转成设施记录。
- **海缆（B 连接性）**：EASSy/SAS1/SAS2 在 Port Sudan 登陆——连接性非 DC 容量。
- **云缺席（A 负）**：四家官方区域页；区域声称按服务/伙伴线索处理。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **媒体（B）**：DCD（非洲全域条目）、Capacity Media/Developing Telecoms/Balancing Act/IT News Africa/CIO Africa、SUNA（引官员 A）、Dabanga（独立强源，战争/断网/设施损坏）、Sudan Tribune、Altaghyeer（B/C）、Actum Sudan（政策/数字简报，2025-10 Khartoum DC 重启）、Zain 集团年报（A/B）、Totogi/Light Reading/cloudcomputing-news（Zain 计费/生产/DR 迁到 AWS 上——B）、PeeringDB/PCH/sixp.sd（B/C 陈旧）。
- **运营者/厂商**：Sudatel/Sudani（A 服务/设施存在；Tier 自称）、Zain Sudan（B/C 核心/DR 线索，**不是可计数公共 DC**；集团游说“固定/数据中心服务权利”非设施）、MTN Sudan（C）、NIC/NDC/SIXP（A/B）、Canar/Canartel Al-Mashtal Street（C，Canar 并入 Sudani，与 SDC 可能不同站点或重复旧条目）、EBS 电子银行服务（C，SWIFT 服务中心，加入 CBOS 证据）、SUDASAT（卫星回程，非 DC，排除除非托管证据）、ISP/转售商（C，不重复计在 Sudatel 设施之后）、厂商（Huawei/ZTE/Ericsson/Vertiv 等，B/C）。
- **状态动词捕获**：`announces/MoU/plans`=意图（C/B）；`rehabilitates/reactivates/reopens`=战后恢复（B/A 若官方）；`occupied/damaged/shutdown`=战争状态（B，带日期）；`operational/launched/hosts`=运营信号（用运营者/官方页核验到 A）。
- **聚合器去重**：datacentermap（2 个 Sudatel 站点）、datacenterplatform（3 含 Canartel）、inflect（1 Canar）指向同一小池——按运营者+街道核对，绝不单独用于 A 级状态/容量。
- **防重**：Sudatel SDC Khartoum（Sinkat St）vs Canar/Sudani Al-Mashtal 设施——每个物理站点一条规范记录并注明不确定性。

## 来源分级

- **A** = 一手/官方/法律：TPRA 牌照或官方页、MTDT/NIC/SIXP 官方材料、SUNA 官方报道、州/政府公告、运营者官方设施页、云厂商官方声明。
- **B** = 强二级：Dabanga、Actum Sudan、Sudan Tribune、可信贸易/本地媒体、PeeringDB/PCH 记录、Uptime 类或运营者佐证的公告、复现运营者数据的可信聚合器。
- **C** = 弱线索：通用市场报告、社交帖、无依据目录条目、无设施证据的 NGO/智库片段、旧 MoU。
- **状态时效**：2023-2025 期间关于 Khartoum DC 的任何文字可能数周内过时；每条记录带日期，优先 2025-10+ 源并仍复核当前运营。
- **云区域 ≠ 设施**：无超大规模区域；本地云映射到 Sudatel/NIC 站点；电信交换机/机房不是商业 DC（除非源描述具名设施上的托管/colo/云服务）。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=SD，divisions=18 州）。
2. 种子：Sudatel/Sudani 官方页（SDC/业务/云）+ NIC + SUNA/MTDT + TPRA 牌照 + 海缆（EASSy/SAS1/SAS2）。
3. 每州四遍：①媒体/厂商（州+主要城镇+英/阿 DC 术语）；②运营者（Sudatel/Zain/MTN/NIC/EBS+州首府）；③官方（SUNA/MTDT/NIC/TPRA/州政府 ICT）；④互联/聚合器（SIXP/PeeringDB、datacentermap 等——验证前不升 C）。
4. Khartoum 深扫：SDC、NIC/NDC/国家 DC、SIXP、Canar Al-Mashtal、Zain/MTN 核心、EBS；加战争词（RSF、occupation、rehabilitation、Feb 2024 shutdown）；Port Sudan 次扫：第二 DC/SAS1、海缆登陆、政府迁移。
5. 每个线索提取：运营者/项目、州/市/街道、类型（商业 colo/云服务/国家 DC/IXP/电信核心/银行机房）、阶段+日期、容量（MW/机架/m2）、电力、连接性、承包商/出资方、源 URL/日期/等级。
6. 去重：Sudatel SDC vs Canar（Sinkat vs Al-Mashtal）；聚合器计数冲突按运营者+街道核对；政府计划与设施分开；Kordofan/Darfur 冲突区做可辩护的负搜索（州部委+SUNA+运营者），不把 NGO 机房当 DC。
7. 输出与 world 探索同 schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；状态带日期；无容量用 null。
8. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核苏丹数据中心（18 州粒度，Khartoum/Red Sea 深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：国家 DC（1,300 m2）重启后的实际运营状态与地址、Sudatel 两座 Tier III DC 的独立认证（Uptime 等）、Port Sudan 街道/容量官方确认、SIXP 是否恢复（PeeringDB 更新）、NIC 更名法令、Zain 是否获固定/数据中心服务权并建公共设施、2025-10 后 Khartoum 电力/无人机恢复对设施的影响。
