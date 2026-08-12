---
name: ma-datacenter-methodology
location: scripts/expansion/world/country-skills/MA/SKILL.md
description: |
  Morocco (MA) datacenter discovery & audit methodology — how to enumerate, verify, and update Morocco datacenter projects at region granularity (12 regions under the 2015 reform, ISO 3166-2:MA, 75 prefectures/provinces, 1503 communes). No public national datacenter register and no open national planning-permit search: enumeration joins ANRT telecom context, Ministry of Digital Transition/ADD policy, CRI-Invest/CRUI investment-permit routes, ONEE/ANRE/MASEN energy & self-production, CNDP data protection, Portail National des Marches Publics procurement, Uptime Institute certification pages, operator pages, and Oracle OCI official pages. Oracle OCI Morocco West / Casablanca (af-casablanca-1, LEJ, live 2026-02-20, hosted at N+ONE) is the only verified hyperscaler cloud region; AWS/Azure/GCP have no Morocco public region. Read this before running MA exploration/audit batches. Routes to explorer-official.md (regulators/investment/energy/procurement/hyperscaler/per-region strategy) and explorer-industry.md (market frame/high-signal sources/facility leads/pipeline/status language).
---

# MA · 摩洛哥数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：摩洛哥**无**全国数据中心注册库、**无**开放的国家建设许可搜索引擎；枚举联合 ANRT（电信）、数字转型部/ADD（政策）、CRI-Invest/CRUI（投资与许可）、ONEE/ANRE/MASEN（能源与自产）、CNDP（数据保护）、国家公共采购门户、Uptime 认证页、运营商页与 Oracle OCI 官方页。
> 分区模型：**12 大区（regions，2015 改革/ISO 3166-2:MA）**；最强集群 Casablanca-Settat 与 Rabat-Sale-Kenitra；每区先跑 CRI/CRUI 路线。
> 超规模云：**Oracle OCI Morocco West / Casablanca（af-casablanca-1 / LEJ，2026-02-20 上线，N+ONE 托管）为唯一已核实公共云区域（A）**；AWS（仅 Wavelength 计划）/Azure/GCP 无摩洛哥公共区域。
> 容量纪律：仅当来源将数字绑定具名数据中心站点才记录 MW/MVA/机架/面积；可再生能源 MW/海缆带宽/国家电网项目是背景。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供摩洛哥探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：ANRT、数字转型部/ADD/Maroc Digital 2030、CRI-Invest/CRUI 与自由区（Tanger Med Zones/Atlantic Free Zone/Midparc/Technopark）、AMDIE、ONEE/ANRE/MASEN 能源与 Law 82-21 自产、CNDP、公共采购、Oracle/OCI 官方页与 AWS Wavelength、Uptime/运营商页、12 大区官方枚举策略 |
| `explorer-industry.md` | 行业/厂商发现：市场框架（Oracle/N+ONE、Uptime MA 国家页、inwi/MDC/Atlas/HostoWeb/IAM）、高信号来源表、运营/认证设施（N+ONE Settat/Nouaceur、Orange Tech Nouaceur、inwi Rabat Technopolis DC2、MDC Temara、Atlas Benguerir、OCP DC2、Maroc Telecom 市中心）、规划管线（Naver 500 MW、Iozera 386 MW、Dakhla 500 MW、Rabat 50 MW、Oracle Settat）、状态语言与验证规则 |

## 核心结构事实（框定每次搜索）

