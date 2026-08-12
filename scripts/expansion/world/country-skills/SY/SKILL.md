---
name: sy-datacenter-methodology
location: scripts/expansion/world/country-skills/SY/SKILL.md
description: |
  Syria (SY) data-center enumeration methodology. Division model: 14 governorates (Damascus, Aleppo, Homs, Hama, Latakia, Tartus, Daraa, Suwayda, Quneitra, Idlib, Raqqa, Deir Ezzor, Hasaka, Damascus Countryside). No public datacenter registry and no public online planning-permit register; a record is a facility only when evidence names an operating or planned facility with site/owner/type/status/date. No AWS/Azure/GCP/Oracle cloud region listed for SY (negative evidence). Market is discovery-heavy and facility-light: strongest leads are Mijad/Sham Cloud (Damascus, SANA-reported) and Ministry of Higher Education IT center (Damascus); SilkLink (5 planned IXPs), Medusa/Ugarit/Aletar cable landings (Tartus) and Go/Etihad Atheeb MoU are connectivity/program-level, not facilities. Electricity is a gating condition; verify power evidence separately. Read this before running SY exploration/audit batches. Routes to explorer-official.md (MOCT/Digital Syria/SYTPRA/SANA/SIA/utility playbook) and explorer-industry.md (trade press/vendor/catalog seeding).
---

# SY · 叙利亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：叙利亚无公共数据中心注册库、无公开在线规划许可登记册，枚举靠「部委/监管/投资机构 + 官方新闻 SANA + 运营商 + 目录/贸易媒体」多轨交叉。电力是任何叙利设施的门槛条件，须单独核实电力证据；MoU、IXP、海缆登陆、移动核心网不得升格为设施。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：MOCT、Digital Syria、SYTPRA、SANA、投资局 SIA、叙电信/移动运营商、电力当局、海缆/IXP 分类、14 省逐省策略 |
| `explorer-industry.md` | 行业/厂商管线：DCD/Capacity/Developing Telecoms 等贸易媒体、STC/Go/Mijad/Sham Cloud 线索、Uptime 核验、阿/英搜索库、验证规则 |

## 核心结构事实（框定每次搜索）

1. 行政划分：**14 个省（governorate）** = 大马士革、阿勒颇、霍姆斯、哈马、拉塔基亚、塔尔图斯、德拉、苏韦达、库奈特拉、伊德利卜、拉卡、代尔祖尔、哈塞克、大马士革农村省。repo 分区即这 14 省；仅当来源点名城市/省/工业城/港口/大学/登陆点/IXP 位置时才路由到具体省。
2. **无数据中心注册库、无公开规划许可登记册**。只有证据点名「运营或规划中的设施」（含场地、业主/运营商、设施类型、状态、来源日期）才算设施记录。国家数字计划、移动牌照、IXP、海缆登陆、MoU、云厂商意向均为线索。
3. **无超大规模云区域**（A 级否定证据）：AWS/Azure/GCP/Oracle 官方区域页均未列叙利亚。与 Google/Amazon/Oracle/Microsoft 的「可能合作」声明属愿景，除非官方区域/可用区/本地区/边缘公告点名叙利亚。
4. 关键官方面：**MOCT**（https://moct.gov.sy，项目页/Telegram https://t.me/moct_gov）为官方意图与范围 A 级，除非页面点名物理 DC 场地否则不是设施证明；**Digital Syria**（https://www.digitalsyria.sy）的 National Data Center 项目页（https://www.digitalsyria.sy/project/113-mshroaa-mrkz-almaatyat-alotny）为 A 级程序级线索——无省/地址/MW/机架/运营商/开放日期，记 `program-level/planned` 而非运营设施；**SYTPRA**（https://sytpra.gov.sy）A 级用于牌照事实与持牌电信/ISP 实体，非 DC 注册库；**SANA**（https://sana.sy, /en/）A 级用于官方公告（注意其也转载国外科技新闻）；**SIA 投资局**（https://invest.gov.sy）A 级用于投资牌照与一站式分支，公开站点无检索式 DC 牌照登记册。
5. 运营商页为自身服务 A 级；旧交换局、移动核心机房、网络 PoP 不是商业数据中心，除非运营商或可靠源点名托管/云/colo/DC 服务或认证设施。
6. 电力为门槛条件：电力部（经 SANA/MOCT 链接找当前官方域名）、PEEGT（المؤسسة العامة لتوليد ونقل الكهرباء）、各省电力公司；不得把电信项目误当可建 DC 场地。
7. 状态语义（精确使用）：`operational`（在用/已开放且点名业主运营商）、`under_construction`（开工/EPC/电力连接/实体建设）、`licensed`（有 SYTPRA/SIA/MOCT 牌照但无场地证明）、`program-level`（国家计划/Digital Syria 项目/RFI/战略）、`MoU`（非约束或框架协议，不计为设施）、`connectivity`（仅 IXP/海缆/骨干/传输）、`negative`（官方云区域页或来源扫描未发现叙利亚设施）。
8. 语言：阿拉伯语核心词 `مركز بيانات / مركز المعطيات / مراكز البيانات / مراكز المعطيات`、托管/云 `استضافة / خدمات الاستضافة / خوادم / حوسبة سحابية / سحابة`、连接 `نقطة تبادل إنترنت / نقطة تبادل / كابل بحري / محطة إنزال / ألياف ضوئية`、状态 `مذكرة تفاهم / اتفاقية / ترخيص / إجازة استثمار / تخصيص أرض / وضع حجر الأساس / بدء الأعمال / افتتاح / تدشين / إطلاق`、电力 `كهرباء / محطة تحويل / أحمال / مولّدات / طاقة شمسية / بطاريات / ميغاواط`；英文同样全套。

