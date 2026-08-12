# IM Explorer Industry — 马恩岛数据中心行业/厂商枚举方法

> 日期 Date: 2026-08-12
> 范围 Scope: Isle of Man (IM)。manifest 已核验：`subnational_type: country`，`divisions: ["Isle of Man"]`。行业枚举按单分区全岛执行，再将设施落到 Douglas、Ballasalla/Ronaldsway、Braddan 等 locality。
> 角度 Angle: 行业/厂商主导发现（运营商、数据中心服务商、行业媒体、目录、e-gaming/金融需求方），并回查官方/监管来源。
> 可靠度分级 Reliability grades: **A** = 运营商现行官方设施页、官方/监管/许可/公司记录；**B** = 行业媒体、本地媒体、专业顾问文章；**C** = 目录/聚合/经纪商/SEO/社媒。

---

## 0. 市场形态（Market shape）

- 马恩岛是小型离岸数据中心市场，主要服务 e-gaming、金融服务、云/托管、灾备、网络互联和本地企业 IT；当前没有 hyperscale campus 或 AWS/Azure/GCP/OCI 公共云区域。
- 行业枚举应先扫现行运营商官方页，再用目录补地址，最后用规划/CURA/Companies Registry/GSC 回查。
- 当前一手/强信号集中在 **Douglas** 与 **Ballasalla/Ronaldsway**；低产出 locality 仍需跑负面覆盖，防止遗漏小型 server room、灾备点或发电机规划记录。
- “Isle of Man data centre”搜索噪声很高。很多结果是云转售、UK colocation、咨询或办公地址；没有岛内物理设施声明时不得作为设施入库。

---

## 1. 优先运营商/设施扫描（Priority operator and facility sweep）

| 运营商/设施 | 当前核验 URL | locality | 证据用途与分级 |
|---|---|---|---|
| Manx Telecom Datacentre / Isle of Man Datacentre | https://www.manxtelecom.com/business/solutions-for-enterprise/what-we-do/datacentre/；https://www.isleofmandatacentre.com/ | Isle of Man；Douglas North / Greenhill 需地址核验 | **A**：官方称拥有并运营 two Datacentres，built to Tier 3 standards，提供 colo、managed platforms、DR。DCD 可补 Douglas North/Greenhill 面积与机柜数（B）。 |
| Netcetera / The Dataport | https://new.netcetera.im/；https://new.netcetera.im/datacentre/ | Ballasalla / Malew | **A**：官方称 owns and operates The Dataport，Tier 3/3+ datacentre，1U to full rack。目录常给 The Dataport, Ballasalla/Malew IM9 2AP（C，需回查）。 |
| Domicilium (IOM) Limited / The Isle of Man Datacentre | https://www.domicilium.com/；https://www.digitalisleofman.com/digital-experience-services/domicilium/ | Ballasalla / Ronaldsway Industrial Estate | **A/B**：Domicilium 官方为服务证据；Digital Isle of Man 给出 Domicilium (IOM) Limited, The Isle of Man Datacentre, Ronaldsway Industrial Estate, Ballasalla IM9 2RS。规划/公司注册可提升地址置信度。 |
| Continent 8 Technologies Isle of Man Data Centre | https://www.continent8.com/locations/emea/isle-of-man/ | Douglas / Pulrose Road | **A**：官方称 Isle of Man data centre 是 purpose-built Tier-3 facility in Douglas；privacy/legal 页给出 Pulrose Road 注册办公室。目录给 Pulrose Rd IM2 1AL（C 地址补充）。 |
| Sure by Beyon / Sure Isle of Man | https://business.sure.com/products-and-services/offshore-data-centres/；https://www.sure.com/assets/terms-conditions/IsleofMan/Data-Centre-Services/DATACE2.PDF | Isle of Man（具体地址需核验） | **A**：官方 offshore data-centres 服务页覆盖 Isle of Man，且 IOM data-centre hosting terms PDF 存在。Spring 2026 opening 的 LinkedIn/社媒信号只能作 C/B 种子，需官方页/规划核实状态。 |
| BlueWave Communications | https://bwc.im/；https://bwc.im/products/off-island-wholesale-transit/ | Douglas（通信运营商） | **A（通信身份）/非设施**：CURA 频谱页列为运营商；官方页称如需 co-location/data centre services，由 UK sister company aql 提供。不要把 BlueWave 作为已确认岛内数据中心设施，除非另有一手设施证据。 |
| Wi-Manx / Noventre | https://www.wimanx.com/；https://www.noventre.com/ | Douglas / Heywood House 历史线索；当前 Noventre 注册地址在 Braddan | **B/C 种子**：wimanx.com 当前为 Noventre 站点，页面说明 Wi-Manx name changed / formerly Wi-Manx；DCD 2010 报道和目录提到 Heywood House 数据中心。未找到当前官方设施页前，只作历史/目录线索。 |
| Manx Technology Group | https://manxtechgroup.com/isle-of-man-datacentre-services/ | 全岛顾问 | **B**：2026 市场文章称其 regularly work in all four Isle of Man datacentres，并列出 ASN/供应商；不是设施所有者。用于市场覆盖和负面控制。 |

