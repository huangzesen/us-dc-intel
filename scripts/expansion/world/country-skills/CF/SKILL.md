---
name: cf-datacenter-methodology
location: scripts/expansion/world/country-skills/CF/SKILL.md
description: |
  Central African Republic (CF) parent-level methodology for data-center enumeration at division
  granularity (17 manifest divisions; current administration is 20 prefectures + Bangui after the
  2020/2021 reform - normalize to manifest names, keep current locality in notes). CAR has a very thin
  data-centre market with no verified operational commercial colo; Bangui is the high-yield city.
  Enumeration joins ARCEP licensing (80 TB PGNSP monitoring platform = institutional compute, not a DC),
  government portal gouv.cf, AfDB CAB-CAR national datacentre + Digital Training Centre lead, GreenLine/
  SOCATEL Tier 3 plan (USD 150M, MoU 2025-09, operational-phase launch 2026-07, still planned), Huawei
  Tier III government lead, Cybastion 2021 signing (stale), ECCAS/PIDA regional plan, Orange Centrafrique
  Bangui core (2021 fire, telco facility), IANA .cf/SOCATEL registry, energy (Boali/ENERCA), and donors
  (World Bank PGNSP P174620 USD 35M). No hyperscaler region; Starlink is connectivity only. Routes to
  explorer-official.md (regulator/government/donor pipeline) and explorer-industry.md (press/operator/
  directory pipeline).
---

# CF · 中非共和国数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：中非共和国数据中心市场极薄，无已核实的运营中商业 colo；班吉（Bangui）是高产区城市。枚举必须拼接 ARCEP 许可（PGNSP 监测平台 80 TB = 机构计算，非 DC）、政府门户 gouv.cf、AfDB CAB-RCA 国家数据中心 + 数字培训中心线索、GreenLine/SOCATEL Tier 3 计划（1.5 亿美元，2025-09 MoU，2026-07 运营阶段启动，仍为 planned）、Huawei Tier III 政府线索、Cybastion 2021 签署（已陈旧）、ECCAS/PIDA 区域计划、Orange Centrafrique 班吉核心（2021 火灾，电信设施）、IANA .cf/SOCATEL 注册局、能源（Boali/ENERCA）与捐助者（世行 PGNSP P174620，3,500 万美元）。无超大规模区域；Starlink 仅为连通性。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供中非共和国探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：ARCEP、gouv.cf/部委域、AfDB/CAB-CAR、SOCATEL/IANA/.cf、世行 PGNSP、Huawei/Cybastion/ECCAS-PIDA、ENERCA 能源、云区域阴性对照、候选处理表、17 区矩阵 |
| `explorer-industry.md` | 行业管线：行业/本地媒体（Agence Ecofin/Radio Ndeke Luka/Digital Business Africa 等）、运营商/厂商扫库、目录处理、逐区矩阵、分级范例 |

## 核心结构事实（框定每次搜索）

