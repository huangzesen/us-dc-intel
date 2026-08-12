# LK Explorer Industry - Sri Lanka Datacenter Enumeration

Date reviewed: 2026-08-12. Country: **LK - Sri Lanka**. Scope: industry, press, operator, vendor, directory, IXP, market-report, and local-language discovery for Sri Lankan data centers and data-center-like infrastructure. Division model: **9 provinces**: Western; Central; Southern; Northern; Eastern; North Western; North Central; Uva; Sabaragamuwa.

Use this file with `explorer-official.md`. Industry sources are useful for discovery, but final facility records should be upgraded through operator pages, Uptime, government records, permits, procurement, or BOI where possible.

## Reliability Grades

- **A**: primary source for the exact fact claimed: official operator page/news, Uptime Institute certification directory, TRCSL/ICTA/BOI/DPA/UDA/CEB/Treasury/NPC, official cloud-region pages, eROC/RIPE for entity facts.
- **B**: reputable secondary source: Data Center Dynamics, Daily FT, EconomyNext, Daily Mirror, Sunday Times, The Island, Capacity Media, TeleGeography/Submarine Cable Map, Submarine Networks, ITU/UN/World Bank, vendor case study naming a site.
- **C**: lead source only: DataCenterMap, datacenters.com, Cloudscene, Baxtel, Inflect, PeeringDB-only inference, social posts, market-report snippets, tender aggregators without original documents.
- **U**: unsupported or contradicted.

## 0. Market Frame

- Sri Lanka's visible data-center market is concentrated in **Western Province**, especially Colombo District and suburbs: Pitipana/Homagama, Malabe, Piliyandala, Colombo 07, Welikada, and Mount Lavinia.
- Verified primary/strong leads include SLT-Mobitel Pitipana, SLT HQ/Welikada lead, Dialog Malabe, Dialog Piliyandala, Lankacom Colombo 07 services, MillenniumIT/LSEG Malabe, National Savings Bank Production Data Center, ICTA/Lanka Government Cloud estate, and cable landing stations.
- **No AWS, Azure, Google Cloud, or Oracle OCI public cloud region in Sri Lanka** was found on official region lists checked 2026-08-12. Local "cloud" claims are usually SLT Akaza, Dialog cloud/colocation, Lankacom hosting, or ICTA government cloud.
- Cable/connectivity is central: Submarine Networks lists five cable landing stations in Sri Lanka and identifies SLT's Welikada premises as the international backhaul hub. Four of the five cable landing stations are in Western Province; Matara CLS is in Southern Province.
- Market reports can describe demand, share, or forecasts, but they do not prove a facility. Keep Mordor, 6Wresearch, and similar snippets at C unless they point to a named facility that can be verified elsewhere.

## 1. Core Industry Queries

Use exact phrases and localities. Avoid over-broad OR chains when using search engines; run separate queries if results are noisy.

```text
"Sri Lanka" "data centre"
"Sri Lanka" "data center"
"Sri Lanka" "colocation"
"Sri Lanka" "Tier III" "data centre"
"Colombo" "data centre" "Sri Lanka"
"Homagama" "data centre"
"Pitipana" "data center"
"Malabe" "data centre"
"Piliyandala" "data centre"
"Matara" "cable landing station"
"Hambantota" "data centre"
"Kandy" "data centre"
"Lanka Government Cloud" "data centre"
"SLT" "National Data Center" "Pitipana"
"Dialog" "Data Centre" "Malabe"
"Dialog" "Data Centre" "Piliyandala"
"Lankacom" "data center"
"MillenniumIT" "Tier 3 data centre"
```

Sinhala/Tamil local-search set:

```text
"දත්ත මධ්‍යස්ථානය" "ශ්‍රී ලංකාව"
"දත්ත මධ්‍යස්ථානය" "කොළඹ"
"දත්ත මධ්‍යස්ථානය" "හෝමාගම"
"දත්ත මධ්‍යස්ථානය" "මාලබේ"
"මුහුදු යට කේබලය" "මාතර"
"தரவு மையம்" "இலங்கை"
"தரவு மையம்" "கொழும்பு"
"தரவு மையம்" "யாழ்ப்பாணம்"
"கடலடி கேபிள்" "இலங்கை"
```

