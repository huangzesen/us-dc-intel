---
name: et-datacenter-methodology
location: scripts/expansion/world/country-skills/ET/SKILL.md
description: |
  Ethiopia (ET) data-center enumeration methodology. Division model: 13 manifest divisions (Addis Ababa; Afar; Amara/Amhara; Benshangul-Gumaz; Dire Dawa; Gambela Peoples; Harari People; Oromia; Sidama; Somali; Southern Nations/legacy SNNPR; Southwest Ethiopia Peoples; Tigrai/Tigray). Administrative caution: South West Ethiopia created 2021, South Ethiopia and Central Ethiopia split from SNNPR 2023 — keep SNNPR as manifest bucket but search newer names when clearing it. No public national datacenter registry and no comprehensive planning-permit search; enumeration joins ECA (now explicitly lists Data Center Service Provider License and Hosting Service Provider License), EIC investment permits, IPDC/SEZ park records, EEP/EEU power evidence, INSA/government cloud, local permits, operator pages, Uptime. Main cluster: Addis Ababa (Ethio ICT Park) — Raxio ET1 (up to 800 racks/3MW), Wingu Africa (10 MW/800 racks at full build), Redfox, Ethio telecom Gola Sefer modular DC, Safaricom Ethiopia core DC (+Adama/Dire Dawa planned), Dashen Bank enterprise DC, ADDIX, crypto/data-mining segment (Phoenix 80 MW PPA lead). No AWS/Azure/GCP/OCI region listed; local cloud (Cloud 251, Ethio telecom, Wingu Cloud Exchange) is not hyperscaler. Read this before running ET exploration/audit batches. Routes to explorer-official.md (ECA/EIC/IPDC/power/local-permit playbook) and explorer-industry.md (operator/trade-press/regional playbook).
---

# ET · 埃塞俄比亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：埃塞俄比亚无公共国家数据中心登记册、无综合公共规划许可检索。枚举靠拼接「ECA 电信/数据中心/托管牌照 + EIC 投资许可 + IPDC/SEZ 园区分配 + EEP/EEU 电力证据 + INSA/政府云 + 当地许可/土地 + 运营商设施页 + Uptime」。物理集群主在亚的斯亚贝巴 Ethio ICT Park。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：ECA 牌照类别、EIC 投资、IPDC/SEZ 园区、EEP/EEU 电力、INSA/政府云与当地许可、官方设施种子表、超大规模护栏、13 分区逐区策略、提取字段与置信规则 |
| `explorer-industry.md` | 行业/厂商管线：高价值媒体源、运营商/项目扫描、行业到官方验证 pivot、区域搜索剧本、聚合器处理、超大规模核查、最终证据规则 |

## 核心结构事实（框定每次搜索）

