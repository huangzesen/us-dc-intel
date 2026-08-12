# BD Explorer Official - Bangladesh Datacenter Enumeration Methodology

Date: 2026-08-12. Review status: final methodology after live URL and source checks. Scope: official, regulator, registry, utility, planning, e-procurement, government-IT, cloud-region-list, and operator-primary methods for enumerating datacenter facilities and projects in Bangladesh (BD). Division model: **division** (8 divisions). Reliability grades are field-scoped: **A** = official government/registry/law/utility/cloud-region-list, primary IXP/PeeringDB, or operator-owned source for the fact stated; **B** = reliable trade press, local press, or regulator-adjacent source naming a project fact; **C** = aggregator, directory, broker listing, social post, or weak repost; **U** = unverified or not found in the current check.

## 0. Administrative model and coverage requirement

Bangladesh has **8 first-level administrative divisions**. Every census run must cover all eight, even when the expected result is negative.

| # | Division | Priority districts/localities for DC search |
|---|---|---|
| 1 | Barishal | Barishal city; Patuakhali/Kuakata cable landing; Bhola |
| 2 | Chattogram | Chattogram city/Agrabad/Nasirabad; Cox's Bazar cable landing; Cumilla; Feni; Mirsarai/BSMSN SEZ |
| 3 | Dhaka | Dhaka North/South: Gulshan, Mohakhali, Banani, Kawran Bazar, Agargaon, Rampura, Bashundhara, Asad Avenue; Gazipur/Kaliakair Bangabandhu Hi-Tech City; Narayanganj; Savar |
| 4 | Khulna | Khulna city/KDA Commercial Area; Jashore Software Technology Park and commercial colo sites; Mongla; Satkhira |
| 5 | Rajshahi | Rajshahi city; Bogura; Pabna |
| 6 | Rangpur | Rangpur city; Dinajpur; Gaibandha |
| 7 | Sylhet | Sylhet city; Moulvibazar; Habiganj; Sunamganj |
| 8 | Mymensingh | Mymensingh city; Jamalpur; Netrokona; Sherpur |

No public Bangladesh datacenter registry was found. Build records by joining official legal/entity/procurement/park evidence with operator-primary pages, BDIX/PeeringDB, and reliable press. Do not infer a datacenter from a head office, a telecom exchange, a NOC, an IXP, a CDN cache, a cable landing station, or a reseller page unless a source names a physical colocation/cloud/server-hosting facility.

## 1. Legal and regulatory anchors

| Topic | Verified route | Use | Grade guidance |
|---|---|---|---|
| Telecom law and BTRC | BTRC: http://www.btrc.gov.bd/ ; LIMS: https://lims.btrc.gov.bd/ ; Bangladesh Telecommunication Act, 2001: https://bdlaws.minlaw.gov.bd/act-857.html | Proves telecom-law basis and licensing context for ISP/NTTN/IIG/IGW/ICX/VSAT/mobile operators. | **A** for law, regulator identity, notices, and licence documents. No public DC-specific licence list was found; DC status still needs another source. |
| Company registry | RJSC portal: https://www.roc.gov.bd/ ; name search: https://app.roc.gov.bd/psp/nc_search ; Companies Act, 1994: https://bdlaws.minlaw.gov.bd/act-788.html | Confirm legal entities and SPV names. Full filings may require authenticated/paid access. | **A** for entity existence returned by RJSC; do not treat name search as facility proof. |
| Cybersecurity law | Cyber Security Ordinance, 2025: https://bdlaws.minlaw.gov.bd/act-1538.html ; Prothom Alo/BSS gazette report: https://en.prothomalo.com/bangladesh/government/5gj5obvmuw | Compliance and critical-information-infrastructure context. | **A** for law text; **B** for press interpretation. Not facility evidence. |
| Personal data protection | Personal Data Protection Ordinance, 2025: https://bdlaws.minlaw.gov.bd/act-1574.html ; DLA Piper tracker: https://www.dlapiperdataprotection.com/?c=BD&t=law | Demand/localization signal. Some secondary sources report later Act/ordinance changes; re-check each run. | **A** for official law text; **B/C** for law-firm or blog analysis. Not facility evidence. |
| Cloud/localization policy | Search ICT Division/BCC/BTRC and official laws for cloud, data localization, critical information infrastructure, and government hosting rules. | Context for sovereign cloud and in-country hosting demand. | **A** only when an official policy or law text is found. |

