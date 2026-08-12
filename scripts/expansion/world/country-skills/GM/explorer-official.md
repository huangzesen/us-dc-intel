# GM Explorer Official - Gambia Datacenter Enumeration via Regulators, Government Cloud, Power, Procurement, and Councils

Layer: **FINAL**. Date: 2026-08-12. Country: **GM - The Gambia**. Division model from `world-manifest.jsonl`: **6 city/divisions**: Banjul; Lower River; Central River; North Bank; Upper River; Western. Angle: **official/regulatory-first datacenter discovery**. Use industry and press sources only as leads unless they are operator-owned pages.

Reliability grades are field-level:
- **A** = primary source for the exact field: government/regulator/operator page, MOCDE/GICTA document, GPPA tender, NAWEC record, PURA licence/regulation, GIEPA document, council/building record, official cloud-region page, World Bank/MOCDE WARDIP document.
- **B** = strong named secondary source: The Standard, The Point, Foroyaa, GRTS, GambiaJ, Biometric Update, ITWeb Africa, Developing Telecoms, Connecting Africa, Capacity, Techpoint Africa, DCD, Cloudflare/Internet Society analysis, PeeringDB/IXP page for network presence.
- **C** = lead only: directory entry, social post, generic market report, unsupported address/capacity claim, MoU with no site/power/permit evidence, reseller/cloud-partner claim.

Do not count a datacenter from a law, licence class, fibre route, IXP, cloud resale page, tower-colocation offer, or MoU alone. Count only where a named operator or public body is tied to a physical facility or data-centre service. Keep status values separate: `operational`, `under construction`, `approved`, `planned`, `MoU/intent`, `lead only`.

---

## 0. Official Facts That Shape Enumeration

- The Gambia has **no public national datacenter register** and no central online planning-permit database. Build records by joining MOCDE/GICTA e-government evidence, PURA ICT licensing, NAWEC power evidence, GPPA tenders, GIEPA investment materials, WARDIP documents, council records, and operator pages.
- Use exactly these six divisions: **Banjul**, **Lower River**, **Central River**, **North Bank**, **Upper River**, **Western**. Normalise `Western Region`, `West Coast Region`, `WCR`, `Kanifing`, `Serekunda`, `Abuko`, `Bakau`, `Brikama`, and `Yundum` to **Western** unless a source explicitly places the site in Banjul city/division.
- The Greater Banjul Area straddles **Banjul** and **Western**. Do not collapse the two divisions. Banjul contains the capital and government/telco HQ surfaces; Western contains the main urban belt including Kanifing/Serekunda, Abuko, Bakau, Brikama, and Yundum.
- Confirmed countable or near-countable official seeds as of this review:
  - **Gambia National Data Centre, Abuko, Western**. Strong press and vendor reporting say President Barrow inaugurated the National Data Centre in Abuko with the National Identity Management System on 2026-07-01. Grade **B** for inauguration/facility existence until an official GICTA/MOCDE/State House page is opened; grade **A** only for any fields later confirmed on an official source. `ISO-certified` remains **B/C** unless a certificate or accredited certification entry is produced.
  - **GAMTEL co-location/facility rental services**. GAMTEL's own page says customers can rent space to co-locate telecom hardware or servers in any of GAMTEL's 43 sites or towers countrywide. Grade **A** for the service offering. Do **not** multiply this into 43 datacenters; a named exchange/tower remains a facility lead until it has site-level evidence.
  - **WARDIP / DTFA**. MOCDE and World Bank documents for P176932 cover second-cable, landing-station, and data-infrastructure works, including construction/upgrading of GAMTEL facilities and data centers across the country. Grade **A** for program scope; per-site records need tender, permit, power, or operator evidence before being counted.
  - **SIXP / Serekunda Internet Exchange Point, Western**. PeeringDB and AfPIF evidence place the national IXP in Serekunda. This is network-presence evidence, not datacenter proof.
