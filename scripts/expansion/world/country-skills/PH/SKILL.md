---
name: ph-datacenter-methodology
location: scripts/expansion/world/country-skills/PH/SKILL.md
description: |
  Philippines (PH) parent-level methodology for data-center enumeration at region granularity (18 PSGC
  regions as of 31 Jul 2025; the Negros Island Region/NIR was created by RA 12000 - Negros Occidental incl.
  Bacolod, Negros Oriental and Siquijor now belong to NIR, not Western/Central Visayas). The Philippines
  publishes no single national datacenter registry; a reliable census assembles LGU permits (zoning/building/
  occupancy/business/Sanggunian/BFP), NTC registrations (DTIP under RA 12234 / NTC MC 002-02-2026; VAS;
  SRF exemption NTC MO 001-02-2026 for 2025-2028), DICT/GovCloud records, DENR-EMB ECC/CNC online, energy
  and grid evidence (Meralco dominant; DOE/ERC/NGCP/regional utilities), PEZA/BOI/SIPP incentives, NPC
  privacy registration, official operator pages, and official cloud infrastructure pages. Cloud: AWS Manila
  Local Zone + Direct Connect exist but there is NO full PH region (no Azure/GCP/OCI PH region either).
  Commercial core is NCR + CALABARZON + Central Luzon (VITRO/ePLDT, STT GDC, Equinix MN1-MN3 ex-TIM,
  Converge, DITO Clark, SpaceDC MNL1, plus planned Flow/A-Flow and DAMAC/EDGNEX). Routes to
  explorer-official.md (LGU/regulator/energy/environment/incentives chain) and explorer-industry.md
  (operator/interconnection/press chain).
---

# PH · 菲律宾数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：菲律宾不发布单一国家数据中心登记册；可靠普查必须拼接 LGU 许可（分区/建筑/占用/商业/市议会条例/BFP）、NTC 注册（RA 12234 Konektadong Pinoy 法下的 DTIP + NTC MC 002-02-2026；VAS；SRF 豁免 NTC MO 001-02-2026 覆盖 2025-2028）、DICT/GovCloud 记录、DENR-EMB ECC/CNC 在线检索、能源与电网证据（Meralco 主导；DOE/ERC/NGCP/区域公用事业）、PEZA/BOI/SIPP 激励、NPC 隐私注册、运营商官方页与官方云基础设施页。**当前分区为 18 个 PSGC 区域**（RA 12000 创设 Negros Island Region/NIR：Negros Occidental 含 Bacolod、Negros Oriental、Siquijor 归 NIR，不再属于 Western/Central Visayas）。云状态：AWS 马尼拉 Local Zone + Direct Connect 存在，但**无完整 PH 区域**（Azure/GCP/OCI 亦无）。商业核心为 NCR + CALABARZON + Central Luzon。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供菲律宾探索与复核批次使用。

## 入口

| 文档 | 用途 |
|---|---|
| `explorer-official.md` | 官方/监管管线：PSGC 18 区、NTC（DTIP/VAS/SRF）、DICT/GovCloud、DENR-EMB ECC/CNC、DOE/ERC/NGCP/公用事业、PEZA/BOI/SIPP、NPC、云基础设施阴性对照、逐区官方策略、红色警戒 |
| `explorer-industry.md` | 行业管线：运营商版图（VITRO/STT/Equinix/Converge/DITO/SpaceDC 等）、超大规模与云、互联生态（IXP/海缆）、行业机构（DCAP）、行业媒体、逐区行业策略、枚举工作流 |

## 核心结构事实（框定每次搜索）

