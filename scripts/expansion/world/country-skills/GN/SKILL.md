---
name: gn-datacenter-methodology
location: scripts/expansion/world/country-skills/GN/SKILL.md
description: 几内亚（Guinea）数据中心发现与审计方法论：官方/监管/云管线（总统府、政府门户/MPTEN、ARPT 电信监管局、ANSSI 网络安全局、GUILAB 官方页、WARDIP/World Bank、CNT/Journal Officiel、官方云区域列表）叠加行业/厂商发现（行业媒体、运营商页、供应商页、目录、IX/对等记录、矿业部门 IT、本地媒体）；以清单中的 8 个分区（Boke、Conakry、Kindia、Faranah、Kankan、Labe、Mamou、Nzerekore）为工作模型，法语/本地拼写作别名。运行 GN 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。Bilingual discovery & audit methodology for Guinea datacenters: official/regulatory/cloud pipeline + industry/trade-press discovery, at the 8-division working model from the manifest (French/local spellings as aliases); read before running GN exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# GN · 几内亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：几内亚处于过渡期国家背景，部委名称与数字事务组合自 2021 年起多变——按物理站点归属设施而非文章中的部委名。已核实的高置信种子集中在 Conakry：**GUILAB** 运营商公布的 Kipe 发射中心数据中心/托管/云服务，与 **Data Center National**（2025-09 与 `.gn` 域名一同启用/投入服务，位于 ARPT 大楼 Kipe/Koloma/Ratoma 一带）。Conakry 之外无已核实的商业托管设施——矿业/工业 IT、电信 PoP 与公共行政机房按 C 级线索处理。运行任何 GN 探索/审计批次前必须阅读本 skill，并按需路由到两份探索报告。

## 入口（Entry points）

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | 总统府（国家 DC/`.gn` 启用）、政府门户/MPTEN、ARPT、ANSSI、GUILAB、WARDIP/世行、CNT、Journal Officiel/SGG、IXP-GUINEE/PeeringDB、官方云区域列表、EDG/能源部、官方搜索模板、已验证种子表、监管与许可逻辑、8 分区覆盖策略、云负向检查、最低记录标准 |
| explorer-industry.md | 行业/厂商发现 | 行业来源分诊表、贸易/运营商查询块、运营商与项目种子（GUILAB、Data Center National、ACE 登陆站、IXP-GUINEE、Orange/MTN/Cellcom/Guinee Telecom/MOUNA/Leadernet、银行、矿业 IT）、逐地区行业策略、云/CDN/边缘处理、证据升级规则、常见陷阱、推荐发现顺序 |

## 核心结构事实（框定每次搜索）