## 2. Official source pipeline

### 2.1 BTRC and telecom licensing

Primary routes: http://www.btrc.gov.bd/ and https://lims.btrc.gov.bd/ . LIMS is an application and document surface, not a reliable public datacenter registry.

Use BTRC to validate operator regulatory context for ISPs, NTTNs, IIGs, IGWs, ICXs, VSAT, mobile networks, and related service categories. If a facility operator says it is licensed, search the operator name plus BTRC terms and then match the legal entity in RJSC.

Queries:

```text
site:btrc.gov.bd ("data center" OR datacenter OR IDC OR colocation OR "ডেটা সেন্টার")
site:lims.btrc.gov.bd (ISP OR NTTN OR IIG OR IGW OR ICX OR license)
"BTRC" "{operator}" ("ISP license" OR NTTN OR IIG OR "data center")
"বিটিআরসি" "{operator}" ("ডেটা সেন্টার" OR "লাইসেন্স")
```

Grade: **A** for BTRC/licence facts. **B/C/U** for facility status unless a primary source names the facility.

### 2.2 BCC, NDC, ICT Division, and a2i

Primary routes: ICT Division https://ictd.gov.bd/ ; BCC https://bcc.gov.bd/ ; NDC https://ndc.bcc.gov.bd/ ; BCC CA contact/address page https://www.bcc-ca.gov.bd/contact ; a2i https://a2i.gov.bd/ .

NDC is a strong official source. The NDC site and service documents name Bangladesh Computer Council at ICT Tower, Agargaon, Dhaka, and describe VPS, load balancer, cloud, managed database, email, and colocation/framework services. Record BCC National Data Center as **A** for existence, government ownership/service, and Agargaon/Dhaka location. Treat tier/capacity claims as **B** unless independently certified.

Queries:

```text
site:ndc.bcc.gov.bd ("National Data Center" OR cloud OR colocation OR VPS OR "ডাটা সেন্টার")
site:bcc.gov.bd ("data center" OR "ডেটা সেন্টার" OR cloud)
site:ictd.gov.bd ("data center" OR cloud OR "ডেটা সেন্টার")
"BCC" "National Data Center" Agargaon Dhaka
```

### 2.3 BDCCL and Meghna Cloud

Primary routes: BDCCL https://bdccl.gov.bd/ ; BDCCL portal pages https://bdccl.portal.gov.bd/ ; Meghna Cloud https://www.meghnacloud.com/ and docs https://docs.meghnacloud.com/ .

BDCCL is the state-owned anchor for the National Data Centre at Bangabandhu Hi-Tech City, Kaliakair, Gazipur. DCD and local press reported Meghna Cloud starting operations in February 2024 at the BDCCL National Data Centre; use those as **B** corroboration for launch timing and reported capacity. BDCCL/Meghna official pages are **A** for service existence and operator identity; Tier IV, "largest", "zero downtime", rack, MW, or cost figures stay **B** unless tied to a certifying body or official engineering filing.

Queries:

```text
site:bdccl.gov.bd ("data center" OR "National Data Centre" OR "Meghna Cloud" OR colocation OR "Tier IV")
site:bdccl.portal.gov.bd "National Data Center"
site:meghnacloud.com Bangladesh ("data center" OR cloud OR GPU OR "Tier-IV")
"BDCCL" (Kaliakair OR Kaliakoir OR Gazipur) ("data center" OR "Meghna Cloud")
```

### 2.4 Bangladesh Hi-Tech Park Authority

Primary routes: BHTPA https://bhtpa.gov.bd/ ; Kaliakair page https://bhtpa.gov.bd/pages/static-pages/6922e01d933eb65569e25897 ; investor OSS https://ossbhtpa.gov.bd/ .

BHTPA proves park, land, investor, and plot context. It does not prove a datacenter unless a park page, official notice, or investor record names a datacenter project. Bangabandhu Hi-Tech City/Kaliakair is the key official host geography for BDCCL, Felicity IDC, Yotta, DataVolt, and other announced projects. Jashore Software Technology Park is important for Khulna-division searches.

