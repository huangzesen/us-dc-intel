---
name: om-datacenter-methodology
location: scripts/expansion/world/country-skills/OM/SKILL.md
description: |
  阿曼（Oman, OM）数据中心发现与审计方法论。11 个省（South/North Batina、Buraymi、Interior、Muscat、
  Musandam、Southeastern、Northeastern、Central、Dhahira、Dhofar）全覆盖，记录用仓库分区名并保留官方别名/
  wilayat/阿拉伯名。无统一国家 DC 登记册，需三角化 gov.om、Muscat Municipality、OPAZ/SEZAD/自由区、
  Madayn/KOM、MTCIT、TRA、APSR/Nama/OETC/NPWP、Environment Authority。主要种子：Equinix MC1（Barka/
  South Batina 实体，Muscat 品牌）、Equinix SN1（Salalah/Dhofar）、Ooredoo Bawshar/Barka/Sohar/Salalah、
  Otech/Oman Data Park KOM4、Otech Firq/Nizwa、OCI Dedicated Region（Muscat 主 + Ibri 备）、Datamount
  Al Bandar/Jabal Al Akhdar、AWS Local Zone Muscat（me-south-1-mct-1a，非完整 Region）。阿拉伯语搜索强制。
  详见 explorer-official.md 与 explorer-industry.md。
---

# OM · 阿曼数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：阿曼已有真实 DC 集群，但覆盖不均且常用 metro 标签掩盖实体省份（如 MC1 标 Muscat、实体在 Barka）。
> 枚举以官方/运营商种子 + 分区粒度扫描为主，云节点（Local Zone / Dedicated Region）与 colo 容量必须分开。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供按 11 省粒度复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：gov.om、Muscat Municipality、MTCIT 云托管与获批供应商登记、TRA、OPAZ/SEZAD/自由区、Madayn/KOM、APSR/NPWP/MEM/EA、Otech/Ooredoo/Equinix/Datamount 官方页、AWS Local Zone 文档；每省查询块与设施证据分类。 |
| `explorer-industry.md` | 行业/厂商发现：DCD 阿曼标签、Times of Oman、Oman Observer、Muscat Daily、ONA；运营商/厂商查询模式、英阿双语搜索库、去重与 watchlist。 |

## 核心结构事实（框定每次搜索）

1. **11 省模型**：South Batina、North Batina、Buraymi、Interior、Muscat、Musandam、Southeastern、Northeastern、Central、Dhahira、Dhofar；官方别名（Al Batinah South、Ad Dakhiliyah、Ash Sharqiyah South/North、Al Wusta、Ad Dhahirah 等）与 wilayat 必须保留。11 省全部有正/负向记录才算覆盖完成。
2. **无统一许可检索**：Muscat Municipality（Muscat）、OPAZ/zoneservices（Duqm、Sohar Free Zone、Salalah Free Zone、Al Mazunah、Khazaen）、Madayn（工业城 + Knowledge Oasis Muscat）是主要许可面。
3. **电力是最佳官方佐证**：APSR/Nama/OETC/NPWP + 分区配电公司查 MW/变电站/MVA/自发电/太阳能。
4. **云证据精确分类**：AWS Muscat 是 Local Zone（me-south-1-mct-1a）而非 Region；Otech/ITHCA/Oracle 的 OCI Dedicated Region（Muscat 主、Ibri 备）是专属/主权云设施；Azure/Google 无阿曼公共区域。
5. **海缆登陆是线索不是设施**：Barka、Salalah（2Africa）、Qalhat/Sur（TGN-Gulf/SMW5）优先；登陆站需单独举证。
6. **状态词纪律**：MoU/JDA/land lease/groundbreaking/launched/operational/built to Tier III/Uptime certified 是不同的状态，保留源动词。
7. **容量字段分离**：it_mw、facility_power_mw、grid_connection_mva、solar_mwp、racks、white_space_sqm、announced_campus_mw、mining_machines 不得混算。
8. **阿拉伯语强制**：مركز بيانات/مراكز البيانات/الحوسبة السحابية/تصريح بناء/تخصيص أرض/محطة تحويل/ميغاواط/الكابلات البحرية/محطة إنزال الكابلات + 阶段动词（افتتاح、تدشين、إطلاق、وضع حجر الأساس）。

## 查询模式（复制粘贴模板见 explorer-official.md / explorer-industry.md）

```text
site:mtcit.gov.om ("Cloud Hosting and Data Center Services" OR "approved hosting" OR "data center" OR "مراكز البيانات")
site:otech.om ("data center" OR "Farq" OR "Firq" OR "Nizwa" OR "Ibri" OR "OCI" OR "KOM")
site:ooredoo.om ("data centre" OR Barka OR Salalah OR Sohar OR Bawshar)
site:equinix.com Oman ("MC1" OR "SN1" OR Muscat OR Salalah)
site:datamount.om ("Al Bandar" OR Jabal OR Dakhiliyah OR "Tier III")
site:docs.aws.amazon.com/local-zones "Oman (Muscat)" OR "me-south-1-mct-1a"
site:opaz.gov.om OR site:duqm.gov.om OR site:soharportandfreezone.om ("data center" OR "cloud data" OR AI)
site:apsr.om OR site:omanpwp.om ("data center" OR "self generation" OR MW OR substation)
site:omannews.gov.om ("data centre" OR "مركز بيانات" OR "مراكز البيانات")
"{wilayat}" ("data center" OR "مركز بيانات") (MW OR MVA OR racks OR "data halls")
"{operator}" "{wilayat}" (MW OR MVA OR "محطة تحويل" OR substation)
```

