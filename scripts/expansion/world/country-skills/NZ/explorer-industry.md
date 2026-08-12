# NZ Explorer Industry - trade press, vendors, and regional query patterns

Date: 2026-08-12. Scope: New Zealand datacentre enumeration methodology focused on industry/trade press, operator/vendor pages, cloud-region pages, and repeatable region-level search patterns. Country code: **NZ**. Reliability grades: **A** = official/primary source (operator-owned facility page, cloud provider official region page, council consent record/public notice, NZX/company announcement), **B** = strong secondary/trade press/local press with named project details, **C** = directory, event page, market report snippet, social post, or weak/aggregate lead.

---

## 0. New Zealand-specific frame

- New Zealand has no single public national datacentre registry. Enumerate by combining **operator facility pages**, **cloud region official pages**, **trade press**, **council resource consent files**, and **data-centre directories** for older telecom/edge sites.
- Planning evidence is usually under the Resource Management Act as **resource consent**, **land use consent**, **building consent**, **discharge permit**, **water take**, **stormwater**, **earthworks**, **substation/Grid Exit Point**, **designation**, or **fast-track consenting** material. Large projects can require both a territorial authority and a regional council.
- The market is concentrated in **Auckland** for hyperscale/colo/cloud-region infrastructure. Secondary operational nodes are **Hamilton/Waikato**, **Wellington/Upper Hutt/Tawa**, **Christchurch/Canterbury**, **Tauranga/Bay of Plenty**, and **Dunedin/Otago**. New large-load project discovery is currently strongest in **Southland**, **Taranaki**, and **Canterbury** because renewable power, cool climate, land, and fibre/subsea routes matter.
- English is sufficient for most searches. Add te reo Maori/Aotearoa variants only for broad web search and stakeholder/public-material discovery: `Aotearoa`, `Te Waipounamu`, `whare raraunga`, `pokapu raraunga`, `raraunga`, `wai`, `mana whenua`, `iwi`, `mahi tahi`.
- Use both spellings: New Zealand sources often use **data centre**, while global press and US hyperscalers use **data center**. Also search `datacentre`, `hyperscale`, `AI factory`, `cloud region`, `sovereign cloud`, `colocation`, `edge centre`, `EdgeCentre`, `exchange`, `carrier neutral`, `submarine cable`, and `Tasman Ring`.

---

## 1. Source map and grades

### 1.1 Industry and trade press

Use these sources to discover project names, owners, MW claims, consent references, and local-government jurisdictions. Promote a lead to Grade A only after confirming it through an operator, cloud provider, council, NZX, or other primary source.

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Dynamics - New Zealand tag/news | https://www.datacenterdynamics.com/en/news/?tag=new-zealand | Best international trade feed for AWS/Microsoft cloud regions, DCI, CDC, Datagrid, T4/TenPeaks, Google plans, and consent milestones. | B |
| Reseller News / TechPartner NZ | https://www.reseller.co.nz/ and https://www.techpartner.news/ | Strong NZ channel/IT trade coverage for CDC, NEXTDC, Datacom, Microsoft, Spark/TenPeaks, and local cloud-market shifts. | B |
| IT Brief New Zealand / TechDay | https://itbrief.co.nz/ and https://techday.co.nz/ | Useful for operator launches, DCI/NEXTDC/Spark items, and local cloud/colo announcements. | B |
| RNZ | https://www.rnz.co.nz/ | Useful for AWS/cloud-region construction context, local scrutiny, and large-project public-interest coverage. | B |
| Otago Daily Times / Southland Times / Stuff / local business press | https://www.odt.co.nz/ and https://www.stuff.co.nz/ | Important for Southland/Otago/Canterbury project approvals, local opposition, hearings, and regional economic-development details. | B/C |
| Interest.co.nz technology | https://www.interest.co.nz/technology | Good for Chorus EdgeCentre, infrastructure and telecom-market context. | B |
| Tech New Zealand / NZTech reports | https://technewzealand.org.nz/ | Industry report context for national infrastructure, power, latency, and policy framing; not a facility registry. | B/C |
| Data Centre Leaders Summit New Zealand | https://datacentreleadersnz.com/ | Speaker/sponsor list for current NZ operator/vendor universe. Use as a seed list only. | C |
| Datacenter Map / Cloudscene / Datacenters.com / Inflect / PeeringDB | https://www.datacentermap.com/new-zealand/ ; https://www.cloudscene.com/ ; https://www.datacenters.com/locations/new-zealand ; https://inflect.com/ ; https://www.peeringdb.com/ | Best discovery layer for old Spark/TenPeaks, Chorus exchange/EdgeCentre, Datacentre220, DataVault, Plan B/CCL, and regional edge facilities. Verify with operator where possible. | C, sometimes B- for address cross-checks |
| Market reports: Arizton, Mordor, BCG, JLL/CBRE/Knight Frank | example: https://www.arizton.com/market-reports/new-zealand-data-center-portfolio and https://www.bcg.com/publications/2026/data-centres-as-strategic-infrastructure | Use for market-sizing, city coverage, pipeline direction, and operator lists. Do not use as sole evidence for a project. | C for project facts; B for market context |

