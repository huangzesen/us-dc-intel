# CN Explorer 1 — Chinese-Language Web Discovery of China Datacenter Projects

Date: 2026-08-11. Scope: how to efficiently and correctly discover China (mainland) datacenter / 智算中心 projects using Chinese-language web sources. Reliability grades: **A** = official/primary (government filings, license registries, operator official pages, listed-company disclosures), **B** = strong secondary (established trade press, industry associations), **C** = weak/unverified (aggregators, self-media 自媒体, forum posts).

---

## 0. Key structural facts (frame every search around these)

- **东数西算 (East-Data-West-Computing)**, launched Feb 2022 by 发改委/网信办/工信部/能源局, defines **8 national hub nodes (八大算力枢纽)**: 京津冀、长三角、粤港澳大湾区、成渝、内蒙古、贵州、甘肃、宁夏; and **10 national datacenter clusters (十大数据中心集群)**: 张家口、长三角生态绿色一体化示范区、芜湖、韶关、天府、重庆、和林格尔、贵安、庆阳、中卫. Most large new builds since 2022 concentrate in these clusters — geo-target searches accordingly (e.g. 乌兰察布、和林格尔、贵安新区、中卫、庆阳、韶关、芜湖、张北/怀来).
- Every IDC operator in China needs an **IDC 增值电信业务许可证** (B11 类) from MIIT — the license registry is a near-complete operator census (not a facility census).
- Every sizable project needs **发改委 备案/核准** (project filing) and, above thresholds, **节能审查** (energy-saving review; 新版《固定资产投资项目节能审查办法》 effective 2023-06-01). These filings leak MW / 机架数 / 投资额 — the best free capacity evidence in China.
- Since ~2023 the hot category is **智算中心 / 算力中心** (AI compute centers), often announced by local governments rather than classic IDC vendors. Search both vocabularies: 数据中心, 智算中心, 算力中心, 超算中心, 云计算中心, 大数据中心, IDC, 机架/机柜, 标准机架, P (算力规模, e.g. "1000P").

---

## 1. Chinese search query patterns

### 1.1 Engines
- **Baidu (baidu.com)** — best mainland coverage of gov sites and news. Supports `site:`, `intitle:`, `filetype:`, `""` exact match, date filter in UI (搜索工具→时间). Grade of engine coverage: best for .gov.cn.
- **Bing 中国 (cn.bing.com)** — good operator support, cleaner results, supports full operator syntax; often better than Baidu for PDFs.
- **360 搜索 (so.com)** — secondary; occasionally surfaces county-level gov pages Baidu misses. Same `site:` syntax.
- **搜狗微信搜索 (weixin.sogou.com)** — the only practical way to search WeChat 公众号 articles, where local 发改委/园区管委会 and IDC vendors publish announcements that never hit the open web. Rate-limited and captcha-heavy; search manually or with slow crawl.
- **Sogou (sogou.com)** — general fallback; also indexes 知乎.

### 1.2 Query templates (copy-paste, substitute {城市}/{公司})

Discovery — new projects:
```
"{城市}" (数据中心 OR 智算中心 OR 算力中心) (开工 OR 奠基 OR 签约 OR 投产 OR 点亮 OR 封顶 OR 落成)
"{城市}" 数据中心 项目 (备案 OR 核准 OR 节能审查 OR 环评 OR 公示)
"{集群名}" 数据中心集群 (新增 OR 在建 OR 规划) 机架
intitle:(智算中心) (开工 OR 投产) 2026
"万卡" OR "十万卡" 智算 集群 (点亮 OR 投产)      ← GPU-cluster announcements
```

Capacity extraction:
```
"{项目名}" (机架 OR 机柜 OR 兆瓦 OR MW OR 千瓦 OR IT负载)
"{项目名}" (总投资 OR 一期 OR 二期) (亿元) (机架 OR P)
"{公司}" 数据中心 "标准机架" 规模
```

Government-filing hunting (highest-value):
```
site:gov.cn 数据中心 节能审查 (审查意见 OR 批复)
site:gov.cn (智算中心 OR 数据中心) 备案 公示 {省份}
site:fgw.{省拼音}.gov.cn 数据中心            ← 省发改委站内
site:gov.cn 数据中心 环境影响评价 (受理 OR 拟批准) 公示
filetype:pdf 数据中心 节能报告 site:gov.cn
```

