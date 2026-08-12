---
name: ls-datacenter-methodology
location: scripts/expansion/world/country-skills/LS/SKILL.md
description: |
  莱索托（Lesotho, LS）数据中心发现与审计方法论（小型市场）。10 个 district 全覆盖（Butha-Buthe 兼搜
  Botha-Bothe 拼写）。无国家 DC 登记册，需拼接 LCA 牌照、gov.ls/MICSTI e-Gov、土地（LAA/LNDC）、环评
  （environment.gov.ls）、电力（LEC/LEWA/LHDA）与运营商证据。已证种子：Vodacom Lesotho 双数据中心
  （Maseru West + Lekokoaneng，官方页背书 colocation）、LCA 数据中心（Maseru，托管 LIXP）、Mohale's Hoek
  政府数据中心（另有两个政府 DC，位置未公开，2021 EOI 佐证）；ETL/Econet 为 Maseru lead；Kobong 水电+AI
  数据中心项目（Mokhotlong）仅为 announced 管线。无 AWS/Azure/GCP/OCI 区域，最近公共区域在南非。
  详见 explorer-official.md 与 explorer-industry.md。
---

# LS · 莱索托数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：莱索托没有公共国家 DC 登记册，枚举需拼接监管、政府 ICT、土地、环评、能源、运营商与云区域证据。
> 已证设施宇宙很小（Vodacom 双中心、LCA/LIXP、政府 DC 项目）；Kobong 为 announced 管线，不得升级为设施。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供按 10 区粒度复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：LCA 牌照与咨询通知、gov.ls/MICSTI e-Gov（Mohale's Hoek 机房 + 2021 EOI）、LAA/LNDC 土地、environment.gov.ls EIA、LEC/LEWA/LHDA 电力、LIXP、云区域缺省；设施种子表与逐区策略。 |
| `explorer-industry.md` | 行业/厂商发现：Vodacom/ETL/LCA/LIXP/Convalt 扫描、Kobong 管线处理、本地/贸易媒体、目录负向控制、负向搜索协议。 |

## 核心结构事实（框定每次搜索）

1. **10 区模型**：Maseru、Berea、Butha-Buthe（兼搜 Botha-Bothe）、Leribe、Mafeteng、Mohale's Hoek、Mokhotlong、Qacha's Nek、Quthing、Thaba-Tseka。
2. **无国家 DC 登记册**：枚举 = LCA 牌照/咨询 + gov.ls/MICSTI e-Gov + LAA/LNDC 土地 + 环评 EIA + LEC/LEWA/LHDA 电力 + 运营商页 + 云区域缺省核查。
3. **已证种子**：Vodacom Lesotho 官方页点名两个数据中心（Maseru West、Lekokoaneng）并销售 colocation（A 级存在）；LIXP 官方页确认 2017 年迁入 LCA 数据中心（A 级机构设施）；gov.ls + 2021 e-Gov EOI 支持 Mohale's Hoek 政府 DC 与共三个政府 DC。
4. **Kobong 管线保守处理**：Convalt/US 使馆 + 贸易媒体支持已批准的 MoA/$6.2bn 投资故事；无可行性、EIA、LEWA 牌照、土地或建设证据前保持 announced。
5. **无 hyperscaler 区域**：AWS/Azure/GCP/OCI 官方表均无 LS；最近公共区域在南非；hyper-scaler 引用按 tenant/partner/cache/edge lead 处理。
6. **区属注意**：Lekokoaneng 在 Maseru-TY/Berea 一侧（Berea 区，凭 parcel 记录核验）；两个非 Mohale's Hoek 政府 DC 位置未公开，不得擅自归区。
7. **发电容量 ≠ DC 负载**：Kobong 水电/太阳能数字是发电声明，不得换算为数据中心 MW；MVA/kVA 不擅自换算。
8. **LTA/LCA 去重**：新旧材料中为同一监管机构，按法人/地址去重；IXP 存在不算独立 DC（LIXP 宿主于 LCA DC）。

## 查询模式（复制粘贴模板见 explorer-official.md / explorer-industry.md）

```text
site:lca.org.ls "data centre" OR "data center" OR datacentre
site:gov.ls "data centre" OR "data center" OR "Mohale's Hoek"
site:communications.gov.ls "data centre" OR cloud OR "e-Government"
site:environment.gov.ls "data centre" OR EIA
site:lec.co.ls OR site:lewa.org.ls "data centre" OR "large power" OR substation
site:laa.org.ls OR site:lndc.org.ls "data centre" OR lease OR "industrial estate"
"Vodacom Lesotho" "Maseru West" "Lekokoaneng"
"Econet Telecom Lesotho" "data centre" OR hosting
"LIXP" "LCA data centre"
"Kobong" "Convalt" "AI Data Centre" Lesotho
"{district}" Lesotho "data centre" OR "data center" OR datacentre
site:lena.gov.ls OR site:lestimes.com OR site:selibeng.com "{district}" "data centre" OR "ICT" OR UPS
```

