---
name: va-datacenter-methodology
location: scripts/expansion/world/country-skills/VA/SKILL.md
description: 圣座/梵蒂冈数据中心查询方法论：唯一 Holy See 分区，确认 DTSI 公共部门 datacenters 而商业 colo/云区域不存在，字段级分级且地址容量不推断。Holy See datacenter methodology: single Holy See division, DTSI public-sector datacenters confirmed while commercial colo/cloud region absent, field-level grading without address/capacity inference.
---

# VA · 圣座/梵蒂冈数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：合并 explorer-official.md 与 explorer-industry.md 双线方法论，指导对 Holy See（VA）数据中心与数字基础设施证据的枚举、分级与边界排除。官方线覆盖总督府 DTSI、`.va`/IANA、官方云区域负向、能源与采购；行业线覆盖供应商（NTT DATA 等）、贸易媒体与目录否定。核心规则：唯一分区 `Holy See`；梵蒂冈城国边界内的接受设施才计入，罗马与治外地产默认排除。

## 入口

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | vaticanstate.va/vatican.va 官方站、DTSI 访谈、IANA `.va`、四大云官方区域列表负向、能源（Fratello Sole 光伏）、数据保护/安全/采购 |
| explorer-industry.md | 行业/厂商/媒体发现 | DTSI 等优先核验对象、NTT DATA/Vatican Library 数字化、贸易媒体、目录（Baxtel/DatacenterMap/Cloudscene/PeeringDB）、容量与地址提取规则 |

## 核心结构事实

1. **行政区划模型**：manifest `{"country_code":"VA","country_name":"Holy See","subnational_type":"country","divisions":["Holy See"]}`——仅 **1 个分区 `Holy See`**；不再拆分省市区，所有被接受设施必须归入 `Holy See` 并以物理位置是否在梵蒂冈城国边界内为准；罗马市内或圣座城外治外地产默认不计入 VA，除非项目规则明确把对应几何纳入。
2. **注册库现状**：VA 有官方可证的政府 ICT/datacenter 基础设施——总督府（Governatorato）下属 **Direzione delle Telecomunicazioni e dei Sistemi Informatici（DTSI）** 2024 官方访谈称职责包括数据网络、datacenter 管理、VoIP 公共交换、Cloud 平台、ERP 与网络安全；2026 官方访谈称数据在“datacenter presenti nello Stato”内驻留并处理，部分 datacenter 区域将工程化为 “AI ready”。未发现官方公开的商业 colocation、hyperscale campus 或公有云区域。
3. **法律与监管**：官方域名为 `vatican.va`、`vaticanstate.va`、`press.vatican.va`、`vaticannews.va`、`observatoreromano.va`；机构站有 `vaticanlibrary.va`、`digi.vatlib.it`、`archivioapostolicovaticano.va`、`museivaticani.va`；AAS《宗座公报》、梵蒂冈城国法律与官方公告；采购查 `bandi di gara`/`esiti di gara`/`appalti` 及 `vatican.va`/AAS 合同透明度法律；网络安全合作与 AI 治理（Rome Call for AI Ethics、AI 委员会）只作 posture 线索，不等于设施。
4. **互联与云**：IANA `.va` ccTLD manager 为 Holy See - Vatican City State / Governatorato S.C.V.，admin contact Department of Telecommunications（Palazzo del Belvedere）、technical contact Vatican Internet Service Provider（Cortile del Triangolo），列出 authoritative name servers；这些是联系地址，不得自动录为机房地址。AWS/Azure/Google Cloud/Oracle OCI 官方区域列表均无 Holy See / Vatican City region（A 级负向）；“cloud platform”“sovereign cloud”“Outposts/edge appliance”只说明服务或技术使用，不等于本地 region/AZ 或 commercial datacenter。
5. **设施/项目种子**：DTSI datacenters（operational，public-sector，地址/容量未公开，A 存在性）；Vatican Internet Service Provider / `.va` DNS（network infrastructure，A 网络身份）；Vatican Library 数字化（NTT DATA 2014 起合作，在线 manuscript 超 27,500 件，整体目标 82,000 manuscripts / 41 million pages，digitization infrastructure 非 colo）；Vatican Apostolic Archive 数字服务（机构线索，设施级不足）；Vatican Media/Musei Vaticani（数字服务需求，无设施级证据不建条目）；Santa Maria di Galeria agrivoltaic（2024 motu proprio Fratello Sole + 2026 Fondazione Fratello Sole）在意大利治外区域，排除出 VA facility count；Vatican Radio 发射台同样排除。
6. **语言与词汇**：官方模板必须至少跑英语和意大利语，拉丁语与中文补充（查询见模板）；状态词：`operational`、`proposed`、`under construction`（须官方公告/采购/许可或具名 B 级报道）、`not present`（云 region A 级负向）；地址/容量无字段级来源时保留 `null`/`undisclosed`，不得从建筑、DNS 联系地址或电力项目推断。
7. **可靠性分级**：A=官方/一手（vatican.va 系、AAS、IANA、四大云官方区域列表；供应商官方新闻稿只对其自身合作/产品/服务交付事实为 A）；B=强二手（Data Center Dynamics、CorCom、Il Sole 24 Ore、Wired Italia、ComputerWeekly、The Register、Catholic News Service 等具名作者/日期/当事方报道）；C=弱来源（目录、聚合页、SEO 页、未署名转载、论坛、无法打开或缺少原始出处）；U=不可复核。字段级评分：同一来源可对“机构/项目存在”给 A，但对“地址/容量”不给分或给 C。
8. **计数与去重规则**：供应商新闻稿可证明合作/系统上线，不自动证明物理数据中心位置或容量；数字化基础设施（Library/Archive）与 datacenter/colo 分开统计；广播/媒体基础设施（Vatican Media、Radio、流媒体/演播室）可作 ICT 线索，Santa Maria di Galeria 发射台排除；光伏/电网/UPS/发电机是背景或依赖项，不等于 datacenter，有 MWh/kW 报道时保留原单位不换算为 capacity；目录-only 线索为 C 级种子，无官方或具名二手来源确认时不得进入最终清册；无公开 MW 来源时 `capacity_mw: null`。