High-value trade queries:

```text
site:datacenterdynamics.com/en/news/ "New Zealand" "data center"
site:datacenterdynamics.com/en/news/ "New Zealand" "data centre" "resource consent"
site:reseller.co.nz "data centre" "New Zealand" "Auckland"
site:itbrief.co.nz "data centre" "New Zealand" DCI OR CDC OR Datagrid OR NEXTDC
site:rnz.co.nz "data centre" "New Zealand" AWS OR Datagrid OR Microsoft
site:interest.co.nz/technology Chorus EdgeCentre data centre
"New Zealand" "data centre" "MW" "resource consent"
"Aotearoa" "data centre" "AI factory"
```

### 1.2 Primary official sources

| Source | URL | Use | Grade |
|---|---|---|---|
| Operator facility pages | DCI https://dcidatacenters.com/auckland/ ; CDC Auckland https://www.cdc.com.au/locations/auckland/ ; NEXTDC AK1 https://www.nextdc.com/data-centres/new-zealand-data-centres/ak1-auckland ; Datacom https://datacom.com/nz/en/products/data-centres/locations ; TenPeaks https://tenpeaks.co.nz/ ; Chorus EdgeCentre https://www.chorus.co.nz/enterprise/data-centre-connectivity/edgecentre ; Datacentre220 https://www.datacentre.co.nz/ | Confirms owned/operated facilities, sometimes capacity and status. | A for existence/status when operator-owned; B for marketing capacity if not auditable |
| Cloud provider region pages | AWS NZ region https://aws.amazon.com/local/new-zealand/ and launch blog https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-new-zealand-region/ ; Microsoft NZ region https://news.microsoft.com/en-nz/2024/12/12/new-zealands-first-hyperscale-cloud-is-open-for-business/ ; Google Cloud NZ announcement https://www.googlecloudpresscorner.com/2022-08-09-Google-Cloud-Announces-First-Cloud-Region-in-New-Zealand ; Google locations https://cloud.google.com/about/locations ; Oracle/TEAM Cloud https://teamcloud.nz/sovereign-regions and https://www.oracle.com/customers/team-im-oracle-alloy/ | Proves cloud-region or sovereign-cloud presence/plans, not exact physical addresses. | A for cloud region; B/C for facility inference |
| Council resource consent pages | Auckland Council, Environment Southland, Southland District Council, Invercargill City Council, Selwyn District Council, Central Otago District Council, Stratford District Council, regional councils | Primary path for planned/approved large physical projects. Many records are not full-text-indexed by Google; search council pages and project names. | A |
| Environment Southland Datagrid file | https://www.es.govt.nz/datagrid | Public resource-consent page for Datagrid near Makarewa; includes consent documents/technical material. | A |
| Southland District Council proposals of public interest | https://www.southlanddc.govt.nz/home-and-property/resource-consents/proposals-of-public-interest/ | Tracks Datagrid consent conditions/reviews, including RMA 2025 5312 material. | A |
| Ministry for the Environment / Fast-track | https://environment.govt.nz/ and https://www.fasttrack.govt.nz/ | Search for large unlisted/fast-track proposals, referral applications, and comments. Some data-centre components appear inside mixed-use proposals. | A |
| NZX announcements | https://www.nzx.com/announcements/ | Primary source for Spark/TenPeaks transaction and listed-company disclosures by Spark, Infratil, Contact Energy, Mercury, etc. | A |
| Electricity/generation/transmission sources | Contact Energy https://contact.co.nz/ ; Mercury https://www.mercury.co.nz/ ; Transpower https://www.transpower.co.nz/ ; Electricity Authority EMI https://www.emi.ea.govt.nz/ | Large-load clues: PPAs, grid connection, GXP, substation, load applications, renewable-power tie-ins. | A/B depending on document |

