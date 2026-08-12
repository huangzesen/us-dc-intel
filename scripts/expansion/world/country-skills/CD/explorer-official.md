# CD Explorer Official - Democratic Republic of the Congo Datacenter Enumeration via Planning, ARPTC, Energy, Cloud, Colo, and Trade Sources

Date: 2026-08-12. Country: **CD Congo, Democratic Republic of the**. Division model: **26 province/city divisions**: Central Kongo, Lower Uele, Equator, Upper Katanga, Upper Lomami, Upper Uele, Ituri, Central Kasai, Eastern Kasai, Kwango, Kwilu, Kinshasa, Kasai, Lomami, Lualaba, Maniema, Mai-Ndombe, Mongala, North Kivu, North Ubangi, Sankuru, South Kivu, South Ubangi, Tanganyika, Tshopo, Tshuapa. Angle: **official/regulatory/cloud pipeline** for finding commercial colocation, carrier-neutral, telco, government, cloud/edge, and project-stage data-centre facilities.

Reliability grades:
- **A** = official/primary/legal source: GUPEC construction-permit record, national/provincial urbanisme/habitat source, ARPTC licence/authorization/declaration material, ARE/SNEL electrical title or official grid/connection evidence, Ministry/ADN/PTNTIC government-cloud record, official cloud-provider location page, official operator facility page, Uptime Institute certification record, official procurement notice.
- **B** = strong secondary source: DCD/Connecting Africa/Ecofin/CIO Mag/Telecompaper/Computer Weekly, Internet Society/PeeringDB/IXP operator record, donor/investment market brief, developer or construction-contractor case study, reputable local business press.
- **C** = weak lead: generic market report, directory-only listing, social post, map listing, unsupported "data center" claim, national strategy target without named site or construction status.

---

## 0. DRC-specific structure facts

- The DRC does **not** have a complete national public datacenter registry. Enumeration must combine: **GUPEC construction-permit workflow**, **provincial/urbanisme sources**, **ARPTC telecom titles and observatories**, **ARE/SNEL electricity evidence**, **ADN/Ministry digital-government sources**, **official operator pages**, **Uptime Institute records**, **cloud-provider region lists**, **IXP/PeeringDB leads**, and **trade press**.
- Official language is French. Search French first, then English variants. High-yield terms: `centre de donnees`, `centres de donnees`, `data center`, `datacenter`, `centre d'hebergement`, `hebergement datacenter`, `cloud souverain`, `nuage souverain`, `colocation`, `co-location`, `carrier neutral`, `neutre`, `Tier III`, `TIER 3`, `Uptime`, `salle serveur`, `serveurs`, `internet exchange`, `point d'echange Internet`, `IXP`, `poste electrique`, `33kV`, `MVA`, `MW`, `permis de construire`, `GUPEC`, `urbanisme`, `EIES`, `etude d'impact environnemental et social`.
- Practical facility evidence is **Kinshasa-first**. Current strong facility seeds are Raxio DRC1 in Limete industriel, OADC Texaf Kinshasa at SILIKIN Village/COTEX, Orange Business RDC datacenter service, and weaker GBS/United hosting-directory leads. Non-Kinshasa province searches should expect many negative results except telco core/switch rooms, government digitisation projects, mining-campus IT rooms, energy projects, or IXP/edge nodes.
- Be strict on country disambiguation. `Congo`, `Congo data center`, and `datacenter national du Congo` often return **Republic of Congo / Brazzaville (CG)**. Always include `RDC`, `RD Congo`, `Congo-Kinshasa`, `Republique Democratique du Congo`, `DRC`, or a DRC city/province in queries.
- The Plan National du Numerique Horizon 2025 is useful as policy context and a province-capital lead generator, but it is **not facility evidence by itself**. It called for data-hosting centres for public/market/institutional use and promoted certified, interconnected data centres by provincial capitals; only assign facilities where a named site/operator/procurement/permitting source exists.

---

## 1. Official/regulatory portals and how to use them

### 1.1 Construction permits, urban planning, land, and environment

