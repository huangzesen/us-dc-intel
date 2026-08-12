# HM Explorer Industry — 赫德岛和麦克唐纳群岛数据中心行业管线枚举方法（行业 / 运营商 / 基础设施管线）

> 日期：2026-08-12。范围：赫德岛和麦克唐纳群岛（Heard Island and McDonald Islands，ISO 3166-1: **HM** / HMD / 334）。
> 划分模型（Division model）：**单一 division（subnational_type: country）** — `Heard Island and McDonald Islands`。
> 角度：**行业 / 运营商 / 基础设施管线（industry / operator / infrastructure pipeline）**。
> 语言：中文为主、双语（Chinese-primary bilingual），关键英文术语保留原词。

## 0. 行业结论（Market Reality）

HM 的行业侧枚举结论为 **verified-negative**：没有商业数据中心市场，也没有可作为数据中心候选的运营商、园区、电力或网络基础设施。

判断依据：

- manifest 中 HM 只有一个 division：`Heard Island and McDonald Islands`；行业枚举不再拆分岛屿或营地点。
- AAD 官方页面确认 HM 由 Australian Antarctic Division 管理、无人居住，且人类活动极少。
- AAD Human activities 页面将现有人类活动限定为科研/管理、少量私人访问、监视执法和 HIMI Fishery；历史 Atlas Cove 研究站只在 1947-1955 年运行。
- UNESCO 将 HM 描述为高度原始、低人类扰动的世界遗产区域，由 AAD 按 strict nature reserve 管理。
- `.hm` ccTLD 已委派且 registry.hm 显示开放注册；这是域名服务，不代表 HM 本地存在 ISP、机房或 cloud edge。
- 数据中心行业搜索未发现 HM 商业设施；命中主要是 AADC 科学数据仓库、全球市场报告国家下拉列表、McDonald’s 品牌、AAT 南极站或通用数据中心内容。

## 1. 行业可靠性分级（Industry Evidence Grades）

- **A 级**：运营方/官方一手来源：AAD、DCCEEW、AFMA、ACMA、IANA/registry.hm、ITU、AWS/Azure/Google Cloud/Oracle 官方区域清单、具名运营商公告。
- **B 级**：权威行业/科学参考：UNESCO、CCAMLR、SCAR、Submarine Cable Map / TeleGeography / SubTel Forum、APNIC/PeeringDB/BGP 工具、引用官方文件的主流媒体。
- **C 级**：数据中心目录站、SEO 市场报告、供应商国家选择列表、社交媒体、未引用来源的文章。C 级只作为 false-positive 或 lead，不计数。

## 2. 行业来源（Industry Surfaces）

### 2.1 数据中心与云（Data Centers / Cloud）

优先复核官方云区域清单：

- AWS Regions: `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html`
- Azure regions: `https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- Google Cloud locations: `https://cloud.google.com/about/locations`
- Oracle OCI regions: `https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm`

计数纪律：官方清单没有 HM region / zone / edge location；澳大利亚 mainland region（Sydney、Melbourne、Canberra 等）不得归入 HM。

目录站（Data Center Map、Cloudscene、Baxtel、datacenters.com）只作为 C 级线索。若出现 HM 国家页、空列表或表单国家选项，记录为 “directory placeholder”，不得计数。

### 2.2 网络、海缆与电信（Network / Cable / Telecom）

- 海缆：复核 Submarine Cable Map、TeleGeography、SubTel Forum；预期无 HM cable landing station。
- 运营商：复核 ACMA Register of Radiocommunications Licences、APNIC WHOIS、PeeringDB、BGP 工具；预期无 HM 本地 carrier、IXP、ASN 或 fixed ISP。
- 移动网络：预期无 HM 专属 MCC/MNC 和陆上 PLMN。卫星/海事/航空国际 MCC 不代表 HM 本地移动网络。
- 卫星通信：Iridium、Inmarsat、Starlink 等只能作为科考/船舶/应急通信背景；终端可用性不是数据中心设施证据。

### 2.3 渔业、船舶与科考（Fishery / Vessels / Research）

- AFMA HIMI Fishery 和 CCAMLR 是行业侧最可能出现实体名称的来源。
- 持牌渔船的卫星通信、冷藏、加工、导航、船载 IT 均不计为陆上数据中心。
- AAD 科考营地、自动气象站、海平面站、遥测设备、发电机和临时卫星终端可记录为 non-DC infrastructure lead，但默认不计数。

## 3. 查询模板（Industry Query Templates）

主机托管 / 云 / AI：

```text
"Heard Island" OR "McDonald Islands" (datacenter OR "data center" OR "data centre" OR colocation OR "rack space" OR hosting)
"Heard Island and McDonald Islands" (AWS OR Azure OR "Google Cloud" OR Oracle OR "cloud region" OR "edge location")
"Heard Island" OR "McDonald Islands" (GPU OR AI OR HPC OR supercomputer) (facility OR data)
site:datacenterdynamics.com "Heard Island" OR "McDonald Islands"
site:datacentermap.com "Heard Island" OR "McDonald Islands"
site:baxtel.com "Heard Island" OR "McDonald Islands"
```

海缆 / 网络：

```text
"Heard Island" OR "McDonald Islands" ("submarine cable" OR "cable landing" OR "landing station")
submarinecablemap "Heard Island" OR "McDonald Islands"
"Heard Island" OR "McDonald Islands" (ISP OR carrier OR ASN OR IXP OR "internet exchange")
site:peeringdb.com "Heard Island" OR "McDonald Islands"
site:bgp.tools "Heard Island" OR "McDonald Islands"
```

