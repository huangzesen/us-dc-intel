# JP Explorer - Industry, Trade Press, Vendors, and Prefecture Query Patterns

Date: 2026-08-12. Scope: Japan datacenter enumeration through Japanese search patterns, trade press, industry bodies, vendor/operator pages, hyperscaler region pages, and prefecture-by-prefecture query pivots. Reliability grades: **A** = official government/operator/investor disclosure, official cloud-region documentation, public procurement/permitting record; **B** = established trade press, industry association, reputable market broker/research; **C** = aggregator, local promotional article, event listing, repost, or unsourced map.

---

## 0. Japan-specific discovery model

Japan has no single public facility registry. Enumeration works by triangulating:

1. Japanese trade press and construction press for launches, groundbreakings, land acquisitions, and capacity claims.
2. Operator location pages for marketed sites and cloud/on-ramp facilities.
3. Government subsidy selections, local-government investment-attraction pages, building/environment/public-notice records, and grid/power-provider releases.
4. Hyperscaler region pages as proof of cloud-region presence, then local press/operator clues for physical sites.
5. Prefecture and municipality searches in Japanese, especially around known datacenter clusters.

The core geography is metro/power-network driven, not evenly spread across all prefectures:

- **Tokyo metro / Greater Tokyo**: Tokyo 23 wards, Tama/Fuchu, Kanagawa/Yokohama/Kawasaki, Saitama, and especially **Chiba/Inzai/Shiroi** for hyperscale campuses.
- **Kansai**: Osaka city, Ibaraki/Suita/Minoh/Sakai, Kyoto/Keihanna, Nara edge cases, and Hyogo/Kobe enterprise sites.
- **Emerging decentralization clusters**: Hokkaido/Ishikari/Tomakomai/Sapporo, Kyushu/Fukuoka/Kitakyushu, Aomori/Rokkasho, Miyagi/Sendai, Niigata, Toyama/Ishikawa, Okayama/Hiroshima, Okinawa.
- Government policy is pushing **地方分散** (regional decentralization), **ワット・ビット連携** (watt-bit integration), GX/renewable-power-linked datacenters, and domestic AI compute. These terms are high-signal for future sites.

Japanese searches should be the default. English searches are useful for global operators and broker reports, but they miss local municipal announcements and Japanese construction coverage.

Core Japanese terms:

```text
データセンター
データセンタ
DC
IDC
AIデータセンター
生成AI データセンター
計算基盤
GPUクラウド
クラウド基盤
ハイパースケール
コロケーション
ハウジング
サーバールーム
コンテナ型データセンター
グリーンデータセンター
ゼロエミッション・データセンター
地方分散
ワット・ビット連携
GX戦略地域
```

Status / evidence words:

```text
開設
竣工
稼働
運用開始
サービス開始
着工
起工式
地鎮祭
建設
新設
増設
拡張
新棟
キャンパス
用地取得
土地取得
誘致
立地
協定
覚書
基本合意
補助金
採択
公募
建築確認
開発許可
環境影響評価
公告
入札
落札
受電容量
電力容量
IT電力
IT負荷
変電所
特別高圧
高圧受電
系統接続
ラック
サーバールーム面積
延床面積
敷地面積
```

Stage interpretation:

- `協定`, `覚書`, `基本合意`, `誘致` = intent only; **C** unless followed by land/permit/subsidy/construction.
- `補助金 採択`, `用地取得`, `土地取得`, `立地協定` = stronger planned signal; **B/A-** depending on source.
- `建築確認`, `開発許可`, `環境影響評価`, `公告`, `入札`, `落札` = primary project trail; **A** if official.
- `地鎮祭`, `着工`, `起工式` = construction start; **B** in trade press, **A-** from operator/government.
- `竣工`, `開設`, `稼働`, `運用開始`, `サービス開始` = operational claim; verify with operator page or customer/cloud region.

---

## 1. High-signal Japanese trade press and industry media

