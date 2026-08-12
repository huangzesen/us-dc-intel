# BT Explorer - Industry / Press / Vendor Discovery for Bhutan Datacenters

Date: 2026-08-12. Scope: Bhutan datacenter and digital-infrastructure discovery through trade press, local media, operator/vendor pages, mining-sector disclosures, directories, and dzongkhag-level query patterns. Repo divisions: Paro, Chhukha, Haa, Samtse, Thimphu, Tsirang, Dagana, Punakha, Wangdue Phodrang, Sarpang, Trongsa, Bumthang, Zhemgang, Trashigang, Monggar, Pema Gatshel, Lhuentse, Samdrup Jongkhar, Gasa, Trashi Yangtse.

Reliability grades: **A** = primary/official/operator/company filing/regulator; **B** = established trade press or local media with named operator/site/capacity; **C** = directory, market report, social post, promotional article, or unsourced aggregator.

---

## 0. Bhutan-specific industry frame

- Bhutan is a **small datacenter market with a large energy narrative**. Confirmed non-mining facilities are concentrated at Thimphu TechPark: GovTech's Government Data Centre (GDC), Data Centre Services (DCS), and btIX. Large-MW coverage mostly concerns Bitdeer/DHI crypto-mining or proposed AI compute campuses.
- Industry coverage often conflates four different asset classes: **government hosting**, **commercial colocation**, **crypto-mining datacenters**, and **planned AI/GPU infrastructure**. Preserve the asset class before counting capacity.
- Status verbs are mandatory. `LOI`, `proposal`, `feasibility study`, `roadmap target`, `under construction`, `energized`, `online`, and `operational` mean different things in Bhutan.
- Latest verified Bitdeer status changed the earlier draft: Bitdeer public materials in 2026 list **Gedu, Bhutan - 100 MW - Online - Crypto** and **Jigmeling, Bhutan - 500 MW - Online - Crypto**. Do not describe Jigmeling as merely planned unless using older historical coverage.
- SATO/GMC is the opposite case: it is an **LOI** announced July 2026, not a built facility. SATO says the project would start at 5 MW, target about 100 MW firm hydro power, and may scale toward 500 MW; record these as planned pathway values.
- English is the main language for discovery. Bhutanese English-language media (The Bhutanese, Kuensel, BBS, Business Bhutan) is more useful than Dzongkha for this domain.

Verified anchor URLs:

- DCS official site: https://www.dcs.bt/
- GovTech/GDC ITU presentation: https://www.itu.int/en/ITU-D/Regional-Presence/AsiaPacific/Documents/Events/2023/RDF-2023/Presentations%20and%20Relevant%20Reports/Session%209/Speaker%204%20Bhutan%20Session%209%20presentation%20Mr%20Choney.pdf
- Bitdeer June 2026 operations update: https://ir.bitdeer.com/news-releases/news-release-details/bitdeer-announces-june-2026-production-and-operations-update/
- Bitdeer Q2 2026 results PDF: https://ir.bitdeer.com/node/9696/pdf
- DHI and Bitdeer partnership release: https://www.dhi.bt/newsroom/news/69455944151590a78f28ad59
- SATO LOI: https://www.bysato.com/news/sato-bhutan-sovereign-ai-compute-campus
- Data Center Dynamics SATO article: https://www.datacenterdynamics.com/en/news/former-cryptominer-sato-inks-preliminary-agreement-to-develop-ai-data-center-in-bhutan/
- The Bhutanese 40-50 MW roadmap story: https://thebhutanese.bt/bhutan-aims-to-build-usd-450-million-data-center/
- The Bhutanese DHI AI proposal: https://thebhutanese.bt/dhi-proposes-ai-data-center-powered-entirely-by-renewable-energy/
- The Bhutanese Jigmeling story: https://thebhutanese.bt/500-mw-bitcoin-mine-to-start-operation-in-phases-from-mid-2025-in-jigmeling/
- DCD GDC opening story: https://www.datacenterdynamics.com/en/news/the-kingdom-of-bhutan-opens-first-government-data-center/
- DCD Gedu story: https://www.datacenterdynamics.com/en/news/bitdeer-completes-construction-of-100mw-bhutan-cryptomine-data-center/
- PeeringDB btIX: https://www.peeringdb.com/ix/2355