1. **划分模型**：按清单的 **8 分区工作模型**：**Boke；Conakry；Kindia；Faranah；Kankan；Labe；Mamou；Nzerekore**（对应七行政区 + Conakry 特区/省）。记录归属用 ASCII 清单名，法语/本地拼写作别名（Boké；Nzérékoré/N'Zérékoré；Labé；Kérouané 等）。
2. **核心设施/项目集**：**GUILAB Data Center / 托管 / 私有云**（Conakry/Ratoma/Centre Emetteur de Kipe；官方页：228.91 m2、Pylone/Meet-Me Room/COLOC 房间、MMR 与 COLOC 间两条 96 纤链路、公共电网 + 2 x 400 kVA 发电机、72 小时电池、ASHRAE 温度范围、精密制冷 1+1、FM200 灭火、门禁、24/7/365——**A 级运营商声明**；未知：机架数、IT 负荷/MW、精确坐标、启用日期、租户、ISO 9001 之外的认证——ISO 9001 是 GUILAB 运营认证非 Tier/Uptime）；**Data Center National / 国家数据中心 / `.gn` 启用**（Conakry/ARPT 大楼 Kipe/Koloma；总统府 A 级启用/投入服务事件；600 m2 与 Tier III 措辞为 B 级；状态 inaugurated/mise en service，规模化运营按部分/过渡处理；未知：法定运营方、业主、资金来源、机架/MW、Uptime 证书、生产割接、客户/负载列表）；**`.gn`/NIC.GN 注册表负载**（不单独立设施，仅当来源证明物理托管于国家 DC 才作为工作负载/上下文附加）；**IXP-GUINEE**（Conakry；PeeringDB ix/2520，4 peers/4 connections/3G 容量——互联对象与发现枢轴，非 DC）；**ACE 登陆站 / GUILAB 基础设施**（Kipe/Ratoma；登陆站职能与 GUILAB 数据中心服务分离，Kipe 场地去重）。
3. **关键机构**：总统府（presidence.gov.gn）、政府门户/MPTEN（gouvernement.gov.gn、service-public.gov.gn/mpten）、ARPT（arpt.gov.gn，总部 Centre Directionnel de Koloma；执照/互联/市场文件——牌照非数据中心证明）、ANSSI（anssi.gov.gn，Loi L/2016/037/AN 网络与个人数据法；APDP 个人数据局在 CNT 审查中）、GUILAB（La Guinéenne de Large Bande SA，guilab.com.gn）、WARDIP/World Bank（wardip-guinee.org.gn）、CNT（cnt.gov.gn，LFI 2025 预算）、Journal Officiel/SGG、EDG/能源部（电力单独定级）、IXP-GUINEE/PeeringDB/PCH。
4. **查询语言与拼写**：法语为主（datacenter、"data center"、"centre de données"、colocation/colocalisation、hébergement、cloud、MMR、COLOC、"salle serveur"、"point de presence"、"groupe électrogène"、"poste électrique"、kVA/MVA、"appel d'offres"、"marché"）+ 英语；分区与首都别名（Kipe/Kipé、Koloma、Ratoma 等）。
5. **容量语义**：字段级定级——同一设施可有 A 级存在与位置但 B/C 级容量、认证或运营状态；目录 MW/机架/sqm/Tier/坐标保持 C 直至运营商/官方许可/采购/公用事业/工程来源确认；不为 cybercafes、网页托管转售、大学实验室、普通银行 IT 机房、铁塔站点、登陆站、光纤线路、政府办公室、NOC、MSC 或矿业控制室建数据中心记录（除非来源证明托管/托管/云/算力功能）。
6. **电力**：GUILAB 官方页：公共电网、2 x 400 kVA 发电机、72 小时电池、精密制冷 1+1（A 运营商声明）；国家 DC 的能源冗余与 Le360 报道的两路市电 + 发电机保持 B 直至官方工程证据。
7. **云区域负向检查（已核查 2026-08-12）**：AWS/Azure/GCP/OCI 官方区域/本地区域列表无几内亚区域；CDN 缓存、客户、经销商、市场或 Outposts/私有云部署不暗示几内亚超大规模数据中心；从法国/塞内加尔/科特迪瓦等地向几内亚销售的网页托管为离岸，除非具名并证明几内亚站点。
8. **可靠度分级**：A = 一手（总统府、部委/机构、ARPT、ANSSI、GUILAB、WARDIP、世行、Journal Officiel/SGG、CNT、EDG/部委电力记录、官方云区域列表、PeeringDB/PCH 互联事实）；B = 强二级（DCD、Agence Ecofin、Connecting Africa、TechAfrica News、Le360 Afrique、Guineematin、Mediaguinee、Guineenews、Guineeactuelle、AGP、Radio Guinee、Avenirguinee、GuineeSource 等具名官方事件/文本转述）；C = 目录/市场、片段、社交、招聘帖、付费市场报告、MoU、不可验证抓取页、转售网页托管、或 NOC/服务器机房/登陆站无托管/托管/云/算力功能的措辞。
9. **陷阱**：FratMat 的 `construction-du-data-center-national...24-mois` 文章是科特迪瓦的，勿用于 GN；GUILAB ISO 9001 ≠ 数据中心 Tier；国家 DC "Tier III" 无 Uptime/工程/官方证书证据不视为独立认证；矿业线索归属前验证省/区（Simandou 南部/Beyla = Nzerekore；Kérouané = Kankan；Lefa/Lélouma 需当前矿业文件确认）；按物理站点归属分区而非文章范围或公司总部。

## 常用查询模板（详见 explorer-official.md / explorer-industry.md）

```text
site:presidence.gov.gn ("data center" OR datacenter OR "centre de données" OR ".gn" OR "mise en service" OR Simandou)
site:gouvernement.gov.gn (MPTEN OR "Télécommunications" OR numérique OR WARDIP OR "data center" OR ".gn")
site:www.arpt.gov.gn (operateur OR licence OR interconnexion OR "catalogue" OR "data center")
site:anssi.gov.gn (WARDIP OR CERT OR "protection des données" OR "data center" OR cloud OR hébergement)
site:guilab.com.gn ("Data Center" OR Colocation OR Colocalisation OR Cloud OR MMR OR COLOC OR Kipe OR kVA OR ASHRAE OR FM200)
site:cnt.gov.gn (datacenter OR "data center" OR "centre de données" OR MPTEN OR WARDIP OR APDP OR budget)
site:wardip-guinee.org.gn (datacenter OR "data center" OR cable OR backbone OR fibre OR CERT OR cloud)
site:journal-officiel.sgg.gov.gn (télécommunications OR numérique OR cybersécurité OR "protection des données" OR électricité)
"{operator}" Guinée (datacenter OR "data center" OR "centre de données" OR colocation OR colocalisation OR cloud OR hébergement OR MMR OR COLOC)
"{division}" Guinée (datacenter OR "data center" OR "centre de données" OR colocation OR hébergement OR cloud)
Conakry Guinée (datacenter OR "data center" OR "centre de données" OR ARPT OR GUILAB OR IXP-GUINEE OR "data center national")
(Boké OR Boke OR Kamsar OR Sangarédi) Guinée (datacenter OR "centre de données" OR colocation OR PoP OR SCADA OR CBG OR GAC)
(Nzérékoré OR Nzerekore OR Beyla) Guinée (datacenter OR "centre de données" OR colocation OR PoP OR Simfer OR Simandou)
"Guinée" ("AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "Oracle Cloud region")  # 云排除
site:datacenterdynamics.com/en/news/ (Guinea OR Guinée) (datacenter OR "data center" OR telecom OR Sotelgui)
```

