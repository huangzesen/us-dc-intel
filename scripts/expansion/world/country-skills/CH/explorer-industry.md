# CH Explorer - Industry, Vendor, Cloud, Trade-Press, and Canton Query Patterns

Date: 2026-08-12. Scope: Switzerland datacenter enumeration from Swiss colo providers, official cloud-region pages, industry/trade press, associations, directories, and repeatable canton-level query patterns. Reliability grades: **A** = official/primary source such as operator-owned facility page, cloud-provider region page, cantonal/municipal permit or procurement record; **B** = established trade press, association, market report, or local press lead requiring primary confirmation; **C** = directory/aggregator/marketing-only lead.

---

## 0. Switzerland-specific frame

- Switzerland has no single national public datacenter registry. Enumerate by **operator/vendor seed -> Swiss ICT/datacenter trade press -> cloud-region official pages -> canton/municipality building-permit or gazette evidence -> power/heat/environment cross-check**.
- The market is concentrated around **Zurich / Glatt Valley / Limmat Valley / Aargau**, then **Geneva / Vaud / Lake Geneva**, **Basel region**, **Bern**, **Ticino**, and selected regional/edge sites in St. Gallen, Luzern, Zug, Schwyz, Valais, Neuchatel, and Graubunden.
- Search in all major Swiss languages. German is essential for Zurich/Aargau/Basel/Bern/eastern Switzerland; French for Geneva/Vaud/Neuchatel/Jura/Valais/Fribourg; Italian for Ticino; Romansh rarely matters but Graubunden local portals may use German/Romansh names.
- Productive German terms: `Rechenzentrum`, `Datacenter`, `Data Center`, `Datenzentrum`, `Colocation`, `Serverraum`, `Cloud Region`, `Baugesuch`, `Baubewilligung`, `Baupublikation`, `Projektauflage`, `Gestaltungsplan`, `Sondernutzungsplan`, `Umweltvertraeglichkeitspruefung`, `Notstromanlage`, `Dieselgenerator`, `Netzanschluss`, `Unterwerk`, `Fernwaerme`, `Abwaerme`, `Leistungsbedarf`, `MW`, `MVA`.
- Productive French terms: `centre de donnees`, `datacenter`, `centre informatique`, `colocation`, `region cloud`, `demande d'autorisation de construire`, `autorisation de construire`, `permis de construire`, `mise a l'enquete`, `avis d'enquete`, `plan localise`, `groupe electrogene`, `raccordement electrique`, `chaleur fatale`, `chauffage a distance`, `MW`, `MVA`.
- Productive Italian terms: `centro dati`, `data center`, `datacenter`, `colocation`, `domanda di costruzione`, `licenza edilizia`, `pubblicazione`, `generatore di emergenza`, `allacciamento elettrico`, `teleriscaldamento`.
- Swiss public evidence is fragmented. Many construction notices are municipal or cantonal gazette items with short objection windows; older notices may disappear from portal search. Use exact operator names, street addresses, municipality names, and parcel/project names from vendor/trade leads.

---

## 1. Industry, association, and trade-press sources

### 1.1 Swiss associations and market context

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Swiss Datacenter Association (Vigiswiss) | https://vigiswiss.ch/ | Swiss sector association. Use for member/operator universe, policy context, sustainability/security framing, and Swiss market contacts. Not a facility registry. | B |
| Swiss Telecommunications Association (asut) | https://asut.ch/ | Telecom/ICT policy context and member ecosystem; useful when datacenter is tied to carriers, fiber, energy, or critical infrastructure. | B-/C+ |
| Digitalswitzerland | https://digitalswitzerland.com/ | Digital infrastructure context, cloud/data-sovereignty ecosystem, not a facility enumeration source. | C+ |
| SwissICT | https://www.swissict.ch/ | ICT-sector organization; use for provider ecosystem and local company pivots, not facility evidence. | C+ |
| Switzerland Global Enterprise / cantonal economic-promotion sites | `site:s-ge.com datacenter Switzerland`, `site:{canton-economic-domain} Rechenzentrum` | Investor/cluster context; useful for regional promotion and site-selection language. Verify facilities elsewhere. | C+/B- |