- Power is a gating filter. **NAWEC** is the state utility for electricity/water/sewerage; record grid connection, substation, connected load, backup generators, UPS, fuel storage, solar/captive power, and outage exposure for every operational claim.
- Regulatory architecture: **PURA** regulates communications and other public utilities under the PURA Act framework. PURA pages show four mobile operators, one fixed-line operator, and four licensed ISPs. No standalone public `data centre licence` class was found in this review; facility evidence is likely embedded in telecom/ISP/gateway records.
- Data-localisation/demand evidence is not facility proof. The MOCDE G-Cloud strategy is an official demand signal. The National Assembly bill tracker now lists **DATA PROTECTION AND PRIVACY BILL, 2024** as **Assented** and last updated 2026-07-15; use that official wording unless a gazetted Act text is opened.
- Official public-cloud-region status checked against provider region pages/searches in this review: **no AWS, Azure, Google Cloud, Oracle OCI, or Huawei Cloud public region is listed in The Gambia**. Treat Gambia cloud-region claims as local/hybrid/edge evidence unless official provider pages change.

Primary URLs verified or usable:
- MOCDE: https://mocde.gov.gm/ ; WARDIP page: https://mocde.gov.gm/wardip/ ; G-Cloud Strategy: https://mocde.gov.gm/wp-content/uploads/2023/11/Gambia-G-Cloud-Strategy-document_Final-Draft.pdf ; Open Data Strategy: https://mocde.gov.gm/wp-content/uploads/2023/10/Final-Government-Open-Data-Strategy-2023-2026.pdf ; WARDIP ESMF: https://mocde.gov.gm/wp-content/uploads/2023/11/Environment-and-Social-Management-Framework-ESMF-%E2%80%93-WARDIP-P176932-The-Gambia.pdf
- GICTA/government directory: https://gambia.gov.gm/gambia-ict-agency/ ; https://gambia.gov.gm/government-directory/
- PURA: https://pura.gm/ ; overview: https://pura.gm/ict/overview/ ; MNOs: https://pura.gm/ict/sub-sectors/mobile-network-operators/ ; fixed line: https://pura.gm/ict/sub-sectors/fixed-line-operator/ ; ISPs: https://pura.gm/ict/sub-sectors/internet-service-providers/
- NAWEC/government page: https://nawec.gm/ ; https://gambia.gov.gm/gambia-app/national-water-and-electricity-corporation-nawec/
- GIEPA: https://www.giepa.gm/ ; media/resources page with Data Centre profile: https://www.giepa.gm/media-and-resources
- GPPA/government tenders: https://www.gppa.gm/ ; https://gppportal.gppa.gm/ ; https://gambia.gov.gm/tenders/
- GAMTEL: https://gamtel.gm/ ; co-location page: https://gamtel.gm/co-location-facility-rental-services/ ; about: https://gamtel.gm/about-us/
- National Assembly bill tracker: https://assembly.gm/bills ; documents: https://assembly.gm/documents
- World Bank WARDIP: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099061825055573661 ; ESMF PDF surfaced by search: https://documents1.worldbank.org/curated/en/099110923121020104/pdf/P1769320b3a0980140827505e38b648bd1d.pdf
- SIXP/network: https://www.peeringdb.com/ix/2682 ; https://www.peeringdb.com/fac/2287 ; AfPIF paper: https://www.afpif.org/wp-content/uploads/2017/10/Gambia-IXP-Experience-.pdf
- Cloud region pages: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; https://learn.microsoft.com/en-us/azure/reliability/regions-list ; https://cloud.google.com/about/locations ; https://www.oracle.com/cloud/public-cloud-regions/ ; https://www.huaweicloud.com/intl/en-us/

---

## 1. MOCDE, GICTA, and Government Cloud

MOCDE is the policy owner; **GICTA** is the operational ICT agency. Use this trail first for sovereign systems, G-Cloud, NIMS, and public data-centre infrastructure.

Verify:
- National Data Centre, Abuko: official ownership, commissioning wording, hosted systems, operator/agency, physical location, tier/ISO claims, and power/facility characteristics.
- G-Cloud and data classification: which government systems must be hosted domestically and what exceptions allow external hosting.
- WARDIP and other digital-infrastructure programs: data-centre, landing-station, backbone, and government-cloud scopes.
- PPP/vendor roles: Ministry of Interior, GICTA, Margins ID Group, Presight or other integrators. MoUs remain `MoU/intent` unless a site/procurement/commissioning record exists.

