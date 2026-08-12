# BV 行业渠道探索 - 布维岛数据中心枚举
# BV Explorer Industry - Bouvet Island Datacenter Enumeration

日期 Date: 2026-08-12。范围 Scope: 从行业侧（数据中心目录、云平台、网络/海缆、卫星通信、行业媒体、域名/电信资源）发现布维岛（Bouvet Island / Bouvetøya, BV）的数据中心项目。始终与 `explorer-official.md` 交叉核对；行业来源只用于发现线索，最终以官方来源定性。

清单条目 (world-manifest.jsonl): `{"country_code":"BV","country_name":"Bouvet Island","subnational_type":"country","divisions":["Bouvet Island"]}`。仓库分区为单一 division: `Bouvet Island`。

本文档为中文为主、英文/挪威语关键词为辅的双语方法论（Chinese-primary bilingual）。

可靠性分级 Reliability grades:

- **A 级**: 运营商/平台/政府一手来源 - 官方云区域清单、Norid/IANA、NPI、regjeringen.no、Lovdata、Nkom/ITU、具名卫星/电信运营商官方页。
- **B 级**: 可靠行业/科学来源 - Data Center Dynamics、SubTel Forum、Telegeography/Submarine Cable Map、APNIC/PeeringDB/BGP 工具、主流媒体、科学机构。
- **C 级**: 目录站、市场报告、SEO 内容、博客、社交媒体、无来源聚合页。仅作线索。
- **U 级**: 无法二次确认或来源无法打开。

核心判断 Core judgement: **BV 没有商业数据中心市场；行业侧枚举预期为零设施。** 行业工作不是寻找正常 pipeline，而是系统排除 false positives。

---

## 0. 市场现实（Market Reality）

- BV 无常住人口、无城镇、无电网、无本地企业需求、无商业电信市场，且为挪威自然保护区。
- 数据中心行业三项基本前提均不存在: 稳定电力、可靠大容量连接、可服务的本地/区域客户。
- 最可能出现的行业命中并非设施: `.bv` ccTLD 页面、业余无线电远征、科考/气象设备、海洋/渔业监测、同名公司或市场报告的国家下拉菜单。
- Data Center Map、Cloudscene、Baxtel、Datacenters.com 等目录若出现 BV，多半是国家选择器或空占位；无 A 级来源不得计数。

---

## 1. 行业来源（Industry Sources）

### 1.1 数据中心目录与行业媒体（Grade C/B）

用途: 快速确认是否存在行业侧异常声称；结果默认弱线索。

```text
site:datacentermap.com "Bouvet Island"
site:cloudscene.com "Bouvet Island"
site:baxtel.com "Bouvet Island"
site:datacenters.com "Bouvet Island"
site:datacenterdynamics.com "Bouvet Island" OR Bouvetøya
"Bouvet Island" ("data center" OR datacenter OR "data centre" OR colocation OR hosting)
```

处理规则:

- 国家下拉菜单、营销页地区列表、市场报告国家枚举不代表设施。
- 行业媒体若仅提到 Norway/Nordics 数据中心市场，不得外推到 BV；挪威本土项目（Oslo、Skien、Lefdal、Glomfjord 等）不属于 Bouvet Island。

### 1.2 云平台官方区域（Grade A 阴性对照）

每轮核查:

```text
AWS regions Bouvet Island
Azure regions Bouvet Island
Google Cloud locations Bouvet Island
Oracle OCI regions Bouvet Island
Cloudflare datacenter Bouvet Island
```

预期: 无 BV region、availability zone、local zone、edge location。SaaS 服务可在全球访问不等于本地设施。

### 1.3 海缆、网络和互联（Grade A/B 阴性对照）

入口:

- Submarine Cable Map / Telegeography
- SubmarineNetworks.com / SubTel Forum
- PeeringDB
- APNIC/RIPE/BGP 工具
- Nkom/ITU 编号资源

查询:

```text
"Bouvet Island" submarine cable
"Bouvet Island" "cable landing"
"Bouvet Island" fiber OR fibre
"Bouvet Island" ISP OR carrier OR ASN OR "internet exchange"
"Bouvet Island" mobile network OR MCC
Bouvetøya telekommunikasjon OR fiber OR mobilnett
```

处理规则:

- 无海底光缆登陆点预期。
- 无本地 ASN/IXP/ISP 预期。
- 船舶、卫星电话、业余无线电、临时科考链路均不构成商业连接基础设施。

### 1.4 卫星通信和科考活动（Grade A/B，非设施证据）

可用表面:

- Iridium / Inmarsat / Viasat / Starlink 官方覆盖或海事服务页面。
- NPI 科考页面。
- 业余无线电 DX-pedition 记录（3Y0 前缀等）。

查询:

```text
"Bouvet Island" satellite communications
"Bouvet Island" Iridium OR Inmarsat OR Starlink OR Viasat
"Bouvet Island" "weather station" OR "automatic weather station"
"Bouvet Island" DXpedition OR "3Y0"
Bouvetøya satellitt OR værstasjon OR ekspedisjon
```

处理规则:

- 卫星覆盖或临时终端是连通性背景，不是数据中心设施。
- 业余无线电活动是临时活动，不能转化为电信运营商或服务器设施。
- 自动气象站/科研采集设备只可标为 `scientific equipment` 或 `rejected false positive`。

### 1.5 域名资源（Grade A，防误报）

Norid 官方页面确认 `.bv` 顶级域存在但从未开放注册。行业侧常见误读是把 ccTLD 当作互联网商业市场。

查询:

```text
site:norid.no ".bv" "Bouvet Island"
site:iana.org "/bv.html"
".bv" domain registration Bouvet Island
```

记录方式:

- `.bv` status: reserved / delegated, not open for registration。
- 不创建任何设施候选。

