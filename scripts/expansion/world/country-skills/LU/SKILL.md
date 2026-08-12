---
name: lu-datacenter-methodology
location: scripts/expansion/world/country-skills/LU/SKILL.md
description: |
  Luxembourg (LU) datacenter discovery & audit methodology — how to enumerate, verify, and update Luxembourg datacenter projects at canton + commune granularity (12 cantons, 100 communes in the current manifest). No national datacenter register and no single national building-permit portal: the practical permit unit is the commune (autorisation de construire via the bourgmestre, PAG/PAP planning, commodo/incommodo classified-establishment, EIE), joined by ILR/Creos energy & grid records, LBR company registry, marches.public.lu procurement, LU-CIX PoP cross-checks, and operator pages (LuxConnect, DEEP, Portus, OVHcloud, SecureIT, BCE). Market clusters: Bettembourg (Esch-sur-Alzette), Bissen (Mersch), Luxembourg City/Contern, Windhof/Koerich (Capellen), Kayl, Betzdorf. Google Bissen is a live pipeline (PAP/permit stage), not an operating facility and not a GCP region. No hyperscaler cloud region. Read this before running LU exploration/audit batches. Routes to explorer-official.md (permits/energy/commune surfaces/canton plan) and explorer-industry.md (operators/cloud controls/press/directories/canton recipes).
---

# LU · 卢森堡数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：卢森堡**无**全国数据中心注册库、**无**单一全国建设许可门户；实际许可单元是 **commune（市镇）**——`autorisation de construire/permis de construire` 向市长（bourgmestre）申请、须符合 PAG/PAP，另有 `établissement classé`（commodo/incommodo）营业许可与 EIE 环评。canton 仅作覆盖控制桶。
> 分区模型：**12 canton → 100 commune**；市场小而密：Bettembourg（Esch-sur-Alzette）、Bissen（Mersch）、Luxembourg City/Contern、Windhof/Koerich（Capellen）、Kayl、Betzdorf（Grevenmacher）。
> 生命周期证据尺度：市镇许可签发/运营商带地址设施页=计数；commodo/EIE 决定=受监管项目（未必已建）；PAP/PAG 采纳=仅线索；目录=仅线索。
> 无 AWS/Azure/GCP/OCI 云区域（官方页负面）；OVHcloud 有官方 Luxembourg datacentre 页（≠超规模区域）；Google Bissen 是管线非设施。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供卢森堡探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：行政与许可框架（Guichet.lu 建设许可/commodo）、Legilux、LBR 注册、marches.public.lu 采购、ILR/Creos 能源电网（网络发展计划 2024-2034）、市镇许可面（vdl/helperknapp/strassen/dudelange 等 12 例）、多语查询模板、12 canton 官方枚举计划、Google Bissen 处理、提取 schema 与验证规则 |
| `explorer-industry.md` | 行业/厂商发现：LuxConnect（DC1.x/DC2 地址+MVA）、DEEP/EBRC、OVHcloud、Portus/EDH、SecureIT、BCE、Visual Online、C2D、LuxNetwork、LuxProvide/MeluXina 种子；LU-CIX/PeeringDB；云区域控制；ICT Luxembourg/Luxinnovation/FEDIL 协会；DCD/Paperjam/Delano/ITnation/Luxembourg Times/RTL Today 媒体；目录（DataCenterMap/Baxtel 等 C）；12 canton 行业配方与查询包 |

## 核心结构事实（框定每次搜索）

