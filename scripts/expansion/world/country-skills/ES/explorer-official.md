# ES Explorer — Official/Regulatory/Cloud Pipeline for Spain Datacenter Enumeration

Date: 2026-08-12. Scope: Spain datacenter discovery using official planning, environmental, electricity-grid, telecom-regulator, cloud-region, operator, association, and trade-press sources. Reliability grades: **A** = official/primary evidence, **B** = strong trade/association/operator evidence, **C** = weak/aggregate/announcement-only evidence.

---

## 0. Structural Facts

- Spain has no single national "datacenter permit" registry. Enumeration must join **municipal urban-planning licenses**, **autonomous-community environmental/strategic-project files**, **electricity access/connection evidence**, **BOE/autonomous gazettes**, **cloud-region announcements**, and **operator facility pages**.
- Large projects are usually visible first through **energy demand and substation filings**. Search BOE and Red Electrica/Redeia for `centro de datos`, `CPD`, `subestacion`, `linea`, `acceso y conexion`, and named promoters.
- The national energy-regulation watchlist is now important. MITECO's datacenter page states that EU energy-efficiency rules require operators of datacenters with **500 kW or more IT electrical demand** to publish/report annual information, and that datacenters above **1 MW total nominal energy input** must use waste heat or justify why not. This is a future facility-level source if published data becomes searchable: https://www.miteco.gob.es/es/energia/eficiencia/centros-de-datos.html
- Spain's primary hyperscale clusters are **Aragon** for AWS and **Community of Madrid** for Microsoft/Google/colocation. The next discovery regions are **Catalonia**, **Valencian Community**, **Basque Country**, **Andalusia**, **Galicia**, **Castile-La Mancha**, **Castile and Leon**, **Navarre**, **Murcia**, and island/edge locations.
- Search in both Spanish and regional languages: Spanish (`centro de datos`, `centro de procesamiento de datos`, `CPD`, `nube`, `hiperescala`), Catalan/Valencian (`centre de dades`, `projecte empresarial estrategic`), Basque (`datu-zentroa`, `datu zentroa`) and Galician (`centro de datos`, `centro de procesamento de datos`).

---

## 1. Official Source Spine

### 1.1 National Energy, Grid, and Gazette Sources

- **MITECO datacenter energy-efficiency page**: https://www.miteco.gob.es/es/energia/eficiencia/centros-de-datos.html  
  Use for regulatory obligations, public consultations, ReportENER/EU reporting thresholds, and sustainability constraints. **Grade A** for rules; currently not a complete facility registry.
- **MITECO environmental assessment public search**: https://sede.miteco.gob.es/portal/site/seMITECO/navServicioContenido  
  Search state-level EIA projects where national competence applies, especially high-voltage lines/substations crossing jurisdictions. Query `centro de datos`, `CPD`, `subestacion`, `linea 400 kV`, promoter names. **Grade A**.
- **BOE official gazette**: https://www.boe.es/buscar/  
  Best for national authorizations, public-information notices, land/public-domain impacts, and electricity infrastructure. Example pattern: BOE notice for `SE Penaflor 400 kV` states the purpose is connection supply for `Centro de Datos ACS DC LA PUEBLA` and cites access/connection permission: https://www.boe.es/diario_boe/txt.php?id=BOE-B-2026-24883. **Grade A**.
- **Red Electrica / Redeia access for demand**: https://www.ree.es/es/clientes/consumidor/acceso-conexion/conoce-la-capacidad-de-acceso  
  Use for demand-side access rules and published status/capacity material. Also search `site:ree.es "centro de datos" "acceso"` and `site:redeia.com "centro de datos"`. **Grade A** for grid-access framework and published capacity statements.
- **Electricity access regulation**: BOE consolidated RD 1183/2020 at https://www.boe.es/buscar/act.php?id=BOE-A-2020-17278 plus CNMC Circular 1/2024 and later CNMC specifications referenced by REE. Use to interpret whether a project has access, connection, or only a request. **Grade A**.
- **Public procurement platform PLACSP/OpenPLACSP**: https://contrataciondelsectorpublico.gob.es/wps/portal/DatosAbiertos  
  Useful mainly for public-sector CPDs, substations, design contracts, cooling/UPS upgrades, and early engineering work. Query `CPD`, `centro de proceso de datos`, `centro de datos`, `SAI`, `climatizacion CPD`, `data center`. **Grade A** for public contract facts.