---

## 1. High-signal industry and press sources

Use industry/local sources to find project names, operators, MW claims, timelines, photos, and official quotes. Then pivot to official/operator/utility evidence.

| Source | URL/search surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ search `Bhutan` | Best free trade source for Bhutan DC/mining/AI stories: GDC opening, Gedu, Bitdeer/Jigmeling, SATO/GMC. | B |
| The Bhutanese | https://thebhutanese.bt/ search `data center` | Strong local detail on Roadmap 40-50 MW, DHI AI proposal, Jigmeling, official quotes, policy framing. | B+; A- for direct named official quotes |
| Kuensel | https://kuenselonline.com/ | National newspaper; good for government, parliament, energy, GMC, BICMA, and telecom context. | B |
| BBS | https://www.bbs.bt/ | National broadcaster; useful for official launches and licensing stories. | B |
| Business Bhutan | https://businessbhutan.bt/ | Business/FDI/TechPark/GMC/DHI angle. | B |
| DHI | https://dhi.bt/ and DHI PDFs | Operator/investor source for Green Digital, Bitdeer partnership, DHI 10X AI datacenter strategy. | A |
| Bitdeer IR/SEC | https://ir.bitdeer.com/ and SEC filings | Best source for current Gedu/Jigmeling capacity/status. | A |
| SATO Technologies | https://www.bysato.com/news/ | Primary source for SATO-GMCA LOI, planned AI campus, phased MW claims. | A for own announcement |
| GMCA / GMC | https://gmc.bt/news/ and official social channels | Official GMC zone/LOI/investment announcements; website can be JS-heavy, so site-search and social mirrors help. | A for official posts |
| GovInsider Asia | https://govinsider.asia/ | Government-tech and digital-assets context, especially DHI/Green Digital narratives. | B |
| The Block / CoinDesk / Cointelegraph / Bitcoin.com | site-scoped searches | Crypto-mining financing and Bitdeer/DHI coverage. Strong for public-company filing summaries; weak for exact addresses. | B/C |
| Baxtel / DataCenterMap / Cloudscene | https://baxtel.com/data-center/bhutan ; https://www.datacentermap.com/bhutan/ | Facility leads and rough inventory. Treat capacity/status as unverified until backed by A/B sources. | C |
| PeeringDB / PCH | https://www.peeringdb.com/ix/2355 ; https://www.pch.net/ixp/details/1954 | IX/facility interconnection evidence for btIX at Thimphu TechPark. | A for IX facts |
| Market reports | Arizton, ResearchAndMarkets, Mordor, etc. | Market sizing and demand context only. Do not use for facility proof. | C |

Trade/local search patterns:

```text
site:datacenterdynamics.com/en/news/ Bhutan ("data center" OR "data centre" OR "AI" OR "Bitdeer" OR "SATO")
site:thebhutanese.bt ("data center" OR "data centre" OR "AI" OR "mining" OR "Jigmeling" OR "Gedu")
site:kuenselonline.com ("data center" OR "data centre" OR "GMC" OR "Bitdeer" OR "SATO")
site:bbs.bt ("data center" OR "Bitdeer" OR "Jigmeling" OR "BICMA" OR "Starlink")
site:businessbhutan.bt ("DHI" OR "GMC" OR "TechPark") ("data" OR "AI" OR "digital")
site:govinsider.asia Bhutan ("digital assets" OR "AI" OR "data center")
site:theblock.co OR site:coindesk.com OR site:cointelegraph.com ("Bitdeer" "Bhutan")
```

---

## 2. Vendor/operator seed list

