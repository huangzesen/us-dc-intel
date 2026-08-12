# BE Explorer Official - Belgium Datacenter Enumeration via Regional Permits, Grid, Cloud Regions, Official Registries

Date: 2026-08-12. Scope: Belgium (BE). Subnational model: **region**. Required division coverage: **Brussels-Capital Region**, **Flanders**, **Wallonia**. Focus: official/regulatory methodology for enumerating datacenter facilities and projects from permitting, grid, procurement, company, cloud, and other primary sources.

Reliability grades in this file are evidence grades, not facility ratings:

| Grade | Meaning |
|---|---|
| A | Official, regulator, registry, cloud-provider, IXP-operator, or operator-owned source for the exact fact stated. |
| B | Reliable trade press, professional analysis, association report, or regulator-adjacent source. |
| C | Directory, broker, market report, or other weak/secondary source; use only as seed material. |
| U | Unverified or unresolved; do not count without stronger evidence. |

A source can be A for one fact and unusable for another. Example: an Azure page is A for the existence of Azure Belgium Central, but U for the undisclosed physical buildings.

---

## 0. Belgium Structure Facts That Shape Enumeration

- Belgium has no single national datacenter register. Enumeration must join regional permits, regional and federal energy evidence, federal company/legal records, official cloud-region pages, operator pages, IXP sources, and procurement signals.
- Use the three Regions as the required divisions:
  - **Brussels-Capital Region**: 19 municipalities, including Brussels City/Neder-Over-Heembeek and Evere.
  - **Flanders / Flemish Region**: includes the Brussels Airport and ring-road datacenter cluster in Flemish Brabant: Zaventem, Machelen/Diegem, Asse/Zellik, Vilvoorde, plus Antwerp, Ghent, Aalst, Hasselt, Mechelen, Oostkamp/Bruges, and other Flemish municipalities.
  - **Wallonia / Walloon Region**: includes Hainaut, Liege, Luxembourg, Namur, and Walloon Brabant; the German-speaking Community is inside Wallonia.
- Assign each facility by **municipality**, not by marketing metro. "Brussels" in an operator or directory name frequently means Zaventem, Diegem/Machelen, Aalst, Huizingen, or Asse, which are all **Flanders**, not Brussels-Capital.
- Regional permitting is the controlling official path:
  - Brussels separates urban planning and environmental permits, with online Brussels urbanism surfaces and Brussels Environment for environmental permits.
  - Flanders uses the integrated **omgevingsvergunning** process.
  - Wallonia uses **permis d'environnement**, **permis d'urbanisme**, and for mixed projects the **permis unique**.
- Grid evidence is essential but not a permit substitute. A grid request, capacity reservation, congestion zone, or flexible-connection requirement is a project/status signal; it does not prove construction or operation.

---

## 1. Official Source Backbone

### 1.1 Federal Registries and Legal Sources

| Source | URL | Use | Grade |
|---|---|---|---|
| Crossroads Bank for Enterprises / KBO-BCE public search | `https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=en` | Confirms legal entity, establishment units, status, NACE-BEL codes, registered seat. Not a facility register. | A |
| Belgian Official Gazette / Belgisch Staatsblad / Moniteur belge | `https://www.ejustice.just.fgov.be/cgi/welcome.pl` | Official legal publications, company annexes, Justel legal database, regional legal acts. | A |
| Data Protection Authority / GBA-APD | `https://www.dataprotectionauthority.be/` | GDPR authority; useful for privacy/compliance context, not facility discovery. | A |
| Centre for Cybersecurity Belgium NIS2 pages | `https://ccb.belgium.be/regulation/nis2` | NIS2 compliance context for operators and digital infrastructure. Belgium's NIS2 law is the Law of 26 April 2024; it entered into force on 18 October 2024. | A |

Use KBO/BCE after identifying an operator name from permits or industry sources. Search legal names as well as trading names: `LCL Belgium`, `Datacenter United`, `KevlinX`, `Google Belgium`, `Microsoft`, `Proximus`, `Interxion`, `Digital Realty`.

