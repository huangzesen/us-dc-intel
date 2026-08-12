# MW Explorer Official - Malawi Datacenter Enumeration via Regulators, Power, Procurement, Government Cloud, and Councils

Date: 2026-08-12. Country: **MW Malawi**. Division model: **3 regions**: Central Region; Northern Region; Southern Region. Angle: **official/regulatory-first datacenter discovery**. Use industry and press sources only as leads unless they are operator-owned pages.

Reliability grades are field-level, not record-level:
- **A** = primary source for the specific field: regulator/government/operator page, MACRA licence or consultation, MERA/ESCOM/EGENCO power document, PPPC/DIGMAP or PPDA procurement record, Ministry of Information/Department of e-Government page, RBM tender/bank record, MITC/SEZ instrument, council planning/building record, official hyperscale region page, operator-owned facility page.
- **B** = strong named secondary source: DCD, ITWeb Africa, Capacity, Developing Telecoms, Connecting Africa, Xinhua, Nyasa Times, The Nation, Maravi Post, Malawi Voice, MANA, vendor case study, PeeringDB/IXP page for network presence.
- **C** = lead only: directory entry, social post, generic market report, old MoU with no site/power/permit evidence, unsupported capacity/address claim, academic concept paper.

Do not count a datacenter from a legal demand driver, licence class, fibre route, IXP membership, cloud resale, or MoU alone. Count only when a named operator or public body is tied to a physical facility or data-centre service; keep status values separate: `operational`, `under construction`, `approved`, `planned`, `MoU/intent`, `lead only`.

---

## 0. Official Malawi Facts That Shape Enumeration

- Malawi has **no public national datacenter register** and no unified national planning-permit database. Enumerate by joining official surfaces: MACRA (communications licensing **and** Data Protection Authority under the Data Protection Act 2024), Ministry of Information/Department of e-Government (ict.gov.mw), PPPC/DIGMAP (World Bank Digital Malawi Acceleration Project), the PPDA/PPPC/RBM procurement trail, MERA/ESCOM/EGENCO power evidence, MITC investment/SEZ instruments, and Lilongwe/Blantyre/Mzuzu council planning records.
- Malawi is divided into **three regions** (Central, Northern, Southern) and 28 districts; use exactly the three manifest divisions: `Central Region`, `Northern Region`, `Southern Region`. The capital is **Lilongwe** (Central Region); the commercial capital is **Blantyre** (Southern Region); the main Northern city is **Mzuzu**.
- The government runs a **dual national data-centre architecture**: the **Government Data Centre in Lilongwe** (World Bank-funded, under PPPC/DIGMAP, designed as the **Primary** data centre, hyper-converged infrastructure) and the **National Data Centre in Blantyre** (Huawei-built, commissioned July 2022, officially designated the **Secondary/Backup** data centre). Both are official/operator-grade seeds; neither has disclosed MW capacity.
- **Power is a gating filter.** Malawi's grid is capacity-constrained; use MERA tariff and licence filings, ESCOM notices, EGENCO supply statements, and candidate-specific UPS/generator/connection evidence before treating any "cloud" claim as facility-grade. Backup generation, fuel storage, UPS, solar/captive generation, BESS, and power supply agreements are decisive evidence fields for any candidate facility.
- The **Data Protection Act No. 3 of 2024** (gazetted February 2024, in force 3 June 2024) designates **MACRA as the Data Protection Authority**. Registration of data controllers/processors is live via the DPA (dpa.mw); in June 2026 MACRA invited comments on proposed registration fees for Data Controllers and Data Processors of Significant Importance. The Act is A-grade demand/legal context, **not facility proof**; do not infer a datacenter from a registration alone.
- **Official public cloud-region status**, checked against provider region pages on 2026-08-12: **no AWS, Microsoft Azure, Google Cloud, Oracle OCI, or Huawei Cloud public region is listed in Malawi.** Nearest public regions are in South Africa (Johannesburg/Cape Town). Treat any Malawi "cloud region" claim as local/hybrid/partner cloud unless an official provider region page lists Malawi.
- Honest yield statement: this review identifies **about 6-8 official/operator-grade datacenter records or procurement records**, all in Central and Southern Regions, and **no verified Northern Region facility**. Public sources disclose **no IT MW or facility MW capacity for any Malawi datacenter**; expect `capacity_mw` to remain null unless new official disclosures appear. Do not convert kVA/UPS figures into MW.

