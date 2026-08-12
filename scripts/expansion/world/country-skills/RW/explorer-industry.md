# RW Explorer Industry - Rwanda Press, Vendor, Interconnection, And Aggregator Discovery

Date verified: 2026-08-12. Scope: Rwanda datacenter enumeration from local press, African/international trade press, operator/vendor pages, interconnection records, hosting directories, job posts, and division-level search patterns. Pair with `explorer-official.md`; official sources decide final facility status where conflicts exist.

Reliability grades:
- **A** = primary/operator/official/donor: operator service pages or tenders, RURA/MINICT/RISA/NCSA/RPPA/RDB, World Bank, official cloud-region lists.
- **B** = strong secondary: Data Centre Dynamics, Connecting Africa, Agence Ecofin, The Stack, Datacentre Magazine, The New Times, IGIHE, KT Press, Africa Renewal, Internet Society, PeeringDB for interconnection metadata.
- **C** = lead only: DataCenterMap, datacenters.com, datacenterplanet, Baxtel, Inflect, colo.exchange, LinkedIn/social posts, unsourced blogs, vendor marketing without a named Rwanda site.
- **U** = unverified: aggregator-only or single-weak-source claims pending confirmation.

---

## 0. Rwanda Industry Frame

- Rwanda has a small but visible datacenter story: one ISP-operated hosting/colocation claim (TrAC, Telecom House), one aggregator-reported 3 MW carrier-neutral project inside Kigali Innovation City (PAIX), one announced 2 MW Africa Data Centres project from 2022 with no verified current build status, a 2026 Otech/Omantel x Broadband Systems Corp MoU, and aggregator-only listings (AOS, Raxio RW1, Paratus). Hyperscale clouds do not operate a Rwanda region (negative evidence, section 4).
- Kigali is the only commercial cluster. The four provinces are expected to yield telecom PoPs, university computing rooms, one satellite ground station (Eastern), and mostly negative commercial searches.
- Data-protection law (Law 058/2021), public-sector hosting requirements, RDAP, and IremboGov create hosting demand; a historical RURA fine against MTN (2017, IT services run offshore) shows enforcement pressure to keep regulated workloads in-country - useful context, not a facility.
- Connectivity is landlocked: international bandwidth arrives via terrestrial fibre to EASSy/TEAMS/SEACOM (Kenya/Tanzania). Kigali is also where the Rwanda Internet Exchange (RINEX) and the .rw registry (RICTA) operate, making Telecom House the interconnection anchor.
- Language: English and French give the best recall; Kinyarwanda is low yield. Key French terms: centre de donnees, hebergement, colocation, serveurs, salle des serveurs, fibre optique, point de presence, appel d'offres, mise en service.

---

## 1. Local Press

