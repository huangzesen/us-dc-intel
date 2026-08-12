# SK Explorer Official - Slovakia Datacenter Enumeration from Permits, EIA, Grid, Telecom, Procurement, and State-IT Records

Date: 2026-08-12. Country: **SK Slovakia**. Division model: **8 self-governing regions / kraje**. Angle: **official, regulatory, permit, procurement, state-IT, grid, cadastral, and public-institution routes** for finding operational, planned, under-construction, public-sector, HPC, and enterprise data-center assets.

Reliability grades:
- **A** = primary / official evidence for the specific claim: ministry, municipality, self-governing region, Enviroportal EIA/SEA or IPKZ record, Slov-Lex law page, CRZ contract, UVO/IS EPVO notice, ORSR / Register UZ legal record, official operator facility page, official cloud-region list, official public institution page, or official grid / telecom-regulator source.
- **B** = strong secondary evidence: established Slovak or international press, government trade guide, vendor case study, investment-agency article, or operator announcement that does not itself identify a permit / exact facility / current operation.
- **C** = weak lead: directories, marketplace pages, maps, PeeringDB-only facility records, social posts, SEO pages, market reports, or capacity claims without primary support.

Grade discipline: grade the exact fact supported. An official operator page is A for that operator's service / named facility, but not automatically A for Uptime certification, MW, parcel, or construction permit unless that page or another primary record states those facts.

---

## 0. Slovakia-specific structural facts

- Slovakia has **8 self-governing regions** (`samospravne kraje`, also `VUC` / `kraje`) and **79 districts** (`okresy`). Statistics Slovakia and Slovakia.travel both describe the country with 8 regions and 79 districts.
- The required manifest divisions are complete: **Banska Bystrica; Bratislava; Kosice; Nitra; Presov; Trnava; Trencin; Zilina**.
- There is **no single national public building-permit registry** for all datacenter-relevant construction. Building permits and occupancy / commissioning decisions are usually on municipal or borough official boards (`uradna tabula`, `verejna vyhlaska`) and may be PDF-only or poorly indexed.
- Slovakia is landlocked. It has **no submarine cable landing stations**. Treat IXPs, terrestrial fibre routes, network PoPs, cloud edge nodes, and peering points as connectivity evidence only, not data centers.
- The commercial market is Bratislava-heavy. Košice is the secondary hub. Other regions are mostly public-sector, hospital, university, industrial, disaster-recovery, or enterprise server-room hunting territory unless a new large project is officially filed.
- Government and research facilities are real infrastructure but must be classified separately from commercial colocation: NASES / Government Cloud, SPP-hosted state DC capacity, SAV / PERUN, NSCC / Košice HPC.
- Hyperscaler absence must be re-checked on official provider pages each cycle. As of this review, AWS, Azure, Google Cloud, and Oracle OCI official location pages do not list a Slovakia public region or local zone.

Core Slovak vocabulary:

```text
datove centrum / dátové centrum
datacentrum / datacentra / data centrum
serverovna / serverovňa / serverove miestnosti
kolokacia / kolokácia / housing / serverhousing / colocation
cloud / cloudove sluzby / privátny cloud / vladny cloud
AI datove centrum / AI factory / superpocitac / superpočítač
technologicka budova / technologicky park / datova sala
uradna tabula / verejna vyhlaska / oznamenie o zacati konania
stavebne povolenie / rozhodnutie o stavebnom zamere / uzemne rozhodnutie
kolaudacne rozhodnutie / kolaudacia / skusobna prevadzka
posudzovanie vplyvov na zivotne prostredie / EIA / zistovacie konanie
integrovane povolenie / IPKZ / IPPC
pripojenie do elektrizacnej sustavy / rezervovany vykon / prikon
rozvodna / trafostanica / transformator / 110 kV / 400 kV / VVN
nahradny zdroj / zalozny zdroj / dieselagregat / UPS / generator
chladenie / free cooling / odpadove teplo / chladiaca jednotka
verejne obstaravanie / zmluva / vestnik / profil verejneho obstaravatela
```

