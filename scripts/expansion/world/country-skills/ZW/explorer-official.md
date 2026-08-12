# ZW Explorer Official - Zimbabwe Datacenter Enumeration via Regulators, Power, Investment, Procurement, and Councils

Date: 2026-08-12. Country: **ZW Zimbabwe**. Division model: **10 provinces**: Bulawayo; Harare; Manicaland; Mashonaland Central; Mashonaland East; Mashonaland West; Matabeleland North; Matabeleland South; Midlands; Masvingo. Angle: **official/regulatory-first datacenter discovery**. Use industry and press sources only as leads unless they are operator-owned pages.

Reliability grades are field-level, not record-level:
- **A** = primary source for the exact field: regulator/government/operator page, POTRAZ licence or Data Protection Authority record, EMA EIA/project document, ZERA licence or ZETDC/ZESA power document, ZIDA investment-licence record, PRAZ/eGP tender/award record, Ministry of ICT or National Data Centre page, council planning/building record, official hyperscale cloud-region page, official law text from ZimLII or Veritas.
- **B** = strong named secondary source: Parliament/PAC reports, state media, national press, reputable local technology press, DCD, ITWeb Africa, Developing Telecoms, Connecting Africa, Capacity, Ecofin Agency, vendor case study, PeeringDB/PCH/IX-F for network presence.
- **C** = lead only: directory entries, social posts, generic market reports, unsupported capacity/address claims, and MoU or conference claims with no site, power, permit, or operator facility page.
- **U** = unverified after this review. Re-check before use.

Count a facility only when a named operator or public body is tied to a physical facility or a datacenter service. Do not count legal demand drivers, licence classes, fibre routes, IXP membership, cloud resale, data-protection registration, or MoUs by themselves. Keep statuses separate: `operational`, `under construction`, `approved`, `planned`, `MoU/intent`, `lead only`, `no confirmed facility found`.

---

## 0. Verified Official Context

- Zimbabwe has **no public national datacenter register** and no single national planning-permit database. Enumeration must join multiple official surfaces: POTRAZ licensing and data-protection records, EMA EIA/project notices, ZERA/ZETDC/ZESA power evidence, ZIDA investment records, PRAZ/eGP procurement notices, Ministry of ICT/National Data Centre material, and city council records.
- Zimbabwe has **ten provinces**, including the city provinces of Bulawayo and Harare. The Government of Zimbabwe portal has province pages for Bulawayo and Harare and uses a province navigation structure; third-party administrative references agree on the ten-province model. Use exactly: Bulawayo; Harare; Manicaland; Mashonaland Central; Mashonaland East; Mashonaland West; Matabeleland North; Matabeleland South; Midlands; Masvingo.
- Harare is the administrative and commercial centre. The official Harare province page describes it as housing the capital city, most head offices, and ICT investment opportunities including Sunway City integrated industrial park. This supports high expected yield but is not facility proof.
- Bulawayo is a city province and industrial/transport hub. The official Bulawayo province page supports separate province treatment; do not merge Bulawayo into Matabeleland for facility records.
- Legal/regulatory basis: telecoms are regulated by **POTRAZ** under the Postal and Telecommunications Act [Chapter 12:05]. Electricity is regulated by **ZERA** under the Energy Regulatory Authority Act [Chapter 13:23], with **ZETDC** as the transmission/distribution company in the ZESA Holdings group. Planning is decentralised under the Regional, Town and Country Planning Act [Chapter 29:12] and Urban Councils Act [Chapter 29:15]. Investment facilitation is through **ZIDA** under the ZIDA Act [Chapter 14:38]. Public procurement is through **PRAZ** and the national eGP portal.
- Data protection: the **Cyber and Data Protection Act [Chapter 12:07] of 2021** is live at ZimLII. Section 5 designates POTRAZ as the Data Protection Authority. The **Cyber and Data Protection (Licensing of Data Controllers and Appointment of Data Protection Officers) Regulations, 2024**, S.I. 155 of 2024, are live at ZimLII/Veritas. POTRAZ's data-controller licensing portal opens and redirects to a login page. This is A-grade legal/demand context, not facility proof.
- Power is a gating filter. Zimbabwe's grid constraints make ZERA, ZETDC, ZESA, captive generation, solar, UPS, generator, fuel-storage, and power-service-agreement evidence decisive. Preserve units exactly: IT MW, facility MW, MVA, kVA, generator kVA, solar/captive MW.
- Confirmed facility provinces from reviewed sources: **Harare** (TelOne Harare service page, government/National Data Centre evidence, Econet EDC press evidence, Liquid/Dandemutande/ZOL leads), **Bulawayo** (TelOne Bulawayo press/operator-social evidence), and **Mashonaland Central** (TelOne Mazowe Earth Station press/operator-social evidence). The other seven provinces remain `no confirmed facility found` unless new evidence is found.
- Zimbabwe is landlocked. There are no subsea cable landing stations inside Zimbabwe; international backhaul arrives via terrestrial routes to regional landing countries. Treat cable/backhaul evidence as viability context only.