Queries:

```text
site:bhtpa.gov.bd ("data center" OR "ডেটা সেন্টার" OR investor OR plot)
site:ossbhtpa.gov.bd (Kaliakoir OR Kaliakair OR Jashore OR Rajshahi OR Sylhet OR Rangpur)
"Bangabandhu Hi-Tech City" ("data center" OR investor OR plot OR Yotta OR DataVolt OR Felicity)
"Sheikh Hasina Software Technology Park" Jashore ("data center" OR colocation OR ICT)
```

### 2.5 RJSC entity matching

Search exact names and variants: Bangladesh Data Center Company Limited, BDCCL, Gennext Technologies, Felicity IDC Limited, DhakaColo Limited, BDCOLO, ColoAsia Limited, Rajshahi Colo, Colocloud, Zorn Ventures/BengalCloud, Aamra Technologies, Fiber@Home Limited, Summit Communications Limited, Summit Group/Summit Technopolis, Grameenphone, Banglalink Digital Communications, Robi Axiata, Teletalk Bangladesh, BTCL, Bangladesh Submarine Cables PLC/BSCCL/BSCPLC, Yotta Bangladesh, DataVolt Bangladesh, Wolast, A Cloud Planet, CoLoCity, Nova Colo, ColoBD.

Queries:

```text
app.roc.gov.bd/psp/nc_search "{company name}"
"{company}" "RJSC" Bangladesh
site:roc.gov.bd "{company}" ("data center" OR datacenter)
```

Grade: **A** for legal entity facts only.

### 2.6 Investment, zones, and procurement

Primary routes: BIDA https://www.bida.gov.bd/ ; Invest Bangladesh https://investbangladesh.gov.bd/ ; BIDA OSS https://oss.bida.gov.bd/ ; BEZA https://www.beza.gov.bd/ (live site may block automated clients with 403); BEPZA https://www.bepza.gov.bd/ ; e-GP https://www.eprocure.gov.bd/ ; BPPA https://www.bppa.gov.bd/e-gp.html ; Planning Commission https://plancomm.gov.bd/ ; IMED https://imed.gov.bd/ .

Use investment and procurement records only when they name the facility/project, owner/SPV, site, tender, award, or PPP. Generic ICT equipment or server-room procurement is a lead only.

Queries:

```text
site:bida.gov.bd OR site:investbangladesh.gov.bd ("data center" OR datacenter OR "digital infrastructure")
site:beza.gov.bd OR site:bepza.gov.bd ("data center" OR ICT OR cloud)
site:eprocure.gov.bd ("data center" OR "ডেটা সেন্টার" OR IDC OR "server room")
site:bppa.gov.bd ("data center" OR e-GP OR tender)
site:plancomm.gov.bd OR site:imed.gov.bd ("data center" OR "National Data Center" OR Kaliakair OR Kaliakoir)
"{agency}" "Annual Procurement Plan" ("data center" OR server OR ICT)
```

Grade: **A** for official tender/award/project facts; **B/C** for press leads until an official record is located.

### 2.7 Development authorities and permits

Primary routes checked: RAJUK https://www.rajuk.gov.bd/ ; CDA https://www.cda.gov.bd/ ; KDA https://www.kda.gov.bd/ ; RDA https://rda.gov.bd/ ; city corporations for local building permits.

Bangladesh does not have a practical national public building-permit keyword search for datacenters. Use development-authority records only when they name the owner, plot, building, project, or land-use approval.

Queries:

```text
site:rajuk.gov.bd ("data center" OR "ডেটা সেন্টার" OR "ICT building")
site:cda.gov.bd OR site:kda.gov.bd OR site:rda.gov.bd ("data center" OR "IT park" OR "server room")
"building permit" "{company}" Bangladesh "data center"
"{city} Development Authority" "{company}" "data center"
```

### 2.8 Power and energy evidence

Primary routes checked: BPDB https://www.bpdb.gov.bd/ ; PGCB https://www.pgcb.gov.bd/ ; DPDC https://www.dpdc.gov.bd/ ; DESCO https://www.desco.org.bd/ (curl timeout from this environment; check browser/manual route during runs); REB https://www.reb.gov.bd/ ; BERC https://berc.org.bd/ .

