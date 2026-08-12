---
name: ck-datacenter-methodology
location: scripts/expansion/world/country-skills/CK/SKILL.md
description: 库克群岛数据中心发现与审计方法论（bilingual）。Cook Islands datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (PPCI procurement.gov.ck incl. CIG Data Centre Colocation RFT, MFEM, OPM National Digital Strategy/ICT policy, CRA telecom regulator, CIIC/ACL Avaroa Cable & Manatua, TAU power, official cloud-region absence checks) plus industry/trade-press discovery (Vodafone Cook Islands Data Housing & Hosting, APAC Outlook/Aiscorp/Submarine Networks/commsupdate/RNZ/Cook Islands News, PeeringDB/PCH, directories). Division model: country with 1 division (Cook Islands); site clusters Rarotonga/Aitutaki/Pa Enua. Read before running CK exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# CK · 库克群岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：库克群岛（CK）是极小市场，但**不能写成「零数据中心」**。已核实的设施级线索包括：**Vodafone Cook Islands / Telecom Cook Islands 的数据托管与小型 data centre 能力**、**OPM 的 CIG Data Center colocation 采购/升级**、以及 **Avaroa Cable 的 Manatua 登陆/国际与国内批发互联资产**。商用超大规模/大体量 colocation 缺位：未见 AWS/Azure/GCP/OCI 公共云区域，未见目录列出 CK 托管市场；但 Vodafone 的 Data Housing & Hosting、Cloud Services 与 Avarua/Aroa/Aitutaki 小型机房必须作为 `telco-hosting/data-centre` 线索记录。海缆不是数据中心：Manatua/Avaroa Cable 是互联锚点，只有来源明确指向机房、rack、hosting、data centre、government data center/colocation 时才可入设施候选。本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/媒体/厂商发现（explorer-industry.md）**双轨三角验证；本 skill 汇总两份最终审定报告，作为 CK 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | PPCI 采购门户（RFT Data Centre Colocation tender=3374、HCI/ICT 网络升级 tender=3361）、MFEM 采购、OPM（National Digital Strategy 2024-2030、Cyber Security Policy、National ICT Policy 2023-2027）、CRA 电信监管（Telecommunications Act 2019）、CIIC/ACL（Avaroa Cable/Manatua）、TAU 电力、ADB 可再生能源、官方云区域缺失检查 |
| explorer-industry.md | 行业/媒体/厂商发现 | Vodafone Cook Islands（Data Housing & Hosting、Cloud Services、LinkedIn Aitutaki 升级）、APAC Outlook 访谈（Avarua/Aroa/Aitutaki 三站）、Aiscorp（CIG colocation 升级）、Submarine Networks/GeoCables/commsupdate/Developing Telecoms/RNZ/Cook Islands News、PeeringDB/PCH（IXP/互联）、DataCenterMap/Cloudscene/Baxtel 目录 |

## 核心结构事实

