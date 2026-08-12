---
name: bd-datacenter-methodology
location: scripts/expansion/world/country-skills/BD/SKILL.md
description: |
  Bangladesh (BD) datacenter discovery & audit methodology — how to enumerate, verify, and update Bangladesh datacenter projects at division + locality granularity (8 divisions in the current manifest). Bangladesh has no public datacenter registry and no hyperscale cloud region: enumeration joins BTRC/LIMS licensing, RJSC company registry, BCC NDC / BDCCL National Data Centre (Kaliakair, Gazipur) + Meghna Cloud, BHTPA hi-tech parks, e-GP/BPPA procurement and BIDA/BEZA investment records, utility/development-authority evidence, operator pages (Felicity IDC, Fiber@Home, DhakaColo/BDCOLO, ColoAsia, Rajshahi COLO, CoLoCity), and BDIX/PeeringDB plus SMW-4/SMW-5 cable geography. Read this before running BD exploration/audit batches. Routes to explorer-official.md (regulation/registries/state DC/procurement/power) and explorer-industry.md (operators/press/directories/Bengali-language recipes).
---

# BD · 孟加拉国数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：孟加拉国**没有**公开的全国数据中心注册库，也无 AWS/GCP/Azure/Alibaba/OCI/Huawei 公有云区域（每批负向核验）；枚举必须联合 BTRC 牌照、RJSC 法人、国家数据中心（BCC NDC、BDCCL Kaliakair）、BHTPA 高科技园区、e-GP/BPPA 采购、投资/开发区记录、运营商页与 BDIX/PeeringDB、海缆地理（SMW-4 Cox's Bazar、SMW-5 Kuakata）多轨交叉。总部、电信交换局、NOC、IXP、CDN 缓存、海缆登陆站、转售商页均不算数据中心。
> 分区模型：**8 个专区（divisions）**（Dhaka、Chattogram、Khulna、Rajshahi、Rangpur、Sylhet、Mymensingh、Barishal）；Dhaka 为全国枢纽（含 Kaliakair/Gazipur 高科技城），Chattogram 为次枢纽（含海缆/港口/SEZ），其余专区低密度。
> 已知种子：BDCCL National Data Centre/4TDC + Meghna Cloud（Kaliakair）、BCC NDC（ICT Tower, Agargaon, Dhaka）、Felicity IDC（Kaliakair，Uptime 认证）、Fiber@Home、Grameenphone Super Core DC（Sylhet，2024-01-30 启运 4 MW）、BTCL/ADB 绿色 DC（Chattogram 附近，计划中）、DhakaColo/BDCOLO、ColoAsia、Rajshahi COLO、CoLoCity、Yotta/DataVolt/Summit（宣布/计划）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供孟加拉国探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：BTRC/LIMS 牌照（电信法 2001）、RJSC 法人（公司法 1994）、网络安全/个保条例 2025、ICT Division/BCC/NDC/a2i、BDCCL/Meghna Cloud、BHTPA 高科技园区、BIDA/BEZA/BEPZA 投资与 e-GP/BPPA 采购、RAJUK/CDA/KDA/RDA 开发当局、BPDB/PGCB/DPDC/DESCO/REB/BERC 电力、8 专区逐区期望与已知证据表 |
| `explorer-industry.md` | 行业/厂商发现：运营商种子表（BDCCL/BCC/Felicity/Fiber@Home/DhakaColo/ColoAsia/Rajshahi COLO/CoLoCity/Colocloud/BengalCloud/Aamra/XeonBD/GP/BTCL/BSCCL/Yotta/DataVolt/Summit）、DCD/W.Media/TBS/Daily Star 等媒体、目录（C）、BDIX/SDNF/PeeringDB 互连、SMW-4/5/6 海缆、孟加拉语查询配方、8 专区剧本 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库、无云区域**：记录必须联合牌照/法人/园区/采购/运营商/互连证据；云场景通常是 Meghna Cloud、BCC NDC 云、本地 colo 或私有云，不等于超大规模区域。
2. **政府/国资数据中心是官方锚点**：BCC NDC（Agargaon，云/VPS/colo 服务文档，A）；BDCCL National Data Centre/4TDC（Bangabandhu Hi-Tech City, Kaliakair, Gazipur，A 存在/位置）+ Meghna Cloud（2024-02 启运，B 时间线）；Tier/MW/面积等营销数字保持 B 直到独立认证。
3. **BTRC 证运营商身份，LIMS 非注册库**：ISP/NTTN/IIG/IGW/ICX/VSAT/移动牌照用于运营商上下文；设施状态仍需他源；法人用 RJSC（app.roc.gov.bd/psp/nc_search）按法定名与商号匹配。
4. **BHTPA 高科技园区是主机地理**：Kaliakair 承载 BDCCL/Felicity/Yotta/DataVolt 等；Jashore Software Technology Park 对 Khulna 专区重要；园区页/投资者记录点名数据中心才算数。
5. **采购/投资记录只在其点名项目时用**：e-GP/BPPA、BIDA/BEZA/BEPZA、Planning Commission/IMED；通用 ICT 设备或服务器机房采购仅为线索。
6. **电力证据用于风险/区位验证**：BPDB/PGCB/DPDC/DESCO/REB/BERC 的变电站/馈线/电价/停电/气荒背景；不从发电机营销推断 MW。
7. **互连与海缆是枢轴非设施证据**：BDIX（PeeringDB ix/2516）Dhaka/Chattogram；SMW-4 Cox's Bazar、SMW-5 Kuakata（Barishal）、SMW-6 状态待查；登陆站 ≠ 数据中心，除非 BSCCL 点名 colo/IDC 服务。
8. **语言**：孟加拉语 `ডেটা সেন্টার`/`ডাটা সেন্টার`/`আইডিসি`/`কোলোকেশন`/`সার্ভার`/`ক্লাউড`/`জাতীয় ডেটা সেন্টার` + 英语变体（Chattogram/Chittagong、Kaliakair/Kaliakoir）双轨必搜；目录页（如 Mymensingh）不代表设施存在。

