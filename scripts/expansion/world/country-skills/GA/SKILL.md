---
name: ga-datacenter-methodology
location: scripts/expansion/world/country-skills/GA/SKILL.md
description: 加蓬（Gabon）数据中心发现与审计方法论：官方/监管/云管线（数字经济部、ANINF 国家数字基础设施局、ARCEP 电信监管局、APDPVP 数据保护局、SPIN/ACE/Medusa 海缆、SEEG 能源、Uptime Institute、官方云区域排除）叠加行业/厂商发现（运营商、IXP/对等、捐赠方项目、贸易媒体、目录）；以清单中的 9 个省（Estuary、Upper Ogooue、Middle Ogooue、Ngounie、Nyanga、Ogooue-Ivindo、Ogooue-Lolo、Maritime Ogooue、Woleu-Ntem）为划分粒度，先法语搜索并积极消歧。运行 GA 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。Bilingual discovery & audit methodology for Gabon datacenters: official/regulatory/cloud pipeline + industry/trade-press discovery, at the 9 province division granularity from the manifest; search French first and disambiguate aggressively; read before running GA exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# GA · 加蓬数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：加蓬没有公开的国家数据中心登记册，公共托管市场极小。本趟核实 **2 座已确认物理设施**（ST Digital Nkok；Moov Africa Gabon Telecom DC1 Cenacom 大楼）、**1 个在建主要设施**（Cybastion/加蓬主权 DC，报道 20 MW）、**1 个未决 ANINF/国家设施线索** 与少量目录级线索；现实全国库存预期 **至多 4–7 条物理记录**，9 个省中 8 个预期无公共托管。不得用政策声明、登陆站、IXP PoP 或实验室凑数。运行任何 GA 探索/审计批次前必须阅读本 skill，并按需路由到两份探索报告。

## 入口（Entry points）

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | 数字经济部、ANINF（国家数据中心计划、GAB-IX）、ARCEP、APDPVP、SPIN/海缆官方（ACE/Medusa）、能源/电网/许可（SEEG、水电/气电）、捐赠方与采购（AfDB/世行/Cybastion）、云区域负向控制、Uptime Institute、已验证设施/线索种子表、9 省覆盖策略、证据捕获规则与拒绝模式 |
| explorer-industry.md | 行业/厂商发现 | 运营商/设施种子（ST Digital lbv01、Cybastion 20 MW、Moov DC1 Cenacom、ANINF 线索、Airtel Gabon、GABIX、SPIN/ACE、Medusa）、云/CDN/接入检查、按类型行业来源、查询库、逐省行业模式、验证与去重规则 |

## 核心结构事实（框定每次搜索）