Primary sources:
- GUPEC - Guichet Unique de delivrance de Permis de Construire: https://gupec-rdc.com/
- GUPEC note that construction permits are issued through GUPEC nationally: https://gupec-rdc.com/le-permis-de-construire-est-delivre-par-le-gupec/
- GUPEC online/request pages: https://gupec-rdc.com/demande-de-permis/ and https://gupec-rdc.com/gupec-en-ligne/
- Ministry of Urbanisme et Habitat: https://urbanisme.gouv.cd/
- Ministry of Environment and Sustainable Development: https://medd.gouv.cd/
- Agence Congolaise de l'Environnement (ACE) references are often surfaced through MEDD, project EIES PDFs, and donor documents rather than a reliable searchable standalone register.

Use GUPEC as the **A-grade construction-permit workflow anchor**. The public site states that any person wishing to build in DRC, in urban or rural areas, must obtain a construction permit from GUPEC. A searchable public permit register was not found in this pass, so enumeration normally requires web-indexed GUPEC/urbanisme notices, ministerial releases, local press naming permits, or direct permit documents.

Permit/planning query templates:

```text
site:gupec-rdc.com "data center"
site:gupec-rdc.com "centre de données"
site:gupec-rdc.com "datacenter"
site:gupec-rdc.com "permis de construire" "{operator}"
site:urbanisme.gouv.cd "centre de données"
site:urbanisme.gouv.cd "permis de construire" "Kinshasa"
site:urbanisme.gouv.cd "{province}" "permis de construire" "data center"
site:cadastre.gouv.cd "{operator}" "Kinshasa"
site:medd.gouv.cd "centre de données" "EIES"
site:medd.gouv.cd "data center" "étude d'impact"
site:medd.gouv.cd/wp-content/uploads "{operator}" "EIES"
"{operator}" "RDC" "permis de construire"
"{operator}" "Kinshasa" "GUPEC"
"{facility}" "Limete" "permis de construire"
"{facility}" "SILIKIN" "EIES"
```

Extract from any permit/EIES/planning record: province/city, commune/territory, avenue/parcel/concession, proponent legal entity, project description, floors/white space, IT load or site load, utility import voltage/MVA, standby generators and fuel storage, cooling/water, EIES/certificat environmental status, permit/approval dates, and construction/occupancy status.

### 1.2 ARPTC telecom regulator

Primary sources:
- ARPTC homepage: https://arptc.gouv.cd/
- ARPTC telecommunications titles page: https://arptc.gouv.cd/telecommunications/
- ARPTC publications/observatories: https://arptc.gouv.cd/observatoires/ and https://arptc.gouv.cd/observatoire-internet/
- ARPTC guichet unique link from homepage: https://www.servicemanagementquality.com/
- Leganet copy of AM 037/2022 on telecom concessions: https://www.leganet.cd/Legislation/Droit%20economique/telecommunication/AM.037.2022.11.07.2022.html
- Leganet copy of AM 036/2022 on authorizations: https://www.leganet.cd/Legislation/Droit%20economique/telecommunication/AM.036.11.07.2022.html

ARPTC is useful for **operator/service legality and network role**, not a complete physical-facility register. The official telecom page lists concession categories including `reseau et services des telecommunications`, wholesale services over network infrastructure, services/applications, and basic infrastructure such as national backbone, landing stations, and international transit centres. It also lists authorizations for telecom-equipment installation/construction, infrastructure sharing/management by third parties, leased-line commercialization, virtual networks, and declarations for internal networks, value-added services, hotspots, and community internet exchange points.

High-yield ARPTC names:
- Commercial/colo/interconnect: `Raxio Data Centre SAS`, `Open Access Data Centres`, `OADC Texaf Digital DRC`, `WIOCC`, `TEXAF`, `Orange RDC`, `Global Broadband Solution`, `United S.A.`, `Microcom`, `Standard Telecom Congo`, `Orioncom`, `Paratus`, `ITM`.
- Mobile/telco: `Vodacom Congo`, `Airtel RDC`, `Orange RDC`, `Africell RDC`, `SCPT`, `Liquid`, `Bandwidth and Cloud Services`, `AFR-IX`.
- IX/peering: `KINIX`, `ACIX`, `Internet pour tous`, `ISPA-DRC`, `point d'echange Internet`.

