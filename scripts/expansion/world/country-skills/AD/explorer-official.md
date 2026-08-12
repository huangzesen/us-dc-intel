# AD Explorer Official - Andorra Datacenter Enumeration

Date: 2026-08-12. Country: **AD Andorra**. Division model: **7 parishes (parroquies)** per `world-manifest.jsonl`: **Canillo; Encamp; La Massana; Ordino; Sant Julia de Loria; Andorra la Vella; Escaldes-Engordany**. Scope: official and regulator-facing methodology for finding commercial, telecom, public-sector, colocation, cloud, disaster-recovery, AI/HPC, and large server-room facilities in Andorra.

Reliability grades used in this file:

- **A** = primary evidence from a public body, official register/gazette, utility, public procurement record, operator-owned facility/service page, or official cloud-provider region page.
- **B** = strong secondary evidence: named-executive interview, reputable local press, CATNIX/CSUC/RIPE/PeeringDB, vendor case study, or trade press with enough detail to follow up.
- **C** = weak lead: aggregator directory, marketplace page, reseller claim, investment-promotion narrative without a named site, address inferred from a corporate office, social post, or job ad.
- **U** = unverified rumour or unsupported inference; use only as a search cue.

Apply the grade only to the fact proved by the source. Example: Andorra Telecom's own Data Centre page is **A** for a marketed data-centre service in La Massana, but it is not proof that every aggregator-listed Andorra Telecom site is public colocation. A CEO interview is **B** for the statement that Andorra Telecom operates three data centres, but aggregator addresses for La Comella, Nexus/Santa Coloma, or La Massana remain **C** until matched to an operator, BOPA, Comu, or cadastral source. Official Govern/Andorra Digital announcements are **A** for cloud collaboration agreements; they are **not** proof of a hyperscale physical region in Andorra.

---

## 0. Andorra Structure Facts

- Andorra has **no public national datacenter registry** and no independent data-centre regulator. Enumeration must join BOPA/legal acts, Govern and Comu planning records, FEDA grid evidence, Andorra Telecom operator evidence, APDA/data-protection records, official digital-transformation pages, procurement, and local press.
- Administrative model: **7 parishes**: Canillo, Encamp, La Massana, Ordino, Sant Julia de Loria, Andorra la Vella, Escaldes-Engordany. The parishes are the planning/permitting tier below the national Government; each Comu controls urbanism, works licences, and activity licences.
- A real new data-centre build would normally leave at least three official traces: **Comu urbanism/works/activity licence**, **FEDA large-consumer/grid connection planning**, and **BOPA/procurement/corporate act** if the Government, FEDA, Andorra Telecom, or another public entity is involved.
- Market shape is small and state-operator-led. The only operator-owned public evidence found for a marketed facility is Andorra Telecom's **Data Centre for businesses** page, which says the facility is in **La Massana** and offers server-hosting services: https://www.andorratelecom.ad/en/business/data-center-new-abc/.
- Andorra Telecom's CEO stated in an all-andorra.com interview dated 2026-08-05 that the company operates three data centres: **La Massana, La Comella, and Santa Coloma**. Grade this **B** for the three-site statement. Treat exact street addresses, capacity, tier, and customer availability for La Comella/Santa Coloma as unverified unless an operator, BOPA, or Comu source confirms them.
- Energy is a hard constraint. FEDA is the state utility: https://www.feda.ad/. Andorra imports much of its electricity from Spain and France. Cadena SER Andorra reported on 2025-10-20 that FEDA and Endesa extended their supply convention to 2037 and publicly discussed the possibility of a data center in Andorra: https://cadenaser.com/andorra/2025/10/20/feda-i-endesa-allarguen-el-conveni-de-subministrament-electric-fins-al-2037-radio-ser-principat-d-andorra/. Grade this **B** for intent only: no site, no capacity, no project approval.
- Cloud-agreement signals are official but do not imply local hyperscale regions. Govern and Andorra Digital announced a Google Cloud agreement on 2025-04-01: https://www.govern.ad/ca/w/andorra-signa-acord-google-cloud-impulsar-digitalitzacio-ambit-public-privat and https://andorra-digital.com/en/news/agreement-google-cloud-drive-digitalization-public. Govern also announced an AWS strategic alliance on 2025-07-18: https://www.govern.ad/ca/w/andorra-amazon-services-signen-alianca-estrategica-per-accelerar-la-transformacio-digital-del-pais. Grade these **A** for official cloud collaboration, **negative** for physical cloud-region evidence.
- Hyperscale negative checks as of this file date: AWS, Microsoft Azure, Google Cloud, and Oracle OCI official region lists show no Andorra region. Nearest official regions include AWS Europe (Spain) `eu-south-2`, Azure Spain Central `spaincentral`, Google Cloud `europe-southwest1` Madrid, and Oracle Spain Central / Madrid. Re-check every sweep.
- Expected real yield for a national sweep: **3-6 discrete facilities**: Andorra Telecom La Massana (A), Andorra Telecom La Comella and Santa Coloma (B until primary confirmation), possible internal operator/government CPDs, and small private server rooms. Do not inflate counts from aggregators.

