# IN Explorer — Official / Regulatory / Cloud Pipeline for India Datacenter Enumeration

Date: 2026-08-12. Country: **IN India**. Division model for world expansion: **states / union territories + districts** (763 district-level targets in the current manifest). Focus: official and regulatory paper trail, government e-permitting, state investment portals, pollution / energy approvals, SEZ and industrial-park approvals, official cloud-region pages, and legally accountable operator disclosures.

Reliability grades used here:
- **A** = primary / official / legally accountable source: central or state government portal, statutory clearance, official cloud-region page, official operator facility page, exchange filing / annual report.
- **B** = strong secondary source: established trade press, industry association, datacenter-map aggregator when corroborated, state investment promotion article that summarizes an MoU.
- **C** = weak lead: consultant summaries, social media, unsourced maps, stale marketing pages, signing-ceremony articles with no approval trail.

---

## 1. India-Specific Structure Facts

India does not have one searchable national planning-permit database equivalent to a US county planning portal or China's investment-filing platform. Enumeration works by combining:

1. **Industrial single-window approvals**: NSWS plus state portals such as MAITRI, TG-iPASS, Nivesh Mitra, Tamil Nadu Single Window, GO SWIFT, Silpa Sathi, Invest Karnataka / Udyog Mitra, etc. These prove the project entered the approval pipeline, but public detail is uneven. Grade **A** when a public approval / incentive order names the project; otherwise use as portal index only.
2. **Environmental / pollution approvals**: PARIVESH and SEIAA / SEAC minutes for EC where the building threshold applies; State Pollution Control Board Consent to Establish / Consent to Operate for DG sets, STP, fuel storage, batteries, construction, and operation. Grade **A**.
3. **Power and energy trail**: state electricity distribution / transmission connectivity approvals, open-access renewable approvals, captive-power approvals, electrical inspector / CEIG approvals, and high-tension substation tender / award notices. Grade **A** for official orders and tenders.
4. **Land / industrial park trail**: MIDC, SIPCOT, TSIIC, APIIC, UPSIDA, YEIDA, NOIDA / Greater Noida, GIDC, KIADB, HSIIDC, WBIDC, IDCO, KINFRA, Infopark / SmartCity, IT parks, SEZ Online and SEZ Board of Approval minutes. Grade **A**.
5. **Official cloud and operator footprint**: AWS, Azure, Google Cloud, OCI, Jio / Azure, Airtel Nxtra, Tata, STT GDC India, NTT, CtrlS, Sify, Yotta, AdaniConneX, Web Werks / Iron Mountain, CapitaLand, PDG, Equinix, Digital Realty / Brookfield BAM Digital Realty. Grade **A** for existence and city / campus statements; capacity is **A** only when from filings or official spec sheets.

Important caveat: a datacenter in India is usually permitted as **building / construction / IT-ITES / industrial infrastructure**, not under a single datacenter license. Absence from one portal is not absence of a project.

---

## 2. Central Government Portals and Query Patterns

### 2.1 NSWS — National Single Window System

- Portal: https://www.nsws.gov.in/
- About / coverage: https://www.nsws.gov.in/about-us
- FAQ: https://www.nsws.gov.in/faqs
- Role: front door for identifying and applying for approvals. NSWS says it guides approvals across central departments and state governments and hosts applications for many of those approvals. Use **Know Your Approvals (KYA)** for a generic "Data Centre / IT-ITES / Building Construction / Industrial Park" unit by state.
- Grade: **A** for portal and approval requirement metadata; **A** for any downloaded approval certificate / order; **C** for mere application existence if no public certificate is visible.
- Query pattern:
  - KYA industry: `Information Technology`, `IT/ITES`, `Data Centre`, `Building Construction`, `Industrial Infrastructure`.
  - Location: run state-by-state, then district-by-district for high-priority districts.
  - Capture required departments: state industry department, urban local body / development authority, fire service, pollution board, electricity distribution / transmission, labour, water / sewerage, factory inspector where applicable.

### 2.2 CPPP / Government eProcurement