1. 行政划分：**13 个 manifest 分区**：Addis Ababa；Afar；Amara（Amhara）；Benshangul-Gumaz（Benishangul-Gumuz）；Dire Dawa；Gambela Peoples；Harari People；Oromia；Sidama；Somali；Southern Nations（遗留 SNNPR 桶）；Southwest Ethiopia Peoples；Tigrai（Tigray）。**行政注意**：2021 年设立 Southwest Ethiopia Peoples；2023 年 South Ethiopia 与 Central Ethiopia 自 SNNPR 拆分——保留 SNNPR 为 manifest 桶，但清桶时搜新名（`South Ethiopia`、`Central Ethiopia`、`Wolaita`、`Gamo`、`Gofa`、`Hadiya`、`Gurage` 等）。
2. **无公共国家登记册、无综合许可检索**。枚举多轨：电信/数据中心牌照、投资许可、工业园/SEZ 分配、电力证据、当地建设/土地记录、运营商设施页。
3. **ECA 现明确列出 Data Center Service Provider License 与 Hosting Service Provider License 类别**（https://www.eca.et/services/）——商业数据中心/托管运营商的关键官方路径（A）。ECA 还管 ADDIX 与个人数据保护公告 1321/2024 的控制者/处理者注册。
4. **主物理集群 = 亚的斯亚贝巴**，尤其 **Ethio ICT Park / ICT Park**（城市东南缘）。高价值种子：Raxio Ethiopia、Wingu Africa、Redfox、Ethio telecom Gola Sefer 模块化 DC、Safaricom Ethiopia Addis 核心 DC、Dashen Bank 企业 DC、本地云服务、加密/数据挖矿设施。次级：Oromia（Adama、Bishoftu、Burayu、Sebeta、Dukem、Modjo、Sululta、Holeta、Jimma）、Amhara（Bahir Dar、Kombolcha、Debre Berhan、Gondar、Dessie）、Dire Dawa、Sidama/Hawassa。其余分区通常为负面搜索。
5. **无超大规模云区域**：AWS/Azure/GCP/Oracle OCI 官方区域/位置页未列埃塞俄比亚。本地/主权云服务（Cloud 251、Ethio telecom cloud、Wingu Cloud Exchange）按本地运营商或主机设施枚举，不按 AWS/Azure/GCP/OCI 基建。
6. 拼写变体：`data centre / data center / datacentre`；`Addis Ababa / Addis Abeba`；`Amara / Amhara`；`Benshangul-Gumaz / Benishangul-Gumuz`；`Tigrai / Tigray`；`Jigjiga / Jijiga`；`Debre Birhan / Debre Berhan`。阿姆哈拉语次级词：`ዳታ ሴንተር / የኢንፎርሜሽን መዳረሻ / የሰርቨር ክፍል / ኢንተርኔት / ክላውድ / ኮምፒውተር / ቴክኖሎጂ`。
7. 生命周期动词逐字捕获：`MoU / plans / targets / considering / feasibility / seeks investors` = 意图；`secured land / breaks ground / under construction / launched / inaugurated / operational / hosts / leased / certified / PPA signed` = 更强但需源分级。
8. 加密/数据挖矿是实质细分：EEP 与 ECA 声明使其成为真实 DC 细分，但许多文章不点名 SPV/场地/MW——未点名保持 C。

## 查询模式（复制粘贴模板见 explorer-official.md §1-5 与 explorer-industry.md §1-4）

- ECA：`site:eca.et "Data Center Service Provider License"`、`site:eca.et "Hosting Service Provider License"`、`site:eca.et "data center" OR "data centre" Ethiopia`、`site:eca.et "{operator}" licence OR license`、`site:eca.et "internet exchange" OR ADDIX`、`"Ethiopian Communications Authority" "{operator}" "data center"`。
- EIC：`site:investethiopia.gov.et "data center" OR "data centre"`、`site:investethiopia.gov.et "special economic zone" "ICT"`、`site:investethiopia.gov.et "investment permit" "{operator}"`。
- IPDC/MinT：`site:ipdc.gov.et "data center" OR "ICT"`、`site:ipdc.gov.et "Kilinto" "ICT"`、`site:ipdc.gov.et "Bole Lemi" "{operator}"`、`site:mint.gov.et "ICT Park" "data center"`、`"Ethio ICT Park" "{operator}"`。
- 电力：`site:eep.com.et "data center" OR "data miner" OR "crypto"`、`site:eep.com.et "{operator}" "MW" OR "MVA"`、`site:eeu.gov.et "data center" OR "{operator}"`、`"Ethiopian Electric Power" "data mining" Ethiopia MW`、`"Ethiopian Electric Power" "Phoenix Group" "80 MW"`、`"Ethiopian Electric Utility" "Wingu" "data center"`。
- 政府/当地：`site:insa.gov.et "data center" OR cloud`、`site:addisababa.gov.et "data center" OR "server"`、`"Addis Ababa" "Building Permit" "{operator}"`、`"{city}" Ethiopia "land lease" "ICT" OR "data center"`、`"Fayda" Ethiopia "data center"`。
- 行业媒体（B）：`site:datacenterdynamics.com/en/news/ Ethiopia "data center" OR "data centre"`、`site:shega.co Ethiopia "data center" OR "data centre"`、`site:capitalethiopia.com Ethiopia Wingu OR Raxio`、`site:addisfortune.news Safaricom "data centre"`、`site:ethiopianmonitor.com "data miner" OR "data mining"`、`site:thereporterethiopia.com "ICT Park" Wingu OR Raxio`、`site:fanamc.com Ethiopia "modular data center"`、`site:ena.et Ethiopia "Tier III" OR Wingu`。
- 运营商：`"Raxio" Ethiopia "ICT Park" "800 racks" "3MW"`、`"Wingu" Ethiopia "ICT Park" "10MW" "800 racks"`、`"Ethio telecom" "Gola Sefer" "modular data center"`、`"Safaricom Ethiopia" "data centre" "Adama" OR "Dire Dawa"`、`"Redfox" "ICT Park" "modular data center" Ethiopia`、`"Dashen Bank" "Tier III" "data center"`、`"Phoenix Group" Ethiopia "80 MW" "power purchase agreement"`。
- 验证 pivot：`site:eca.et "{operator}" "Data Center Service Provider License"`、`site:investethiopia.gov.et "{operator}" "investment permit"`、`site:ipdc.gov.et "{operator}" OR "{park}" "data"`、`site:eep.com.et "{operator}" MW OR MVA`、`site:uptimeinstitute.com "{operator}" Ethiopia`、`"{operator}" "Ethiopian Electric Power" MW Ethiopia`。
- 分区模板：`"{division}" Ethiopia ("data center" OR "data centre" OR datacentre)`、`"{town}" Ethiopia ("crypto mining" OR "bitcoin mining" OR "data mining") (MW OR EEP)`、`"{industrial park}" Ethiopia ("data center" OR ICT OR cloud OR server)`、`site:eca.et "{operator}" OR "{town}" "data center"`、`site:eep.com.et "{operator}" OR "{town}" MW OR MVA`。