Use trade press as the live discovery feed. Grade project facts as **B** unless the article directly links an operator release, public filing, or local-government notice.

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Impress Cloud Watch / クラウド&データセンター完全ガイド | https://cloud.watch.impress.co.jp/cdc/hw/datacenter/ | Best Japanese open-web feed for datacenter launches, vendor announcements, regional facilities, facility tours, and glossary context. The archive claims coverage of domestic operators and publishes project-level pieces. | B+ |
| ITmedia BUILT | https://built.itmedia.co.jp/ | Excellent for construction starts, large-project announcements, land/building/capacity details, and real-estate framing. Search `site:built.itmedia.co.jp データセンター {都道府県}`. | B+ |
| ITmedia NEWS / MONOist / business network.jp | `site:itmedia.co.jp データセンター`, `site:monoist.itmedia.co.jp データセンター`, https://businessnetwork.jp/ | Good for AI infrastructure, operators, telcos, and equipment vendors. | B |
| Data Center Cafe / DC ASIA | https://cafe-dc.com/ and https://www.dcasia-ltd.com/solution/dccafe/ | Japanese-language datacenter news hub; republishes/summarizes global and domestic DC items. Useful watchlist feed, but verify original source. | B-/C+ |
| DatacenterDynamics | https://www.datacenterdynamics.com/ | Best English global DC trade feed for AirTrunk, Colt DCS, Digital Realty, NTT, STACK, Gaw, ESR, GLP, AWS/Microsoft/Google. | B+ |
| Nikkei / xTECH / Japan Times / Bloomberg Japan | site-scoped search | Strong for major investments, real estate, energy, and M&A; may be paywalled. | B |
| ASCII.jp / INTERNET Watch / EnterpriseZine / ZDNET Japan | site-scoped search | Secondary tech-business coverage for cloud/AI/edge projects and facility announcements. | B-/C+ |
| Construction/property sources: 日刊建設工業新聞, 建設通信新聞, Kensetsu News, LOGI-BIZ, R.E.port | site-scoped search | Construction-stage leads, contractor names, industrial/logistics redevelopment sites. Usually requires verification. | B-/C+ |
| Aggregators: DataCenterMap, Baxtel, Cloudscene, Datacenters.com, OCOLO | site search by operator/city | Useful for address aliases and nearby-facility discovery. Never final-proof capacity from these alone. | C |

Trade-press templates:

```text
site:cloud.watch.impress.co.jp/docs データセンター "{都道府県}"
site:cloud.watch.impress.co.jp/docs データセンター "{市区町村}" (開設 OR 竣工 OR 着工 OR 地鎮祭 OR 増設)
site:built.itmedia.co.jp データセンター "{市区町村}" ("MW" OR "メガワット" OR "受電容量")
site:itmedia.co.jp データセンター "{事業者}" "{市区町村}"
site:businessnetwork.jp データセンター "{事業者}" "{都道府県}"
site:cafe-dc.com "{事業者}" "{市区町村}" データセンター
site:datacenterdynamics.com Japan "{operator}" "data center" "{city}"
site:datacenterdynamics.com Japan Inzai Osaka Keihanna Tomakomai Ishikari Fukuoka
```

Trade press is usually reliable for the **event** and **named parties**, but headline capacity often means full-campus buildout. Capture exact words: `受電容量`, `IT電力容量`, `設計容量`, `最終的に`, `第1期`, `段階的`, `最大`, `予定`, `見込み`, `運用開始`.

---

## 2. Industry bodies, government policy, and market reports

| Source | URL | Use | Grade |
|---|---|---|---|
| Japan Data Center Council / 日本データセンター協会 (JDCC) | https://www.jdcc.or.jp/ and English page https://www.jdcc.or.jp/english/ | Member/operator universe, events, policy discussions. The English member list exposes many Japanese DC operators and suppliers. Not a facility registry. | B+ for operator seeds |
| METI public offers / 経済産業省 公募・採択 | https://www.meti.go.jp/information/publicoffer/ | Search for `データセンター地方拠点整備事業費補助金`, `GX戦略地域`, `採択結果`. Subsidy selections can reveal planned regional DCs and infrastructure works. | A |
| Digital Agency / デジタル庁 | https://www.digital.go.jp/ | Policy basis for regional decentralization, digital infrastructure plans, data strategy working-group materials. | A for policy |
| MIC / 総務省 | https://www.soumu.go.jp/ | Digital-infrastructure decentralization, submarine cables, telecom resilience, regional network plans. Search `データセンター 海底ケーブル 地方分散`. | A |
| JETRO | https://www.jetro.go.jp/ | English/Japanese policy and investment summaries; useful for explaining regional subsidy program and foreign investor entry. | A-/B |
| JEITA / IDC Japan / MM Research / Fuji Chimera / CBRE / JLL / Cushman / Structure Research / Arizton / ResearchAndMarkets | site-scoped search | Market sizing and metro pipeline summaries. Use as context and operator seeds; verify facility records elsewhere. | B/C depending detail |
| Local governments and industrial parks | `{prefecture}.lg.jp`, `{city}.lg.jp`, industrial-port/land-bank pages | Best for incentive programs, siting candidate lots, local MOUs, environmental/public notices, and resident opposition. | A for hosted records |

Government/policy templates:

```text
site:meti.go.jp データセンター 採択 結果
site:meti.go.jp "データセンター地方拠点整備事業費補助金"
site:meti.go.jp "GX戦略地域" "データセンター集積型"
site:digital.go.jp データセンター 地方分散
site:soumu.go.jp データセンター 海底ケーブル 地方分散
site:jetro.go.jp データセンター 地方分散 日本
"データセンター立地候補地" filetype:pdf
"データセンター" "地方自治体" "立地候補地"
"データセンター" "補助金" "{都道府県}" "{市区町村}"
```

Known official/policy facts to encode:

- Japan policy documents describe concentration in Tokyo/Osaka and support regional DC/site development to improve resilience and balance power load; JETRO summarizes the regional DC subsidy purpose.
- METI has published adoption results for the `データセンター地方拠点整備事業費補助金` program and `GX戦略地域` screening. Use these as a change feed for future regional projects.
- Digital Agency priority-plan materials use terms such as `ワット・ビット連携` and `AI向け計算資源・データセンターの整備`. These are good search pivots for post-2025 AI DC announcements.

---

## 3. Vendor/operator seed list

Official operator pages are **A** for existence/current marketed location and **B** for rounded capacity unless facility-level specifications or filings provide exact numbers.

| Operator / developer | Primary URLs / evidence | Japan location pivots | Grade notes |
|---|---|---|---|
| NTT DATA / NTT Global Data Centers / former NTT Com Nexcenter | https://services.global.ntt/en-us/services-and-products/global-data-centers | Tokyo, Osaka, Saitama, Yokohama, Keihanna, Shiroi. NTT official page lists global DC portfolio; NTT announced Keihanna OSK11 opening and Osaka OSK12 as first building on a 36MW campus; DCD reported Shiroi/SHR1 groundbreaking. | A for official facility pages; B for DCD pipeline. |
| AT TOKYO | https://www.attokyo.com/ and https://www.attokyo.com/datacenter/ | Tokyo Chuo/Toyosu/Chuo Center, Osaka, Hokkaido, Hiroshima, Fukuoka, Okinawa. Official page says 13 data centers in Japan's main business centers; DCD reported CC3 40MW launch and 11-site older footprint. | A for current own page; B for historic capacity. |
| KDDI / Telehouse | https://www.telehouse.com/global-data-centers/asia/japan-data-centers/ | Tokyo Otemachi, Tokyo Tama, Osaka, Nagoya, Fukuoka and other KDDI network sites. | A for Telehouse official locations. |
| Equinix Japan | https://www.equinix.com/data-centers/asia-pacific-colocation/japan-colocation/tokyo-data-centers and Osaka page | Tokyo TY sites, Osaka OS sites. Official Tokyo page lists 14 Tokyo DCs and ecosystem/certification details. | A for IBX existence/specs. |
| MC Digital Realty / Digital Realty | https://www.digitalrealty.com/data-centers/asia-pacific/tokyo and investor releases | Chiba/Inzai NRT campus, Osaka KIX campus. Digital Realty official investor release reports NRT14 opening; Japanese trade press reports NRT/KIX AI-ready campus context. | A for official release/facility pages; B for press. |
| AirTrunk | https://www.airtrunk.com/ and press releases | TOK1 in Chiba/Inzai; OSK1 in Osaka area if confirmed by official/DCD. ITmedia Built reported TOK1 new 40MW building and 300MW-plus campus capacity. | A for AirTrunk release; B for trade articles. |
| Colt Data Centre Services | https://www.coltdatacentres.net/ | Tokyo Inzai campus, Osaka Keihanna. Official Inzai 4 page gives 20MW IT power and white space; PRNewswire/DCD reported Osaka Keihanna 45MW-class facility and Inzai campus history. | A for official pages; B for press-release reposts. |
| STACK Infrastructure | https://www.stackinfra.com/locations/asia-pacific/tokyo/ | Inzai, Chiba. Official page describes two-building 36MW campus. | A for own page. |
| Digital Edge | https://www.digitaledgedc.com/products-services/data-centers/japan/ | Tokyo and Osaka; acquired CTC sites reported by Cloud Watch in 2021. | A for own page; B for acquisition press. |
| IDC Frontier / SoftBank | https://www.idcf.jp/en/datacenter/ and https://www.idcf.jp/en/datacenter/location/ | Tokyo Fuchu/Ariake/Nihombashi, Kanagawa Yokohama, Osaka Suita, Fukuoka Kitakyushu, plus SoftBank/IDC Frontier Tomakomai AI DC. SoftBank official release says first 50MW planned in FY2026 and later 300MW-plus at Tomakomai; DCD reported possible 1GW campus. | A for official IDC Frontier pages/SoftBank release; B for future campus scale. |
| Sakura Internet | https://www.sakura.ad.jp/ and Ishikari DC pages | Ishikari, Hokkaido; Osaka/Tokyo service footprint. Search `さくらインターネット 石狩データセンター GPU 整備`. | A for own pages; B for capacity/GPU plan unless filings/subsidy docs. |
| IIJ | https://www.iij.ad.jp/ | Matsue Data Center Park (Shimane), Shiroi DC Campus (Chiba), Osaka/Tokyo network sites. Search `IIJ 松江データセンターパーク`, `IIJ 白井 データセンターキャンパス`. | A for own pages. |
| NEC | https://jpn.nec.com/ and cloud/data center pages | Kobe, Kanagawa, Inzai/Chiba, Nagoya, Fuchu/enterprise sites. DCD/Bloomberg reported potential sale and three core cloud DCs. | A for own pages; B for sale/pipeline reporting. |
| Fujitsu | https://www.fujitsu.com/jp/services/infrastructure/data-center/ | Tatebayashi (Gunma), Yokohama, Akashi, Osaka/Tokyo/enterprise sites. Search Japanese service pages and annual reports. | A for own pages. |
| NRI / 野村総合研究所 | https://www.nri.com/jp/service/solution/mcs | Yokohama, Osaka, Tokyo-area enterprise DCs. | A for own page; capacity usually not public. |
| Internet Initiative Japan / regional telcos and electric-utility IT arms | own sites | Hokkaido, Tohoku, Chubu, Hokuriku, Shikoku, Kyushu regional enterprise DCs. | A for own pages; often small but important outside Tokyo/Osaka. |
| Regional operators: STNet, QTnet, K-Opticom/OPTAGE, HTNet, HBA, AGS, Aomori Cloud Base, KCCS, SCSK, CTC, TIS, NS Solutions, NTT West/East affiliates | own pages + JDCC member list | Takamatsu, Fukuoka/Kitakyushu, Osaka/Kansai, Toyama, Sapporo, Saitama, Aomori/Rokkasho, Ishikari, Tokyo/Osaka. | A for official; use JDCC as seed. |
| Real-estate/infrastructure developers: ESR, GLP, Gaw Capital, Goodman, Mitsui/Fidelity JV, Daiwa House, Hulic, Mitsubishi Estate, Keppel, STT GDC, EdgeConneX, Vantage, CyrusOne/KEPCO | company releases, DCD, ITmedia Built, property press | Chiba/Inzai/Shiroi, Osaka/Kansai, Fukuoka, Hokkaido. Many are planned/land-stage; status must be verified. | B unless official project page/filing. |