- Central Public Procurement Portal: https://eprocure.gov.in/eprocure/app
- NIC state eProc portals use the same pattern, e.g. Maharashtra https://mahatenders.gov.in/nicgep/app and central-state portal https://etenders.gov.in/eprocure/app.
- Use: tenders for state data centres, public cloud empanelment, data centre O&M, electrical works, 220 kV / 132 kV GIS substations, DG sets, chillers, BMS, fire systems, fibre routes, and government disaster-recovery sites. CPPP is better for government / captive facilities than private hyperscale campuses, but it often exposes EPC and utility work.
- Grade: **A** for tender existence, buyer, site, tender value, dates, and work description; **B** for inferred private-campus status unless the tender directly names the owner / project.
- Query patterns:
  - CPPP basic search: `"data centre"`, `"data center"`, `"datacenter"`, `"cloud data centre"`, `"state data centre"`, `"disaster recovery site"`, `"DR site"`, `"server farm"`, `"IT load"`, `"DG set"`, `"chiller"`, `"GIS substation"`.
  - Web search: `site:eprocure.gov.in/eprocure/app "Data Centre" "{district}"`, `site:etenders.gov.in/eprocure/app "data center" "{operator}"`, `site:mahatenders.gov.in "data centre" "Navi Mumbai"`.
  - Hindi / local: `डेटा सेंटर निविदा`, `डाटा सेंटर`, plus state-language terms for "tender" if district search is sparse.

### 2.3 PARIVESH / Environmental Clearance

- PARIVESH 2.0: https://parivesh.nic.in/
- Legacy EC portal: https://environmentclearance.nic.in/
- Role: environmental-clearance filings under EIA Notification 2006. Datacenters appear when filed as item **8(a) Building / Construction** or area-development projects, especially large built-up-area campuses. Example public PARIVESH record found: Amazon Data Services India "Data Center Construction Project" at Chandanvelly / Hythabad, Shahbad tehsil, Ranga Reddy district, Telangana, file `SIA/TG/INFRA2/503345/2024`, with SEIAA amendment order.
- Grade: **A** for EC / amendment letters, Form 1, conceptual plan, SEAC / SEIAA minutes; **A** for coordinates, built-up area, water, wastewater, DG, and project proponent; **B** for capacity inferred from building area.
- Critical caveat: datacenters do **not always** require prior EC as a datacenter category. EC trigger is usually building / construction area or area-development threshold. Therefore PARIVESH is high precision, low recall.
- Query patterns:
  - Web: `site:parivesh.nic.in "Data Center Construction Project" India`
  - Web: `site:environmentclearance.nic.in "data centre" "Environmental Clearance" "{state}"`
  - Portal keywords: `Data Center`, `Data Centre`, `IT/ITES`, `Commercial (IT/ITES, Data Centre)`, `Amazon Data Services`, `NTT Global Data Centers`, `AdaniConneX`, `Yotta`, `CtrlS`, `Nxtra`, `STT Global Data Centres`, `Web Werks`, `Sify`.

### 2.4 MeitY AMBUD / Government Cloud Empanelment

- AMBUD: https://www.ambud.meity.gov.in/
- FAQ: https://ambud.meity.gov.in/faq
- Role: MeitY platform for empanelment of cloud service providers and registration of data centres. AMBUD states that CSP empanelment requires datacentres in India; FAQ text says the datacentre must be in India and at least 100 racks operational or 1 MVA IT load.
- Grade: **A** for government-cloud provider eligibility / registration status and minimum operational threshold; not a complete commercial facility registry.
- Query pattern: search AMBUD documents / empanelment lists for CSP names, then pivot each CSP to official facility and state approval searches.

### 2.5 SEZ and Industrial Park Approvals

- SEZ Online: https://www.sezonline-ndml.com/
- Ministry of Commerce SEZ site: https://sezindia.gov.in/
- Role: IT / ITES SEZs and industrial parks host some datacenters; Board of Approval minutes and unit approvals can identify developers and plots. Use especially for Chennai, Pune, Navi Mumbai, Noida / Greater Noida, Bengaluru, Hyderabad, GIFT City, Kochi, and Kolkata.
- Grade: **A** for notified SEZ, unit approval, co-developer approval, and Board of Approval minutes; **B** when used only as host-park context.
- Query patterns:
  - `site:sezindia.gov.in "data centre"`, `site:sezindia.gov.in "data center"`, `site:sezindia.gov.in "{operator}" "SEZ"`
  - `"{park name}" "data centre" "SEZ"`, e.g. `"SIPCOT IT Park Siruseri" "data centre"`, `"Hiranandani Fortune City" "data center"`.

### 2.6 Corporate and Securities Filings

