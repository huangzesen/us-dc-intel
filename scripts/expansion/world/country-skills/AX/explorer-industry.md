# AX Explorer — 行业/媒体/厂商发现（Industry / Trade Press / Vendor Discovery）· 奥兰群岛（Åland Islands）数据中心发现方法论

国家：**AX 奥兰群岛（Åland Islands）**；瑞典语 **Åland**，芬兰语 **Ahvenanmaa**。已核对 manifest：

```json
{"country_code":"AX","country_name":"Aland Islands","subnational_type":"country","divisions":["Aland Islands"]}
```

本文件覆盖贸易媒体、行业协会、运营商/厂商页面、聚合器、瑞典语/芬兰语/英语查询模板和分级规则。**正式 division 只有 `Aland Islands`；16 个市镇仅作检索桶。**

可靠性分级：**A** = 官方/监管/运营商一手披露；**B** = 成熟媒体、行业协会、强研究报告；**C** = 聚合器、自报、社交、营销、缺少一手出处的宣传。行业侧线索要回到 explorer-official.md 的 A 级表面定稿。

---

## 0. AX 特定市场框架（AX-specific frame）

- **语言覆盖**：瑞典语是最重要检索语言；芬兰侧资料用芬兰语；国际行业媒体用英语。
- **主要关键词**：`datahall`、`serverhall`、`datacenter`、`datacentral`、`kolokalisering`、`IT-infrastruktur`、`molntjänst`；芬兰语 `konesali`、`datakeskus`、`palvelinkeskus`、`palvelinhuone`、`pilvipalvelu`；英语 `data center`、`data centre`、`colocation`、`colo`、`edge`、`hosting`、`server farm`、`cloud region`。
- **市场判断**：截至 2026-08-12，AX 极不可能有公开商业 DC 市场。Ålcom 有 Webbhotell/AX-domain 服务，但未发现公开 colocation / serverhall / datahall 披露；四大云官方区域页未命中 Åland。
- **候选类型**：可能存在本地运营商机房、市政 IT 机房、银行/航运自用机房，但这些默认不是可枚举商业 DC，除非有明确客户托管、设施地址、许可或运营商设施页。
- **对照市场**：芬兰大陆 Helsinki/Hamina/Turku 与瑞典 Stockholm 是最近真实 DC 市场。任何「服务 Åland」或「连接 Åland」报道都要区分设施是否实际在 AX。

---

## 1. 高信号媒体（High-signal media）

### 1.1 Åland 本地媒体

| 来源 | URL | 用途 | 级别 |
|---|---|---|---:|
| Nya Åland | https://www.nyan.ax | 本地项目、市政、能源、电信、企业新闻；若有 AX DC，极可能出现 | B |
| Ålandstidningen | https://www.alandstidningen.ax | 本地商业/政府/能源报道 | B |
| Ålands Radio och TV | https://www.alandsradio.ax | 公共广播；政府、电网、电信、公共采购 | B |
| Åland 官方信息门户 | https://www.aland.ax | 事实、政府介绍、招商/生活信息 | A/B |

查询模板：

```text
site:nyan.ax datacenter
site:nyan.ax serverhall
site:nyan.ax datahall
site:nyan.ax datacentral
site:alandstidningen.ax datacenter
site:alandstidningen.ax serverhall
site:alandsradio.ax datahall
site:alandsradio.ax serverhall
"Åland" "serverhall"
"Åland" "datahall"
"Åland" "datacenter" ("planerar" OR "bygger" OR "öppnar" OR "inviger")
```

### 1.2 芬兰/瑞典商业与技术媒体

| 来源 | URL / 查询方式 | 用途 | 级别 |
|---|---|---|---:|
| Hufvudstadsbladet | https://www.hbl.fi | 芬兰瑞典语政策/商业报道 | B |
| Yle / Svenska Yle | https://yle.fi | 公共媒体；能源、区域经济、技术 | B |
| Kauppalehti | https://www.kauppalehti.fi | 芬兰商业投资、公司新闻 | B |
| Tekniikka & Talous / Tivi / Talouselämä | site-scoped | 芬兰 IT/DC/能源报道 | B |
| Dagens Industri | https://www.di.se | 瑞典/北欧资本与产业新闻 | B |
| Computer Sweden / Ny Teknik | site-scoped | 瑞典 IT/基础设施新闻 | B |

