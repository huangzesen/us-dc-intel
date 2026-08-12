# VA Explorer Official - Holy See（圣座/梵蒂冈）数据中心枚举：官方渠道方法论

**国家（Country）**：Holy See（圣座；梵蒂冈城国相关主权实体），ISO `VA`。

**Manifest 核验**：`{"country_code":"VA","country_name":"Holy See","subnational_type":"country","divisions":["Holy See"]}`。

**分区（Divisions）**：仅 **1 个分区：`Holy See`**。枚举时不再拆分省、市、区；所有被接受设施必须归入 `Holy See`，并以物理位置是否在梵蒂冈城国边界内为准。罗马市内或圣座城外治外地产默认不计入 VA，除非项目规则明确把对应几何纳入 `VA`。

**结论先行（official baseline）**：
- VA 有官方可证的政府 ICT / datacenter 基础设施。梵蒂冈城国总督府（Governatorato）下属 **Direzione delle Telecomunicazioni e dei Sistemi Informatici** 在 2024 年官方访谈中说明其职责包括数据网络、datacenter 管理、VoIP 公共交换、Cloud 平台、ERP 与网络安全；2026 年官方访谈进一步说明数据在“datacenter presenti nello Stato”内驻留并处理。
- VA 未发现官方公开的商业 colocation、hyperscale campus 或公有云区域。AWS、Azure、Google Cloud、Oracle OCI 官方区域列表均无 Holy See / Vatican City region。
- 官方资料通常不公开机房精确地址、机柜数、面积、PUE、MW 或电力冗余。没有字段级来源时，地址和容量必须保留 `null` / `undisclosed`，不得从建筑、DNS 联系地址或电力项目推断。

---

## 0. 可靠性分级（Reliability Grades）

**A - 官方/一手来源**
- 圣座与梵蒂冈城国官方域名：`vatican.va`、`vaticanstate.va`、`press.vatican.va`、`vaticannews.va`、`observatoreromano.va`。
- 官方机构站点：`vaticanlibrary.va`、`digi.vatlib.it`、`archivioapostolicovaticano.va`、`museivaticani.va`。
- AAS《宗座公报》、梵蒂冈城国法律与官方公告。
- IANA `.va` delegation record、四大云厂商官方区域列表。
- 供应商官方新闻稿只对其自身合作、产品或服务交付事实为 A；不自动证明数据中心地址或容量。

**B - 强二手来源**
- 具名作者、日期、当事方的贸易媒体/本地媒体/供应商案例稿：Data Center Dynamics、CorCom、Il Sole 24 Ore、Wired Italia、ComputerWeekly、The Register、Catholic News Service 等。

**C - 弱来源**
- 目录、聚合页、SEO 页面、未署名转载、论坛、无法打开或缺少原始出处的页面。

**字段级评分（field-level grading）**：同一来源可对“机构/项目存在”给 A，但对“地址/容量”不给分或给 C。IANA 联系地址可证明 `.va` 管理与网络联系人，不能直接当作 datacenter 物理地址。

---

## 1. 官方事实框架（Official Frame）

### 1.1 治理与 ICT 机构

优先从总督府官方站点核实组织架构与职能：

- `https://www.vaticanstate.va/it/sistemi-informatici.html`  
  说明 `Servizio Sistemi Informatici` 原为 `Ufficio dei Sistemi Informativi`，2018 年纳入总督府 **Direzione delle Telecomunicazioni e dei Sistemi Informatici**；内部单元包括 administration/support、systems、user support、application development。
- `https://www.vaticanstate.va/it/novita/335-a-colloquio-con-antonino-intersimone-direttore-della-direzione-delle-telecomunicazioni-e-dei-sistemi-informatici-del-governatorato.html`  
  2024-07-11 官方访谈：该 Direzione 的能力范围包括数据网络建设、datacenter 管理、公共 VoIP 交换、Cloud 平台、ERP、IT infrastructure 与网络安全。
- `https://www.vaticanstate.va/it/novita/3725-a-colloquio-con-l-ingegner-antonino-intersimone-direttore-della-direzione-delle-telecomunicazioni-e-dei-sistemi-informatici-del-governatorato.html`  
  2026-02-17 官方访谈：以数据主权为主题，称数据驻留并处理在位于梵蒂冈城国境内的 datacenters；同时提到部分 datacenter 区域将工程化为 “AI ready”。

官方查询模板：