### 1.2 Telecom and Internet Infrastructure

| Source | URL | Use | Grade |
|---|---|---|---|
| BIPT/IBPT | `https://www.bipt.be/` | Telecom regulator; confirms telecom policy, operator context, fiber/building communications regulation. Not a datacenter licensing body. | A |
| BELNET | `https://www.belnet.be/` | National research network; operator of BNIX; government/research network context. | A |
| BNIX | `https://www.bnix.net/` and `https://www.bnix.net/en/partners/pops` | Official IXP source. BNIX states it is deployed across five sites in and around Brussels. | A |
| BelgiumIX | `https://belgiumix.net/` | IXP lead source. Confirms an active Belgian internet exchange platform; map facilities separately. | A/B |

IXP presence proves interconnection relevance, not building size or permit status. Always map the PoP host address to a municipality before assigning a Region.

### 1.3 Energy and Grid Sources

| Source | URL | Use | Grade |
|---|---|---|---|
| Elia, Belgian TSO | `https://www.elia.be/en` | High-voltage grid, development plans, connection and congestion context for hyperscale projects. | A |
| CREG, federal energy regulator | `https://www.creg.be/` | Transmission regulation, tariffs, Elia oversight. | A |
| Fluvius, Flanders DSO | `https://www.fluvius.be/` and congestion news `https://www.fluvius.be/nl/veelgestelde-vragen/netcongestie`; Fall-Back Flex `https://www.fluvius.be/nl/aansluitingen/netcongestie/wat-is-fall-back-flex` | Flanders distribution grid, flexible connections, congestion. | A |
| Sibelga, Brussels DSO | `https://www.sibelga.be/en` | Brussels electricity/gas distribution; Sibelga states it serves the 19 Brussels-Capital municipalities. | A |
| ORES, Wallonia DSO | `https://www.ores.be/` | Wallonia distribution grid by service area. | A |
| RESA, Wallonia DSO | `https://www.resa.be/` | Liege-area Wallonia distribution grid. | A |
| Vlaamse Nutsregulator, formerly VREG | `https://www.vlaamsenutsregulator.be/` | Flanders utility/energy regulator; legacy searches for VREG remain useful. | A |
| BRUGEL | `https://www.brugel.brussels/` | Brussels energy regulator. | A |
| CWaPE | `https://www.cwape.be/` | Wallonia energy regulator. | A |

Grid extraction fields: `aansluitvermogen`, `puissance de raccordement`, MVA/MW, `hoogspanningsstation`, `poste haute tension`, `flexibele aansluiting`, `raccordement flexible`, congestion zone, connection queue, on-site generation, emergency generators, batteries, and heat-reuse obligations.

### 1.4 Regional Planning and Environmental Permits

#### Brussels-Capital Region

| Source | URL | Use | Grade |
|---|---|---|---|
| Urban.brussels / Brussels urbanism portal | `https://urbanisme.irisnet.be/` | CoBAT, permis d'urbanisme, public inquiries, online permit links. | A |
| MyPermit Brussels | `https://mypermit.brussels/fr/` | Online filing/tracking surface for Brussels permits where available. | A |
| Brussels Environment | `https://environment.brussels/` and `https://leefmilieu.brussels/` | Environmental permits and classified installations. | A |
| perspective.brussels | `https://perspective.brussels/` | Regional planning instruments, PRAS/PRDD/PAD context. | A |
| Brussels municipal sites | `site:{commune}.brussels` | Public-inquiry notices and municipal permit agendas. | A/B |

Brussels queries:

```text
site:urbanisme.irisnet.be datacenter OR "centre de données" OR datacentrum
site:mypermit.brussels datacenter OR "centre de données"
site:environment.brussels datacenter OR "centre de données" "permis d'environnement"
site:leefmilieu.brussels datacenter OR datacentrum milieuvergunning
"KevlinX" "Neder-Over-Heembeek" permis OR vergunning
"Antoon Van Oss" datacenter permis OR vergunning
site:{commune}.brussels datacenter permis OR "centre de données"
```