ARPTC query templates:

```text
site:arptc.gouv.cd "centre de données"
site:arptc.gouv.cd "data center"
site:arptc.gouv.cd "datacenter"
site:arptc.gouv.cd "{operator}"
site:arptc.gouv.cd "fourniture des services de gros" "{operator}"
site:arptc.gouv.cd "infrastructures de base" "{operator}"
site:arptc.gouv.cd "centre de transit international"
site:arptc.gouv.cd "station d'atterrage"
site:arptc.gouv.cd "point d'échange internet"
site:arptc.gouv.cd "observatoire internet" "{province}"
site:arptc.gouv.cd/app/uploads "{operator}"
```

Capture: licence/title category, legal name, address, province/city coverage, issue/expiry dates, network/infrastructure type, service scope, and whether the record proves a service licence only or an actual facility.

### 1.3 Electricity, grid, and energy approvals

Primary sources:
- ARE - Autorite de Regulation du secteur de l'Electricite: https://are.gouv.cd/
- ARE missions: https://are.gouv.cd/nos-missions/
- ARE norms: https://are.gouv.cd/normes/
- ARE FAQ on authorization/licence thresholds: https://are.gouv.cd/helpie_faq_page/
- SNEL utility: https://snel.cd/
- Ministry of Hydraulic Resources and Electricity: https://www.mrhe.gouv.cd/
- Leganet decree on electricity-sector concession/licence/authorization requirements: https://www.leganet.cd/Legislation/Droit%20economique/Energie/Decret.18.052.24.12.2018.html
- FAOLEX copy of Law 14/011 on electricity: https://faolex.fao.org/docs/pdf/cng140374.pdf

ARE is the regulatory path for electricity-sector licences, authorizations, tariffs, contracts, and norms. Use it to check whether a datacenter has its own generation, private electrical line, dedicated distribution arrangement, or large commercial connection. The ARE FAQ states that authorizations cover autoproduction installations outside the public domain from 100 kW to 999.99 kW and certain private electrical lines; larger independent production/import/export/commercialisation may require higher-level titles. Data centers with major diesel, solar, or private-line arrangements may appear under power evidence even when not labelled as data centers.

Power query templates:

```text
site:are.gouv.cd "data center"
site:are.gouv.cd "centre de données"
site:are.gouv.cd "{operator}" "MVA"
site:are.gouv.cd "{operator}" "autorisation"
site:are.gouv.cd "{operator}" "licence"
site:snel.cd "data center"
site:snel.cd "centre de données"
site:snel.cd "{operator}" "Kinshasa"
site:snel.cd "Limete" "33kV"
site:mrhe.gouv.cd "{province}" "poste électrique"
"Raxio" "Kinshasa" "33kV"
"OADC" "Kinshasa" "MVA"
"data center" "SNEL" "RDC"
"centre de données" "poste électrique" "Kinshasa"
```

Extract: power source (SNEL grid, hydro-sourced utility power, diesel/solar/gas backup), connection voltage, site load/MVA, IT load/MW, substation/feeder, generator/fuel-storage permits, energy title if applicable, energisation date, and whether the figure is utility/site load or usable IT load.

### 1.4 Digital-government, national cloud, and public procurement

Primary sources:
- Ministry of Digital Economy: https://numerique.gouv.cd/
- Ministry of PTNTIC: https://ptntic.gouv.cd/
- Presidency: https://presidence.cd/
- Agence pour le Developpement du Numerique (ADN): https://adn.cd/
- Public procurement regulator ARMP: https://armp-rdc.cd/
- Donor/procurement mirrors can surface official notices when DRC sites are hard to search; verify against ministry/ARMP where possible.
- Plan National du Numerique Horizon 2025 mirror: https://droitnumerique.cd/wp-content/uploads/2024/08/Plan_National_du_Numerique_HORIZON_2025-1.pdf

