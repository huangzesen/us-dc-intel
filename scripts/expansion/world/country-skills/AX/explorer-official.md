# AX Explorer — 官方/监管/云管线（Official / Regulatory / Cloud Pipeline）· 奥兰群岛（Åland Islands）数据中心发现方法论

国家：**AX 奥兰群岛（Åland Islands）**；瑞典语 **Åland**，芬兰语 **Ahvenanmaa**。已核对 manifest 条目：

```json
{"country_code":"AX","country_name":"Aland Islands","subnational_type":"country","divisions":["Aland Islands"]}
```

行政区划模型：**全国只有一个 manifest division：`Aland Islands`**。实际搜索与证据归档可按 16 个市镇（kommuner / municipalities）做检索桶，但不要把市镇写成 manifest division。

可靠性分级（Reliability grades）：
- **A** = 一手、官方或可问责来源：政府/议会/市政文件，法定许可，电信与能源监管文件，电力公司文件，运营商官方设施页，官方云区域页，TED/Hilma 采购，YTJ/PRH 公司登记，ÅSUB/StatFi 官方统计。
- **B** = 强二级来源：成熟新闻媒体、行业协会、研究报告、TeleGeography、与一手记录一致的运营商新闻稿。
- **C** = 弱线索：聚合器、自报目录、社交媒体、无出处地图、顾问摘要、营销材料、签约仪式报道。

---

## 0. 结论先行（Market assessment）

截至 2026-08-12 复核，AX **极不可能存在可枚举的商业数据中心市场**：未发现 Åland 云区域，未发现公开 colocation / hyperscale 设施，Ålcom 公开页面显示的是宽带、移动、电视、Webbhotell 与 AX 域名等服务，不构成数据中心设施证据。发现工作应按「快速证伪」执行：先扫官方、监管、电力、采购和运营商表面；无信号则记录为「无市场/未发现」。

### 0.1 已复核事实（Verified facts）

| 事实 | 证据表面 | 级别 | 方法论含义 |
|---|---|---:|---|
| Åland 为芬兰自治、非军事化、瑞典语区域，人口约 3 万，Mariehamn 超过 40% 人口 | https://www.aland.ax/en/facts-about-aland/facts-about-aland；https://um.fi/the-special-status-of-the-aland-islands | A | 小市场，优先证伪而非深挖 |
| Åland 官方资料确认有 16 个市镇 | https://www.aland.ax/en/facts-about-aland/municipalities | A | 市镇仅作检索桶；manifest division 仍为 `Aland Islands` |
| AWS、Azure、Google Cloud、Oracle Cloud 官方区域页未命中 Åland / Aland Islands / Ahvenanmaa | 官方云区域页，2026-08-12 页面文本复核 | A | 无云区域；未来每轮重查 |
| Kraftnät Åland 是 Åland 输电系统运营方；其 stamnät 页面说明 Sweden cable 80 MW、现有取电受订阅容量限制 | https://www.kraftnat.ax/stamnatet/ | A | 大型 DC 供电信号应出现在电网/连接文件 |
| ÅL-Link / Finland cable 为 100 MW 级 HVDC 连接、2015 投运 | https://www.nib.int/news/nib-finances-energy-cable-between-aland-islands-and-mainland-finland；https://www.nordpoolgroup.com/en/message-center-container/newsroom/exchange-message-list/2013/Q1/No-062013---New-submarine-cable-Aland---continental-Finland-impacts-on-transmission-capacities-between-Finland-and-Sweden/ | A/B | 电力安全项目，不是 DC 项目 |
| Ålands Elandelslag canonical URL 为 https://www.el.ax；Mariehamns Energi canonical URL 为 https://energi.ax | live URL check / official search results | A | 替换原稿中的错误能源域名 |
| Ålands miljö- och hälsoskyddsmyndighet（ÅMHM）是环境与健康许可/监管机构，官方 URL 为 https://www.amhm.ax | https://www.amhm.ax；https://www.regeringen.ax/understallda-myndigheter/alands-miljo-halsoskyddsmyndighet | A | 环境许可应查 ÅMHM 与 regeringen.ax |
| Ålcom 官网有 Webbhotell & AX-domän；未发现 colocation/serverhall/datahall 设施披露 | https://www.alcom.ax/privat/produkter/webbhotell-ax-doman | A（服务存在）/ C（设施推断不成立） | Web hosting 不等于可枚举 DC |