Search both with and without diacritics. Facility documents may avoid `datove centrum` and instead describe a `technologicka budova`, `serverovna`, `strojovna chladenia`, `trafostanica`, `nahradny zdroj`, or `datova sala`.

---

## 1. Grade A official source routes

### 1.1 Administrative / notice-board route

Verified regional portals:

| Manifest division | Region / kraj | Seat | Regional portal | Main city / municipal portal |
|---|---|---|---|---|
| Bratislava | Bratislavsky samospravny kraj | Bratislava | https://bratislavskykraj.sk | https://www.bratislava.sk plus borough portals |
| Trnava | Trnavsky samospravny kraj | Trnava | https://www.trnavskykraj.sk | https://www.trnava.sk |
| Trencin | Trenciansky samospravny kraj | Trencin | https://www.tsk.sk | https://www.trencin.sk |
| Nitra | Nitriansky samospravny kraj | Nitra | https://www.unsk.sk | https://www.nitra.sk |
| Zilina | Zilinsky samospravny kraj | Zilina | https://www.zilinskykraj.sk | https://www.zilina.sk |
| Banska Bystrica | Banskobystricky samospravny kraj | Banska Bystrica | https://www.bbsk.sk | https://www.banskabystrica.sk |
| Presov | Presovsky samospravny kraj | Presov | https://www.psk.sk | https://www.presov.sk |
| Kosice | Kosicky samospravny kraj | Kosice | https://kosickykraj.sk | https://www.kosice.sk |

Use municipality and city-district boards first for permits. In Bratislava, search the borough as well as the city: Ružinov, Petržalka, Nové Mesto, Staré Mesto, Vajnory, Rača, Devínska Nová Ves, etc.

Building / official-board templates:

```text
site:{municipality-domain} "datove centrum" "stavebne povolenie"
site:{municipality-domain} "dátové centrum" "verejná vyhláška"
site:{municipality-domain} "datacentrum" "rozhodnutie o stavebnom zámere"
site:{municipality-domain} "serverovňa" "kolaudačné rozhodnutie"
site:{municipality-domain} "technologická budova" "trafostanica"
site:{borough-domain} "{operator}" "stavebné povolenie"
site:{borough-domain} "{address}" "kolaudácia"
filetype:pdf "dátové centrum" "Bratislava" "stavebné povolenie"
filetype:pdf "datacentrum" "Košice" "verejná vyhláška"
"{legal_entity}" "úradná tabuľa" "dátové centrum"
"{parcel}" "stavebné povolenie" "{municipality}"
```

Extract: applicant, legal entity / ICO, case number, parcel IDs, cadastral area, project name, permit type, authority, decision date, validity, appeals, building description, generators, fuel storage, transformer capacity, and whether it is only a server room inside another building.

### 1.2 EIA / SEA and IPKZ

Primary routes:

| Source | URL | Use |
|---|---|---|
| Enviroportal EIA/SEA | https://www.enviroportal.sk/eia-sea | EIA / SEA module and public project documents. |
| EIA information-system page | https://www.enviroportal.sk/eia-sea/informacny-system | Route to the central information system and public records. |
| Ministry EIA board | https://www.minzp.sk/uradna-tabula/eia/ | Ministry notice board; points users to Enviroportal EIA records. |
| Enviroportal IPKZ | https://www.enviroportal.sk/ipkz | Integrated pollution prevention and control route. |
| IPKZ register | https://www.enviroportal.sk/ipkz/register-prevadzok-a-povoleni | Register of IPKZ operations and permits. |

The old draft route `/sk/ippc` is stale; use `/ipkz` and `/ipkz/register-prevadzok-a-povoleni`.

EIA / IPKZ query templates:

```text
site:enviroportal.sk/eia-sea "dátové centrum"
site:enviroportal.sk/eia "dátové centrum"
site:enviroportal.sk "datacentrum" "zisťovacie konanie"
site:enviroportal.sk "serverovňa" "náhradný zdroj"
site:enviroportal.sk "technologická budova" "UPS"
site:enviroportal.sk "{operator}" "dátové centrum"
site:enviroportal.sk "{municipality}" "datacentrum"
site:enviroportal.sk/ipkz "{operator}"
site:enviroportal.sk/ipkz "integrované povolenie" "dieselagregát"
"okresný úrad" "{municipality}" "dátové centrum" "EIA"
```

