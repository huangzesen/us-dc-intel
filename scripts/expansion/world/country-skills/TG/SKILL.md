---
name: tg-datacenter-methodology
location: scripts/expansion/world/country-skills/TG/SKILL.md
description: 多哥数据中心查询方法论（Togo datacenter discovery & audit methodology）——双线来源（官方/监管/云管线 + 行业/厂商/媒体发现）与 region 五区模型下的设施枚举规则。
---

# TG · 多哥数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：发现商业、电信、政府、企业与管线（pipeline）数据中心设施的官方与监管证据。双线方法论：`explorer-official.md`（官方/监管/云管线）与 `explorer-industry.md`（行业/媒体/厂商发现），均为 codex 审核定稿。划分模型（per manifest）：**5 个大区（region）**：Central、Kara、Maritime、Plateaus、Savannahs。法语常用拼写：Région Centrale、Région de la Kara、Région Maritime、Région des Plateaux、Région des Savanes；检索别名保留 `Plateaus/Plateaux`、`Savannahs/Savanes`、`Central/Centrale`。首都洛美（Lomé）位于 Maritime 区，并处在 Grand Lomé 城市圈。评审日期：2026-08-12。

## 入口

| 入口 | 管线 | 内容 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线 | 结构事实、已核官方/准官方入口（政府门户/数字部委/Lomé Data Centre/ARCEP/ARCOP/CEET/CEB/ARSE/IPDCP/API-ZF/PIA/World Bank）、核心设施与官方证据、监管与许可路径、海缆与互联、官方云区域负向检查、分区官方覆盖图、计数/分级/去重规则、输出字段模板 |
| `explorer-industry.md` | 行业/厂商/媒体发现 | 行业框架、本地媒体与政府新闻、非洲/国际行业媒体、运营商/托管商/厂商、互联/IXP/聚合目录与云负向、搜索模板（英/法）、分区枚举矩阵、分级与验证规则、已记录公告、来源锚点 |

## 核心结构事实

