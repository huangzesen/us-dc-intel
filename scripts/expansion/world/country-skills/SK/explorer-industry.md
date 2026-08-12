# SK Explorer Industry - Slovakia Datacenter Enumeration from Operators, Cloud, IXPs, Associations, Directories, HPC, and Press

Date: 2026-08-12. Country: **SK Slovakia**. Scope: industry / operator / press / directory-led discovery for Slovak data centers, with official verification routes in `explorer-official.md`. Reliability grades: **A** = official operator, cloud, IXP, association, public-institution, or certifier page for the fact claimed; **B** = reputable press, vendor case study, or government trade guide; **C** = directory, marketplace, social, map, SEO, or unverified claim.

---

## 0. Slovakia market frame

- Slovakia is a **small, Bratislava-centric** colocation and hosting market. Bratislava has the strongest cluster: Slovak Telekom, Orange TechPark, SWAN, VNET / DC Digitalis / SHC, SITEL, 1 Cloud Lab, eServer-in-Digitalis, WebSupport-style hosting leads, NASES / Government Cloud, SPP-hosted government capacity, and SAV / PERUN.
- **Košice** is the secondary hub. SITEL POPKE is the clearest commercial colocation anchor; MIRRI has also announced the policy direction for a Košice national-supercomputer component.
- **Trnava, Trencin, Nitra, Zilina, Banska Bystrica, and Presov** are low-density for commercial colocation. Search them mainly for public-sector server rooms, hospital/university procurements, industrial enterprise IT, disaster recovery, and future Tatra Supercompute / AI-factory filings.
- Slovakia is landlocked. IXPs and terrestrial fibre are important discovery routes but **not facility counts**.
- No official AWS, Microsoft Azure, Google Cloud, or Oracle OCI page reviewed on 2026-08-12 lists a Slovakia public cloud region or local zone.

Core industry queries:

```text
Slovakia "data center" Bratislava
Slovakia datacenter Košice
Slovensko "dátové centrum" "kolokácia"
"datacentrum" Bratislava operator
"serverhousing" Bratislava Slovensko
"colocation" "Bratislava" "Slovakia"
"dátové centrum" "Košice" "kolokácia"
"AI factory" Slovakia "data center"
"Tatra Supercompute" OR "Tatra AI"
"superpočítač" Bratislava Košice PERUN
```

Status-language interpretation:

- `prevádzkuje`, `operates`, `service page`, `housing`, `colocation`, `virtual data center` = operational service signal, subject to facility specificity.
- `coming soon`, `planned`, `building`, `will build`, `project`, `MoU`, `government endorsed` = lead / planned lead until official site evidence appears.
- `TIER 3`, `Tier III`, `Tier 3+`, `TIER3 ECO` on operator or directory pages = self-claim unless matched to a certifier record.
- `PoP`, `IXP`, `peering facility`, `edge`, `CloudFront`, `Direct Connect`, `ExpressRoute`, `sales office` = connectivity / service lead only.

---

## 1. Official cloud-region status

| Provider | Official URL | Review result | Counting instruction |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | Official pages reviewed on 2026-08-12 did not contain Slovakia. | Do not count an AWS Slovakia Region or Local Zone. Treat edge / partner mentions as network leads only. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | Official region list reviewed on 2026-08-12 did not contain Slovakia. | Do not count an Azure Slovakia region. Partner Azure services are not regions. |
| Google Cloud | https://cloud.google.com/about/locations and https://datacenters.google/locations | Official location pages reviewed on 2026-08-12 did not contain Slovakia. | Do not count a Google Cloud Slovakia region or Google-owned Slovak DC. |
| Oracle OCI | https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | Official region documentation reviewed on 2026-08-12 did not contain Slovakia. | Do not count OCI Slovakia unless Oracle adds it. |
| Tatra Supercompute / Tatra AI | https://www.tatrasupercompute.com/ and https://www.trade.gov/country-commercial-guides/slovakia-strategic-technologies | Project / policy lead for sovereign AI infrastructure; no verified site-level official evidence found. | Keep as B-grade planned lead. Route to Enviroportal, permits, land, grid, and strategic-investment records before counting. |

---

## 2. Operator and facility seed list