Primary URLs verified for use (checked 2026-08-12):
- MACRA: https://macra.mw/ ; telecoms directorate: https://macra.mw/telecommunications/ ; broadcasting licensing: https://macra.mw/broadcasting/
- Data Protection Authority: https://www.dpa.mw/ ; Act download: https://www.dpa.mw/download/data-protection-act-2024/ ; gov.mw acts page: https://www.malawi.gov.mw/index.php/resources/publications/acts?download=153:data-protection-act-2024 . Do not use the old mca.ac.mw mirror unless re-verified; it returned 404 on 2026-08-12.
- Ministry of Information / ICT: https://ict.gov.mw/index.php/home ; e-Government: https://ict.gov.mw/index.php/services/e-government ; National Fiber Backbone: https://ict.gov.mw/index.php/projects/national-fiber-backbone ; Digital Malawi: https://ict.gov.mw/index.php/projects/digital-malawi
- DIGMAP (PPPC): https://digmap.pppc.mw/ ; Government Data Centre progress article: https://digmap.pppc.mw/government-data-center-making-progress/ ; PPPC procurement: https://www.pppc.mw/ ; NDC expansion RFB page: https://www.pppc.mw/procurement/reports-notices/request-for-bids-goods-two-envelope-bidding-process-procurement-of-expansion-of-national-data-centre ; RFB PDF: https://api.pppc.mw/api/download/722 ; older early-market page: https://www.pppc.mw/procurement/reports-notices/invitation-to-early-market-engagement-expansion-of-the-national-data-centre
- World Bank results brief (Malawi DIGMAP data centre, Jun 2025): https://www.worldbank.org/en/results/2025/06/23/digitalizing-afe-malawi-to-improve-access-to-education-public-services-and-income-opportunities
- MERA: https://mera.mw/ ; 2022-26 base tariff application: https://mera.mw/2022/08/15/2022-26-electricity-base-tariff-application/
- ESCOM: https://www.escom.mw/
- MITC: https://www.mitc.mw/
- RBM: https://www.rbm.mw/ (CDC Invitation to Bid: https://www.rbm.mw/Home/GetContentFile/?ContentID=62075)
- OCL (operator): https://www.ocl.mw/tier3.html ; https://www.ocl.mw/
- MTL (operator): https://www.mtl.mw/hosted-services/datacentre/ (valid page, but local curl required `-k` on 2026-08-12 because the TLS chain did not verify)
- Cloud region pages: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google https://cloud.google.com/about/locations ; Oracle https://www.oracle.com/cloud/public-cloud-regions/ ; Huawei https://www.huaweicloud.com/intl/en-us/

---

## 1. MACRA - Communications Licensing and the Data Protection Authority

MACRA, established under the Communications Act 1998 (Cap. 68:01), licenses telecommunications, internet, and broadcasting operators in Malawi. Since the Data Protection Act 2024 it also functions as the **Data Protection Authority**, registering data controllers and processors. MACRA is an A-grade surface for operator existence and legal obligations, but not for floor area, MW, racks, or operational datacenter status unless a MACRA document explicitly names a facility.

Use MACRA to verify:
- Operator legal names and licence classes (telecom service provider, ISP, international gateway, VSAT, broadcasting/content, postal/courier).
- Licencing news that reveals infrastructure ambition: e.g., DCD reported MACRA was close to granting **Malcel** a licence as Malawi's third mobile operator (2022) - a network/spectrum lead, not a DC proof.
- Data protection registration flows and the June 2026 consultation on registration fees for Data Controllers/Data Processors of Significant Importance - demand-side signal for cloud/DC operators.
- Consultations, market reports, and enforcement notices that mention data centres, cloud, hosting, gateways, or network infrastructure.

Query templates:
```text
site:macra.mw "data centre" OR "data center" OR "cloud" OR "hosting"
site:macra.mw "licence" "{operator}" (e.g., TNM, Airtel, MTL, OCL, SimbaNet)
site:macra.mw "international gateway" OR "gateway licence"
site:macra.mw "data controller" OR "data processor" OR "Data Protection Act"
site:macra.mw "consultation" "2026"
"MACRA" "{operator}" "licence" Malawi
"MACRA" "data centre" OR "server" Malawi
"{operator}" "MACRA" "registration" Malawi
```