### 1.2 Telecom/Regulator Sources

- **CNMC telecom regulator page**: https://www.cnmc.es/en/sectores-que-regulamos/telecomunicaciones  
  CNMC supervises electronic communications operators, broadband and internet access providers, signal transport, and market conflicts. Use for operator status and market context, not facility capacity. **Grade A**.
- **CNMC Operators Registry**: https://www.cnmc.es/en/sectores-que-regulamos/telecomunicaciones/registro-de-operadores  
  Spain requires prior notification for operation of public networks/electronic communications services under Law 11/2022. Use to validate telecom/carrier entities related to datacenters. **Grade A** for company/operator status; not facility-level.
- **CNMC Data portal**: https://data.cnmc.es/telecomunicaciones-y-sector-audiovisual/conjuntos-de-datos/datos-provinciales/telecomunicaciones and monthly data at https://data.cnmc.es/telecomunicaciones-y-sector-audiovisual/conjuntos-de-datos/datos-mensuales/telecomunicaciones  
  Use provincial/CCAA telecom indicators, fiber/mobile coverage, operator market context. **Grade A** context only.
- **Ministry broadband maps**: https://digital.gob.es/en/telecomunicaciones-infraestructuras-digitales/areas-interes/banda-ancha/informacion-cobertura/mapas-servicios-banda-ancha  
  Useful for regional connectivity screening and edge viability. **Grade A** context.

### 1.3 Autonomous-Community Environmental and Planning Sources

Spain's autonomous communities control many environmental and strategic-project procedures; municipalities control urban licenses. For each region, combine the regional official gazette, environmental portal, land-use portal, and the target municipality's planning/license search.

- **Community of Madrid**:
  - BOCM: https://www.bocm.es/
  - Comunidad de Madrid environmental/legal portal: https://gestiona.comunidad.madrid/rlma_web/
  - Madrid City licenses and CONEX search: https://sede.madrid.es/ and CONEX license query page (`Consulta de licencias y expedientes urbanisticos`).
  - Query municipalities around existing clusters: Madrid, Alcobendas, San Sebastian de los Reyes, Tres Cantos, Algete, Alcala de Henares, Getafe, Leganes, Fuenlabrada, Mostoles, Pinto. **Grade A**.
- **Aragon**:
  - Gobierno de Aragon PIGA/strategic-project pages. AWS expansion official page: https://www.aragon.es/-/expansion-aws-aragon and earlier PIGA page https://www.aragon.es/-/piga-aws-ampliacion.
  - BOA official gazette: https://www.boa.aragon.es/
  - Search Huesca, Zaragoza, Villanueva de Gallego, La Puebla de Hijar, Azaila, San Mateo de Gallego, El Burgo de Ebro. **Grade A**.
- **Catalonia**:
  - DOGC: https://dogc.gencat.cat/
  - Strategic business project classification: https://tramits.gencat.cat/ca/tramits/tramits-temes/Classificacio-de-projectes-empresarials-estrategics
  - Govern press release identifying 26 potential datacenter projects and seven poles: https://govern.cat/salapremsa/notes-premsa/811964/el-govern-identifica-26-projectes-potencials-de-centres-de-dades-i-n-estableix-set-pols-d-implantacio-a-catalunya
  - Search Barcelona metro plus Sant Adria de Besos, Terrassa, Cerdanyola, L'Hospitalet, El Prat, Tarragona/Reus, Lleida, Girona. **Grade A** for official filings/press; **B** for press interpretation.
- **Andalusia**:
  - BOJA search: https://www.juntadeandalucia.es/eboja/buscador/
  - Environmental prevention portal: https://www.juntadeandalucia.es/medioambiente/portal/areas-tematicas/prevencion-y-calidad-ambiental/prevencion-ambiental
  - AAU granted search: https://www.juntadeandalucia.es/medioambiente/servtc1/AAUo/
  - AAI granted search: https://www.juntadeandalucia.es/medioambiente/servtc1/AAIo
  - Search Sevilla/La Cartuja, Malaga, Granada, Cordoba, Cadiz/Campo de Gibraltar, Almeria. **Grade A**.