1. **划分模型**：清单为 **9 个省**：Estuary；Upper Ogooue；Middle Ogooue；Ngounie；Nyanga；Ogooue-Ivindo；Ogooue-Lolo；Maritime Ogooue；Woleu-Ntem（法语：Estuaire；Haut-Ogooue；Moyen-Ogooue；Ngounie；Nyanga；Ogooue-Ivindo；Ogooue-Lolo；Ogooue-Maritime；Woleu-Ntem）。活跃市场集中在 **Estuary 省**（Libreville + Nkok 经济特区，距 Libreville 约 30 km）。
2. **核心设施/项目集**：**ST Digital Nkok DC (lbv01)**（Estuary/Nkok SEZ；运营商官方页：100% 运营、1 MW、Tier 3 certified 主张、太阳能/绿色设计、无水制冷、托管/IaaS/SaaS；报道 2026-07-03 开业、2025-08 动工；We Are Tech 报道 8 bn FCFA、>3,000 sqm、92 机架、1 MW——保持 B 级直至 ST Digital 发布同细节；**Tier III 为运营商/媒体主张，Uptime 列表点名 lbv01 前认证未验证**）；**Cybastion / 加蓬政府 / ANINF 主权 DC 项目（报道 20 MW）**（Estuary/Libreville–Nkok 走廊，确切站点未决；公司 PR 2025-06-28 协议（Cisco/Citibank/EXIM）；DCD/Le360 提供 20 MW、站点、承包商、燃气电厂细节；**与 ST Digital lbv01 保持分离**直至官方声明同一建筑）；**Moov Africa Gabon Telecom DC1, Cenacom 大楼, Libreville**（Uptime Institute 记录——GA 唯一 Uptime 记录；tier 等级/日期须在列表确认；运营商中立与否待查）；**ANINF/国家数据中心线索（Libreville）**（ANINF 项目/文章页为 A 级计划证据，物理站点身份未决；不与 Cybastion 或 ST Digital 重复计数）；**Airtel Gabon Libreville**（目录 C 级线索）；**GABIX/GAB-IX**（IXP，非 DC——PoP ACE 在 ACE 登陆站、PoP CT-1 在 Cenacom 大楼附近；不得因目录把 POP CT-1 标为 3 MW DC 就计数）。
3. **关键机构**：数字经济部（economie-numerique.gouv.ga，2025–2026 主权 DC 推进）、ANINF（aninf.ga，国家数字基础设施技术臂，GABIX 10 Gbps 成员，2025-06-28 Cybastion 协议国家共同签约方）、ARCEP（arcep.ga，监管 Moov Africa Gabon Telecom/Airtel Gabon；**无数据中心登记册或专门数据中心执照类别**）、APDPVP（apdpvp.ga，数据保护/本地托管合规信号，非登记册）、SPIN（spin.ga，数字基础设施资产公司；子公司 ACE Gabon 运营 Libreville ACE 登陆站，是 Medusa Africa 在 Port-Gentil 的登陆方）、SEEG（能源，1997 起特许经营，2026 拆分重组）、AfDB/World Bank（ANINF 2018 赠款含 CAB 光纤可行性 + 国家数据中心；Cybastion 项目）、Uptime Institute。
4. **查询语言与术语**：**先法语**：`centre de donnees`、`datacenter`、`data center`、`centre de stockage de donnees`、`hebergement`、`colocation`、`salle serveurs`、`cloud souverain`、`souverainete numerique`、`Tier III`、`GABIX`、`point d'echange Internet`、`cable sous-marin`、`atterrissement`、ACE、Medusa、SAT-3、LION2、BNG、fibre optique、dorsale、poste electrique、MVA、MW、SEEG、centrale a gaz、ZES de Nkok、appel d'offres、permis de construire。**积极消歧**：拒收/重查 Brazzaville/Pointe-Noire（刚果布）、Kinshasa/Lubumbashi（刚果金）、Douala/Yaounde（喀麦隆）、Bata/Malabo（赤道几内亚）与任何实为 GABON TELECOM 品牌史或其他行业的 "Gabon" 提及。
5. **容量语义**：Nkok 的 1 MW 来自运营商官方页（A），20 MW 为 Cybastion 报道值（B）；ST Digital "Tier 3 Certified" 与媒体 "certifie Tier III" 在 Uptime 列表点名 lbv01 前为主张；状态层级：官方/运营商运营页或开幕 > 调试报道 > 在建官方/捐赠页 > 合同授予 > 公约/MoU > 招标 > 政策/战略；容量层级：官方数据表 > 运营商声明 > 引述运营商的行业媒体 > 目录。
6. **海缆/IXP/大学实验室不是数据中心**：ACE Libreville 与 Medusa Port-Gentil（2026-27）登陆站为连接性；GABIX PoP 为 IXP 托管；USTM Franceville 数据中心实验室为教育捐赠（解释 Haut-Ogooue 为何无公共托管）；石油/矿业/银行服务器机房（TotalEnergies、Perenco、VAALCO、Eramet/Comilog、BGFI、Ecobank）为私营，除非公开提供托管/DC 服务。
7. **云区域负向控制（A 级）**：AWS/Azure/GCP/OCI 均无 GA 区域；最近公共区域在南非（AWS Cape Town；Azure South Africa North/West；GCP africa-south1 Johannesburg；OCI af-johannesburg-1）；全球云引用为经销商/CDN/入口/租户线索。
8. **可靠度分级**：A = 政府/部委/ANINF/ARCEP/APDPVP/SPIN 页、官方运营商设施页、官方云区域页、Uptime Institute 记录、高管签署的公司新闻稿；B = 强二级（Agence Ecofin、DCD、Digital Business Africa、We Are Tech Africa、Gabon Review、L'Union、Gabon Actu、Gabon Media Time、AGP、Convergence Afrique、Le360、Euro-IX ixpdb、引述具名官员/运营商的本地媒体）；C = 仅线索（DataCenterMap、colo.exchange、DataCenters.com、Inflect、Baxtel、Tracxn、聚合新闻、社交、无引述厂商主张、模糊托管/云主张、纯政策声明）。
9. **去重陷阱**：三个 Nkok/Libreville 叙事（ST Digital lbv01 运营；ANINF/Cybastion 20 MW 在建；ANINF 遗留 Libreville DC）不得无地址/运营方/所有权声明即合并；"Data center national" 标题常混淆三者——合并前先解决归属。

## 常用查询模板（详见 explorer-official.md / explorer-industry.md）