- MCA company master data / filings: https://www.mca.gov.in/
- NSE filings: https://www.nseindia.com/companies-listing/corporate-filings-announcements
- BSE filings: https://www.bseindia.com/corporates/ann.html
- SEBI: https://www.sebi.gov.in/
- Role: SPV discovery, annual reports, debt documents, investor presentations, related-party approvals, acquisitions, and capex commitments. Use for listed parents: Bharti Airtel / Nxtra, Reliance / Jio, Tata Communications, Sify, Adani Enterprises / AdaniConneX, Hiranandani / Yotta if bond docs are available, Anant Raj, RailTel, ESDS, etc.
- Grade: **A** for filings; **B** for investor decks where capacity is forward-looking.
- Query patterns:
  - `site:bseindia.com "{operator}" "data centre"`
  - `site:nseindia.com "{operator}" "data center"`
  - `site:ril.com "data centres" "Microsoft" "Azure"`
  - `"{SPV name}" "CIN" "data center"`, `"{operator}" "annual report" "MW" "data centre"`.

---

## 3. State / District Approval Pipeline

Run this in **state-first** order, then bucket records to districts. Most public approval portals are state-level; India district names are noisy and often hidden inside PDF addresses.

### Step A — state investment / single-window sweep

Use the state portal to identify approvals, incentives, land allocation, and named policy beneficiaries. Capture project name, legal entity, district, taluka / tehsil, village / plot, land area, proposed IT load / MW, investment, and status.

High-priority portals:

| State / UT | Portal / agency | URL | Priority districts / metros | Grade |
|---|---|---|---|---|
| Maharashtra | MAITRI / MIDC / MMRDA / Navi Mumbai / Pune agencies | https://maitri.maharashtra.gov.in/ ; https://www.midcindia.org/ | Mumbai, Navi Mumbai, Thane, Raigad, Pune, Nagpur | A |
| Telangana | Invest Telangana / TG-iPASS / TSIIC | https://invest.telangana.gov.in/ ; https://ipass.telangana.gov.in/ | Hyderabad, Ranga Reddy, Sangareddy, Medchal-Malkajgiri | A |
| Tamil Nadu | Guidance TN / Tamil Nadu Single Window / SIPCOT / ELCOT | https://www.investingintamilnadu.com/ ; https://tnswp.com/ ; https://www.sipcot.tn.gov.in/ | Chennai, Chengalpattu, Kancheepuram, Tiruvallur, Coimbatore | A |
| Uttar Pradesh | Invest UP / Nivesh Mitra / Noida / Greater Noida / YEIDA / UPSIDA | https://invest.up.gov.in/ ; https://niveshmitra.up.gov.in/ | Gautam Buddha Nagar, Ghaziabad, Lucknow, Kanpur Nagar | A |
| Karnataka | Invest Karnataka / Karnataka Udyog Mitra / KIADB | https://www.investkarnataka.co.in/ ; https://kum.karnataka.gov.in/ ; https://kiadb.in/ | Bengaluru Urban, Bengaluru Rural, Kolar, Mysuru | A |
| Gujarat | Investor Facilitation Portal / iNDEXTb / GIDC / GIFT City | https://ifp.gujarat.gov.in/ ; https://investgujarat.in/ ; https://gidc.gujarat.gov.in/ ; https://www.giftgujarat.in/ | Gandhinagar, Ahmedabad, Surat, Kutch | A |
| Haryana | HEPC / HSIIDC | https://investharyana.in/ ; https://hsiidc.org.in/ | Gurugram, Manesar, Faridabad, Sonipat | A |
| Andhra Pradesh | AP Industries Single Desk / APIIC | https://apindustries.gov.in/ ; https://apiic.in/ | Visakhapatnam, Anakapalli, Krishna, Tirupati | A |
| Odisha | GO SWIFT / IDCO | https://investodisha.gov.in/ ; https://idco.in/ | Bhubaneswar / Khordha, Cuttack | A |
| West Bengal | Silpa Sathi / WBIDC / Webel | https://silpasathi.wb.gov.in/ ; https://www.wbidc.com/ ; https://www.webel.in/ | Kolkata, North 24 Parganas, Howrah | A |
| Kerala | K-SWIFT / KINFRA / Infopark | https://kswift.kerala.gov.in/ ; https://www.kinfra.org/ ; https://infopark.in/ | Ernakulam / Kochi, Thiruvananthapuram | A |
| Madhya Pradesh | Invest MP | https://invest.mp.gov.in/ | Indore, Bhopal | A |
| Rajasthan | Raj Nivesh | https://rajnivesh.rajasthan.gov.in/ | Jaipur, Alwar, Jodhpur | A |
| Delhi NCT | Delhi industrial / building portals; use MCD / DDA / fire and pollution board | https://mcdonline.nic.in/ ; https://dda.gov.in/ | Delhi districts; mostly enterprise / edge / government DCs | A |

