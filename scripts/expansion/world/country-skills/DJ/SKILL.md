---
name: dj-datacenter-methodology
location: scripts/expansion/world/country-skills/DJ/SKILL.md
description: 吉布提（Djibouti）数据中心发现与审计方法论：官方/监管/云管线（ARMD 多部门监管局、Journal Officiel、MDENI/ANSIE 政府 ICT、DPFZA/DIFTZ 自由区、EdD 电力、FSD 主权基金、官方云区域排除）叠加行业/厂商发现（Wingu/DDC、Wingu TO7、Djibouti Telecom 海缆与托管、AMS-IX/DjIX、PAIX JIB1、目录）；以清单中的 6 个地区/城市（Arta、Ali Sabieh、Dikhil、Djibouti、Obock、Tadjourah）为划分粒度，设施证据集中于 Djibouti 市。运行 DJ 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。Bilingual discovery & audit methodology for Djibouti datacenters: official/regulatory/cloud pipeline + industry/trade-press discovery, at the 6 region/city division granularity from the manifest; read before running DJ exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# DJ · 吉布提数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：吉布提没有公开的国家数据中心登记册，也无公开可检索的施工/EIA 门户——登记册缺席不等于活动缺席。本方法论通过官方/监管/云管线（explorer-official.md）与行业/厂商发现（explorer-industry.md）双通道枚举商业、电信、政府、企业与管线数据中心设施，并规定：一次运行必须覆盖全部 6 个划分地区，否则须对每个负向地区输出 `no_projects: true` 并附查询/日期说明。运行任何 DJ 探索/审计批次前必须阅读本 skill，并按需路由到两份探索报告。

## 入口（Entry points）

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | ARMD 多部门监管局、政府数字/公共部门 ICT（MDENI/ANSIE/egouv）、数据保护与法律（Journal Officiel）、电力/电网（EdD/IRENA）、环境规划与自由区（DPFZA/DIFTZ）、投资与主权基金（FSD/PAIX）、官方云区域排除、6 地区覆盖图与验证配方 |
| explorer-industry.md | 行业/厂商发现 | 设施/项目普查种子（Wingu/DDC、Wingu TO7、PAIX JIB1、Djibouti Telecom、ANSIE、AMS-IX/DjIX）、运营商与生命周期查询、海缆/IXP 证据、行业媒体监控、目录与聚合器、云厂商状态、行业机构/认证、常见误报清单 |

## 核心结构事实（框定每次搜索）