Query templates:
```text
site:gicta.gov.gm "data centre" OR "data center" OR "NIMS" OR "national data centre"
site:mocde.gov.gm "data centre" OR "data center" OR "G-Cloud" OR "cloud"
site:gambia.gov.gm "GICTA" "data centre" OR "National Identity Management System"
"Gambia National Data Centre" Abuko GICTA
"National Identity Management System" Gambia "data centre" Margins
"G-Cloud" "Gambia" "data classification"
"Presight" Gambia "digital ID" OR "data centre"
```

Extraction fields: agency, facility name, operator, division, town/site/address, hosted systems, status wording, PPP/vendor role, certification/tier wording, source URL, source date, field grade.

---

## 2. PURA - ICT Licensing and Telecom Regulation

PURA is the A-grade source for licensed telecom and ISP market structure. Its public pages confirm: four GSM/mobile operators, four ISPs, and one fixed-line service provider; GAMTEL is the only fixed/wireless line operator. Licences and services are leads, not facility records.

Use PURA to verify:
- Legal operator names and public licence/service classes: GAMCEL, AFRICELL, COMIUM, QCELL, GAMTEL, and licensed ISPs.
- Whether an operator has gateway, fixed wireless, hosting, or internet/data services that could explain a facility lead.
- Enforcement, QoS, spectrum, mast/tower, or tariff records that identify sites.

Query templates:
```text
site:pura.gm "data centre" OR "data center" OR "colocation" OR "co-location"
site:pura.gm "GAMTEL" "fixed" OR "gateway" OR "licence"
site:pura.gm "Internet Service Providers" "web hosting"
site:pura.gm "Africell" OR "QCell" OR "Comium" OR "Gamcel"
site:pura.gm "energy" "tariff" OR "generator" OR "substation"
"{operator}" "PURA" "licence" Gambia
```

Extraction fields: licence holder, licence/service class, issue/renewal date if available, authorised services, town/division if stated, facility mention if any, source URL, grade.

---

## 3. NAWEC - Power Trail

NAWEC evidence should decide whether an operational datacenter claim is plausible. The public trail may be sparse; still record every facility's power fields as `unknown` until sourced.

Query templates:
```text
site:nawec.gm "data centre" OR "data center" OR "server" OR "ICT"
site:nawec.gm "{operator}" "connection" OR "substation" OR "MVA" OR "kV"
site:nawec.gm "generator" OR "backup" OR "solar" OR "power purchase"
"NAWEC" "data centre" Gambia
"{facility}" "generator" OR "UPS" OR "fuel" Gambia
"{facility}" "NAWEC" "power" Gambia
```

Preserve units exactly. Do not convert MVA to MW/IT load unless a source does. Capture backup generators, UPS, fuel storage, solar/captive power, outage exposure, grid connection, and any power-sale or tariff record.

---

## 4. GPPA, GIEPA, and World Bank Procurement

**GPPA** and the government tenders page are the official procurement surfaces. **GIEPA** is useful for investment-promotion and incentive evidence; its Data Centre sector profile is not facility proof.

Query templates:
```text
site:gppa.gm "data centre" OR "data center" OR "ICT infrastructure" OR "landing station"
site:gppportal.gppa.gm "data centre" OR "WARDIP" OR "landing station"
site:gambia.gov.gm/tenders "WARDIP" OR "data centre" OR "ICT"
site:giepa.gm "data centre" OR "data center" OR "ICT"
"WARDIP" Gambia "data centre" contract OR award
"GIEPA" "data centre" Gambia
```

Extract: tender/contract reference, procuring entity, scope, location, award date, contractor, value, source URL, and grade. Treat `tenders.gm` and other aggregators as C unless they reproduce an official tender with a verifiable source.

---

## 5. Submarine Cable, Landing Station, and IXP Trail

Connectivity evidence is necessary context, but it is not datacenter proof.

- ACE cable landing in/near Banjul and GAMTEL's role are connectivity anchors. Use cable and outage reports to understand resilience and likely landing-station sites.
- WARDIP second-cable and new landing-station works are official program evidence. Count a landing-station/data-centre facility only when a specific site, tender, construction record, or operator statement exists.
- SIXP/Serekunda IXP and PeeringDB records identify network concentration in Western division. PeeringDB facility entries are B/C leads for location/network presence; confirm with operator/council/PURA records before counting as a datacenter.

Query templates:
```text
"ACE" "Gambia" "landing station" OR "landing point" Banjul GAMTEL
"WARDIP" Gambia "second submarine cable" OR "landing station"
"Serekunda Internet Exchange" OR "SIXP" Gambia
site:peeringdb.com Gambia Serekunda Banjul
"Gambia" "internet outage" ACE 2022 Cloudflare Internet Society
```

