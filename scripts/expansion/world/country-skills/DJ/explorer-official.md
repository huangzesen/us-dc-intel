# DJ Explorer Official - Djibouti Datacenter Enumeration via Government, Regulator, Power, ICT, Investment and Cable Records

Date verified: 2026-08-12. Country: **DJ - Djibouti**. Division model from `world-manifest.jsonl`: **6 regions/cities** (`subnational_type = region/city`): **Arta, Ali Sabieh, Dikhil, Djibouti, Obock, Tadjourah**. Scope: official and regulator-led evidence for commercial, telecom, government, enterprise and pipeline data-centre facilities.

Reliability grades:
- **A** = primary/official evidence: ARMD pages and laws, Journal Officiel acts, ministry/agency pages, Djibouti Telecom official pages, FSD/DPFZA/DIFTZ official announcements, official cable/operator pages, Uptime Institute award pages, official cloud-region pages.
- **A-** = official operator or investor announcement proving a named project or operating claim, but not a permit/regulator filing; use cautiously for design capacity and status.
- **B** = strong secondary evidence: Data Center Dynamics (DCD), SDxCentral, SubTel Forum, Capacity/Connecting Africa, African Business, Agence Ecofin, ADI/La Nation/RTD state media when reporting events rather than publishing documents.
- **C** = discovery lead only: directories, market reports, SEO pages, social posts, aggregator capacity tables, and claims that cannot be tied to an official/operator source.

Grade the exact claim being made. A site can be **A-** for existence from Wingu's own page, **B** for a launch date from trade press, and **C** for MW/rack figures that appear only in a directory.

---

## 0. Djibouti Structure and Market Facts

- Djibouti has **no public national data-centre register** and no public searchable construction/EIA portal that surfaced in this review. Absence from a register is therefore not absence of activity.
- The six divisions above are the complete coverage set. A run is incomplete unless all six are searched or explicitly output as `no_projects: true` with query/date notes.
- Facility evidence is overwhelmingly **Djibouti City-centred**. Confirmed or strongly sourced records are in the **Djibouti** division: Wingu/Djibouti Data Center (DDC), Wingu TO7 Technology Park data centre and CLS, Djibouti Telecom cable landing and colocation infrastructure, AMS-IX Djibouti/DjIX, and PAIX JIB1 as an announced project.
- **Arta, Ali Sabieh, Dikhil, Obock and Tadjourah** are expected negatives for commercial colocation. Still check government/telco rooms, port ICT, customs ICT, cable/fibre huts, and power projects before marking them negative.
- French is the highest-yield official search language. Also search English because most datacenter/cable operators publish in English.
- Use aliases: `data center`, `data centre`, `datacenter`, `centre de donnees`, `centre d'hebergement`, `hebergement`, `colocation`, `salle serveur`, `station d'atterrissement`, `cable sous-marin`, `CLS`, `Haramous`, `Boulaos`, `Siesta`, `Ras Dika`, `PK12`, `PK23`, `DIFTZ`, `TO7`, `PAIX`, `JIB1`.
- Large-MW claims require extra scepticism. Electricity is expensive and grid/power supply is a constraint, so do not convert announced design MW into operational IT load without commissioning or power evidence.
- No AWS, Azure, Google Cloud or Oracle public cloud region in Djibouti was found on official provider pages during this review.

---

## 1. ARMD - Multisector Regulator

Primary sources:
- ARMD home: https://www.armd.dj/
- ARMD who-we-are page: https://www.armd.dj/Qui-Somme-Nous and https://www.armd.dj/fr/Qui-Somme-Nous
- ARMD law PDF found on the ARMD site: https://www.armd.dj/storage/juridiques/June2023/Ib9ZJbFO9u0RBPJH0qlj.pdf
- English ARMD law PDF mirror on ARMD site: https://www.armd.dj/storage/juridiques/May2026/JJk70dicEW7sJHWmELie.pdf

Verified points:
- **Loi n°074/AN/20/8eme L** created the Autorite de Regulation Multisectorielle de Djibouti (ARMD). The ARMD page also cites implementation decree **N°2022-047/PRE**.
- ARMD covers regulated sectors including telecommunications/ICT, energy, water and postal services. It grants authorisations, licences and concessions; manages spectrum; controls service quality; and can inspect/sanction regulated providers.
- ARMD is not a data-centre permit registry. Use it to identify telecom/ICT licensees, regulated-service providers, spectrum/interconnection context, tariff or energy regulation, and possible authorisations for operators adjacent to datacenters.
- No public ARMD data-centre facility list surfaced in this review.