#### Flanders

| Source | URL | Use | Grade |
|---|---|---|---|
| Vlaanderen.be omgevingsvergunning | `https://www.vlaanderen.be/omgevingsvergunning` | Official overview; confirms omgevingsvergunning covers building, operating classified activities, subdivision, etc.; links to public inspection and decisions. | A |
| Omgevingsloket and Inzageloket | `https://www.vlaanderen.be/omgevingsvergunning/omgevingsloket-inzageloket-omgevingscheck-en-oefenloket`; public inspection `https://omgevingsloketinzage.omgeving.vlaanderen.be/` | Official explanation of the application, public-inspection, check, and practice portals; use Inzageloket for public inquiries and decided permits. | A |
| Omgevingsloket Inzageloket | `https://omgevingsloketinzage.omgeving.vlaanderen.be/` | Public inquiries and decided permits. | A |
| Departement Omgeving | `https://omgeving.vlaanderen.be/` | Flemish environment/planning authority, forms, decisions, legislation. | A |
| Province and municipal permit pages | e.g. province/municipality sites | Local permit decisions and public inquiries. | A/B |

Flanders queries:

```text
site:omgevingsloketinzage.omgeving.vlaanderen.be datacenter OR datacentrum
site:omgeving.vlaanderen.be datacenter OR datacentrum omgevingsvergunning
"datacenter" "omgevingsvergunning" "Zaventem" OR "Machelen" OR "Diegem"
"datacentrum" "openbaar onderzoek" "Antwerpen" OR "Gent" OR "Aalst" OR "Hasselt"
"Digital Realty" "Zaventem" omgevingsvergunning
"Datacenter United" "omgevingsvergunning" "Machelen" OR "Evere" OR "Mechelen"
"LCL" "Aalst" "omgevingsvergunning"
"Penta Infra" "Asse" OR "Zellik" "omgevingsvergunning"
```

#### Wallonia

| Source | URL | Use | Grade |
|---|---|---|---|
| Wallonie.be class 1/2 environmental and unique permits | `https://www.wallonie.be/fr/demarches/demander-un-permis-denvironnement-ou-un-permis-unique-pour-un-etablissement-de-classe-1-ou-2` | Official process for class 1/2 environmental permits and permis unique. | A |
| SPW / Wallonie environment permit document surfaces | `https://twice.spw.wallonie.be/` permit PDFs; `https://environnement.wallonie.be/` | Permit decisions, environmental conditions, IED lists, plan revisions. | A |
| Wallex | `https://wallex.wallonie.be/` | Walloon legal database. | A |
| Commune public inquiries | `site:{commune}.be "enquête publique"` | Public inquiry and permit notices. | A/B |

Wallonia queries:

```text
site:wallonie.be datacenter OR "centre de données" "permis unique"
site:twice.spw.wallonie.be datacenter OR "centre de données" OR "Google"
site:environnement.wallonie.be Farciennes Google "permis unique"
"Google" "Farciennes" "permis unique" "conditions"
"Saint-Ghislain" Google datacenter extension permis
"LCL" Gembloux "centre de données" permis
"centre de données" "enquête publique" "Farciennes" OR "Saint-Ghislain" OR "Gembloux"
```

---

## 2. Official Cloud-Region Seeds

Cloud-region sources are strong seeds but must not be converted into facility counts unless a physical site is independently identified.

