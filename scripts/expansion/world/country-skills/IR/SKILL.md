---
name: ir-datacenter-methodology
location: scripts/expansion/world/country-skills/IR/SKILL.md
description: |
  Iran (IR) datacenter discovery & audit methodology — how to enumerate, verify, and update Iran datacenter projects at province + city granularity (31 provinces). Iran has no single open planning-permit database or facility registry: enumeration triangulates ICT-ministry / provincial-ICT announcements, CRA/Ratel license holders (operator census), ITO datacenter-rating and Iran Cloud (ابر ایران) records, TIC/IXP anchors, power/grid evidence (Tavanir, regional distribution companies), municipal/DOE/land permits, domestic cloud & colo operator pages, and Persian trade press. Persian-first searching is mandatory; English misses most official pages. Read this before running IR exploration/audit batches. Routes to explorer-official.md (official/regulatory/cloud pipeline) and explorer-industry.md (trade press / vendor discovery).
---

# IR · 伊朗数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：伊朗**没有**统一开放的全国规划许可/设施注册库（无 FOIA、无统一许可搜索），楼宇许可归市政、电信/云授权分散在 ICT 监管机构与政务服务门户，不能按美欧方式直接枚举。
> 伊朗枚举靠**波斯语优先的多轨三角测量**：ICT 部与省级 ICT 管理局公告（مرکز داده استانی）、CRA/Ratel 持牌运营商（运营商普查）、ITO 数据中心评级与「伊朗云」（ابر ایران）计划、TIC/IXP 地理锚点、电力证据（Tavanir 与区域配电公司）、市政/环境/土地许可、国内云与 IDC 运营商官方页、波斯语行业媒体。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供伊朗探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：CRA/Ratel 持牌页、ITO 评级与 Iran Cloud、国家许可门户 mojavez.ir、ICT 部与省级子域、TIC/IXP、Tavanir 电力、DOE/市政/土地许可、全球超大规模商负向对照、国内云/colo 运营商表、31 省优先级表 |
| `explorer-industry.md` | 行业/厂商发现：波斯语 ICT 媒体（Peivast/CITNA/Digiato/Zoomit/ITMen/官媒）、IranNSR 行业协会、目录与网络情报（DataCenterMap/Cloudscene/PeeringDB/RIPE）、运营商扫描清单、逐省波斯语模板、分级规则 |

## 核心结构事实（框定每次搜索）

1. **无统一设施注册库**：官方最有力的技术轨迹来自 ICT 部生态——CRA/Ratel 持牌商（运营商普查，非设施普查）、ITO 数据中心评级与云服务计划、TIC/IXP 公告、省级 ICT 管理局、MCI/TCI/ISP 官方公告。
2. **波斯语优先**：核心词 `مرکز داده` / `دیتاسنتر` / `دیتا سنتر` / `مرکز داده استانی` / `مرکز داده ملی` / `زیرساخت ابری` / `ابر ایران` / `کولوکیشن` / `مرکز تبادل ترافیک`；英文搜索漏掉绝大多数官方页。
3. **省级政府数据中心 ≠ 商用 IDC**：历史「مرکز داده استانی」多为政府 / National Information Network（NIN）节点，规模小；仅当来源确认机架、服务器、运营商或运营状态才计为设施，否则保留为政府基础设施线索。
4. **地理集中**：现代私营容量集中在 Tehran / Alborz / Qom / Isfahan / Fars / East Azerbaijan / Khorasan Razavi / Khuzestan / Hamadan，与德黑兰需求、IXP 位置和省级云改造点一致。
5. **云证据语义**：全球超大规模商（AWS/Azure/GCP/OCI）官方区域表**无伊朗公共区域**——中东区域 ≠ 伊朗设施，作负向对照；「云区域」是服务地理，需官方源指名数据中心/城市才计设施。国内「region/AZ」语言多为产品可用性，须回查底层设施。
6. **容量语义**：官方 ICT/运营商页的 rack/server/m²/MW > 招标/采购 > 行业媒体 > 聚合库；注意「可扩展设计容量」与当前容量的区分，波斯数字需正确换算。
7. **陷阱**：波斯历（Solar Hijri）日期换算后再比较生命周期事件；`ابر` 可指云软件/SaaS/CDN 而非物理设施；英文「Kurdistan」常命中伊拉克 KRG，需加 Iran/Sanandaj；加密挖矿与 GPU/HPC 公告可能伪装成数据中心。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§5 / explorer-industry.md §1-§4）

