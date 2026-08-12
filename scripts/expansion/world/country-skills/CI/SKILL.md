---
name: ci-datacenter-methodology
location: scripts/expansion/world/country-skills/CI/SKILL.md
description: |
  Cote d'Ivoire (CI) data-center enumeration methodology. Division model: 14 districts (Abidjan; Yamoussoukro; Bas-Sassandra; Comoe; Denguele; Goh-Djiboua; Lacs; Lagunes; Montagnes; Sassandra-Marahoue; Savanes; Vallee du Bandama; Woroba; Zanzan). No verified national public register of data centers; enumeration joins operator pages, ARTCI telecom/data-protection records, Ministry of Digital Transition releases, SIGUPC/building-permit evidence, VITIB free-zone records, ANARE-CI/CI-ENERGIES/CIE energy evidence, ANDE/EIES, CEPICI/IDU company records, public procurement, PeeringDB/Uptime and trade press. Market is Greater-Abidjan-first but district attribution must be exact: Grand-Bassam/VITIB is in Comoe district (Sud-Comoe) even when marketed as Abidjan-area. No AWS/Azure/GCP/OCI public cloud region listed. Key seeds: Data Center National (Abidjan/Anoumambo/AIGF, construction, 36bn FCFA, $66m EXIM, first stone 2023-12-14), Raxio CIV1 (Comoe/VITIB, operational 2024, 3MW IT, Tier III, 2,000 m2 white space, 400 racks current/800 full), Equinix/MainOne AB1 & AB1.2 (Comoe/VITIB), ST Digital CIV01 (Comoe/VITIB, inaugurated 2025-10-02, ~160 racks), PAIX Abidjan ABJ1 (Abidjan/Cocody), Orange CI Grand-Bassam lead, MTN CI eCentre/Yopougon lead. Read this before running CI exploration/audit batches. Routes to explorer-official.md (ministry/ARTCI/SIGUPC/energy/registry playbook) and explorer-industry.md (operator deep dives/trade press playbook).
---

# CI · 科特迪瓦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：科特迪瓦无经核实的全国数据中心公共登记册，枚举靠拼接「运营商页 + ARTCI 电信/数据保护记录 + 数字转型部发布 + SIGUPC 建筑许可 + VITIB 免税区记录 + ANARE-CI/CI-ENERGIES/CIE 能源 + ANDE/EIES + CEPICI/IDU 公司记录 + 公共采购 + PeeringDB/Uptime + 贸易媒体」。市场以大阿比让为先，但区级归属必须精确：Grand-Bassam 与 VITIB 属 **Comoé 区（Sud-Comoé）**，即使运营商按 Abidjan 周边营销。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：数字部/国家 DC、ARTCI 与数据保护、SIGUPC/区门户、能源/电网、环境/EIES、CEPICI/IDU/采购、ANSSI、认证/互联/超大规模负面、设施种子正确区级归属、14 区策略 |
| `explorer-industry.md` | 行业/厂商管线：运营商深潜（Raxio、Equinix/MainOne、ST Digital、PAIX、国家 DC、Orange、MTN）、连接/互联、超大规模跟踪、贸易媒体/聚合器、14 区行业扫描、验证管线与陷阱 |

## 核心结构事实（框定每次搜索）

