# CI Explorer Official -- Côte d'Ivoire Datacenter Enumeration

Date: 2026-08-12. Country: **CI / Côte d'Ivoire**. Scope: official, regulatory and primary-source methodology for enumerating commercial, telco, sovereign and edge data-centre facilities. Administrative model: **14 districts**: Abidjan; Yamoussoukro; Bas-Sassandra; Comoé; Denguélé; Gôh-Djiboua; Lacs; Lagunes; Montagnes; Sassandra-Marahoué; Savanes; Vallée du Bandama; Woroba; Zanzan.

## Reliability Grades

- **A** -- primary evidence naming a facility, project, licence, permit, certification or site: ministry or regulator page, official operator page, Uptime Institute record, PeeringDB facility record, company registry record, EXIM/USG release, public-procurement notice, environmental or power filing.
- **B** -- strong secondary evidence: Data Center Dynamics, Capacity Media, Connecting Africa, The Tech Capital, Agence Ecofin, TechAfrica News, We Are Tech Africa, Fraternité Matin, AIP, Abidjan.net, Digitalmag.ci, Jeune Afrique, Financial Afrik, operator repost of third-party article.
- **C** -- lead only: generic market reports, directory listings, SEO market blogs, social posts, reseller claims, MoUs or announcements without named site/status, capacity values not backed by operator/official evidence.

Grade each fact separately. A page can be A for existence but C for an uncited MW/rack value. Do not promote a facility to operational solely because a directory lists it.

## Ground Rules

- There is no verified national public register of data centres in Côte d'Ivoire. Enumeration must join **operator pages**, **ARTCI telecom/data-protection records**, **Ministry of Digital Transition releases**, **SIGUPC/building-permit evidence**, **VITIB/free-zone records**, **energy evidence from ANARE-CI / CI-ENERGIES / CIE**, **ANDE/EIES disclosures**, **CEPICI / IDU company records**, **public-procurement notices**, **PeeringDB/Uptime**, and trade press.
- Search in French first: `centre de données`, `data center`, `datacenter`, `centre d'hébergement`, `hébergement`, `colocation`, `baies`, `salle informatique`, `cloud souverain`, `Tier III`, `Tiers 3`, `mise en service`, `inauguration`, `raccordement`, `poste`, `MVA`, `MW`.
- The market is **Greater-Abidjan-first**, but district assignment must be exact. Grand-Bassam and VITIB are in **Comoé district / Sud-Comoé**, even when operators market the site as Abidjan-area.
- Treat telco switch rooms, cable landing stations and bank IT rooms as data-centre leads only. Classify them as commercial colocation/cloud only when official service pages or customer-facing materials prove that role.
- Hyperscaler public cloud regions are negative evidence as of this review: AWS, Microsoft Azure, Google Cloud and Oracle OCI official region lists do not show a Côte d'Ivoire public region. Re-check official pages every run.

## Verified Official and Primary Sources

### National Digital Ministry and State DC

Primary URLs:
- https://www.telecom.gouv.ci/
- https://www.telecom.gouv.ci/new/actualite/63 -- launch / first-stone item for the Data Center National.
- https://www.telecom.gouv.ci/new/actualite/73 -- 2024-05-16 site visit: Anoumambo, AIGF site, 36 billion FCFA, 24-month construction, first stone on 2023-12-14.
- https://www.exim.gov/news/export-import-bank-united-states-board-directors-approves-nearly-514-million-strengthen -- EXIM Board approval of a $66 million guarantee for Côte d'Ivoire national data-centre construction.
- https://www.exim.gov/news/exim-awards-industries-future-deal-year-cybastion-institute-technology-for-cote-divoire -- EXIM award/transaction follow-up for Cybastion.

Use these as A-grade evidence for the **Data Center National** project: district **Abidjan**, locality **Anoumambo**, site **AIGF**, state sponsor, Cybastion equipment/export role, PORTEO/build consortium only where a source names it, 36bn FCFA local budget and $66m EXIM guarantee. EXIM financing approval is not operational status. Keep status as construction / project unless ministry or operator confirms commissioning.