| Source | URL / route | Use | Grade |
|---|---|---|---|
| The New Times | https://www.newtimes.co.rw/ | Highest-value English-language outlet. Verified: Liquid Intelligent Technologies at AFPIF 2022 Kigali (data sovereignty): https://www.newtimes.co.rw/article/561/news/featured/liquid-intelligent-technologies-at-the-forefront-of-africas-data-sovereignty ; Liquid acquired Rwandatel assets 2013: https://www.newtimes.co.rw/article/93378/National/liquid-telecom-acquires-rwandatel-assets ; MTN 5G launch: https://www.newtimes.co.rw/article/27117/news/featured/mtn-rwanda-begins-5g-network-rollout | B; A when quoting official documents |
| IGIHE | https://en.igihe.com/ ; Kinyarwanda https://www.igihe.com/ | Operator/telecom coverage. MTN 5G rollout incl. Kigali and Kamonyi (Southern Province) sites: https://en.igihe.com/business-62/article/mtn-rwanda-launches-5g-network ; RDAP innovation-funding coverage (Kinyarwanda): https://www.igihe.com/ikoranabuhanga/mudasobwa/article/imishinga-22-yahawe-arenga-miliyari-2-frw-mu-mushinga-rdap | B/C |
| KT Press | https://www.ktpress.rw/ | Government/technology announcements; Irembo history: https://www.ktpress.rw/2019/01/untold-story-of-irembo-rwandas-one-stop-centre-for-govt-services/ | B/C |
| RwandaTechNews | https://rwandatechnews.com/ | Digital-government and KIC coverage: https://rwandatechnews.com/kigali-innovation-city-driving-rwandas-tech-future/ ; IremboGov upgrade: https://rwandatechnews.com/rwanda-digital-public-services-irembogov-upgrade/ | C (B when quoting officials) |
| CNBC Africa | https://www.cnbcafrica.com/ | Verified: MTN USD 8.5M fine for running IT services offshore (2017): https://www.cnbcafrica.com/2017/rwanda-utilities-regulatory-authority-fines-mtn-us-85m-non-compliance/ ; Starlink Rwanda launch: https://www.cnbcafrica.com/media/6320977012112/rwanda-launches-starlink-satellite-internet | B |
| The East African / AllAfrica | https://www.theeastafrican.co.ke/ ; https://allafrica.com/ | Regional corroboration (pay-TV/telecom context): https://allafrica.com/stories/202506250235.html | C/B |
| House in Rwanda | https://www.houseinrwanda.com/ | KIC/Africa50 context: https://www.houseinrwanda.com/news/africa50-signs-agreement-help-develop-kigali-innovation-city-rwanda | C |

Queries:
```text
site:newtimes.co.rw Rwanda ("data centre" OR "data center" OR Liquid OR colocation OR hosting)
site:en.igihe.com Rwanda ("data centre" OR "data center" OR serveurs OR fibre OR Raxio OR PAIX)
site:igihe.com Rwanda ("data centre" OR "data center" OR serveurs OR fibre OR Raxio OR PAIX)
site:ktpress.rw (Irembo OR "data centre" OR MTN OR Airtel OR cloud)
site:rwandatechnews.com ("data centre" OR datacenter OR KIC OR hosting)
"Rwanda" "data centre" OR "data center" news 2025 OR 2026 (Kigali OR Gasabo OR Kicukiro OR Nyarugenge)
```

Lifecycle verbs to capture: projet / MoU / etude (intent); appel d'offres / AMI / tender / awarded (pipeline); construction / travaux / groundbreaking (under construction); mise en service / inaugurated / go-live (operational).

---

## 2. African And International Trade Press

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Data Centre Dynamics | https://www.datacenterdynamics.com/en/regions/africa/ ; Rwanda tag https://www.datacenterdynamics.com/en/tags/rwanda/ | ADC Kigali 2MW announcement (2022-11): https://www.datacenterdynamics.com/en/news/africa-data-centres-to-build-first-data-center-in-kigali-rwanda/ ; Otech/BSC MoU (2026-06): https://www.datacenterdynamics.com/en/news/omantels-otech-signs-mou-to-build-data-center-in-rwanda/ . DCD pages may return 403 to curl but are indexed and open in browsers/search. | B for sourced articles |
| Connecting Africa | https://www.connectingafrica.com/ | MTN 5G coverage: https://www.connectingafrica.com/5g-networks/mtn-rwanda-launches-5g ; Pan-African DC roundups. | B/C |
| Agence Ecofin | https://www.agenceecofin.com/ | French-language infrastructure finance; Raxio/Africa DC expansion context. | B |
| Datacentre Magazine | https://datacentremagazine.com/ | Raxio USD 380M capital (2026-07): https://datacentremagazine.com/news/raxio-group-secures-380m-for-data-centres-in-africa | B |
| The Stack | https://www.thestack.technology/ | Raxio strategy interview; notes Raxio confirmed Ivory Coast/Tanzania but not Rwanda: https://www.thestack.technology/judy-nguru-raxio-african-co-location-data-centre-growth/ | B |
| IT News Africa / TechAfricaNews / WeAreTech Africa | https://www.itnewsafrica.com/ ; https://techafricanews.com/ ; https://www.wearetech.africa/ | Pan-African lead generation (e.g., historic Rwandatel/TEAMS route: https://www.itnewsafrica.com/2010/05/rwanda-to-seek-alternative-fibre-cable-route-to-seacom/ ). | B/C |
| Africa Data Centres Association | https://africadca.org/ | Regional market context; no Rwanda facility membership expected. | B for reports; C for unsourced facility claims |

