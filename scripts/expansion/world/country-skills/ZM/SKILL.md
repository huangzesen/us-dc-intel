---
name: zm-datacenter-methodology
location: scripts/expansion/world/country-skills/ZM/SKILL.md
description: |
  赞比亚（Zambia, ZM）数据中心发现与审计方法论。10 个省（Lusaka 为主集群）。无国家 DC 登记册、无统一规划许可
  库，需拼接 ZICTA 牌照、ZEMA 环评/发电机/燃料、ERB/ZESCO/CEC/NWEC 电力、ZDA SEZ/MFEZ、Data Protection
  Commission 本地化需求、Smart Zambia/INFRATEL/ZNDC 政府云与市议会许可。已证 A 级种子集中在 Lusaka：
  INFRATEL/Zambia National Data Centre（官方页称运营 3 个国家级 Tier III 数据中心，政府云/colo/备份）、
  Paratus Zambia（Lusaka Tier III-by-design 商业 DC，colo/云/DR，ISO/PCI 认证，DCD 报道 1 MW）、Liquid
  Intelligent Technologies Zambia（Azure Stack/本地云 + 2023 新 DC MoU 管线）、Smart Zambia/华为国家 AI
  数据中心 MoU（2026-05，仅 MoU/intent）。无 AWS/Azure/GCP/OCI/Huawei Cloud 公共区域（Azure Stack 是本地云）。
  详见 explorer-official.md 与 explorer-industry.md。
---

# ZM · 赞比亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：赞比亚是小而早期的 Lusaka-centred DC 市场；官方/运营商级种子比初稿更强（INFRATEL 官方页证实三个国家
> Tier III 数据中心）。电力是门槛过滤器，负载转移（load-shedding）期后备发电/燃料/UPS/太阳能是关键证据字段。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供按 10 省粒度复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：ZICTA 牌照/网关、ZEMA EIA/EPB/EIS、ERB/ZESCO/CEC/NWEC 电力、ZDA SEZ/MFEZ、DPC 本地化、Smart Zambia/INFRATEL/ZNDC、市议会许可、云区域状态表、10 省策略与提取清单。 |
| `explorer-industry.md` | 行业/厂商发现：INFRATEL/Paratus/Liquid/Smart Zambia 种子、Zamtel/MTN/Airtel 核心、Lusaka IXP（PeeringDB ix/615）、DCD/ITWeb Africa/Developing Telecoms/本地媒体、网络/peering/CDN 证据、10 省行业策略与确认工作流。 |

## 核心结构事实（框定每次搜索）

1. **10 省模型**：Central、Copperbelt、Eastern、Luapula、Lusaka、Muchinga、Northern、North-Western、Southern、Western；`North Western` 归一为 `North-Western`。
2. **无国家 DC 登记册/统一许可库**：枚举 = ZICTA + ZEMA + ERB/ZESCO/CEC/NWEC + ZDA SEZ/MFEZ + DPC + Smart Zambia/INFRATEL/ZNDC + 市议会规划/建筑记录。
3. **A 级种子（Lusaka）**：INFRATEL/ZNDC 三个国家 Tier III 数据中心（官方页：数据中心、云、colo、备份、数字服务；议会记录关联 Smart Zambia Phase I 三个 DC + DR 站点）；Paratus Zambia（Lusaka Tier III-by-design、colo/云/DR、ISO 9001/ISO 27001/PCI DSS 认证组页）；Liquid（Azure Stack 启动 + 2023 MoU 新 DC）；Smart Zambia/华为 AI DC MoU（2026-05，仅 MoU/intent）。
4. **状态纪律**：`operational`/`under construction`/`approved`/`planned`/`MoU/intent`/`lead only` 分离；MoU 不计施工、施工不计运营。
5. **Tier 措辞精确**：`Tier III by design` 不得升为 certified Tier III 除非 Uptime/认证证据；`Tier III`、`Tier 3` 按发布措辞原样记录。
6. **无 hyperscaler 公共区域**：AWS/Azure/GCP/OCI/Huawei Cloud 官方表均无 ZM；Azure Stack = 本地/混合云，非 Azure 公共区域。
7. **电力门控**：ZESCO 国家电网、CEC（Copperbelt 矿业电力）、NWEC（Solwezi/Kalumbila/North-Western）；ERB 许可；记录 IT MW/设施 MW/连接负载/MVA/发电机 kVA/太阳能 MW 精确单位，不擅自换算。
8. **telco 核心 ≠ 开放 colo**：Zamtel、MTN Zambia、Airtel Zambia 核心站点是基础设施 lead，除非来源说明开放托管/colo。

## 查询模式（复制粘贴模板见 explorer-official.md / explorer-industry.md）

