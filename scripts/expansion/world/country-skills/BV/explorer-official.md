# BV 官方渠道探索 - 布维岛数据中心枚举
# BV Explorer Official - Bouvet Island Datacenter Enumeration

日期 Date: 2026-08-12。范围 Scope: 布维岛（Bouvet Island / Bouvetøya, ISO 3166-1: BV）。清单条目 (world-manifest.jsonl): `{"country_code":"BV","country_name":"Bouvet Island","subnational_type":"country","divisions":["Bouvet Island"]}`。仓库分区为单一 division: `Bouvet Island`。

本文档为中文为主、英文/挪威语关键词为辅的双语方法论（Chinese-primary bilingual）。核心目标是把 BV 做成可审计的 **verified-negative**：官方来源证明其没有常住人口、没有城镇、电网、商业电信或数据中心市场；任何命中都先按科研/航海/业余无线电/域名占位等假阳性处理。

可靠性分级 Reliability grades:

- **A 级**: 官方/一手来源 - Norsk Polarinstitutt (`npolar.no`)、挪威政府 (`regjeringen.no`)、Lovdata、Norid、Nkom/ITU/IANA、官方云区域清单。
- **B 级**: 权威二级来源 - 科学机构、主流媒体、行业媒体、海缆/网络地图、CIA World Factbook 等。
- **C 级**: 弱来源 - 数据中心目录站、SEO 市场报告、博客、社交媒体、未引用来源的中英文文章。仅作线索。

---

## 0. 地面实况（Ground Truth）

### 0.1 领土与行政事实

- BV 是挪威在南大西洋/南大洋的无人属地（Norwegian dependency），挪威语名 **Bouvetøya**。
- 挪威极地研究所说明布维岛是世界最偏远岛屿之一，约 89% 被冰川覆盖，面积约 49 km2，岛屿及周边领海为自然保护区（nature reserve）。
- 挪威政府文件确认布维岛是挪威属地，位于《南极条约》区域以北；Lovdata 收录 `Forskrift om Bouvetøya naturreservat`，保护对象包括岛屿和相邻领海的自然环境。
- 没有常住人口、城镇、港口、机场、道路、市政电网或常规商业服务。登岛活动主要为挪威授权的科考/监测任务、少量探险和船舶活动。

### 0.2 数据中心结论

- **BV 不存在商业数据中心市场**。预期设施清单（expected facility inventory）= **0**。
- 任何自动气象站、临时科考营地、卫星电话/无线电、船载通信、业余无线电 DX-pedition，都不是 commercial datacenter / colocation / cloud region。
- 本 country-skill 的产出应是 `verified-negative`，并记录核查过的官方表面；只有 A 级来源点名商业设施、项目名称、运营方和位置时，才允许升级为候选。

### 0.3 为什么没有设施

1. **人口与需求为零**: 无居民、无企业、无本地客户群。
2. **基础设施为零**: 无公共电网、无固定宽带/移动网络、无海底光缆、无数据中心级供水/冷却/物流。
3. **地理极端偏远**: 登陆困难，补给依赖远洋船舶/直升机窗口，不具备常规建设和运维条件。
4. **保护区限制**: 自然保护区法规以保护地貌、动植物和生态系统为核心，商业开发与大型工程缺乏许可基础。
5. **数字资源也不构成市场**: `.bv` ccTLD 由 Norid 管理，但官方说明从未开放域名注册；这只说明 ISO/互联网编号存在，不代表本地互联网产业。

---

## 1. 官方来源主干（Official Source Backbone）

### 1.1 Norsk Polarinstitutt - 第一官方表面

入口: https://npolar.no/en/themes/bouvetoya/

用途:

- 确认 Bouvetøya 的地理、冰川覆盖、保护区状态和历史。
- 查找近期科考、监测、自动气象站、登陆限制、地图/影像资料。
- 将科研设备与商业数据中心分开标注。

查询模板:

```text
site:npolar.no Bouvetøya
site:npolar.no "Bouvet Island" (station OR expedition OR weather OR monitoring)
site:npolar.no Bouvetøya (stasjon OR ekspedisjon OR værstasjon OR overvåking)
site:npolar.no Bouvetøya ("data center" OR "data centre" OR datacenter OR server OR datasenter)
```

### 1.2 挪威政府 - 政策与属地状态

入口: https://www.regjeringen.no/

重点表面:

- `Meld. St. 33 (2014-2015) Norske interesser og politikk for Bouvetøya`：布维岛政策、法律地位和管理框架。
- `Meld. St. 29 (2020-2021)` 与海洋/保护区政策文件：确认布维岛及领海受保护。
- 司法与公共安全部（Justis- og beredskapsdepartementet）/极地事务相关页面。

查询模板:

```text
site:regjeringen.no Bouvetøya biland
site:regjeringen.no "Bouvet Island" "Norwegian dependency"
site:regjeringen.no Bouvetøya naturreservat
site:regjeringen.no Bouvetøya (infrastruktur OR telekommunikasjon OR datasenter OR kraft)
```

### 1.3 Lovdata - 法规原文

入口: https://lovdata.no/dokument/SF/forskrift/1971-12-17-9

用途:

- 核实 `Forskrift om Bouvetøya naturreservat` 现行文本。
- 核实 `Lov om Bouvet-øya, Peter I's øy og Dronning Maud Land m.m.` 的适用关系。
- 判断任何工程、登陆、建设、采样或设备安装是否需要许可。