1. **划分模型**：清单为 **6 个地区/城市**（region/city）：**Arta、Ali Sabieh、Dikhil、Djibouti、Obock、Tadjourah**。已确认/强来源的商业设施证据几乎全部集中在 **Djibouti** 分区（Djibouti 市）；其余 5 个地区预期为商业托管负向，但标记负向前必须搜索政府/电信机房、港口 ICT、海关 ICT、海缆/光缆小屋与电力项目。
2. **核心设施集**（Djibouti 分区）：**Wingu / Djibouti Data Center (DDC)**（2013 年开业的老运营商中立托管设施，别名 Djibouti Data Center SARL / Wingu Africa Djibouti 1，目录约 1 MW 仅为 C 级）；**Wingu TO7 Technology Park 数据中心 + 运营商中立 CLS**（2024-11 启用，设计容量约 3 MW——作为 announced/design 容量，"Tier 3" 为运营商/媒体措辞，无 Uptime 记录前不得升级）；**Djibouti Telecom 海缆登陆与数据中心/托管基础设施**（仅当来源明确数据中心/托管/服务器措辞才计入设施；旧路径 international.djiboutitelecom.dj/data-centre-colocation/ 已 404，勿再用）；**PAIX JIB1 / PAIX Djibouti**（与 FSD 主权基金合作，公布最高 5 MW、首期目标 2026——状态不超过 announced/planned，用 `announced_capacity_mw`）；**AMS-IX Djibouti / DjIX**（2024 起运行的 IXP，托管于 DDC——IXP 上下文而非独立数据中心）；**ANSIE 国家数据中心托管服务**（总统府 2023-11-14 部长会议关税法令摘要提及——政府托管上下文，未点名物理站点/运营方，不单独立设施）。
3. **关键机构**：ARMD（多部门监管局，Loi n°074/AN/20/8ème L 设立，实施法令 N°2022-047/PRE；发放授权/执照/特许、频谱管理；非数据中心许可登记处）、Journal Officiel（journalofficiel.dj）、MDENI（numerique.gouv.dj，间歇性不可达）、ANSIE（ansie.dj，间歇性不可达）、egouv.dj、DPFZA/DIFTZ（土地/投资/自由区线索）、Electricité de Djibouti（EdD，电力）、FSD（主权基金）。法律锚点：Loi n°100/AN/19 个人数据保护、Loi n°18/AN/23/9ème L 批准非盟马拉博公约、Code du Numerique（引用前须核验 Journal Officiel 文本）。
4. **查询语言与别名**：法语产出最高（"centre de données"、"centre d'hébergement"、"hébergement"、"colocation"、"salle serveur"、"station d'atterrissement"、"câble sous-marin"、"etude d'impact"）+ 英语（多数运营商以英文发布）。必用别名：data center/centre/datacenter、CLS、Haramous、Boulaos、Siesta、Ras Dika、PK12、PK23、DIFTZ、TO7、PAIX、JIB1、Rue de Geneve。
5. **容量语义**：电力昂贵且电网供给受限，大型 MW 主张需额外怀疑——公告设计 MW 不得换算为运营 IT 负荷，需调试/并网/电力证据；`capacity_mw: null` 除非来源明确给出，管线项目用 `announced_capacity_mw`。
6. **生命周期阶梯**：rumour < MoU < announced < land acquired < permit applied < permit granted < construction started < commissioned/inaugurated < operational；逐条按其所在阶梯编码状态。
7. **云区域排除**：截至 2026-08-12，AWS/Azure/GCP/Oracle 官方页面均无吉布提区域；海缆联盟参与、CDN/缓存节点、PoP、云交换产品、经销商页面均不得构造云区域设施；每次批次重查官方页面。
8. **可靠度分级**：A = 一手/官方（ARMD 页面与法律、Journal Officiel、部委/机构页面、Djibouti Telecom 官方页、FSD/DPFZA/DIFTZ 官方公告、官方海缆/运营商页、Uptime 奖页、官方云区域页）；A- = 官方运营商/投资人公告证明具名项目或运营主张但无许可/监管申报；B = 强二级（DCD、SDxCentral、SubTel Forum、Capacity/Connecting Africa、African Business、Agence Ecofin、ADI/La Nation/RTD 报道事件时）；C = 仅发现线索（目录、市场报告、SEO 页、社交、聚合容量表）。按具体主张分别定级：同一站点可存在 A-、B、C 并存。
9. **别名去重**：DDC = Djibouti Data Center = Djibouti Data Center SARL = Wingu Africa Djibouti 1（同一老设施）；Wingu TO7 = TO7 Technology Park = "second carrier-neutral data center"（新设施，可凭 TO7/CLS 措辞区分）；PAIX JIB1 = PAIX Djibouti = PAIX/FSD 项目；DjIX = AMS-IX Djibouti（同一 IXP 品牌过渡）。

## 常用查询模板（详见 explorer-official.md / explorer-industry.md）

