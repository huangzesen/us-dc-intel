---
name: sg-datacenter-methodology
location: scripts/expansion/world/country-skills/SG/SKILL.md
description: |
  Singapore (SG) datacenter discovery & audit methodology — how to enumerate, verify, and update Singapore datacenter projects at URA planning-area + CDC-district granularity (5 CDC districts: Central Singapore, North East, North West, South East, South West). Singapore has no public datacenter registry and no public planning-application database searchable by datacenter use: enumeration joins IMDA/EDB capacity allocation (pilot DC-CFA ~80 MW; DC-CFA2 ≥200 MW from 2025-12-01; Green Data Centre Roadmap ≥300 MW), URA B2 planning-permission rule, BCA-IMDA Green Mark for Data Centres, EMA/SP grid and GeBIZ procurement, ACRA/SGX/REIT filings, official cloud-region pages (AWS ap-southeast-1, Azure Southeast Asia, GCP asia-southeast1, OCI ap-singapore-1, Alibaba ap-southeast-1), and operator facility pages (Equinix, Digital Realty, Keppel, STT GDC, Nxera, AirTrunk, DayOne, Global Switch, ST Engineering). Read this before running SG exploration/audit batches. Routes to explorer-official.md (IMDA/URA/BCA/EMA/procurement/cloud) and explorer-industry.md (operators/press/IXP/subsea/directories).
---

# SG · 新加坡数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：新加坡**没有**公开的数据中心注册库，也无可按“数据中心用途”检索的公开规划申请库；**IMDA/EDB 容量分配（DC-CFA）是新增容量（2019 暂停后）的官方主控线索**；枚举采用“IMDA/EDB 容量分配 → URA 规划许可 → BCA Green Mark → EMA/SP 能源 → GeBIZ 采购 → ACRA/SGX/REIT 法人/资产 → 云区域官方页 → 运营商设施页”多轨。
> 分区模型：**5 个 CDC 区（Community Development Council districts）**（Central Singapore、North East、North West、South East、South West）；设施先按 URA 规划区/园区/地址地理编码，再赋 CDC 区；CDC 边界基于选区、选举后可能变动，边界敏感记录标记 `division_check_needed`。
> 已知种子：Equinix SG5/SG6、Digital Realty SIN10（29A IBP）、Keppel DC SGP1-5/DC1/7-8、STT Singapore 1/2/3（Defu）、Nxera DC Tuas（58 MW，2026-02-09 开业）、DayOne SG1（21 Jalan Buroh，20 MW）、Global Switch Tai Seng/Woodlands、AirTrunk SGP1（Loyang）、ST Engineering DC@Boon Lay（2026 目标）；云区域 AWS ap-southeast-1 / Azure Southeast Asia / GCP asia-southeast1 / OCI ap-singapore-1 / Alibaba ap-southeast-1。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供新加坡探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：IMDA/EDB DC-CFA + DC-CFA2 + Green Data Centre Roadmap、MDDI/MTI/国会、URA SPACE/B2 许可规则、BCA/CORENET/Green Mark、EMA/SP Group、GovTech/GeBIZ、ACRA/BizFile/SGX/Keppel DC REIT、云区域官方页、5 区逐区方法、验证清单 |
| `explorer-industry.md` | 行业/厂商发现：运营商主源管道（Equinix/Digital Realty/Keppel/STT GDC/Nxera/AirTrunk/DayOne/Global Switch/ST Engineering + 待查清单）、DCD/BT/ST/CNA/W.Media 等媒体、SGIX/DE-CIX/BBIX/PeeringDB 互连、Changi North/Tanah Merah/Tuas 海缆、目录（C）、马来语/华语/泰米尔语补全词、已知设施证据表 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库**：枚举必须多轨交叉；政策目标、CFA 分配、云 AZ 数、IXP PoP、海缆登陆站一律**不**算数据中心设施。
2. **DC-CFA 是新增容量官方主线**：pilot DC-CFA（2023-07-14 选定四提案，约 80 MW：AirTrunk-ByteDance、Equinix、GDS、Microsoft，A 仅于授奖/容量分配事实）；**DC-CFA2** 2025-12-01 启动、至少 200 MW（+绿色能源通道），授奖结果未公布前不计入；Green Data Centre Roadmap 为政策背景（近期至少 300 MW 增量目标）。
3. **URA B2 规则**：B2 Allowable Uses 页明确 **Data Farms/Data Centres 需事先规划许可**（A 监管背景）；用 URA SPACE 记录总体规划分区与规划区；无搜索结果 ≠ 无许可（新加坡规划许可记录非完整公开注册库）。
4. **Green Mark 仅证认证**：BCA-IMDA Green Mark for Data Centres（GMDC:2024）在 BCA/IMDA/运营商页找到即 A 于认证事实，但不证完工/运营；CORENET 是电子提交系统，非设施注册库。
5. **能源/电网无公开连接注册库**：EMA/SP Group 用于政策、绿色能源进口与具名连接公告；运营商融资/PPA 公告 A（运营商自有）或 B（媒体），除非声明通电/开业，否则不证设施运营。
6. **云区域事实仅 A 于区域存在**：AWS ap-southeast-1（3 AZ）、Azure Southeast Asia（southeastasia）、GCP asia-southeast1、OCI ap-singapore-1、Alibaba ap-southeast-1（4 zones）；不映射物理地址/CDC 区/MW。
7. **法人/资产走 ACRA/SGX/REIT**：BizFile UEN 是招标/融资/许可/运营商页的连接键；REIT 年报（Keppel DC REIT）A 于投资组合构成与所有权比例。
8. **拼写/语言**：新加坡惯用 **data centre**，美国/云页用 **data center**，两者都搜；马来语 `pusat data`、华语 `数据中心`、泰米尔语 `தரவு மையம்` 用于媒体补全。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§3 / explorer-industry.md §2-§7）

