# PG Explorer Official - Papua New Guinea Datacenter Enumeration

Date: 2026-08-12. Scope: official, regulatory, cloud, energy, and trade-press methodology for enumerating data centers and datacenter-like cloud/telecom facilities in Papua New Guinea (PNG). Reliability grades: **A** = official/primary source; **B** = strong secondary/trade press/operator interview; **C** = directory/social/weak aggregate.

## 0. Market Shape

- PNG is a small datacenter market. Treat **National Capital District / Port Moresby** as the primary search geography, then **Madang** and **Morobe / Lae** as secondary nodes because PNG DataCo and telecom backhaul/cable infrastructure point there. Highlands cities such as **Mount Hagen**, **Goroka**, **Mendi**, and **Tari** are grid/connectivity search targets, not proven carrier-neutral colo markets.
- Current confirmed public signals are mostly **government, telco, bank, and sovereign cloud** rather than hyperscale campuses. Known seed entities: **PNG DataCo**, **Telikom Limited**, **Datec (PNG) Limited**, **CloudSigma**, **Oracle / OCI via PNG DataCo**, **Vodafone PNG**, **Digicel (PNG)**, **Bank of South Pacific**, and the legacy **Huawei-built PNG government data centre**.
- Do not assume "cloud service" means a new physical facility. In PNG, cloud announcements often mean hosted services on PNG DataCo, Telikom/Datec, or overseas regions connected through local partners.

## 1. Official / Regulatory Backbone

### 1.1 Physical Planning and Building Permits

**National Capital District Commission (NCDC)** is the most useful public planning source for Port Moresby:

- Main site: https://www.ncdc.gov.pg/
- Building permit application page: https://www.ncdc.gov.pg/how-to/apply-for-a-building-license.html
- Applications and permit forms: https://ncdc.gov.pg/license-forms/
- Land development procedures in NCD: https://www.ncdc.gov.pg/regulatory-department/2_land_development_procedures/land-development-procedures-in-ncd.html
- Physical planning/regulatory pages: https://www.ncdc.gov.pg/regulatory-pp/ and planning forms/checklists under `/regulatory-pp/3_application_forms/` and `/regulatory-pp/1_application_checklist/`

Use NCDC for **A-grade existence/status only when an actual planning/building notice, application, checklist response, tender, or board notice names a site or project**. The portal is mostly forms and policy pages, so web search is usually better than browsing.

Queries:

```text
site:ncdc.gov.pg ("data centre" OR "data center" OR "datacenter" OR "cloud") "Port Moresby"
site:ncdc.gov.pg ("building permit" OR "planning permission") ("data centre" OR "ICT" OR "telecommunication")
site:ncdc.gov.pg ("Waigani" OR "Gerehu" OR "Savannah Heights" OR "Caution Bay") ("data centre" OR "cloud" OR "telecom")
"Planning Permission Application" "data centre" "Port Moresby"
"Building Permit" "data centre" "NCDC"
```

**Department of Lands and Physical Planning (DLPP)** is the national planning authority:

- DLPP physical planning acts/regulations page: https://dlpp.gov.pg/services/physical-planning/acts-regulations
- DLPP overview page: https://dlpp.gov.pg/services/physical-planning/overview

DLPP pages may return 403 in direct access, but search snippets confirm the Physical Planning Act 1989 jurisdiction and contact points. Use DLPP as **A for the legal pathway**, not a facility enumeration portal. Search provincial physical planning boards and municipal authorities for provinces outside NCD.

Queries:

```text
site:dlpp.gov.pg "Physical Planning Act 1989" "data centre"
"Physical Planning Board" "data centre" "Papua New Guinea"
"Provincial Physical Planning Board" ("data centre" OR "telecommunication") "{province}"
"planning permission" "data centre" "Papua New Guinea"
```

### 1.2 Environmental Permits

The **Conservation and Environment Protection Authority (CEPA)** permit route can reveal diesel generation, cooling water, waste discharge, and construction footprints, but there is no obvious datacenter-specific public register.

- CEPA site: https://cepa.gov.pg/
- PNG Environment Data Portal CEPA forms: https://png-data.sprep.org/
- Environment (Permits) Regulation 2002 text: https://faolex.fao.org/docs/pdf/png70630.pdf

