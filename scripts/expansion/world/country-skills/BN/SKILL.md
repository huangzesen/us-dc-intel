---
name: bn-datacenter-methodology
location: scripts/expansion/world/country-skills/BN/SKILL.md
description: |
  Brunei Darussalam (BN) datacenter discovery & audit methodology — how to enumerate, verify, and update Brunei datacenter projects at district granularity (4 districts in the current manifest: Brunei-Muara, Belait, Tutong, Temburong). Brunei is a tiny state-led market: no public national datacenter registry; enumeration joins AITI licensing, EGNC government data-centre pages, UNN/DST/imagine/BIG operator pages, submarine cable landing records (Tungku, Telisai), DES/Berakas Power energy records, procurement, cloud-provider region pages (all negative for BN), and trade press. Read this before running BN exploration/audit batches. Routes to explorer-official.md (official/regulatory/cloud pipeline) and explorer-industry.md (industry/vendor discovery).
---

# BN · 文莱数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：文莱**没有**公共国家数据中心注册库，不能按注册库枚举；市场极小且国有主导。
> 文莱枚举靠**官方管线拼接**：AITI 牌照、EGNC（电子政府国家中心）数据中心页、UNN/DST/imagine/BIG 运营商页、海缆登陆记录（Tungku 文莱-穆阿拉、Telisai 都东）、DES/Berakas Power 能源记录、采购与贸易媒体；云厂商区域表为负面检查。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供文莱探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：AITI 牌照与市场结构、MTIC/Digital Brunei 政策、EGNC 政府数据中心（Gadong）、UNN 设施页、DES/能源部/BPC 电力、海缆登陆站、云区域负面清单、Uptime 注册负面检查 |
| `explorer-industry.md` | 行业/厂商发现：运营商种子（UNN BRUDC2/3/4、EGNC、DST、BIG、Tech Greencloud）、贸易媒体（DCD/The Scoop/Borneo Bulletin/The Bruneian）、目录、Borneo-IX 与海缆管线、分区扫描、月度/季度更新节奏 |

## 核心结构事实（框定每次搜索）

1. **行政区划 = 4 区（district）**：Brunei-Muara（首都区，含 BSB、Gadong、Tungku、Berakas、Jerudong）、Belait（Kuala Belait、Seria、Lumut，油气腹地）、Tutong（Tutong 镇、Telisai）、Temburong（东部飞地，雨林为主）；四行全部记录，负面也要记。
2. **国有整合市场**：2019-2020 年电信与数字基础设施整合进 **Unified National Networks（UNN）**（国有批发网络公司，吸收 TelBru、DST、Progresif、BIG 资产及海缆资产）；DST/imagine 等在其上销售服务；政府自营共享服务数据中心由 **EGNC**（Gadong）运营。
3. **设施锚点集中在 Brunei-Muara**：UNN Tungku 预制 DC / `BRUDC4`（51,000 sq ft 园区、一期 200 机架、2023-04 开工、UNN 托管页在售）、`BRUDC2 Sumbiling Telhouse DC`、`BRUDC3 Tungku DC`（Tungku Zone 8 见 DST-UNN 2025-12-02 转售协议）、EGNC 政府/私营托管（Gadong, Jalan E-Kerajaan, Simpang 69-18, BE1110）、DST 托管服务（轻资产，容量来自 UNN）、Tech Greencloud（目录线索 C）。
4. **基础设施 ≠ 数据中心**：Tungku（文莱-穆阿拉）与 Telisai（都东）海缆登陆站、Borneo-IX（Tungku CLS，2021-02-04 成立，UNN+DE-CIX）、NiAT Telisai 卫星地球站均为数字基础设施锚点，只有配套文档化托管/DC 房间才计为数据中心行。
5. **无超大规模公共云区域**：2026-08-12 检查 AWS/Azure/GCP/OCI 官方区域表均无文莱条目；最近东盟区域为新加坡/马来西亚/印尼/泰国/雅加达等（按厂商而异）；本地 `cloud` 营销 = 本地托管服务。
6. **Tier/ISO 是设计/合规声称**：UNN “Tier 3 Uptime Certified Design”、Vertiv “electrical Tier IV / mechanical Tier III” 均为设计声称；只有 Uptime Institute 注册表条目证明认证（本通过检查无文莱条目）；ISO 27001 同为运营商声称。
7. **容量语义**：文莱设施极少公布 MW——最强公开规模是 UNN Tungku 一期 200 机架 / 51,000 sq ft 园区；EGNC 公布机架产品细节而非设施总机架数；不得编造 MW/机架数。
8. **政策管线**：Wawasan 2035、Digital Economy Masterplan 2025（2020-06）、Digital Brunei 2030（2026-06-02，MTIC，Digital Brunei Council 2024-08 更名）点名未来国家级 AI 数据中心与主权云——政策管线源，非具体设施证据。
9. **语言**：英语 + 马来语（`pusat data`=数据中心、`pengehosan`=托管、`kolokasi`、`awan`/`pengkomputeran awan`=云、`stesen pendaratan kabel`=海缆登陆站）；官方页面多为双语或英语优先。
10. **诚实产出预期**：全国约 3-6 条可记录项目/设施行（几乎全在 Brunei-Muara）+ 2 条基础设施锚点（Tutong 的 Telisai CLS/地球站）+ 2 个负面区（Belait、Temburong）；无超大规模/区域枢纽市场。

