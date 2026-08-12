# FR Explorer Industry - trade press, vendors, and department query patterns

Date: 2026-08-12. Scope: France datacenter enumeration methodology focused on industry/trade press, France Datacenter, vendor footprints, and repeatable department-level query patterns. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/market source, **C** = aggregator, activist map, weak secondary, or unverified lead.

---

## 0. France-specific frame

- France has no single public national "all datacenters" registry. Enumeration must combine: (1) operator facility pages, (2) cloud region pages, (3) prefecture ICPE/environmental authorization files, (4) municipal building-permit/enquiry pages, (5) trade press.
- The strongest facility evidence is usually not the permit itself but a bundled **enquete publique unique** or **consultation du public** covering both **autorisation environnementale / ICPE** and **permis de construire**. Search terms: `centre de donnees informatiques`, `datacenter`, `data center`, `centre de calcul`, `installation classee`, `ICPE`, `autorisation environnementale`, `permis de construire`.
- For Ile-de-France, large projects also need a regional-prefect approval for business premises over 5,000 m2 (`agrement prefectural`, Code de l'urbanisme R.510-1/R.510-6). Treat this as an extra A-grade lead, not a complete facility registry.
- Large new AI/hyperscale projects are spreading from Paris/Marseille into power/industrial-land locations: Dunkirk/Escaudain/Bouchain in Hauts-de-France, former industrial sites, EDF/RTE-adjacent land, and Paris-south Essonne/Yvelines clusters.

---

## 1. Source grades and URLs

### 1.1 Association and events

- **France Datacenter association** - https://www.francedatacenter.com/ and member list https://www.francedatacenter.com/adherents/ . Use as a sector-actor seed list: operators, design/build firms, electrical suppliers, cooling vendors, consultants. Grade **B** for membership/existence; not a facility registry.
- France Datacenter description via European/German Datacenter Association partner page: https://www.germandatacenters.com/en/partner/france-datacenter/ . Useful for confirming its role as the French sector association. Grade **B**.
- **Data Centre World Paris / Tech Show Paris partners** - https://www.techshowparis.fr/data-centre-world/partenaires . Good for current French ecosystem names and sponsors. Grade **B/C** depending on whether the linked member page is official.

### 1.2 Trade press and market sources

- **Le Monde Informatique - Datacenter channel**: https://www.lemondeinformatique.fr/datacenter-5.html . Best French IT trade press feed. Search with `site:lemondeinformatique.fr datacenter France {operator}` and `site:lemondeinformatique.fr "centre de donnees"`. Grade **B**.
- Le Monde Informatique example: Google Cloud outage tied to Global Switch Clichy, with useful market detail on the Paris cloud-region hosting ecosystem: https://www.lemondeinformatique.fr/actualites/lire-google-cloud-sous-l-eau-suite-a-un-incendie-chez-global-switch-clichy-90281.html . Grade **B** for site/operator clues; verify with operator or official filings.
- **Data Center Dynamics (DCD)** France tag: https://www.datacenterdynamics.com/en/tags/france/ . Excellent for M&A, hyperscale, AI clusters, operator announcements, and construction. Grade **B**.
- DCD examples to seed follow-up searches: Eclairion/Mistral in Bruyeres-le-Chatel https://www.datacenterdynamics.com/en/news/french-data-center-firm-eclairion-raises-50m-hosts-mistral-ai-cluster/ ; NTT 84 MW campus https://www.datacenterdynamics.com/en/news/ntt-to-build-84mw-data-center-campus-outside-paris-france/ ; Data4 Escaudain 700 MW https://www.datacenterdynamics.com/en/news/data4-confirms-5bn-plan-for-700mw-ai-data-center-in-northern-france/ . Grade **B**, then verify against official operator/project filings.
- **DCMag / Datacenter Magazine France**: https://dcmag.fr/ and map update article https://dcmag.fr/dcmag-renforce-sa-carte-des-datacenters-en-france-avec-les-projets-en-cours/ . French sector media; good for operator map leads. Grade **B/C** depending on sourcing.
- **DataCenter POST**: https://datacenterpost.com/ . Good conference/operator quote feed; not France-specific but useful for DATA4/European AI infrastructure narratives. Example DATA4 panel article: https://datacenterpost.com/ai-infrastructure-growth-tests-the-limits-of-power-capital-and-scale/ . Grade **B/C**.
- **GlobalData construction/project trackers**: GlobalData store/construction-project pages such as https://www.globaldata.com/store/industry/data-center-market/ and company project pages such as https://www.globaldata.com/company-profile/digital-realty-trust-inc/premium-data/construction-projects/ . Usually paywalled; use as a lead index only unless the project record is visible. Grade **C for snippets**, **B** if a full paid project record is inspected.
- **DC Byte, Structure Research, CBRE/JLL/Cushman/Knight Frank/Arizton/Mordor**: market sizing and pipeline direction, not facility truth. Grade **B** for market context; **C** for individual projects unless independently verified.
- **Aggregators**: DataCenterMap https://www.datacentermap.com/france/ , Datacenters.com https://www.datacenters.com/locations/france , PeeringDB facility pages, Baxtel. Grade **C** for discovery, **B-** for address cross-checks when multiple aggregators agree; never use as the only evidence for capacity/status.

### 1.3 Official/public records

- **Georisques installations classees**: https://www.georisques.gouv.fr/risques/installations/donnees . Search by operator/legal entity, commune, or AIOT/SIRET. Facility inspection PDFs often reveal generator counts, ICPE rubriques, status, and exact address. Grade **A**.
- **Projects-environnement.gouv.fr**: https://www.projets-environnement.gouv.fr/ . Search `datacenter`, `centre de donnees`, `centre de calcul`, operator names. Example Digital MRS5 project page: https://www.projets-environnement.gouv.fr/page/fiche/?q=recordsid%3A202419016069 . Grade **A** for environmental-procedure metadata.
- **Consultations publiques - developpement durable**: https://www.consultations-publiques.developpement-durable.gouv.fr/ . Search exact terms and MRAe opinions. Grade **A** when hosting official consultation/MRAe files.
- **Prefecture department sites**: `https://www.{department-slug}.gouv.fr/` usually under `Publications`, `Actions de l'Etat`, `Enquetes publiques`, `Installations classees`. Examples: Seine-Saint-Denis Data Hills and SEGRO pages at https://www.seine-saint-denis.gouv.fr/ ; Essonne LCP Data Village at https://www.essonne.gouv.fr/ ; Val-de-Marne Icade Rungis at https://www.val-de-marne.gouv.fr/ . Grade **A**.
- **Municipal/EPCI pages**: city pages often mirror the full public-enquiry dossier. Example Vaujours page for Tremblay/Goodman: https://vaujours.fr/enquete-publique . Grade **A-** when it hosts the official file; verify permit number with prefecture when possible.

---

## 2. Core French query templates

Use Google/Bing with `site:`. Keep accents optional; many official PDFs are OCRed without accents.

### 2.1 Facility/project discovery

```text
"{departement}" ("datacenter" OR "data center" OR "centre de donnees" OR "centre de données" OR "centre de calcul") ("permis de construire" OR "autorisation environnementale" OR ICPE OR "enquete publique" OR "consultation du public")
site:{prefecture_slug}.gouv.fr ("datacenter" OR "centre de donnees" OR "centre de données" OR "centre de calcul")
site:{commune}.fr ("datacenter" OR "centre de donnees" OR "centre de calcul") ("permis de construire" OR "enquete publique")
site:projets-environnement.gouv.fr ("datacenter" OR "centre de donnees" OR "centre de calcul") "{departement}"
site:georisques.gouv.fr ("datacenter" OR "centre de donnees" OR "centre de données") "{commune}"
```

### 2.2 Trade press/vendor triangulation

```text
site:lemondeinformatique.fr datacenter France {operator}
site:datacenterdynamics.com/en/ France datacenter {operator OR commune OR departement}
site:dcmag.fr datacenter {operator OR commune OR departement}
site:datacenterpost.com France "data center" {operator}
site:globaldata.com "data center" France {operator OR commune}
"{operator}" "{commune}" ("MW" OR "megawatt" OR "MVA" OR "m2" OR "racks")
```

### 2.3 French official vocabulary variants

```text
"centre de donnees informatiques"
"centre de données informatiques"
"centre d'hebergement de donnees"
"hebergement de donnees"
"centre de calcul"
"salle informatique"
"groupes electrogenes" "datacenter"
"rubrique 2910" "datacenter"
"rubrique 2925" "datacenter"
"dossier de demande d'autorisation environnementale" "datacenter"
"avis MRAe" "datacenter"
```

### 2.4 Lifecycle/status words

- **Planned/intent only**: `projet`, `annonce`, `protocole`, `memorandum`, `accord`, `choix du site`, `foncier`, `envisage`.
- **Permit evidence**: `permis de construire`, `PC 0xx`, `autorisation environnementale`, `ICPE`, `arrete prefectoral`, `enquete publique`, `consultation du public`, `avis MRAe`.
- **Construction**: `chantier`, `travaux`, `pose de la premiere pierre`, `livraison`, `mise en service`, `ouverture`.
- **Operational**: operator page lists the facility, cloud region live page, PeeringDB active facility, public incident/status references, or ICPE `en exploitation`.

---

## 3. Vendor/operator seed list by region

Use these as search pivots. Operator official pages are **A-** for existence/location and **B** for marketing capacity unless backed by permit/annual-report data.

| Region/cluster | Operators and official URLs | Notes |
|---|---|---|
| Ile-de-France / Greater Paris | Digital Realty Paris https://www.digitalrealty.com/data-centers/emea/paris ; Equinix France/Paris https://www.equinix.com/data-centers/europe-colocation/france-colocation ; DATA4 Paris-Saclay https://www.data4group.com/en/data-center-in-paris-france/ ; Global Switch Paris/Clichy https://www.globalswitch.com/data-centres/paris/ ; Telehouse Paris/Magny https://www.telehouse.net/data-centre-services/france/paris/ ; Scaleway/Iliad/OpCore https://www.opcore.com/ ; Eclairion https://eclairion.com/en ; NTT Paris 1 https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/emea/paris-1-data-center | Highest density. Query departments 75/77/78/91/92/93/94/95 first, especially Clichy, La Courneuve, Saint-Denis, Aubervilliers, Rungis, Marcoussis/Nozay, Magny-les-Hameaux, Bruyeres-le-Chatel, Le Coudray-Montceaux/Corbeil-Essonnes, Lognes/Emerainville. |
| Provence-Alpes-Cote d'Azur / Marseille | Digital Realty Marseille pages via https://www.digitalrealty.com/data-centers/emea ; Oracle France South/Marseille https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm ; OpCore Marseille https://www.opcore.com/ ; local carriers at Marseille port/subsea ecosystem | Search 13 Bouches-du-Rhone and Marseille municipal files for `MRS5`, `Digital`, `Port`, `Fos`, `Arenc`, `bassin`. Marseille is a subsea/cloud gateway. |
| Hauts-de-France | OVHcloud Roubaix/Gravelines https://www.ovhcloud.com/en/datacenter/ ; DATA4 Escaudain official announcement https://www.data4group.com/en/news-data4/in-northern-france-data4-launches-its-largest-data-center-campus-to-support-europes-ai-growth/ ; Microsoft/Azure France expansion via Microsoft pages and local press; Etix Lille/Tourcoing https://www.etixeverywhere.com/our-data-centers/ | Query 59 Nord and 62 Pas-de-Calais for Dunkerque, Gravelines, Roubaix, Tourcoing, Lille, Escaudain, Bouchain. Power/industrial-land angle is essential. |
| Grand Est | OVHcloud Strasbourg https://www.ovhcloud.com/en/datacenter/ ; OVH infrastructure regions https://www.ovhcloud.com/en/about-us/global-infrastructure/regions/ ; UltraEdge Strasbourg hub https://www.ultraedge.com/en/data-centers | Query 67 Bas-Rhin and 68 Haut-Rhin for Strasbourg/SBG rebuilds, edge sites, and ICPE generator filings. |
| Nouvelle-Aquitaine | Equinix Bordeaux/BX1 https://www.equinix.com/data-centers/europe-colocation/france-colocation/bordeaux-data-centers ; UltraEdge Bordeaux hub https://www.ultraedge.com/en/data-centers | Query 33 Gironde, especially Bordeaux/Bruges. |
| Auvergne-Rhone-Alpes | OpCore Lyon https://www.opcore.com/ ; Etix Lyon https://www.etixeverywhere.com/our-data-centers/ ; nLighten Lyon https://www.nlighten.com/en/ ; UltraEdge Lyon hub | Query 69 Rhone and 38 Isere first; include Lyon, Villeurbanne, Saint-Priest, Grenoble. |
| Pays de la Loire / Bretagne / Normandy / Centre | Etix Nantes and regional sites https://www.etixeverywhere.com/our-data-centers/ ; UltraEdge Rennes/Bordeaux/Lille/Paris/Lyon/Strasbourg hubs https://www.ultraedge.com/en/data-centers ; Nation Data Center regional expansion leads via DCD/DCMag | Query 44 Loire-Atlantique, 35 Ille-et-Vilaine, 76 Seine-Maritime, 14 Calvados, 45 Loiret for edge/proximity datacenters and municipal hosting facilities. |
| Occitanie | Etix Toulouse/Montpellier and acquired Eurofiber sites; nLighten/Eurofiber local edge leads | Query 31 Haute-Garonne, 34 Herault, 30 Gard, 32 Gers for Toulouse, Balma, Labege, Montpellier, Nimes, Auch. |
| Bourgogne-Franche-Comte / Centre industrial sites | EDF/OpCore/SoftBank-style AI feasibility leads and power-adjacent projects | Query by former power station, RTE substation, industrial park names; expect trade-press leads before prefecture filings. |

Additional national operators to pivot: Orange Business, SFR/Altice, Bouygues Telecom, Free/Iliad, Colt DCS, CloudHQ, CyrusOne, Prologis, Goodman, SEGRO, Icade, Ecritel, Jaguar Network/Free Pro, Thales, Worldline, Atos/Eviden, OVHcloud, Scaleway, Outscale/Dassault Systemes.

---

## 4. Hyperscaler/cloud official pages

Cloud pages prove region existence, not physical addresses. Use them as seed signals, then map to colocation operators via incidents, press, PeeringDB, and permits.

- **AWS Europe (Paris), eu-west-3, 3 AZs**: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html . Grade **A** for cloud-region existence.
- **Microsoft Azure France Central / France South**: https://learn.microsoft.com/en-us/azure/reliability/regions-list . France Central physical location Paris; France South physical location Marseille/restricted DR-style region. Grade **A**.
- **Google Cloud Paris, europe-west9**: https://cloud.google.com/about/locations and regions/zones docs https://docs.cloud.google.com/compute/docs/regions-zones . LMI/DCD incident reporting links one zone to Global Switch Clichy and mentions Interxion/Digital Realty, DATA4, Telehouse, Global Switch as Paris-zone hosts; verify per record. Grade **A** for region, **B** for facility mapping unless sourced to operator/incident.
- **Oracle Cloud Infrastructure**: public regions include France Central (Paris, `eu-paris-1`) and France South (Marseille, `eu-marseille-1`) in OCI docs https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and Oracle region page https://www.oracle.com/cloud/public-cloud-regions/ . Grade **A**.
- **OVHcloud**: official locations list Gravelines, Paris, Roubaix, Strasbourg; region page says north of France SecNumCloud region uses Gravelines/Roubaix/Strasbourg. https://www.ovhcloud.com/en/datacenter/ and https://www.ovhcloud.com/en/about-us/global-infrastructure/regions/ . Grade **A-**.
- **Scaleway/Iliad/OpCore**: use Scaleway cloud docs/region pages plus OpCore official pages and Iliad/InfraVia releases; verify exact sites through ICPE and PeeringDB. https://www.scaleway.com/en/ , https://www.opcore.com/ , https://www.iliad.fr/en/actualites/article/the-iliad-group-and-infra-via-partner-to-develop-a-major-european-hyperscale-data-center-platform .

---

## 5. Department-level enumeration method

For every department, run the same four passes:

1. **Prefecture pass (A)**: query `site:{slug}.gouv.fr` using the templates below. Look for `Enquetes publiques`, `Installations classees`, `ICPE`, `autorisation environnementale`, `arrete prefectoral`, `avis de consultation`.
2. **National environmental pass (A)**: query `site:projets-environnement.gouv.fr "{department name}" datacenter` and `site:georisques.gouv.fr "{commune}" datacenter`.
3. **Municipal/EPCI pass (A-/B)**: once a commune/operator is suspected, query city/EPCI pages for the PC number and enquiry dossier.
4. **Trade/vendor pass (B/C)**: query DCD, LMI, DCMag, DataCenter POST, GlobalData snippets, and operator pages for the same commune/operator.

Copy/paste pattern:

```text
site:{prefecture_slug}.gouv.fr ("datacenter" OR "data center" OR "centre de donnees" OR "centre de données" OR "centre de calcul" OR "centre de donnees informatiques" OR "centre de données informatiques")
site:{prefecture_slug}.gouv.fr ("permis de construire" OR "autorisation environnementale" OR "enquete publique" OR ICPE) ("datacenter" OR "centre de donnees" OR "centre de calcul")
"{department_name}" "{main_city}" ("datacenter" OR "centre de donnees" OR "centre de calcul") ("MW" OR MVA OR "groupes electrogenes" OR "permis de construire")
```

### 5.1 All department search seeds

| Code | Department | Prefecture-site query seed |
|---|---|---|
| 01 | Ain | `site:ain.gouv.fr datacenter OR "centre de donnees"` |
| 02 | Aisne | `site:aisne.gouv.fr datacenter OR "centre de donnees"` |
| 03 | Allier | `site:allier.gouv.fr datacenter OR "centre de donnees"` |
| 04 | Alpes-de-Haute-Provence | `site:alpes-de-haute-provence.gouv.fr datacenter OR "centre de donnees"` |
| 05 | Hautes-Alpes | `site:hautes-alpes.gouv.fr datacenter OR "centre de donnees"` |
| 06 | Alpes-Maritimes | `site:alpes-maritimes.gouv.fr datacenter OR "centre de donnees"` |
| 07 | Ardeche | `site:ardeche.gouv.fr datacenter OR "centre de donnees"` |
| 08 | Ardennes | `site:ardennes.gouv.fr datacenter OR "centre de donnees"` |
| 09 | Ariege | `site:ariege.gouv.fr datacenter OR "centre de donnees"` |
| 10 | Aube | `site:aube.gouv.fr datacenter OR "centre de donnees"` |
| 11 | Aude | `site:aude.gouv.fr datacenter OR "centre de donnees"` |
| 12 | Aveyron | `site:aveyron.gouv.fr datacenter OR "centre de donnees"` |
| 13 | Bouches-du-Rhone | `site:bouches-du-rhone.gouv.fr datacenter OR "centre de donnees" OR MRS5` |
| 14 | Calvados | `site:calvados.gouv.fr datacenter OR "centre de donnees"` |
| 15 | Cantal | `site:cantal.gouv.fr datacenter OR "centre de donnees"` |
| 16 | Charente | `site:charente.gouv.fr datacenter OR "centre de donnees"` |
| 17 | Charente-Maritime | `site:charente-maritime.gouv.fr datacenter OR "centre de donnees"` |
| 18 | Cher | `site:cher.gouv.fr datacenter OR "centre de donnees"` |
| 19 | Correze | `site:correze.gouv.fr datacenter OR "centre de donnees"` |
| 2A | Corse-du-Sud | `site:corse-du-sud.gouv.fr datacenter OR "centre de donnees"` |
| 2B | Haute-Corse | `site:haute-corse.gouv.fr datacenter OR "centre de donnees"` |
| 21 | Cote-d'Or | `site:cote-dor.gouv.fr datacenter OR "centre de donnees"` |
| 22 | Cotes-d'Armor | `site:cotes-darmor.gouv.fr datacenter OR "centre de donnees"` |
| 23 | Creuse | `site:creuse.gouv.fr datacenter OR "centre de donnees"` |
| 24 | Dordogne | `site:dordogne.gouv.fr datacenter OR "centre de donnees"` |
| 25 | Doubs | `site:doubs.gouv.fr datacenter OR "centre de donnees"` |
| 26 | Drome | `site:drome.gouv.fr datacenter OR "centre de donnees"` |
| 27 | Eure | `site:eure.gouv.fr datacenter OR "centre de donnees"` |
| 28 | Eure-et-Loir | `site:eure-et-loir.gouv.fr datacenter OR "centre de donnees"` |
| 29 | Finistere | `site:finistere.gouv.fr datacenter OR "centre de donnees"` |
| 30 | Gard | `site:gard.gouv.fr datacenter OR "centre de donnees"` |
| 31 | Haute-Garonne | `site:haute-garonne.gouv.fr datacenter OR "centre de donnees" OR Balma OR Labege` |
| 32 | Gers | `site:gers.gouv.fr datacenter OR "centre de donnees"` |
| 33 | Gironde | `site:gironde.gouv.fr datacenter OR "centre de donnees" OR Bruges OR Bordeaux` |
| 34 | Herault | `site:herault.gouv.fr datacenter OR "centre de donnees" OR Montpellier` |
| 35 | Ille-et-Vilaine | `site:ille-et-vilaine.gouv.fr datacenter OR "centre de donnees" OR Rennes` |
| 36 | Indre | `site:indre.gouv.fr datacenter OR "centre de donnees"` |
| 37 | Indre-et-Loire | `site:indre-et-loire.gouv.fr datacenter OR "centre de donnees"` |
| 38 | Isere | `site:isere.gouv.fr datacenter OR "centre de donnees" OR Grenoble` |
| 39 | Jura | `site:jura.gouv.fr datacenter OR "centre de donnees"` |
| 40 | Landes | `site:landes.gouv.fr datacenter OR "centre de donnees"` |
| 41 | Loir-et-Cher | `site:loir-et-cher.gouv.fr datacenter OR "centre de donnees"` |
| 42 | Loire | `site:loire.gouv.fr datacenter OR "centre de donnees"` |
| 43 | Haute-Loire | `site:haute-loire.gouv.fr datacenter OR "centre de donnees"` |
| 44 | Loire-Atlantique | `site:loire-atlantique.gouv.fr datacenter OR "centre de donnees" OR Nantes OR Carquefou` |
| 45 | Loiret | `site:loiret.gouv.fr datacenter OR "centre de donnees" OR Orleans` |
| 46 | Lot | `site:lot.gouv.fr datacenter OR "centre de donnees"` |
| 47 | Lot-et-Garonne | `site:lot-et-garonne.gouv.fr datacenter OR "centre de donnees"` |
| 48 | Lozere | `site:lozere.gouv.fr datacenter OR "centre de donnees"` |
| 49 | Maine-et-Loire | `site:maine-et-loire.gouv.fr datacenter OR "centre de donnees"` |
| 50 | Manche | `site:manche.gouv.fr datacenter OR "centre de donnees"` |
| 51 | Marne | `site:marne.gouv.fr datacenter OR "centre de donnees"` |
| 52 | Haute-Marne | `site:haute-marne.gouv.fr datacenter OR "centre de donnees"` |
| 53 | Mayenne | `site:mayenne.gouv.fr datacenter OR "centre de donnees"` |
| 54 | Meurthe-et-Moselle | `site:meurthe-et-moselle.gouv.fr datacenter OR "centre de donnees"` |
| 55 | Meuse | `site:meuse.gouv.fr datacenter OR "centre de donnees"` |
| 56 | Morbihan | `site:morbihan.gouv.fr datacenter OR "centre de donnees"` |
| 57 | Moselle | `site:moselle.gouv.fr datacenter OR "centre de donnees"` |
| 58 | Nievre | `site:nievre.gouv.fr datacenter OR "centre de donnees"` |
| 59 | Nord | `site:nord.gouv.fr datacenter OR "centre de donnees" OR Dunkerque OR Gravelines OR Roubaix OR Escaudain` |
| 60 | Oise | `site:oise.gouv.fr datacenter OR "centre de donnees" OR Rantigny` |
| 61 | Orne | `site:orne.gouv.fr datacenter OR "centre de donnees"` |
| 62 | Pas-de-Calais | `site:pas-de-calais.gouv.fr datacenter OR "centre de donnees"` |
| 63 | Puy-de-Dome | `site:puy-de-dome.gouv.fr datacenter OR "centre de donnees"` |
| 64 | Pyrenees-Atlantiques | `site:pyrenees-atlantiques.gouv.fr datacenter OR "centre de donnees"` |
| 65 | Hautes-Pyrenees | `site:hautes-pyrenees.gouv.fr datacenter OR "centre de donnees"` |
| 66 | Pyrenees-Orientales | `site:pyrenees-orientales.gouv.fr datacenter OR "centre de donnees"` |
| 67 | Bas-Rhin | `site:bas-rhin.gouv.fr datacenter OR "centre de donnees" OR Strasbourg OR SBG` |
| 68 | Haut-Rhin | `site:haut-rhin.gouv.fr datacenter OR "centre de donnees"` |
| 69 | Rhone | `site:rhone.gouv.fr datacenter OR "centre de donnees" OR Lyon OR Villeurbanne` |
| 70 | Haute-Saone | `site:haute-saone.gouv.fr datacenter OR "centre de donnees"` |
| 71 | Saone-et-Loire | `site:saone-et-loire.gouv.fr datacenter OR "centre de donnees"` |
| 72 | Sarthe | `site:sarthe.gouv.fr datacenter OR "centre de donnees"` |
| 73 | Savoie | `site:savoie.gouv.fr datacenter OR "centre de donnees"` |
| 74 | Haute-Savoie | `site:haute-savoie.gouv.fr datacenter OR "centre de donnees"` |
| 75 | Paris | `site:paris.gouv.fr datacenter OR "centre de donnees" OR Telehouse OR Scaleway` |
| 76 | Seine-Maritime | `site:seine-maritime.gouv.fr datacenter OR "centre de donnees" OR Rouen OR Le Havre` |
| 77 | Seine-et-Marne | `site:seine-et-marne.gouv.fr datacenter OR "centre de donnees" OR Lognes OR Emerainville` |
| 78 | Yvelines | `site:yvelines.gouv.fr datacenter OR "centre de donnees" OR Magny-les-Hameaux` |
| 79 | Deux-Sevres | `site:deux-sevres.gouv.fr datacenter OR "centre de donnees"` |
| 80 | Somme | `site:somme.gouv.fr datacenter OR "centre de donnees"` |
| 81 | Tarn | `site:tarn.gouv.fr datacenter OR "centre de donnees"` |
| 82 | Tarn-et-Garonne | `site:tarn-et-garonne.gouv.fr datacenter OR "centre de donnees"` |
| 83 | Var | `site:var.gouv.fr datacenter OR "centre de donnees" OR Toulon` |
| 84 | Vaucluse | `site:vaucluse.gouv.fr datacenter OR "centre de donnees"` |
| 85 | Vendee | `site:vendee.gouv.fr datacenter OR "centre de donnees"` |
| 86 | Vienne | `site:vienne.gouv.fr datacenter OR "centre de donnees"` |
| 87 | Haute-Vienne | `site:haute-vienne.gouv.fr datacenter OR "centre de donnees"` |
| 88 | Vosges | `site:vosges.gouv.fr datacenter OR "centre de donnees"` |
| 89 | Yonne | `site:yonne.gouv.fr datacenter OR "centre de donnees"` |
| 90 | Territoire de Belfort | `site:territoire-de-belfort.gouv.fr datacenter OR "centre de donnees"` |
| 91 | Essonne | `site:essonne.gouv.fr datacenter OR "centre de donnees" OR Marcoussis OR Nozay OR Bruyeres-le-Chatel OR Coudray` |
| 92 | Hauts-de-Seine | `site:hauts-de-seine.gouv.fr datacenter OR "centre de donnees" OR Clichy` |
| 93 | Seine-Saint-Denis | `site:seine-saint-denis.gouv.fr datacenter OR "centre de donnees" OR Aulnay OR Le Bourget OR Tremblay` |
| 94 | Val-de-Marne | `site:val-de-marne.gouv.fr datacenter OR "centre de donnees" OR Rungis OR Vitry` |
| 95 | Val-d'Oise | `site:val-doise.gouv.fr datacenter OR "centre de donnees" OR Saint-Ouen-l'Aumone` |
| 971 | Guadeloupe | `site:guadeloupe.gouv.fr datacenter OR "centre de donnees"` |
| 972 | Martinique | `site:martinique.gouv.fr datacenter OR "centre de donnees"` |
| 973 | Guyane | `site:guyane.gouv.fr datacenter OR "centre de donnees"` |
| 974 | La Reunion | `site:reunion.gouv.fr datacenter OR "centre de donnees"` |
| 976 | Mayotte | `site:mayotte.gouv.fr datacenter OR "centre de donnees"` |

Notes:
- Some prefecture slugs differ or redirect after site migrations. If `site:{slug}.gouv.fr` fails, query `"Prefecture {department}" "datacenter"` and use the current `*.gouv.fr` domain.
- For Paris-region projects, search neighboring departments together because environmental/permitting notices often cover multiple communes: `91 78`, `93 95`, `77 94`, etc.

---

## 6. Verification recipe

1. Start with a trade/vendor lead, but do not count the project until it has at least one A/A- source or two independent B sources.
2. Extract and store: legal entity, operator brand, commune, department, project name, permit number (`PC ...`), ICPE/environmental file URL, declared electrical connection/MW/MVA, generator count, floor area, status verb, and date.
3. Reconcile aliases: `Interxion` = Digital Realty in many French records; `Online`/`Iliad`/`Scaleway`/`OpCore` can describe related but distinct entities; `Paris` often means 91/92/93/94/95, not department 75.
4. Capacity grade: **A** only from permit dossier, MRAe opinion, operator technical spec, or official cloud/operator release; **B** from DCD/LMI/DCMag/operator marketing; **C** from market reports/aggregators.
5. Status grade: `announced` from press only, `permitted` from PC/ICPE/enquete, `under_construction` from official construction notice or credible construction trade source, `operational` from operator live page/PeeringDB/cloud active reference/ICPE en exploitation.

## 7. Fast priority order for France batch work

1. Ile-de-France departments 91, 93, 94, 92, 78, 77, 95, 75.
2. Marseille/Bouches-du-Rhone 13.
3. Hauts-de-France 59 and 62.
4. OVHcloud/Grand Est 67/68 plus Nord 59.
5. Regional edge/proximity departments: 33, 44, 31, 34, 69, 35, 76, 45, 06.
6. Sweep remaining departments with the prefecture seed table; most will be no-project or small enterprise/edge facilities, but this catches outlier AI/industrial-land proposals.