---

## 1. AX 结构事实（Structure facts）

1. **自治地位**：Åland 是芬兰的自治、非军事化、瑞典语地区，有自己的议会（Lagtinget）与政府（Ålands landskapsregering）。  
   English: Åland is an autonomous, demilitarised, Swedish-speaking region of Finland.
2. **单一 division**：数据库/manifest 层只使用 `Aland Islands`。16 个市镇只用于查询覆盖与候选定位。
3. **税收特区**：Åland 在欧盟 VAT 区外；这影响贸易、物流和账单处理，但不是设施证据。
4. **电信**：芬兰国家电信监管由 Traficom 执行；Åland 本地主要运营商为 Ålands Telekommunikation Ab / Ålcom。
5. **电力**：Kraftnät Åland 负责输电；Ålands Elandelslag 与 Mariehamns Energi 是关键本地配电/能源表面；芬兰侧对照 Fingrid。
6. **无 DC 注册库**：不存在单独数据中心登记表；必须通过规划/建筑许可、环境许可、电力连接、采购、运营商设施页交叉验证。
7. **无云区域**：官方云区域页当前无 Åland。最近真实云/DC 市场在 Stockholm、Helsinki/Hamina、其他芬兰大陆节点。

---

## 2. 官方/监管管线（Official / regulatory pipeline）

### 2.1 Ålands landskapsregering（政府）

- URL：https://www.regeringen.ax
- 级别：**A**
- 用途：政策、新闻、采购、能源、环境、基础设施、法律草案、政府物业项目。任何大型 DC 投资、公共 IT 采购或能源接入争议都可能在此留下记录。
- 查询模板：

```text
site:regeringen.ax datacenter
site:regeringen.ax serverhall
site:regeringen.ax datahall
site:regeringen.ax datacentral
site:regeringen.ax konesali
site:regeringen.ax "digital infrastruktur"
site:regeringen.ax upphandling server
site:regeringen.ax "elanslutning" data
site:regeringen.ax "miljötillstånd" data
```

### 2.2 Ålands lagting（议会）

- URL：https://www.lagtinget.ax
- 级别：**A**
- 用途：landskapslag、预算、议会问题、委员会材料。用于验证是否存在 DC 激励、能源例外、规划法变更或数据保护争议。
- 查询模板：

```text
site:lagtinget.ax datacenter
site:lagtinget.ax serverhall
site:lagtinget.ax datahall
site:lagtinget.ax "digital infrastruktur"
site:lagtinget.ax "dataskydd"
```

### 2.3 官方统计（ÅSUB / Statistics Finland）

- ÅSUB：https://www.asub.ax
- Statistics Finland：https://stat.fi
- 级别：**A**（统计事实），**B**（市场上下文）
- 用途：人口、企业结构、能源、ICT、劳动力。AX 市场小，统计用于校验「是否值得深挖」。
- 查询模板：

```text
site:asub.ax befolkning kommun
site:asub.ax energi Åland
site:asub.ax företag IT
site:stat.fi Ahvenanmaa tietotekniikka
```

### 2.4 市政规划与建筑许可（Municipal planning & building permits）

- Mariehamn：https://www.mariehamn.ax
- 其他市镇见 §3 矩阵；本轮复核确认 `{municipality}.ax` 形式的 15 个非 Mariehamn 市镇站点均可访问。
- 级别：**A**（市政决议、planläggning、bygglov）
- 用途：大型机房会涉及 bygglov、详细规划、用地变更、消防/环境条件或公用事业连接。
- 查询模板：