State-portal query templates:
```
site:{state-portal-domain} "data centre"
site:{state-portal-domain} "data center"
site:{state-portal-domain} "Data Centre Policy"
site:{state-portal-domain} "{operator}" "data centre"
site:{state-industrial-agency-domain} "data centre" "allotment"
site:{development-authority-domain} "data centre" "plot"
```

Hindi and Indian-English variants:
```
"{district}" "data centre" "single window"
"{district}" "data center" "land allotment"
"{district}" "IT load" "MW" "data centre"
"{district}" "डेटा सेंटर" "निवेश"
"{district}" "डाटा सेंटर" "भूमि"
```

### Step B — pollution / environmental sweep

Every state has a Pollution Control Board / Pollution Control Committee. Search for Consent to Establish (CTE), Consent to Operate (CTO), public hearing / minutes where applicable, and online consent order PDFs.

High-value boards:
- Maharashtra Pollution Control Board: https://mpcb.gov.in/
- Telangana State Pollution Control Board: https://tspcb.cgg.gov.in/
- Tamil Nadu Pollution Control Board: https://tnpcb.gov.in/
- Uttar Pradesh Pollution Control Board: https://www.uppcb.com/
- Karnataka State Pollution Control Board: https://kspcb.karnataka.gov.in/
- Gujarat Pollution Control Board: https://gpcb.gujarat.gov.in/
- Haryana State Pollution Control Board: https://hspcb.gov.in/
- Andhra Pradesh Pollution Control Board: https://pcb.ap.gov.in/
- Odisha State Pollution Control Board: https://ospcboard.org/
- West Bengal Pollution Control Board: https://www.wbpcb.gov.in/
- Kerala State Pollution Control Board: https://kspcb.kerala.gov.in/
- Delhi Pollution Control Committee: https://www.dpcc.delhigovt.nic.in/

Query templates:
```
site:{spcb-domain} "data centre" "Consent to Establish"
site:{spcb-domain} "data center" "Consent to Operate"
site:{spcb-domain} "{operator}" "Consent"
site:{spcb-domain} "DG set" "data centre"
site:{spcb-domain} "IT/ITES" "data centre"
```

What to extract: project proponent, address, industry category, CTE / CTO date, validity, DG capacity, water draw, sewage / STP, hazardous waste, battery waste, fuel storage. Pollution approvals are often the best evidence that a facility moved beyond MoU stage.

### Step C — power, grid, and open-access sweep

Datacenters leave a large power trail: HT / EHT service connection, dedicated substations, transmission bays, open-access renewable procurement, captive solar / wind, and electrical inspector approvals.

Targets:
- Central Electricity Authority: https://cea.nic.in/
- Central Electricity Regulatory Commission: https://cercind.gov.in/
- State Electricity Regulatory Commissions: search `"{state}" "Electricity Regulatory Commission" "open access" "data centre"`
- State transmission / distribution utilities: MSETCL / MSEDCL, TSTRANSCO / TGSPDCL, TANTRANSCO / TANGEDCO, UPPTCL / UPPCL, KPTCL / BESCOM, GETCO / PGVCL / Torrent, HVPNL / DHBVN, APTRANSCO / APEPDCL, OPTCL, WBSETCL / WBSEDCL, KSEB, etc.

Query templates:
```
site:{utility-domain} "data centre" "substation"
site:{utility-domain} "data center" "220 kV"
site:{utility-domain} "{operator}" "HT connection"
site:{serc-domain} "data centre" "open access"
site:{serc-domain} "{operator}" "renewable" "open access"
```

Grade **A** when an order / tender names the datacenter or operator; **B** when the utility work is adjacent to a known industrial park but does not name the facility.

### Step D — land, development authority, fire, and building permission

Use this for exact siting and status:
- Industrial land agencies: MIDC, TSIIC, SIPCOT, APIIC, UPSIDA, NOIDA / Greater Noida / YEIDA, GIDC, KIADB, HSIIDC, WBIDC, IDCO, KINFRA.
- Municipal / planning portals: MCGM / BMC, Navi Mumbai Municipal Corporation, MMRDA, HMDA / GHMC, CMDA, DTCP Tamil Nadu, BDA / BBMP, DDA / MCD, GMDA, GMADA, GIFT, etc.
- Fire NOC portals: state fire services often publish NOC / renewal searchable by building.

Query templates:
```
site:{land-agency-domain} "data centre" "allotment"
site:{development-authority-domain} "data center" "building permission"
site:{fire-domain} "{operator}" "fire NOC"
site:{municipal-domain} "{operator}" "commencement certificate"
site:{municipal-domain} "data centre" "occupancy certificate"
```

