# AL Explorer Industry - Albania Datacenter Discovery

Date: 2026-08-12. Scope: Albania datacenter enumeration from operators, industry media, aggregators, IXP/connectivity records, investment-promotion channels, public cloud checks, and Albanian-language searches.

Reliability grades:

- **A** = operator-owned facility page, official public-sector source, official cloud-provider region page, official IXP/operator page, or source-of-record registry/procurement/permit.
- **B** = strong trade press, EU/IFI/ITU/Energy Community source, PeeringDB, Submarine Networks, vendor case study, or detailed local press that can be followed to a primary record.
- **C** = aggregator, marketplace, directory, reseller location page, LinkedIn/social page, job ad, investment-promotion language, or unverified address/municipality inference.

Use industry sources for discovery. Promote a facility only after official/operator/registry/procurement/permit/power evidence supports the specific claim.

---

## 0. Industry discovery frame

- Albania is a small, **Tirana-centric** colocation and telecom infrastructure market. Data Center Map lists 5 facilities in Albania, all in Tirana, but that is a **C-grade lead set**: https://www.datacentermap.com/albania/ and https://www.datacentermap.com/albania/tirana/.
- The largest pipeline lead is **Albania Data Center (ADC)** in the TEDA free economic zone at Kashar/Tirane: 32 MW first phase, potential 100 MW expansion, about EUR 100 million / USD 118 million, reported by Globes, DCD, SeeNews, and Albania Economia in 2026. Keep it **B** until Albanian QKB, permit/KKTU, OST/OSHEE/ERE, EBRD, or operator documentation is found.
- Strongest currently verified operator/interconnection evidence: **Host.al Datacenter Albania HS1** and **RASH/ANIX** in Tirana. Host.al has an operator-owned colocation page; ANIX states that it is hosted at RASH's carrier-grade data center in central Tirana.
- Secondary potential geographies: **Durres** for cable/port landing context and **Vlore** for port/coastal context plus Nisatel's registered-seat/operator lead. Treat both as lead geographies until facility evidence appears.
- No official AWS/Azure/GCP/OCI public cloud region is listed for Albania in checked official region/location pages. Local `cloud` usually means AKSHI/government cloud, telecom/operator cloud, hosting, or foreign-region resale.

---

## 1. Trade press and market sources

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Globes | https://en.globes.co.il/en/article-israels-adc-to-build-albanias-first-data-center-1001533793 | ADC/TEDA project lead: 32 MW, possible 100 MW, EUR 100m, Nvidia/HPC, hydro/dedicated substation claims. | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/32mw-israeli-backed-data-center-coming-to-albania/ | ADC summary, cost/site/capacity, notes existing Albania directory landscape. | B |
| SeeNews | https://seenews.com/news/israels-h-a-p-i-preparing-to-build-data-centre-in-tirana-1289874 | H.A.P.I./Alis Initiatives/TEDA land-lease lead; useful names for QKB follow-up. | B |
| Albania Economia | https://www.albaniaeconomia.com/adc-to-build-albanias-first-data-center-e100-million-investment-to-create-a-balkan-digital-hub/ | ADC and Albania digital-hub investment context. | B |
| Albanian Daily News | https://albaniandailynews.com/news/govt-plans-eur-7m-for-cloud-infrastructure | AKSHI centralized government cloud-hardware tender lead. | B |
| SeeNews cloud tender | https://seenews.com/news/albania-opens-7-mln-euro-tender-for-govt-cloud-infrastructure-1246014 | Same AKSHI tender lead; follow to APP. | B |
| DCD One Albania merger | https://www.datacenterdynamics.com/en/news/4ig-finalizes-merger-of-two-albanian-operators-to-form-one-albania/ | ALBtelecom/ONE merger context for stale operator names. | B |
| ATA | https://ata.gov.al/ | Official news agency for government digital/energy statements. | A/B |
| Monitor.al, CNA, Tirana Times, Albanian Daily News, Durres Lajm | site-specific search | Local telecom, energy, permits, tenders, and construction news. | B/C |
| ITU / EBRD / WBIF / EU / Energy Community | itu.int, ebrd.com, wbif.eu, enlargement.ec.europa.eu, energy-community.org | Broadband, energy, digital-government, and financing context. | A/B |

