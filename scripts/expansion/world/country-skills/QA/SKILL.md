---
name: qa-datacenter-methodology
location: scripts/expansion/world/country-skills/QA/SKILL.md
description: |
  Qatar (QA) datacenter discovery & audit methodology — how to enumerate, verify, and update Qatari datacenter projects at municipality (baladiyah) granularity (8 municipalities: Doha, Al Khor, Ash Shamal, Al Rayyan, Al Shahaniya, Umm Salal, Al Wakrah, Al Daayen). Qatar has no public datacenter registry and only aggregate (non-project-level) building-permit data: enumeration joins CRA telecom licensing and Decision 12/2026 cable-access policy, MCIT Government Data Center / Hukoomi hosting, QFZ free zones (Ras Bufontas, Umm Alhoul) and Invest Qatar, Kahramaa/Ashghal utility evidence, official cloud-region pages (Google Cloud Doha me-central1, Azure Qatar Central qatarcentral; no AWS/OCI public region), operator pages (Ooredoo, Syntys/Q Data, MEEZA M-VAULT 1-5), and QIX/Doha IX + cable-landing records. Read this before running QA exploration/audit batches. Routes to explorer-official.md (regulators/government/free zones/cloud/procurement) and explorer-industry.md (operators/press/IXP/cables/directories/Arabic recipes).
---

# QA · 卡塔尔数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：卡塔尔**没有**公开的全国数据中心注册库，公共建筑许可数据是**聚合级**（按市镇与建筑类型，非项目级）；枚举必须三角验证 CRA 电信记录、MCIT 政府托管、自由区页面、Kahramaa/Ashghal 基础设施、采购门户、云区域页、IX/海缆记录与行业媒体。**云区域/IXP/海缆登陆站/投资基金/MoU 本身不算数据中心建筑**。
> 分区模型：**8 个市镇（baladiyah）**（Doha、Al Rayyan、Al Daayen、Al Wakrah、Al Khor、Ash Shamal、Al Shahaniya、Umm Salal）；Doha 都会区为核心，但非所有 “Doha” 线索都归 Doha 市镇——QSTP/Education City → Al Rayyan，Umm Qarn/Lusail → Al Daayen，Umm Alhoul/Hamad Port/Mesaieed → Al Wakrah。
> 已知种子：Ooredoo Qatar Data Centres（5 座设施 ~60,000 sq ft）+ GDC2、Syntys/Q Data QFZ（5 MW 运营 + 7.5 MW 在建）、MEEZA M-VAULT 4/5（QSTP，Al Rayyan）、M-VAULT 2（Umm Qarn，Al Daayen，QIX 落点）、Google Cloud Doha `me-central1`、Azure Qatar Central `qatarcentral`、Doha IX（Ooredoo + DE-CIX）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供卡塔尔探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：CRA（Emiri Decree 42/2014、个体牌照、SCLS Decision 12/2026）、MCIT Government Data Center/Digital Agenda 2030、Hukoomi/开放数据、市政与建筑许可（聚合数据）、Kahramaa/Ashghal、QFZ/Invest Qatar/QFC、采购、云区域官方页（GCP/Azure/AWS/OCI）、8 市镇逐区枚举 |
| `explorer-industry.md` | 行业/厂商发现：运营商管道（Ooredoo/Syntys/MEEZA/Vodafone/QNBN/GBI）、DCD/Gulf Times/Peninsula/Zawya 等媒体、QIX/Doha IX/DE-CIX/PeeringDB、Submarine Networks 海缆（AAE-1/FALCON/GBI/Qatar-UAE 等）、目录（C）、阿拉伯语搜索配方、已知设施/信号表、规范化规则 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库、无项目级许可**：data.gov.qa 建筑许可数据集仅用于了解市镇建设体量与许可类别；设施记录需要运营商、政府公告、公用事业/NOC 证据、采购引用或点名项目的强媒体。
2. **CRA 是电信/互联/云政策主监管**：固定牌照持有者 Ooredoo QPSC、Vodafone Qatar QPSC、Qnbn QPJSC 等（Individual Licenses 页）；CRA Decision No. (12) of 2026 关于 SCLS 国际互联服务接入（官方支持海缆接入背景，非建筑证据）。
3. **政府托管服务存在但地址未公开**：MCIT Government Data Center 页确认政府托管（空间/电力/冷却/物理安全/连接），无街道地址——不赋市镇，除非他源点名。
4. **自由区是重点宿主地理**：Ras Bufontas（机场自贸区，Doha/HIA 区域，QFZ 将云数据服务列为入驻行业）；Umm Alhoul（港口自贸区，Al Wakrah）；Q Data QFZ 精确园区（Ras Bufontas vs Umm Alhoul）未公开——保持 unknown/Qatar Free Zones。
5. **云区域 A 仅于区域存在**：Google Cloud Doha `me-central1`（a/b/c）、Azure Qatar Central `qatarcentral`（Doha，AZ 支持）；AWS/OCI 无卡塔尔公共区域（A 缺席）；不推断建筑/地址。
6. **IXP 与海缆分离记账**：**QIX**（qix.qa 落点 = MEEZA MV2, Umm Qarn → Al Daayen）与 **Doha IX**（Ooredoo + DE-CIX，托管于 Ooredoo 数据中心，无建筑地址）是不同实体；海缆登陆站（Ooredoo Doha CLS、Halul Island CLS、Vodafone North Doha CLS）为连接性证据；2Africa 的 Ooredoo 声明属阿曼非卡塔尔。
7. **M-VAULT 家族勿混**：MV2（Umm Qarn/Al Daayen）≠ MV4/5（QSTP/Al Rayyan）；MV3 的 Tier III/LEED Gold 为运营商声明（A 声明/C 位置）；DCD 报道 MEEZA 2026 完成 4 MW 超大规模客户扩容（B，建筑/客户未披露）。
8. **语言**：英语 + 阿拉伯语 `مركز بيانات`/`استضافة`/`الحوسبة السحابية`/`نقطة تبادل الإنترنت`/`الكابلات البحرية`/`رخصة بناء`/`كهرماء` + 市镇阿语名（الدوحة/الريان/الضعاين/الوكرة/الخور/الشمال/الشحانية/أم صلال）双轨搜索。