```text
site:vaticanstate.va "Direzione delle Telecomunicazioni e dei Sistemi Informatici"
site:vaticanstate.va "gestione di datacenter"
site:vaticanstate.va "datacenter presenti nello Stato"
site:vaticanstate.va "centro elaborazione dati" OR "Ced"
site:vaticanstate.va "piattaforma Cloud" "Governatorato"
site:vatican.va "sistemi informatici" "Città del Vaticano"
```

### 1.2 `.va`、DNS 与连接性

IANA 记录是官方级网络身份来源：

- `https://www.iana.org/domains/root/db/va.html`  
  `.VA` ccTLD manager 为 `Holy See - Vatican City State / Governatorato S.C.V.`；administrative contact 为 Department of Telecommunications（Palazzo del Belvedere, V-00120）；technical contact 为 Vatican Internet Service Provider（Cortile del Triangolo, V-00120）；列出 `.va` authoritative name servers。

使用方式：
- 证明 `.va` 管理者、DNS 技术联系人、官方网络存在性：A。
- 生成官方域名/站点种子：A。
- 证明某一 datacenter 地址：不充分。`Palazzo del Belvedere` 与 `Cortile del Triangolo` 是联系人地址，不得自动录为机房地址。

连接性查询：

```text
site:iana.org/domains/root/db va "Holy See"
"Vatican Internet Service Provider" "Cortile del Triangolo"
"Department of Telecommunications" "Palazzo del Belvedere" "Vatican"
"Vatican" "+39 06 698" telecommunications
site:vaticanstate.va "reti internet" "Stato della Città del Vaticano"
```

### 1.3 公有云区域不存在性

以下官方列表用于核验 “no public cloud region in VA”：

- AWS regions: `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html`
- Azure regions: `https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- Google Cloud locations: `https://cloud.google.com/about/locations`
- Oracle OCI regions: `https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm`

录入规则：
- 若四大厂商列表无 Holy See / Vatican City / VA，结论为 A 级“无公有云 region”。
- “cloud platform”“sovereign cloud”“AWS technology”“Azure services”“Outposts/edge appliance”只说明服务或技术使用，不等于本地 region、AZ 或 commercial datacenter。

### 1.4 能源与关键设施背景

能源资料可解释可用性背景，但通常不构成数据中心清册条目：

- `https://press.vatican.va/content/salastampa/it/bollettino/pubblico/2024/06/26/0529/01095.html`  
  2024-06-26 发布 Pope Francis motu proprio **Fratello Sole**，要求在 Santa Maria di Galeria 治外区域建设 agrivoltaic plant。
- `https://www.vaticannews.va/en/pope/news/2024-06/pope-orders-construction-of-agrivoltaic-plant-for-the-vatican.html`  
  Vatican News 英文报道同一项目，明确地点为 Santa Maria di Galeria extraterritorial zone。
- `https://www.vatican.va/content/leo-xiv/it/letters/2026/documents/20260601-chirografo-fratello-sole.html`  
  2026-06-01 Chirograph 建立 `Fondazione Fratello Sole`，其 legal seat 在 Vatican City State，operational activity 在 Santa Maria di Galeria。

处理规则：
- Santa Maria di Galeria 物理在意大利罗马周边治外区域，**不计入 VA datacenter division**。
- 保罗六世大厅光伏、Santa Maria di Galeria 光伏、电网/UPS/发电机只作供电背景。无官方容量字段时不写 MW；有 MWh/kW 报道时保留原单位，不换算为 datacenter capacity。

查询模板：

```text
site:press.vatican.va "Fratello Sole" "Santa Maria di Galeria"
site:vaticannews.va "agrivoltaic" "Santa Maria di Galeria"
site:vatican.va "Fondazione Fratello Sole"
site:vaticanstate.va "Centro di elaborazione dati" "trasformatori"
"Città del Vaticano" UPS "gruppo elettrogeno"
```

### 1.5 数据保护、安全与采购

这些来源通常是支持性 evidence，不单独证明设施：

- 安全：`https://www.vaticanstate.va/en/directorates/directorate-security/gendarmerie-corps.html` 可证明 Gendarmerie / Security and Civil Protection 职责，但不列数据中心。
- 网络安全合作：`https://www.vaticanstate.va/it/novita/340-accordo-cybersecurity.html` 可作为 cyber posture 线索。
- AI governance：`https://www.vaticanstate.va/en/tag-manager/ai.html` 可证明 AI 委员会和 DTSI 参与治理；不等于设施。
- 采购与法律：查 `vaticanstate.va` 的 `bandi di gara`、`esiti di gara`、`appalti`，以及 `vatican.va` / AAS 的合同透明度法律。