### 1.2 Swiss and international trade press

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ ; `site:datacenterdynamics.com Switzerland data center {operator|city}` | Best international DC trade source for Swiss expansions, acquisitions, cloud-region builds, and capacity/MW leads. Verify status through operator or permits. | B |
| Netzwoche | https://www.netzwoche.ch/ ; `site:netzwoche.ch Rechenzentrum Schweiz {operator|Ort}` | Swiss German ICT trade press. Strong for Green, Microsoft/AWS/Google/Oracle regions, Swisscom, sustainability, and local-market announcements. | B |
| inside-it.ch | https://www.inside-it.ch/ ; `site:inside-it.ch Rechenzentrum Schweiz {operator|Ort}` | Swiss IT business press; good for cloud-provider Swiss launches, acquisitions, government/cloud-sovereignty topics, and operator moves. | B |
| Computerworld Switzerland | https://www.computerworld.ch/ ; `site:computerworld.ch Rechenzentrum Schweiz Datacenter` | Swiss CIO/ICT news; useful for regional cloud and large enterprise infrastructure leads. | B-/C+ |
| ICTjournal | https://www.ictjournal.ch/ ; `site:ictjournal.ch centre de donnees Suisse datacenter` | French-language Swiss ICT press. Essential for Geneva/Vaud/Neuchatel/Jura/Valais leads and Romandy operator news. | B |
| Le Temps / Tribune de Geneve / 24 heures / RTS | `site:letemps.ch datacenter Suisse`, `site:tdg.ch centre de donnees Geneve`, `site:24heures.ch centre de donnees Vaud`, `site:rts.ch datacenter Suisse` | Local/mainstream leads for Geneva/Vaud planning, energy, opposition, or large public-sector projects. Verify via permit or operator. | B-/C+ |
| Handelszeitung / NZZ / Aargauer Zeitung / Tages-Anzeiger | `site:nzz.ch Rechenzentrum Schweiz`, `site:aargauerzeitung.ch Rechenzentrum Lupfig`, `site:tagesanzeiger.ch Rechenzentrum Zuerich` | Useful for investment, energy, and local controversy around major German-speaking sites. | B-/C+ |
| Datacenter-Insider | https://www.datacenter-insider.de/ ; `site:datacenter-insider.de Schweiz Rechenzentrum` | German DC trade press often covers Swiss Green/Equinix/Digital Realty/NTT expansions. | B |
| Telecompaper / Capacity Media / Cloud7 | `site:telecompaper.com Switzerland data center`, `site:capacitymedia.com Switzerland data centre` | Telecom/DC transaction and expansion leads; many snippets are paywalled, so use as search pivots. | C+/B- |

### 1.3 Directories and neutral cross-checks

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Map Switzerland | https://www.datacentermap.com/switzerland/ | Fast facility/operator/city seed list. Good for smaller colo sites; verify every active facility via operator or local record. | C+ |
| Baxtel Switzerland | https://baxtel.com/data-centers/switzerland | Useful for hyperscale/campus aliases, addresses, expansions, and operator history. Treat MW and status as leads. | C+ |
| Datacenters.com Switzerland | https://www.datacenters.com/locations/switzerland | Commercial directory; good for addresses and provider aliases, not authoritative. | C |
| PeeringDB | https://www.peeringdb.com/ | Confirms interconnection facilities, IX presence, facility aliases, and sometimes addresses. Good operational cross-check, weak for capacity/pipeline. | B-/C+ |
| Cloudscene / Inflect / OCOLO | Search `{operator} Switzerland datacenter Cloudscene Inflect OCOLO` | Additional seed/cross-check layer for small regional facilities and carrier hotels. | C |

---

## 2. Major Swiss operators and vendor pivots

Operator official pages are **A for current marketed existence/location**. They are **B for capacity** unless they expose a facility datasheet/spec. For pipeline projects, prefer permit, press release, council/canton record, or grid/heat record.