Queries:
```text
site:datacenterdynamics.com Rwanda OR Kigali data center
site:connectingafrica.com Rwanda "data center" OR 5G OR fibre
site:agenceecofin.com Rwanda "centre de donnees" OR datacenter OR Raxio OR PAIX OR Otech
site:datacentremagazine.com Raxio OR Rwanda
site:thestack.technology Raxio OR Rwanda
"Rwanda" "data centre" Africa news (2025 OR 2026) Kigali
```

---

## 3. Operators, Hosters, And Vendors

| Entity | Primary or lead URL | Industry signal | Grade and handling |
|---|---|---|---|
| TrAC - TransAfrica Communications | https://trac.africa/ ; PeeringDB https://www.peeringdb.com/org/29956 ; DataCenterMap address https://www.datacentermap.com/rwanda/kigali/trac-kigali/ | Operator site markets cloud and tier 3 data centre hosting. Aggregator places TrAC at Telecom House, 8 KG 7 Ave, Kacyiru. | A for marketed service; C/U for facility specifics (racks, MW, certification) until independently confirmed. Do not treat "tier 3" wording as Uptime certification. |
| PAIX Data Centres | https://www.paix.io/ ; contact page https://www.paix.io/contact-us ; Africa50 profile https://www.africa50.com/our-funds/projects/paix-data-centers/ ; Kigali listings https://www.datacentermap.com/rwanda/kigali/paix-kigali/ and https://www.datacenters.com/paix-paix-kigali | Pan-African carrier-neutral operator. Aggregators list a 3 MW Kigali Innovation City facility, but PAIX official public pages and Africa50's profile currently emphasize Ghana/Kenya operating assets rather than Rwanda. | C aggregator; U for Rwanda status until PAIX/RDB/RURA/KIC/trade press confirms construction or go-live. |
| Africa Data Centres (ADC) | https://www.africadatacentres.com/ ; Cassava release https://www.cassavatechnologies.com/africa-data-centres-to-build-its-first-data-centre-in-kigali/ ; DCD coverage (2022, 2026) | 2 MW Kigali facility announced Nov 2022 (ground break Q1 2023); no current operator facility page or construction/go-live evidence found in this pass. | B for announcement; U for current status. |
| Otech (Omantel) / Broadband Systems Corporation | DCD coverage: https://www.datacenterdynamics.com/en/news/omantels-otech-signs-mou-to-build-data-center-in-rwanda/ ; BSC LinkedIn (via DCD link) | Otech (ex-Oman Data Park) + Kigali ISP BSC signed 2026-06 MoU to co-invest in an AI-ready Tier III data centre in Rwanda. | B for MoU; U for site/construction. |
| Raxio Group | https://www.raxiogroup.com/ ; data centres page https://www.raxiogroup.com/data-centres/ | Official data-centres page lists Angola, Cote d'Ivoire, DRC, Ethiopia, Mozambique, Tanzania, and Uganda - Rwanda is not listed. Aggregator 'Raxio RW1 Kigali' (Gasabo) is unconfirmed: https://datacenterplanet.com/listings/raxio-rw1-kigali-rwanda | U/C for any Rwanda claim; watch for official Rwanda expansion news. |
| MTN Rwanda | https://www.mtn.com/case-study/partnerships-for-the-planet-clean-energy-solutions-mtn-rwanda/ ; PeeringDB facility https://www.peeringdb.com/fac/11839 | Market leader (~61.8%, 2024); 5G from June 2025; MTN Centre Kigali facility on PeeringDB. | B for network/5G; C for DC claim; facility record only with hosting/cloud evidence. |
| Airtel Rwanda | https://www.airtel.co.rw/ ; contact page https://www.airtel.co.rw/contact-us ; Ecofin 4G article https://www.ecofinagency.com/telecom/2607-44768-rwanda-airtel-and-mtn-launch-4g-networks | Second MNO; no public DC claim verified. | B operator; C for DC. |
| Liquid Intelligent Technologies Rwanda | https://za.liquid.tech/ ; New Times coverage (above) | Ex-Rwandatel fibre assets acquired in 2013; markets connectivity/cloud regionally; no verified local colo DC. | B fibre presence; U for local DC. |
| Broadband Systems Corporation (BSC) | DCD coverage (above) | Kigali ISP described by DCD as founded in 2010 with nationwide fibre and radio networks; Otech MoU partner. | B via DCD for company/MoU facts; use official site/RURA licence if available before adding facility details. |
| Paratus | https://www.paratus.africa/ ; 2026 Goma-Mombasa route announcement https://paratus.africa/blog/paratus-lights-up-new-east-africa-fiber-highway-linking-goma-to-mombasa/ ; listing https://datacenterplanet.com/listings/paratus-rwanda-data-centre-kigali | Pan-African connectivity provider; official announcement says the Goma-Mombasa protected route runs via Kigali and that Paratus Rwanda is licensed. Its official data-centre menu lists Angola, Namibia, and Zambia, not Rwanda. | B for connectivity/Rwanda presence; C/U for local DC listing. |
| AOS Ltd | https://www.datacentermap.com/rwanda/kigali/aos/ | Local IT-service provider colocation at Kigali Business Centre, KN 5 Rd (not carrier-neutral; listing updated 2023-06). | C; verify current operations. |
| Huawei / ZTE / Ericsson | vendor + operator tender pages | 4G/5G/fibre/core equipment suppliers in Rwanda (MTN/Airtel/Liquid rollouts). | B/C; vendor case studies rarely prove facility status. |
| Starlink | https://www.cnbcafrica.com/media/6320977012112/rwanda-launches-starlink-satellite-internet | Operating since Feb 2023; enterprise backhaul option. | Connectivity only; ground-station/gateway claims need confirmation. |