Extraction fields: licence holder, licence class/type, issue/renewal date, licence number if public, authorised services, gateway rights, region/town if stated, data-protection registration status, source URL, grade.

---

## 2. Data Protection Act 2024 - Registration and Cross-Border Demand

The Data Protection Act No. 3 of 2024 is Malawi's first comprehensive data protection law (it replaced the data-protection provisions of the Electronic Transactions and Cyber Security Act 2016). It came into force 3 June 2024; MACRA is the supervisory authority and operates the Data Protection Authority portal at dpa.mw. The Act regulates processing of personal data, imposes obligations on controllers/processors (including cloud and hosting providers that process personal data), and conditions cross-border transfers - **demand context for domestic hosting, not proof of any facility**.

Use DPA evidence for:
- Demand screening: financial, telecom, health, government, education, mobile-money, and cloud-service sectors are the most likely consumers of domestic hosting/colocation.
- Identifying registered controllers/processors if a public register or export becomes available.
- Cross-border-transfer/storage authorisation signals that may motivate domestic DC demand.

Query templates:
```text
site:dpa.mw "data centre" OR "data center" OR "hosting" OR "registration"
site:dpa.mw "transfer" "outside Malawi" OR "cross-border"
site:dpa.mw "controller" "processor" "register"
"Data Protection Act 2024" "transfer" "Malawi" "safeguards"
"{operator}" "data controller" OR "data processor" Malawi
"Malawi" "data localisation" "data centre"
```

Extract: registration status of candidate operators (if public), legal basis notes, transfer conditions, enforcement notices naming data centres or hosting providers, and any explicit storage-location statements.

---

## 3. Ministry of Information and Digitalisation - e-Government and National Infrastructure

The Ministry of Information (ict.gov.mw) hosts the **Department of E-Government**, which leads government-wide ICT, including the **National Fiber Backbone** and **Digital Malawi** projects. This is the A-grade surface for the government's own data-centre assets and the policy drivers behind them (Malawi 2063 digitalisation agenda, Digital Economy Strategy 2021-2026).

Use ict.gov.mw to verify:
- The existence and role of the National Data Centre (Blantyre) and the Government Data Centre (Lilongwe) in official messaging.
- National Fiber Backbone scope - the backbone is a connectivity driver, **not** a DC proof.
- e-Government services that consume government hosting (e.g., Boma Mail, government portals), useful as demand evidence.
- Ministerial statements, project pages, and press releases that name data centres, cloud, or hosting procurements.

Query templates:
```text
site:ict.gov.mw "data centre" OR "data center" OR "National Data Centre" OR "Government Data Centre"
site:ict.gov.mw "cloud" OR "hosting" OR "server"
site:ict.gov.mw "National Fiber Backbone" OR "Digital Malawi"
"Department of e-Government" "data centre" Malawi
"{operator}" "Department of e-Government" OR "Ministry of Information" Malawi
```

Extract: named facility, ministry/department, project phase, official description, procurement reference, region/city if stated, date, source URL, grade.

---

## 4. PPPC, DIGMAP, and World Bank Records

The **Public Private Partnership Commission (PPPC)** implements the **Digital Malawi Acceleration Project (DIGMAP)** with World Bank funding, including the Government Data Centre in Lilongwe. PPPC/DIGMAP and World Bank pages are A-grade for government data-centre projects.

Verified official records:
- **Government Data Centre / National Data Centre Production Site, Lilongwe (Primary)**: DIGMAP article of 1 Mar 2024 states the facility was under construction in Lilongwe, 51% complete, expected completion May 2024, with hyper-converged infrastructure (HCI), built to complement the existing Blantyre data centre, with Lilongwe designated **Primary** and Blantyre **Secondary/Backup**. World Bank results brief (23 Jun 2025) confirms a new data centre in Lilongwe was constructed for government hosting. Status: `operational` for existence after World Bank 2025, unless the current run requires commissioning-date precision. No MW disclosed.
- **Expansion of the National Data Centre, Lilongwe**: PPPC RFB/PDF ref **MW-PPPC-494042-GO-RFB** is for expansion of the National Data Centre under the Digital Malawi Acceleration Project. The RFB names the final destination/project site as the National Data Centre off/along Paul Kagame Road in Lilongwe, states the existing Production Site is a **Tier-III facility**, and says the Department of e-Government built the Lilongwe national data centre and is increasing its capacity. It discloses two 160 kVA UPS systems and HCI node details, but **not MW capacity**. Status: `planned` or `procurement` until award/commissioning evidence appears.