| Operator / asset | Best source | Grade | Location / status signal | How to use |
|---|---|---:|---|---|
| Slovak Telekom | https://www.telekom.sk/biznis/stredne-velke-firmy/datove-centra; https://wholesale.telekom.com/global-connectivity/our-solutions/sd-wan-enabling-transport/data-center-services | A for official service; B/C for address details unless primary page captured | Bratislava official service page says the DC is near Bratislava center; wholesale material says Telekom Slovakia operates DCs in Bratislava and Košice. | Confirm exact Bratislava address and Košice status through Telekom primary material, borough permits, ZSE/VSE, and cadastre. |
| Orange Slovensko TechPark | https://www.orange.sk/biznis/ict-specialne-riesenia/techpark; https://www.orange.sk/biznis/ict-specialne-riesenia/techpark/virtualne-datove-centrum | A | Official Orange page describes a data center with 1,026+ m2 total and 680 m2 customer halls; business menu includes housing and virtual data center. | Treat as Bratislava telecom_colocation / cloud-service anchor; verify Petržalka address and certification by permits / certifier. |
| SWAN | https://www.swan.sk/firmy/cloud-a-datove-centrum/datove-centrum/ | A for service | Official data-center service page; legal seat Landererova 12, Bratislava appears on SWAN contact/privacy pages. | Confirm physical DC site; search CRZ for SWAN public-sector hosting / cloud contracts. |
| VNET a.s. | https://www.vnet.sk/en/business/data/housing/ | A | Operator says it has 3 Bratislava data centers: DC Digitalis, SHC III, and Datapark 48. Datapark 48 is listed as coming soon. | Count DC Digitalis and SHC III as operational if inventory rules accept operator page; keep Datapark 48 planned until launch evidence. |
| DC Digitalis | https://www.dcdigitalis.sk/; https://www.dcdigitalis.sk/en/services/colocation/ | A | Bratislava ecological data center; VNET page gives Trnavska cesta 110/B and 1,000 m2 data halls. | Dedicated facility record; verify parcel / permits. |
| SITEL POP1 / POP2 / POPKE | https://www.sitel.sk/en/datacenter/ and https://www2.sitel.sk/sk/datacentrum/ | A | SITEL states it operates three data centers: POP1 Bratislava, POP2 Bratislava, POPKE Košice. | Strongest neutral-colocation multi-site seed. Confirm exact addresses; use PeeringDB only as support. |
| 1 Cloud Lab | https://www.1cloudlab.sk/ and https://www.1cloudlab.sk/en/ | A | Official page states Bratislava data center, colocation, and public cloud; operating since 2000. | Verify address / facility specs. |
| eServer | https://www.eserver.net/en/store/colocation; https://www.eserver.eu/about/ | A for service; C/B for Tier claim | eServer sells SK colocation in Bratislava and says it operates its own location in Digitalis data center. | Do not create a separate facility if it is a suite/customer location inside DC Digitalis. |
| WebSupport | https://www.websupport.sk/; https://www.websupport.sk/kontakt/ | B/C for facility | Official hosting brand and Bratislava office, but no captured physical data-center page with facility location. | Provider lead only; resolve actual hosting location before counting. |
| Datalan | https://www.datalan.sk/ | B for services / integrator lead | IT integrator with infrastructure services; no site-specific DC proof in this review. | Use for public-sector contract discovery only. |
| DICIT / DC providers via ITAS | https://itas.sk | C/B lead | Association membership or service profile may show DC design / operation skills. | Membership is not facility evidence. |
| SPP enterprise data center hosting NASES | https://mirri.gov.sk/aktuality/informatizacia/nases-presuva-datove-centrum-do-priestorov-spp/; https://www.spp.sk | A/B | MIRRI says NASES second DC would be located in SPP's Bratislava DC from end-2021. | Count as enterprise / government host only after contract/site validation; not commercial colo. |
| NASES / Government Cloud | https://sk.cloud; https://sk.cloud/en; https://mirri.gov.sk/sekcie/informatizacia/dokumenty/vladny-cloud/; https://www.nases.gov.sk | A | State cloud platform for public administration. | government_or_public_sector class; map constituent physical DCs via CRZ/MIRRI/NASES. |
| SAV / PERUN supercomputer | https://www.sav.sk/?doc=services-news&lang=sk&news_no=13312&source_no=20 | A | SAV says PERUN arrived at the Centre of Common Activities of SAV in Bratislava on 2025-12-18 for installation. | public_HPC_research class; not commercial colo. |
| NSCC / Košice supercomputer component | https://mirri.gov.sk/aktuality/digitalna-agenda/ministerstvo-investicii-regionalneho-rozvoja-a-informatizacie-sr-posilnuje-vyskumnu-infrastrukturu-slovenska-superpocitac-novej-generacie-bude-aj-v-kosiciach/; https://zive.aktuality.sk/clanok/klKPWVG/slovensko-bude-mat-dva-superpocitace-namiesto-jedneho-v-bratislave-aj-kosiciach-ake-budu-stroje-za-40-milionov-porovnanie/ | A for MIRRI project direction; B for press technical comparison | Košice planned HPC / national-supercomputer route. | Track procurement, site, permits, and installation before operational count. |
| Tatra Supercompute / Tatra AI | https://www.tatrasupercompute.com/; https://www.trade.gov/country-commercial-guides/slovakia-strategic-technologies; https://www.itapa.sk/20239-en/tatra-supercompute-ai-tovaren-v-srdci-europy-7-min/ | B | Project and policy lead for AI infrastructure, CEE brownfield / NVIDIA-partner claims, exact Slovak sites not verified. | Highest-priority watch item; no facility count until official site evidence. |
| Atos / Eviden Košice directory lead | datacenters.com / Baxtel / market directories | C | Košice legacy data-center entries appear in directories. | Verify with Eviden/Atos primary pages, permits, CRZ, and VSE before counting. |
| Packet Exchange Bratislava | https://packetexchange.eu/colocation/slovakia/bratislava-colocation/ | C/B | Vendor page claims Bratislava colocation but is not a local facility operator proof. | Verify host facility; likely reseller / remote-hands service. |

