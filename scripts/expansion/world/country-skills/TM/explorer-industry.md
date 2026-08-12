# TM（土库曼斯坦）Explorer — 行业 / 厂商发现方法学

# TM Explorer — Industry / Vendor Discovery Methodology

- 日期（Date）：2026-08-12
- 国家（Country）：Turkmenistan / Türkmenistan / Туркменистан（TM）
- 行政区（Divisions，来自 manifest）：Ahal、Balkan、Dashoguz、Lebap、Mary、Ashgabat
- 覆盖要求：6/6 division buckets 必须逐一跑查询；不要把 Ashgabat 并入 Ahal，也不要把 Arkadag/Ahal 线索误归 Ashgabat。
- 语言说明：中文为主、双语（Chinese-primary bilingual）；查询串保留 EN/RU/TK 原文。

---

## 0. 数据可用性约束（行业角度）— Data Availability Constraints

1. **行业媒体稀缺**：DCD 的 Turkmenistan 标签页可访问，但本次仅核到一条 2023 Huawei 固网扩容相关报道；没有稳定的 TM 数据中心新闻流。
2. **公开运营商信息有限**：`telecom.tm` 有官方 hosting/Physical Server 服务页，支持“国营电信提供 hosting/服务器服务”的 A 级结论，但未公开设施名称、容量、Tier 或机房地址。
3. **目录覆盖弱**：Data Center Map、Datacenters.com、Cloudscene、Baxtel 等可作为目录入口，但 TM 市场预期为空或噪声大；目录条目一律 C 级。
4. **厂商消息多为 MoU/论坛**：Huawei、ZTE、Bitdeer 等在 TM 的公开资料多是会谈、论坛演讲、意向或探索。没有官方开工/启用/电网/土地证据前，不计为设施。
5. **采购和地图不可直接计数**：采购站、地图点、BGP/WHOIS、社交媒体只提供 seed，不提供设施 existence。
6. **流亡/独立媒体**：Chronicles of Turkmenistan、Turkmen.news、Azatlyk 可发现被官方隐藏的线索，但需回官方/运营商/厂商材料复核；默认 B-/C。
7. **容量慎用**：任何 MW 必须标注 `IT load / facility load / grid / generation / unspecified`。论坛或投资稿中的“可利用能源”不能转成 DC MW。

---

## 1. 分级规则（Grading Rules）

| 级别 | 来源类型 | 使用方式 |
|---|---|---|
| **A** | `telecom.tm`、`mincom.gov.tm`、政府/TDH/部委/市官网、云厂商官方区域页、Uptime Institute | 可支持实体、政策、服务或状态；是否支持设施取决于页面是否明确设施 |
| **A-** | 官方城市/数字服务介绍、未披露设施细节的运营商服务页 | 背景或单一线索；不能拆分容量/位置 |
| **B** | DCD、Business Turkmenistan、Turkmenportal、ORIENT、Arzuw、Times of Central Asia、Trend.az、Caspian News、Bitdeer IR/官方活动页 | 发现和交叉验证；MoU/探索保持 planned/prospect |
| **C** | Data Center Map、Datacenters.com、Cloudscene、Baxtel、2GIS/Yandex Maps、BGP.tools、WHTop、采购聚合、社交媒体、营销 SEO 页面 | 种子和排除噪声；不直接入册计数 |

容量层级（Capacity hierarchy）：官方/运营商 IT MW > Uptime/认证设施规格 > 官方启用报道 > 厂商官方披露 > 行业媒体 > 目录。

状态层级（Status hierarchy）：运营服务/启用报道 > 建成/运营认证 > 融资+开工 > 开工仪式 > 土地/许可 > MoU/lease/explores > 政策话语 > 目录。

---

## 2. 市场分桶（Market Buckets）