| Provider | Belgium signal as of 2026-08-12 | Official source | Grade |
|---|---|---|---|
| Microsoft Azure | Azure **Belgium Central** is live. Microsoft announced opening in Brussels on 2025-11-18; the Microsoft datacenter community page for Belgium Central is live. Physical datacenter addresses are not public. | `https://datacenters.microsoft.com/gl_regions/belgiumcentral/`; `https://pulse.microsoft.com/en/transform-2/na/fa2-microsoft-opens-its-first-cloud-region-in-belgium-accelerating-innovation-and-economic-growth/` | A for region; U for buildings/division assignment |
| Google Cloud | Google has a St. Ghislain, Belgium datacenter location, and Google Cloud `europe-west1` is Belgium. Google announced an additional EUR 5 billion Belgium AI/cloud infrastructure investment in 2025. | `https://datacenters.google/locations/belgium/`; `https://cloud.google.com/about/locations`; `https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-ai-infrastructure-investment-belgium/` | A |
| AWS | No Belgium Region or Local Zone appears in the current AWS global infrastructure list. Brussels may have edge/Direct Connect presence through colocations, but that is not an AWS Region. | `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/` | A for current official list; recheck each run |
| Oracle Cloud | No Belgium public cloud region appears in Oracle's public cloud region list. | `https://www.oracle.com/cloud/public-cloud-regions/` | A for current official list; recheck each run |
| IBM Cloud | IBM's current cloud data center locations page does not present Belgium as an IBM Cloud region/datacenter market. | `https://www.ibm.com/cloud/data-centers` | A for current official list; recheck each run |

---

## 3. Government Procurement and Public-Sector Demand

| Source | URL | Use | Grade |
|---|---|---|---|
| Federal e-Procurement / BOSA | `https://www.publicprocurement.be/` | Government tenders for colocation, hosting, cloud, datacenter services, facility upgrades, generators, cooling, network rooms. | A |
| BOSA e-procurement information | `https://bosa.belgium.be/en/applications/e-procurement` | Confirms platform role and public procurement context. | A |
| TED | `https://ted.europa.eu/` | EU-level procurement notices above thresholds. | A |
| Regional/government IT bodies | BELNET, Smals, CIRB/paradigm.brussels, Digitaal Vlaanderen, SPW Digital | Public-sector facility demand and contracts; facility details often not public. | A/U |

Procurement queries:

```text
site:publicprocurement.be datacenter OR datacentrum OR "centre de données"
site:publicprocurement.be colocation OR colocatie OR hébergement
site:publicprocurement.be "salle serveur" OR serverruimte OR "data center"
site:ted.europa.eu Belgium datacenter colocation hosting cloud
site:bosa.belgium.be datacenter OR cloud OR hosting
site:belnet.be datacenter OR BNIX
```

Procurement is lead evidence unless the notice identifies a facility address or an awarded operator/service location.

---

## 4. Per-Division Enumeration Guidance

### 4.1 Brussels-Capital Region

Expected profile: interconnection-heavy urban datacenters, telecom/operator facilities, KevlinX BRU01, DCU Evere, legacy Proximus/Colt/Lumen-type rooms, government/parastatal facilities, and IXP PoPs. Do not include Zaventem, Machelen/Diegem, Aalst, Huizingen, or Asse here.

Official path:

1. Start with Brussels urbanism and Brussels Environment searches for `datacenter`, `datacentrum`, and `centre de données`.
2. Drill into municipality pages for public inquiries and commission agendas, especially Brussels City/Neder-Over-Heembeek and Evere.
3. Pair with Sibelga for distribution-grid context and Elia if the load is high-voltage scale.
4. Use KBO/BCE to resolve legal entity names.
5. Use BNIX/BelgiumIX and operator pages only to confirm interconnection/marketed existence, not permits.

Known official/primary seeds:

| Facility/project | Municipality | Evidence status | Grade |
|---|---|---|---|
| KevlinX BRU01 | Brussels City / Neder-Over-Heembeek | Operator page confirms 32 MW+ BRU01 in northern Brussels; BESIX says the data centre was handed over in Dec 2025; DCD reports ready-for-service. Permit references still need Brussels official lookup before using as permit evidence. | A for operator existence/spec; B for construction/status press; U for permit numbers |
| Datacenter United DC Evere | Evere | Operator page exists for DC Evere; map to Brussels-Capital. Verify exact address and permits. | A for operator existence; U for permit |
| Government/parastatal sites | Brussels municipalities | BELNET/BOSA/Smals/CIRB-type demand exists, but facility-level public detail is sparse. | A for organization; U for facility count |