查询模板：

```text
site:vaticanstate.va "bando di gara" informatica
site:vaticanstate.va "gara" "telecomunicazioni"
site:vaticanstate.va "appalto" "sistemi informatici"
site:vatican.va "Per la trasparenza" appalti
site:vaticanstate.va "cybersicurezza" "Telecomunicazioni"
site:vaticanstate.va "Commissione sull'Intelligenza Artificiale"
```

---

## 2. 档案、图书馆与文化机构（Official/Digitization）

### 2.1 Biblioteca Apostolica Vaticana / Vatican Library

官方与供应商来源：

- `https://www.vaticanlibrary.va/en/home.php`：官方入口，链接 Digital Vatican Library。
- `https://digi.vatlib.it/`：数字馆藏访问入口。
- `https://www.nttdata.com/global/en/news/press-release/2024/may/ntt-data-celebrates-10-years-of-project-with-vatican-library`：NTT DATA 2024 官方新闻稿，称 2014 年合作开始，NTT DATA 创建长期存储、保存和展示所需基础设施，在线 manuscript 已超过 27,500 件。
- `https://www.nttdata.com/global/en/news/press-release/2016/july/2016/reproductions-of-rare-vatican-manuscript-to-be-presented-to-project-donors`：NTT DATA 2016 官方新闻稿，说明 2014 年起计划到 2018 年数字化约 3,000 份手稿，并描述整体目标为 82,000 manuscripts / 41 million pages。

录入规则：
- 作为 **digitization infrastructure / storage and compute lead**，不是 commercial DC。
- 如果仅能证明在线平台或存储系统，不应创建独立 datacenter 条目；可作为 DTSI/机构 ICT 资产线索。
- 供应商新闻稿可给项目事实 A；设施地址、MW、机柜数仍为 `null`。

### 2.2 Archivio Apostolico Vaticano / Vatican Apostolic Archive

官方来源：

- `https://www.archivioapostolicovaticano.va/content/aav/en/l-archivio.html`：档案馆官方说明其保存并提供圣座治理相关文书。

处理规则：
- 官方站点可证明机构与数字服务存在，不能单独证明 datacenter。
- 原始待核实线索中关于 “IBM 合作（搜索/索引技术）” 的设施级说法未找到可稳定核验的一手 IBM 新闻稿；仅保留为二次研究查询线索，不得写入最终设施清册，除非后续找到 IBM 官方或档案馆官方页面。

查询模板：

```text
site:archivioapostolicovaticano.va PIUS digitalizzazione
site:archivioapostolicovaticano.va "digital" "archive"
"Archivio Apostolico Vaticano" "IBM"
"Vatican Apostolic Archive" "digitization" "IBM"
"Archivio Apostolico Vaticano" "sala server" OR "centro dati"
```

### 2.3 Vatican Media、Musei Vaticani 与其他机构

官方入口：

- Vatican News / Vatican Media: `https://www.vaticannews.va/`
- Musei Vaticani: `https://www.museivaticani.va/`

处理规则：
- 这些机构有明确数字服务、媒体发布、票务或安全需求，但除非找到官方机房/数据中心/采购文件，不创建独立 facility。
- Vatican Radio 的 Santa Maria di Galeria 发射台是常见误收录点：广播发射基础设施在意大利治外区域，排除出 VA datacenter 清册。

---

## 3. 唯一分区查询模板（Per-Division Templates）

`{division}` 固定为 `Holy See`。必须至少跑英语和意大利语；拉丁语和中文用于补充。

```text
"Holy See" "data center"
"Holy See" "data centre"
"Vatican City" "data center"
"Vatican City" "data centre"
"Città del Vaticano" "datacenter"
"Stato della Città del Vaticano" "datacenter"
"Santa Sede" "centro elaborazione dati"
"Città del Vaticano" "centro elaborazione dati" OR "Ced"
"Vaticano" "sala server" OR "sala macchine"
site:vaticanstate.va "gestione di datacenter"
site:vaticanstate.va "datacenter presenti nello Stato"
site:vaticanstate.va "AI ready" datacenter
site:vatican.va "centro elaborazione dati"
site:vaticannews.va "data center" OR "centro dati"
"00120 Città del Vaticano" "server"
"Status Civitatis Vaticanae" "instrumenta informatica"
"Sancta Sedes" "bibliotheca digitalis"
```

