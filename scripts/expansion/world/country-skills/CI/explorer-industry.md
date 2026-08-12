# CI Explorer Industry -- Côte d'Ivoire Datacenter Enumeration

Date: 2026-08-12. Country: **CI / Côte d'Ivoire**. Scope: operator, market, connectivity and trade-press methodology for finding commercial, telco, sovereign-cloud and edge data-centre facilities. Division model: **14 districts**: Abidjan; Yamoussoukro; Bas-Sassandra; Comoé; Denguélé; Gôh-Djiboua; Lacs; Lagunes; Montagnes; Sassandra-Marahoué; Savanes; Vallée du Bandama; Woroba; Zanzan.

## Reliability Grades

- **A** -- official operator facility/spec page, company registry record, Uptime record, PeeringDB facility record, hyperscaler official region page, government/regulator page naming the facility.
- **B** -- reputable trade or local press with named site/status: Data Center Dynamics, Capacity Media, Connecting Africa, The Tech Capital, Agence Ecofin, TechAfrica News, We Are Tech Africa, ITWeb Africa, Financial Afrik, FratMat, AIP, Abidjan.net, Digitalmag.ci.
- **C** -- directories and lead sources: Datacenter Map, Baxtel, OCOLO, Datacenters.com, HostDir, Data Center Planet, Systalink, LinkedIn/social, reseller pages, market reports and unsourced capacity tables.

Use source grades honestly: PeeringDB is A- for existence/location/interconnection metadata because it is user-maintained but operationally used; directories are C even when useful.

## Market Facts To Preserve

- The commercial market is concentrated in **Greater Abidjan**, especially **VITIB / Grand-Bassam in Comoé district** and **Cocody/Yopougon in Abidjan district**.
- Verified/strong facility seeds: **Raxio CIV1**, **Equinix/MainOne AB1 or AB1.2**, **ST Digital CIV01**, **PAIX Abidjan ABJ1**, **Data Center National**, **Orange Côte d'Ivoire Grand-Bassam lead**, **MTN Côte d'Ivoire eCentre/Yopougon lead**.
- District attribution matters. Raxio's official page places CIV1 in **Grand-Bassam inside VITIB**, 30 km from Abidjan. PeeringDB places Equinix AB1 at **Parc Technologique du VITIB - Zone Franche, Grand Bassam**. Treat these as **Comoé** records with an Abidjan-metro note.
- No AWS/Azure/GCP/OCI public cloud region is listed in Côte d'Ivoire on official region pages as of this review. Track CDN/edge/reseller claims separately from cloud-region records.
- Subsea and interconnection drive demand: MainOne landing at Grand-Bassam, ACE/SAT-3/WASC, 2Africa/MTN GlobalConnect announcements, CIVIX/PeeringDB, PAIX and Equinix/MainOne interconnection.

## Operator Deep Dives

### Raxio Group -- CIV1

Primary URLs:
- https://www.raxiogroup.com/data-centres/cote-divoire/ -- current facility/spec page.
- https://www.raxiogroup.com/ivory-coast-gains-significant-boost-to-digital-economy-with-launch-of-raxio-data-centre/ -- launch release.
- https://www.telecom.gouv.ci/new/actualite/92 -- ministry inauguration coverage.

Current facts:
- District: **Comoé**. Locality: Grand-Bassam, VITIB; marketed as Abidjan/UEMOA regional hub.
- Official Raxio page: Grand-Bassam inside VITIB, 2,000 m2 white space, 3MW IT power, Tier III certified, 15kV utility supply, 48h fuel backup, ESIA executive-summary link, 400 key-fact racks.
- Launch/ministry/trade sources also cite up to 800 racks at full capacity and over 20bn FCFA investment. Store current vs full-build rack values separately.

Queries:
```text
site:raxiogroup.com "CIV1" OR "Côte d'Ivoire" OR "Grand Bassam"
"Raxio CIV1" "Uptime" OR "Tier III" OR "3MW"
"Raxio" "VITIB" "Grand-Bassam" "ESIA" OR "EIES"
"Raxio" "Côte d'Ivoire" "800 racks" OR "400 racks"
```

### Equinix / MainOne -- AB1 and AB1.2

Primary / strong URLs:
- https://www.equinix.com/data-centers/europe-colocation/cote-divoire-colocation/abidjan-data-centers -- Equinix Abidjan market page.
- https://www.equinix.com/data-centers/europe-colocation/cote-divoire-colocation/abidjan-data-centers/ab1 -- AB1 page; curl may be Akamai-blocked.
- https://mainone.net/inside-the-mainone-cote-divoire-data-centre-and-cable-landing-station/ -- MainOne cable landing station and data centre article.
- https://www.peeringdb.com/fac/12168 -- Equinix AB1 / MainOne MDXi Abidjan; VITIB Grand Bassam location and networks.

