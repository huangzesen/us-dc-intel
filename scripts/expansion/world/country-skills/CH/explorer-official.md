# CH Explorer Official - Switzerland Datacenter Enumeration via Cantonal Permits, Energy/Grid, OFCOM, Cloud Regions

Date: 2026-08-12. Scope: Switzerland (CH), 26 cantons. Focus angle: official/regulatory/cloud pipeline for enumerating datacenter facilities and projects, with priority on Swiss planning permits, energy/grid sources, official cloud-region pages, OFCOM/telecom context, major colo players, trade press, and canton-level query patterns. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/association source, **C** = weak aggregate/unverified.

---

## 0. Structural facts that shape Switzerland enumeration

- Switzerland has **no single national public datacenter facility register** and no single national building-permit portal. Building law and publication practice are primarily **cantonal and communal**. Use the canton as the routing unit, then drill into the municipality/commune/comune that publishes `Baugesuch`, `Baubewilligung`, `permis de construire`, or `domanda di costruzione` notices.
- Public records are multilingual. German sources dominate Zurich, Aargau, Bern, Basel, Zug, Lucerne, St. Gallen, Schaffhausen, Thurgau, Solothurn, Schwyz, Graubuenden, etc.; French sources dominate Geneva, Vaud, Neuchatel, Jura, Fribourg, Valais; Italian sources dominate Ticino. Search all local-language forms before English.
- For live construction discovery, the best official route is usually **cantonal/municipal permit publication + official gazette/amtsblatt + map/open-data layers**. Zurich is unusually strong because the canton publishes current building applications as open data; Geneva has a public construction-authorization status platform and open data; Vaud publishes permit inquiry notices through FAO/CAMAC.
- The largest Swiss datacenter projects can be more visible in **energy/grid documents** than in planning summaries. Extract and store grid-connection power, emergency-generator capacity, substation/Unterwerk needs, cooling/water demand, and waste-heat reuse separately from IT load. The Beringen/Schaffhausen case shows that a datacenter can require a new substation and become politically material even after a legally binding permit.
- Federal sources are mostly policy/aggregate, not facility-level. The Swiss Federal Office of Energy (SFOE/BFE) has high-value studies on datacenter electricity use; Swissgrid gives the transmission-grid connection framework; ElCom is the electricity regulator; OFCOM/BAKOM is the telecom/digital regulator and useful for telecom-provider context, not a datacenter permit register.
- Official hyperscale cloud regions provide strong city/country seeds but normally hide facility addresses. Switzerland has official Zurich/Geneva cloud-region signals from AWS, Microsoft Azure, Google Cloud, and Oracle Cloud. Treat these as Grade A cloud-region existence, then pivot to permits, grid, and operator pages before counting physical sites.
- Commercial density is concentrated in **Greater Zurich** (Zurich, Opfikon/Glattbrugg, Ruemlang, Schlieren, Dielsdorf, Lupfig/Aargau, Rafz/Beringen/Schaffhausen), **Geneva/Vaud arc** (Geneva, Gland, Lausanne/Renens), **Bern/Zollikofen/Ittigen**, **Ticino/Lugano/Manno/Melano**, plus smaller Basel, Zug, Lucerne, St. Gallen and public-sector/HPC sites.

Key lifecycle vocabulary:

`Standortsuche` / `demande prealable` / `studio preliminare` < `Baugesuch` / `demande de permis` / `domanda di costruzione` < `Auflage` / `mise a l'enquete` / `pubblicazione` < `Baubewilligung` / `permis delivre` / `licenza edilizia` < `rechtskraeftig` / `entree en force` / `cresciuta in giudicato` < `Baufreigabe` / `debut chantier` / `inizio lavori` < `Inbetriebnahme` / `mise en service` / `messa in esercizio`

Count `Baubewilligung/permis/licenza`, `rechtskraeftig/entree en force`, `Baufreigabe`, `construction start`, or stronger as permit/construction evidence. Treat public inquiry notices and applications as leads until cross-checked.

---

## 1. Multilingual query patterns

### 1.1 German terms

```text
Rechenzentrum
Datencenter OR Data Center OR Datacenter
Cloud Region OR Cloudregion
Colocation OR Co-Location
Hyperscale OR Hochleistungsrechenzentrum
KI-Rechenzentrum OR AI-Rechenzentrum
Baugesuch Rechenzentrum
Baubewilligung Rechenzentrum
Baupublikation Rechenzentrum
Amtsblatt Rechenzentrum
Auflagefrist Rechenzentrum
Nutzungsplanung Rechenzentrum
Gestaltungsplan Rechenzentrum
Sondernutzungsplan Rechenzentrum
Industriezone Rechenzentrum
Netzanschluss Rechenzentrum
Unterwerk Rechenzentrum
Transformatorenstation Rechenzentrum
Notstromgruppe Rechenzentrum
Notstromanlagen Rechenzentrum
Abwaerme Rechenzentrum
Fernwaerme Rechenzentrum
Kuehlung Rechenzentrum
UVP Rechenzentrum OR Umweltvertraeglichkeitspruefung Rechenzentrum
```