```text
site:economie-numerique.gouv.ga "data center" OR "centre de donnees" OR datacenter OR Nkok OR Cybastion
site:aninf.ga "data center" OR "centre de donnees" OR GABIX OR BNG OR Cybastion
site:arcep.ga "centre de donnees" OR "data center" OR GABIX OR licence operateur
site:apdpvp.ga "data center" OR hebergement OR cloud
site:spin.ga "data center" OR ACE OR Medusa
site:seeg-gabon.com "data center" OR "centre de donnees"
site:uptimeinstitute.com Gabon Libreville OR Cenacom OR "ST Digital"
(Gabon OR Libreville OR "Port-Gentil") (datacenter OR "data center" OR "centre de donnees" OR colocation) -Congo -Brazzaville -Kinshasa -Douala
(Gabon OR Libreville) ("Tier III" OR "Tier 3" OR "Uptime Institute")
"data center national" Gabon Nkok OR ANINF OR Cybastion OR "ST Digital"
"ST Digital" Nkok datacenter OR colocation OR "Tier III" OR lbv01
"Cybastion" Gabon datacenter OR "20 MW" OR ANINF
"{province}" OR "{city}" (datacenter OR "centre de donnees" OR colocation OR "salle serveurs") Gabon -Congo
"Nkok" "centrale a gaz" MW datacenter
site:afdb.org Gabon datacenter OR "centre de donnees"
"Gabon" "cloud region"   # 云排除
```

## 官方/监管管线要点（详见 explorer-official.md）

- 数字经济部/ANINF：国家数据中心计划、主权 DC 推进、GABIX 事实、骨干（BNG）事实；ANINF 老 "Data Center National" 页为计划证据除非给出当前物理站点地址/运营方；引用前显式解析 ANINF 页所指设施（Libreville 遗留 vs Nkok 新建）。
- ARCEP：运营商存在/牌照/电信市场事实；电子通信执照是否覆盖托管/托管需先查执照框架。
- APDPVP：本地托管与个人数据合规信号；可经检查活动（如 Lambarene）浮现省级机房/托管合规线索。
- 能源/许可：SEEG/能源部；无全国可检索建筑许可登记册，许可在 commune/urbanism 层面、EIES 可能经捐赠方/顾问浮现；具名许可/EIES 依签发者定 A/B。
- 捐赠方：AfDB（ANINF 2018 赠款 US$800,000，含国家数据中心）、World Bank 项目列表、Cybastion PR（2025-06-28）；采购公告为 B 级计划设施证据直至中标/站点/施工出现。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商页胜过目录：ST Digital/Moov/ANINF 确认设施时仅将已确认事实定 A；目录专属容量/地址保持 C 直至匹配。
- GABIX PoP 定位机房：PoP ACE 在 ACE 登陆站、PoP CT-1 在 Cenacom 大楼附近；GVA、iPi9、PCH、GBM、TLDC、ST Digital-AS 等成员逐一枢轴到 PoP/缓存/托管搜索。
- 状态日期显式：Cybastion 战略协议报道 2025-01-28；国家/ANINF/Cybastion 协议 2025-06-28；ST Digital Nkok 动工报道 2025-08、开业 2026-07-03；GABIX 重启报道 2026-05；Medusa C&MA 2025-03-19 签署、Port-Gentil 登陆为连接性邻接。
- 目录（DataCenterMap/colo.exchange/DataCenters.com/Inflect/Baxtel/DataCenterPlatform/DataCenterJournal/Tracxn）仅用于别名/地址直至并入；保护型目录/新闻页（ISOC Pulse/Uptime）对 curl 可能 403/429/522，作 B/C 支持而非唯一设施证明。

## 维护注意（更新纪律）

- **更新节奏**：每次刷新重查官方/运营商页（ST Digital、Moov、ANINF、SPIN、Cybastion、Medusa）、Uptime 列表（确认 Cenacom tier/日期与 lbv01 是否出现）、云区域页、AfDB/世行项目页、GABIX/Euro-IX；跟踪 Cybastion 站点解决、ST Digital 客户/容量确认、Medusa Port-Gentil 建设。
- **来源核验**：旧部委短路径 /aninf 已 404；ST Digital 集团页可能混合多国市场内容（科特迪瓦/喀麦隆/多哥/刚果主张须对照加蓬 Nkok 设施核验）；约 8 bn FCFA 数字不同来源绑定的对象不同——按来源 URL 与日期记录成本数字。
- **不删除纪律**：无法核实的旧线索保留为降级线索并注明缺失证据（如 Shapoorji Pallonji MoU 历史线索，可能已被 Cybastion 协议或 ST Digital 建设取代）；每条候选记录捕获 facility_name、operator_or_owner、province_manifest_9、city_quartier_address、status、source_grade_by_fact、source_urls、physical_evidence、capacity、power_cooling、connectivity、tenant_or_service_scope、dedupe_notes、country_disambiguation。