Grade **A** for allotment, building permit, commencement certificate, occupancy certificate, or fire NOC. Treat MoUs as **C** until land / CTE / power evidence appears.

---

## 4. Official Cloud Provider Region Pages

Cloud regions prove operational market presence and narrow the search to metro / state, but do not reveal exact campuses. Use them as **A-grade city evidence**, then join to operator / EC / power filings.

| Provider | Official URL | India regions / locations | Enumeration value |
|---|---|---|---|
| AWS | https://aws.amazon.com/local/india/ ; https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | Asia Pacific (Mumbai) `ap-south-1`; Asia Pacific (Hyderabad) `ap-south-2`, each with 3 AZs | Search Maharashtra and Telangana approval trails for Amazon Data Services India; PARIVESH has Ranga Reddy EC evidence. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list ; https://news.microsoft.com/source/asia/features/microsofts-newest-india-datacenter-region-goes-live-to-power-the-countrys-ai-economy-and-enable-frontier-firms/ | Central India (Pune), South India (Chennai), West India (Mumbai), India South Central (Hyderabad, live August 2026); also Jio India West / Jio India Central partnership regions | Search Microsoft, Jio, Reliance, and local SPVs in Maharashtra, Tamil Nadu, Telangana, Gujarat. |
| Google Cloud | https://cloud.google.com/about/locations ; https://docs.cloud.google.com/compute/docs/regions-zones | Mumbai `asia-south1`; Delhi `asia-south2` | Search Google / Raiden Infotech / AdaniConneX / partner entities around Mumbai and Delhi NCR. |
| Oracle Cloud Infrastructure | https://www.oracle.com/in/cloud/public-cloud-regions/ ; https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | India West (Mumbai) `ap-mumbai-1`; India South (Hyderabad) `ap-hyderabad-1` | Search Oracle, OCI, and colocation partners in Maharashtra / Telangana. |
| Jio + Microsoft | Reliance release: https://www.ril.com/sites/default/files/2023-01/MRMicrosoft.pdf ; annual report note: https://www.ril.com/ar2019-20/mda.html | Initial Jio datacentres in Gujarat and Maharashtra for Azure platform, up to 7.5 MW IT equipment each per RIL disclosure | Official Reliance filings / releases are A-grade seeds; exact facility requires state / pollution / power join. |

Query templates:
```
"Amazon Data Services India" "Environmental Clearance" "Data Center"
"Microsoft" "data centre" "India South Central" Hyderabad
"Google" "data center" "Mumbai" "environmental clearance"
"Oracle" "India West" "Mumbai" "data centre"
"Jio" "Azure" "data centres" "Gujarat" "Maharashtra"
```

---

## 5. Official / Operator Facility Pages to Seed the Facility Universe

Operator pages are not regulators, but they are primary statements by the facility owner. Use as **A** for existence / marketed campus and **B** for planned capacity unless backed by filings.