1. **官方表面八项**：ANRT（不单列数据中心牌照）、数字转型部/ADD、CRI-Invest/CRUI（在线投资与许可路径）、AMDIE（投资激励）、ONEE/ANRE/MASEN（电网/自产 Law 82-21）、CNDP（数据保护，通常 C 设施证据）、公共采购（marchespublics.gov.ma，招标≠投运）、Uptime/运营商/Oracle 官方页。
2. **Oracle Casablanca 是唯一超规模区域（A）**：`af-casablanca-1`、区域键 LEJ、单一可用区、2026-02-20 发布、托管伙伴 N+ONE（Oracle 2026-04-07 公告）；Oracle Settat 第二区域仍为计划（2024 公告，A 计划，非 live）；AWS Wavelength+Orange 为边缘/网络设施非 AWS Region。
3. **Uptime MA 国家页是最佳认证骨架（A）**：列 N+ONE Settat/Nouaceur、Orange Maroc Nouaceur、Wana/inwi Rabat-Sale、OCP/Atlas Benguerir 等；尽量用项目专属页；Tier 主张须 Uptime/运营商证书页。
4. **已证实运营/认证设施**：N+ONE（Settat/Nouaceur，A）、Orange Tech Nouaceur/Casablanca（2025-11-19 启用、初始 1.5 MW、15000 m2、700 kWc 光伏，A 官方 PDF）、inwi Rabat Technopolis DC2（A Uptime/inwi，B 1000 m2/启用报道）、MDC Temara（A 官方页，2000 m2、Tier III-designed 自述）、Atlas Cloud Services Benguerir（A 自述 + Uptime）、OCP Benguerir DC2（A Uptime 项目）、Maroc Telecom 市中心 Casablanca DC（B，2018 TelQuel/Minkels，IAM 页找到才升 A）。
5. **规划管线一律 planned**：Naver/Nexus/Lloyds 500 MW AI 园区（A 公司公告/B）、Iozera/Eureka Park Tetouan 386 MW（A-公司/B）、Dakhla 500 MW 可再生能源 DC（B，含西撒哈拉敏感性）、Rabat 主权 DC 50 MW + Vertiv（B）、Oracle Settat 第二区域（A 计划）。
6. **语言**：法语 `centre de données`/`cloud souverain`/`permis de construire`/`raccordement électrique`/`station d'atterrissement`；阿语 `مركز البيانات`/`الاستضافة`/`السحابة السيادية`/`رخصة البناء`；状态词保守解读（`MoU/annonce/plan`=planned；`appel d'offres/attribution/CRUI approval`=采购/许可；`construction started/chantier`=在建；`inauguré/mis en service/operational`=运营）。
7. **资产类型分开**：`cloud region` ≠ `data center` ≠ `cable landing station` ≠ `R&D hub` ≠ `tech park`；Nador Medusa 登陆站、Agadir Oracle R&D、Noor Ouarzazate 能源、Haliopark 均为背景/连接。
8. **去重**：按 运营商+设施/地点+大区；N+ONE Settat 与 Nouaceur 是两个 Uptime 项目；每批次重查超规模官方区域列表。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§2 / explorer-industry.md §0-§3）

- 官方：`site:anrt.ma "data center" OR "centre de donnees"`、`site:mmsp.gov.ma "data center" OR "cloud souverain"`、`site:cri-invest.ma "data center"`、`site:{regional_cri_domain} "centre de donnees"`、`site:amdie.gov.ma "data center"`、`site:marchespublics.gov.ma "data center" OR "centre de donnees"`。
- 能源：`site:one.org.ma "data center" OR "poste" "Nouaceur"`、`site:anre.ma "autoproduction"`、`"autoconsommation" "data center" "Maroc"`、`site:masen.ma "data center"`。
- 超规模/认证：`"af-casablanca-1" "LEJ"`、`site:uptimeinstitute.com/uptime-institute-awards/country/id/MA Morocco`、`site:uptimeinstitute.com "N+ONE DATACENTER" Morocco`、`"INWI Rabat Technopolis DC2"`、`"Benguerir Data Center DC2"`。
- 运营商：`site:inwi.ma "datacenter"`、`site:mdc.ma "Temara" "datacenter"`、`site:corporate.orange.ma "Orange Tech" "Data Center"`、`site:atlascloudservices.com "Benguerir"`、`site:iam.ma "data center" OR "hebergement"`。
- 行业/媒体：`site:datacenterdynamics.com/en/news/ Morocco "data center"`、`site:agenceecofin.com Maroc "data center"`、`site:medias24.com "data center" Maroc`、`site:le360.ma "datacenter" Maroc`、`site:telquel.ma "Maroc Telecom" "data center"`。
- 阿语复核：`"المغرب" "مركز البيانات"`、`"الدار البيضاء" "مركز البيانات"`、`"الرباط" "مركز البيانات"`、`"الداخلة" "مركز البيانات" "500"`。
- 管线：`"NAVER Cloud" "Morocco" "500MW"`、`"Iozera" "Eureka Park" "Tetouan"`、`"Dakhla" "500MW" "renewable" "data center"`、`"Vertiv" "Morocco" "50 MW" "sovereign data center"`、`"Oracle" "Settat" "cloud region"`。

## 官方/监管管线要点（详见 explorer-official.md）