For large AI / HPC / hyperscale leads, require an EIA, local permit, strategic-investment decision, land, or grid record before assigning `planned` above B. Generic zoning text that says `datacentrum` is a permitted land-use category is not a facility.

### 1.3 Legal basis

Use Slov-Lex static / current-law pages for act numbers and amendments:

| Topic | Primary law / route | URL |
|---|---|---|
| Construction | Act No. 25/2025 Coll., Building Act (`Stavebny zakon`), effective 2025-04-01 | https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2025/25/ |
| EIA | Act No. 24/2006 Coll. on environmental impact assessment | https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2006/24/ |
| IPKZ / IPPC | Act No. 39/2013 Coll. on integrated prevention and pollution control | https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2013/39/ |
| Energy | Act No. 251/2012 Coll. on energy | https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2012/251/ |
| Electronic communications | Act No. 452/2021 Coll. on electronic communications | https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2021/452/ |
| Personal data | Act No. 18/2018 Coll. on personal-data protection | https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2018/18/ |
| Cybersecurity | Act No. 69/2018 Coll. on cybersecurity | https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2018/69/ |
| Strategic investments | Act No. 142/2024 Coll. on extraordinary measures for strategic investments and TEN-T construction | https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2024/142/ |

The strategic-investment law can matter for large compute / datacenter campus projects, but a strategic-investment policy page is not facility evidence unless it names the investor, place, and project.

### 1.4 Company, contract, procurement, cadastre

| Route | URL | Use |
|---|---|---|
| Obchodny register SR | https://orsr.sk | Legal entity, registered seat, statutory body, historical names. |
| Register uctovnych zavierok | https://www.registeruz.sk | Financial statements, entity confirmation. |
| CRZ / Central Register of Contracts | https://www.crz.gov.sk and legacy landing https://www.zmluvy.gov.sk | State and public-sector contracts for DC, cloud, colocation, server rooms, Govnet. |
| UVO / public procurement | https://www.uvo.gov.sk/vestnik-a-registre and https://www.uvo.gov.sk/vestnik-a-registre/vestnik | Public procurement notices and buyer profiles. |
| IS EPVO / EVO order search | https://evo.isepvo.sk/evoportal/sk-sk/Public/OrderSearch/Index | Current official electronic-procurement search. |
| Cadastre / geodesy | https://www.skgeodesy.sk, https://www.katasterportal.sk, https://kataster.vugk.sk | Parcel, building, ownership, easement, address validation after a location is known. |

Procurement / entity templates:

```text
site:crz.gov.sk "dátové centrum" "{operator}"
site:crz.gov.sk "datacentrum" "NASES"
site:crz.gov.sk "housing" "server" "Bratislava"
site:crz.gov.sk "kolokácia" "server"
site:uvo.gov.sk "dátové centrum"
site:uvo.gov.sk "serverovňa"
site:evo.isepvo.sk "dátové centrum"
site:evo.isepvo.sk "kolokácia"
site:orsr.sk "{legal_entity}" "{ICO}"
site:registeruz.sk "{legal_entity}"
site:skgeodesy.sk "{address}" OR "{parcel}"
```

CRZ / UVO evidence is A for the purchase or contract. It is A for a physical facility only when the document identifies a site, host facility, or room.

### 1.5 Telecom, cloud, grid, and government IT

Primary routes:

| Topic | URL | Use |
|---|---|---|
| Telecom regulator | https://www.teleoff.gov.sk | Electronic-communications regulator; official route for telecom context. |
| MIRRI | https://mirri.gov.sk | Informatization, Government Cloud, HPC / digital-agenda project notices. |
| NASES | https://www.nases.gov.sk | State network and e-government operator. |
| Government Cloud | https://sk.cloud and https://sk.cloud/en | Official government-cloud service route. |
| Slovensko.sk | https://www.slovensko.sk | e-government service context. |
| URSO | https://www.urso.gov.sk | Energy regulator. |
| SEPS | https://www.seps.sk | Transmission system operator; development plans and connection context. |
| ZSE / VSE / SSE | https://www.zse.sk, https://www.vse.sk, https://www.sse.sk | Distribution areas and grid-context searches. |