---

## 2. Core NZ search templates

### 2.1 National discovery

```text
"New Zealand" ("data centre" OR "data center" OR datacentre) ("MW" OR "MVA" OR "racks" OR "hyperscale")
"New Zealand" ("AI factory" OR "AI data centre" OR "hyperscale data centre")
"Aotearoa" ("data centre" OR "data center" OR "AI factory")
"data centre" "resource consent" "New Zealand"
"data centre" "land use consent" "New Zealand"
"data centre" "building consent" "New Zealand"
"data centre" "substation" "New Zealand"
"data centre" "Grid Exit Point" OR GXP "New Zealand"
"data centre" "water take" "New Zealand"
"data centre" "discharge permit" "New Zealand"
"data centre" "submarine cable" "New Zealand"
```

### 2.2 Operator/vendor triangulation

```text
"{operator}" "{region}" "data centre"
"{operator}" "{city}" "data center" OR "data centre"
site:{operator-domain} "New Zealand" "data centre"
site:{operator-domain} Auckland OR Hamilton OR Wellington OR Christchurch OR Tauranga OR Dunedin
"{operator}" "resource consent" "data centre"
"{operator}" "MW" "New Zealand"
"{operator}" "NZX" "data centre"
```

### 2.3 Council/consent verification

```text
site:{council-domain} "data centre" "resource consent"
site:{council-domain} "data center" "resource consent"
site:{council-domain} datacentre
site:{council-domain} "hyperscale" "data centre"
site:{council-domain} "AI factory"
site:{council-domain} "substation" "data centre"
site:{council-domain} "water take" "data centre"
site:{council-domain} "earthworks" "data centre"
site:{council-domain} "notified consent" "data centre"
site:{regional-council-domain} "{operator}" "data centre"
```

Inside council portals/document stores, search:

```text
data centre
data center
datacentre
hyperscale
AI factory
server hall
diesel generator
backup generator
substation
Grid Exit Point
GXP
cooling
water take
stormwater
discharge
earthworks
land use consent
building consent
```

Record these fields from the primary file: consent/application reference, applicant/legal entity, site address or land parcel, activity description, consent authority, notification status, decision date, lapse/expiry date, conditions, construction staging, power capacity/MW/MVA, backup generator count/fuel storage, water use/cooling method, stormwater/discharge permits, earthworks area, substation/GXP evidence, iwi/hapu consultation, and appeal/review status.

---

## 3. Operator and developer seed list

Operator pages are the fastest way to identify live facilities. Consent files are still required for planned facilities and capacity/status claims when a public project has not opened.

