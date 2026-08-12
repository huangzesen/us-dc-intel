# PN Explorer Official — 皮特凯恩群岛数据中心官方口径枚举方法 / Pitcairn Datacenter Enumeration via Official & Regulatory Sources

> 状态日期 / Status date: 2026-08-12  
> 范围 / Scope: Pitcairn（PN，英国海外领地 British Overseas Territory）  
> Manifest: `subnational_type: country`, `divisions: ["Pitcairn"]`  
> 结论 / Working conclusion: **verified negative** — 未发现商业数据中心、托管/colo、云区域、AI/HPC 园区、海底光缆或登陆站。  
> 语言 / Language: 中文为主、双语（Chinese-primary bilingual）。

## 信源可靠性 / Reliability Grades

- **A / 官方一手**：UK FCDO/GOV.UK、Pitcairn Islands Government `government.pn`、Island Council Minutes、Laws of Pitcairn、legislation.gov.uk、IANA `.pn` delegation、AWS/Azure/GCP/OCI 官方区域清单。
- **B / 强二级**：Pitcairn Islands Tourism（政府生态内旅游站）、RNZ、PACNEWS、SubTel Forum、Submarine Networks、DCD、Reuters/The Guardian 等引用具名官员或官方文件的报道。
- **C / 弱信源**：数据中心目录站、SEO 云/colo 营销页、无引用中文文章、论坛、社交媒体、BGP/监控页。C 级只作线索，不作计数依据。

## 0. 官方结论 / Official Baseline

PN 在本 repo 中只有一个 division：`Pitcairn`。所有官方枚举按全国单一市场处理；可归属线索填 `division: Pitcairn`，无法定位但明确属于 PN 的线索填 `Unknown PN`。

截至 2026-08-12，官方和准官方表面支持负向结论：

- `government.pn` 官方门户显示 PN 人口约 50，主岛约 3.2 km x 1.6 km，首府 Adamstown 位于 Bounty Bay 上方；站点公开政府、移民、法律、Island Council Minutes、财政信息和公告，但未见数据中心、colo、云区域、AI/HPC 或大型 ICT 园区公告。
- FCDO 的 Pitcairn 页面说明英国政府在 PN 的外交/领地事务由新西兰方向远程治理，岛上有 Governor's Representative；GOV.UK 服务页还说明 PN 没有英国使领馆。
- `government.pn/laws` 说明 Pitcairn 法律由 Governor 制定的 ordinances、适用于 PN 的英国立法/Order in Council，以及在当地条件允许范围内适用的普通法组成；这意味着任何大型设施、土地、电信或公用事业事项都应能在政府/法律/会议记录表面留下痕迹。
- IANA `.pn` delegation 显示 ccTLD manager 是 Pitcairn Island Administration，技术/注册服务由 Nominet 相关联系人和 `nic.pn` 承接；域名注册或 DNS 服务不等于本地数据中心。
- Pitcairn Islands Tourism 2022-11-23/28 发布的 Starlink 报道说明 Starlink 终端运到 Adamstown 并已运行，用于改善此前慢且不稳定的卫星互联网；这是连接服务，不是本地 DC。
- AWS、Azure、Google Cloud、Oracle OCI 官方区域清单均未列出 Pitcairn 区域；Google Cloud 页面显示 43 个 regions / 130 zones，AWS/Azure/OCI 表格列出的区域地理位置不含 PN。

## 1. 官方表面 / Official Source Register

### 1.1 UK FCDO / GOV.UK（Grade A）

- `https://www.gov.uk/world/pitcairn-island`
  - 用途：英国面向 PN 的服务、旅行、生活、领事和业务入口。
  - 核验点：页面说明 British High Commission Wellington 是相关英国驻外机构，且 PN 无英国使领馆；作为治理和负向项目搜索入口。
- `https://www.gov.uk/world/pitcairn-island/news`
  - 用途：FCDO/Pitcairn 官方新闻、Overseas Territories 公报、项目公告。
  - 核验点：页面说明 PN 从新西兰远程治理，岛上有 Governor's Representative；未见 DC 或大型 ICT 项目公告。
- `https://www.gov.uk/government/organisations/foreign-commonwealth-development-office`
  - 用途：FCDO 组织入口和站内检索入口。