| Operator | Official source | India footprint signals | Follow-up official joins |
|---|---|---|---|
| NTT Global Data Centers India | https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/india | Mumbai, Navi Mumbai, Bengaluru, Chennai, Delhi NCR / Noida, Kolkata; page names many facilities such as Mumbai 5/6/7, Vikhroli, Navi Mumbai, Bengaluru 2/3/4, Chennai 1/2, Noida 1/2; Kolkata 25+ MW signal | Search NTT / Netmagic in PARIVESH, state pollution boards, MIDC, Noida / Greater Noida, SIPCOT, KSPCB. |
| STT GDC India | https://www.sttelemediagdc.com/in-en/locations | 34 facilities across 10 cities per official page | Join to Tata Communications history, SEZ / park approvals, pollution CTE/CTO, state MoUs. |
| CtrlS | https://www.ctrls.com/ ; https://www.ctrls.com/about-us/ | Mumbai, Chennai, Hyderabad, Noida, Bangalore, Kolkata, Lucknow, Patna, Ahmedabad, Bhubaneswar, Bhopal listed in site navigation; official history names first Rated-4 Hyderabad facility | Search CtrlS in TSPCB, GHMC / HMDA, Tamil Nadu / SIPCOT, UP, West Bengal, Odisha portals. |
| Airtel Nxtra | https://www.nxtra.in/who-we-are/ ; examples https://www.nxtra.in/data-center-hyderabad and https://www.nxtra.in/data-center-manesar | 120+ locations; hyperscale Hyderabad Kokapet; NCR Manesar; official Airtel release says 120+ locations and trajectory to over 400 MW | Join to Bharti Airtel annual reports, HSPCB, TSPCB, power open-access orders. |
| Yotta | https://yotta.com/data-center-in-india/ ; press releases under https://yotta.com/press-releases/ | NM1 Navi Mumbai; D1 Greater Noida; G1 GIFT City; TB1/TB2 Navi Mumbai; official press says Greater Noida park 30,000 racks / 200 MW and Navi Mumbai park 30,000 racks / 250 MW | Join to MIDC / Panvel / Raigad, UP / Greater Noida, GIFT / Gujarat pollution and power approvals. |
| Reliance Jio | https://www.ril.com/businesses/digital-services-jio ; RIL annual reports / releases | Jio / Microsoft Azure datacentres in Gujarat and Maharashtra; Jio has large captive telecom / edge footprint | Join to RIL filings, state industrial approvals, power approvals, Azure region docs. |
| Tata Communications | https://www.tatacommunications.com/cloud/managed-services and annual reports | Tata Vayu cloud / managed hosting / colocation; legacy and retained DCs require filings because many Indian colocation assets became STT GDC JV | Join to Tata Communications annual reports, BSE/NSE, STT pages, SEZ / pollution approvals. |
| Sify Technologies | https://www.sifytechnologies.com/ | Indian DC operator with official investor filings / Form 20-F | Join to SEC / annual reports, Chennai / Mumbai / Noida / Hyderabad / Bengaluru state approvals. |
| AdaniConneX | https://www.adaniconnex.com/ | Hyperscale campuses in Chennai, Noida, Hyderabad, Pune / Mumbai, Vizag and other markets reported by company / group | Join to Adani Enterprises filings, state investment orders, pollution / power approvals. |
| Web Werks / Iron Mountain | https://www.webwerks.in/ ; https://www.ironmountain.com/data-centers | Mumbai, Pune, Noida, Bengaluru / Hyderabad pipeline signals | Join to Iron Mountain filings, state pollution boards, land agencies. |
| CapitaLand India Trust / CLI | https://www.capitaland.com/in/en.html and investor announcements | Navi Mumbai, Chennai, Hyderabad, Bengaluru data centre development pipeline | Join to SGX / CapitaLand announcements, state land / EC / power. |
| PDG India | https://www.princetondg.com/ | Mumbai / Navi Mumbai MU1 campus and India expansion | Join to MIDC / pollution / power, operator official releases. |
| Equinix India | https://www.equinix.com/locations/india-colocation | Mumbai IBX facilities and Chennai expansion signals | Join to Equinix filings, MMR / Chennai approvals. |

Operator query templates:
```
"{operator legal name}" "Consent to Establish"
"{operator legal name}" "Environmental Clearance"
"{operator}" "data centre" "{district}" "MW"
"{operator}" "annual report" "data centre" "India"
"{operator}" "open access" "data centre"
"{operator}" "220 kV" "substation"
```

---

## 6. Priority Geography and District Bucketing

Run all 763 district targets, but prioritize districts that intersect cloud regions, submarine cable landing, hyperscale power availability, and state data-centre policies.

### Tier 1 enumeration districts

| Cluster | Districts to bucket | Why |
|---|---|---|
| Mumbai / Navi Mumbai / Pune | Mumbai City, Mumbai Suburban, Thane, Raigad, Pune | AWS / Azure / GCP / OCI Mumbai region; NTT, STT, Yotta, Web Werks, Equinix, CapitaLand, PDG; MIDC / MMR / Navi Mumbai / Panvel approval trail. |
| Hyderabad | Hyderabad, Ranga Reddy, Medchal-Malkajgiri, Sangareddy | AWS Hyderabad, OCI Hyderabad, Azure India South Central; Amazon EC examples in PARIVESH; CtrlS, Nxtra, STT, Microsoft / Oracle pipeline. |
| Chennai | Chennai, Chengalpattu, Kancheepuram, Tiruvallur | Azure South India, cable landing, NTT / STT / Sify / CtrlS / AdaniConneX / Yotta pipeline; SIPCOT / ELCOT / CMDA / TNPCB trail. |
| Delhi NCR / Noida / Greater Noida / Manesar | Gautam Buddha Nagar, Ghaziabad, Delhi districts, Gurugram, Faridabad, Jhajjar | GCP Delhi region, Yotta D1, NTT Noida, STT / CtrlS / Nxtra / AdaniConneX; UP Data Centre Policy, Noida / Greater Noida / YEIDA / HSIIDC trail. |
| Bengaluru | Bengaluru Urban, Bengaluru Rural, Kolar | NTT, STT, CtrlS, Sify, cloud on-ramps; KIADB / KSPCB / BESCOM trail. |
| Kolkata | Kolkata, North 24 Parganas, Howrah | NTT Kolkata, CtrlS Kolkata, STT / Sify / Webel / Tata; WBIDC / Webel / WBPCB trail. |
| Gujarat / GIFT | Gandhinagar, Ahmedabad, Surat, Kutch | Jio / Microsoft initial Gujarat DC, Yotta G1 at GIFT City, new Gujarat DC policy, GIDC / GIFT / GETCO trail. |
| Visakhapatnam | Visakhapatnam, Anakapalli | Coastal / cable potential, Google / Adani AI DC reports, APIIC / APPCB / APTRANSCO trail. Treat recent mega-project claims as C until official approvals are found. |
| Bhubaneswar | Khordha, Cuttack | CtrlS / state DC / Odisha policy; IDCO / GO SWIFT / OSPCB trail. |
| Kochi / Kerala | Ernakulam, Thiruvananthapuram | Cable landing / Infopark / government cloud; K-SWIFT / KINFRA / KSPCB trail. |