ARMD query templates:
```text
site:armd.dj "data center" OR "data centre" OR "centre de donnees" OR colocation
site:armd.dj licence OR autorisation OR concession telecommunication OR TIC
site:armd.dj "Djibouti Telecom" OR Wingu OR PAIX OR TO7
site:armd.dj energie tarif concession "Electricite de Djibouti"
site:journalofficiel.dj "Loi n°074/AN/20" OR "Autorite de Regulation Multisectorielle"
"ARMD" Djibouti "data center" OR "centre de donnees" OR colocation
```

Extraction: licensee/SPV, service class, regulated sector, address/location text, decision date, effective/expiry dates, interconnection or tariff terms.

Grade guidance: **A** for ARMD and Journal Officiel documents; **B** for trade press quoting an ARMD action; **C** for unsourced licence lists.

---

## 2. Government Digital and Public-Sector ICT Sources

Primary/official sources:
- MDENI / digital-economy portal domain: `numerique.gouv.dj` (confirmed on the Presidency government composition page; intermittently unreachable to curl during review)
- ANSIE domain: `www.ansie.dj` (linked from Presidency pages; intermittently unreachable to curl during review)
- E-government portal: https://www.egouv.dj/
- Presidency government composition page confirming MDENI contact/domain: https://www.presidence.dj/composition
- Presidency Council of Ministers page on ANSIE service tariffs, including hosting within a national data center: https://www.presidence.dj/conseil-des-ministres/2023-11-14
- World Bank Djibouti Digital Economy Diagnostic press page: https://www.banquemondiale.org/fr/news/press-release/2024/05/15/djibouti-digital-economy-opportunities-and-challenges-for-growth-and-development

Verified points:
- MDENI and the World Bank Digital Economy Diagnostic are policy/context sources. They can explain demand, digital-public-infrastructure priorities and gaps, but they are not facility registers.
- ANSIE operates state information-system and e-government functions. Search ANSIE and egouv.dj for hosting, cybersecurity, identity, procurement and server-room language.
- The Presidency's 2023-11-14 Council of Ministers page says an ANSIE tariff decree covers services including **"Les Hebergements au sein d'un centre de donnees national ou DATA CENTER"**. This is **A-grade evidence that ANSIE/government uses or offers hosting in a national data center**, but it does **not** name a physical site, operator, address, capacity or whether the national data center is a standalone ANSIE facility or hosted inside another state/telecom facility.
- No public ANSIE or egouv.dj facility page naming the address of that national data center surfaced in this review. Treat government hosting inside Djibouti Telecom/DDC as an inference unless a ministry, ANSIE, procurement or operator source names it.

Templates:
```text
site:numerique.gouv.dj "data center" OR "data centre" OR "centre de donnees" OR cloud OR hebergement
site:ansie.dj "data center" OR "centre de donnees" OR hebergement OR cloud OR "salle serveur"
site:egouv.dj hebergement OR cloud OR "centre de donnees" OR "data center"
site:presidence.dj ANSIE "centre de donnees" OR DATA CENTER OR hebergement
site:*.gouv.dj Djibouti "data center" OR "centre de donnees" OR hebergement
"Djibouti" "Smart Nation" "data center" OR cloud OR hebergement
```

Grade guidance: **A** for official ministry/agency pages and procurement documents; **B** for state-media reports quoting officials; **C** for platform/portal operation without a physical hosting source.

---

## 3. Data Protection, Cybersecurity and Legal Records

Official/legal sources:
- Journal Officiel: https://www.journalofficiel.dj/
- ARMD legal library pages under https://www.armd.dj/

Known legal anchors:
- **Loi n°100/AN/19** on personal-data protection is commonly cited as Djibouti's data-protection law. Verify the Journal Officiel text before citing as **A**.
- **Loi n°18/AN/23/9eme L** ratifies the African Union Malabo Convention on cybersecurity and personal-data protection. Verify exact publication details in the Journal Officiel before treating it as **A**.
- A **Code du Numerique** has been reported in legal/trade summaries, but the exact enacted text/law number must be retrieved from the Journal Officiel before it is used as Grade A.

Templates:
```text
site:journalofficiel.dj "donnees a caractere personnel" Djibouti
site:journalofficiel.dj "Code du Numerique" OR "cybersecurite"
site:journalofficiel.dj "Loi n°100/AN/19" OR "100/AN/19"
site:journalofficiel.dj "18/AN/23" OR "Convention de Malabo"
"CNDP" Djibouti "protection des donnees" OR operationnelle
```

Handling: data-protection laws are demand and compliance context. They are not facility records unless a source names a hosting location, operator, or regulated processing facility.

---

## 4. Power, Energy and Grid Evidence

Primary/context sources:
- ARMD energy/regulator remit: https://www.armd.dj/
- IRENA Renewable Readiness Assessment for Djibouti: https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2015/IRENA_RRA_Djibout_2015_EN.pdf

