# IO Explorer Official — 英属印度洋领地（British Indian Ocean Territory）数据中心官方面枚举方法

Date 日期: 2026-08-12. Status 状态: final source-verification pass. Country 国家/地区: **IO 英属印度洋领地 (British Indian Ocean Territory / BIOT)**. Division model 行政区划模型（per `world-manifest.jsonl`）: `subnational_type=country`, `divisions=["British Indian Ocean Territory"]`。IO 在清单模型中只按整个领地枚举，不拆分环礁或岛屿；公开有人活动集中在 **Diego Garcia 迪戈加西亚** 的英美军事基地。Companion file 配套文件: `explorer-industry.md`（行业面负向核查）。

可靠性分级 Reliability grades: **A** = 官方/一级来源（政府、监管机构、法律文本、军方官方页、云厂商官方区域页、运营商自有设施页）；**B** = 强二级来源（可靠媒体、行业媒体、PeeringDB/TeleGeography/ISOC 等目录或研究）；**C** = 弱线索（聚合器、市场页、转售商、地址推断）；**U** = 未证实传闻，仅作搜索提示。

---

## 0. 官方结论（Official conclusion）

- **预期商业数据中心产出 = 0**。IO 没有可公开枚举的商业 colocation、批发数据中心、云区域或民用托管市场。
- 核查目标不是“找设施”，而是用官方与行业负向证据确认“没有可入清单设施”。军事通信、基地 IT、军方电力/通信节点、承包商机房均不进入商业 DC 清单。
- `.io` ccTLD 与领地本地基础设施无关。`.io` 域名使用量、注册商生态、DNS/CDN/域名业务不能作为 IO 境内设施线索。

### 已核实结构事实（2026-08-12）

| Fact 事实 | Verified source 已核实来源 | Grade |
|---|---|---:|
| GOV.UK BIOT 页面称 BIOT 为英国海外领地、从伦敦管理、无永久人口、无本地正式外交/领事存在。 | https://www.gov.uk/world/british-indian-ocean-territory/news | A |
| BIOT Administration 官网称 BIOTA formally administered from the UK；Commissioner 由国王任命，Administrator 管日常事务，Brit Rep 在 Diego Garcia 代表行政机构。 | https://www.biot.gov.io/governance/ | A |
| BIOT 不是旅游目的地；进入受限、需许可、无商业航班；Diego Garcia 仅限与军事设施或领地行政相关人员进入。 | https://www.biot.gov.io/visiting/ and https://www.gov.uk/foreign-travel-advice/british-indian-ocean-territory/entry-requirements | A |
| U.S. Navy 官方 NSF Diego Garcia 页面称该设施为印度洋/波斯湾前沿部署部队提供后勤支持。 | https://cnrj.cnic.navy.mil/Installations/NSF-Diego-Garcia/ | A |
| UK/Mauritius 关于 Chagos Archipelago including Diego Garcia 的条约于 2025-05-22 提交英国议会；生效前 BIOT 仍按当前官方结构处理。 | https://www.gov.uk/government/publications/ukmauritius-agreement-concerning-the-chagos-archipelago-including-diego-garcia-cs-mauritius-no12025 | A |
| `world-manifest.jsonl` 中 IO 为单一 division: `["British Indian Ocean Territory"]`。 | `/scripts/expansion/world/world-manifest.jsonl` line with `country_code:"IO"` | A-local |

---

## 1. 管理面与官方入口（Official administration surfaces）