| Operator / developer | Official URL / query surface | Canton / cluster pivots | Notes |
|---|---|---|---|
| Green | https://www.green.ch/en/data-centers/ and Green Datacenter pages | Zurich, Aargau | Primary Swiss operator seed. Pivot locations include Dielsdorf/Zurich area and Lupfig/Aargau campuses. Search `Green Datacenter Lupfig`, `Green Metro-Campus Zurich`, `Green Datacenter Dielsdorf`, `Green Zurich West`, `Green Zurich Metro`. |
| Digital Realty / Interxion | https://www.digitalrealty.com/data-centers/emea/zurich | Zurich | Legacy Interxion Zurich facilities are now Digital Realty. Use official Zurich page plus searches for `ZUR1`, `ZUR2`, `ZUR3`, `Glattbrugg`, `Opfikon`, `Zurich`. |
| Equinix | https://www.equinix.com/data-centers/europe-colocation/switzerland-colocation | Zurich, Geneva | Official Swiss colocation page is the starting point for Zurich and Geneva IBX facilities. Search `Equinix ZH`, `Equinix GV`, `Equinix Zurich data center`, `Equinix Geneva data center`. |
| NTT Global Data Centers | https://services.global.ntt/en/services/data-centers/global-locations/emea | Zurich | Use NTT EMEA/Switzerland pages for Zurich campus/facility references. Search `NTT Global Data Centers Zurich Switzerland`. |
| Safe Host / STACK Infrastructure | https://www.safehost.com/ and https://www.stackinfra.com/locations/emea/ | Geneva, Vaud, Zurich | Safe Host is the key Romandy operator seed and has been associated with STACK. Pivot Geneva, Gland, Plan-les-Ouates, SH1/SH2/SH3 aliases, and STACK EMEA location pages. |
| NorthC Switzerland | https://www.northcdatacenters.com/ | Basel-Landschaft, Bern, Zurich/Aargau leads | NorthC entered Switzerland through acquisitions. Search official pages for `Switzerland`, `Muenchenstein`, `Biel/Bienne`, `Basel`, `NTS Workspace`, `Netrics`. |
| Vantage Data Centers | https://vantage-dc.com/data-center-locations/emea/ | Zurich / northern Switzerland leads | Treat official Vantage location pages and DCD articles as seed. Verify any Swiss campus through municipality/canton records before storing status. |
| AtlasEdge | https://atlasedge.com/locations/ | Zurich | Edge/colo operator with Zurich leads. Use official page and PeeringDB/Data Center Map for facility alias confirmation. |
| Swisscom | https://www.swisscom.ch/ | Bern, Zurich, Vaud, Ticino, national | Swisscom is important for enterprise, cloud, telecom, and historical DC sites. Official pages are often service-focused; use local press/procurement/PeeringDB for specific facilities. |
| Aspectra | https://www.aspectra.ch/ | Zurich, Basel, Bern/Luzern leads | Swiss managed-hosting operator; use for smaller enterprise colo/server-room sites and partner facilities. |
| EveryWare / ti&m / local managed hosts | `site:{operator-domain} Rechenzentrum Schweiz` | Zurich, Bern, Basel, St. Gallen, Ticino | Seed smaller active facilities; verify address and whether owned facility vs leased colo. |
| Exoscale / Akenes | https://www.exoscale.com/ | Geneva/Vaud/Zurich logical zones | Important Swiss cloud provider; do not count logical zones as owned datacenters without facility evidence. Use as customer/operator lead. |
| Open Telekom Cloud / T-Systems / local sovereign cloud vendors | Provider official pages plus `Schweiz Rechenzentrum Standort` | Zurich/Bern/Geneva leads | Usually logical cloud/service evidence. Verify facility owner separately. |

Operator sweep patterns:

```text
site:{operator-domain} (Switzerland OR Schweiz OR Suisse OR Svizzera) ("data center" OR datacenter OR Rechenzentrum OR "centre de donnees")
"{operator}" ("Zurich" OR Zuerich OR Glattbrugg OR Opfikon OR Dielsdorf OR Lupfig) ("data center" OR Rechenzentrum OR Datacenter)
"{operator}" ("Geneva" OR Geneve OR "Plan-les-Ouates" OR Gland OR Lausanne) ("data center" OR "centre de donnees")
"{operator}" ("Basel" OR Muenchenstein OR "Biel" OR Bienne OR Bern) ("data center" OR Rechenzentrum)
"{operator}" ("MW" OR MVA OR racks OR "IT load" OR "Leistungsbedarf") Switzerland
```

---

## 3. Official cloud-region handling

Cloud pages are **A for logical cloud-region existence and metro/country name**, but **C for exact physical facility mapping** unless the provider publishes a named datacenter/campus or a local permit identifies it. Never create separate facility records from availability zones alone.

| Provider | Swiss signal to verify | Official URL / query surface | Grade |
|---|---|---|---|
| AWS | Europe (Zurich) Region, `eu-central-2`, with multiple Availability Zones | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and AWS launch/news pages for Europe (Zurich) | A region / C facility |
| Microsoft Azure | Switzerland North and Switzerland West geographies/regions, generally Zurich and Geneva areas | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ and Azure regions list | A region / C facility |
| Google Cloud | Zurich region, `europe-west6` | https://cloud.google.com/about/locations and Google Cloud Zurich launch/location pages | A region / C facility |
| Oracle Cloud Infrastructure | Zurich region, `eu-zurich-1` | https://www.oracle.com/cloud/public-cloud-regions/ | A region / C facility |
| IBM Cloud | Swiss cloud/availability-zone claims should be checked on IBM official locations pages | https://www.ibm.com/cloud/data-centers | A region/service / C facility |
| Alibaba / Tencent / Huawei / local sovereign clouds | Check official global-infrastructure pages before assuming Swiss region | Provider official infrastructure pages | A if official / C facility |