- **Valencian Community**:
  - DOGV search: https://dogv.gva.es/
  - Regional environmental/territorial files: https://mediambient.gva.es/
  - Example official PIA materials for `Data Center "El Lobo"` in Monforte del Cid: `site:mediambient.gva.es "Data Center \"El Lobo\""`.
  - Search Valencia, Paterna, Riba-roja, Sagunto, Alicante, Elche, Monforte del Cid, Castellon. **Grade A**.
- **Basque Country**:
  - BOPV: https://www.euskadi.eus/bopv2/
  - Environmental public notices: https://www.euskadi.eus/
  - Example official environmental file: `Data Center Euskadi S.L.` in Abanto-Zierbena / Ezkerraldea-Meatzaldea technology park, with 2025 public information in Euskadi files. Search `AAU01497 data center euskadi`. **Grade A**.
- **Galicia**:
  - DOG: https://www.xunta.gal/diario-oficial-galicia
  - Environmental assessment: https://cmatv.xunta.gal/
  - Search A Coruna/Arteixo, Santiago, Vigo, Lugo, Ourense, cable-landing/coastal areas. Use Galician query variants: `centro de procesamento de datos`, `centro de datos`, `avaliacion ambiental`. **Grade A**.
- **Castile-La Mancha**:
  - DOCM: https://docm.jccm.es/
  - JCCM environmental procedures: https://www.castillalamancha.es/
  - Search Toledo, Guadalajara/Alovera, Illescas, Talavera, Cuenca, Ciudad Real. Important spillover from Madrid grid/land constraints. **Grade A**.
- **Castile and Leon**:
  - BOCYL: https://bocyl.jcyl.es/
  - Environmental public information: https://medioambiente.jcyl.es/
  - Search Valladolid, Burgos, Leon, Palencia, Salamanca and substations. **Grade A**.
- **Navarre, La Rioja, Murcia, Extremadura, Cantabria, Asturias, Balearic Islands, Canary Islands**:
  - Use each official gazette plus environmental portal. Query `centro de datos`, `CPD`, `nube`, `subestacion`, `declaracion impacto ambiental`, `autorizacion ambiental`, and municipality names. These are more likely to host edge/public CPD or renewable-linked proposals than hyperscale campuses. **Grade A** when official.

---

## 2. Cloud Regions and Hyperscaler Seeds

Treat cloud pages as **A** for existence and region/zone count; they rarely disclose exact addresses or MW. Use them as seeds for permitting and grid searches.

| Provider | Official source | Geography to pivot | Notes |
|---|---|---|---|
| AWS | AWS launch post: https://aws.amazon.com/blogs/aws/now-open-aws-region-in-spain/ and AWS regions table: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | Aragon; Zaragoza and Huesca provinces; expansion to additional Aragon campuses | Region `Europe (Spain)`, API `eu-south-2`, three AZs. Also use Amazon Spain local page: https://aws.amazon.com/es/local/spain/ and Invest in Spain AWS expansion posts. |
| Microsoft Azure | Microsoft Spain Central launch: https://news.microsoft.com/es-es/2024/06/11/microsoft-opens-its-first-cloud-region-in-spain-to-accelerate-the-development-of-the-ai-economy/ and Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list | Community of Madrid | `Spain Central` with three Availability Zones; pivot to Madrid municipalities, Ferrovial construction references, and substation/BOCM filings. |
| Google Cloud | Google Cloud Madrid launch: https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-in-madrid-spain-now-open | Madrid, Telefonica infrastructure | Madrid region `europe-southwest1`, built with Telefonica. Cross-check Telefonica Tech/Telefonica real-estate and Madrid environmental/license files. |
| Oracle Cloud | Oracle cloud-region docs and Spanish press/operator pages | Madrid | Verify current regions from Oracle official region list before counting. |
| IBM Cloud | IBM cloud regions/Cloud Infrastructure Map references | Madrid | Treat aggregate maps as **C** until verified on IBM pages. |