运营商查询模板：

```text
"Manx Telecom" "data centre" "Douglas North"
"Manx Telecom" "Greenhill" "data centre"
site:isleofmandatacentre.com Manx Telecom "data centre"
site:manxtelecom.com "two Datacentres" "Isle of Man"
"Netcetera" "The Dataport" "Ballasalla"
site:new.netcetera.im "The Dataport" datacentre
"Domicilium" "The Isle of Man Datacentre" "Ronaldsway"
site:digitalisleofman.com "Domicilium" "Datacentre"
"Continent 8" "Isle of Man data centre" "Douglas"
site:continent8.com/locations/emea/isle-of-man "data centre"
site:business.sure.com "Offshore Data Centres" "Isle of Man"
site:sure.com "Data Centre Services" "IsleofMan"
site:bwc.im "co-location" OR "data centre"
"Wi-Manx" OR "Noventre" "Heywood House" "data center"
"Noventre" "data centre" "Isle of Man"
```

---

## 2. 行业媒体与二级来源（Trade press and secondary sources）

| 来源 | URL | 马恩岛用途 | 分级 |
|---|---|---|---|
| Data Centre Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Manx Telecom dedicated datacentre unit；Wi-Manx 2010 historical project；facility size/rack clues | B |
| Manx Technology Group article | https://manxtechgroup.com/isle-of-man-datacentre-services/ | 2026 market overview, ASN list, “all four Isle of Man datacentres” clue | B |
| Capacity Media | https://www.capacitymedia.com/ | subsea, carrier, network infrastructure | B |
| CommsUpdate / Telecompaper | https://www.commsupdate.com/；https://www.telecompaper.com/ | Manx Telecom/Sure/BlueWave/Domicilium telecom events | B |
| IOM Today | https://www.iomtoday.co.im/ | 本地商业、规划、政府 IT 线索 | B |
| Manx Radio | https://www.manxradio.com/ | 本地公共广播，政府/商业项目 | B |
| BBC Isle of Man | https://www.bbc.co.uk/news/world_europe_isle_of_man | 政府/商业/基础设施报道 | B |
| LinkedIn / company social posts | linkedin.com company/showcase pages | 新开业/招聘/项目节奏线索；必须回查官网或规划 | C，个别公司官方账号可作 B 种子 |

行业查询示例：

```text
site:datacenterdynamics.com "Isle of Man" "data center"
site:datacenterdynamics.com "Manx Telecom" "data center"
site:datacenterdynamics.com "Wi-Manx" "data center"
site:capacitymedia.com "Isle of Man" "data centre"
site:commsupdate.com "Manx Telecom" OR "Sure" OR "BlueWave"
site:telecompaper.com "Isle of Man" "BlueWave"
site:iomtoday.co.im "data centre" OR "datacentre"
site:manxradio.com "data centre" OR "datacentre"
"Isle of Man" "data centre" "Tier 3" "Douglas"
"Isle of Man" "data centre" "Ballasalla"
```

---

## 3. 目录与经纪商（Directories and brokers）

目录只用于播种设施名、地址和市场覆盖；不得单独给 A。