Verified points:
- Electricite de Djibouti (EdD) is the state utility. Use EdD/MoE/ARMD and donor documents for power feasibility, tariffs, interconnections and large-customer evidence.
- Djibouti's power cost and supply constraints are material. Any claim above a few MW needs corroboration from operator commissioning, grid connection, power purchase, generator/substation procurement, or official energy documents.
- Ethiopia-Djibouti interconnection and geothermal-development documents are context for possible power supply; they do not prove a data centre by themselves.

Templates:
```text
"Electricite de Djibouti" OR EdD "data center" OR "centre de donnees" OR "gros client"
site:armd.dj energie tarif licence concession Djibouti
"Djibouti" "230 kV" OR interconnexion OR substation OR poste "data center"
"PK12" Djibouti poste OR substation "data center" OR "centre de donnees"
"Djibouti" geothermie "data center" OR "centre de donnees"
"Djibouti" "MW" "data center" power OR electricity OR grid
```

Grade guidance: **A** for utility/ministry/regulator/donor documents; **B** for reputable press quoting official project data; **C** for market-report MW.

---

## 5. Environment, Planning, Land and Free Zones

Official sources:
- Journal Officiel: https://www.journalofficiel.dj/
- DPFZA: https://dpfza.gov.dj/
- DIFTZ: https://www.diftz.dj/
- ADI state news: https://adi.dj
- La Nation: https://www.lanation.dj
- RTD: https://rtd.dj/

Verified points:
- No public searchable EIA database or city construction-permit portal surfaced in this review.
- DPFZA/DIFTZ are land, investment and free-zone leads. No confirmed commercial data-centre facility inside DIFTZ surfaced; do not count DIFTZ as a datacenter.
- Djibouti City municipality and national land acts may appear only through Journal Officiel, ADI/La Nation/RTD, or operator announcements.
- Search land/project terms around Haramous, Boulaos, Siesta beach, Ras Dika, PK12, PK23/DIFTZ, Rue de Geneve and TO7 Technology Park.

Planning and environment templates:
```text
site:diftz.dj "data center" OR "data centre" OR "centre de donnees" OR ICT
site:dpfza.gov.dj "data center" OR "centre de donnees" OR technologie OR ICT
site:journalofficiel.dj "Djibouti Data Center" OR Wingu OR TO7 OR PAIX OR "centre de donnees"
site:adi.dj "data center" OR "centre de donnees" OR "cable sous-marin" OR Wingu OR PAIX
site:lanation.dj "data center" OR "centre de donnees" OR "economie numerique" OR Wingu OR PAIX
"Djibouti" "etude d'impact environnemental" "data center" OR "centre de donnees" OR "station d'atterrissement"
"Rue de Geneve" Djibouti PAIX OR "data center"
"PK23" OR DIFTZ Djibouti "data center" OR "centre de donnees"
```

Grade guidance: **A** for official acts/permits; **A-** for official operator or investment-agency releases proving a project; **B** for state-media event coverage; **C** for directories or free-zone marketing without a named facility.

---

## 6. Investment and Sovereign-Fund Sources

Primary/near-primary sources:
- FSD / Fonds Souverain de Djibouti: search direct FSD pages and official reposts each run.
- DPFZA and DIFTZ: https://dpfza.gov.dj/ and https://www.diftz.dj/
- Journal Officiel legal notices: https://www.journalofficiel.dj/

Current facility anchor:
- **PAIX JIB1** is an announced project by PAIX Data Centres with the Djibouti Sovereign Fund. Trade press and release syndication consistently describe up to **5 MW** and first phase targeted **2026**, but during this review no regulator permit or commissioning source was found. Keep status no higher than `announced/planned` until construction or launch evidence appears.

Templates:
```text
"Fonds Souverain de Djibouti" PAIX "data center" OR "data centre"
"FSD" Djibouti PAIX JIB1 OR "centre de donnees"
site:journalofficiel.dj PAIX OR "Djibouti Data Center" OR Wingu OR TO7
site:dpfza.gov.dj PAIX OR Wingu OR "data center"
"Djibouti" "registre du commerce" "Djibouti Data Center" OR Wingu OR PAIX
```

Grade guidance: **A/A-** for FSD/PAIX/official announcements depending on source type; **B** for DCD/SubTel/African Business summaries; **C** for directory-only PAIX JIB1 capacity or rack details.

---

## 7. Official Cloud-Region Exclusion

Check these official provider pages each batch:
- AWS Regions and AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure geographies and region list: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ and https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

As of 2026-08-12, no official AWS, Azure, Google Cloud or Oracle page listed a Djibouti cloud region. Do not create a hyperscale/public-cloud-region facility from cable-consortium participation, CDN/cache nodes, PoPs, cloud exchange products, reseller pages or customer data-sovereignty marketing.