Cloud pivot queries:

```text
site:aws.amazon.com Zurich Region "eu-central-2" "Availability Zones"
site:azure.microsoft.com "Switzerland North" "Switzerland West" datacenter
site:learn.microsoft.com "Switzerland North" "Switzerland West" "Azure regions"
site:cloud.google.com Zurich "europe-west6" "Cloud region"
site:oracle.com "eu-zurich-1" "Oracle Cloud" Zurich
"{provider}" Schweiz Rechenzentrum Standort Cloud Region
"{provider}" Suisse "centre de donnees" "region cloud"
```

---

## 4. Official/public-record surfaces

### 4.1 National-level official sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| simap.ch | https://www.simap.ch/ | Swiss public procurement. Search for public-sector datacenter construction, colocation, migration, `Rechenzentrum`, `centre de donnees`, `centro dati`, `Serverraum`, `Housing`, `Cloud Region`. | A |
| Swiss Official Gazette of Commerce (SOGC/SHAB/FOSC/FUSC) | https://www.shab.ch/ | Company events, new datacenter subsidiaries, mergers/acquisitions, insolvency, address changes. Not a project registry but useful for legal-entity aliases. | A for company facts |
| Fedlex / federal law and policy | https://www.fedlex.admin.ch/ | Critical infrastructure, energy, data-sovereignty, environmental context. Rarely facility-level. | A context |
| Swiss Federal Office of Energy (SFOE/BFE/OFEN) | https://www.bfe.admin.ch/ | Energy-efficiency, waste-heat, grid and large-consumer context. Facility details usually local/cantonal. | A/B context |
| Swissgrid | https://www.swissgrid.ch/ | Transmission-grid context; useful for very large projects or substation/geography clues, not facility registry. | A/B context |
| Cantonal gazettes / official publications | Search `Amtsblatt {Kanton} Rechenzentrum`, `Feuille officielle {canton} centre de donnees`, `Foglio ufficiale Ticino centro dati` | Building applications, permits, public consultation, environmental/noise notices. This is the key A-grade layer after vendor leads. | A |
| Cantonal/municipal building portals | Search `Baugesuche {Gemeinde}`, `Baubewilligungen {Kanton}`, `autorisation de construire {commune}`, `permis de construire {canton}` | Permit/status confirmation. Availability and archive depth vary by canton and municipality. | A |

### 4.2 Permit and status search patterns

```text
site:{canton-or-municipality-domain} ("Rechenzentrum" OR Datacenter OR "Data Center") ("Baugesuch" OR "Baubewilligung" OR "Baupublikation" OR "Projektauflage")
site:{canton-or-municipality-domain} ("Rechenzentrum" OR Datacenter) ("Notstrom" OR "Dieselgenerator" OR "Netzanschluss" OR "Unterwerk" OR "Abwaerme")
site:{commune-domain} "{operator}" ("Baugesuch" OR "Baubewilligung" OR "Gestaltungsplan" OR "Sondernutzungsplan")
site:{canton-or-commune-domain} ("centre de donnees" OR datacenter) ("autorisation de construire" OR "permis de construire" OR "mise a l'enquete")
site:{canton-or-commune-domain} ("centre de donnees" OR datacenter) ("groupe electrogene" OR "raccordement electrique" OR "chaleur fatale")
site:{canton-or-commune-domain} ("centro dati" OR "data center") ("domanda di costruzione" OR "licenza edilizia")
site:simap.ch ("Rechenzentrum" OR "centre de donnees" OR "centro dati" OR Datacenter) ("Bau" OR construction OR colocation OR housing)
site:shab.ch ("Datacenter" OR "Data Center" OR Rechenzentrum OR "centre de donnees") Schweiz
```

Lifecycle/status vocabulary:

- **Lead only**: `Absicht`, `Planung`, `Projekt`, `Standortpruefung`, `Machbarkeitsstudie`, `Vorprojekt`, `projet`, `etude`, `annonce`, `intention`, `concept`.
- **Permit evidence**: `Baugesuch`, `Baupublikation`, `Baubewilligung`, `Bauentscheid`, `Projektauflage`, `Einsprachefrist`, `autorisation de construire`, `demande d'autorisation`, `mise a l'enquete`, `permis de construire`, `domanda di costruzione`, `licenza edilizia`.
- **Planning/zoning evidence**: `Gestaltungsplan`, `Sondernutzungsplan`, `Nutzungsplanung`, `Quartierplan`, `zone industrielle`, `plan localise de quartier`, `plan d'affectation`, `piano regolatore`.
- **Energy/environment evidence**: `Notstromanlage`, `Dieselgeneratoren`, `USV`, `Kuehlung`, `Rueckkuehler`, `Abwaerme`, `Fernwaerme`, `Netzanschluss`, `Unterwerk`, `Umweltvertraeglichkeitspruefung`, `groupe electrogene`, `refroidissement`, `chaleur fatale`.
- **Construction/operation**: `Spatenstich`, `Baustart`, `Grundsteinlegung`, `Inbetriebnahme`, `eroeffnet`, `operationell`, `mise en service`, `ouverture`, `operativo`.
- **Rejected/canceled**: `abgelehnt`, `zurueckgezogen`, `sistiert`, `Beschwerde`, `Einsprache`, `recours`, `refuse`, `retire`, `sospeso`.

---

## 5. Canton-by-canton enumeration recipes

Run each canton as: **known operators/places -> directories/PeeringDB -> Swiss trade press -> canton/municipal permit search -> power/heat/procurement cross-check**. Store the manifest division names below, but search local names with accents and alternate spellings.