## 查询模式（复制粘贴模板见 explorer-official.md §2-§3 / explorer-industry.md §2-§4）

- CRA：`site:cra.gov.qa ("data centre" OR "data center" OR "مركز بيانات")`、`site:cra.gov.qa ("cloud" OR "cable landing" OR "internet exchange")`、`"CRA" Qatar "Decision No. (12) of 2026" "SCLS"`。
- 政府托管：`site:mcit.gov.qa ("Government Data Center" OR "data centre")`、`site:hukoomi.gov.qa ("Shared Government Data Center" OR "Government Data Center")`、`"مركز البيانات الحكومي" قطر`。
- 许可/市政：`site:mme.gov.qa OR site:mun.gov.qa ("data centre" OR "مركز بيانات")`、`"رخصة بناء" "مركز بيانات" قطر`、`site:data.gov.qa "Total Building Permits Issued" municipality`。
- 公用事业：`site:km.qa ("data centre" OR "substation" OR "MW")`、`site:ashghal.gov.qa ("data centre" OR ICT)`、`"Kahramaa" "data centre" Qatar`、`"district cooling" "data centre" Doha OR Lusail OR QSTP`。
- 自由区/投资：`site:qfz.gov.qa ("data centre" OR "cloud data" OR "مركز بيانات")`、`site:qfz.gov.qa ("Ras Bufontas" OR "Umm Alhoul") ("data" OR "digital" OR "cloud")`、`site:invest.qa ("data centre" OR "digital infrastructure")`。
- 云：`"Google Cloud" "Doha" "me-central1" ("MEEZA" OR "QFZ" OR "QSTP")`、`"Azure" "Qatar Central" "qatarcentral"`、`"AWS" Qatar ("edge location" OR CloudFront OR Outposts)`、`"Oracle" Qatar ("dedicated cloud" OR "public cloud region")`。
- 运营商：`site:ooredoo.qa ("Qatar Data Centre" OR "Government Data Centre" OR GDC2)`、`site:syntys.com Qatar "Q Data QFZ" OR "data centre"`、`site:meeza.net ("M-VAULT" OR "data centre")`、`site:qix.qa ("MV2" OR "Umm Qarn")`。
- 互连/海缆：`"QIX" OR "Qatar Internet Exchange" "Umm Qarn" OR "MV2"`、`"Doha IX" Ooredoo DE-CIX "data centers"`、`"Doha Cable Landing Station" Ooredoo`、`"Halul Island" "cable landing"`、`"2Africa" Qatar "landing" -Oman`。
- 市镇/阿语：`"Umm Qarn" "MEEZA" OR "M-VAULT 2" OR "QIX"`（Al Daayen）、`"QSTP" OR "Qatar Science and Technology Park" ("M-VAULT" OR MEEZA)`（Al Rayyan）、`"Umm Alhoul" ("data centre" OR "cloud data services")`（Al Wakrah）、`"الدوحة" "مركز بيانات" "أوريدو"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 入口：CRA → MCIT GDC/Hukoomi → 市政许可（聚合）→ Kahramaa/Ashghal → QFZ/Invest Qatar/QFC → 采购（Hukoomi tenders、机构页）→ 云区域官方页；每市镇必跑英语+阿语，负向市镇（Al Khor、Ash Shamal、Al Shahaniya、Umm Salal）记录搜索日期与词项。
- 已知官方/主源矩阵：Ooredoo 组合（A 组合/C-U 单址）、Ooredoo GDC2（A 服务/U 址）、Syntys/Q Data QFZ（A 收购/容量/U 园区）、M-VAULT 4/5（A，QSTP/Al Rayyan）、M-VAULT 2/QIX 落点（A QIX 点/C 目录容量）、Google/Azure 区域（A 区域）、Doha IX（A IXP）、QIX（A IXP/位置）、海缆 CLS（B 连接性）、AWS/OCI 缺席（A）。
- 规范化：不因云区域/AZ/IXP/登陆站/投资载体/MoU 建设施记录；QIX 与 Doha IX 分离；MV2 与 MV4/5 分离；自由区项目在园区点名前不映射；容量字段区分 IT 负荷 MW/总装机/电网输入/太阳能/面积/投资额。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商：Ooredoo（A 组合/服务；地址 C/U）、Syntys（A 自身发布：Q Data QFZ 5 MW + 7.5 MW）、MEEZA（A 运营商声明：Tier III/ISO/LEED、MV4 为卡塔尔最大 DC 建筑、MV5 QSTP）、Vodafone Qatar（U 设施/ A-B 电信事实）、QNBN（A 牌照上下文，非 DC 运营商）、GBI（B 上下文，经 Ooredoo/Vodafone 落地）、QSTP 目录（A 租户/简介）。
- 媒体/库：DCD Qatar tag（MEEZA 扩容、Syntys 分拆/收购、4 MW 超大规模扩容 B）、Gulf Times、The Peninsula、Qatar Tribune、Zawya、The Fast Mode、Telecom Review、W.Media、Middle East AI News（B）；Submarine Networks（B）；ISOC Pulse QIX（B/C）。
- 目录（C）：Data Center Map（MV2 Umm Qarn 线索，可能 429）、Baxtel、datacenters.com、Cloudscene、DatacenterHawk、PeeringDB（ix/4715、fac/13248）。
- 状态措辞：`operational/launched/handed over` 可支撑设施（若点名运营商/项目）；`MoU/partnership/investment/JV/fund` 仅背景，除非含土地/电力/建设/运营设施。

## 已知设施/项目与证据状态

| 设施/项目 | 市镇 | 状态与证据 |
|---|---|---|
| Ooredoo Qatar Data Centres 组合（5 座，~60,000 sq ft） | Doha/卡塔尔；单址未公布 | A（Ooredoo 官方页组合声明）；单址地址 C/U |
| Ooredoo GDC2 / 政府托管服务 | 址未公开 | A（MCIT/Hukoomi/Ooredoo 确认政府托管 + Tier III GDC2 措辞）；址 U |
| Syntys / Q Data QFZ | Qatar Free Zones；园区未定 | A（Syntys/Ooredoo：5 MW 运营 + 7.5 MW 在建，超大规模设施）；园区 U |
| MEEZA M-VAULT 4 | Al Rayyan/QSTP | A（MEEZA 官方发布：卡塔尔最大 DC 建筑） |
| MEEZA M-VAULT 5 | Al Rayyan/QSTP | A（MEEZA 官方发布点名 QSTP） |
| MEEZA M-VAULT 2 / QIX 落点 | Al Daayen/Umm Qarn | A（qix.qa 联系页点名 MV2, Umm Qarn）；目录容量/地址 C |
| MEEZA M-VAULT 3 | 卡塔尔；精确映射待佐证 | A（运营商声明 Tier III/LEED Gold）；位置/容量 C |
| MEEZA 4 MW 超大规模扩容 | MEEZA 设施；建筑/客户未披露 | B（DCD/MEEZA 新闻：2026 完成/移交） |
| Google Cloud Doha `me-central1` | Doha 都会区 | A（Google 官方区域/专区文档）；仅区域 |
| Microsoft Azure Qatar Central `qatarcentral` | Doha 都会区 | A（Microsoft Learn）；仅区域 |
| Doha IX | Doha/Ooredoo 设施，无地址 | A（Ooredoo + DE-CIX 官方发布：托管于 Ooredoo 数据中心） |
| QIX | Al Daayen（经 MV2/Umm Qarn） | A（qix.qa 官方） |
| Ooredoo Doha CLS / Halul Island CLS / Vodafone North Doha CLS | Doha / Halul 离岸 | B（Submarine Networks：AAE-1/FALCON/FOG/GBI/Qatar-UAE/TGN-Gulf）；连接性证据 |
| Vodafone Qatar 数据中心服务 | 未知 | U（公共设施证据薄弱；仅线索） |
| GBI | QSTP/公司线索 | B（上下文；经 Ooredoo/Vodafone 落地） |
| Energy City Qatar / NavLink DC MoU | Al Daayen/Lusail | C/U 历史（2007 MoU；无现行建设证据） |
| AWS / Oracle OCI 卡塔尔公共区域 | 无 | A（官方区域列表缺席） |
| Qai/Brookfield、Blue Owl/QIA、Nvidia/Ooredoo | 投资/技术背景 | B 上下文；本身无卡塔尔设施 |

## 更新节奏

- 每月：CRA 新闻/文档、MCIT/Hukoomi GDC 页、QFZ/Invest Qatar、Ooredoo/Syntys 页、MEEZA 新闻、DCD Qatar tag、Gulf Times/Peninsula/QNA 搜索。
- 季度：Google/Azure/AWS/Oracle 官方区域表、qix.qa 与 Doha IX/DE-CIX 页、PeeringDB、Submarine Networks/TeleGeography、Uptime 认证目录。
- 待办（2026-08-12）：两份 explorer 初稿已完成（codex 复核）；下一步 codex terra agent 分批复核（8 市镇粒度）；本 skill 作为国家层参考注入。
