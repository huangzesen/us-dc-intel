# PN Explorer Industry — 皮特凯恩群岛数据中心产业口径枚举方法 / Pitcairn Datacenter Enumeration via Industry, Operator & Infrastructure Sources

> 状态日期 / Status date: 2026-08-12  
> 范围 / Scope: Pitcairn（PN，英国海外领地 British Overseas Territory）  
> Manifest: `subnational_type: country`, `divisions: ["Pitcairn"]`  
> 结论 / Working conclusion: **verified negative** — 未发现商业数据中心、colo、云区域、AI/HPC、IXP、海底光缆或登陆站市场。  
> 语言 / Language: 中文为主、双语（Chinese-primary bilingual）。

## 信源可靠性 / Reliability Grades

- **A / 官方或运营商一手**：Pitcairn Islands Government、Island Council Minutes、Pitcairn Telecom/telecom 官方页面、UK FCDO、Starlink 官方覆盖资料、AWS/Azure/GCP/OCI 官方区域清单、IANA、Telegeography/Submarine Cable Map。
- **B / 强二级产业信源**：RNZ、PACNEWS、SubTel Forum、Submarine Networks、DCD、Reuters/The Guardian、卫星行业媒体；只有引用官方或具名运营商时才可增强信心。
- **C / 弱线索**：Data Center Map、Cloud Infrastructure Map、SEO 目录、供应商国家下拉框、营销文章、社交媒体、论坛、无引用中文内容。C 级不得单独计数。

## 0. 市场现实 / Market Reality

PN 是极小型、极偏远、单一定居岛市场。Repo manifest 只有一个 division：`Pitcairn`。产业枚举不做省州/城市拆分；Adamstown 线索归 `Pitcairn`，无法定位但明确属于 PN 的线索归 `Unknown PN`。

截至 2026-08-12，产业侧结论为 verified negative：

- **无商业 DC/colo 市场**：公开搜索只发现目录/营销型泛页面，没有 PN 内运营商、设施名称、地址、机架产品、客户案例或建设公告。
- **无云区域**：AWS、Azure、Google Cloud、OCI 官方区域清单均未列出 Pitcairn。
- **无海底光缆/登陆站**：Telegeography/Submarine Cable Map 和公开海缆新闻未显示 PN landing point。涉及 PN 的区域海缆讨论只作为远期连接背景，不构成已建设施。
- **连接以卫星/Starlink 为核心**：2022 年 Pitcairn Islands Tourism 转发/发布的 Starlink 报道称终端运抵 Adamstown、岛民可使用 Starlink，高速互联网改善了此前慢且不稳定的卫星连接。Starlink terminal、VSAT、卫星电话和地面通信设备是 connectivity，不是 data center。
- **供电和物流不支持商业 DC**：岛内为村社级柴油/太阳能供电；无机场、无深水货港，货物依赖补给船和长艇转运。多机架 colo、MW 级负载或 AI/HPC 园区声称必须视为异常，需 A 级证据。

## 1. 产业信源 / Industry Source Register

### 1.1 Pitcairn Telecom / Local Telecom（Grade A/B）

- 优先入口：`government.pn` 的 telecom、notices、Island Council Minutes、Pitcairn Miscellany/旅游站文章，以及可访问的 Pitcairn Telecom 页面。
- 核验目标：
  - 当前电话/互联网服务清单；
  - Starlink/VSAT/卫星链路状态；
  - 是否存在 `hosting`, `server`, `rack`, `colo`, `colocation`, `data centre/data center` 产品。
- 处理规则：运营商机柜、地面站、电源柜、Starlink terminal = `telecom facility lead`；只有公开销售托管/机架/colo 且有设施证据，才可升级为 DC 候选。

### 1.2 Starlink and Satellite（Grade A/B）

- Starlink: `https://www.starlink.com/map`
  - 用途：覆盖/可用性背景；覆盖不等于本地设施。
- Pitcairn Islands Tourism Starlink article:
  - 用途：2022 年 Starlink 试验/上线的具名本地佐证；报道引用 Deputy Governor Alasdair Hamilton，说明此前互联网慢且不稳定，Starlink 是改善连接的步骤。
- 其他卫星背景：Kacific、O3b/SES、Inmarsat、海事卫星电话等只作历史或备援背景。

