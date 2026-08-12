---
name: cg-datacenter-methodology
location: scripts/expansion/world/country-skills/CG/SKILL.md
description: |
  Republic of the Congo / Congo-Brazzaville (CG) datacenter discovery & audit methodology — how to enumerate, verify, and update CG datacenter projects at department granularity (12 legacy/manifest departments; official 15-department frame since the 2024 reform maps back to legacy coverage). No public national datacenter registry: enumeration is French-first and joins ministry (postetelecom.gouv.cg) and ARPCE regulator/IXP evidence, AfDB/World Bank donor records (Bacongo national DC, Oyo secondary), official operator pages (ST Digital), E2C energy/grid clues, and disambiguated trade press (Agence Ecofin, DCD, ADIAC). Verified seeds: ST Digital Brazzaville, ARPCE Pointe-Noire Tier 3+ DC (hosts CGIX-PN), AfDB-funded national datacenter at Bacongo (near completion target May 2026, not yet proven operational), ARPCE Brazzaville 2021 lead, Congo Telecom PNR1 carrier lead. Read this before running CG exploration/audit batches. Routes to explorer-official.md (regulators/donors/energy/cloud-negative/12-department map) and explorer-industry.md (operators/IXP/trade press/dedupe rules).
---

# CG · 刚果（布）数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：刚果（布）**无**全国数据中心注册库，法语优先搜索（`centre de données`、`datacenter`、`hébergement`、`colocation`、`salle serveurs`、`cloud souverain`、`point d'échange Internet`、`CGIX`、`poste électrique`、`EIES`、`appel d'offres`）；每次必须与刚果（金）DRC 消歧（本国防 Brazzaville/Pointe-Noire/Oyo/ARPCE/Congo Telecom，DRC 常见 Kinshasa/ARPTC/SNEL/Raxio/OADC）。
> 分区模型：manifest 用 **12 旧省**（Bouenza; Brazzaville; Cuvette; Cuvette-Ouest; Kouilou; Lekoumou; Likouala; Niari; Plateaux; Pointe-Noire; Pool; Sangha）；2024 年改革后官方为 **15 省**（新增 Nkeni-Alima、Djoue-Lefini、Congo-Oubangui），搜索时叠加新名但记录归 12 旧省。
> 市场集中在 **Brazzaville** 与 **Pointe-Noire**；Oyo（Cuvette）二级国家 DC 仅招标/规划。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供刚果（布）探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：邮电部（postetelecom.gouv.cg）、ARPCE（监管 + IXP 赞助，CGIX-PN 寄主）、ANSSI、E2C 电力与许可/EIES、AfDB/世界银行（P175592/PATN）采购、云区域负面控制、Uptime、12 省覆盖策略与记录规则 |
| `explorer-industry.md` | 行业/厂商发现：设施种子表（ST Digital、国家 DC Bacongo、ARPCE Pointe-Noire、ARPCE Brazzaville 2021、Oyo、Congo Telecom PNR1、WACS/2Africa）、云/CDN/on-ramp 检查、贸易媒体分级、查询库、省际模式、验证与去重规则 |

## 核心结构事实（框定每次搜索）

1. **无注册库，链条式取证**：官方/监管 + 捐赠方项目 + 运营商官方页 + IXP 证据 + 能源/许可线索 + 贸易媒体；物理设施记录需要“地点或设施语言”（机架、白空间、colo、IXP 寄主、Tier 设计/认证、launch/construction/commissioning）。
2. **三大已证实种子（Brazzaville/Pointe-Noire）**：① ST Digital Brazzaville——官方页确认 colo/cloud/DRP/BCP 与 Tier 3 语言（A 服务/地点；Uptime 认证未验证）；② ARPCE Pointe-Noire DC——2024-02-28 投运，Tier 3+ 主张，2024-09-20 起寄主 CGIX-PN，DCD 报 54 机架/156 sqm/3.8bn FCFA（B，官方数据表前容量为 B/C）；③ 国家数据中心 Bacongo（Brazzaville）——AfDB 融资、三层+地下室技术用房、Tier III 目标、Sumec 承包商；最新公开状态 95%/2026-05 目标投运，**无可靠 inauguration 证据前不标 operational**（A 项目/融资，B 状态）。
3. **三个 Brazzaville 线索必须分别对待**：ST Digital、AfDB Bacongo 国家 DC、ARPCE 2021 Brazzaville DC——仅在精确地址/运营商/项目证据出现时才可合并。
4. **Oyo（Cuvette）**：二级国家 DC 与第三个 CGIX 规划为招标/规划线索（Agence Ecofin 2022-02 招标，B），无中标/施工/投运证据前不升级。
5. **连接资产 ≠ 数据中心**：WACS Matombi（Kouilou）、2Africa Pointe-Noire 登陆站、CGIX/CGIX-PN、Congo Telecom PNR1（目录 C）——除非源点名 colo/机架/白空间。
6. **15 省改革映射**：Nkeni-Alima≈Plateaux；Djoue-Lefini≈Pool/Plateaux/Brazzaville 腹地；Congo-Oubangui≈Cuvette/Likouala 河域；搜索含新名，存储归旧省。
7. **无超规模云区域**：AWS/Azure/GCP/OCI 官方列表无 CG（A 级负面）；本地 cloud/hosting 须有刚果物理场地证据。
8. **状态/容量层级**：官方/运营商投运页 > 投运报道 > 在建官方/捐赠页 > 中标 > 招标 > 政策；官方数据表 > 运营商声明 > 引述运营商媒体 > 目录。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§3 / explorer-industry.md §4）