Grid / telecom templates:

```text
site:urso.gov.sk "dátové centrum" OR "datacentrum"
site:seps.sk "dátové centrum" OR "rezervovaný výkon"
site:seps.sk "plán rozvoja prenosovej sústavy"
site:zse.sk "dátové centrum" "pripojenie"
site:vse.sk "dátové centrum" "pripojenie"
site:sse.sk "dátové centrum" "pripojenie"
"{operator}" "rezervovaný výkon" OR "požadovaný príkon"
"{municipality}" "rozvodňa" "dátové centrum"
site:teleoff.gov.sk "{operator}" "dátové centrum"
site:mirri.gov.sk "vládny cloud" "dátové centrum"
site:nases.gov.sk "dátové centrum" OR "Govnet"
```

Keep grid facts separate from facility status: `requested_connection_MW_or_MVA`, `connection_point`, `DSO`, `grid_status`, `permit_status`, `construction_status`, `operational_status`.

---

## 2. Officially verified facility / project anchors

These are not final inventory counts by themselves; they are high-value anchors for permit, contract, grid, and cadastre follow-up.

| Facility / project | Division | Status | Grade | Verified official / primary source | Enumeration action |
|---|---|---|---:|---|---|
| Slovak Telekom data center service | Bratislava; possible Kosice lead from wholesale material | Operational service | A for service; B/C for individual address until primary address proof | https://www.telekom.sk/biznis/stredne-velke-firmy/datove-centra; https://wholesale.telekom.com/global-connectivity/our-solutions/sd-wan-enabling-transport/data-center-services | Search Slovak Telekom legal entity, Bratislava / Kosice permits, ZSE/VSE, CRZ. Do not count Košice solely from third-party directories. |
| Orange Slovensko TechPark data center | Bratislava | Operational service | A for official facility/service; certification/location details need separate proof | https://www.orange.sk/biznis/ict-specialne-riesenia/techpark; https://www.orange.sk/biznis/ict-specialne-riesenia/techpark/virtualne-datove-centrum | Search Petrzalka / Bratislava permits, Orange Slovensko ICO, ZSE, Uptime certificates. |
| SWAN data center | Bratislava | Operational service | A for official service; address not proven on service page | https://www.swan.sk/firmy/cloud-a-datove-centrum/datove-centrum/ | Search SWAN, Landererova HQ, city/borough permits, CRZ hosting contracts. |
| VNET DC Digitalis | Bratislava | Operational | A | https://www.vnet.sk/en/business/data/housing/; https://www.dcdigitalis.sk/ | VNET page names DC Digitalis at Trnavska cesta 110/B and lists 1,000 m2 data halls. Confirm cadastral parcel and permits. |
| VNET SHC III | Bratislava | Operational | A | https://www.vnet.sk/en/business/data/housing/ | VNET page names SHC III at Namestie hraniciarov, Bratislava; confirm exact street number / parcel. |
| VNET Datapark 48 | Bratislava | Coming soon / planned | A for operator listing; not operational | https://www.vnet.sk/en/business/data/housing/ | Search Cernysevskeho / Petrzalka permits and grid; do not count operational until launch evidence. |
| SITEL POP1 / POP2 | Bratislava | Operational | A | https://www.sitel.sk/en/datacenter/ and https://www2.sitel.sk/sk/datacentrum/ | SITEL says it operates POP1 and POP2 in Bratislava. Confirm addresses / permits; PeeringDB fac 465 is C/B support only. |
| SITEL POPKE | Kosice | Operational | A | https://www.sitel.sk/en/datacenter/ and https://www2.sitel.sk/sk/datacentrum/ | Only confirmed Košice commercial-colocation anchor; confirm address / permits via Košice boards and VSE. |
| 1 Cloud Lab data center | Bratislava | Operational | A for official service | https://www.1cloudlab.sk/ and https://www.1cloudlab.sk/en/ | Page states Bratislava data center and colocation / public-cloud services; verify address and specs. |
| eServer colocation in Bratislava | Bratislava | Operational service | A for service; C/B for Tier claim | https://www.eserver.net/en/store/colocation; https://www.eserver.eu/about/ | eServer says SK colocation is in a Bratislava TIER3 ECO DC and that it operates its own location in Digitalis; do not treat as separate facility unless site evidence proves it. |
| NASES / Government Cloud | Bratislava / state estate | Operational government cloud | A | https://sk.cloud; https://sk.cloud/en; https://mirri.gov.sk/sekcie/informatizacia/dokumenty/vladny-cloud/; https://www.nases.gov.sk | Count as government/public-sector infrastructure, not commercial colo. |
| NASES second DC in SPP premises | Bratislava | Operational / migration completed after 2021 target unless later contrary evidence | A/B: official MIRRI for move, CRZ needed for contract details | https://mirri.gov.sk/aktuality/informatizacia/nases-presuva-datove-centrum-do-priestorov-spp/ | MIRRI says the second NASES DC would be in SPP's Bratislava DC from end-2021. Find CRZ contract and SPP site details. |
| PERUN supercomputer at SAV / CSČ SAV | Bratislava | Installed / operational-testing-to-operational HPC | A | https://www.sav.sk/?doc=services-news&lang=sk&news_no=13312&source_no=20 | SAV says PERUN was delivered on 2025-12-18 to the Centre of Common Activities of SAV in Bratislava. Classify as public_HPC_research. |
| National supercomputer in Kosice | Kosice | Planned / project route | A for MIRRI decision direction; B for technical comparison press | https://mirri.gov.sk/aktuality/digitalna-agenda/ministerstvo-investicii-regionalneho-rozvoja-a-informatizacie-sr-posilnuje-vyskumnu-infrastrukturu-slovenska-superpocitac-novej-generacie-bude-aj-v-kosiciach/ | Track procurement, installation location, municipal permit, VSE/grid. |
| Tatra Supercompute / Tatra AI | Western Slovakia, exact division not public | Planned lead | B | https://www.tatrasupercompute.com/; https://www.trade.gov/country-commercial-guides/slovakia-strategic-technologies | Official project and US trade-guide lead, but no verified division / parcel / permit / EIA found. Keep out of counts until primary site evidence appears. |

