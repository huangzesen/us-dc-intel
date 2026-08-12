# SL Explorer Official — 塞拉利昂数据中心枚举方法（官方来源）

日期 (Date reviewed): 2026-08-12。国家 (Country): **塞拉利昂 Sierra Leone (SL)**。区划模型 (Division model, per manifest): **province/area** — 5 个一级区划：**Eastern 东部省、Northern 北部省、North Western 西北省、Southern 南部省、Western Area 西区**。

范围 (Scope): 官方政府、监管、电力、环境、采购、海缆/IXP、运营商一级来源与官方云/Uptime 缺席检查，用于发现塞拉利昂商业托管 (colocation)、电信数据中心、海缆登陆站、IXP、政府平台机房、金融灾备和机构服务器房。

## 1. 可靠性分级 (Reliability Grades)

- **A** — 一级/官方来源直接证明具体主张：gov.sl / State House / MoCTI / MoICE；NatCA/NATCOM 牌照与监管记录；EDSA/EGTC/能源部；EPA-SL 许可/EIA/ESIA；NPPA/e-GP；ACE 官方；运营商官网或政府公告确认的 Orange / Zoodlabs / SALCAB 设施；官方云区域页；Uptime Institute 认证页；银行/机构官网设施页。
- **B** — 强二级来源：World Bank/AfDB/UNDP/EU 项目文件；DCD、Capacity、CommsUpdate/TeleGeography、SubTel Forum、Developing Telecoms；PCH/PeeringDB 用于 IXP 位置；信誉良好的塞拉利昂媒体且点名站点、阶段或业主。
- **C** — 仅发现线索：目录/聚合器、社交媒体、市场报告摘要、无原始链接的招标转载、无站点/状态的 MoU、仅说明 ICT 系统/服务器而未证明物理数据中心的记录。
- **U** — 暂不可用/拒绝：无塞拉利昂上下文、无物理站点、通用云营销、地名假阳性，或只出现 `Waterloo`、`Bo`、`Kabala`、`Kambia` 等多义地名而未绑定 Sierra Leone/SL。

## 2. 已核实基线 (Verified Baseline)

- 塞拉利昂**没有公开国家数据中心登记册**。枚举必须拼接监管牌照、政府数字化文件、采购、电力/环境许可、海缆和 IXP 证据、运营商公告及可靠媒体。
- **Western Area / Freetown** 仍是最高召回区域：ACE 登陆站、Zoodlabs/SALCAB 生态、Michcom-IX/SLIX、Orange Freetown 主数据中心、政府/金融机构机房线索集中在此。
- **Southern / Bo** 已有官方确认的 Orange Sierra Leone 数据中心。MoICE 2025-12-01 公告称总统正式启用 Bo City 的 €23m Orange Sierra Leone Data Centre，并说明它是国家灾备枢纽、配合 Freetown 主中心运行。
- MoCTI 的 National Broadband Strategy 2023-2028 确认：Cable Landing Station 由 **Zoodlabs SL Limited** 管理，国家光纤骨干由 **Leonecom** 承包；该文件还把 SLIX/SLIXP 作为 Freetown 2010 年启动的互联网交换点，并提出省级第二 IXP 目标。
- 官方云厂商区域列表与 Uptime 认证列表未发现 Sierra Leone 区域或 SL Tier 认证记录；任何云区域/Tier/MW/机架主张都必须回验一级来源。

## 3. 已验证官方来源 (Verified Official Sources)

