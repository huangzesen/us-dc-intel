---
name: tk-datacenter-methodology
location: scripts/expansion/world/country-skills/TK/SKILL.md
description: 托克劳数据中心查询方法论（Tokelau datacenter discovery & audit methodology）——双线来源（官方/监管/云管线 + 行业/厂商发现）与 single-division 模型下的 verified-negative 枚举协议。
---

# TK · 托克劳数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：证明托克劳（Tokelau, TK）是否存在任何数据中心、云区域、托管设施、政府服务器房、电信交换局、海缆登陆站或类似数据中心的信息通信设施。双线方法论：`explorer-official.md`（官方/监管/云管线）与 `explorer-industry.md`（行业/厂商发现），均为 codex 审核定稿。划分模型（per manifest）：**`["Tokelau"]`** — 单一 division；环礁名（Atafu、Nukunonu、Fakaofo）只作 `sub_location` 值，不得发明省级/区级/NZ 式细分。最后核验（final source-verification pass）：2026-08-12。

## 入口

| 入口 | 管线 | 内容 |
|---|---|---|
| `explorer-official.md` | 官方/监管/云管线 | 官方地面真值（政治/行政地位、治理地理、人口/需求基、能源约束、连接性修正、无商业 DC 市场基线）、官方来源登记表、官方负项证据（云区域/政府域检查）、按 division 枚举策略、候选字段 schema、常见误报、变化检测触发器、复核清单 |
| `explorer-industry.md` | 行业/厂商发现 | 行业现实（verified-negative 基线、连接性改善、极小运营商集、微尺度需求与电力）、运营商与基础设施来源、互联 pivots（Southern Cross NEXT/旧卫星与本地接入）、云/托管/IXP 负检查、`.tk` 域名噪声、能源与可建性、按环礁行业枚举、候选字段、误报与升级、复核清单 |

## 核心结构事实