Primary official URLs verified in this review:
- POTRAZ: https://www.potraz.gov.zw/ ; licence categories PDF surfaced at https://www.potraz.gov.zw/wp-content/uploads/2022/03/Licence-Categories-Including-Fees.pdf ; DPA portal https://dclicensing.potraz.zw/ ; POTRAZ data-controller guidelines and DP1 forms are linked from POTRAZ/Veritas surfaces.
- Laws/data protection: https://zimlii.org/akn/zw/act/2021/5/eng@2022-03-11 ; https://zimlii.org/akn/zw/act/si/2024/155/eng@2024-09-13 ; https://www.veritaszim.net/node/7187 .
- Energy: https://www.zera.co.zw/ ; https://www.zetdc.co.zw/ ; https://www.energy.gov.zw/ and ZESA group structure at https://www.energy.gov.zw/?page_id=1855 .
- Investment/procurement: https://zidainvest.com/ ; https://eregulations.zidainvest.com/ ; ZIDA Q3 2025 report at https://zidainvest.com/wp-content/uploads/2025/10/ZIDA-QUARTERLY-REPORT-Q3-2025-WEB-1.pdf ; PRAZ https://www.praz.org.zw/praz/ ; eGP https://egp.praz.org.zw/ .
- Government/councils/environment: https://www.ictministry.gov.zw/ ; Ministry projects page https://www.ictministry.gov.zw/pages/projects ; Government portal https://www.zim.gov.zw/ ; Harare province page https://www.zim.gov.zw/index.php/my-government/provinces/harare ; Bulawayo province page https://www.zim.gov.zw/index.php/my-government/provinces/bulawayo ; EMA https://www.ema.co.zw/ ; City of Harare https://www.hararecity.co.zw/ ; City of Bulawayo https://www.citybyo.co.zw/ .
- Companies registry: government/provincial pages cite the Companies and Intellectual Property Office of Zimbabwe and `www.cipz.gov.zw`; the newer online portal is reported as `cipz.pfms.gov.zw`, but both timed out during curl checks in this review. Use as U-grade until reachable.
- Cloud-region pages: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google Cloud https://cloud.google.com/about/locations and Compute regions page https://docs.cloud.google.com/compute/docs/regions-zones ; Oracle https://www.oracle.com/cloud/public-cloud-regions/ ; Uptime certification list https://uptimeinstitute.com/tier-certification/tier-certification-list .

---

## 1. Search Vocabulary

Zimbabwe's datacenter, telecom, government, and press discourse is overwhelmingly **English**. Shona and Ndebele searches are low-yield and loanword-heavy; use them only as a completeness sweep.

