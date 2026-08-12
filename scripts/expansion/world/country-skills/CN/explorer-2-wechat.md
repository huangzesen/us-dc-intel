# Explorer 2 — WeChat Ecosystem (微信私域) for China Datacenter/IDC Intelligence

Date: 2026-08-11. Scope: how to efficiently extract DC/IDC/智算中心 project intelligence from
微信公众号, 小程序, 视频号, and industry 微信群. Written for an analyst who may operate from
outside China with only browser + optionally a WeChat account.

Key constraint up front: WeChat is a **closed garden**. There is no public API for article
search. The practical stack is: (a) Sogou's licensed WeChat search (`weixin.sogou.com`) from a
browser, (b) in-app 搜一搜 if you have a WeChat account, (c) RSS bridges built on 微信读书
credentials, (d) permalinks (`mp.weixin.qq.com/s/...`) which are publicly readable without
login once you have the URL — always capture these as citations.

---

## 1. Key WeChat Official Accounts (公众号) publishing Chinese DC news

### Tier B+ industry media (primary daily-monitoring set)

| Account (名称) | WeChat ID / anchor | What it gives you |
|---|---|---|
| 中国IDC圈 | `idc-quan` (site: idcquan.com) | The single best account. Weekly 《IDC圈周刊》 explicitly lists **new projects** ("14新项目3智算" style roundups), policy, M&A, 智算中心 tracking. Parent site has a 机房名录 directory (dh.idcquan.com/jifang/). |
| 云头条 | search 云头条 in 搜一搜 | Famous for publishing **中标/招标 results with prices** (cloud + IDC contract awards). Excellent for who-won-what and per-project capex signals. |
| 数据中心之家 | search by name | DC engineering/ops focused; carries project case studies and vendor deployments. |
| CDCC | 中国数据中心工作组 | Standards body community; conference content, design/build case studies, expert commentary on new builds. |
| ODCC 开放数据中心委员会 | `ODCC-org` (odcc.org.cn) | White papers, hyperscaler (BAT/ByteDance) DC technology direction, annual 大会 material. |
| 半导体行业观察 | `icbank` | Upstream: AI chips, GPU supply — leading indicator for 智算中心 buildouts. |
| DT财经 | 第一财经旗下 | Data journalism; occasional 算力/东数西算 explainer pieces with datasets. |
| 算力智库 / 算力Time / 智算研究 (several 算力-branded accounts) | search 算力 in account search | 自媒体 cluster tracking 智算中心 announcements province by province. Quality varies — treat as leads (Tier C, see §6). |
| 科智咨询 | idcquan sibling (研究 arm) | Market sizing reports, regional IDC supply/demand studies. |
| 通信产业网 / C114通信 | trade press | Telecom-operator DC (三大运营商) tenders and buildouts. |
| 中国信通院 CAICT | `CAICT` | Authoritative: 算力发展指数, DC white papers, policy interpretation. Effectively Tier A. |
| 北极星电力网 (北极星售电网 etc.) | bjx.com.cn family | Power-side view: substations/绿电 deals for DC campuses — confirms real construction. |
| 华为数字能源 / 维谛技术Vertiv / 施耐德电气 | vendor accounts | Project case studies name customer + site + MW after delivery — good ground truth, delayed. |

### Tier A government / regulator accounts

- **工信微报** — MIIT's official account; national DC/算力 policy, 国家枢纽节点 progress.
- **Provincial 通信管理局 accounts** — pattern: search “<省>通信管理局” in 公众号 search
  (e.g. 广东省通信管理局, 河北省通信管理局). They publish **IDC 业务许可 (电信业务经营许可)
  approvals/cancellations** — a hard registry of who may legally operate a DC in the province.
