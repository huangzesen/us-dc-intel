# HM Explorer Official — 赫德岛和麦克唐纳群岛数据中心官方管线枚举方法（官方 / 监管 / 政府管线）

> 日期：2026-08-12。范围：赫德岛和麦克唐纳群岛（Heard Island and McDonald Islands，ISO 3166-1: **HM** / HMD / 334）。
> 划分模型（Division model）：**单一 division（subnational_type: country）** — `Heard Island and McDonald Islands`。
> 角度：**官方 / 监管 / 政府管线（official / regulatory / government pipeline）**。
> 语言：中文为主、双语（Chinese-primary bilingual），关键英文术语保留原词。

## 0. 已核验结论（Verified Conclusion）

HM 的官方枚举结论为 **verified-negative**：截至本次复核，没有可计数的商业数据中心、政府数据中心、公有云区域、海缆登陆站、本地电信运营商设施或大型电力基础设施。

官方基础事实：

- `world-manifest.jsonl` 已包含 HM：`{"country_code":"HM","country_name":"Heard Island and McDonald Islands","subnational_type":"country","divisions":["Heard Island and McDonald Islands"]}`。因此本 repo 只枚举一个 division。
- 澳大利亚南极局（Australian Antarctic Division, **AAD**）官方页面说明 HM 是澳大利亚外部领地，享有世界遗产和海洋保护区地位，由 AAD 管理，并且 “unoccupied by humans”。AAD 还记录 2025-10 之后的短期科考访问。
- AAD “Human activities” 页面说明，HM 人类活动受极端隔绝、恶劣天气和海况限制；自 1855 年以来 Heard Island 只有约 240 次 shore-based visits，McDonald Island 只有 1971 和 1980 两次登陆；岛上活动主要是科研、管理、监督和少量受许可访问。
- AAD 记录 ANARE/AAD 曾在 Atlas Cove 运行研究站（1947-1955），但该站已属历史设施；后续为短期科考/管理访问，不是常设商业或政府 IT 设施。
- UNESCO 世界遗产条目确认 HM 位于 Perth 西南约 4,100 km、南极洲以北约 1,700 km，具有极高 wilderness quality，并由 AAD 按 strict nature reserve / IUCN Category 1a 逻辑管理。
- IANA `.HM` 委派记录最新更新时间为 2026-08-04，ccTLD 管理人为 HM Domain Registry；registry.hm 页面显示 `.HM` 可注册。域名开放注册只说明命名资源存在，**不是**本地网络、机房或市场证据。

## 1. 可靠性分级（Reliability Grades）

- **A 级**：官方 / 一手来源：`antarctica.gov.au`（AAD）、`dcceew.gov.au`、`legislation.gov.au`、`afma.gov.au`、`acma.gov.au`、IANA、ITU、云厂商官方区域清单。
- **B 级**：权威二级来源：UNESCO、SCAR、CCAMLR、Geoscience Australia、BoM、Submarine Cable Map / TeleGeography、引用官方材料的主流媒体或科学机构。
- **C 级**：弱来源：数据中心目录站、SEO 市场报告、社交媒体、未引用来源的中英文文章、BGP/网络聚合器。C 级只能作为线索，不能计数。

## 2. 官方来源登记册（Official Source Register）

