---
name: af-datacenter-methodology
location: scripts/expansion/world/country-skills/AF/SKILL.md
description: |
  Afghanistan (AF) parent-level methodology for data-center enumeration at province granularity (34 provinces).
  The country has no public national data-center register or construction-permit portal, so enumeration joins
  MCIT/ANDC procurement (ANDC, second-DC tender, MoMP data center, NIXA), ATRA entity licensing, DABS energy
  evidence, operator facility pages (ALEF, AryanICT, ACG Kabul), and local/trade press. Market is small and
  Kabul-centric; every non-Kabul province is a negative-control sweep except Nangarhar (MCIT planned second
  National Data Center) and ACG directory-only multi-city claims (C). No hyperscaler public region exists.
  Routes to explorer-official.md (state/regulator/energy pipeline) and explorer-industry.md (operator/directory/
  press pipeline).
---

# AF · 阿富汗数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：阿富汗没有公开的国家数据中心登记册或施工许可门户，枚举必须由 MCIT/ANDC 采购、ATRA 实体许可、DABS 电力证据、运营商设施页面与本地/行业媒体拼接而成；市场小而集中于喀布尔（Kabul），非喀布尔省份多数为阴性对照，Nangarhar 仅有官方计划信号（第二国家数据中心）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供阿富汗探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：MCIT/ANDC 采购与标书、ATRA 许可、阿富汗电信、DABS/电力、NIXA、云区域阴性对照、34 省官方策略 |
| `explorer-industry.md` | 行业管线：运营商设施页面（ALEF/AryanICT/ACG）、行业媒体与目录、逐省行业工作流、提取模式 |

## 核心结构事实（框定每次搜索）

1. **无登记册**：阿富汗没有公开的国家数据中心登记册、施工许可登记册或可检索的市级建筑许可门户；枚举必须从 MCIT/ANDC 采购、ATRA 实体许可、运营商页面、DABS 能源证据、NIXA、IFI/USAID/世行记录和本地媒体构建。
2. **喀布尔锚点**：最高置信市场是 Kabul，已核实锚点包括 ANDC、MCIT 第二数据中心/DR 招标、矿业石油部数据中心、NIXA、ALEF Technology、AryanICT、ACG Kabul、DABS/Tarakhil DR 计划以及多个喀布尔承包商案例。
3. **ANDC 状态**：阿富汗国家数据中心（ANDC）为政府数据中心（A）；独立站点曾返回默认页/404，以 MCIT 为官方来源；关键升级招标由 Digital CASA / World Bank（IDA-D2820）资助。
4. **第二数据中心**：MCIT 在喀布尔市中心发布了第二个数据中心招标（tender-only，A-for-tender）；Nangarhar 有官方计划声明（第二国家数据中心将设在楠格哈尔省），但无完工/容量证据，记录为 **planned / no capacity**。
5. **MoMP DC**：矿业石油部数据中心 + MCRS，来源称 160 TB 并连接 ANDC（A，政府数据中心）。
6. **NIXA 是网络设施**：NIXA 是喀布尔的物理 IXP（含缓存/根 DNS 上下文），是运营商集聚信号，但成员身份不等于数据中心设施。
7. **无超大规模区域**：官方 AWS/Azure/GCP/OCI 列表中无阿富汗公共区域或本地区域；电信/国家的 "cloud" 语言是本地负载或服务证据，不是超大规模自有 DC 证据。
8. **e& 公共云 RFP**：Etisalat Afghanistan 2025-2026 RFP 提及阿富汗境内托管、未经批准不可迁移的 Public Cloud 数据中心——采购/服务证据（A/B），设施证据（C）直到地址/运营商公开。
9. **语言三通道**：英文（data center/colocation/hosting/Tier III）+ 达利语（مرکز داده/مرکز معلوماتی/هاستینگ/سرور/ابر）+ 普什图语（ډیټا مرکز/د معلوماتو مرکز/سرور）。
10. **电力限制**：Panjshir、Nuristan、Paktika 缺乏活跃 DABS 运营是重要阴性背景；不得从变压器/发电机/MVA/电厂容量推断 IT MW。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§3/§6、explorer-industry.md §3/§4）

```text
site:mcit.gov.af "data center"
site:mcit.gov.af "ANDC" OR "National Data Center"
site:mcit.gov.af "DRDC" OR "disaster recovery"
site:mcit.gov.af "مرکز داده" OR "ډیټا مرکز"
site:atra.gov.af "data center" OR hosting OR cloud
"Digital CASA Afghanistan" "data center"
"World Bank" "Afghanistan" "NIXA" "data center"
site:main.dabs.af "data center"
"Tarakhil" "data center" OR "Chaman Hazouri" "DABS" "data center"
site:afghantelecom.af "data center" OR datacenter OR "server"
"Kabul" "data center" "co-location"
"ALEF" "data center" Kabul
"AryanICT" "data center" Afghanistan
"Asia Consultancy Group" "data center" Afghanistan
"Etisalat Afghanistan" "Public Cloud data center"
"کابل" "مرکز داده"
"{province}" "data center" Afghanistan
site:pajhwok.com "{province}" "data center"
site:bakhtarnews.af "{province}" "data center"
"{province_dari}" "مرکز داده"
"{province_pashto}" "د معلوماتو مرکز" OR "ډیټا مرکز"
site:datacentermap.com/afghanistan "{province}"
"Afghanistan" "AWS Region" site:aws.amazon.com
```

