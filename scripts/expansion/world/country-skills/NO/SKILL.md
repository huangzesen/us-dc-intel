---
name: no-datacenter-methodology
location: scripts/expansion/world/country-skills/NO/SKILL.md
description: |
  Norway (NO) data-center enumeration methodology. Division model: repo uses 2020-2023 county labels plus Arctic territories (Oslo; Rogaland; More and Romsdal; Northland; Svalbard; Jan Mayen; Viken; Inland; Vestfold and Telemark; Agder; Westland; Trondelag; Troms and Finnmark); search both old and current county names (2024 splits of Viken, Vestfold og Telemark, Troms og Finnmark). Master register: Nkom (datasenterforskriften under ekomloven, in force 2025-01-01) — verified 2026-08-12: 115 registered data centres incl. internal sites, 61 commercial operators listed publicly (internal sites not named). Facility-grade evidence: Nkom registration, municipal planning/building records (saksinnsyn/planinnsyn/postjournal), Statsforvalteren/Miljodirektoratet pollution permits (norskeutslipp.no), NVE/Statnett grid records, Lovdata. Azure Norway East and Norway West are live regions (metro anchors, not addresses); no AWS/Google/Oracle Norway region (Google/WS Computing has a physical Skien/Gromstul DC project). Key seeds: Green Mountain (SVG-Rennesoy 25 MW/22,600 m2, TEL-Rjukan 50 MW/29,000 m2, OSL-Enebakk 93 MW/75,000 m2, OSL-Hamar 150 MW campus/TikTok), Bulk OS-IX Oslo + N01 Agder (up to 1 GW marketed), STACK/DigiPlex SI OSL SPVs, Nscale Glomfjord (30->60 MW), atNorth NOR01 Haugaland (planned 120 MW phases/350 MW site), WS Computing/Google Gromstul Skien, Lefdal Mine (Sigma2/HPE Olivia), Datafjellet Bergen, Tydal Data Center/Bitdeer, Tussa/Tafjord/NEAS regional, Storespeed Halden, PolarDC, Exanorth (crypto), Magnora Averoya (100 MW development). Read this before running NO exploration/audit batches. Routes to explorer-official.md (Nkom/municipal/environment/grid playbook) and explorer-industry.md (operator/association/trade-press playbook).
---

# NO · 挪威数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：挪威自 2025-01-01 起实行国家数据中心监管（新 ekomloven + datasenterforskriften），**Nkom 为国家主登记册**——先取 Nkom 商业运营商全集，再以市政规划/建筑记录、Statsforvalteren/Miljødirektoratet 环境许可、NVE/Statnett 电网文件与运营商页逐设施核实。按字段分级，而非按设施分级。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：Nkom 主登记册与 CSV、市政 saksinnsyn/planinnsyn/postjournal、Statsforvalteren/Miljødirektoratet/norskeutslipp、NVE/RME/Statnett、政府战略/NSM、13 分区（含 Svalbard/Jan Mayen 北极领土）逐区策略、法律/流程词汇 |
| `explorer-industry.md` | 行业/厂商管线：Nkom 优先运营商清单、行业协会（Norsk Datasenterindustri）、运营商/平台图谱、云区域事实、逐区行业线索、工作流与设施置信规则 |

## 核心结构事实（框定每次搜索）