## 官方/监管管线要点（详见 explorer-official.md）

- ECA（https://www.eca.et/ A）：先用于商业电信/数据中心/托管/IXP/VISP 证据；colo/云设施尽量 join ECA。ECA 记录点名运营商/服务时为 A；媒体引 ECA 但无底层公开记录为 B。
- EIC（https://investethiopia.gov.et/ A）：投资许可/一站式记录/激励/SEZ 语境；作为 join 源而非唯一发现路径。
- IPDC（https://www.ipdc.gov.et/，园区路由 https://www.ipdc.gov.et/service/parks/ A）：园区清单含 Bole Lemi、Kilinto、Adama、Hawassa、Dire Dawa、Kombolcha、Debre Birhan、Mekelle、Bahir-Dar、Jimma、Semera——用于把园区放入正确 manifest 分区并核实 DC 声明是否在 IPDC 园区/SEZ 内；园区证据本身不推断租户。MinT（https://mint.gov.et/）：Ethio ICT Park、Digital Ethiopia、政府云、创新园区公告。
- EEP/EEU（https://www.eep.com.et/、https://eeu.gov.et/ A）：廉价水电与直供电使能源证据关键；提取 MW/MVA、电压、变电站、馈线、连接日期、PPA 客户、电价/货币条款、站点是园区还是 EEP 直客。
- INSA（https://insa.gov.et/ A 计划/机构证据）：政府云、网络安全基建、国家 ID/Fayda 基建、采购线索；物理政府 DC 位置可能不公开——不得从计划级证据臆造。Addis Ababa 与区域/城市当局（https://www.addisababa.gov.et/）：建筑许可、土地租赁、土地拍卖、施工控制通知；公开检索弱，结合网络索引公告与运营商/ECA/IPDC 证据。
- 置信规则：**A** 仅当一手源点名设施/运营商与相关事实（运营商页=存在/容量、ECA 牌照=服务授权、IPDC 记录=园区位置、EEP 记录=MW/PPA、Uptime=认证）；**B** = DCD/Shega/Capital/Addis Fortune/ENA/FBC/Ethiopian Monitor/厂商案例/引述官员媒体；**C** = 聚合器/社交/市场报告/未点名声明/无场地与许可电力证据的公告。加密/挖矿：operator+site+MW 才超 C（EEP/ECA/运营商记录可 A；三者俱全的可信媒体 B）。云产品不点明主机设施或运营商自有 DC 不计为物理 DC。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场形态：年轻、Addis 中心；无综合公共设施登记册。工作流 = 媒体/运营商页发现线索 → 官方 join（ECA/EIC/IPDC/EEP-EEU/当地许可/Uptime）。
- 运营商扫描：**Raxio Ethiopia ET1**（Addis/Ethio ICT Park；官方页 up to 800 racks/3 MW IT 功率 A；DCD 2023 年 11 月启动 B；join Uptime/ECA/IPDC/电力）；**Wingu Africa Ethiopia**（Addis/ICT Park；DCD 报满建 10 MW/800 racks、15,000 m2 地块——容量细节 B 直到运营商/认证页确认；join ECA/ADDIX/EEU 租户证据）；**Ethio telecom**（官方模块化 DC 租赁页 + 云/托管服务页 A；Gola Sefer/Huawei 细节经 DCD/Fana 为 B）；**Safaricom Ethiopia**（官方站点证实运营商在场；2022 报道 Addis 预制 DC、Adama/Dire Dawa 规划扩张——设施细节 B 直到官方/ECA/电力记录；Addis Fortune 报 1 亿美元 DC）；**Redfox**（ICT Park 模块化 DC，Shega B，join ECA 牌照与 MinT/ICT Park 租约）；**Dashen Bank**（企业自用 Tier-III-ready DC，Shega B，join 银行年报/采购/NBE 连续性义务）；**Cloud 251**（本地云产品，主机设施不明确——C/B 线索，主机/场地未识别前不建设施）；**ADDIX/IXP 生态**（仅官方 ECA/运营商记录 A；目录 C/B-）；**Phoenix Group 等加密/挖矿**（EEP/ECA/媒体：Phoenix 80 MW 购电线索——operator+site+MW 俱全才 B）；**INSA/政府云**（A 计划/机构证据，不推断未披露物理场地）。
- 媒体源（B）：DCD、Shega、Capital Ethiopia、Addis Fortune、Ethiopian Monitor、The Reporter、ENA（A/B）、Fana（B）、Connecting Africa、Mobile Europe/CIO Africa/TelcoTitans（B/C）。聚合器（C）：DataCenterMap/ethiopia/addis-ababa、Baxtel、Datacenters.com、OCOLO；IXP 索引（C/B）：PeeringDB、Internet Exchange Map。厂商案例（B/C）：Huawei、Schneider、Vertiv、Caterpillar、Cummins、Sterling & Wilson。