## 查询模式（复制粘贴模板见 explorer-official.md §3 / explorer-industry.md §7）

- 官方：`"{division_en}" Bangladesh ("data center" OR datacenter OR IDC OR colocation) site:gov.bd`、`site:btrc.gov.bd ("data center" OR NTTN OR license)`、`site:ndc.bcc.gov.bd OR site:bcc.gov.bd ("data center" OR cloud OR colocation)`、`site:bdccl.gov.bd ("data center" OR Tier OR Meghna)`、`site:bhtpa.gov.bd ("data center" OR "hi-tech park" OR investor)`、`site:eprocure.gov.bd ("data center" OR IDC OR server)`。
- 孟加拉语：`"{division_bn}" ("ডেটা সেন্টার" OR "ডাটা সেন্টার" OR সার্ভার OR কোলোকেশন) site:gov.bd`、`"জাতীয় ডেটা সেন্টার" (Gazipur OR Kaliakair OR Dhaka)`。
- 法人：`app.roc.gov.bd/psp/nc_search "{company}"`、`"{company}" "RJSC" Bangladesh`。
- 采购/投资：`site:eprocure.gov.bd ("data center" OR "server room")`、`site:bida.gov.bd OR site:investbangladesh.gov.bd ("data center" OR "digital infrastructure")`、`site:plancomm.gov.bd OR site:imed.gov.bd ("data center" OR Kaliakair)`。
- 电力：`site:bpdb.gov.bd OR site:pgcb.gov.bd ("data center" OR electricity OR substation)`、`"Bangladesh" ("load shedding" OR "gas crisis") "data center"`。
- 行业：`site:datacenterdynamics.com Bangladesh ("data center" OR "green data centre")`、`site:w.media Bangladesh ("data center" OR "digital infrastructure")`、`site:tbsnews.net Bangladesh ("data centre" OR Summit OR BTCL OR Grameenphone)`、`"{company}" Bangladesh ("data center" OR IDC OR colocation) 2024 2025 2026`。
- 互连/海缆：`site:bdix.net OR site:peeringdb.com Bangladesh (BDIX OR facility OR Chattogram)`、`site:submarinenetworks.com Bangladesh ("Cox's Bazar" OR Kuakata OR SMW-4 OR SMW-5)`、`"Kuakata" ("data center" OR "landing station" OR IDC)`。