1. 行政划分：repo 沿用 2020-2023 郡标签 + 北极领土：Oslo、Rogaland、More and Romsdal、Northland（Nordland）、Svalbard、Jan Mayen、Viken、Inland、Vestfold and Telemark、Agder、Westland、Trondelag、Troms and Finnmark。2024-01-01 起 Viken、Vestfold og Telemark、Troms og Finnmark 重新拆分（政府/Kartverket 官方映射 https://www.regjeringen.no/no/tema/kommuner-og-regioner/kommunestruktur/fylkesinndelingen-fra-2024/id2922222/）——新旧郡名都要搜。
2. **主登记册 Nkom**：国家数据中心监管 2025-01-01 生效（ekomloven + datasenterforskriften，Lovdata https://lovdata.no/dokument/SF/forskrift/2024-12-18-3313）。2026-08-12 核验：Nkom 概览页（https://nkom.no/datasenter/oversikt）标「Sist oppdatert: 11.08.2026」，共 **115 个已登记数据中心（含内部站点）、61 个商业运营商**；公开表只列商业运营商（出于安全/备灾原因不公布企业内部设施名称与细节）。CSV 导出：https://stenonicprdnoea01.blob.core.windows.net/enonicpubliccontainer/prd/tildeling/datasenter/datasenter-operatorer.csv 。Nkom 不给出全部场地地址；从 Nkom 运营商名 pivot 到市政许可/环境许可/NVE-Statnett/运营商页。加密挖矿旗标按 Nkom 原文保留。
3. 设施高置信计数条件：至少一个 A 级设施源——Nkom 商业注册绑定运营商、市政许可、环境许可、NVE/Statnett 电网记录或运营商自有设施页。购地、政治支持、电网容量预留、云区域命名、目录条目均为线索。
4. **云区域事实**：Azure **Norway East 与 Norway West 为在用区域**（仅都市锚点，物理地址不公开，https://datacenters.microsoft.com/gl_regions/norwayeast/）；AWS 官方区域页无挪威区域（2022 年 Oslo 区域公告为过期线索）；Google Cloud 官方位置无挪威公共区域——但 **Google/WS Computing 在 Skien/Gromstul 建设物理数据中心**（市政与 Statsforvalteren 许可为证）——「云区域存在」与「物理 DC 存在」分开表示；Oracle OCI 无挪威公共区域。
5. 生命周期词汇：规划/建筑 `planinitiativ / oppstartsmote / planprogram / planforslag / horing / offentlig ettersyn / reguleringsplan / detaljregulering / rammetillatelse / igangsettingstillatelse / midlertidig brukstillatelse / ferdigattest / postjournal / saksinnsyn`；环境 `soknad om tillatelse etter forurensningsloven / utslippstillatelse / forurensende virksomhet / nodstromsaggregat / dieselaggregat / testkjoring / stoy / overvann / prosessavlopsvann / kjolevann`；电网 `nettilknytning / tilknytningsavtale / reservert effekt / tilknyttet effekt / anleggskonsesjon / omradekonsesjon / transformatorstasjon / 132 kV / 420 kV / MVA / MW / TWh`。发现词：`datasenter / datasentre / datalagringssenter / serverhall / datahall / kolokasjon / samlokalisering / skytjenester / hyperscale / AI-datasenter / KI-datasenter / kraftkrevende næring / elintensivt / overskuddsvarme / fjernvarme / reservekraft / nødstrøm / kjøling / frikjøling / væskekjøling`。
6. 电网字段分离：`reservert effekt`（容量预留/排队位置）、`tilknyttet effekt`（连接容量）、`IT load`（运营商/客户 IT 容量）、`gross power / site power`（营销或工程场地容量）。**北部限制**：2026 年可靠报道称 Statnett 临时停止 Svartisen 以北 >5 MW 项目新预留（Nordland）——在捕获具体日期官方 Statnett 页面前作为 gating 线索处理。

## 查询模式（复制粘贴模板见 explorer-official.md §1-2 与 explorer-industry.md §1）