### 1.3 海底光缆与网络地图 / Subsea and Network Maps（Grade A/B）

- Telegeography / Submarine Cable Map: `https://www.submarinecablemap.com/`
  - 用途：核验 PN 无 cable landing station。
- Submarine Networks: `https://www.submarinenetworks.com/`
  - 用途：太平洋海缆新闻背景；任何 PN landing claim 必须有项目方或政府公告。
- Internet exchange / peering:
  - 搜索 `Pitcairn IXP`, `Adamstown IXP`, `Pitcairn peering`, `Pitcairn AS`。
  - 预期：无本地 IXP；卫星接入和家庭终端不构成中立互联点。

### 1.4 云与边缘 / Cloud and Edge（Grade A）

官方区域清单是唯一可计数的 cloud-region 依据：

- AWS Regions: `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html`
- Azure regions: `https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- Google Cloud locations: `https://cloud.google.com/about/locations`
- Oracle OCI regions: `https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm`

处理规则：

- 官方区域清单无 PN，即 `cloud-region: verified-negative`。
- 供应商国家下拉框、可从 PN 购买云服务、CDN 全球服务、SaaS 可用性、Oracle/Google/Microsoft 服务可用国家映射，都不等于 PN 本地云区域。
- Edge、PoP、CDN cache 也必须有设施地址或官方 PoP 名称；仅有网络可达性不计数。

### 1.5 目录站与市场报告 / Directories and Market Reports（Grade C）

- Data Center Map / Cloud Infrastructure Map / generic procurement pages:
  - 若只有 "Pitcairn Islands quotes"、国家选择器或空白国家页，标记 `false_positive_directory`.
  - 不得由目录页自动生成设施、容量或城市。
- 供应商页面包含 Pitcairn 多数是国家下拉框、联系电话国家码或全球可服务列表；这不是设施证据。

### 1.6 太平洋媒体 / Pacific Media（Grade B）

使用目的：补充 Starlink、卫星互联网、电力、补给船、治理和人口背景。

```text
site:rnz.co.nz Pitcairn (Starlink OR internet OR telecom OR power OR solar)
site:pacnews.com Pitcairn (internet OR telecom OR satellite OR power)
site:submarinenetworks.com Pitcairn (cable OR submarine OR landing)
site:datacenterdynamics.com Pitcairn ("data center" OR "data centre" OR cloud)
site:theguardian.com Pitcairn (internet OR Starlink OR telecom)
```

## 2. 产业查询模板 / Industry Query Templates

运营商与本地设施：

```text
"Pitcairn Telecom" ("data centre" OR "data center" OR datacenter OR hosting OR racks OR colocation)
"Pitcairn Telecom" (Starlink OR satellite OR VSAT OR internet OR telephone)
site:government.pn ("Pitcairn Telecom" OR telecom OR internet OR Starlink OR satellite)
site:government.pn ("hosting" OR "server room" OR "data centre" OR "data center" OR colocation)
```

卫星与连接：

```text
"Pitcairn" Starlink (terminal OR install OR launch OR internet OR service OR coverage)
"Pitcairn Islands" satellite internet (Starlink OR Kacific OR O3b OR Inmarsat OR VSAT)
site:starlink.com Pitcairn
```

海缆、IXP、网络：

```text
"Pitcairn" ("submarine cable" OR "cable landing" OR "landing station" OR fibre OR fiber)
"Pitcairn" ("internet exchange" OR IXP OR peering OR "carrier hotel")
"Adamstown" Pitcairn (telecom OR internet OR satellite OR server OR power)
```

云、colo、AI/HPC 负向：

```text
"Pitcairn" (colocation OR colo OR "rack space" OR hosting OR "server farm")
"Pitcairn" ("data centre" OR "data center" OR datacenter) -tourism -cruise
"Pitcairn" (AWS OR Azure OR "Google Cloud" OR Oracle OR OCI OR "cloud region" OR "edge location")
"Pitcairn" (GPU OR AI OR "artificial intelligence" OR HPC OR supercomputer OR bitcoin OR mining)
```

中文监控：

```text
"皮特凯恩" (数据中心 OR 云区域 OR 算力 OR 托管 OR 机房 OR 海底光缆 OR 卫星互联网)
"Pitcairn" ("data centre" OR "data center" OR cloud OR ICT) (China OR Chinese OR Huawei OR satellite)
```