| 表面 | URL | 用途 | 分级 |
|---|---|---|---|
| AAD HM 主页面 | `https://www.antarctica.gov.au/antarctic-operations/stations-and-field-locations/heard-island/` | 确认 AAD 管理、无人居住、最新科考访问 | A |
| AAD Human activities | `https://www.antarctica.gov.au/antarctic-operations/stations-and-field-locations/heard-island/human-activities/` | 确认访问稀少、历史 Atlas Cove 研究站、科研/渔业/监督活动边界 | A |
| AAD Location and geography | `https://www.antarctica.gov.au/antarctic-operations/stations-and-field-locations/heard-island/location-geography/` | 确认位置、距离、HIMI Marine Reserve、AADC 地图链接 | A |
| DCCEEW / EPBC | `https://www.dcceew.gov.au/`、`https://www.legislation.gov.au/` | 环境保护、许可、世界遗产相关法律 | A |
| AFMA HIMI Fishery | `https://www.afma.gov.au/` | 确认主要经济活动是受管制渔业；船载设备不计为陆上设施 | A |
| ACMA RRL | `https://www.acma.gov.au/register-radiocommunications-licences-rrl` | 复核澳大利亚无线电牌照；预期无 HM 商业电信设施 | A |
| IANA `.HM` | `https://www.iana.org/domains/root/db/hm.html` | ccTLD 委派状态；不得把域名注册服务误判为数据中心 | A |
| HM Domain Registry | `https://www.registry.hm/` | `.hm` 注册状态；开放注册不是本地基础设施证据 | A |
| UNESCO World Heritage | `https://whc.unesco.org/en/list/577/` | 世界遗产、strict nature reserve、低人类扰动 | B |
| 官方云区域清单 | AWS / Azure / Google Cloud / Oracle OCI official region lists | 阴性对照：无 HM region / edge location | A |

## 3. 为什么默认无设施（No-Market Rationale）

1. **人口与需求**：无永久人口、无本地居民、无城市、无常设商业客户。数据中心的本地需求和运营劳动力均不存在。
2. **进入与物流**：无港口、无机场/跑道、无道路；登陆取决于船舶、天气、海况和许可窗口。
3. **能源**：无公共电网、无大型发电或输配电系统。科考营地的临时发电/通信设备属于 kW 级后勤，不支持 MW 级 IT load。
4. **通信**：无已知海底光缆登陆站、无本地 ISP/IXP/移动网络。科考通信预期为卫星/HF 等任务链路。
5. **法律与环境**：世界遗产、海洋保护区、AAD 管理和许可制度使商业开发高度不可行。

## 4. 分区枚举策略（Per-Division Official Enumeration Strategy）

| Repo division | 优先级 | 官方检索策略 | 计数规则 |
|---|---:|---|---|
| Heard Island and McDonald Islands | High | AAD 站点/科考页面；DCCEEW/legislation 环境许可；ACMA 牌照；IANA/ITU 编号资源；AFMA/CCAMLR 渔业；官方云区域阴性对照 | 只有 A 级来源点名“设施名称 + 功能 + 位置 + 运营方”时才升级；默认 verified-negative |

地理亚区只用于 tagging，不拆分 division：

- **Atlas Cove**：历史 ANARE/AAD 研究站（1947-1955）和后续科考清理/访问地点；历史站点不计为现役数据中心。
- **Spit Bay / Magnet Point / 其他 Heard Island 科考点位**：短期科考、仪器安装或营地活动；默认不计数。
- **McDonald Islands / Shag Islet / Morgan Island / Sail Rock**：无人岛礁；仅按官方点名记录自然/科考线索。
- **HIMI Marine Reserve / 周边水域**：渔业和监管巡查海域；船载设备不计为陆上设施。

## 5. 官方查询模板（Official Query Templates）

英文：

```text
site:antarctica.gov.au "Heard Island" (station OR camp OR expedition OR communications OR satellite)
site:antarctica.gov.au "Heard Island" ("data centre" OR "data center" OR datacenter OR server OR hosting)
site:antarctica.gov.au ("Atlas Cove" OR "Spit Bay" OR "Magnet Point") (camp OR generator OR power OR satellite OR station)
site:dcceew.gov.au "Heard Island" (permit OR reserve OR "marine park" OR "marine reserve")
site:legislation.gov.au "Heard Island and McDonald Islands Act"
site:afma.gov.au "Heard Island and McDonald Islands Fishery"
site:acma.gov.au "Heard Island" (licence OR radiocommunication OR amateur)
site:iana.org ".hm" delegation
"Heard Island" OR "McDonald Islands" ("data centre" OR "data center" OR datacenter OR colocation OR hosting)
"submarine cable" "Heard Island" OR "McDonald Islands"
```

