---
name: gq-datacenter-methodology
location: scripts/expansion/world/country-skills/GQ/SKILL.md
description: 赤道几内亚（GQ）数据中心发现与审计方法论：官方/监管/云管线以 GITGE 国家电信基础设施公司（含 Sipopo 托管服务）、CNIAPGE 政府信息化、PAMFP/AfDB 援助采购、海底电缆登陆与能源/许可线索为主，行业侧以运营商/厂商新闻、目录与 PeeringDB 交叉验证；国家无公共数据中心注册库，按 manifest 的 2 个大区（Continental 大陆区、Insular 岛屿区）组织结果。运行 GQ exploration/audit 批次前必读，详细来源与查询模板路由至 explorer-official.md 和 explorer-industry.md。Equatorial Guinea (GQ) datacenter discovery & audit methodology: official/regulatory/cloud pipeline (GITGE, CNIAPGE, PAMFP/AfDB, cable landings) + industry/trade-press discovery, organized by the manifest's 2 regions (Continental, Insular); no national registry exists.
---

# GQ · 赤道几内亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：赤道几内亚无公共国家数据中心注册库、无公开建筑许可数据库，市场极小（人口约 190 万、仅一条在用国际海缆、无公共 IXP、无超大规模云区域）。本 skill 汇总两份已评审探索报告的发现与纪律：以官方电信基础设施证据（GITGE）、政府信息化记录（CNIAPGE）、援助采购（PAMFP/AfDB）、海缆登陆与能源/许可线索拼接全国清单，并用行业/厂商证据交叉验证。预期全国真实记录约 3-6 条（含政府/公用事业内部设施），切勿用登陆站、运营商办公室或部长级机房充数。

## 入口

| 文件 | 管线 | 用途 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线 | GITGE 国家基础设施、CNIAPGE 政府数据中心、PAMFP/Hacienda 采购、能源（SEGESA）证据、官方云区域否定控制、IXP/Uptime 否定控制 |
| `explorer-industry.md` | 行业/厂商发现 | 运营商与设施种子、云/CDN/接入点检查、行业来源分级、目录与 PeeringDB 交叉验证、分大区行业模式 |

## 核心结构事实

