---
name: mz-datacenter-methodology
location: scripts/expansion/world/country-skills/MZ/SKILL.md
description: |
  莫桑比克（Mozambique, MZ）数据中心发现与审计方法论。10 个 manifest 省（Maputo 市+省合并到 Maputo，
  保留精确官方地点）。无国家 DC 登记册；INTIC 2026 年起推出数据中心/云许可制度（Decreto 71/2025 与 72/2025，
  2026-06-08 首批许可）。已证商业设施集中在 Maputo：Raxio MZ1（Beluluane，最高 400 racks/3 MW，Uptime
  Tier III 设计与建成认证）、iColo/Digital Realty MPM1（Maputo 市，80 racks/350 m²，2023-02-07 开业）、
  Vodacom Business Matola DC（Tchumene，2025-03 启用，USD 25m，Tier III 双认证）；另有 UEM/CIUEM 机构 DC
  （2026-08 启用）、EDM 国家控制中心（Matalane/CTM）等公用事业 lead。无 AWS/Azure/GCP/OCI 区域。
  葡萄牙语优先（centro de dados）。详见 explorer-official.md 与 explorer-industry.md。
---

# MZ · 莫桑比克数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：莫桑比克 DC 市场呈 Maputo-centric 且真实增长；INTIC 许可制度是最新官方管线，商业 colo 仅 Maputo 省有实证。
> 非 Maputo 省份默认负向，直到具名物理设施/许可/中标出现。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供按 10 省粒度复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：INTIC 数据中心/云许可（Decreto 71/2025、72/2025）、INCM、CEDSIF、UEM、APIEX/BAU、ARENE/EDM/MIREME/HCB、Boletim da Republica；设施观察清单与 10 省覆盖矩阵。 |
| `explorer-industry.md` | 行业/厂商发现：Raxio/Uptime/iColo/Digital Realty/Vodacom/UEM/INTIC/Bubble 等 A 级源、DCD/Club of Mozambique/AIM 媒体、目录升级工作流与逐省策略。 |

## 核心结构事实（框定每次搜索）

1. **10 省模型 + Maputo 合并**：manifest 仅一个 `Maputo` 分区，Maputo 市与 Maputo 省（Matola、Boane/Beluluane、Namaacha、Manhica、Matalane）都映射到它，精确官方地点写入 notes。
2. **INTIC 许可制（2026 起）**：Decreto n.o 71/2025（数据中心）与 72/2025（云计算），2025-12-31 批准、2026-06-08 首批许可；许可证类别决定计数——DC 运营者/设施可计为 licensed lead，纯云/平台运营商不算物理设施。
3. **已证商业设施**：Raxio MZ1、iColo/Digital Realty MPM1、Vodacom Business Matola DC——均在 Maputo；UEM/CIUEM 机构 DC 为 2026-08 新增。
4. **Uptime 是权威**：Uptime 国家记录列出 MZ 两个 Tier III（Raxio MZ1、Vodacom Matola），均为设计与建成双认证；无 Uptime 的 Tier 措辞是声明。
5. **无 hyperscaler 区域**：AWS/Azure/GCP/OCI 官方表均无 MZ；总理 "17/18 个数据中心" 言论仅作市场规模上下文（两媒体数字不一，非登记册）。
6. **葡萄牙语优先**：`centro de dados`、`centro de processamento de dados`、`computacao em nuvem`、`licenca`、`Titulo Unico`、`sala de servidores`、`colocation`/`alojamento`。
7. **非 Maputo 提升规则**：只有官方/运营商命名物理设施、具名中标、Uptime/认证或强媒体+可追责站点才入册，否则记 C lead 或负向。
8. **海缆/IXP/PeeringDB/CDN/云接入/卫星站/ISP PoP ≠ DC**；VPS/云/托管页无 MZ 实体站点不计。

## 查询模式（复制粘贴模板见 explorer-official.md / explorer-industry.md）