Status interpretation:

- `opened`, `launched`, `commissioned`, `inaugurated`: operational claim; verify with operator/official source.
- `certified`: only A when Uptime or another certifier directory confirms the exact facility/certification.
- `planned`, `MoU`, `partnership`, `proposed`: lead only until site/operator/stage are named.
- `hosting`, `cloud`, `VPS`, `managed services`: service evidence only unless a physical facility is named.

## 2. High-Signal Industry Sources

| Source | URL / route | Use | Default grade |
|---|---|---|---|
| Data Center Dynamics | https://www.datacenterdynamics.com/en/tags/sri-lanka/ ; SLT Pitipana article; Dialog Piliyandala article; Dialog/Malabe Tier III article | Sparse but strong DC trade coverage | B |
| Daily FT | https://www.ft.lk/ ; MillenniumIT and SLT Pitipana coverage | Local business/telecom reporting | B |
| Sunday Times | https://www.sundaytimes.lk/ | Business coverage, MillenniumIT references | B |
| EconomyNext | https://economynext.com/ | Telecom/macro/tech news | B |
| Daily Mirror | https://www.dailymirror.lk/ | Operator strategy/policy news | B |
| The Island | https://island.lk/ | Business/telecom context | B/C depending detail |
| readme.lk | https://readme.lk/ | Local technical background on cloud outages and cable stations | B/C |
| Capacity Media / Developing Telecoms / Telecompaper | site-scoped searches | Cable/operator launch corroboration | B |
| Submarine Networks | https://www.submarinenetworks.com/en/stations/asia/sri-lanka | Cable station inventory and SLT Pitipana secondary article | B, sometimes A/B for cable-source facts |
| TeleGeography Submarine Cable Map | https://www.submarinecablemap.com/ | Cable-route/status cross-check | B |
| FITIS / SLASSCOM | https://fitis.lk/ ; https://slasscom.lk/ | ICT sector policy/events; weak facility evidence | B/C |
| LIRNEasia | https://lirneasia.net/ | Policy/economic analysis, e.g. 2026 data-centre hub commentary | B/C for context only |
| Mordor / 6Wresearch | market-report pages | Demand forecasts and market framing | C only |

Useful site-scoped queries:

```text
site:datacenterdynamics.com "Sri Lanka" "data center"
site:ft.lk "Sri Lanka" "data centre"
site:sundaytimes.lk "data centre" "Sri Lanka"
site:economynext.com "data centre" "Sri Lanka"
site:dailymirror.lk "SLT-Mobitel" "data centre"
site:readme.lk "Lanka Government Cloud"
site:capacitymedia.com "Sri Lanka" "cable"
site:telecompaper.com "Dialog Axiata" "data centre"
site:lirneasia.net "data centre" "Sri Lanka"
```

## 3. Operator and Facility Leads