Use these sources for government cloud, national-data-center, sovereign-cloud, e-government and provincial digitisation leads. A government project can be **A** for an issued procurement/contract or official launch, **B** for an announced intention or ministerial statement without site details, and **C** for policy-only targets. Watch current procurement terms: `Cloud souverain`, `centre des donnees`, `data center national`, `plateformes numeriques securisees`, `sauvegarde`, `disaster recovery`, `certification Tier`.

Government/procurement query templates:

```text
site:numerique.gouv.cd "centre de données"
site:numerique.gouv.cd "data center"
site:numerique.gouv.cd "cloud souverain"
site:ptntic.gouv.cd "centre de données"
site:adn.cd "data center"
site:adn.cd "appel d'offres" "centre de données"
site:armp-rdc.cd "data center"
site:armp-rdc.cd "centre des données"
site:presidence.cd "centre de données" "RDC"
"RDC" "cloud souverain" "serveurs routeurs switchs gateway"
"Plan National du Numérique" "centres de données" "Goma"
"Plan National du Numérique" "chef-lieu de province" "centres de données"
```

### 1.5 Official cloud-region and edge signals

Cloud pages are **A for cloud-region/local-zone existence** but do not disclose physical facility addresses. As of this pass, no AWS, Azure, Google Cloud, or Oracle OCI public cloud region was found for DRC/Kinshasa on the official global-region pages. Use cloud-provider pages to avoid false positives, then use local carrier-neutral facilities as possible partner/edge/PoP leads only.

| Provider | Official source | DRC signal | Enumeration use |
|---|---|---|---|
| AWS | Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Local Zones docs: https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html | No DRC/Kinshasa Region or Local Zone found. Africa Local Zone documentation showed Nigeria/Lagos, not DRC. | Do not infer AWS facility. Search only for `AWS Direct Connect`, `CloudFront`, partner PoP, or tenant references in Raxio/OADC/Orange. |
| Microsoft Azure | Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Azure geographies: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No DRC public Azure region found. | Treat Microsoft as policy/customer/edge lead only unless official Azure page announces DRC. |
| Google Cloud | Locations: https://cloud.google.com/about/locations | No DRC cloud region found. | Use for CDN/edge/interconnect leads only; do not assign physical region. |
| Oracle OCI | Public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/ ; OCI regions docs: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No DRC OCI public region found. | Tenant/partner lead only. |

Cloud query templates:

```text
site:aws.amazon.com "Democratic Republic of Congo" "Local Zone"
site:docs.aws.amazon.com "Kinshasa" "Local Zone"
site:learn.microsoft.com "Democratic Republic of Congo" "Azure region"
site:cloud.google.com "Kinshasa" "region"
site:oracle.com "Democratic Republic of Congo" "cloud region"
"Kinshasa" "cloud region" "data center" AWS OR Azure OR Google OR Oracle
"OADC" "Kinshasa" "cloud provider"
"Raxio" "Kinshasa" "cloud provider"
```

### 1.6 Uptime Institute certification records

Primary sources:
- Uptime awards list: https://uptimeinstitute.com/uptime-institute-awards/list
- Raxio DRC1 Uptime record: https://uptimeinstitute.com/uptime-institute-awards/datacenter/drc1/1917
- OADC Texaf FIH1 Uptime record: https://uptimeinstitute.com/uptime-institute-awards/datacenter/oadc-texaf-fih1/2010
- OADC announcement of Tier III design certification: https://www.openaccessdc.net/news/open-access-data-centres-texaf-kinshasa-awarded-tier-iii-design-certification-by-the-uptime-institute

Use Uptime as **A for certification existence, named facility, and location**. It is not a complete market list and it may not expose all award details in easily indexed text, so pair it with official operator pages for capacity and address.

Uptime query templates:

```text
site:uptimeinstitute.com/uptime-institute-awards "Congo, Democratic Republic of the" "Kinshasa"
site:uptimeinstitute.com/uptime-institute-awards "DRC1"
site:uptimeinstitute.com/uptime-institute-awards "OADC Texaf"
site:uptimeinstitute.com "Raxio Data Centre SAS" "Ville-Province de Kinshasa"
site:uptimeinstitute.com "Open Access Data Centers Texaf Digital DRC"
```

---

## 2. Operator, IXP, and trade-press seed list