| Manifest division | Local names / priority places | Operator/vendor pivots | Query templates |
|---|---|---|---|
| Aargau | `Aargau`, `AG`, `Lupfig`, `Birr`, `Brugg`, `Baden`, `Aarau`, `Spreitenbach` | Green Lupfig/Zurich West/Metro-Campus; possible Zurich spillover and industrial-power sites. | `site:ag.ch Rechenzentrum Baugesuch Lupfig`; `site:amtsblatt.ag.ch Rechenzentrum`; `"Green Datacenter" Lupfig Baubewilligung`; `"Lupfig" Rechenzentrum Abwaerme`; `"Aargau" Datacenter Netzanschluss`. |
| Appenzell Innerrhoden | `Appenzell Innerrhoden`, `AI`, `Appenzell` | Low-density; look for cantonal/municipal IT rooms, small hosting, disaster recovery. | `site:ai.ch Rechenzentrum Baugesuch`; `"Appenzell Innerrhoden" Rechenzentrum`; `"Appenzell" Serverraum`; `site:simap.ch Appenzell Rechenzentrum`. |
| Appenzell Ausserrhoden | `Appenzell Ausserrhoden`, `AR`, `Herisau`, `Teufen`, `Heiden` | Low-density; search regional ICT/edge and public-sector procurement. | `site:ar.ch Rechenzentrum Baugesuch`; `"Herisau" Rechenzentrum`; `"Appenzell Ausserrhoden" Datacenter`; `site:simap.ch Herisau Rechenzentrum`. |
| Bern | `Bern`, `Berne`, `BE`, `Biel`, `Bienne`, `Muenchenbuchsee`, `Ostermundigen`, `Thun` | Swisscom/government DCs; NorthC/Netrics/NTS Biel/Bienne leads; federal/cantonal procurement. | `site:be.ch Rechenzentrum Baugesuch`; `site:bern.ch Rechenzentrum Baubewilligung`; `"Biel" OR "Bienne" Rechenzentrum NorthC Netrics`; `site:simap.ch Bern Rechenzentrum`; `"Bundesverwaltung" Rechenzentrum Bern`. |
| Basel-Landschaft | `Basel-Landschaft`, `Baselland`, `BL`, `Muenchenstein`, `Pratteln`, `Muttenz`, `Reinach` | NorthC/Netrics Muenchenstein/Basel-area leads; regional enterprise/colo. | `site:bl.ch Rechenzentrum Baugesuch`; `"Muenchenstein" Rechenzentrum NorthC Netrics`; `"Pratteln" Datacenter`; `"Baselland" Rechenzentrum Notstrom`. |
| Basel-Stadt | `Basel-Stadt`, `BS`, `Basel`, `Bale` | Carrier/enterprise and pharma-related facilities; possible operators market as Basel. | `site:bs.ch Rechenzentrum Baugesuch`; `site:basel.ch Rechenzentrum`; `"Basel" Datacenter Colocation`; `"Basel" Rechenzentrum Abwaerme`. |
| Fribourg | `Fribourg`, `Freiburg`, `FR`, `Bulle`, `Marly`, `Villars-sur-Glane` | Romandy/regional enterprise DCs; check public-sector and industrial-zone projects. | `site:fr.ch ("Rechenzentrum" OR "centre de donnees")`; `"Fribourg" "centre de donnees" "autorisation de construire"`; `"Freiburg" Rechenzentrum Baugesuch`; `site:simap.ch Fribourg "centre de donnees"`. |
| Geneve | `Geneve`, `Geneva`, `GE`, `Plan-les-Ouates`, `Meyrin`, `Vernier`, `Lancy`, `Carouge`, `Satigny` | Safe Host/STACK; Equinix Geneva; Swisscom/IX/carrier sites; hyperscaler logical Switzerland West proximity. | `site:ge.ch ("centre de donnees" OR datacenter) ("autorisation de construire" OR "requete")`; `"Safe Host" Geneve "centre de donnees"`; `"Plan-les-Ouates" datacenter`; `"Equinix" Geneva data center`; `"Geneve" datacenter "groupe electrogene"`. |
| Glarus | `Glarus`, `GL`, `Netstal`, `Niederurnen`, `Bilten` | Low-density; search hydropower/industrial edge and public-sector IT. | `site:gl.ch Rechenzentrum Baugesuch`; `"Glarus" Datacenter`; `"Glarus" Serverraum`; `site:simap.ch Glarus Rechenzentrum`. |
| Graubunden | `Graubunden`, `Grisons`, `GR`, `Chur`, `Landquart`, `Davos`, `Thusis` | Low-density; regional hosting, public-sector, alpine/energy narratives. | `site:gr.ch Rechenzentrum Baugesuch`; `"Chur" Rechenzentrum`; `"Graubunden" Datacenter`; `"Davos" data center`; `site:simap.ch Graubunden Rechenzentrum`. |
| Jura | `Jura`, `JU`, `Delemont`, `Porrentruy` | Low-density; French public-sector and regional ICT leads. | `site:jura.ch ("centre de donnees" OR datacenter)`; `"Delemont" "centre de donnees"`; `"Jura" "permis de construire" datacenter`; `site:simap.ch Jura "centre de donnees"`. |
| Luzern | `Luzern`, `Lucerne`, `LU`, `Emmen`, `Kriens`, `Sursee`, `Rothenburg` | Regional managed hosting, Swisscom/enterprise, central Switzerland DR. | `site:lu.ch Rechenzentrum Baugesuch`; `site:stadtluzern.ch Rechenzentrum`; `"Luzern" Datacenter Colocation`; `"Emmen" Rechenzentrum`; `site:simap.ch Luzern Rechenzentrum`. |
| Neuchatel | `Neuchatel`, `NE`, `La Chaux-de-Fonds`, `Le Locle`, `Marin-Epagnier` | Romandy regional hosting, watchmaking/industrial IT, public-sector DCs. | `site:ne.ch ("centre de donnees" OR datacenter)`; `"Neuchatel" "centre de donnees"`; `"La Chaux-de-Fonds" datacenter`; `site:simap.ch Neuchatel "centre de donnees"`. |
| Nidwalden | `Nidwalden`, `NW`, `Stans`, `Hergiswil` | Low-density; public-sector/DR/server-room search. | `site:nw.ch Rechenzentrum Baugesuch`; `"Nidwalden" Rechenzentrum`; `"Stans" Datacenter`; `site:simap.ch Nidwalden Rechenzentrum`. |
| Obwalden | `Obwalden`, `OW`, `Sarnen`, `Kerns` | Low-density; public-sector/DR/server-room search. | `site:ow.ch Rechenzentrum Baugesuch`; `"Obwalden" Rechenzentrum`; `"Sarnen" Datacenter`; `site:simap.ch Obwalden Rechenzentrum`. |
| Sankt Gallen | `St. Gallen`, `Sankt Gallen`, `SG`, `Rapperswil-Jona`, `Buchs`, `Wil`, `Gossau` | Eastern Switzerland regional colo/MSP; university/HPC and enterprise facilities. | `site:sg.ch Rechenzentrum Baugesuch`; `site:stadt.sg.ch Rechenzentrum`; `"St. Gallen" Datacenter Colocation`; `"Rapperswil" Rechenzentrum`; `site:simap.ch "St. Gallen" Rechenzentrum`. |
| Schaffhausen | `Schaffhausen`, `SH`, `Neuhausen`, `Beringen` | Zurich-north spillover, regional enterprise/industrial sites. | `site:sh.ch Rechenzentrum Baugesuch`; `"Schaffhausen" Datacenter`; `"Neuhausen" Rechenzentrum`; `"Schaffhausen" Netzanschluss Datacenter`. |
| Solothurn | `Solothurn`, `SO`, `Olten`, `Grenchen`, `Zuchwil`, `Oensingen` | Zurich/Basel/Bern corridor spillover; regional MSP and industrial DCs. | `site:so.ch Rechenzentrum Baugesuch`; `"Olten" Datacenter`; `"Solothurn" Rechenzentrum Colocation`; `"Oensingen" Rechenzentrum`; `site:simap.ch Solothurn Rechenzentrum`. |
| Schwyz | `Schwyz`, `SZ`, `Pfaffikon`, `Freienbach`, `Wollerau`, `Brunnen` | Zurich/Zug financial and managed-hosting spillover; small high-security hosting. | `site:sz.ch Rechenzentrum Baugesuch`; `"Pfaffikon" Rechenzentrum`; `"Freienbach" Datacenter`; `"Wollerau" data center`; `site:simap.ch Schwyz Rechenzentrum`. |
| Thurgau | `Thurgau`, `TG`, `Frauenfeld`, `Kreuzlingen`, `Weinfelden`, `Arbon` | Eastern Switzerland regional/edge leads; possible industrial reuse. | `site:tg.ch Rechenzentrum Baugesuch`; `"Thurgau" Datacenter`; `"Frauenfeld" Rechenzentrum`; `"Kreuzlingen" data center`; `site:simap.ch Thurgau Rechenzentrum`. |
| Ticino | `Ticino`, `Tessin`, `TI`, `Lugano`, `Bellinzona`, `Mendrisio`, `Chiasso`, `Manno` | Ticino regional/cloud and finance/crypto-related hosting; Swisscom/local MSPs. | `site:ti.ch ("centro dati" OR datacenter) ("domanda di costruzione" OR "licenza edilizia")`; `"Lugano" "centro dati"`; `"Manno" data center`; `"Ticino" datacenter colocation`; `site:simap.ch Ticino "centro dati"`. |
| Uri | `Uri`, `UR`, `Altdorf` | Low-density; public-sector/DR, alpine/energy server-room leads. | `site:ur.ch Rechenzentrum Baugesuch`; `"Uri" Rechenzentrum`; `"Altdorf" Datacenter`; `site:simap.ch Uri Rechenzentrum`. |
| Vaud | `Vaud`, `VD`, `Lausanne`, `Gland`, `Nyon`, `Renens`, `Yverdon-les-Bains`, `Morges` | Safe Host Gland/Romandy; Swisscom/EPFL/regional cloud; Geneva spillover. | `site:vd.ch ("centre de donnees" OR datacenter) ("permis de construire" OR "mise a l'enquete")`; `"Gland" "Safe Host" datacenter`; `"Lausanne" "centre de donnees"`; `"Vaud" datacenter "chaleur fatale"`; `site:simap.ch Vaud "centre de donnees"`. |
| Valais | `Valais`, `Wallis`, `VS`, `Sion`, `Sierre`, `Martigny`, `Visp`, `Brig` | Hydropower/energy-adjacent leads, regional hosting, EPFL/innovation sites. | `site:vs.ch ("centre de donnees" OR Rechenzentrum OR datacenter)`; `"Valais" datacenter hydropower`; `"Sion" "centre de donnees"`; `"Wallis" Rechenzentrum`; `site:simap.ch Valais "centre de donnees"`. |
| Zug | `Zug`, `ZG`, `Baar`, `Cham`, `Risch`, `Rotkreuz`, `Steinhausen` | Zurich financial/cloud spillover, crypto/enterprise hosting, managed service providers. | `site:zg.ch Rechenzentrum Baugesuch`; `"Zug" Datacenter Colocation`; `"Baar" Rechenzentrum`; `"Rotkreuz" data center`; `site:simap.ch Zug Rechenzentrum`. |
| Zurich | `Zurich`, `Zuerich`, `ZH`, `Glattbrugg`, `Opfikon`, `Dielsdorf`, `Winterthur`, `Urdorf`, `Ruemlang`, `Kloten`, `Wallisellen`, `Dietikon` | Digital Realty/Interxion, Equinix, Green Dielsdorf/Metro, NTT, AtlasEdge, AWS/GCP/Oracle/Azure logical-region vicinity, SwissIX/PeeringDB carrier sites. | `site:zh.ch Rechenzentrum Baugesuch`; `site:amtsblatt.zh.ch Rechenzentrum`; `site:stadt-zuerich.ch Rechenzentrum Baubewilligung`; `"Glattbrugg" "data center" Digital Realty Interxion`; `"Opfikon" Rechenzentrum Equinix`; `"Dielsdorf" Green Datacenter Baugesuch`; `"Zurich" "AWS Region" data center`; `"Zurich" Datacenter Abwaerme`. |