Queries:
```text
site:telecom.gouv.ci "Data Center National"
site:telecom.gouv.ci "centre de données" "Anoumambo" OR "AIGF"
site:gouv.ci "Data Center National" "Cybastion" OR "PORTEO"
site:exim.gov "Côte d'Ivoire" "data center" OR "data centre"
"Data Center National" "36 milliards" "Côte d'Ivoire"
```

### ARTCI and Data Protection

Primary URLs:
- https://artci.ci/ -- regulator portal, decisions, licences and activity reports. `www.artci.ci` redirects to `artci.ci`.
- https://www.autoritedeprotection.ci/ -- ARTCI personal-data protection portal. Curl may fail certificate validation; verify by browser/search before downgrading.

Use ARTCI as A-grade evidence for licence holders, telecom authorisations and data-protection decisions, not as a facility registry unless the decision names a facility. Data-protection/local-hosting claims should reference Loi n°2013-450 and ARTCI guidance rather than market blogs.

Queries:
```text
site:artci.ci "centre de données" OR "data center" OR "datacenter"
site:artci.ci "licence" "{operator}" "Côte d'Ivoire"
site:artci.ci "décision" "{operator}" "autorisation"
site:autoritedeprotection.ci "{operator}" "traitement" OR "hébergement"
site:autoritedeprotection.ci "cloud" OR "transfert" OR "hébergement"
"ARTCI" "Raxio" "data center" OR "centre de données"
```

### Planning, Building Permits and District Portals

Primary URLs:
- https://guichet.construction.gouv.ci/GUPC/ -- SIGUPC/GUPC building-permit portal; verified HTTP 200.
- https://www.construction.gouv.ci/ -- Ministry of Construction.
- https://abidjan.district.ci/ and https://abidjan.district.gouv.ci/ -- Abidjan district portals.
- https://districtyakro.ci/ -- Yamoussoukro district portal.
- https://www.vitib.ci/ -- VITIB / ZBTIC Grand-Bassam free-zone portal; verified redirect to `/fr` and HTTP 200.

Use SIGUPC and district/commune portals for A-grade permits only when records identify the applicant/site. Many district portals have poor search; combine official-domain search with generic search.

Queries:
```text
site:guichet.construction.gouv.ci/GUPC "data center" OR "centre de données" OR "salle informatique"
site:construction.gouv.ci "data center" OR "centre de données" OR "permis de construire"
site:abidjan.district.ci "data center" OR "centre de données" OR "permis"
site:districtyakro.ci "numérique" OR "centre de données" OR "data center"
site:vitib.ci "data center" OR "centre de données" OR "Raxio" OR "MainOne" OR "ST Digital"
"VITIB" "Grand-Bassam" "data center" "permis"
```

Extract applicant/SPV, parcel/locality, commune, district, floor area, electrical load, permit date and status.

### Energy and Grid Evidence

Primary URLs:
- https://anare.ci/ -- ANARE-CI electricity regulator. Verified reachable but may return 403 to some clients.
- https://www.cinergies.ci/ -- CI-ENERGIES; verified HTTP 200.
- https://www.cie.ci/ -- CIE distribution/concessionaire. Curl may fail local certificate validation; verify with browser/search.

Energy evidence is high value because real data centres need MV supply, transformers, generators, fuel storage and often solar/backup disclosures. Public records are sparse, so an A-grade power fact normally requires an official utility/regulator document or operator technical sheet.

Queries:
```text
site:anare.ci "data center" OR "centre de données" OR "raccordement"
site:cinergies.ci "data center" OR "centre de données" OR "poste" OR "MW"
site:cie.ci "data center" OR "raccordement" OR "grand compte"
"{facility}" "15kV" OR "MVA" OR "MW" "Côte d'Ivoire"
"{operator}" "raccordement" "Grand-Bassam" OR "Abidjan"
```

### Environment and EIES

Primary public portal evidence for ANDE is weaker than other agencies; use named EIES documents, consultant disclosures and ministry records only when they name the project. Raxio's official CIV1 page links an **ESIA Executive Summary**, which is A-grade for Raxio environmental diligence if the linked document is accessible.