---

## 2. 行业查询模板（Search Templates）

英文主检索:

```text
"Bouvet Island" ("data center" OR datacenter OR "data centre")
"Bouvet Island" (colocation OR colo OR hosting OR "server farm")
"Bouvet Island" ("cloud region" OR "edge location" OR CDN)
"Bouvet Island" (GPU OR AI OR HPC OR supercomputer) (facility OR datacenter)
"Bouvet Island" (telecom OR ISP OR carrier OR fiber OR submarine cable)
"Bouvet Island" (power OR electricity OR generator) (facility OR station)
```

挪威语:

```text
Bouvetøya datasenter
Bouvetøya serverhall
Bouvetøya skytjeneste
Bouvetøya telekom
Bouvetøya fiber
Bouvetøya kraftforsyning
Bouvetøya forskningsstasjon
```

中文:

```text
"布维岛" "数据中心"
"布韦岛" "数据中心"
"布维岛" "云区域"
"布维岛" "服务器"
"布维岛" "海底光缆"
```

目录/媒体专项:

```text
site:datacenterdynamics.com Bouvet
site:baxtel.com Bouvet
site:cloudscene.com Bouvet
site:datacentermap.com Bouvet
site:subtelforum.com Bouvet
site:submarinenetworks.com Bouvet
```

---

## 3. 逐分区行业策略（Per-Division Industry Strategy）

| Repo division | 优先级 | 行业检索角度 | 升级条件 |
|---|---:|---|---|
| Bouvet Island | High | 目录站/行业媒体负向扫描；官方云区域缺失；海缆/网络/ASN/IXP 缺失；卫星/科考/业余无线电误报排除；`.bv` 域名误读排除 | 只有 A 级来源点名商业数据中心/托管项目（名称+运营方+位置+用途+电力/连接证据）时计数 |

地理亚区仅用于解释，不作为 division:

- **Nyrøysa**: 可能出现登陆、科考或自动设备线索；默认非商业设施。
- **Bouvetøya territorial waters**: 船舶与渔业/海洋监测线索；船载设备不计数。
- **Larsøya / cliffs / glaciers / Olavtoppen**: 地理背景；无设施预期。

---

## 4. 必填字段（Required Fields per Candidate）

本领地预期候选为空；若出现线索，按下列字段记录并先标为 `lead` 或 `rejected`:

```text
country_code: BV
division: Bouvet Island
facility_or_project_name:
operator:
facility_type: commercial datacenter | telco room | scientific equipment | satellite terminal | amateur radio | vessel equipment | false positive
status: lead | rejected | verified-negative
evidence_grade: A | B | C | U
primary_urls:
secondary_urls:
site_address: none unless official source gives a location
coordinates:
power: no public grid; require source-backed exception
connectivity: no submarine cable; require source-backed exception
notes:
last_checked: 2026-08-12
```

升级到设施记录前，必须同时满足:

- 来源不是目录占位、国家选择器或 SEO 汇总；
- 设施在 Bouvet Island 陆地上，而非挪威本土、南极站、船舶或同名公司；
- 功能明确为 commercial datacenter/colocation/cloud/hosting；
- 有可核查的电力和连接方案；
- 有 A 级官方或运营商来源。

---

## 5. 假阳性清单（False Positives）

1. **`.bv` ccTLD**: 由 Norid 管理但未开放注册；不是本地互联网产业。
2. **Bouvet ASA / Bouvet Norge AS**: 挪威 IT 咨询公司名称含 Bouvet，与 Bouvet Island 无关。
3. **挪威本土数据中心项目**: Lefdal、Oslo、Skien、Glomfjord、Tydal 等都不属于 BV。
4. **南极/亚南极科研设施**: Troll、Svalbard/SvalSat、Jan Mayen、Dronning Maud Land、其他国家南极站不得归入 BV。
5. **自动气象站与科考营地**: 科学数据采集和临时通信设备不是商业 DC。
6. **业余无线电 DX-pedition**: 3Y0 等呼号活动为临时远征通信，不是运营商设施。
7. **海洋/渔业船舶设备**: 船载通信、冷藏、导航和数据采集设备不属于陆上数据中心。
8. **市场报告国家列表**: 将 ISO 国家/地区下拉菜单误写为市场覆盖，C 级且默认排除。
9. **中文 SEO 拼接**: “布维岛 数据中心/云/算力” 无 A/B 级来源时按误报处理。

---

## 6. 已验证阴性（Verified Negatives）

截至 2026-08-12:

- **商业数据中心 / colocation / hosting**: 无。
- **云区域 / edge / CDN 本地节点**: 无。
- **海底光缆 / cable landing station**: 无。
- **IXP / ASN / 本地 ISP / 移动网络**: 无。
- **公共电网 / MW 级电力负载基础**: 无。
- **行业目录有效设施条目**: 无；若出现仅可作 C 级线索。

---

## 7. 工作流（Workflow）

1. 先读 `explorer-official.md`，确认 BV 单一 division 与官方地面实况。
2. 跑第 2 节英文/挪威语/中文组合检索，抓取所有 “data center / datasenter / 数据中心” 命中。
3. 对每条命中按第 5 节分类；优先排除 ccTLD、同名公司、挪威本土项目、科考/无线电/船载设备。
4. 重跑云区域、海缆、PeeringDB/BGP、Nkom/Norid 阴性对照。
5. 输出 verified-negative 记录。若发现异常项目，按第 4 节字段记录为 `lead`，并回到官方文件核查 A 级证据。

结论 Bottom line: **BV 行业侧预期设施数为 0；任何“布维岛数据中心”命中都必须先证明它不是域名、科考、无线电、船舶、同名企业或挪威本土市场误归属。**