| Lead | Province / locality | What is verified | Handling |
|---|---|---|---|
| SLT-Mobitel National Data Center | Western / Pitipana-Homagama | SLT official pages name Pitipana, Tier III services, 500 racks, opening on 2018-01-16, Rs. 2.4bn+ investment; Uptime lists Tier III Design and Constructed Facility awards for SLT National Data Center in Pitipana-Homagama; DCD corroborates 500 racks. | Strong facility. A for operator/Uptime facts; B for DCD/Submarine Networks corroboration. |
| SLT HQ Data Centre / Welikada | Western / Colombo-Welikada | SLT's Pitipana article references an HQ Data Centre in Colombo; Submarine Networks states SLT connects CLSs to the international backhaul hub at Welikada premises. | Keep as network/data-center lead unless a direct SLT HQ DC page is found. Capacity U. |
| Dialog Broadband Networks Malabe Data Center #2 | Western / Malabe | Uptime lists Tier III Design and Constructed Facility awards; Dialog 2017 official news says the facility is at Malabe and offers hosting, colocation, and cloud services with a media hub. | Strong facility. A for certification/location/services. |
| Dialog Data Centre Piliyandala | Western / Piliyandala | Dialog official 2021 news announces latest fully owned data centre in Piliyandala offering hosting, co-location, and cloud services; DCD corroborates. | A for launch/location/services. Do not transfer Malabe Uptime certification to Piliyandala without a separate Uptime entry. |
| Lankacom data center / hosting services | Western / Colombo 07 | Lankacom official pages state datacenter/cloud hosting services and 65C Dharmapala Mawatha address. | A for service/address; no capacity/certification unless separately sourced. |
| MillenniumIT / LSEG Malabe data centre | Western / Malabe | Daily FT reports 2015 launch of Sri Lanka's first privately held Tier 3 data centre with 80 racks and 3,000 sq ft raised floor; LSEG page confirms Malabe campus. | B for data-centre/Tier/capacity claims; A for campus address only. |
| National Savings Bank Production Data Center | Western / Colombo | Uptime country page lists Tier III Certification of Design Documents. | A for certification and city-level location; institutional, not public colo. |
| ICTA / Lanka Government Cloud | Western likely; national service | ICTA official role; SLT LGN 2.0 communications infrastructure role; readme.lk can provide outage/background context. | A for ICTA/LGN program; B/C for physical hosting unless source names the data hall. |
| Lanka Bell / FALCON CLS | Western / Colombo | Submarine Networks lists Lanka Bell Colombo CLS for FALCON. | Cable facility; re-check operational status. |
| Host Asia and other hosting providers | Western likely | Marketing pages may claim Sri Lanka data centers or Tier III facilities. | C until operator identity, facility, and certification are independently verified. |
| Bank, university, and enterprise server rooms | Mostly Western; some provincial | Usually internal IT/DR facilities. | Count only when source names a data center; otherwise note as institutional lead. |

## 4. Directory / Aggregator Handling

Use directories only as pivots:

| Directory | Use | Caveat |
|---|---|---|
| DataCenterMap | Facility names, locality hints, sometimes addresses and rack/power claims | C; counts vary and facility facts must be verified elsewhere |
| datacenters.com | Provider profiles such as SLTMobitel Pitipana | C; do not import power/building figures without operator or strong press support |
| Cloudscene / Baxtel / Inflect | Discovery and cross-reference | C by default |
| PeeringDB | IX/ASN/network presence | C for facility inference; does not prove a data center |
| RIPE / APNIC records | Entity or network registration | A for registration facts only |
| Uptime Institute | Certification directory | A for exact certification and listed location |

Upgrade workflow:

1. Capture exact facility name, operator, locality, claimed capacity, and source URL.
2. Search operator site and official news with exact quoted names.
3. Search Uptime country/certification pages for Tier claims.
4. Search BOI, ICTA, TRCSL, UDA/OSU/local authority, and procurement sources.
5. If no primary or strong secondary support exists, keep the lead at C or U.

## 5. Province-by-Province Industry Matrix

| Province | Locality pivots | Expected industry yield |
|---|---|---|
| **Western Province** | Colombo, Colombo 07, Welikada, Port City, Mount Lavinia, Malabe, Piliyandala, Pitipana, Homagama, Ratmalana, Gampaha, Katunayake, Kalutara | Highest yield. Verified SLT, Dialog, Lankacom, MillenniumIT/LSEG, National Savings Bank, cable landings, government cloud leads, IX/PeeringDB pivots, and most industry press. |
| **Central Province** | Kandy, Matale, Nuwara Eliya, Peradeniya | Low yield. Search for Kandy DC growth claims, universities, banks, telco POPs, and cool-climate proposals. Market-report "Kandy growth" remains C unless a named facility appears. |
| **Southern Province** | Matara, Galle, Hambantota, Mirijjawila, Weerawila | Matara CLS is verified cable infrastructure. Hambantota is a recurring logistics/energy/investment-zone lead but no data-center project was verified. |
| **Northern Province** | Jaffna, Vavuniya, Mannar, Kilinochchi, Mullaitivu | No verified commercial DC. Search Tamil terms, Jaffna university/government ICT, and telco network upgrades. |
| **Eastern Province** | Trincomalee, Batticaloa, Ampara | No verified commercial DC. Search port/BOI/energy/digital-zone rumors carefully; keep unsourced Trincomalee claims U. |
| **North Western Province** | Kurunegala, Puttalam | No verified commercial DC. Search energy projects, BOI zones, telco POPs, banks/universities. |
| **North Central Province** | Anuradhapura, Polonnaruwa | No verified commercial DC. Search government ICT, telco POPs, and institutional server-room mentions. |
| **Uva Province** | Badulla, Moneragala | No verified commercial DC. Negative-search default after EN/SI/TA and official passes. |
| **Sabaragamuwa Province** | Ratnapura, Kegalle | No verified commercial DC. Negative-search default after EN/SI/TA and official passes. |