- Nkom：`site:nkom.no/datasenter "Registrerte datasenteroperatorer og datasentre"`、`"{operator}" site:nkom.no/datasenter`。提取：运营商法定名、组织号、加密挖矿旗标、页面更新日期、CSV 日期、商业 vs 内部。
- 市政：`site:{kommune}.kommune.no datasenter`、`site:{kommune}.kommune.no serverhall`、`site:{kommune}.kommune.no "reguleringsplan" datasenter`、`site:{kommune}.kommune.no "rammetillatelse" datasenter`、`site:{kommune}.kommune.no "igangsettingstillatelse" datasenter`、`site:{kommune}.kommune.no "ferdigattest" datasenter`、`site:{kommune}.kommune.no "postjournal" "{operator}"`、`site:{kommune}.kommune.no "{gbnr}" datasenter`。核心门户：Oslo PBE Saksinnsyn（https://innsyn.pbe.oslo.kommune.no/saksinnsyn/main.asp）、DiBK、Altinn 建筑申请、Kartverket、eInnsyn（https://einnsyn.no）。提取：市政、旧 repo 分区、现行郡、规划/案件 ID、申请人、物业（gbnr）、地址、地块、建筑数、毛面积、电力/冷却文字、应急发电机、决定日期、许可类型、上诉状态、PDF URL。
- 环境：`site:statsforvalteren.no datasenter "{operator}"`、`site:statsforvalteren.no "datalagringssenter" "{kommune}"`、`site:miljodirektoratet.no/hoeringer datasenter`、`site:norskeutslipp.no "{operator}" datasenter`、`"{operator}" "{kommune}" "tillatelse etter forurensningsloven"`、`"{operator}" "{kommune}" "nødstrømsaggregat"`。
- 电网：`site:nve.no datasenter`、`site:nve.no "anleggskonsesjon" datasenter`、`site:nve.no "{project}" "transformatorstasjon"`、`site:statnett.no datasenter`、`site:statnett.no "Svartisen" "5 MW"`、`"{kommune}" datasenter "132 kV"`、`"{kommune}" datasenter "420 kV"`、`"{operator}" "{kommune}" "nettilknytning"`。
- 已知官方 pivot：`"WS Computing" Gromstul Skien datasenter`、`"Google" Gromstul Skien datasenter`、`"Green Mountain" Enebakk "rammetillatelse"`、`"Green Mountain" Rennesøy "utslippstillatelse"`、`"Bulk Data Centers" OS-IX Oslo`、`"Bulk Data Centers" N01 Kristiansand Vennesla`、`"Nscale" Glomfjord Meløy datasenter`、`"Tydal Data Center" Tydal datasenter`、`"Lefdal Mine" Stad datasenter`、`"atNorth" Haugaland Gismarvik Tysvær datasenter`。
- 行业：`"{operator}" Norge datasenter`、`"{site}" "rammetillatelse"`、`"{site}" "utslippstillatelse"`、`"{site}" "nettilknytning"`、`site:datasenterindustrien.no "{operator}"`、云：`site:learn.microsoft.com azure "Norway East" "Norway West"`、`site:docs.aws.amazon.com "Norway" "Region"`、`"WS Computing" Google Skien Gromstul`。

## 官方/监管管线要点（详见 explorer-official.md）