Operator queries:
```text
site:trac.africa ("data centre" OR colocation OR hosting OR cloud)
site:paix.io (Kigali OR Rwanda)
site:raxiogroup.com Rwanda
site:mtn.co.rw ("data centre" OR cloud OR hosting)
site:africadatacentres.com (Kigali OR Rwanda)
"Broadband Systems Corporation" Rwanda fibre OR "data centre"
"Paratus" Rwanda "data centre" OR Kigali
"Liquid Intelligent Technologies" Rwanda cloud OR "data centre" OR colocation
"Huawei" Rwanda MTN OR Airtel OR Liquid OR "data centre"
```

---

## 4. Interconnection, IXP, Aggregators, And Hyperscaler Negative Evidence

| Channel | URL | Use | Grade |
|---|---|---|---|
| RINEX / Rwanda Internet Exchange | ISOC Pulse IXP tracker: https://pulse.internetsociety.org/en/ixp-tracker/country/RW/ ; AS329521 whois: https://whois.ipip.net/AS329521 | Operating IXP at Telecom House, Kacyiru; ~15 members late 2025. Interconnection anchor, not DC capacity. | B |
| .rw registry (RICTA) | http://www.ricta.org.rw/ | ccTLD registry; registry infrastructure in Kigali. | B/C |
| PeeringDB | https://www.peeringdb.com/fac/11839 (MTN Centre Kigali); https://www.peeringdb.com/org/29956 (TrAC) ; search 'Kigali' facilities | Interconnection metadata: facilities, networks, exchanges. | B/C metadata only |
| Submarine cables | TeleGeography map: https://www.submarinecablemap.com/ ; ISOC 2024 East Africa outage report: https://www.internetsociety.org/resources/doc/2024/2024-east-africa-submarine-cable-outage-report/ | No cable lands in Rwanda (landlocked); Rwanda connects via Kenya/Tanzania landings (TEAMS, SEACOM, EASSy; 2Africa onward). PoP location matters for latency. | B for geography |
| DataCenterMap Rwanda | https://www.datacentermap.com/rwanda/ ; Kigali list https://www.datacentermap.com/rwanda/kigali/ | 3 facilities listed (PAIX Kigali, TrAC, AOS). | C discovery |
| datacenters.com | https://www.datacenters.com/paix-paix-kigali ; Raxio provider page https://www.datacenters.com/providers/raxio | PAIX Kigali and Raxio provider profiles. | C discovery |
| datacenterplanet | https://datacenterplanet.com/listings/raxio-rw1-kigali-rwanda ; https://datacenterplanet.com/listings/paratus-rwanda-data-centre-kigali | Raxio RW1 and Paratus Rwanda listings (unverified). | U/C |
| Inflect | https://inflect.com/building/kigali-kigali/africa-data-centres/datacenter/kigali | ADC Kigali building listing. | C corroboration of 2022 announcement |
| Baxtel / colo.exchange / Colomap | https://baxtel.com/data-centers/raxio-group ; https://colo.exchange/ | Lead discovery only. | C |
| Uptime Institute | https://uptimeinstitute.com/ | No Rwanda facility verified as Uptime-certified in this pass. TrAC's 'tier 3' is a self/operator marketing claim unless a certificate appears. | C/U negative |
| Hyperscaler regions | AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; GCP https://cloud.google.com/about/locations ; OCI https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Rwanda region; nearest are Johannesburg/Cape Town. Negative evidence for local hyperscale. | A negative |

