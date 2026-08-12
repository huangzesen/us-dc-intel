---
name: mm-datacenter-methodology
location: scripts/expansion/world/country-skills/MM/SKILL.md
description: |
  Myanmar (MM) datacenter discovery & audit methodology — how to enumerate, verify, and update Myanmar datacenter projects at Region/State/Union-Territory granularity (15 first-level units: 7 Regions, 7 States, Naypyidaw UT). Myanmar has no national datacenter registry, no DC-specific approval list, and no usable public building-permit search; the market is small and concentrated in Yangon, Naypyidaw, and Mandalay. Enumeration joins PTD telecom-law licensing, DICA/MyCO entity + MIC/Region-State investment approvals, YCDC/YBPS building permits (Yangon only), MONREC/ECD environmental and Thilawa SEZ records, MOEP/YESC/MESC/ESE power evidence, operator-primary pages (True IDC, MICTDC, MPT, MTG, Mytel), MMIX/PeeringDB, and official cloud-region lists (no hyperscaler region in Myanmar). English + Burmese search is mandatory, plus Vietnamese (Mytel), Thai (True IDC), Chinese (Huawei/Campana/SEZ). Read this before running MM exploration/audit batches. Routes to explorer-official.md (PTD/DICA/permits/power/cloud) and explorer-industry.md (operator/press/IXP/division playbook).
---

# MM · 缅甸数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：缅甸**没有**全国数据中心注册库、**没有** DC 专用公共审批清单、**没有**可用的全国建筑许可检索——市场小而高度集中于 **Yangon、Naypyidaw、Mandalay**。
> 枚举靠**多轨交叉**：PTD 电信法/牌照框架、DICA/MyCO 法人查询 + MIC/省邦投资委批复、YCDC/YBPS 建筑许可（仅 Yangon）、MONREC/ECD 环评与 Thilawa SEZ、MOEP/YESC/MESC/ESE 电力、运营商一手页（True IDC、MICTDC、MPT、MTG、Mytel）、MMIX/PeeringDB、官方云区域清单（**无任何超大规模区域**）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供缅甸探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/电力/云管线：PTD 电信法与牌照、DICA/MyCO/MIC/Project Bank（MTG DC、e-Government Integrated Data Center）、YCDC/YBPS 许可、MONREC/ECD/Thilawa SEZ、MOEP/YESC/MESC/ESE 电力、网络安全法 1/2025、云区域缺失核查、15 省逐省策略与状态规则 |
| `explorer-industry.md` | 行业/厂商发现：英缅双语词表与模板、高信号媒体（DCD/W.Media/Frontier/Eleven/Irrawaddy/GNLM/MDN）、市场与聚合源、运营商/设施种子表（True IDC/MICTDC/MPT/Mytel/MTG/Ocean Wave/Zenlayer/Burst/Campana）、连通性证据（SMW3/SMW5/AAE-1/UMO-SIGMAR/MMIX）、逐省 playbook、证据规则与陷阱 |

## 核心结构事实（框定每次搜索）

1. **15 个一级单位**：7 省（Ayeyarwady、Bago、Magway、Mandalay、Sagaing、Tanintharyi、Yangon）+ 7 邦（Chin、Kachin、Kayah、Kayin、Mon、Rakhine、Shan）+ Naypyidaw 联邦区；自洽区/分区不单独算一级覆盖。
2. **无全国注册库**：枚举 = PTD 法律框架 + DICA/MyCO/MIC 实体与投资批复 + YCDC/YBPS（Yangon）许可 + MONREC/ECD/SEZ 环境 + MOEP/YESC/MESC/ESE 电力 + 运营商一手页 + MMIX/PeeringDB + 官方云区域清单。
3. **已确认设施种子（A=存在/位置）**：True IDC Myanmar（MICT Park, Hlaing, Yangon，2015 年设立，首个商业 DC）；MICT Data Center（ICT Park Hlaing，官方页称 Tier III、至多 162 racks——容量为 B）；MPT Data Centers（Yangon Hantharwady/Bayintnaung + Naypyitaw Dekkhina，官方页，A）；MTG DC（Dekkhinathiri, Naypyidaw，DICA 2019 实地访问确认，A）；Mytel Data Center（Yangon，Viettel 家族新闻 2023-08-26 开业、Tier 3-standard、600 racks 可扩 1,000——**B+，容量为声称**）；e-Government Integrated Data Center（Project Bank：主 DC 在 Naypyidaw、DR 在 Yangon，A 计划/批复级）；MMIX Yangon @ True IDC（PeeringDB，A IXP/设施映射）。
4. **无超大规模云区域**：AWS/GCP/Azure/Alibaba Cloud/Huawei Cloud 官方清单均无缅甸区域——不得建 hyperscaler-region 记录；本地云/colo/互联：MPT Cloud（IaaS 托管于缅甸境内 DC，A 服务存在）、True IDC、MICTDC、MTG、Mytel、Zenlayer Yangon（A- 城市存在，B/C 物理宿主推断）。
5. **连通性 ≠ 设施**：SMW5/AAE-1 在 Ngwe Saung、SMW3 在 Pyapon、UMO/SIGMAR 至 Thanlyin——海缆登陆站是电信设施，除非点名商业 colo/服务器托管/DC 建筑；边境光纤（Muse/Ruili、Myawaddy/Mae Sot、Tachileik/Mae Sai、Tamu）只作 edge/cache/机房线索。
6. **语言**：英语 + 缅甸语强制（`ဒေတာစင်တာ`=data center、`အင်တာနက်ဒိတ်`=IDC、`က‌‌လောက်`=cloud、`ဆာဗာ`/`ဆာဗာခန်း`=server/机房、`လိုင်စင်`=licence、`ရင်းနှီးမြှုပ်နှံမှု`=investment、`ဆောက်လုပ်ရေး`=construction、`ခွင့်ပြုချက်`=permit、`လျှပ်စစ်`=electricity）；另用越南语（Mytel/Viettel）、泰语（True IDC）、中文（华为/Campana/SEZ）。
7. **风险环境**：电网不稳/燃料短缺/制裁合规/汇率管制/冲突安全是运营约束与风险字段；Kayin/Shan 的 server-farm/诈骗窝点报道须与合法商业 DC 枚举分离，记录前验证合法所有者与合法服务。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§4 与 explorer-industry.md §1-§7）