| 来源 (Source) | URL | 用途 (Use) | 分级 |
|---|---|---|---|
| Government information portal | https://info.gov.sl/ | 政府信息、新闻与公共通告入口；具体证据优先回到部委域名。 | A |
| State House | https://statehouse.gov.sl/ | 总统出席的落成/启动/政策公告。 | A |
| Ministry of Information and Civic Education (MoICE) | https://moice.gov.sl/ | 政府新闻；已确认 Orange Bo Data Centre 公告。 | A |
| MoCTI | https://mocti.gov.sl/ | 通信、技术与创新部；政策、新闻、National Broadband Strategy。 | A |
| DSTI | https://www.dsti.gov.sl/ | 科技创新局；NIDS/数字项目线索。 | A/C 按内容 |
| NatCA/NATCOM registry | https://natcom.gov.sl/registered-operator/ | 持牌电信运营商名录；只证明资质，不自动证明机房。 | A |
| NPPA | https://nppa.gov.sl/ | 公共采购门户。 | A |
| e-GP | https://egp.nppa.gov.sl/ | 电子采购通知、计划、合同、数据。 | A |
| Ministry of Finance e-GP launch | https://mof.gov.sl/the-electronic-government-procurement-e-gp-will-increase-transparency-and-accountability-in-public-procurement-systems-deputy-minister-of-finance-i/ | e-GP 政府系统背景；寻找财政部托管/数据中心线索。 | A/C |
| EDSA | https://www.edsa.sl/ | 配电与供电证据；网站可用但内容有限。 | A |
| Ministry of Energy — EGTC | https://moe.gov.sl/egtc/ | 发输电公司入口；EGTC 独立域名未确认。 | A |
| EPA-SL | https://epa.gov.sl/ | 环境许可、EIA/ESIA、油储/发电机/建设项目线索。 | A |
| ACE official | https://ace-submarinecable.com/en/submarine-cable/ | ACE 系统、Freetown 登陆站、2012 投运背景。 | A |
| World Bank ACE ESMF | https://documents1.worldbank.org/curated/en/695051468193477570/pdf/E25810EA0P1162101public10BOX353785B.pdf | SALCAB/ACE 登陆站候选地点、Freetown/Lumley/Juba 证据。 | B/A for project docs |
| MoCTI National Broadband Strategy | https://mocti.gov.sl/wp-content/uploads/2024/12/National-Broadband-Strategy.pdf | Zoodlabs CLS 管理、Leonecom backbone、SLIX/IXP 目标、运营商生态。 | A |

## 4. 核心官方查询模板 (Official Query Templates)

所有查询同时跑 `data centre` 与 `data center`，并补充 `datacentre`、`server room`、`colocation`、`co-location`、`hosting`、`landing station`、`meet-me room`、`IXP`、`SLIX`、`SLIXP`、`disaster recovery`、`government cloud`、`generator`、`substation`、`MW`、`MVA`、`Tier III`、`Uptime`。

```text
site:gov.sl Sierra Leone "data centre" OR "data center" OR "National Data"
site:statehouse.gov.sl Sierra Leone "data centre" OR "data center" OR Orange OR Bo
site:moice.gov.sl "data centre" OR "data center" OR Orange OR Bo
site:mocti.gov.sl "data centre" OR "data center" OR "Broadband Strategy" OR SLIX OR Zoodlabs
site:dsti.gov.sl "National Data" OR "data centre" OR "data center" OR cloud
site:natcom.gov.sl "Registry of Operators" OR "licensed telecommunications operators" OR "data centre" OR SLIX
site:nppa.gov.sl "data centre" OR "data center" OR server OR cloud OR "disaster recovery"
site:egp.nppa.gov.sl "data centre" OR "data center" OR server OR cloud OR "disaster recovery"
site:mof.gov.sl "e-GP" "data center" OR "data centre" OR server
site:epa.gov.sl "data centre" OR "data center" OR telecommunications OR generator OR EIA OR ESIA
site:edsa.sl "data centre" OR "data center" OR substation OR "large customer"
site:moe.gov.sl EGTC OR EDSA OR substation OR "data centre"
```

## 5. 设施/项目种子表 (Official Facility / Project Seeds)