```text
site:mariehamn.ax bygglov server
site:mariehamn.ax datahall
site:mariehamn.ax datacenter
site:{kommun}.ax bygglov server
site:{kommun}.ax datahall
site:{kommun}.ax datacenter
"{kommun}" "bygglov" "serverhall" Åland
"{kommun}" "detaljplan" "datahall" Åland
```

### 2.5 电信监管与本地运营商（Telecom regulation & operator）

- Traficom：https://www.traficom.fi
- Ålcom：https://www.alcom.ax
- 级别：Traficom **A**；Ålcom 官方服务页 **A**；从 Web hosting 推断设施 **C/不可入库**
- 用途：Traficom 查电信网络、编号、频谱、NIS2/安全要求；Ålcom 查企业服务、wholesale、Metro Ethernet、Webbhotell、任何 colocaton/serverhall 页面。
- 已核验：Ålcom 有 `Webbhotell & AX-domän`，描述为网站空间、邮箱、DNS、备份等服务；未发现公开 colocation/serverhall/datahall 设施披露。
- 查询模板：

```text
site:traficom.fi Åland telecom
site:traficom.fi Ahvenanmaa tele
site:alcom.ax webbhotell
site:alcom.ax hosting
site:alcom.ax serverhall
site:alcom.ax datahall
site:alcom.ax colocation
"Ålands Telekommunikation" "serverhall"
```

### 2.6 电力/电网（Power & grid）

- Kraftnät Åland：https://www.kraftnat.ax
- Ålands Elandelslag：https://www.el.ax
- Mariehamns Energi：https://energi.ax
- Fingrid：https://www.fingrid.fi
- 级别：**A**
- 用途：大型负荷连接、电网容量、海缆、备用发电、输配电边界。DC 级项目如果真实存在，通常至少能在电力连接、容量升级、用地或环境许可中留痕。
- 查询模板：

```text
site:kraftnat.ax data
site:kraftnat.ax server
site:kraftnat.ax "elanslutning"
site:kraftnat.ax "stamnät"
site:el.ax "ny elanslutning"
site:el.ax datahall
site:energi.ax server
"Kraftnät Åland" datacenter
"Åland" "elanslutning" "datacenter" MW
"Åland" "serverhall" MW
```

### 2.7 环境许可（Environmental permits）

- ÅMHM：https://www.amhm.ax
- 政府下属机构页：https://www.regeringen.ax/understallda-myndigheter/alands-miljo-halsoskyddsmyndighet
- 级别：**A**
- 用途：miljötillstånd、tillsyn、燃油备用电源、冷却、水使用、噪声。小型设备间可能没有可见环境许可；大型设施应有痕迹。
- 查询模板：

```text
site:amhm.ax datahall
site:amhm.ax serverhall
site:amhm.ax "miljötillstånd" data
site:regeringen.ax "miljökonsekvensbedömning" data
"Åland" "miljötillstånd" "datacenter"
"ÅMHM" "serverhall"
```

### 2.8 海缆/登陆站（Submarine cables & landing stations）

- Ålcom 网络/wholesale 页面：https://www.alcom.ax
- TeleGeography：https://www.telegeography.com
- Submarine Cable Map：https://www.submarinecablemap.com
- 级别：Ålcom **A**；TeleGeography **B**；Submarine Cable Map 默认 **C**
- 用途：判断是否有可支持 DC 的国际互联枢纽。电力海缆或区域光缆新闻不能直接计为 DC 项目。
- 查询模板：

```text
"Åland" "submarine cable" fibre landing
"Åland" "sjökabel" fiber
"Ålcom" kabel Finland Sverige
"Åland" "landing station"
site:submarinecablemap.com Åland
```

### 2.9 云区域官方页（Cloud region official pages）