---

## 3. Industry discovery routes

### 3.1 Operators and providers

```text
"{operator}" "dátové centrum" "Bratislava"
"{operator}" "datacentrum" "Košice"
"{operator}" "housing" "Slovensko"
"{operator}" "serverhousing" "Bratislava"
"{operator}" "virtualne datove centrum"
"{operator}" "TIER 3" "Slovakia"
"{operator}" "ISO 27001" "dátové centrum"
"{operator}" "adresa" "dátové centrum"
"{operator}" "IČO" "dátové centrum"
```

### 3.2 Expansion / large project discovery

```text
"dátové centrum" "postaví" Slovensko
"datacentrum" "otvorí" Bratislava OR Košice
"AI továreň" Slovensko
"AI factory" Slovakia "Tatra Supercompute"
"Tatra AI" "dátové centrum"
"Slovakia" "data center" "MW"
"Slovakia" "hyperscale" "data center"
"superpočítač" "Košice" "MIRRI"
"PERUN" "superpočítač" "SAV"
```

### 3.3 Associations / IXPs / peering

| Route | URL | Use | Grade posture |
|---|---|---|---|
| NIX.SK | https://www.nix.sk and PeeringDB https://www.peeringdb.com/ix/299 | Bratislava neutral IX discovery; NIX.CZ annual report says NIX.SK has operated as a Bratislava peering node since 2015. | A for IXP existence, C/B for facility inference. |
| SIX | https://www.six.sk and https://www.six.sk/?lang=en | Slovak Internet eXchange operated by technical universities in Bratislava and Košice; contact shown at STU Bratislava. | A for IXP, not data center. |
| PeeringDB facilities | https://www.peeringdb.com/fac/465 and facility pages | Sitel Bratislava, Digitalis, STU, network lists. | C/B seed only. |
| ITAS | https://itas.sk | Slovak IT association and member discovery. | Association membership is not facility proof. |
| SAPIE | https://www.sapie.sk | Innovation economy / AI-policy leads. | B/C lead. |
| Košice IT Valley | https://www.kosiceitvalley.sk | Eastern-Slovakia tech-cluster lead source. | B/C lead. |

IXP / association queries:

```text
site:nix.sk "Bratislava" "datacentrum"
site:six.sk "Košice" OR "Bratislava"
site:peeringdb.com "Sitel Bratislava"
site:peeringdb.com "DIGITALIS Bratislava"
site:itas.sk "dátové centrum"
site:sapie.sk "AI" "dátové centrum"
site:kosiceitvalley.sk "dátové centrum" OR "superpočítač"
```

### 3.4 Press sources

Use press for leads, dates, project language, interviews, and technical details. Then confirm with official routes in `explorer-official.md`.