## 来源分级

- **A**：一手/官方——ECA 服务/牌照记录、EIC 投资/SEZ 记录、IPDC 园区页、EEP/EEU 文件、Addis Ababa 或区域许可/土地记录、运营商设施页、Uptime 认证记录、官方云区域列表。
- **B**：强二手——可信贸易/本地媒体、厂商案例、官方通讯社文章、或两个相互一致的独立媒体报道（生命周期/容量线索）。
- **C**：弱线索——聚合器、社交、市场报告片段、MoU、可行性公告、未点名加密挖矿声明、无支撑「云区域」营销。

## 使用流程（探索/复核批次）

1. 读本 SKILL.md 与两份 explorer 报告，确定目标分区与候选项。
2. 每分区跑四遍：官方/牌照、工业园/SEZ、电力/公用事业、运营商/当地许可；显式记录负面搜索。
3. 对每个候选项做行业到官方 join（ECA/EIC/IPDC/MinT/EEP-EEU/Uptime 模板）。
4. 按置信规则定级（A/B/C；加密/挖矿需 operator+site+MW）。
5. 每季度复核：ECA 牌照类别与清单、PDPP 注册门户、IPDC 园区清单、超大规模区域页、EEP/EEU PPA 政策、Ethio ICT Park 租户公告、Safaricom/Wingu/Raxio 扩张页。
6. 遵守 NO-DELETION；不改写 explorer-*.md。

## 待办（2026-08-12 03:24Z）

- [x] 合并两份探索报告为 SKILL.md + ANATOMY.md。
- [ ] Raxio ET1/Wingu：Uptime/ECA/IPDC/电力 joins；Wingu 10 MW/800 racks 容量对账。
- [ ] Safaricom：Addis 核心 DC + Adama/Dire Dawa 官方/ECA/电力记录。
- [ ] Phoenix 80 MW：EEP/ECA 一手记录（operator+site+MW 升 B/A）。
- [ ] 待核实：Redfox/Dashen 的 ECA 牌照与租约/年报证据；Cloud 251 主机设施；SNNPR 桶内新区域名（South/Central Ethiopia）清桶。