1. **行政区划模型**：region，5 个大区：Central（Sokodé、Tchamba）、Kara（Kara、Niamtougou）、Maritime（Lomé、Adétikopé）、Plateaus（Atakpamé、Kpalimé）、Savannahs（Dapaong、Mango）。商业/设施发现集中在 **Maritime - Lomé**。
2. **注册库现状**：多哥**没有公开的国家数据中心注册库**，官方枚举采用证据链：设施/运营者名称 -> 政府或运营方页面 -> 监管许可/决定 -> 建设或环评许可 -> 电力接入 -> 海缆/互联 -> 采购/融资记录。
3. **法律与监管**：ARCEP（arcep.tg，Autorité de Régulation des Communications Électroniques et des Postes，已纠正旧草稿 `artp.tg`）监管电子通信与邮政——列出 Loi n°2012-018、Loi n°2013-003 修订、Décret n°2015-091/PR；**ARCEP 不是数据中心建设许可机关**，用于核实运营商许可、网络互联、频谱/VSAT/电子信任服务、`.tg` 域名与通信基础设施线索。ARCOP（arcop.tg）公共采购监管。数字部委：`numerique.gouv.tg`（当前 Ministère de l'Efficacité du Service Public et de la Transformation Numérique，历史名保留作检索别名）。ANCy（ancy.gouv.tg，Loi n°2018-026 网络安全）与 IPDCP（ipdcp.tg，Loi n°2019-014 个人数据保护）均不证明物理设施。注意：`adetic.tg`/`adetic.td` 指向乍得相关 ADETIC，不得作为多哥官方来源。
4. **互联与云**：Maritime - Lomé 是已确认正篇——Lomé Data Centre 是已投运的国家/运营商中立托管设施；TogoIX/TGIX、WACS 与 Equiano 海缆登陆、运营商总部和核心网络也集中在洛美。WACS（Lomé/Afidegnigba 直接登陆）与 Equiano（2022 年 Lomé 登陆/CLS，CSquared Togo 页面确认；旧草稿缺口已补入）是互联资产非 DC；GLO-1 无确认多哥直接登陆（无可靠来源前不得写 Lomé landing，只记加纳/区域回程线索）；TogoIX/TGIX 由 ISOC Pulse/PeeringDB 佐证，不计入商业 DC 容量。官方云区域负向：截至 2026-08-12，AWS/Azure/Google Cloud/Oracle OCI 官方区域列表均未列多哥公有云 Region（负向证据 = A，按核验日期）；CDN/缓存/边缘节点、经销商或本地云服务不得升级为 hyperscaler region。
5. **设施/项目种子**：**Lomé Data Centre / LDC / Centre de Données de Lomé**（Maritime - Lomé，**operational**——政府官方页称 2021 年 6 月启用、首个中立 colocation centre、2022 年授权交予私人主体管理；World Bank WARCIP additional financing 支持 carrier-neutral colocation data center（WARCIP-Togo 总额 $30m、追加融资 $11m）；LDC 官网列 hosting、interconnection、1+ MW、800+ m2 usable space、Equiano/IX 路由）；**Société d'Infrastructures Numériques（SIN）**（owner/operator entity，A-/B 按来源拆分——政府/媒体称 SIN 管理国家数字资产并控制 LDC；写运营者优先用 LDC 官网/政府公告；Africa Data Centres 的 2021 管理角色需标日期）；**ST Digital private cloud at LDC**（marketed/private cloud service，B 待官方合同/新闻升级——服务级记录，不等同新物理 DC）；**TogoIX / TGIX**（operational IXP，B 互联资产）；**WACS landing - Lomé/Afidegnigba**（operational cable landing，B/A- 互联资产）；**Equiano landing - Lomé**（operational cable landing，A-/B 互联资产）；**GLO-1**（无确认直接登陆，B 负向/回程线索）；**PIA Adétikopé**（watch zone，A 园区，DC=U/negative until sourced——Togo + ARISE IIP 公私合作工业平台，无数据中心租户证据前不建设施）。
6. **语言与词汇**：法语召回最好；英语用于 DCD、World Bank、Connecting Africa、Telecompaper。关键词：`centre de données`、`data center`、`datacenter`、`carrier hotel`、`hébergement`、`colocation`、`cloud privé`、`salle des serveurs`、`fibre optique`、`point de présence`、`station d'atterrissement`、`mise en service`、`inauguration`、`câble sous-marin`、`appel d'offres`。生命周期动词：`projet / étude / MoU`（意向）；`appel d'offres / soumission / tender`（采购）；`construction / travaux / chantier`（在建）；`mise en service / inauguration / opérationnel / go-live`（启用）。
7. **可靠性分级**（对具体声明分级，而非对整座设施分级；同一设施可「存在性=A」「开通日期=A/B」「Tier 认证=A-/B」「MW=A」「机架数=C」）：A=一手/官方证据（`gouv.tg`、`republiquetogolaise.tg`、数字部委、Lomé Data Centre 官方站、ARCEP、ARCOP/公共采购、CEET/CEB/ARSE、IPDCP、世界银行/IFC/AfDB/BOAD、API-ZF/PIA 官方页、官方云区域页）；A-=政府、国有运营实体或运营商公告可证明具名设施/服务存在，但未给出许可、电力、地址或认证细节；B=可信二级证据且含具体当事方/日期/地点事实（DatacenterDynamics、Togo First、Agence Ecofin、Connecting Africa、TechAfricaNews、Telecompaper、TeleGeography/SubmarineCableMap、ISOC Pulse、PeeringDB）；C=仅线索（目录站、SEO 列表、社交帖、市场报告、无来源的机架/MW/面积表、Wikipedia）；U=未验证（仅见于聚合目录或单一弱来源；升级前必须复核）。
8. **计数与去重规则**：设施存在当且仅当来源点名**基础设施+位置**且足以区分物理站点；无具名站点的托管/云服务 = 服务级线索，单独保留。`facility_type` 保持精确：`commercial_colocation`、`government_hosting`、`national_data_center`、`telco_core`、`ixp`、`landing_station`、`planned_commercial_dc`、`lead_only`、`negative`。`status` 保持精确：`operational`、`marketed_service`、`announced`、`procurement`、`under_construction`、`commissioning`、`unknown`、`negative`。Lomé Data Centre 当前应写 `operational`，而不是 `announced/under_construction`。「Tier III」若由政府/运营方称述可记声明；若需认证级事实必须查 Uptime Institute 证书/公告或证书号；`Tier III+` 不是标准 Uptime 等级，按营销措辞记录。MW/机架/面积字段只记录来源明示单位：LDC 可记运营方 `1+ MW`、`800+ m2 usable space`；Togo First 2021 的 server-room/generator details 作 B 级补充。去重：LDC、TGIX、WACS/Equiano landing、Togocom/Moov 核心网络、ST Digital 私有云服务分开；IXP/landing station 不计商业 DC 容量。负向规则：`no_projects: true` 仅在完成带日期与查询记录的扫网后写入，不得静默遗漏。

## 常用查询模板