| 种子 (Seed) | 省/区 / 市 | 分级 | 已核实内容 | 枚举规则 |
|---|---:|---:|---|---|
| Orange Sierra Leone Freetown Data Centre | Western Area / Freetown | A | Orange 官网称 Freetown 新数据中心已启动且“Since 2018”；MoICE Bo 公告称 Bo 站与 Freetown 主中心配合运行。 | 计为 Orange 自用/电信数据中心；第三方托管、容量、Tier 仅在 Orange/官方来源明确时填写。 |
| Orange Sierra Leone Bo Data Centre | Southern / Bo City | A | MoICE 2025-12-01 确认总统启用 €23m Bo 数据中心；称为国家灾备枢纽、配合 Freetown 主中心运行。 | 计为 Orange 电信/DR 数据中心；状态 operating/commissioned；容量 unknown，除非一级来源给出。 |
| Zoodlabs / SALCAB Cable Landing Station | Western Area / Freetown | A/B | ACE 官方列 Freetown 为登陆站；World Bank ESMF 证明 SALCAB ACE landing station project 与 Freetown 候选地点；MoCTI NBS 称 CLS 由 Zoodlabs 管理。 | 计为海缆登陆站/互联设施；是否公开 colo 需运营商页面或合同证实。避免与 IXP 重复计数。 |
| Michcom-IX / SLIX / SLIXP | Western Area / Freetown；Western Area / Jui | A/B | MoCTI NBS 确认 SLIX 在 Freetown 2010 年启动；Michcom-IX/PeeringDB 显示 Freetown Zoodlabs CLS MMR 与 Jui Leonecom MMR。 | 计为 IXP/meet-me/边缘互联，不单独计为数据中心；可关联到承载设施。 |
| Ministry of Finance e-GP data center 线索 | Western Area / Freetown | C/B | MoF/e-GP 官方确认 e-GP 平台和采购系统；社媒/本地报道提到财政部 e-GP data center，但需官方页面或采购记录点名。 | 除非官方采购/财政部公告点名物理机房，否则仅作机构线索。 |
| 政府 National Data Centre / Government Cloud 线索 | Western Area / Freetown unless specified | C | 数字战略、DPI、AI/Data Strategy 文件可产生线索；尚未发现可计数的已运营国家数据中心一级证据。 | 在落成、采购、EIA 或运营证据出现前不计为已证实设施。 |
| NatCA/NATCOM 持牌运营商机房 | 各省区；主要在 Freetown | A for licence / C for facility | 牌照名录确认运营商资质；不证明数据中心。 | 逐家回查 Orange、Africell、QCell/Lintel、Sierratel、Zoodlabs、Leonecom、ISPs；只有点名数据中心/机房/托管才计数。 |
| BSL / 银行 / NCRA / Stats SL 等机构机房 | 主要 Western Area | C unless named | 机构数字系统存在；公开设施证据有限。 | 自用服务器房可按 institutional 记录，但必须点名物理设施与位置。 |
| 云区域 / Uptime Tier | 无 | A（缺席） | 官方云和 Uptime 列表未发现 SL 区域或认证。 | 不创建云区域或 Tier 记录；CDN/缓存按 edge/cache 处理。 |

## 6. 海缆、IXP 与去重规则 (Subsea / IXP Deduping)

- **ACE / Freetown**：ACE 官方证明 Freetown landing station；World Bank ESMF 证明项目位置在 Freetown/Lumley-Juba 范围；MoCTI NBS 证明 Zoodlabs 管理 CLS。优先名称使用 `Zoodlabs/SALCAB ACE Cable Landing Station`，业主/运营关系按来源日期记录。
- **Michcom-IX / SLIX / SLIXP**：SLIX 是互联网交换，不是数据中心。PeeringDB 显示 Michcom-IX 本身位于 Freetown，并列出 Zoodlabs CLS MMR 与 Leonecom MMR Jui。Jui 属 Western Area Rural，不是 North Western。
- **Leonecom MMR Jui**：按 meet-me/IXP PoP 处理；只有 Leonecom 或官方资料点名数据中心/机房时才升级为设施记录。
- **Orange Freetown vs Orange Bo**：两个站点可分别计数，因为官方资料将 Bo 描述为 Freetown 主站的灾备/复制站。容量字段保持 unknown，除非 Orange 一手资料给出。

## 7. 分省/区官方策略 (Per-Division Official Strategy)

对每个一级区划运行：

```text
"{division}" Sierra Leone "data centre" OR "data center" OR datacentre
"{division capital}" Sierra Leone "data centre" OR "data center" OR "server room"
"{town}" Sierra Leone colocation OR "co-location" OR "meet-me room" OR IXP
"{division}" Sierra Leone "cloud" OR "e-government" OR "ICT hub" OR broadband
"{division}" Sierra Leone "captive power" OR generator OR substation
site:mocti.gov.sl "{division}" OR "{town}" ICT OR broadband OR data
site:natcom.gov.sl "{operator}" "{division}" OR "{town}"
site:nppa.gov.sl "{division}" ICT OR server OR data
site:egp.nppa.gov.sl "{division}" ICT OR server OR data
site:epa.gov.sl "{division}" telecommunications OR ICT OR generator
```

