# SL Explorer Industry — 塞拉利昂数据中心发现（行业/媒体/厂商）

日期 (Date reviewed): 2026-08-12。范围 (Scope): 塞拉利昂 (Sierra Leone, SL) 数据中心发现 — 运营商页面、行业媒体、本地媒体、海缆/IXP 记录、云/边缘来源、目录聚合器与分省/区查询模式。

区划覆盖 (Division coverage): **5 个一级区划**，与 manifest 一致：Eastern 东部省、Northern 北部省、North Western 西北省、Southern 南部省、Western Area 西区。

## 1. 可靠性分级 (Reliability Grades)

- **A** — 官方/运营商一级证明：Orange Sierra Leone、Zoodlabs/SALCAB、MoCTI/MoICE/State House、NatCA/NATCOM、NPPA/e-GP、EDSA/EGTC/EPA、ACE 官方、云厂商官方页、Uptime、银行/机构官网设施页。
- **B** — 强行业或机构线索：DCD、Capacity、CommsUpdate/TeleGeography、SubTel Forum、Developing Telecoms、Balancing Act Africa、TechCabal、Techpoint Africa、WeAreTech Africa、TechAfrica News、ITWeb Africa、World Bank/AfDB/UNDP、PCH/PeeringDB，或点名站点/阶段的可信本地媒体。
- **C** — 仅发现线索：数据中心目录、市场报告摘要、社交媒体、招标聚合器、博客转载、无原始来源支撑的本地文章、Krio 社媒命中。
- **U** — 拒绝或搁置：无物理站点、无塞拉利昂上下文、通用厂商可用性，或地名假阳性（Waterloo/Bo/Kabala/Kambia 等）。

## 2. 行业框架 (Industry Frame)

- 市场不是纯 Freetown-only：**Western Area** 集中 ACE/Zoodlabs/SALCAB、IXP 和 Orange Freetown 主站；**Southern / Bo** 已有 Orange Sierra Leone Bo Data Centre，官方描述为 Freetown 主站的灾备/复制站。
- Zoodlabs/SALCAB 是最强互联种子：ACE 官方列 Freetown landing station；MoCTI National Broadband Strategy 称 Cable Landing Station 由 Zoodlabs 管理，Leonecom 管理国家骨干。
- Michcom-IX/SLIX/SLIXP 是 IXP/meet-me 生态，不是数据中心本体。PeeringDB 和 Michcom-IX 页面列出 Freetown 的 Zoodlabs CLS MMR 与 Jui 的 Leonecom MMR。
- Orange Sierra Leone 是最强电信数据中心种子：官网显示 Freetown 数据中心自 2018 年；政府 2025-12 公告确认 Bo 数据中心已启用。
- 截至本次审核，官方云厂商区域页无 SL 区域/本地区域；Uptime 认证列表未发现 SL。把 CDN/cache/IXP 节点按 edge/interconnection 处理。
- 英语为主；Krio 仅作为补充发现词。关键变体：`Salone`、`Fritawn`、`data senta`、`kompyuta senta`、`seva`、`netwok`、`intanet`。

## 3. 高信号行业来源 (High-Signal Industry Sources)