Listed-company disclosure hunting:
```
"{公司}" (年报 OR 招股书 OR 可转债 OR 募集说明书) 数据中心 机柜
site:static.sse.com.cn OR site:cninfo.com.cn {公司} 数据中心   ← 巨潮资讯 cninfo is the A-share filing archive
```

Useful verb/noun vocabulary for status inference: 签约 (signed, paperware) → 备案/核准 (filed/approved) → 节能审查/环评批复 (permits) → 开工/奠基 (construction start) → 封顶 (topped out) → 点亮/投产/交付/上架 (live) → 满架/上架率 (utilization). "拟建/规划" = planned only.

### 1.3 Practical notes
- Baidu from non-CN IPs works but degrades (captchas); prefer `site:gov.cn`-scoped Bing queries when scripted.
- Chinese numbers: 1 万 = 10,000 (e.g. "3万架" = 30k racks); 1 亿元 ≈ US$14M; "P" = PFLOPS (usually FP16 for 智算, deflate accordingly); 机架 sizes vary — look for "以2.5kW标准机架折算" clauses in gov docs.
- WeChat 公众号 to follow via 搜狗微信: 中国IDC圈, 数据中心WIKI, 智能计算芯世界, CDCC (数据中心标准), 各省发改委官方号, vendor official accounts (万国数据GDS, 世纪互联, 秦淮数据).

---

## 2. Authoritative Chinese sources (Grade A backbone)

### 2.1 MIIT 工信部 — telecom license registry (IDC/ISP/CDN 许可)
- **电信业务市场综合管理信息系统**: https://dxzhgl.miit.gov.cn/ (also https://tsm.miit.gov.cn/ and query UI at https://tsm.miit.gov.cn/dxxzsp/). Left-nav "许可信息查询" → search by 公司名 or 许可证号. Company-level query URL pattern (observed working):
  `https://dxzhgl.miit.gov.cn/dxxzsp/xkz/xkzgl/resource/qiyesearch.jsp?num={URL-encoded 公司名}&type=xuke`
- What it gives: which companies hold **IDC (B11)**, **ISP (B14)**, **CDN (B12)** 跨地区/省内 licenses, covered provinces, validity dates. This is an **operator census** — use it to enumerate every licensed IDC company per province, then pivot each company name into project searches. It does NOT list facilities. **Grade A** (official registry; verify company still active via 企查查/爱企查).
- MIIT also publishes 拟批准经营电信业务名单公示 (weekly-ish) on miit.gov.cn — a change-feed of new IDC entrants.

### 2.2 东数西算 official documents
- NDRC 发改委 hub/cluster approvals and progress: https://www.ndrc.gov.cn/ (search 东数西算 in 站内搜索; e.g. progress report https://www.ndrc.gov.cn/fzggw/jgsj/gjss/sjdt/202209/t20220923_1336061.html). **Grade A.**
- Each cluster has a managing body publishing project lists: e.g. 和林格尔新区管委会 (horinger.gov.cn), 贵安新区 (gaxq.guizhou.gov.cn), 中卫市工信局, 庆阳市"东数西算"产业园官网 (qydsxs.com — check liveness), 韶关市发改局. Search `site:gov.cn {集群} 数据中心 (入驻 OR 项目清单)`. **Grade A** for gov pages, **B** for park promo pages.