| Operator/developer | NZ geographies to check first | Official / useful page | Notes |
|---|---|---|---|
| CDC Data Centres | Auckland: Silverdale, Hobsonville; possible future NZ expansion | https://www.cdc.com.au/locations/auckland/ | Official page lists Auckland campuses and capacity. Also search Infratil/Future Fund disclosures and DCD. |
| DCI Data Centers | Auckland: Westgate AKL01, Albany/North Shore AKL02 | https://dcidatacenters.com/auckland/ | Official page confirms AKL01/AKL02; DCI news says AKL01 complete and AKL02 planned/constructed with 50MW+ combined strategy. |
| Datacom | Auckland North Orbit, Auckland South Highbrook, Hamilton Kapua, Wellington Abel, Christchurch Gloucester | https://datacom.com/nz/en/products/data-centres/locations | Strong primary facility/capacity source for Datacom-owned NZ sites. |
| NEXTDC | Auckland AK1 | https://www.nextdc.com/data-centres/new-zealand-data-centres/ak1-auckland | AK1 is in development. Search Auckland Council/NEXTDC annual reports for consent/build details. |
| TenPeaks Data Centres / Spark data-centre portfolio | Auckland/Takanini/North Shore plus metro/edge sites across NZ | https://tenpeaks.co.nz/ and NZX Spark announcements https://www.nzx.com/announcements/ | Spark sold 75% of its data-centre business to Pacific Equity Partners and the unit launched as TenPeaks. DCD reported 23MW live capacity and a pipeline toward 130MW. |
| Datagrid | Southland Makarewa; Canterbury/North Rakaia; subsea cable landing | https://www.datagrid.nz/ and https://www.es.govt.nz/datagrid | Large consent-led AI/hyperscale developer. Southland primary sources are Environment Southland/Southland DC/Invercargill; Canterbury needs Selwyn/ECan search. |
| Chorus EdgeCentre | Auckland/Mt Eden, Tauranga, Christchurch, regional exchange sites | https://www.chorus.co.nz/enterprise/data-centre-connectivity/edgecentre | Official page confirms EdgeCentre service; directories/local press help locate individual exchange sites. Treat tiny exchange sites separately from hyperscale DCs. |
| Datacentre220 | Auckland CBD | https://www.datacentre.co.nz/ | Primary for Auckland carrier-neutral/interconnection facility; cross-check PeeringDB and Datacenter Map. |
| Vocus / 2degrees / One NZ / telco colocation | Auckland/Albany and network exchange estate | https://www.vocus.com.au/enterprise/colocation-hybrid-cloud | Operator pages often describe services but not all facility addresses; directories and PeeringDB fill gaps. |
| CCL / Plan B | Wellington/Tawa and managed-services DCs | https://www.planb.co.nz/data-centre/ | Good regional colo/DR lead; verify with company page plus directories. |
| DataVault / DTS / Advantage / Earthlight / ECO Data Centre | Hamilton, Palmerston North, Dunedin/Invermay, Tauranga | operator sites and directories | Smaller regional facilities often require directory discovery plus local business/company confirmation. |
| Contact Energy / Mercury / Transpower-linked projects | Clyde/Otago, Stratford/Taranaki, Southland/Manapouri grid | Contact https://contact.co.nz/ ; Mercury https://www.mercury.co.nz/ ; Transpower https://www.transpower.co.nz/ | Energy-company announcements are high-value for new large-load datacentre projects and PPAs. |

Operator sweep templates:

```text
site:dcidatacenters.com "Auckland" "data centre"
site:cdc.com.au "Auckland" "MW" "data centres"
site:nextdc.com "AK1" "Auckland"
site:datacom.com/nz/en/products/data-centres "MW" "Hamilton" OR "Auckland" OR "Wellington" OR "Christchurch"
site:tenpeaks.co.nz "data centres" Auckland OR Waikato OR Dunedin OR "Upper Hutt"
site:chorus.co.nz EdgeCentre "data centre"
site:datacentre.co.nz "Auckland" "90 networks"
site:nzx.com/announcements Spark "data centre" TenPeaks
```

---

## 4. Hyperscaler/cloud region sweep

Cloud region pages prove cloud-service geography, not physical building locations. Treat exact addresses as unknown unless an operator/council/filing establishes them.

| Provider | Official page | NZ signal | Grade |
|---|---|---|---|
| AWS | https://aws.amazon.com/local/new-zealand/ and https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-new-zealand-region/ | AWS Asia Pacific (New Zealand), API name `ap-southeast-6`, opened 2025-09-01 with three Availability Zones. Search DCD/RNZ for leased-space/construction context; do not infer AWS-owned sites from region existence. | A |
| Microsoft Azure | https://news.microsoft.com/en-nz/2024/12/12/new-zealands-first-hyperscale-cloud-is-open-for-business/ and Azure regions list https://learn.microsoft.com/en-us/azure/reliability/regions-list | Microsoft opened its first NZ hyperscale cloud region in December 2024. Search `New Zealand North`, `Hobsonville`, `Silverdale`, and Auckland Council terms for facility clues. | A |
| Google Cloud | https://www.googlecloudpresscorner.com/2022-08-09-Google-Cloud-Announces-First-Cloud-Region-in-New-Zealand and https://cloud.google.com/about/locations | Google announced a future NZ cloud region with three zones; verify current status on Google locations before recording operational status. | A for official plan/status |
| Oracle / TEAM Cloud | https://teamcloud.nz/sovereign-regions and https://www.oracle.com/customers/team-im-oracle-alloy/ | TEAM Cloud uses Oracle Alloy and states two independent North Island sovereign regions within NZ. Map to TEAM IM-owned/leased data centres only with primary or strong secondary evidence. | A for service geography; B for facility inference |