```text
site:armd.dj "data center" OR "centre de donnees" OR colocation
site:journalofficiel.dj "Loi n°074/AN/20" OR "Autorite de Regulation Multisectorielle"
site:ansie.dj "data center" OR "centre de donnees" OR hebergement OR "salle serveur"
site:presidence.dj ANSIE "centre de donnees" OR DATA CENTER
site:diftz.dj "data center" OR "centre de donnees" OR ICT
site:dpfza.gov.dj "data center" OR "centre de donnees" OR technologie
"Wingu" Djibouti "TO7" OR "Technology Park" OR "carrier-neutral" OR "CLS" OR "3 MW"
site:wingu.africa Djibouti "data centre" OR colocation OR "TO7"
"PAIX" Djibouti JIB1 OR "5MW" OR "Sovereign Fund"
"Djibouti Telecom" "data centre" OR colocation OR "cable landing station"
site:ams-ix.net Djibouti OR "Djibouti Internet Exchange"
"{division}" Djibouti "data center" OR "centre de donnees" OR "salle serveur"   # 6 分区通用扫描
"Djibouti" "AWS region" OR "Azure region" OR "Google Cloud region" OR "Oracle Cloud region"  # 云排除
```

## 官方/监管管线要点（详见 explorer-official.md）

- ARMD 界定电信/ICT 持牌运营商宇宙并管理频谱/互联/能源监管；从牌照转向设施。
- MDENI/World Bank 数字经济诊断是政策/需求上下文，非设施登记册。
- 数据保护法律（Loi 100/AN/19、马拉博公约）是需求与合规上下文；仅当来源指明托管位置/运营方/受监管处理设施才构成设施记录。
- 电力：EdD/能源部/ARMD/捐赠文件用于可行性、电价、互联与大户证据；埃塞-吉布提互联与地热文件是供电上下文，不单独证明数据中心。
- 规划/环境：无公开 EIA 数据库或城市施工许可门户；DPFZA/DIFTZ 是土地/投资/自由区线索，DIFTZ 本身不得计为数据中心；围绕 Haramous、Boulaos、Siesta、Ras Dika、PK12、PK23/DIFTZ、Rue de Geneve、TO7 搜索土地/项目术语。
- 投资：FSD/DPFZA/DIFTZ/Journal Officiel；PAIX JIB1 状态不超过 announced/planned，直至出现施工或启用证据。
- 云排除：每次批次重查 AWS/Azure/GCP/Oracle 官方区域页。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 从运营商/一手源播种（Wingu、Djibouti Telecom、AMS-IX/PeeringDB、PAIX/FSD、官方海缆公告），再按"运营商/官方页 → 监管/法律记录 → 投资/土地 → 电力 → 环境/规划 → 行业媒体 → 目录"顺序寻求证据。
- 目录（Baxtel、DataCenterMap、DataCenters.com、Cloudscene、OCOLO）仅用于别名/地址/邻近设施检查；目录 MW/机架/面积字段保持 claimed_* 或注释，聚合器国家计数不稳定，绝不用作普查。
- 海缆/IXP：2Africa（2022-05 随 Djibouti Telecom 登陆）、DARE1、PEACE、IEX/Africa-1 为连接性证据；仅当来源说明建筑含托管/数据中心空间才从 CLS 建记录。
- 误报清单：DIFTZ 营销、海缆、PoP/edge/CDN/云交换公告、DjIX 单列、目录别名多重计数、PAIX 5 MW 提前运营化、无 Uptime 记录的 "Tier 3" 升级、目录容量当官方、吉布提市外电信机房当商业托管。

## 维护注意（更新纪律）

- **更新节奏**：每次批次重跑云区域排除与 6 分区负向检查；核对 ARMD/Journal Officiel/Wingu/Djibouti Telecom 官方页与 DCD/SDxCentral/SubTel 新闻。
- **来源核验**：numerique.gouv.dj 与 ansie.dj 间歇性不可达但为官方索引域名，交互验证后再把"无搜索结果"当负向证据；DCD/SDxCentral/African Business/Capacity 等对 curl/HEAD 可能返回 403/429，但真实可检索；旧 Djibouti Telecom /data-centre-colocation/ 路径已 404。
- **不删除纪律**：无法核实的旧线索保留为降级线索并注明缺失证据；ANSIE 国家数据中心不单独立设施直至来源指明站点/运营方/地址；每条记录拆分 status、division、operator、developer、SPV、address、capacity_mw、announced_capacity_mw、racks、tier_certification、source_urls、evidence_date、evidence_grade 字段。