查询模板：

```text
site:hbl.fi Åland datacenter
site:hbl.fi Åland serverhall
site:yle.fi Ahvenanmaa datakeskus
site:yle.fi Ahvenanmaa konesali
site:kauppalehti.fi Ahvenanmaa datakeskus
site:tekniikkatalous.fi Ahvenanmaa konesali
site:tivi.fi Åland datacenter
site:di.se Åland datacenter
"Ahvenanmaa" "datakeskus"
"Maarianhamina" "konesali"
```

### 1.3 国际数据中心/互联媒体

| 来源 | URL / 查询方式 | 用途 | 级别 |
|---|---|---|---:|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com | 北欧 DC 新闻；已见 Finland 市场报道但未见 AX 设施信号 | B |
| Capacity Media | https://www.capacitymedia.com | 互联、海缆、运营商交易 | B |
| Data Center Knowledge | https://www.datacenterknowledge.com | 国际 DC 新闻 | B |
| Dgtl Infra / W.Media | site-scoped | 投资与市场报道 | B/C |

查询模板：

```text
site:datacenterdynamics.com Åland
site:datacenterdynamics.com "Aland Islands"
site:capacitymedia.com Åland submarine cable data center
site:datacenterknowledge.com Åland datacenter
"Aland Islands" "data center" "colocation"
"Åland" ("hyperscale" OR "edge data center")
```

媒体规则：媒体只能证明「有报道」。设施状态、容量、位置必须回到官方许可、运营商设施页、采购、电力连接或公司登记核实。

---

## 2. 行业协会、政策机构与研究（Associations, policy & research）

| 机构/来源 | URL | 用途 | 级别 |
|---|---|---|---:|
| Ålands Näringsliv | https://www.an.ax | 本地商业生态、企业倡议、数字化议题 | A/B |
| Finnish Data Center Association (FDCA) | https://www.fdca.fi | 芬兰 DC 市场、会员、政策报告；AX 若出现即高信号 | B |
| TIVIA | https://www.tivia.fi | 芬兰 IT 社群/事件；konesali/云服务上下文 | B |
| European Data Centre Association (EUDCA) | https://www.eudca.org | 欧洲 DC 政策/统计背景 | B |
| JLL / CBRE / Cushman & Wakefield 北欧 DC 报告 | site-scoped | 城市级市场报告；AX 几乎不会出现，出现即线索 | B |
| TeleGeography | https://www.telegeography.com | 海缆/互联参考 | B |
| Submarine Cable Map | https://www.submarinecablemap.com | 海缆地图聚合 | C |

查询模板：

```text
site:an.ax datacenter
site:an.ax serverhall
site:an.ax digitalisering
site:fdca.fi Åland
site:fdca.fi Ahvenanmaa
site:tivia.fi Åland konesali
"Åland" "data center" report filetype:pdf
"Ahvenanmaa" "datakeskus" raportti filetype:pdf
"Åland" "digital infrastruktur" rapport
```

---

## 3. 运营商/厂商页面（Operator / vendor pages）

| 主体 | URL / 查询方式 | AX 相关信号 | 级别 |
|---|---|---|---:|
| Ålcom / Ålands Telekommunikation Ab | https://www.alcom.ax | 本地主要电信运营商；Webbhotell、wholesale、Metro Ethernet；未发现公开 colocation/serverhall 披露 | A（服务页）/ C（设施推断） |
| Ålcom Webbhotell & AX-domän | https://www.alcom.ax/privat/produkter/webbhotell-ax-doman | Web hosting、邮箱、DNS、备份；不是设施证据 | A（服务） |
| Elisa / Telia / DNA | site-scoped | 芬兰/北欧运营商服务覆盖；通常不是 AX 设施 | B/C |
| Tietoevry | https://www.tietoevry.com | 政府/企业 IT 托管线索；需核实设施所在地 | B |
| Ålandsbanken | https://www.alandsbanken.ax | 银行自用 IT/外包线索；默认不可入库 | C |
| Eckerö Line / Viking Line / shipping operators | site-scoped | 航运 IT/灾备线索；默认不可入库 | C |
| PeeringDB | https://www.peeringdb.com | Mariehamn/Åland POP、网络自报 | C |
| Baxtel / DataCenterMap / Cloudscene / datacenters.com | site-scoped | 聚合设施条目；AX 空结果属预期 | C |