1. 行政划分：**14 个区（district）**：Abidjan、Yamoussoukro、Bas-Sassandra、Comoé、Denguélé、Gôh-Djiboua、Lacs、Lagunes、Montagnes、Sassandra-Marahoué、Savanes、Vallée du Bandama、Woroba、Zanzan。
2. **无核实国家登记册**；枚举多轨拼接。搜索法语优先：`centre de données / data center / datacenter / centre d'hébergement / hébergement / colocation / baies / salle informatique / cloud souverain / Tier III / Tiers 3 / mise en service / inauguration / raccordement / poste / MVA / MW`。
3. **区级归属陷阱**：Grand-Bassam 与 VITIB 在 **Comoé 区**；Raxio 官方页把 CIV1 放在 VITIB 内 Grand-Bassam（距阿比让 30 km），PeeringDB 把 Equinix AB1 放 VITIB Zone Franche, Grand Bassam——记 Comoé 记录并加 Abidjan-metro 注记；不得把 VITIB 设施直接归 Abidjan。
4. **无超大规模云区域**（A 级负面）：AWS/Azure/GCP/Oracle OCI 官方区域页未列科特迪瓦公共区域；CDN/边缘/经销商声明与云区域记录分开跟踪，负面结果带日期与所查官方 URL 记录。
5. 电信交换机房、海缆登陆站、银行 IT 机房仅作 DC 线索；仅当官方服务页或面向客户材料证明商业 colo/云角色时才归类为商业 colocation/cloud。
6. 状态归一：announced/MoU < financed < permitted < first stone < under construction < inaugurated/launched < operational。融资与奠基 ≠ 运营；EXIM 担保 ≠ 投运。
7. 去重营销名：同一 VITIB 物理站点可能以 Abidjan、Grand-Bassam、MainOne、MDXi 或 Equinix 出现——用坐标/地址/运营商页判断是独立建筑还是别名。

## 查询模式（复制粘贴模板见 explorer-official.md 与 explorer-industry.md）