Operator pages are **A for self-claimed active service/location/capacity**. Trade press is **B** unless it quotes or links an official filing. Always join back to GUPEC/ARPTC/ARE/SNEL/Uptime before classifying construction status where possible.

| Operator / project | Official or strong source | DRC footprint signal | Follow-up joins |
|---|---|---|---|
| Raxio Kinshasa DRC1 | Raxio page: https://www.raxiogroup.com/data-centres/dr-congo/ ; Uptime: https://uptimeinstitute.com/uptime-institute-awards/datacenter/drc1/1917 ; DCD: https://www.datacenterdynamics.com/en/news/raxio-group-inaugurates-30m-data-center-in-democratic-republic-of-the-congo/ | Raxio places DRC1 in Limete industriel, 12eme Rue, Kinshasa, 1,056 m2 white space, 400 racks, 1.5 MW IT power, 33 kV utility feed, fuel backup. Uptime record places DRC1 in Ville-Province de Kinshasa. | Search GUPEC/Urbanisme permit, ARPTC titles for Raxio Data Centre SAS, SNEL/ARE 33 kV/substation, local inauguration releases. |
| OADC Texaf Kinshasa / FIH1 | OADC page: https://www.openaccessdc.net/kinshasa ; OADC certification news: https://www.openaccessdc.net/news/open-access-data-centres-texaf-kinshasa-awarded-tier-iii-design-certification-by-the-uptime-institute ; Uptime: https://uptimeinstitute.com/uptime-institute-awards/datacenter/oadc-texaf-fih1/2010 | OADC official page lists Kinshasa facility, 1,000 m2 technical space, N+1 cooling, 2 MW site load. Certification release places it at SILIKIN Village and says it was planned for Q3 2024 go-live, initial 400 m2 IT white space, future 550+ racks. | Search Texaf/SILIKIN/COTEX concession, GUPEC, ARPTC/WIOCC, PeeringDB, ARE/SNEL, trade press confirming live status. |
| Orange Business RDC Data Center | Official Orange Business RDC service page: https://business.orange.cd/fr/ict/hbergement-datacenter.html | Orange offers enterprise datacenter hosting, rack space, protected AC/DC power, optional link to Orange RDC datacenter, 24/7/365 support, SLA if linked. Exact facility address/capacity not public on the page. | Search ARPTC Orange titles, Uptime, Orange RDC press/LinkedIn, Kinshasa permits, Orange backbone/IXP records. |
| Global Broadband Solution / GBS Datacenter | Directory lead: https://www.datacentermap.com/dr-congo/kinshasa/gbsdc1/ ; KINIX member evidence from Internet Society Pulse: https://pulse.internetsociety.org/en/ixp-tracker/ixp/293/ | DataCenterMap lists GBSDC1 in Kinshasa; Pulse lists Global Broadband Solution among KINIX members. Operator facility page was not found in this pass. | Treat as C until official GBS page, ARPTC title, PeeringDB facility, or address evidence is found. |
| United S.A. / United Kinshasa | United hosting page: https://unitedrdc.com/hebergement/ ; PeeringDB/KINIX lead: https://www.peeringdb.com/ix/628 ; DE-CIX ACIX press: https://www.de-cix.net/en/about-de-cix/media/press-releases/africa-congo-internet-exchange-acix-becomes-first-distributed-ix-in-drc-with-support-from-de-cix | United offers hosting services; PeeringDB lists United as KINIX member and KINIX local facilities include OADC FIH1 and Raxio DRC1. DE-CIX says United and Internet pour tous support ACIX expansion into OADC. | Verify physical United facility through ARPTC, official facility/address page, lease/PeeringDB facility record, or local press. |
| KINIX / ISPA-DRC | Internet Society 2019 Lubumbashi IXP release: https://www.internetsociety.org/news/press-releases/2019/new-internet-exchange-point-in-democratic-republic-of-congo/ ; PeeringDB KINIX: https://www.peeringdb.com/ix/628 ; Pulse tracker: https://pulse.internetsociety.org/en/ixp-tracker/ixp/293/ | KINIX is a Kinshasa exchange; Internet Society also launched a Lubumbashi IXP. PeeringDB currently lists KINIX local facilities at OADC FIH1 and Raxio DRC1. | Use IX records as facility/tenant/interconnection leads, not standalone datacenters unless facility record exists. |
| ACIX / Internet pour tous / DE-CIX | DE-CIX press release above; Telecompaper/Computer Weekly follow-ups | ACIX expanded into OADC Texaf Kinshasa in 2026, making DRC's first distributed IX according to DE-CIX/trade press. | Seed OADC, United, Internet pour tous, ARPTC declarations for community IXPs and infrastructure-sharing titles. |
| Government cloud / national data centers | Ministry/ADN/PTNTIC/procurement searches; Plan National du Numerique mirror above; dgMarket lead for 2026 sovereign-cloud equipment: https://afd.dgmarket.com/tenders/adminShowBuyer.do?buyerId=7823690 | Leads include sovereign-cloud equipment procurement and policy targets for certified, interconnected data centres. These may be equipment refreshes, government data rooms, or future facilities. | Verify through official ministry/ARMP tender, award notice, contract, site, and delivery status before recording a facility. |
| Goma neutral Tier III/Tier IV plan | Plan National du Numerique / implementation-evaluation PDFs surfaced through ICT Policy Africa and local reports | Policy lead for urban centres such as Goma; no confirmed construction/operational facility found in this pass. | Search North Kivu/Goma government, ADN, ARPTC, donor procurement, and energy/security press; mark C/B policy lead until site evidence appears. |