Official investment/context sources:
- **Invest in Spain/ICEX digital economy sector**: https://www.investinspain.org/en/sectors/tic. Good for policy framing and FDI context; **B+** unless citing government-written project facts.
- **Invest in Spain AWS expansion**: https://www.investinspain.org/en/noticias-main/2024/aws and 2026 AWS support-facility article https://www.investinspain.org/en/noticias-main/2026/aws. **B+**/official investment promotion.
- **Amazon EU Aragon community page**: https://www.aboutamazon.eu/amazon-data-centre-impact-in-communities. **A-/B** for AWS self-disclosure.

---

## 3. Colo and Datacenter Operator Seeds

Use official facility pages for existence, city, facility count, and marketing capacity. Verify MW/status through permits, BOE/BOCM/DOGC, annual reports, or local planning files.

| Operator | Official/source URL | Primary geographies | Reliability notes |
|---|---|---|---|
| Equinix | Spain page: https://www.equinix.com/data-centers/europe-colocation/spain-colocation; Madrid/Barcelona pages | Madrid, Barcelona/Terrassa | Official page says Madrid and Barcelona; facility count may change, so verify current pages. **A-** existence, **B** capacity. |
| Digital Realty / Interxion | Madrid page: https://www.digitalrealty.com/data-centers/emea/madrid; investor news for Barcelona opening: https://investor.digitalrealty.com/news-releases/news-release-details/digital-realty-opens-first-data-center-barcelona-strengthening | Madrid, Barcelona/Sant Adria de Besos | Use official/investor releases plus municipal/DOGC filings. **A-**. |
| Global Switch | Madrid page: https://www.globalswitch.com/data-centres/madrid/ and locations list https://www.globalswitch.com/data-centres/ | Madrid | Locations list publishes Madrid 1/2 and MW figures; verify expansions in BOCM/municipal files. **A-**. |
| Iron Mountain | https://www.ironmountain.com/data-centers/locations/madrid-data-center | Madrid | Official says MAD-1/MAD-2/MAD-3 and planned campus; use permits for phase status. **A-**. |
| Telefonica / Telefonica Tech | Telefonica press and Google partnership pages; Ferrovial project page for Telefonica data centre in Alcala de Henares: https://www.ferrovial.com/en/business/projects/telefonica-data-centre/ | Madrid, national enterprise/cloud | Major local partner for Google Cloud and sovereign cloud. **A-** for official pages. |
| Nabiax | https://www.nabiax.com/ | Madrid/Spain | Telefonica-linked DC platform; use official + corporate registry and permits. **A-/B**. |
| Merlin Properties / Edged | Corporate releases; search Getafe/Madrid | Madrid/Getafe | Important new hyperscale/AI-ready campus signal; verify via BOCM, municipal planning, grid access. **B until official permit found**. |
| Templus | https://templus.com/ | Edge/regional Spain | Edge provider; verify by site and permits. **A-/B**. |
| Adam | https://adam.es/en/ | Barcelona/Madrid and connectivity | Regional colo/connectivity operator. **A-/B**. |
| Acens | https://www.acens.com/ | Madrid/Barcelona | Telefonica company; use official. **A-/B**. |
| Gigas / Walhalla / other local operators | Operator pages + CNMC registry | Madrid, Catalonia, Valencia, Basque | Good for SME/edge CPDs, but facility addresses often sparse. **B unless permit-backed**. |

Trade-press sources for change detection:
- **Data Center Dynamics Spanish/English**: https://www.datacenterdynamics.com/es/ and https://www.datacenterdynamics.com/en/ — strong for project announcements, permits, operator launches. **B**.
- **Cinco Dias / El Pais**, **El Economista**, **Cadena SER regional**, **Europa Press**, **La Vanguardia**, **El Periodico** — useful for regional political and planning coverage. **B** for event facts, **C** for capacity totals unless sourced to official documents.
- **Spain DC association**: https://spaindc.com/ and board/member pages. Sector voice; useful for market maps and member universe. **B**.

---

## 4. Search Query Patterns

### 4.1 General Discovery

```text
"centro de datos" +"informacion publica" +"{region_or_city}"
("centro de datos" OR "CPD" OR "centro de procesamiento de datos") ("licencia urbanistica" OR "declaracion responsable" OR "licencia de actividad") "{municipio}"
("data center" OR "centro de datos") ("subestacion" OR "linea electrica" OR "400 kV" OR "220 kV") "{provincia}"
("centro de datos" OR "CPD") ("autorizacion ambiental" OR "evaluacion de impacto ambiental" OR "declaracion de impacto ambiental")
("centro de datos" OR "CPD") ("Proyecto de Interes" OR "Proyecto Empresarial Estrategico" OR "Plan de Interes General")
```