1. **18 区（非 17 区）**：PSA PSGC 页称 2025-07-31 起为 18 区；RA 12000 创设 **Negros Island Region（NIR）**（Negros Occidental、Bacolod 市、Negros Oriental、Siquijor）；不要再用旧 17 区模板，当前记录把 Negros/Siquijor 归 NIR。18 区：NCR、CAR、Region I（Ilocos）、Region II（Cagayan Valley）、Region III（Central Luzon）、Region IV-A（CALABARZON）、Mimaropa（IV-B）、Region V（Bicol）、Region VI（Western Visayas，不含 Negros Occidental）、NIR、Region VII（Central Visayas，不含 Negros Oriental/Siquijor）、Region VIII（Eastern Visayas）、Region IX（Zamboanga Peninsula）、Region X（Northern Mindanao）、Region XI（Davao）、Region XII（Soccsksargen）、Region XIII（Caraga）、BARMM。
2. **无国家登记册**：许可在地方（LGU 建筑/占用/分区/商业/电气/消防许可；RA 11032 电子一站式但无全国规划门户）；枚举 = LGU + NTC + DICT/GovCloud + DENR-EMB + 能源 + PEZA/BOI + NPC + 运营商页 + 官方云页。
3. **NTC 双轨**：RA 12234（Konektadong Pinoy 法）创设开放接入数据传输框架，NTC MC 002-02-2026 规定 DTIP 资格与义务；VAS 注册是托管/托管服务/colo 提供商的可能线索；NTC MO 001-02-2026 据报道豁免数据中心 2025-2028 年监管费（B 级确认用 Quisumbing Torres/Baker McKenzie）；实体注册 = 服务权限，非具体建筑证明。
4. **环境记录异常有用**：DENR-EMB ECC Online 公开检索（ecconline.emb.gov.ph/live/search.aspx）可按项目名/主张者/地点/ECC 编号检索（关键词最短 10 字符）；提取 ECC/CNC 编号、日期、主张者、位置、EMB 区域办、含冷却/水/废水/备用发电机/油罐/空气噪声的条件。
5. **能源常是最强官方线索**：Meralco 主导大马尼拉、Bulacan、Rizal、Cavite、Laguna 及部分 Batangas/Quezon；区分区域私有公用事业与电合作社（Davao Light、VECO、CEPALCO、MORE Power、PELCO/TARELCO/CENECO）；提取 PSA/RCOA/通电通知/并网协议/变电站中的客户/项目名、MW/MVA、电压、变压器容量、专用变电站、馈线与通电日期。
6. **云状态**：AWS 马尼拉 Local Zone + Direct Connect（近/内 ePLDT Makati 基础设施，2025 宣布 100G 扩展）为官方存在；AWS/Azure/GCP/OCI 官方列表均无完整菲律宾区域——"菲律宾云区域"主张为 C 直到官方区域页存在。
7. **商业核心**：NCR（VITRO Makati 1/2、Pasig、Parañaque；Equinix MN1/MN2/MN3 ex-TIM——2025-06 完成收购 3 个 TIM 马尼拉 DC、1,000+ 机柜、托管主要马尼拉 IX；STT GDC Makati/Manila；STT Fairview——Fairview 1 于 2025 Q2 宣布 ready for service、园区目标 124 MW IT；Converge Pasig）、CALABARZON（VITRO Sta. Rosa/Pulong Santa Cruz——AI-ready 超大规模、专用变电站、50MW 级公共主张；SpaceDC MNL1/Cainta；STT Cavite/General Trias；Flow/A-Flow+Ayala Land Laguna B；DAMAC/EDGNEX Laguna AI 宣布 2026——planned/MoU 级 B/C）、Central Luzon（DITO Clark Super Core；New Clark City/BCDA；Subic；Bataan/AFAB；Baler/Aurora 登陆）。
8. **地理消歧**："Manila" 通常是大马尼拉营销标签，解析到 Makati/Pasig/Taguig/Quezon City/Parañaque 等；Cainta=Rizal/CALABARZON；Sta. Rosa=Laguna/CALABARZON；General Trias=Cavite；Clark=Pampanga/Central Luzon；Baguio=CAR；Bacolod=NIR。
9. **互联生态**：PHOpenIX、PhIX、GetaFIX、GIX/NIGX、AMS-IX Manila、BBIX Philippines；海缆系统/线索：Bifrost（Davao）、Apricot（Baler/Digos）、TPU（Claveria/Cagayan）、Candle（Nasugbu/Batangas）、PLCN、AUG、ALC、SEA-H2X、ADC 等——登陆站是连通性锚点，非 colo DC，除非单独证明。
10. **状态/容量纪律**：状态梯 proposed < MoU-only < permit-stage < under-construction < ready-for-service < operating < cancelled；MoU 与总统投资会面不是设施；宣布 MW ≠ 运营 MW；NTC VAS/DTIP 注册是实体证据非建筑地址；ECC/CNC 公开检索缺失不具决定性（用 SPV/地主/园区/barangay/公用事业项目/承包商名重搜）。