Queries:
```text
"ANDE" "EIES" "data center" "Côte d'Ivoire"
"étude d'impact environnemental" "Raxio" OR "VITIB" OR "Data Center National"
"{operator}" "EIES" OR "ESIA" "Grand-Bassam"
site:envitech.ci OR site:enval-group.com "data center" OR "centre de données"
```

### Investment, Company Registry and Procurement

Primary URLs:
- https://cepici.ci/ and https://cepici.africa/ -- CEPICI investment portals. Some clients see redirects/SSL issues; verify in browser/search.
- https://elicence.cepici.ci/ -- e-Licences catalogue.
- https://annuaireidu.ci/ -- IDU/company directory. Useful primary registry evidence; e.g. PAIX DATA CENTRES is listed with an object including operation/development of a neutral datacenter and colocation.
- https://www.marchespublics.ci/ and https://marchespublics.gouv.ci/ -- DGMP public-procurement portal mirrors found live in search.
- https://sigomap.gouv.ci/ -- SIGOMAP dematerialized public-procurement platform.

Queries:
```text
site:annuaireidu.ci "{operator}" "datacenter" OR "data center" OR "collocation"
site:cepici.ci "data center" OR "centre de données" OR "TIC"
site:elicence.cepici.ci "ARTCI" "Information, Communication"
site:marchespublics.ci OR site:marchespublics.gouv.ci OR site:sigomap.gouv.ci "data center" OR "centre de données" OR "hébergement" OR "cloud"
"{operator}" "RCCM" OR "IDU" "Côte d'Ivoire"
```

### ANSSI and State-Data Hosting

Primary URLs:
- https://www.anssi.ci/ -- national cybersecurity authority.

Use ANSSI for cybersecurity/state-hosting requirements, qualified security providers and government digital-infrastructure partners. ANSSI evidence can support why local hosting demand exists, but it does not prove a facility unless a site/operator is named.

Queries:
```text
site:anssi.ci "cloud" OR "hébergement" OR "centre de données"
site:anssi.ci "prestataire" "sécurité" "systèmes d'information"
"ANSSI" "Côte d'Ivoire" "data center" OR "centre de données"
```

### Certifications, Interconnection and Hyperscaler Negative Evidence

Primary URLs:
- https://uptimeinstitute.com/uptime-institute-awards/country/id/CI -- country awards page pattern; observed redirect/anti-bot behavior in curl, so verify with browser/search and operator certificate claims.
- https://www.peeringdb.com/fac/12168 -- Equinix AB1 / MainOne MDXi Abidjan, location Grand Bassam, address VITIB, networks listed.
- https://www.peeringdb.com/fac/6246 -- PAIX Abidjan / ABJ1, Cocody, Abidjan.
- https://www.peeringdb.com/fac/15646 -- ST Digital Datacenter Services / CIV01, Grand-Bassam/VITIB.
- AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html
- Azure: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud: https://cloud.google.com/about/locations
- Oracle: https://www.oracle.com/africa/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

Queries:
```text
site:uptimeinstitute.com "Côte d'Ivoire" OR "Ivory Coast" "Tier"
"Raxio CIV1" "Uptime Institute" "Tier III"
site:peeringdb.com "Côte d'Ivoire" "facility" "data center"
site:aws.amazon.com "Côte d'Ivoire" OR "Ivory Coast" "region"
site:learn.microsoft.com "Côte d'Ivoire" OR "Ivory Coast" "region"
site:cloud.google.com "Côte d'Ivoire" OR "Ivory Coast" "location"
site:oracle.com "Côte d'Ivoire" OR "Ivory Coast" "cloud region"
```

## Facility Seeds With Correct District Attribution