## 官方/监管管线要点（详见 explorer-official.md）

- **LCA**（lca.org.ls）：现行监管机构；`telecommunications-licensees` 列出 Econet、Vodacom、LEC Communications、Comnet、Starlink、Jenny 等；咨询通知为逐条发布，用 site 搜索。
- **gov.ls / MICSTI**：Mohale's Hoek 机房（power-house 文章，确认机房 + 双房 + e-Gov 基建组件 + 五座塔）；2021 EOI PDF（A 级：三个政府 DC + Mohale's Hoek 委托/整合范围）；AfDB MapAfrica/Phase II 文档佐证。
- **LAA / LNDC**：租约/地籍/工业地产（Tikoe、Maputsoe、Butha-Buthe、Mafeteng）；EIA Clearance Certificate 属投资流程。
- **环境/能源**：environment.gov.ls（Environment Act 2008）、LEC/LEWA/LEGCO/DoE/LHDA（'Muela、Katse、Mohale、Polihali）。
- **云缺省**：AWS（Cape Town）、Azure（South Africa North/West）、GCP（Johannesburg 区域锚点）、OCI（Johannesburg/South Africa Central）——无 LS 区域。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Vodacom Lesotho**（vodacom.co.ls/business/fixed-solutions/）：官方页点名 Maseru West + Lekokoaneng 双中心并营销 colocation——A 级存在/名称/位置；容量/电力/parcel 待补。
- **ETL/Econet Telecom Lesotho**：持牌在位者 + LIXP peer；目录列 Maseru 为 C，需 ETL/LCA/土地/电力/采购证据升 A。
- **LCA 数据中心 / LIXP**：互联证据（A 级存在经 LIXP 页；lixp.org.ls/about + PeeringDB ix/5015），非独立设施。
- **Kobong（Convalt Energy）**：DCD/Investment Monitor/TechAfricaNews 报道 $6.2bn MoA 与 12GW 水电+AI DC 规划——announced 管线；升级触发条件见 explorer-industry.md。
- **负向协议**：每区查媒体变体、LCA 牌照、gov.ls/e-Gov、EIA、电力、土地、具名运营商（Vodacom、ETL、LCA、LIXP、LECC、Comnet、Jenny、Starlink、Liquid、Huawei、Schneider、Vertiv）后才写 defensible negative。
- **目录**（DataCenterMap/datacenters.com/Baxtel）：仅发现线索；贸易媒体 "two operational data centers" 是市场下限而非穷尽计数。

## 已知设施/项目与证据状态

| 设施/项目 | 区/地点 | 状态与证据 |
|---|---|---|
| Vodacom Lesotho Maseru West 数据中心 | Maseru | 运营/运营商在售，A 级官方页；容量/电力待核。 |
| Vodacom Lesotho Lekokoaneng 数据中心 | Berea（凭 parcel 核验） | 运营/运营商在售，A 级官方页；不得与 Maseru West 合并。 |
| LCA 数据中心 / LIXP 宿主 | Maseru | 运营机构/互联设施，A 级存在（LIXP 页）；规格 B 级。 |
| Mohale's Hoek 政府数据中心 | Mohale's Hoek | 建成/委托/整合证据（gov.ls + 2021 EOI，A 级）。 |
| 另两个政府数据中心 | 位置未公开（likely Maseru 候选） | 存在为 A 级政府项目资产；地点未决，不得擅自归区。 |
| ETL/Econet 数据中心 lead | Maseru（likely） | 商业/telco lead，B/C 级；需 ETL/官方记录点名设施。 |
| Kobong 水电 + AI 数据中心项目 | Mokhotlong（Kobong） | Announced/approved MoA（B 级公告），非设施；待可行性/EIA/LEWA 牌照/土地/建设。 |

## 更新节奏

- 每批次：重跑 LCA 牌照/咨询、gov.ls e-Gov、Vodacom/ETL 页、LIXP、Kobong 生命周期触发器、本地媒体与云缺省。
- 每季度：检查 AfDB e-Gov Phase II 交付、Mohale's Hoek 集成进展与 Kobong 许可/采购；重跑 10 区负向协议。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（10 区粒度）；本 skill 作为国家层参考注入。