Vendor query templates:

```text
site:{vendor-domain} データセンター "{都道府県}"
site:{vendor-domain} データセンター "{市区町村}"
"{operator}" "{市区町村}" ("データセンター" OR "DC" OR "IDC") ("MW" OR "受電容量" OR "IT電力")
"{operator}" "{市区町村}" ("開設" OR "竣工" OR "着工" OR "地鎮祭" OR "運用開始")
"{operator}" "{市区町村}" ("用地取得" OR "土地取得" OR "開発許可" OR "建築確認")
"{operator legal name}" "有価証券報告書" データセンター
site:disclosure2.edinet-fsa.go.jp "{operator}" データセンター
site:www.release.tdnet.info "{operator}" データセンター
```

---

## 4. Hyperscaler official region pages

These are **A** for cloud region existence and city/metro naming, but not a physical facility census. Japan physical locations are usually leased or owned behind generic region names; pivot to local construction/vendor sources.

| Provider | Official URL | Japan region pivots |
|---|---|---|
| AWS | https://aws.amazon.com/local/japan/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | Asia Pacific (Tokyo) `ap-northeast-1`, Asia Pacific (Osaka) `ap-northeast-3`. Physical searches: `AWS 印西 データセンター`, `AWS 千葉 データセンター`, `AWS 大阪 データセンター`, `アマゾン データセンター 住民 反対`. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | Japan East (Tokyo/Saitama area in Azure naming), Japan West (Osaka). Physical searches: `マイクロソフト データセンター 日本`, `Microsoft Japan East データセンター`, `Azure 大阪 データセンター`. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | Tokyo `asia-northeast1`, Osaka `asia-northeast2`. Physical searches: `Google Cloud 東京 リージョン データセンター`, `Google 大阪 データセンター`, `グーグル データセンター 千葉`. |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ and OCI region docs | Japan East (Tokyo), Japan Central (Osaka). Search `Oracle Cloud Tokyo Osaka data center Japan`. |
| IBM Cloud / SAP / Salesforce / Akamai / Cloudflare / Fastly | official locations and peering pages | Usually colocated in Equinix/AT TOKYO/NTT/KDDI. Treat as demand/connectivity signal, not facility-owner proof. |

Pivot templates:

```text
"AWS" "ap-northeast-1" "data center" Japan
"AWS" "大阪" "データセンター" ("開設" OR "リージョン")
"Microsoft" "Japan East" "data center" "Saitama" OR "Tokyo"
"Google Cloud" "asia-northeast2" Osaka "data center"
"Oracle Cloud" Tokyo Osaka "data center" Japan
"{cloud provider}" "{metro}" ("Equinix" OR "AT TOKYO" OR "NTT" OR "Telehouse" OR "Digital Realty")
```

---

## 5. Japanese query patterns

### 5.1 National discovery sweep

Run these with both Kanji/kana place names and romanized English names:

```text
"{都道府県}" ("データセンター" OR "AIデータセンター" OR "IDC") ("開設" OR "竣工" OR "稼働" OR "運用開始")
"{都道府県}" ("データセンター" OR "AIデータセンター") ("着工" OR "地鎮祭" OR "起工式" OR "新設" OR "増設")
"{市区町村}" ("データセンター" OR "DC") ("MW" OR "メガワット" OR "受電容量" OR "IT電力")
"{市区町村}" ("データセンター" OR "AIデータセンター") ("用地取得" OR "土地取得" OR "誘致" OR "立地協定")
"{市区町村}" ("データセンター" OR "IDC") ("変電所" OR "特別高圧" OR "系統接続" OR "送電線")
"{市区町村}" ("データセンター" OR "IDC") ("建築確認" OR "開発許可" OR "環境影響評価" OR "公告")
"{都道府県}" ("データセンター" OR "計算基盤") ("補助金" OR "採択" OR "公募")
"{都道府県}" "ワット・ビット連携" データセンター
"{都道府県}" "GX戦略地域" データセンター
```

### 5.2 Official/local-government sweep

Japan local pages vary by domain, but prefectures usually use `pref.{pref}.lg.jp`; municipalities use `{city}.lg.jp`. Search both prefecture and city domains.

```text
site:pref.{pref}.lg.jp データセンター "{市区町村}"
site:pref.{pref}.lg.jp データセンター ("誘致" OR "立地" OR "補助金" OR "採択")
site:{city}.lg.jp データセンター ("誘致" OR "協定" OR "説明会" OR "公告")
site:{city}.lg.jp "{地区名}" データセンター
site:{city}.lg.jp ("建築確認" OR "開発許可") データセンター
site:{city}.lg.jp ("環境影響評価" OR "環境アセスメント") データセンター
site:{city}.lg.jp データセンター ("住民説明会" OR "反対" OR "騒音" OR "排熱")
```

Local-government signal words:

- `企業立地`, `産業立地`, `企業誘致`, `立地協定`, `進出協定`
- `工業団地`, `産業団地`, `流通業務団地`, `サイエンスパーク`, `テクノパーク`
- `港湾`, `臨海部`, `工業専用地域`, `市街化調整区域`, `用途地域`
- `開発行為`, `大規模建築物`, `建築計画`, `縦覧`, `公告`

### 5.3 Power, construction, and procurement sweep

Power and construction sources catch projects before operator marketing pages.

```text
"{市区町村}" データセンター ("特別高圧" OR "66kV" OR "154kV" OR "275kV")
"{市区町村}" データセンター ("変電所" OR "送電線" OR "系統接続" OR "受電")
site:{utility-domain} データセンター "{都道府県}"
site:{utility-domain} "{市区町村}" "データセンター"
"{市区町村}" データセンター ("竹中工務店" OR "大成建設" OR "清水建設" OR "鹿島" OR "大林組" OR "戸田建設")
"{市区町村}" データセンター ("入札" OR "落札" OR "設計" OR "施工" OR "EPC")
```

Major utility domain pivots:

```text
site:tepco.co.jp OR site:tepco-pg.co.jp データセンター
site:kepco.co.jp データセンター
site:chuden.co.jp データセンター
site:energia.co.jp データセンター
site:yonden.co.jp データセンター
site:kyuden.co.jp データセンター
site:heco.co.jp データセンター
site:tohoku-epco.co.jp データセンター
site:rikuden.co.jp データセンター
site:okiden.co.jp データセンター
```

### 5.4 English fallback

```text
"{prefecture}" Japan "data center" MW
"{city}" Japan "data center" "groundbreaking" OR "opened" OR "land"
"Inzai" "data center" AirTrunk Colt Digital Realty STACK NTT
"Shiroi" "data center" NTT STACK ESR
"Keihanna" "data center" Colt NTT
"Tomakomai" "AI data center" SoftBank IDC Frontier
"Ishikari" "data center" Sakura KCCS renewable
"Fukuoka" OR "Kitakyushu" "data center" Japan
```

---

## 6. Prefecture-by-prefecture enumeration matrix

For every prefecture, run:

1. `"{都道府県}" データセンター (開設 OR 着工 OR 補助金 OR 誘致 OR 受電容量)`
2. `site:pref.{pref}.lg.jp データセンター`
3. Local city/domain queries for the priority municipalities below.
4. Operator sweeps for the named vendors, plus JDCC member names with that prefecture.
5. Power-company and construction-company queries for high-capacity claims.

### Hokkaido / Tohoku