- 持牌/评级：`site:cra.ir "دارندگان پروانه" "{运营商波斯语名}"`、`site:ito.gov.ir "رتبه‌بندی" "مرکز داده"`、`site:khadamat.mardom.ir "گواهینامه رتبه‌بندی ارائه‌دهندگان خدمات مرکز داده"`、`site:mojavez.ir "مرکز داده"`。
- ICT/省域：`site:ict.gov.ir "مرکز داده استانی" "{استان}"`、`site:{省子域}.ict.gov.ir "مرکز داده"`、`site:ict.gov.ir "مرکز تبادل ترافیک" "{شهر}"`（子域不固定，先用搜索引擎发现确切子域）。
- 电力：`site:news.tavanir.org.ir "مرکز داده" "مصرف برق"`、`"مرکز داده" "پست برق" "{شهر}"`、`"دیتاسنتر" "مولد اضطراری" "{استان}"`。
- 环境/市政：`site:doe.ir "مرکز داده" "ارزیابی اثرات زیست محیطی"`、`site:{省}.doe.ir "مرکز داده"`、`site:tehran.ir "دیتاسنتر" "پروانه ساختمانی"`、`"پنجره واحد مدیریت زمین" "مرکز داده"`。
- 行业：`site:peivast.com "دیتاسنتر"`、`site:peivast.com "ابر ایران"`、`site:digiato.com "دیتاسنتر" "آروان"`、`site:zoomit.ir "دیتاسنتر" "رتبه‌بندی مراکز داده"`、`site:citna.ir "دیتاسنتر" "{运营商}"`。
- 目录/网络：`site:datacentermap.com/iran/ "{城市}" "{运营商}"`、`site:cloudscene.com/market/iran "{运营商}"`、`site:peeringdb.com "Tehran" "data center"`、`site:bgp.he.net "{运营商}" "Iran"`。
- 负向对照：`site:aws.amazon.com/about-aws/global-infrastructure Iran "Region"`、`site:cloud.google.com/about/locations "Iran"`、`"AWS" "Iran" "data center" -Bahrain -UAE -Saudi`。

## 官方/监管管线要点（详见 explorer-official.md）

- CRA/Ratel 持牌页（A 级=公司授权，C 级=设施存在）：种子 FCP/Servco/PAP/移动与固网运营商；ITO / khadamat.mardom 数据中心评级服务（A 级=证书/官方服务与具名受让方；计划接入国家许可门户）。
- 国家许可门户 mojavez.ir（A 级=具体执照/证书记录，否则仅作监管语境）。
- ICT 部 + 省级 ICT 管理局：官方设施开园/状态与 rack/server 数（A 级）；实例——MCI Tabriz 数据中心（西北最大）：3,000 m²、250 机架可扩至 350、1,500 物理服务器、16,000 虚拟服务器；IXP 在 Mashhad/Shiraz/Tabriz 上线。
- TIC/IXP（A 级=IXP 存在/位置；仅作数据中心邻近代理 B/C）；Tavanir/区域配电（A 级=电力事实：数据中心/AI/加密负载五年翻倍讨论、新变电站、专线、备用发电）。
- DOE/市政/土地（项目级 A 但稀疏）：`site:doe.ir`、省 DOE 子域、市政建设许可页按城市检索（Tehran 等），不期待完整项目列表。
- 云管线：全球超大规模商区域表作负向对照；国内运营商表——ArvanCloud（B，境内 4 座 DC）、Asiatech（B，Milad Tower）、Afranet（B）、Pars Online（B，现归 HiWEB）、Shatel（B，CRA 执照页脚）、MCI（A/B，Tabriz 官方种子）、TCI（B）、Mobinnet（B）、HostIran（B）、Amin IDC（B）、Tebyan/Respina/Sefroyek/Noor IDC（B/C）。
- Iran Cloud（ابر ایران）：ITO 与 Asiatech、Zharfnegar、Abr ZS、ArvanCloud、Fanap 签约（20 家申请者中选定），云化改造约 10 座现有数据中心；点名城市 Tabriz、Ahvaz、Karaj、Isfahan、Shiraz、Mashhad、Qom、Hamadan（Isfahan 出现两次）——作线索清单，逐城用 ICT/ITO 招标、开园或运营商证据核验（B 级，官方确认后升 A）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 波斯语媒体（B 级）：Peivast（最强数字经济技术媒体，`ابر دولت`/ITOI 政策/运营商发布）、CITNA（ICT 活动/图集/部委引语）、Digiato（ArvanCloud 产品/DC 发布）、Zoomit（评级政策/云产品）、ITMen（B-/C+）、官媒 Tasnim/Mehr/Fars/IRNA/ISNA（常复读 PR）、Way2Pay/Donya-e Eqtesad（B-/C+）、Aftana（B-/C+）；DCD（英文市场综述，B）。
- 协会：Iranian ICT Guild / IranNSR（27k+ 会员、30 省，政府与私营 ICT 的法定接口）——协会活动、DCAS/评级讨论、省级公司线索，不作设施证据（B/C）。
- 目录与网络情报（C 级线索，地址可 B）：DataCenterMap Iran（19 设施、6 市场：Tehran 14、Isfahan、Rasht、Shiraz、Hamedan、Qom）、Cloudscene（Pars Online/Afranet）、Data Center Platform、Datacenters.com/Inflect/Baxtel、PeeringDB/RIPEstat/bgp.tools/bgp.he.net（ASN/运营商在场可确认，不可单独用于物理设施清点）。
- 运营商扫描种子（A=官方存在/B=容量）：ArvanCloud（官方页称 40 PoP/30+ 国、境内 4 座数据中心；VPS Iran 页点名 Tabriz/Isfahan/Tehran；产品页 DC 名 Bamdad/Shahriar，Bamdad 报道位于 Payam 经济特区）、Afranet、Pars Online、Asiatech/cloud.ir（Milad Tower 开园 >900 m²）、Mobinnet、Irancell、MCI、TCI、Shatel/Pishgaman/HiWEB/Fanava/Respina/Datak/SabaNet、Amin IDC/Chakavak/HostIran/Pars Data/Mahan Server/SamaPardaz/Radcom/Abre Nik（非德黑兰线索与认证面包屑）。
- 常见失败模式：转售商广告「伊朗服务器/德黑兰数据中心」不拥有设施——仅记 C 级线索，回查实际网络/运营商名、ASN、地址、CRA 执照或官方设施页。

