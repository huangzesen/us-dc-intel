---
name: lr-datacenter-methodology
location: scripts/expansion/world/country-skills/LR/SKILL.md
description: |
  Liberia (LR) datacenter discovery & audit methodology — how to enumerate, verify, and update Liberia datacenter projects at county granularity (15 counties). Liberia has no public national datacenter registry and no hyperscale cloud region/Uptime Tier III-IV commercial campus; the market is small and Monrovia-led. Enumeration joins LTA telecom licensing, MoPT National Digital Strategy documents (NDC at LTC Mobile, NIR storage, CBL DR center, planned national DR center), EPA EIA/ESIA records, LEC power evidence, PPCC procurement, CCL ACE cable-landing colocation, LIXP/LIXPA interconnection, operator pages, and cloud/Uptime absence checks. Monrovia IN/CA false-positive filtering is mandatory. Read this before running LR exploration/audit batches. Routes to explorer-official.md (LTA/MoPT/EPA/LEC/PPCC/CCL pipeline) and explorer-industry.md (operator/press/cable-IXP/county matrix).
---

# LR · 利比里亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：利比里亚**没有**公开的全国数据中心注册库，也**没有**超大规模云区域或 Uptime Tier III/IV 商业园区（截至复核）——市场**小且由 Monrovia 主导**。
> 枚举靠**多轨交叉**：LTA 电信牌照、MoPT 国家数字战略文件、EPA 环评/ESIA、LEC 电力、PPCC 采购、CCL ACE 海缆登陆/colo、LIXP/LIXPA 互联、运营商页、云区域与 Uptime 缺失核查。
> 已知设施种子集中于 **Montserrado 郡 / Monrovia**：CCL ACE 登陆与 colo/托管节点、LIXP/LIXPA 互联、National Data Center（NDC @ LTC Mobile，建立但利用不足，规划 2025-2027 翻新）、NIR 本地集中存储（规划 NDC colo）、CBL 灾备中心（主要服务金融机构）、电信机房、银行/机构服务器房。本 skill 汇总两份探索报告（官方管线 + 行业发现），供利比里亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/电力/采购管线：LTA 牌照注册表与订单、MoPT/NDS 2025-2029（NDC/NIR/CBL DR/国家 DR 计划）、EPA ESIA、LEC 电力、PPCC 采购、CCL/LIXP/海缆、云与 Uptime 缺失核查、15 郡逐郡官方策略与证据提取清单 |
| `explorer-industry.md` | 行业/厂商发现：运营商与设施种子（CCL/LIXP/LTC-NDC/NIR/CBL/MTN/Orange/银行）、贸易媒体分级（DCD/Capacity/CommsUpdate/SubTel/Developing Telecoms/WeAreTech/TechAfrica）、本地媒体（FrontPageAfrica/Observer/New Dawn/Analyst/LINA）、云/边缘/CDN 核查、目录处理、逐郡行业矩阵、捐赠方信号与终验规则 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库**：枚举 = LTA 牌照 + MoPT 数字战略 + EPA 环评 + 采购 + 电力 + 海缆/IXP + 运营商页 + 本地媒体；牌照本身**不证明物理数据中心**。
2. **官方种子集（A=存在/状态）**：CCL ACE 登陆/托管/colo 节点（Monrovia，运营商页营销 24/7 托管、冗余/安全/NOC、LIXPA 接入 + Google cache——**edge/cache 非 Google 区域**）；LIXP/LIXPA（LTA 确认 2015 年设立、全国首个且唯一 IXP，PCH 确认 Monrovia 活跃，PeeringDB 定位 CCL Building/Libtelco Compound, Lynch Street——**IXP≠数据中心**）；NDC @ LTC Mobile（NDS：已建立、MoPT/LTC Mobile 管理、利用不足/系统过时、2025-2027 翻新路线图——政府 DC，状态=已建立+规划升级）；NIR 本地集中存储（无独立 DR，规划 NDC colo 讨论中）；CBL DR 中心（主要金融机构使用）；国家 DR 中心（**仅计划**，目标 Q4 2027，须 PPCC/MoPT award/EIA/投运证据才升级）。
3. **Monrovia 误报规则**：Monrovia, Indiana 与 Monrovia, California 会产生美国 DC 命中——只计与利比里亚/`.lr`/LTA/LEC/CCL/LIXP/LIXPA/LTC/利比里亚郡或国家码 LR 绑定的记录。
4. **无云区域/Uptime 园区**：AWS/Azure/GCP/Oracle 官方清单无利比里亚区域/Local Zone；接受任何 Tier 声称前先查 Uptime awards list/map 的 Liberia/LR。
5. **语言与拼写**：`data centre`/`data center` 都要搜，另加 `datacentre`/`server room`/`server farm`/`colocation`/`co-location`/`hosting`/`carrier neutral`/`landing station`/`meet-me`/`IXP`/`LIXP`/`cloud`/`sovereign cloud`/`government cloud`/`disaster recovery`/`NDC`/`NIR`/`LTC Mobile`/`generator`/`captive power`/`substation`/`MVA`/`MW`/`Tier III`/`Uptime`；River Cess 与 Rivercess 两种拼写都要搜。
6. **阶段语言纪律**：`plans`/`MoU`/`revamp`/`needs assessment`/`study`/`cloud strategy` 是管道语言非运营状态；`tender`/`RFP`/`PPCC`/`EIA`/`ESIA`/`groundbreaking`/`construction`/`upgrade` 是管道；`commissioned`/`launched`/`opened`/`operational`/`hosting`/`colocation`/`NOC`/`Uptime award`/`customer live` 是运营。
7. **County Service Centers ≠ 数据中心**：15 郡都有 CSC 但 NDS 称资源不足、网络不稳——只作公共服务 ICT/机房线索，除非升级招标具名设施。