## 常用查询模板

```text
site:vaticanstate.va "Direzione delle Telecomunicazioni e dei Sistemi Informatici"
site:vaticanstate.va "gestione di datacenter"
site:vaticanstate.va "datacenter presenti nello Stato"
site:vaticanstate.va "centro elaborazione dati" OR "Ced"
site:vaticanstate.va "piattaforma Cloud" "Governatorato"
site:vatican.va "sistemi informatici" "Città del Vaticano"
site:iana.org/domains/root/db va "Holy See"
"Vatican Internet Service Provider" "Cortile del Triangolo"
"Department of Telecommunications" "Palazzo del Belvedere" "Vatican"
"Vatican" "+39 06 698" telecommunications
site:vaticanstate.va "reti internet" "Stato della Città del Vaticano"
site:press.vatican.va "Fratello Sole" "Santa Maria di Galeria"
site:vaticannews.va "agrivoltaic" "Santa Maria di Galeria"
site:vatican.va "Fondazione Fratello Sole"
site:vaticanstate.va "Centro di elaborazione dati" "trasformatori"
"Città del Vaticano" UPS "gruppo elettrogeno"
site:vaticanstate.va "bando di gara" informatica
site:vaticanstate.va "gara" "telecomunicazioni"
site:vaticanstate.va "appalto" "sistemi informatici"
site:vatican.va "Per la trasparenza" appalti
site:vaticanstate.va "cybersicurezza" "Telecomunicazioni"
site:vaticanstate.va "Commissione sull'Intelligenza Artificiale"
"Holy See" "data center"
"Holy See" "data centre"
"Vatican City" "data center"
"Vatican City" "data centre"
"Città del Vaticano" "datacenter"
"Stato della Città del Vaticano" "datacenter"
"Santa Sede" "centro elaborazione dati"
"Città del Vaticano" "centro elaborazione dati" OR "Ced"
"Vaticano" "sala server" OR "sala macchine"
site:vaticanstate.va "AI ready" datacenter
site:vaticannews.va "data center" OR "centro dati"
"00120 Città del Vaticano" "server"
"Status Civitatis Vaticanae" "instrumenta informatica"
"Sancta Sedes" "bibliotheca digitalis"
"Palazzo del Belvedere" "data center" OR datacenter
"Cortile del Triangolo" "Vatican Internet Service Provider"
"Governatorato" "centro elaborazione dati"
"Vatican Media" "Città del Vaticano" "server"
"Biblioteca Apostolica Vaticana" "storage" OR "server"
"Musei Vaticani" "sala server" OR "sistemi informatici"
"Santa Maria di Galeria" "data center" OR "datacenter"
"Castel Gandolfo" "data center" OR server
"Lateran Palace" OR "Laterano" "data center"
"Santa Maria Maggiore" "server room"
"Bambino Gesù" "data center"
"via della Conciliazione" "data center"
"Rome" "Vatican" "data center" -"Città del Vaticano"
"Vatican" "datacenters" "sovereignty of data"
"Vatican" "AI-ready" "datacenter"
"Vatican" "server room" OR "data hall"
"Vatican Library" "NTT DATA" digitization storage
"Vatican Library" "AMlad" "storage"
"Vatican Apostolic Archive" IBM digitization
"Vatican" "new data center" 2024 OR 2025
"Vatican" "colocation" OR "colo"
"Vatican" "cloud region"
"Direzione delle Telecomunicazioni e dei Sistemi Informatici" datacenter
"Biblioteca Apostolica Vaticana" "NTT DATA"
"Archivio Apostolico Vaticano" digitalizzazione
"Vaticano" "nuovo data center"
"Sancta Sedes" "instrumenta informatica"
"Status Civitatis Vaticanae" "centrum datorum"
"bibliotheca digitalis" Vaticana
"圣座" "数据中心"
"梵蒂冈" "数据中心" OR "机房" OR "档案数字化"
site:datacenterdynamics.com Vatican "data center"
site:corrierecomunicazioni.it Vaticano "data center" OR digitale
site:ilsole24ore.com Vaticano "data center" OR digitale
site:wired.it Vaticano tecnologia OR "intelligenza artificiale"
site:baxtel.com Vatican "data center"
site:datacentermap.com Vatican "data center"
site:cloudscene.com Vatican "data center"
site:datacenters.com Vatican "data center"
site:peeringdb.com Vatican "facility" OR "exchange"
"Vatican Library" "27,500 manuscripts"
"Vatican Library" "82,000 manuscripts" "41 million pages"
"Vatican Library" "petabytes" OR "terabytes"
"Vatican" "datacenter" "MW" OR "megawatt"
"Città del Vaticano" "datacenter" "metri quadrati"
"Vatican" "PUE" "data center"
```