1. **国营电信 / Hosting**：Türkmentelekom / Turkmentelekom（`https://telecom.tm`）。官方 hosting 页列出 Physical Server 产品和 Ashgabat Archabil pr. 88 联系地址；记录为 hosting 服务线索，除非新页面披露机房。
2. **通信主管机构**：Ministry Communications of Turkmenistan / Türkmenistanyň Aragatnaşyk ministrligi（`https://mincom.gov.tm`）。用于确认 Turkmentelekom、TM CELL 等官方关联实体。
3. **移动核心网**：TM CELL / Altyn Asyr、MTS Turkmenistan。核心网/5G 机房通常未公开；没有设施披露时只作 telecom core room seed。
4. **电子政务 / 国家 Data Centre**：官方资料支持国家 Data Centre 计划级线索，重点在 Ashgabat；需继续寻找 opened/commissioned 证据。
5. **Arkadag 智慧城市 ICT**：Ahal 桶。5G、GPON、e-government、数字服务等是强 ICT 背景，但不是 DC 设施。
6. **Huawei / ZTE 厂商项目**：固网扩容、智慧城市、5G、政府数字化。DCD 和国家媒体可作 B 级线索，需回官方。
7. **Bitdeer / AI-HPC prospect**：2025-2026 公开资料显示 Bitdeer 参与官方活动并探索/签署数字基础设施相关 MoU；当前按 B/C prospect，不计设施。
8. **跨境光纤 / 里海项目**：Balkan、Lebap 可能受益；除非有登陆站/机房/运营商设施证据，否则只作 connectivity context。
9. **目录/地图/SEO**：只用于找名称，必须回 A/B 级复核。

---

## 3. 权威行业来源（Authoritative Industry Sources）

### 3.1 运营商、认证、云

| 来源 | 已核验 URL | 用途 | 级别 |
|---|---|---|---|
| Turkmentelekom | https://telecom.tm | 国营电信、互联网、hosting 服务入口 | A |
| Turkmentelekom hosting | https://telecom.tm/en/hosting/ | Physical Server/hosting 服务；未给设施规格 | A- |
| 通信部 / Ministry Communications | https://mincom.gov.tm | 机构和下属通信实体确认 | A |
| Uptime TM 国家页 | https://uptimeinstitute.com/uptime-institute-awards/country/id/TM | 认证复检入口；未核到具体 TM award | A |
| Uptime 全列表 | https://uptimeinstitute.com/uptime-institute-awards/list | 按 country/client 复扫 | A |
| AWS/Azure/GCP/Oracle/Yandex/Alibaba | 见官方方法学云章节 | 确认无 TM public cloud region | A |

### 3.2 行业媒体与区域媒体

| 来源 | URL | 用途 | 级别 |
|---|---|---|---|
| Data Center Dynamics（TM 标签） | https://www.datacenterdynamics.com/en/tags/turkmenistan/ | 行业媒体；本次核到 Huawei 固网扩容新闻，非 DC 设施 | B |
| Business Turkmenistan | https://business.com.tm | 商业/投资/论坛；Bitdeer 等线索 | B |
| Turkmenportal | https://www.turkmenportal.com | 国家对齐新闻/公告/目录 | B |
| ORIENT | https://orient.tm | 俄语新闻，适合搜数字化/通信 | B |
| Arzuw News | https://arzuw.news | 土/俄新闻补充 | B |
| Times of Central Asia | https://timesca.com | 区域英文报道，适合投资/数字化/能源 | B |
| Trend.az | https://trend.az | 里海/中亚通信与能源线索 | B |
| Caspian News | https://caspiannews.com | 里海项目、跨境基础设施 | B |
| News Central Asia | https://www.newscentralasia.net | Bitdeer/论坛类线索；需回官方/公司复核 | B-/C |
| Chronicles of Turkmenistan | https://www.hronikatm.com | 流亡媒体线索 | B-/C |
| Turkmen.news | https://turkmen.news | 独立媒体线索 | B-/C |
| Azatlyk / RFE-RL | https://www.azathabar.com | 独立广播媒体线索 | B-/C |