### District-level record-building recipe

For each district `D` in state `S`:

1. Search official state portal and investment agency:
   ```
   site:{state-investment-domain} "{D}" "data centre"
   site:{state-investment-domain} "{D}" "data center"
   site:{industrial-agency-domain} "{D}" "data centre"
   ```
2. Search PARIVESH / EC and SEIAA minutes:
   ```
   site:parivesh.nic.in "{D}" "Data Center"
   site:environmentclearance.nic.in "{D}" "data centre"
   "{D}" "SEIAA" "data centre"
   ```
3. Search pollution board:
   ```
   site:{spcb-domain} "{D}" "data centre" "Consent"
   site:{spcb-domain} "{operator}" "{D}"
   ```
4. Search power / utility:
   ```
   site:{utility-domain} "{D}" "data centre" "substation"
   site:{serc-domain} "{D}" "data centre" "open access"
   ```
5. Search land / planning authority:
   ```
   site:{development-authority-domain} "{D}" "data centre" "plot"
   site:{municipal-domain} "{D}" "data centre" "building permission"
   ```
6. Search official cloud / operator pages and filings for each seed operator in the state.
7. Dedupe by `(ultimate parent, legal project proponent / SPV, campus name, plot / village, phase)`. Indian records often use different spellings: `Data Centre`, `Data Center`, `Datacenter`, `IT/ITES`, `server farm`, `cloud infrastructure`, `digital infrastructure`.

---

## 7. Evidence Grades for India

| Grade | India source examples | Use |
|---|---|---|
| **A** | NSWS approval certificate; state single-window order; PARIVESH EC / EC amendment; SEIAA / SEAC minutes; SPCB CTE / CTO; state electricity / SERC order; industrial land allotment; development authority building / occupancy certificate; fire NOC; SEZ Board of Approval minutes; official cloud-region docs; official operator facility page; BSE / NSE / MCA / annual report filings; CPPP / state eProc tender | Primary project / status / location evidence. |
| **B** | PIB / state government press release; state investment promotion MoU page; established trade press (DCD, Economic Times datacenter vertical, C114-style telecom press equivalents); industry association reports; datacenters.com / Baxtel / DataCenterMap when matched to an official source | Lead or corroboration. Promote to A only after matching a filing, permit, or official operator page. |
| **C** | LinkedIn posts, Facebook posts, consultant policy summaries, unsourced maps, local articles about MoUs, political signing ceremonies, promotional brochures | Discovery only. Do not count as operational or under-construction without A/B corroboration. |

Status semantics:
- **MoU / investment intent** = planned lead only, usually **C** unless backed by state cabinet order or incentive approval.
- **Land allotted / building permission / CTE** = real permitted project, not necessarily under construction.
- **EC / CTE / power connection / EPC tender** = strong pre-construction or construction signal.
- **CTO / occupancy / fire operational NOC / operator facility page live** = operational or near-operational evidence.
- **Cloud region live** = operational cloud capacity in metro, not facility address.

Capacity semantics:
- Prefer IT load MW from official operator pages, power orders, EC / conceptual plans, annual reports, or exchange filings.
- Built-up area and rack count are secondary; convert to MW only with explicit rack density assumptions and mark inferred.
- Planned "campus MW" across many phases should be stored separately from live / commissioned MW.

