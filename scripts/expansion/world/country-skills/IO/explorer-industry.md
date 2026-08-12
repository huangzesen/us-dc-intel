# IO Explorer Industry — 英属印度洋领地（British Indian Ocean Territory）数据中心行业面发现方法

Date 日期: 2026-08-12. Status 状态: final source-verification pass. Country 国家/地区: **IO 英属印度洋领地 (British Indian Ocean Territory / BIOT)**. Division model 行政区划模型（per `world-manifest.jsonl`）: `divisions=["British Indian Ocean Territory"]`。Scope 范围: 行业/运营商/目录/媒体侧负向核查，用于确认 IO 没有可公开枚举的商业数据中心设施。Companion file 配套文件: `explorer-official.md`（官方管理、访问限制、军事边界、云区域负核查）。

可靠性分级 Reliability grades: **A** = 官方/一级证据（运营商自有设施页、政府/军方/监管机构、云厂商官方区域页）；**B** = 强二级证据（可靠行业媒体、TeleGeography/DCD/Reuters 类报道、PeeringDB/IXPDB/ISOC 等目录）；**C** = 弱线索（聚合器、市场页、转售商、地址推断）；**U** = 未证实传闻，仅作搜索提示。

---

## 0. 行业结论（Industry conclusion）

- **商业设施预期 = 0**。IO 没有公开商业 colocation、批发 DC、云区域、Local Zone、民用 IXP 或可销售托管市场。
- 行业面工作的重点是排除误判：`.io` 域名生态、Diego Garcia 军事通信、基地承包商 IT、海缆秘密/军事支线、聚合器错误地址。
- 任何“正结果”必须升级到 A 级来源才可进入候选；在 IO 场景下，B/C 级来源通常只证明军事或连接性背景，不证明商业 DC。

### 常见误判源（False positives）

1. **`.io` ccTLD**：大量科技公司使用 `.io`，但域名注册业务与 BIOT 本地数据中心无关。IANA `.io` 页面只用于确认 TLD 委托，不是设施证据。
2. **Diego Garcia military IT**：NSF Diego Garcia 的 NOC、通信机房、卫星/海缆接入、承包商 IT 属国防任务，不是公开销售的 colo/cloud。
3. **OAC/Diego Garcia cable spur**：DCD/Reuters 报道的 Oman Australia Cable 支线指向美国海军基地通信韧性；这是 military connectivity，不能当作商业海缆登陆站或 DC。
4. **聚合器/地址错误**：Data Center Map、datacenters.com、Cloudscene 等若出现 IO/Diego Garcia 条目，优先假设为 TLD、地址复用或目录错误，必须找运营商/官方 A 级来源。

---

## 1. 行业媒体与新闻（Trade press and news）

| Source 来源 | URL / route | Use 用途 | Grade |
|---|---|---|---:|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ | 检索 Diego Garcia、BIOT、OAC；已知 2023 报道为军事海缆支线背景，不是商业 DC。 | B |
| Reuters / AP / BBC | site search | Diego Garcia、Chagos、UK/Mauritius 主权与军事基地新闻；政治/军事背景，不直接构成设施证据。 | B |
| TeleGeography / Submarine Cable Map | https://www.submarinecablemap.com/ | 海缆和 landing-point 背景；需要区分商业系统与军事/未公开支线。 | B/C |
| Capacity Media / Light Reading / SubTel Forum | site search | 连接性、海缆、卫星通信补充检索。 | B |
| Defense industry press | site search | 国防合同和基地支持线索；只作 exclusion 背景。 | B/C |

高价值搜索模板：

```text
"British Indian Ocean Territory" ("data centre" OR "data center" OR datacenter OR colocation OR "cloud region")
"Diego Garcia" ("data centre" OR "data center" OR datacenter OR colocation OR "server room")
"Diego Garcia" ("cloud region" OR "edge node" OR "internet exchange" OR IXP)
site:datacenterdynamics.com "Diego Garcia"
site:datacenterdynamics.com "British Indian Ocean Territory"
site:reuters.com "Diego Garcia" "submarine cable"
site:capacitymedia.com "Diego Garcia"
site:subtelforum.com "Diego Garcia"
```

处理规则：

- 行业媒体只要没有明确商业运营商、商业服务、设施地址/客户市场，就不得入候选。
- 军事海缆/通信报道记录为 `military connectivity; excluded from commercial DC enumeration`。