Hyperscaler queries:

```text
"AWS" "ap-southeast-6" "New Zealand" "data centre"
"AWS" "Auckland" "data center" "resource consent"
"Microsoft" "New Zealand North" "data centre"
"Microsoft" Hobsonville Silverdale "data centre"
"Google Cloud" "New Zealand cloud region" "Auckland" "data centre"
"TEAM Cloud" "Oracle Alloy" "data centre" "New Zealand"
"Oracle Alloy" "New Zealand" "sovereign regions"
```

---

## 5. Region-by-region enumeration recipes

For every region, run four passes:

1. **Operator pass (A/B)**: query major operators plus directories for city names and facility names.
2. **Trade/local press pass (B/C)**: DCD, Reseller, IT Brief, RNZ, ODT/Stuff/local press for project announcements, approvals, and MW claims.
3. **Consent pass (A)**: territorial authority resource-consent/building-consent pages plus regional council pages for water, discharge, earthworks, coastal, or air-discharge consents.
4. **Infrastructure pass (A/B)**: Transpower/GXP, electricity generator PPA, fibre/subsea cable, exchange/IX/PeeringDB clues.

### Auckland

Highest-priority region. Known pivots: AWS region, Microsoft NZ region, CDC Silverdale/Hobsonville, DCI AKL01/AKL02, NEXTDC AK1, Datacom Orbit/Highbrook, Datacentre220, TenPeaks/Spark, Vocus Albany, Chorus Mt Eden/EdgeCentre.

```text
"Auckland" "data centre" OR "data center" OR datacentre
"Westgate" "data centre" DCI
"Albany" "data centre" DCI OR Vocus
"Silverdale" "data centre" CDC OR Microsoft
"Hobsonville" "data centre" CDC OR Microsoft
"Takanini" "data centre" Spark OR TenPeaks
"Highbrook" "data centre" Datacom
"Mayoral Drive" OR "Queen Street" "data centre"
site:aucklandcouncil.govt.nz "data centre" "resource consent"
site:aucklandcouncil.govt.nz "datacentre" OR "data center"
site:aucklandcouncil.govt.nz "hyperscale" "data centre"
site:epa.govt.nz "data centre" "Auckland"
site:fasttrack.govt.nz "data centre" "Auckland"
```

### Waikato

Known pivots: Datacom Kapua Hamilton, DataVault Hamilton, TenPeaks/Spark Waikato, University of Waikato/innovation park, hydro/geothermal power proximity.

```text
"Waikato" "data centre" OR "data center"
"Hamilton" "data centre" Datacom OR Kapua OR DataVault OR TenPeaks
"Waikato Innovation Park" "data centre"
site:waikatoregion.govt.nz "data centre" "resource consent"
site:hcc.govt.nz "data centre" "resource consent"
site:waipadc.govt.nz "data centre"
site:waikatodistrict.govt.nz "data centre"
```

### Bay of Plenty

Known pivots: Tauranga TenPeaks/Spark, Chorus Tauranga EdgeCentre/Otumoetai, ECO Data Centre, StrataGate, port/fibre and geothermal/industrial load.

```text
"Bay of Plenty" "data centre"
"Tauranga" "data centre" OR "EdgeCentre" OR "Otumoetai"
"Tauranga" "Spark" OR TenPeaks OR Chorus "data centre"
site:tauranga.govt.nz "data centre" "resource consent"
site:boprc.govt.nz "data centre" "resource consent"
site:westernbay.govt.nz "data centre"
site:rotorualakescouncil.nz "data centre"
```

### Canterbury

Known pivots: Datacom Gloucester Christchurch, Chorus Christchurch EdgeCentre, TenPeaks/Spark Christchurch, Datagrid/T4 North Rakaia/Selwyn, power and fibre routes.

