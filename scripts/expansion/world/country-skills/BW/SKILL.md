---
name: bw-datacenter-methodology
location: scripts/expansion/world/country-skills/BW/SKILL.md
description: |
  Botswana (BW) datacenter discovery & audit methodology — how to enumerate, verify, and update Botswana datacenter projects at district/town granularity (16 target divisions: 10 district councils + 6 city/town councils). Botswana has no public national data-centre planning register and no hyperscaler cloud region: enumeration joins local-authority development permission (Town and Country Planning Act Cap 32:09) -> DEA environmental assessment (Environmental Assessment Act 2011) -> BOCRA ICT licensing (NFP/SAP/VANS) -> BPC/BERA energy evidence -> official operator pages (BoFiNet/Digital Delta DDDC, BTC Sentlhaga, BDIH DC, Orange Botswana, Unitel). Activity is concentrated in Gaborone/South East (BDIH Block 8 cluster); Palapye/Leupane (Central) holds an announced solar-powered campus lead only. Read this before running BW exploration/audit batches. Routes to explorer-official.md (planning/EA/BOCRA/energy/cloud) and explorer-industry.md (press/vendor/division sweeps).
---

# BW · 博茨瓦纳数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：博茨瓦纳**没有**公开的全国数据中心规划注册库，也**没有**任何超大规模云区域（最近区域在南非）——枚举靠**许可链交叉**：地方当局开发许可（Town and Country Planning Act Cap 32:09）→ DEA 环评（Environmental Assessment Act 2011）→ BOCRA 电信/ICT 牌照 → BPC/BERA 电力证据 → 官方运营商页面。
> 活动几乎全部集中在 **Gaborone 市/东南走廊**：BDIH Block 8 集群（BoFiNet Digital Delta DDDC + BDIH DC）、BTC Sentlhaga、Orange Botswana、Unitel；Central 省 Palapye/Leupane 只有**已宣布/MoU 级**太阳能数据中心园区线索（AAAS Energy + ChillMine）。本 skill 汇总两份探索报告（官方管线 + 行业发现），供博茨瓦纳探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/能源/云管线：gov.bw e-portal（EA 授权、地方当局目录）、地方议会规划许可、DEA 环评、BOCRA 牌照与 licensee 名单、政府 ICT（Ministry of Communications and Innovation/SmartBots/BDIH/BoFiNet/BTC）、BPC/BERA 电力、官方云区域页（无 BW 区域）、16 省逐省策略与反误报清单 |
| `explorer-industry.md` | 行业/厂商发现：贸易媒体分级（DCD/Connecting Africa/Tech In Africa/Ecofin）、本地商报（Mmegi/Guardian/DailyNews/Business Weekly）、运营商扫描（DDDC/BDIH/BTC Sentlhaga/Orange/Unitel/AAAS-ChillMine）、BINX/PeeringDB 互联证据、逐省行业路线、生命周期与去重规则 |

## 核心结构事实（框定每次搜索）

1. **无全国设施注册库**：枚举 = 议会开发许可 + DEA EA 授权/EIS + BOCRA licensee 名单 + BPC/BERA 电力 + 官方运营商页 + 州/贸易媒体；议会不会公开许可检索门户，**DEA EA 记录是公开痕迹最完整的路径**。
2. **已确认运营设施集中于 Gaborone**：BTC **Sentlhaga Data Center**（官方页称 Tier II、Uptime 认证、120 sqm、5 kW/rack）；**BDIH Data Centre**（Plot 69184 Block 8、80 racks、Tier III compliant、DCaaS）；BoFiNet **Digital Delta DDDC**（1,000 sqm DC1、2025-10 Uptime Tier III Constructed Facility 认证、2025-11-25 启用，官方/州新闻/贸易媒体佐证）。
3. **BDIH 集群去重**：DDDC（BoFiNet，1,000 sqm，行业简报称可扩至 ~400 racks）与 BDIH DC（80 racks）是**同一园区两个独立设施**，不得合并。
4. **无超大规模云区域**：AWS/Azure/GCP/OCI 官方清单均无博茨瓦纳区域；Azure 经 BTC Cloud Connect（Microsoft 365 转售）触达——只算转售/合作伙伴存在，**不是**微软设施证据。
5. **电力证据**：BPC 是唯一发输配售一体化公用事业（https://www.bpc.bw/）；BERA（https://www.bera.co.bw/）发发电许可与重大电力基建授权；发电地理：Morupule A/B 煤电在 **Palapye, Central**（~80% 本国发电）、Mmamabula、Tlou Lesedi CBM（Serowe）、Jwaneng/Mmadinare/Maun 太阳能 IPP。记录 MVA/MW、电压、变电站/馈线、备用发电机、燃料存储、IT load 与 utility load **分列**。
6. **语言**：英语覆盖几乎全部官方/商业记录；两种拼写 `data centre`/`data center` 都要搜（另加 `datacentre`/`colo`/`co-location`/`server farm`/`cloud`/`Tier III`/`hyperscale`/`MW`/`MVA`/`substation`/`racks`）；Setswana 仅作二级扫掠（`lefelo la data`、`polokelo ya data`）并须英文文档验证。
7. **政策上下文**：Data Protection Act 2024（2025-01 生效报道，驱动数据主权本地化）、Smart Botswana/SmartBots 2019-2036 战略；Orapa 出现在 gov.bw 地方当局页面——按 **Central 省别名** 扫掠以免漏掉矿业/电信/电力线索。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§3 与 explorer-industry.md §1-§2）