| Operator/developer | Primary URLs | Bhutan signal | Grade and handling |
|---|---|---|---|
| GovTech Agency / GDC / Neyduetewa | https://tech.gov.bt/ ; https://support.neyduetewa.gov.bt/ ; ITU PDF | Government DC at Thimphu TechPark, operationalized 2017; ITU says 200+ government systems in 2023. | A for existence/status; capacity stats only with source/date. |
| Data Centre Services Pvt. Ltd. (DCS) | https://www.dcs.bt/ ; https://www.dcs.bt/about-us/ | Tier 2/3 Internet Data Centre inside Thimphu TechPark, commercial colo/hosting/backup/connectivity. | A for operator claims; verify exact racks/MW if needed. |
| Thimphu TechPark Ltd | https://thimphutechpark.bt/ | Host IT park for GDC/DCS/btIX and IT/ITES tenants. | A for park; B/C for tenant rumors. |
| btIX | https://www.btix.bt/ ; https://www.peeringdb.com/ix/2355 | Bhutan Internet Exchange at Thimphu TechPark. | A for IX; not a DC record alone. |
| DHI / Green Digital | https://dhi.bt/ | State investment arm; Green Digital/Bitdeer mining partnership; DHI 10X AI datacenter strategy. | A for strategy/partnership, site-specific only when named. |
| Bitdeer | https://ir.bitdeer.com/ ; https://www.bitdeer.com/ | Gedu 100 MW online crypto; Jigmeling 500 MW online crypto in 2026 public materials. | A for status/capacity from IR/filings; asset class `crypto`. |
| GMCA / GMC | https://gmc.bt/ | Gelephu Mindfulness City / Sarpang; Green Technology Valley; SATO LOI. | A for official GMC announcements. |
| SATO Technologies | https://www.bysato.com/news/sato-bhutan-sovereign-ai-compute-campus | LOI for hydro-powered sovereign AI compute campus in GMC; 5 MW initial, 100 MW firm hydro target, potential 500 MW pathway. | A for LOI; B for future scale until permits/construction. |
| Bhutan Telecom | https://www.bhutan-telecom.bt/ | State telco, DrukNet/fiber/backbone; possible enterprise hosting/server rooms. | A for telecom service, C for facility details until explicit. |
| Tashi InfoComm / TashiCell | https://www.tashicell.bt/ | Second mobile/ISP operator; possible core network/server rooms. | A for telecom service, C for facility details until explicit. |
| NewEdge Technologies | via DCS pages | DCS JV partner. | C+ lead unless own facility evidence appears. |

Operator query bundle:

```text
"Data Centre Services" Bhutan ("Tier" OR "colocation" OR "TechPark" OR "Olakha" OR "Semtokha")
"Government Data Centre" OR "Government Data Center" OR "Neyduetewa" Bhutan
"Bitdeer" ("Gedu" OR "Jigmeling") ("MW" OR "online" OR "energized" OR "crypto")
site:ir.bitdeer.com Bhutan ("Gedu" OR "Jigmeling" OR "Online" OR "MW")
"SATO" "Bhutan" ("AI data center" OR "Gelephu" OR "100 MW" OR "500 MW")
"Gelephu Mindfulness City" ("SATO" OR "AI data center" OR "Green Technology Valley")
"DHI" "Bhutan" ("AI data center" OR "Green Digital" OR "Bitdeer")
"Bhutan Telecom" ("data center" OR "colocation" OR "cloud" OR "server room")
"TashiCell" OR "Tashi InfoComm" ("data center" OR "cloud" OR "server room")
```

---

## 3. Project/status watchlist

### 3.1 Operational or online

| Project | Division | Asset class | Current status | Best evidence |
|---|---|---|---|---|
| Government Data Centre / GDC / Neyduetewa | Thimphu | Government/sovereign hosting | Operational since 2017 | ITU presentation, GDC support portal, DCD opening story |
| DCS Internet Data Centre | Thimphu | Commercial colo/hosting | Operational | DCS official pages |
| btIX | Thimphu | Internet exchange | Operational | PeeringDB, btIX/PCH |
| Bitdeer Gedu | Chhukha | Crypto-mining datacenter | 100 MW online crypto in 2026 Bitdeer materials | Bitdeer June 2026/Q2 2026 materials; DCD 2023 for historical construction |
| Bitdeer Jigmeling | Sarpang | Crypto-mining datacenter | 500 MW online crypto in 2026 Bitdeer materials | Bitdeer June 2026/Q2 2026 materials; The Bhutanese/BBS/DCD for historical launch/construction |