Query templates:
```text
site:digmap.pppc.mw "data centre" OR "data center" OR "cloud"
site:pppc.mw "data centre" OR "National Data Centre" OR "Government Data Centre"
site:worldbank.org "Malawi" "data centre" OR "data center" "DIGMAP"
"PPPC" "{operator}" "data centre" Malawi
"MW-PPPC" "data centre" OR "Data Centre"
"MW-PPPC-494042-GO-RFB" "National Data Centre" "Lilongwe"
"api.pppc.mw/api/download/722" "National Data Centre"
"DIGMAP" "Government Data Centre" Lilongwe
```

Extract: project name, implementing body, funding source, phase/completion percentage, facility role (primary/secondary), tier wording, procurement reference, dates, capacity if disclosed, source URL, grade.

---

## 5. Procurement Trail - PPDA, PPPC, and RBM Tenders

Malawi public-sector data-centre builds frequently surface first as procurement notices: the PPPC/PPDA e-procurement system (and ministry-specific portals such as dmap.staging.ict.gov.mw and RBM's own site) publish ITBs, RFPs, and contract awards. This trail is the single most productive official surface for **new/planned** facilities, including bank and government DCs.

Verified tender example:
- **Reserve Bank of Malawi Corporate Data Centre (CDC), Blantyre Branch**: Invitation to Bid ref **RBM/ICT/BT/01/2025**, issued 13 Nov 2025, for design and construction of a modern Corporate Data Centre at the RBM Blantyre branch; bids due 3 Dec 2025 at 10:00 (primary source: RBM ITB PDF on rbm.mw; secondary aggregators are lead-only cross-checks). Status: `planned` (tender stage). No MW disclosed.

Query templates:
```text
site:ppda.mw "data centre" OR "data center" OR "server room" OR "ICT infrastructure"
site:pppc.mw "data centre" OR "early market engagement"
site:rbm.mw "data centre" OR "Corporate Data Centre" OR "ICT"
"RBM/ICT/BT/01/2025" "Corporate Data Centre" "Blantyre"
"{bank/agency}" "data centre" "tender" OR "invitation to bid" Malawi
"Malawi" "design and construction" "data centre" 2025 OR 2026
site:malawitenders.com "data centre"
```

Extract: procuring entity, reference number, publication/closing dates, facility location, scope wording (new build vs fit-out), award announcement and contractor when published, source URL, grade.

---

## 6. Power Trail - MERA, ESCOM, EGENCO

Power evidence separates credible datacenters from marketing claims. Malawi's national grid is capacity-constrained; any serious DC must show backup generation, UPS, fuel storage, solar/captive generation, or a power supply agreement.

Official source roles:
- **MERA** (Malawi Energy Regulatory Authority): electricity licence requirement and licensee information for generation/transmission/distribution/supply; tariff filings (e.g., the 2022-26 base tariff application documents load shedding of up to ~10 hours/day) are A-grade grid-context evidence.
- **ESCOM** (Electricity Supply Corporation of Malawi): distribution network, substations, feeders, load-shedding schedules, BESS/energy projects (12 BESS containers delivered to Kanengo, Lilongwe from Jan 2026), and connection notices. ML.mw (B/C) says ESCOM itself operates a datacenter - treat as a `lead only` until an official ESCOM page confirms it.
- **EGENCO** (Electricity Generation Company): generation supply position (about 500 MW vs ~1,000 MW demand per Aug 2025 statements) - decisive context for grid reliability assumptions.

Query templates:
```text
site:mera.mw "data centre" OR "data center" OR "captive power" OR "backup"
site:mera.mw "licence" "{operator}"
site:escom.mw "data centre" OR "data center" OR "server" OR "ICT"
site:escom.mw "{operator}" "substation" OR "MVA" OR "33kV" OR "66kV" OR "132kV"
site:escom.mw "Kanengo" OR "BESS" OR "load shedding"
site:egenco.mw "generation" "MW" "2025"
"{project}" "power supply" OR "captive power" OR "PPA" Malawi
"{operator}" "backup generators" OR "UPS" OR "fuel" Malawi
```

Preserve units exactly. Record whether a number is IT MW, facility MW, connected load, MVA, generator kVA, or solar/captive MW. Never convert MVA to MW unless the source does. For Malawi, expect no public MW figures for DCs at all; record `null` rather than inventing.

---

## 7. Investment Trail - MITC, SEZ, and Trade Records

The **Malawi Investment and Trade Centre (MITC)** is the one-stop investment promotion body (alongside the Ministry of Trade and Industry, MRA, RBM, and PPPC per the U.S. Investment Climate Statement). Malawi's Special Economic Zones programme is governed by the **Special Economic Zones Act of 2025**; MITC has run China-Malawi SEZ investment forums (Aug 2025) and land has been identified for pioneer zones. No SEZ-specific datacenter tenant has been verified as of 2026-08-12 - monitor only.

Query templates:
```text
site:mitc.mw "data centre" OR "data center" OR "ICT" OR "digital"
site:mitc.mw "special economic zone" "{zone}"
"Malawi" "SEZ" "data centre" OR "ICT park"
"{operator}" "MITC" "investment" Malawi
"Malawi" "Special Economic Zones Act 2025"
```

Extract: investor name, SEZ/zone, sector, announced capex, jobs, power/water/fibre commitments, status (MoU/commitment/operational), source URL, grade.

---

## 8. Financial-Sector Records - RBM and Banks

The **Reserve Bank of Malawi (RBM)** licences banks and issues its own ICT infrastructure tenders (see Section 5: RBM Corporate Data Centre, Blantyre). Malawi's commercial banks operate in-house datacenters (ML.mw, B/C) to meet RBM business-continuity and data-residency expectations; bank DCs are only counted when a named bank/facility is confirmed by a primary or strong secondary source, not from generic "banks have data centres" statements.

Query templates:
```text
site:rbm.mw "data centre" OR "ICT" OR "business continuity"
site:rbm.mw "{bank}" "data centre"
"{bank}" "data centre" Malawi "disaster recovery" OR "DR site"
"Reserve Bank of Malawi" "data centre" 2025
```

---

## 9. Council Planning and Building Permits

City council planning/building departments are the A-grade surface for new-build confirmation, but Malawian councils publish little searchable permit data. Prioritise Lilongwe City Council (Central), Blantyre City Council and Zomba (Southern), and Mzuzu City Council (Northern); search council sites, minutes, and planning departments, and cross-check via the Ministry of Local Government local-authority directory. Candidate domains to verify on first use: lcc.gov.mw (Lilongwe), bcc.mw (Blantyre), and the Mzuzu City Council site.

Query templates:
```text
site:{council-domain} "data centre" OR "data center" OR "server" OR "ICT"
site:{council-domain} "building permit" OR "planning" "{operator}"
"{council}" "planning" "data centre" Malawi
"{capital}" "stand" OR "plot" "data centre" Malawi
"Lilongwe City Council" "data centre" OR "Kanengo"
```

Extract: applicant, plot/stand, ward, land-use category, decision date, conditions, building-use wording, occupancy/completion certificate, and whether the record is a council page, minute, or eRegistry procedure.

---

## 10. Official Cloud-Region Status

| Provider | Official source | Malawi status | Enumeration rule |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Malawi Region found; Africa regions are South Africa (`af-south-1`) and Cape Town | Treat reseller, partner, Direct Connect, or edge/cache claims as non-region evidence |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Malawi public Azure region found | Azure Stack/partner/local cloud in Malawi is local/hybrid cloud, not an Azure public region |
| Google Cloud | https://cloud.google.com/about/locations | No Malawi region found; Africa region is Johannesburg (`africa-south1`) | CDN/cache evidence is network/edge only |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Malawi region found; Africa commercial region is Johannesburg | Recheck official page before accepting any OCI Malawi claim |
| Huawei Cloud | https://www.huaweicloud.com/intl/en-us/ | No official Malawi public cloud region found | Huawei's Malawi role (National Data Centre Blantyre 2022) is a project/equipment record, not public-cloud region proof |

Annual verification query:
```text
site:aws.amazon.com Malawi "Region"
site:learn.microsoft.com/azure "Malawi" "region"
site:cloud.google.com/about/locations Malawi
site:oracle.com/cloud "Malawi" "region"
"Malawi" "cloud region" "official" 2026
```

---

## 11. Per-Region Official Enumeration Strategy

Run every region, even if expected yield is low. Objective is complete coverage, not only Lilongwe hits.

| Region | Anchor cities | Official anchors | Strategy and honest expected yield |
|---|---|---|---|
| **Central Region** | Lilongwe (capital), Kasungu, Salima, Dedza | ict.gov.mw/Dept of e-Government; PPPC/DIGMAP; PPDA/PPPC procurement; MACRA; ESCOM; MITC; Lilongwe City Council; MTL; OCL | **Highest yield.** Confirm Government Data Centre/National Data Centre Production Site, Lilongwe (primary), National Data Centre expansion (Tier-III existing site, planned/procurement), OCL Kanengo, MTL colocation page, CTN micro-DC announcement, and TNM third-DC announcement made in Lilongwe. Search procurement, council permits, ESCOM connections, MACRA licences. Expected **4-6 records**, but only PPPC/DIGMAP/World Bank/RFB/OCL/MTL are A-grade for specific facility/service claims. |
| **Southern Region** | Blantyre (commercial capital), Zomba, Thyolo, Mangochi | RBM; ESCOM; ict.gov.mw (National Data Centre Blantyre); Blantyre City Council; MACRA licence holders (TNM, Airtel) | **Medium-high yield.** Confirm National Data Centre Blantyre (secondary/backup, Huawei 2022), RBM Corporate Data Centre (planned/tender), Airtel Blantyre DC (2013; verify current), TNM existing DCs, Korena/1nga claim, ESCOM DC (lead only). Search RBM tenders, council records, MACRA licences. Expected **3-5 official-grade records**. |
| **Northern Region** | Mzuzu, Karonga, Rumphi, Nkhata Bay | Mzuzu City Council; ESCOM; provincial administration/e-Government; Mzuzu University | **Very low yield.** Only weak/academic leads (Mzuzu University data-centre concept, 2021). Search Mzuzu/Karonga for government ICT, university research infrastructure, and council permits. Expected **0-1 records (likely none)**; record `no_projects` honestly if nothing surfaces. |

Region query block:
```text
"{region}" OR "{capital}" "data centre" OR "data center" Malawi
site:ict.gov.mw "{capital}" OR "{region}" "data centre"
site:pppc.mw OR site:ppda.mw "{capital}" "data centre"
site:escom.mw "{capital}" "substation" OR "BESS" OR "data"
site:macra.mw "{operator}" "{capital}"
site:{council-domain} "ICT" OR "building permit" "{capital}"
```

---

## 12. Extraction Checklist

For every candidate, record these fields and grades independently:
- Facility/operator: legal name, brand, SPV, government body (e.g., PPPC/DIGMAP, RBM, TNM, Airtel Malawi, MTL, OCL, CTN, Korena/1nga Solutions).
- Status: MoU/intent, announced, approved, under construction, operational, closed/unknown.
- Location: region, district, city/town, plot/stand/address, coordinates, source precision.
- Official permits: MACRA licence, DPA registration, MERA/ESCOM power connection or licence, RBM/PPPC/PPDA procurement reference, council planning/building/occupancy record, MITC/SEZ instrument.
- Technical: tier wording exactly as published (`Tier III`, `Tier 3`, `Tier III by design`), IT load/facility load/MVA (record units exactly; Malawi sources rarely disclose - use `null`), racks/cabinets, halls, backup generators, UPS, fuel storage, cooling/water, certifications.
- Connectivity: carriers, IXP membership (MIX-BT), gateway licence, fibre routes (National Fiber Backbone, MTL backbone, Malawi-Mozambique/Zambia/Tanzania borders), meet-me-room, CDN/cache presence.
- Cloud/service: colocation, cloud, government-only vs private availability, backup/DR relation (Lilongwe primary vs Blantyre secondary).
- Sources: URL, title, publisher, date accessed, publication date, grade, quoted field.

Red flags: `cloud region` without an official hyperscale page; `Tier III` without `by design`/certification distinction; directory address without operator page; MoU counted as construction; social post treated as primary; MVA converted to MW; region missing because no hits were found; any MW figure for a Malawi DC that is not explicitly disclosed by an official source.