## 官方/监管管线要点（详见 explorer-official.md）

- **MTCIT**：云托管与数据中心服务审批 + 获批供应商登记册（可见 Oman Data Park/Otech 联系人与 KOM4 地址）——A 级获批证据。
- **Muscat Municipality / OPAZ / zoneservices / Madayn / SEZAD(Duqm) / Sohar Port & Freezone**：各省许可/土地/一站式路线。
- **TRA**：电信/ICT 牌照与项目（含 DC/云服务框架）；牌照不等于设施。
- **APSR / NPWP / OETC / Nama / MEM / Environment Authority**：电力、容量规划、绿色氢能与 EIA 佐证。
- **认证**：Uptime Institute 认证表验证；`Tier III`/`Level 3+`/`built to Tier III` 一律按运营商声明处理。
- **政府新闻**：ONA（omannews.gov.om）是阿语/英语启用公告主面。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **DCD 阿曼标签**是 Equinix MC1/SN1、Ooredoo、Otech/ODP、Exahertz、绿色 DC JDA 的最佳整合贸易面。
- **Equinix MC1**（与 Omantel JV，725 cabinets + 扩展潜力）与 **SN1**（Salalah，2024-11 启用，carrier-neutral）为 A 级。
- **Ooredoo**：Bawshar/Muscat 2.5 MW（2021 起运营）、Barka DC+2Africa 登陆（2022 动工，待启用验证）、Sohar 1,200 racks/最高 10 MW（2024-11 启用，Level 3+ 声明）、Salalah DC+CLS（2025 启用报道 B 级）。
- **Otech/Oman Data Park**：KOM4（Muscat/Rusayl）运营并获 MTCIT 登记；Firq/Farq Nizwa（Interior，4.4 MW/太阳能待核实拼写与状态）；Duqm（Central，历史 lead，需 Otech/SEZAD 现页重确认）。
- **Datamount**：Al Bandar（Muscat/Seeb，700+ racks 声明 B 级）与 Jabal Al Akhdar（Interior）均为运营商声明。
- **Exahertz/Afaaq**（Salalah Free Zone）：$370m/11 MW/Bitmain 详情来自 DCD/crypto 媒体，优先 ONA/MTCIT/Oman Observer。
- **150 MW 绿色 AI DC JDA**：仅 planned，不得计为设施；阿曼-阿尔及利亚合作为 MoU。

## 已知设施/项目与证据状态

| 设施/项目 | 分区/地点 | 状态与证据 |
|---|---|---|
| Equinix MC1 | South Batina 实体（Barka）/ Muscat 品牌 | Operational，A 级 Equinix，B 级实体位置。 |
| Equinix SN1 | Dhofar（Salalah） | Operational，2024-11 启用，A 级。 |
| Ooredoo Bawshar DC | Muscat | Operational（2021 起），2.5 MW，A 级 Ooredoo。 |
| Ooredoo Barka DC + 2Africa | South Batina | 2022 动工/登陆 lead，启用待验证。 |
| Ooredoo Sohar DC | North Batina | Operational（2024-11），1,200 racks/最高 10 MW，Level 3+ 声明。 |
| Ooredoo Salalah DC + CLS | Dhofar | 2025 启用报道（B），125→500 racks。 |
| Otech/Oman Data Park KOM4 | Muscat（KOM/Rusayl） | Operational/accredited，MTCIT 登记含地址。 |
| Otech Farq/Firq Nizwa | Interior | 运营商声明；拼写/状态/4.4 MW 待核。 |
| OCI Dedicated Region（主） | Muscat | Dedicated/sovereign 云，非公共区域；宿主设施待识别。 |
| OCI Dedicated Region（备） | Dhahira（Ibri） | 可用/已启动（Otech + ITHCA + Oracle）。 |
| Datamount Al Bandar / Jabal Al Akhdar | Muscat / Interior | Operational/运营商声明；容量 B 级。 |
| ODP/Otech Duqm | Central（SEZAD） | 历史运营 lead，需现页重确认。 |
| Exahertz/Afaaq Salalah Free Zone | Dhofar | 运营中 crypto/数据托管，按独立类记录。 |
| AWS Local Zone Muscat | Muscat（宿主未公开） | Available Local Zone，不计设施数。 |
| 150 MW 绿色 AI DC JDA | 未定 | Planned/JDA，不计设施。 |

## 更新节奏

- 每批次：重跑官方（MTCIT/OPAZ/APSR/Otech/Ooredoo/Equinix/Datamount）与行业（DCD/Times/Observer/Muscat Daily）查询块；解决 watchlist（Firq 拼写、Barka 启用、Salalah 官方页、Duqm 现页、Exahertz 对账、150MW JDA 落地）。
- 每季度：重核云官方页（AWS Local Zones、Azure、GCP、Oracle Dedicated Region）；重跑 11 省英阿双语负向扫描。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（11 省粒度）；本 skill 作为国家层参考注入。