### 4.2 Flanders

Expected profile: the largest commercial colo cluster by count, especially Zaventem, Machelen/Diegem, Aalst, Huizingen, Asse/Zellik, Antwerp, Ghent, Hasselt, Mechelen, Oostkamp/Bruges, and Mouscron/Moeskroen if DCU develops it. Grid congestion and flexible connections are central status filters.

Official path:

1. Search Omgevingsloket/Inzageloket by operator and municipality.
2. Search provincial and municipal public-inquiry pages for `datacenter`, `datacentrum`, `noodstroomaggregaat`, `koelinstallatie`, `hoogspanning`, and `omgevingsvergunning`.
3. Pair with Fluvius congestion/connection evidence; use Elia for high-voltage or hyperscale-scale projects.
4. Use KBO/BCE and the Official Gazette for corporate events.
5. Correct misleading metro names: Digital Realty Brussels BRU1/BRU3/BRU4 are listed by Digital Realty at Zaventem addresses; LCL Brussels-North is Diegem, Brussels-West is Aalst, Brussels-South is Huizingen; Penta Infra BRU01 is marketed as Brussels but is a Flemish-Brabant lead.

Known official/primary seeds:

| Facility/project | Municipality | Evidence status | Grade |
|---|---|---|---|
| Digital Realty Brussels BRU1 | Zaventem | Operator page lists Wezembeekstraat 2, 1930 Zaventem, 5,000 m2. | A |
| Digital Realty Brussels BRU3 | Zaventem | Operator page lists Mercuriusstraat 27, 1930 Zaventem, 1,470 m2. | A |
| Digital Realty Brussels BRU4 | Zaventem | Operator page lists Mercuriusstraat 27, 1930 Zaventem, 6,700 m2. | A |
| LCL Brussels-North | Diegem/Machelen | LCL states its five Belgian datacenters are Diegem, Aalst, Huizingen, Antwerp, and Gembloux; contact page gives Kouterveldstraat 13, 1831 Diegem. | A |
| LCL Brussels-West | Aalst | LCL FAQ and Uptime-related LCL news identify Brussels-West as Aalst. | A |
| LCL Brussels-South | Huizingen | LCL FAQ/news identify Brussels-South as Huizingen. | A |
| LCL Antwerp | Antwerp | LCL identifies Antwerp as one of its five Belgian datacenters; confirm address and permits separately. | A for existence |
| Datacenter United network | Multiple Flemish municipalities | DCU says it has 14 datacenters across 12 Belgian locations; operator pages include DC Antwerp, DC Machelen, DC Ghent, DC Mechelen, DC Hasselt, DC Oostkamp-Bruges, and DC Moeskroen/Mouscron. | A for operator pages; U for unverified permits |
| Penta Infra BRU01 | Asse/Zellik lead | Penta page confirms a Brussels-market BRU01 datacenter; directory/market pages place it in Asse/Zellik. Map by address before count. | A for operator existence; C/U for address if not on operator page |
| Combell colocation | Ghent lead | Combell markets colocation; use KBO and permits/directories to establish facility address. | A for service; U for facility details |

### 4.3 Wallonia

Expected profile: hyperscale-dominated. Google St. Ghislain is the anchor operational campus; Google Farciennes is a major under-construction/new campus; commercial colo is thinner, with LCL Wallonia One in Gembloux and smaller/uncertain leads.

Official path:

1. Search Wallonie/SPW permit and environmental document surfaces for `Google`, `Farciennes`, `Saint-Ghislain`, `centre de données`, and `permis unique`.
2. Search commune public-inquiry notices for Farciennes, Aiseau-Presles, Sambreville, Saint-Ghislain, Gembloux, Namur, Liege, Charleroi, and Mons.
3. Pair with Elia and ORES/RESA grid evidence, especially around Hainaut and Charleroi-area reinforcement.
4. Use Google official pages for campus existence and investment, but use Walloon permit documents for permit status.