截至 2026-08-12，下列官方页面文本检索 `Åland / Aland Islands / Ahvenanmaa` 均为 0 命中：

```text
https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
https://cloud.google.com/about/locations
https://www.oracle.com/cloud/public-cloud-regions/
```

级别：**A**。若未来出现 Åland，应立即升级为高优先级官方信号，并核对区域/Local Zone/edge location 的准确类型。

### 2.10 政府采购/招标（Public procurement）

- EU TED：https://ted.europa.eu
- Finnish Hilma：https://www.hankintailmoitukset.fi
- Åland 政府采购：regeringen.ax 站内 `upphandling`
- 市政采购：各市镇站点
- 级别：**A**
- 用途：公共 IT、服务器、托管、灾备、网络、建筑、电力工程。采购只能证明需求或合同，不自动证明设施所在地。
- 查询模板：

```text
site:ted.europa.eu Åland datacenter
site:ted.europa.eu Ahvenanmaa server
site:hankintailmoitukset.fi Åland server
site:hankintailmoitukset.fi Ahvenanmaa konesali
site:regeringen.ax upphandling server
site:regeringen.ax upphandling IT
"Ålands landskapsregering" upphandling "datahall"
```

### 2.11 公司登记（Company registry）

- PRH：https://www.prh.fi
- YTJ：https://ytj.fi（curl 直连可能拒绝/超时，但为芬兰官方 BIS 入口；必要时从 PRH 或 Suomi.fi 链接进入）
- 级别：**A**
- 用途：核验公司实体、Business ID、注册地址、行业代码、SPV。Åland 公司仍在芬兰公司登记体系中核查。
- 查询模板：

```text
site:prh.fi "Ålands Telekommunikation"
site:ytj.fi "Åland" "data"
"Åland" datacenter Ab
"Åland" serverhall Ab
"Ahvenanmaa" datakeskus yritys
```

---

## 3. Division / 市镇覆盖矩阵（Coverage matrix）

Manifest division：`Aland Islands`。市镇桶（16）如下；这些是检索覆盖单位，不是 subnational divisions。

| 市镇 | 官方站点 | 优先级 | 重点表面 |
|---|---|---:|---|
| Mariehamn | https://www.mariehamn.ax | 高 | 市政 IT、政府/银行/航运总部、建筑许可、Mariehamns Energi |
| Jomala | https://www.jomala.ax | 高 | Maxinge/企业区、Ålcom、ÅMHM、用地/电力连接 |
| Finström | https://www.finstrom.ax | 中高 | Godby、主岛北部企业/电力 |
| Sund | https://www.sund.ax | 中 | 主岛东部规划、电力 |
| Saltvik | https://www.saltvik.ax | 中 | 主岛北部、配电 |
| Hammarland | https://www.hammarland.ax | 中 | Tellholm/Sverige cable 区域、电网 |
| Eckerö | https://www.eckero.ax | 中 | 渡口/海缆线索 |
| Lemland | https://www.lemland.ax | 中 | Långnäs/港口、能源/网络 |
| Lumparland | https://www.lumparland.ax | 低 | Långnäs 周边 |
| Vårdö | https://www.vardo.ax | 低 | 群岛连接 |
| Geta | https://www.geta.ax | 低 | 低密度覆盖 |
| Föglö | https://www.foglo.ax | 低 | 群岛覆盖 |
| Kökar | https://www.kokar.ax | 低 | 群岛覆盖 |
| Sottunga | https://www.sottunga.ax | 低 | 群岛覆盖 |
| Kumlinge | https://www.kumlinge.ax | 低 | 群岛覆盖 |
| Brändö | https://www.brando.ax | 低 | 群岛覆盖 |

通用模板：

```text
"{kommun}" "datacenter" Åland
"{kommun}" "serverhall" Åland
"{kommun}" "datahall" Åland
"{kommun}" "konesali"
"{kommun}" bygglov server
site:{kommun}.ax server
site:{kommun}.ax datahall
site:{kommun}.ax upphandling IT
```