The Environment (Permits) Regulation requires public notice of accepted permit applications and grants, with documents available for review for stated periods. Use this as a search hook across government pages and newspapers. **A** when a CEPA public notice or permit names a project; **B/C** when only a newspaper notice is found without permit number.

Queries:

```text
"Environment Permit" ("data centre" OR "data center" OR "cloud" OR "telecommunications") "Papua New Guinea"
site:cepa.gov.pg ("data centre" OR "telecommunications" OR "generator" OR "cooling")
site:png-data.sprep.org "Environment Permit" "Papua New Guinea" "telecommunications"
"public notice" "environment permit" "data centre" "Port Moresby"
```

### 1.3 Telecom / ICT Licensing - NICTA

**NICTA** is the official ICT regulator and the best operator census source.

- NICTA home: https://www.nicta.gov.pg/
- Registered licensees: https://www.nicta.gov.pg/licensing/registered-licensees/
- Network licensees: https://www.nicta.gov.pg/licensing/registered-licensees/network-licensees-list/
- Application licensees: https://www.nicta.gov.pg/licensing/registered-licensees/application-licensees-list/
- Operator class licensees: https://www.nicta.gov.pg/licensing/registered-licensees/operator-class-licensees-list/
- Licensing categories/application process: https://www.nicta.gov.pg/licensing/

The NICTA pages use public Ninja Tables AJAX endpoints. Pull table rows by table ID if the UI is hard to scrape:

```text
https://www.nicta.gov.pg/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=9331&target_action=get-all-data&default_sorting=old_first&skip_rows=0&limit_rows=0&ninja_table_public_nonce={nonce}
https://www.nicta.gov.pg/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=9357&target_action=get-all-data&default_sorting=old_first&skip_rows=0&limit_rows=0&ninja_table_public_nonce={nonce}
https://www.nicta.gov.pg/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=9320&target_action=get-all-data&default_sorting=old_first&skip_rows=0&limit_rows=0&ninja_table_public_nonce={nonce}
```

Important NICTA-listed operators to pivot into datacenter searches include **PNG Dataco Limited**, **Datec (PNG) Limited**, **Telikom Limited**, **Digicel (PNG) Limited**, **Vodafone PNG / Amalgamated Telecom Holdings PNG**, **Global Internet Limited**, **Kumul Communications Limited**, **Comserv (PNG) Limited**, **Niugini Comtech**, **Digitec ICT**, **Daltron**, **Speedcast PNG**, and regional licensees such as **Heavy Equipment Repairs Limited - Goroka**, **Jiwaka Development Corporation**, and **Alotau Enterprises**. A NICTA license proves telecom/ICT authority, not a data center; grade as **A for operator existence/license**, then require facility evidence.

Queries:

```text
site:nicta.gov.pg "PNG Dataco Limited" "license"
site:nicta.gov.pg "Datec (PNG) Limited" "license"
"{licensee}" ("data centre" OR "data center" OR "cloud" OR "colocation" OR "hosting") "Papua New Guinea"
"{licensee}" ("Port Moresby" OR "Lae" OR "Madang" OR "Mount Hagen") "data centre"
```

## 2. Government Cloud and Sovereign Hosting

**Department of ICT (DICT)** is the source for GovCloud, government data repository, government private network, and Digital Government Act compliance:

- DICT/DataCo managed service agreement: https://www.ict.gov.pg/dict-and-png-dataco-formalize-digital-transformation-partnership/
- DICT digital events/GovCloud references: https://www.ict.gov.pg/90168-2/
- Draft Government Cloud Policy 2023: https://www.ict.gov.pg/Policies/Cloud%20Policy/Draft%20Government%20Cloud%20Policy%202023%20V2.0.pdf
- DTO Manual reference to government-sanctioned cloud/datacenter: https://www.ict.gov.pg/DTO%20MANUAL/DIGITAL%20TRANSFORMATION%20OFFICER%20%28DTO%29%20MANUAL%20-%20Approved.pdf