1. **行政区划模型**：manifest 单一 division `Tokelau`；环礁 Atafu/Nukunonu/Fakaofo 只作 sub_location（Unknown TK 作默认桶）。托克劳是新西兰王国范围内的非自治领地：NZ MFAT 说明其有自己的政治机构、司法系统和公共服务，新西兰保留国际义务、防务/安全和 EEZ 管理责任。行政地理由三个环礁组成，Ulu o Tokelau 角色在三位 Faipule 间逐年轮换，General Fono 含各环礁民选代表。托克劳政府网站列出国家部门包括 Energy and Telecommunications、Office of the Administrator、Office of the Council、Transport & Support Services、Health、Education（tokelau.org.nz）。
2. **注册库现状**：无商业 DC 市场基线——截至本次核验，无任何官方（Tokelau Government、NZ MFAT、Teletok/IANA）或 hyperscaler 来源识别托克劳商业数据中心、托管设施、云区域、IXP、AI/HPC 站点或 carrier-neutral 设施。商业 DC/colo/cloud 预期计数为零；只有一级来源点名官方服务器房、电信或海缆/登陆设施才计数。
3. **法律与监管**：NZ 法律基础为 Tokelau Act 1948（legislation.govt.nz，仅用于宪政/监管背景）；IANA `.tk` root 记录确认 ccTLD 管理者为 Telecommunication Tokelau Corporation（Teletok），Fakaofo，技术联系在荷兰——不是本地 DC 证明。政治/行政与公共服务引用走 NZ MFAT 与 Tokelau Government。
4. **互联与云**：**连接性修正——托克劳不再是纯卫星**。旧 Tokelau 政府材料称每个环礁有自己的卫星链路、由政府拥有的 Teletok 管理；但 Southern Cross NEXT 现在为托克劳和基里巴斯提供第一条国际海底光纤连接（来源：Ciena/Southern Cross launch release 与 Southern Cross 官网）。Southern Cross NEXT 是**海缆/连通性 lead**，本身不是数据中心 lead。官方云区域检查（AWS/Azure/GCP/OCI 官方列表）均无 TK 区域；最近的官方区域条目在新西兰/澳大利亚/亚太。云供应商销售页、CDN 国家可用性、Starlink 可用性、域名注册、泛泛的 “serve customers in Tokelau” 页面都是服务可用性，不是设施。BGP/ASN 工具（bgp.tools/APNIC/RIPE/PeeringDB 搜 Teletok、AS57382、AS198147、AS55523）只显示网络足迹，不是设施证明。
5. **设施/项目种子**（预期起始记录）：**Southern Cross NEXT / Tokelau connection**——海缆/连通性设施 lead，按 Southern Cross/Ciena 后期引用可能位于 Nukunonu，但只有来源明确支持时才分配环礁；不是数据中心。**Teletok telecom facilities**——电信交换局/旧卫星链路/运营商设施 lead，官方身份由 Tokelau Government 与 IANA 强支持；除非 Teletok 发布 hosting/colo 服务，否则不是商业托管。**Government IT / server rooms**——可能只有小型公共服务机房，仅凭一级证据记录为 lead。**Commercial colocation / cloud region / AI-HPC**——verified-negative 基线。
6. **语言与词汇**：英语为主（官方/运营商/行业来源）；中文辅助检索：`托克劳 (数据中心 OR 云 OR 算力 OR 海底光缆 OR 卫星互联网)`。
7. **可靠性分级**：A=官方/一手来源（Tokelau Government、NZ MFAT、法律、IANA、运营商/云厂商官方页、官方项目文件、Teletok、Southern Cross/Ciena）；B=强二级来源或具名项目/厂商/行业来源（行业媒体、海缆系统数据库、网络元数据、具名厂商/项目发布）；C=目录、SEO 页面、社交帖、地图片段、无出处的媒体或弱线索。分类规则：若唯一证据是泛泛云转售商、`.tk` 域名注册页、卫星服务可用页、SEO 市场报告或国家码下拉菜单，标 **C / false positive** 且不计数。
8. **计数与去重规则**：最低计数标准——一级来源点名设施/项目及功能；或运营商/政府页 + 一个独立 A/B 来源确认同一物理站点；且任何环礁级分配有明确的环礁/地址证据。`.tk` 域名注册、Dot TK、Freenom、DNS 域名服务器基础设施与托克劳物理设施分开——IANA 确认 ccTLD 关系，但 `.tk` 运营涉及境外技术联系/域名服务器，不证明本地托管。Southern Cross NEXT 营销提到悉尼/奥克兰/洛杉矶的 “datacentres” 是离岸端点，不是 TK 设施。海缆登陆站、卫星终端、VSAT、Starlink/Kacific/O3b 终端、电信交换局不得计为商业数据中心。太阳能电站、电池、发电机、鱼冷库、制冷负载或其它环礁微电网设备不得计为 IT load。NZ 托管的托克劳政府网站、邮件、云服务或厂商支持不得计为托克劳本地基础设施。候选 schema：country_code TK、division Tokelau、sub_location Atafu|Nukunonu|Fakaofo|Unknown TK、facility_or_project_name、operator_or_owner（Teletok|Tokelau Government/Tokelau Public Service|Southern Cross/Teletok cable node|donor project|other）、consent_or_authorisation、site_address、coordinates、status（operational|planned|lead|verified-negative）、facility_type（cable landing/subsea terminal|satellite earth station|telecom exchange|government server room|colocation|cloud-region|AI/HPC|other）、it_load_mw、power_connection（atoll microgrid (solar + batteries + generators)|dedicated generator|unknown）、connectivity（Southern Cross NEXT submarine fibre|satellite|local access network|unknown）、evidence_grade、primary_urls、secondary_urls、notes、last_checked。

## 常用查询模板