### 1.2 French terms

```text
centre de donnees
centre de données
data center OR datacenter
centre informatique
hebergement informatique
colocation
hyperscale
centre de calcul IA
demande de permis de construire centre de donnees
permis de construire data center
mise a l'enquete centre de donnees
autorisation de construire data center
feuille des avis officiels data center
plan d'affectation centre de donnees
raccordement electrique data center
sous-station data center
groupes electrogenes centre de donnees
rejets thermiques OR chaleur fatale OR recuperation de chaleur
refroidissement centre de donnees
```

### 1.3 Italian terms

```text
centro dati
centro di calcolo
data center OR datacenter
colocation
domanda di costruzione centro dati
licenza edilizia centro dati
pubblicazione domanda di costruzione data center
albo comunale centro dati
piano regolatore centro dati
allacciamento elettrico centro dati
sottostazione elettrica data center
gruppi elettrogeni centro dati
calore residuo OR recupero calore
raffreddamento centro dati
```

### 1.4 Official permit queries

Substitute `{canton}`, `{municipality}`, `{operator}`, `{address}`, `{parcel}`, `{gazette-domain}`.

```text
"{municipality}" "Rechenzentrum" "Baugesuch"
"{municipality}" "Rechenzentrum" "Baubewilligung"
"{municipality}" "Datencenter" "Baugesuch"
"{canton}" "Rechenzentrum" "Amtsblatt"
site:{municipality-domain} Rechenzentrum Baugesuch
site:{canton-domain} Rechenzentrum Baubewilligung
site:{gazette-domain} Rechenzentrum Baugesuch
filetype:pdf "Rechenzentrum" "Baugesuch" "{municipality}"
filetype:pdf "Rechenzentrum" "Auflagefrist"

"{commune}" "centre de donnees" "permis de construire"
"{commune}" "data center" "mise a l'enquete"
site:{commune-domain} "centre de donnees" "autorisation de construire"
site:{canton-domain} "data center" "permis de construire"
filetype:pdf "centre de donnees" "mise a l'enquete"

"{comune}" "centro dati" "domanda di costruzione"
"{comune}" "data center" "licenza edilizia"
site:{comune-domain} "centro dati" "domanda di costruzione"
site:{canton-domain} "centro dati" "licenza edilizia"
```

### 1.5 Energy/grid/environment queries

```text
site:bfe.admin.ch Rechenzentren Schweiz Stromverbrauch
site:pubdb.bfe.admin.ch Rechenzentren Schweiz Stromverbrauch
site:uvek.admin.ch Rechenzentren Schweiz Stromverbrauch
site:swissgrid.ch grid connection Switzerland datacenter
site:swissgrid.ch Rechenzentrum Netzanschluss
site:elcom.admin.ch Rechenzentrum OR Datencenter
"{operator}" "{municipality}" "MW" "Rechenzentrum"
"{operator}" "{municipality}" "Unterwerk" OR "substation" OR "sous-station"
"{municipality}" "Rechenzentrum" "Notstrom"
"{municipality}" "Rechenzentrum" "Abwaerme" OR "Fernwaerme"
"{commune}" "centre de donnees" "chaleur fatale" OR "raccordement electrique"
"{comune}" "centro dati" "allacciamento elettrico" OR "recupero calore"
```

### 1.6 English operator/cloud/trade pivots

```text
"Switzerland" "data center" "building permit"
"Zurich" "data center" "building permit"
"Beringen" "data center" "building permit"
"Switzerland" "data center" "grid connection"
"Switzerland" "data center" "substation"
"Switzerland" "data center" "waste heat"
"AWS" "Europe (Zurich)" "eu-central-2"
"Azure" "Switzerland North" "Switzerland West"
"Google Cloud" "europe-west6" "Zurich"
"Oracle Cloud" "eu-zurich-1"
"Green Datacenter" "Dielsdorf" OR "Lupfig" OR "Zurich West"
"STACK Infrastructure" "ZUR02" OR "Beringen" OR "Rafz" OR "Geneva"
"Digital Realty" "Zurich" "ZUR1" OR "ZUR2" OR "ZUR3"
"Equinix" "Switzerland" "ZH" OR "GV"
"NTT" "Zurich 1" "Ruemlang"
```

---

## 2. Official/regulatory source backbone

### 2.1 Federal planning baseline