```text
site:intic.gov.mz "centro de dados" OR "Operadores de Centros de Dados" OR "licencas"
"Decreto 71/2025" "centro de dados" Mocambique
site:incm.gov.mz "centro de dados" OR "licenca" "{operator}"
site:uem.mz "centro de dados" OR CIUEM OR MOZIX
site:edm.co.mz "centro de dados" OR "Centro Nacional de Controlo" OR Matalane OR CTM
site:apiex.gov.mz "data center" OR "Beluluane" OR MozParks
"Raxio MZ1" Mozambique OR Mocambique
"iColo" OR "Digital Realty" "MPM1" Maputo
"Vodacom Business Matola Data Center" OR "Vodacom" Tchumene Matola
"Uptime Institute" Mozambique "Tier III"
site:datacenterdynamics.com Mozambique OR site:clubofmozambique.com Mozambique ("data center" OR "centro de dados")
"{province}" OR "{capital}" "centro de dados" OR "data center" Mocambique
"Bubble Cloud" Mocambique "centros de dados" OR "licenca"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **INTIC**（intic.gov.mz）：数据中心/云许可与监管——A 级许可证据；每条 run 收割精确 licensee 名单。
- **INCM**：电信/邮政监管，运营商宇宙（Tmcel/Mocambique Telecom、Vodacom、Movitel、TV Cabo、Webmasters、Moztel、TeleData、Paratus、WIOCC、SEACOM 等）；牌照是电信授权，非设施。
- **政府系统**：CEDSIF/e-SISTAFE（平台证据 A/C，物理设施待证）；UEM/CIUEM 官方页（A 级机构 DC，支持 .mz/MOZIX）。
- **投资/建筑**：APIEX（投资批准 A，非运营状态）、BAU/e-BAU（经济活动许可，非可检索建筑许可库）；Maputo 市/区工程许可分散。
- **能源/公用事业**：ARENE/EDM/MIREME/HCB；EDM RENMOZ 2026 演示（ALER 托管）给出国家控制中心 Matalane/CTM 的数据中心组件与 Chibata/Nampula 区域控制/数据收集点。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Raxio MZ1**：Beluluane Industrial Park/Matola-Boane（距 Maputo 市中心约 20 km），最高 400 racks、2,000 m² white space、3 MW IT 电力；Uptime Tier III 双认证（A）。
- **iColo/Digital Realty MPM1**：Maputo 市，80 racks、350 m² IT 空间、9,500 m² 园区；2023-02-07 开业公告（A）；保留 iColo 容量值，不用目录估算替代。
- **Vodacom Business Matola DC**：Tchumene/Matola，2025-03 启用（DCD/Club of Mozambique），USD 25m、2023-10 动工、carrier-neutral、2Africa 接入；Uptime Tier III 双认证；capacity_mw 保持 null 除非 Vodacom 公布。
- **UEM/CIUEM DC**：Maputo 市机构/大学 DC，2026-08 启用（A）；非商业 colo 除非出现官方服务条款。
- **Bubble Cloud**：首个获 INTIC 云牌照的提供商（B/C）；AIM 报道两个数据中心——命名站点前不得计两个物理 DC。
- **目录**（DataCenterMap/Datacenters.com/Baxtel 等）：C 级 lead；按升级工作流（精确名+运营商域→Uptime→INTIC/INCM→媒体）处理。

## 已知设施/项目与证据状态

| 设施/项目 | 省/地点 | 状态与证据 |
|---|---|---|
| Raxio MZ1 | Maputo（Beluluane Industrial Park/Matola-Boane） | 运营商业 colo，A 级（Raxio 规格 + Uptime Tier III 双认证）。 |
| iColo / Digital Realty MPM1 | Maputo 市 | 运营商业 colo，A 级（iColo 开业 + Digital Realty 页）；80 racks/350 m²/9,500 m² 园区。 |
| Vodacom Business Matola DC | Maputo（Tchumene/Matola） | 运营（2025-03 启用），A/B；Uptime Tier III 双认证；容量未知。 |
| Vodacom 2013 模块化 DC | Maputo（Matola） | 历史遗留 lead（B），仅当清单区分遗留模块设施时单列。 |
| UEM/CIUEM 数据中心 | Maputo 市 | 机构/大学 DC，2026-08 启用（A）；非商业 colo。 |
| CEDSIF / e-SISTAFE | Maputo | 机构 lead（A/C）；物理设施待证。 |
| INTIC 持牌 DC 运营者/设施 | 各省（likely Maputo-heavy） | Licensed（A）；按 INTIC 页收割精确名单。 |
| Bubble Cloud | Maputo（站点待核） | 持牌云/数据驻留 lead（B/C）；站点未命名前不计物理 DC 数。 |
| EDM 国家控制中心（Matalane/CTM） | Maputo | 计划/采购中公用事业 DC 组件（A/B）；待 EDM 招标/授标复核。 |
| EDM Chibata / Nampula 区域控制 | Manica/Sofala 边界待核 / Nampula | 计划公用事业控制/数据收集 lead（A/B）；DC 组件显式化前不计。 |

## 更新节奏

- 每批次：重跑 INTIC 许可页（收割 licensee）、INCM/运营商页、Uptime 国家记录、DCD/Club/AIM/Jornal Noticias/Carta/Diario Economico/O Pais 与 10 省扫描；盯 Bubble 站点命名与 EDM 招标。
- 每季度：重核 hyperscaler 官方区域表；复核总理 "17/18" 言论是否有官方设施清单出台。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（10 省粒度）；本 skill 作为国家层参考注入。