1. **17 区清单模型**：Ouham, Bamingui-Bangoran, Bangui, Basse-Kotto, Haute-Kotto, Haut-Mbomou, Haute-Sangha/Mambere-Kadei, Gribingui, Kemo-Gribingui, Lobaye, Mbomou, Ombella-Mpoko, Nana-Mambere, Ouham-Pende, Sangha, Ouaka, Vakaga；现行行政为 2020/21 改革后的 20 省 + Bangui——归一化到清单名，现行名放 notes；映射：Haute-Sangha/Mambere-Kadei = 现行 Mambere-Kadei/Berberati 走廊，Sangha = Sangha-Mbaere，Kemo-Gribingui = Kemo/Nana-Grebizi 旧区，Gribingui = Nana-Grebizi 区。
2. **班吉主导**：已确认与候选 DC/机房证据在 Bangui 或可默认 Bangui 的无地点国家项目（仅当来源语境支持）；班吉以外预期为光纤、电力、行政或电信节点背景。
3. **公开 DC 项目线索多、已验证运营设施少**：最强官方线索为 AfDB/CAB-CAR 组件（MapAfrica 文本描述班吉城市环网含国家数据中心与数字培训中心）；其他线索：GreenLine/SOCATEL Tier 3、Huawei/政府 Tier III、Cybastion 政府数据中心、ECCAS/PIDA 区域数据中心计划、Orange Centrafrique 班吉核心/数据中心设施、ARCEP 80 TB 监测平台。
4. **区分数据中心与机构计算**：ARCEP 80 TB 网络监测平台（世行博客 2025-10-28，2024-04 在 ARCEP 总部启用，A 机构计算，非 DC）、SOCATEL .cf 注册局基础设施、部委服务器机房、银行服务器机房、移动运营商核心站点均证明本地计算，除非来源明确说 `data center`/`datacenter`/`centre de donnees`，否则不是商业 colo 或国家 DC 项目。
5. **GreenLine/SOCATEL Tier 3 为 planned**：GreenLine 官方 2025-09-18 公告获 SOCATEL 私有化/振兴/转型授权（卡萨布兰卡 MoU），含新 Tier 3 数据中心与 1.5 亿美元初期投资（A 厂商自述）；2026 年媒体报道 2026-07-16 在班吉启动运营阶段（B 政府阶段细节）；无站点地址/机架/MW/认证/施工许可。
6. **无商业 colo 市场**：截至 2026-08-12 无已核实的载波中立商业 colo；多数记录为政府、电信、规划或机构性质。
7. **无超大规模区域**：AWS/Azure/GCP/OCI 官方列表无 CF 公共区域（A 阴性对照）；`Tier 3/Tier III` 声明在 Uptime 或具名认证机构确认前为自述/设计目标。
8. **语言**：法语为主（centre de donnees、centre national de donnees、salle serveur、hebergement、cloud souverain、fibre optique、groupe electrogene、permis de construire、appel d'offres、agrement）；英文用于贸易媒体/云区域。
9. **电力是门控约束**：Bangui/Ombella-Mpoko 依赖 Boali 水电与柴油备用；无发电机组/UPS/电网互联/太阳能/变电站证据的 MW 级主张保持 `capacity_mw=null` 并加电力警示。
10. **连通性≠设施**：CAB-CAR 光纤骨干（AfDB+EU 共同出资）、Starlink（2025-12 批准后 2026-03 商业上线，DEVEAG-Centrafrique 本地管理）仅为连通性服务。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§3、explorer-industry.md §1/§2/§4/§5）