```text
site:zicta.zm "data centre" OR "data center" OR "gateway licence" OR "{operator}"
site:zema.org.zm ("data centre" OR ICT OR generator OR "fuel storage" OR "Environmental Project Brief") "Lusaka"
site:erb.org.zm OR site:zesco.co.zm OR site:cec.com.zm OR site:northwesternenergycorp.com "{operator}" OR "data centre"
site:zda.org.zm ("data centre" OR ICT OR "Lusaka East" OR "Lusaka South" OR Chambishi OR Kalumbila)
site:dataprotection.gov.zm "data centre" OR "store personal data outside Zambia"
site:infratel.co.zm ("data centre" OR "Tier III" OR "three" OR "Azure Stack" OR colocation)
site:szi.gov.zm OR site:parliament.gov.zm ("National Data Centre" OR ZNDC OR "AI data centre")
"INFRATEL" "three" "data centres" Zambia
"Paratus Zambia" "data center" "Lusaka" "Tier III"
"Liquid Zambia" "Azure Stack" OR "new data centre"
"SMART Zambia" "National AI Data Centre" Huawei
site:lcc.gov.zm OR site:{council-domain} ("data centre" OR "building permit" OR "{operator}")
"{province}" OR "{capital}" "data centre" OR "data center" OR "server room" Zambia
site:lusakatimes.com OR site:diggers.news OR site:datacenterdynamics.com Zambia ("data centre" OR "data center")
"Lusaka IXP" OR site:peeringdb.com Zambia OR Lusaka
```

## 官方/监管管线要点（详见 explorer-official.md）

- **ZICTA**：牌照/网关/咨询/执法——A 级运营商存在与授权，非面积/MW/racks 证明；Paratus 数据网关牌照（2023 媒体 B，打开牌照记录才 A）。
- **ZEMA**：DC 可能以 ICT 建筑、商业建筑、变电站、备用发电厂、燃料储存、e-waste 或 SEZ 租户项目出现；EIA/EPB/EIS 与征求意见页 A 级。
- **电力**：ERB 许可、ZESCO 连接/变电站/PSA、CEC 铜带电力（Ndola/Kitwe/Chambishi）、NWEC North-Western。
- **ZDA/SEZ/MFEZ**：Lusaka East/South、Chambishi/ZCCZ、Jiangxi（Chibombo/Central）、Kalumbila（North-Western）；租户声明单独分级。
- **DPC**：Data Protection Act No. 3 of 2021 + 2024 条例——本地化/境外存储授权是需求信号，非设施证明。
- **Smart Zambia/INFRATEL/ZNDC**：政府云与三个 DC（A 级服务/运营商声明）；议会记录（A/B+）政府授权与阶段史；华为 AI DC MoU（A 级 MoU/intent）。
- **市议会**：Lusaka City Council City Planning 等；eRegistry/BRRA 列建筑平面与 MFEZ 程序；许多议会可检索许可数据少。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **INFRATEL/ZNDC**：三个国家 Tier III DC；官方页 A 级（服务/存在），地址/容量需字段级来源；DR 站点可能含 Roma/Lusaka 与 Kitwe 引用（议会记录）。
- **Paratus Zambia**：Lusaka Tier III-by-design、colo/云/DR；组页 ISO 9001/ISO 27001/PCI DSS 认证措辞（A）；1 MW 为 DCD 2021-04 报道（B）——运营商/官方页给同数才 A。
- **Liquid Zambia / Liquid C2**：Azure Stack 启动（A）+ 2023 MoU 新 DC（A 级意图）——站点/许可/电力/委托证据出现前不计运营。
- **Smart Zambia / 华为 AI DC**：2026-05 MoU（A 级 MoU/intent）；站点未公开。
- **Lusaka IXP**（lusakaixp.co.zm, PeeringDB ix/615）：中性互联信号（A/B 网络存在，非 DC 证明）。
- **本地媒体**：Lusaka Times、News Diggers、Zambia Daily Mail、Times of Zambia、ZANIS、Techtrends；国际：DCD、ITWeb Africa、Developing Telecoms、Connecting Africa、Capacity。
- **矿业/金融**：Copperbelt/North-Western 矿企 OT/IT 房与 DR（CEC/NWEC/ZEMA 记录强于新闻）；银行 DR/机房 C 级。

## 已知设施/项目与证据状态

| 设施/项目 | 省/地点 | 状态与证据 |
|---|---|---|
| INFRATEL / Zambia National Data Centre | Lusaka（DR 可能含 Kitwe） | 运营政府云/colo（A 级官方页：3 个国家级 Tier III DC）；地址/容量待字段级来源。 |
| Paratus Zambia DC | Lusaka | 运营商业 colo（A 级设施/服务/认证措辞）；1 MW 为 B 级媒体值。 |
| Liquid Zambia（Azure Stack） | Lusaka | 本地云运营（A）+ 新 DC MoU（2023，意图）；新设施不计运营。 |
| Smart Zambia / 华为国家 AI 数据中心 | 站点未公开 | MoU/intent（2026-05，A 级 MoU）；无站点/许可/电力证据不计设施。 |
| Zamtel / MTN Zambia / Airtel Zambia 核心 | Lusaka 及全国 | 运营商/服务 A；设施细节 C；无开放 colo 证据不建记录。 |
| Lusaka IXP | Lusaka | 互联信号（A/B），非 DC。 |
| Raxio / ADC / Teraco / Equinix / Vantage 等 | — | 无 ZM 设施（C），watch Lusaka only。 |

## 更新节奏

- 每批次：重跑 INFRATEL/Paratus/Liquid/Smart Zambia 官方页、ZICTA/ZEMA/ERB/ZDA/DPC/议会面、DCD/ITWeb/Developing Telecoms 与 10 省扫描；盯 Liquid 新 DC 站点落地与华为 AI DC 后续。
- 每季度：重核 hyperscaler + Huawei Cloud 官方区域表；复查 Lusaka IXP 成员与议会记录中 INFRATEL DR 站点。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（10 省粒度）；本 skill 作为国家层参考注入。