Templates:
```text
site:aws.amazon.com Djibouti "Region" "Availability Zone"
site:learn.microsoft.com/azure Djibouti "Azure region"
site:cloud.google.com/about/locations Djibouti region
site:oracle.com/cloud Djibouti "cloud region"
"Djibouti" "AWS region" OR "Azure region" OR "Google Cloud region" OR "Oracle Cloud region"
```

---

## 8. Per-Division Official Coverage Map

| Division | Official search focus | Expected result / coding guidance |
|---|---|---|
| **Djibouti** | Djibouti City, Haramous, Boulaos, Siesta beach, Ras Dika, Rue de Geneve, PK12, PK23/DIFTZ, TO7 Technology Park; ARMD, MDENI, ANSIE, Djibouti Telecom, FSD, DPFZA, Journal Officiel, ADI/La Nation | Positive division. Confirm DDC/Wingu, TO7 DC+CLS, Djibouti Telecom CLS/colo, AMS-IX Djibouti/DjIX, and PAIX JIB1 as announced. |
| **Arta** | Arta town/coast; possible telco/government/server rooms | Expected negative for commercial colo. Search before `no_projects: true`. |
| **Ali Sabieh** | Ali Sabieh town, rail/road/customs corridor to Ethiopia | Expected negative for commercial colo; logistics/customs ICT rooms are not datacenters unless facility evidence is explicit. |
| **Dikhil** | Dikhil town, Lake Abbe/geothermal context | Expected negative; geothermal projects are power context only. |
| **Obock** | Obock port/Gulf of Tadjoura, migration/UN/government services | Expected negative; port/telco rooms need explicit hosting/colo evidence. |
| **Tadjourah** | Tadjourah town/port | Expected negative; port ICT and fibre PoPs are not commercial datacenters without facility evidence. |

Generic division sweep:
```text
"{division}" Djibouti "data center" OR "data centre" OR "centre de donnees" OR "salle serveur"
"{division}" Djibouti colocation OR hebergement OR cloud OR ICT
site:*.gouv.dj "{division}" "data center" OR "centre de donnees" OR "salle serveur"
"{division}" Djibouti "station d'atterrissement" OR "cable sous-marin"
"{division}" Djibouti "etude d'impact" OR permis OR construction
```

---

## 9. Verification Recipe

1. Seed named facilities from operator/official evidence: Wingu Djibouti/DDC, Wingu TO7 Technology Park DC+CLS, Djibouti Telecom cable/colo infrastructure, AMS-IX Djibouti/DjIX, PAIX JIB1, and ANSIE's referenced national data center hosting service.
2. Resolve aliases before counting: `DDC` = `Djibouti Data Center` = `Djibouti Data Center SARL` = Wingu's older Djibouti facility; `TO7 Technology Park` = Wingu's second Djibouti facility; `PAIX JIB1` = PAIX Djibouti/FSD project; `DjIX` = AMS-IX Djibouti since 2024.
3. For each candidate, seek evidence in this order: operator/official page -> regulator/legal record -> official investment/land/source -> utility/power source -> environment/planning source -> trade press -> directory. For ANSIE, do not create a separate physical facility unless a source identifies site/operator/address; otherwise record it as government hosting context.
4. Split facts into separate fields: `status`, `division`, `operator`, `developer`, `SPV`, `address`, `capacity_mw`, `announced_capacity_mw`, `racks`, `tier_certification`, `source_urls`, `evidence_date`, `evidence_grade`.
5. Use the lifecycle ladder: rumour < MoU < announced < land acquired < permit applied < permit granted < construction started < commissioned/inaugurated < operational.
6. Keep capacity null unless the source states capacity. Use `announced_capacity_mw` for PAIX JIB1 and other pre-commissioning figures.
7. Re-run cloud-region and six-division negative checks every batch.

## 10. URL Validation Notes From This Review

- Confirmed reachable by browser/search or curl: ARMD, Journal Officiel, DPFZA, DIFTZ, ADI, La Nation, RTD, Wingu, AMS-IX, PeeringDB, SubTel Forum, Baxtel, DataCenterMap, AWS, Azure, Google, Oracle, World Bank and IRENA pages listed above.
- Some reputable press sites returned curl/HEAD blocking or rate limiting during review (403/429) but are real and discoverable via search: DCD, SDxCentral, African Business, Agence Ecofin, Capacity, DataCenterMap.
- The old Djibouti Telecom `/data-centre-colocation/` path under `international.djiboutitelecom.dj` returned 404 during review. Do not use that retired path as a primary source unless it reappears; prefer current Djibouti Telecom pages, archived copies, Wingu operator pages, and cable-landing releases.
- `numerique.gouv.dj` and `ansie.dj` were intermittently unreachable to curl, but they are official/search-indexed domains referenced by Presidency pages. Verify interactively before treating absence of search results as negative evidence.