- PTD：`site:ptd.gov.mm ("data center" OR "datacenter" OR "IDC" OR "colocation")`、`"PTD" Myanmar "{operator}" ("licence" OR "license")`。
- 投资/实体：`site:dica.gov.mm ("data center" OR "datacenter" OR "ICT")`、`site:projectbank.gov.mm "data center" Myanmar`、`site:gnlm.com.mm (MIC) "data center"`、`myco.dica.gov.mm "{company name}"`。
- 许可：`site:ybps.ycdc.gov.mm "{township}"`、`"YCDC" "building permit" "{company}" Myanmar`、`"Mandalay City Development Committee" "{company}" "data center"`。
- 环境/SEZ：`site:monrec.gov.mm ("data center" OR "EIA")`、`site:thilawasez.gov.mm ("data center" OR "datacenter" OR "ICT" OR "Burst")`。
- 电力：`site:yesc.gov.mm "{township}"`、`"Yangon Electricity Supply Corporation" "{township}" "data center"`、`"Myanmar" "electricity blackouts" "data center"`。
- 云核查：`"Myanmar" "cloud region" ("AWS" OR "Azure" OR "Google Cloud" OR "Alibaba Cloud" OR "Huawei Cloud")`、`"MPT Cloud" "hosted at Data Center in Myanmar"`。
- 行业：`site:datacenterdynamics.com (Myanmar OR Burma) ("data center" OR datacenter OR submarine)`、`site:gnlm.com.mm ("data center" OR "ICT") ("investment" OR "opening")`、`"Mytel" "data center" "Yangon"`。
- 通用 division：`"{division_en}" Myanmar ("data center" OR "datacenter" OR "IDC" OR "colocation" OR "cloud" OR "server room")`、`"{division_my}" ("ဒေတာစင်တာ" OR "အင်တာနက်ဒိတ်" OR "ကလောက်" OR "ဆာဗာခန်း")`。

## 官方/监管管线要点（详见 explorer-official.md）