| 来源 (Source) | URL / 入口 | 用途 (Use) | 分级 |
|---|---|---|---|
| Orange Sierra Leone | https://www.orange.sl/ | Freetown/Bo 数据中心、网络升级、B2B 服务；一级运营商来源。 | A |
| MoICE Orange Bo 公告 | https://moice.gov.sl/h-e-president-dr-julius-maada-bio-commissions-e23m-orange-sierra-leone-data-centre-in-bo-to-strengthen-national-digital-systems/ | Bo Data Centre 官方启用、金额、DR 角色。 | A |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | Orange Bo/Freetown 容量与行业背景；回验官方。 | B |
| ACE 官方海缆站 | https://ace-submarinecable.com/en/submarine-cable/ | ACE 系统、Freetown landing station。 | A |
| Zoodlabs | https://zoodlabs.com/ | CLS/metro fiber/ISP 运营商线索；页面内容需逐条核实。 | A/C |
| CrossBoundary Energy — Zoodlabs Data Centre | https://crossboundaryenergy.com/project/zoodlabs/ | Zoodlabs Freetown data centre/CLS 电力系统、0.8 MWp solar、0.7 MW thermal、1.95 MWh storage、Q2 2023。 | B/A for supplier claim |
| MoCTI National Broadband Strategy | https://mocti.gov.sl/wp-content/uploads/2024/12/National-Broadband-Strategy.pdf | Zoodlabs CLS 管理、Leonecom backbone、SLIX/IXP 目标。 | A |
| Michcom-IX | https://www.michcom-ix.net/ | Sierra Leone/Guinea/Liberia IXP、Freetown and Jui PoPs、members。 | A for operator claim |
| PeeringDB Michcom-IX | https://www.peeringdb.com/ix/4892 | Michcom-IX city/country, facilities, peers, prefixes。 | B/C |
| PCH IXP directory | https://www.pch.net/ixp/dir | IXP cross-check；页面可能不 expose all rows to crawler, search internally. | B |
| CommsUpdate / TeleGeography | https://www.commsupdate.com/ | SL telecom, ACE, operator news。 | B |
| SubTel Forum | https://subtelforum.com/ | 海缆和 landing station 线索。 | B |
| Developing Telecoms | https://developingtelecoms.com/ | 电信/海缆/监管新闻。 | B |
| Capacity Media | https://www.capacitymedia.com/ | 容量、海缆、运营商投资。 | B |
| TechAfrica News | https://techafricanews.com/ | Orange/政府数字公告与海缆线索。 | B |
| Datacentres Africa | https://datacentresafrica.com/ | 区域 DC 新闻；回验官方。 | B/C |
| Awoko | https://www.awoko.org/ | 本地项目、运营商、政府 ICT 线索。 | B/C |
| Politico SL | https://politicosl.com/ | SALCAB/Zoodlabs、政府 ICT 线索。 | B/C |
| Sierra Leone Telegraph | https://www.thesierraleonetelegraph.com/ | SALCAB/政策/政府项目线索。 | B/C |
| Sierraloaded | https://sierraloaded.sl/ | 本地新闻与社媒型线索；需回验。 | C/B |
| U.S. Trade Guide | https://www.trade.gov/country-commercial-guides/ | 采购与 ICT 市场背景。 | B |
| 目录聚合器 | datacenters.com、cloudscene.com、colo.exchange、datacentermap.com、fiberatlantic.com | 仅别名/地址线索；容量和状态必须回验。 | C |

## 4. 行业查询模板 (Industry Query Sets)

### 4.1 通用媒体与行业检索（英语）

```text
Sierra Leone "data centre" OR "data center" Orange OR Zoodlabs OR SALCAB OR Leonecom
Freetown "data centre" OR "data center" OR "meet-me room" OR "landing station"
Bo Sierra Leone "data centre" OR "data center" Orange OR Sonatel OR "disaster recovery"
"Orange Sierra Leone" "data centre" OR "data center" OR Freetown OR Bo
"Zoodlabs" Sierra Leone "data centre" OR "data center" OR "cable landing station" OR CLS
"SALCAB" OR "Sierra Leone Cable" "landing station" OR ACE OR "Cable Landing Station"
"Michcom-IX" OR "SLIX" OR "SLIXP" OR "Sierra Leone Internet Exchange Point"
"Leonecom" Sierra Leone "meet-me room" OR MMR OR backbone OR data
site:datacenterdynamics.com/en/news/ Sierra Leone "data center" OR Orange OR Bo
site:capacitymedia.com Sierra Leone ACE OR Zoodlabs OR Orange OR SLIX
site:commsupdate.com Sierra Leone ACE OR "submarine cable" OR Orange
site:subtelforum.com Sierra Leone ACE OR "landing station" OR SALCAB
site:developingtelecoms.com Sierra Leone ACE OR "data centre" OR "landing station"
site:techafricanews.com Sierra Leone "data center" OR Orange OR "second submarine cable"
site:awoko.org Sierra Leone "data centre" OR ICT OR Zoodlabs OR SALCAB
site:politicosl.com Sierra Leone Zoodlabs OR SALCAB OR ICT OR digital
site:thesierraleonetelegraph.com Sierra Leone SALCAB OR "data centre" OR ICT
```

阶段词处理 (Stage terms):

- 线索：`plans`、`seeks`、`MoU`、`study`、`needs assessment`、`strategy`、`framework`。
- 流水线：`tender`、`RFP`、`NPPA`、`e-GP`、`EIA`、`ESIA`、`groundbreaking`、`construction`、`upgrade`。
- 运营：`commissioned`、`launched`、`opened`、`operational`、`hosting`、`colocation`、`meet-me room`、`NOC`。

### 4.2 Krio / 英语变体模板 (Krio/English Variants)

Krio 命中一律按 C 级线索，必须用英语官方/运营商/主流媒体佐证。

```text
"data senta" Salone OR Fritawn
"kompyuta senta" Salone OR Freetown
"seva" OR "serfa" Salone OR Fritawn data
"Salone" "data centre" OR "data center" OR "server room"
"Fritawn" "data" OR "kompyuta" OR "intanet" OR "netwok"
"na Fritawn" data OR senta OR kompyuta
"na Salone" data OR server OR cloud
```

## 5. 运营商与设施种子 (Operators and Facility Seeds)