## 查询模式（复制粘贴模板见 explorer-official.md 各节 与 explorer-industry.md §查询集）

- LTA：`site:lta.gov.lr "data centre" OR "data center"`、`site:lta.gov.lr LIXP OR LIXPA OR peering`、`site:lta.gov.lr "National Data Center" OR NDC`、`site:lta.gov.lr "{operator}" licence OR license OR registry`。
- MoPT/NDS：`site:mopt.gov.lr "National Data Center" OR "National Data Centre"`、`site:mopt.gov.lr "LTC Mobile" "National Data"`、`site:mopt.gov.lr "NIR" "co-location"`、`"Central Bank of Liberia" "disaster recovery center"`。
- EPA：`site:epa.gov.lr "data centre" OR "data center"`、`"{operator}" Liberia ESIA OR EIA "generator" OR "fuel storage" OR substation`。
- LEC：`site:lecliberia.com substation "Monrovia"`、`"LEC" Liberia "data center" OR "large customer"`、`"{facility}" Liberia substation OR generator OR "fuel storage"`。
- PPCC：`site:ppcc.gov.lr "data center" OR "data centre"`、`site:ppcc.gov.lr "National Data Center" OR "disaster recovery" OR "cloud"`。
- CCL/LIXP：`site:ccliberia.com colocation OR "co-location" OR hosting OR "NOC"`、`site:pch.net "Liberia Internet Exchange Point"`、`"ACE cable" Monrovia "landing station" Liberia`。
- 云缺失：`site:aws.amazon.com Liberia "region" OR "Local Zone"`、`site:uptimeinstitute.com/uptime-institute-awards Liberia OR "LR"`。
- 行业：`site:datacenterdynamics.com/en/news/ Liberia "data centre" OR "landing station"`、`site:commsupdate.com Liberia ACE OR "submarine cable"`、`site:frontpageafricaonline.com Liberia "data center" OR "digital"`。
- 通用 county：`"{county}" Liberia ("data centre" OR "data center") ("MW" OR racks OR "IT load" OR server)`、`"{county}" Liberia "County Service Center" ICT OR server`。

## 官方/监管管线要点（详见 explorer-official.md）