```text
"Canterbury" "data centre" OR "data center"
"Christchurch" "data centre" Datacom OR Gloucester OR Chorus OR TenPeaks
"North Rakaia" Datagrid "data centre"
"Rakaia" "hyperscale" "data centre"
"Selwyn" "data centre" "resource consent"
site:ecan.govt.nz "data centre" "resource consent"
site:selwyn.govt.nz "data centre" "resource consent"
site:ccc.govt.nz "data centre" "resource consent"
site:ashburtondc.govt.nz "data centre"
```

### Southland

Highest-priority large-load region outside Auckland. Known pivots: Datagrid Makarewa/Invercargill AI factory and Tasman Ring Network; T4/TenPeaks Invercargill/Southland; Manapouri/Tiwai/Transpower power context.

```text
"Southland" "data centre" OR "AI factory" OR Datagrid
"Makarewa" "data centre" OR "AI factory"
"Invercargill" "data centre" Datagrid OR T4 OR TenPeaks
"Tasman Ring Network" "data centre" OR "Oreti Beach"
"Datagrid" "RMA 2025 5312"
site:es.govt.nz Datagrid "datacentre"
site:southlanddc.govt.nz Datagrid "Hyperscale Data Centre"
site:icc.govt.nz Datagrid "data centre"
site:environment.govt.nz Datagrid "Sustainable Data Centre Park"
site:fasttrack.govt.nz Datagrid "data centre"
site:transpower.co.nz Makarewa Datagrid GXP
```

Primary anchors: Environment Southland Datagrid resource-consents page (`https://www.es.govt.nz/datagrid`) and Southland District Council proposals of public interest (`https://www.southlanddc.govt.nz/home-and-property/resource-consents/proposals-of-public-interest/`).

### Taranaki

Known pivots: Contact Energy/CDC proposed Stratford hyperscale project, power-generation/industrial land, substations.

```text
"Taranaki" "data centre" OR "data center"
"Stratford" "data centre" CDC OR "Contact Energy"
"Contact Energy" "CDC Data Centres" "Stratford"
"Taranaki" "hyperscale" "data centre" "250MW"
site:trc.govt.nz "data centre" "resource consent"
site:stratford.govt.nz "data centre" "resource consent"
site:contact.co.nz "data centre" "Taranaki"
site:transpower.co.nz Stratford "data centre" OR GXP
```

### Greater Wellington

Known pivots: Datacom Abel Wellington, Datacentre220-related interconnection context, Plan B/CCL Tawa, TenPeaks Upper Hutt/Spark, Chorus exchange sites, government/sovereign hosting.

```text
"Wellington" "data centre" Datacom OR Abel OR "Plan B" OR CCL OR Tawa
"Upper Hutt" "data centre" Spark OR TenPeaks
"Greater Wellington" "data centre"
site:wellington.govt.nz "data centre" "resource consent"
site:gw.govt.nz "data centre" "resource consent"
site:poriruacity.govt.nz "data centre"
site:upperhuttcity.com "data centre"
site:huttcity.govt.nz "data centre"
```

### Otago

Known pivots: Contact Energy/Lake Parime Clyde, TenPeaks Dunedin, Earthlight Invermay, University/HPC and hydro-load context.

```text
"Otago" "data centre" OR "data center"
"Clyde" "data centre" "Lake Parime" OR "Contact Energy"
"Dunedin" "data centre" TenPeaks OR Spark OR Earthlight OR Invermay
"Central Otago" "data centre" "resource consent"
site:orc.govt.nz "data centre" "resource consent"
site:codc.govt.nz "data centre" "resource consent"
site:dunedin.govt.nz "data centre" "resource consent"
site:contact.co.nz "Lake Parime" "data centre"
```

### Manawatu-Whanganui

Known pivots: Advantage Palmerston North, regional fibre/edge and disaster-recovery sites.

```text
"Manawatu" "data centre" OR "data center"
"Palmerston North" "data centre" Advantage OR colocation
"Whanganui" "data centre"
site:horizons.govt.nz "data centre" "resource consent"
site:pncc.govt.nz "data centre"
site:whanganui.govt.nz "data centre"
site:peeringdb.com "Palmerston North" "data centre"
```

### Northland

Known pivots: Chorus Whangarei/Kensington exchange facilities, potential subsea/space-ground-station and renewable-fibre leads. Expect mostly small edge sites unless a new power/fibre project appears.

