---
name: bv-datacenter-methodology
location: scripts/expansion/world/country-skills/BV/SKILL.md
description: 布维岛数据中心发现与审计方法论（bilingual）。Bouvet Island datacenter discovery & audit methodology: verified-negative territory — enumerate the official/regulatory/cloud pipeline (Norsk Polarinstitutt npolar.no, regjeringen.no dependency policy, Lovdata nature-reserve regulations, Norid .bv/IANA/ITU numbering, Nkom & official cloud-region absence checks) plus industry/trade-press discovery (datacenter directories, cloud region lists, submarine-cable/network maps, satellite/expedition surfaces, domain-name pitfalls). Division model: country with 1 division (Bouvet Island); expected facility inventory = 0. Read before running BV exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# BV · 布维岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：布维岛（Bouvet Island / Bouvetøya, BV）为挪威在南大西洋/南大洋的**无人属地**（Norwegian dependency，挪威语 Bouvetøya），约 89% 被冰川覆盖、面积约 49 km²，岛屿及周边领海为自然保护（nature reserve）。无常住人口、无城镇、无电网、无商业电信、无数据中心市场。**本 skill 的核心目标是把 BV 做成可审计的 verified-negative**：官方来源证明其没有数据中心行业；任何命中都先按科研/航海/业余无线电/域名占位等假阳性处理。本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/厂商/媒体发现（explorer-industry.md）**双轨系统排除 false positives；本 skill 汇总两份最终审定报告，作为 BV 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | Norsk Polarinstitutt（npolar.no 地理/保护区/科考）、regjeringen.no（属地政策，Meld. St. 33 (2014-2015) 等）、Lovdata（保护区法规原文）、Norid `.bv`/IANA/ITU（编号资源）、Nkom 与官方云区域清单（阴性对照） |
| explorer-industry.md | 行业/厂商发现 | 数据中心目录（DataCenterMap、Cloudscene、Baxtel、datacenters.com）、行业媒体（DCD、SubTel Forum）、云区域/海缆/网络地图（Submarine Cable Map/Telegeography、PeeringDB/BGP、APNIC/RIPE）、卫星/科考/业余无线电表面（Iridium/Inmarsat/Starlink、NPI、3Y0 DX-pedition）、`.bv` 域名误读排除 |

## 核心结构事实

1. **行政区划模型**：manifest 为 **country**，恰好 **1 个 division：`Bouvet Island`**（subnational_type="country"，divisions=["Bouvet Island"]）；地理亚区（**Nyrøysa** 可登陆区、Bouvetøya 自然保护/领海、Larsøya/悬崖/冰川/Olavtoppen）仅用于解释与地理标注，**不是 division**；船舶/渔业/海洋监测线索不计数。
2. **注册库现状**：不存在数据中心注册表；预期设施清单（expected facility inventory）= **0**；`verified-negative` 为默认状态，只有 A 级来源点名商业设施（名称+运营方+位置+用途）并具备电力与连接证据时才允许升级为候选。
3. **地面实况（为什么没有设施）**：①人口与需求为零（无居民、无企业、无本地客群）；②基础设施为零（无公共电网、无固定宽带/移动网络、无海底光缆、无 DC 级供水/冷却/物流）；③地理极端偏远（登陆依赖远洋船只/直升机窗口，不具备常规建设运维条件）；④保护区限制（自然保护法规以保护地貌/动植物/生态为核心，商业开发与大型工程缺乏许可基础）；⑤数字资源也不构成市场（`.bv` ccTLD 由 Norid 管理但**从未开放域名注册**，只说明 ISO/互联编号存在，不代表本地互联产业）。
4. **法律与监管**：挪威属地；Lovdata 收录 `Forskrift om Bouvetøya naturreservat`（1971-12-17-9）与 `Lov om Bouvet-øya, Peter I's øy og Dronning Maud Land m.m.`；Norsk Polarinstitutt 为第一官方表面（npolar.no/en/themes/bouvetoya）；挪威政府文件 Meld. St. 33 (2014-2015) 明确属地政策/法律地位/管理框架。
5. **设施/项目种子（2026-08 证据状态）**：**无**；自动气象站、临时科考营地、卫星电话/无线电、船载通信、业余无线电 DX-pedition（3Y0 前缀）都不是 commercial datacenter/colocation/cloud region；`.bv` 域名、同名公司（Bouvet ASA / Bouvet Norge AS——挪威 IT 咨询公司）、挪威本土 DC 项目（Lefdal、Oslo、Skien、Glomfjord、Tydal）、南极/亚南极科研设施（Troll、Svalbard/SvalSat、Jan Mayen、Dronning Maud Land）均为假阳性，不得归入 BV。
6. **语言与词汇**：中文为主、英文/挪威语关键词为辅；挪威语召回：datasenter、serverhall、datarom、telekommunikasjon、fiber、kraft、værstasjon、ekspedisjon satellitt、skytjeneste、kraftforsyning、forskningsstasjon；中文召回：布维岛/布韦岛 数据中心/云区域/海底光缆/科考 通信；英文：data center/centre、datacenter、colocation、hosting、cloud region、submarine cable、cable landing、telecommunications、satellite、weather station。
7. **可靠性分级**：A = 官方/一手（NPI、regjeringen.no、Lovdata、Norid、Nkom/ITU/IANA、官方云区域清单、具名卫星/电信运营商官方页）；B = 权威二级（DCD、SubTel Forum、Telegeography/Submarine Cable Map、APNIC/PeeringDB/BGP 工具、主流媒体、科学机构、CIA World Factbook）；C = 弱来源（目录站、市场报告、SEO 内容、博客、社交媒体、无来源聚合页）——仅作线索；U = 无法二次确认或来源无法打开。**分级只覆盖该源实际支撑的事实**：目录国家下拉列表/营销页地区列表/市场报告国家枚举不代表设施；行业媒体仅提 Norway/Nordics DC 市场不得外推至 BV。
8. **计数与去重规则**：默认 `verified-negative`，预期设施数 0；升级候选须同时满足：来源非目录占位/国家选择器/SEO 汇总；设施在 Bouvet Island 陆地上而非挪威本土/南极站/船舶/同名公司；功能明确为 commercial datacenter/colocation/cloud/hosting 而非科研/气象/卫星通信/无线电/船载系统；有可核查的电力与连接方案；有 A 级官方或运营商来源；卫星覆盖/临时终端是连通性背景不是 DC 设施；业余无线电是临时活动不能转化为电信运营商或服务器设施；自动气象站/科研采集设备只标 `scientific equipment` 或 `rejected false positive`。