### 3.3 目录与地图

| 来源 | URL | 用途 | 级别 |
|---|---|---|---|
| Data Center Map | https://www.datacentermap.com/datacenters/ | 全球国家目录；搜索 TM/Turkmenistan | C |
| Datacenters.com | https://www.datacenters.com/locations | 全球 location/provider 目录 | C |
| Cloudscene | https://cloudscene.com | 市场/服务商目录；TM 可能无市场页 | C |
| Baxtel | https://baxtel.com/map | 全球 DC 地图；TM 预期无条目 | C |
| 2GIS / Yandex Maps | https://2gis.tm / https://yandex.com/maps | 地址种子，覆盖稀疏 | C |
| BGP.tools | https://bgp.tools/as/20661 | Turkmentelekom AS/network context | C |
| WHTop | https://www.whtop.com/top.10-web-hosting/country-tm | hosting provider seed；已显示 telecom.tm | C |

---

## 4. 国家查询模板（National Query Templates）

### 4.1 广撒网（Broad Discovery）

```text
Turkmenistan "data center" OR "datacenter" "Ashgabat"
Turkmenistan "National data centre" OR "single Information Center"
Turkmenistan "colocation" OR "hosting" "Turkmentelekom"
Туркменистан "дата-центр" OR "центр обработки данных" OR "ЦОД"
Туркменистан "серверная" OR "хостинг" "Ашхабад"
Türkmenistan "maglumat merkezi" OR "serwer" OR "hosting"
"sanly ykdysadyýet" OR "цифровая экономика" "Türkmenistan" "maglumat"
"умный город" OR "akylly şäher" "Arkadag" "сервер" OR "5G" OR "GPON"
```

### 4.2 源限定扫描（Source-Restricted Sweeps）

```text
site:telecom.tm "hosting" OR "Physical Server" OR "data center"
site:mincom.gov.tm "сервер" OR "дата-центр" OR "hosting"
site:datacenterdynamics.com Turkmenistan "data center" OR "Huawei" OR "telecoms"
site:business.com.tm Turkmenistan "data center" OR "Bitdeer" OR "digital infrastructure"
site:turkmenportal.com "дата-центр" OR "сервер" OR "ЦОД" OR "Arkadag"
site:orient.tm "дата-центр" OR "цифровизация" OR "сервер"
site:timesca.com Turkmenistan "data center" OR "digital" OR "White City Ashgabat"
site:trend.az Туркменистан "оптоволокно" OR "цифровой" OR "дата-центр"
site:newscentralasia.net Turkmenistan "Bitdeer" OR "data center"
site:hronikatm.com "дата-центр" OR "сервер"
site:turkmen.news "data center" OR "дата-центр"
site:azathabar.com "дата-центр" OR "maglumat merkezi"
```

### 4.3 运营商 / 项目扫描（Operator / Project Sweeps）

```text
"Turkmentelekom" OR "Türkmentelekom" OR "Туркментелеком" "hosting" OR "дата-центр" OR "сервер"
"telecom.tm" "Physical Server" OR "hosting" OR "сервер"
"TM CELL" OR "Altyn Asyr" OR "Алтын Асыр" "5G" OR "сервер" OR "ЦОД"
"MTS Turkmenistan" "data center" OR "дата-центр" OR "server"
"Huawei" "Turkmenistan" "fixed line" OR "Arkadag" OR "smart city" OR "data center"
"ZTE" "Turkmenistan" "связь" OR "сервер" OR "цифров"
"Bitdeer" "Turkmenistan" "data center" OR "digital infrastructure" OR "White City Ashgabat"
"Транскаспийский" OR "Trans-Caspian" "fiber" OR "оптоволокно" "Turkmenistan"
"национальный дата-центр" OR "единый информационный центр" "Туркменистан"
```

### 4.4 状态 / 容量抽取（Status / Capacity Extraction）