查询模板：

```text
site:alcom.ax webbhotell
site:alcom.ax hosting
site:alcom.ax serverhall
site:alcom.ax datahall
site:alcom.ax colocation
site:alcom.ax "Metro Ethernet"
"Ålcom" "serverhall"
"Ålands Telekommunikation" "datahall"
"Åland" hosting server Ab
"Åland" colocation
peeringdb Åland
peeringdb Mariehamn
site:baxtel.com Åland
site:datacentermap.com Åland
site:cloudscene.com Åland
```

---

## 4. 市镇 × 来源枚举矩阵（Municipality enumeration matrix）

Division = `Aland Islands`。行是检索桶；列是来源类型。每一行至少跑一组媒体 + 市政 + 电力/运营商查询；高优先级行加查采购与公司登记。

| 市镇 | 媒体（B） | 市政/规划（A） | 电力（A） | 运营商/厂商（A/B/C） | 优先级 |
|---|---|---|---|---|---:|
| Mariehamn | Nya Åland / Ålandstidningen / Radio | mariehamn.ax | energi.ax / kraftnat.ax | Ålcom、银行、政府 IT | 高 |
| Jomala | 同上 | jomala.ax | el.ax / kraftnat.ax | Ålcom、ÅMHM、企业区 | 高 |
| Finström | 同上 | finstrom.ax | el.ax / kraftnat.ax | Ålcom、本地主岛网络 | 中高 |
| Sund | 同上 | sund.ax | el.ax / kraftnat.ax | Ålcom | 中 |
| Saltvik | 同上 | saltvik.ax | el.ax / kraftnat.ax | Ålcom | 中 |
| Hammarland | 同上 | hammarland.ax | kraftnat.ax / el.ax | Sweden cable 区域线索 | 中 |
| Eckerö | 同上 | eckero.ax | el.ax / kraftnat.ax | 海缆/渡口线索 | 中 |
| Lemland | 同上 | lemland.ax | el.ax / kraftnat.ax | Långnäs/港口线索 | 中 |
| Lumparland | 同上 | lumparland.ax | el.ax | Långnäs 周边 | 低 |
| Vårdö | 同上 | vardo.ax | el.ax | 群岛网络 | 低 |
| Geta | 同上 | geta.ax | el.ax | 群岛/主岛边缘 | 低 |
| Föglö | 同上 | foglo.ax | el.ax | 群岛网络 | 低 |
| Kökar | 同上 | kokar.ax | el.ax | 群岛网络 | 低 |
| Sottunga | 同上 | sottunga.ax | el.ax | 群岛网络 | 低 |
| Kumlinge | 同上 | kumlinge.ax | el.ax | 群岛网络 | 低 |
| Brändö | 同上 | brando.ax | el.ax | 群岛网络 | 低 |

通用模板：

```text
"{kommun}" "datacenter" Åland
"{kommun}" "data center" "Aland Islands"
"{kommun}" "serverhall" Åland
"{kommun}" "datahall" Åland
"{kommun}" "konesali"
"{kommun}" "bygglov" "server"
"{kommun}" "upphandling" IT
site:{kommun}.ax server
site:{kommun}.ax datahall
```

---

## 5. 查询模板总集（Cookbook）