Known official/primary seeds:

| Facility/project | Municipality | Evidence status | Grade |
|---|---|---|---|
| Google St. Ghislain | Saint-Ghislain, Hainaut | Google official location page confirms St. Ghislain, Belgium datacenters; Google Cloud locations identify Belgium/europe-west1. | A |
| Google Farciennes campus | Farciennes area, Hainaut | DCD and Brussels Times report construction started in 2024 and cite permit/environmental conditions; Walloon/SPW permit document surfaces must be used for final permit numbers. | B for project/status; U/A pending exact SPW permit record |
| LCL Wallonia One | Gembloux, Namur province | LCL announced acquisition of the ENGIE Solutions data center in Gembloux and renamed it LCL Wallonia One. | A |
| Etix Belgium/Liege datacenter | Liege market; address lead at Villers-le-Bouillet | Etix official pages confirm Belgium/Liege presence; directory sources place the site at Rue de la Science 3, 4530 Villers-le-Bouillet. Confirm permit/address before final count. | A/C |

---

## 5. Query Vocabulary

### Dutch

```text
datacenter
datacentrum
datacentra
serverruimte
colocatie
cloudregio
internetknooppunt
omgevingsvergunning
openbaar onderzoek
vergunning verleend
netaansluiting
hoogspanningsstation
noodstroomaggregaat
koelinstallatie
restwarmte
netcongestie
flexibele aansluiting
```

### French

```text
centre de données
datacenter
salle de serveurs
colocation
hébergement
région cloud
point d'échange Internet
permis d'urbanisme
permis d'environnement
permis unique
enquête publique
permis accordé
raccordement électrique
poste haute tension
groupes électrogènes
refroidissement
récupération de chaleur
congestion du réseau
```

### English

```text
data center OR data centre OR datacentre
colocation
cloud region
internet exchange point OR IXP
environmental permit
building permit
unique permit
substation
grid connection
backup generators
cooling
heat reuse
```

### German, for the German-speaking Community only

```text
Rechenzentrum
Serverraum
Colocation
Baugenehmigung
Umweltgenehmigung
```

---

## 6. Lifecycle and Count Rules

Count as a facility/project only when evidence reaches one of these levels:

| Level | Count? | Evidence examples |
|---|---|---|
| Lead | No | market report, directory listing, vague announcement, land search, region-level cloud page |
| Application/public inquiry | Usually no; track as pipeline | `aanvraag`, `demande`, `openbaar onderzoek`, `enquête publique` |
| Permitted | Yes as planned/permitted | `vergunning verleend`, `permis accordé`, official decision PDF, appeal status checked |
| Under construction | Yes | operator/contractor announcement, official construction notice, reliable trade press, permit + visible construction evidence |
| Operational | Yes | operator page, cloud location page, IXP PoP, procurement award with live service, official opening |
| Expansion | Count as expansion, not new facility unless a separate address/building is clear | operator/permit expansion record |
| Canceled/refused | No active count | `geweigerd`, `refusé`, `ingetrokken`, `retiré`, `beroep`, `recours` |

Do not count:

- Cloud regions as physical buildings.
- Edge PoPs or IXP switches as datacenters unless they identify a host facility.
- Directory-only listings without operator/official confirmation.
- Multiple operator brands at the same address as separate facilities unless there are separately operated buildings.

---

## 7. Update Cadence

- **Every run**: recheck official cloud region lists for Microsoft, Google, AWS, Oracle, IBM; these change.
- **Monthly**: public procurement, Brussels/Flanders/Wallonia permit searches, Elia and DSO grid news.
- **Quarterly**: operator location pages, BNIX/BelgiumIX/PeeringDB facility lists, DCD/Brussels Times/Belgian trade press.
- **Annual**: BDIA reports and database/map, Uptime Institute certified-facility list, regional policy plans.
- **Event-triggered**: ownership deals, Elia connection-queue policy changes, large public inquiries, hyperscaler investment announcements, or Brussels integrated-permit reform.