- 官方门户：`site:gov.bw "data centre"`、`site:gov.bw "data centre" "{district OR town}"`、`site:gov.bw ("Digital Delta" OR "BDIH" OR "BoFiNet")`、`site:gov.bw "environmental impact" "{operator}"`。
- 议会/规划：`site:{council-domain} "data centre"`、`"{council}" "data centre" "plot"`、`"{operator}" "{district}" "plot No" "data centre"`、`"Gaborone City Council" "data centre"`。
- 环评：`site:gov.bw "environmental impact" "data"`、`"{operator}" "environmental impact statement" Botswana`、`"{operator}" "EA authorization" Botswana`、`site:eia.co.bw "{town OR operator}"`。
- BOCRA：`site:bocra.org.bw "data centre" OR "data center"`、`site:bocra.org.bw "NFP" "{operator}"`、`"{operator}" "BOCRA" "licence" "data"`。
- 电力：`site:bpc.bw "{operator}" "MVA" OR "substation"`、`site:bera.co.bw "generation licence" "{operator}"`、`"{project}" "dedicated substation" Botswana`、`"Palapye" "data centre" OR "data center"`、`"Morupule" "data centre"`。
- 运营商：`"{operator}" "Botswana" "data centre" "MW"`、`"{facility}" "Uptime Institute" Botswana`、`"Digital Delta" "BoFiNet"`、`"AAAS Energy" "ChillMine" "Palapye" "data center"`。
- 行业：`site:datacenterdynamics.com/en/news/ Botswana "data centre"`、`site:mmegi.bw "data centre" OR "data center"`、`site:connectingafrica.com Botswana "data center"`、`site:businessweekly.co.bw "data centre"`。
- 云核查：`site:aws.amazon.com Botswana`、`site:learn.microsoft.com Botswana "edge"`、`"Botswana" "sovereign cloud"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **gov.bw e-portal**（https://www.gov.bw/）：EA 授权服务页、地方当局目录、部委页（Communications and Innovation、Minerals and Energy、Lands and Agriculture）。
- **规划许可**：Town and Country Planning Act (Cap 32:09, 1977)——Gaborone City Council 等地方当局为规划机关，DTRP（Ministry of Lands）专业支持；州地由 Ministry of Lands 划拨（如 BDIH Plot 69184）、部落土地经 Land Boards（Tribal Land Act）；**记录 plot 号——最精确的区/地块证据**。
- **DEA 环评**：screening → scoping/ToR → EIS → EA authorization；公开通知与 EIS 摘要是最可见痕迹；独立追踪器 https://www.eia.co.bw/tracker（B）。
- **BOCRA**（https://www.bocra.org.bw/licensing）：框架分 **NFP**（设施）/ **SAP**（服务）/ **CSP**（内容），商用 colo/云通常需 NFP 和/或 SAP； licensee 名单 xlsx/PDF 与在线核验 https://customerportal.bocra.org.bw/OnlineLicenseVerification/verify；BOCRA 是 BINX（AS37771）运营方，PeeringDB 参与者名单可查实际在网运营商；**BOCRA 记录 = 运营商/服务授权证据，不是设施计数证据**。
- **政府 ICT/国家设施**：Ministry of Communications and Innovation、SmartBots（https://smartbots.org.bw/strategy）、BDIH DC（https://www.bih.co.bw/bdih-data-centre/）、BoFiNet/DDDC（https://www.bofinet.co.bw/、https://www.digitaldelta.co.bw/）、BTC Sentlhaga（https://btc.bw/business/sentlhaga-data-center/）。
- **BPC/BERA**：大用户连接、专用馈线/变电站、供电协议、电价审批；现场柴油发电机（燃料存储可能触发环保/健康审批）；超过阈值的光伏/嵌入式发电需 BERA 授权。
- **云区域页**：AWS/Azure/GCP/OCI 均无博茨瓦纳区域；国际互联：BoFiNet 持有 WACS/EASSy/EIG/Equiano 份额 + 陆缆至 Swakopmund（WACS）与 Johannesburg——Gaborone 是自然互联枢纽。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商种子（A=官方存在/B=容量）**：BoFiNet DDDC（锚设施，Tier III 认证）、BDIH DC（80 racks）、BTC Sentlhaga（Tier II）、Orange Botswana（New Lobatse Rd，~2 MW 为聚合器数字 B）、Unitel（colo 服务声称 B/C）、Mascom/Orange/BTC 核心机房（**内部设施**，仅当以 colo/云/Tier 营销才计）、Liquid/Africa Data Centres（Gaborone 办事处/城域环——**运营商在场≠设施**）、Starlink（BOCRA 2024-05 牌照——卫星 ISP 非 DC）、AAAS Energy + ChillMine Palapye/Leupane 园区（**仅 B/C 管道线索**，直至 DEA/BERA/BPC/议会/运营商施工证据出现）。
- **厂商/承包商**：Zhong Gan/CJIC 承建 DDDC（DCD）；Siemon/Schneider/Vertiv/Huawei/ZTE/Caterpillar 案例页做设备交付证据（B/C，容量常缺）。
- **贸易媒体分级**：DCD（B，链接一手文档可达 A）、Connecting Africa（B）、Tech In Africa（B）、Ecofin（B）、TechFinancials（B）、Mmegi（B，引用官方文档 A）、DailyNews（州报，官方公告逐字 A-）、Botswana Guardian/Weekend Post/Sunday Standard/Business Weekly（B/B/C）、BW TechZone（B/C）、Africa Data Centres Association + D4D Hub/Xalam 市场简报（B，背景非设施证明）、BINX/PeeringDB（B，互联证明）。
- **目录对账**：datacentermap（~5 设施）与 datacenters.com（~8）计数不一致、容量/状态错位——只做发现，每条必须解析到运营商页面。
- **生命周期**：`announces`/`signs MoU`/`plans`/`feasibility`=意图（C/B）；`breaks ground`/`starts construction`=管道（B，官方 A）；`opened`/`launched`/`operational`/`Uptime certified`=运营信号（须运营商/Uptime 页验证为 A）。

## 来源分级

- **A** = 官方/一手/法律可问责：议会开发许可/建筑许可、DEA EA 授权/EIS、BOCRA 牌照或 licensee 名单、BERA/BPC 官方能源材料、官方运营商或政府页（BoFiNet、BTC、BDIH、部委）、官方云厂商声明、Uptime Institute 认证记录。
- **B** = 强二级：本地成熟商报（Mmegi、Botswana Guardian、Business Weekly、Weekend Post、Sunday Standard）、贸易媒体（DCD、Connecting Africa、Tech In Africa、Ecofin）、Uptime 认证记录（记录本身 A，报道 B）、EU/D4D Hub 市场简报、开发商/公告发布。
- **C** = 弱线索：聚合目录（datacentermap、datacenters.com）、泛市场报告、社交帖、无来源目录条目、旧 MoU。
- 状态语义：设施存在（A）仅当官方运营商/政府页具名 DC 与位置，或 DEA/议会/BOCRA/BPC 文件识别；施工（A/B）仅当官方/政府/运营商施工开始证据，贸易媒体单独为 B；容量区分 IT load 与 utility load，**不把 MVA 换算 MW**（除非来源给出换算）；云提及仅作种子。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=BW，divisions=16 议会区/市镇）。
2. 建种子：DDDC、BDIH DC、BTC Sentlhaga、Orange、Unitel + 运营商官方页 + Uptime 记录。
3. 逐 division 执行标准流程：官方域扫掠（gov.bw/BOCRA/BERA/BPC/DEA/运营商/议会/SEZA-BITC）→ 英文变体词表 → 具名运营商扫掠 → 任一线索须至少一个一手源才可评 A。
4. 验证：A 级设施证据 = 运营商/政府页具名 + 位置，或 DEA/议会/BOCRA/BPC 文件；记录 plot 号；IT MW 与 utility MVA/MW 分列。
5. 负扫掠协议：议会站点 + BOCRA licensee 名单 + DEA EA 扫掠 + 具名运营商扫掠 + 词表；不把数据采集办公室、网吧、电脑室、银行服务器房、议会 ICT 房当数据中心。
6. 输出 world schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；无项目 division 写 `no_projects: true`。
7. 遵守 NO-DELETION；只新增 SKILL.md 与 ANATOMY.md。

## 待办（2026-08-12 02:58Z）

- [x] explorer-official.md 与 explorer-industry.md 已完成并合并为本 SKILL.md。
- [ ] 下一步：50× codex terra agent 按 16 division 逐区枚举（优先 Gaborone、South East、Central/Palapye）。
- [ ] 待核实：DDDC 运营后容量/租户证据与 BDIH DC 运营主体（tenders）；Orange Botswana DC 的官方容量；AAAS/ChillMine Palapye 园区是否有 DEA/BERA/BPC/议会证据升级；云区域列表是否新增博茨瓦纳。