```text
# 瑞典语 / Swedish
"Åland" "serverhall"
"Åland" "datahall"
"Åland" "datacenter"
"Åland" "datacentral"
"Åland" "kolokalisering"
"Åland" "IT-infrastruktur"
"Åland" "elanslutning" data
"Åland" upphandling server
"Åland" planerar datahall
"Mariehamn" serverhall

# 芬兰语 / Finnish
"Ahvenanmaa" "konesali"
"Ahvenanmaa" "datakeskus"
"Ahvenanmaa" "palvelinkeskus"
"Ahvenanmaa" "palvelinhuone"
"Maarianhamina" "konesali"
"Ahvenanmaa" "sähköliittymä" "datakeskus"

# 英语 / English
"Åland" "data center"
"Aland Islands" "data centre"
"Aland Islands" "colocation"
"Åland" "server farm"
"Åland" "cloud region"
"Åland" "submarine cable" "landing"
"Åland" ("hyperscale" OR "edge data center")
```

---

## 6. 分级与升级规则（Grading and escalation）

- **A 级可直接定稿**：运营商设施页明确写 colocation/serverhall/datahall 并给出位置；政府/市政 bygglov；ÅMHM 环境许可；Kraftnät/el.ax/energi.ax 电力连接；TED/Hilma 采购；官方云区域页；PRH/YTJ 实体登记。
- **B 级仅作线索/佐证**：Nya Åland、Ålandstidningen、Ålands Radio、HBL、Yle、Kauppalehti、DCD、FDCA、TeleGeography 等。
- **C 级不可单独入库**：PeeringDB、Baxtel、DataCenterMap、Cloudscene、Submarine Cable Map、自媒体、LinkedIn、Facebook、营销页、签约仪式。
- **升级**：B 级媒体 + A 级许可/电力/运营商页 = 可入库；C 级聚合器 + A 级官方页 = 可入库；C 级孤证 = 不入库。
- **降级**：只出现 `hosting/webbhotell/DNS/email/cloud service`，没有客户托管或设施披露，降为服务线索，不计 DC。

---

## 7. 实操陷阱（Pitfalls）

- **拼写召回**：必须同时搜 `Åland`、`Aland`、`Aland Islands`、`Ahvenanmaa`、`Mariehamn`、`Maarianhamina`。
- **Web hosting ≠ colocation**：Ålcom Webbhotell 说明网站空间、邮箱、DNS、备份；它不是公开可枚举数据中心。
- **电信机房 ≠ DC**：交换局、基站、POP、Metro Ethernet 节点只有在提供第三方托管/colocation 且可定位时才算候选。
- **电力/海缆新闻 ≠ DC 项目**：Sweden/Finland 电力海缆、区域光缆、风电扩容只说明基础设施背景。
- **芬兰/瑞典服务覆盖 ≠ AX 设施**：运营商服务 Åland 客户不代表设施在 Åland。
- **聚合器空结果不是强证据**：空结果符合预期；最终负结论要来自官方/监管/采购/运营商表面无信号。
- **本地媒体语义**：`datacenter` 可能指政府机房、学校服务器间或软件平台；需要地址、许可或运营商设施页确认。

---

## 8. 行业侧 CHECK 顺序（Industry-side checklist）

1. Nya Åland、Ålandstidningen、Ålands Radio：跑 `datacenter / datahall / serverhall / konesali`。
2. Ålcom：核查 `webbhotell / hosting / serverhall / datahall / colocation / Metro Ethernet`，区分服务与设施。
3. Ålands Näringsliv、FDCA、TIVIA：查 Åland/Ahvenanmaa 是否出现在 DC、数字基础设施或投资报告。
4. DCD、Capacity、Data Center Knowledge：查 Åland/Aland Islands 与 `data center / submarine cable / colocation`。
5. Kauppalehti、HBL、Yle、DI、Computer Sweden：查瑞典语/芬兰语关键词。
6. PeeringDB、Baxtel、DataCenterMap、Cloudscene：仅作发现；任何命中都回官方管线核实。
7. 全部无 A/B 信号时，与 explorer-official.md 结论合并：`Aland Islands: no commercial data center facilities found in verified official, operator, procurement, power, and industry surfaces`。