- Swiss federal citizen portal building-permit explainer: https://www.ch.ch/en/housing/homeownership/planning-application-and-building-permit/. Grade A process source. It confirms buildings/installations generally need authority permits and that cantonal legislation and communes determine details.
- opendata.swiss: https://opendata.swiss/en. Grade A for datasets from the Confederation, cantons, communes, and public-mandate organizations. Use as the national discovery hub for cantonal building applications, Geneva construction-authorizations, Zurich building applications, building-zone layers, and Federal Register of Buildings and Dwellings datasets.
- Federal Register of Buildings and Dwellings (RegBL/RBD): https://www.bfs.admin.ch/bfs/en/home/registers/federal-register-buildings-dwellings.html. Grade A for building/address identifiers and building status context. It is not a datacenter list, but since 2018 includes non-residential buildings; use for EGID/address validation once a candidate site is known.
- Harmonized Swiss building zones dataset: https://opendata.swiss/en/dataset/bauzonen-schweiz-harmonisiert/resource/92bd7649-90dd-4e12-b89a-5e72aa9f8987. Grade A for zoning context. Use to verify industrial/commercial/building-zone compatibility, not as proof of a facility.

Operational rule: Swiss building-permit publication is decentralized. For each candidate, capture the authority, municipality, canton, publication date, application/permit number, parcel/GB number, address, applicant/operator, project description, public-inspection period, appeal status, and whether the decision is legally binding.

### 2.2 Zurich / Greater Zurich permit backbone

Zurich is the highest-priority official sweep because it has the densest market and good open-data/publication routes.

- Kanton Zurich eBaugesucheZH: https://www.zh.ch/de/planen-bauen/baubewilligung/elektronische-baugesuche.html. Grade A process source. It covers the digital building-permit workflow from application through review, permit, and acceptance where municipalities use the platform.
- City of Zurich online building applications: https://www.stadt-zuerich.ch/de/planen-und-bauen/baubewilligungen/bewilligungsprozess/baugesuch-einreichen.html. Grade A process source. It says Zurich city building applications are submitted electronically through eBaugesucheZH.
- Zurich open-data building applications: https://opendata.swiss/de/dataset/baugesuche-im-kanton-zurich/resource/9463a1cb-a62b-4648-8ee4-a146d445ff52. Grade A lead source. It covers current building applications in the canton over the last 20 days, corresponding to the statutory objection period; use WMS/WFS/API resources where available.
- Kanton Zurich environmental impact assessment page: https://www.zh.ch/de/planen-bauen/baubewilligung/umweltvertraeglichkeitspruefung.html. Grade A process source for projects with significant environmental impact.

Zurich search route:

```text
site:zh.ch Rechenzentrum Baugesuch
site:zh.ch Datencenter Baubewilligung
site:amtsblatt.zh.ch Rechenzentrum
site:stadt-zuerich.ch Rechenzentrum Baugesuch
"Opfikon" OR "Glattbrugg" "Rechenzentrum" "Baugesuch"
"Ruemlang" OR "Rümlang" "Rechenzentrum" "Baubewilligung"
"Dielsdorf" "Green Datacenter" "Baugesuch"
"Lupfig" "Green Datacenter" "Baubewilligung"
"Rafz" "STACK" "Rechenzentrum"
```

Priority municipalities and operators: Zurich city, Opfikon/Glattbrugg, Ruemlang, Schlieren, Dielsdorf, Rafz, Wallisellen, Winterthur, Dietikon, Horgen; Green, Digital Realty, NTT, STACK, Equinix, Swisscom, AWS/Microsoft/Google/Oracle SPVs.

### 2.3 Vaud / Geneva / Romandy permit backbone

- Canton Vaud public inquiry notices for building permits: https://www.vd.ch/prestation/consulter-les-avis-de-mise-a-lenquete. Grade A. It allows searches for `autorisation prealable d'implantation`, `permis de construire`, complementary inquiries, and rectifying notices published in the official gazette (FAO).
- Vaud ACTIS-CAMAC permit-submission source: https://www.vd.ch/territoire-et-construction/permis-de-construire/realiser-son-dossier-en-vue-dune-demande-de-permis-de-construire. Grade A process source. It identifies ACTIS-CAMAC as the platform for the general questionnaire.
- FAO Vaud permit pages, example Lausanne district: https://www.faovd.ch/permis-de-construire/district/lausanne/. Grade A for official/public permit notices.
- Vaud geodata for building permit public inquiries: https://viageo.ch/md/cb71405f-13f6-421b-b2ee-3ca76efbd56d. Grade A metadata. Use the GEOVD_CAMAC layer for mapped public inquiries and CAMAC identifiers.
- Canton Geneva construction authorization consultation: https://www.ge.ch/consulter-autorisation-construire. Grade A. Geneva's SAD platform gives synthesis data and status for construction-authorization and land-use-plan files.
- Geneva construction-authorization open data via opendata.swiss: https://opendata.swiss/en/dataset/autorisation-de-construire-dossier1/resource/ac086cd0-bf00-4dee-9193-936e7c3f3f1a. Grade A. Use for dossier-level status and identifiers.
- SITG Geneva mapping/catalogue: https://sitg.ge.ch/ and map URL parameters including `locautorisationconstruire`: https://sitg.ge.ch/ressources/cartes-par-url-interactives. Grade A for geospatial localization of permit files.

Romandy queries:

```text
site:vd.ch "data center" "permis de construire"
site:faovd.ch "data center" "permis de construire"
site:faovd.ch "centre de donnees" "mise a l'enquete"
site:geo.vd.ch CAMAC "data center"
site:ge.ch "data center" "autorisation de construire"
site:ge.ch "centre de donnees" "permis de construire"
site:sitg.ge.ch "autorisation de construire" "data center"
"Gland" "STACK" "data center" "permis"
"Geneve" "Equinix" "data center"
"Renens" "data center" "Etat de Vaud"
```

Priority areas: Geneva, Vernier, Meyrin, Plan-les-Ouates, Gland, Lausanne, Renens, Ecublens/EPFL, Yverdon-les-Bains, Nyon. STACK's Geneva/Gland campus and Equinix Geneva are key operator pivots.

### 2.4 Bern / Ticino / other official permit routes

- Canton Bern eBau: https://www.bauen.dij.be.ch/de/start/baubewilligungsverfahren/eBau.html. Grade A process source. Since 2022, Bern building applications are handled electronically; private researchers usually still need the responsible municipality or published notices for public details.
- Bern government district offices building page: https://www.rsta.dij.be.ch/de/start/themen/bauen.html. Grade A process source. It states building applications are submitted electronically through eBau and points applicants to municipal access.
- Canton Ticino building-application office: https://www4.ti.ch/dt/sg/udc/temi/domande-di-costruzione/tema/tema. Grade A process source. The Ufficio delle domande di costruzione provides cantonal review/pre-opinion in building-license procedures; municipalities publish applications.
- Ticino building-application forms: https://www4.ti.ch/dt/sg/udc/temi/domande-di-costruzione/sportello/formulari-e-tabelle/domande-di-costruzione. Grade A process source.
- Lugano municipal building-application notices: https://www.lugano.ch/la-mia-citta/amministrazione/albo-comunale/domande-costruzione/. Grade A for Lugano notices; replicate this municipal-albo approach across Ticino communes.
- Basel-Stadt Baupublikationen: https://www.bs.ch/bvd/planauflagen-und-anordnungen/baupublikationen. Grade A. Current building publications for Basel-Stadt, Riehen, and Bettingen.
- Basel-Stadt e-Kantonsblatt: https://www.bs.ch/regierungsrat/staatskanzlei/e-kantonsblatt-basel-stadt. Grade A official gazette.
- Basel-Landschaft Bauinspektorat publications/amtsblatt: https://www.baselland.ch/politik-und-behorden/direktionen/bau-und-umweltschutzdirektion/bauinspektorat/publikationen-amtsblatt. Grade A for official publication route.
- Schwyz Amtsblatt: https://www.sz.ch/kanton/amtsblatt.html/8756-8757-10020. Grade A official gazette; use `Rechenzentrum`, `Baugesuch`, `Datencenter`.

Queries:

```text
site:be.ch Rechenzentrum Baugesuch
site:be.ch Rechenzentrum eBau
site:bern.ch Rechenzentrum Baubewilligung
"Zollikofen" "Rechenzentrum" "Baubewilligung"

site:ti.ch "centro dati" "domanda di costruzione"
site:lugano.ch "data center" "domande costruzione"
"Manno" "BancaDati.ch" "centro dati"
"Melano" "Moresi" "data centre"
"Lugano" "CSCS" "permesso" OR "licenza edilizia"

site:bs.ch Rechenzentrum Baupublikation
site:baselland.ch Rechenzentrum Baugesuch
site:zg.ch Rechenzentrum Baugesuch
site:sz.ch Rechenzentrum Amtsblatt
```

### 2.5 Schaffhausen/Beringen as the official large-load template

Use Schaffhausen's Beringen project as the template for how Swiss hyperscale files surface across official and semi-official records:

- Kanton Schaffhausen government decision PDF, 2021-12-07: https://sh.ch/CMS/get/file/7840012c-3dc8-454d-bea1-cd5f086dabf6. Grade A. It states the datacenter building permit was granted by the cantonal building inspectorate on 2021-07-20, was not appealed, and became legally binding; it also records the large power need and required new substation.
- Kanton Schaffhausen PDF on Beringen data center permit process: https://sh.ch/CMS/get/file/fe471dad-76aa-47eb-a409-4018a14c1a96. Grade A process/project source. It explains the roles of Beringen municipality, cantonal bodies, building-police authority, and EKS grid connection.
- Schaffhausen Amtsblatt PDF notice, 2021-04-23: https://sh.ch/CMS/get/file/8f1bc025-920a-4a58-9d3a-b68df5be26a5. Grade A. The notice describes demolition of existing buildings, construction of a datacenter with photovoltaic installation, two emergency-power buildings on both north and south sides, parking spaces, parcel GB Nr. 862, Industriestrasse 6, 8222 Beringen.
- EKS media release PDF, "Beringen - Digitaler Knotenpunkt in Schaffhausen": https://www.eks.ch/medienmitteilungen?_hash=lGIoCiLqiBIrIbq8KyL23z5Yl68jnwQG7khqn8nxjp0%3D&ctx=a%3A1%3A%7Bs%3A2%3A%22id%22%3Bi%3A11102%3B%7D&d=attachment&f=2021_04_15+Beringen+-+Digitaler+Knotenpunkt+in+Schaffhausen.pdf&p=content%2Fueber_uns%2FMedienmitteilungen%2FArchiv_alte_Medienmitteilungen%2F2021%2F2021_04_15+Beringen+-+Digitaler+Knotenpunkt+in+Schaffhausen.pdf. Grade B+/A- depending on use: official grid/operator-adjacent for utility context, not a permit.
- Later political/trade/context sources can identify operator and controversy. For example, ZEIT and Swissinfo report STACK Infrastructure and protest context; SRF reports power-grid stress and Beringen as a high-consumption example. Grade B.