| Prefecture | Japanese queries and pivots | Known operator/region seeds |
|---|---|---|
| Hokkaido / 北海道 | `北海道 データセンター 石狩 苫小牧 札幌`, `石狩 データセンター さくら KCCS 再エネ`, `苫小牧 AIデータセンター ソフトバンク IDCフロンティア 50MW 300MW`, `北海道 ワット・ビット連携 データセンター` | Sakura Internet Ishikari, SoftBank/IDC Frontier Tomakomai, KCCS zero-emission Ishikari, HBA/Sapporo, AT TOKYO Hokkaido. |
| Aomori / 青森 | `青森 データセンター 六ヶ所 八戸`, `青い森クラウドベース データセンター`, `六ヶ所 再エネ データセンター` | Aomori Cloud Base, renewable/cold-climate projects, GX-region leads. |
| Iwate / 岩手 | `岩手 データセンター 盛岡 北上`, `岩手 AIデータセンター 誘致`, `岩手 工業団地 データセンター` | Mostly emerging/local-government leads; verify through prefecture/city pages. |
| Miyagi / 宮城 | `宮城 データセンター 仙台`, `宮城AIデータセンター 東北電力 コンテナ型`, `仙台 データセンター 竣工` | Tohoku Electric/Tohoku regional IT operators; Sendai enterprise sites. |
| Akita / 秋田 | `秋田 データセンター 再エネ`, `秋田 AIデータセンター 誘致`, `秋田 風力 データセンター` | Weak emerging leads; use power/renewable and GX searches. |
| Yamagata / 山形 | `山形 データセンター`, `山形 企業誘致 データセンター`, `米沢 データセンター` | Mostly local enterprise/municipal leads. |
| Fukushima / 福島 | `福島 データセンター 郡山 会津`, `会津 データセンター`, `福島 再エネ AIデータセンター` | Search disaster-resilience and renewable projects. |

### Kanto

| Prefecture | Japanese queries and pivots | Known operator/region seeds |
|---|---|---|
| Ibaraki / 茨城 | `茨城 データセンター つくば 常総`, `つくば データセンター`, `茨城 企業誘致 データセンター` | Science/research/enterprise sites; watch overflow from Chiba/Tokyo. |
| Tochigi / 栃木 | `栃木 データセンター 宇都宮`, `栃木 工業団地 データセンター` | Low-density; local gov and industrial park searches. |
| Gunma / 群馬 | `群馬 データセンター 館林`, `富士通 館林 データセンター`, `前橋 高崎 データセンター` | Fujitsu Tatebayashi and enterprise/DR sites. |
| Saitama / 埼玉 | `埼玉 データセンター さいたま 戸田`, `NTT 埼玉 データセンター`, `Azure Japan East 埼玉 データセンター` | NTT/enterprise metro facilities, hyperscaler ambiguity, Tokyo overflow. |
| Chiba / 千葉 | `千葉 データセンター 印西 白井`, `印西 データセンター AirTrunk Colt Digital Realty STACK`, `白井 データセンター NTT`, `千葉 データセンター 住民説明会` | Japan's key hyperscale cluster: Inzai, Shiroi, Chiba New Town; AirTrunk TOK1, Colt Inzai, MC Digital Realty/Digital Realty NRT, STACK, NTT Shiroi, likely hyperscaler leases. |
| Tokyo / 東京 | `東京 データセンター 大手町 豊洲 府中 多摩`, `AT TOKYO 中央センター`, `Equinix TY 東京`, `KDDI Telehouse 大手町 多摩`, `IDCフロンティア 府中 有明 日本橋` | AT TOKYO, Equinix, KDDI/Telehouse, IDC Frontier, NTT, Digital Edge, KINX/network-rich urban sites. |
| Kanagawa / 神奈川 | `神奈川 データセンター 横浜 川崎 座間`, `IDCフロンティア 横浜 データセンター`, `NEC 神奈川 データセンター`, `富士通 横浜 データセンター` | Yokohama/Kawasaki enterprise and metro DR sites; IDC Frontier, Fujitsu, NEC, CEC. |

### Chubu / Hokuriku

| Prefecture | Japanese queries and pivots | Known operator/region seeds |
|---|---|---|
| Niigata / 新潟 | `新潟 データセンター 長岡`, `新潟 AIデータセンター 再エネ`, `新潟 ワット・ビット連携` | Regional decentralization and power-linked candidates. |
| Toyama / 富山 | `富山 データセンター`, `北陸 データセンター HTNet 富山`, `富山 企業誘致 データセンター` | Hokuriku Telecom/HTNet and regional IT sites. |
| Ishikawa / 石川 | `石川 データセンター 金沢`, `金沢 データセンター`, `北陸 データセンター 石川` | Regional enterprise/telecom sites. |
| Fukui / 福井 | `福井 データセンター`, `福井 企業誘致 データセンター`, `敦賀 データセンター` | Low-density; power/infrastructure searches. |
| Yamanashi / 山梨 | `山梨 データセンター`, `山梨 AIデータセンター 再エネ`, `山梨 誘致 データセンター` | Tokyo-adjacent/renewable candidate; verify carefully. |
| Nagano / 長野 | `長野 データセンター 松本`, `長野 寒冷地 データセンター`, `長野 企業誘致 データセンター` | Cold-climate/DR searches; local operators. |
| Gifu / 岐阜 | `岐阜 データセンター`, `岐阜 工業団地 データセンター` | Low-density; search Chubu overflow. |
| Shizuoka / 静岡 | `静岡 データセンター 浜松`, `静岡 再エネ データセンター`, `浜松 データセンター` | Chubu/Tokyo-Osaka corridor; enterprise and power-linked leads. |
| Aichi / 愛知 | `愛知 データセンター 名古屋`, `名古屋 データセンター KDDI NTT NEC`, `中部 データセンター` | Nagoya metro sites, KDDI/Telehouse, NEC, NTT, Chubu enterprise operators. |

