# MG Explorer Official - Madagascar Datacenter Enumeration via Official, Regulatory, Energy, Procurement, and Cloud Sources

Date: 2026-08-12. Country: **MG Madagascar**. Division model: **province** (`faritany`): **Antananarivo; Antsiranana; Fianarantsoa; Mahajanga; Toamasina; Toliara**. Angle: official/primary-source methodology for finding operational, planned, government, telecom, and datacenter-like facilities.

Reliability grades are per fact, not per entity:
- **A** = official/primary source proving the specific claim: government/regulator/statute, SOE/utility, World Bank project record, operator-owned facility page, cloud-provider official region list, certification registry.
- **B** = reputable press/trade source with named parties, dates, and places: DCD, SubTel Forum, Submarine Networks, Connecting Africa, Agence Ecofin, 2424.mg, L'Express, Midi, World Bank-adjacent summaries.
- **C** = directory, marketplace, social page, search snippet, Wikipedia/Statoids-style seed, or market-report snippet. Use for leads only until matched to primary evidence.
- **U** = unresolved after this pass. Do not promote U-grade facts to facility records.

## 0. Verified national baseline

- Madagascar currently uses **24 regions** as de facto first-level units, but ISO 3166-2:MG and the requested methodology model use the **6 provinces**: Antananarivo, Antsiranana, Fianarantsoa, Mahajanga, Toamasina, and Toliara. ISO lists those six province codes at https://www.iso.org/obp/ui/#iso:code:3166:MG . Secondary subdivision references: https://statoids.com/umg.html and https://www.geonames.org/MG/administrative-division-madagascar.html .
- Province coverage is complete for the six requested provinces. Use this 2026 region-to-province working map in searches:

| Province | Regions to sweep | Main anchor cities |
|---|---|---|
| Antananarivo | Analamanga, Vakinankaratra, Itasy, Bongolava | Antananarivo, Antsirabe |
| Antsiranana | Diana, Sava | Antsiranana/Diego-Suarez, Nosy Be, Sambava |
| Fianarantsoa | Amoron'i Mania, Haute Matsiatra, Ihorombe, Atsimo-Atsinanana, Vatovavy, Fitovinany | Fianarantsoa, Ambositra, Manakara, Mananjary |
| Mahajanga | Boeny, Betsiboka, Melaky, Sofia | Mahajanga/Majunga, Antsohihy |
| Toamasina | Atsinanana, Analanjirofo, Ambatosoa, Alaotra-Mangoro | Toamasina/Tamatave, Ambatondrazaka, Fenoarivo Atsinanana |
| Toliara | Atsimo-Andrefana, Androy, Anosy, Menabe | Toliara/Tulear, Taolagnaro/Fort Dauphin, Morondava |