| Source | URL / route | Default grade |
|---|---|---:|
| Živé / Aktuality technology | https://zive.aktuality.sk | B |
| DSL.sk | https://www.dsl.sk | B |
| Nextech | https://www.nextech.sk | B |
| TouchIT | https://touchit.sk | B |
| Trend | https://www.trend.sk | B |
| Forbes Slovakia | https://www.forbes.sk | B |
| HNonline | https://hnonline.sk | B |
| Dennik N | https://dennikn.sk and https://e.dennikn.sk | B |
| ITAPA | https://www.itapa.sk | B for conference / speaker statements |
| Data Center Dynamics | https://www.datacenterdynamics.com | B |
| Capacity Media / Data Centre Magazine | site searches | B |
| US International Trade Administration | https://www.trade.gov/country-commercial-guides/slovakia-strategic-technologies | B for market / policy lead |

Press queries:

```text
site:zive.aktuality.sk "dátové centrum" Slovensko
site:zive.aktuality.sk "superpočítač" "Košice"
site:nextech.sk "dátové centrum" Bratislava
site:touchit.sk "dátové centrum" Slovensko
site:trend.sk "datacentrum" OR "dátové centrum"
site:forbes.sk "VNET" "dátové centrum"
site:hnonline.sk "dátové centrum" "Slovensko"
site:dennikn.sk "datacentrum" "NASES"
site:datacenterdynamics.com Slovakia "data center"
site:trade.gov Slovakia "data center" "Tatra Supercompute"
```

---

## 4. Per-division industry strategy

| Manifest division | Industry density | Primary leads | First queries | Confirmation route |
|---|---:|---|---|---|
| Bratislava | High | Slovak Telekom, Orange TechPark, SWAN, VNET DC Digitalis / SHC III / Datapark 48, SITEL POP1/POP2, 1 Cloud Lab, eServer-in-Digitalis, NASES/GovCloud, SPP, PERUN, NIX.SK/SIX, WebSupport lead | `Bratislava dátové centrum kolokácia`, `Orange TechPark dátové centrum`, `VNET SHC III`, `SITEL POP Bratislava`, `NASES SPP dátové centrum` | Operator page -> borough board -> ZSE -> cadastre -> CRZ/UVO for public-sector workloads. |
| Trnava | Low-mid / watch | Industrial enterprise IT, Stellantis supplier ecosystem, possible western-SK AI-factory lead | `Trnava datacentrum`, `Sereď dátové centrum`, `Tatra Supercompute Trnava`, `TTSK dátové centrum` | Press/project lead -> Enviroportal -> TTSK / municipal boards -> ZSE. |
| Trencin | Low | Hospitals, public administration, industrial IT | `Trenčín dátové centrum`, `Považská Bystrica serverovňa`, `TSK datacentrum` | Institution / press -> municipal boards -> UVO/CRZ -> ZSE/SSE. |
| Nitra | Low-mid / watch | Jaguar Land Rover / industrial IT, UKF / public-sector server rooms, possible western-SK AI-factory lead | `Nitra dátové centrum`, `Jaguar Land Rover Nitra serverovňa`, `NSK dátové centrum` | Company / procurement lead -> municipal / NSK board -> ZSE -> cadastre. |
| Presov | Low | PU Prešov, hospitals, regional public-sector IT | `Prešov dátové centrum`, `PU Prešov serverovňa`, `PSK datacentrum` | Institution page / tender -> PSK / municipal board -> VSE. |
| Banska Bystrica | Low | UMB, hospitals, regional state IT, Datalan branch/service leads | `Banská Bystrica dátové centrum`, `UMB serverovňa`, `BBSK cloud` | Institution / integrator lead -> BBSK / municipal board -> SSE -> CRZ. |
| Zilina | Low-mid / watch | UNIZA, Kia / suppliers, Martin hospital, possible future AI/HPC leads | `Žilina dátové centrum`, `Kia Žilina serverovňa`, `ŽSK dátové centrum` | Company / press -> ŽSK / municipal boards -> SSE. |
| Kosice | Medium | SITEL POPKE, NSCC / Košice supercomputer, TUKE, Košice IT Valley, US Steel enterprise IT, Atos/Eviden directory lead, possible Telekom Košice lead | `Košice dátové centrum`, `SITEL POPKE`, `Košice superpočítač`, `Telekom Košice data center` | Operator / MIRRI / press -> Košice boards -> KSK -> VSE -> cadastre. |