## 查询模式（复制粘贴模板见 explorer-official.md §2-§11、explorer-industry.md §1/§2/§4/§7）

```text
site:qcgov.ph OR site:makati.gov.ph OR site:pasigcity.gov.ph OR site:taguig.gov.ph "data center"
"{operator}" "{city}" "building permit" OR "occupancy permit" OR "business permit" OR "locational clearance"
"{city}" "data center" "Sanggunian" OR "ordinance"
site:ntc.gov.ph "DTIP" "{operator}" OR "Data Transmission Industry Participants"
site:ntc.gov.ph "VAS" "{operator}" OR "value-added service"
site:ntc.gov.ph "Supervision and Regulation Fees" "data centers"
site:ntc.gov.ph "cable landing" "{operator}"
site:dict.gov.ph "data center" OR "National Government Data Center" OR "GovCloud"
site:foi.gov.ph "National Government Data Center" "DICT"
"North Luzon Data Center" "DICT" "BCDA" "John Hay"
site:ecconline.emb.gov.ph "{operator}" OR "data center"
"Environmental Compliance Certificate" "{operator}" Philippines
"CNC" "{operator}" "data center"
site:meralco.com.ph "data center" OR "{operator}" MW OR MVA
"Meralco" "data center" "substation"
site:erc.gov.ph "data center" OR "{operator}" "power supply agreement"
site:doe.gov.ph OR site:ngcp.com.ph "data center"
"data center" "VECO" OR "Davao Light" OR "CEPALCO" OR "MORE Power"
site:peza.gov.ph "data center" OR "{operator}"
"PEZA" "data center" "{city}" OR "IT Park" "data center"
site:boi.gov.ph "data center" OR "{operator}" "data center"
"SIPP" "data center" 2026 Philippines OR "CREATE MORE" "data center"
site:privacy.gov.ph "{operator}" "PIC" OR "PIP"
"VITRO Makati" OR "VITRO Pasig" OR "VITRO Parañaque"
"VITRO Sta. Rosa" OR "Pulong Santa Cruz" "data center"
"Equinix" "MN1" OR "MN2" OR "MN3" "Philippines"
"STT GDC" "Makati" OR "Fairview" OR "Cavite" OR "Davao"
"Fairview" "124MW" "data center"
"SpaceDC" "MNL1" OR "Cainta"
"DITO" "Clark" "Super Core" "data center"
"DAMAC" OR "EDGNEX" "Laguna" "data center"
"AWS Local Zone" Manila OR "AWS Direct Connect" Makati
"Azure" OR "Google Cloud" OR "Oracle" "Philippines" "region"
"{city}" "data center" "ECC" OR "{region}" "data center" "DICT"
"Bacolod" OR "Negros Island Region" "data center"
"data center" OR "datacenter" "{lgu_or_city}"
"ordinansa" OR "ordinance" "data center"
```

## 官方/监管管线要点（详见 explorer-official.md）