## 官方/监管管线要点（详见 explorer-official.md）

- 入口：BTRC/LIMS → BCC/NDC + BDCCL/Meghna → BHTPA → RJSC 法人 → e-GP/BPPA + BIDA/BEZA/BEPZA → RAJUK/CDA/KDA/RDA 与市镇当局（无实用全国建筑许可关键词搜索）→ BPDB/PGCB/DPDC/DESCO 电力 → Planning Commission/IMED。
- 8 专区姿态：Dhaka 枢纽（Kaliakair/Gazipur 国家 DC 群 + Dhaka 城区 colo 群）；Chattogram（BTCL/ADB 绿色 DC 计划、SMW-4、BDIX Chattogram、Agrabad/NRB 线索）；Khulna（Jashore 科技园 + DhakaColo/ColoAsia/BengalCloud 线索）；Sylhet（GP Super Core 已确认）；Rajshahi（Rajshahi COLO、Bogura 线索）；Rangpur/Mymensingh/Barishal 稀疏——`no_projects` 仅在有记录的双语负向扫描后标注。
- 证据规则：按字段分级（A/B/C/U）；运营商营销 A 只对其自身声明，Tier/MW/机架/“最大/首个”保持 B 除非认证；公告/MoU/投资声明 = 计划，直到许可/建设/投运/开业；登陆站/IXP/NOC/交换局/CDN 缓存不计数。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商种子：BDCCL/Meghna（A 官方/B 媒体）、BCC NDC（A）、Felicity IDC（A 运营商页 + Uptime 客户端页，PeeringDB org/40434）、Fiber@Home（A 服务页）、DhakaColo/BDCOLO（A 运营商声明多城链；逐址 C）、ColoAsia（A 存在/C 逐址）、Rajshahi COLO（A 活跃服务）、CoLoCity（A 服务/B-C 历史）、Colocloud（C）、BengalCloud/ADNGateway（A 声明/C 站点独立）、Aamra/XeonBD（C）、GP Super Core Sylhet（B，GP 主源待 A）、BTCL/ADB 绿色 DC（B 计划/U 建设）、Yotta Dhaka（B/C 计划，4,800 机架 28.8 MW Kaliakair）、DataVolt（B/C 宣布 $100m）、Summit Group（B 计划 2026）、小主机商（C 线索/转售）。
- 高信号媒体：DCD Bangladesh tag、W.Media、The Business Standard、Daily Star、Dhaka Tribune、Prothom Alo、UNB/BSS、New Age、Financial Express、Developing Telecoms/TelecomTalk（B）。
- 目录（C，仅种子）：DatacenterMap、Datacenters.com、DataCentersList、Baxtel（GP Sylhet 线索）、Inflect、OCOLO/DC Atlas/DCPulse、colocation.bd、Mordor/Arizton 等市场报告。
- 状态映射：运营=活跃服务页/官方开业/活跃 PeeringDB 设施证据；建设=许可/电网/动工/EPC/PPP 授标；批准/计划=内阁批准/MoU/招标/投资批准；仅线索=目录/社媒/市场报告提及。

## 已知设施/项目与证据状态