---

## 1. Search Vocabulary

Use Catalan first for official records and local press, Spanish for Endesa/REE and Spanish press, French for RTE/border connectivity, and English for hyperscaler and aggregator checks.

English:

```text
data center
data centre
datacenter
colocation
co-location
cloud
cloud region
server room
disaster recovery
business continuity
Tier III
Tier IV
Uptime
MW
MVA
substation
transformer
backup generator
IXP
cross-border fiber
```

Catalan:

```text
centre de dades
centre de processament de dades
CPD
col.locacio
colocacio
nuvol
nuvol sobira
sala de servidors
servidors
hosting
allotjament
MW
MVA
subestacio
estacio transformadora
grup electrogen
llicencia d'activitat
llicencia d'obres
permis d'obres
pla d'urbanisme
pla general d'ordenacio
modificacio urbanistica
parroquia
comu
BOPA
licitacio
concurs public
adjudicacio
```

Spanish:

```text
centro de datos
centro de procesamiento de datos
CPD
nube soberana
sala de servidores
subestacion electrica
licencia de actividad
licencia de obras
suministro electrico
```

French:

```text
centre de donnees
centre de traitement de donnees
hebergement
cloud souverain
salle de serveurs
sous-station electrique
raccordement au reseau
```

---

## 2. Official Permit, Legal, Registry, and Cadastre Sources

### 2.1 National Sources

| Source | URL | Use | Grade |
|---|---|---|---|
| Govern d'Andorra | https://www.govern.ad/ | National laws/decrees, ministry news, public cloud agreements, telecom policy. | A |
| BOPA - Butlleti Oficial del Principat d'Andorra | https://www.bopa.ad/ | Official gazette: laws, decrees, public tenders, awards, public-company acts. | A |
| Portal Juridic | https://portaljuridicandorra.ad/ | Consolidated law. Key checked law: LGOTU at https://portaljuridicandorra.ad/L20001229C_10. | A |
| Tramit portal | https://www.tramits.ad/ | Electronic administrative procedures and licence routes. | A for process |
| Andorra Digital | https://andorra-digital.com/ | State digital agency; cloud agreements and homologated cloud services. | A |
| APDA | https://www.apda.ad/ | Data-protection authority; cloud/international transfer guidance and compliance context. | A |
| Departament d'Estadistica | https://www.estadistica.ad/ | Energy, population, ICT and economic datasets for feasibility context. | A |
| Andorra Business | https://www.andorrabusiness.com/ | Investment agency and business setup; use as project lead source, not facility proof unless specific. | A/B |

### 2.2 Parish Planning Sources

Use all seven Comuns; division coverage must stay exactly aligned to `world-manifest.jsonl`.

| Parish | Comu URL | Search focus | Grade |
|---|---|---|---|
| Canillo | https://www.canillo.ad/ | Urbanism, activity licences, ski-resort infrastructure. | A |
| Encamp | https://www.comuencamp.ad/ | Urbanism, activity licences, Encamp/Pas de la Casa utility traces. | A |
| La Massana | https://www.lamassana.ad/ | Andorra Telecom La Massana facility, works/activity licences. | A |
| Ordino | https://www.ordino.ad/ | Urbanism and low-probability server-room leads. | A |
| Sant Julia de Loria | https://comusantjulia.ad/ | Border/industrial land watch-list, works/activity licences. | A |
| Andorra la Vella | https://www.andorralavella.ad/ and https://www.andorralavella.ad/comu/?q=tramits/propietat-i-urbanisme | Capital parish, La Comella, Santa Coloma, NODE/Annexus, government/bank CPDs. | A |
| Escaldes-Engordany | https://www.e-e.ad/ and https://tramits.e-e.ad/ | Office/finance server rooms, edicts, e-administration, and urbanism records. | A |