---

## 2. 聚合器与设施目录（Aggregators and directories）

| Source 来源 | URL | Expected result 预期 | Handling 处理 |
|---|---|---|---|
| Data Center Map | https://www.datacentermap.com/ | 无 IO/Diego Garcia 商业设施。 | 出现条目按 C；需 A 级复核，否则丢弃。 |
| datacenters.com | https://www.datacenters.com/ | 无 IO 提供商/设施。 | 同上。 |
| Cloudscene | https://www.cloudscene.com/ | 无 IO 数据中心/云节点。 | 同上。 |
| PeeringDB | https://www.peeringdb.com/ | 无 Diego Garcia/BIOT public facility 或 IXP。 | B/C 负证据；网络对象不等于 DC。 |
| IXPDB / Euro-IX | https://ixpdb.euro-ix.net/ | 无 IO IXP。 | 无结果支持 0 结论。 |
| Internet Exchange Map | https://www.internetexchangemap.com/ | 无 IO IXP。 | C 级背景。 |
| RIPE/APNIC/ARIN DB | registry search | 可能有与军方、TLD、研究或远程地址相关的对象；不证明设施。 | 只作网络线索。 |

目录搜索模板：

```text
site:datacentermap.com "British Indian Ocean Territory"
site:datacentermap.com "Diego Garcia"
site:datacenters.com "British Indian Ocean Territory"
site:datacenters.com "Diego Garcia"
site:cloudscene.com "British Indian Ocean Territory"
site:cloudscene.com "Diego Garcia"
site:peeringdb.com "Diego Garcia"
site:peeringdb.com "British Indian Ocean Territory"
site:ixpdb.euro-ix.net "British Indian Ocean Territory" OR "Diego Garcia"
```

---

## 3. 云厂商、CDN、边缘节点（Cloud, CDN, edge）

无全球云厂商在 IO 设立公开商业 region、zone、local zone 或 edge market。用官方页面确认 absence；不要用销售覆盖、合作伙伴、`.io` 客户、军事/政府云合同推断本地设施。

| Provider | Official source 官方来源 | IO expected result | Grade |
|---|---|---|---:|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; https://aws.amazon.com/about-aws/global-infrastructure/localzones/ | No IO Region/Local Zone. | A |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No IO public region. | A |
| Google Cloud | https://cloud.google.com/about/locations ; https://datacenters.google/locations/ | No IO region/Google-owned DC. | A |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No IO public region. | A |
| Cloudflare / Akamai / CDN edge | official network pages + PeeringDB | No public IO PoP expected; any Diego Garcia military service is excluded. | A/B |

查询：

```text
"AWS" "British Indian Ocean Territory" "region"
"Azure" "Diego Garcia" "region"
"Google Cloud" "British Indian Ocean Territory" "location"
"OCI" "Diego Garcia" "cloud region"
"Cloudflare" "Diego Garcia" OR "British Indian Ocean Territory"
"Akamai" "Diego Garcia" OR "British Indian Ocean Territory"
```

---

## 4. 连接性与海缆（Connectivity and subsea）

### 4.1 已知军事连接性背景

- DCD 2023 报道称 Oman Australia Cable 有通往 Diego Garcia 美国海军基地的秘密支线，目的是提高美国太平洋舰队通信韧性。该报道的价值是说明 **military communications exist**，不是说明存在商业 landing station、IXP 或数据中心。
- 任何 OAC/Diego Garcia、US Pacific Fleet、Pentagon、SubCom、Big Wave、base communications 结果都标记为军事连接性背景。

### 4.2 商业海缆/IXP负核查

```text
"Diego Garcia" "submarine cable landing station"
"Diego Garcia" "commercial cable landing"
"British Indian Ocean Territory" "internet exchange"
"British Indian Ocean Territory" IXP
site:submarinecablemap.com "Diego Garcia"
site:peeringdb.com "Diego Garcia" facility
site:ixpdb.euro-ix.net "Diego Garcia"
```

处理：

- 若公开地图列出 Diego Garcia landing point，必须判读其服务对象。若无公共运营商、商业接入、设施服务页，则不作为商业 DC/IXP。
- Cable landing station 也不自动等于数据中心；在 IO 场景下，军事或保密用途默认排除。

---

## 5. 基地承包商、国防 IT、招聘（Contractors and military IT）