查询模板:

```text
site:lovdata.no Bouvetøya naturreservat
site:lovdata.no "Bouvet-øya" biland
site:lovdata.no Bouvetøya (ferdsel OR fredning OR forskrift)
```

### 1.4 Norid / IANA / ITU - 编号资源

入口:

- Norid `.bv`: https://www.norid.no/en/omnorid/toppdomenet-bv/
- IANA root DB: https://www.iana.org/domains/root/db/bv.html
- ITU 国家/地区编号与呼号清单按最新版核查。

处理规则:

- `.bv` 存在且由 Norid 管理，但 Norid 官方说明该顶级域从未开放注册；不得把 ccTLD 当作本地互联网市场证据。
- 业余无线电前缀（如 3Y0）只能证明远征/临时通信活动，不是电信运营商或数据中心。

### 1.5 云区域和数据中心监管阴性对照

仅使用官方平台列表确认缺失:

```text
AWS global infrastructure Bouvet Island
Azure regions Bouvet Island
Google Cloud locations Bouvet Island
Oracle Cloud regions Bouvet Island
site:nkom.no Bouvetøya datasenter
site:nkom.no Bouvet Island data center
```

预期结论: 无 BV 云区域、无边缘位置、无 Nkom 数据中心登记、无本地运营商记录。

---

## 2. 官方查询模板（Official Query Catalog）

挪威语:

```text
Bouvetøya datasenter
Bouvetøya serverhall
Bouvetøya datarom
Bouvetøya telekommunikasjon
Bouvetøya fiber
Bouvetøya kraft
Bouvetøya værstasjon
Bouvetøya ekspedisjon satellitt
Bouvetøya Nyrøysa stasjon
```

英语:

```text
"Bouvet Island" "data center"
"Bouvet Island" datacenter
"Bouvet Island" "data centre"
"Bouvet Island" colocation OR hosting OR "cloud region"
"Bouvet Island" submarine cable OR "cable landing"
"Bouvet Island" telecommunications OR satellite OR "weather station"
"Bouvet Island" infrastructure power
```

中文:

```text
"布维岛" 数据中心
"布韦岛" 数据中心
"布维岛" 云 区域
"布维岛" 海底光缆
"布维岛" 科考 通信
```

---

## 3. 分区枚举策略（Per-Division Strategy）

| Repo division | 优先级 | 官方检索策略 | 计数规则 |
|---|---:|---|---|
| Bouvet Island | High | NPI 地理/保护区页面；regjeringen.no 属地政策；Lovdata 保护区法规；Norid/IANA 编号资源；Nkom/官方云列表阴性核查；海缆/电信关键词负向扫描 | 默认 `verified-negative`；仅 A 级来源点名商业设施（名称+运营方+位置+用途）时计数 |

地理标注（非 division）:

- **Nyrøysa**: 岛上少数可登陆区域，可能出现科考/临时站点/自动气象设备；默认不计数。
- **Bouvetøya Nature Reserve / territorial waters**: 保护区和周边领海；船载设备不计入陆上设施。
- 其他海岸/冰川/山峰位置只用于地理描述，不拆分枚举。

---

## 4. 候选处理（Candidate Handling）

任何疑似设施必须先通过最小验证标准:

- A 级来源点名设施或项目；
- 有明确运营方/业主；
- 有明确位置在 `Bouvet Island`；
- 功能为 commercial datacenter / colocation / cloud / hosting，而非科研、气象、卫星通信、无线电或船载系统；
- 有电力和连接证据支撑其可运行性。

候选记录模板:

```text
country_code: BV
division: Bouvet Island
facility_or_project_name: （预期为空）
operator_or_owner: （预期为空）
status: verified-negative | lead | rejected
facility_type: none | scientific equipment | temporary expedition communications | amateur radio | vessel equipment
evidence_grade: A | B | C | U
site_address: none
coordinates: only if official source states them
power: no public grid; temporary expedition power only
connectivity: no submarine cable; temporary satellite/radio only
primary_urls:
secondary_urls:
notes:
last_checked: 2026-08-12
```

---

## 5. 已验证阴性（Verified Negatives）

截至 2026-08-12:

- **商业数据中心 / colocation / hosting**: 无。
- **公有云区域 / availability zone / edge location**: 无。
- **海底光缆 / cable landing station**: 无。
- **本地 ISP / 移动网络 / IXP**: 无。
- **公共电网 / 大型电力设施**: 无。
- **可注册本地域名生态**: 无；`.bv` 未开放注册。

---

## 6. 复核清单（Checker Checklist）

每轮复核至少完成:

1. 打开 NPI Bouvetøya 页面，确认保护区、孤立性和无常住设施背景未变。
2. 在 regjeringen.no 检索 Bouvetøya/Bouvet Island，确认属地与政策状态未变。
3. 打开 Lovdata 保护区法规，确认无会改变大型商业建设判断的新规。
4. 打开 Norid `.bv` 页面，确认 `.bv` 仍未开放注册。
5. 复核官方云区域列表和 Nkom 数据中心登记，确认无 BV 条目。
6. 搜索 `Bouvet Island data center/datacenter/data centre` 与 `Bouvetøya datasenter/serverhall`，将命中按科研、域名、业余无线电、同名企业或 SEO 误报分类。

结论应保持为: **BV = verified-negative, expected facility count 0**，除非出现挪威官方或具名运营商一手证据。