## 官方/监管管线要点（详见 explorer-official.md）

- **MCIT/MoCIT + ANDC**：首选入口（mcit.gov.af/en），搜索 `data center`、`ANDC`、`National Data Center`、`NIXA`、`DRDC`、`cloud`、`server` 及达利/普什图语词；MCIT/ANDC 页面针对具名政府设施/招标/计划为 **A**；招标对采购事件为 A，对建成状态仅为 B/C。
- **ATRA**：用于实体授权（AWCC、Roshan/TDCA、e&/Etisalat、M1/MTN、Afghan Telecom/Salaam、Wasel 及 ISP），不是设施枚举；许可/监管通知对许可状态为 A，对 DC 设施为 C。
- **阿富汗电信/国家公司**：FTTX/NOC 页面确认光纤与数据服务，但**不是**公开数据中心设施；GTR 案例（ANDC、UNDP WEPS DR、AUAF server farm、AFMIS DC）为 **B 厂商案例**，需匹配政府页面。
- **DABS/电力**：DCD 报道 USAID/DABS 计划在 Tarakhil 电厂建 DR 数据中心、Chaman Hazouri 有现存 DABS 数据中心（B 计划证据）；电力规则：不从变压器/发电机/MVA 推断 IT MW。
- **云区域阴性对照**：每次运行都检查 AWS/Azure/GCP/OCI 官方区域列表（均无阿富汗区域）；Cloudflare 无阿富汗境内城市。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **ALEF Technology**（Kabul，A）：运营商页面声明 Kabul 专职企业级数据中心，提供托管/colo。
- **AryanICT**（Kabul，A/B）：2024-05-09 公司宣布阿富汗数据中心，地址为 Kabul；录入容量前需核实具体设施/地址。
- **ACG Kabul**（A/B）：ACG 官方 ICT 页面确认 Kabul HQ 5,000 sq ft 数据中心与 co-location；目录给出 Shashdarak 2nd 地址/规格。
- **ACG 多城声明**（C）：DataCenterMap 公司档案声称 Herat、Kandahar、Mazar-e-Sharif、Jalalabad、Kunduz 有 ACG 数据中心，但无独立运营商页面；仅目录线索。
- **DABS/Tarakhil DR 计划**（B）、**GTR 案例**（B，默认 Kabul 需注明）、**Pamir Alpha Technologies**（B/C，Network World 引导）、**ANHDC/ASDC 自然灾害数据中心**（B/C，iMMAP/ANDMA 需核实）。
- **AWCC/Roshan/Afghan Telecom 等**：目录条目（datacenters.com 的 Afghan Wireless Kabul 条目）为 **C**，直到运营商具名设施。
- **目录纪律**：DataCenterMap/DataCenterCatalog/datacenters.com/Cloudscene/PeeringDB 仅作线索；Uptime Institute 阿富汗页无可见奖项 = 本地 Tier 声明未认证。

## 来源分级

- **A** = 主要或控制性来源：MCIT/MoCIT、ANDC、ATRA、DABS、Afghan Telecom/Salaam、e&/Etisalat Afghanistan 招标、运营商官方设施页面、World Bank/IFI 采购、政府-公司声明、Uptime Institute 证书。
- **B** = 具名项目/运营商/地点的强二级来源：DCD、Network World、Pajhwok、Ariana、Bakhtar、TOLOnews、APNIC、Chatham House、具名承包商案例研究。
- **C** = 仅线索：DataCenterMap、DataCenterCatalog、datacenters.com、PeeringDB、Cloudscene、Mordor/市场报告、托管营销、目录、社交帖子、仅光纤/IXP 证据。
- 状态语义：`operational` 需近期运营证据；`planned` 需官方计划声明；`tender-only` 仅采购事件；`directory-only` 为 C；容量仅在带单位（MW/kW/racks/sqm/sq ft/TB）时记录，绝不从发电机/变压器/电厂数字推断。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 AF 记录，检查已录入 facility 与种子列表（ANDC、MoMP DC、ALEF、AryanICT、ACG Kabul、NIXA、DABS/Tarakhil、e& cloud、GTR 案例等）。
2. 逐省扫描：Kabul 详尽扫描；Nangarhar 检索 MCIT 第二 NDC 后续招标/调试；其余 32 省执行阴性对照紧凑扫描后才记录 "no public project found"。
3. 官方优先：MCIT/ANDC → ATRA → DABS → 运营商页面 → 行业/本地媒体 → 目录；禁止把线索提升到超过最弱必要环节。
4. 输出 schema：`{country_code: AF, country_name: Afghanistan, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目省份写入 `no_projects: true`。
5. 保留阴性对照记录（云区域、Uptime、NIXA 网络属性），不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] Nangarhar 第二国家数据中心：追踪 MCIT 后续招标/调试/容量证据。
- [ ] DABS/Tarakhil DR 数据中心：寻找 DABS/USAID 完工证明以升级 B 计划证据。
- [ ] AryanICT 数据中心：核实具体设施地址与容量。
- [ ] ACG 多城声明（Herat/Kandahar/Mazar/Jalalabad/Kunduz）：逐一寻找独立运营商页面。
- [ ] e& 公共云数据中心：等待地址/运营商公开后升级设施证据。
- [ ] Pamir Alpha Technologies、ANHDC/ASDC：寻找主源页面。
- [ ] 云区域与 Cloudflare 阴性对照：每次运行复查。