基地支持合同可能出现 `IT`, `communications`, `network operations`, `data`, `telecom`, `fiber`, `power`, `facility maintenance` 等关键词。这些是 exclusion search，不是设施发现。

```text
"NSF Diego Garcia" ("IT" OR "communications" OR "network operations" OR "telecommunications")
"Diego Garcia" "base support" contractor
"Diego Garcia" "fiber optic" "US Navy"
"Diego Garcia" "data center" "contract"
"Diego Garcia" "server room" "contractor"
site:sam.gov "Diego Garcia" ("IT" OR "communications" OR "network")
site:govtribe.com "Diego Garcia" ("IT" OR "communications")
```

规则：

- 合同、招聘、承包商案例只能证明基地有 IT/通信需求。
- 不记录承包商 office、network room、communications facility、power plant、satellite terminal、fiber landing as commercial DC。
- 若承包商声称提供 `data center operations`，仍需确认是否公开商业服务；基地内国防运维仍排除。

---

## 6. `.io` TLD 误判排除（TLD false-positive filter）

```text
".io" "data center"
"Identity Digital" ".io"
"Internet Computer Bureau" ".io"
"British Indian Ocean Territory" ".io" "registry"
site:iana.org/domains/root/db/io.html
```

记录方式：

- `.io` registration / registry / registrar / DNS / startup usage = TLD background only.
- 不从 `.io` 域名数量、注册商、Whois、DNS 服务、CDN 客户推断 BIOT 境内设施。
- 若某商业 DC 公司使用 `.io` 域名，按其真实国家/设施地址枚举，不归入 IO。

---

## 7. 负向核查汇总（Negative query bundle）

每次更新 IO 清单前完整跑一遍，保存检索日期和异常结果：

```text
"British Indian Ocean Territory" ("data centre" OR "data center" OR datacenter OR colocation OR "cloud region")
"Diego Garcia" ("data centre" OR "data center" OR datacenter OR colocation OR "cloud region")
"British Indian Ocean Territory" ("cable landing" OR IXP OR "internet exchange" OR "edge node")
"Diego Garcia" ("commercial" AND ("data center" OR "cable landing" OR "internet exchange"))
site:datacenterdynamics.com "Diego Garcia" ("data center" OR "submarine cable")
site:datacentermap.com "Diego Garcia"
site:datacenters.com "British Indian Ocean Territory"
site:cloudscene.com "British Indian Ocean Territory"
site:peeringdb.com "Diego Garcia"
site:gov.uk "British Indian Ocean Territory" "data centre"
site:biot.gov.io "data centre" OR "data center" OR "cloud"
```

预期结果：无商业设施。异常结果按以下顺序处理：

1. 是否只是 `.io` TLD？是则排除。
2. 是否军事/基地通信？是则排除。
3. 是否只有聚合器/SEO 页面？无 A 级来源则丢弃。
4. 是否有运营商自有页面、云厂商区域页、政府许可/公告？若有，转入人工复核并同步更新 `explorer-official.md`。

---

## 8. 检查员清单（Checker checklist）

1. 确认 `explorer-official.md` 的官方结构事实仍成立，特别是访问限制、BIOTA governance、UK/Mauritius treaty 状态。
2. 重跑 §1–§7 搜索模板，记录日期、搜索引擎、异常结果。
3. 打开 DCD/Reuters/TeleGeography 类海缆结果，标注是否 military-only。军事专用连接不入 DC 清单。
4. 检查 Data Center Map、datacenters.com、Cloudscene、PeeringDB、IXPDB；没有 A 级来源的条目全部丢弃。
5. 检查 AWS/Azure/GCP/OCI 官方区域页；确认无 IO 区域或 Local Zone。
6. 检查 `.io` 注册局/IANA信息；排除 TLD 相关噪声。
7. 若出现商业设施正信号，必须补齐：设施运营商、物理地点、商业服务类型、官方/运营商来源、division=`British Indian Ocean Territory`。
8. 最终产出：`0 commercial datacenter facilities; military/base communications excluded; .io TLD false positives excluded.`

---

## 9. Expected yield 预期产出

- Commercial datacenter / colocation / wholesale DC / public cloud region / Local Zone / civilian IXP: **0**.
- Military communications, defense IT, base support facilities, private/secret cable spur: **excluded**.
- `.io` TLD, registrar, DNS/CDN, startup-domain references: **excluded**.
- Any future sovereignty or treaty change triggers a governance refresh, not an automatic market assumption.