Trade queries:

```text
site:seenews.com Albania "data centre" OR "data center"
site:datacenterdynamics.com Albania "data center"
site:en.globes.co.il Albania "data center"
site:albaniaeconomia.com Albania "data center"
site:albaniandailynews.com Albania "cloud" "AKSHI"
site:tiranatimes.com "data center" Albania
site:monitor.al "qendra e te dhenave" OR "data center"
site:cna.al "qendra e te dhenave" OR "data center"
"Albania Data Center" "TEDA" "Kashar"
"H.A.P.I" "Alis Initiatives" "TEDA"
"Albania" "32MW" "data center"
"Shqiperi" "qendra e te dhenave" "investim"
```

Lifecycle verbs matter:

- `plans`, `selected`, `preparing`, `signed land lease`, `suitable`, `promoted` = lead/pipeline.
- `tender`, `design`, `permit`, `grid connection`, `construction started` = pipeline with official follow-up required.
- `opened`, `operates`, `hosts`, `colocation`, `dedicated servers`, `IXP hosted at` = stronger facility signal.

---

## 2. Operator and facility seed sweep

| Operator / project | Official or lead URL | Facility/locality signal | Grade | Handling |
|---|---|---|---|---|
| Host.al / Datacenter Albania HS1 | https://host.al/colocation-datacenter-in-albania/?lang=en ; https://host.al/support/?lang=en | Operator markets a Tirana datacenter with colocation, redundant power/cooling/security, connectivity via local IXP, Cogent and Hurricane Electric. PeeringDB gives Host.al org address at Tefta Tashko Koco 23, Tirana. | A for service; B/C for address | Count as Tirana operator facility; verify QKB/permit/power for address/capacity. |
| RASH / ANIX | https://www.anix.al/ ; https://anix.rash.al/ ; https://www.peeringdb.com/fac/4508 ; https://www.peeringdb.com/ix/2004 | ANIX says it is hosted at RASH's carrier-grade data center in central Tirana. PeeringDB facility address: Rruga e Durresit 219, Tirana 1001; ANIX has 23 peers in PeeringDB checked snippet. | A for official ANIX statement; B for PeeringDB | Count as interconnection/data-center facility with scope caveat. |
| Albania Data Center / ADC / TEDA | Press: Globes, DCD, SeeNews, Albania Economia URLs above; LinkedIn: https://al.linkedin.com/company/albania-data-center | TEDA free economic zone, Kashar, Tirane municipality; 32 MW to possible 100 MW; reported owners/entities include H.A.P.I./Happy Technologies, DIT, Alis Initiatives. | B/C | Do not count as operational; verify QKB entity, TEDA lease, permit/KKTU, OST/OSHEE, EBRD. |
| One Albania / ALBtelecom | https://www.one.al/ ; DCD merger URL above | Aggregators place ALBtelecom DC at Autostrada Tirane-Durres Km 7, Kashar; company renamed/merged into One Albania context. | C until operator/official facility proof | Check One enterprise/cloud pages, AKEP, QKB, permits, energy. |
| Abissnet | https://www.abissnet.al/ ; PeeringDB/RIPE/AKEP searches | ISP and ANIX peer; Tirana office/hosting/network lead. | B/C | Count only if operator page or official record identifies DC/colo/server-room facility. |
| Nisatel | https://nisatel.al/ | ISP/hosting lead; registered-seat clues point to Vlore in secondary/RIPE references. | C | Verify physical facility vs hosting resale through QKB, AKEP, permits, OSHEE. |
| Vodafone Albania | https://www.vodafone.al/ | Mobile/network operator; likely core sites in Tirana. | C for DC enumeration | Telecom operator status is not facility proof. |
| AKSHI government data center/cloud | https://akshi.gov.al/ ; APP/OpenProcurement; press tender URLs above | Government data-center/cloud/server-room infrastructure in Tirana; exact facility and tender scope must be verified. | A when official procurement/AKSHI page found; B for press | Separate government IT/server rooms from commercial colo. |
| iregisterdata.center | https://iregisterdata.center/ | Markets `Albanian Data Center, Tirana` style services. | C | Verify company identity, physical address, underlying facility. |
| Albanian Telecommunications Union / Tirana DataCom | Example aggregator: https://inflect.com/building/rruga-industriale-kashar/albanian-telecommunications-union-sh-p-k/datacenter/tirana-datacom | Rruga Industriale/Kashar colocation lead from aggregator. | C | Verify via operator/QKB/AKEP/permit before counting. |
| Pronet / older Tirana directory leads | DataCenterJournal/Data Center Map routes | Stale directory records possible. | C | Resolve current operator and physical site before counting. |