English terms:
```text
data centre / data center / datacentre
server farm / server room / server hosting
colocation / colo / co-location / carrier-neutral
hosting / web hosting / managed hosting / dedicated servers
cloud / local cloud / sovereign cloud / IaaS / PaaS / SaaS / Azure Stack / edge
Tier III / Tier 3 / Tier III by design / Uptime Institute
network operations centre / NOC / internet exchange point / IXP / peering
fibre / backbone / international gateway / backhaul / SEACOM / EASSy / WACS
data sovereignty / data localisation / disaster recovery / business continuity
power / solar / backup generator / captive power / PPA / ZESA / ZETDC / load-shedding
```

Shona/Ndebele sweep terms:
```text
"data centre" Zimbabwe Shona Ndebele
indaneti / maseva / kombuta
"nzvimbo yekuchengetedza data" / "isikhungo sedatha"
```

---

## 2. POTRAZ and Data-Protection Trail

POTRAZ is A-grade for operator licensing, telecom service categories, and data-controller regulatory context. It is **not** A-grade for a datacenter facility unless the document names a physical site or datacenter service.

Use POTRAZ to verify:
- Licence holder, legal name, service class, issue/renewal facts, gateway/data-network rights, and public notices.
- Data-controller/processer registration status when a public result is available. The DPA portal is real but login-gated; do not infer registration from inability to search.
- Sector reports and consultations mentioning data centres, cloud, hosting, international gateway, digital infrastructure, or Digital Centres.
- Starlink/IMC licensing as connectivity evidence only unless POTRAZ names a facility.

Query templates:
```text
site:potraz.gov.zw "data centre" OR "data center"
site:potraz.gov.zw "cloud" OR "hosting" OR "Public Data Network" OR "International Gateway"
site:potraz.gov.zw "data controller" OR "Data Protection Authority" OR "DP1"
site:dclicensing.potraz.zw "data controller" OR "register"
"POTRAZ" "{operator}" "licence" Zimbabwe
"POTRAZ" "Starlink" OR "IMC" licence Zimbabwe
"Cyber and Data Protection" "S.I. 155 of 2024" Zimbabwe
```

Extract: legal name, licence type, date, licence/reference number if public, authorised service, town/province if stated, source URL, grade, and whether the evidence is facility, service, network, or legal-context only.

---

## 3. Power Trail - ZERA, ZETDC, ZESA

Power evidence is the best official discriminator between a real facility and a hosting/cloud marketing claim.

Use:
- **ZERA** for generation, transmission, distribution, supply, captive/IPP, and fuel-storage licensing.
- **ZETDC** for large-load connections, substations, feeders, energisation, tenders, power-service agreements, and meter/transformer evidence.
- **ZESA Holdings / Ministry of Energy** for group structure and power-sector context, including Powertel as a telecom lead, not a datacenter operator unless a facility is named.
- **Captive/solar evidence** for planned AI/data-centre parks, especially Econet InfraCo's reported 100 MW solar-backed park near Robert Gabriel Mugabe International Airport.

Query templates:
```text
site:zera.co.zw "{operator}" OR "data centre" OR "ICT" OR "licence"
site:zera.co.zw "generation" OR "captive" OR "solar" "licence" "{project}"
site:zetdc.co.zw "data centre" OR "server" OR "cloud"
site:zetdc.co.zw "{operator}" "substation" OR "MVA" OR "33kV" OR "66kV" OR "132kV"
site:energy.gov.zw "data centre" OR "digital" OR "ICT" OR "Powertel"
"{project}" "power supply agreement" OR "PPA" OR "captive power" Zimbabwe
site:egp.praz.org.zw "ZETDC" "substation" OR "ICT" OR "data"
```

Never convert MVA/kVA to MW or IT load. Record source wording exactly.

---

## 4. ZIDA and Investment Records

ZIDA is A-grade for investment-licence facts and investment-policy context, but not facility completion. Its quarterly reports can identify ICT, energy, infrastructure, and SEZ projects that may later become datacenter candidates.