- **Local-government “X发布” accounts** — every DC-cluster locality has one and they announce
  groundbreakings/签约 first: 乌兰察布发布, 和林格尔新区 (内蒙古), 贵安新区发布 (贵州),
  中卫发布 (宁夏), 庆阳发布 (甘肃), 韶关发布 (广东), 张北发布/怀来发布 (河北). Pattern:
  “<市/县/新区>发布”.
- **Operator official accounts** — 万国数据GDS, 世纪互联, 数据港, 润泽科技, 秦淮数据/Chindata,
  中金数据, 光环新网, plus 中国电信/移动/联通 provincial accounts. First-party announcements
  of signings, groundbreakings, deliveries.

Not every 自媒体 name above is stable — accounts get renamed/banned. The durable method:
account-search the keyword set {IDC, 数据中心, 智算中心, 算力, 东数西算} monthly and refresh
your follow list (see §2 and §5).

## 2. Searching WeChat article archives

### 2a. 搜狗微信搜索 — weixin.sogou.com (verified live, 2026-08)

Sogou has the exclusive external license to index 公众号 content. Two modes:

- **Account search**: `https://weixin.sogou.com/weixin?type=1&query=中国IDC圈` — returns
  account name, WeChat ID, verification status, QR code.
- **Article search**: `https://weixin.sogou.com/weixin?type=2&query=智算中心+开工` — full-text
  article search; supports time filtering (一天内/一周内/一月内/一年内 via the `tsn` parameter
  in the UI) and sort by relevance/time.

Practical notes:
- Anti-bot is aggressive: after a handful of paginated requests you get a captcha (SNUID
  cookie challenge). Fine for manual/analyst use; scraping needs slow rates + cookie rotation
  and is fragile. Budget for manual sessions, not bulk harvest.
- Result links are time-limited Sogou redirect URLs. **Resolve and save the underlying
  `mp.weixin.qq.com/s/...` permalink immediately** — that permalink is stable and publicly
  readable.
- Index depth is shallow (recent months, roughly ≤1 year, ~top-100 results per query). It is
  a discovery tool, not an archive.

### 2b. In-app 搜一搜 (best coverage, needs a WeChat account)

- Top search bar → 搜一搜 → tab 文章 or 公众号; filter by 发布时间 and 公众号 scope.
- **Per-account archive search** (the killer feature Sogou lacks): open the account profile →
  right-top ⋯ / 消息 page → search icon → keyword-search that account's **entire history**.
  E.g. inside 中国IDC圈 search “庆阳” to pull every article mentioning that hub.
- 搜一搜 also surfaces 视频号 and mini-program results for the same keyword.

### 2c. 微信读书 + RSS bridges (for standing monitoring)

微信读书 (WeChat Read app) can subscribe to 公众号 and exposes their article feed — this is
the backend trick used by RSS tools:

- **Wechat2RSS** — `https://wechat2rss.xlab.app/` — hosted, maintained, per-account RSS feeds
  (~6h latency). Check its feed list for IDC accounts; request additions.
- **WeWe RSS** — `github.com/cooderl/wewe-rss` — self-hosted, uses your 微信读书 login.
  Archived by the author 2026-01 but still functional. Best option if you want a private
  pipeline of the ~20 accounts in §1 into your own RSS reader/LLM summarizer.
- Paid aggregators: 今天看啥, 瓦斯阅读, 语鲸 — convenient but account-limited.
- Dead tools to not waste time on: 传送门 (chuansong.me), 爱微帮 — both long gone.

### 2d. Generic search engines

Articles shared outside WeChat get indexed: query `site:mp.weixin.qq.com 智算中心 开工 <省名>`
on Google/Bing. Coverage is partial but reaches older articles Sogou dropped. Also useful:
新榜 (newrank.cn), 清博 (gsdata.cn), 西瓜数据 — account-ranking platforms to *discover* which
accounts dominate a keyword/industry (free tier enough for discovery; article export is paid).

## 3. 小程序 (Mini-program) data sources

Mini-programs are queried inside WeChat (search the name in the top bar). The useful ones for
DC intel are mostly tender/registry front-ends:

