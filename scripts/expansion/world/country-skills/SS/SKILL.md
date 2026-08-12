---
name: ss-datacenter-methodology
location: scripts/expansion/world/country-skills/SS/SKILL.md
description: |
  南苏丹（South Sudan, SS）数据中心发现与审计方法论。10 个 state 覆盖。无商业 colo 市场、无设施登记册、
  无 DC/colo 专属牌照类别；监管者为 NCA（National Communication Authority，依据 National Communication
  Act 2012，非 "NTC"）。唯一可计数的政府 DC 种子为 Juba 国家数据中心（NDC，2026-04 部长称在建且过半，
  B 级直到官方页/招标/委托记录出现）。其余：SSIGW 国际网关（2014 起运营，网关非 DC）、Liquid/Muya
  Juba–Uganda 光纤、NCT Juba–Torit、Bayobab/MTN Digital Infrastructure 牌照、MTN/Zain/Digitel 核心机房。
  全国无电网（仅 Juba/Malakal/Wau 孤立网络），无 IXP（PeeringDB 为空），无 AWS/Azure/GCP/OCI 区域。
  冲突背景（Upper Nile/Unity）影响州级核查。英语为主 + 阿拉伯语变体。详见 explorer-official.md 与
  explorer-industry.md。
---

# SS · 南苏丹数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：SS 是数字基建极薄的市场——World Bank 2022 诊断确认当时无正常运作的 carrier-neutral DC、无 IXP；
> 一切可数内容集中在 Juba（Central Equatoria）。电力（无国家电网）与冲突背景是核查的强制维度。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供按 10 州粒度复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：NCA 牌照与监管、MICT&PS、国家数据中心（NDC）与 SSIGW、能源/电网证据、云区域缺省、运营商种子表、10 州覆盖矩阵与优先级分层。 |
| `explorer-industry.md` | 行业/厂商发现：Eye Radio/Radio Tamazuj/Sudans Post/Ecofin/TechAfrica 等媒体、运营商/载波/卫星扫描、互联记录（IXP 为空）、状态动词映射、验证配方与发现管线。 |

## 核心结构事实（框定每次搜索）

1. **监管者修正**：SS 法定电信监管者是 NCA（National Communication Authority，2012 年法案，2015-06 全面运作，DG Hon. Rizig Dominic Samuel）；"NTC" 属于苏丹/巴基斯坦，勿混淆。
2. **NDC 是唯一可计数政府 DC 种子**：Juba；2026-01 NCA 成立 Gateway Services and Data Center Oversight Committee（MGI Communications AG 技术支持），2026-04 部长称在建且 "halfway complete"——B 级（媒体转述官员），容量/地址/运营方/时间线全部未公开；出现 NCA/MICT&PS 页、采购、委托或运营商页才升 A。
3. **SSIGW 是网关不是 DC**：Juba 国际语音/SMS 网关（约 2014 起运营），World Bank 2022 诊断 A 级存在；单独记录类型。
4. **无 IXP**：PeeringDB API（country=SS）返回空（2026-08-12，A-negative）；ISOC SS 分会 2025-06 办 Peering Roadshow 为能力建设；"Juba IXP" 保持 planned/absent。
5. **电力硬约束**：无国家电网，仅 Juba/Malakal/Wau（+Renk）孤立网络；Juba Thermal ~33 MW 柴油（扩至 100 MW 计划），停电频繁——任何真实 DC 需自备发电/UPS 证据。
6. **无 hyperscaler 区域**：AWS/Azure/GCP/OCI 官方表均无 SS；Starlink（2024 持牌）为连接性。
7. **冲突背景强制**：2025–2026 年 Upper Nile（Nasir）与 Unity（Mayom/Koch）战斗、Jonglei/Warrap/Lakes 牛袭、苏丹战争难民——州级设施声明须日期戳并复核；被毁/被抢电信设施可能性高。
8. **光纤是授权/走廊不是 DC**：Liquid Juba–Uganda（约 200 km）、Muya、NCT Juba–Torit（2022–2023 交付）、Bayobab/MTN Digital Infrastructure（2025-10-16 生效 15 年牌照）、2,400–2,700 km 国家骨干计划（2025-12 起）。

## 查询模式（复制粘贴模板见 explorer-official.md / explorer-industry.md）