| 来源 | URL | 当前用途 | 分级 |
|---|---|---|---|
| DataCenterMap | https://www.datacentermap.com/isle-of-man/ | 当前显示 Isle of Man 6 facilities / Douglas 4 / Ballasalla 2；逐条回查运营商/规划 | C |
| DataCenterMap Douglas | https://www.datacentermap.com/isle-of-man/douglas/ | Wi-Manx Heywood House、Continent 8 等地址线索 | C |
| Data Center Platform | https://datacenterplatform.com/countries/isle-of-man/ | 设施汇总：Continent 8、Netcetera、Domicilium、Manx Telecom、Wi-Manx 等 | C |
| Colo-X | https://www.colo-x.com/ | UK broker；可补 Netcetera/Wi-Manx 地址线索 | C |
| Datacenters.com / Cloudscene / Inflect / ColocationM | 各目录页 | 补充地址、机柜、服务标签；需回查 | C |

目录到一手核验流程：

1. 从目录记录 facility/operator/address/locality。
2. 搜索运营商官网是否有同名设施或明确 “owns and operates”。
3. 用 `services.gov.im/planning-applications/` 或 `pabc.gov.im` 搜地址、发电机、改建、用途变更。
4. 用 CURA 查通信许可，用 Companies Registry 查法律实体。
5. 若只有目录和经纪商页面，记录为 C 并标明缺失的一手证据。

目录查询模板：

```text
site:datacentermap.com/isle-of-man "{operator}"
site:datacenterplatform.com "Isle of Man" "{operator}"
site:colo-x.com "Isle of Man" "{operator}"
site:cloudscene.com "Isle of Man" "{operator}"
site:datacenters.com "Isle of Man" "{operator}"
"{facility name}" "{address}" "Isle of Man"
```

---

## 4. Locality 搜索配方（Locality recipes）

通用模板：

```text
"{locality}" "Isle of Man" "data centre"
"{locality}" "Isle of Man" "data center"
"{locality}" "Isle of Man" datacentre
"{locality}" "Isle of Man" colocation
"{locality}" "Isle of Man" "server room"
"{locality}" "Isle of Man" "backup generator"
"{locality}" "Isle of Man" "substation" "data centre"
site:pabc.gov.im "{locality}" "data centre"
site:services.gov.im/planning-applications "{locality}" "data centre"
```

高优先 locality：

```text
"Douglas" "Manx Telecom" "data centre"
"Douglas North" "data centre" "Manx Telecom"
"Greenhill" "data centre" "Manx Telecom"
"Douglas" "Continent 8" "data centre"
"Pulrose Road" "Continent 8" "data centre"
"Douglas" "Sure" "data centre"
"Ballasalla" "Netcetera" "The Dataport"
"Malew" "The Dataport" "data centre"
"Ronaldsway Industrial Estate" "Domicilium" "data centre"
"Ballasalla" "Domicilium" "data centre"
"Heywood House" "Wi-Manx" "data centre"
```

低产出 locality 负面覆盖：

```text
"Onchan" "data centre" "Isle of Man"
"Braddan" OR "Union Mills" "data centre" "Isle of Man"
"Ramsey" "data centre" "Isle of Man"
"Peel" "data centre" "Isle of Man"
"Castletown" "data centre" "Isle of Man"
"Port Erin" OR "Port St Mary" "data centre" "Isle of Man"
"St John's" OR "Laxey" OR "Sulby" "data centre" "Isle of Man"
```

---

## 5. 枚举矩阵（Enumeration matrix）

| 段/地点 | 运营商官方 | 行业媒体 | 目录 | 规划 | CURA | 公司注册 |
|---|---|---|---|---|---|---|
| Douglas | 高：Manx Telecom、Continent 8、Sure、Wi-Manx/Noventre history | 高：DCD、local media | 高 | 中 | 高 | 高 |
| Ballasalla / Ronaldsway / Malew | 高：Netcetera、Domicilium | 中 | 高 | 中 | 中 | 高 |
| Braddan / Union Mills / Tromode | 低-中 | 低 | 低 | 中 | 低 | 低 |
| Onchan | 低 | 低 | 低 | 中 | 低 | 低 |
| Ramsey | 低 | 低 | 低 | 中 | 低 | 低 |
| Peel / Castletown / Port Erin / Port St Mary | 极低 | 极低 | 极低 | 低 | 极低 | 极低 |
| 全岛需求方（e-gaming/金融/DR） | 中 | 中 | 高噪声 | 低 | 低 | 中 |