### 4.2 Official-Site Scoped Queries

```text
site:boe.es "centro de datos" "autorizacion administrativa"
site:boe.es "centro de datos" "subestacion"
site:boe.es "CPD" "licitacion"
site:miteco.gob.es "centro de datos" "evaluacion ambiental"
site:ree.es "centro de datos" "acceso"
site:redeia.com "centro de datos" "demanda"
site:cnmc.es "registro de operadores" "{company}"
site:data.cnmc.es telecomunicaciones "{provincia}"
site:contrataciondelestado.es ("CPD" OR "centro de proceso de datos" OR "centro de datos")
```

### 4.3 Regional Query Templates

Madrid:
```text
site:bocm.es "centro de datos" ("Algete" OR "Getafe" OR "Alcala de Henares" OR "Tres Cantos")
site:sede.madrid.es "centro de datos" "licencia"
site:gestiona.comunidad.madrid "centro de datos" "evaluacion ambiental"
```

Aragon:
```text
site:aragon.es ("centro de datos" OR "AWS") ("PIGA" OR "Plan de Interes General")
site:boa.aragon.es "centro de datos" "Amazon Data Services Spain"
site:boe.es "ACS DC LA PUEBLA" OR "Amazon Data Services Spain" "Aragon"
```

Catalonia:
```text
site:dogc.gencat.cat ("centre de dades" OR "centro de datos")
site:tramits.gencat.cat "centres de dades" "Projectes empresarials estrategics"
site:govern.cat "centres de dades" "projectes potencials"
site:tauler.seu.cat ("centre de dades" OR "data center") "{municipi}"
```

Andalusia:
```text
site:juntadeandalucia.es/eboja "centro de datos" OR "CPD"
site:juntadeandalucia.es/medioambiente "centro de datos" "Autorizacion Ambiental Unificada"
site:contrataciondelestado.es "centro de datos" "Junta de Andalucia"
```

Valencian Community:
```text
site:dogv.gva.es "centro de datos" OR "edge data center"
site:mediambient.gva.es "Data Center" "Proyecto Interes Autonomico"
site:gva.es "centro de datos periférico"
```

Basque Country:
```text
site:euskadi.eus ("data center" OR "centro de procesamiento de datos" OR "datu-zentroa") ("autorizacion ambiental" OR "ingurumen")
site:euskadi.eus "Data Center Euskadi"
site:euskadi.eus "Abanto-Zierbena" "centro de datos"
```

Galicia:
```text
site:xunta.gal ("centro de datos" OR "centro de procesamento de datos") ("avaliacion ambiental" OR "informacion publica")
site:xunta.gal "subestacion" "centro de datos"
```

Castile-La Mancha:
```text
site:docm.jccm.es "centro de datos" "informacion publica"
site:castillalamancha.es "centro de datos" "evaluacion ambiental"
```

### 4.4 Operator/Promoter Pivot Queries

```text
"{operator}" "centro de datos" "{municipio}"
"{operator}" "subestacion" "{provincia}"
"{operator}" "licencia urbanistica" "{municipio}"
"{operator}" "declaracion de impacto ambiental"
"{SPV_name}" ("BOE" OR "BOCM" OR "DOGC" OR "BOA" OR "DOGV" OR "BOPV")
```

Common promoter/SPV strings: `Amazon Data Services Spain`, `Microsoft 7724 Spain`, `Google Cloud Spain`, `Interxion Espana`, `Digital Realty`, `Equinix`, `Global Switch`, `Iron Mountain Data Centers`, `Nabiax`, `Merlin Properties`, `Edged`, `ACS DC`, `Data Center Euskadi`, `Adequa`, `Goodman`, `Ponentia Logistics`.

---

## 5. Per-Region Enumeration Approach

### Madrid