- **LGU 许可栈**：分区/选址许可、建筑许可（含电气/机械/管道/卫生/消防子许可）、占用许可、商业许可/市长许可、Sanggunian 条例/决议/纪要、BFP 消防检查证、本地水与卫生许可（冷却/废水/储油/备用发电影响）；A 仅实际 LGU 许可/条例/纪要，B 官方 LGU 新闻稿，C 许可经纪/地产营销。
- **NTC**：DTIP 注册（RA 12234 + NTC MC 002-02-2026：参与者名/层级/有效期/服务区/分配资产）、VAS 注册、遗留公共电信授权（PLDT/Globe-Innove/Converge/DITO/PT&T/ETPI）、海缆登陆/国际网关/骨干授权（La Union、Batangas、Cavite、Aurora/Baler、Cagayan/Claveria、Davao/Digos）、SRF 豁免记录；NTC 站点可能阻止自动访问——保留截图/PDF，律所摘要仅 B 佐证。
- **DICT/GovCloud**：Cloud First 政策与 GovCloud 认证通告（cms-cdn.e.gov.ph）、FOI 门户搜 "National Government Data Center"/"GovCloud"/"NGDC"、BCDA/JHMC/DICT 记录（Camp John Hay/Baguio 的 North Luzon Data Center）；政府设施可能不发布商业级容量/地址——保留确切公开措辞。
- **DENR-EMB**：ECC Online + CNC Online + EIA 处；条件含冷却/水源/废水/备用发电机/油罐/空气噪声许可/施工交通/洪涝地震风险；替代主张者名（SPV、地主、园区运营商、施工子公司、公用事业项目名）。
- **能源**：DOE、ERC（PSA 批准/费率影响）、NGCP（输电项目）、Meralco、NEA/电合作社、IEMOP/WESM、区域公用事业；功率容量主张需公用事业/ERC/NGCP 佐证后才存为运营 MW。
- **PEZA/BOI/SIPP**：注册企业名/项目标题/注册活动/注册地点/投资额/状态；PEZA IT 园区/建筑线索（Eastwood、BGC/Taguig、Makati CBD、Laguna Technopark、Cebu IT Park、Clark/Subic、Carmelray/LISP）；BOI/SIPP 类别（datacenter development、digital infrastructure、AI/data science、off-grid/renewable）。
- **NPC**：RA 10173 下 PIC/PIP/DPO 注册——实体归一化与合规证据，非物理设施证据。
- **云基础设施**：AWS Local Zone/Direct Connect 官方页（A 存在；B/C 物理节点地址除非 AWS 或宿主确认）；Azure/GCP/OCI 官方列表无 PH 区域（A 阴性对照）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **VITRO/ePLDT/PLDT 集团**：官方页列组合（VITRO Makati 1/2、Pasig、Parañaque、Sta. Rosa/Pulong Santa Cruz、Cebu 1/2、规划/宣布 Cavite 站点）；Sta. Rosa 官方定位 AI-ready 超大规模 + 专用变电站 + 50MW 级公共主张（A 官方页，B 媒体容量）。
- **STT GDC Philippines**（Globe/Ayala/STT 平台）：Makati/Manila 遗留、STT Cavite、STT Davao、STT Fairview（Fairview 1 2025 Q2 宣布 ready for service；园区目标 124 MW IT，A）。
- **Converge ICT**：光纤运营商，数据中心与登陆角色（Pasig/Reliance IT Center、Clark、Parañaque 超大规模计划、Davao/Baler 登陆生态，A/B）。
- **DITO**：Clark Super Core 数据中心 / Clark Global City NOC/R&D（A/B）。
- **Equinix Philippines**：2025-06 完成收购 3 个 TIM 马尼拉 DC（MN1/MN2/MN3、1,000+ 机柜、扩展土地、托管主要马尼拉 IX，A 官方稿）。
- **SpaceDC MNL1**：Cainta/Rizal 大型绿色超大规模园区（A/B——状态与 MW 需从 SpaceDC/JLL/运营商页 + EMB/LGU 证据核实）。
- **EdgeConneX MNL01**（B/C 目录）、**Flow/A-Flow + Ayala Land Laguna**（B，需运营商/LGU/EMB/公用事业升级）、**DAMAC Digital/EDGNEX Laguna AI**（2026 宣布，planned/MoU 级 B/C）、**Evolution + Megawide 69MW 型项目**（B/C，位置与许可待确认）、**Digital Edge/Yondr**（C 仅搜索种子）。
- **互联**：PHOpenIX、AMS-IX Manila、BBIX Philippines POP 列表（A 官方 IXP/运营商/NTC/海缆系统页；B 可信电信媒体；C 众包目录行）。
- **DCAP**（dcap.ph）：成员/倡导/宏观容量目标（PNA 报 DCAP 2029 年 1GW 目标，B 市场背景）。
- **媒体分级**：DCD、W.Media（B）、PNA、BusinessWorld、Inquirer、Philstar、Manila Bulletin、Manila Standard、BusinessMirror、Rappler、Reuters/AP、Bilyonaryo、ABS-CBN、GMA（B）；承包商搜索 First Balfour/EEI/D.M. Consunji/Megawide/Ayala Land/Bouygues。
- **目录纪律**：Baxtel/DataCenterMap/Cloudscene/datacenters.com/ocolo/colomap 为 C 直到运营商/官方源确认设施名/运营商/城市；警惕收购品牌变动导致的重复记录（Equinix/TIM、STT/Globe、VITRO）。