中文：

```text
"赫德岛" OR "麦克唐纳群岛" ("数据中心" OR "云" OR "海底光缆" OR "服务器" OR "算力")
"赫德岛" OR "麦克唐纳群岛" (澳大利亚南极局 OR 科考 OR 通讯 OR 许可)
"赫德岛" OR "麦克唐纳群岛" 数据中心 -"麦当劳"
```

## 6. 候选处理与抽取规则（Candidate Handling）

本领地预期候选数为 **0**。任何候选必须满足：

- 至少一份 A 级来源点名设施/项目；
- 来源同时给出名称、功能、位置、运营方；
- 能排除 AADC、AAT 南极站、Kerguelen、McDonald’s 品牌、船载设备、临时科考仪器等假阳性；
- 若声称有 MW 级负载，必须有 A 级电力、许可、采购或运营商证据。

候选记录模板：

```text
country_code: HM
division: Heard Island and McDonald Islands | Unknown HM
facility_or_project_name:
operator_or_owner:
consent_or_authorisation:
site_address:
coordinates:
status: verified-negative | lead | rejected_false_positive
facility_type:
it_load_mw:
power_connection:
connectivity:
evidence_grade:
primary_urls:
last_checked: 2026-08-12
notes:
```

## 7. 假阳性清单（False Positives）

- **Australian Antarctic Data Centre（AADC, `data.aad.gov.au`）**：AAD 的科学数据仓库/地图与数据服务，不是 HM 岛上数据中心。
- **`.hm` 域名注册服务**：IANA/registry.hm 说明 ccTLD 委派和开放注册；这不是本地机房、ISP 或云节点证据。
- **AAT 澳属南极领地设施**：Mawson、Davis、Casey、Wilkins 跑道等不得归入 HM。
- **Mawson Peak vs Mawson Station**：Mawson Peak 是 HM 活火山 Big Ben 的峰；Mawson Station 是南极站。
- **McDonald Islands vs McDonald’s**：中文/英文品牌误命中必须排除。
- **Kerguelen / 法属南方和南极领地设施**：最近有人设施不属于 HM。
- **渔业船载设备**：HIMI Fishery 船舶的通信、冷藏、加工系统不计为陆上数据中心。
- **科考自动站 / 海平面站 / 气象遥测**：可记录为 scientific instrument lead，但不计数。

## 8. 每轮复核清单（Checker Checklist）

1. 读取 manifest HM 行，确认 division 仍为 `Heard Island and McDonald Islands`。
2. 复核 AAD HM 主页面和 Human activities 页面，确认无人居住、AAD 管理、访问/许可边界未改变。
3. 检索 AAD / DCCEEW / legislation / AFMA 是否出现“永久站点、建设许可、机房、通信设施、能源设施”等新公告。
4. 检索 ACMA RRL 是否有 HM 位置相关商业电信牌照；若有，仅作为 lead，需确认是否陆上设施。
5. 复核 IANA `.HM` 委派和 registry.hm 注册状态；记录为编号/域名资源，不作为设施。
6. 复核官方 AWS / Azure / Google Cloud / Oracle OCI 区域清单，确认无 HM region / edge location。
7. 复核海缆地图和行业海缆资料，确认无 HM cable landing station。
8. 搜索中英文 “HM data center / 赫德岛 数据中心 / McDonald Islands cloud”等，按 §7 排除假阳性。

## 9. 已验证阴性（Verified Negatives，截至 2026-08-12）

- **商业数据中心 / colocation / hosting**：无。
- **政府或科研数据中心设施**：无；AADC 是塔斯马尼亚侧科学数据服务，不是 HM 岛上设施。
- **公有云区域 / 边缘节点**：无。
- **海底光缆 / cable landing station**：无。
- **本地电信运营商 / 移动网络 / IXP**：无可计数设施。
- **公共电网 / 大型电力项目**：无。
- **有效设施清单预期**：空表；输出 verified-negative。