覆盖规则：Douglas 与 Ballasalla/Ronaldsway 需要逐设施回查；其他 locality 需要通用扫描和 negative log。任何低产出 locality 的命中必须至少有一个一手来源或两个独立 B 来源才可入库。

---

## 6. 种子清单（Seed list for validation）

| 种子 | locality | 当前状态倾向 | 最佳证据路径 |
|---|---|---|---|
| Manx Telecom two datacentres | Douglas North / Greenhill（待地址确认） | 运营 | Manx Telecom 官方页 + isleofmandatacentre.com + DCD + 规划/公司 |
| Netcetera The Dataport | Ballasalla / Malew | 运营 | Netcetera 官方页 + 规划 + Companies Registry |
| Domicilium The Isle of Man Datacentre | Ronaldsway Industrial Estate, Ballasalla | 运营 | Domicilium 官方页 + Digital Isle of Man + 规划 + CURA |
| Continent 8 Isle of Man Data Centre | Douglas / Pulrose Road | 运营 | Continent 8 official location + legal/address + directory/planning |
| Sure Isle of Man data centre services | Isle of Man；地址待核验 | 运营/扩展中 | Sure Business official page + IOM terms PDF + CURA + planning |
| Wi-Manx / Noventre Heywood House | Douglas（历史）；Braddan（当前 Noventre 注册/联系地址） | 历史/待核实现状 | DCD 2010 + directory + wimanx.com/Noventre rebrand pages + planning |
| BlueWave Communications | Douglas | 通信运营商；非确认岛内 DC | bwc.im + CURA；若提到 data centre，多为 UK aql colocation |
| Government Data Centre | Douglas 线索 | 历史/待核实现状 | gov.im + Tynwald + procurement + planning |
| e-gaming operators（Microgaming、Rational/PokerStars 等） | Douglas/Onchan 等办公地点 | 需求方，不是设施 | 公司官网 + GSC licence + media；不得以办公地址作 DC |

---

## 7. 分级与入库规则（Grading and ingestion rules）

- **A 级设施**：运营商官网明确 owns/operates/located on Isle of Man，或规划/政府/监管文件确认物理设施。
- **A 级服务但非地址**：运营商官网确认 data-centre/colo 服务，但没有具体地址。入库时 facility_address_confidence 需低或 unknown。
- **B 级设施线索**：DCD、Manx Technology Group、本地媒体给出设施名/规模/地址；需要一手回查。
- **C 级设施线索**：DataCenterMap、Data Center Platform、Colo-X、Inflect、ColocationM、社媒、SEO 页面。只播种，不单独确认。
- **不得入库为设施**：AWS/Azure/GCP/OCI “Isle of Man cloud” reseller、运营商总部、e-gaming 公司办公室、network PoP、radio mast、substation、generator-only planning record。

---

## 8. 负面控制（Negative controls）

```text
"Isle of Man" "AWS region" -aws.amazon.com
"Isle of Man" "Azure region" -microsoft.com -azure.microsoft.com
"Isle of Man" "Google Cloud region" -cloud.google.com
"Isle of Man" "Oracle Cloud region" -oracle.com
"BlueWave" "Isle of Man" "data centre" -bwc.im
"BlueWave" "data center" "bluewave.net"
"BlueWave" "data centre" "bluewave.bm"
"Manx Telecom headquarters" "data centre"
"e-gaming" "Isle of Man" "data centre" "office"
```

记录 negative log 时注明：检索日期、查询式、未发现内容（例如 no hyperscale public region；BlueWave current site points colocation to UK aql DCs；company office only）。

---

## 9. 执行顺序（Execution order）

1. 用 Manx Telecom、Netcetera、Domicilium、Continent 8、Sure 官方页建立 A/B 种子。
2. 用 DataCenterMap/Data Center Platform/Colo-X 补地址和漏项，但全部标 C。
3. 用 planning services / pabc 查地址、发电机、用途变更和扩建。
4. 用 CURA 查运营商许可，用 Companies Registry 查实体。
5. 用 GSC 与本地媒体解释 e-gaming/金融需求，不把需求方办公室当设施。
6. 用官方云区域页做 hyperscale 缺位确认。
7. 对 Douglas、Ballasalla/Ronaldsway 做深扫；其余 locality 做通用扫描并记录负面结果。