Method: search each Comu for `llicencia d'activitat`, `llicencia urbanistica`, `llicencia d'obres`, `pla d'urbanisme`, `actes del comu`, `adjudicacio`, and candidate facility names. A data centre should show electrical, cooling, generator, fire-safety, and/or change-of-use traces even if it is described as a CPD or technical building.

### 2.3 Business Registry and Cadastre

- Andorra does **not** expose a simple free public company-registry search equivalent to many EU registers. Do not invent NRT numbers.
- Use BOPA notices, public procurement awards, company pages, or notarial/registry extracts as identifiers when available.
- Cadastre and property records are local/registry-led. Treat parcel ownership or address claims as **A** only when obtained from a Comu, cadastre, Registre de la Propietat, BOPA, or operator page.

---

## 3. Energy and Utility Evidence

| Source | URL | Use | Grade |
|---|---|---|---|
| FEDA | https://www.feda.ad/ | Grid, tariffs, energy news, annual reports, large-user signals. | A |
| FEDA Solucions | https://fedasolucions.ad/ | Retail/contract mechanics and energy services. | A |
| FEDA transparency portal | https://transparencia.feda.ad/ | Public-company governance, plans, procurement traces. | A |
| Cadena SER FEDA/Endesa convention | https://cadenaser.com/andorra/2025/10/20/feda-i-endesa-allarguen-el-conveni-de-subministrament-electric-fins-al-2037-radio-ser-principat-d-andorra/ | Data-centre possibility discussed with supply extension to 2037. | B |
| Endesa Andorra PPA news | https://www.endesa.com/es/prensa/sala-de-prensa/noticias/transicion-energetica/renovables/ppa-estrategico-andorra | Official company confirmation of the strategic energy agreement; not a DC project page. | A for PPA, not facility |
| Estadistica | https://www.estadistica.ad/ | Energy balance, electricity imports and demand context. | A |

Energy method:

1. Search FEDA and FEDA transparency for `centre de dades`, `data center`, `gran consumidor`, `potencia`, `subestacio`, `ETR`, `transformador`, `connexio`, and `adjudicacio`.
2. Track Spain and France interconnection context through Endesa/REE/RTE only as feasibility evidence unless a named Andorra project appears.
3. For each candidate facility, verify the connection point, contracted power, transformer/generator permits, and whether the load could fit local constraints.
4. Treat power figures from press or aggregators as **C** until FEDA, BOPA, Comu, or operator documents confirm them.

---

## 4. Telecom and Connectivity Evidence

| Source | URL | Use | Grade |
|---|---|---|---|
| Andorra Telecom | https://www.andorratelecom.ad/ | Operator-owned services and press. | A |
| Andorra Telecom Data Centre | https://www.andorratelecom.ad/en/business/data-center-new-abc/ | Primary evidence for a business data-centre service in La Massana. | A |
| Andorra Telecom cloud services | https://www.andorratelecom.ad/en/business/cloud-services/ | Marketed cloud services; verify whether service maps to local DC or partner cloud. | A |
| Govern telecom/digital pages | https://www.govern.ad/ | Telecom policy and state digital transformation. | A |
| CATNIX | https://www.catnix.net/en/operadors-cat-and-andorra-telecom-upgrade-their-connection-to-catnix/ | Andorra Telecom CATNIX upgrade to 20 Gbps on a 100 Gbps port. | B |
| CSUC mirror | https://www.csuc.cat/es/noticia/operadorscat-y-andorra-telecom-amplian-conexion-al-catnix | Same CATNIX connectivity announcement in Spanish. | B |
| PeeringDB - ANDORRA TELECOM SAU | https://www.peeringdb.com/org/18174 | ASN/interconnection/facility seeds; requires cross-check. | B/C |
| RIPE Database | https://apps.db.ripe.net/db-web-ui/ | AS and network registration details. | B |
| IXPDB | https://ixpdb.euro-ix.net/ | Negative/positive check for IXP presence. | B |

Connectivity method: Andorra is landlocked and has no confirmed domestic IXP in the common public directories. International connectivity is via Andorra Telecom links toward Spain and France, with CATNIX in Barcelona as an important public peering signal. A new commercial DC with external customers should create traces in PeeringDB, CATNIX/IXP news, RIPE objects, operator press, or transit-provider case studies.