All 8 required divisions are covered. For low-density regions, absence of directory listings is not enough; run public-procurement and municipal-board sweeps because server-room projects rarely appear in commercial DC directories.

---

## 5. Directory and aggregator handling

| Directory / source | URL | Use | Caveat |
|---|---|---|---|
| DataCenterMap Slovakia / Bratislava | https://www.datacentermap.com/slovakia/ and https://www.datacentermap.com/slovakia/bratislava/ | Seed list for Bratislava operators and addresses such as Datacube, Perpetuus, DC Digitalis, SITEL. | C. It duplicates and may include old / reseller / PoP entries. |
| Baxtel Slovakia | https://baxtel.com/data-center/slovakia | Broad market list; surfaced entries such as Datacube, DC Digitalis, Perpetuus, Deutsche Telekom Košice / Tajov. | C unless corroborated. |
| datacenters.com Slovakia | https://www.datacenters.com/slovakia | Provider profiles and address leads. | C; sales directory. |
| Cloudscene / OCOLO / Inflect / colomap | site-specific searches | Peering / on-net / facility leads. | C/B only; useful for IXP and facility cross-reference, not final counts. |
| PeeringDB | https://www.peeringdb.com | Facility and IXP relationships such as Sitel Bratislava and Digitalis. | Network/facility listing is not permit or operator proof. |
| Uptime Institute | https://uptimeinstitute.com/tier-certification | Validate exact Tier certifications. | No Tier claim should be upgraded without matching record. |

Directory upgrade workflow:

1. Capture exact facility name, claimed address, operator, city, and capacity.
2. Search the operator domain for the exact name and address.
3. Search official-board / Enviroportal / CRZ / UVO / cadastre routes.
4. Search certifier records for Tier / ISO claims.
5. If no primary or strong secondary source appears, keep the entry at C and exclude it from facility totals.

---

## 6. Known traps and quality controls

- **Datacube / Perpetuus**: directories show these as major Bratislava assets, and old state-DC reporting references private DC Perpetuus in Devínska Nová Ves. Treat them as leads until current operator / official records are captured.
- **VNET three-site handling**: DC Digitalis and SHC III are operational on the VNET page; Datapark 48 is `coming soon`. Do not count Datapark 48 operational.
- **eServer**: eServer's own page places its own location in Digitalis. Treat it as a service / suite lead, not automatically a separate building.
- **Orange TechPark**: now has official Orange evidence. Still verify exact street address, permit, and any Uptime / Tier claim separately.
- **Telekom Košice**: do not elevate directory snippets to A. Capture a Slovak Telekom or permit source for the Košice physical site.
- **IXP presence**: NIX.SK, SIX, STU, Sitel, Digitalis and PeeringDB are excellent discovery routes, but peering presence alone is not a data center.
- **Hyperscalers**: no AWS/Azure/GCP/OCI Slovakia public region as of the reviewed official pages. Re-check quarterly.
- **Tatra Supercompute**: impressive announced capacity language remains B-grade until exact Slovak site(s), permit/EIA, land, grid, or strategic-investment records are found.

---

## 7. Re-check cadence

1. **Monthly**: press sweep for `dátové centrum`, `datacentrum`, `AI factory`, `Tatra Supercompute`, `Tatra AI`, `superpočítač`, `PERUN`, `Košice`.
2. **Quarterly**: AWS/Azure/GCP/OCI official location pages; NIX.SK/SIX/PeeringDB facility changes; Uptime certification search.
3. **Semi-annual**: DataCenterMap, Baxtel, datacenters.com, Cloudscene, OCOLO, colomap Slovakia refresh; de-duplicate against operator pages.
4. **Annual**: per-division reconciliation with `explorer-official.md`, including all 8 region/municipality sweeps and CRZ/UVO searches.

Priority unresolved leads:

```text
Tatra Supercompute / Tatra AI exact site(s), division(s), permits, EIA, grid
Telekom Košice primary facility evidence
Datacube / Perpetuus current operator and official status
VNET Datapark 48 launch / permit / address details
Orange TechPark exact address and certification record
SITEL POP1 / POP2 / POPKE exact address and permit/cadastre details
SWAN exact physical data-center site
WebSupport physical hosting location(s)
NSCC Košice machine installation site and operating status
```