---

## 3. Per-division official strategy

| Manifest division | DSO / grid area | Priority localities | Official-first workflow | Current count posture |
|---|---|---|---|---|
| Bratislava | ZSE | Bratislava boroughs: Ružinov, Petržalka, Nové Mesto, Staré Mesto, Vajnory, Devínska Nová Ves; Pezinok / Senec corridor | Start with operator names + borough boards, then Enviroportal, CRZ/UVO, ZSE, cadastre. Check NASES/SPP and SAV separately. | Highest density: Telekom, Orange TechPark, SWAN, VNET, SITEL, 1 Cloud Lab, eServer-in-Digitalis, NASES/GovCloud, SPP, PERUN. Deduplicate carefully. |
| Trnava | ZSE | Trnava, Sereď, Galanta, Hlohovec, D1 / industrial parks | Search municipal boards and TTSK board for `datacentrum`, `technologicka budova`, `serverovna`, Tatra Supercompute, industrial users. | No verified commercial colo anchor in this review. Watch Tatra / industrial DR leads. |
| Trencin | ZSE / SSE edge | Trenčín, Považská Bystrica, Púchov, Nové Mesto nad Váhom | Municipal / TSK board, UVO/CRZ for hospitals and public bodies, SSE/ZSE grid context. | Low-density; expect enterprise and public-sector server rooms. |
| Nitra | ZSE | Nitra, Levice, Šaľa, Topoľčany, industrial parks | Municipal / NSK board, Jaguar Land Rover / suppliers as enterprise leads, UVO/CRZ, ZSE. | No verified commercial colo anchor. Treat automotive IT as enterprise leads only. |
| Presov | VSE | Prešov, Poprad, Humenné, Bardejov, Svidník | PSK / municipal boards, hospitals/university tenders, VSE. | Low-density; public-sector server rooms likely. |
| Banska Bystrica | SSE | Banská Bystrica, Zvolen, Lučenec, Brezno | BBSK / municipal boards, UMB / hospital procurement, SSE. | Low-density; no verified commercial colo anchor. |
| Zilina | SSE | Žilina, Martin, Ružomberok, Teplička nad Váhom | ŽSK / municipal boards, UNIZA / hospitals / Kia enterprise IT, SSE. | Low-density; enterprise and university leads only unless official filings appear. |
| Kosice | VSE | Košice boroughs, Šaca, Košice-okolie | SITEL POPKE first; then city / borough boards, KSK, MIRRI/NSCC, TUKE / hospital tenders, VSE, cadastre. | Secondary hub: SITEL POPKE confirmed; NSCC / supercomputer planned; Telekom Košice remains a lead needing primary facility proof. |