Use ZIDA for:
- ICT/digital/datacenter investment licences, sector classification, province/district, capex, and implementation status.
- SEZ and industrial-park leads, including Sunway City and reported Harare airport industrial/IT park concepts.
- eRegulations workflows for company registration and licensing context.

Query templates:
```text
site:zidainvest.com "data centre" OR "data center" OR "ICT" OR "cloud" OR "digital"
site:zidainvest.com "investment licence" "{operator}" Zimbabwe
site:zidainvest.com "quarterly report" "ICT" OR "technology" OR "infrastructure"
"ZIDA" "special economic zone" "ICT" OR "data" Zimbabwe
site:eregulations.zidainvest.com "ICT" OR "licence" OR "company registration"
```

Extract: investor/SPV, licence number if public, sector, capex, location, power/water/fibre claims, status, source URL, grade.

---

## 5. PRAZ / eGP Procurement Trail

The eGP portal is A-grade for tender and award facts. It does not by itself prove a datacenter is operational.

Verified high-value procurement lead:
- eGP tender details page for **OPC/DATACENTR/D/10/2025**, Tender Id 42451, closed, direct procurement, non-consulting services, GoZ Treasury funding, delivery/project location **Munhumutapa Building**. Treat as A-grade procurement evidence and a government-facility lead; do not count as a standalone public colocation facility without scope/award/implementation evidence.

Use eGP for:
- Tenders and awards naming data centres, server rooms, cloud, hosting, DR, backup, NOC, cybersecurity centres, or ICT infrastructure.
- Procuring entity, location, contract reference, supplier, value, and delivery date.
- ZETDC/ZESA/TelOne/ministry ICT procurements that reveal power or facility work.

Query templates:
```text
site:egp.praz.org.zw "data centre" OR "data center" OR "DATACENTR" OR "server" OR "cloud" OR "hosting"
site:egp.praz.org.zw "ICT infrastructure" OR "disaster recovery" OR "backup"
site:egp.praz.org.zw "TelOne" OR "ZETDC" OR "Ministry of ICT" OR "OPC"
site:praz.org.zw "data centre" OR "digital" OR "e-government"
"PRAZ" "tender" "data centre" Zimbabwe
"eGP" "{operator}" "data centre" OR "cloud" Zimbabwe
```

---

## 6. Ministry, Councils, EMA, and National Data Centre

- **Ministry of ICT**: the official projects page says the National Data Centre Project Priority Document covers development and implementation of centralized data infrastructure. The National Broadband Plan 2023-2030 PDF references IXPs, the fibre backbone, and the National Data Centre. Use this as A-grade policy/project context; seek project documents, operator pages, or procurement records for facility details.
- **National Data Centre**: Techzim's 2017 TelOne launch coverage says the TelOne Harare data-centre/cloud launch was described as the first phase of the National Data Centre; Bulawayo24 reported a February 2021 commissioning by the President. These are B-grade for date/existence unless the Ministry/OPC page names the exact facility details.
- **Councils**: Harare and Bulawayo have official sites. Building/planning records are not consistently searchable. Council minutes/permits are A-grade only for the exact permit facts.
- **EMA**: use for EIA/project brief, generator, fuel-storage, substation, and commercial/ICT-building notices. The EMA site is live, but datacenter-specific EIA page paths were not confirmed.

Query templates:
```text
site:ictministry.gov.zw "data centre" OR "National Data Centre" OR "cloud" OR "e-government"
site:ictministry.gov.zw "National Broadband Plan" "data centre"
site:zim.gov.zw "data centre" OR "ICT" OR "digital" "{province}"
site:hararecity.co.zw "data centre" OR "TelOne" OR "Econet" OR "building plan"
site:citybyo.co.zw "data centre" OR "TelOne" OR "building"
site:ema.co.zw "data centre" OR "ICT" OR "telecom" OR "generator" OR "fuel storage"
"EMA" "project brief" OR "EIA" "{operator}" Zimbabwe
"National Data Centre" Zimbabwe e-government TelOne Huawei
```

---