Trade-press query templates:

```text
site:datacenterdynamics.com "Democratic Republic of the Congo" "data center"
site:connectingafrica.com "DRC" "data center" Kinshasa
site:developingtelecoms.com "DRC" "data centre"
site:cio-mag.com "RDC" "data center"
site:agenceecofin.com "RDC" "data center"
site:wearetech.africa "RDC" "data center"
site:telecompaper.com "Kinshasa" "data centre"
site:computerweekly.com "Africa Congo Internet Exchange"
"RDC" "Raxio" "Limete" "data center"
"RDC" "OADC Texaf" "SILIKIN Village"
"Kinshasa" "Tier III" "Uptime" "data center"
```

---

## 3. Province enumeration strategy

### 3.1 Standard workflow for every province

1. Search official sources first: GUPEC, urbanisme/habitat, provincial government pages, ARPTC, ARE/SNEL/MRHE, MEDD/ACE/EIES, Ministry of Digital Economy, PTNTIC, ADN, ARMP/procurement.
2. Search local French terms plus English variants: `centre de donnees`, `data center`, `datacenter`, `salle serveur`, `cloud`, `cloud souverain`, `hebergement`, `colocation`, `fibre optique`, `IXP`, `point d'echange`, `Tier III`, `permis de construire`, `poste electrique`, `33kV`, `MVA`.
3. Add province capital/city and aliases. Example: `Haut-Katanga Lubumbashi`, `Kongo Central Matadi`, `Nord-Kivu Goma`, `Tshopo Kisangani`.
4. Search named operators: `Raxio`, `OADC`, `WIOCC`, `TEXAF`, `Orange`, `Vodacom`, `Airtel`, `Africell`, `SCPT`, `United`, `GBS`, `Microcom`, `Liquid`, `Paratus`, `KINIX`, `ACIX`, `ISPA-DRC`, `Internet pour tous`.
5. Treat telco switches, bank server rooms, and ministry data rooms as separate from commercial colocation. Record them only when they are significant physical facilities with named location/status.

Generic province query block:

```text
"{province}" "{capital}" "centre de données" RDC
"{province}" "{capital}" "data center" RDC
"{province}" "{capital}" datacenter RDC
"{capital}" "salle serveur" "RDC"
"{capital}" "cloud souverain" "RDC"
"{capital}" "colocation" "RDC"
"{capital}" "point d'échange internet" OR IXP
"{capital}" "{operator}" "data center"
"{capital}" "permis de construire" "centre de données"
"{capital}" "poste électrique" "data center"
site:arptc.gouv.cd "{capital}" "{operator}"
site:are.gouv.cd "{capital}" "{operator}"
site:medd.gouv.cd "{capital}" "EIES" "centre de données"
site:gupec-rdc.com "{capital}" "permis de construire"
```