---

## 5. State IT, Procurement, and Cloud Agreements

| Source | URL | Use | Grade |
|---|---|---|---|
| BOPA | https://www.bopa.ad/ | Tenders/awards for hosting, CPD, cloud, backup, DR, generators, cooling, network equipment. | A |
| Andorra Digital Google Cloud agreement | https://andorra-digital.com/en/news/agreement-google-cloud-drive-digitalization-public | Official strategic agreement. | A for agreement |
| Govern Google Cloud announcement | https://www.govern.ad/ca/w/andorra-signa-acord-google-cloud-impulsar-digitalitzacio-ambit-public-privat | Official Government announcement dated 2025-04-01. | A for agreement |
| Govern AWS alliance | https://www.govern.ad/ca/w/andorra-amazon-services-signen-alianca-estrategica-per-accelerar-la-transformacio-digital-del-pais | Official Government announcement dated 2025-07-18. | A for agreement |
| Andorra Digital homologated services | https://andorra-digital.com/serveis-homologats | Homologated cloud catalogue; useful for provider leads and sovereign/cloud wording. | A |

Search BOPA and Govern for:

```text
"centre de dades"
"centre de processament de dades"
CPD
"sala de servidors"
"serveis cloud"
"nuvol sobira"
Google Cloud
Amazon Web Services
AWS
Microsoft Azure
backup
continuitat de negoci
recuperacio de desastres
grup electrogen informatica
climatitzacio CPD
```

Government IT facilities are likely internal and security-sensitive. Do not record a "Govern CPD" above **C** without a public procurement, budget, BOPA act, official page, or facility address.

---

## 6. Official Cloud-Region Negative Checks

Run every sweep and record date checked:

| Provider | Official source | Andorra result as of 2026-08-12 | Nearest relevant region |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Andorra region. | Europe (Spain), `eu-south-2`. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Andorra region. | Spain Central, `spaincentral`, Madrid. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | No Andorra region. | `europe-southwest1`, Madrid. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Andorra region. | Spain Central / Madrid regions. |

Positive but non-region signals to monitor: Govern/Andorra Digital Google Cloud agreement, Govern/AWS alliance, Andorra Digital homologated cloud services, and any future BOPA decree or Andorra Telecom facility announcement. A "sovereign cloud" service can be a legal/cryptographic/operational-control model without an Andorran hyperscale facility.

---

## 7. Official and Operator Facility Seed List

| Facility / lead | Parish | Status | Best current evidence | Grade |
|---|---|---|---|---|
| Andorra Telecom Data Centre for businesses | La Massana | Operational marketed service | Operator page: https://www.andorratelecom.ad/en/business/data-center-new-abc/ | A |
| Andorra Telecom La Massana | La Massana | Operational | Same operator page plus CEO interview naming La Massana. | A for service/parish; B for three-site context |
| Andorra Telecom La Comella | Andorra la Vella | Operational per CEO; details unverified | CEO interview; Data Center Map/datacenters.com as address/name leads only. | B for existence, C for aggregator details |
| Andorra Telecom Santa Coloma / Nexus | Andorra la Vella | Operational per CEO; details unverified | CEO interview; Data Center Map "Nexus" lead; operator corporate address in Santa Coloma is not facility proof. | B for existence, C for aggregator details |
| Andorra Telecom NODE/Annexus corporate CPD | Andorra la Vella | Technical/corporate CPD lead | CATNIX/CSUC connectivity and operator corporate context; verify with operator/BOPA. | B/C |
| Govern d'Andorra internal CPD | Andorra la Vella likely | Internal facility lead | E-government operations imply infrastructure, but no public facility source found. | C/U |
| Tecnoland "DataCenter Andorra" | Unknown; likely Andorra la Vella area | Marketed local IT/data-centre service | https://tecnoland.ad/datacenter-andorra-centre-de-dades/ - verify physical site and ASN. | B/C |
| Aitek Souverain Cloud | Unknown | Company/service lead, not a facility | all-andorra.com / El Periodic trade-show reporting; verify Andorran registry and infrastructure. | B for company/service, U for facility |

Do not add a facility to the production inventory unless it has a named operator, physical parish, evidence URL, status, and reliability grade. For Andorra, **parish-level precision is mandatory**; street-level precision is optional only when public and verified.