Use utility evidence for risk, locality, feeder/substation, tariff, outages, and power-availability validation. It rarely proves a datacenter by itself. Do not infer a facility MW load from generator marketing.

Queries:

```text
site:bpdb.gov.bd OR site:pgcb.gov.bd ("data center" OR electricity OR substation OR load)
site:dpdc.gov.bd OR site:desco.org.bd ("data center" OR "large customer" OR outage OR substation)
"Bangladesh" ("load shedding" OR "gas crisis" OR "power shortage") "data center" 2025 2026
"{facility}" (substation OR MW OR generator OR electricity OR gas)
```

## 3. Official query pack

```text
"{division_en}" Bangladesh ("data center" OR datacenter OR IDC OR colocation OR "server room") site:gov.bd
"{division_bn}" ("ডেটা সেন্টার" OR "ডাটাসেন্টার" OR সার্ভার OR কোলোকেশন) site:gov.bd
site:btrc.gov.bd OR site:lims.btrc.gov.bd ("data center" OR NTTN OR ISP OR IIG OR license)
site:ndc.bcc.gov.bd OR site:bcc.gov.bd ("data center" OR cloud OR colocation)
site:bdccl.gov.bd OR site:bdccl.portal.gov.bd ("data center" OR Tier OR Meghna)
site:bhtpa.gov.bd ("data center" OR "hi-tech park" OR investor)
site:eprocure.gov.bd ("data center" OR "ডেটা সেন্টার" OR IDC OR server)
site:bida.gov.bd OR site:investbangladesh.gov.bd ("data center" OR digital OR cloud)
app.roc.gov.bd/psp/nc_search "{company}"
"National Data Center" OR "জাতীয় ডেটা সেন্টার" (Gazipur OR Kaliakair OR Kaliakoir OR Dhaka)
"{operator}" (BTRC OR license OR RJSC) "data center"
```

Bengali/local variants to include: `ডেটা সেন্টার`, `ডাটা সেন্টার`, `ডেটাসেন্টার`, `আইডিসি`, `কোলোকেশন`, `সার্ভার রুম`, `ক্লাউড`, `হাই-টেক পার্ক`, `জাতীয় ডেটা সেন্টার`, plus Chattogram/Chittagong and Kaliakair/Kaliakoir spellings.

## 4. Division-by-division official expectations

| Division | Official posture | Known seeds and required checks |
|---|---|---|
| **Dhaka** | National hub and highest-density division. | Confirm BDCCL National Data Centre/4TDC and Meghna Cloud at Kaliakair/Gazipur; BCC NDC at Agargaon; Felicity IDC at Kaliakair; Fiber@Home, DhakaColo, CoLoCity, Aamra/XeonBD, Wolast, ACP, Gotipath and other Dhaka-city colos. Search BHTPA, RJSC, BTRC, e-GP, RAJUK, DPDC/DESCO. |
| **Chattogram** | Secondary hub plus cable/port/SEZ infrastructure. | Check BTCL/ADB green DC near Chattogram; DhakaColo Chattogram; ColoAsia/NRB Agrabad leads; Colocloud claims; BDIX Chattogram; Cox's Bazar SMW-4 landing. Search CDA, BSCCL/BSCPLC, BEZA/Mirsarai, BPDB/PGCB. |
| **Khulna** | Small but active, driven by Khulna city and Jashore. | Check DhakaColo Jashore/Khulna, ColoAsia Jashore, BengalCloud Khulna/Jashore, Jashore Software Technology Park. Search KDA and BHTPA Jashore pages. |
| **Rajshahi** | Small market with Rajshahi city and Bogura leads. | Check Rajshahi COLO and ColoAsia/Bogura claims; Rajshahi hi-tech park; RDA and local government permits. |
| **Rangpur** | Sparse. | Check Colocloud Rangpur claim and Rangpur hi-tech park/STP. Treat as **no_projects** only after English+Bengali negative sweep. |
| **Sylhet** | Niche but confirmed telco DC. | Verify Grameenphone Super Core DC in Sylhet; DhakaColo/ColoAsia Sylhet claims; Sylhet hi-tech park/STP. |
| **Mymensingh** | No confirmed commercial DC found in current sweep. | Search Mymensingh city, Jamalpur, Netrokona, Sherpur; avoid counting generic `datacenters.com` geographic pages unless they name a facility. |
| **Barishal** | No confirmed commercial DC found; important cable geography. | Verify Kuakata/Patuakhali SMW-5 landing and any BSCCL/BTCL/ISP hosting at the landing station; search Barishal city and Patuakhali in English+Bengali. Cable landing is not a DC without colocation/server-hosting evidence. |