```text
site:lomedatacentre.tg hosting OR colocation OR "private cages" OR interconnection
site:arcep.tg "centre de donnees" OR "data center" OR hebergement OR colocation
site:arcep.tg "cable sous-marin" OR "station d'atterrissement" OR "fibre optique"
site:numerique.gouv.tg "Lome Data Centre" OR "centre de donnees" OR datacenter
site:republiquetogolaise.tg "Data Center de Lome" OR "centre de donnees"
site:ancy.gouv.tg "centre de donnees" OR "infrastructure critique" OR hebergement
site:ipdcp.tg hebergement OR "centre de donnees" OR "transfert transfrontalier"
site:arcop.tg "centre de donnees" OR datacenter OR "infrastructure numerique"
site:worldbank.org Togo WARCIP "carrier-neutral colocation data center"
site:projects.worldbank.org Togo "data center" OR "centre de donnees" OR WARCIP OR WARDIP
site:ifc.org CSquared Togo Equiano "data center" OR "landing"
site:ceet.tg "Lome Data Centre" OR datacenter OR "centre de donnees" OR raccordement
site:arse.tg "Lome Data Centre" OR datacenter OR "autoproduction" OR "groupe electrogene"
site:apizf.org "data center" OR datacenter OR "centre de donnees" OR numerique
site:pia-togo.com "data center" OR datacenter OR "centre de donnees" OR TIC
"Togo" ("data center" OR "data centre" OR datacenter OR colocation) (Lome OR Lomé OR Maritime)
"Lome Data Centre" OR "Lomé Data Centre" (SIN OR "Africa Data Centres" OR "ST Digital" OR "World Bank")
"Togo" "carrier-neutral colocation data center" OR "carrier hotel"
"Togo" (WACS OR Equiano OR "GLO-1") (landing OR "landing station" OR "submarine cable")
"Togo" ("centre de donnees" OR "data center" OR datacenter OR "centre d'hebergement" OR colocation)
"Societe d'Infrastructures Numeriques" Togo "centre de donnees" OR "Lome Data Centre"
"Adetikope" OR PIA Togo ("centre de donnees" OR datacenter OR numerique)
site:togofirst.com Togo "Lome Data Centre" OR "centre de donnees" OR "cloud prive"
site:agenceecofin.com Togo "centre de donnees" OR datacenter OR "cloud prive"
site:datacenterdynamics.com Togo "Lome Data Centre" OR "data center" OR Equiano
site:connectingafrica.com Togo "data center" OR "Lome Data Centre" OR CSquared OR "ST Digital"
site:submarinecablemap.com WACS Lome Togo
site:submarinecablemap.com Equiano Lome Togo
site:csquared.com Togo Equiano Lome "landing"
"Togo Internet Exchange Point" OR TGIX OR TogoIX Lome
site:pulse.internetsociety.org "Togo Internet Exchange Point" OR TGIX
site:peeringdb.com "Lome Data Centre" OR TGIX OR Togo
site:uptimeinstitute.com Togo "Lome Data Centre" OR "SIN-1-LOME"
```