### 3.2 Planned, proposal, or LOI

| Project | Division | Asset class | Current status | Handling |
|---|---|---|---|---|
| 40-50 MW / USD 450M national datacenter | TBD; GMC/Sarpang possible but not fixed | National / AI-ready / commercial datacenter | Roadmap/feasibility; construction target 2027 in local reporting | Keep as pipeline. Upgrade only after official site selection, land, utility, permit, or construction evidence. |
| DHI AI datacenter proposal | TBD | AI/GPU compute / GPU colocation / cloud AI | Proposal presented at Invest Bhutan Summit 2026; DHI roadmap supports feasibility studies for green AI datacenters | Do not count as operational. Extract business model and power claims as proposal fields. |
| SATO-GMCA AI compute campus | Sarpang / GMC / Gelephu | AI datacenter campus | LOI effective 2026-06-20, announced 2026-07-06; phased 5 MW start, 100 MW target, possible 500 MW expansion | Record as `planned_LOI`. Do not count 100/500 MW as live capacity. |

Status-verification queries:

```text
"Bhutan aims to build USD 450 million data center" "2027"
"DHI proposes AI Data Center powered entirely by renewable energy"
"Invest Bhutan Summit" "AI Data Center" "DHI"
"GMCA and SATO sign LOI" "AI data center"
"SATO Technologies" "effective date" "June 20, 2026" Bhutan
"Bitdeer Reports Unaudited Financial Results" "Gedu, Bhutan" "Jigmeling, Bhutan"
"Bitdeer Announces June 2026 Production" "Jigmeling, Bhutan" "Online"
```

---

## 4. Hyperscaler/cloud discovery

Official cloud pages are useful mainly to prevent false positives. Bhutan does not have a public AWS, Azure, Google Cloud, or Oracle OCI cloud region as of 2026-08. Any "cloud in Bhutan" claim is likely one of:

- government-hosted services at GDC/Neyduetewa,
- commercial services at DCS,
- telco/ISP hosting,
- out-of-country hyperscaler region serving Bhutan customers,
- planned AI/GPU infrastructure not yet built.

Queries:

```text
"AWS" "Bhutan" ("region" OR "availability zone" OR "edge")
"Microsoft Azure" "Bhutan" ("region" OR "data center")
"Google Cloud" "Bhutan" ("region" OR "data center")
"Oracle Cloud" "Bhutan" ("region" OR "data center")
"cloud" "Bhutan" ("GovTech" OR "DCS" OR "DHI" OR "Neyduetewa")
"sovereign cloud" Bhutan
"data residency" Bhutan ("cloud" OR "data center")
```

---

## 5. English search patterns

Use US and British spellings, plus Bhutan-specific place names and lifecycle terms.

```text
"Bhutan" ("data center" OR "data centre" OR datacenter OR datacentre)
"Bhutan" ("data center" OR "data centre") ("MW" OR "IT load" OR "racks" OR "GPU" OR "hydropower")
"Bhutan" ("colocation" OR "colo" OR "carrier neutral" OR "Tier II" OR "Tier III")
"Bhutan" ("groundbreaking" OR "construction" OR "energized" OR "online" OR "operational") "data"
"Bhutan" ("bitcoin mining" OR "crypto mining" OR "digital asset mining") ("data center" OR "facility" OR "MW")
"Gedu" OR "Jigmeling" ("Bitdeer" OR "data center" OR "mining" OR "MW")
"Gelephu" OR "GMC" OR "Gelephu Mindfulness City" ("data center" OR "AI" OR "SATO" OR "Green Technology Valley")
"Thimphu TechPark" ("data centre" OR "DCS" OR "GDC" OR "btIX")
"Bhutan" ("fiber" OR "internet exchange" OR "btIX" OR "bandwidth") ("India" OR "Bangladesh")
"Bhutan" "data center" ("power" OR "hydropower" OR "substation" OR "seasonal")
```