| Facility / project | District | Status | Best current source grade | Evidence to keep / verify |
|---|---:|---|---|---|
| Data Center National, Anoumambo / AIGF | Abidjan | Project / construction evidence, not proven operational | A | Ministry pages and EXIM releases: 36bn FCFA, 24-month build, first stone 2023-12-14, $66m EXIM guarantee. Join SIGUPC, ANDE, CIE and ministry progress. |
| Raxio CIV1 | Comoé (Grand-Bassam, VITIB) | Operational / launched 2024 | A | Official Raxio page: Grand-Bassam inside VITIB, 2,000 m2 white space, 400 key-fact racks, 3MW IT power, Tier III certified, ESIA link. Ministry page says 12,000 m2 site, 800 racks and 3MW. Reconcile 400 current vs 800 full-build. |
| Equinix / MainOne AB1 / MDXi Abidjan | Comoé for VITIB record; market label Abidjan | Operational | A/A- | Equinix AB1 page confirms AB1; PeeringDB fac/12168 gives VITIB Grand Bassam and networks; MainOne article confirms cable landing and data centre. Avoid stale address claims unless operator confirms. |
| MainOne / Equinix AB1.2 | Comoé (Grand-Bassam, VITIB) | Operational / launched 2023 | B until official page isolated | Trade press says open-access carrier-neutral facility at Uptime Tier III standards. Join to Equinix/MainOne official pages, VITIB and PeeringDB before using as separate record from AB1. |
| ST Digital Datacenter Services / CIV01 | Comoé (Grand-Bassam, VITIB) | Operational / inaugurated 2025-10-02 | A-/B | ST Digital reposted article states VITIB, Tier III infrastructure, 4,000 m2, ~160 racks. PeeringDB fac/15646 confirms ST Digital facility coordinates and electrical services. Treat "Tier III" as design/claim unless Uptime record found. |
| PAIX Abidjan / ABJ1 | Abidjan (Cocody) | Operational colocation | A- | PAIX homepage confirms company; PeeringDB fac/6246 confirms ABJ1/Cocody/Abidjan. A former PAIX facility path was stale in this review; use homepage, PeeringDB and annuaireidu until PAIX publishes a current facility page. |
| Orange Côte d'Ivoire Grand-Bassam DC | Comoé likely; verify exact locality | Operational telco/cloud lead | B | Local/business press supports Grand-Bassam DC and cloud/colo claims. Need Orange official page, CIE and ARTCI joins before A-grade. |
| MTN Côte d'Ivoire eCentre / next-gen DC | Abidjan (Yopougon in older reporting) | Operational telco/internal lead | B | DCD/Abidjan.net/Ecofin support modular eCentre and later facility. Treat as telco internal unless MTN Business page proves colocation/cloud service. |
| Moov Africa CI internal DC | Unknown, likely Abidjan | Internal telco lead | C | Official telco presence only; no named public DC page found. |
| Ambra Cloud / CenterServ / other local hosts | Abidjan leads | Cloud/hosting leads | B/C | Use operator pages, IDU, ARTCI and office addresses before creating facility records. |

## Per-District Strategy and Coverage

Run this exact 14-division sweep before setting `no_projects: true`. Search both district and capital/major-city names; for Comoé add Grand-Bassam and VITIB.