Aggregator/IXP queries:
```text
"RINEX" OR "Rwanda Internet Exchange" members facilities Kigali
site:peeringdb.com Kigali Rwanda facility
site:datacentermap.com Rwanda Kigali colocation
site:datacenterplanet.com Rwanda Kigali
site:inflect.com Rwanda Africa Data Centres
site:uptimeinstitute.com Rwanda ("certified" OR "Tier III" OR "data center" OR "data centre")
```

---

## 5. Search Templates

### 5.1 English templates

```text
"Rwanda" ("data centre" OR "data center" OR datacentre OR colocation) (Kigali OR Gasabo OR Kicukiro OR Nyarugenge)
"Rwanda" ("national data centre" OR "sovereign cloud" OR "data hosting" OR "cloud first")
"Kigali" ("data centre" OR "data center" OR "server room" OR "server hosting" OR "tier 3")
"Kigali Innovation City" ("data centre" OR datacenter OR hosting OR cloud)
"Rwanda" (Raxio OR PAIX OR "Africa Data Centres" OR Otech OR Omantel OR Paratus OR TrAC OR AOS) ("data centre" OR datacenter)
"Rwanda" (MTN OR Airtel OR Liquid) ("data centre" OR "server" OR "core network" OR cloud)
filetype:pdf Rwanda "data centre" OR "data center" OR "hebergement des donnees"
filetype:pdf Rwanda ("data centre" OR "data center" OR "hebergement des donnees")
"Rwanda" "data center" tender OR "request for proposals" 2025 OR 2026
"Rwanda" "data center" (tender OR "request for proposals") (2025 OR 2026)
```

### 5.2 French templates

```text
"Rwanda" ("centre de donnees" OR "data center" OR datacenter OR "centre d'hebergement" OR colocation)
"Kigali" ("centre de donnees" OR hebergement OR colocation OR "salle des serveurs")
"Rwanda" (Raxio OR PAIX OR Otech OR Omantel OR TrAC) "centre de donnees"
"Rwanda" "appel d'offres" ("centre de donnees" OR serveurs OR hebergement OR "infrastructure numerique")
"Rwanda" (fibre optique OR "point de presence" OR "mise en service") "centre de donnees"
```

### 5.3 Kinyarwanda low-yield checks

Use only as a recall aid for district-level government posts; verify positives in English/French.