## 6. Candidate Decision Rules

- **SLT Pitipana**: accept as operational data center. Record Uptime Tier III Design and Constructed Facility as A. Record 500 racks and Rs. 2.4bn+ as operator-stated A/B, with SLT page preferred over aggregator copies.
- **Dialog Malabe**: accept as Uptime-certified operational data center. Keep separate from Piliyandala.
- **Dialog Piliyandala**: accept as operational operator-announced data center. Tier/capacity claims require exact facility evidence.
- **Lankacom**: accept as data-center/cloud-hosting service provider at Colombo 07; capacity and physical data-hall details remain unknown.
- **MillenniumIT/LSEG**: accept as strong B institutional/private data-center lead; not public colo unless a service offer is found.
- **ICTA government cloud**: accept program/service estate; do not assign a physical facility unless source names it.
- **Cable landing stations**: accept as cable facilities; do not count as commercial DCs.
- **Port City / Hambantota / Kandy growth**: keep as future-market leads only until a named project appears.
- **Hyperscaler claims**: reject or mark U unless AWS/Azure/GCP/OCI official pages list a Sri Lanka region or a named edge/POP facility.

## 7. Output Discipline

- Prefer `data centre` in notes when quoting Sri Lankan/Commonwealth sources; normalize schema values as needed.
- Use province, district, and locality. For Western Province, distinguish Colombo city, Malabe, Piliyandala, Pitipana/Homagama, Mount Lavinia, and Colombo 07.
- Do not collapse Dialog Malabe and Dialog Piliyandala into one facility.
- Do not import MW from aggregators. Use `capacity_mw` only for exact site-named MW/IT-load evidence.
- Keep "no_projects" conservative and evidence-backed for the seven low-yield provinces.
- Re-check DCD, Daily FT, EconomyNext, BOI, ICTA, Uptime, Submarine Networks, Submarine Cable Map, PeeringDB, and operator pages on every refresh.

## 8. Verified Industry URL Ledger

Opened and usable in this review: https://www.datacenterdynamics.com/en/tags/sri-lanka/ ; https://www.datacenterdynamics.com/en/news/sri-lanka-telecom-opens-national-data-center/ ; https://www.datacenterdynamics.com/en/news/dialog-axiata-opens-new-data-center-in-piliyandala-sri-lanka/ ; https://www.datacenterdynamics.com/en/news/sri-lanka-gets-first-tier-iii-certified-data-center/ ; https://www.ft.lk/IT-Telecom-Tech/millenniumit-launches-sri-lankas-first-privately-held-tier-3-data-centre/50-505901 ; https://www.slt.lk/en/business/data-center ; https://www.slt.lk/en/content/slt-announces-grand-opening-state-art-tier-3-%25E2%2580%259Cnational-data-center%25E2%2580%259D-sri-lanka ; https://dialog.lk/news/Dialog-Launches-Sri-Lankas-first-TIER-III-Certified-Data-Center-and-Media-Hub?language=en ; https://dialog.lk/news/dialog-axiata-launches-its-latest-data-centre-built-to-global-standards-in-piliyandala?language=en ; https://www.lankacom.net/ ; https://www.lankacom.net/datacenter-services/ ; https://www.submarinenetworks.com/en/stations/asia/sri-lanka ; https://uptimeinstitute.com/uptime-institute-awards/country/id/LK ; https://www.lseg.com/en/locations/details/malabe ; https://www.portcitycolombo.lk/ ; https://lirneasia.net/2026/03/rethinking-sri-lankas-data-centre-hub-ambition/ ; https://www.datacentermap.com/sri-lanka/ ; https://www.datacenters.com/locations/sri-lanka/colombo/colombo-2 ; https://cloudscene.com/ ; https://www.peeringdb.com/ .