1. **Division 模型**：manifest 规定 2 个大区（`subnational_type = region`）：**Continental**（Rio Muni 大陆，含 Litoral/Centro Sur/Kie-Ntem/Wele-Nzas/Djibloho 各省）与 **Insular**（Bioko 岛 + Annobon 岛 + Corisco）。所有结果必须挂在 2 个大区下，省/市名（Malabo、Bata、Luba、Ebebiyin、Mongomo、Oyala/Ciudad de la Paz 等）仅作搜索锚点。
2. **语言与拼写**：先以西班牙语搜索（非洲唯一西语国家），再用法语/英语检索官方与捐助方文件。高收益词：`centro de datos`、`coubicación`/`coubicacion`、`sala de servidores`、`nube soberana`、`estación de aterrizaje`、`punto de intercambio`、`licitación`、`CNIAPGE`、`GITGE`、`ORTEL`、`PAMFP`、`SEGESA`、`Minsait`、`Mandji`、`Ceiba`、`ACE`、`Ultramar GE`、`Annobón`。
3. **国家消歧**：每次必须与几内亚（Conakry，`Guinée`）、几内亚比绍及刚果（金/布）区分；GQ 证据通常出现 Malabo、Bata、Bioko、Rio Muni、Annobon、GITGE、GETESA、CNIAPGE、PAMFP 或 `Guinea Ecuatorial`。不得合并。
4. **计数口径**：只计物理设施（具备 siting 或 facility 语言：data center、racks、技术机房、white space、colocation/coubicacion、IXP 主机、Tier 设计/认证、launch、construction、commissioning）。政策目标、公司办公室、通用云服务、基站、海缆登陆点、运营商 POP 不计。
5. **关键机构**：GITGE（国家电信基础设施管理者，Decreto 44/2011 设立，AS37529，Sipopo 数据中心运营商）；CNIAPGE（总统府下公共行政信息化机构，其行政数据中心位于 Malabo II，2014 设备招标、2016 启用、2025 更新计划，A 级官方证据）；PAMFP（财政现代化项目，AfDB 共同融资，2026-06 招标 Malabo 主数据中心 + Bata 备份数据中心）；SEGESA（电力公司，Minsait/Indra 2019 年约 500 万欧元合同含 Malabo+Bata 新数据中心供应）；ORTEL/OERT 电信监管机构（未找到官方网站，引述监管机构按 B 级）。
6. **容量语义**：能力层级为官方数据表 > 运营商声明 > 引述运营商的行业媒体 > 目录。Sipopo 的容量/Tier/机柜数目前仅 C 级（目录/PeeringDB 用户维护字段），不得升格；GITGE 官方 colocation 服务存在性为 A 级。
7. **可靠性分级规则**：A = 主要/官方证据（GITGE 官方页/年报、政府新闻、部委/监管声明、CNIAPGE 董事会记录、官方捐助项目页、官方云区域页、ISOC Pulse、官方法律文件）；B = 强二级或当事方商业证据（Agence Ecofin/AhoraEG/DCD/Telecompaper 等、引述具名官员的地方媒体、厂商对自己合同范围的新闻稿）；C = 仅线索（目录、PeeringDB 用户维护字段、市场报告、社交帖、模糊托管/云声称）。分级作用于具体事实，同一设施不同事实可不同级。
8. **云/IXP/Uptime 否定控制**：AWS/Azure/GCP/OCI 均无 GQ 公共区域（官方区域页 A 级否定，2026-08-12 复核）；ISOC Pulse 显示 GQ 无活跃 IXP（约 3% 本地缓存）；Uptime Institute 列表无 GQ 设施，任何 `Tier III` 语言视为设计/合规/运营方声称，除非 Uptime 列表确认。
9. **状态层级**：官方/运营商运营页或启用典礼 > 开通报道 > 在建官方/捐助页 > 合同授予 > 招标 > 协议/MoU > 政策。禁止将协议/招标升级为在建（BCN 商业数据中心为 2026-02 协议级、PAMFP 批次为 2026-06 招标级、8 缆国家数据中心为 2023-04 待招标提案）。
10. **政府设施去重**：GITGE Sipopo DC、CNIAPGE Malabo II DC、PAMFP/Hacienda Malabo DC、规划的 8 缆国家 DC、BCN 商业 DC 在官方证据证明同一建筑/合同前必须作为独立记录；CNIAPGE 默认定位在 Malabo II 市区/片区级，不等于 Sipopo。

## 常用查询模板

官方/监管管线（GITGE、政府新闻、CNIAPGE、PAMFP、云否定控制）：

```text
site:gitge.com "centro de datos"
site:gitge.com coubicacion
site:gitge.com Sipopo
"GITGE" "centro de datos" Malabo
"GITGE" "data center" Sipopo
site:guineaecuatorialpress.com "centro de datos"
site:guineaecuatorialpress.com CNIAPGE
"CNIAPGE" Malabo OR Bata OR sede
"Centro de Datos de la Administración" "Malabo II"
site:pamfp.org "centro de datos" OR "data center" OR licitacion
"PAMFP" "centro de datos" Malabo OR Bata OR Hacienda
"Guinea Ecuatorial" "cloud region" OR "regiones de nube"
site:uptimeinstitute.com "Equatorial Guinea" OR "Guinea Ecuatorial"
```

行业/厂商发现（含国家消歧）：

```text
("Guinea Ecuatorial" OR Malabo OR Bata) (datacenter OR "data center" OR "centro de datos" OR coubicacion OR colocation) -Conakry -"Guinea-Bissau"
"GITGE" Sipopo datacenter OR coubicacion OR racks OR Tier
"Minsait" SEGESA "centro de datos" Malabo Bata
"BCN" OR "Backbone Connectivity Network" "Guinea Ecuatorial" cable OR "centro de datos"
"Google" "centro de datos" "Guinea Ecuatorial"
site:datacenterdynamics.com "Equatorial Guinea" "data center"
("{division}" OR "{city}") (datacenter OR "centro de datos" OR coubicacion OR colocation) "Guinea Ecuatorial"
```

逐条记录捕获模板：

```text
facility_name:
operator_or_owner:
division_manifest_2: Continental | Insular
province_city_address:
status: operational | commissioned | under construction | planned | tender | agreement | lead-only | rejected
source_grade_by_fact:
source_urls:
physical_evidence: racks | rooms | MW/MVA | Tier | IXP host | landing station | POP | office
capacity:
power_cooling:
connectivity:
tenant_or_service_scope:
dedupe_notes:
country_disambiguation:
```