## 来源分级

- **A** = 主要或法律可问责来源：LGU 许可/条例、NTC 发布或注册表、DICT 通告/认证/FOI 披露、DOE/ERC/NGCP/公用事业记录、DENR-EMB ECC/CNC 记录、NPC 注册、PEZA/BOI 注册/发布、官方运营商设施页、官方云基础设施页、法定申报、年报。
- **B** = 具名事实的可信二级：PNA、Reuters/AP、BusinessWorld、Inquirer、Philstar、Manila Bulletin、Manila Standard、BusinessMirror、Rappler、DCD、W.Media、识别法令/命令的律所提示、承包商发布。
- **C** = 仅发现线索：目录、经纪页、社交帖子、会议议程、转载 MoU、无源市场清单、招聘广告、泛 "cloud region" 营销。
- 状态语义与官方线索字段：`official_sources`（LGU/NTC/DICT/EMB/DOE-ERC-NGCP-utility/PEZA/BOI/NPC/cloud-official）、`ntc_registration_type`（DTIP/VAS/PTE/CLS/unknown）、`power_MW_or_MVA`、`utility_or_grid_node`、`incentive_registration`；容量需公用事业/ERC/NGCP 佐证。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中的 PH 记录与种子（VITRO 组合、STT GDC、Equinix MN1-3、Converge、DITO Clark、SpaceDC、EdgeConneX、Flow/A-Flow、DAMAC/EDGNEX、North Luzon Data Center、GovCloud 认证商）。
2. 归一化实体：品牌、SEC/法律实体、NTC 注册持有人、PEZA/BOI 企业、SPV/地主、设施品牌；地理解析到当前 PSGC 区域/省/市/barangay/工业园区（"Manila" → 实际城市）。
3. 官方链交叉验证：LGU → EMB → 公用事业/ERC/NGCP → PEZA/BOI → NTC → DICT → NPC；互联检查：IXP、PeeringDB、海缆登陆、Direct Connect/云入口、运营商列表。
4. 逐区扫描：Tier 1（NCR、CALABARZON、Central Luzon）详尽；Tier 2（Central Visayas、Davao、NIR、Western Visayas、Ilocos-CAR、Cagayan Valley、Northern Mindanao）区域边缘/BPO/海缆/政府/DR；Tier 3（Bicol、Eastern Visayas、Zamboanga、Soccsksargen、Caraga、BARMM、Mimaropa）政府/电信边缘/能源主导。
5. 输出 schema：`{country_code: PH, country_name: Philippines, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`（division 用 18 区现行名；notes 保留 marketed_MW vs IT_load_MW 区分与官方线索已拉取清单）；阴性区 `no_projects: true`。不动 explorer-*.md，NO-DELETION。

## 待办（2026-08-12）

- [ ] NIR 记录迁移：把 Negros Occidental/Bacolod、Negros Oriental、Siquijor 记录按现行 PSGC 重新指派。
- [ ] STT Fairview 园区：核实 Fairview 1 运营状态与 124 MW 园区目标分期。
- [ ] DAMAC/EDGNEX Laguna：寻找 LGU/EMB/公用事业/PEZA/BOI/运营商设施证据以升级 planned。
- [ ] SpaceDC MNL1：用 SpaceDC/EMB/LGU 证据核实状态与 MW。
- [ ] Equinix MN1-3 ex-TIM：确认机柜/容量与 IX 托管细节。
- [ ] VITRO Sta. Rosa：用官方/许可/公用事业证据核实 50MW 级主张与专用变电站。
- [ ] AWS Local Zone/Direct Connect 物理节点：确认宿主设施（ePLDT Makati 2 等）。
- [ ] 云区域阴性对照（含 PH 区域传闻）与 ECC 检索（SPV/地主/园区词）：每次运行复查。