## 7. Companies Registry - CIPZ / DCIP

Use Companies and Intellectual Property Office/Registry evidence only to confirm legal names, SPVs, directors, and registered offices. It has no land-use or facility data. The official online registry endpoints were not reliably reachable during this review (`cipz.gov.zw` and `cipz.pfms.gov.zw` timed out), though government/provincial pages cite CIPZ/DCIP. Grade registry URL availability as U until opened live.

Query templates:
```text
"CIPZ" OR "Companies and Intellectual Property" "{operator}" Zimbabwe
"DCIP" "{operator}" Zimbabwe
"Registrar of Companies" Zimbabwe "{operator}" OR "data centre"
"{operator}" "certificate of incorporation" Zimbabwe "Chapter 24:31"
```

---

## 8. Official Cloud-Region and Certification Status

| Provider / certifier | Verified official source | Zimbabwe status on 2026-08-12 | Rule |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Zimbabwe AWS Region found; Africa offering is South Africa-based. | Reseller, partner, Direct Connect, Outposts, edge/cache claims are not a Zimbabwe Region. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Zimbabwe public Azure region; South Africa North is Johannesburg and South Africa West is Cape Town. | Azure Stack/local cloud is hybrid/private, not a public Azure region. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | No Zimbabwe region; `africa-south1` zones are Johannesburg, South Africa. | CDN/cache claims are network evidence only. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Zimbabwe OCI public region; South Africa Central (Johannesburg) is live. | Recheck official page before accepting any OCI Zimbabwe claim. |
| Uptime Institute | https://uptimeinstitute.com/tier-certification/tier-certification-list | No Zimbabwe certification found in searched results. | Operator `Tier 3`, `Tier III by design`, or `Tier 3 environment` wording is not certification unless Uptime lists the facility. |

Annual verification query:
```text
site:aws.amazon.com Zimbabwe "Region"
site:learn.microsoft.com/azure Zimbabwe region
site:cloud.google.com Zimbabwe "africa-south1" OR "Zimbabwe"
site:oracle.com/cloud Zimbabwe region
site:uptimeinstitute.com Zimbabwe "TelOne" OR "Econet" OR "Dandemutande"
```

---

## 9. Per-Province Official Enumeration Strategy

| Province | Capital / seat | Official anchors | Strategy and expected yield |
|---|---|---|---|
| **Harare** | Harare | POTRAZ HQ; Ministry of ICT; ZIDA; PRAZ/eGP; ZERA/ZETDC; EMA HQ; City of Harare; National Data Centre; TelOne Runhare House; Econet EDC; Liquid; Dandemutande; ZOL; ZINX/HIX | **Primary hub.** Confirm TelOne official services, National Data Centre documents, Econet EDC procurement/power/official pages, Liquid/Dandemutande/ZOL facility evidence, council building plans, EMA generator/fuel records, ZETDC loads, ZIDA licences, and eGP tenders. |
| **Bulawayo** | Bulawayo | City of Bulawayo; ZETDC regional; ZIDA regional; ZITF; TelOne Bulawayo | **Secondary node.** Confirm TelOne Bulawayo via official/operator or council records; rack/power figures are B unless TelOne/council/power record confirms. Watch bank DR and ZITF ICT announcements. |
| **Mashonaland Central** | Bindura | Mazowe District; TelOne Mazowe Earth Station; ZETDC; provincial administration | **Low but one real asset.** Map Mazowe Earth Station to Mashonaland Central, not Harare, even when directories file it under Harare. Seek TelOne, ZETDC, and EMA evidence. |
| **Manicaland** | Mutare | Provincial administration; ZETDC/EMA; Harare-Beira corridor | **Very low watch.** Search Mutare/border/fibre PoPs; count only physical facility evidence. |
| **Mashonaland East** | Marondera | Provincial administration; City of Marondera; Sunway/Ruwa context | **Very low watch.** Search government/agriculture ICT, Ruwa/Sunway digital projects, and server rooms. |
| **Mashonaland West** | Chinhoyi | Provincial administration; Kariba power context; ZETDC | **Very low watch.** Search Chinhoyi/Kariba ICT and power-sector digital infrastructure; no confirmed DC. |
| **Matabeleland North** | Lupane; Victoria Falls commercial centre | Hwange power context; Victoria Falls tourism/finance; ZETDC | **Very low watch.** Search Victoria Falls and Hwange for ICT/power leads; no confirmed DC. |
| **Matabeleland South** | Gwanda | Beitbridge border/logistics corridor; ZETDC | **Very low watch.** Border ICT only unless facility documents appear. |
| **Midlands** | Gweru | ZETDC; mining; Somabhula fibre node lead | **Very low watch.** Dandemutande Somabhula is connectivity evidence, not a facility. Search Gweru/Kwekwe/mining DR. |
| **Masvingo** | Masvingo | Provincial administration; Masvingo City Council; POTRAZ Digital Centres | **Very low watch.** Digital Centres/Starlink upgrades are connectivity infrastructure, not datacenters. Record no confirmed facility unless new evidence appears. |