建筑/地址级核验模板：

```text
"Palazzo del Belvedere" "data center" OR datacenter
"Cortile del Triangolo" "Vatican Internet Service Provider"
"Governatorato" "centro elaborazione dati"
"Vatican Media" "Città del Vaticano" "server"
"Biblioteca Apostolica Vaticana" "storage" OR "server"
"Musei Vaticani" "sala server" OR "sistemi informatici"
```

排除模板：

```text
"Santa Maria di Galeria" "data center" OR "datacenter"
"Castel Gandolfo" "data center" OR server
"Lateran Palace" OR "Laterano" "data center"
"Santa Maria Maggiore" "server room"
"Bambino Gesù" "data center"
"via della Conciliazione" "data center"
"Rome" "Vatican" "data center" -"Città del Vaticano"
```

---

## 4. 设施分类规则（Facility Classification）

| 分类 | VA 适用规则 |
|---|---|
| Operational colo / hosting DC | VA 当前无公开官方证据。出现供应商或目录主张时必须追到运营商官网、地址和服务页；否则不收录。 |
| Public-sector datacenter / server room | DTSI datacenters 是 A 级存在性；地址/容量未公开。机构机房需独立官方证据。 |
| Proposed / under construction | 只有官方公告、采购、许可或具名 B 级报道可标 proposed。没有官方确认前不得并入 operational。 |
| Digitization infrastructure | Vatican Library / Archive 数字化、存储、访问平台按“数字化基础设施线索”处理，不按 colo 计数。 |
| Broadcast / media infrastructure | Vatican Media、Vatican Radio、流媒体/演播室可作 ICT 线索；Santa Maria di Galeria 发射台排除。 |
| Energy / utility | 光伏、电网、UPS、发电机是背景或依赖项，不等于 datacenter。 |
| Directory-only lead | C 级种子。无官方或具名二手来源确认时不得进入最终清册。 |

已核实官方级种子表：

| 设施/项目 | 证据 | 状态 | 分区处理 | 等级 |
|---|---|---|---|---|
| DTSI datacenters / government ICT | 2024 vaticanstate.va 访谈称职责含 datacenter 管理；2026 vaticanstate.va 访谈称数据驻留并处理在 State 内 datacenters | Operational public-sector datacenters | `Holy See`；具体地址未公开 | A（存在性）；地址/容量 null |
| Vatican Internet Service Provider / `.va` DNS | IANA `.va` delegation record | Operational network/DNS infrastructure | `Holy See`；联系人地址不是机房地址 | A（网络身份）；设施地址不充分 |
| Vatican Library digital infrastructure | Vatican Library / Digital Vatican Library + NTT DATA 官方稿 | Operational digitization infrastructure | `Holy See` 机构线索；不按 colo | A（项目）；容量用 manuscript/page 指标 |
| Vatican Apostolic Archive digital services | Archive 官方站点 | Digitization / archive systems lead | `Holy See` 机构线索；设施级不足 | A（机构）；设施细节不足 |
| Santa Maria di Galeria agrivoltaic / radio site | 2024 motu proprio、2026 Foundation documents | Energy/broadcast background | 物理在意大利治外区域，排除出 VA facility count | A（存在性）；VA 清册排除 |

---

## 5. 最终校验清单（Final Validation Checklist）

- Manifest 唯一分区 `Holy See` 已覆盖；没有省/市级漏项。
- 每个接受设施都有字段级来源；DTSI 可收“存在性”，地址/容量留空。
- `.va` / IANA 只作网络身份和联系人证据，不作 datacenter 地址。
- Vatican Library / Archive 数字化项目与 datacenter / colo 分开统计。
- Santa Maria di Galeria、Castel Gandolfo、Lateran、Santa Maria Maggiore、Bambino Gesù、Rome `Vatican` commercial addresses 已作为跨境陷阱处理。
- AWS / Azure / Google Cloud / OCI 官方区域列表均核验无 VA region。
- 没有公开 MW 来源时 `capacity_mw: null`；代理指标保留原单位和来源。
- 目录或营销页不得提升到 A；不能打开或无法追溯的一律 C 或弃用。