## 来源分级

- **A** = 官方/一手/可追责：CRA/Ratel 执照记录（公司授权）、ITO/政府服务页证书与具名受让方、ICT 部/省级 ICT 官方开园与机架数、TIC/IXP 官方公告、Tavanir/区域电力官方声明（具名项目）、项目级 DOE/市政/土地许可、运营商官方设施/服务页（存在；容量 A-/B 视具体度）、具名项目时的官方招标/采购、云区域官方文档（负向对照）。
- **B** = 强二级：Peivast/CITNA/Digiato/Zoomit/IRNA/Mehr/Tasnim/Donya-e Eqtesad、DCD、开园仪式报道、运营商自述云区域/评级新闻稿（A 仅当与 ITO/政府合同配对）、目录中与官方源匹配的字段级条目。
- **C** = 弱/未验证：DataCenterMap/Cloudscene/Datacenters.com/Inflect、转售商页、社交帖、SEO 托管页、市场研究摘要；聚合库默认 C，除非官方页/权威记录/披露核验。
- 状态语义（波斯语动词）：`فراخوان/مزایده`（招标）= 线索；`قرارداد`（签约）= 已承诺；`ایجاد/توسعه`（建设/扩展）= 在建信号；`افتتاح/راه‌اندازی/بهره‌برداری`（开园/上线/投产）= 运营；运营商在售服务页（当前销售/联系）= 运营或近运营。仅最后两级计为运营容量。
- 容量规则：rack/server/m²/MW 官方口径优先；可扩展设计容量须在 notes 标注；政府 NIN/e-government 节点与商用 IDC 分开存储，不得同表比较；大型 AI/云规模声明若无变电站/并网/发电/冷却故事支撑，置信度保持 B/C。
- **政策/计划 ≠ 项目容量**：Iran Cloud 城市清单、省级数据中心计划须有具名设施+运营商+状态才能计；不把中东（UAE/Bahrain/Qatar/KSA）超大规模区域当伊朗设施。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=IR，divisions=31 省 + 城市）。
2. 建种子：CRA/Ratel 持牌商 + 已知 FCP/移动运营商 + ITO 评级受让方 + Iran Cloud 中标方；官方设施种子：ICT/ITO/TIC 省级数据中心、MCI/TCI 数据中心、IXP 邻近设施、Iran Cloud 城市记录。
3. 逐省执行省域模板（ICT 省级子域、波斯语城市词、Tavanir、省 DOE），优先 Tehran、Alborz、Qom、Isfahan、Khorasan Razavi、East Azerbaijan、Fars、Khuzestan、Hamadan，再 Markazi/Gilan/Mazandaran 等。
4. 电力/许可扫描：Tavanir、区域配电公司、DOE、市政、土地管理术语；运营商确认：官方站点 colo/cloud 页、机架数、设施照片、证书、客户接入语言、执照页脚。
5. 二级补漏：Peivast/Digiato/Zoomit/IRNA/DCD + 聚合目录；无一级佐证则降级。
6. 去重：按 (母公司, 设施/园区名, 城市/省, 来源日期) 键；注意品牌与法定名混用、波斯历日期换算；不把中东超大规模区域当伊朗设施。
7. 输出 world 同 schema：`{country_code=IR, country_name=Iran, division=省, city, name, operator, status, capacity_mw, racks, area_m2, source_urls, evidence_date, evidence_grade, notes}`；无项目 division 写 `no_projects: true`。
8. 遵行 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:35Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：探索/复核批次按省优先 → 城市分桶；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：ITO 评级接入国家许可门户后的具名设施清单；Iran Cloud 各城市（Tabriz/Ahvaz/Karaj/Isfahan/Shiraz/Mashhad/Qom/Hamadan）逐项官方开园/招标证据；ArvanCloud Bamdad/Shahriar 与 Payam SEZ 的官方记录；MCI Tabriz 数据中心当前运营状态。