Province query block:
```text
"{province}" "data centre" OR "data center" Zimbabwe
"{capital}" "data centre" OR "server room" OR "hosting" Zimbabwe
site:zim.gov.zw "{province}" "ICT" OR "digital" OR "data"
site:egp.praz.org.zw "{province}" OR "{capital}" "ICT" OR "server" OR "data" OR "DATACENTR"
site:ema.co.zw "{capital}" OR "{province}" "ICT" OR "generator" OR "fuel"
site:zera.co.zw "{capital}" OR "{province}" "licence" OR "substation"
site:potraz.gov.zw "{province}" "Digital Centre" OR "connectivity" OR "licence"
"{capital}" "TelOne" OR "Econet" OR "NetOne" OR "Liquid" OR "Dandemutande" OR "ZOL"
```

---

## 10. Extraction Checklist

For each candidate, record field-level grades:
- Facility/operator: legal name, brand, SPV, government body.
- Status: MoU/intent, announced, approved, under construction, operational, closed/unknown.
- Location: province, district, city/town, plot/stand/address, coordinates, precision source.
- Official permits: POTRAZ licence/DPA, ZERA power licence, ZETDC connection/PSA, ZIDA investment licence, EMA EIA/project brief, council planning/building/occupancy, PRAZ/eGP contract.
- Technical: exact tier wording, certification status, IT load/facility load/MVA/kVA, racks/cabinets, halls, UPS, generator, fuel, cooling/water, ISO/PCI/Uptime certifications.
- Connectivity: carriers, IXP membership, gateway licence, fibre routes, meet-me room, CDN/cache, international backhaul.
- Cloud/service: colocation, private cloud, public cloud resale, DR, backup, government-only or commercial availability.
- Sources: URL, title, publisher, publication date, access date, grade, exact field supported.

Red flags: cloud region without official hyperscaler page; `Tier 3` upgraded to certified without Uptime listing; directory address without operator/council support; MoU counted as construction; social post treated as primary; MVA/kVA converted to MW; Mazowe filed under Harare; provinces omitted because searches had no hits.

---

## 11. Update Cadence

- POTRAZ licences, DPA, and sector reports: quarterly.
- ZIDA reports and investment licences: quarterly.
- PRAZ/eGP tenders and awards: monthly for `data centre`, `DATACENTR`, `cloud`, `server`, `hosting`, `DR`, `backup`.
- EMA and council notices: monthly for Harare/Bulawayo; quarterly/triggered for other provinces.
- ZERA/ZETDC/ZESA power evidence: quarterly.
- Ministry of ICT/National Data Centre/e-government announcements: monthly.
- Cloud-region and Uptime certification pages: annually and on any Zimbabwe cloud-region/Tier-certification claim.
- CIPZ/DCIP: on new SPV/operator announcements, only after live registry access is confirmed.