分区通用扫描：`"{division_or_city}" Togo "centre de donnees" OR datacenter OR "data center" OR "salle de serveurs"`；`"{division_or_city}" Togo hebergement OR colocation OR cloud OR "point de presence"`；`site:arcep.tg "{division_or_city}" fibre OR licence OR autorisation`；`site:ceet.tg "{division_or_city}" raccordement OR poste OR "grand client"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **核心官方锚点**：政府门户 `gouv.tg` / `republiquetogolaise.tg`（后者有 Lomé Data Centre 2022 管理安排报道，A）、数字部委 `numerique.gouv.tg`（A/A-，旧新闻页存占位需交叉验证）、Lomé Data Centre `lomedatacentre.tg`（A）、ARCEP `arcep.tg`（A）、ARCOP `arcop.tg`（A）、电力 CEET `ceet.tg/tg/` / CEB `cebnet.org` / ARSE `arse.tg`（A）、数据保护 IPDCP `ipdcp.tg`（A，不证明物理设施）、投资/自贸区 API-ZF `apizf.org` / PIA `pia-togo.com`（A）、国际融资 World Bank/IFC（A）。
- **监管与许可路径**：ARCEP 页面/下载 = A、可信媒体转述 ARCEP 决定 = B、无 URL 的许可清单 = C。数据中心项目采购通常更可能出现在 World Bank/IFC/AfDB 或部委文件中（World Bank 2021 press release 确认 WARCIP additional financing 用于 carrier-neutral colocation data center，WARCIP-Togo $30m + $11m；不要把 WARDIP 项目编号写入 TG 记录，除非当批从 World Bank 项目页直接核到 Togo 组件）。电力/环境/建设许可：CEET 配电/售电与接入、CEB 贝宁-多哥发输电共同体（跨境/高压输电线）、ARSE 电力监管（生产/自发电/许可和服务质量）；环评/建设许可按 Grand Lomé、Golfe/Agoè-Nyivé 等地方政府与环境关键词检索，未见统一机检全国数据库；备用发电机、燃料、冷却、水耗、噪声等只能按 EIES/许可原文记录。
- **分区官方覆盖**：Maritime——正篇（Lomé/LDC/SIN/ST Digital、TogoIX/TGIX、WACS、Equiano、CSquared Woezon、Togocom/Yas/Moov、Grand Lomé 建设/环评、CEET 接入、PIA/Adétikopé）；Plateaus、Central、Kara、Savannahs——`no_projects_expected`，仅 PoP/行政机房/大学计算房线索（Kara 大学计算房线索不自动计数），交换机房需官方证据。
- **输出字段模板**（示例 LDC）：country_code TG、division Maritime、commune Lome、operator 按最新官方来源（SIN/current operator）、status operational、facility_type national_data_center / carrier_neutral_colocation、capacity_mw 1.0（运营方营销值，不超出原文推断 IT load）、area_sqm 800（运营方 800+ m2；2021 媒体给五个 133 m2 服务器房）、tier 按声明记录（Uptime 证书才入认证级）、evidence_grade A（存在性）/B（行业媒体技术细节）、evidence_date 2026-08-12。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **行业框架**：多哥市场很小但有一个明确核心设施 **Lomé Data Centre（LDC）**——洛美运营中 carrier-neutral colocation / national data center，World Bank WARCIP 融资支持，政府 2022 页称其 2021 年 6 月启用。当前 LDC 官网营销 `1+ MW`、`800+ m2 usable space`、hosting、interconnection、remote hands、managed cybersecurity services，并列 Equiano、regional IX partnerships、submarine/fiber routes。**ST Digital + SIN 私有云**是 2026 年服务级线索（部署在 LDC，不是新建物理数据中心）。**互联资产强**：TGIX/TogoIX、WACS、Equiano——支持设施可用性判断但不计 DC 容量。
- **本地媒体与政府新闻**：Togo First（B；引用官方时 A-）、République Togolaise/Togo Officiel（A）、数字部委（A/A-）、Agence Ecofin（B）、ATOP（B/B+ 官方通讯社）、Togo Matin/Lomé Actu/TogoBreakingNews（C+/B-）。
- **非洲/国际行业媒体**：DCD（B/B+）、Connecting Africa（B）、TechAfricaNews（B/C）、Telecompaper（B，通常需原始来源补强）、Submarine Networks（B，需 TeleGeography/运营方交叉）、IFC/World Bank（A）、ADCA/市场报告（B/C，不作单独设施证据）。
- **运营商/托管商/厂商**：LDC（A）、SIN（A-/B 按来源拆分，无稳定单独官网）、ST Digital Togo（stdigital.io 集团 + Togo First/Connecting Africa，B 服务级）、Africa Data Centres（B 历史运营角色，需最新官方确认）、Togocom/Yas/Togo Telecom/Togocel（B/C，普通电信服务不计 DC）、Moov Africa Togo（B/C）、CSquared Woezon/CSquared Togo（A-/B 互联，不是 DC）、TogoIX/TGIX（B 互联）、PIA Adétikopé（A 园区，DC=U/negative until sourced）。
- **已记录公告**：LDC（已投运，status operational）；SIN + ST Digital private cloud at LDC（marketed_service / service_at_existing_facility，不新增数据中心）；TogoIX/TGIX（互联资产）；WACS + Equiano Lomé landings（直接海缆登陆，互联资产，Equiano 已补为确认线索）；GLO-1（未确认直接登陆，不得写 Lomé landing）；PIA Adétikopé（watch zone，无 DC 租户证据不建记录）。

## 维护注意（更新纪律）

- 不删除/移动任何既有文件；双 explorer 文件是 codex 审核定稿，SKILL.md 忠实提炼其内容，细则差异以 explorer 原文件为准。
- 每批核查动作：① LDC 官网与 news 页 ② `republiquetogolaise.tg`/`numerique.gouv.tg`/Togo First ③ World Bank/IFC ④ DCD/Connecting Africa/Agence Ecofin ⑤ ISOC Pulse/PeeringDB/SubmarineCableMap ⑥ AWS/Azure/GCP/OCI 官方区域页。
- 多哥枚举应围绕一个已运营的 LDC 设施展开，谨慎分离「物理数据中心」「私有云服务」「IXP」「海缆登陆站」「运营商 PoP」；行业目录可用于发现别名（如 LOM1/ADC Lome），但不得覆盖官方/运营方证据。
- 不得从 CDN、edge cache、Marketplace、本地合作伙伴、私有云服务或数据驻留营销创建多哥 hyperscaler facility；MW/机架/面积除非官方/运营商/招标来源明示一律 null。