## 常用查询模板（详见 explorer-official.md §3 / explorer-industry.md §1、§3-§5）

- 官方站内：`site:aiti.gov.bn "data centre" OR "pusat data"`、`site:mtic.gov.bn "Digital Brunei 2030" OR "AI-capable Data Centre"`、`site:egnc.gov.bn "data centre" OR "co-location"`、`site:unn.com.bn "BRUDC" OR "Tungku" OR "Sumbiling"`、`site:unn.com.bn "Borneo-IX"`、`site:des.gov.bn "pusat data"`、`site:digitalbrunei.bn "data centre" OR "sovereign cloud"`、`site:data.gov.bn "EGNC"`。
- 马来语：`"pusat data" "Negara Brunei Darussalam" "{district}"`、`"pusat data" "Kerajaan Brunei" OR "EGNC"`、`"pusat data" "stesen pendaratan kabel"`。
- 地点：`"data centre" Brunei "Tungku" OR "Sumbiling" OR "Gadong" OR "Berakas"`、`"Sumbiling Telephone House" "data centre" OR colocation`、`"Berakas Power" "data centre" OR "power feed" OR Tungku`。
- 云负面：`site:docs.aws.amazon.com/global-infrastructure "Brunei"`、`site:learn.microsoft.com/en-us/azure/reliability/regions-list "Brunei"`、`site:cloud.google.com/about/locations "Brunei"`、`site:docs.oracle.com/iaas "Brunei"`。
- 海缆/IXP：`"Tungku" "cable landing" Brunei`、`"Telisai" "landing" Brunei SJC`、`"Asia Link Cable" Brunei UNN "Tungku"`、`"Borneo-IX" UNN DE-CIX`、`site:peeringdb.com Brunei`。
- 贸易媒体：`site:datacenterdynamics.com/en/ Brunei`、`site:thescoop.co UNN OR Borneo-IX OR DST`、`site:borneobulletin.com.bn "pusat data" OR UNN`。

## 官方/监管管线要点（详见 explorer-official.md）