## 3. Division 产业策略 / Per-Division Industry Strategy

| Repo division | 优先级 | 产业枚举策略 | 计数规则 |
|---|---:|---|---|
| Pitcairn | 1 | 全国统一处理：本地电信/Starlink 表面 -> 海缆和 IXP 负向 -> 云区域负向 -> DC/colo/AI 目录清扫 -> 政府侧交叉。 | 只有 A 级或 A+B 证据确认 PN 内设施、业主、功能、地点时计数。Starlink/VSAT、`.pn`、政府电脑房、目录国家页不计 DC。 |

## 4. 候选字段 / Required Candidate Fields

```text
country_code: PN
division: Pitcairn | Unknown PN
facility_or_project_name:
operator: Pitcairn Telecom | Pitcairn Island Administration | Starlink/SpaceX | FCDO/donor | other
facility_type: telecom/satellite facility | government ICT/server room | power facility | colocation | cloud-region | AI/HPC | IXP | other
status: operational | planned | lead | verified-negative
capacity_or_scale: terminal count / bandwidth / racks / MW / unknown
it_load_mw:
evidence_grade: A | B | C
primary_urls:
secondary_urls:
connectivity: Starlink/satellite | no known submarine cable | unknown
power: village diesel/solar microgrid | unknown
site_address:
coordinates:
notes:
last_checked: 2026-08-12
```

最小计数标准 / Minimum counting standard:

- 1 个 A 级信源明确点名设施或项目；或运营商/政府一手页 + 独立 A/B 级佐证；
- 设施必须在 PN 内，有明确功能和位置；
- 容量、机架数、MW、坐标不得推断；无来源则填 `unknown`；
- 对 `cloud-region`, `colo`, `AI/HPC`, `IXP`, `submarine landing` 的正向判断必须高于一般政府 ICT lead 标准。

## 5. 已验证负项与误报 / Verified Negatives and False Positives

- **Commercial colocation**：未发现 PN colo provider、facility address、rack product、SLA 或客户案例。
- **Cloud region**：AWS/Azure/GCP/OCI 官方区域清单无 Pitcairn。
- **Submarine cable / landing station**：Telegeography/Submarine Cable Map 与公开海缆新闻未显示 PN landing point。
- **IXP / carrier hotel**：未发现 PN 本地 IXP、中立机房或 carrier hotel。
- **Starlink / VSAT / satellite**：连接服务，不是数据中心。即使每户/政府建筑有终端，也只代表 access network。
- **`.pn` registry / DNS**：IANA 显示 ccTLD manager 和 Nominet 技术/注册联系人；DNS/name server 不等于 PN 本地机房。
- **Directory pages**：Data Center Map 等可能生成国家页或采购询价页；无设施名称和运营商时一律 C 级误报。
- **Crypto / AI / HPC marketing**：无 A 级政府或项目文件时忽略。
- **Tourism, shipping, research centre**：旅游、补给船、科研访问设施不是 DC；如研究中心有网络设备，只记非商业 ICT lead。

## 6. 推荐扫查顺序 / Recommended Sweep Order

1. 读取 manifest PN 行，确认单 division `Pitcairn`。
2. 查 `government.pn` 与 Island Council Minutes：`Starlink`, `internet`, `telecom`, `server`, `data centre`, `power`, `solar`, `generator`。
3. 查 Pitcairn Telecom/telecom 官方页面：确认服务清单中是否有 hosting/rack/colo。
4. 查 Starlink 官方覆盖和 2022 Starlink 本地报道：只记录 connectivity 背景。
5. 查 Telegeography/Submarine Cable Map 与 Submarine Networks：确认无 landing station。
6. 查 AWS/Azure/GCP/OCI 官方区域清单：确认无 PN region。
7. 查 RNZ/PACNEWS/DCD/SubTel Forum：只采纳引用官方或具名运营商的电信/电力/基建事实。
8. 查 Data Center Map、Cloud Infrastructure Map、SEO 目录和中文结果：标记误报，不从空白国家页生成候选。
9. 任何正向候选都回到 `explorer-official.md` 做政府、法律、Island Council、供电与物流交叉验证。