- There is **no public national datacenter registry** and no public datacenter-specific licence class found. Enumeration must triangulate telecom licensing, operator pages, planning/environment records, energy connection evidence, public procurement, cable/IXP records, and certification/directories.
- The commercial market is very small and concentrated in **Antananarivo province**. ISOC Pulse reports **1 active data center** and **1 IXP** in Madagascar for 2026 (https://pulse.internetsociety.org/en/reports/mg/). Treat the ISOC number as a B-grade market indicator, not as an exhaustive facility registry, because STELLARIX's own site now lists two Antananarivo data centers.
- The strongest current facility evidence is **STELLARIX**. Its own website states it is a Madagascar data-hosting and infrastructure-management specialist and names two Madagascar data centers: **TNR1 Analakely, Lalana Paul Dussac, Antananarivo 101** and **TNR2 Galaxy, Building KUBE D 2nd floor Galaxy Andraharo, BP 763 Antananarivo 101** (https://stellar-ix.com/en/a-propos-de-stellarix/ and https://www.stellar-ix.com/en/). Grade **A for operator-owned facility/address claims**. Its “TIER III ready” language is **operator claim only**, not Uptime/TIA certification unless confirmed in a registry.
- PeeringDB lists **Bâtiment Sirius / Zone Galaxy Andraharo, Antananarivo 101** as a facility for MGIX and shows **MGIX** as a local exchange there (https://www.peeringdb.com/fac/2993 and https://www.peeringdb.com/org/14435). Grade **C/A-by-source**: PeeringDB is self-reported, but useful for interconnection/address leads.
- DataCenterMap lists **2 Antananarivo data centers** and has an entry for **STELLARIX Antananarivo TNR01** at Immeuble Tanashore / Enceinte Futura (https://www.datacentermap.com/madagascar/antananarivo/ and https://www.datacentermap.com/madagascar/antananarivo/tnr011/). Grade **C**, because directory records must be matched to the operator page and local address evidence before use.

## 1. Search vocabulary

French is the main official and business language for government, telecom, and local press. English is useful for cable, cloud, trade press, and international directories. Malagasy terms have low yield and should be used only as discovery seeds.

French terms:
```text
centre de données | centre de traitement de données | datacenter | data center
hébergement de données | hébergement de serveurs | colocation | co-location | serveur | salle serveur
cloud | informatique en nuage | infrastructure numérique | infrastructure digitale
point d'échange Internet | IXP | peering | point de présence | PoP
câble sous-marin | station d'atterrissement | station de câble | fibre optique | backbone
site de secours | reprise d'activité | PRA | continuité d'activité
licence | autorisation | régime de déclaration | opérateur télécoms
permis de construire | étude d'impact environnemental | EIE | raccordement électrique
délestage | groupe électrogène | onduleur | refroidissement | puissance installée
appel d'offres | marché public | acquisition de serveurs | infrastructure virtuelle
souveraineté numérique | données à caractère personnel | gouvernement digital
```

English terms:
```text
data center | data centre | datacenter | colocation | colo | hosting | cloud
server room | network operations centre | NOC | disaster recovery | DR site
internet exchange | IXP | peering | cable landing station | CLS | submarine cable
satellite gateway | ground station | Starlink | OneWeb | O3b
Tier III | Uptime Institute | TIA-942 | racks | kW | MW | MVA
```

Malagasy discovery terms:
```text
foibe data | foiben-drakitra | rahona | mpampiantrano | tambajotra | tariby amban-dranomasina | herinaratra
```

## 2. Official / regulatory pipeline

### 2.1 Telecom and ICT regulator - ARTEC

Primary routes:
- ARTEC home: https://www.artec.mg/
- About / mandate: https://www.artec.mg/artec-madagascar-regulation-telecoms-et-tic-a-propos/
- Loi n°2005-023 PDF: https://www.artec.mg/wp-content/uploads/2024/10/loi_2005-023.pdf
- Declaration/licensing pages: https://www.artec.mg/regime-de-declaration/ , https://www.artec.mg/regime-libre/ , https://www.artec.mg/delivrance-de-licence/
- ARTEC 2024 activity report: https://www.artec.mg/wp-content/uploads/2025/11/RAPPORT-DACTIVITES-2024_FINAL.pdf

Use ARTEC to identify telecom operators, satellite authorisations, service categories, and regulatory changes. ARTEC is not a facility registry. The 2024 activity-report snippet confirms ARTEC decision n°2024/02-ARTEC/DG/L of 2024-04-29 granting a satellite licence to **Starlink Madagascar**; 2424.mg also reports the five-year licence and EUR 100,000 initial fee (https://2424.mg/starlink-madagascar-obtient-sa-licence-internet-satellite-moyennant-100-000-euros/). Grade **A for ARTEC licence fact when the ARTEC PDF is used; B for press details**. This is not ground-station or datacenter evidence.

Queries:
```text
site:artec.mg ("centre de données" OR datacenter OR "data center" OR cloud OR hébergement OR IXP)
site:artec.mg (Starlink OR satellite OR "licence satellite" OR "régime de déclaration")
site:artec.mg (Telma OR Yas OR Orange OR Airtel OR Gulfsat OR STELLARIX)
"ARTEC" "Madagascar" ("centre de données" OR datacenter OR hébergement OR colocation)
"decision n°2024/02-ARTEC/DG/L" Starlink Madagascar
```

### 2.2 Digital ministry, UGD, and PRODIGY

Primary routes:
- Digital ministry MNDPT: https://mndpt.gov.mg/
- Unité de Gouvernance Digitale (UGD): https://digital.gov.mg/
- PRODIGY / World Bank project P169413: https://www.worldbank.org/en/news/loans-credits/2020/09/29/madagascar-digital-governance-and-identification-management-system-project and https://documents.worldbank.org/en/publication/documents-reports/documentdetail/344611594308641385

The World Bank identifies PRODIGY / Digital Governance and Identification Management System Project, project ID **P169413**, with a US$140 million equivalent IDA credit and a project objective to strengthen the ID-M system and government capacity to deliver services in selected sectors. UGD publishes tenders and addenda on digital.gov.mg for biometric, virtual-infrastructure, server, connectivity, and anti-power-cut equipment. Grade **A for project/tender existence**. Do not infer a national government datacenter unless a tender, ESMP, or official page names a facility, address, or hosting arrangement.

Queries:
```text
site:digital.gov.mg ("centre de données" OR datacenter OR "data center" OR hébergement OR serveur OR "infrastructure virtuelle")
site:digital.gov.mg (PRODIGY OR biométrique OR interopérabilité OR X-Road OR "identifiant unique") (serveur OR données OR infrastructure)
site:mndpt.gov.mg ("centre de données" OR datacenter OR cloud OR souveraineté OR "stratégie numérique")
"P169413" Madagascar (server OR cloud OR data center OR infrastructure OR hosting)
"Madagascar" "centre de données national" OR "national data center" OR "sovereign cloud"
```

### 2.3 Data protection and data-residency context

Primary route:
- Loi n°2014-038 on personal data, hosted by the digital portal: https://digital.gov.mg/2022/07/05/loi-n-2014-038-sur-la-protection-des-donnees-a-caractere-personnel/

Use data-protection material as demand/regulatory context only. It does not identify datacenters. If a functioning supervisory authority, registration list, or data-residency rule is found later, add it as an official pipeline lead and keep the grade tied to the exact fact.

Queries:
```text
"loi n°2014-038" Madagascar données personnelles hébergement
site:digital.gov.mg "protection des données" Madagascar hébergement cloud
"Madagascar" "données à caractère personnel" "localisation" OR "hébergement"
```

### 2.4 Energy and utility evidence - JIRAMA

Primary routes:
- JIRAMA home: https://www.jirama.mg/
- About: https://www.jirama.mg/la-jirama/
- IMF selected issues on Madagascar electricity/JIRAMA: https://www.imf.org/en/publications/selected-issues-papers/issues/2025/03/31/the-electricity-sector-and-jirama-republic-of-madagascar-565708

JIRAMA says it produces, transports, and distributes electricity and supplies water across Madagascar. Energy reliability is a major siting constraint; the IMF notes JIRAMA struggles with production inefficiency, losses, below-cost tariffs, and low access. Treat power evidence as corroboration for serious datacenter loads: dedicated feeders, transformer capacity, generator/fuel permits, UPS/cooling procurement, or named enterprise tariffs. Do not promote a facility solely from a utility outage article.

Queries:
```text
site:jirama.mg ("centre de données" OR datacenter OR serveur OR informatique OR "raccordement")
site:jirama.mg (STELLARIX OR Telma OR Yas OR Orange OR Airtel OR Galaxy OR Andraharo)
"JIRAMA" "data center" OR "centre de données" Madagascar
"délestage" Madagascar (STELLARIX OR Telma OR Orange OR Airtel OR "centre de données")
"Antananarivo" "groupe électrogène" "data center" OR datacenter
```

### 2.5 Investment promotion and company setup - EDBM / ORINASA

Primary routes:
- EDBM: https://edbm.mg/
- ORINASA one-stop company creation: https://orinasa.edbm.mg/
- U.S. State Department 2024 ICS: https://2021-2025.state.gov/reports/2024-investment-climate-statements/madagascar/
- U.S. ITA digital economy guide: https://www.trade.gov/country-commercial-guides/madagascar-digital-economy

Use EDBM/ORINASA for investor and legal-entity pivots, especially STELLARIX, AXIAN/Telma/Yas, and ICT/BPO investors. The State Department describes EDBM as Madagascar's one-stop investment shop; trade.gov says Madagascar launched **Choose Digital Madagascar** in February 2025 to attract digital-economy investment. These sources are not facility records unless they name a datacenter project or investor site.

Queries:
```text
site:edbm.mg (datacenter OR "data center" OR "centre de données" OR cloud OR numérique OR ICT OR BPO)
site:orinasa.edbm.mg (STELLARIX OR "Stellar-IX" OR "Telma" OR "Yas" OR Orange OR Airtel)
"Choose Digital Madagascar" (datacenter OR cloud OR infrastructure OR hébergement)
"EDBM" Madagascar ("centre de données" OR datacenter OR cloud OR "infrastructure numérique")
```

### 2.6 Planning, building permits, and environment

Primary/official routes:
- Office National pour l'Environnement (ONE): https://www.pnae.mg/ and ministry profile https://www.environnement.mg/organisme-rattache/office-national-pour-lenvironnement/
- Ivotoro procedure page for permis de construire: https://www.ivotoro.mg/procedure/permis-de-construire/

ONE is the environmental authority route for EIE/E&S records. Ivotoro describes the building-permit workflow: request to the relevant commune, referral to SRAT, and projects above 1,000 m2 routed to the ministry responsible for land-use/planning competence. Building permits are not exposed in one national searchable database. Grade **A** only when an official document names the applicant, parcel/site, and project; **B/C** for explanatory private articles or press.

Queries:
```text
site:pnae.mg ("centre de données" OR datacenter OR télécommunications OR "station d'atterrissement" OR fibre)
site:environnement.mg ("centre de données" OR datacenter OR EIE OR "étude d'impact")
"permis de construire" Madagascar (datacenter OR "centre de données" OR télécommunications OR "salle serveur")
"étude d'impact environnemental" Madagascar ("câble sous-marin" OR datacenter OR télécommunications OR fibre)
"Galaxy Andraharo" permis construire OR EIE OR JIRAMA
"Lalana Paul Dussac" permis construire OR EIE OR STELLARIX
```

### 2.7 Public procurement

Primary routes:
- ARMP: http://armp.mg/
- UGD tenders: https://digital.gov.mg/
- e-GP rollout coverage: https://appn-racop.org/madagascar-une-plateforme-en-ligne-e-gp-pour-ameliorer-le-processus-de-passation-et-dexecution-des-marches-publics/

Search procurement for server rooms, hosting, government cloud, virtual infrastructure, identity-system hardware, civil-registry modernization, power backup kits, and ministry disaster recovery. Grade **A** for official tender/award documents; **B/C** for third-party tender indexers.

Queries:
```text
site:armp.mg ("centre de données" OR datacenter OR hébergement OR serveurs OR cloud OR "infrastructure virtuelle")
site:digital.gov.mg ("appel d'offres" OR DAOI OR addendum) (serveur OR cloud OR hébergement OR "infrastructure virtuelle")
"marché public" Madagascar ("centre de données" OR datacenter OR serveurs OR cloud OR hébergement)
"appel d'offres" Madagascar PRODIGY serveur OR infrastructure OR cloud
```

### 2.8 Official cloud-region checks

No AWS, Azure, Google Cloud, or Oracle OCI public cloud region/local zone was found in Madagascar on official lists during this pass. Recheck every refresh, because absence can change.

| Provider | Official list | MG status on 2026-08-12 | Grade |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | AWS page lists global regions/AZs; no Madagascar region/local zone found | A for list check |
| Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | Azure public-region list has no Madagascar entry | A |
| Google Cloud | https://cloud.google.com/about/locations | No Madagascar region/zone found | A |
| OCI | https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | No Madagascar region found | A |

Queries:
```text
"Madagascar" ("AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region")
"Madagascar" ("Local Zone" OR "edge location" OR "cloud region" OR "sovereign cloud")
```

## 3. Province coverage workflow

Run the same workflow for all six provinces and explicitly record negative results. Anchor-city searches must include both French and English names where applicable.

| Province | Official-first route | Expected result |
|---|---|---|
| Antananarivo | STELLARIX operator pages; ARTEC; JIRAMA; Antananarivo/Analamanga planning; ARMP/UGD; PeeringDB/MGIX | Highest yield. Confirm STELLARIX TNR1/TNR2, MGIX/Batiment Sirius, telecom NOCs, government/server tenders, bank DR rooms. |
| Antsiranana | ARTEC operator coverage, Nosy Be/Sambava ICT projects, commune/ONE searches, satellite gateway terms | Expect telecom PoPs and enterprise server rooms only; no public commercial DC found. |
| Fianarantsoa | UGD civil-status/identity projects, university/government server procurement, JIRAMA reliability | Expect government/service server rooms only; no public commercial DC found. |
| Mahajanga | 2Africa landing in Mahajanga, Telma/Vodafone cable evidence, port/telecom planning, JIRAMA | Important connectivity province because 2Africa landed at Mahajanga. Treat CLS as connectivity unless hosting evidence appears. |
| Toamasina | LION/LION2 Toamasina landing, port/industrial ICT, Ambatovy enterprise IT, JIRAMA | Important cable/port province. LION/LION2 land at Toamasina. No public commercial DC found. |
| Toliara | METISS Fort Dauphin/Taolagnaro lead, QMM/mining enterprise IT, port/energy projects | Important cable/enterprise lead because METISS landed at Fort Dauphin/Taolagnaro. No public commercial DC found. |

Province query template:
```text
"{province}" OR "{anchor city}" Madagascar ("centre de données" OR datacenter OR "data center" OR hébergement OR colocation OR serveur)
"{anchor city}" Madagascar ("station d'atterrissement" OR "câble sous-marin" OR "cable landing" OR fibre)
site:artec.mg "{anchor city}" OR "{operator}"
site:armp.mg "{anchor city}" (serveur OR hébergement OR cloud OR informatique)
site:digital.gov.mg "{anchor city}" (PRODIGY OR serveur OR identité OR état civil)
site:pnae.mg "{anchor city}" (EIE OR télécommunications OR fibre OR datacenter)
site:jirama.mg "{anchor city}" (raccordement OR délestage OR industriel OR "gros client")
```

## 4. Facility and project seed list for enumerators

| Seed | Province / location | Evidence | Grade | Enumeration handling |
|---|---|---|---|---|
| STELLARIX TNR1 Analakely | Antananarivo, Lalana Paul Dussac, Antananarivo 101 | Operator page names TNR1 and address: https://stellar-ix.com/en/a-propos-de-stellarix/ | A for operator facility/address claim | Confirm parcel, operations status, power, and any certification separately. |
| STELLARIX TNR2 Galaxy | Antananarivo, Building KUBE D 2nd floor Galaxy Andraharo, BP 763, Antananarivo 101 | Operator page names TNR2 and address: https://stellar-ix.com/en/a-propos-de-stellarix/ | A for operator facility/address claim | Cross-check against PeeringDB Batiment Sirius/Zone Galaxy and MGIX. |
| MGIX / Batiment Sirius | Antananarivo, Zone Galaxy Andraharo | PeeringDB facility and org pages; ISOC Pulse IXP tracker | C/A-by-source for PeeringDB, B for ISOC indicator | IXP/interconnection facility. Count as DC only if hosting/colo/data hall evidence exists. |
| Telma/Yas historical NOC and disaster recovery centre | Antananarivo | Yas/Telma 2011 corporate PDF says Antananarivo-based NOC and disaster recovery centre: https://services.yas.mg/data/corporate/2011_en.pdf | A for old operator statement; current status U | Use as historical lead; refresh against Yas/STELLARIX current pages. |
| PRODIGY government compute/tenders | Mostly Antananarivo; pilots in provinces | UGD and World Bank P169413 | A for project/tender existence | Do not create facility unless source names hosting site/address. |
| 2Africa Madagascar landing | Mahajanga province, Mahajanga | Connecting Africa says Telma/Vodafone teams at Mahajanga landing site in Feb 2023; 2Africa official says core complete and ready in most landing countries | B for landing; A/B for system status | Connectivity site, not DC. Check Telma/ARTEC/permits for CLS building. |
| LION/LION2 | Toamasina province, Toamasina | LION official site/search snippet and Submarine Networks; consortium includes Orange Madagascar/Mauritius Telecom/France Telecom | A/B for cable/landing | Connectivity site, not DC. |
| METISS | Toliara province, Fort Dauphin/Taolagnaro lead | Submarine Networks says in service since March 2021; press reports Madagascar landing at Fort Dauphin | B | Connectivity site, not DC. Confirm local CLS/operator and exact town. |
| Starlink Madagascar | National | ARTEC 2024 activity report snippet; 2424.mg and Agence Ecofin coverage | A for licence if ARTEC PDF used; B for press | No gateway/DC evidence found. |

## 5. Decision rules and pitfalls

- **Do not overcount cable landing stations.** Toamasina, Mahajanga, and Fort Dauphin/Taolagnaro cable sites are connectivity infrastructure unless the source says they host servers, colocation, cloud, or a datacenter facility.
- **Do not treat “Tier III ready” as certified.** STELLARIX can be A-grade for facility names/addresses from its own site, but Uptime/TIA certification is separate. Uptime search surfaced STELLARIX Tanzania, not Madagascar; TIA/EPI searches did not surface a Madagascar STELLARIX certificate in this pass.
- **Resolve STELLARIX address conflicts before final records.** Operator page says TNR1 Analakely and TNR2 Galaxy Andraharo; DataCenterMap has TNR01 at Immeuble Tanashore / Enceinte Futura; PeeringDB has Batiment Sirius / Zone Galaxy. Keep all as address leads until operator/parcel evidence reconciles them.
- **ISOC Pulse can be stale or scoped differently.** It reports one active data center, while STELLARIX says two. Use ISOC as market baseline and use facility-level evidence for records.
- **Operator existence is not facility evidence.** Telma/Yas, Orange Madagascar, Airtel Madagascar, Gulfsat, Blueline/BIP, and Starlink are A/B for operator or licence facts only. They become DC records only with named facility/service/address evidence.
- **Capacity stays null unless explicit.** Do not infer MW, racks, or square meters from cable capacity, operator market share, tier language, or investment announcements.
- **Grade separately.** Example: Starlink licence can be A/B; Starlink ground gateway is U if no source names one. 2Africa landing at Mahajanga can be B; a Mahajanga datacenter remains U without hosting/compute evidence.

## 6. Refresh cadence

- **Quarterly:** STELLARIX site and jobs; PeeringDB MGIX/facility records; ISOC Pulse MG report and IXP tracker; ARTEC licence/news PDFs; UGD/PRODIGY tenders; ARMP searches; cable status for 2Africa, LION/LION2, METISS, Africa-1; local press for JIRAMA outages affecting Antananarivo/Mahajanga/Toamasina/Taolagnaro.
- **Semi-annual:** AWS/Azure/GCP/OCI official region lists; Uptime Institute awards; TIA/EPI lists; DataCenterMap/OCOLO/Inflect/datacenters.com; EDBM/Choose Digital Madagascar publications; operator enterprise pages for Yas/Telma, Orange, Airtel, Gulfsat.
- **Annual:** telecom law/regulatory changes; data-protection authority status; State Department investment climate statement; trade.gov ICT/digital-economy guide; regional/province mapping updates.

## 7. Validation log - 2026-08-12

Live web checks confirmed these URLs or search-result snippets as usable: ISO OBP, ISOC Pulse MG report, ARTEC about/licensing/report/PDF routes, UGD/digital.gov.mg, World Bank P169413, JIRAMA, IMF JIRAMA paper, EDBM/ORINASA/State/trade.gov routes, ONE/pnae.mg and environnement.mg, Ivotoro permis de construire procedure, AWS/Azure/GCP/OCI official region lists, STELLARIX official site/about page, PeeringDB MGIX/Batiment Sirius, DataCenterMap Antananarivo/STELLARIX, 2Africa official site, Submarine Networks LION/METISS, Connecting Africa 2Africa Madagascar, 2424.mg/Agence Ecofin Starlink. Remaining unresolved facts are explicitly marked as leads or U-grade rather than promoted.