---

## 6. Query bundles

### 6.1 Broad discovery

```text
("Rechenzentrum" OR Datacenter OR "Data Center" OR "Datenzentrum") (Schweiz OR Switzerland OR Suisse OR Svizzera) ("MW" OR MVA OR "Racks" OR "Colocation")
("centre de donnees" OR datacenter) (Suisse OR Geneve OR Vaud OR Neuchatel OR Valais) ("MW" OR MVA OR colocation)
("centro dati" OR datacenter) (Ticino OR Lugano OR Bellinzona) ("MW" OR colocation)
site:netzwoche.ch Rechenzentrum Schweiz {operator OR canton OR city}
site:inside-it.ch Rechenzentrum Schweiz {operator OR canton OR city}
site:ictjournal.ch "centre de donnees" Suisse {operator OR canton OR city}
site:datacenterdynamics.com Switzerland "data center" {operator OR city}
site:datacentermap.com/switzerland {city} datacenter
site:baxtel.com/data-centers/switzerland {operator OR city}
site:peeringdb.com "{facility alias}" Switzerland
```

### 6.2 Operator/address confirmation

```text
site:{operator-domain} "{city}" ("data center" OR datacenter OR Rechenzentrum OR "centre de donnees")
"{facility alias}" "{street OR municipality}" ("data center" OR Rechenzentrum OR "centre de donnees")
"{operator}" "{municipality}" ("Baubewilligung" OR "Baugesuch" OR "autorisation de construire" OR "permis de construire")
"{operator}" "{municipality}" ("Notstrom" OR "Dieselgenerator" OR "groupe electrogene" OR "Abwaerme" OR "chaleur fatale")
"{operator}" "{municipality}" ("in Betrieb" OR "Inbetriebnahme" OR "mise en service" OR "opened")
```