| 设施/项目 | 专区/地点 | 状态与证据 |
|---|---|---|
| BDCCL National Data Centre / 4TDC | Dhaka/Kaliakair, Gazipur | 运营；A（bdccl.gov.bd 官方）+ B（20 万 sq ft/发电机/Tier IV 营销）；DCD 佐证 Meghna 2024-02 启运 |
| Meghna Cloud（BDCCL/Gennext） | Dhaka/Kaliakair | 运营；A（官方服务页）+ B（2024-02 启运、JV 历史、DCD/Daily Star/Dhaka Tribune） |
| BCC National Data Center | Dhaka/Agargaon, ICT Tower | 运营；A（ndc.bcc.gov.bd + NDC 服务文档）；容量/Tier 待独立支持 |
| Felicity IDC Limited | Dhaka/Kaliakair Hi-Tech Park | 运营；A（felicity.net.bd + Uptime 客户端页/923）；面积/机架/MW 为营销声明 |
| Fiber@Home colocation | Dhaka | 运营服务；A（fiberathome.net/co-location）；设施/地址粒度待逐址确认 |
| Grameenphone Super Core DC | Sylhet | 运营；B（DCD + 孟媒，2024-01-30 启运、4 MW、GP+ZTE、Tier III 标准但非 Uptime 列表）；GP 主源待 A |
| BTCL/ADB 绿色数据中心 | Chattogram 附近（BTCL 地块） | 计划/PPP 线索；B（UNB/TBS/DCD 2025-01）；无运营证据 |
| BSCCL 登陆站：Cox's Bazar SMW-4；Kuakata SMW-5 | Chattogram；Barishal | A/B（海缆事实）；登陆站商业 DC/colo U/C 待 BSCCL 点名 |
| DhakaColo / BDCOLO 链 | Dhaka、Chattogram、Khulna/Jashore、Sylhet | A（运营商多城声明）；各物理址 C 待逐点确认 |
| ColoAsia | Dhaka、Khulna/Jashore、Sylhet、Rajshahi/Bogura（声明不一） | A（colooasiabd.com 存在）/C（目录地址细节）；逐址核验后计数 |
| Rajshahi COLO | Rajshahi | A/C（rajshahicolo.com 活跃支持服务存在）；Tier/日期/地址需独立证明 |
| CoLoCity | Dhaka/Mohakhali | A（colocity.com.bd 服务存在）；历史“首个/Tier”声明 B/C |
| Colocloud | 多址声明 | C；物理站点证实前不计入 |
| BengalCloud / ADNGateway | Dhaka、Khulna/Jashore | A（运营商声明）/C（站点独立性与宿主） |
| Yotta Dhaka | Dhaka/Kaliakair | 计划；B/C（DCD 2023：两栋、4,800 机架、28.8 MW，Shamsul Alamin Group）；无运营 |
| DataVolt Bangladesh | Dhaka/BHTC | 宣布；B/C（DCD/W.Media：$100m、3 英亩）；建设/运营 U |
| Summit Group DC | Dhaka 附近 | 计划；B（TBS 2026 计划，依托气/电/光纤资产）；无物理记录 |
| Aamra / XeonBD / Wolast / ACP / Nova Colo / ColoBD / Gotipath 等小主机 | Dhaka 等 | C 线索/转售服务；除非设施业主/地址/宿主可验证，否则不建独立设施记录 |
| Banglalink / Robi / Teletalk 内部 DC | 各专区 | U；点名设施前不计数 |

## 更新节奏

- 每月：BTRC 公告、e-GP/BPPA 招标、BDCCL/BCC/BHTPA 新闻、DCD/W.Media/TBS/Daily Star/Dhaka Tribune/UNB/BSS 搜索。
- 季度：超大规模官方区域表（AWS/GCP/Azure/Alibaba/OCI/Huawei）、Uptime 授奖、PeeringDB 国家/IX/设施记录、Yotta/DataVolt/Summit/BTCL-ADB 状态、BIDA/BEZA/BEPZA 项目页。
- 待办（2026-08-12）：两份 explorer 初稿已完成（codex 复核）；下一步 codex terra agent 分批复核（8 专区粒度，含双语负向扫描日志）；本 skill 作为国家层参考注入。