1. **市镇许可为主干**：`autorisation de construire`（Guichet.lu 市民/企业两页，A）→ bourgmestre 权限 + PAG/PAP 符合性 + 公开展示/上诉；commodo/incommodo 分级（1/3 类→Administration de l'environnement/ITM，2 类→bourgmestre）；PAG/PAP 投票≠建成设施。
2. **能源是门槛**：ILR（监管）、Creos（TSO/DSO，网络发展计划 2024-2034 含变电站与大型负荷规划）、PNEC/Energieauer；大型负荷合理性须以电网证据验证。
3. **运营商官方页（A）**：LuxConnect（DC1.1/1.2/1.3 @ 202 Z.A.E. Wolser F, Bettembourg；DC2 @ 3 op der Poukewiss, Bissen；MVA/面积）、DEEP（POST 集团 B2B 品牌，融合 EBRC/Elgon/Digora Luxembourg/POST Telecom）、Portus（前 EDH，地下 Tier IV + 1 MW IT-load 扩展声称）、OVHcloud（官方 Luxembourg datacentre 页）、LuxProvide MeluXina（HPC 锚负荷，非公共 colo）。
4. **LU-CIX 网络图（A/B）**：确认具名 PoP/设施位置——BCE、DEEP West（Windhof）、DEEP East（Betzdorf）、DEEP South（Kayl）、LuxConnect DC1.1/DC2、Portus；PoP 存在≠总容量或全部商业服务。
5. **Google Bissen 是活跃管线**：33.7 ha 用地改划（2019 DCD）、PAP 实施协议完成（RTL 2025）、2025-08 中旬提交建设许可申请（RTL 2025-11-18，尚未获批、项目缩小、风冷）；状态按 `PAG/PAP/permit application/EIE/commodo/construction` 记录日期与来源；无许可/开工证据不标 under construction。
6. **多语必搜**：法语 `centre de données`、`autorisation de construire`、`établissement classé`、`commodo/incommodo`、`raccordement électrique`；德语 `Rechenzentrum`、`Baugenehmigung`、`Umspannwerk`、`Betriebsgenehmigung`；卢森堡语 `Rechenzenter`、`Baugenehmegung`、`Gemengebuet`；英语兜底。
7. **无超规模云区域**：官方页负面（最近 AWS 区域通常法兰克福 eu-central-1）；客户可用区措辞不推断 LU 区域；OVH 官方 datacentre 页 ≠ 云区域。
8. **旧名/新名并用**：EBRC→DEEP、EDH→Portus、Telindus→Proximus NXT、Datacenter Luxembourg→LuxNetwork；目录可能含别名/退役设施/所有权滞后。

## 查询模式（复制粘贴模板见 explorer-official.md §4 / explorer-industry.md §7）

- 许可/规划：`"{commune}" ("centre de donnees" OR datacenter OR Rechenzentrum) ("autorisation de construire" OR "autorisation de batir" OR "permis de construire")`、`site:{commune-domain} (PAG OR PAP OR autorisation OR permis OR commodo) (Google OR LuxConnect OR DEEP OR EBRC OR OVHcloud OR SecureIT OR DATA4)`、`filetype:pdf Luxembourg ("centre de donnees" OR datacenter OR Rechenzentrum) (PAP OR PAG OR commodo OR EIE)`。
- 能源：`site:creos-net.lu ("data center" OR "centre de donnees" OR Rechenzentrum)`、`site:creos-net.lu (raccordement OR Netzanschluss OR Anschlussleistung OR MVA)`、`"{operator}" "{commune}" (MW OR MVA OR Creos OR poste OR transformateur)`。
- 运营商/地址：`site:luxconnect.lu infrastructure`、`"202 Z.A.E. Wolser F"`、`"3 op der Poukewiss"`、`"DEEP Resilience Center Luxembourg West" OR East OR South`、`"9 rue Robert Stumper"`、`site:ovhcloud.com/en/datacenter/europe/luxembourg`。
- 云：`site:aws.amazon.com/about-aws/global-infrastructure Luxembourg`、`site:cloud.google.com/about/locations Luxembourg`、`"Google" "Bissen" ("building permit" OR PAP OR EIE OR commodo OR "permis de construire")`。
- 采购/法律/注册：`site:marches.public.lu ("centre de donnees" OR "data center" OR colocation OR Rechenzentrum OR cloud OR HPC)`、`site:legilux.public.lu ("centre de donnees" OR datacenter)`、`site:lbr.lu ("Data Center" OR Datacenter OR LuxConnect OR SecureIT OR Portus OR DATA4)`。
- 媒体/目录：`site:datacenterdynamics.com Luxembourg (Google OR LuxConnect OR Bissen OR Bettembourg)`、`site:paperjam.lu OR site:delano.lu OR site:itnation.lu Luxembourg (datacenter OR "data center")`、`site:lu-cix.lu/infrastructure/network-map Luxembourg`。

## 官方/监管管线要点（详见 explorer-official.md）