1. Start with official cloud/colo seeds: Microsoft Spain Central, Google Cloud Madrid/Telefonica, Equinix, Digital Realty, Global Switch, Iron Mountain, Nabiax, Telefonica, Merlin/Edged.
2. Search BOCM and each municipality for urban instruments, special plans, licenses, activity declarations, first-occupation licenses, and environmental determinations.
3. Search BOE/REE for 220/400 kV substations and lines serving Getafe, Algete, Alcala de Henares, Tres Cantos, San Sebastian de los Reyes, Pinto, Fuenlabrada, Leganes, Mostoles.
4. Capacity should be accepted only from permit/electrical filings or official operator pages; marketing campus plans remain **B/C** until licensed.

### Aragon

1. Use AWS as anchor. Official AWS region is in Aragon with three AZs; Amazon/AWS and Invest in Spain identify Zaragoza and Huesca provinces.
2. Search Gobierno de Aragon PIGA pages and BOA for `Expansión Región AWS Aragón`, `Amazon Data Services Spain`, `Villanueva de Gallego`, `Huesca`, `La Puebla de Hijar`, `Azaila`, `San Mateo de Gallego`.
3. Search BOE for named substations/lines, e.g. `ACS DC LA PUEBLA`, `Penaflor 400 kV`, `SET Remota`.
4. Track support facilities separately from data halls: server assembly, logistics, AI server repair, water projects, substations, treatment plants.

### Catalonia

1. Use Generalitat strategic-project classification and Govern press releases as a lead list, then verify each project in DOGC/municipal files.
2. Search `centre de dades`, `centres de dades`, `projecte empresarial estrategic`, `pol d'implantacio`, and promoter names.
3. Anchor existing colo in Barcelona/Terrassa and Digital Realty BCN1/Sant Adria de Besos; search Barcelona-area municipalities plus Tarragona/Reus and Lleida for new large-load projects.
4. Be strict on status: Generalitat "potential projects" are **C/B** until there is DOGC, environmental, municipal, or grid evidence.

### Andalusia

1. Search BOJA and the Junta environmental prevention applications (AAU/AAI/AAUS/CA).
2. Separate public-sector CPD projects from commercial facilities. The Junta's Sevilla/La Cartuja CPD is discoverable via procurement/trade press, but should not be conflated with hyperscale colo.
3. Focus Sevilla, Malaga, Granada, Cordoba, Cadiz/Campo de Gibraltar and Almeria. Use PLACSP for public CPDs and municipal sede portals for private licenses.

### Valencian Community

1. Search DOGV and Medi Ambient territorial/project files for `centro de datos`, `edge data center`, `Proyecto de Interes Autonomico`.
2. Use `Data Center "El Lobo"` in Monforte del Cid as an official pattern: regional project folder with descriptive memory and land-use materials.
3. Search Valencia/Paterna/Riba-roja/Sagunto and Alicante/Elche/Monforte del Cid for edge and logistics-adjacent facilities.

### Basque Country

1. Search Euskadi/BOPV for environmental authorization files. `Data Center Euskadi S.L.` at Abanto-Zierbena/Ezkerraldea-Meatzaldea shows the useful pattern: company, technology park, environmental authorization, public-information notice.
2. Search Bilbao metro, Abanto-Zierbena, Zamudio/Derio technology parks, Vitoria-Gasteiz, San Sebastian/Donostia.
3. Cross-check with grid/substation notices because industrial-energy constraints are often the limiting evidence.

### Other Regions

- **Galicia**: prioritize A Coruna/Arteixo, Vigo, Santiago, coastal cable-landing infrastructure; search Galician variants.
- **Castile-La Mancha**: likely spillover from Madrid; search Toledo, Guadalajara, Alovera, Illescas, Talavera and grid substations.
- **Castile and Leon**: search Valladolid, Burgos, Leon, Palencia; watch industrial parks and renewable/grid-linked proposals.
- **Navarre/La Rioja/Murcia/Extremadura/Cantabria/Asturias/Balearic/Canary Islands**: mostly edge, public-sector CPD, telecom nodes, or renewable-linked proposals; rely on official gazettes and environmental/municipal portals.

---

## 6. Evidence and Status Rules

### 6.1 Evidence Hierarchy