| 运营商 / 项目 | 优先位置 | 行业用途 | 分级规则 |
|---|---|---|---|
| Orange Sierra Leone Freetown DC | Western Area / Freetown | 主电信数据中心；Bo 的 primary counterpart。 | A 来自 Orange/MoICE；容量需一级来源，DCD 容量按 B 待回验。 |
| Orange Sierra Leone Bo DC | Southern / Bo City | 灾备/复制数据中心；2025-11-29 启用。 | A 来自 MoICE/State House/Orange；DCD/Datacentres Africa 为 B。 |
| Zoodlabs/SALCAB ACE CLS | Western Area / Freetown | ACE landing station、CLS、metro fiber、电力系统。 | A/B：ACE/MoCTI/World Bank/CrossBoundary；colo 需运营商证据。 |
| Michcom-IX / SLIX / SLIXP | Western Area / Freetown; Jui | IXP、meet-me、edge discovery。 | A for operator page；B/C PeeringDB；不按 DC 本体计数。 |
| Leonecom MMR Jui | Western Area / Jui | IXP PoP / meet-me room; backbone operator seed。 | B/C until Leonecom or official facility proof. |
| Sierratel | Freetown + 全国 | 固网/前垄断运营商，交换机房和老网络设施线索。 | 仅官方/运营商/EPA/采购点名时升 A。 |
| Africell | Freetown + 全国 | 移动运营商数据/交换机房线索。 | 同上。 |
| QCell / Lintel | Freetown + 主要城镇 | 移动/数据运营商线索。 | 同上。 |
| Ministry of Finance e-GP facility | Western Area / Freetown | 政府采购平台托管/机房线索。 | 官方平台 A；物理 data center 需 MoF/NPPA 原文。 |
| BSL / commercial banks | Western Area / Freetown + branches | 金融 DR、支付、核心银行系统。 | 银行/BSL 年报点名才计数。 |
| NCRA / Stats SL / NRA / universities | Freetown, Njala, Bo, Kenema | 机构服务器房、校园 ICT、数据系统。 | 通常 C；点名服务器房或 DC 才计数。 |

```text
"Orange Sierra Leone" "Freetown" "Data Center" OR "Data Centre"
"Orange Sierra Leone" "Bo" "Data Center" OR "Data Centre" OR "disaster recovery"
"Sonatel" "Orange Sierra Leone" "data centre" OR "data center"
"Zoodlabs Data Centre" Freetown Sierra Leone
"Zoodlabs" "cable landing station" Sierra Leone OR Freetown
"Sierra Leone Cable" OR SALCAB "co-location" OR colocation OR hosting OR "NOC"
"Michcom-IX" "Zoodlabs CLS MMR" OR "Leonecom MMR Jui"
"SLIX" "Freetown" "Internet Exchange"
"Bank of Sierra Leone" "data centre" OR "data center" OR "disaster recovery"
"Sierra Leone" "Uptime Institute" "Tier III" OR "Tier IV"
```

## 6. 云、边缘与 CDN (Cloud, Edge, and CDN)

官方缺席检查：

- AWS 区域/AZ: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- AWS Local Zones: https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html
- Azure 区域: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud 位置: https://cloud.google.com/about/locations
- Oracle 公有云区域: https://www.oracle.com/cloud/public-cloud-regions/
- Uptime 认证列表: https://uptimeinstitute.com/uptime-institute-awards/list

截至本次审核，上述官方页面未发现 SL 区域、本地区域或 Uptime Tier 认证。若发现 Google/Microsoft/AWS/Meta cache、CDN 或 on-net service，按**edge/cache/IXP participant**处理，不按云区域计数。

## 7. 目录与聚合器 (Directories and Aggregators)

仅作线索，且不得直接采信容量、Tier、状态：

```text
site:datacenters.com Sierra Leone Freetown OR Bo OR Orange OR Zoodlabs
site:cloudscene.com Sierra Leone OR Freetown OR Bo
site:colo.exchange Sierra Leone OR Freetown OR Zoodlabs
site:datacentermap.com Sierra Leone OR Freetown OR Bo
site:fiberatlantic.com Sierra Leone Freetown "cable landing station"
site:peeringdb.com Sierra Leone OR "Michcom-IX" OR "Zoodlabs CLS MMR"
```

目录线索必须回验到 Orange、Zoodlabs/SALCAB、MoCTI/MoICE、ACE、World Bank、PeeringDB/PCH 或其他一级/强二级来源。

## 8. 枚举矩阵 (Division-Level Enumeration Matrix)

对每个一级区划：