- 部委：`site:postetelecom.gouv.cg "data center" OR "centre de donnees" OR datacenter`、`site:postetelecom.gouv.cg "Bacongo" OR "Oyo"`、`"Leon Juste Ibombo" "data center" Congo`。
- ARPCE/IXP：`site:arpce.cg "centre de donnees" OR "point d'echange Internet"`、`"ARPCE" "Tier 3+" "Pointe-Noire"`、`"CGIX-PN" "datacenter"`。
- 捐赠/采购：`site:afdb.org Congo datacenter`、`site:documents.worldbank.org P175592`、`"Congo" "appel d'offres" datacenter Oyo Brazzaville`。
- 能源：`site:e2c.cg "Brazzaville" OR "Pointe-Noire" "poste"`、`"datacenter national" Bacongo electricite OR E2C OR MVA OR MW`。
- 消歧通用：`("Republique du Congo" OR "Congo-Brazzaville" OR Brazzaville OR "Pointe-Noire") (datacenter OR "data center" OR "centre de donnees" OR colocation)`、`"Congo" datacenter -RDC -Kinshasa -Lubumbashi -ARPTC`。
- 运营商 pivot：`"ST Digital" Brazzaville datacenter OR colocation OR "Tier III"`、`"datacenter national" Congo Bacongo OR Sumec OR BAD OR AfDB`、`"Congo Telecom" PNR1 OR hebergement OR Matombi`。
- 云/CDN：`"Brazzaville" ("AWS Direct Connect" OR ExpressRoute OR "Cloud Interconnect" OR FastConnect OR CDN OR edge)`。

## 官方/监管管线要点（详见 explorer-official.md）

- 邮电部（A）：国家 DC 计划、Congo Telecom/运营商机构页、官方项目描述；单独不足以推断商业 colo。
- ARPCE（A 监管/许可/IXP；B 经 ADIAC/Agence Ecofin 的 DC 事实）：CGIX 页与 Pointe-Noire DC 事实源。
- ANSSI（合规/主权托管线索，非注册库）；E2C（电力/电网）；无全国建设许可搜索库——许可在市镇/城市规划层，具名许可为 A/B。
- 捐赠方：AfDB（国家 DC/CAB，A 融资范围）、世界银行 PATN/P175592（A 文档）；招标公告（B）至中标/施工前为规划。
- Uptime：CG 无公开认证记录；Tier III/Tier 3+ 仅是设计/合规/运营商主张，除非 Uptime 列表确认。
- 证据规则：运营商页 > 目录；IXP 寄主仅在寄主点名时算设施证据；登陆站是连接非 colo；DRC 源一律拒收；`cloud/hébergement/hosting` 无刚果物理场地证据不计数。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 贸易媒体（B）：Agence Ecofin、DCD、Digital Business Africa、Telecompaper、We Are Tech Africa、ADIAC、ACI、Vox.cg、Tribune-Eco、Pages Afrik、Les Dépêches de Brazzaville；本地报道引述具名官员/运营商时 B+。
- 运营商/实体种子：ST Digital（A）、Congo Telecom（A 公司页/B 连接）、ARPCE、SOFIA/GVA-Canal Box/MTN/Airtel/Alink/AMC/PI Service-Sky TIC/Silicone Connect/Mambs（B 市场存在，多数仅网络线索）、CEC Telecom（C）。
- 目录（C）：DataCenterMap/DataCenters.com/DataCentersList/colo.exchange/Inflect/Neocloud——仅用于别名与地址，须 join 官方/运营商。
- 去重：Brazzaville 三线索按日期/业主；PNR1 与 ARPCE DC 分开；登录站/IXP 不单列；Oyo 招标不升级；Tier 语言须认证证明；状态日期显式（Pointe-Noire 2024-02-28 投运、CGIX-PN 2024-09-20、Bacongo 目标 2026-05 未证实）。

## 已知设施/项目与证据状态

| 设施/项目 | 省 | 状态与证据 |
|---|---|---|
| Datacenter national du Congo – Bacongo | Brazzaville | 在建/近完成（A 项目融资/部委页；B 2026-05 目标）；Sumec 承包商、Tier III 目标；无投运证据前不标 operational |
| ARPCE Data Center – Pointe-Noire | Pointe-Noire | 2024-02-28 投运（B）；Tier 3+ 主张；CGIX-PN 寄主（2024-09-20）；54 机架/156 sqm 为 B/C |
| ARPCE Data Center – Brazzaville 2021 | Brazzaville | B 线索（DCD/Telecompaper 引述 ARPCE DG）；与 ST Digital/Bacongo 分别对待 |
| ST Digital Brazzaville | Brazzaville | A（官方页服务/地点）；Uptime 认证未验证；地址/合规待 join |
| Data center national secondaire – Oyo | Cuvette | 仅招标/规划（B）；无中标/施工证据 |
| Congo Telecom PNR1 carrier facility | Pointe-Noire | C 目录线索；须 Congo Telecom/PeeringDB/ARPCE 确认 |
| WACS Matombi / 2Africa Pointe-Noire | Kouilou/Pointe-Noire | 连接资产（B）；非 DC |
| CGIX / CGIX-PN | Brazzaville/Pointe-Noire | IXP（A ARPCE 页/B 报道）；CGIX-BZV 寄主未定 |

## 更新节奏

- 每批次：云区域负面核查、Bacongo 国家 DC inauguration/投运新闻、Oyo 中标与施工、ARPCE 数据表、ST Digital 地址/认证。
- 季度：15 省新标签（Nkeni-Alima/Djoue-Lefini/Congo-Oubangui）搜索、CGIX 第三点、新海缆（2Africa/WACS）相邻设施、Uptime CG 列表。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（12 省粒度）；本 skill 作为国家层参考注入。