| Source 来源 | URL | Use 用途 | Grade |
|---|---|---|---:|
| GOV.UK BIOT location page | https://www.gov.uk/world/british-indian-ocean-territory/news | 英国官方领地页、公告、出版物入口；确认“从伦敦管理、无永久人口”。 | A |
| BIOT Administration | https://www.biot.gov.io/ | 领地行政官网；治理、访问许可、法律/Gazette、科学/渔业许可。 | A |
| BIOT Governance | https://www.biot.gov.io/governance/ | Commissioner、Administrator、Brit Rep、BIOT Police/Customs/Immigration、独立电信监管员等结构。 | A |
| BIOT Visiting | https://www.biot.gov.io/visiting/ | 访问受限、无商业航班、Diego Garcia 仅限军事/行政相关进入。 | A |
| FCDO travel advice | https://www.gov.uk/foreign-travel-advice/british-indian-ocean-territory | 入境限制和安全建议；支撑“无民用可进入市场”。 | A |
| UK legislation search | https://www.legislation.gov.uk/ | 检索 `British Indian Ocean Territory Constitution Order`、相关 Ordinances；用于法律框架核查。 | A |
| UK/Mauritius treaty page | https://www.gov.uk/government/publications/ukmauritius-agreement-concerning-the-chagos-archipelago-including-diego-garcia-cs-mauritius-no12025 | 主权安排变化监控。条约生效才会改变领地状态；不得用政治新闻推断 DC 市场。 | A |
| U.S. Navy NSF Diego Garcia | https://cnrj.cnic.navy.mil/Installations/NSF-Diego-Garcia/ | 美军基地官方事实页；确认军事/后勤性质。 | A |
| CIA World Factbook | https://www.cia.gov/the-world-factbook/countries/british-indian-ocean-territory/ | 地理、人口、通信背景；不是 DC 设施证据。 | A/B |
| IANA country codes | https://www.iana.org/assignments/country-codes/country-codes.xhtml | ISO 3166-1 alpha-2 `IO` 代码确认。 | A |
| IANA `.io` root DB | https://www.iana.org/domains/root/db/io.html | `.io` ccTLD 委托确认；用于排除 TLD 误判。 | A |

---

## 2. 为什么是 0（Why zero）

1. **封闭/许可进入的军事领地**：BIOT 和 FCDO 访问页均确认不是旅游目的地、无商业航班、进入需许可，Diego Garcia 只允许军事设施或领地行政相关人员进入。没有普通客户、员工、供应商可自由进入的民用设施市场。
2. **无永久平民人口与无本地商业生态**：GOV.UK 确认无永久人口；BIOTA 从英国管理。即使 BIOTA 有预算、警务、海关移民、渔业/科学许可和独立电信监管职能，也不是面向公众的数据中心许可/注册/招商体系。
3. **基地用途为国防支持**：NSF Diego Garcia 官方页面将任务定位为支持前沿部署和作战/后勤需求。此类 IT、通信、电力、网络机房属于国防基础设施，不是商业 colocation 或云区域。
4. **商业云区域为负**：AWS、Azure、Google Cloud、Oracle OCI 官方区域列表无 IO/Diego Garcia 区域或 Local Zone。最近商业区域在印度、新加坡、南非、澳大利亚/中东方向。
5. **公开商业设施目录为负**：Data Center Map、datacenters.com、Cloudscene、PeeringDB、IXPDB 等应预期无 IO 商业设施。若出现条目，必须用 A 级运营商/官方来源验证；否则按 C/U 丢弃。
6. **海缆/通信信号多为军事专用**：行业报道显示 Diego Garcia 存在与 OAC 相关的秘密/军事用途支线线索；这加强的是“军事通信基础设施存在”，不是商业登陆站、IXP 或 DC 市场。

结论模板: `IO / British Indian Ocean Territory was checked on YYYY-MM-DD against UK/BIOT official administration pages, FCDO travel advice, U.S. Navy NSF Diego Garcia pages, cloud-region lists, cable/directories, and trade press. Result: 0 public commercial datacenter facilities. Military/base communications are excluded from commercial enumeration.`

---

## 3. 官方负向核查流程（Official negative checks）

### 3.1 领地法律、商业注册、投资许可

- 在 GOV.UK、BIOT Administration、legislation.gov.uk 检索 `data centre/data center/cloud/colocation/company registration/investment/telecommunications licence`.
- 预期：只出现治理、访问、环保、渔业、科学、移民、警务、法院/法律、主权谈判等材料；无商业 DC 许可、无投资促进项目、无公开公司注册/园区招商入口。
- 注意：BIOTA governance 页面提到 independent telecoms regulator。记录为 **A 级治理事实**，但不得误写为普通民用电信市场或 DC 许可框架。

### 3.2 访问与人员限制

核查：

```text
site:biot.gov.io/visiting Diego Garcia access restricted permit commercial flights
site:gov.uk/foreign-travel-advice/british-indian-ocean-territory "commercial flights" OR "restricted access"
```

预期：访问受限、无商业航班、Diego Garcia 仅限军事/行政相关进入。这是“无商业 DC 市场”的核心 A 级证据。

### 3.3 军事设施边界

核查：

```text
site:cnrj.cnic.navy.mil/Installations/NSF-Diego-Garcia "mission" OR "logistic support"
site:gov.uk "Diego Garcia" "military base"
```

处理规则：