```text
site:tokelau.org.nz ("data centre" OR "data center" OR datacenter OR "server room" OR "server farm" OR colocation OR hosting OR cloud)
site:tokelau.org.nz (ICT OR digital OR telecommunications OR "Energy and Telecommunications") (project OR tender OR procurement OR contract OR strategy)
site:mfat.govt.nz Tokelau ("data centre" OR "data center" OR cloud OR ICT OR digital OR broadband OR cable OR infrastructure)
site:legislation.govt.nz Tokelau (telecommunications OR privacy OR "data protection" OR "electronic transactions")
site:pacificdata.org Tokelau (internet OR phone OR computer OR telecommunications)
"Teletok" Tokelau (hosting OR server OR colocation OR "data centre" OR "data center" OR cloud)
"Telecommunication Tokelau Corporation" (hosting OR server OR colocation OR cable OR satellite)
site:tokelau.org.nz Teletok (server OR data OR cloud OR telecommunications OR cable)
"Teletok" (Southern Cross NEXT OR fibre OR "submarine cable" OR bandwidth OR capacity)
"Southern Cross NEXT" Tokelau ("landing" OR "cable landing" OR "Nukunonu" OR Teletok)
"Tokelau" ("submarine cable" OR fibre OR "cable landing" OR "landing station") ("Southern Cross" OR NEXT)
"Tokelau" (colocation OR colo OR "rack space" OR "carrier hotel" OR IXP OR "internet exchange")
"Tokelau" ("data centre" OR "data center" OR datacenter) -tourism
"Tokelau" (AWS OR Azure OR "Google Cloud" OR Oracle OR OCI OR "cloud region" OR "local zone" OR "edge location")
"Tokelau" (GPU OR AI OR "artificial intelligence" OR supercomputer OR "high performance computing")
"Tokelau" (solar OR battery OR diesel OR generator OR microgrid) (Teletok OR telecommunications OR "data centre" OR "server")
"Tokelau Renewable Energy Project" (kW OR MW OR panels OR battery OR diesel)
site:datacentermap.com Tokelau
site:cloudinfrastructuremap.com Tokelau
"Tokelau" ".tk" ("data center" OR hosting OR server OR DNS)
"Dot TK" OR Freenom Tokelau (registry OR registrar OR DNS OR hosting)
"托克劳" (数据中心 OR 云 OR 算力 OR 海底光缆 OR 卫星互联网)
```

环礁模板：`"Atafu" Tokelau ("data centre" OR "data center" OR datacenter OR "server room" OR Teletok OR telecom OR cable OR "landing station")`（Nukunonu/Fakaofo 同构）；`site:tokelau.org.nz "{atoll}" (ICT OR telecommunications OR Teletok OR server OR cable OR solar OR power)`；`"{atoll}" Tokelau (Teletok OR telecom OR satellite OR fibre OR "earth station" OR server OR hosting OR colocation)`。变化检测触发器：`"Tokelau" ("cloud region" OR "sovereign cloud" OR "government cloud" OR "national data centre")`、`"Tokelau" ("Southern Cross NEXT" OR "submarine cable" OR fibre OR "landing station" OR "cable landing")`、`"Teletok" (hosting OR server OR colocation OR cloud OR "data centre" OR "data center")`。

## 官方/监管管线要点（详见 explorer-official.md）