```text
Rwanda ikigo cy'imyirondoro OR "serveurs" OR ikoranabuhanga
Kigali data serveurs itumanaho OR ikoranabuhanga
```

---

## 6. Division Enumeration (5 divisions)

| Division | Seeds and expectations |
|---|---|
| City of Kigali | Everything commercial: TrAC (Telecom House, Kacyiru/Gasabo), RINEX, NCSA, PAIX lead (KIC), AOS lead (KN 5 Rd), MTN Centre, Airtel HQ, ADC/Otech/BSC/Raxio-RW1/Paratus pending. Highest yield; expect facility records/leads plus IXP and government-hosting context. |
| Eastern | Rwanda Space Agency teleport, Mwulire (Rwamagana) - operational ground station (satellitetoday URL in section 4/official file). Bugesera airport digital infrastructure; Tanzania-border fibre corridor (Kirehe/Kayonza). Mostly negative commercial searches. |
| Northern | Musanze, Gicumbi, Rulindo: university labs, tourism-tech, backbone PoPs. Negative commercial expectation. |
| Western | Rubavu, Rusizi, Karongi, Nyamasheke: DRC-border fibre, Lake Kivu methane power (energy context). Negative commercial expectation. |
| Southern | Huye (University of Rwanda), Nyanza, Muhanga, Kamonyi (MTN 5G sites per IGIHE), Ruhango: university computing and telecom edge. Negative commercial expectation. |

Division query block:
```text
"Kigali" OR "Gasabo" OR "Kicukiro" OR "Nyarugenge" Rwanda (TrAC OR PAIX OR RINEX OR AOS OR MTN OR Airtel) ("data centre" OR colocation OR hosting OR "tier 3")
"Rwamagana" OR "Bugesera" OR "Eastern Province" Rwanda (teleport OR "ground station" OR satellite OR "data centre" OR airport OR fibre)
"Musanze" OR "Gicumbi" OR "Northern Province" Rwanda ("data centre" OR serveurs OR fibre OR "point de presence")
"Rubavu" OR "Rusizi" OR "Western Province" Rwanda ("data centre" OR serveurs OR fibre OR "point de presence")
"Huye" OR "Kamonyi" OR "Southern Province" Rwanda ("data centre" OR serveurs OR fibre OR "point de presence" OR university)
```

Negative-search rule: do not count ICT offices, cybercafes, computer labs, NGO server rooms, GIS rooms, or software platforms unless a source describes hosting/colo/compute infrastructure with a named operator and location.

---

## 7. Grading And Verification Rules

- **A operating facility**: official/operator/donor source names a site with location and infrastructure function.
- **B operating facility**: strong press names a site/location with enough detail to distinguish a facility, preferably quoting an official.
- **C lead**: aggregator listing, social/job post, reseller page, or service page with no local physical evidence.
- **U**: aggregator-only or single weak source; re-check before promotion (Raxio RW1, Paratus DC listing, PAIX status, ADC current status, TrAC Uptime Tier III certification, AOS).
- **Provider-level service**: official hosting/cloud/server offer without a named facility (TrAC hosting, Liquid cloud, MTN services).
- **Planned/pipeline**: ADC (announced 2022, status unclear), Otech/BSC (2026 MoU), PAIX Kigali (status unverified) - all stay non-operational until tender/construction/inauguration evidence.
- **Interconnection**: RINEX, PeeringDB entries, subsea/terrestrial fibre routes - not datacenter capacity.
- **Telco core**: MTN/Airtel/Liquid sites count only if the source describes core/network/server/hosting infrastructure, not merely coverage.
- **Capacity**: keep null unless kW/MW/racks/floor area are stated by an official/operator/tender source (PAIX 3 MW and ADC 2 MW come from listings/announcements - cite as such).
- **Power**: cross-check large claims with REG/EUCL grid evidence, RURA electricity context, and generator/substation procurement (official file section 2.5).
- **Cloud**: AWS/Azure/GCP/OCI official region pages are negative evidence for Rwanda.
- **De-dup**: one building (Telecom House) may host TrAC, RINEX, NCSA - record per operator, do not merge.