DICT says PNG DataCo is the implementation partner for **GovCloud Infrastructure Services**, the **Central Electronic Data Repository**, and the **Government Private Network**, with data sovereignty requirements. This is **A-grade for national government cloud pipeline**, but not automatically a new facility.

**PNG DataCo official pages**:

- Data center services: https://www.pngdataco.com/services/ict-and-cloud-solutions/data-center-services/
- Oracle Cloud service: https://www.pngdataco.com/services/ict-and-cloud-solutions/oracle-cloud/
- DataCo coverage / cable landing stations: https://www.pngdataco.com/png-dataco-coverage/ and https://www.pngdataco.com/cable-landing-stations/

The DataCo data center services page describes secure rack space in PNG's Tier 3 data center, ISO-certified environment, PNG data residency, redundant power/cooling, and 24/7 monitoring. Business Advantage PNG's 2026 interview with DataCo's CEO says DataCo has data centers in **Port Moresby and Madang** and is looking at another data center at **Kumul Petroleum's Caution Bay SEZ**, a **Lae SEZ**, the **Islands**, and the **Highlands**. Treat the interview as **B**, then verify any site through NCDC/DLPP/CEPA/PNG Power/tenders before counting.

Queries:

```text
site:ict.gov.pg ("GovCloud" OR "Government Cloud" OR "Central Electronic Data Repository" OR "Government Private Network")
site:pngdataco.com ("data center" OR "data centre" OR "Oracle Cloud" OR "Tier 3")
"PNG DataCo" ("Caution Bay" OR "Lae SEZ" OR "Highlands" OR "Islands") "data centre"
"PNG DataCo" "Madang" "data centre"
```

## 3. Cloud Region Checks

No major public-cloud provider appears to list a dedicated PNG public cloud region. Record this explicitly when enumerating.

Official pages to check:

- AWS Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/

PNG-relevant cloud signals are **partner/local-cloud**, especially Oracle with PNG DataCo and the Telikom/Datec/CloudSigma sovereign AI data center.

**Sovereign AI Data Centre**:

- Kumul Consolidated Holdings official announcement: https://www.kch.com.pg/papua-new-guinea-advances-with-launch-of-first-sovereign-ai-data-centre/
- Datec page: https://www.datec.com.pg/detail/papua-new-guinea-advances-with-launch-of-first-sovereign-ai-data-centre

This is **A for announcement/pre-launch and named parties** (Telikom, Datec, CloudSigma) but capacity and exact facility status require follow-up.

Cloud queries:

```text
"Papua New Guinea" "AWS Region"
"Papua New Guinea" "Azure region"
"Papua New Guinea" "Google Cloud region"
"Papua New Guinea" "Oracle Cloud Infrastructure" "DataCo"
"Sovereign AI Data Centre" "Papua New Guinea" "Telikom" "Datec" "CloudSigma"
```

## 4. Energy / Grid Methodology

Grid evidence matters because PNG power supply is fragmented and reliability-constrained.

Key sources:

- PNG Power: https://www.pngpower.com.pg/
- PNG Power portfolio page at Kumul Consolidated Holdings: https://www.kch.com.pg/our-portfolio/png-power-limited/
- KCH 132kV Highlands/Ramu backbone announcement: https://www.kch.com.pg/132kv-power-line-commissioned-for-highlands-region/
- PM NEC power-sector statements: https://www.pmnec.gov.pg/
- World Bank/ADB project PDFs for older grid topology and electrification constraints.

PNG Power / KCH states PPL operates major grids and standalone provincial systems; KCH gives installed capacity and network size. The 2026 Tari-Hagen-Yonki (Ramu) 132kV commissioning strengthens the Highlands/Ramu corridor, relevant to **Eastern Highlands, Chimbu, Jiwaka, Western Highlands, Southern Highlands, Hela, Enga, Morobe, and Madang**. Use this to prioritize power-feasibility checks for any Lae/Madang/Highlands announcement.

Queries:

```text
site:pngpower.com.pg ("data centre" OR "data center" OR "substation" OR "connection") "{city}"
site:kch.com.pg ("132kV" OR "Ramu Grid" OR "Port Moresby Grid" OR "PNG Power") "{province}"
site:pmnec.gov.pg ("power" OR "electricity" OR "132kV") ("Lae" OR "Port Moresby" OR "Madang" OR "Mount Hagen")
"PNG Power" ("data centre" OR "data center" OR "cloud") "Port Moresby"
"Ramu Grid" ("data centre" OR "ICT" OR "telecom") "Lae"
```

