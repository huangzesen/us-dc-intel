# AL Explorer Official - Albania Datacenter Enumeration

Date: 2026-08-12. Country: **AL Albania**. Division model: **12 counties (qarqe) and 61 municipalities (bashki)**. Scope: official/regulatory methodology for finding commercial, telecom, government, education, cloud, colocation, disaster-recovery, AI/HPC, and large server-room facilities in Albania.

Reliability grades used in this file:

- **A** = primary public-sector or operator-owned proof: permit/planning decision, Official Gazette law/VKM, QKB business-register record, APP/e-procurement record, AKEP/ERE/OST/OSHEE/KESH record, AKSHI/RASH/ANIX official page, municipal record, or operator-owned facility page.
- **B** = strong but non-primary evidence: DCD, Globes, SeeNews, WBIF/EBRD/EU/ITU/Energy Community, PeeringDB, Submarine Networks, vendor case study, or local press with enough detail to follow up.
- **C** = weak lead: aggregator directory, marketplace page, LinkedIn/social page, reseller VPS location claim, job ad, investment-promotion text without a named facility, or unverified address/municipality inference.

Use the highest grade only for the fact actually supported. Example: Host.al's own colocation page is **A** for a marketed Tirana datacenter service, but a street address copied from PeeringDB/Data Center Map is **B/C** until QKB or a permit confirms it. The Albania Data Center/TEDA project is **B** until an Albanian permit, QKB subject record, APP/EBRD record, or grid-connection source is found.

---

## 0. Albania structure facts