---

## 8. Verified Source Anchors (industry side, as of 2026-08)

- The New Times: https://www.newtimes.co.rw/
- IGIHE EN: https://en.igihe.com/ ; MTN 5G/Kamonyi: https://en.igihe.com/business-62/article/mtn-rwanda-launches-5g-network
- KT Press: https://www.ktpress.rw/
- DCD Rwanda tag: https://www.datacenterdynamics.com/en/tags/rwanda/ ; ADC Kigali: https://www.datacenterdynamics.com/en/news/africa-data-centres-to-build-first-data-center-in-kigali-rwanda/ ; Otech/BSC: https://www.datacenterdynamics.com/en/news/omantels-otech-signs-mou-to-build-data-center-in-rwanda/
- Connecting Africa MTN 5G: https://www.connectingafrica.com/5g-networks/mtn-rwanda-launches-5g
- Datacentre Magazine Raxio: https://datacentremagazine.com/news/raxio-group-secures-380m-for-data-centres-in-africa
- CNBC Africa MTN fine: https://www.cnbcafrica.com/2017/rwanda-utilities-regulatory-authority-fines-mtn-us-85m-non-compliance/ ; Starlink: https://www.cnbcafrica.com/media/6320977012112/rwanda-launches-starlink-satellite-internet
- TrAC: https://trac.africa/new-home/ ; PeeringDB https://www.peeringdb.com/org/29956
- PAIX: https://www.paix.io/ ; Africa50 profile https://www.africa50.com/our-funds/projects/paix-data-centers/ ; listings https://www.datacentermap.com/rwanda/kigali/paix-kigali/ ; https://www.datacenters.com/paix-paix-kigali
- Raxio: https://www.raxiogroup.com/data-centres/ ; RW1 listing https://datacenterplanet.com/listings/raxio-rw1-kigali-rwanda
- ADC: Cassava release https://www.cassavatechnologies.com/africa-data-centres-to-build-its-first-data-centre-in-kigali/ ; Inflect https://inflect.com/building/kigali-kigali/africa-data-centres/datacenter/kigali
- Paratus listing: https://datacenterplanet.com/listings/paratus-rwanda-data-centre-kigali
- AOS: https://www.datacentermap.com/rwanda/kigali/aos/
- DataCenterMap Rwanda: https://www.datacentermap.com/rwanda/
- ISOC IXP tracker: https://pulse.internetsociety.org/en/ixp-tracker/country/RW/ ; ISOC 2024 outage report: https://www.internetsociety.org/resources/doc/2024/2024-east-africa-submarine-cable-outage-report/
- RINEX AS329521: https://whois.ipip.net/AS329521 ; RICTA: http://www.ricta.org.rw/
- MTN Centre Kigali (PeeringDB): https://www.peeringdb.com/fac/11839
- IremboGov: https://irembo.gov.rw/ ; Irembo: https://irembo.com/
- KIC ground-breaking (RDB): https://rdb.rw/the-government-of-rwanda-africa50-and-badea-break-ground-on-the-construction-of-kigali-innovation-city/
- D4D Hub Rwanda Data Center Market Brief: https://cms.d4dhub.eu/assets/Initiatives/Data-Governance-in-Africa/Digital-Investment-Facility/2507_Country-Market-Briefs/Data-Center-Market-Brief-Rwanda.pdf
- Rwanda Space Agency / Mwulire: https://www.satellitetoday.com/technology/2025/07/16/atlas-space-operations-adds-to-ground-network-with-rwanda-antenna/ ; https://space.gov.rw/
- Wikipedia Telecommunications in Rwanda: https://en.wikipedia.org/wiki/Telecommunications_in_Rwanda

Final note: in a small market like Rwanda, aggregators matter for discovery but only official/operator/trade-press evidence closes a record. Keep every pending facility or facility detail (PAIX, ADC, Otech/BSC, Raxio RW1, Paratus, TrAC Tier III, AOS) flagged with its true grade until re-verified.