## 5. Trade Press / Secondary Sources

Use these for discovery and lifecycle clues, then backfill official permits/licenses.

- **Business Advantage PNG**: strong ICT and SOE interviews. Example: https://www.businessadvantagepng.com/png-dataco-chief-executive-on-ntn-oracle-and-the-possibilities-of-ai/ (**B**).
- **DataCenterDynamics**: useful for international datacenter coverage and the Huawei PNG government data center security story. Example: https://www.datacenterdynamics.com/en/news/australia-huaweis-papua-new-guinea-data-center-security-openly-broken-making-potential-spying-easy/ (**B**).
- **Developing Telecoms**: telecom/cloud project announcements. Example Morobe project: https://developingtelecoms.com/telecom-technology/telecom-cloud-virtualization/19900-png-dataco-and-oracle-to-give-pngs-morobe-govt-an-ai-makeover.html (**B**).
- **NBC PNG / The National / Post-Courier / PNG Business News / APAC Outlook**: local event and operator news. Grade **B** for named projects and dates; **C** for broad claims without facility specifics.
- **DataCenterMap / Inflect / Baxtel / ocolo**: useful facility leads only. Grade **C** unless independently verified by operator/government.

Discovery queries:

```text
site:businessadvantagepng.com ("data centre" OR "data center" OR "cloud" OR "GovCloud") "Papua New Guinea"
site:datacenterdynamics.com "Papua New Guinea" "data center"
site:developingtelecoms.com "Papua New Guinea" ("data centre" OR "cloud" OR "Oracle")
site:nbc.com.pg ("data centre" OR "cloud" OR "AI") "Papua New Guinea"
site:thenational.com.pg ("data centre" OR "data center" OR "cloud") "Papua New Guinea"
```

## 6. Seed Projects / Operators to Verify

| Division | Seed | Status Signal | Sources | Grade |
|---|---|---:|---|---|
| National Capital District | PNG DataCo primary/Tier 3 data center, likely Port Moresby/Gerehu Earth Station | Operational service | PNG DataCo data center services; Business Advantage PNG interview; directories for address | A for service/existence, C for directory address |
| National Capital District | Telikom / Datec / CloudSigma Sovereign AI Data Centre | Pre-launched 2026 | KCH and Datec announcements | A for announcement, unknown capacity |
| National Capital District | PNG government Huawei-built National Data Centre / IGIS | Built/opened 2018, troubled | DCD/AFR/DICT references | B |
| National Capital District | Bank of South Pacific data and operations centres | Delivered | RPS project page | A for professional project reference |
| Madang | PNG DataCo Madang data center / cable landing / DR site | Operational/secondary | Business Advantage PNG interview; DataCenterMap | B for DataCo interview, C for directory details |
| Morobe | Morobe Digital Government Project - MMU with PNG DataCo and Oracle | Digital government/cloud platform, not proven physical DC | Developing Telecoms | B |
| Morobe / Lae | DataCo future Lae SEZ data center; Datec AI sovereign solutions roadshow in Lae | Pipeline / market-development | Business Advantage PNG; NBC PNG | B/C until permit/tender |
| Western Highlands | Vodafone PNG regional data center in Mount Hagen | Planned per operator profile | APAC Outlook | B/C until NICTA/operator/permit confirmation |

## 7. Province-by-Province Search Pattern

Use English as the primary language. Add Tok Pisin terms mainly for local media/social posts: **"data senta"**, **"gavman cloud"**, **"kompiuta senta"**, **"intanet"**, **"telekom"**, **"haus data"**. Search both British and US spelling: `data centre` and `data center`.

Base template for every division:

```text
"{province}" ("data centre" OR "data center" OR "datacenter" OR "cloud" OR "GovCloud" OR "ICT hub")
"{capital/city}" ("data centre" OR "data center" OR "server room" OR "colocation" OR "hosting")
"{province}" ("PNG DataCo" OR "Telikom" OR "Datec" OR "Oracle" OR "Vodafone" OR "Digicel")
"{province}" ("building permit" OR "planning permission" OR "environment permit") ("data centre" OR "telecommunications")
"{province}" ("substation" OR "132kV" OR "PNG Power" OR "Ramu Grid") ("data centre" OR "ICT" OR "telecom")
```