- **剑鱼标讯** — free tender/bid search with keyword subscriptions. Set standing alerts for:
  `数据中心`, `IDC机房`, `智算中心`, `算力中心`, `液冷`, plus `<省名>+数据中心`. Pushes
  中标公告 (award notices) with amounts — the single highest-signal mini-program.
- **千里马招标 / 采招网 / 比地招标** — same category; overlapping coverage, keep one as backup.
- **企查查 / 天眼查 mini-programs** — resolve project SPVs: a “XX县XX智算中心” announcement
  usually maps to a newly registered project company; registration capital/shareholders reveal
  the real investor behind a local-government press release.
- **微信指数** (official Tencent mini-program, verified) — keyword heat over 7/30/90 days with
  **source breakdown** (搜一搜 vs 公众号 vs 视频号). See §4 for use.
- **中国IDC圈 / conference mini-programs** (IDCC大会 etc.) — attendee lists, agenda, sponsor
  lists = map of active players per region.

There is no mini-program that exposes a raw DC project database; treat mini-programs as
convenient mobile front-ends to tender + corporate-registry data.

## 4. Industry 微信群 — best-effort public methods

You cannot search 微信群 content from outside; groups are invite-only and scraping personal
chats violates ToS (and burns accounts). Realistic approaches, ranked:

1. **Entry via 公众号 articles**: industry accounts (中国IDC圈, CDCC, various 算力 accounts)
   regularly run “扫码进群 / 加小编微信拉群” footers. Following §1's accounts for 2–4 weeks
   yields invites to regional/thematic groups (IDC招投标群, 液冷技术群, X省算力产业群).
2. **Conferences**: IDCC产业年度大典 (中国IDC圈, annual, Beijing/Shenzhen), CDCC数据中心标准
   峰会, ODCC开放数据中心大会 — every session has a QR-code attendee group; these persist for
   years and are where brokers post “急寻 华东 20MW 机柜资源 / 出售指标” style intel.
3. **知识星球 / 小报童 paid communities** attached to the accounts — searchable archives,
   effectively a paywalled proxy for group chatter.
4. **Leakage proxies (no account needed)**: group screenshots and “朋友圈流传” project lists
   get republished in 公众号 articles — 搜一搜/Sogou query patterns like `网传 数据中心 名单`,
   `流出 算力 项目表` catch them.
5. **微信指数 as a tripwire**: a spike in `<地名>+智算中心` heat with 公众号-dominant source
   share usually means an announcement wave; check the date window in Sogou/搜一搜 next.

Grade everything from groups as **rumor (Tier C/D)** until cross-verified (§6). Do not
automate personal WeChat accounts (itchat-style bots) — high ban risk, and unlawful access to
private communications is out of scope; stick to the public/consented surfaces above.

## 5. Practical workflow: WeChat sweep for a given province/division

Inputs: province name 〈P〉 (e.g. 甘肃), its DC localities (from 国家枢纽节点 list or prior
research, e.g. 庆阳), and aliases (city, 新区/园区 names).

1. **Build the keyword matrix**: 〈P or locality〉 × {数据中心, 智算中心, 算力中心, IDC} ×
   {开工, 投产, 签约, 交付, 中标, 备案, 能评, 环评, 点亮}. “点亮” (lit up / energized) is the
   industry verb for capacity coming online; “签约” is the weakest (MOU-grade).
2. **Sogou article sweep** (browser): `weixin.sogou.com/weixin?type=2&query=庆阳+智算中心+开工`
   etc., time-filtered to your window. Save `mp.weixin.qq.com/s/...` permalinks + screenshots
   (articles get deleted; permalink rot is real).
3. **In-app 搜一搜 sweep** (if account available): same matrix; then per-account archive
   search inside 中国IDC圈 / 云头条 / 〈P〉发布 for the locality name — this recovers the
   backlog Sogou can't see.