---

## 4. Counting and status rules

Count only facilities that have enough evidence for a physical computing / colocation / government / HPC site.

- **Operational**: current official operator facility page tied to Slovakia, official public-institution page, occupancy / commissioning decision, current procurement/contract naming an operating host site, or current service page with physical facility details.
- **Under construction**: building permit or official construction-start notice tied to a named project and place.
- **Planned**: official announcement plus at least one site-level primary indicator: EIA, permit, strategic-investment decision, land / parcel, grid request, public procurement, or municipality document.
- **Lead**: press, project-site claim, investment promotion, zoning land-use, grid-interest, directory, or PeeringDB record without enough site evidence.
- **Do not count**: AWS/Azure/GCP/OCI sales presence, CDN/cache nodes, exchange ports, internet exchanges, terrestrial fibre routes, network PoPs, software offices, retail offices, and generic cloud service pages without a facility tie.

Recommended fields:

```text
country_code, division, kraj_name, okres, municipality, city_district,
facility_name, operator, operator_legal_entity, ICO,
address, parcel_ids, facility_type,
status, status_date, evidence_grade,
permit_case_id, eia_case_id, ipkz_case_id,
requested_connection_MW_or_MVA, transformer_or_generator_capacity,
connection_point_or_DSO, cooling_notes, source_urls, notes
```

Facility type values:

```text
commercial_colocation
telecom_colocation
cloud_provider_datacentre_or_local_zone
enterprise_corporate
government_or_public_sector
public_HPC_research
network_pop_or_exchange_only
lead_unconfirmed
```

---

## 5. High-risk traps

- **Directory inflation**: DataCenterMap, Baxtel, Cloudscene, datacenters.com, colomap, Inflect, and PeeringDB repeat and mix facilities, suites, PoPs, and old brands. Use them as C-grade seed lists.
- **Tier claims**: `Tier 3`, `TIER3 ECO`, `Tier III quality`, and `Tier 3+` on operator pages are self-claims unless Uptime Institute or another named certifier record confirms the exact facility.
- **VNET / eServer duplication**: eServer states it operates its own location in Digitalis; do not count it as a separate building unless primary evidence proves a separate facility.
- **VNET Datapark 48**: operator-listed as coming soon, not operational on the reviewed page.
- **Telekom Košice**: wholesale / directory evidence suggests a Košice data center, but primary Slovak Telekom facility evidence must be captured before counting it as an A-grade facility.
- **Tatra Supercompute**: strong policy / project lead, but no verified EIA, permit, grid, parcel, or exact division found in this review. Keep as `lead_unconfirmed` or `planned_lead` until official site evidence appears.
- **State cloud**: NASES / Government Cloud and SPP-hosted state capacity are not commercial colocation inventory.

---

## 6. Re-check cadence

1. **Monthly**: Tatra Supercompute / Tatra AI, MIRRI, SARIO, Economy Ministry strategic-investment notices, Enviroportal EIA searches, and Slovak tech/business press.
2. **Quarterly**: AWS, Azure, Google Cloud, and Oracle official location pages; NIX.SK / SIX / PeeringDB facility changes; Uptime certification search.
3. **Semi-annual**: all 8 regional + priority municipal official-board sweeps; CRZ/UVO/IS EPVO searches for `dátové centrum`, `datacentrum`, `serverovňa`, `housing`, `kolokácia`, `vládny cloud`.
4. **Annual**: cadastral validation for all counted addresses; grid context for high-load sites; deduplication of directories against primary sources.