- Nkom 优先：商业运营商全集 → 每设施 pivot 到市政许可/环境许可/NVE-Statnett/运营商页。Nkom 公开表只给商业运营商；企业内部站点不计入公开行。
- 环境许可常是在用/近在用 DC 的最佳官方证明（备用发电机、噪声、雨水、冷却触发污染法许可）：Statsforvalteren（https://www.statsforvalteren.no/）、Miljødirektoratet（https://www.miljodirektoratet.no/，hoeringer）、Norske utslipp 许可库（https://www.norskeutslipp.no/）、Forurensningsloven（https://lovdata.no/lov/1981-03-13-6）。验证示例：**WS Computing/Google Gromstul, Skien**——Statsforvalteren 称 Datasenter 1 于 2025-08-25 获污染许可、Datasenter 2 于 2026 年听证；**Green Mountain Rennesøy** 许可 PDF 经 Norske utslipp。
- 电网：NVE 许可门户（https://www.nve.no/konsesjon）、RME（https://www.nve.no/reguleringsmyndigheten/）、Statnett（https://www.statnett.no/）。电网源证明使能基建，非 DC 运营。
- 政府战略/安全：2025 数据中心战略（https://www.regjeringen.no/en/documents/the-data-centre-industry-a-sustainable-industry-of-the-future-for-the-digital-norway/id3112356/）、NSM（https://nsm.no/）、Nkom Data Act 页——政策语境，A 级规则/目标，站点计数需引用具体登记册。
- 覆盖纪律：低活跃郡与 Svalbard/Jan Mayen 保留负面结果日志以便审计。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 来源优先级：Nkom → 运营商页 → 协会（Norsk Datasenterindustri https://www.datasenterindustrien.no/ B+，会员非设施普查）→ Business Norway（B）→ Doffin/anskaffelser（A 采购通知）→ DCD/Datacenter Forum（B）→ Baxtel（B-/C+）→ DataCenterMap（C+，地址/线索）。
- 运营商图谱（A 存在性/B 未来容量）：**Green Mountain**（A 组合页；SVG-Rennesøy 25 MW/22,600 m2 运营、TEL-Rjukan 50 MW/29,000 m2 运营、OSL-Enebakk 93 MW/75,000 m2 三栋楼、OSL-Hamar Heggvin 150 MW 园区/TikTok 租户/前三栋建成在用）；**Bulk OS-IX**（Oslo，Hans Møller Gasmanns vei 9）+ **Bulk N01**（Agder，3 km2 数据中心用地、营销至 1 GW——确认精确市政与许可后建设施行）；**STACK/DigiPlex 遗留**（Nkom SPV `SI OSL 01/02/03.1/03.2/04 AS`，Oslo Ulven/Fetsund/Ringerike 资产——地址/许可确认前 B/C）；**Nscale Glomfjord**（Meløy，30 MW 运营可扩 60 MW；Nkom 列 NSCALE DRIFT AS；Meløy/NVE/Statsforvalteren 核验）；**atNorth NOR01 Haugaland**（Tysvær Gismarvik，规划 36 ha、120 MW 初始阶段、350 MW 场地功率——许可/电网确认前为规划）；**WS Computing/Google Gromstul, Skien**（A：Skien 市政 2024-02 Google 6 亿欧元投资公告 + Statsforvalteren Datasenter 1 许可/Datasenter 2 听证；品牌按 WS Computing AS 记录）；**Lefdal Mine**（Vestland/Stad，A；Sigma2/HPE Olivia AI/HPC 使用，https://www.sigma2.no/our-data-centre）；**Datafjellet Bergen**（A 运营商页，Bergen 记录核验）；**Tydal Data Center/Bitdeer**（Nkom 列 Tydal Data Center AS；180 MW AI 声明 B 直到 Tydal/NVE/Statsforvalteren 记录）；**Exanorth**（Nkom 列加密挖矿；Namsskogan/Tunnsjødalen B 直到市政/电网记录）；**Tussa IKT / Tafjord Connect / NEAS IT**（区域运营商页 A + Nkom 列；Ørsta/Alesund/Kristiansund-Oppdal 核验）；**GlobalConnect**（北欧 colo A；挪威设施地址常目录派生，核验 Oslo/Trondheim 地址）；**Storespeed Halden**（Nkom 列；Magnora 称其运营 Halden DC）；**PolarDC**（A 运营商存在；DRA/HER01/MW 精确场地 C/B 直到市政记录；Nkom 列 POLARDC DRA AS）；**Magnora Scale Averøya**（100 MW 开发线索，非运营）；**Trollfjord IKT Senter**（Nkom 列；Stokmarknes/Hadsel 本地核验）；**Kolos Ballangen**（休眠历史线索，无新官方证据不计）。
- 北部：Troms and Finnmark 无已确认大型商业园区；Svartisen 以北电网约束使容量/日期核验尤其重要。

## 来源分级

- **A**：官方/一手证明该具体事实——Nkom 数据中心登记册、市政规划/建筑/postjournal 记录、Statsforvalteren/Miljødirektoratet 许可、NVE/Statnett 电网文件、Lovdata 法律/法规、运营商自有设施页。
- **B**：具名运营商/地点/日期/状态的可信二手源，但无底层许可/登记册。
- **C**：目录、市场报告、社交、谣言、无源追踪的媒体。仅线索。
- 设施置信规则：至少两个独立信号一致（可用时其一为 A 级）。新监管商业运营商：Nkom + 运营商页可证存在，但状态、地址与 MW 仍需独立源分级。

## 使用流程（探索/复核批次）

1. 拉 Nkom CSV，规范化法定名、组织号与加密挖矿旗标。
2. 将明显运营商名 join 官方运营商页。
3. 每个命名站点按 explorer-official.md 映射表赋 repo 分区与现行郡。
4. 搜市政规划/建筑门户找许可/案件 ID。
5. 搜 Statsforvalteren/Miljødirektoratet/Norske utslipp 污染许可与听证。
6. 搜 NVE/Statnett 与本地电网公司变电站、连接容量与限制。
7. 按字段分级；保留 Svalbard/Jan Mayen/Troms-Finnmark/低活跃郡的负面结果。
8. 遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:22Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] Nkom CSV 全量规范化并与运营商页 join（61 商业运营商逐行）。
- [ ] atNorth NOR01：Tysvær 土地/分区/发电机冷却许可与电网确认。
- [ ] Tydal Data Center/Bitdeer：Tydal/NVE/Statsforvalteren 记录的 180 MW 声明核验。
- [ ] 待核实：Bulk N01 精确市政与许可；Storespeed Halden 运营商页/市政记录；Google/WS Computing Gromstul Datasenter 2 许可决定。