Operator queries:

```text
site:host.al "datacenter" OR "colocation" OR "HS1"
site:host.al "Tirana" "Datacenter Albania"
site:anix.al "carrier-grade data center"
site:anix.rash.al "data center"
site:one.al "data center" OR "cloud" OR "hosting"
site:abissnet.al "server" OR "hosting" OR "qender"
site:nisatel.al "data center" OR "hosting" OR "server"
site:vodafone.al "data center" OR "cloud" "Albania"
site:iregisterdata.center "Tirana" "data center"
"Autostrada Tirane-Durres Km 7" "ALBtelecom" "data center"
"Rruga Industriale" "Kashar" "Tirana DataCom"
"Tefta Tashko Koco" "Host.al"
```

---

## 3. Aggregators, interconnection directories, and marketplaces

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Map Albania | https://www.datacentermap.com/albania/ | Says 5 data centers, 1 market, Tirana. | C |
| Data Center Map Tirana | https://www.datacentermap.com/albania/tirana/ | Facility/provider lead list for Tirana. | C |
| Data Center Map Host.al | https://www.datacentermap.com/albania/tirana/hostal-shpk/ | Host.al lead/details. | C, corroborated by Host.al A page |
| Data Center Map ANIX | https://www.datacentermap.com/ixp/anix/ | ANIX lead; page says exact DC locations unknown. | C |
| datacenters.com Albania | https://www.datacenters.com/locations/albania | Provider/facility marketplace. | C |
| datacenters.com Host.al HS1 | https://www.datacenters.com/host-al-shpk-albania-hs1 | Host.al marketplace listing. | C |
| DataCenterJournal Tirana | https://www.datacenterjournal.com/data-centers/albania/tirana/ | Older Tirana providers/facilities; useful for stale ALBtelecom/RASH/Tirana DataCom/Pronet leads. | C |
| Data Center Platform Albania | https://datacenterplatform.com/countries/albania/ | Albania country/facility lead count. | C |
| Baxtel Albania | https://baxtel.com/data-center/albania | RASH/ADC lead aggregation. | C |
| PeeringDB RASH-ANIX facility | https://www.peeringdb.com/fac/4508 | Facility/interconnection record with address and exchange. | B |
| PeeringDB ANIX IX | https://www.peeringdb.com/ix/2004 | Exchange members/capacity. | B |
| Inflect | https://inflect.com/ search Albania/Kashar/ALBtelecom/Tirana DataCom | Marketplace address/service leads. | C |
| Cloudscene, ColoMap, LinkedIn/jobs | site search | Lead discovery only. | C |

Aggregator queries:

```text
site:datacentermap.com/albania Tirana
site:datacenters.com Albania "data center"
site:datacenterjournal.com Albania Tirana "data center"
site:datacenterplatform.com Albania "data centers"
site:baxtel.com "Albania" "data center"
site:inflect.com Albania "data center"
site:peeringdb.com "Tirana" "ANIX"
site:colomap.com "ANIX" Albania
"Albania" "data center" "Kashar" "aggregator"
```

Aggregator rules:

- Treat counts, addresses, capacities, and status as provisional.
- Reconcile old names: ALBtelecom may now be One Albania; records may lag mergers.
- Do not assign facility capacity from a directory unless an operator, permit, power record, or strong technical source confirms it.
- Do not count a reseller VPS page as a data center unless the underlying facility is identified.

---

## 4. Connectivity, cable, and edge signals

Strong sources and routes:

| Signal | Sources | Use | Grade |
|---|---|---|---|
| ANIX / RASH | https://www.anix.al/ ; https://anix.rash.al/ ; PeeringDB links above | Confirms an interconnection-active RASH data center in Tirana. | A/B |
| Italy-Albania cable | https://www.submarinenetworks.com/en/systems/intra-europe/italy-albania ; https://www.submarinecablemap.com/ | Bari-Durres cable/landing context. | B/A- |
| Albania Crossing / Adria 1 | Submarine Networks, Submarine Cable Map, operator/news searches | International connectivity context. | B/C until source-specific |
| CDN/cache peers | PeeringDB ANIX peer list and ISP pages | Edge/cache hints; not independent DC proof. | B/C |
| Planned energy/subsea corridors | ICIS/Albania Economia/official energy sources | Long-term siting context, especially Durres/Vlore. | B/C |

Queries:

```text
"ANIX" "RASH" "data center" Tirana
"RASH - ANIX" "Rruga e Durresit 219"
"Albanian Neutral Internet eXchange" Cloudflare
"Italy-Albania" "Durres" "submarine cable"
"Albania Crossing" "Sparkle" "ALBtelecom"
"Adria 1" "Albania" "submarine cable"
"Durres" "cable landing station" "data center"
"Vlore" "subsea" "data center"
```

Edge/cache nodes are useful tenant/interconnection signals. They are not standalone data centers unless a facility/operator source identifies the physical site.

---

## 5. Investment-promotion and economic-zone channels

| Source | URL | Use | Grade |
|---|---|---|---|
| AIDA | https://aida.gov.al/ | Investment-promotion and TEDA/incentive context. | B for promotion; C for facility claims |
| TEDA Tirana | https://teda.al/ and https://teda.tirana.al/ | Free economic zone in Kashar/Tirana; infrastructure and investor context. | A/B for zone facts, not facility proof |
| Tirana municipality | https://tirana.al/ | TEDA/Kashar and municipal planning/procurement follow-up. | A |
| WBIF / EU / EBRD | wbif.eu, ebrd.com, enlargement.ec.europa.eu | Financing/project context for digital and energy infrastructure. | A/B |

Queries:

```text
site:aida.gov.al "TEDA" "data center"
site:teda.al "data center" OR "infrastructure" OR "Kashar"
site:teda.tirana.al "data center" OR "Kashar"
site:tirana.al "TEDA" "Kashar" "data center"
"TEDA" "Alis Initiatives" "land lease"
"TEDA" "H.A.P.I" "data center"
"WBIF" Albania "digital infrastructure" "GOVnet"
"EBRD" "Albania Data Center" OR "ADC" "Tirana"
```

Promotion pages can identify target zones and infrastructure. They are not facility evidence unless they name a project with legal/permit/contract details.

---

## 6. Cloud and local hosting checks

Official cloud checks:

| Provider | Official URL | Albania result to re-check |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Albania public Region/Local Zone in checked list. |
| Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Albania Azure public region in checked list. |
| Google Cloud | https://cloud.google.com/about/locations ; https://datacenters.google/locations | No Albania cloud region or Google-owned data-center country location in checked lists. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Albania public cloud region in checked list. |

Local cloud/hosting searches:

```text
"Albania" "sovereign cloud" "data center"
"AKSHI" "cloud" "server" "tender"
"One Albania" "cloud" "data center"
"Host.al" "cloud" "datacenter"
"Abissnet" "hosting" "server" "Tirana"
"Nisatel" "hosting" "server" "Vlore"
"Tirana" "Google Global Cache" OR "Cloudflare" "PeeringDB"
```

A local cloud product is a facility lead only. It may run in an Albanian operator facility, a government server room, or a foreign cloud/colo region.

---

## 7. Albanian-language search patterns

National sweep:

```text
"qendra e te dhenave" "Shqiperi"
"qender e te dhenave" "Shqiperi"
"qendër e të dhënave" "Tirane"
"dhoma e servereve" "Shqiperi"
"qender serveresh" "Shqiperi"
"kolokacion" "Tirane"
"cloud" "Shqiperi" "qendra e te dhenave"
"qendra e te dhenave qeveritare"
"disaster recovery" "Shqiperi"
"data center" "Shqiperi" "leje ndertimi"
"qendra e te dhenave" "fletorja zyrtare"
```

Operator/locality sweep:

```text
"Albania Data Center" Tirane
"ADC" "TEDA" Kashar
"Alis Initiatives" "TEDA"
"Host.al" "HS1"
"Abissnet" "qender" server
"Nisatel" "Vlore" hosting
"One Albania" OR "ALBtelecom" "qendra e te dhenave"
"Vodafone Albania" "qendra e te dhenave"
"AKSHI" "qendra e te dhenave"
"RASH" "ANIX" Tirane
```

Permit/procurement/power sweep:

```text
"{municipality}" "leje ndertimi" "qendra e te dhenave"
"{municipality}" "leje ndertimi" "server"
"{municipality}" "leje zhvillimi" "data"
"{municipality}" "prokurim publik" "server"
"{municipality}" "prokurim publik" "qendra e te dhenave"
"{municipality}" "nenshtacion" "MW"
"{operator}" "OSHEE" "lidhje"
"{operator}" "OST" "MVA"
"{county}" "zone ekonomike" "data"
"{county}" "zone industriale" "server"
```

---

## 8. County-level industry strategy

Run the county workflow in this priority order: **Tirane -> Durres -> Vlore -> Fier -> Elbasan -> Korce -> Shkoder -> Lezhe -> Berat -> Diber -> Kukes -> Gjirokaster**. Store negative results only after checking industry sources, official sources, operator names, Albanian terms, and municipality names.

### 8.1 Berat county

Municipalities: Berat, Kucove, Polican, Skrapar, Ura Vajgurore.

Industry view: no verified commercial or government DC lead in checked sources. Kucove/Polican industrial context may create electrical/industrial false positives; require IT facility language.

```text
"Berat" "data center" OR "qendra e te dhenave"
"Kucove" "server" OR "hosting"
"Polican" "data center" OR "server room"
"Berat" "cloud" "server"
```

### 8.2 Diber county

Municipalities: Bulqize, Diber, Klos, Mat.

Industry view: low expected yield. Search local ISP/municipal IT, mining/industrial false positives, and disaster-recovery/server-room procurement.

```text
"Diber" "data center" OR "qendra e te dhenave"
"Peshkopi" "server" "hosting"
"Bulqize" "data center" OR "server"
"Mat" "cloud" "server"
```

### 8.3 Durres county

Municipalities: Durres, Kruje, Shijak.

Industry view: high-priority lead geography because of port, Tirana-Durres corridor, and Bari-Durres cable context. No verified commercial DC outside Tirana in checked sources; look for cable landing station, port IT, logistics/industrial zones, and future cable-adjacent projects.

```text
"Durres" "data center" OR "qendra e te dhenave"
"Durrës" "cable landing" "data center"
"Durrës" "port" "data center" OR "server"
"Italy-Albania" "Durres" "data center"
"Kruje" OR "Shijak" "data center" OR "server"
site:durreslajm.al "data center" OR "server" OR "leje ndertimi"
```