## 5. Known official/primary evidence status

| Facility/project | Division | Status and grade |
|---|---|---|
| BDCCL National Data Centre / 4TDC, Bangabandhu Hi-Tech City, Kaliakair, Gazipur | Dhaka | **Operational. A** for state operator/service/location from https://bdccl.gov.bd/ and portal pages; **B** for reported 200,000 sq ft, generator, cost, and Tier IV marketing unless independently certified. DCD corroboration: https://www.datacenterdynamics.com/en/news/bangladeshs-first-cloud-data-center-starts-operations/ |
| Meghna Cloud, BDCCL/Gennext | Dhaka | **Operational. A** for official service from https://www.meghnacloud.com/ and https://docs.meghnacloud.com/ ; **B** for February 2024 launch, JV history, and location from DCD/Daily Star/Dhaka Tribune. |
| BCC National Data Center, ICT Tower, Agargaon, Dhaka | Dhaka | **Operational. A** from https://ndc.bcc.gov.bd/ and NDC service documents naming BCC/ICT Tower/Agargaon. Capacity/tier claims require separate support. |
| Felicity IDC Limited, Kaliakair Hi-Tech Park | Dhaka | **Operational. A** for operator page https://felicity.net.bd/ and Uptime client page https://uptimeinstitute.com/component/tierachievement/client/felicity-idc-limited/923 . Use Uptime page for certification existence; operator page for sq ft/rack/MW marketing. |
| Fiber@Home colocation | Dhaka | **Operational service. A** for operator co-location page https://www.fiberathome.net/co-location . Facility/address granularity needs per-site confirmation. |
| Grameenphone Super Core Data Center, Sylhet | Sylhet | **Operational. B** from DCD and Bangladeshi press; launched 2024-01-30, 4 MW, GP+ZTE, Tier III standard but not Uptime-listed in the DCD report. Seek GP primary page for **A**. |
| BTCL/ADB green data centre near Chattogram | Chattogram | **Planned/PPP lead. B** from UNB/TBS/DCD January 2025 reports. No operating evidence found; keep status planned until tender/PPP/construction evidence appears. |
| BSCCL/BSCPLC cable landing stations: Cox's Bazar SMW-4; Kuakata SMW-5 | Chattogram; Barishal | **A** for cable landing facts from BSCCL/BSCPLC and Submarine Networks. **U/C** for commercial DC/colo at landing stations unless a primary BSCCL service page names that service and location. |
| DhakaColo / BDCOLO chain | Dhaka, Chattogram, Khulna, Sylhet | **A** for operator claim of multi-city service from https://www.dhakacolo.com/about-us/ and https://bdcolo.net/about ; **C** for individual directory addresses until each physical site is confirmed by operator page, contract, or PeeringDB/facility evidence. |
| ColoAsia | Dhaka, Khulna/Jashore, Sylhet, Rajshahi/Bogura (claims vary) | **A** for operator-owned https://www.coloasiabd.com/ and **C** for colocation.bd/Inflect/DataCenters.com location detail. Verify per physical site before counting. |
| Rajshahi COLO | Rajshahi | **A/C**: operator site https://rajshahicolo.com/ is live and supports service existence; claims and exact facility details need independent support. |
| CoLoCity | Dhaka | **A** for operator site https://colocity.com.bd/ service existence; historical first/Tier claims need **B/C** corroboration. |
| Yotta Dhaka / DataVolt Bangladesh / Summit Group DC | Dhaka | **Planned/announced. B/C/U**. Use DCD, W.Media, TBS, and BHTPA/BIDA searches as leads. Do not mark operational without construction/opening/operator service evidence. |