### Kansai

| Prefecture | Japanese queries and pivots | Known operator/region seeds |
|---|---|---|
| Mie / 三重 | `三重 データセンター`, `三重 工業団地 データセンター`, `四日市 データセンター` | Low-density; search power and industrial land. |
| Shiga / 滋賀 | `滋賀 データセンター`, `滋賀 企業誘致 データセンター`, `草津 データセンター` | Osaka/Kyoto overflow candidate. |
| Kyoto / 京都 | `京都 データセンター けいはんな`, `精華町 データセンター Colt NTT`, `京田辺 データセンター`, `京都 環境影響評価 データセンター` | Keihanna Science City: Colt Osaka Keihanna, NTT Keihanna/OSK11. |
| Osaka / 大阪 | `大阪 データセンター 茨木 吹田 堺 梅田`, `NTT 大阪北 データセンター 茨木 36MW`, `IDCフロンティア 吹田`, `Equinix Osaka`, `AT TOKYO 大阪`, `Digital Realty KIX`, `Azure Google Oracle Osaka region` | Japan's second core metro: NTT, Equinix, AT TOKYO, Digital Realty/MC Digital Realty, IDC Frontier, KDDI/Telehouse, Digital Edge. |
| Hyogo / 兵庫 | `兵庫 データセンター 神戸`, `NEC 神戸 データセンター`, `神戸 データセンター 竣工` | NEC Kobe, enterprise/DR sites, Osaka-adjacent demand. |
| Nara / 奈良 | `奈良 データセンター`, `奈良 けいはんな データセンター`, `奈良 企業誘致 データセンター` | Keihanna-adjacent leads; verify municipality. |
| Wakayama / 和歌山 | `和歌山 データセンター`, `和歌山 再エネ データセンター`, `白浜 データセンター` | Disaster-recovery and regional candidate searches. |

### Chugoku / Shikoku

| Prefecture | Japanese queries and pivots | Known operator/region seeds |
|---|---|---|
| Tottori / 鳥取 | `鳥取 データセンター`, `鳥取 企業誘致 データセンター` | Low-density; local gov/enterprise. |
| Shimane / 島根 | `島根 データセンター 松江`, `IIJ 松江データセンターパーク`, `松江 データセンター 外気冷却` | IIJ Matsue Data Center Park is the anchor. |
| Okayama / 岡山 | `岡山 データセンター`, `岡山 企業誘致 データセンター`, `岡山 受電容量 データセンター` | Chugoku regional/DR candidate. |
| Hiroshima / 広島 | `広島 データセンター`, `AT TOKYO 広島 データセンター`, `中国地方 データセンター` | AT TOKYO Hiroshima and regional operators. |
| Yamaguchi / 山口 | `山口 データセンター`, `山口 再エネ データセンター`, `山口 企業誘致 データセンター` | Low-density; power/industrial land. |
| Tokushima / 徳島 | `徳島 データセンター`, `徳島 サテライトオフィス データセンター`, `徳島 企業誘致 データセンター` | Small/regional leads. |
| Kagawa / 香川 | `香川 データセンター 高松`, `STNet Powerico 新高松データセンター`, `高松 データセンター` | STNet/Takamatsu anchor. |
| Ehime / 愛媛 | `愛媛 データセンター 松山`, `愛媛 企業誘致 データセンター` | Regional enterprise/telecom. |
| Kochi / 高知 | `高知 データセンター`, `高知 企業誘致 データセンター`, `高知 防災 データセンター` | Low-density; DR/local-gov searches. |

### Kyushu / Okinawa

| Prefecture | Japanese queries and pivots | Known operator/region seeds |
|---|---|---|
| Fukuoka / 福岡 | `福岡 データセンター 北九州`, `IDCフロンティア 北九州 データセンター`, `QTnet データセンター 福岡`, `AT TOKYO 福岡`, `福岡 AIデータセンター` | Fukuoka/Kitakyushu are top decentralization candidates; IDC Frontier, QTnet, AT TOKYO, NTT/KDDI/regional operators. |
| Saga / 佐賀 | `佐賀 データセンター`, `佐賀 企業誘致 データセンター`, `鳥栖 データセンター` | Fukuoka spillover; local-gov/industrial park. |
| Nagasaki / 長崎 | `長崎 データセンター`, `長崎 企業誘致 データセンター`, `長崎 海底ケーブル データセンター` | Subsea/DR candidate; verify. |
| Kumamoto / 熊本 | `熊本 データセンター`, `熊本 半導体 データセンター`, `熊本 AIデータセンター` | Semiconductor cluster may create future DC/power leads; separate factories from DCs. |
| Oita / 大分 | `大分 データセンター`, `大分 再エネ データセンター`, `大分 企業誘致 データセンター` | Power/renewable candidate. |
| Miyazaki / 宮崎 | `宮崎 データセンター`, `宮崎 企業誘致 データセンター`, `宮崎 再エネ データセンター` | Low-density; local gov. |
| Kagoshima / 鹿児島 | `鹿児島 データセンター`, `鹿児島 再エネ データセンター`, `鹿児島 海底ケーブル データセンター` | Renewable/subsea candidate; verify. |
| Okinawa / 沖縄 | `沖縄 データセンター`, `AT TOKYO 沖縄 データセンター`, `沖縄 クロス・ヘッド データセンター`, `沖縄 海底ケーブル データセンター` | Okinawa DR/subsea node; AT TOKYO Okinawa, Okinawa Cross Head/regional operators. |