4. **Follow the Tier A locals**: 〈P〉通信管理局 (IDC license grants), 〈市/新区〉发布 accounts,
   provincial 发改委/工信厅 accounts. Add them to your Wechat2RSS/WeWe-RSS pipeline.
5. **Tender confirmation**: 剑鱼标讯 alert `〈P〉 数据中心` — EPC/监理/设备 tenders prove a
   project moved past PR into procurement; award notices give real contractors and amounts.
6. **Entity resolution**: for each project name, look up the SPV in 企查查/天眼查 mini-program;
   record registered capital, shareholders, registration date.
7. **Log per project**: name, locality, investor/SPV, scale claim (MW / 机柜 / P of 算力 —
   record the unit verbatim), stage verb (签约/开工/投产/点亮), source permalink, source tier,
   date. Same project will re-announce at each stage — dedupe on SPV + site, not headline.
8. **Standing watch**: RSS bridge on the ~10 relevant accounts + 剑鱼 alerts + monthly 微信指数
   check on the locality keyword. ~1h/week per province once set up.

## 6. Reliability grading & cross-verification

### Source tiers

- **A — regulatory/first-party**: 通信管理局 license lists, 发改委/工信 policy accounts,
  operator official accounts, tender award notices. Facts (licenses, awards) are reliable;
  first-party **scale claims are promotional** — planned full-buildout MW is routinely quoted
  as if current.
- **B — established trade media**: 中国IDC圈, CDCC, ODCC, 信通院, C114, 北极星. Mostly
  accurate, but much content is lightly edited company PR; the 周刊 roundups are aggregation,
  inherit source errors.
- **C — 自媒体/算力 marketing accounts, group chatter, 网传名单**: leads only. Common failure
  modes: recycling year-old news as new, conflating 签约 with 开工, unit inflation (机柜数 at
  2.5kW quoted next to MW figures that assume 8kW), phantom projects that never pass 能评.
- **D — anonymous group screenshots**: hypothesis-grade.

### Cross-verification ladder (WeChat claim → official record)

1. **MIIT telecom-license registry** — 电信业务市场综合管理信息系统 (`dxzhgl.miit.gov.cn`):
   does the operator hold an IDC (B11) license for that province?
2. **全国投资项目在线审批监管平台** (`tzxm.gov.cn`) + provincial 发改委 sites: project 备案/核准
   record with coded project number = the project formally exists.
3. **环评/能评 公示** on provincial 生态环境厅 / 发改委 sites: real siting, real MW, real water
   and power numbers — best public ground truth on scale.
4. **Tenders**: `ccgp.gov.cn` (政府采购), 中国招标投标公共服务平台 (`cebpubservice.com`) — award
   = construction is funded.
5. **Listed-company disclosures**: 巨潮资讯 (`cninfo.com.cn`) for GDS/数据港/润泽/光环新网 etc. —
   audited capacity and utilization numbers to calibrate PR inflation.
6. **Satellite/imagery** (outside WeChat) as the final arbiter for 开工/投产 claims.

Rule of thumb: a project is “real” when it appears in ≥2 rungs of the ladder; it is “operating”
only on 点亮/投产 claims from Tier A/B **plus** a non-WeChat rung (环评 record, tender award, or
imagery). Never database a capacity figure from a Tier C account without a unit-verbatim note.

---

### Quick-start (30 minutes)

1. Browser: `weixin.sogou.com` → type=2 query `IDC圈周刊` → grab the latest weekly roundup permalink.
2. Follow/bridge: 中国IDC圈 (`idc-quan`), 云头条, CDCC, 信通院, target-province 通信管理局 + “X发布”.
3. In WeChat: add 剑鱼标讯 mini-program alert for `数据中心` + target province; open 微信指数 and
   baseline `智算中心` and your target locality.
4. Start the §5 log with whatever the weekly roundup lists for your province.