1. **行政区划模型**：manifest 为 **country**，恰好 **1 个 division：`Cook Islands`**；站点头簇：**Rarotonga-Avarua/Parekura**（P1，OPM/CIG colocation、Vodafone HQ/Data Housing、CRA、政府采购）、**Rarotonga-Aroa/Rutaki/Avatiu**（P1，Vodafone Aroa 机房线索、Manatua landfall/CLS、TAU/Avatiu 电力）、**Aitutaki/Arutanga**（P1/P2，Manatua 国内登陆、Vodafone Aitutaki DC 升级）、**Southern Group**（Atiu/Mangaia/Mauke/Mitiaro，P2/P3，记录负向）、**Northern Group**（Penrhyn/Manihiki/Pukapuka/Rakahanga/Nassau，P2/P3，记录负向）、**无人岛/特殊**（Takutea/Manuae/Palmerston/Suwarrow，P3，通常 no_projects）；所有记录 division 固定 `Cook Islands`，island/site 填 Rarotonga/Aitutaki 等。
2. **注册库现状**：无全国数据中心注册库；验证渠道 = 政府采购（PPCI）、运营商官方页、CRA 牌照、官方云区域清单；非命中站点簇须记录 `no_projects` 避免误以为未查。
3. **法律与监管**：现行电信监管主体为 **Competition & Regulatory Authority of the Cook Islands (CRA)**（cra.org.ck；自 2021-03-01 起电信归其管辖，依据 **Telecommunications Act 2019** 与 Competition and Regulatory Authority Act 2019）；MFEM Telecommunications Reform 页确认 2019 政策与两部法律通过；旧法或「电信专家过渡期」说法仅作历史/误差线索。
4. **互联与云（负向+例外）**：**Manatua/Avaroa Cable**（ACL，A 级；3,600 km、two-fiber-pair，连接 Samoa/Niue/Rarotonga/Aitutaki/Tahiti/Bora Bora，RFS 2020-07-22）为互联锚点——asset_class=cable-landing 非 data-center；CK 登陆点至少覆盖 **Rarotonga 与 Aitutaki**（Avarua/Rutaki/Aroa 更细站名须来源支撑）；容量 10 Tb/s per fibre pair 仅作 connectivity capacity，不写入 IT MW；无 AWS/Azure/GCP/OCI CK region（A 级缺失）；**无本地 IXP**（PCH/PeeringDB live check；PeeringDB AS10131 Telecom Cook Islands 在 Equinix Sydney 的 public peering 是境外互联，不是 CK IXP/DC）。
5. **设施/项目种子（2026-08 证据状态）**：**CIG Data Center colocation / OPM ICT environment**（RFT 2020-11 发布、2020-12-09 截标——A 采购；Aiscorp 2022 发布稿称 2021-12 已升级 centralised network and data centre colocation——B 交付/授标线索，托管地点未公开）；**OPM HCI/Government ICT Network Upgrade**（RFT 2020-10/closed 2020-11——A，ICT 平台非独立新 DC）；**Vodafone Data Housing & Hosting**（官网 A 服务存在；Avarua/Aroa/Aitutaki 三站 per APAC Outlook——B；Aitutaki DC Upgrade 10m×5m 建筑、冗余 UPS/备用发电机/24×7 监控/冗余空调/结构化布线、2021-09 完成 per Vodafone LinkedIn——A-social/B）；**VakaNet**（ACL 故障公告列为客户——ISP/批发线索，非 DC）；**Manatua Rarotonga/Aitutaki landing**（A/B，cable-landing，当前故障状态须每次 live-check）；CRA（监管，A）；TAU（电力，A 非 DC）。
6. **语言与词汇**：英文为主；注意 **Avaroa（公司）与 Avarua（首都/镇）必须分开**；「data center」在联合国电子政务统计语境可能指「数据门户/统计数据库」而非机房；Manatua、O3b、Starlink、Kacific、WiFi hotspot 均为 connectivity 非 data centre；Vodafone Group 全球 DC/云引用 ≠ CK 设施，只接受 `Vodafone Cook Islands` 或本地站点证据。
7. **可靠性分级**：A = 政府/PPCI/MFEM/OPM/CRA/CIIC/TAU/ACL 官方页、官方采购公告、官方云区域页、PeeringDB/PCH 互联记录；A-social/B = 运营商自有 LinkedIn/Facebook 帖（可用于站点线索和状态，重要字段应尽量找官网备份）；B = Aiscorp（引用 OPM 时）、Submarine Networks/GeoCables、APAC Outlook/Developing Telecoms/commsupdate/RNZ/Cook Islands News/Islands Business（具名运营者与日期）；C = 市场报告、SEO 页、通用厂商国家下拉页、目录页、非运营者持有的社交帖、tender 镜像；U = 死链、无出处主张、无法关联 CK（而非 Samoa/Niue/法属波利尼西亚）的事实。**同一记录可按字段分级**：Vodafone `service exists` = A，`三站在 Avarua/Aroa/Aitutaki` = B，`Aitutaki 建筑尺寸` = A-social/B。
8. **计数与去重规则**：RFT/RFQ 只证明 `tender published/closed`，除非有 award/completion/operating 证据不得升级为 operational；「Government ITC network / HCI / Microsoft 365 / cloud」默认是 ICT 平台或云迁移，不等于本地数据中心，除非来源明示 colocation、data center、rack、server room 或具体站址；CIG Data Center 记录 division=Cook Islands、island/site 优先 Rarotonga-Avarua，合同未披露托管地点则地址写 `not publicly disclosed`；数据中心记录不得从电站 MW 推导 IT load——Vodafone/OPM 小型托管设施无公开电力数据时 `capacity_it_mw=null`、`power_caveat=small-island grid; no public IT-load evidence`；asset_class 精确：telco-hosting-data-centre、government-data-centre-colocation、government-ict-platform、cable-landing、telco-core、satellite-gateway、cloud-region-absence。

## 常用查询模板