---

## 7. Verification and grading recipe

Grade each data point, not just each project.

1. **Existence/location**
   - A: operator facility page, official press release, local-government record, building/environment/public notice.
   - B: Impress/ITmedia/DCD/Bloomberg/Nikkei article with named facility and municipality.
   - C: aggregator map, broker list, job posting, conference slide, or repost.
2. **Status**
   - Count `運用開始`, `稼働`, `開設`, `竣工` as operational only if operator/government or repeated trade press confirms.
   - Count `着工`, `地鎮祭`, `起工式` as under construction.
   - Keep `誘致`, `覚書`, `協定`, `構想`, `予定`, `最大`, `将来的に` as planned/proposed.
3. **Capacity**
   - Prefer `IT電力`, `IT負荷`, `IT power`, `受電容量`, `電力容量`, `サーバールーム面積`, `ラック数`.
   - Distinguish building/phase from campus buildout: `第1期`, `新棟`, `全体`, `最終`, `最大`, `将来的に`.
   - Treat `受電容量` and `IT電力` as different when both are present. Japanese press sometimes loosely equates them; record the original label.
4. **No double counting**
   - Same campus may appear under operator, JV, landowner, contractor, and cloud customer. Key record by `(ultimate operator, campus name, phase/building, municipality)`.
   - Watch aliases: Inzai may be described as `Tokyo` in English; Keihanna may be marketed as `Osaka` while located in Kyoto/Nara border municipalities.
5. **Resident opposition / cancellation**
   - Search `住民説明会`, `反対`, `騒音`, `排熱`, `景観`, `中止`, `撤回`, `延期`, `白紙` for each large planned site.

Suggested source grades:

| Source type | Grade |
|---|---|
| METI/MIC/Digital Agency subsidy and policy pages; local-government permits/notices | A |
| Operator official facility page or press release | A for existence/status; B/A- for capacity depending specificity |
| Listed-company filings / TDnet / EDINET | A |
| Utility/grid releases, public procurement/contract award notices | A/A- |
| Impress Cloud Watch, ITmedia Built, DCD, Nikkei/Bloomberg | B/B+ |
| JDCC member list | B+ for operator seeds, not facility proof |
| Broker reports from CBRE/JLL/Cushman/IDC/Arizton/ResearchAndMarkets | B for market context, C/B for facility details unless named/sourced |
| DataCenterMap/Baxtel/Cloudscene/Datacenters.com/OCOLO | C lead source |
| Local promotional MoU articles, social media, blogs | C |

---

## 8. Recommended JP discovery pipeline

1. **Seed operators** from JDCC member list, top vendor pages, and aggregator maps. Build a vendor dictionary with Japanese name, English name, parent/JV, and official domain.
2. **Run trade-press sweeps** across Impress Cloud Watch, ITmedia Built, DCD, Nikkei/Bloomberg, and Data Center Cafe for the last 5 years using status verbs and known clusters.
3. **Run the prefecture matrix**. Prioritize Chiba, Tokyo, Osaka, Kyoto, Kanagawa, Saitama, Hokkaido, Fukuoka, Aomori, Miyagi, Shimane, Kagawa, Okinawa, Aichi, Hyogo, Gunma.
4. **Check official trails**: METI subsidy selections, Digital Agency/MIC policy pages, municipality announcements, environmental/building/public notices, power-company releases, and construction bids.
5. **Verify capacity/status** by operator release or official/local record. Split current operational, under-construction, and planned campus buildout.
6. **Alias reconciliation**: normalize English marketing metros to real municipalities, e.g. `Tokyo` = Inzai/Shiroi/Fuchu/Otemachi/Tama/etc.; `Osaka` = Ibaraki/Suita/Keihanna/Sakai/urban Osaka.

Pitfalls recap: English `Tokyo` often means Chiba or Saitama; `Osaka` can mean Kyoto's Keihanna; `MW` may be utility receiving capacity rather than IT load; local `誘致` and `協定` articles are not construction evidence; Japanese operators often market services without exact addresses for security; aggregators duplicate old/renamed sites.
