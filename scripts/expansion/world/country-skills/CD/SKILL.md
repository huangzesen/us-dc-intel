---
name: cd-datacenter-methodology
location: scripts/expansion/world/country-skills/CD/SKILL.md
description: |
  Democratic Republic of the Congo (CD/DRC/RDC) datacenter discovery & audit methodology — how to enumerate, verify, and update DRC datacenter projects across 26 province/city divisions. The DRC has no complete national datacenter registry: enumeration triangulates GUPEC construction permits, provincial/urbanisme sources, ARPTC telecom titles (operator census — ARPTC, not CG's ARPCE), ARE/SNEL electricity evidence, ADN/PTNTIC digital-government records, Uptime Institute certifications, operator pages (Raxio DRC1, OADC Texaf, Orange RDC, Fastnet Lubumbashi), IXP/PeeringDB leads (KINIX, ACIX), and trade press. French-first search; strict CD-vs-CG disambiguation. Read this before running CD exploration/audit batches. Routes to explorer-official.md (official/regulatory/cloud pipeline) and explorer-industry.md (trade press / vendor discovery).
---

# CD · 刚果民主共和国数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：刚果（金）**没有**完整的全国公共数据中心注册库，实用设施证据**Kinshasa 优先**；枚举须组合：GUPEC 建设许可流程、省级 urbanisme/habitat 来源、ARPTC 电信牌照与观察站、ARE/SNEL 电力证据、ADN/数字部政府云来源、运营商官方页、Uptime Institute 认证记录、云厂商区域表、IXP/PeeringDB 线索与行业媒体。
> **法语优先**（centre de données / datacenter / hébergement / colocation / cloud souverain / permis de construire / poste électrique / EIES），再补英文变体；刚果（金）与刚果（布）严格区分。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供刚果（金）探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：GUPEC 许可、Urbanisme/MEDD/ACE（EIES）、ARPTC 牌照与观察站、ARE/SNEL/MRHE 电力、数字部/PTNTIC/ADN/ARMP 政府云与采购、云区域负向对照、Uptime 认证记录、运营商种子表、26 省别名表与逐省策略 |
| `explorer-industry.md` | 行业/厂商发现：Raxio/OADC/Orange/Fastnet/GBS/United 种子、ARPTC ISP/MNO 名单、KINIX/ACIX/PeeringDB/ISOC Pulse 互联、ADCA 协会、DCD/Connecting Africa/Developing Telecoms/Ecofin 媒体、目录（C 级）、26 省查询模式、验证与陷阱 |

## 核心结构事实（框定每次搜索）

1. **Kinshasa 为主市场**：强设施种子——Raxio DRC1（Limete industriel 12ème Rue 9/11：1,056 m² 白空间、400 机架、1.5 MW IT、33 kV 供电、2024 开园、Tier III）、OADC Texaf Kinshasa/FIH1（SILIKIN Village/COTEX：1,000 m² 技术空间、N+1 冷却、2 MW 场地负载、Tier III 设计认证、计划 2024 Q3 上线、初始 400 m²、远期 550+ 机架）、Orange Business RDC 托管服务、GBS/United 较弱线索。
2. **法语优先**：`centre de données`、`centres de données`、`data center`、`datacenter`、`hébergement datacenter`、`cloud souverain`、`colocation`、`carrier neutral`、`Tier III`、`salle serveur`、`point d'échange Internet`、`poste électrique`、`permis de construire`、`GUPEC`、`EIES`。
3. **刚果（金）/刚果（布）混淆是头号陷阱**：`Congo data center`、`datacenter national du Congo` 常返回布拉柴维尔（CG）结果；查询必须带 `RDC`/`RD Congo`/`Congo-Kinshasa`/`République Démocratique du Congo`/`DRC` 或刚果（金）城市/省；刚果（金）监管机构是 **ARPTC**，刚果（布）是 **ARPCE**；拒绝含 Brazzaville/Pointe-Noire/CEMAC 的结果。
4. **PNN Horizon 2025 = 目标城市图，不是设施证据**：规划文本呼吁在 Goma、Moanda、Kisangani、Kinshasa、Lubumbashi 建设至少 5 座中立 Tier-3/4 数据中心——只有具名招标/合同/场地/建设/开园才计设施；不得凭空建 26 个「规划设施」。
5. **云证据语义**：AWS/Azure/GCP/OCI 官方区域表**无刚果（金）区域**（最近为南非区域：AWS af-south-1 Cape Town、Azure SA North/West、GCP africa-south1 Johannesburg、OCI af-johannesburg-1）——「刚果（金）云服务」营销不构成物理设施，除非点名本地数据中心。
6. **容量语义**：精确保存来源口径——`IT power`、`site load`、`MVA`、`white space`、`technical space`、`racks`；无假设不把 MVA 换算 MW；运营商官方 MW/机架或认证数据表 = A，行业文章引述运营商 = B，目录数字 = C。
7. **IXP ≠ 数据中心**：KINIX（23 ASN、累计 1,407 Gbps 成员端口，本地设施 OADC FIH1 + Raxio DRC1）、Lubumbashi IXP（ISOC 2019）、ACIX（DE-CIX 支持，2026 扩展入 OADC——刚果（金）首个分布式 IX）是互联线索；区分交换设施与建筑。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§3 / explorer-industry.md §4-§5）

- 许可/规划：`site:gupec-rdc.com "data center"`、`site:gupec-rdc.com "centre de données"`、`site:urbanisme.gouv.cd "permis de construire" "Kinshasa"`、`site:cadastre.gouv.cd "{运营商}" Kinshasa`、`site:medd.gouv.cd "centre de données" "EIES"`。
- ARPTC：`site:arptc.gouv.cd "centre de données"`、`site:arptc.gouv.cd "station d'atterrage"`、`site:arptc.gouv.cd "point d'échange internet"`、`site:arptc-solution.cd/license_list/operatorinternetgrp`（ISP 名单，A 级运营商普查）。
- 电力：`site:are.gouv.cd "data center"`、`site:snel.cd "centre de données"`、`site:snel.cd "Limete" "33kV"`、`"Raxio" "Kinshasa" "33kV"`、`"OADC" "Kinshasa" "MVA"`。
- 政府云/采购：`site:numerique.gouv.cd "cloud souverain"`、`site:adn.cd "data center"`、`site:ptntic.gouv.cd "centre de données"`、`site:armp-rdc.cd "centre des données"`、`"RDC" "Fourniture d'équipements de centre des données" "Cloud souverain"`。
- Uptime：`site:uptimeinstitute.com/uptime-institute-awards "Congo, Democratic Republic of the"`、`site:uptimeinstitute.com "DRC1"`、`site:uptimeinstitute.com "OADC Texaf"`。
- 行业：`site:datacenterdynamics.com "Democratic Republic of the Congo" "data center"`、`site:connectingafrica.com "DRC" "data center" Kinshasa`、`site:agenceecofin.com "RDC" "data center"`、`site:mediacongo.net "centre des données"`。
- 云负向：`site:aws.amazon.com "Democratic Republic of Congo" "Local Zone"`、`site:cloud.google.com "Kinshasa" "region"`、`"Kinshasa" "cloud region" AWS OR Azure OR Google OR Oracle`。

## 官方/监管管线要点（详见 explorer-official.md）

- **GUPEC（A 级建设许可锚点）**：全国统一发放 `permis de construire`；本探索未发现可检索的公共许可登记册——靠网页索引的 GUPEC/urbanisme 公告、部委发布、点名许可的地方媒体或直接许可文件。
- **ARPTC（A=运营商/服务合法性，非设施登记）**：电信特许经营类别含全国骨干、登陆站、国际转接中心、基础设施共享、内部网络申报、社区 IXP；高收益名称：Raxio Data Centre SAS、OADC Texaf Digital DRC、WIOCC、TEXAF、Orange RDC、GBS、United、Microcom、Standard Telecom Congo、Orioncom、Paratus、ITM、Vodacom/Airtel/Africell/SCPT/Liquid/AFR-IX。
- **ARE/SNEL（A=电力）**：ARE 对公共领域外自发电 100 kW–999.99 kW 及部分私营线路发放授权，更大独立发电/进出口/商业化需更高级别牌照——柴油/光伏/私营线路数据中心可能以电力记录出现；SNEL 检索 `data center`/`centre de données`/33 kV/变电站。
- **数字政府（A=已发采购/合同/官方上线）**：数字经济部、PTNTIC、ADN、ARMP；采购术语 `Cloud souverain`、`centre des données`、`data center national`、`plateformes numériques sécurisées`、`sauvegarde`、`disaster recovery`、`certification Tier`；dgMarket/AFD 采购镜像可作线索。
- **Uptime Institute（A=认证存在/具名设施/位置）**：Raxio DRC1 与 OADC Texaf FIH1 均有记录；与运营商页配合取容量与地址。
- **云**：无刚果（金）超大规模区域（负向对照）；本地 carrier-neutral 设施仅作可能的伙伴/边缘/PoP 线索。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商/设施种子（A=官方存在/B=容量）：Raxio DRC1（A，数据表 1.5 MW IT/400 机架/Limete）、OADC Texaf Kinshasa（A/B，2 MW 场地/550+ 机架/SILIKIN）、Fastnet Lubumbashi（B，ESNAP 地面站、50 机架、2017 开园——先核验是否仍在运营）、Orange Business RDC 托管（B，无公开地址/容量）、GBS（C 直到官方页/ARPTC/PeeringDB 确认）、United S.A.（C/B，165 Batetela Ave，托管/光纤）、Orioncom/Microcom/Afrinet/Liquid/CSquared/GVA（B 运营商线索——POP/交换室≠数据中心，须有明确 colo/白空间证据）。
- 运营商登记（A=持牌存在，非设施）：ARPTC ISP 名单（Airtel、Orange、Vodacom、GVA、Liquid、Microcom、United、CSquared、Orioncom、GBS、Fastnet、Africell 等）与移动运营商名单；Africa Data Centres Association 会员（B，泛非运营商 Raxio 等）。
- 互联（B+ 生态系统，非设施证据）：KINIX/ISOC Pulse（2026-07：23 ASN、1,407 Gbps）、Lubumbashi IXP、ACIX/DE-CIX 分布式 IX（进入 OADC）；Console Connect Africa Interconnection Report 2025（B）点名 Kinshasa 两座新 DC、约 20 家运营商与 Goma/Lubumbashi IXP。
- 媒体（B）：DCD、Connecting Africa、Developing Telecoms、Agence Ecofin、Actualite.cd/Radio Okapi/Zoom Eco/DeskEco/MediaCongo/CIO Mag（B/C，视是否引述具名运营商/部委/招标）；D4D Hub/Xalam 市场简报（B，市场语境，不作单设施归因）。
- 目录（C 线索）：DataCenterMap、Datacenters.com、Inflect、Baxtel、DC Hub、Data Center Platform——用于地址/别名发现，常含 POP/托管办公室/陈旧设施，须回查运营商页/ARPTC/PeeringDB/开园报道。

## 来源分级

- **A** = 官方/一手/法律来源：GUPEC 许可记录、国家/省 urbanisme/habitat 来源、ARPTC 牌照/授权/申报材料（运营商地位）、ARE/SNEL 电力权证或官方电网/并网证据、数字部/ADN/PTNTIC 政府云记录（已发采购/合同/上线）、云厂商官方位置页（区域/边缘存在）、运营商官方设施页（存在/位置）、Uptime Institute 认证记录、官方采购公告。
- **B** = 强二级：DCD、Connecting Africa、Ecofin、CIO Mag、Telecompaper、Computer Weekly、Internet Society/PeeringDB/IXP 运营商记录、捐赠方/投资市场简报、开发商或施工承包商案例研究、可靠本地商业媒体（引述官方文件时）。
- **C** = 弱线索：泛泛市场报告、目录条目、社交帖、地图条目、无依据的「data center」声明、无具名场地或建设状态的国家战略目标。
- 状态层级：`operational/launch/inauguration` + 运营商页 > `under construction/groundbreaking` > `procurement/contract award` > PNN 战略/政治声明；政策目标（如「每个省首府建数据中心」）仅线索，不创建 26 个规划设施。
- **陷阱**：`hébergement`/`hosting`/`cloud` 页可能是境外托管服务——须有 `data center Orange RDC` 类文字、刚果（金）地址、ARPTC/PeeringDB 设施或运营商确认；矿业公司内部 IT 机房 ≠ 商用 colo；无一级许可时设施仍可凭「运营商官方页 + Uptime/PeeringDB/开园报道」判 `operational`（运营商/Uptime 事实记 A，缺 GUPEC/ARE 证据在 notes 说明）；`armp-rdc.org` 可能不可靠，先打开验证再用。
- **容量规则**：不换算无假设的 MVA→MW；`IT load`、`site load`、`white space`、`racks` 按原文存储。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=CD，divisions=26 省/市：Central Kongo…Tshuapa，见 explorer-official.md 头部列表与 §3.3 别名表）。
2. Kinshasa 种子：Raxio、OADC、Orange、GBS、United、KINIX 成员 + 目录；按地址与运营商去重（Limete/Gombe/Ngaliema/SILIKIN/COTEX）。
3. Lubumbashi 种子：Fastnet + 每个 ARPTC/KINIX 运营商名对 Lubumbashi/Haut-Katanga 逐一扫描；扫 PNN 目标城市 Goma、Moanda、Kisangani。
4. 逐省执行通用查询块（法语省名/首都 + centre de données/data center/datacenter/salle serveur/cloud souverain/colocation/point d'échange/permis de construire/poste électrique），26 省用别名表。
5. 官方核验：GUPEC/urbanisme 许可、ARPTC 牌照、ARE/SNEL 电力、Uptime 认证、运营商页、ARMP/部委采购；对每个命中记录证据等级并说明为何非 Kinshasa 项目是或不是真数据中心。
6. 行业补漏：DCD/Connecting Africa/Developing Telecoms/Ecofin/本地媒体 + 目录，无一级佐证则降级。
7. 云负向对照每次刷新前复核；当前公共证据不支持刚果（金）任何超大规模区域。输出 world 同 schema；无项目 division 写 `no_projects: true`（电信交换/银行机房/部委数据房单列）。
8. 遵行 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:45Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：探索/复核批次按 26 省分桶（Kinshasa 优先 → Lubumbashi → PNN 目标城市 → 其余 26 省别名扫描）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：OADC Texaf FIH1 是否已按计划 2024 Q3 上线及当前运营容量；Fastnet Lubumbashi 当前运营状态；GBS/United 设施官方页证据；Goma/Moanda/Kisangani 是否有具名招标/场地；主权云设备采购（dgMarket）最终授标与交付。