```text
"{project}" "MW" OR "МВт" OR "IT capacity" OR "quwaty"
"{project}" "Tier III" OR "Tier 3" OR "Uptime"
"{project}" "opened" OR "commissioned" OR "operational"
"{project}" "открыт" OR "введён в эксплуатацию" OR "работает"
"{project}" "açyldy" OR "işe girizildi" OR "işleýär"
"{project}" "construction began" OR "началось строительство" OR "gurluşyk başlandy"
"{project}" "MoU" OR "memorandum" OR "меморандум" OR "explores"
"{project}" "electricity" OR "электроэнергия" OR "подстанция" OR "elektrik"
```

---

## 5. 枚举矩阵（Enumeration Matrix：6 行政区 × 分桶）

| 行政区 | 国营电信/hosting | 移动核心网 | 电子政务/国家 DC | 厂商/智慧城市 | 投资者/AI-HPC | 目录/地图 |
|---|---|---|---|---|---|---|
| **Ahal** | 近首都节点，需与 Ashgabat 去重 | 5G/GPON/区域移动节点 | 无已核国家 DC | **Arkadag 智慧城市 ICT，高优先但非 DC** | Bitdeer/论坛若落 Ahal 需官方证据 | 稀疏，C |
| **Balkan** | 港区/油气通信节点 | 区域节点 | 无已核 | 跨里海光纤潜在登陆点 | 低 | 稀疏，C |
| **Dashoguz** | 区域通信机房 | 区域节点 | 无已核 | 低 | 低 | 稀疏，C |
| **Lebap** | Türkmenabat/东部走廊节点 | 区域节点 | 无已核 | 口岸/跨境光纤 | 低 | 稀疏，C |
| **Mary** | 区域通信机房 | 区域节点 | 无已核 | 天然气工业数字化 | 低 | 稀疏，C |
| **Ashgabat** | **telecom.tm hosting、核心网、Archabil Ave. 实体地址** | **TM CELL/MTS 核心网线索** | **国家 Data Centre 计划级单一线索** | 政府数字化/部委 IT | Bitdeer/White City 活动需核地点 | 中，C |

每区主查询（替换 `{div}`/`{city}`）：

```text
"{city_ru}" "дата-центр" OR "ЦОД" OR "серверная" OR "телекоммуникационный узел"
"{city}" "maglumat merkezi" OR "serwer otagy" OR "aragatnaşyk"
"{div_ru}" "цифровизация" OR "информационные технологии" OR "дата-центр"
"{div}" "sanly" OR "maglumat" OR "serwer"
```

---

## 6. 当前已知行业信号（不要直接计数）

1. **Turkmentelekom hosting（A-/Ashgabat）**：官方 hosting 页列 Physical Server 和服务价格；支持“运营商提供 hosting/服务器服务”，不支持具体 DC 容量或 Tier。
2. **国家 Data Centre（A policy lead/Ashgabat）**：官方 2018-2022 资料显示计划/推进创建；本次未核到启用证据。
3. **Arkadag 智慧城市（A-/B/Ahal）**：官方城市站和国家媒体支持 smart/digital city、5G/GPON/数字服务；不等于独立 DC。
4. **Huawei 固网/ICT（B）**：DCD TM 标签页列 2023 “Huawei to support Turkmenistan's fixed line telecoms expansion”；作为 telecom vendor lead，非 DC。
5. **Bitdeer（B/C prospect）**：Business Turkmenistan 2025 报道 Bitdeer 探索在 TM 建高科技计算中心；News Central Asia 2026 报道 White City Ashgabat 2026 MoU/first data center 说法。除非 Bitdeer IR、政府公告或合同/土地/电力证据确认，不计设施。

---

## 7. 云 / 超大规模信号（Cloud / Hyperscaler Signals）