## 查询模式（复制粘贴模板见 explorer-official.md §1-2 与 explorer-industry.md §2-5）

- MOCT：`site:moct.gov.sy ("مركز بيانات" OR "مركز المعطيات" OR "مراكز البيانات")`、`site:moct.gov.sy ("استضافة" OR "حوسبة سحابية")`、`site:moct.gov.sy ("سيلك لينك" OR SilkLink)`、`site:moct.gov.sy ("كابل بحري" OR "محطة إنزال" OR طرطوس)`。
- Digital Syria：`site:digitalsyria.sy ("مركز المعطيات الوطني" OR "مركز بيانات" OR "البيانات الوطنية")`、`site:digitalsyria.sy ("حوسبة" OR "سحابة" OR "استضافة" OR "منصة")`。
- SYTPRA：`site:sytpra.gov.sy ("مركز بيانات" OR "استضافة" OR "حوسبة سحابية")`、`site:sytpra.gov.sy ("دليل المرخص لهم" OR "المرخص لهم")`、`site:sytpra.gov.sy ("زين" OR "رخصة المشغل الخليوي")`。
- SANA：`site:sana.sy ("مركز بيانات" OR "مركز المعطيات" OR "مراكز البيانات") سوريا -نيويورك -الفضاء`、`site:sana.sy ("مجاد" OR "شام كلاود" OR "Uptime Institute")`、`site:sana.sy ("سيلك لينك" OR "كابل بحري" OR "محطة إنزال")`、`site:sana.sy/en ("data center" OR hosting OR cloud) Syria`。
- SIA/运营商/电力：`site:invest.gov.sy ("مركز بيانات" OR "مراكز البيانات" OR "حوسبة سحابية")`、`site:syriantelecom.com.sy ("مركز بيانات" OR "استضافة" OR "سحابة")`、`site:syriatel.sy ("مركز بيانات" OR "استضافة" OR "cloud")`、`"وزارة الكهرباء" ("مركز بيانات" OR "أحمال كبيرة")`、`"شركة كهرباء {governorate_ar}" ("أحمال" OR "محطة تحويل")`。
- 行业（B）：`site:datacenterdynamics.com Syria ("data center" OR SilkLink OR Medusa OR Ugarit)`、`site:capacitymedia.com Syria ("data centre" OR "submarine cable" OR Tartous)`、`site:developingtelecoms.com Syria ("Ugarit" OR "Syrian Telecom")`、`site:submarinenetworks.com Syria ("Aletar" OR "Medusa")`、`site:syria-report.com Syria (telecom OR electricity)`、`site:english.enabbaladi.net Syria ("Ugarit" OR "SilkLink")`。
- 目录（C 种子）：`site:datacentermap.com Syria`、`site:baxtel.com Syria`、`site:cloudscene.com Syria`、`site:datacenters.com Syria`、`site:peeringdb.com Syria ("IXP" OR "Syrian Telecom")`、`site:uptimeinstitute.com/tier-certification/tier-certification-list Syria`。目录负面结果应记录为「检查当日无目录/认证列示」，不得证明不存在。

## 官方/监管管线要点（详见 explorer-official.md）