```text
"Northland" "data centre" OR "data center"
"Whangarei" "data centre" Chorus OR exchange
"Kensington" "data centre" Chorus
"Northland" "submarine cable" "data centre"
site:nrc.govt.nz "data centre" "resource consent"
site:wdc.govt.nz "data centre"
site:kaipara.govt.nz "data centre"
site:fndc.govt.nz "data centre"
```

### Hawke's Bay

Known pivots: Chorus Hastings exchange, Napier/Hastings edge/DR, regional fibre resilience.

```text
"Hawke's Bay" "data centre"
"Hastings" "data centre" Chorus OR exchange
"Napier" "data centre" colocation
site:hbrc.govt.nz "data centre" "resource consent"
site:hastingsdc.govt.nz "data centre"
site:napier.govt.nz "data centre"
```

### Gisborne

Known pivots: Spark/TenPeaks or directory-listed Gisborne facility; expect edge/telecom records rather than hyperscale.

```text
"Gisborne" "data centre" OR "data center"
"Gisborne" Spark OR TenPeaks OR Chorus "data centre"
"Customhouse Street" Gisborne "data centre"
site:gdc.govt.nz "data centre" "resource consent"
site:inflect.com Gisborne "Spark NZ"
```

### Marlborough

Known pivots: Chorus Blenheim exchange, fibre/subsea and regional exchange infrastructure.

```text
"Marlborough" "data centre"
"Blenheim" "data centre" Chorus OR exchange
site:marlborough.govt.nz "data centre" "resource consent"
"Marlborough" "submarine cable" "data centre"
```

### Nelson

Known pivots: Chorus Nelson/Stoke exchange facilities, regional edge/colo.

```text
"Nelson" "data centre" OR "data center"
"Stoke" "data centre" Chorus OR exchange
site:nelson.govt.nz "data centre" "resource consent"
site:datacentermap.com "Nelson" "New Zealand" "data centre"
```

### Tasman

No strong public hyperscale/colo lead found in initial sweep. Search for Nelson-adjacent facilities, fibre, substations, and council consent records.

```text
"Tasman" "data centre" "New Zealand"
"Richmond" "data centre" "New Zealand"
"Motueka" "data centre"
site:tasman.govt.nz "data centre" "resource consent"
```

### West Coast

No strong public lead found in initial sweep. Focus on regional council/territorial authority consent searches and power/fibre industrial-site leads.

```text
"West Coast" "data centre" "New Zealand"
"Greymouth" "data centre"
"Westport" "data centre"
site:wcrc.govt.nz "data centre" "resource consent"
site:greydc.govt.nz "data centre"
site:bdc.govt.nz "data centre"
site:westlanddc.govt.nz "data centre"
```

### Chatham Islands Territory

No datacentre lead expected beyond telecom exchanges/satellite connectivity. Use as a negative-control region; record `no_projects` unless primary evidence appears.

```text
"Chatham Islands" "data centre"
"Chatham Islands" "telecommunications" "exchange"
site:cidc.govt.nz "data centre"
```

---

## 6. Validation and status rules

- **Operational**: operator facility page lists the site as live; cloud region official page says generally available/open; directory evidence is supported by operator, PeeringDB, or current connectivity listing.
- **Construction**: operator or council document says construction/earthworks/building works commenced; do not infer construction from "in development" alone.
- **Approved**: council/resource-consent decision granted or official company announcement says full resource consent/approval granted. Capture consent authorities and references.
- **Planned/announced**: operator/company/trade press announces site, land purchase, feasibility, PPA, or future region, but no consent/construction/opening evidence.
- **Dormant/uncertain**: older project with no recent operator/council confirmation, especially crypto/HPC proposals and delayed hyperscale builds.

Reliability upgrade rules:

- Trade article with MW plus named consent authority = **B**, upgraded to **A** only after consent or operator page is inspected.
- Operator page with facility name/location = **A** for existence; MW remains **B** if it is marketing text without technical backup.
- Cloud region = **A** for service region; physical facilities remain **unknown** unless separately verified.
- Directories = **C** unless corroborated by operator page, PeeringDB active facility, NZX disclosure, or local public record.
- For regional Chorus/Spark/TenPeaks exchange facilities, separate **edge/telecom exchange datacentre** from hyperscale/wholesale datacentre in notes; do not aggregate MW unless site-specific primary capacity is public.