- AITI：国家级信息通信监管；InTi 基础设施牌照确认 UNN 为唯一批发基础设施供应商；竞争/市场管理页确认 UNN SMP；无独立“数据中心”牌照类别（托管/云由持牌电信商或政府 EGNC 交付）——枚举前检查是否有新类别。
- MTIC/Digital Brunei：政策新闻与里程碑；Digital Brunei 2030 为政策管线源（A 级政策日期、U 级设施细节）。
- EGNC：政府 ICT 共享服务局（2008-04-01 成立，原 PMO，2019 转 MTIC）；数据中心共址服务页 + 2026 服务目录给出 Gadong 地址、42U APC 机架、私有套间/共享机房、N+1 UPS、VESDA、FM-200、双路机架电源、备用发电机、CCTV、生物识别/门禁——A 级服务/特性/地址事实。
- UNN：官方页陈述共址“符合 Tier 3 要求”、99.982% 可用性声称、ISO 27001 声称、在售 DC 名单 `BRUDC4`/`BRUDC2`/`BRUDC3`；项目新闻陈述 51,000 sq ft 园区与一期 200 机架——A 级 UNN 声称、U 级 MW/正式认证。
- 能源：DES（发电/输配 + 供电监管）、Ministry of Energy、BPC（Berakas Power，政府关联，为 Tungku 站点第二路独立电源——B 级 DCD 细节）；无公共负荷注册。
- 规划/建筑：Ministry of Development/TCP/建筑控制为预期路径，但无公开在线规划许可检索门户——低产出轨迹，不用 Wikipedia 作规划证据。
- 投资促进：BDEB/InvestBrunei——本次未确认文莱数据中心专项激励，检查后再假设。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 贸易媒体：DCD（B，UNN 建设/2026-01-16 分析/ALC）、The Scoop（B，DST-UNN 2025-12-03、Borneo-IX 2021）、Borneo Bulletin（B）、The Bruneian（B）、Biz Brunei（B）、BruDirect（B）、Everything Brunei（B/C 镜像）、Vertiv（B，厂商自有工作）、Submarine Networks（B）、SubTel Forum/Capacity Media/Telecompaper（B）、6Wresearch（C 市场报告）。
- 目录（C 级线索）：DataCenterMap（UNN Tungku SCLS 条目 + Tech Greencloud Zainuddin Complex）、Datacenters.com、Inflect、Cloudscene、OCOLO/ColocationM/UpStack、D&B/LinkedIn（公司事实 B、设施声称 C）。
- 目录到一手验证：目录种子 → UNN/EGNC/运营商官方页 → AITI → 可靠本地媒体 → 仍仅目录则 C。
- 误报控制：本地 VPS/云/托管营销 ≠ 数据中心；Borneo-IX/海缆登陆站/卫星地球站 ≠ 数据中心；`cloud` 营销 = 本地托管；油气行业“data centre”多为内部机房；`data centre` 也可能出现在无关上下文（配送中心、开斋节中心）。
- 2026-06 内阁改组后：引用结构前重新核实 EGNC/AITI/MTIC 部委归属。

## 来源分级

- **A** = 运营商官方页、公共部门页、监管/许可源、上市公司文件、Uptime Institute 注册表、云官方区域页（区域存在/缺失）。
- **B** = 具名可靠贸易/本地媒体（DCD、The Scoop、Borneo Bulletin、The Bruneian 等）、厂商对自有工作的声明（Vertiv）。
- **C** = 目录/市场页/SEO 托管页/合作伙伴列表。
- **U** = 未独立核实。每个字段独立分级：运营商页证明其声称设施/服务，不证明 MW、Uptime 认证或许可。
- **负面检查要记录**：无云区域、无 Uptime 注册条目、Belait/Temburong 无设施——均为 A 级负面事实。

## 维护注意（更新纪律）

- **更新节奏**：月度——UNN 新闻/服务页、DST、imagine、BIG、The Scoop、Borneo Bulletin、The Bruneian、Biz Brunei、BruDirect、DCD 文莱标签、Vertiv 发布；季度——AITI 牌照/指引、EGNC、MTIC/Digital Brunei、DES/energy.gov.bn、PeeringDB/PCH、Submarine Networks/TeleGeography（ALC 状态）、Uptime 注册表、云厂商区域页、目录；半年——BDEB/InvestBrunei、政府采购、data.gov.bn；事件驱动——ALC ready-for-service（Tungku）、UNN Tungku DC 正式投运、DST-UNN 里程碑、Borneo-IX 扩张、Digital Brunei 2030 实施、外资数据中心 MoU、新海缆登陆/电力连接公告。
- **来源验证**：地址优先级 = 运营商官方页 > 政府/EGNC 页 > 可靠本地媒体 > 目录；Tier/ISO 声称与注册表区分；MW/机架不得编造；2026-06 内阁改组后核实部委归属。
- **不删除纪律（NO-DELETION）**：只创建自己的结果文件与 skill 文件；不修改/删除 explorer 源文件与其他工作产物；新证据以新增记录 + 分级并存，不覆盖旧证据；负面区显式记录负面搜索。