- **PTD/MOTC**（https://www.ptd.gov.mm/）：电信法 2013、NFS 牌照模板、频谱路线图——法律类别与监管身份（Network Facilities Service / Network Service Provider / Service & VAS）；**PTD 不是可靠公共 licensee 库**，作法律上下文并连到 MyCO/MIC/运营商页/媒体。
- **DICA/MyCO/MIC/省邦投资委**（https://www.dica.gov.mm/、MyCO 法人检索、GNLM 州报 MIC 批次、Project Bank）：实体/项目/批复/实地访问为 A；MTG DC（Dekkhinathiri 2019-08-29 实地访问）与 e-Government Integrated Data Center（PB-ID-1126）为已确认官方线索。
- **YCDC/YBPS**（https://ybps.ycdc.gov.mm/）：真实可用但只做流程/统计，**不是 DC 关键词库**；建筑许可仅在具名业主/项目/地块/建筑/镇区时才升为 A 设施证据。Mandalay/Naypyidaw 无可靠公开许可检索。
- **MONREC/ECD/Thilawa SEZ**：数据中心不会可靠出现在公开 EIA 列表；按项目/实体与相关电力/变电站/发电机工程搜；**EIA 缺失不是否定证据**。
- **MOEP/YESC/MESC/ESE**：证明电价/变压器/停电/地方电力条件，极少具名 DC；UPS/发电机声称只作设施特性，**不推断 MW load**（除非原文声明）。
- **网络安全法 1/2025**（2025-07-30 生效，法律分析）：数字平台与网络安全服务商注册/牌照义务、关键信息基础设施——**需求与合规驱动，不是设施清单**；DLA Piper 称缅甸无一般性独立数据保护法。
- **云区域页**：AWS/GCP/Azure/Alibaba/Huawei 官方清单均无缅甸；本地云经 MPT Cloud；外部云经新加坡/泰国等 APAC 区域互联。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商种子（A=官方存在/B=容量/Tier）**：True IDC Myanmar、MICTDC、MPT（Yangon 双址 + Naypyitaw Dekkhina）、Mytel（容量声称）、MTG DC、Zenlayer Yangon、Ocean Wave IDC/MMIX Mandalay（B，须存档官方 MMIX/运营商源）、IT Spectrum DC-2/MMIX Naypyitaw POP（B）、Burst Myanmar/Thilawa SEZ（C，目录线索，须 SEZ/运营商/Uptime/许可验证）、Campana/UMO/SIGMAR（B/C，海缆/模块化基础设施线索）、Seanet MICT Park 卫星地面站（B/C，非 colo DC）、GDMS（C，无具名设施）。
- **媒体分级**：DCD（B）、W.Media（B）、Frontier Myanmar/Frontier Energy（B，电力/制裁/经济）、Eleven Myanmar（B，停电/电信）、The Irrawaddy（B，政策/冲突风险）、GNLM（州报，A-/B）、MDN（州新闻，A-/B）、Myanmar Now/Mizzima/DVB（B，MyCO 限制/制裁/网络控制）、Myanmar Insider（B，牌照监管）、MMNOG/MMIX（A，IXP 事实）、Viettel Family（B+，母公司事实，容量仍为声称）、True IDC 官网（A）、新华社/中国媒体（B/C）。
- **聚合源**：Mordor/DataCenterMap/Baxtel/Inflect/Cloudscene 等 C 级线索；US ITA Burma Digital Economy（B 背景）、DLA Piper（B 法律）、PeeringDB（A 自报 IXP/设施事实）。
- **防重/防陷阱**：MMIX 节点、Zenlayer PoP、云互联、海缆登陆站可能位于另一设施内部——按物理 locality/运营商/地址/IXP-ASN 匹配去重；"Myanmar" 营销默认 Yangon 除非点名 Naypyidaw/Mandalay（MPT 与 MTG 是 Naypyidaw 例外）；rack/MW/Tier/SLA 声称 B 除非官方证书或工程文件；Kayin/Shan 诈骗窝点区域须法律所有者+合法服务验证。

## 来源分级

- **A** = 官方/一手：PTD 法律/规则/模板/通知、MyCO/DICA/MIC/Project Bank、具名 YCDC/YBPS/MCDC/NDC/DHSHD 许可、MOEP/YESC/MESC/ESE 官方电力声明、MONREC/ECD/SEZ 官方记录（项目具名时）、运营商一手页（存在/位置/服务）、MMIX/PeeringDB（IXP 与设施映射）、官方云区域清单。
- **B** = 强二级：律师事务所/监管分析（对法律文本核实）、贸易/本地媒体（发现与事件事实）、Viettel 家族母公司源（具名事实）、US ITA；运营商页上的容量/Tier/SLA 营销声称（除非第三方认证）。
- **C** = 仅线索：目录/聚合器/社交/中介/经纪列表、泛市场报告、无主源转发。
- 状态语义：operational=运营商服务页/官方开业/活跃 IXP 设施/可验证客户面向 colo 云服务；construction=具名许可/电力连接/官方奠基/SEZ 施工通知；approved/planned=MIC/Project Bank/官方批复或政策项目（无运营证明）；lead only=目录/社交/营销；no projects found=英缅双语扫掠+运营商扫掠+官方注册/批复检索+IXP/连通性检索均负之后。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=MM，divisions=15 一级单位）。
2. 建种子：运营商一手页（True IDC/MICTDC/MPT/MTG/Mytel/Zenlayer）+ MMIX/PeeringDB。
3. 对每个实体/项目搜 MyCO/DICA/MIC/Project Bank；对每个 division 跑英缅双语 sweep + 高信号媒体 + 连通性 pivot（Yangon/Ayeyarwady/Mandalay/Naypyidaw/Shan/Kayin）。
4. 验证：字段级分级；A 级存在/位置证据 = 运营商页/政府页/IXP 数据库；容量声称 B 直到认证；把 IXP/PoP/海缆站与宿主设施匹配去重。
5. 记录风险字段（冲突/制裁/电力/燃料）但不得据此抹掉已核实设施。
6. 输出 world schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；no_projects 须有负搜记录。
7. 遵守 NO-DELETION；只新增 SKILL.md 与 ANATOMY.md。

## 待办（2026-08-12 03:00Z）

- [x] explorer-official.md 与 explorer-industry.md 已完成并合并为本 SKILL.md。
- [ ] 下一步：50× codex terra agent 按 15 division 逐省枚举（优先 Yangon、Naypyidaw、Mandalay）。
- [ ] 待核实：Mytel DC 容量与认证（Uptime/工程文件）；Ocean Wave/IT Spectrum 的官方 MMIX/运营商存档；Burst/Thilawa 是否有 SEZ/运营商/Uptime 证据；e-GIDC 实施状态；云区域列表是否新增缅甸。