---

## 6. Councils and Local Government

Online council planning records are limited. Use council websites where available, Ministry of Lands/local-government sources, official notices, and local press for land allocations, building permits, and completion/occupancy evidence.

Query templates:
```text
"Banjul City Council" "data centre" OR "server" OR "building permit"
"Kanifing Municipal Council" "data centre" OR "server" OR "building permit"
"Brikama Area Council" "{operator}" OR "ICT" OR "server"
"Mansakonko Area Council" "ICT" OR "server"
"Kerewan Area Council" "ICT" OR "server"
"Basse Area Council" "ICT" OR "server"
"{council}" "land" "{operator}" Gambia
```

Extract: applicant, plot/site, ward/town, land-use category, permit/application number, decision date, conditions, completion/occupancy evidence, source type, grade.

---

## 7. Official Cloud-Region Status

| Provider | Official source | Gambia status | Enumeration rule |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Gambia public Region found | Reseller, edge, or Direct Connect claims are not region evidence |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Gambia public Azure region found | Azure Stack/local partner claims are local/hybrid only |
| Google Cloud | https://cloud.google.com/about/locations | No Gambia cloud region found | CDN/cache evidence is network/edge only |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Gambia public region found | Recheck official page before accepting any OCI Gambia claim |
| Huawei Cloud | https://www.huaweicloud.com/intl/en-us/ | No official Gambia public cloud region found | Huawei project claims are project/DC evidence, not public-region proof |

Annual verification:
```text
site:aws.amazon.com Gambia "Region"
site:learn.microsoft.com/azure "Gambia" "region"
site:cloud.google.com/about/locations Gambia
site:oracle.com/cloud "Gambia" "region"
"Gambia" "cloud region" official
```

---

## 8. Per-Division Official Enumeration Strategy

| Division | Capital / core towns | Official anchors | Strategy and honest expected yield |
|---|---|---|---|
| **Banjul** | Banjul | Banjul City Council; GAMTEL HQ; ministries; GPPA; ACE/landing-station evidence | **Medium-low.** Search GAMTEL HQ, ACE landing-station works, government server rooms, WARDIP tenders, and council records. Do not inflate Banjul into a cluster without site evidence. |
| **Western** | Serekunda, Kanifing, Abuko, Bakau, Brikama, Yundum | GICTA; National Data Centre Abuko; GAMTEL/Serekunda/Kairaba leads; SIXP; PURA; NAWEC; GIEPA; ISPs | **Highest yield.** Confirm Abuko NDC via official pages; verify GAMTEL colo site-level leads; inspect GPPA/WARDIP, PURA, NAWEC, and council trails. Expected 1-3 countable or near-countable facilities plus network leads. |
| **Lower River** | Mansakonko | Area council; NAWEC distribution; telco/backbone nodes | **Very low watch.** Search for government ICT rooms, GAMTEL/telco exchange upgrades, WARDIP/NBN works; record `no confirmed facility found` if none. |
| **Central River** | Janjanbureh, Kuntaur | Area councils; telco/backbone nodes; public-service ICT | **Very low watch.** Search Janjanbureh/Kuntaur for e-government, telco, and power evidence; facility count unlikely. |
| **North Bank** | Kerewan | Area council; NAWEC distribution; ferry/corridor systems; telco/backbone nodes | **Very low watch.** Search Kerewan/corridor records; count only named facilities. |
| **Upper River** | Basse Santa Su | Area council; border systems; telco/backbone nodes | **Very low watch.** Search Basse for government ICT, border/trade systems, and telco nodes; facility count unlikely. |

Division query block:
```text
"{division}" "data centre" OR "data center" OR "server room" OR "hosting" Gambia
"{capital}" "data centre" OR "server room" OR "ICT" Gambia
site:gicta.gov.gm "{division}" OR "{capital}"
site:mocde.gov.gm "{capital}" OR "{division}"
site:pura.gm "{capital}" "licence"
site:gppa.gm "{capital}" OR "{division}" "ICT"
"{capital}" "GAMTEL" OR "GICTA" OR "WARDIP" Gambia
"{division}" "NBN" OR "fiber" OR "backbone" Gambia
```