- 部委/国家 DC：`site:telecom.gouv.ci "Data Center National"`、`site:telecom.gouv.ci "centre de données" "Anoumambo" OR "AIGF"`、`site:gouv.ci "Data Center National" "Cybastion" OR "PORTEO"`、`site:exim.gov "Côte d'Ivoire" "data center"`、`"Data Center National" "36 milliards" "Côte d'Ivoire"`。
- ARTCI/数据保护：`site:artci.ci "centre de données" OR "data center"`、`site:artci.ci "licence" "{operator}"`、`site:autoritedeprotection.ci "{operator}" "hébergement"`、`"ARTCI" "Raxio" "data center"`。
- 规划/许可/区门户：`site:guichet.construction.gouv.ci/GUPC "data center" OR "centre de données"`、`site:abidjan.district.ci "data center"`、`site:districtyakro.ci "numérique" OR "centre de données"`、`site:vitib.ci "data center" OR "Raxio" OR "MainOne"`、`"VITIB" "Grand-Bassam" "data center" "permis"`。
- 能源/电网：`site:anare.ci "data center" OR "raccordement"`、`site:cinergies.ci "data center" OR "poste" OR "MW"`、`site:cie.ci "data center" OR "grand compte"`、`"{facility}" "15kV" OR "MVA" OR "MW" "Côte d'Ivoire"`。
- 环境/EIES：`"ANDE" "EIES" "data center" "Côte d'Ivoire"`、`"étude d'impact environnemental" "Raxio" OR "VITIB"`、`"{operator}" "EIES" OR "ESIA" "Grand-Bassam"`。
- 登记/采购：`site:annuaireidu.ci "{operator}" "datacenter" OR "collocation"`、`site:cepici.ci "data center" OR "TIC"`、`site:marchespublics.ci OR site:sigomap.gouv.ci "data center" OR "hébergement" OR "cloud"`、`"{operator}" "RCCM" OR "IDU" "Côte d'Ivoire"`。
- 认证/互联/负面：`"Raxio CIV1" "Uptime Institute" "Tier III"`、`site:peeringdb.com "Côte d'Ivoire" "facility"`、`site:uptimeinstitute.com "Côte d'Ivoire" OR "Ivory Coast" "Tier"`、`site:aws.amazon.com "Côte d'Ivoire" OR "Ivory Coast" "region"`、`site:oracle.com "Côte d'Ivoire" OR "Ivory Coast" "cloud region"`。
- 行业/互联：`site:raxiogroup.com "CIV1"`、`"Raxio" "VITIB" "Grand-Bassam" "ESIA"`、`site:equinix.com "AB1" "Côte d'Ivoire"`、`site:mainone.net "Côte d'Ivoire" "data centre"`、`site:st.digital "Grand-Bassam" "data center"`、`site:paix.io "Abidjan" OR "ABJ1"`、`site:annuaireidu.ci "PAIX DATA CENTRES"`、`"MainOne" "Grand Bassam" "cable landing station"`、`"2Africa" "Côte d'Ivoire" OR "Abidjan"`、`site:peeringdb.com "Côte d'Ivoire" "Facility"`、`"CIVIX" "Abidjan" "PeeringDB"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **Data Center National**（A 级）：区 Abidjan、地点 Anoumambo、场地 AIGF；部委页（https://www.telecom.gouv.ci/new/actualite/63 与 /73：2024-05-16 现场考察、360 亿 FCFA、24 个月建设、2023-12-14 奠基）+ EXIM 董事会批准 6,600 万美元担保（Cybastion 设备/出口角色）。EXIM 融资批准 ≠ 运营状态；保持 construction/project 直到部委或运营商确认投运。
- **ARTCI**（https://artci.ci A）：牌照持有人、电信授权与数据保护决定的 A 级证据，非设施登记册（除非决定点名设施）。数据保护/本地托管声明应引用 Loi n°2013-450 与 ARTCI 指引而非市场博客。
- **SIGUPC/GUPC 建筑许可**（https://guichet.construction.gouv.ci/GUPC/，验证 200）：仅当记录识别申请人/场地时为 A 级许可；区门户搜索弱，结合官方域名搜索与通用搜索。
- **能源**：ANARE-CI（https://anare.ci，403 需浏览器）、CI-ENERGIES（https://www.cinergies.ci，200）、CIE（https://www.cie.ci，证书问题用浏览器）。A 级电力事实通常需官方公用事业/监管文件或运营商技术表。
- **ANDE/EIES**：Raxio 官方 CIV1 页链接 ESIA Executive Summary——可访问时为 Raxio 环境尽调的 A 级。
- **CEPICI/IDU**：https://cepici.ci / https://annuaireidu.ci ——PAIX DATA CENTRES 在 IDU 列示，经营目标含中立数据中心运营/开发与 colocation（一手登记证据）。采购：https://www.marchespublics.ci / https://sigomap.gouv.ci。
- **ANSSI**（https://www.anssi.ci）：网络安全/国家托管要求语境，点名站点/运营商前不证明设施。
- 记录提取清单：`facility_name/operator/owner-SPV/source_name/source_url/source_grade/fact_grade`；`district/region-commune/locality/坐标`（区分营销 metro 与法定区）；状态按 MoU→permit/financed→first stone→construction→inaugurated→operational；容量带来源限定词（racks current vs full build、m2 site vs white space、MW utility vs IT load、Tier certified vs designed-to/standards）；所需 joins：ARTCI 牌照、IDU/CEPICI、SIGUPC 许可、EIES/ANDE、CIE/CI-ENERGIES 电力、Uptime、PeeringDB 网络、运营商服务页。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场事实：商业市场集中于大阿比让，尤其 **VITIB/Grand-Bassam（Comoé 区）** 与 **Cocody/Yopougon（Abidjan 区）**。海缆/互联驱动需求：MainOne Grand-Bassam 登陆、ACE/SAT-3/WASC、2Africa/MTN GlobalConnect 公告、CIVIX/PeeringDB、PAIX 与 Equinix/MainOne 互联。
- 设施深潜：**Raxio CIV1**（Comoé/Grand-Bassam/VITIB；官方页：2,000 m2 白空间、3MW IT 功率、Tier III 认证、15kV 市电、48h 燃油后备、400 机架 key-fact；部委页 12,000 m2 场地/800 机架/3MW——400 当前 vs 800 满建分开存；2024 年投运）；**Equinix/MainOne AB1 & AB1.2**（Comoé/VITIB；PeeringDB fac/12168 给 VITIB Grand Bassam 与网络列表；AB1.2 为 2023 年开放的中立设施，Uptime Tier III standards 为 B 级设计/标准声明；AB1 vs AB1.2 身份明确，无独立建筑/产品证据不重复）；**ST Digital CIV01/CloudStore**（Comoé/Grand-Bassam/VITIB；2025-10-02 启用、4,000 m2 建筑面积、约 160 机架、Tier III 基建声明、主权云定位；PeeringDB fac/15646 列 48VDC/400VAC；Tier III 无 Uptime 记录视为设计/声明）；**PAIX Abidjan ABJ1**（Abidjan/Cocody；PeeringDB fac/6246 确认存在与别名；旧 `/en/locations/abidjan` 路径 404，用 paix.io 主页 + PeeringDB + IDU 直到 PAIX 发当前设施页；目录容量 ~900 m2/~2MW/~240 机架为 C 除非 PAIX 规格表确认）；**Data Center National**（见官方要点）；**Orange CI Grand-Bassam DC**（Comoé 可能，核验精确地点；B 级本地/商业媒体支持，需 Orange 官方页/ARTCI/CIE/VITIB 佐证；忽略目录不合理功率数字）；**MTN CI eCentre/下一代 DC**（Abidjan，旧报道 Yopougon；2014-2016 模块化交换/DC 设施，B 级电信内部基建，MTN Business 页证明对外服务前 C/B）；**Moov Africa CI**（仅电信在场 A，无公开设施页）；**Ambra Cloud/CenterServ/Stellarix 等本地主机**（线索，用官方页/ARTCI/IDU/面向客户托管报价后再建记录）。
- 贸易媒体（B）：DCD、Capacity Media、Connecting Africa、The Tech Capital、Agence Ecofin、TechAfrica News、We Are Tech Africa、ITWeb Africa、Financial Afrik、FratMat、AIP、Abidjan.net、Digitalmag.ci、Jeune Afrique。聚合器（C）：Datacenter Map、Baxtel、OCOLO、Datacenters.com、HostDir、Data Center Planet、Systalink、社交/经销商页/市场报告。PeeringDB 为 A-（存在/地点/互联元数据，用户维护但运营使用）。

## 来源分级

- **A**：点名设施/项目/牌照/许可/认证/场地的一手证据——部委或监管页、官方运营商页、Uptime 记录、PeeringDB 设施记录、公司登记记录、EXIM/USG 发布、公共采购通知、环境或电力申报。
- **B**：强二手——DCD、Capacity、Connecting Africa、The Tech Capital、Agence Ecofin、TechAfrica News、We Are Tech Africa、FratMat、AIP、Abidjan.net、Digitalmag.ci、Jeune Afrique、Financial Afrik、运营商转载第三方文章。
- **C**：仅线索——通用市场报告、目录条目、SEO 市场博客、社交、经销商声明、无具名场地/状态的 MoU 或公告、无运营商/官方支撑的容量值。按事实分别分级；一页可对存在性 A、对未引用 MW/机架值 C。

## 使用流程（探索/复核批次）

1. 从 A/A- 源播种：Raxio 官方页、Equinix 官方/PeeringDB、ST Digital/PeeringDB、PAIX PeeringDB/IDU、部委/EXIM（国家 DC）。
2. 加 B 级贸易媒体启用日期与公告容量；标记任何不在官方/运营商页的数字。
3. Join 官方记录：ARTCI、SIGUPC、VITIB、CIE/CI-ENERGIES/ANARE、ANDE/EIES、IDU/CEPICI、Uptime。
4. 跑 14 区扫描；仅当法/英词 + 运营商名查询失败后，才对非 Abidjan/Comoé 区标记 `no_projects: true`。
5. 状态归一化并去重营销名（坐标/地址/运营商页判定）。
6. 每轮重查超大规模官方区域页并带日期记录负面。遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:18Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] Data Center National：SIGUCP/ANDE/CIE/部委进展 joins，确认投运状态。
- [ ] Raxio CIV1：Uptime 记录直接核验；400 vs 800 机架对账。
- [ ] Equinix/MainOne AB1 vs AB1.2：官方页/PeeringDB 确认独立建筑与产品。
- [ ] 待核实：Orange CI Grand-Bassam 官方页/ARTCI/CIE 佐证；MTN Business 对外 colo/云服务证据；PAIX 当前设施页。