```text
site:arcep.cf agrement operateur OR "centre de donnees" OR cloud
"ARCEP" "Centrafrique" "80 terabytes" OR "80 TB"
site:gouv.cf "Projet Dorsale-Fibre Optique" "Composante RCA"
site:gouv.cf "centre de donnees" OR datacenter OR "centre national de donnees"
site:telecommunications.gouv.cf "centre de donnees" OR datacenter
site:mapafrica.afdb.org "46002-P-CF-GB0-002"
site:afdb.org "P-CF-GB0-002" OR "Composante RCA" "datacentre"
"Universite de Bangui" "datacentre" OR "Digital Training Centre"
"SOCATEL" "Greenline" "Tier 3" OR "Tier III" OR datacenter
"Greenline Technologies" "SOCATEL" "data center" OR "150 million"
site:socatel.cf datacenter OR "centre de donnees"
site:iana.org/domains/root/db/cf.html SOCATEL
site:documents.worldbank.org "P174620" "Central African Republic" "data center"
"PGNSP" Centrafrique "centre de donnees" OR datacenter OR hebergement
"Cybastion" "Central African Republic" "data centers"
"PIDA PAP2" "Central African Republic" "data centers"
"Orange Centrafrique" "data centre" OR "coeur de reseau" OR incendie
site:enerca-rca.com "centre de donnees" OR datacenter
"{prefecture}" "centre de donnees" Centrafrique
"{prefecture}" datacenter OR "data center" "Central African Republic"
"{prefecture}" "salle serveur" OR "salle informatique"
site:agenceecofin.com Centrafrique "data center" OR SOCATEL OR Huawei
site:radiondekeluka.org SOCATEL OR "Green Line" OR Starlink OR datacenter
site:digitalbusiness.africa Centrafrique Huawei OR Orange OR "Tier III"
site:datacenterdynamics.com "Central African Republic" Orange OR "data center"
"Centrafrique" "cloud souverain" OR "cloud national"
"Central African Republic" "Tier III" OR "Tier 3" "data center"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **ARCEP**（arcep.cf）：官方门户仍是施工占位页（联系 contact@arcep.cf，B.P. 1046 Bangui）——在线决策缺失 ≠ 缺失；用于运营商/agrement 许可、Starlink/卫星/云托管授权、市场统计、ARCEP 领导层官方访谈。
- **gouv.cf/部委域**：政府门户列 CAB-CAR 为主要在建项目（AfDB+EU 共同出资，经光纤接入喀麦隆与刚果）；部委域 telecommunications/modernisation/finances/plan/energies.gouv.cf；部长姓名需标注日期（Justin Gourna-Zacko 历史页 vs 2026 年 Roger Andjalandji）。
- **AfDB/CAB-CAR**（46002-P-CF-GB0-002）：班吉国家数据中心 + 数字培训中心的官方项目线索（A 项目纳入；阶段需按最新状态核实，无调试证据不得称运营；开发商 = 中非政府/AfDB/EU）。
- **SOCATEL/.cf**：IANA 列 SOCATEL 为 .cf ccTLD 管理者（Rue Guerillot, Bangui BP 939），技术联系人为阿姆斯特丹 Centrafrique TLD B.V.、名称服务器在境外地址空间——IANA 是实体/地址/注册局角色 A，不证明班吉数据中心。
- **世行 PGNSP**（P174620，2022-05 批准 3,500 万美元赠款）：ARCEP 监测平台 2024-04 启用（80 TB 存储，A 机构计算）；项目文件需搜索 e-政府托管/DR/政府云/身份/互操作平台/DC 组件。
- **Huawei/Cybastion/ECCAS-PIDA**：Huawei Tier III 政府 DC（Digital Business Africa 2026-05，B 待佐证）；Cybastion 2021-04-29 政府数据中心签署（A 自述签署，现状 unknown/stale）；ECCAS/PIDA PAP2 六新 DC 之一含 CF（B 规划背景）。
- **ENERCA/能源**：Boali 水电/Ombella-Mpoko 与班吉变电站为电力背景；搜索与具名 DC 项目绑定的发电机组/UPS/变电站/变压器/太阳能/冷却/柴油存储。
- **云区域/认证**：AWS/Azure/GCP/OCI 官方列表 = 无 CF 区域（A 阴性对照）；Uptime 为 Tier 声明认证来源。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **GreenLine Technologies**（greenline-tech.com）：SOCATEL 授权、1.5 亿美元、Tier 3 DC 计划（A 自述）；2026-07-16 运营阶段启动媒体（B）；保持 planned。
- **Cybastion**（cybastiontech.com）：2021-04-29 签署（A）；后期年评/政府页中 CAR 缺席则保持 unknown/stale。
- **Orange Centrafrique**：2021 火灾报道明确提数据中心/核心网络/无线设施，后恢复运营（B）；电信技术设施，非 colo；`developer=Orange Centrafrique`、`division=Bangui`、`capacity_mw=null`。
- **Telecel/Moov Africa**：移动运营商核心/机房，无公开 DC 证据（MIA AI 助手不证明本地托管）。
- **媒体分级**：Agence Ecofin/Ecofin Agency（B）、We Are Tech（B）、Radio Ndeke Luka（B，官方转述 A）、RJDH/Oubangui Medias（B）、Digital Business Africa（B，Huawei/Orange）、DCD/Developing Telecoms/Telecompaper（B）、ET Cluster（B，Orange 火灾后韧性）。
- **目录纪律**：datacenters.com 称 CF 有 2 个 DC/提供商（C，需抓取具名并佐证，页面可能 403/429）、DataCenterMap/Cloudscene/Baxtel/NSRC 非洲 DC 地图（C）；升级流程 = 精确名称 → 运营商域/gouv.cf/arcep.cf/AfDB/世行 → 电力/冷却/认证词 → 无佐证保持 C。
- **状态词**：`protocole d'accord/MoU/partenariat/mandat/ambition` = planned；`lance la phase operationnelle` = 伙伴关系执行开始，仍非施工；`pose de la premiere pierre/lancement des travaux/construction` = 施工线索；`inaugure/mis en service/operationnel` = 仅对所启动事物；Starlink/光纤服务启用不是 DC 调试。