Dzongkha note: do not spend much time on Dzongkha for datacenters. If a local Dzongkha-only announcement appears, look for the English BBS/Kuensel/The Bhutanese version and use that for structured extraction.

---

## 6. Division enumeration method

Enumeration unit is the dzongkhag, but evidence is usually a town/site. Use `dzongkhag -> town/site -> operator -> status -> official cross-check`.

### 6.1 Thimphu

Targets: GDC/Neyduetewa, DCS, Thimphu TechPark, btIX, Bhutan Telecom/Tashi core sites, bank/government server rooms.

```text
"Thimphu" ("data center" OR "data centre" OR colocation OR "server room")
"Thimphu TechPark" ("DCS" OR "data centre" OR "Government Data Centre" OR "btIX")
"Neyduetewa" OR "GDC" "Thimphu"
"Thimphu" ("Bhutan Telecom" OR "TashiCell" OR "Tashi InfoComm") ("exchange" OR "data center" OR "cloud")
"Thimphu" ("BPC" OR "substation" OR "Olakha" OR "Semtokha") "data"
```

### 6.2 Sarpang

Targets: Jigmeling Industrial Park / Bitdeer 500 MW crypto, Gelephu/GMC, SATO LOI, Green Technology Valley.

```text
"Sarpang" ("data center" OR "data centre" OR "AI" OR "mining")
"Jigmeling" ("Bitdeer" OR "500 MW" OR "data center" OR "mining" OR "online")
"Gelephu" ("data center" OR "AI" OR "GMC" OR "Green Technology Valley")
"Gelephu Mindfulness City" ("SATO" OR "data centre" OR "AI compute")
site:thebhutanese.bt "Jigmeling" "500 MW"
site:gmc.bt OR site:bysato.com "Gelephu" "SATO"
```

### 6.3 Chhukha / Chukha

Targets: Gedu / Bitdeer 100 MW crypto, Chukha/Tala hydro corridor, Phuentsholing industrial and cross-border connectivity leads.

```text
"Chhukha" OR "Chukha" ("data center" OR "data centre" OR "mining" OR "Bitdeer")
"Gedu" ("Bitdeer" OR "100 MW" OR "data center" OR "mining" OR "online")
"Phuentsholing" ("data center" OR "colocation" OR "server room" OR "IT")
"Chukha" ("hydropower" OR "substation" OR "transmission") ("data" OR "mining")
```

### 6.4 Other 17 dzongkhags - negative sweep

For Paro, Haa, Samtse, Tsirang, Dagana, Punakha, Wangdue Phodrang, Trongsa, Bumthang, Zhemgang, Trashigang, Monggar, Pema Gatshel, Lhuentse, Samdrup Jongkhar, Gasa, and Trashi Yangtse, run and log a negative sweep. Known hydro projects, substations, fiber routes, airports, banks, hospitals, and government offices are not datacenters unless a source says datacenter/data centre/server room/colo/HPC/AI compute/mining facility.

```text
"{dzongkhag}" ("data center" OR "data centre" OR datacenter OR "server room" OR "cloud")
"{dzongkhag}" ("AI" OR "GPU" OR "HPC" OR "supercomputer" OR "mining")
"{dzongkhag}" ("Bhutan Telecom" OR "TashiCell" OR "Tashi InfoComm") ("exchange" OR "fiber" OR "server")
"{dzongkhag}" ("BPC" OR "DGPC" OR "hydropower" OR "substation")
"{dzongkhag}" ("industrial park" OR "FDI" OR "digital infrastructure" OR "IT park")
```

Special watch items:

- **Paro:** airport/connectivity and government continuity claims; no confirmed datacenter from current sources.
- **Samtse / Samdrup Jongkhar:** industrial-border leads; no confirmed datacenter from current sources.
- **Punakha / Wangdue Phodrang:** Punatsangchhu/Sephu energy context; not datacenter evidence.
- **Trongsa:** Mangdechhu/Nikachhu energy context; not datacenter evidence.
- **Trashigang / Monggar / Pema Gatshel / Lhuentse / Trashi Yangtse:** eastern hydro/education/government-server leads only; no confirmed datacenter from current sources.
- **Gasa / Haa / Dagana / Tsirang / Zhemgang / Bumthang:** low probability; log negative searches.

---

## 7. Directory and market-report handling

Directories are useful lead generators but weak evidence:

- **Baxtel** may list DCS, Gedu, Jigmeling, and possible total MW. Use it to find names, then verify against DCS/Bitdeer.
- **DataCenterMap** may list planned SATO/Gelephu or DCS. Treat status and address as C unless operator/GMCA confirms.
- **Cloudscene/Datacenters.com/OCOLO-like directories** are normally C for Bhutan.
- **Market reports** often describe "Bhutan data center market" without facility lists. Use only for demand context, never facility proof.

Directory queries:

```text
site:baxtel.com Bhutan "data center"
site:datacentermap.com/bhutan ("DCS" OR "Bitdeer" OR "SATO" OR "Gelephu")
site:cloudscene.com Bhutan "data center"
"Bhutan data center market" ("Arizton" OR "Mordor" OR "ResearchAndMarkets")
```

---

## 8. Validation rules and pitfalls

### Evidence hierarchy

1. **A:** operator/company filing, government/regulator/utility page, official cloud-region page, PeeringDB for IX, official PDF/presentation.
2. **B:** established local/trade press with named site/operator/date/MW.
3. **C:** directory/social/market-report or promotional material.

### Capacity handling

- Keep **electrical MW**, **IT MW**, **crypto/mining MW**, **firm power allocation**, and **future expansion pathway** separate.
- For Bitdeer, public materials describe electrical capacity and planned usage as crypto; do not convert to IT load.
- For SATO, `5 MW`, `100 MW`, and `500 MW` are planned/LOI pathway numbers until evidence of power allocation, lease, construction, or energization appears.
- For the Roadmap national datacenter, `40-50 MW` and `USD 450M` are planning targets. Do not assign a division until site selection is official.

### Common false positives

- Hydropower plant or substation = power source/context, not a datacenter.
- Telecom exchange or ISP POP = lead only unless marketed or filed as datacenter/colo.
- Cloud service availability in Bhutan = not a Bhutan cloud region.
- Crypto-mining datacenter = count separately from commercial colocation and AI cloud.
- GMC investment theme = not a facility unless tied to a named developer and status.

### Output fields

For every positive or pipeline record, store:

- `name`, `operator`, `asset_class`, `division`, `town/site`
- `status`, `status_date`, exact source status verb
- `capacity_electrical_mw`, `capacity_it_mw`, `capacity_crypto_mw`, `planned_scale_mw`
- `power_source`, `substation/feed`, `seasonal_power_caveat`
- `connectivity`, `IX/PeeringDB`, `fiber/ISP`
- `source_grade`, `source_url`, `notes`

### Known seed inventory for starting a run

| Name | Division | Asset class | Status | Source grade |
|---|---|---|---|---|
| GDC / Neyduetewa | Thimphu | Government hosting | Operational | A |
| DCS Internet Data Centre | Thimphu | Commercial colo | Operational | A |
| btIX | Thimphu | Internet exchange | Operational | A |
| Bitdeer Gedu | Chhukha | Crypto-mining DC | 100 MW online crypto | A |
| Bitdeer Jigmeling | Sarpang | Crypto-mining DC | 500 MW online crypto | A |
| SATO-GMCA AI campus | Sarpang | Planned AI DC | LOI/planned | A for LOI, B for scale |
| National 40-50 MW DC | TBD | Planned national/AI-ready DC | Roadmap/feasibility | B until official site/permit |
| DHI AI datacenter proposal | TBD | Planned AI/GPU DC | Proposal | A for strategy, B for facility details |