- IMDA/EDB：`site:imda.gov.sg "data centre" Singapore`、`site:imda.gov.sg "DC-CFA" OR "Call for Application"`、`site:imda.gov.sg "Data Centre 2" "200MW"`、`site:edb.gov.sg "{operator}" "data centre"`、`"DC-CFA" "AirTrunk" OR "Equinix" OR "GDS" OR "Microsoft"`。
- 部委/国会：`site:mddi.gov.sg "Digital Connectivity Blueprint" "data centre"`、`site:mti.gov.sg "data centre" "groundbreaking"`、`site:sprs.parl.gov.sg "data centre"`。
- URA/许可：`site:ura.gov.sg "data centre"`、`site:ura.gov.sg "Data Farms" "Data Centres"`、`"{address}" "URA" "data centre"`。
- Green Mark/CORENET：`site:imda.gov.sg "Green Mark for Data Centres"`、`"BCA-IMDA Green Mark" "{operator}" "data centre"`。
- 能源/采购：`site:ema.gov.sg "data centre"`、`site:spgroup.com.sg "data centre"`、`site:gebiz.gov.sg "colocation" OR "data centre hosting"`、`site:tech.gov.sg "Government on Commercial Cloud"`。
- 法人/REIT：`site:bizfile.gov.sg "{legal_entity}"`、`site:sgx.com "Keppel DC REIT" "data centre"`、`site:keppeldcreit.com "KDC SGP" "annual report"`。
- 云：`"AWS" "ap-southeast-1" "Singapore" "Availability Zones"`、`"Azure" "Southeast Asia" "Singapore" "southeastasia"`、`"Google Cloud" "asia-southeast1" "Singapore"`、`"Oracle Cloud" "ap-singapore-1"`、`"Alibaba Cloud" "Singapore" "ap-southeast-1"`。
- 分区：`"Ayer Rajah" OR "one-north" "data centre" Singapore`（Central）、`"STT Singapore" "Defu"`（NE 边界核验）、`"Global Switch" "7 Woodlands Height"`（NW）、`"AirTrunk" "SGP1" "Loyang"` + `"Keppel DC Singapore 2" OR 3 OR 4`（SE）、`"Digital Realty" "SIN10" "29A International Business Park"` + `"Nxera" "DC Tuas" "58MW"`（SW）。
- 行业/互连：`site:datacenterdynamics.com Singapore "data centre"`、`site:businesstimes.com.sg "data centre" Singapore`、`site:sgix.sg "Singapore"`、`site:peeringdb.com "Singapore" "{facility}"`、`"BBIX" "Singapore" "Global Switch" "Tai Seng"`、`"{cable}" "Singapore" "landing" "Changi" OR "Tuas" OR "Tanah Merah"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 入口：IMDA/EDB DC-CFA 材料（A 于分配事实）→ MDDI/MTI/国会（A 于部长声明/仪式）→ URA SPACE + B2 规则 → BCA/IMDA Green Mark（认证证据）→ EMA/SP Group（政策/具名连接）→ GovTech/GeBIZ（公共合同/授标，通常无物理位置）→ ACRA/BizFile + SGX/REIT（法人/资产）→ 云区域官方页（区域存在）。
- 已知官方/主源锚点表（节选）：Equinix SG6（SW，9 层，2027 Q1 预期、满建 20 MW、pilot DC-CFA 授标，A）；Keppel DC SGP1（NE，Serangoon North，A）、SGP2/3/4（SE，Tampines，A）、SGP5（SW，Jurong，A）、DC1（NW，Woodlands，A）；STT Singapore 1（13 MW）/2（12 MW）/3（Defu 3，2022 开业，A/B）；Nxera DC Tuas（SW，58 MW IT、Green Mark、海缆整合、Singtel 2026-02-09 开业稿，A）；DayOne SG1（SW，21 Jalan Buroh、39,978 sqm、20 MW、RFS 2027、氢 SOFC 试点，A/B）；ST Engineering DC@Boon Lay（SW，2024-06-25 动工、2026 目标、$120m、PUE 1.25 设计，A）。
- 验证清单：URL 存活且页面确证 → 事实按字段分级 → OneMap/URA SPACE 地理编码 → 赋 CDC 区（边界敏感标记）→ 2019 后绿地项目查 DC-CFA/DC-CFA2 → 设施计数仅用 A/B 证据。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商主源：Equinix（SG 平台 A、SG5 2021 开业 A、SG6 建设中 A）、Digital Realty SIN10（A）、Keppel（各址 A）、STT GDC（Defu 1/2/3，A/B）、Nxera/Singtel（DC Tuas A、DC West/Kim Chuan 2 存在 A、分区待 GIS）、AirTrunk SGP1（Loyang 开业，60+ MW 设计声明，A/B）、DayOne SG1（A/B）、Global Switch Tai Seng 17 MW / Woodlands 22 MW（A）、ST Engineering DC@Boon Lay（A/B）；待查清单：StarHub、M1、CMI、Tata、OneAsia、i-Sprint、ViewQwest、PDG、Bridge、SpaceDC、Empyrion、CyrusOne、Vantage、NEXTDC（未证实前不入 A/B 库存）。
- 媒体（B）：DCD、Business Times、Straits Times、CNA、W.Media、The Edge Singapore、Reuters/Bloomberg/FT、工程/承包商页（Aurecon、HDR、PM Group）。
- 互连/海缆：SGIX（PeeringDB ix/429）、DE-CIX Singapore、BBIX Singapore No.3 @ Global Switch Tai Seng（A PoP 事实）；IMDA 海缆登陆指导、Submarine Networks、TeleGeography（Changi/Tanah Merah/Tuas 登陆点，A/B）；IXP PoP 与登陆站不计数，除非另有数据中心源支持设施。
- 目录（C，仅线索）：DataCenterMap Singapore、Baxtel、DataCenterJournal、Cloudscene、datacenters.com、Colomap。
- 红灯：云区域/AZ 非物理设施数；运营商设施 ID 非地址；营销 MW/承诺 MW/IT 负荷/电网 MVA/实际投运容量是不同事实；目录计数因范围混杂不可靠。

## 已知设施/项目与证据状态

| 设施/项目 | 分区（CDC）/地点 | 状态与证据 |
|---|---|---|
| Equinix SG5 | South West/6 Sunview Drive | 运营（2021 开业）；A（Equinix 设施页） |
| Equinix SG6 | South West | 建设中；A（Equinix/EDB：9 层、2027 Q1 预期、满建 20 MW、pilot DC-CFA 授标） |
| Digital Realty SIN10 | South West/29A International Business Park | 运营；A（Digital Realty 页） |
| Keppel DC SGP 2/3/4 | South East/Tampines Industrial Park | 运营；A（Keppel 页） |
| Keppel DC SGP 1 | North East（GIS 核验）/Serangoon North | 运营；A（Keppel 页） |
| Keppel DC DC1 | North West/Woodlands | 运营；A（Keppel 页） |
| Keppel DC SGP 5 | South West/Jurong | 运营；A（Keppel 页） |
| Keppel DC SGP 7/8 | 分区待地址/GIS | Keppel Data Centre Campus 相邻设施；KDC SGP 7 Green Mark Platinum 声明；A 于存在/认证声明 |
| STT Singapore 1 | North East 或 SE 边界核验/Defu | 运营；13 MW；A（STT GDC） |
| STT Singapore 2 | 同上/Defu | 运营；12 MW；A（STT GDC） |
| STT Singapore 3（Defu 3） | 同上/Defu | 运营（2022 开业）；15 MW（DCD）；A/B |
| Nxera DC Tuas | South West/Tuas | 运营（Singtel 2026-02-09 开业稿）；58 MW IT、PUE/Green Mark、海缆整合；A |
| Nxera DC West / DC Kim Chuan 2 | SW 可能 / SE-Central 边界（GIS） | 存在（Nxera 列表）；分区待地址；A 于存在 |
| AirTrunk SGP1 | South East/Loyang | 运营（2020 开业，BT）；60+ MW 设计声明（AirTrunk）；A/B |
| DayOne SG1 | South West/21 Jalan Buroh, Jurong East | 建设中；39,978 sqm、20 MW、RFS 2027、氢 SOFC 试点；A/B（DayOne/BT） |
| Global Switch Tai Seng | South East/2 Tai Seng Avenue | 运营；17 MW；A |
| Global Switch Woodlands | North West/7 Woodlands Height | 运营；22 MW；A（含 Aurecon/PM Group 工程页） |
| ST Engineering Data Centre@Boon Lay | South West/Jalan Boon Lay | 建设中（2024-06-25 动工）、2026 目标；$120m、PUE 1.25 设计；A（ST Engineering/MTI/ST） |
| StarHub Tai Seng DCs / CMI 15A Tai Seng | South East | 候选；C 直到 StarHub/CMI 主源确认 |
| Meta Tanjong Kling / Jurong | South West | 候选超大规模园区声明；C 直到 Meta/法定源确认 |
| Punggol Digital District | North East | 数字园区本身；A 仅于园区事实，非设施 |
| SGIX / DE-CIX Singapore / BBIX No.3 | n/a（互连） | A 于 IXP/PoP 事实；非设施计数 |
| Changi North / Tanah Merah / Tuas 登陆点 | South East / South West | 海缆登陆集群；A/B（IMDA/Submarine Networks/TeleGeography）；非 DC |

## 更新节奏

- 每月：IMDA/EDB/MDDI/MTI 新闻、DC-CFA2 页、GeBIZ、Equinix/Digital Realty/Keppel/STT GDC/Nxera/AirTrunk/DayOne/Global Switch/ST Engineering 页面、DCD/W.Media/BT/ST/CNA/The Edge。
- 季度：云区域官方页、URA 通函/SPACE 分区核验、BCA/IMDA Green Mark、EMA/SP Group 能源公告、SGX/REIT 披露、PeeringDB/IXP PoP、目录线索。
- 里程碑触发：DC-CFA2 申请截止/入围/授标/动工/通电各节点立即重查。
- 待办（2026-08-12）：两份 explorer 初稿已完成（codex 复核）；下一步 codex terra agent 分批复核（5 CDC 区粒度，边界敏感址 GIS 复查）；本 skill 作为国家层参考注入。