### 2.3 国家新型数据中心典型案例名单 (MIIT annual lists)
- 2021 (44 cases) and 2022 (33 cases) lists published by 工信部办公厅; find via query `国家新型数据中心典型案例名单 通知 site:miit.gov.cn` (mirror with full list: https://www.ncsti.gov.cn/kjdt/tzgg/202303/t110914.html-style pages; also c114.com.cn coverage). Also **国家绿色数据中心名单** (annual, 六部门公告, e.g. 2023年度 = 公告2024年第12号) — names specific facilities with operator + location. **Grade A.** These are curated facility-level lists — seed your registry with them.

### 2.4 Provincial 发改委 / 能源局 approvals (the richest per-project source)
- Pattern: every 省/市发改委 publishes 备案/核准 results and 节能审查意见 on its 政务公开 page. Examples verified: 北京市发改委 datacenter energy-review rules (fgw.beijing.gov.cn), 广州市发改委 节能审查意见 for 广州智晟算力中心 (fgw.gz.gov.cn/gkmlpt/...), 上海经信委 数据中心建设导则符合性评估名单 (sheitc.sh.gov.cn). **Grade A.**
- Systematic sweep: for each of ~31 provinces, query `site:fgw.{省}.gov.cn (数据中心 OR 智算)` and `site:{市}.gov.cn 数据中心 节能审查`. Also 全国投资项目在线审批监管平台 (tzxm.gov.cn) — national project-filing platform; public search is limited but 备案公示 pages of provincial mirrors (e.g. tzxm.zj.gov.cn) are searchable.
- 环评 (environmental impact) public-notice pages of 省生态环境厅 give backup diesel-generator counts and cooling details → cross-check MW. Query: `site:sthjt.{省}.gov.cn 数据中心 环评 公示`.
- Also: 能耗指标/用能权 trading notices and 电力接入 (电网) announcements mention datacenter loads.

### 2.5 CDN/IDC license bulk lists
- Third-party mirrors of the MIIT registry make bulk enumeration easier: 企查查/爱企查/天眼查 filter by 行政许可 "IDC许可证"; site beian.miit.gov.cn is ICP (website) filing — different thing, don't confuse. Community-maintained lists appear on idcquan and zhihu. **Grade B** (mirror lag) — always re-verify a specific company on dxzhgl.miit.gov.cn (**A**).

---

## 3. Key Chinese IDC vendors — public DC lists

Two complementary channels per vendor: (a) official 数据中心分布 page (**A**, but marketing-rounded), (b) investor disclosures — US SEC 20-F / HKEX filings / A-share 年报 on cninfo.com.cn — with per-campus sqm/MW/utilization tables (**A**, the best capacity numbers in the market).

| Vendor | Official list | Investor channel | Notes |
|---|---|---|---|
| 万国数据 GDS (NASDAQ: GDS / HKEX 9698) | https://www.gds-services.com/ → 数据中心 (about_4.html); campuses in 北京(亦庄/顺义/昌平)、廊坊、张北、上海+昆山"双星"、深圳、广州、成都 etc. | 20-F + quarterly presos list every DC with area & commitment % | Largest carrier-neutral; intl arm split off as DayOne |
| 世纪互联 VNET (NASDAQ: VNET) | https://www.vnet.com/ → 数据中心 | 20-F, quarterly | Retail+wholesale; wholesale campuses 太仓、河北 etc. |
| 秦淮数据 Chindata | https://www.chindatagroup.com/ (张家口怀来、山西大同、马来西亚) | Taken private (Bain) 2023 — historical SEC filings still useful | Hyperscale, ByteDance-heavy |
| 润泽科技 Runze (A股 300442) | https://www.runze.com/ — 廊坊、平湖、佛山、惠州、兰州、重庆 园区 | 年报/募集书 on cninfo | Wholesale campuses, big MW |
| 数据港 AtHub (A股 603881) | https://www.athub.com.cn/ | 年报 on cninfo | Mostly Alibaba build-to-suit; sites in 张北、南通、杭州、深圳 |
| 首都在线 Capital Online (A股 300846) | https://www.capitalonline.net/ | 年报 | Cloud+IDC, smaller |
| 优刻得 UCloud (A股 688158) | https://www.ucloud.cn/ (自建 乌兰察布、上海青浦) | 年报 | Cloud provider with 2 self-built campuses |
| 浩云长盛 Haoyun | https://www.haoyunlink.com/ (广州、佛山、江门 etc.) | Private (PE-backed) — rely on 官网+园区政府新闻 | South-China wholesale |
| 鹏博士 Dr.Peng (A股 600804) | https://www.drpeng.com.cn/ | 年报 | Legacy retail IDC, has divested assets — treat old lists carefully |
| 光环新网 Sinnet (A股 300383) | https://www.sinnet.com.cn/ — 北京(酒仙桥/亦庄)、房山、燕郊、天津宝坻 | 年报 | Operates AWS 中国(北京) region |
| 科华数据 Kehua (A股 002335) | https://www.kehua.com.cn/ | 年报 | UPS maker + IDC operator (北上广) |
| Others worth adding | 奥飞数据(300738), 佳力图, 云赛智联, 中国电信/移动/联通 (the 3 telcos are the largest IDC owners in China — see 年报 "IDC机架数" and their 智算中心 announcements: 移动呼和浩特/哈尔滨, 电信京津冀/安徽, 联通) | cninfo / HKEX | Telco disclosures give national totals + flagship sites |

Hyperscaler official region/AZ pages (**A** for existence/location-city; they hide exact addresses):
- 阿里云: https://help.aliyun.com/zh/ecs/user-guide/regions-and-zones (regions incl. 青岛、北京、张家口、呼和浩特、乌兰察布、杭州、上海、深圳、河源、广州、成都、南通(福州) …)
- 腾讯云: https://cloud.tencent.com/document/product/213/6091 (地域和可用区); own campuses: 天津、上海青浦、深圳/清远、重庆、贵安七星洞
- 华为云: https://developer.huaweicloud.com/endpoint or https://www.huaweicloud.com/ region page; own campuses: 贵安、乌兰察布、廊坊
- 字节/火山引擎: https://www.volcengine.com/docs/6396/72806 (地域可用区); capacity mostly leased from Chindata/润泽 etc.
- 百度智能云: https://cloud.baidu.com/doc/Reference/s/2jwvz23xx (阳泉 self-built flagship)
- AWS 中国: https://www.amazonaws.cn/ — 北京 region (operated by 光环新网 Sinnet), 宁夏中卫 region (operated by 西云数据 NWCD). Azure 中国 = 世纪互联运营 (https://www.azure.cn/). Cross-reference cloud regions to physical operator campuses — in China every foreign cloud maps to a licensed local operator's buildings.

---

## 4. Trade press & industry media (Grade B)

- **中国IDC圈 idcquan.com** — the sector's main portal since 2005. Key sections: news https://news.idcquan.com/news/ (国内 IDC news), 数据中心/设施 https://dc.idcquan.com/, plus 项目动态 and **IDC建设月报** (monthly construction round-up — excellent discovery feed) and 东数西算 topic pages. Annual 中国IDC产业年度大典 reports give market shares. **Grade B** (accurate on announcements; capacity numbers are as-claimed by vendors).
- **CDCC / 数据中心标准 (via WeChat 公众号 & cdcc.org.cn)** — engineering-side association; publishes 白皮书 and project case studies. **B.**
- **算力网/中国算力大会 (China Computing Power Conference)** materials & 中国信通院 CAICT 白皮书 (caict.ac.cn — 《中国算力发展指数白皮书》, annual) — best national aggregate stats (total racks ~ EFLOPS by province). **A-/B+** (official think-tank).
- **数据中心世界 / 机房360 (jifang360.com)** — older trade site, still posts project news. **B-/C+.**
- **DT财经 / 各财经媒体** (财新, 界面, 36氪, 晚点LatePost) — good for hyperscaler capex strategy and GPU-cluster scoops (晚点 especially for 字节/阿里 AI datacenter plans). **B** (晚点 scoops often accurate but unconfirmed).
- **智算中心 news**: search 通用词 "智算中心 点亮" on Baidu news + 搜狗微信; also 央视/新华 provincial channels cover 开工 ceremonies (**B+** for event truth, useless for capacity).
- **C114 通信网 (c114.com.cn)** — telecom trade press, strong on telco (移动/电信/联通) datacenter tenders and MIIT lists. **B.**
- **Bidding/tender platforms** — 中国招标投标公共服务平台 (cebpubservice.com), 中国政府采购网 (ccgp.gov.cn), and telco e-procurement (中国移动采购与招标网 b2b.10086.cn) — 中标公示 for datacenter EPC/设备 reveal project scale and timing before press coverage. **A** for existence/scale signals.

---

## 5. Verifying capacity / status / evidence grade for Chinese sources

### 5.1 Evidence hierarchy (assign per data point, not per project)
1. **A — regulatory filings**: 节能审查意见 (states 年综合能耗, from which IT MW is derivable), 环评报告 (diesel gensets, cooling water), 发改委备案 (投资额, 机架数), listed-company annual reports/prospectuses (audited sqm/MW/机柜数/上架率), MIIT/six-ministry named lists.
2. **A- — operator official pages** for existence/location; treat capacity as design-max marketing.
3. **B — trade press** (idcquan, C114) reporting a specific filing or ceremony with numbers.
4. **C — local-gov promo articles, 自媒体, park brochures**: notorious for announcing 签约 mega-projects (「总投资100亿」) that never break ground; also for summing 远期规划 phases as if built.

### 5.2 Status verification recipe
- Map the announcement verb to lifecycle (签约 < 备案 < 节能审查/环评 < 开工 < 封顶 < 投产/点亮). Only count 开工+ as real; only 投产/点亮 as operational.
- Cross-check ≥2 independent channels: e.g. gov filing + operator page, or filing + satellite imagery (乌兰察布/怀来/中卫 campuses are easily visible; use historical imagery to date construction).
- For claimed "xx万机架": check whether it's 规划 (plan, all phases) vs 已建成 (built) vs 已上架 (utilized). Chinese sources routinely headline the plan number.
- Power sanity check: 机架数 × 折算功率 (gov docs often use 2.5 kW 标准机架; hyperscale actual 6–15 kW; 智算 30–120 kW/rack). If 机架数 × plausible kW ≫ stated 能耗指标 from the 节能审查, the rack number is inflated.
- 智算 "P" claims: assume FP16 unless stated; 1000P FP16 ≈ ~500 H800-class GPUs equivalent — sanity-check against reported GPU counts ("万卡" = 10k GPUs) and MW.
- Company liveness: 企查查/爱企查 (aiqicha.baidu.com, free) for registration status, 股权, and 行政许可 (shows the IDC license) — catches shell-company "projects". **A-** as a registry mirror.
- Beware double counting: the same campus appears under park name, operator SPV name, and brand name (e.g. 润泽(廊坊)国际信息港 = 润泽科技 A区/B区…). Key projects by (operator ultimate parent, campus, phase).

### 5.3 Suggested per-source grade summary
| Source | Grade |
|---|---|
| MIIT dxzhgl 许可查询 / named national lists | A |
| 省/市发改委 节能审查·备案·环评 公示 | A |
| Listed-company filings (cninfo/SEC/HKEX) | A |
| Operator official DC pages; cloud region docs | A- (existence) / B (capacity) |
| CAICT 白皮书 | A-/B+ |
| idcquan / C114 / CDCC | B |
| Tender platforms 中标公示 | A (signal) |
| 搜狗微信 公众号 articles (gov/vendor official accounts) | B+ |
| Local-gov promo news, 签约 ceremonies | C (existence-of-intent only) |
| 自媒体/知乎/贴吧 aggregations | C |

---

## 6. Recommended discovery pipeline (actionable order)

1. **Seed with named lists** (§2.3: 新型数据中心典型案例 + 绿色数据中心名单 + 十大集群项目清单) → ~200 facility-grade A records.
2. **Enumerate operators** via MIIT IDC-license query per province (§2.1) + 企查查 license filter → operator universe.
3. **Vendor sweep**: official DC pages + latest annual report tables for the ~15 vendors in §3 + 3 telcos + hyperscaler region docs → campus-level records with A-grade capacity where listed.
4. **Filing sweep**: per-province `site:gov.cn` queries for 节能审查/备案/环评 (§1.2, §2.4), prioritizing the 10 cluster geographies → new/under-construction projects with MW evidence.
5. **News watch**: idcquan IDC建设月报 + 搜狗微信 on 开工/点亮 verbs + tender 中标公示 → change detection.
6. **Verify** each record per §5.2 before grading.

Pitfalls recap: plan-vs-built inflation; 标准机架 normalization; same-campus aliasing; dead 签约 projects (esp. 2021–22 vintage in 甘肃/宁夏); ICP备案 ≠ IDC许可; Baidu 竞价 ads polluting top results (skip entries marked 广告).