- **官方来源登记表**：NZ MFAT Tokelau 页（宪政/治理基线，A）、Tokelau Government 门户 tokelau.org.nz（国家部门、通知、统计、General Fono，A）、Energy and Telecommunications 部门页（历史官方文本，需核实时效）、Solar Project 页（环礁微电网/可再生能源背景，A）、Statistics 页（人口与普查指针，A）、SPC/Pacific Data Hub 2022 人口与住房普查（最新普查数据集路由，A/B）、Tokelau Act 1948（NZ 法律基础，仅宪政背景，A）、IANA `.tk` root 记录（ccTLD 管理者 Teletok/Fakaofo，非本地 DC 证明，A）、Southern Cross NEXT/Ciena launch（确认托克劳与基里巴斯首批国际海底光纤连接，A/B）、Southern Cross Cable Network（系统总览，列 Fiji/Tokelau/Kiribati 连接，A/B）。
- **按 division 枚举策略**：Fakaofo（中优先级——Tokelau Government village/departments、IANA `.tk` 记录、Teletok/Fenuafala 引用；只有一级来源点名 Fakaofo 物理服务器房/电信设施/海缆/登陆设备或 DC 类功能才计数）；Nukunonu（中——Southern Cross NEXT 路由引用、Teletok/政府电信材料；海缆/电信节点按电信/海缆设施处理，除非明确证据显示 hosting/colo 服务）；Atafu（低——预期无 DC，只记录点名的一级来源设施）；Unknown TK（高——任何国家级或无法分配环礁的来源，优先 Unknown TK 而非发明环礁分配）。
- **变化检测**：每次生产枚举前重跑触发器；若任何 A/B 来源报告新海缆登陆站建筑、Teletok hosting/colo 产品、政府数据中心采购、带 TK 物理站点的 sovereign-cloud 计划、hyperscaler edge/region/Local Zone、为持续 IT load 扩容的电力系统、或任何带机架/冷却/安防的具名设施，升级人工审查。
- **复核清单**：确认 manifest 仍列 TK；重查 NZ MFAT 与 Tokelau Government 的 ICT/海缆/云/采购/公共服务 IT 变化；重查 Southern Cross/Ciena 的登陆节点细节与环礁位置；通过 Tokelau Government 与 IANA 重查 Teletok 身份与当前官方服务页；重查 AWS/Azure/GCP/OCI 官方区域列表；重查能源/项目记录是否有工业规模发电或电网变化；保持 `.tk`/Freenom/DNS 基础设施与托克劳物理设施分离；若无一级设施证据，记录 TK 为 **commercial DC/colo/cloud verified-negative**。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **行业现实**：商业 DC/colo/云市场 verified-negative 基线——公开运营商、官方、云厂商和行业搜索未发现托克劳商业托管商、云区域、carrier-neutral 设施、IXP、CDN edge 设施、AI/HPC 站点或企业 DC 市场；预期商业计数为零。连接性已实质改善但这不是 DC 证据（Southern Cross NEXT 提供首条国际海底光纤连接）。运营商集极小：Teletok / Telecommunication Tokelau Corporation 是关键电信实体。需求与电力是微尺度：官方 2016 年人口 1,499（Atafu 541、Fakaofo 506、Nukunonu 452），可再生能源系统为本地太阳能阵列、电池和发电机——支持电信/政府 IT 机房，不支持 MW 级商业 IT load。
- **互联 pivots**：Southern Cross NEXT（2022-07-07 发布，Ciena 称提供托克劳与基里巴斯首批国际海底光纤连接；2023 年 400GbE 商用服务重申）作为主要现代互联 pivot，是海缆/连通性 lead 不是 DC lead；旧卫星链路（每环礁一条、Teletok 管理）作为历史/当前韧性 lead，不把卫星终端/VSAT/Starlink 终端或网关计为 DC，除非来源明确点名 hosting/compute/colo 功能。
- **`.tk` 域名噪声**：`.tk` 是托克劳最高风险误报源——IANA 记录 `.tk` 为 ccTLD 并列出管理者 Teletok（Fakaofo），但技术联系指向阿姆斯特丹的 BV Dot TK，域名服务器不是托克劳本地数据中心容量证据；Freenom/Dot TK 免费域名历史只与网络/DNS 市场注释相关。规则：除非来源独立证明托克劳境内物理设备，`.tk` 条目只作 DNS/registry 上下文记录。
- **能源与可建性**：托克劳政府太阳能项目页描述三环礁本地太阳能板、电池和发电机满足岛屿需求；能源与电信材料显示 Teletok 是本地系统重要电力用户，强化电信负载在微电网背景下可见。任何商业 DC 主张必须展示其电源来源；MW 级 IT load 在没有单独证实的发电、燃料、冷却、土地和物流计划的情况下不可信。
- **候选字段与升级**：最低计数标准同一级；升级触发器：Teletok 发布 hosting/rack/cloud/IXP/caching/企业数据中心服务、Tokelau Government 或 NZ MFAT 发布数据中心/云采购或物理服务器房项目、Southern Cross/Teletok 发布带 rack/power/hosting 功能的详细登陆站或海底终端信息、hyperscaler 将 TK 加入官方 region/Local Zone/edge/cloud-location 列表、能源项目文件显示为持续非电信 IT load 定容的发电/储能。

## 维护注意（更新纪律）

- 不删除/移动任何既有文件；双 explorer 文件是 codex 审核定稿，SKILL.md 忠实提炼其内容，细则差异以 explorer 原文件为准。
- 默认基线：**Tokelau 截至 2026-08-12 无已核实的商业数据中心、托管、hyperscale 云、IXP 或 AI/HPC 市场**；只有一级来源改变基线。唯一可信基础设施 lead 是绑在 Teletok、Tokelau Government 与 Southern Cross NEXT 上的微尺度电信/海缆/政府 IT 设施，无明确一级证据前不得计为商业 DC 容量。
- 保持 `.tk`/Freenom/DNS 基础设施与托克劳物理设施分离；海缆登陆站/卫星终端/电信交换局不得计为托管；太阳能/电池/发电机/制冷负载不得计为 IT load；离岸 NZ/萨摩亚托管的政府服务不得计为 TK 本地托管。