## 常用查询模板

```text
# 官方
site:npolar.no Bouvetøya ("data center" OR "data centre" OR datacenter OR server OR datasenter)
site:npolar.no "Bouvet Island" (station OR expedition OR weather OR monitoring)
site:regjeringen.no Bouvetøya (biland OR naturreservat OR infrastruktur OR telekommunikasjon OR datasenter OR kraft)
site:lovdata.no Bouvetøya (naturreservat OR biland OR ferdsel OR fredning OR forskrift)
site:norid.no ".bv" ; site:iana.org "/bv.html" ; ".bv" domain registration Bouvet Island
# 挪威语
Bouvetøya datasenter ; Bouvetøya serverhall ; Bouvetøya datarom ; Bouvetøya telekommunikasjon
Bouvetøya fiber ; Bouvetøya kraft ; Bouvetøya værstasjon ; Bouvetøya ekspedisjon satellitt
# 英文
"Bouvet Island" ("data center" OR datacenter OR "data centre")
"Bouvet Island" (colocation OR colo OR hosting OR "server farm" OR "cloud region" OR "edge location")
"Bouvet Island" (telecom OR ISP OR carrier OR fiber OR submarine cable OR "cable landing")
"Bouvet Island" (satellite communications OR Iridium OR Inmarsat OR Starlink OR Viasat)
"Bouvet Island" (DXpedition OR "3Y0") ; "Bouvet Island" "weather station"
# 中文
"布维岛" "数据中心" ; "布韦岛" "数据中心" ; "布维岛" "云区域" ; "布维岛" "海底光缆"
# 目录/媒体专项（C/B，仅发现）
site:datacenterdynamics.com Bouvet ; site:baxtel.com Bouvet ; site:cloudscene.com Bouvet
site:datacentermap.com Bouvet ; site:subtelforum.com Bouvet ; site:submarinenetworks.com Bouvet
# 云/互联阴性对照
AWS regions Bouvet Island ; Azure regions Bouvet Island ; Google Cloud locations Bouvet Island
Oracle OCI regions Bouvet Island ; Cloudflare datacenter Bouvet Island ; site:nkom.no Bouvetøya datasenter
"Bouvet Island" (ISP OR carrier OR ASN OR "internet exchange" OR mobile network OR MCC)
```