### 3.2 High-yield provinces and city anchors

- **Kinshasa**: highest yield. Query communes and industrial/digital hubs: `Limete`, `12eme Rue Industriel`, `Gombe`, `Ngaliema`, `SILIKIN Village`, `Concession COTEX`, `Avenue Colonel Mondjiba`, `Gare Centrale`, `N'Djili`, `Kingabwa`, `Masina`, `Kintambo`, `Gombe Boulevard du 30 Juin`. Operators: Raxio, OADC Texaf, Orange RDC, GBS, United, KINIX/ACIX, Vodacom/Airtel/Africell core sites. Primary joins: GUPEC, ARPTC, ARE/SNEL, Uptime, operator pages.
- **Upper Katanga / Haut-Katanga (Lubumbashi)**: second-highest because of mining economy, fibre routes, and Internet Society's Lubumbashi IXP launch. Query `Lubumbashi`, `Haut-Katanga`, `Kasumbalesa`, `Kipushi`, `Ruashi`, `Kamalondo`, `Luano`, `mining data center`, `salle serveur minier`, `IXP Lubumbashi`, `point d'echange Internet Lubumbashi`, `SNEL poste`. Expect IXP/edge/telco evidence more than large colo.
- **Central Kongo / Kongo Central (Matadi, Moanda, Boma, Inga, Kasangulu)**: high infrastructure relevance because of Atlantic gateway, fibre/subsea/terrestrial routes, Inga power, and Kinshasa-Matadi corridor. Query `Matadi data center`, `Moanda cable`, `station d'atterrage`, `Inga data center`, `Kasangulu fibre`, `Kongo Central cloud`, `poste electrique Inga`.
- **North Kivu (Goma, Beni, Butembo)**: policy lead from PNN/Goma and regional edge demand. Query `Goma centre de donnees`, `Goma Tier III`, `Goma IXP`, `Goma fibre`, `Beni data center`, `Nord-Kivu cloud`, `ADN Goma`. Security conditions make announced projects prone to delay; require fresh confirmation.
- **South Kivu (Bukavu, Uvira)**: cross-border connectivity and government/NGO infrastructure leads. Query `Bukavu centre de donnees`, `Bukavu salle serveur`, `Uvira fibre`, `Ruzizi electricity data center`, `Sud-Kivu cloud`.
- **Tshopo (Kisangani)**: large city and national backbone node. Query `Kisangani centre de donnees`, `Kisangani IXP`, `Tshopo fibre optique`, `Kisangani ARPTC`, `Kisangani cloud`.
- **Lualaba (Kolwezi)** and **Upper Katanga/Lualaba mining belt**: mining-company IT rooms, private power, and industrial-load evidence. Query `Kolwezi data center`, `Kolwezi salle serveur`, `Lualaba cloud`, `mine data center RDC`, `poste electrique Kolwezi`, `33kV Kolwezi`.
- **Central Kasai / Eastern Kasai / Kasai (Kananga, Mbuji-Mayi, Tshikapa)**: government digitisation and telco core-site leads, lower probability of commercial colo. Query capital names plus `centre de donnees`, `salle serveur`, `fibre optique`, `cloud provincial`.
- **Ituri (Bunia)**, **Tanganyika (Kalemie)**, **Maniema (Kindu)**: search for government, telco, humanitarian/UN, and energy-backed edge infrastructure; expect mostly negative.
- **Equator / Equateur (Mbandaka)**, **South Ubangi (Gemena)**, **North Ubangi (Gbadolite)**, **Mongala (Lisala)**, **Tshuapa (Boende)**, **Lower Uele (Buta)**, **Upper Uele (Isiro)**: low-yield remote/northern provinces. Search provincial capitals with `salle serveur`, `fibre`, `telecom`, `IXP`, `e-gouvernement`; mark no-project only after checking French variants.
- **Kwilu (Bandundu/Kikwit)**, **Kwango (Kenge)**, **Mai-Ndombe (Inongo)**, **Lomami (Kabinda)**, **Upper Lomami (Kamina)**, **Sankuru (Lusambo)**: mostly negative unless government data rooms, telco switches, or power/fibre projects surface. Include old province/city names in queries, e.g. `Bandundu`, `Kikwit`, `Kamina`.