Current facts:
- District: **Comoé** when using VITIB/Grand-Bassam location; note operator markets it under Abidjan.
- PeeringDB gives AB1 alias MainOne MDXi Abidjan, VITIB Zone Franche, Grand Bassam, CI and network list.
- MainOne/Equinix and trade press support cable-landing/data-centre role and AB1.2 expansion. Keep AB1 vs AB1.2 identity explicit; do not duplicate unless sources show distinct buildings or service products.
- Treat "Uptime Tier III standards" as B-grade design/standard claim unless Uptime record is found.

Queries:
```text
site:equinix.com "AB1" "Côte d'Ivoire" OR "Abidjan"
site:mainone.net "Côte d'Ivoire" "data centre" OR "Grand Bassam"
"MainOne" "AB1.2" "VITIB" OR "Grand Bassam"
site:peeringdb.com/fac "MainOne MDXi Abidjan" OR "Equinix AB1"
"Equinix" "Côte d'Ivoire" "carrier-neutral" OR "subsea"
```

### ST Digital -- Datacenter Services / CIV01, CloudStore

Primary / strong URLs:
- https://st.digital/zh_CN/blog/std-s-blog-presse-3/cote-d-ivoire-digital-made-in-africa-asserts-itself-with-the-inauguration-of-a-data-center-in-grand-bassam-507 -- ST Digital repost/press page; verified HTTP 200.
- https://www.peeringdb.com/fac/15646 -- ST Digital Datacenter Services / CIV01.
- https://cloudstore.africa/ -- linked from ST Digital site for CloudStore.

Current facts:
- District: **Comoé**, Grand-Bassam / VITIB.
- Inaugurated 2025-10-02 according to ST Digital reposted article; 4,000 m2 built area, about 160 racks, Tier III infrastructure claim, CloudStore sovereign-cloud positioning.
- PeeringDB confirms facility lead and lists voltage services 48 VDC / 400 VAC. Use PeeringDB for existence/location; use ST Digital article for announcement and capacity. Use Uptime only if a certificate record is found.

Queries:
```text
site:st.digital "Grand-Bassam" "data center" OR "datacenter"
"ST Digital" "VITIB" "Côte d'Ivoire" "CloudStore"
site:peeringdb.com/fac "ST DIGITAL DATACENTER SERVICES" OR "CIV01"
"ST Digital" "Tier III" "Grand-Bassam" "160 racks"
```

### PAIX Data Centres -- PAIX Abidjan / ABJ1

Primary / strong URLs:
- https://www.paix.io/ -- current company site; the old `/en/locations/abidjan` path returned 404 in this review.
- https://www.peeringdb.com/fac/6246 -- PAIX Abidjan / ABJ1, Cocody, Abidjan.
- https://annuaireidu.ci/ -- search `PAIX DATA CENTRES`; registry text says the company object includes operation/development of a neutral datacenter and colocation.

Current facts:
- District: **Abidjan**, Cocody.
- PeeringDB confirms facility existence, ABJ1 alias and Cocody/Abidjan location. Direct PAIX facility page was not available at the draft URL, so capacity values from directories (~900 m2, ~2MW, ~240 racks) remain C unless PAIX sales/spec sheet confirms them.

Queries:
```text
site:paix.io "Abidjan" OR "Côte d'Ivoire" OR "ABJ1"
site:peeringdb.com/fac/6246 "PAIX Abidjan" OR "ABJ1"
site:annuaireidu.ci "PAIX DATA CENTRES" "datacenter" OR "collocation"
"PAIX Abidjan" "Cocody" "capacity" OR "racks" OR "MW"
```

### Data Center National -- State / Sovereign

Primary URLs:
- https://www.telecom.gouv.ci/new/actualite/63
- https://www.telecom.gouv.ci/new/actualite/73
- https://www.exim.gov/news/export-import-bank-united-states-board-directors-approves-nearly-514-million-strengthen

Current facts:
- District: **Abidjan**, Anoumambo / AIGF site.
- State project, first stone 2023-12-14, 36bn FCFA, 24-month construction estimate reported by ministry in 2024, $66m EXIM guarantee approved in 2025 for Cybastion-provided equipment. This is not proof of operational status.

Queries:
```text
"Data Center National" "Anoumambo" OR "AIGF"
site:telecom.gouv.ci "Data Center National" "travaux" OR "réception" OR "mise en service"
site:exim.gov "Cybastion" "Côte d'Ivoire" "data center"
```

### Orange Côte d'Ivoire -- Grand-Bassam DC Lead

Primary / strong URLs:
- https://www.orange.ci/ and Orange Business/enterprise pages -- A only if they name the facility or services.
- Local/trade press including Digitalmag.ci, Magazine de l'Afrique/New African and Batirici are B for launch/solar/service claims.