- **LTA**（https://lta.gov.lr/）：牌照注册表、订单与通知、LIXP 页、ccTLD、网络安全、年度报告、行业统计、Liberia Digital Transformation Project/USAID-World Bank 页；扫描 licensee 找移动/固定/ISP/国际网关/海缆/VAS/托管/数据服务运营商。
- **MoPT/OTDI/数字战略**：National Digital Strategy 2025-2029 PDF 是政府 DC 枚举最高价值官方源（NDC@LTC Mobile、NIR、CBL DR、国家 DR 计划、政府云与 DR 路线图、可再生能源评估）；Draft National Data Governance Policy 2026。
- **EPA**：ESIA Procedural Guidelines 2017；DC 项目可能藏在建筑/电信/备用发电机/燃料存储/变电站/光纤/工业园/港口/政府园区升级之下。
- **LEC**（https://lecliberia.com/）：电网可靠性是已知约束——认真设施须查发电机/自备电/燃料存储/冗余；仅电力证据不建 DC 记录。
- **PPCC**（https://www.ppcc.gov.lr/）：招标与合同阶段 A 证据；聚合器招标站只 C 除非链回 PPCC 或采购部委。
- **CCL/LIXP/海缆**：CCL 是利比里亚最强商业/互联种子；LIXP 2015 年设立、LIXPA 运营、Google cache 服务器在 LIXPA；ACE 系统上下文；去重：CCL 设施记录 / LIXP 互联交换 / Google cache 边缘分别处理。
- **云与 Uptime 缺失**：AWS/Azure/GCP/Oracle 官方页无利比里亚区域；Uptime awards list 查 Liberia/LR。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **运营商/设施种子（A=官方存在）**：CCL（主 colo/互联种子）、LIXP/LIXPA（A from LTA、B from PCH、B/C from PeeringDB）、LTC/LTC Mobile（NDC 管理者+老牌运营商）、政府 NDC（NDS A，翻新目标）、NIR、CBL、Lonestar Cell MTN（CCL 股东，聚合器 `MTN Monrovia` 只 C）、Orange Liberia/Cellcom（CCL 股东）、银行（Ecobank/GTBank/UBA/AccessBank/LBDI——银行年报 A，媒体 B/C）、大学/机构机房（通常 C）。
- **媒体分级**：DCD（B）、Capacity（B）、CommsUpdate/TeleGeography（B）、SubTel Forum（B）、Developing Telecoms（B）、WeAreTech Africa（B）、TechAfrica News（B）、FrontPageAfrica（B/C）、Daily Observer（B/C）、The New Dawn（B/C）、The Analyst（B/C）、LINA/MICAT（B，政府新闻）、allAfrica（C/B，须溯源）、tender aggregators（C，须回 PPCC）、US trade guide（B 背景）。
- **目录处理**：datacenters.com/datacenterplatform/colo.exchange/cloudscene/DataCenterMap 等只做线索；`CCLiberia Cable Landing Facility Monrovia` 目录条目须 CCL/LTA/PCH/PeeringDB 确认，**不复制目录容量字段**。
- **捐赠方信号**：World Bank Liberia 项目页、Digital Liberia Week、LTA Liberia Digital Transformation Project、USAID——GREAT project/WARDIP 等计划名**不得**直接转为 DC 记录，除非具名物理设施/采购包/实施站点。
- **去重与终验**：Montserrado 记录（CCL 设施、LIXP/LIXPA、NDC/LTC Mobile、NIR 存储、CBL DR、电信设施、银行设施）仅在证据支持独立物理/运营商身份时分列；每个候选须有郡+城市/地点（最低 Montserrado/Monrovia）；区分设施类型（海缆登陆站、colo/托管室、IXP、电信交换机/数据室、政府 NDC、机构服务器房、银行 DR、云区域）。

## 来源分级

- **A** = 声称事实的一手源：LTA 牌照/订单/页面、MoPT 或官方数字战略/政策文件、EPA EIA/ESIA/许可记录、LEC 公用事业证据、PPCC 招标、CCL 运营商页、官方云厂商位置页、Uptime award 记录、官方运营商/银行/机构/大学设施页。
- **B** = 强二级：世界银行/ECOWAS/USAID 项目文件、贸易媒体（TeleGeography/CommsUpdate/Capacity/DCD）、可信利比里亚媒体（具名站点/阶段）、PeeringDB/PCH（IXP 位置）、具名站点/阶段的政府新闻。
- **C** = 仅弱线索：目录/聚合器、社交帖、市场报告摘要、无 PPCC 链接的采购转载、无站点/状态的 MoU、不能证明数据中心的郡 ICT/机房提及。
- **U** = 不可用（需佐证）：无位置、无利比里亚上下文、泛云营销、Monrovia USA 误报。
- 状态语义：NDC=已建立/利用不足+规划翻新；国家 DR 中心=计划；CCL colo=运营商营销；LIXP=活跃 IXP；NIR colo=NDS 中计划/讨论；绝不从聚合器赋 hyperscale/云区域/Tier III-IV/MW/racks/Uptime 声称。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=LR，divisions=15 郡）。
2. 建种子：CCL、LIXP/LIXPA、NDC/LTC Mobile、NIR、CBL DR + 运营商页 + 银行年报。
3. 逐郡执行官方 pass：LTA → MoPT/NDS → EPA → LEC → PPCC → CCL/海缆 → 云/Uptime 缺失核查 + 行业媒体扫掠。
4. 验证：每条候选记录郡+城市/地点+证据分级+精确 URL；容量字段（IT MW/site MW-MVA/utility import/captive/racks/面积/存储）分列，未公布则 unknown。
5. 过滤 Monrovia IN/CA 误报；区分电缆登陆 vs colo、IXP vs DC、电信交换机 vs 公共 colo、CSC vs DC、银行 DR vs 公共 colo、MoU vs 施工。
6. 输出 world schema：`{country_code, country_name, division, name, status, capacity_mw, developer, source_urls, evidence_date, evidence_grade, notes}`；no_projects 须有负搜记录。
7. 遵守 NO-DELETION；只新增 SKILL.md 与 ANATOMY.md。

## 待办（2026-08-12 03:01Z）

- [x] explorer-official.md 与 explorer-industry.md 已完成并合并为本 SKILL.md。
- [ ] 下一步：50× codex terra agent 按 15 郡逐郡枚举（优先 Montserrado/Monrovia，其余郡以负扫掠+CSC 核查为主）。
- [ ] 待核实：NDC 翻新 2025-2027 的 PPCC/MoPT 招标或 award；国家 DR 中心设立证据；CBL DR 地址/容量；CCL colo 容量官方数据；云区域/Uptime 列表是否新增利比里亚。