Extraction lesson: for each large-load project, search the municipality + canton + grid utility + cantonal parliament/council record. The permit publication may be short, while a government response or utility paper can reveal legal status, MW/load, substation requirement, and operator.

---

## 3. Energy, grid, environmental and telecom regulators

### 3.1 SFOE/BFE, UVEK, and energy studies

- SFOE/BFE commissioned study PDF, "Rechenzentren in der Schweiz - Stromverbrauch und Effizienzpotenzial": https://pubdb.bfe.admin.ch/de/publication/download/12607. Grade A-/B+ for aggregate market/energy estimates. It estimates Swiss datacenter electricity consumption at just under 2.1 TWh in 2024 and separates commercial colocation/cloud/hyperscale sites from internal enterprise datacenters. It is not a facility register.
- UVEK news release on the same study: https://www.uvek.admin.ch/de/newnsb/GV-_d7OgIlqjfQDGZqbkN and French version https://www.uvek.admin.ch/fr/newnsb/GV-_d7OgIlqjfQDGZqbkN. Grade A policy/aggregate source. Useful for current official framing of datacenter consumption, AI training facilities, and efficiency potential.
- BFE waste-heat study, "Abwaermenutzung von Rechenzentren": https://pubdb.bfe.admin.ch/de/publication/download/11426. Grade A-/B+ for heat-reuse methodology and Swiss examples.
- BFE Watt d'Or Green Datacenter Lupfig page: https://www.bfe.admin.ch/bfe/en/home/swiss-federal-office-of-energy/watt-d-or/winners-of-the-watt-dor-awards/winners-of-the-2013-watt-d-or-awards.html. Grade A for historical official recognition of Green Datacenter in Lupfig.

Use these to calibrate national totals, expected power ranges, waste-heat terms, and operator/site leads. Do not use aggregate estimates as facility counts without operator/permit corroboration.

### 3.2 Swissgrid, ElCom, and local utilities

- Swissgrid grid connection page: https://www.swissgrid.ch/en/home/customers/topics/grid-connection.html. Grade A process source. Swissgrid owns and operates the highest voltage level (NE1/transmission grid); large datacenters may still connect through distribution utilities or require substation upgrades.
- ElCom: https://www.elcom.admin.ch/. Grade A regulator for electricity-market/network oversight. Search ElCom decisions/publications for grid access, tariffs, large consumers, and network disputes; facility names are unlikely but possible in dispute records.
- Federal winter-reserve/emergency-power context: UVEK page https://www.uvek.admin.ch/de/nsb?id=91321 and UVEK scarcity-measures factsheet https://www.uvek.admin.ch/dam/de/sd-web/y2uUzwPMuZlW/faktenblatt-massnahmen-strommangellage.pdf. Grade A policy context. Datacenters and emergency generators appear in security-of-supply discussions; do not treat reserve participation as proof of a new facility.
- Local utilities are often decisive: EKS in Schaffhausen/Beringen, ewz in Zurich, EKZ in Zurich canton, AEW in Aargau, BKW in Bern, SIG in Geneva, Romande Energie in Vaud, IWB in Basel, CKW/WWZ in central Switzerland, Azienda Elettrica Ticinese/local municipal utilities in Ticino.

Utility query templates:

```text
site:ewz.ch Rechenzentrum Netzanschluss
site:ekz.ch Rechenzentrum Unterwerk
site:aew.ch Rechenzentrum Lupfig
site:bkw.ch Rechenzentrum Bern Netzanschluss
site:sig-ge.ch "centre de donnees" OR "data center"
site:romande-energie.ch "centre de donnees"
site:iwb.ch Rechenzentrum Abwaerme
site:wwz.ch Rechenzentrum Datacenter Zug
site:eks.ch Beringen Rechenzentrum Unterwerk
```

Fields to keep separate:

- `IT load` / `IT-Leistung` / `puissance informatique`;
- total electrical connection / `Anschlussleistung` / `raccordement`;
- grid level and substation/Unterwerk;
- emergency generation MVA/MW and fuel storage;
- annual electricity consumption;
- water/cooling demand;
- waste-heat delivery capacity and district-heating counterparty.

### 3.3 OFCOM/BAKOM and telecom context