- 入口：Guichet.lu（建设许可程序 A）→ 市镇许可面（优先 bettembourg/bissen/vdl/koerich/kayl/betzdorf/contern/mersch/sanem/roeser/leudelange/strassen/dudelange/esch）→ Legilux/公报 → LBR（法人/所有权）→ marches.public.lu（colo/HPC/云/DC 建设/备用站点）→ 环境（environnement.public.lu、AEV，EIE/commodo）→ 电网（Creos/ILR）。
- 证据尺度：仅签发许可、营业许可、带地址运营商页或物理存在设施计正记录；无设施 canton 须记录所搜 commune 的负面注释。
- Google Bissen：逐阶段记录（用地改划→PAP 实施协议→许可申请→EIE/commodo→施工）；未获批前为管线。
- 验证规则：勿从目录计数推断权威设施总数；LBR 用于法人/所有权主张；目录所有权历史未经确认不采用。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商 pivot：LuxConnect（DC1.x/DC2，A 容量/地址）、DEEP（DEEP West/East/South，LU-CIX A/B）、OVHcloud（A 官方页，Bissen 精确地址 B/C）、SecureIT（DCC City/DCB Bettembourg/DCR Bissen，C/B）、Portus（A 存在，地址别名经 LBR/市镇对账）、BCE（A/B PoP/colo 线索）、Visual Online（B，Contern）、C2D（C，Windhof）、Datacenter Luxembourg/LuxNetwork（404 旧 URL→用 luxnetwork.eu + LBR）、LuxProvide/MeluXina（HPC 锚负荷）、Verizon 旧条目（退役/未验证）。
- 媒体/协会：ICT Luxembourg、Luxinnovation、FEDIL（B）、Cloud Community Europe Luxembourg（B/C）、DCD（B）、Paperjam、Delano、ITnation、Luxembourg Times、RTL Today（B）、Chronicle.lu（B/C）；目录（C）：DataCenterMap、Baxtel、DataCenterJournal、Datacenters.com、PeeringDB（B/C 交叉验证）。
- 去重：SecureIT 三址、Portus/EDH 别名、LuxConnect 两校区、Google Bissen 与 OVH Bissen 线索分开；所有权交易扫（SecureIT/Colony/Genii、EDH/Portus/Arcus、Proximus 出售、POST-DEEP 合并 2024-12-31）。
- 状态语言：`MoU/plan/will build/exploring`=规划；`permit issued/PAP adopted`=许可/规划阶段；`construction started`=在建（须验证日期与地点）；`inaugurated/operational/certified constructed facility`=运营。

## 已知设施/项目与证据状态

| 设施/项目 | Canton/Commune | 状态与证据 |
|---|---|---|
| LuxConnect DC1.1/1.2/1.3 | Esch-sur-Alzette/Bettembourg（202 Z.A.E. Wolser F） | 运营（A 官方页，MVA/面积）；扩展须现许可 |
| LuxConnect DC2 | Mersch/Bissen（3 op der Poukewiss） | 运营（A 官方页） |
| DEEP West / East / South（前 EBRC） | Capellen-Windhof / Grevenmacher-Betzdorf / Esch-sur-Alzette-Kayl | 运营/品牌（LU-CIX A/B + DEEP 官方页） |
| OVHcloud Luxembourg datacentre | Mersch/Bissen（媒体指向） | A 官方页存在；Bissen 精确映射 B/C |
| Portus Data Centers（前 EDH） | Luxembourg（9 rue Robert Stumper 别名） | A 当前官方页；地下 Tier IV + 1 MW 扩展声称；别名对账中 |
| SecureIT DCC/DCB/DCR | Luxembourg/Bettembourg/Bissen | C/B 线索；运营商页/LBR/许可确认前不计数 |
| BCE（Broadcasting Center Europe） | Luxembourg（43 bd Pierre Frieden） | A/B PoP/colo 线索 |
| LuxProvide MeluXina | Mersch/Bissen | A HPC 锚负荷；非公共 colo |
| Google Bissen 数据中心 | Mersch/Bissen | 管线（B：2019 改划、2025 PAP、2025-08 许可申请未批）；非运营、非 GCP 区域 |

## 更新节奏

- 每批次：云区域负面核查、Google Bissen（bissen.lu/AEV/EIE/RTL/Paperjam/DCD/Creos）状态、LuxConnect 扩展许可、SecureIT 三址、Portus 别名。
- 季度：12 canton 负面扫回顾（尤其 Clervaux/Diekirch/Echternach/Redange/Remich/Vianden/Wiltz）、所有权交易（DEEP/POST、SecureIT、Portus/EDH）、目录别名对账。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（12 canton 粒度）；本 skill 作为国家层参考注入。