### 6.3 Government/procurement sweep

```text
site:simap.ch ("Rechenzentrum" OR Datacenter OR "centre de donnees" OR "centro dati") ("Colocation" OR Housing OR Bau OR "Cloud")
site:simap.ch ("Serverraum" OR "centre informatique" OR "centro informatico") ("USV" OR "Notstrom" OR "Kuehlung")
site:shab.ch ("Datacenter" OR Rechenzentrum OR "Data Center" OR "centre de donnees") ("AG" OR "SA" OR "GmbH")
site:{canton-domain} ("Rechenzentrum" OR "centre de donnees" OR "centro dati") ("Ausschreibung" OR adjudication OR "appel d'offres")
```

---

## 7. Fast validation checklist

1. **Normalize geography**: store the manifest canton, but search municipalities and local canton names. Many Zurich-branded sites are in Glattbrugg/Opfikon/Dielsdorf/Lupfig; Geneva-branded sites may be in Plan-les-Ouates, Gland, Meyrin, Vernier, or other Romandy municipalities.
2. **Separate facility from cloud region**: AWS/Azure/GCP/OCI Swiss regions prove logical presence only. Do not infer individual buildings or AZ count into facility records.
3. **Confirm active facility**: operator page, PeeringDB/IX presence, or current customer-facing datasheet. Directory-only records remain C.
4. **Confirm pipeline/status**: canton/municipal `Baugesuch`, `Baubewilligung`, `autorisation de construire`, or `permis de construire`; trade press alone is B lead.
5. **Capture Swiss-specific evidence**: parcel/site address, municipality, canton, permit reference if visible, public-notice date, objection/appeal status, emergency generator count, electrical connection, waste-heat/district-heating link, and operator legal entity.
6. **Capacity discipline**: prefer operator IT MW or permit electrical import. Treat MVA/kVA as apparent power and note when converted or not directly IT load.
7. **Avoid double counting**: Interxion/Digital Realty aliases, Safe Host/STACK aliases, Netrics/NorthC/NTS legacy names, and Zurich/Geneva marketing names can refer to the same physical facility.