- OFCOM/BAKOM official site: https://www.bakom.admin.ch/en. Grade A for telecom/digital policy. OFCOM is the federal competence center for media and telecommunications and supports digital transformation; it is **not** a datacenter siting/permit register.
- OFCOM open data organization page: https://opendata.swiss/en/organization/bundesamt-fur-kommunikation-bakom?res_format=SERVICE. Grade A for telecom datasets.
- OFCOM broadband infrastructure page: https://www.bakom.admin.ch/en/broadband-infrastructure. Grade A telecom infrastructure context.

Use OFCOM to identify telecom operators, broadband/fiber infrastructure, and internet-service context. For physical datacenter enumeration, pivot from telecom operators (`Swisscom`, `Sunrise`, `Salt`, `init7`, `Quickline`, `WWZ`, `CKW`, local utilities) to municipal permits, operator facility pages, and energy records.

---

## 4. Official cloud and operator seed list

### 4.1 Hyperscale cloud regions (Grade A cloud-region existence)

| Provider | Official source | Switzerland signal | Enumeration use |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and launch post https://aws.amazon.com/blogs/aws/a-new-aws-region-opens-in-switzerland/ | Europe (Zurich), `eu-central-2`, 3 AZs, opened 2022-11-08 | Seed Zurich-area hyperscale search; exact sites hidden. Search `Amazon Data Services Switzerland`, `AWS Zurich`, `eu-central-2`, permits/grid. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table | Switzerland North = Zurich; Switzerland West = Geneva; paired-region relationship | Search `Microsoft Switzerland North`, `Switzerland West`, `Microsoft datacenter Zurich Geneva`, local SPVs, permits. |
| Google Cloud | https://docs.cloud.google.com/compute/docs/regions-zones and https://cloud.google.com/about/locations plus launch blog https://cloud.google.com/blog/products/infrastructure/new-gcp-region-in-zurich-growing-our-support-for-swiss-and-european-businesses | Zurich region `europe-west6`, 3 zones | Search `Google Cloud Zurich region`, `Google Switzerland data center`, permits and grid around Zurich metro. |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ and release note https://docs.oracle.com/iaas/releasenotes/changes/f5ad59ae-8328-48b0-9a24-122102822dc5/index.htm | Zurich `eu-zurich-1`, region key ZRH | Search `Oracle eu-zurich-1`, `Oracle Switzerland North`, partner/dedicated-region announcements. |

Cloud-region rule: cloud region pages prove service geography, not buildings. Count a physical facility only when an operator page, permit, utility/grid record, or credible trade source identifies a site/campus.

### 4.2 Major colocation and infrastructure operators

| Operator | Official/strong source | Swiss facility seed | Reliability/use |
|---|---|---|---|
| Green / Green Datacenter | Green official business page https://www.green.ch/de/grosskunden and S-GE project news https://www.s-ge.com/invest/en/articles/news/green-datacenter-starts-construction-work-two-additional-data-centers | Zurich-area campuses including Lupfig/Zurich West, Dielsdorf, Schlieren/Zurich City, Glattbrugg; two additional Metro-Campus Zurich DCs started in 2025 | Grade A/B. Use official/company and Swiss trade/investment news as seeds, then permits in Aargau/Zurich municipalities. |
| STACK Infrastructure | Zurich official page https://www.stackinfra.com/locations/emea/zurich/ and Geneva page https://www.stackinfra.com/locations/emea/geneva/ | ZUR01/Rafz, ZUR02/Beringen, ZUR03/Zurich area; Geneva/Gland GEN02/GEN03 | Grade A for operator facility names; cross-check Beringen with Schaffhausen official permit files. |
| Digital Realty | Zurich official page https://www.digitalrealty.com/data-centers/emea/zurich | Three Zurich/Glattbrugg data centers ZUR1/ZUR2/ZUR3; official page gives total colocation space and ecosystem | Grade A operator seed; cross-check Opfikon/Glattbrugg permits and energy. |
| Equinix | Switzerland official page https://www.equinix.com/data-centers/europe-colocation/switzerland-colocation | Five Swiss data centers: Geneva and Zurich metros | Grade A operator seed; exact sites need facility pages/permits. |
| NTT Global Data Centers | Zurich 1 official page https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/emea/zurich-1-data-center | Zurich 1 in Ruemlang; page gives 10,500+ m2 server space and max IT load 20 MW | Grade A operator seed; search Ruemlang permit/energy records. |
| Swisscom | Corporate/official pages, Uptime Institute case for Bern/Wankdorf, OFCOM telecom context | Swisscom internal/enterprise datacenters including Bern/Wankdorf and other national sites | Grade A/B depending on source; telecom facilities may be non-colo and less transparent. |
| T Cloud Public / T-Systems | https://www.t-cloud-public.com/en/data-security-gdpr-cloud/data-centers | Swiss T Cloud Public references datacenters in Bern and Zollikofen | Grade B+/official operator seed; cross-check Bern/Zollikofen permits. |
| CKW / WWZ / Datacenter Zug / CONVOTIS / Datasource / Moresi.com / BancaDati.ch | CKW story https://www.ckw.ch/ueber-ckw/ckw-storys/aio-setzt-auf-ckw, WWZ story https://www.wwz.ch/de/ueber-wwz/blog/2022/telekommunikation/datacenter-zug, Ticino source https://www4.ti.ch/can/oltreconfiniti-en/from-1990-to-the-present-day/leading-international-companies/information-and-communication-technology-ict/moresicom | Zug/Rotkreuz, Zug, Ticino Manno/Melano, regional telco/enterprise colocation | Grade A/B. Useful for secondary-city enumeration; verify with municipal notices and operator pages. |