## 6. Reliability rules

1. Apply grades per field, not per facility. A source can prove existence but not capacity, certification, ownership, or exact coordinates.
2. Operator-owned marketing is **A** for what the operator says exists, but Tier, MW, racks, SLA, and "first/largest" claims remain **B** unless certified or backed by official engineering/procurement records.
3. Directory counts are never authoritative. DatacenterMap, Datacenters.com, DataCentersList, Baxtel, Inflect, OCOLO, DCPulse, and colocation.bd are discovery leads unless the page is clearly operator-controlled.
4. `no_projects` requires logged negative English+Bengali searches, operator searches, official searches, and connectivity searches for that division.
5. Announcements, MoUs, and investment declarations are **planned** until a permit, construction, commissioning, active service page, or opening is found.
6. Cable landing stations, IXP nodes, NOCs, telecom exchanges, and CDN caches must not be counted as datacenters without explicit facility evidence.

## 7. Re-check cadence

- **Monthly:** BTRC notices, e-GP/BPPA tenders, BDCCL/BCC/BHTPA news, DCD/W.Media/TBS/Daily Star/Dhaka Tribune/UNB/BSS searches.
- **Quarterly:** hyperscaler official region lists, Uptime Institute awards, PeeringDB country/IX/facility records, Yotta/DataVolt/Summit/BTCL-green-DC status, BIDA/BEZA/BEPZA project pages.
- **Annual or after legal change:** full 8-division sweep; RJSC entity refresh; legal status of cybersecurity/data-protection/cloud policy; SMW-6 and other cable status.

## 8. Quick URL index

- BTRC: http://www.btrc.gov.bd/ ; LIMS: https://lims.btrc.gov.bd/
- Laws: Telecom Act 2001 https://bdlaws.minlaw.gov.bd/act-857.html ; Companies Act 1994 https://bdlaws.minlaw.gov.bd/act-788.html ; Cyber Security Ordinance 2025 https://bdlaws.minlaw.gov.bd/act-1538.html ; Personal Data Protection Ordinance 2025 https://bdlaws.minlaw.gov.bd/act-1574.html
- ICT/BCC/NDC: https://ictd.gov.bd/ ; https://bcc.gov.bd/ ; https://ndc.bcc.gov.bd/ ; https://www.bcc-ca.gov.bd/contact
- BDCCL/Meghna: https://bdccl.gov.bd/ ; https://bdccl.portal.gov.bd/ ; https://www.meghnacloud.com/ ; https://docs.meghnacloud.com/
- BHTPA/RJSC/procurement: https://bhtpa.gov.bd/ ; https://ossbhtpa.gov.bd/ ; https://www.roc.gov.bd/ ; https://app.roc.gov.bd/psp/nc_search ; https://www.eprocure.gov.bd/ ; https://www.bppa.gov.bd/e-gp.html
- Investment/planning/zones: https://www.bida.gov.bd/ ; https://investbangladesh.gov.bd/ ; https://oss.bida.gov.bd/ ; https://www.beza.gov.bd/ ; https://www.bepza.gov.bd/ ; https://plancomm.gov.bd/ ; https://imed.gov.bd/
- Development/power: https://www.rajuk.gov.bd/ ; https://www.cda.gov.bd/ ; https://www.kda.gov.bd/ ; https://rda.gov.bd/ ; https://www.bpdb.gov.bd/ ; https://www.pgcb.gov.bd/ ; https://www.dpdc.gov.bd/ ; https://www.desco.org.bd/ ; https://www.reb.gov.bd/ ; https://berc.org.bd/
- Connectivity/operators: https://www.bsccl.com.bd/ ; https://www.btcl.gov.bd/ ; https://bdix.net/ ; https://www.peeringdb.com/ix/2516 ; https://felicity.net.bd/ ; https://uptimeinstitute.com/component/tierachievement/client/felicity-idc-limited/923 ; https://www.fiberathome.net/co-location ; https://www.dhakacolo.com/about-us/ ; https://bdcolo.net/about ; https://www.coloasiabd.com/ ; https://rajshahicolo.com/ ; https://colocity.com.bd/