```text
site:nca.gov.ss ("data centre" OR "data center" OR "gateway" OR "licence" OR Starlink)
site:mictps.gov.ss ("data centre" OR "fiber" OR "backbone" OR "national data")
"national data centre" OR "national data center" "South Sudan" OR Juba
"SSIGW" OR "South Sudan International Gateway"
"Juba" ("data centre" OR "server room" OR "server farm" OR generator OR diesel OR substation)
"MTN South Sudan" OR "Zain South Sudan" OR "Digitel" "data centre" OR server
"Liquid" OR "Muya" OR "NCT" OR "Bayobab" "South Sudan" fiber OR fibre OR PoP
site:eyeradio.org OR site:radiotamazuj.org OR site:sudanspost.com ("data centre" OR "data center")
site:ecofinagency.com OR site:techafricanews.com "South Sudan" "data center"
"مركز بيانات" OR "مركز البيانات" "جنوب السودان"
"{state}" OR "{capital}" "South Sudan" "data centre" OR "data center"
"South Sudan" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region")
```

## 官方/监管管线要点（详见 explorer-official.md）

- **NCA**（nca.gov.ss）：牌照（MTN 15 年、Zain、Digitel、Starlink 卫星/VSAT、Liquid/Muya/NCT 光纤基础设施牌照、Bayobab/MTN Digital Infrastructure）；每条牌照是授权非设施；USAF（2020 设立，2% 收入）为未来骨干/DC 资金池。
- **MICT&PS**（mictps.gov.ss）：国家数据中心（NDC）主管；Cybercrime and Computer Misuse Act 2025；Data Protection Act 推进中；国家 ICT Authority 筹建中；UN EGDI 0.1191（倒数第二）——Juba 之外几乎没有 e-gov 数字基建。
- **能源**：SSEC/Juba Thermal、AfDB 孤立网络事实、World Bank Energy Access Project——用电佐证设施，不单独建记录。
- **World Bank 2022 诊断**：A 级基线（无 carrier-neutral DC、无 IXP、推荐 Juba DC+IXP）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商**：MTN（约 1.7M 用户，Juba 核心/DR 机房，C/B）、Zain（Juba 核心，C/B）、Digitel（首家全南苏丹业主运营商，2021-07 启动，2024-06 5G 试验，Torit 2024-10、NBEG 2026-05 扩展，C/B）、Gemtel（2006 持牌，历史/区域，C）、Vivacell（2018-02 牌照暂停，C 历史）。
- **载波**：Liquid（A 级线路存在，C 级设施细节）、Muya（B/C）、NCT（B 公司页，经 NCA 验证）、Bayobab（B 公司页）、SSIGW（A 存在，非 DC）。
- **卫星/银行**：Starlink（A 级牌照，C 级设施）、BoSS NIPS 与商业银行机房（C）。
- **验证配方**：任何正向命中需 ≥2 独立渠道；Juba 卫星影像（4.85°N, 31.6°E）核对 NDC 在建 vs 运营；容量 sanity check（无电网下 10+ MW 声明不现实）；NDC/SSIGW/PoP/核心机房/银行机房去重，Juba 每个物理站点一条记录。
- **状态动词映射**：announces/plans/MoU=intent（C）；licence/approved tariffs=authorisation（A/B）；under construction/halfway complete=build（官方 A、媒体 B）；launched/commissioned=live；trial=pilot。

## 已知设施/项目与证据状态

| 设施/项目 | 州/地点 | 状态与证据 |
|---|---|---|
| 国家数据中心（NDC） | Central Equatoria（Juba） | 在建、过半（2026-04，B 级媒体转述）；容量/地址/运营方未公开；首个可计数的 SS DC 记录候选。 |
| SSIGW 国际网关 | Juba | 运营中（约 2014 起，A 级 World Bank）；网关类型，非 DC。 |
| Liquid Juba PoP / Juba–Uganda 光纤 | Juba | A 级线路/协议；PoP/NOC 为互联点，非 DC。 |
| Muya Fiber / NCT Juba–Torit / Bayobab 牌照 | Juba / Eastern Equatoria | 光纤授权/走廊（B/C），非 DC。 |
| MTN / Zain / Digitel 核心机房 | Juba | C/B 核心/DR 证据；无公开 colo 页不建设施记录。 |
| Gemtel / Vivacell | Juba/Yei 等 | C 历史/区域；无 DC 证据。 |
| Starlink 等卫星 | 全国 | A 级牌照；连接性，非 DC。 |

## 更新节奏

- 每批次：重跑 NCA/MICT&PS 官方面、Eye Radio/Radio Tamazuj/Sudans Post/Ecofin/TechAfrica 媒体、运营商/载波页与 10 州 4 重扫描（媒体/运营商/官方/互联聚合）；盯 NDC 承包商授标、站点地址、容量与委托事件。
- 每季度：重核 PeeringDB IX（SS 应为空）、hyperscaler 官方区域表、ISOC SS 分会动向；按冲突报告复核 Upper Nile/Unity/Jonglei 州级声明。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（10 州粒度）；本 skill 作为国家层参考注入。