- **SilkLink**：官方 RFI（https://silklink.moct.gov.sy/pages/introduction.html）——骨干目标、ITU-T G.652/G.655 光纤、初期 10 Tbps/未来 25 Tbps、五个 IXP（大马士革、阿勒颇、塔尔图斯、帕尔米拉、卡米什利）、批发互联网服务、叙利亚电信运营、MOCT 监管。A 级程序设计；五个 IXP 不得计为运营 DC。STC 中标（DCD 2026-02-12）为 B 级建设细节。
- **Medusa 塔尔图斯登陆**：MOCT 项目页 + Medusa 官网（https://medusascs.com/news/tartous-syria-medusa-signs-agreement-with-syria-telecom-to-establish-a-new-east-to-west-route/）——记 `cable landing/landing station lead`，非 DC。**Ugarit/Ugarit 2**：SANA 英文一阶段报道（https://sana.sy/en/syria/354083/），海缆/登陆站证据，除非点名托管/colo。**Aletar 断缆**（DCD 2026-06-18）：路由多样性/断供风险证据，非 DC 证据。
- **Go / Etihad Atheeb MoU**（DCD 2025-07-28）：与叙政府的数据中心相关 MoU，设施细节不明，记 `status=MoU`。
- **Mijad/Sham Cloud**（SANA https://sana.sy/economy/2464512/，2026-05-01 大马士革 Syria HiTech 12）：点名 Mijad Technical Services、Sham Cloud、Mijad 私有数据中心、与 CanaGulf 及 Uptime Institute 代表的 MoU。SANA 报道的陈述 A 级；Uptime 认证须直接核验后才记录等级。**教育部 IT 中心**（https://sana.sy/education/2350216/）：大马士革公有/教育托管设施，非商业 colo。**Zain 第二移动牌照**（https://sana.sy/economy/syrian-economy/2519276/）：A 级牌照事实，无 DC 场地。
- 流程：全国官方扫描 → 只提取具名项目并按状态分类 → 仅当来源点名位置时路由到省 → 低概率省跑完查询并记录负面搜索 → 每个设施候选查电力证据 → 查超大规模区域页并记录负面 → 认证声明直接对 Uptime 核验。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场形态：叙利亚商业 DC 市场极薄，多为程序级/连接级/小型私人与政府托管；当前为「发现重、设施轻」。最强的设施型线索 = 大马士革 Mijad/Sham Cloud 与教育部 IT 中心，均需运营商/规格/认证跟进。
- 实体线索表：**Syrian Telecom**（骨干/国际网关/登陆站/托管/PoP；自有声明 A）；**STC Group**（SilkLink 运营/开发；B/A，站点细节需 MOCT/SANA/STC 核验）；**Go/Etihad Atheeb**（仅 MoU，B）；**Mijad/Sham Cloud**（A/C，核验认证与地址）；**CanaGulf**（Mijad 认证/咨询伙伴，B/C）；**Uptime Institute**（仅当设施直接出现在认证列表才 A）；**Syriatel**（移动核心/网络机房，非 colo 除非点名托管/DC 服务）；**MTN Syria/Zain**（牌照与未来移动核心基建，重命名期间避免重复计数）；**UNIFI/CYTA**（Ugarit 路由/登陆站，B/A）；**Medusa 联盟**（塔尔图斯登陆，A/B）；**银行/公共部门**（企业 DC，通常私有难核验，B/C）。
- 验证规则：只有运营商/政府/认证源点名在用设施功能才升格 operational；只有建设/EPC/土地/许可/电力连接/官方进展证据才升格 under_construction；MoU 保持 MoU；SilkLink IXP 保持 connectivity 直到 IXP 启动或点名共置设施；Medusa/Ugarit/Aletar 保持海缆/登陆站；Zain/Syriatel/MTN 为电信/移动基建线索，移动核心网不计商业 colo；每个正面候选搜电力词，`power_evidence` 与带宽/海缆容量分开存。

## 来源分级

- **A**：叙政府/部委/监管/投资机构/省级来源、SANA 官方新闻、运营商官方页、官方云区域文档、Uptime 认证列表（若有叙利奖项）。
- **B**：成熟贸易媒体、通讯社（Reuters/AP/AFP B+）、法律/投资指南、厂商案例、具名会议材料。
- **C**：目录、社交（LinkedIn/X/FB/Telegram）、营销页、市场报告公关、无来源本地文章。仅线索。

## 使用流程（探索/复核批次）

1. 读本 SKILL.md 与两份 explorer 报告，确定目标省与候选项。
2. 全国官方扫描：MOCT、Digital Syria、SYTPRA、SIA、SANA 阿/英、叙利亚电信。
3. 只提取具名项目并按状态分类（operational/construction/licence/program-level/MoU/connectivity/negative）。
4. 仅当来源点名位置（城市/省/工业城/港口/大学/登陆点/IXP）时路由到 14 省之一；对低概率省（Quneitra、Suwayda、Hama、Idlib、Raqqa、Deir Ezzor）跑完查询并记录负面。
5. 每个设施候选查电力证据（电力部/PEEGT/省电力公司）；查官方超大规模区域页并记录负面叙利亚结论。
6. 认证声明直接对 Uptime Institute 核验后才记 tier。
7. 遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:06Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] Mijad/Sham Cloud：直接核验 Uptime 列表、地址与运营商规格。
- [ ] SilkLink：STC 运营细节、五个 IXP 站点进度、任何点名 DC 的官方/运营商证据。
- [ ] Go/Etihad Atheeb MoU：等待 MOCT/SIA/SANA 点名场地、土地、容量或建设。
- [ ] 待核实：Medusa 塔尔图斯登陆站设施服务（托管/colo 证据）；教育部 IT 中心是否对外提供商业托管。