- 官方军方页面可作为“基地存在/任务性质”证据。
- 不枚举基地内 server room、通信节点、NOC、机房、卫星/海缆接入、承包商 IT 设施。
- 只有公开 A 级来源明确表示某设施面向公众销售 colocation/hosting/cloud 服务时才可转入候选；当前预期为无。

### 3.4 云厂商区域（Cloud region negative table）

每轮核查重跑并记录日期：

| Provider | Official source 官方来源 | IO result | Notes |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and https://aws.amazon.com/about-aws/global-infrastructure/localzones/ | No IO Region/Local Zone expected. | 最近商业选择通常为 Mumbai/Singapore/Cape Town/Middle East routes. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No IO public region expected. | India/Singapore/South Africa/Australia are nearest practical regions. |
| Google Cloud | https://cloud.google.com/about/locations and https://datacenters.google/locations/ | No IO cloud region or Google-owned DC expected. | Cable references are connectivity, not cloud regions. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No IO public region expected. | Check public cloud regions only; DoD/government service models are not local IO facilities. |

### 3.5 `.io` ccTLD 排除

- IANA `.io` root DB 用于确认 ccTLD 委托；域名注册和注册局运营不代表 BIOT 境内基础设施。
- 搜索到 `*.io`、startup、developer、DNS、domain registry、registrar、GoDaddy/Identity Digital/ICB 等内容时，标记为 TLD 背景，不得入设施候选。

### 3.6 海缆、IXP、公用事业

核查：

```text
"Diego Garcia" "submarine cable" "data center"
"British Indian Ocean Territory" IXP OR "internet exchange"
site:submarinecablemap.com "Diego Garcia"
site:datacenterdynamics.com "Diego Garcia" "Oman Australia Cable"
```

处理：

- 公开图或行业报道若显示 Diego Garcia landing/spur，先判断是否服务军方/基地。军事专用或未公开商业接入的一律不计为商业 DC 或 IXP。
- 无民用电网/地产/客户市场。基地电力和通信不作为公共 utility 市场处理。

---

## 4. 检查员清单（Checker checklist）

1. 确认 manifest 仍为 `country_code="IO"`, `subnational_type="country"`, `divisions=["British Indian Ocean Territory"]`。
2. 打开 GOV.UK BIOT 页面、BIOT governance/visiting、FCDO travel advice、U.S. Navy NSF Diego Garcia 页面，记录核查日期。
3. 检查 UK/Mauritius treaty 和相关 UK law 页面：若条约已生效并改变 BIOT 状态，更新命名与治理部分；仍不得将主权变化直接解释为商业 DC 市场。
4. 重跑 cloud-region negative table。官方云厂商页面优先，市场博客不用于证明区域存在。
5. 重跑 `.io` TLD 排除和海缆/IXP搜索，特别标注军事 OAC/Diego Garcia spur 类报道为 **military connectivity, excluded**。
6. 与 `explorer-industry.md` 的目录、聚合器、贸易媒体、承包商搜索交叉核对。
7. 若发现商业正信号，必须取得 A 级来源：运营商设施页、云厂商区域页、政府许可/公告、公开商业海缆/IXP/设施运营页。B/C/U 只能做线索。
8. 产出记录应写明：`0 commercial datacenter facilities; military/base communications excluded from public commercial inventory.`

---

## 5. 搜索模板（Official query bundle）

```text
site:gov.uk/world/british-indian-ocean-territory ("data centre" OR "data center" OR cloud OR colocation)
site:biot.gov.io ("data centre" OR "data center" OR cloud OR colocation OR "telecoms regulator")
site:biot.gov.io (business OR company OR investment OR licence OR license) "British Indian Ocean Territory"
site:legislation.gov.uk "British Indian Ocean Territory" ("telecommunications" OR "data" OR "company")
site:gov.uk "Diego Garcia" "military base"
site:cnrj.cnic.navy.mil/Installations/NSF-Diego-Garcia ("data center" OR "communications" OR "mission")
"British Indian Ocean Territory" ("data centre" OR "data center" OR datacenter OR colocation OR "cloud region")
"Diego Garcia" ("commercial data center" OR colocation OR "cloud region" OR IXP)
```

---

## 6. Expected yield 预期产出

- 商业数据中心、colocation、批发 DC、云区域、Local Zone、民用 IXP：**0**。
- 军方通信/基地 IT/承包商设施：**不公开枚举，不入商业清单**。
- `.io` 域名生态：**排除为境外/TLD 误判**。
- 若将来主权/行政安排变化，先更新官方结构，再重新跑同一负向核查；除非出现 A 级商业设施来源，否则产出仍为 0。