### 1.2 Pitcairn Islands Government / Island Council（Grade A）

- `https://www.government.pn/`
  - 用途：PN 官方门户；人口、岛屿基础信息、公告、媒体访问审批、移民和政府链接。
  - 核验点：首屏写明人口 only around fifty；媒体访问需先向 Mayor and Island Council 提交 request letter。任何 DC 选址、建设、媒体/商业访问或大型基建均应从该表面可追踪。
- `https://www.government.pn/government/island-council-minutes`
  - 用途：Island Council Minutes，当前公开到 2026/2025/2024 等年份。
  - 核验点：查 `internet`, `Starlink`, `telecom`, `ICT`, `server`, `data centre`, `generator`, `solar`, `power`；政府电脑房或电信机柜只记 lead，不计商业 DC。
- `https://www.government.pn/laws`
  - 用途：Laws of Pitcairn、ordinances 和 UK Orders in Council 链接。
  - 核验点：电信、电力、土地、移民、数据保护/隐私；没有公开 DC 专门审批或激励表面。
- `https://www.government.pn/government/financial-information`
  - 用途：财政信息和账户；可用于确认政府支出规模与是否存在大型 ICT/基建资本项目。

### 1.3 法律、域名与注册 / Legal, Domain and Registry（Grade A）

- Pitcairn Constitution Order 2010: `https://www.legislation.gov.uk/uksi/2010/244/contents`
  - 用途：宪制框架、Governor 和本地机构权限。
- IANA `.pn`: `https://www.iana.org/domains/root/db/pn.html`
  - 用途：确认 `.pn` ccTLD manager；避免把注册机构、DNS、Nominet 技术联系人误判为 PN 本地 DC。
- `https://nic.pn`
  - 用途：`.pn` 注册服务入口；只作域名业务背景。

### 1.4 电信与互联网 / Telecom and Internet（Grade A/B）

- `government.pn` 政府公告、Island Council Minutes、Pitcairn Miscellany/旅游站文章是电信事实的优先核验面。
- Pitcairn Telecom / telecom 相关站点如可访问，检查电话、互联网、卫星、Starlink、资费、服务说明。
- Starlink 终端、VSAT、卫星电话、无线中继、政府网络设备均记为 `telecom facility lead` 或 `government ICT lead`；只有公开销售 rack/colo/hosting 且有设施证据时，才升级为 DC 候选。

### 1.5 电力与物流 / Power and Logistics（Grade A/B）

- PN 没有可支撑商业 DC 市场的公开电力公司表面。电力资料以 `government.pn` 公告、Island Council Minutes、FCDO 项目文件和可信媒体为主。
- 岛内供电按村社级柴油/太阳能微电网处理。任何 kW 级政府设备可作为背景；任何 MW 级 IT load 声称必须有 A 级项目文件、供电方案和物流证据。
- PN 无机场或深水货运港；到岛货物依赖补给船和长艇转运。重型发电机、冷却设备、机架批量交付和备件 SLA 均不符合商业 DC 条件。

## 2. 官方查询模板 / Official Query Templates

GOV.UK / FCDO:

```text
site:gov.uk Pitcairn ("data centre" OR "data center" OR datacenter OR server OR ICT OR telecom OR Starlink)
site:gov.uk Pitcairn (electricity OR power OR renewable OR solar OR generator)
site:gov.uk "Pitcairn Island" ("Governor" OR "Island Council" OR "Governor's Representative")
site:gov.uk "Pitcairn Constitution Order" OR "Pitcairn" "Overseas Territories"
```

Pitcairn Government:

```text
site:government.pn ("data centre" OR "data center" OR datacenter OR server OR hosting OR ICT OR Starlink OR satellite)
site:government.pn (electricity OR power OR generator OR solar OR battery OR renewable)
site:government.pn ("Island Council" OR mayor OR magistrate OR administration OR governor)
site:government.pn ("Pitcairn Telecom" OR telecom OR telephone OR internet)
```

法律、域名、注册：

```text
site:government.pn/laws Pitcairn (telecommunications OR electricity OR "data protection" OR privacy OR land)
site:legislation.gov.uk Pitcairn (telecommunications OR electricity OR "data protection" OR privacy)
site:iana.org/domains/root/db pn
site:nic.pn Pitcairn
```