## 官方/监管管线要点（详见 explorer-official.md）

- **GITGE** 是国家级骨干/海缆/托管问题第一入口；colocation 服务页与 2024 年报为 A 级；Sipopo 数据中心地址（Carretera Malabo-Sipopo）与身份由 PeeringDB fac 9041/目录补足（C 级）。
- **CNIAPGE / Centro de Datos de la Administración（Malabo II）** 是最强 A 级政府数据中心证据：2014-07-12 公开招标（主动+被动设备）、2016-06-04/06 启用、2025-04-15 董事会记录（设备更新、数据托管/连续性命脉）；容量未公开。
- **PAMFP/Hacienda**：Malabo 主数据中心（lot 1）与 Bata 备份数据中心（lot 2），2026-06-04 招标报道，各 4 个月工期，含太阳能设备，国家招标，AfDB 共同融资；Bata 记录是 Continental 大区最强数据中心线索。
- **能源线索**：SEGESA 为电力公司；Minsait/Indra 2019-01-15 官方新闻稿确认 SEGESA 转型合同含 Malabo+Bata 新数据中心供应（约 EUR 500 万，运营商内部设施，非公共托管）。
- **云区域否定控制**：AWS/Azure/GCP/OCI 官方区域列表均无 GQ（2026-08-12）；GQ 云声称一律视为转售/CDN/接入/租户证据。
- **IXP/Uptime 否定控制**：ISOC Pulse 显示 GQ 无活跃 IXP；Uptime 无记录。
- **仅连通性（勿计为数据中心）**：ACE 国际海缆 Bata 登陆、Ceiba-1（287 km Malabo-Bata）/Ceiba-2（2017-03 起 Malabo-Bata-Kribi）、Ultramar GE Annobon（约 263 km，2023-04-03 激活，>EUR 1200 万，4.8 Tbps）、Mandji（Corisco-Cabo San Juan 50 km）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **市场分布**：公共数据中心市场集中在 Malabo（Insular/Bioko Norte）：GITGE Sipopo 托管、CNIAPGE Malabo II、PAMFP/Hacienda 主 DC（招标）、规划 8 缆国家 DC、BCN 商业 DC（地点未定）。Bata（Continental/Litoral）为次级节点：ACE 登陆站、GITGE 技术机房、RNFO 城域、PAMFP 备份 DC（招标）、SEGESA/Minsait 内部 DC 线索。
- **运营商**：GETESA（Orange GQ 遗留品牌，AS37173）、GECOMSA、HITS-EG 存在性 A/B 级，但无公共数据中心/托管服务证据，仅作 POP/机房线索。
- **行业来源分级**：运营商官方页（A）、PeeringDB org 17440/fac 9041 与 AS37529 路由（A/B/C）、ISOC Pulse（A 否定）、GeoCables 路由研究（B）、行业媒体（B）、目录（C，仅用于别名/地址直至与 A/B 源联接）。
- **厂商线索**：Incubaweb 称 GITGE 有世界级 DC 抱负、Huawei Marine 参与 SAIL、中国进出口银行贷款 GECOMSA 项目——均仅作承包商发现线索（C），不得计为设施。
- **目录注意**：Inflect GQ 页返回 HTTP 404（2026-08-12），仅作历史搜索线索，不是已验证 URL。

## 维护注意（更新纪律）

- **更新节奏**：每次 exploration/audit 批次前重跑官方云区域否定控制与 ISOC Pulse/Uptime 检查；招标/协议类状态（PAMFP 招标、BCN 协议、8 缆国家 DC、SEGESA/Minsait 交付）每批追踪 award/construction/commissioning 证据。
- **来源验证**：任何 C 级目录线索必须与非目录源（A/B）联接才能升格；Tier 声称需 Uptime 列表或官方数据表；容量以官方数据表优先，宣布容量与已投运容量分开记录。
- **禁止删除纪律**：本 skill 与两份 explorer 均不删除既有事实；发现身份合并（如 Sipopo DC 与规划 8 缆国家 DC 为同一建筑）时保留原记录并添加 dedupe_notes 与证据链接。