```text
"{division}" Sierra Leone ("data centre" OR "data center" OR datacentre) ("MW" OR racks OR "IT load" OR server)
"{division capital}" Sierra Leone ("data centre" OR "data center") (opened OR launched OR commissioned OR construction OR upgrade)
"{division}" Sierra Leone colocation OR "co-location" OR "carrier neutral" OR "Tier III" OR "Tier IV"
"{division}" Sierra Leone "cloud" OR "e-government" OR "ICT hub" OR broadband
"{division}" Sierra Leone "captive power" OR generator OR substation
"{operator}" "{division OR town}" Sierra Leone
"{division}" Salone data OR senta OR kompyuta
site:awoko.org "{division}" "data" OR ICT
site:politicosl.com "{division}" ICT OR digital
site:thesierraleonetelegraph.com "{division}" ICT OR digital
```

| 一级区划 | 首府 / 主要城镇 | 行业种子与处理 |
|---|---|---|
| Eastern 东部省 | Kenema；Kailahun、Koidu/Sefadu | Orange Bo 公告提到向 Kono/Kenema corridor 提升服务，但不证明 Eastern 站点。查矿区、Kenema ICT、运营商站点；预期商业 DC 阴性。 |
| Northern 北部省 | Makeni；Magburaka、Kabala、Bendugu | Orange Bo 公告提到 Makeni 服务韧性；不证明 Northern 站点。查 Makeni、Tonkolili、Kabala 的网络/矿区自用机房。 |
| North Western 西北省 | Port Loko；Lungi、Kambia、Kamakwie | 查 Lungi 机场通信、Port Loko/边境连接。Jui 属 Western Area Rural，不归 North Western。预期商业 DC 阴性。 |
| Southern 南部省 | Bo；Bonthe/Mattru Jong、Moyamba、Pujehun、Njala | **已证实 Orange Bo Data Centre**。另查 Bo/Kenema 光纤、Njala、矿区/港口自用机房。注意 Bo 假阳性。 |
| Western Area 西区 | Freetown；Jui；Waterloo | 最高召回：Orange Freetown DC、Zoodlabs/SALCAB ACE CLS、Michcom-IX/SLIX、Leonecom MMR Jui、MoF/e-GP、BSL/银行/机构机房。过滤 Waterloo 假阳性。 |

## 9. 分级与去重规则 (Grading and Deduping Rules)

- **Orange Bo**：MoICE/State House/Orange 官方启用信息为 A；DCD 和 Datacentres Africa 为 B；社媒为 C。状态可记 `operating / commissioned 2025-11-29`；容量 unknown，除非官方给出。
- **Orange Freetown**：Orange 官网和 MoICE 对“main Freetown centre”的描述为 A；DCD 的面积/机架容量为 B，需 Orange/施工/监管原文才能入 capacity 字段。
- **Zoodlabs/SALCAB CLS**：ACE/MoCTI/World Bank 可证明 landing station 和管理关系；CrossBoundary 可证明电力系统和“Zoodlabs Data Centre”供应商视角。公共 colo/托管服务仍需 Zoodlabs/SALCAB 一手页面或合同。
- **IXP/meet-me**：Michcom-IX、SLIX、Zoodlabs CLS MMR、Leonecom MMR Jui 是互联/PoP 记录，不自动变成数据中心。若被设施清单收录，类型必须标为 `IXP / meet-me room / edge`.
- **政府/金融/机构**：e-GP、BSL、NCRA、Stats SL、NRA、大学系统默认是 institutional leads；只有点名 data center/server room/DR site 且有位置时计数。
- **容量诚实**：MW、机架、面积、Tier、Uptime、PUE、市电接入、自备电源只采信一级来源；供应商案例可作为电力系统证据，但不要等同于 IT load。
- **地名过滤**：`Bo` 必须绑定 Sierra Leone/Orange/Bo City/Bo District；`Waterloo` 必须绑定 Western Area Rural；`Jui` 属 Western Area；`Kambia`、`Kabala` 必须绑定 Sierra Leone。

## 10. 最终校验规则 (Final Validation Rules)

- 每个候选必须有省/区 + 城镇：`Western Area / Freetown`、`Western Area / Jui`、`Southern / Bo City` 等。
- 必须区分设施类型：商业/电信数据中心、灾备、海缆登陆站、IXP、MMR、机构服务器房、云区域。
- 未经一级来源确认，不写 SL 云区域、Tier III/IV、Uptime、MW、机架或商业托管能力。
- 计划性语言不得升格：`second submarine cable`、`second IXP`、`government cloud`、`national data centre` 在官方落成/采购/建设证据出现前都是 pipeline/lead。
- 去重时优先按物理承载设施记录，再把 IXP/CDN/缓存作为关联服务：例如 `Zoodlabs CLS MMR` 可关联到 `Zoodlabs/SALCAB ACE CLS`，但不是独立 DC。