### 8.4 Elbasan county

Municipalities: Belsh, Cerrik, Elbasan, Gramsh, Librazhd, Peqin, Prrenjas.

Industry view: industrial/transport corridor with no verified DC lead. Expect `industrial`, `substation`, and manufacturing noise; require hosting/colo/cloud/server-room evidence.

```text
"Elbasan" "data center" OR "qendra e te dhenave"
"Elbasan" "zone industriale" "server"
"Cerrik" OR "Librazhd" "hosting" OR "server"
"Prrenjas" "cloud" "server"
```

### 8.5 Fier county

Municipalities: Divjake, Fier, Lushnje, Mallakaster, Patos, Roskovec.

Industry view: energy/industrial county. No verified DC lead in checked sources; use power/substation searches as siting leads only.

```text
"Fier" "data center" OR "qendra e te dhenave"
"Fier" "nenshtacion" "MW" "data center"
"Patos" "server" OR "hosting"
"Lushnje" "cloud" "server"
```

### 8.6 Gjirokaster county

Municipalities: Dropull, Gjirokaster, Kelcyre, Libohove, Memaliaj, Permet, Tepelene.

Industry view: expected negative for commercial DCs. Search public-sector/server-room leads and avoid tourism/historic-building noise.

```text
"Gjirokaster" "data center" OR "qendra e te dhenave"
"Permet" OR "Tepelene" "server" OR "hosting"
"Dropull" "data center" OR "cloud"
```

### 8.7 Korce county

Municipalities: Devoll, Kolonje, Korce, Maliq, Pogradec, Pustec.

Industry view: no verified DC lead. Korce/Pogradec municipal IT and cross-border connectivity are the practical searches.

```text
"Korce" "data center" OR "qendra e te dhenave"
"Korçë" "server" "hosting"
"Pogradec" "data center" OR "server"
"Devoll" "cloud" "server"
```

### 8.8 Kukes county

Municipalities: Has, Kukes, Tropoje.

Industry view: low expected yield; check border connectivity, municipal IT, and any disaster-recovery language. Do not count fibre-route articles as facilities.

```text
"Kukes" "data center" OR "qendra e te dhenave"
"Tropoje" "server" OR "hosting"
"Has" "cloud" "server"
"Kukes" "fiber" "data center"
```

### 8.9 Lezhe county

Municipalities: Kurbin, Lezhe, Mirdite.

Industry view: north-central logistics/industrial corridor with no verified DC lead. Search Kurbin/Lezhe local portals and industrial-zone articles.

```text
"Lezhe" "data center" OR "qendra e te dhenave"
"Lezhë" "server" "hosting"
"Kurbin" "data center" OR "server"
"Mirdite" "cloud" "server"
```

### 8.10 Shkoder county

Municipalities: Fushe-Arrez, Malesi e Madhe, Puke, Shkoder, Vau i Dejes.

Industry view: northern hub/hydro corridor. No verified commercial DC lead found; RASH/ANIX remains Tirana, not Shkoder. Watch municipal/public IT and energy false positives.

```text
"Shkoder" "data center" OR "qendra e te dhenave"
"Shkodër" "server" "hosting"
"Vau i Dejes" "data center" OR "server"
"Puke" OR "Fushe-Arrez" "cloud" "server"
```

### 8.11 Tirane county

Municipalities: Kamez, Kavaje, Rrogozhine, Tirane, Vore.

Industry view: highest priority and home to all checked facility-grade signals. Confirm the exact municipality and status for each lead.

Known/seed leads:

| Municipality | Leads | Query additions |
|---|---|---|
| Tirane | Host.al HS1; RASH/ANIX; AKSHI; Abissnet; One/ALBtelecom leads; ADC/TEDA in Kashar administrative unit; older Tirana DataCom/Pronet directory leads | `Tirana data center`, `qendra e te dhenave Tirane`, `Kashar data center`, `TEDA Kashar`, `Tefta Tashko Koco Host.al`, `Rruga e Durresit 219 ANIX`, `Autostrada Tirane-Durres Km 7 ALBtelecom` |
| Kamez | Corridor/industrial spillover; no verified lead | `Kamez data center`, `Kamëz server`, `Kamez zone industriale data` |
| Vore | Logistics corridor; no verified lead | `Vore data center`, `Vorë server`, `Vore cloud` |
| Kavaje | Industrial/beach corridor; no verified lead | `Kavaje data center`, `Kavajë server`, `Kavaje industrial data` |
| Rrogozhine | Low lead density; check municipal permits and logistics | `Rrogozhine data center`, `Rrogozhinë server`, `site:bashkiarrogozhine.gov.al leje ndertimi server` |

Tirane queries:

```text
"Tirana" "data center" OR "datacenter" OR "colocation"
"Tirane" "qendra e te dhenave" OR "kolokacion"
"TEDA" "Kashar" "data center"
"Albania Data Center" "Tirana" "32MW"
"Host.al" "Datacenter Albania HS1"
"RASH" "ANIX" "carrier-grade data center"
"AKSHI" "qendra e te dhenave" "Tirane"
"ALBtelecom" OR "One Albania" "data center" "Kashar"
"Abissnet" "hosting" "Tirana" "server"
"Tirana DataCom" "Kashar"
```

### 8.12 Vlore county

Municipalities: Delvine, Finiq, Himare, Konispol, Sarande, Selenice, Vlore.

Industry view: third-priority lead geography because of coastal/port context and Nisatel's operator/registered-seat lead. No verified physical DC found in checked sources; confirm any Nisatel or hosting claim before counting.

```text
"Vlore" "data center" OR "qendra e te dhenave"
"Vlorë" "Nisatel" "hosting" OR "server"
"Nisatel" "data center" OR "colocation"
"Sarande" "data center" OR "server"
"Vlore" "port" "data center"
"Vlore" "subsea" OR "cable" "data center"
```

---

## 9. Evidence handling and false positives

- **ADC is a pipeline lead, not an A-grade facility** until primary Albanian project records are found. Record the press details, then search QKB for `Alis Initiatives`, `Albania Data Center`, `H.A.P.I`, `Happy Technologies`, and `DIT`; search planifikimi/Tirana/KKTU for TEDA/Kashar permits; search OST/OSHEE/ERE for 32 MW/100 MW connection evidence.
- **Host.al is the cleanest commercial operator page** found: its own page supports a Tirana colocation/datacenter service. Still verify address, legal entity, permit, and power separately.
- **RASH/ANIX is interconnection-grade evidence**: official ANIX pages support a RASH carrier-grade data center in central Tirana; PeeringDB supports address/exchange/member details. Classify scope carefully.
- **ALBtelecom/One Albania records are name-fragile** because ALBtelecom/ONE merged into One Albania. Treat older ALBtelecom directory pages as C until One Albania/operator/official records confirm the facility.
- **Data Center Map's 5-facility count is not a final inventory**. It is a lead index to reconcile against operator and official sources.
- **Reseller VPS pages are weak**. Identify the underlying Tirana facility before adding a record.
- **Telecom POPs and mobile cores are not automatically data centers**. Require colocation, hosting, cloud, server-room, disaster-recovery, or IXP-hosted-facility evidence.
- **Government cloud tenders are not automatically new facilities**. They may be hardware refreshes inside an existing AKSHI facility.
- **County negatives must be explicit**. For non-Tirana counties, save the searched terms and sources; do not assume no data center just because aggregators are empty.

Minimum lead record:

```text
name:
operator_or_developer:
county:
municipality:
address_or_area:
status: operational | planned | tender | lead | false_positive
facility_type:
source_urls:
source_grade:
evidence_date:
confidence_notes:
next_primary_sources:
```