## 来源分级

- **A** = 针对确切事实的主要/官方证据：gouv.cf 或部委页、ARCEP 官方页/决定、IANA .cf 委托记录、AfDB MapAfrica/项目记录、世行项目文件/博客、官方运营商或厂商公告、Uptime Institute 认证记录、官方超大规模区域列表。
- **B** = 强二级：Agence Ecofin/Ecofin Agency、We Are Tech、RFI、Radio Ndeke Luka、RJDH、Oubangui Medias、Digital Business Africa、DCD、Developing Telecoms、Telecompaper、Ecomatin、ETC/WFP、具名行为者与日期的可信本地/行业媒体。
- **C** = 仅弱线索：datacenters.com、DataCenterMap、Cloudscene、PeeringDB、市场报告、社交帖子、不可访问片段、无原始买方文件的招标聚合器、无具名站点的本地评论。
- **U** = 已检索阴性/未验证缺失；仅在记录搜索模式后用于 no_projects 行。
- `capacity_mw` 仅来自针对精确设施的来源 MW/IT 负载；kVA、发电机组、平方米、机架、存储 TB 放 notes；MoU/签署语言不得推断施工。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 CF 记录与种子（CAB-CAR 国家 DC、GreenLine/SOCATEL、Huawei、Cybastion、ECCAS/PIDA、Orange 班吉核心、ARCEP 平台、SOCATEL 注册局）。
2. 区分并保持独立：国家/政府规划项目（CAB、GreenLine、Huawei、Cybastion、PIDA）除非来源明确同属一个资产，否则各自独立记录。
3. 逐区扫描 17 个清单区：Bangui 详尽；Ombella-Mpoko 与 Haute-Sangha/Mambere-Kadei 为电力/光纤背景；其余区阴性默认并记录搜索模式。
4. 仅当来源具名 Bangui 或事件/设施语境为班吉国家政府站点时才指派 Bangui（并注明推断）；否则 notes 标记位置未分配。
5. 输出 schema：`{country_code: CF, country_name: Central African Republic, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`（division 用 17 清单名，notes 保留现行省/地）；阴性区完成通用模板 + 运营商/厂商/捐助者词后写 `no_projects: true`。不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] CAB-CAR 国家数据中心：从 AfDB/政府最新状态核实阶段与承包商。
- [ ] GreenLine/SOCATEL Tier 3：寻找站点地址、机架、MW、认证、施工许可证据。
- [ ] Huawei Tier III 政府 DC：寻找政府/Huawei/采购一手佐证；检查与 CAB/PGNSP/Cybastion/GreenLine 重叠。
- [ ] Cybastion：搜索后期进展（年评/政府页）；无进展则保持 unknown/stale。
- [ ] ECCAS/PIDA PAP2：打开 PIDA/ECCAS 项目文件核实。
- [ ] Orange 班吉设施：核实 2021 火灾后恢复与当前状态。
- [ ] 云区域阴性对照与 Uptime 记录：每次运行复查。