- Albania has **no public national datacenter registry**. Enumeration must join planning/permit records, official business and procurement records, telecom and energy regulators, public IT sources, operator pages, interconnection records, and press.
- INSTAT's administrative classification page states that Albania is subdivided into **12 counties and 61 municipalities**: https://www.instat.gov.al/en/documentation/classifications/version/?verId=3488. Use county first, then municipality.
- Current counties: **Berat; Diber; Durres; Elbasan; Fier; Gjirokaster; Korce; Kukes; Lezhe; Shkoder; Tirane; Vlore**.
- Permitting is centralized through **E-Leja** on e-Albania but decision authority may be municipal or KKT/KKTU depending on project type. The Ministry page for E-Lejet e Ndertimit points applicants to e-Albania service code 6093: https://www.infrastruktura.gov.al/e-lejet-e-ndertimit/.
- The AKPT/territorial-planning portal has permit-procedure documentation and KKT decision pages: https://planifikimi.gov.al/index.php?id=procedura and https://planifikimi.gov.al/index.php?id=263.
- Legal framework: Law No. 107/2014 on territorial planning/development and VKM No. 408 dated 13.05.2015 on territorial development regulation. Use QBZ as the legal source of record (https://qbz.gov.al/) and planifikimi.gov.al PDFs as an access route when QBZ search is awkward.
- Market shape is **Tirana-centric**. Public data-center evidence clusters in Tirane county: Host.al, RASH/ANIX, AKSHI/government IT, ALBtelecom/One Albania leads, and the 2026 TEDA/ADC project lead.
- Data Center Map currently lists **5 Albania facilities, all in Tirana** (lead source only): https://www.datacentermap.com/albania/ and https://www.datacentermap.com/albania/tirana/.
- Official hyperscale cloud checks are negative as of this methodology date: no AWS, Microsoft Azure, Google Cloud, or Oracle OCI public cloud region is listed for Albania in the providers' official region/location pages. Re-check on every run.

---

## 1. Albanian and English search vocabulary

English terms:

```text
data center
data centre
datacenter
colocation
co-location
cloud
cloud region
server room
server farm
disaster recovery
business continuity
Tier III
Tier IV
Uptime
MW
MVA
substation
transformer
backup generator
IXP
submarine cable
landing station
free economic zone
industrial zone
```

Albanian terms and common no-diacritic variants:

```text
qender te dhenash
qendra e te dhenave
qender e te dhenave
qendra e te dhenave qeveritare
dhoma e servereve
qender serveresh
server
kolokacion
cloud
re
leje ndertimi
leje zhvillimi
leje shfrytezimi
aplikim per leje ndertimi
plan i pergjithshem vendor
PPV
plan i detajuar vendor
PDV
planifikim territori
zhvillim territori
Keshilli Kombetar i Territorit
KKT
KKTU
nenshtacion
nenstacion
lidhje me rrjetin
kerkese per lidhje
furnizim me energji elektrike
prokurim publik
tender
fletorja zyrtare
VKM
vendim i keshillit te ministrave
bashkia
qarku
njesi administrative
zona e lire ekonomike
zone ekonomike
zone industriale
kadaster
```

Use English for international press, cloud-provider pages, and data-center directories. Use Albanian for municipal, KKT/KKTU, ERE/OST/OSHEE, AKEP, APP, QKB, AKSHI, and local press searches.

---

## 2. Official permit, planning, legal, registry, and cadastre sources

### 2.1 Construction and development permits

Primary sources:

| Source | URL | Use | Grade |
|---|---|---|---|
| Ministry of Infrastructure and Energy - E-Lejet e Ndertimit | https://www.infrastruktura.gov.al/e-lejet-e-ndertimit/ | Confirms E-Leja workflow and e-Albania application route. | A for process |
| e-Albania E-Leja service | https://e-albania.al/ and service route `https://e-albania.al/sherbimi.aspx?kodi=6093` | Permit applications and authenticated service workflow. Public scraping may be blocked. | A when accessed |
| AKPT / planifikimi.gov.al procedure page | https://planifikimi.gov.al/index.php?id=procedura | Permit-documentation route for municipal and KKT/KKTU permits. | A |
| AKPT / KKT decisions | https://planifikimi.gov.al/index.php?id=263 | KKT/KKTU decisions for complex/national/strategic projects. | A |
| AZHT | https://azht.gov.al/ | Agency for Territory Development; use for development-permit guidance, KKT technical-secretariat context, notices. | A/B |
| Municipal portals | `tirana.al`, `durres.gov.al`, `bashkia<name>.gov.al` | Municipal permit notices, council decisions, PPV/PDV, service pages. | A for records |
| Porta Vendore | https://portavendore.al/ | Municipal service descriptions and routing; not facility proof. | B/A- |

Permit queries:

```text
site:planifikimi.gov.al "leje ndertimi" "data center"
site:planifikimi.gov.al "qendra e te dhenave"
site:planifikimi.gov.al "qendër e të dhënave"
site:planifikimi.gov.al "Kashar" "leje ndertimi"
site:planifikimi.gov.al "TEDA" "leje"
site:tirana.al "leje ndertimi" "data center"
site:tirana.al "qendra e te dhenave"
site:durres.gov.al "leje ndertimi" "server"
"{municipality}" "leje ndertimi" "qendra e te dhenave"
"{municipality}" "leje zhvillimi" "server"
"{operator}" "leje ndertimi" "Tirane"
"{operator}" "leje zhvillimi" "Kashar"
filetype:pdf "leje ndertimi" "qendra e te dhenave"
```

Extract: decision authority, decision number/date, applicant/developer, NIPT/NUIS, cadastral zone, parcel, address, municipality, county, building function, gross area, status, floor count, IT/electrical load, substation/feeder, generators/fuel, cooling, water, environmental conditions, and use-permit dates.

### 2.2 Legal and Official Gazette

Primary sources:

| Source | URL | Use | Grade |
|---|---|---|---|
| QBZ / Fletorja Zyrtare | https://qbz.gov.al/ | Laws, VKM/DCM decisions, official legal text. JavaScript search may require browser use. | A |
| Law No. 107/2014 | Use QBZ; English access copy at https://planifikimi.gov.al/index.php?eID=dumpFile&f=6004&t=f&token=8a49182e9a8fd4b738deb28f07e2a7d41f729f14 | Territorial planning and development. | A via QBZ/AKPT |
| VKM No. 408, 13.05.2015 | Use QBZ and AKPT/planifikimi PDFs | Territorial development regulation; permit rules. | A via QBZ/AKPT |
| Law No. 41/2024 amendments | https://planifikimi.gov.al/index.php?eID=dumpFile&f=7987&t=f&token=34ec9d8d32b2861471582e7632a6c8d45381c325 | Introduces/updates KKTU authority language in planning law. | A |

Legal queries:

```text
site:qbz.gov.al "107/2014" "planifikimin dhe zhvillimin e territorit"
site:qbz.gov.al "408" "13.5.2015" "Rregullores se Zhvillimit te Territorit"
site:qbz.gov.al "KKTU" "leje zhvillimi"
site:qbz.gov.al "Komunikimet Elektronike"
site:qbz.gov.al "qendra e te dhenave"
site:qbz.gov.al "data center"
```

Legal text sets authority and process. It is rarely direct facility evidence unless a law/VKM names a specific project, zone, concession, or strategic investment.

### 2.3 Business registry and cadastre

Primary sources:

| Source | URL | Use | Grade |
|---|---|---|---|
| QKB / National Business Center | https://qkb.gov.al/en/business-register/ | Search businesses by name or NIPT/NUIS; verify legal status, address, business details, owners where available. | A |
| QKB home | https://qkb.gov.al/en/home-3/ | Agency context and sector statistics. | A |
| ASHK / State Cadastre Agency | https://www.ashk.gov.al/ | Cadastre/property services and local directorates; parcel-level access may require authentication/payment. | A for registry |

Registry queries:

```text
site:qkb.gov.al "Albania Data Center"
site:qkb.gov.al "Alis Initiatives"
site:qkb.gov.al "Happy Technologies"
site:qkb.gov.al "DIT" "Albania"
site:qkb.gov.al "Host.al"
site:qkb.gov.al "Abissnet"
site:qkb.gov.al "Nisatel"
site:qkb.gov.al "ALBtelecom"
site:qkb.gov.al "One Albania"
"{operator}" "NIPT" Albania
"{operator}" "NUIS" Albania
site:ashk.gov.al "Kashar" "kadaster"
```

Use QKB to prevent name collisions. For ADC, search both the public project name and reported entities such as **Alis Initiatives**, **H.A.P.I. Advanced Technologies / Happy Technologies**, and **DIT**. Do not count a press-named SPV until a QKB record confirms the Albanian subject and address.

---

## 3. Energy, grid, and utility evidence

Primary sources:

| Source | URL | Use | Grade |
|---|---|---|---|
| ERE - Energy Regulatory Authority | https://ere.gov.al/en/ | Regulator, tariffs, licensed entities, board decisions, electricity/natural-gas legal context. | A |
| OST sh.a. | https://ost.al/ | Transmission grid, substations, connection rules, development plans. | A |
| OSHEE / OSSH | https://oshee.al/ | Distribution network and customer/business connection routes. | A |
| KESH sh.a. | https://www.kesh.al/en/ | Generation context, hydro fleet, energy-supply context. | A |
| Ministry of Infrastructure and Energy | https://www.infrastruktura.gov.al/ | Energy policy, major infrastructure, E-Leja links. | A |
| Energy Community | https://www.energy-community.org/ | Albania electricity-market reform and policy context. | A/B |
| EBRD OSHEE sustainability project | https://www.ebrd.com/content/dam/ebrd_dxp/documents/project/55236/oshee-sustainability-project-board-report.pdf | Distribution-sector financing/context; not a facility source. | B |

Energy queries:

```text
site:ere.gov.al "data center"
site:ere.gov.al "qendra e te dhenave"
site:ere.gov.al "Albania Data Center"
site:ost.al "data center"
site:ost.al "nenshtacion" "Kashar"
site:ost.al "nenstacion" "Tirane"
site:ost.al "Fier" "400" "220"
site:oshee.al "kerkese per lidhje"
site:oshee.al "Albania Data Center"
site:oshee.al "Host.al"
site:kesh.al "data center"
"{operator}" "OST" "MVA" Albania
"{operator}" "OSHEE" "MW" Albania
"{project}" "nenshtacion" "MW" "Shqiperi"
```

Extract: requested or contracted MW/MVA, voltage level, substation/feeder, transmission vs distribution connection, connection application/approval date, energization date, dedicated-substation claims, power-source claims, backup generation, and whether the figure is total utility capacity, critical IT load, or marketing capacity.

ADC handling: press claims a 32 MW first phase, possible 100 MW expansion, hydro supply, and a dedicated substation. Keep those as **B** until OST/OSHEE/ERE, permit, or operator/project documentation corroborates them.

---

## 4. Telecom regulator and connectivity evidence

### 4.1 AKEP

Primary sources:

| Source | URL | Use | Grade |
|---|---|---|---|
| AKEP | https://akep.al/ | Albanian electronic/postal communications regulator. | A |
| AKEP English about page | https://akep.al/en/about-akep/ | Confirms AKEP's role and report/publication routes. | A |
| AKEP publications/annual reports | https://akep.al/en/ | Operator identity, authorizations, market context. | A |

AKEP queries:

```text
site:akep.al "data center"
site:akep.al "qendra e te dhenave"
site:akep.al "kolokacion"
site:akep.al "regjistri" "operator"
site:akep.al "raport vjetor" "Abissnet"
site:akep.al "One Albania"
site:akep.al "ALBtelecom"
site:akep.al "Vodafone Albania"
site:akep.al "Nisatel"
site:akep.al ".al" "domain"
```

AKEP confirms operator/regulatory status and network context. It does not prove a data-center facility unless a publication names one.

### 4.2 Connectivity and IXP

Primary and strong secondary sources:

| Source | URL | Use | Grade |
|---|---|---|---|
| ANIX | https://www.anix.al/ | Official IXP page; states ANIX is hosted at RASH in a carrier-grade data center in central Tirana. | A for ANIX/RASH statement |
| ANIX alternate | https://anix.rash.al/ | Official RASH/ANIX page and member list. | A |
| PeeringDB facility 4508 | https://www.peeringdb.com/fac/4508 | RASH-ANIX facility, address Rruga e Durresit 219, Tirana, networks/exchange presence. | B |
| PeeringDB IX 2004 | https://www.peeringdb.com/ix/2004 | ANIX exchange, peers/capacity. | B |
| Submarine Networks - Italy-Albania | https://www.submarinenetworks.com/en/systems/intra-europe/italy-albania | Bari-Durres cable system context. | B/A- |
| Submarine Cable Map | https://www.submarinecablemap.com/ | Cable route and landing lead discovery. | B |

Connectivity queries:

```text
site:anix.al "data center" "Tirana"
site:anix.rash.al "data center"
site:peeringdb.com "RASH - ANIX"
site:peeringdb.com "Albanian Neutral Internet eXchange"
"Italy-Albania" "Durres" "submarine cable"
"Albania Crossing" "ALBtelecom" "Sparkle"
"Adria 1" "Albania" "submarine cable"
"Durres" "cable landing station"
```

RASH/ANIX can be counted as an interconnection/data-center facility only with scope clearly described: it is not evidence of a large commercial colocation campus by itself.

---

## 5. State IT and public procurement

### 5.1 AKSHI and government cloud

Primary/strong sources:

| Source | URL | Use | Grade |
|---|---|---|---|
| AKSHI | https://akshi.gov.al/ | National Agency for Information Society; state IT/e-government operator. May block automated access. | A when accessible |
| APP | https://app.gov.al/home/ | Public Procurement Agency. | A |
| APP e-procurement page | https://www.app.gov.al/e-procurement/ | Electronic procurement route. | A |
| Open Procurement Albania | https://openprocurement.al/en | Open-data procurement mirror. | A/B |
| Albanian Daily News cloud tender | https://albaniandailynews.com/news/govt-plans-eur-7m-for-cloud-infrastructure | March 2024 AKSHI centralized cloud-hardware tender lead. | B |
| SeeNews cloud tender | https://seenews.com/news/albania-opens-7-mln-euro-tender-for-govt-cloud-infrastructure-1246014 | Same tender lead. | B |
| GovNet Expansion project | https://aconium.eu/for-better-communication-in-the-healthcare-sector-albanias-govnet-expansion-project-launched/?lang=en | EU/WBIF GovNet expansion context. | B |

Queries:

```text
site:akshi.gov.al "data center"
site:akshi.gov.al "qendra e te dhenave"
site:akshi.gov.al "GOVnet"
site:akshi.gov.al "cloud"
site:app.gov.al "AKSHI" "server"
site:app.gov.al "AKSHI" "cloud"
site:app.gov.al "qendra e te dhenave"
site:eprocurement.app.gov.al "AKSHI" "server"
site:openprocurement.al "AKSHI" "server"
"AKSHI" "centralized hardware infrastructure" "cloud"
"AKSHI" "GOVnet" "data center"
"Qendra e te Dhenave Qeveritare" "Tirane"
```

Government tenders often identify equipment refreshes, cloud platforms, backup systems, or security upgrades. Count them as facility evidence only if they identify a physical data center/server room or an expansion of one.

---

## 6. Official cloud-region negative checks

Use official provider pages as negative controls. A provider region page is **A** for the logical region list, but it does not prove or disprove local private facilities.

| Provider | Official URL | Albania result to verify each run |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Albania public Region/Local Zone in checked list. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Albania public Azure region in checked list. |
| Google Cloud | https://cloud.google.com/about/locations and https://datacenters.google/locations | No Albania cloud region or Google-owned data-center country listing in checked pages. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Albania public cloud region in checked list. |

Queries:

```text
site:aws.amazon.com "Albania" "Local Zone"
site:learn.microsoft.com "Albania" "Azure" "region"
site:cloud.google.com "Albania" "cloud region"
site:oracle.com "Albania" "cloud region"
"Tirana" "cloud region" AWS Azure Google Oracle
```

If a public cloud later announces Albania, treat the announcement as a region signal and still look for permit/operator/power evidence before enumerating a physical facility.

---

## 7. Official/operator facility seed list

| Facility / lead | Location signal | Source URLs | Grade | Follow-up needed |
|---|---|---|---|---|
| Host.al Datacenter Albania HS1 | Tirana | https://host.al/colocation-datacenter-in-albania/?lang=en ; https://host.al/support/?lang=en | A for marketed colocation/datacenter service | QKB address, municipal permit, OSHEE power, AKEP/operator status. |
| RASH / ANIX carrier-grade data center | Central Tirana; PeeringDB gives Rruga e Durresit 219, Tirana 1001 | https://www.anix.al/ ; https://anix.rash.al/ ; https://www.peeringdb.com/fac/4508 | A for ANIX statement; B for PeeringDB details | Confirm facility scope: interconnection only vs colocation/compute. |
| AKSHI government data-center / government cloud leads | Tirana; public-sector infrastructure | https://akshi.gov.al/ ; APP/OpenProcurement; tender leads above | A for official procurement when found; B for press | APP tender IDs, exact facility address, scope, awardee, whether hardware-only. |
| Albania Data Center / ADC / TEDA project | TEDA free economic zone, Kashar, Tirane municipality | Globes, DCD, SeeNews, Albania Economia press URLs in industry file | B | QKB subject (possibly Alis Initiatives), KKT/KKTU/Tirana permit, OST/OSHEE grid connection, EBRD project page. |
| One Albania / ALBtelecom data-center lead | Aggregator address often `Autostrada Tirane-Durres Km 7, Kashar` | https://www.one.al/ ; AKEP; directories in industry file | C until operator/official facility source found | One Albania enterprise/cloud page, AKEP, QKB, permits, power. |
| Abissnet hosting/network lead | Tirana | https://www.abissnet.al/ ; AKEP; RIPE/PeeringDB | B/C until facility page found | Determine whether Abissnet operates countable colo/DC or only hosting/network services. |
| Nisatel hosting/network lead | Vlore registered-seat lead; facility not confirmed | https://nisatel.al/ ; AKEP/RIPE | C until physical facility found | QKB, AKEP, municipal permit, operator facility page. |

---

## 8. County-level official enumeration strategy

Use this workflow for every county: search official planning/permit routes, QKB, APP/e-procurement, AKEP, ERE/OST/OSHEE/KESH, AKSHI, municipal portals, and official county/municipal documents. Then reconcile any industry lead with a municipality.

Universal templates:

```text
"Qarku i {COUNTY}" "qendra e te dhenave"
"Qarku i {COUNTY}" "data center"
"{COUNTY}" "data center" Albania
"{municipality}" "qendra e te dhenave"
"{municipality}" "leje ndertimi" "server"
"{municipality}" "leje zhvillimi" "data"
"{municipality}" "prokurim publik" "server"
"{municipality}" "nenshtacion" "MW"
"{municipality}" "zone industriale" "data"
site:planifikimi.gov.al "{municipality}" "server"
site:app.gov.al "{municipality}" "server"
site:oshee.al "{municipality}" "lidhje"
```

### Berat county

Municipalities: Berat, Kucove, Polican, Skrapar, Ura Vajgurore.

Strategy: historic/industrial county; no verified data-center lead found in the checked sources. Prioritize municipal permit/procurement searches, Kucove industrial/energy leads, ASHK Berat parcel references, and public-sector server rooms.

```text
"Berat" "data center" OR "qendra e te dhenave"
"Kucove" "server" OR "qendra e te dhenave"
"Polican" "leje ndertimi" "server"
site:planifikimi.gov.al "Berat" "leje ndertimi" "server"
site:app.gov.al "Bashkia Berat" "server"
```

### Diber county

Municipalities: Bulqize, Diber, Klos, Mat.

Strategy: low expected yield; mining/energy and municipal IT are the main official routes. Watch for disaster-recovery/server-room procurements by municipalities or hospitals.

```text
"Diber" "data center" OR "qendra e te dhenave"
"Peshkopi" "server" "prokurim"
"Bulqize" "zone industriale" "data"
site:app.gov.al "Bashkia Diber" "server"
site:planifikimi.gov.al "Diber" "leje ndertimi" "server"
```

### Durres county

Municipalities: Durres, Kruje, Shijak.

Strategy: second-highest official priority after Tirane because of the Bari-Durres submarine cable, main port, Tirana-Durres corridor, and possible cable/power corridor projects. Check Durres municipal permits, KKT/KKTU coastal/port decisions, port-area procurement, and cable-landing evidence.

```text
site:durres.gov.al "leje ndertimi" "server"
site:durres.gov.al "qendra e te dhenave"
site:planifikimi.gov.al "Durres" "data center"
"Durres" "cable landing" "data center"
"Durres" "port" "data center"
"Kruje" OR "Shijak" "qendra e te dhenave"
```

### Elbasan county

Municipalities: Belsh, Cerrik, Elbasan, Gramsh, Librazhd, Peqin, Prrenjas.

Strategy: industrial/transport corridor. No confirmed data-center lead found; run industrial-zone, substation, and municipal procurement searches.

```text
"Elbasan" "data center" OR "qendra e te dhenave"
"Elbasan" "zone industriale" "server"
"Cerrik" OR "Librazhd" "server" "prokurim"
site:planifikimi.gov.al "Elbasan" "leje ndertimi" "server"
site:app.gov.al "Bashkia Elbasan" "server"
```

### Fier county

Municipalities: Divjake, Fier, Lushnje, Mallakaster, Patos, Roskovec.

Strategy: energy/industrial county with transmission infrastructure; no verified data-center lead found. Run power-heavy searches and distinguish industrial electrical projects from IT loads.

```text
"Fier" "data center" OR "qendra e te dhenave"
"Fier" "nenshtacion" "MW" "industrial"
"Patos" OR "Lushnje" "server" "prokurim"
site:ost.al "Fier" "nenshtacion"
site:app.gov.al "Bashkia Fier" "server"
```

### Gjirokaster county

Municipalities: Dropull, Gjirokaster, Kelcyre, Libohove, Memaliaj, Permet, Tepelene.

Strategy: expected negative for commercial DCs; focus on municipal/public-sector server rooms, border/utility projects, and any disaster-recovery procurement.

```text
"Gjirokaster" "data center" OR "qendra e te dhenave"
"Permet" OR "Tepelene" "server" "prokurim"
site:planifikimi.gov.al "Gjirokaster" "server"
site:app.gov.al "Bashkia Gjirokaster" "server"
```

### Korce county

Municipalities: Devoll, Kolonje, Korce, Maliq, Pogradec, Pustec.

Strategy: low confirmed yield; use Pogradec/Korce municipal portals and border/economic-development searches. Watch for municipal IT/server procurements.

```text
"Korce" "data center" OR "qendra e te dhenave"
"Pogradec" "data center" OR "server"
site:bashkiapogradec.gov.al "leje ndertimi"
site:app.gov.al "Bashkia Korce" "server"
```

### Kukes county

Municipalities: Has, Kukes, Tropoje.

Strategy: low expected yield; check border connectivity, public-sector IT, and energy/substation terms. Do not infer a facility from cross-border fibre alone.

```text
"Kukes" "data center" OR "qendra e te dhenave"
"Tropoje" OR "Has" "server" "prokurim"
site:planifikimi.gov.al "Kukes" "server"
site:app.gov.al "Bashkia Kukes" "server"
```

### Lezhe county

Municipalities: Kurbin, Lezhe, Mirdite.

Strategy: north-central corridor, port/logistics spillover, and industrial sites; no verified data-center lead. Kurbin has a municipal portal pattern useful for permits.

```text
"Lezhe" "data center" OR "qendra e te dhenave"
"Kurbin" "leje ndertimi" "server"
"Mirdite" "server" "prokurim"
site:bashkiakurbin.gov.al "leje ndertimi"
site:app.gov.al "Bashkia Lezhe" "server"
```

### Shkoder county

Municipalities: Fushe-Arrez, Malesi e Madhe, Puke, Shkoder, Vau i Dejes.

Strategy: northern hub and hydro corridor; no verified commercial DC lead. Search municipal permits, Vau i Dejes/KESH energy context, and public-sector server rooms.

```text
"Shkoder" "data center" OR "qendra e te dhenave"
"Vau i Dejes" "server" OR "nenshtacion"
site:bashkiamalesiemadhe.gov.al "leje ndertimi"
site:app.gov.al "Bashkia Shkoder" "server"
```

### Tirane county

Municipalities: Kamez, Kavaje, Rrogozhine, Tirane, Vore.

Strategy: highest priority. Confirm/resolve ADC/TEDA in Kashar, Host.al, RASH/ANIX, AKSHI, ALBtelecom/One Albania, Abissnet, Vodafone Albania, and any Data Center Map/PeeringDB/address leads. Tirana municipality includes the Kashar administrative unit, so do not misassign TEDA/Kashar to Durres just because it sits on the airport/port corridor.

```text
site:tirana.al "data center"
site:tirana.al "qendra e te dhenave"
site:planifikimi.gov.al "Kashar" "leje ndertimi"
site:planifikimi.gov.al "TEDA" "leje"
"TEDA" "Kashar" "data center" "leje ndertimi"
"Rruga e Durresit 219" "RASH" "ANIX"
"Tefta Tashko Koco" "Host.al"
"Autostrada Tirane-Durres Km 7" "ALBtelecom" "data center"
"Kamez" OR "Vore" OR "Kavaje" OR "Rrogozhine" "data center"
```

### Vlore county

Municipalities: Delvine, Finiq, Himare, Konispol, Sarande, Selenice, Vlore.

Strategy: third priority because of port/coastal connectivity and Nisatel's Vlore registered-seat lead. Treat Nisatel as a hosting/operator lead until a facility page, permit, QKB record, or power record confirms a physical data center.

```text
"Vlore" "data center" OR "qendra e te dhenave"
"Vlore" "Nisatel" "hosting"
"Sarande" "leje ndertimi" "server"
site:bashkiasarande.gov.al "leje ndertimi"
"Vlore" "port" "data center"
"Vlore" "subsea" OR "cable" "data"
```

---

## 9. Evidence rules and false positives

- **Do not promote press to A**: ADC/TEDA remains **B** until QKB, permit/KKTU, energy, APP/EBRD, or operator documentation verifies the facility.
- **Do not promote aggregators to A**: Data Center Map, datacenters.com, DataCenterJournal, Data Center Platform, Inflect, Baxtel, Cloudscene, ColoMap, and similar sites are lead sources unless independently corroborated.
- **Separate data centers from telecom nodes**: fibre POPs, mobile core sites, exchanges, and AKEP operator authorizations are not data centers unless there is compute/hosting/colocation/cloud/disaster-recovery evidence.
- **Separate public server rooms from commercial colocation**: APP/AKSHI equipment tenders may be valid public IT/server-room evidence but should be classified separately.
- **Capacity discipline**: MW/MVA values require a permit, energy record, operator spec, or strong technical source. Press capacity should stay in notes with grade.
- **Municipality discipline**: assign county/municipality from official address, cadastral zone, permit, QKB, or reliable map evidence. Generic `Tirana` or `Albania` is not enough for parcel-level certainty.
- **Cloud discipline**: local cloud products are facility leads, not cloud-region evidence. Official hyperscale region pages are the source of truth for public cloud regions.
- **Bot-blocked pages**: e-Albania and AKSHI may reject automated requests. Use a real browser session, cached snippets, or official procurement mirrors; never invent hidden URLs.

Minimum facility record:

```text
name:
operator_or_developer:
county:
municipality:
address_or_parcel:
status:
facility_type:
why_this_is_a_data_center:
source_urls:
source_grade:
evidence_date:
confirmed_fields:
unconfirmed_fields:
next_verification_steps:
```