Current facts:
- Likely district: **Comoé** if Grand-Bassam location is confirmed. Some articles may market it as Abidjan area.
- Treat as operational telco/cloud/colocation lead with B-grade facts until Orange official page, ARTCI licence/decision, CIE or VITIB evidence confirms the physical site and service scope.
- Ignore implausible directory power figures unless confirmed by Orange or utility evidence.

Queries:
```text
site:orange.ci "data center" OR "centre de données" OR "cloud" OR "hébergement"
"Orange Côte d'Ivoire" "Grand-Bassam" "data center" OR "centre de données"
"Orange CI" "colocation" OR "hébergement" "Côte d'Ivoire"
```

### MTN Côte d'Ivoire -- eCentre / Next-Generation DC Lead

Strong URLs:
- Data Center Dynamics reports on Flexenclosure/MTN Côte d'Ivoire modular facility.
- Abidjan.net article 499461 and Agence Ecofin reports on Flexenclosure contracts/inauguration.

Current facts:
- District: **Abidjan**, older reporting places the eCentre at Yopougon.
- 2014-2016 vintage modular switching/data-centre facility. It is B-grade for telco internal infrastructure and C/B only for commercial hosting unless MTN Business Côte d'Ivoire pages prove external services.

Queries:
```text
"MTN Côte d'Ivoire" "eCentre" OR "data center" OR "centre de données"
"Flexenclosure" "MTN" "Côte d'Ivoire" OR "Yopougon"
site:mtn.ci OR site:mtn.com "Côte d'Ivoire" "cloud" OR "colocation"
"MTN GlobalConnect" "2Africa" "Côte d'Ivoire" OR "Abidjan"
```

### Moov Africa CI and Local Cloud/Hosting Operators

- Moov Africa CI: https://www.moov-africa.ci/ -- A for telco presence only; no public facility page found in this review.
- Ambra Cloud, CenterServ, Stellarix and similar names are leads. Use their official pages, ARTCI, IDU and customer-facing hosting offers before creating facility records.

Queries:
```text
"Ambra Cloud" "Côte d'Ivoire" OR "Abidjan"
"CenterServ" "Abidjan" OR "Côte d'Ivoire" "serveur" OR "colocation"
"Stellarix" "Côte d'Ivoire" OR "Abidjan" "data center"
site:annuaireidu.ci "cloud" "hébergement" "Abidjan"
site:artci.ci "{operator}" "licence" OR "autorisation"
```

## Connectivity and Interconnection Feeds

Use these as demand-side signals and facility corroboration, not as standalone proof of a commercial data centre unless a facility is named.

- MainOne: Grand-Bassam landing and data centre/cable-landing station evidence via MainOne page and SubCom/Submarine Networks releases.
- PeeringDB: Equinix AB1 fac/12168, PAIX Abidjan fac/6246, ST Digital CIV01 fac/15646, CIVIX organization/exchange records.
- ACE / SAT-3/WASC / 2Africa: search landing announcements, landing partners and activation dates. For 2Africa, MTN GlobalConnect and Agence Ecofin are useful but require official landing/ready-for-service confirmation.

Queries:
```text
"MainOne" "Grand Bassam" "cable landing station" "data centre"
"ACE submarine cable" "Abidjan" OR "Côte d'Ivoire"
"SAT-3" OR "WASC" "Côte d'Ivoire" "landing"
"2Africa" "Côte d'Ivoire" OR "Abidjan" OR "Grand-Bassam"
site:peeringdb.com "Côte d'Ivoire" "Facility" OR "Abidjan" OR "Grand Bassam"
"CIVIX" "Abidjan" "PeeringDB"
```

## Hyperscaler and Cloud Region Tracking

Official pages to re-check each batch:
- AWS regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- AWS Local Zones: https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle regions: https://www.oracle.com/africa/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

Queries:
```text
site:aws.amazon.com "Côte d'Ivoire" OR "Ivory Coast" "region" OR "Local Zone"
site:learn.microsoft.com "Côte d'Ivoire" OR "Ivory Coast" "Azure region"
site:cloud.google.com "Côte d'Ivoire" OR "Ivory Coast" "locations"
site:oracle.com "Côte d'Ivoire" OR "Ivory Coast" "cloud region"
"AWS" OR "Azure" OR "Google Cloud" "Abidjan" "PoP" OR "edge"
```

Record a negative result only as of the run date and with the official URL checked.

## Trade Press and Aggregators