```text
# 政府/采购
site:procurement.gov.ck ("data centre" OR "data center" OR colocation OR "cloud" OR "ICT" OR "hyper-converged" OR HCI)
site:procurement.gov.ck "Office of the Prime Minister" ("data" OR ICT OR cloud OR network)
site:mfem.gov.ck (procurement OR tender OR PPCI) ("data centre" OR "data center" OR ICT OR cloud)
site:pmoffice.gov.ck ("National Digital Strategy" OR "National ICT Policy" OR cybersecurity OR "data centre" OR cloud)
"Cook Islands Government" ("data centre colocation" OR "CIG Data Center" OR "ITC network")
"Cook Islands" "Aiscorp" ("data centre" OR "data center" OR colocation OR "network infrastructure")
# 监管
site:cra.org.ck (telecommunications OR licence OR spectrum OR "frequency band plan" OR "universal access" OR "Telecommunications Act 2019")
"Competition and Regulatory Authority" "Cook Islands" (Vodafone OR Avaroa OR licence OR spectrum)
# 海缆
site:avaroacable.com (Manatua OR "ready for service" OR fault OR repair OR Rarotonga OR Aitutaki)
site:ciic.gov.ck (Avaroa OR Manatua OR cable OR "Crown Enterprise")
"Manatua" ("Rarotonga" OR "Aitutaki" OR "Avarua" OR "Rutaki") ("ready for service" OR RFS OR landed OR repair)
site:submarinenetworks.com Manatua "Cook Islands" ; site:geocables.com Manatua "Cook Islands"
"Avaroa Cable" (Vodafone OR VakaNet OR "wholesale connectivity" OR "domestic connectivity")
# 运营商/托管
site:vodafone.co.ck ("Data Housing" OR Hosting OR "Cloud Services" OR "data centre" OR Aitutaki OR Aroa)
site:vodafone.co.ck/business-cloud-services (hosting OR storage OR backup OR recovery)
"Vodafone Cook Islands" ("data centre" OR "rack space" OR "Data Housing" OR IaaS OR "Aitutaki Data Centre Upgrade")
"Telecom Cook Islands LTD trading as Vodafone Cook Islands" (hosting OR cloud OR "data")
"VakaNet" "Cook Islands" (hosting OR "data centre" OR Manatua)
# 电力
site:teaponga.com (capacity OR MW OR diesel OR solar OR battery OR tariff OR outage OR "Avatiu")
site:adb.org/projects "Cook Islands" "Renewable Energy Sector Project" (solar OR battery OR MW)
"Aitutaki" OR "Mangaia" OR "Atiu" OR "Mauke" OR "Mitiaro" (solar OR battery OR diesel OR microgrid)
# 云/IXP/目录
site:aws.amazon.com/about-aws/global-infrastructure/ "Cook Islands" ; site:learn.microsoft.com/en-us/azure/reliability/regions-list "Cook Islands"
site:cloud.google.com/about/locations "Cook Islands" ; site:oracle.com/cloud/public-cloud-regions/ "Cook Islands"
site:peeringdb.com "Cook Islands" ("Exchange" OR "Facility" OR IXP OR AS10131) ; site:pch.net/ixp "Cook Islands"
"Cook Islands" ("colocation" OR colo OR "data centre") -"Cayman" -"Christmas"
site:datacentermap.com "Cook Islands" ; site:cloudscene.com "Cook Islands" ; site:baxtel.com "Cook Islands" "data center"
# 站点簇
"Rarotonga" OR "Avarua" ("data centre" OR colocation OR "Data Housing" OR hosting OR "server room")
"Aroa" "Cook Islands" "data centre" ; "Aitutaki" "Vodafone" ("data centre" OR hosting OR UPS OR generator)
"Mangaia" OR "Atiu" OR "Mauke" OR "Mitiaro" (Vodafone OR telecom OR internet OR satellite)
"Penrhyn" OR "Manihiki" OR "Pukapuka" OR "Rakahanga" (Vodafone OR telecom OR internet OR satellite)
```

## 官方/监管管线要点（详见 explorer-official.md）