## 官方/监管管线要点（详见 explorer-official.md）

- 总统府：国家 DC 与 `.gn` 启用/投入服务为 A 级事件与政策框架（Simandou 2040 主权叙事）；不证明 sqm/机架/MW/Uptime 认证/法定运营方/详细电力设计。
- ARPT：构建运营商宇宙（Orange Guinee、MTN Guinee、Cellcom、Guinee Telecom/Sotelgui、MOUNA、Leader Net、VDC Telecom）；执照、铁塔、NOC、MSC、光纤 PoP ≠ 数据中心。
- ANSSI：Loi L/2016/037/AN 与主权/本地化压力背景；APDP 为监管上下文非设施证明。
- 采购/预算：搜索 CNT、WARDIP、Journal Officiel 与官方采购门户的 `appel d'offres`、`attribution`、`marché`、`hébergement`、`cloud gouvernemental`、`groupe électrogène`、`climatisation de précision`。
- 环境/建筑许可：Conakry 市镇许可与 EIES 索引差；按市镇/街区 + 承包商/供应商 + 电力/制冷术语搜索。
- 云负向：仅用官方供应商区域页记录缺席。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 先建 Conakry 记录（GUILAB、Data Center National、ACE 登陆站、IXP-GUINEE、ARPT、ANSSI、Orange、MTN、Cellcom、Guinee Telecom、MOUNA、Leadernet、银行）；每个种子搜索 运营方 + 地址 + ARPT/CNT/Journal Officiel/WARDIP/EDG/PeeringDB/采购/电力 术语。
- 用官方 GUILAB 页先于目录；目录仅用于找候选名或陈旧别名（DataCenterMap 对 curl 429——目录值不得覆盖 GUILAB 官方页）。
- 证据升级：公告/MoU C 或 B（视来源），无服务/启用/调试/客户证据绝不 operational；施工/采购 A/B 当官方采购/CNT/WARDIP/部委/运营方/公用事业/承包商记录指明站点与工程；运营 A/B 当运营方服务页、官方 mise en service、客户条款、设施照片/规格、PeeringDB 设施关联、公用事业通电或经审计申报存在。
- 去重：GUILAB DC、ACE 登陆站与 IXP 相关设备可能共享 Kipe 场地；国家 DC 在/近 ARPT Kipe/Koloma 可能托管 `.gn` 或国家云负载；不得把工作负载拆成额外设施。
- 矿业枢轴：CBG/GAC/SMB-Winning/RUSAL（Boke、Kindia）、AngloGold Siguiri/Nordgold Bouly/Simandou-WCS Kérouané（Kankan）、Lefa/Nordgold（Labe）、Simfer Beyla（Nzerekore）——控制室/SCADA/营地 IT 无具名设施/托管证据不计数。

## 维护注意（更新纪律）

- **更新节奏**：每次刷新重查官方云区域/本地区域列表、总统府/政府门户/MPTEN 组合、ARPT 目录、GUILAB 官方页、WARDIP/世行、CNT 法案与预算、Journal Officiel；跟踪国家 DC 生产割接/客户列表/法定运营方、`.gn` IANA 记录、Medusa/第二海缆（2026 MoU 2026-05-06）与 APDP 机构进展。
- **来源核验**：INSTAT 主页 2026-08-12 curl 返回 403 勿直接引用；agenceecofin 部分页对 curl 403 但已索引；GuineeSource curl 406 但浏览器/搜索可取；部委虚荣域名不可达时用政府/service-public 镜像；旧部委名称组合变化——定 A 前在政府门户验证当前组合。
- **不删除纪律**：无法核实的旧线索保留为降级线索并注明缺失证据；每条候选记录必须携带规范名与别名、所有者/运营方/法定实体、8 分区清单名归属、Conakry 市镇/街区、位置/地址/坐标（可源化时）、状态、功能、设施/设备容量（逐字段等级）、电力证据、来源 URL、去重说明。