### 4.3 Trade press and secondary sources

Use trade press to find current projects, operator names, capacity, and construction milestones, then backfill official evidence:

- Data Center Dynamics: Switzerland/Green/STACK/Beringen articles. Grade B.
- SRF/swissinfo.ch: Swiss national media, useful for energy-grid/political context around Beringen and national power concerns. Grade B.
- Swiss IT Magazine, Inside IT, Netzwoche, Handelszeitung, NZZ, Aargauer Zeitung, Schaffhauser AZ, Le Temps, AGEFI, ICTjournal, Computerworld.ch. Grade B/C depending on article specificity.
- Research-and-markets/DatacenterMap/Baxtel/datacenters.com/DC Byte: good for candidate lists and addresses, but Grade C until corroborated by official/operator sources.

Do not import aggregate facility counts from commercial maps directly. Use them as candidate generators only.

---

## 5. Canton-by-canton enumeration routing

For all cantons, run a three-pass sweep:

1. **Official permits**: canton portal, official gazette/amtsblatt/feuille/albo, municipality site, open-data/map layer.
2. **Energy/grid**: utility, cantonal energy office, substation/Unterwerk/raccordement terms, waste-heat/district-heating terms.
3. **Operator/cloud**: official facility pages and trade press for operator/site codes, then back to permits.

| Canton | First official route | Second route | Datacenter-specific notes |
|---|---|---|---|
| ZH Zurich | eBaugesucheZH; Zurich current Baugesuche open data; municipal pages; `amtsblatt.zh.ch` | ewz, EKZ, council minutes, zoning/planning docs | Highest priority. Sweep Zurich city, Opfikon/Glattbrugg, Ruemlang, Schlieren, Dielsdorf, Rafz/Zurich border, Winterthur. Operators: Green, Digital Realty, NTT, STACK, Equinix, hyperscalers. |
| AG Aargau | Municipal Baugesuche/Amtsblatt; AG cantonal planning/building pages; opendata where available | AEW/IBB Energie, district-heating networks | High priority because Green's Lupfig/Zurich West campus is in Aargau. Search Lupfig, Birr, Brugg/Eigenamt. |
| SH Schaffhausen | Kanton SH Amtsblatt and government PDFs; Beringen municipal files | EKS utility and cantonal council/government responses | High priority due STACK/Safe Host Beringen. Use official Beringen permit PDFs as template. |
| GE Geneva | SAD construction authorization platform; Geneva open-data dossier; SITG maps | SIG utility, Grand Conseil docs, commune pages | High priority. Sweep Geneva, Vernier, Meyrin, Plan-les-Ouates. Operators: Equinix, STACK/Geneva-region, Azure Switzerland West signal. |
| VD Vaud | FAO Vaud/CAMAC public inquiry notices; GEOVD_CAMAC layer; municipal pages | Romande Energie, Lausanne/Renens council docs | High priority. Sweep Gland, Lausanne, Renens, Ecublens, Nyon, Yverdon. Operators: STACK Gland/Geneva, state datacenter in Renens. |
| BE Bern | eBau Bern; Regierungsstatthalteramt/municipality notices; Amtsanzeiger | BKW, municipal/cantonal IT procurement | Medium-high. Sweep Bern, Zollikofen, Ittigen/Worblaufen, Biel/Bienne. Operators: Swisscom, T Cloud Public, public-sector DCs. |
| TI Ticino | Canton Ticino UDC process; municipal `albo comunale`/`domande di costruzione`; Lugano notices | AET/local utilities, CSCS/ETH official docs | Medium-high. Sweep Lugano, Manno, Melano, Bellinzona. Operators/sites: CSCS, Moresi.com, BancaDati.ch. |
| BS Basel-Stadt | Basel-Stadt Baupublikationen and e-Kantonsblatt | IWB utility, Basel-Stadt open data | Medium. Search Basel pharma/enterprise, IWB cooling/heat, telecom sites. |
| BL Basel-Landschaft | Bauinspektorat publications/Amtsblatt; municipal notices | EBL/IWB/regional utility searches | Medium. Search Pratteln, Muttenz, Allschwil, Reinach, Liestal. |
| ZG Zug | Zug canton/municipal Baugesuche; official gazette; Zug city/Cham/Risch pages | WWZ/CKW, Datacenter Zug/CONVOTIS/Datasource pages | Medium. Sweep Zug, Baar, Cham, Risch-Rotkreuz, Huenenberg. |
| LU Lucerne | Cantonal/municipal Baugesuche; eBau where available | CKW/eWL utility, council minutes | Medium. Search Lucerne, Emmen, Kriens, Root/D4, Sursee. |
| SG St. Gallen | Canton/municipal Baugesuche; Amtsblatt | SAK/Stadtwerke St. Gallen, local telcos | Medium-low. Sweep St. Gallen, Rapperswil-Jona, Wil, Gossau. |
| TG Thurgau | Canton/municipal Baugesuche; Amtsblatt | EKT/regional utilities | Medium-low. Search Frauenfeld, Kreuzlingen, Weinfelden, Arbon. |
| SO Solothurn | eBau/Solothurn cantonal process; municipal notices; Amtsblatt | AEK/Alpiq/regional utilities | Medium-low. Search Olten, Solothurn, Grenchen, Oensingen. |
| SZ Schwyz | Amtsblatt Schwyz; municipal Baugesuche | EBS/EW utility searches | Medium-low. Search Freienbach, Pfaeffikon SZ, Schwyz. |
| FR Fribourg | French/German permit notices; communes; canton planning pages | Groupe E utility | Medium-low. Search Fribourg, Bulle, Villars-sur-Glane. |
| VS Valais | Canton/commune building notices, French/German; official bulletin | FMV/OIKEN utilities, industrial-energy sites | Medium-low. Search Sion, Martigny, Visp, Sierre; include HPC/energy-intensive leads. |
| NE Neuchatel | Canton/commune permit notices; official feuille | Viteos utility, watch/industrial sites | Low-medium. Search Neuchatel, La Chaux-de-Fonds, Le Locle. |
| JU Jura | Canton/commune permit notices; official journal | local utilities | Low. Search Delemont, Porrentruy. |
| GR Graubuenden | eBBV/digital permit pilots; municipal notices; Amtsblatt | Repower/EW utilities | Low-medium. Search Chur, Landquart, Davos/HPC, St. Moritz. |
| GL Glarus | Cantonal/municipal building notices; Amtsblatt | local utility/hydro context | Low. Search Glarus, Netstal, Naefels. |
| UR Uri | eBau/municipal notices; Amtsblatt | local utility/hydro, Gotthard infrastructure | Low. |
| OW Obwalden | Municipal/cantonal notices; Amtsblatt | local utilities | Low. |
| NW Nidwalden | Municipal/cantonal notices; Amtsblatt | local utilities | Low. |
| AI Appenzell Innerrhoden | Amtsblatt/municipal notices | local utility | Low. |
| AR Appenzell Ausserrhoden | Amtsblatt/municipal notices | SAK/local utility | Low. |