---

## 4. 入库判定规则（Evidence acceptance rules）

- **可入库设施**：必须有 A 级官方/运营商设施页，或 B 级报道加 A 级许可/采购/电力连接交叉验证。
- **不可入库**：Webbhotell、邮箱、DNS、宽带、Metro Ethernet、交换局、基站、政府普通服务器采购、云服务转售，除非明确披露客户托管/colocation 或独立 datahall。
- **状态语义**：`planerar / announced / MoU` = 线索；`bygglov / elanslutning / miljötillstånd / upphandling` = 真实项目证据但未必在建；运营商设施页或开业公告 + 地址 = 运营/近运营。
- **容量语义**：优先官方 IT load MW；其次电力连接容量、机架数、面积。园区总 MW 与已投产 MW 分开存储。
- **负结果语义**：聚合器无记录不是 A 级负证据；官方/监管/采购/运营商表面均无信号时，才记录「未发现商业 DC 市场」。

---

## 5. 快速 URL 索引（Quick-reference index）

| 表面 | URL | 级别 | 复核状态 |
|---|---|---:|---|
| Åland 政府 | https://www.regeringen.ax | A | 200 |
| Åland 议会 | https://www.lagtinget.ax | A | 200 |
| Åland 官方门户 | https://www.aland.ax | A | 200 |
| ÅSUB | https://www.asub.ax | A | 200 |
| Mariehamn 市 | https://www.mariehamn.ax | A | 200 |
| Traficom | https://www.traficom.fi | A | 200 |
| Kraftnät Åland | https://www.kraftnat.ax | A | 200 |
| Ålands Elandelslag | https://www.el.ax | A | 200 |
| Mariehamns Energi | https://energi.ax | A | 200/search verified |
| ÅMHM | https://www.amhm.ax | A | 200/search verified |
| Fingrid | https://www.fingrid.fi | A | 200 |
| Ålcom | https://www.alcom.ax | A | 200 |
| EU TED | https://ted.europa.eu | A | 202 |
| Hilma | https://www.hankintailmoitukset.fi | A | 200 |
| PRH | https://www.prh.fi | A | 200 |
| YTJ | https://ytj.fi | A | official URL; direct curl returned 000 |
| AWS Regions | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | A | 200; no AX hit |
| Azure Geographies | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ | A | 200; no AX hit |
| Google Cloud locations | https://cloud.google.com/about/locations | A | 200; no AX hit |
| Oracle Cloud regions | https://www.oracle.com/cloud/public-cloud-regions/ | A | 200; no AX hit |
| Submarine Cable Map | https://www.submarinecablemap.com | C | aggregator only |
| TeleGeography | https://www.telegeography.com | B | industry/reference |

---

## 6. 执行顺序（CHECK list）

1. 用 `regeringen.ax`、`lagtinget.ax`、ÅMHM 查 `datacenter / datahall / serverhall / konesali / miljötillstånd / upphandling`。
2. 查 Mariehamn、Jomala、Finström、Sund、Hammarland、Lemland/Eckerö 的 bygglov、detaljplan、upphandling。
3. 查 Kraftnät Åland、el.ax、energi.ax 的大型连接、电网扩容和备用电源文件。
4. 查 Ålcom 官方企业/wholesale/Webbhotell 页面；Web hosting 只记为服务，不记设施。
5. 查 AWS/Azure/GCP/OCI 官方区域页是否新增 Åland、Aland Islands、Ahvenanmaa。
6. 查 TED/Hilma 与 PRH/YTJ 的采购和实体线索。
7. 再用 explorer-industry.md 的媒体/行业表面补充线索。
8. 全部无 A/B 信号时，结论写为：`Aland Islands: no commercial data center facilities found in verified official/regulatory/operator surfaces`。