| 一级区划 | 首府 / 主要城镇 | 官方优先策略与预期结果 |
|---|---|---|
| Eastern 东部省 | Kenema；Kailahun、Koidu/Sefadu | 查 Kenema/Kono/Kailahun 的运营商网络、矿区通信、e-GP ICT、EPA 许可。预期商业 DC 阴性；Orange Bo 公告称服务会改善至 Kono/Kenema，但不代表 Eastern 有站点。 |
| Northern 北部省 | Makeni；Magburaka、Kabala、Bendugu | 查 Makeni、Tonkolili、Kabala 的宽带、运营商、矿区/能源 ICT。预期阴性；Orange Bo 公告提到 Makeni 受益，但不代表 Northern 有数据中心。 |
| North Western 西北省 | Port Loko；Lungi、Kambia、Kamakwie | 查 Lungi 机场通信、Port Loko、市政 ICT、边境连接。预期阴性；注意不要把 Jui 或 Freetown 误归 North Western。 |
| Southern 南部省 | Bo；Bonthe/Mattru Jong、Moyamba、Pujehun、Njala | **重点查 Orange Bo Data Centre**、Bo/Kenema 光纤、Njala ICT、矿区自用系统。Bo 站为已证实 A 级种子；其他商业 DC 仍需证据。 |
| Western Area 西区 | Freetown；Jui；Waterloo | 最高召回：Zoodlabs/SALCAB ACE CLS、Michcom-IX/SLIX、Orange Freetown 主数据中心、MoF/e-GP 线索、BSL/NCRA/Stats SL、运营商机房、银行 DR。过滤 Waterloo 假阳性。 |

## 8. 发展伙伴跟进 (Development-Partner Follow-Up)

| 来源 | URL | 用法 |
|---|---|---|
| World Bank projects | https://projects.worldbank.org/en/country/sierraleone | 查 SLDTP、SALCIP、采购包、ESMF/ESIA。 |
| World Bank Documents | https://documents.worldbank.org/ | 查 `Sierra Leone Digital Transformation Project`、`ACE Submarine Cable and Landing Station Project`。 |
| AfDB Sierra Leone | https://www.afdb.org/en/countries/west-africa/sierra-leone | 查能源、宽带、数字基础设施项目。 |
| UNDP Sierra Leone | https://www.undp.org/sierra-leone | 查数字政府、数据系统、灾备线索。 |
| U.S. Trade Guide | https://www.trade.gov/country-commercial-guides/ | 查 ICT/telecom 背景、采购规则；二级背景，不证明设施。 |

```text
site:worldbank.org Sierra Leone "data centre" OR "data center" OR "digital transformation"
site:worldbank.org Sierra Leone "National Data" OR cloud OR broadband OR e-GP
site:afdb.org Sierra Leone ICT OR broadband OR "data centre"
site:undp.org Sierra Leone "data centre" OR "data center" OR digital
"Sierra Leone Digital Transformation Project" "data centre" OR "data center" OR cloud OR "server room"
```

不要把发展伙伴项目名直接转为设施记录，除非文件点名物理站点、采购包、建设状态或运营方。

## 9. 最终校验清单 (Final Validation Checklist)

- 每个候选必须有 `country_code=SL`、manifest 一级区划、省/区内城市或镇；最低位置不得低于 `Western Area / Freetown` 或 `Southern / Bo`。
- 明确设施类型：海缆登陆站、数据中心、灾备中心、IXP/meet-me room、电信交换机房、政府平台机房、机构服务器房、云区域。
- 阶段诚实：`plans`/`strategy`/`MoU`/`study` = 线索；`tender`/`EIA`/`construction` = pipeline；`commissioned`/`opened`/`operational` = operating。
- 牌照不是设施。NATCOM/NatCA 只能证明运营资格，不能单独证明物理数据中心。
- 容量、Tier、机架、MW/MVA、市电、自备电源只采信一级来源；目录和媒体数字必须回原始来源。
- 严格去重：Zoodlabs/SALCAB CLS、Michcom-IX、Orange Freetown、Orange Bo、MoF/e-GP、机构机房仅在证据支持独立物理/运营身份时分别计数。
- 地名假阳性过滤：`Waterloo`、`Bo`、`Kabala`、`Kambia`、`Leone`、`Sierra` 必须绑定 Sierra Leone、`.sl`、Freetown/Bo/Kenema/Makeni、NatCA、MoCTI、Orange SL、Zoodlabs、SALCAB、Leonecom、EDSA、EPA 或其他本国机构。