### 3.3 Province alias table for search

| Division label | French/common aliases and anchor cities |
|---|---|
| Central Kongo | `Kongo Central`, `Bas-Congo`, `Matadi`, `Boma`, `Moanda`, `Inga`, `Kasangulu`, `Mbanza-Ngungu` |
| Lower Uele | `Bas-Uele`, `Buta`, `Bondo`, `Aketi` |
| Equator | `Equateur`, `Mbandaka` |
| Upper Katanga | `Haut-Katanga`, `Lubumbashi`, `Likasi`, `Kasumbalesa`, `Kipushi` |
| Upper Lomami | `Haut-Lomami`, `Kamina`, `Bukama` |
| Upper Uele | `Haut-Uele`, `Isiro`, `Watsa`, `Dungu` |
| Ituri | `Bunia`, `Mahagi`, `Aru`, `Irumu` |
| Central Kasai | `Kasai Central`, `Kananga` |
| Eastern Kasai | `Kasai Oriental`, `Mbuji-Mayi`, `Mbuji Mayi` |
| Kwango | `Kenge`, `Popokabaka`, `Kasongo-Lunda` |
| Kwilu | `Bandundu`, `Kikwit`, `Bulungu` |
| Kinshasa | `Ville-Province de Kinshasa`, `Limete`, `Gombe`, `Ngaliema`, `SILIKIN`, `COTEX` |
| Kasai | `Tshikapa`, `Luebo`, `Ilebo` |
| Lomami | `Kabinda`, `Mwene-Ditu` |
| Lualaba | `Kolwezi`, `Fungurume`, `Dilolo` |
| Maniema | `Kindu`, `Kasongo` |
| Mai-Ndombe | `Inongo`, `Nioki` |
| Mongala | `Lisala`, `Bumba` |
| North Kivu | `Nord-Kivu`, `Goma`, `Beni`, `Butembo` |
| North Ubangi | `Nord-Ubangi`, `Gbadolite`, `Mobayi-Mbongo` |
| Sankuru | `Lusambo`, `Lodja` |
| South Kivu | `Sud-Kivu`, `Bukavu`, `Uvira`, `Ruzizi` |
| South Ubangi | `Sud-Ubangi`, `Gemena`, `Zongo` |
| Tanganyika | `Kalemie`, `Manono`, `Moba` |
| Tshopo | `Kisangani`, `Yangambi` |
| Tshuapa | `Boende`, `Bokungu` |

---

## 4. Evidence handling rules

- A policy statement such as `construire des centres de donnees dans chaque chef-lieu de province` is a **lead only**. Do not create 26 planned facilities unless there are named tenders/sites/projects.
- `Hébergement`, `hosting`, and `cloud` pages may be software/service offers hosted outside DRC. Require text like `data center Orange RDC`, a DRC address, ARPTC/PeeringDB facility, or operator confirmation before assigning a physical DRC facility.
- `IXP` is not automatically a datacenter. Use it to identify host facilities, meet-me rooms, and carrier-neutral sites. PeeringDB facility IDs and Internet Society/DE-CIX releases are strong leads but still distinguish exchange vs building.
- For capacity, store the exact source meaning: `IT power`, `site load`, `MVA`, `white space`, `technical space`, `racks`. Do not convert MVA to MW without assumptions.
- For DRC/CG confusion, reject sources that mention `Brazzaville`, `Pointe-Noire`, `ARPCE`, `Congo Republic`, `Republic of Congo`, `CEMAC datacenter national`, unless the project explicitly crosses into DRC. DRC regulator is **ARPTC**; Republic of Congo regulator is **ARPCE**.
- When no primary permit is found, a facility can still be `operational` if corroborated by official operator page plus Uptime/PeeringDB/trade launch evidence. Grade the operator/Uptime facts A, and note missing GUPEC/ARE evidence.