负向清扫：

```text
"Pitcairn" ("data centre" OR "data center" OR datacenter OR colocation OR "server farm") -tourism -cruise
"Pitcairn" ("cable landing" OR submarine OR fibre OR fiber OR IXP)
"Pitcairn" (AWS OR Azure OR "Google Cloud" OR Oracle OR OCI OR "cloud region")
"Pitcairn" (AI OR GPU OR supercomputer OR HPC OR bitcoin OR mining)
"皮特凯恩" (数据中心 OR 云 OR 算力 OR 区块链 OR 加密货币 OR 海底光缆 OR 卫星互联网)
```

## 3. Division 枚举策略 / Per-Division Official Strategy

| Repo division | 优先级 | 官方枚举策略 | 计数规则 |
|---|---:|---|---|
| Pitcairn | 1 | 全国统一处理：`government.pn` 门户、Island Council Minutes、Laws、FCDO/GOV.UK、IANA、官方云区域清单。所有 PN 线索落到 `Pitcairn` 或 `Unknown PN`。 | 只有 A 级信源明确点名本地数据中心、托管设施、云区域或大型 ICT 项目，且说明功能/业主/地点时才计数。卫星终端、`.pn` 注册、政府电脑房、学校/电信机柜不计 DC。 |

## 4. 候选处理 / Candidate Handling

最小验证标准：

- 至少 1 个 A 级信源点名设施/项目、功能和 PN 内位置；或
- 运营商/政府官方页 + 1 个独立 A/B 级信源，且二者描述同一设施；并且
- 若声称地址、坐标、容量或 IT load，必须有明确来源。

候选字段：

```text
country_code: PN
division: Pitcairn | Unknown PN
facility_or_project_name:
operator_or_owner: Pitcairn Island Administration | Pitcairn Telecom | FCDO/donor | other
consent_or_authorisation: Island Council/Governor approval | ordinance/licence | not found
site_address:
coordinates:
status: operational | planned | lead | verified-negative
facility_type: government ICT/server room | telecom/satellite facility | power facility | colocation | cloud-region | AI/HPC | other
it_load_mw:
power_connection: village diesel/solar microgrid | unknown
connectivity: Starlink/satellite | no known submarine cable | unknown
evidence_grade: A | B | C
primary_urls:
source_documents:
notes:
last_checked: 2026-08-12
```

## 5. Verified Negatives / 已验证负项

- **商业 DC / colo**：未发现 PN 运营商、地址、许可、招聘、建设或客户公告。目录站出现的 Pitcairn 条目只当 C 级销售线索。
- **云区域**：AWS、Azure、Google Cloud、OCI 官方区域表均不含 Pitcairn。
- **海底光缆/登陆站**：Telegeography/Submarine Cable Map 和公开搜索未发现 PN landing point；Pacific cable 新闻若提到 PN，通常是远期连接可能性或区域政策背景，未构成登陆站。
- **Starlink/卫星**：2022 年 Starlink 试验/上线改善互联网；终端和卫星链路不是 DC。
- **`.pn`/DNS**：IANA 记录证明 ccTLD 管理，不证明本地服务器或机房。
- **政府 ICT**：即使发现政府服务器、视频庭审、办公网络、学校设备，也只记 `government ICT lead`，除非有托管服务和设施规格。

## 6. 检查者核验清单 / Checker Checklist

1. Manifest 行确认 `country_code: PN`, `divisions: ["Pitcairn"]`。
2. `government.pn` 门户、Notices、Island Council Minutes 搜索 DC/colo/server/ICT/telecom/Starlink/power 关键词。
3. GOV.UK Pitcairn world/news 页面搜索 DC、ICT、电力、Overseas Territories 项目公告。
4. `government.pn/laws` 与 legislation.gov.uk 搜索电信、电力、土地、数据保护/隐私 ordinances。
5. IANA `.pn` 页面确认 ccTLD manager，避免域名误报。
6. Starlink/卫星报道仅作为连接背景；不要把 terminal、dish、satellite network 写成 DC。
7. AWS/Azure/GCP/OCI 官方区域清单逐一检查，无 PN 才能保留 cloud-region verified negative。
8. 任何未来正向候选必须同时通过：A/B 级证据、PN 内位置、设施功能、供电/连接合理性。