- ANRT：电信运营商状态/许可/5G/光纤决策，A 电信上下文，非设施证据。
- 数字转型部/ADD：政策与公共云需求；Maroc Digital 2030；仅当页面点名设施/地点/承包方才算证据。
- CRI/CRUI：投资级 DC 走 CRI 新闻/年报/董事会纪要/PDF 通讯；普通许可走市镇/省/城市局/CRUI；自由区项目查区运营方（Tanger Med Zones、Atlantic Free Zone、Midparc、CasaNearshore、Technopark、Haliopolis）。
- AMDIE：战略投资公告；公告容量/状态仅当 AMDIE 自己声明才 A。
- 能源：ONEE（电网/项目/采购）、ANRE（Law 48-15/82-21 自产）、MASEN（可再生）；可再生 MW 不得转成 DC IT load。
- 采购：招标证明采购，不证明设施投运；按买家名与通用词搜。
- 超规模：Oracle Casablanca A；AWS/Azure/GCP 区域缺失为 A 负面；Wavelength 为边缘计划。
- 验证规则：每条记录须有运营商/业主、设施名、commune/地点、大区、状态、证据 URL；计划/MoU 项目保持 planned；TLS/地域封锁失败时保留 URL 并加复核注记。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 高信号源：OCI release notes（A）、Oracle 摩洛哥公告（A）、Uptime MA 国家页与 N+ONE 客户故事（A）、inwi 商业 DC 页（A）、Orange 官方 PDF（A）、MDC（A）、Atlas（A）、HostoWeb（A 服务/C 设施）、IAM（A 若找到）、mcnet 工业部 Maroc Datacenter 页（A）、DCD/Agence Ecofin/Medias24/Le360/TelQuel/Le Matin/LesEco（B）。
- 已证实设施种子（见核心事实 4）；目录（C）：DataCenterMap、Datacenters.com、Baxtel、Cloudscene、datacentercatalog、datacenterplatform、Telecontact。
- 管线种子：Naver/Nexus/Lloyds 500 MW、Iozera 386 MW、Dakhla 500 MW、Rabat 50 MW Vertiv、Oracle Settat——全部 A-公司公告/B 媒体，未到许可/施工/投运前不升级。
- 状态词（法语/英语）保守解读（见核心事实 6）；每设施线索需要业主/地点/大区/状态/证据 URL。

## 已知设施/项目与证据状态

| 设施/项目 | 大区 | 状态与证据 |
|---|---|---|
| Oracle OCI Morocco West / Casablanca（af-casablanca-1/LEJ） | Casablanca-Settat | 上线（A OCI 文档/公告）；N+ONE 托管伙伴（A） |
| N+ONE Datacenter II Phase 1（Settat）/ I Phase 2（Nouaceur） | Casablanca-Settat | 认证设施（A Uptime） |
| Orange Maroc Casablanca DC #1 / Orange Tech | Casablanca-Settat（Nouaceur/Casablanca） | 2025-11-19 启用（A Orange PDF + Uptime）；初始 1.5 MW/15000 m2 |
| inwi / Wana INWI Rabat Technopolis DC2 | Rabat-Sale-Kenitra | 运营/认证（A Uptime/inwi；B 报道） |
| MDC / Maroc Datacenter | Rabat-Sale-Kenitra（Temara） | 运营/自述（A 官方页，2000 m2、Tier III-designed） |
| Atlas Cloud Services / OCP Benguerir DC2 | Marrakech-Safi（Benguerir） | 运营/认证（A 自述+Uptime）；5 MW/2000 m2 需独立源（B） |
| Maroc Telecom 市中心 Casablanca DC | Casablanca-Settat | 2018 启用（B TelQuel/Minkels）；IAM 页前不升 A |
| Naver/Nexus/Lloyds 500 MW AI 园区 | Casablanca 附近/自由区（待验） | 计划/公告（A 公司/B 媒体）；无许可/施工证据 |
| Iozera / Eureka Park 386 MW | Tanger-Tetouan-Al Hoceima（Tetouan） | 计划/MoU（A-公司/B）；CRI/许可前不标在建 |
| Dakhla 500 MW 可再生 DC | Dakhla-Oued Ed-Dahab | 计划（B 媒体）；含西撒哈拉敏感性；部委/CRI 页前不升级 |
| Rabat 主权 DC 50 MW（Vertiv） | Rabat-Sale-Kenitra | 计划/讨论（B）；部委/采购页前不升级 |
| Oracle 第二区域 Settat | Casablanca-Settat | 计划（A 2024 公告）；OCI 文档/开区公告前非 live |

## 更新节奏

- 每批次：超规模官方区域列表重查（Oracle/OCI 文档、AWS/Azure/GCP）、Uptime MA 页、Oracle Settat 第二区域、N+ONE/Orange/inwi 状态、管线项目（Naver/Iozera/Dakhla/Rabat 50 MW）许可与施工。
- 季度：12 大区 CRI/CRUI 扫回顾、新海缆/登陆站相邻设施（Medusa/Nador）、自由区新租户、MDC/HostoWeb 设施页更新。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（12 大区粒度）；本 skill 作为国家层参考注入。