科考 / 船舶 / 后勤：

```text
"Heard Island" ("Atlas Cove" OR "Spit Bay" OR "Magnet Point") (camp OR satellite OR generator OR power OR station)
"Heard Island and McDonald Islands Fishery" (vessel OR communications OR licence)
"Heard Island" (Iridium OR Inmarsat OR Starlink OR VSAT OR HF) (expedition OR camp OR vessel)
```

中文 / 谣言监控：

```text
"赫德岛" OR "麦克唐纳群岛" ("数据中心" OR "云" OR "算力" OR "海底光缆" OR "AI")
"赫德岛" OR "麦克唐纳群岛" 数据中心 -"麦当劳"
"赫德岛和麦克唐纳群岛" ("服务器" OR "主机托管" OR "云区域")
```

## 4. 逐分区行业策略（Per-Division Industry Strategy）

| Repo division | 优先级 | 行业检索角度 | 升级条件 |
|---|---:|---|---|
| Heard Island and McDonald Islands | High | 云区域阴性对照；海缆阴性对照；ACMA/APNIC/PeeringDB/BGP 无本地实体；渔业/科考设备排除；目录站占位排除 | 只有 A 级运营方或政府来源点名商业设施/项目，并给出名称、功能、位置、运营方时才计数 |

亚区只做标签，不做 division：

- **Atlas Cove**：历史研究站/科考点。1947-1955 历史站点不计；当前短期营地设备不计。
- **Spit Bay / Magnet Point / Heard Island 其他点位**：科考和仪器点位；默认 non-DC lead。
- **McDonald Islands / Shag Islet / Morgan Island / Sail Rock**：无人岛礁；预期无行业实体。
- **HIMI Marine Reserve / surrounding waters**：渔业和巡查；船载设备不计。

## 5. 候选字段（Required Fields per Candidate）

本领地预期没有设施记录。若发现异常候选，按以下字段记录并先置为 `lead` 或 `rejected_false_positive`：

```text
country_code: HM
division: Heard Island and McDonald Islands | Unknown HM
facility_or_project_name:
operator:
facility_type:
status: lead | rejected_false_positive | verified-negative
capacity_or_scale:
evidence_grade:
primary_urls:
secondary_urls:
connectivity:
power:
site_address:
coordinates:
last_checked: 2026-08-12
notes:
```

最小计数标准：

- A 级来源点名商业数据中心、云区域、edge node、carrier hotel、IXP、海缆登陆站或同等设施；
- 具备位置、运营方、设施功能三个要素；
- 能排除 AADC、AAT、Kerguelen、McDonald’s、目录占位、卫星终端、船载系统、临时科考设备；
- 对 MW 级声明必须有电力接入、许可或项目建设证据。

## 6. 假阳性清单（False Positives）

1. **Australian Antarctic Data Centre（AADC）**：科学数据仓库/地图数据服务，不是 HM 岛上机房。
2. **`.hm` 域名注册**：IANA/registry.hm 只证明 ccTLD 委派和开放注册，不证明本地互联网基础设施。
3. **AAT 南极站**：Mawson、Davis、Casey、Wilkins 等不得归入 HM。
4. **Mawson Peak / Mawson Station 混淆**：HM 的 Mawson Peak 是山峰，不是南极站。
5. **McDonald’s 品牌**：与 McDonald Islands 无关。
6. **Kerguelen 设施**：法国基地和附近海域活动不得归入 HM。
7. **渔业船载设备**：HIMI Fishery 船舶设备不是陆上设施。
8. **卫星通信报道**：Iridium/Inmarsat/Starlink 终端或覆盖不是 cloud edge 或数据中心。
9. **市场报告国家列表**：把 HM 放在国家下拉或统计表中不是市场存在证据。

## 7. 每轮行业复核清单（Checker Checklist）

1. 确认 manifest HM division 未变化。
2. 复核 AAD 页面，确认无人居住、AAD 管理、短期科考/渔业/监督活动边界未变化。
3. 搜索数据中心目录和行业媒体；记录并排除空页、国家列表和通用市场报告。
4. 复核 AWS / Azure / Google Cloud / Oracle 官方区域清单，确认无 HM。
5. 复核 Submarine Cable Map / TeleGeography / SubTel Forum，确认无 HM landing station。
6. 复核 ACMA / APNIC / PeeringDB / BGP 工具，确认无 HM 本地 carrier、IXP、ASN 或 commercial ISP。
7. 对所有 “data centre / data center / 数据中心” 命中先检查是否为 AADC 或科学数据引用。
8. 若出现新建设、能源、通信或海缆声明，要求 A 级来源和位置证据后再升级。

## 8. 已验证阴性（Verified Negatives，截至 2026-08-12）

- **商业数据中心 / colocation / hosting**：无。
- **公有云 region / zone / edge location**：无。
- **海底光缆 / cable landing station**：无。
- **本地 carrier / ISP / IXP / ASN**：无可计数实体。
- **移动网络 / 专属 MCC/MNC / 陆上 PLMN**：无。
- **超大规模 / AI / HPC 设施**：无。
- **公共电网 / 大型电力项目**：无。
- **行业设施清单预期**：空表；输出 verified-negative。