| Source | Grade | Use |
|---|---:|---|
| datacenterdynamics.com | B | Raxio launch, MainOne/AB1.2, MTN/Flexenclosure, regional context. |
| capacitymedia.com / datacenterknowledge.com | B | MainOne and Africa expansion stories. |
| connectingafrica.com / thetechcapital.com | B | Raxio, investment and market launches. |
| agenceecofin.com / ecofinagency.com | B | French/English telco, 2Africa and government-project coverage. |
| techafricanews.com / wearetech.africa / ITWeb Africa / Financial Afrik | B | ST Digital, EXIM, sovereign DC, MainOne. |
| FratMat / AIP / Abidjan.net / Digitalmag.ci / Jeune Afrique | B-/C+ | Ceremonies, local status, ministerial remarks; verify technical numbers. |
| PeeringDB | A- | Facility existence, aliases, coordinates, network presence. |
| Datacenter Map / Baxtel / OCOLO / Datacenters.com / HostDir / Data Center Planet | C | Lead discovery only; never final capacity/status without stronger source. |
| Systalink and SEO blogs | C | Useful market synthesis; verify every operator, address and number. |

## Per-District Industry Sweep

| District | Search focus | Current expectation |
|---|---|---|
| Abidjan | PAIX, MTN, Data Center National, Ambra, CenterServ, banks, enterprise cloud, Cocody/Yopougon/Plateau/Port-Bouët terms. | Positive. Verify PAIX and state DC; telco/internal leads. |
| Yamoussoukro | government DR, ministries, district portal, telecom POPs. | No verified commercial DC. |
| Bas-Sassandra | San-Pédro port, industrial logistics, telco POPs. | No verified DC. |
| Comoé | Grand-Bassam, VITIB, ZBTIC, Raxio, Equinix/MainOne, ST Digital, Orange. | Positive and high priority. |
| Denguélé | Odienné, Minignan, telco POPs. | No verified DC. |
| Gôh-Djiboua | Gagnoa, Divo, education/government hosting. | No verified DC. |
| Lacs | Dimbokro, Toumodi, Daoukro. | No verified DC. |
| Lagunes | Dabou, Agboville, Adzopé, Tiassalé, Abidjan spillover. | No verified DC; possible future industrial/edge leads. |
| Montagnes | Man, Duékoué, Guiglo. | No verified DC. |
| Sassandra-Marahoué | Daloa, Bouaflé, Zuénoula. | No verified DC. |
| Savanes | Korhogo, Ferkessédougou, Boundiali. | No verified DC; future edge candidate. |
| Vallée du Bandama | Bouaké, Katiola, university/telco/backbone. | No verified commercial DC; future DR/edge candidate. |
| Woroba | Séguéla, Mankono, Touba. | No verified DC. |
| Zanzan | Bondoukou, Bouna, border connectivity. | No verified DC. |

Universal industry queries:
```text
"{district}" OR "{capital}" "data center" OR "centre de données" "Côte d'Ivoire"
"{capital}" "hébergement" OR "colocation" OR "cloud" OR "serveur dédié"
"{operator}" "{district}" OR "{capital}" "Côte d'Ivoire"
"{capital}" "Orange" OR "MTN" OR "Moov" "cloud" OR "data center"
"{district}" "Tier III" OR "Tiers 3" OR "baies" OR "MW"
site:peeringdb.com "{capital}" OR "{district}" "CI"
```

## Verification Pipeline

1. Seed from A/A- sources: Raxio official page, Equinix official/PeeringDB, ST Digital/PeeringDB, PAIX PeeringDB/IDU, ministry/EXIM for state DC.
2. Add B-grade trade press for launch dates and announced capacities; flag any number not on official/operator pages.
3. Join official records: ARTCI licence/data-protection, SIGUPC permits, VITIB zone records, CIE/CI-ENERGIES/ANARE power, ANDE/EIES, IDU/CEPICI and Uptime.
4. Run the 14-district sweep. Only mark `no_projects: true` for non-Abidjan/Comoé districts after French and English terms plus operator-name queries fail.
5. Normalize status terms: announced/MoU < financed < permitted < first stone < under construction < inaugurated/launched < operational. Keep financing and ground-breaking separate from operation.
6. De-duplicate marketed names: one physical VITIB site may appear as Abidjan, Grand-Bassam, MainOne, MDXi or Equinix. Use coordinates/address/operator page to decide whether records are separate buildings or aliases.

## Common Pitfalls

- Filing VITIB facilities under Abidjan without a Comoé district note.
- Treating `Tier III standards`, `Tiers 3`, or directory `Tier` values as Uptime certification. Only Uptime or operator certificate evidence is A.
- Copying directory power numbers, especially implausible MW values, into final records.
- Treating a cable landing station, telco switch or bank IT room as commercial colocation without service evidence.
- Treating the national DC's EXIM guarantee as commissioning.
- Leaving dead URLs in seed lists. The stale PAIX `/en/locations/abidjan` path should be replaced by PAIX homepage + PeeringDB/IDU evidence until PAIX publishes a current facility page.