For lower-density cantons, search primarily for `Rechenzentrum`, `Datencenter`, `Serverraum`, `ICT`, `Colocation`, utility datacenters, hospitals/universities, public-sector IT buildings, and operator acquisitions.

---

## 6. Practical extraction workflow

1. Build seed list from official operator/cloud pages: AWS, Azure, Google, Oracle, Green, STACK, Digital Realty, Equinix, NTT, Swisscom, CKW/WWZ, local telcos.
2. For each seed, normalize geography to canton + municipality + address/parcel if possible.
3. Search the canton's official permit route in local language. For Zurich/Geneva/Vaud, use the open-data/map routes first; for Bern/Ticino, use eBau/process sources to identify the municipal publication route; for other German cantons, search Amtsblatt + municipality.
4. Search official gazettes and council/government documents for the operator, project code, address, and parcel number.
5. Search energy/grid sources: Swissgrid/ElCom only for national context, then local utility for connection/substation/heat-reuse evidence.
6. Cross-check with trade press for current status: announced, permit filed, permit granted, construction start, operational.
7. Store confidence:
   - Grade A: official permit/gazette, official map/open data, official utility/government document, official operator facility page.
   - Grade B: reputable national/trade press or association/investment agency with named operator/site/capacity.
   - Grade C: commercial datacenter maps, broker pages, scraped directories, unsourced market reports.

Minimum facility record fields:

```text
country=CH
canton
municipality/commune/comune
address
parcel/GB/CAMAC/SAD/permit number
operator legal entity
operator brand
project/facility code
source_status: application | public_inquiry | permit_granted | legally_binding | construction | operational | expansion
publication_date
permit_authority
source_urls
grid_connection_mw
it_load_mw
emergency_generation
cooling/water
waste_heat
confidence_grade
notes_on_language/source
```

Key caution: Switzerland has many bank, government, telecom, university, hospital, and enterprise server facilities that are real datacenters but may not be commercial colocation. Keep a field for `facility_type` (`commercial_colo`, `hyperscale_cloud`, `telecom`, `public_sector`, `enterprise`, `HPC/research`) instead of forcing all records into the same market category.