| District | Capital / key city terms | Official-first strategy | Expected result as of 2026-08-12 |
|---|---|---|---|
| Abidjan | Abidjan; Cocody; Yopougon; Plateau; Marcory; Port-Bouët; Treichville; Koumassi; Anyama; Bingerville; Songon | Ministry, ARTCI, SIGUPC, Abidjan district portals, CIE, PeeringDB, operator pages. Search named operators: PAIX, MTN, Orange, Ambra, banks, sovereign DC. | Positive: Data Center National, PAIX ABJ1, MTN leads, smaller hosters. Also marketed location for VITIB sites, but do not misassign Grand-Bassam. |
| Yamoussoukro | Yamoussoukro | districtyakro.ci, procurement, ministry disaster-recovery or government cloud references, SIGUPC, CIE. | No verified commercial DC. Watch for government DR/backup site. |
| Bas-Sassandra | San-Pédro; Sassandra; Soubré; Tabou | Port/industrial-zone digital projects, SIGUPC, CIE, local authority pages, telco network rooms. | No verified DC. Port IT/telco rooms only C-grade leads. |
| Comoé | Abengourou; Grand-Bassam; Aboisso; VITIB; ZBTIC | VITIB first, SIGUPC, CIE, PeeringDB, operator pages, district/region searches. | Positive: Raxio CIV1, Equinix/MainOne AB1 or AB1.2, ST Digital, Orange Grand-Bassam lead. Highest priority with Abidjan. |
| Denguélé | Odienné; Minignan | SIGUPC, CIE, ARTCI operator-name sweep. | No verified DC. |
| Gôh-Djiboua | Gagnoa; Divo | SIGUPC, district/region pages, telco and university/government IT searches. | No verified DC. |
| Lacs | Dimbokro; Toumodi; Daoukro | SIGUPC, CIE, official digital-service searches. | No verified DC. |
| Lagunes | Dabou; Agboville; Adzopé; Tiassalé | SIGUPC, industrial parks, fibre/backbone and telco searches. | No verified DC; possible spillover/industrial leads only. |
| Montagnes | Man; Duékoué; Guiglo | SIGUPC, CIE, regional government and telco searches. | No verified DC. |
| Sassandra-Marahoué | Daloa; Bouaflé; Zuénoula | SIGUPC, CIE, university/telco searches. | No verified DC. |
| Savanes | Korhogo; Ferkessédougou; Boundiali | SIGUPC, CIE, digital-government and telco searches. | No verified DC; future regional edge candidate. |
| Vallée du Bandama | Bouaké; Katiola | SIGUPC, CIE, Bouaké municipality, university, telco/backbone terms. | No verified commercial DC; Bouaké is a plausible future edge/DR candidate. |
| Woroba | Séguéla; Mankono; Touba | SIGUPC, CIE, official district searches. | No verified DC. |
| Zanzan | Bondoukou; Bouna | SIGUPC, CIE, border/connectivity terms. | No verified DC. |

Universal district queries:
```text
"{district}" "centre de données" OR "data center" "Côte d'Ivoire"
"{capital}" "centre de données" OR "data center" OR "datacenter"
"{district}" "hébergement" OR "colocation" OR "cloud" "Côte d'Ivoire"
site:gouv.ci "{district}" "numérique" OR "TIC" OR "fibre"
site:guichet.construction.gouv.ci/GUPC "{capital}" "salle informatique" OR "data center"
"{capital}" "Orange" OR "MTN" OR "Moov" "data center" OR "centre de données"
"{district}" "MVA" OR "MW" "data center" OR "centre de données"
```

## Record Extraction Checklist

For each candidate, capture:

- `facility_name`, `operator`, `owner/SPV`, `source_name`, `source_url`, `source_grade`, `fact_grade`.
- `district`, `region/commune`, `locality`, coordinates if source-grade allows; distinguish marketed metro from legal district.
- `status` using: MoU/announced -> permit/financed -> first stone -> construction -> inaugurated/launched -> operational.
- Capacity facts with source-specific qualifiers: racks current vs full build, m2 site vs white space, MW utility vs IT load, Tier certified vs designed-to/standards.
- Joins needed: ARTCI licence, IDU/CEPICI legal record, SIGUPC permit, EIES/ANDE, CIE/CI-ENERGIES power, Uptime, PeeringDB networks, operator service page.

## URL Validation Notes From This Review

- Verified reachable by curl/browser: `artci.ci`, `telecom.gouv.ci/new/actualite/73`, `guichet.construction.gouv.ci/GUPC/`, `vitib.ci`, `raxiogroup.com/data-centres/cote-divoire/`, `st.digital/...grand-bassam-507`, `cinergies.ci`.
- Browser/search-accessible but curl-blocked or certificate-sensitive: Equinix/MainOne pages may return Akamai 403 to curl; `autoritedeprotection.ci` and `cie.ci` showed local certificate-chain issues; `uptimeinstitute.com/uptime-institute-awards/country/id/CI` redirected unexpectedly under curl. Do not mark dead without browser verification.
- For PAIX, use https://www.paix.io/ plus PeeringDB https://www.peeringdb.com/fac/6246 and IDU https://annuaireidu.ci/ searches until PAIX publishes a current facility-specific page.