- **PPCI**（procurement.gov.ck）：政府 tender/RFT/RFQ 入口，MFEM 的 Major Projects & Procurement Support Division 管理；已核实高信号：`RFT - Data Centre Colocation`（tender=3374，OPM 2020-11-11 发布，为 CIG Data Center 找 colocation 服务，联系人 OPM ICT Director、地址 Avarua Rarotonga，修订后 2020-12-09 截标——A 级 `government-data-centre-colocation procurement`，状态 tender published/closed）；`Hyper-Converged Infrastructure Implementation & Government ICT Network Upgrade`（tender=3361，OPM 2020-10-23 发布，HCI 与网络设计/实施/迁移/支持——A 级，不单独证明新建 DC）。
- **OPM/MFEM**：OPM 为政府 ICT 主线（National Digital Strategy 2024-2030、Cyber Security Policy、National ICT Policy 2023-2027）；MFEM 页说明 PPCI 管理；Aiscorp 发布稿引用 OPM 2022 新闻稿称 2021-12 已升级 government centralised network and data centre colocation 且 Aiscorp 获 tender——B 级授标/交付线索，尽量回链 OPM/Cook Islands News 原文。
- **CRA**：独立 statutory body，2021-03-01 起电信归其管辖；页下列出 Telecommunications Act 2019 与 CRA Act 2019 下载入口、licensed service providers、universal access、second mobile operator licence、frequency plan；CRA/MFEM/Parliament/Crown Law 法律与监管文件为 A。
- **ACL/Manatua**：Avaroa Cables Limited 为 CK 政府 Crown Corporate Entity（CIIC 建立并任命董事会）；Manatua 3,600 km、two-fiber-pair，RFS 2020-07（Submarine Networks 交叉：六登陆点 Tahiti/Bora Bora/Rarotonga/Aitutaki/Apia/Niue，RFS 2020-07-22）；执行时须确认当前 operational/impaired/under repair 状态，不要把历史「100% operational since 2020」当当前状态。
- **TAU 电力**：Te Aponga Uira 为 Rarotonga 发电与配电主体（teaponga.com 为当前核实域名），CIIC 列为 critical infrastructure asset；外岛为小型混合微网；ADB 可再生能源项目覆盖南组太阳能——电力背景，非 DC 证据。
- 处理规则：RFT/RFQ 只证明 tender published/closed；「Government ITC network / HCI / Microsoft 365 / cloud」默认 ICT 平台非本地 DC；CIG Data Center 的 division=Cook Islands、island/site 优先 Rarotonga-Avarua，托管地点未公开写 not publicly disclosed；Manatua 记录 asset_class=cable-landing，10 Tb/s per fibre pair 仅作 connectivity capacity。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Vodafone Cook Islands / Telecom Cook Islands**：官网 About 列 `ICT & Cloud Services, Data Housing & Hosting`，Business Cloud Services 列 Email/Cloud PABX/Data Storage/Website/backup-recovery——A 级证明托管/云服务存在但未披露机房数量/规格；APAC Outlook 2022 访谈称 Avarua/Aroa/Aitutaki 三个 purpose-built data centres 提供 rack space/IaaS——B 级；Vodafone LinkedIn 称 Aitutaki Data Centre Upgrade（10m×5m 建筑、冗余 UPS、备用发电机、24×7 监控、冗余空调、结构化布线）2021-09 完成——A-social/B，执行时仍应找官网/新闻稿备份。
- **Aiscorp**：2022 发布稿称 2012 年建的旧 ITC 环境在 2021-12 升级 centralised network and data centre colocation 并获 tender——B；托管地点不公开，不能假定在 Vodafone 某站，除非找到合同/OPM 原文。
- **互联/云**：无 hyperscale/cloud region（官方 region pages 未列 CK）；PCH IXP 目录无 CK；PeeringDB AS10131 Telecom Cook Islands 在 Equinix Sydney 公共 peering——境外互联；目录空白不是绝对 absence proof，只能与官方/运营商/采购缺配合用。
- 枚举矩阵：Rarotonga-Avarua/Parekura（商业托管 Avarua DC 线索、CIG colocation、Manatua/Rarotonga、Vodafone HQ/core、O3b——P1）；Aroa/Rutaki/Avatiu（Aroa DC 线索、Manatua landfall/CLS、TAU/Avatiu power——P1）；Aitutaki（Vodafone Aitutaki DC upgrade、Manatua domestic landing——P1/P2）；Southern/Northern Group（Vodafone offices/mobile、satellite/O3b、无 DC 预期——P2/P3 记录负向）；Takutea/Manuae/Palmerston/Suwarrow（P3 no_projects）。
- 诚实结论（2026-08）：CK 非零但小型——Vodafone telco 托管 + CIG 政府 colocation + Manatua 海缆登陆；无 hyperscale/云区域/本地 IXP；电力按 small-island telco/enterprise hosting 处理而非 MW-scale。

## 维护注意（更新纪律）

- **更新节奏**：月度——PPCI/MFEM tenders、OPM ICT/Digital Strategy、CIIC/ACL 公告、Vodafone CK business/cloud 页与 LinkedIn、CRA 公告/裁定；季度——PCH/PeeringDB、DataCenterMap/Cloudscene/Baxtel、AWS/Azure/GCP/OCI 官方 regions、ADB/UN PDEP 文件、commsupdate/DCD/RNZ/Developing Telecoms 扫描；事件驱动——Manatua fault/repair/RFS 状态、Vodafone 所有权/品牌变化、新运营商牌照、CIG data centre colocation award/renewal、Aitutaki/Rarotonga 设施升级、任何云/主权 DC tender。
- **来源核验**：逐一点击 A 级 URL；ACL 当前状态每次 live-check；Aiscorp 线索尽量回链 OPM/Cook Islands News 原文；Vodafone LinkedIn 事实尽量找官网备份；区分 Avaroa（公司）与 Avarua（首都/镇）；区分 Vodafone Group 全球引用与 CK 本地设施。
- **不删除纪律（no-deletion）**：已核实记录不得删除；状态变化改标（tender published/closed → awarded → operational）并保留原始证据链；无支撑条目降级为 C/U 保留而非移除；负向检索（no_projects / cloud-region-absence / IXP absence）须如实记录而非跳过。