| Evidence | Grade | Use |
|---|---|---|
| BOE/autonomous gazette public-information notices, environmental decisions, grid/substation authorizations, municipal license files | A | Facility/project existence, location, promoter, status, sometimes MW/MVA |
| MITECO/REE/Redeia/CNMC official rules, capacity pages, registry pages | A | Regulatory interpretation, operator validation, grid context |
| Cloud-provider official region pages | A for region existence; B for inferred facilities | Seed geography and AZ count |
| Operator official pages and investor releases | A- for existence; B for capacity/status | Facility list and commercial names |
| Spain DC association reports/pages | B | Market mapping and member universe |
| DCD/Cinco Dias/El Economista/Cadena SER/Europa Press/regional press | B | Announcements and permitting leads |
| Aggregators, maps, LinkedIn, real-estate brochures | C | Lead generation only |

### 6.2 Lifecycle Vocabulary

Spanish lifecycle terms:

```text
anuncio / memorando / acuerdo / firma / intencion = intent only
proyecto de interes autonomico / PIGA / proyecto empresarial estrategico = fast-track or strategic classification; verify permit status
informacion publica = official consultation; project is filed, not approved
autorizacion ambiental / DIA / informe de impacto ambiental = environmental approval or determination
autorizacion administrativa previa / construccion = energy/grid approval stage
licencia urbanistica / licencia de obras / declaracion responsable = municipal construction/activity permission
primera ocupacion / funcionamiento / puesta en servicio = commissioning/operation evidence
```

Status grading:
- Count **operational** only with first-occupation/operation license, operator launch, cloud region launch, or public procurement service commencement.
- Count **under construction** with building license, construction contract, final planning approval, or official start of works.
- Count **approved/planned** with environmental approval, PIGA/strategic classification, BOE public-information notice, or grid access, but keep separate from live capacity.
- Treat `inversion prevista`, `potencia solicitada`, `proyecto potencial`, and `campus plan` as non-operational.

### 6.3 Capacity Verification

- Prefer electrical facts: MVA/MW in substations, `potencia solicitada`, `capacidad de acceso`, transformer counts, and IT-load statements.
- Distinguish **grid connection MVA/MW**, **total site power**, **IT load**, and **marketing campus capacity**.
- If source gives only investment euros or hectares, do not infer MW except as a flagged estimate.
- Large Spanish announcements often aggregate all phases to 2030/2035; store phase separately and avoid counting full master-plan capacity as built.
- Watch support buildings and power infrastructure that are not data halls.

---

## 7. Recommended Official/Regulatory Workflow

1. **Seed cloud and colo universe** from AWS/Azure/Google official pages, Equinix/Digital Realty/Global Switch/Iron Mountain/Telefonica/Nabiax/Templus/Adam/operator pages, and Spain DC members.
2. **For each seed, identify legal promoter/SPV** via official press, mercantile names in gazette notices, or municipal files.
3. **Run BOE + autonomous gazette searches** for the promoter, municipality, and `centro de datos`/`CPD`.
4. **Run regional environmental portal searches** for EIA/AAU/AAI/strategic-project files.
5. **Run municipal planning/license searches** for the exact parcel/industrial estate/campus. For Madrid and Barcelona metros, municipality portals matter more than national search.
6. **Run REE/Redeia and BOE energy searches** for substations/lines feeding the project.
7. **Use PLACSP/OpenPLACSP** for public-sector CPDs and early design/EPC/UPS/cooling tenders.
8. **Fill gaps with trade press** (DCD, Cinco Dias, El Economista, regional press), then back-resolve every concrete project to an official filing where possible.
9. **Assign per-data-point grade** rather than per-project grade: a project may have **A** existence/location, **B** capacity, and **C** future phase timing.

---

## 8. Pitfalls

- `CPD` can mean a private/public server room, not a commercial datacenter; keep enterprise/public IT rooms separate unless the target registry includes them.
- `centro de datos corporativo`, government modernization contracts, UPS/cooling replacement, and managed service contracts are usually not new datacenter builds.
- Spanish sources often call a fast-track classification "approved"; this does not necessarily mean environmental approval, building license, or grid connection.
- Grid-access evidence may refer to a substation/line/SPV before the datacenter name is public; search by transformer/substation and municipality.
- Foreign cloud exact addresses are intentionally obscured; use regions/AZs only as geography seeds unless official permits identify sites.
- Aggregator facility counts are useful for leads but frequently stale or duplicate operator/campus/phase names.