## 官方/监管管线要点（详见 explorer-official.md）

- 治理与 ICT 机构：`vaticanstate.va/it/sistemi-informatici.html` 说明 Servizio Sistemi Informatici 2018 年纳入总督府 DTSI（units：administration/support、systems、user support、application development）；2024-07-11 访谈（职责含数据网络、datacenter 管理、公共 VoIP 交换、Cloud 平台、ERP、IT infrastructure 与网络安全）；2026-02-17 访谈（数据主权主题，数据驻留并处理在 State 内 datacenters，部分区域 AI ready）。
- `.va`/DNS：IANA 记录是官方级网络身份来源；用于证明 `.va` 管理者、DNS 技术联系人、官方网络存在性（A）；用于生成官方域名/站点种子（A）；不用于证明 datacenter 地址（不充分）。
- 公有云不存在性：四大厂商官方列表无 VA region 时结论为 A 级“无公有云 region”；服务/技术使用（cloud platform、AWS technology、Azure services、Outposts/edge appliance）不等于本地 region/AZ 或 commercial datacenter。
- 能源与关键设施背景：Fratello Sole（2024-06-26 motu proprio + 2026-06-01 Chirograph 建 Fondazione Fratello Sole）在 Santa Maria di Galeria 治外区域建 agrivoltaic plant——物理在意大利罗马周边治外区域，不计入 VA datacenter division；光伏/电网/UPS/发电机只作供电背景，无官方容量字段不写 MW，有 MWh/kW 报道保留原单位。
- 档案/图书馆/文化机构：Vatican Library 数字化为 digitization infrastructure / storage and compute lead 而非 commercial DC；仅能证明在线平台或存储系统时不建独立 datacenter 条目；Archivio Apostolico Vaticano 官方站证明机构与数字服务存在，不能单独证明 datacenter；“IBM 合作（搜索/索引）”原始线索无稳定一手 IBM 新闻稿，只保留二次研究查询线索；Vatican Media/Musei 除非找到官方机房/数据中心/采购文件，否则不建独立 facility。
- 已核实官方级种子表：DTSI datacenters（operational public-sector，`Holy See`，地址未公开，A 存在性/地址容量 null）；Vatican ISP / `.va` DNS（network infrastructure，A 网络身份）；Vatican Library digital infrastructure（digitization，A 项目/容量用 manuscript/page 指标）；Vatican Apostolic Archive digital services（机构 A/设施细节不足）；Santa Maria di Galeria（能量/广播背景，排除）。
- 最终校验清单：manifest 唯一分区已覆盖；每个接受设施都有字段级来源；`.va`/IANA 只作网络身份和联系人证据；Library/Archive 数字化与 datacenter/colo 分开统计；Santa Maria di Galeria、Castel Gandolfo、Lateran、Santa Maria Maggiore、Bambino Gesù、Rome `Vatican` 商业地址作为跨境陷阱处理；无公开 MW 来源时 `capacity_mw: null`；目录或营销页不得提升到 A。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 市场形态：VA 是极小、主权/公共部门驱动的数据中心市场；公开证据集中在 DTSI 政府 ICT/datacenters、`.va`/Vatican ISP、图书馆与档案数字化、Vatican Media/Museums 数字服务；未发现公开商业 colocation、hyperscale campus、cloud region、IXP 或 carrier hotel 生态；行业目录空结果只能作 C 级否定佐证，不能替代一手核验。
- 优先核验对象：DTSI（A 存在性/地址容量 null）、DTSI data sovereignty / AI-ready（2026 访谈，A 确认境内 datacenters）、`.va`/Vatican ISP（A 网络身份）、Vatican Library/Digital Vatican Library（A digitization infrastructure 非 colo）、NTT DATA x Vatican Library（A 供应商项目事实：2014 合作约 3,000 manuscripts by 2018，2024 超 27,500 online；容量不换算 MW）、Vatican Apostolic Archive（A 机构/设施不足）、Vatican Media/Vatican News（A 机构/媒体服务）、Musei Vaticani（A/B 机构服务）、Rome Call for AI Ethics（A 倡议存在/C 设施推演）、public cloud regions（A 不存在性）。
- 需降级或剔除的原始待核实线索：“IBM 合作（档案馆/搜索/索引）”（本轮无稳定 IBM 官方新闻稿，保留查询不作已证设施）；“Dell EMC 三 PB 存储”（常见二手/百科转述，无一手 Dell/EMC 页面时只能 B/C 线索，不写容量字段）；“DCD 2024-2025 新建数据中心报道”（本轮只有 tag/search 页，无具体可打开报道；后续出现先按 B 级线索处理并回官方确认）。
- 目录与网络数据库：Baxtel/DatacenterMap/Cloudscene/Datacenters.com/PeeringDB 用于找 seed 或记录否定结论；空结果或只出现国家下拉框/营销表单：C 级“未发现公开 commercial colo”；目录中的 Rome/Italy 地址按意大利处理，不得归入 VA；PeeringDB 无 Vatican City exchange/facility 仅说明无公开登记的 IXP/facility 生态，不能证明没有私有政府网络。
- 容量与地址提取规则：DTSI datacenters 可写 status operational/operator Governatorato - DTSI/division Holy See/evidence_grade A，address null、capacity_mw null，备注“officially confirmed inside Vatican City State; precise locations undisclosed”；Library/NTT DATA 只提取 manuscript/page/online-item 指标；IANA `.va` 提取 manager/contact/name servers/IPs，不把联系地址录为机房地址；光伏只记录能源项目原始指标，Santa Maria di Galeria 设施在意大利治外区域，VA 清册排除；供应商 claim（cloud-based storage system、infrastructure for long-term storage）只证明系统/服务，不证明物理数据中心位置。
- 最终验证工作流：从 manifest 固定 division 为 `Holy See`（不创建 Rome、Vatican City municipality、Santa Maria di Galeria 子分区）→ 先跑官方模板 → 再跑供应商与贸易媒体模板（NTT DATA 映射为 project/digitization evidence）→ 对每个商业 colo/cloud/IXP 主张追到 operator official page，追不到就保留 C 级 seed 或否定 → 做物理归属检查（城国边界内才归 `Holy See`）→ 输出时按字段级评分（存在性/地址/容量/状态/运营商/用途分开标注等级）。

## 维护注意（更新纪律）

- 每次运行：先跑官方模板（DTSI、`.va`、Library、Archive、Vatican Media、Museums、energy/cyber/security），再跑供应商与贸易媒体模板；任何新出现“new data center”“commissioned”“AI-ready datacenter area”报道先按 B 级线索处理并回 vaticanstate.va/press.vatican.va 官方确认。
- 每月/每季：复查 vaticanstate.va 访谈与采购页（bandi/esiti/appalti）、四大云官方区域列表、IANA `.va`、PeeringDB/目录；事件驱动：任何官方公告（motu proprio/chirograph）、AI-ready 工程化进展、数据中心采购或公开容量/地址披露立即重新分级。
- 任何地址、MW、机柜数、PUE 必须有字段级来源；无来源一律 `null`，不推断、不换算、不合并。