| Division | Practical approach |
|---|---|
| National Capital District | Highest priority. Search NCDC planning/building pages, DICT/GovCloud, PNG DataCo, Datec/Telikom/CloudSigma, BSP, Huawei/IGIS, Waigani, Gerehu, Savannah Heights, Caution Bay. |
| Central | Treat Port Moresby-adjacent projects carefully; NCD is separate. Search Caution Bay SEZ, Bautama, Kwikila, LNG/industrial power, and NCDC spillover. |
| Morobe | Priority secondary. Search Lae, Nadzab, Lae SEZ, Ramu Grid, Morobe Digital Government Project, PNG DataCo Oracle, Datec roadshows, Vodafone regional DC. |
| Madang | Priority secondary. Search Madang cable landing station, Modilon Road, PNG DataCo Madang, Kumul Submarine Cable, disaster recovery, Ramu Grid. |
| Eastern Highlands | Search Goroka, Yonki, Ramu grid, telecom licensees, universities/health/government server rooms; likely no standalone DC unless tied to grid/backbone. |
| Western Highlands | Search Mount Hagen, Tari-Hagen-Yonki 132kV, Vodafone regional data centre, Highlands loop/redundancy, PNG DataCo Highlands plan. |
| Chimbu | Search Kundiawa plus Highlands Highway/Ramu 132kV. Expect government/telco edge only. |
| Jiwaka | Search Banz/Minj/Kudjip and Jiwaka Development Corporation NICTA license; likely telecom/edge only. |
| Enga | Search Wabag/Porgera, mining telecom networks, PNG Power Highlands line; watch private enterprise network rooms. |
| Southern Highlands | Search Mendi and the 132kV Highlands corridor; likely grid/telecom only. |
| Hela | Search Tari, Hides gas/power, 132kV line, extractive-sector ICT rooms; likely private industrial facilities, not public colo. |
| East New Britain | Search Kokopo/Rabaul, Gazelle grid, cable landing, Digicel/Telikom exchanges; possible DR/edge, low confidence. |
| West New Britain | Search Kimbe, palm oil/industrial, Hargy/New Britain Palm Oil licensees, telecom edge. |
| New Ireland | Search Kavieng/Lihir, mining and submarine cable terms; private industrial networks more likely than commercial DC. |
| Bougainville | Search Buka/Arawa, ABG ICT, DICT Bougainville MoU, Digicel/Telikom; no known DC signal. |
| East Sepik | Search Wewak, Sepik digital government, PNG DataCo coverage, telecom exchanges. |
| West Sepik | Search Vanimo, border connectivity, PNG DataCo coverage, submarine/backhaul; low DC probability. |
| Manus | Search Lorengau, cable/satellite/defence ICT; low DC probability. |
| Milne Bay | Search Alotau, Alotau Enterprises NICTA license, cable/satellite and government ICT. |
| Northern | Search Popondetta/Oro, provincial government ICT, telecom exchange. |
| Gulf | Search Kerema, LNG/Papua LNG support infrastructure, telecom/edge. |
| Western | Search Daru, Kiunga, Tabubil, Ok Tedi, mining/private network rooms; public colo unlikely. |

## 8. Verification Rules

- Count as **operational data center** only with operator/government page, engineering/project page, license plus facility page, or credible trade press naming a facility and service/status.
- Count **cloud/GovCloud** separately when the evidence is a cloud platform without a new physical facility.
- Do not double count the same Port Moresby facility under PNG DataCo, DICT GovCloud, Oracle/DataCo, and directory entries unless a source clearly describes a separate building/campus.
- Treat social-media-only announcements as **C** unless mirrored by KCH/DICT/NCDC/NICTA/PNG DataCo/operator official pages.
- For capacity, expect sparse public data. If MW/racks are not stated, leave capacity null; do not infer from "Tier 3", "AI", or "sovereign" wording.