## 官方/监管管线要点（详见 explorer-official.md）

- **Norsk Polarinstitutt**（npolar.no）：确认地理/冰川覆盖/保护区状态/历史；查找近期科考、监测、自动气象站、登陆限制、地图/影像资料；将科研设备与商业数据中心分开标注。
- **regjeringen.no**：属地政策/法律地位/管理框架——`Meld. St. 33 (2014-2015) Norske interesser og politikk for Bouvetøya`、`Meld. St. 29 (2020-2021)` 与海洋/保护区政策、司法与公共安全部（Justis- og beredskapsdepartementet）极地事务页面。
- **Lovdata**：核实 `Forskrift om Bouvetøya naturreservat` 现行文本；判断任何工程/登陆/建设/采样/设备安装是否需许可。
- **Norid/IANA/ITU**：`.bv` 存在且由 Norid 管理但从未开放注册；不得把 ccTLD 当本地互联网市场证据；业余无线电前缀（3Y0）只证明远征/临时通信活动，不是电信运营商或数据中心。
- **阴性对照**：四大云区域清单 + Cloudflare + Nkom 数据中心登记——预期无 BV 条目、无边缘位置、无本地运营商记录。
- 每轮复核清单：NPI 页面（保护区/孤立性/无常住设施未变）→ regjeringen.no（属地与政策状态未变）→ Lovdata（无改变大型商业建设判断的新规）→ Norid `.bv`（仍未开放注册）→ 官方云区域 + Nkom（无 BV 条目）→ `Bouvet Island data center/datacenter/data centre` 与 `Bouvetøya datasenter/serverhall` 命中按科研/域名/业余无线电/同名企业/SEO 误报分类；结论保持 **BV = verified-negative, expected facility count 0**，除非出现挪威官方或具名运营商一手证据。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 行业工作不是寻找正常 pipeline，而是**系统排除 false positives**：最可能的行业命中并非设施——`.bv` ccTLD 页面、业余无线电远征、科考/气象设备、海洋/渔业监测、同名公司或市场报告的国家下拉列表。
- 目录（DataCenterMap、Cloudscene、Baxtel、Datacenters.com）若出现 BV 多半是国家选择器或空占位；无 A 级来源不得计数；行业媒体仅提 Norway/Nordics 市场不得外推到 BV（Oslo、Skien、Lefdal、Glomfjord 等项目不属于 Bouvet Island）。
- 云平台/海缆/网络：每轮核对 AWS/Azure/GCP/OCI/Cloudflare 官方页（预期无 region/AZ/local zone/edge）；无海底光缆登陆点、无本地 ASN/IXP/ISP 预期；船舶、卫星电话、业余无线电、临时科考链路均不构成商业连接基础设施。
- 卫星/科考（A/B 级但非设施证据）：Iridium/Inmarsat/Viasat/Starlink 官方覆盖或海事服务页、NPI 科考页、3Y0 DX-pedition 记录。
- 假阳性清单：`.bv` ccTLD、Bouvet ASA/Bouvet Norge AS（挪威 IT 咨询公司）、挪威本土 DC 项目、南极/亚南极科研设施、自动气象站与科考营地、业余无线电 DX-pedition、海洋/渔业船舶设备、市场报告国家列表、中文 SEO 拼接（"布维岛 数据中心/云/算力" 无 A/B 级来源按误报处理）。
- 诚实结论（2026-08）：商业 DC/colocation/hosting 无；公有云区域/AZ/edge 无；海底光缆/登陆站无；本地 ISP/移动网络/IXP 无；公共电网/大型电力设施无；可注册本地域名生态无。

## 维护注意（更新纪律）

- **更新节奏**：每季度——NPI Bouvetøya 页面（保护区/科考/登陆限制）、regjeringen.no 属地检索、Lovdata 法规、Norid `.bv`、四大云区域清单 + Nkom、英文/挪威语/中文关键词负向扫描；事件驱动——任何声称 Bouvet 设施的报道立即按假阳性清单分类并回官方源核实 A 级证据。
- **来源核验**：逐一点击 A 级 URL；命中必须区分 `.bv` 域名页、科研/气象设备、业余无线电活动、船载设备、同名公司（Bouvet ASA）、挪威本土项目与南极站——全部默认排除。
- **不删除纪律（no-deletion）**：已核实记录不得删除；状态变化须保留原始证据链；无支撑条目降级为 C/U 保留而非移除；负向检索（verified-negative）须如实记录核验过的官方表面而非跳过。