本次复检结论：AWS、Azure、Google Cloud、Oracle Cloud、Yandex Cloud、Alibaba Cloud 均无 TM public cloud region。Yandex Cloud 文档明确当前 region 为 Russia、Kazakhstan；Alibaba Global Locations 未列 Turkmenistan；AWS/Azure/GCP/Oracle 页面未出现 Turkmenistan。

查询：

```text
site:aws.amazon.com Turkmenistan "region" OR "Local Zone"
site:azure.microsoft.com Turkmenistan "geography" OR "data center"
site:cloud.google.com Turkmenistan "locations" OR "region"
site:oracle.com Turkmenistan "cloud region"
site:yandex.cloud Turkmenistan "region" OR "Ashgabat"
site:alibabacloud.com Turkmenistan "region"
"Turkmenistan" "cloud region" "AWS" OR "Azure" OR "Google" OR "Oracle" OR "Alibaba" OR "Huawei" OR "Yandex"
```

---

## 8. 验证与去重规则（Verification and Deduplication）

1. 不要把 Turkmentelekom hosting 服务页拆成多个设施；没有机房名/地址/容量时只保留一个运营商服务线索。
2. 不要把国家 Data Centre 的计划报道、Single Information Center、电子政务平台重复计数；除非出现清晰不同物理地点。
3. 不要把 Ashgabat 与 Ahal/Arkadag 混桶：Ashgabat 是 manifest 独立 city bucket；Arkadag 属 Ahal。
4. 移动运营商核心网、5G、GPON、卫星、互联网接入升级不是数据中心，除非披露“ЦОД/дата-центр/серверная/центр обработки данных”设施。
5. MoU、论坛发言、investment pitch、explores/opportunities 一律按 prospect；升级需要官方土地、电力、合同、开工或启用。
6. 目录、地图、SEO 站、采购聚合站不直接计数；必须回运营商、政府、厂商官方或可信媒体。
7. 容量字段必须保留容量类型：`it_load`、`facility_power`、`grid_connection`、`generation_capacity`、`unspecified`。
8. 认证字段只接受 Uptime Institute 官方或同等认证机构官方页面。
9. 所有记录写 `last_verified_date`，TM 尤其需要保留失败核验（timeout/404/no result）说明。

---

## 9. 输出字段（Output Fields）

```text
facility_name
aliases_tk_ru_en
operator
owner_or_sponsor
tenant_anchor_customer
division
city_or_district
address_or_site_description
latitude_longitude_if_verified
status
status_evidence_url
status_evidence_grade
capacity_value
capacity_unit
capacity_type_it_load_facility_load_grid_generation_or_unspecified
certification_type
certification_url
power_or_grid_evidence
source_notes
last_verified_date
```

来源备注标签：

```text
operator official
government announcement
state media
official city digital service
regional trade press
vendor MoU/prospect
exile media seed
directory seed
map seed
telecom core room no public DC evidence
hosting service no facility details
policy no facility
```

---

## 10. 本次已核验行业 URL（Verified Source Set）

```text
https://telecom.tm
https://telecom.tm/en/hosting/
https://mincom.gov.tm
https://www.datacenterdynamics.com/en/tags/turkmenistan/
https://business.com.tm/post/14568/bitdeer-explores-data-center-opportunities-in-turkmenistan
https://www.newscentralasia.net/2026/05/26/why-turkmenistan-is-worth-watching-in-the-global-data-center-race/
https://www.newscentralasia.net/2026/05/25/white-city-ashgabat-2026-bitdeer-technologies-group-to-build-first-data-center-in-turkmenistan/
https://ir.bitdeer.com/news-releases/news-release-details/bitdeer-announces-june-2026-production-and-operations-update/
https://uptimeinstitute.com/uptime-institute-awards/country/id/TM
https://www.datacentermap.com/datacenters/
https://www.datacenters.com/locations
https://cloudscene.com
https://baxtel.com/map
https://bgp.tools/as/20661
https://www.whtop.com/top.10-web-hosting/country-tm
```