---

## 8. Quick-Reference URL Index

Central / national:
- NSWS: https://www.nsws.gov.in/
- CPPP: https://eprocure.gov.in/eprocure/app
- Government eProc state gateway: https://etenders.gov.in/eprocure/app
- PARIVESH: https://parivesh.nic.in/
- Legacy EC portal: https://environmentclearance.nic.in/
- MeitY AMBUD: https://www.ambud.meity.gov.in/
- SEZ India: https://sezindia.gov.in/
- SEZ Online: https://www.sezonline-ndml.com/
- MCA: https://www.mca.gov.in/
- NSE filings: https://www.nseindia.com/companies-listing/corporate-filings-announcements
- BSE filings: https://www.bseindia.com/corporates/ann.html

State portals:
- Maharashtra MAITRI: https://maitri.maharashtra.gov.in/ ; MIDC: https://www.midcindia.org/
- Telangana Invest / TG-iPASS: https://invest.telangana.gov.in/ ; https://ipass.telangana.gov.in/
- Tamil Nadu Guidance / TNSWP / SIPCOT: https://www.investingintamilnadu.com/ ; https://tnswp.com/ ; https://www.sipcot.tn.gov.in/
- Uttar Pradesh Invest UP / Nivesh Mitra: https://invest.up.gov.in/ ; https://niveshmitra.up.gov.in/
- Karnataka Invest / Udyog Mitra / KIADB: https://www.investkarnataka.co.in/ ; https://kum.karnataka.gov.in/ ; https://kiadb.in/
- Gujarat IFP / Invest Gujarat / GIDC / GIFT: https://ifp.gujarat.gov.in/ ; https://investgujarat.in/ ; https://gidc.gujarat.gov.in/ ; https://www.giftgujarat.in/
- Haryana Invest / HSIIDC: https://investharyana.in/ ; https://hsiidc.org.in/
- Andhra Pradesh Industries / APIIC: https://apindustries.gov.in/ ; https://apiic.in/
- Odisha Invest / IDCO: https://investodisha.gov.in/ ; https://idco.in/
- West Bengal Silpa Sathi / WBIDC / Webel: https://silpasathi.wb.gov.in/ ; https://www.wbidc.com/ ; https://www.webel.in/
- Kerala K-SWIFT / KINFRA / Infopark: https://kswift.kerala.gov.in/ ; https://www.kinfra.org/ ; https://infopark.in/

Cloud / operator:
- AWS India: https://aws.amazon.com/local/india/
- AWS global regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Microsoft India South Central launch: https://news.microsoft.com/source/asia/features/microsofts-newest-india-datacenter-region-goes-live-to-power-the-countrys-ai-economy-and-enable-frontier-firms/
- Google Cloud locations: https://cloud.google.com/about/locations
- Google Compute regions / zones: https://docs.cloud.google.com/compute/docs/regions-zones
- OCI India regions: https://www.oracle.com/in/cloud/public-cloud-regions/ ; https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
- Reliance Jio / Microsoft release: https://www.ril.com/sites/default/files/2023-01/MRMicrosoft.pdf
- NTT India: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/india
- STT GDC India: https://www.sttelemediagdc.com/in-en/locations
- CtrlS: https://www.ctrls.com/
- Nxtra: https://www.nxtra.in/who-we-are/
- Yotta India: https://yotta.com/data-center-in-india/

---

## 9. Practical Pitfalls

- **Data centre vs data center**: Indian English uses both. Always search both spellings plus `datacenter`.
- **Public cloud region != facility address**: cloud docs prove a metro and operational status, not the building.
- **MoU inflation**: large MW and crore numbers in investor summits often combine 8-10 year phase plans. Do not mark under construction without land / CTE / EC / power / EPC evidence.
- **PARIVESH low recall**: many datacenters are permitted below EC thresholds or through local building approvals; absence from PARIVESH is not negative evidence.
- **Operator aliasing**: old Netmagic assets now appear under NTT; Tata/STT overlap historically; Jio / Microsoft uses Reliance / Azure language; subsidiaries and SPVs may hold land / permits.
- **District parsing**: addresses may use taluka / mandal / village rather than district. Normalize to the 763-division manifest by state gazette / Census district names.
- **Power is often the best reality check**: a claimed 200 MW campus should have EHT connection, substation, open-access, or utility tender evidence somewhere.

Recommended enumeration order: **official cloud + operator seed list → state investment / land portal → pollution / EC → power / utility → CPPP / tenders → corporate filings → trade press backfill**.
