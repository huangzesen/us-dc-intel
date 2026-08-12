# ES Explorer Industry - trade press, vendors, cloud regions, and autonomous-community query patterns

Date: 2026-08-12. Scope: Spain datacenter enumeration methodology focused on Spanish colo/hyperscale operators, cloud regions, trade press, associations, public planning sources, and repeatable regional query patterns. Reliability grades: **A** = official/primary source or operator-owned current source; **B** = established trade press, association, market report, or strong secondary source requiring verification; **C** = directory/aggregator/weak secondary lead.

---

## 0. Spain-specific frame

- Spain has no single public "all data centers" registry. Enumeration should combine: **SpainDC/operator seed -> cloud-region pages -> DCD/Data Center Market/trade press -> autonomous-community strategic-project/planning portals -> BOE/regional gazettes -> municipal licensing and environmental records -> grid/power evidence**.
- Geography is no longer only Madrid/Barcelona. Start with **Community of Madrid** for live colocation and cloud-region density, **Aragon** for hyperscale/AWS/Microsoft/QTS/Tillion/Vantage/SAMCA-style campus pipelines, **Catalonia** for Barcelona/edge/colo and Mediterranean connectivity, then **Basque Country, Castile-La Mancha, Extremadura, Cantabria, Galicia, Valencian Community, Andalusia, Murcia, Canary/Balearic Islands, Ceuta** for regional campuses, AI sites, cable landing, and public-sector CPDs.
- Use Spanish and local vocabulary. Productive Spanish terms: `centro de datos`, `data center`, `datacenter`, `CPD`, `centro de procesamiento de datos`, `campus de centros de datos`, `nube`, `region cloud`, `hiperescala`, `colocation`, `colocacion`, `sala tecnica`, `licencia de obras`, `licencia urbanistica`, `declaracion responsable`, `autorizacion ambiental`, `evaluacion ambiental`, `informacion publica`, `proyecto de interes general`, `proyecto singular`, `utilidad publica`, `subestacion`, `punto de conexion`, `capacidad de acceso`, `potencia IT`, `MW`, `MWe`, `MVA`.
- Strategic-project regimes matter. In Aragon, many large projects surface as **PIGA / Plan o Proyecto de Interes General de Aragon** in `aragon.es` and `boa.aragon.es`. In Castilla-La Mancha, the Meta campus is under **PSI / Proyecto de Singular Interes** at `urbanismo.castillalamancha.es`. Other regions use `proyecto estrategico`, `interes autonomico`, `interes regional`, `declaracion de utilidad publica`, or ordinary municipal `licencia de obras`.
- Power is often the gating evidence. Search Red Electrica / CNMV / regional energy department / BOE notices for demand-access, substations, high-voltage lines, and expropriation notices. Treat announced multi-GW pipelines as leads until grid access, planning, or building-license evidence exists.
- Spain must also be checked against EU data-center reporting. MITECO explains the EU ReportENER reporting regime for data centers with installed IT electrical demand of at least 500 kW. This is **A for regulatory context**, but the reported facility-level data is confidential/public only in aggregate, so it is not yet a facility census. URL: https://www.miteco.gob.es/es/energia/eficiencia/centros-de-datos.html .

---

## 1. Source grades and URLs

### 1.1 Association, events, and market reports

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| SpainDC | https://spaindc.com/ | Main Spanish data-center association. Use for industry vocabulary, annual reports, Madrid/Spain capacity framing, events, and member/operator leads. Not a public facility registry. | B |
| SpainDC annual/Madrid reports | `site:spaindc.com/wp-content/uploads/ informe anual centros de datos`, `site:spaindc.com Madrid data center informe` | Market geography, installed/pipeline capacity estimates, named operator context. Verify facilities with operator/planning sources. | B |
| DCD company profile for SpainDC | https://www.datacenterdynamics.com/en/company/spaindc/ | Confirms SpainDC role and current membership scale/sector position. | B |
| Data Centre World / Tech Show Madrid | https://www.techshowmadrid.es/ | Events, sponsor/exhibitor/operator leads, SpainDC report summaries. Good for current ecosystem actors. | B/C |
| Datacloud Global Congress SpainDC partner page | https://www.datacloudglobalcongress.com/partners-1/spain-dc | Confirms SpainDC as national association and value-chain actor. | B |
| CBRE/JLL/Colliers/Cushman/Proequity/Cundall/Watson Farley reports | Example: https://www.colliers.com/es-es/services/data-centers ; https://www.cbre.es/insights/reports/data-centers-europe-q1 ; https://www.wfw.com/articles/data-centres-an-international-legal-and-regulatory-perspective-spotlight-on-spain/ | Market sizing, cluster ranking, regulatory/real-estate context. Use for prioritization, not facility truth. | B/C |
| DataCenterMap / Datacenters.com / Baxtel / PeeringDB | https://www.datacentermap.com/spain/ ; https://www.datacenters.com/locations/spain ; https://baxtel.com/data-centers/spain ; https://www.peeringdb.com/ | Fast address/operator aliases, IXP/facility discovery, smaller regional sites. Never final evidence alone. | C/C+ |

### 1.2 Trade press

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics Spain tag | https://www.datacenterdynamics.com/en/tags/spain/ and Spanish search `site:datacenterdynamics.com/es/noticias España "centro de datos"` | Best international trade source for Spanish operator announcements, hyperscale campuses, construction status, M&A, cloud-region news, and regional pipelines. | B |
| Data Center Market | https://www.datacentermarket.es/ ; `site:datacentermarket.es "centro de datos" España {region|operator}` | Strong Spanish-language sector press. Useful for Madrid/Barcelona/Aragon market commentary, operator interviews, sustainability/power issues, and regional announcements. | B |
| El Economista / Cinco Dias / Expansion / El Pais / local business press | `site:eleconomista.es centro de datos {operator}`, `site:cincodias.elpais.com centros de datos España`, `site:expansion.com centro de datos {region}` | Good for large investment announcements, grid-access debates, real-estate developers, and public controversy. Verify permits elsewhere. | B-/C+ |
| Regional press | `Heraldo de Aragon`, `El Periodico de Aragon`, `La Vanguardia`, `Ara`, `Valencia Plaza`, `Murcia Plaza`, `Hoy Extremadura`, `La Voz de Galicia`, `El Correo`, `Diario de Sevilla`, `Canarias7` | Often names municipality, industrial estate, mayoral statements, licensing phase, and local opposition before official portals are indexed. | B-/C+ |
| Construction/legal/real-estate sources | `EjePrime`, `Iberian Property`, `BeBeez`, `DLA Piper`, `Sener/Quark`, `IDOM`, `AECOM` | Useful for developer/project names, design contracts, site-area/power claims, and legal closing announcements. Verify with planning/operator evidence. | B/C |

### 1.3 Official/public-record surfaces

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| BOE | https://www.boe.es/buscar/ | National official notices. Search for expropriations, power lines, substations, environmental authorizations, public information notices, and state public-sector CPDs. | A |
| Regional gazettes | Examples: BOA https://www.boa.aragon.es/ ; BOCM https://www.bocm.es/ ; DOGC https://dogc.gencat.cat/ ; DOCM https://docm.jccm.es/ ; DOE https://doe.juntaex.es/ ; BOPV https://www.euskadi.eus/bopv2 ; DOG https://www.xunta.gal/diario-oficial-galicia | Core primary evidence. Search Spanish terms plus operator/project names. | A |
| Aragon PIGA portal | https://www.aragon.es/urbanismo-y-ordenacion-del-territorio/planes-y-proyectos-de-interes-para-aragon-pigas | Essential for AWS/Microsoft/QTS/Tillion/Vantage/SAMCA/ACS-style Aragon projects. Includes plans/projects of general interest and links to BOA orders. | A |
| Castilla-La Mancha PSI portal | https://urbanismo.castillalamancha.es/planeamiento/planeamiento-territorial/proyectos-de-singular-interes/meta-data-center-campus | Primary model for Meta/Talavera. Search `site:urbanismo.castillalamancha.es "data center"` and `PSI`. | A |
| MITECO environmental/public participation | https://www.miteco.gob.es/ and public participation pages | National environmental context and EU reporting rules; use for state-level environmental files where applicable. | A |
| Autonomous environmental portals | Examples: INAGA Aragon https://www.aragon.es/-/instituto-aragones-de-gestion-ambiental-inaga ; Generalitat Catalunya environment search; Junta de Andalucia environmental authorization; Comunidad de Madrid environment; Xunta environmental evaluation | Find `evaluacion de impacto ambiental`, `autorizacion ambiental integrada`, generator emissions, water, and public-information files. | A |
| Municipal planning/licensing portals | `site:{ayuntamiento}.es "centro de datos" "licencia de obras"` and local e-sede/urbanismo pages | Best source for small/medium projects and final construction license status. | A/B depending on document |
| CNMV filings | https://www.cnmv.es/ | Public-company notices: Solaria grid-demand announcements, Merlin data-center plan updates, REIT/infrastructure disclosures. | A |
| Red Electrica / e-distribucion / Iberdrola / Naturgy / UFD / Endesa references | https://www.ree.es/ plus distribution-company connection notices where public | Grid capacity and substation evidence. Often necessary to distinguish credible campus from land-banking. | A/B |

---

## 2. Core Spain query templates

### 2.1 Broad facility and project discovery

```text
("centro de datos" OR "data center" OR datacenter OR CPD OR "centro de procesamiento de datos") ("España" OR "{comunidad}" OR "{provincia}" OR "{municipio}") ("MW" OR MVA OR "potencia IT" OR "potencia instalada" OR "subestacion")
("{operator}" OR "{developer}") ("centro de datos" OR "data center" OR datacenter) ("España" OR "{region}" OR "{municipio}")
"campus de centros de datos" ("España" OR "{region}" OR "{municipio}")
"hiperescala" "centro de datos" "{region}"
"centro de datos" "{poligono industrial}" "{municipio}"
```

### 2.2 Official planning / permitting

```text
site:boe.es ("centro de datos" OR "data center" OR datacenter OR "centro de procesamiento de datos") "{municipio}"
site:{regional-gazette-domain} ("centro de datos" OR "data center" OR datacenter) ("informacion publica" OR "licencia" OR "autorizacion" OR "evaluacion ambiental" OR "utilidad publica")
site:{ayuntamiento-domain} ("centro de datos" OR "data center" OR CPD) ("licencia de obras" OR "licencia urbanistica" OR "junta de gobierno" OR "pleno")
site:{regional-urbanismo-domain} ("centro de datos" OR "data center" OR datacenter) ("proyecto de interes" OR "plan especial" OR "proyecto singular")
site:{regional-environment-domain} ("centro de datos" OR "data center" OR CPD) ("evaluacion ambiental" OR "autorizacion ambiental" OR "informacion publica")
```

### 2.3 Grid, energy, and land evidence

```text
("{operator}" OR "{project}") ("subestacion" OR "punto de conexion" OR "capacidad de acceso" OR "permiso de acceso" OR "Red Electrica")
"centro de datos" "{region}" ("subestacion" OR "linea electrica" OR "evacuacion" OR "MVA" OR "MW")
site:boe.es "centro de datos" "linea electrica"
site:cnmv.es ("centro de datos" OR "DPC" OR "data center") ("MW" OR "Red Electrica" OR "conexion")
"centro de datos" "agua" "{municipio}" OR "consumo de agua" "{project}"
```

### 2.4 Trade press and operator triangulation

```text
site:datacenterdynamics.com Spain "data center" {operator OR municipality OR region}
site:datacenterdynamics.com/es/noticias "centro de datos" {operator OR municipio OR comunidad}
site:datacentermarket.es "centro de datos" {operator OR municipio OR comunidad}
site:spaindc.com {operator} "data center"
site:datacentermap.com/spain {municipio} datacenter
site:baxtel.com "Spain" "{operator}" "data center"
site:peeringdb.com/fac "{operator}" "{city}"
```

### 2.5 Spanish lifecycle/status vocabulary

- **Lead only**: `anuncia`, `plantea`, `previsto`, `preve`, `memorando`, `MOU`, `acuerdo`, `protocolo`, `reserva de suelo`, `opcion de compra`, `busca socio`, `en estudio`.
- **Planning/permit evidence**: `aprobacion inicial`, `aprobacion definitiva`, `informacion publica`, `licencia de obras`, `licencia urbanistica`, `declaracion de impacto ambiental`, `evaluacion ambiental simplificada`, `autorizacion ambiental integrada`, `PIGA`, `PSI`, `proyecto de interes regional`, `declaracion de interes autonomico`, `declaracion de utilidad publica`.
- **Construction**: `inicio de obras`, `primera piedra`, `adjudicacion`, `obra civil`, `ejecucion`, `fase final`, `puesta en marcha`.
- **Operational**: `inaugura`, `operativo`, `en servicio`, operator facility page live, Uptime certificate, PeeringDB active facility, cloud region GA/open.
- **Rejected/canceled/stale**: `desistimiento`, `retirada`, `denegado`, `caducidad`, `archivo`, `suspension`, `anulado`, `sin capacidad de acceso`, old announcement with no later permit/grid evidence.

---

## 3. Major operators, developers, and vendor pivots

Official operator pages are **A for marketed existence/current site**, **B for capacity and expansion claims** unless backed by filings, utility agreements, or official planning records.

| Operator/developer | Official URL / lead URL | Spanish pivots | Notes |
|---|---|---|---|
| Digital Realty / Interxion | https://www.digitalrealty.com/data-centers/emea/madrid | Madrid, MAD1-MAD5, Julian Camarillo/MaDBit | Digital Realty is the successor brand for Interxion. Search both names, especially older Madrid records. |
| Equinix | https://www.equinix.com/data-centers/europe-colocation/spain-colocation ; Madrid https://www.equinix.com/data-centers/europe-colocation/spain-colocation/madrid-data-centers ; Barcelona https://www.equinix.com/data-centers/europe-colocation/spain-colocation/barcelona-data-centers | Madrid MD sites, Barcelona BA1/BA2, Alcobendas, L'Hospitalet | Strong official site pages for live colocation. xScale/leased sites need local verification. |
| DATA4 | https://www.data4group.com/en/data-center-in-madrid-spain-2/ | Alcobendas, San Agustin del Guadalix, MAD01/MAD02 | Official page gives Madrid campus land/power context; verify new campus permits locally/regionally. |
| Nabiax | https://nabiax.com/en/our-data-centers/spain/alcala-data-center/ ; contact pages list Alcala, Julian Camarillo, Terrassa | Alcala de Henares, Julian Camarillo/Madrid, Terrassa | Telefonica/ProA/ACI-style legacy records may use earlier entity names. |
| Merlin Properties / Edged | https://www.merlinproperties.com/en/assets/data-center-madrid-getafe/ ; https://ir.merlinproperties.com/en/new-opportunity-in-data-centers/ | Madrid-Getafe, Barcelona, Bilbao-Arasur, Extremadura, Plan MEGA | CNMV and Merlin IR are A-grade for corporate status; local permits still needed for site-level lifecycle. |
| Iron Mountain Data Centers | https://www.ironmountain.com/data-centers/locations/madrid-data-center | San Fernando de Henares / MAD-1 | Search XData Properties for older filings. |
| NTT Global Data Centers | https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/emea | Madrid, Spain press/SpainDC membership | Official Spanish facility pages may move; DCD/SpainDC/event pages help seed. |
| Prime Data Centers | https://primedatacenters.com/locations/madrid/ | Alcobendas/MAD01 | Operator page is useful for intended capacity and development status; confirm with Madrid municipal/regional files. |
| Vantage Data Centers | https://vantage-dc.com/data-center-locations/emea/ | Aragon/Villanueva de Gallego, Madrid leads if any | Aragon PIGA/BOA records are primary for local status. |
| QTS / Blackstone | https://q.com/data-centers/calatorao-en/ | Calatorao, Zaragoza province | Official page plus Aragon planning/gazette records. |
| Tillion Data Centres / Azora | https://tilliondc.com/en/locations/spain/zaragoza/ ; https://www.azora.com/en/blog/azora-to-invest-e2-billion-in-zaragoza-data-centre/ | Zaragoza, Tillion campus | Cross-check BOA/PIGA and grid notices. |
| AWS | https://aws.amazon.com/local/spain/ ; https://www.aboutamazon.eu/news/job-creation-and-investment/amazon-investment-spain-2026 | Aragon: Huesca, Zaragoza, Teruel, Villanueva/San Mateo/Azaila/La Puebla de Hijar/Pina/Burgo-style AWS clusters | Official for region/investment; exact sites require PIGA/BOA/local evidence. |
| Microsoft | Spain local https://local.microsoft.com/communities/emea/spain/ ; Aragon local https://local.microsoft.com/blog/understanding-microsoft-datacenters-in-aragon/ ; Madrid cloud-region news https://news.microsoft.com/source/emea/2024/06/microsoft-opens-its-first-cloud-region-in-spain-to-accelerate-the-development-of-the-ai-economy/ | Community of Madrid cloud region, Greater Madrid datacenters, Aragon campuses | Official for region/project frame; use PIGA/municipal docs for exact campus status. |
| Google Cloud | Madrid region news https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-in-madrid-spain-now-open ; locations https://cloud.google.com/about/locations | Madrid cloud region `europe-southwest1` | A for logical cloud region, C for exact facility inference. |
| Oracle Cloud Infrastructure | public regions https://www.oracle.com/cloud/public-cloud-regions/ ; Madrid region release notes https://docs.oracle.com/iaas/releasenotes/changes/590680ed-b19c-43cb-9713-69bf87b09e27/index.htm ; Madrid 3 https://docs.oracle.com/iaas/releasenotes/oci/new-region-madrid-3.htm | Spain Central / Madrid regions | A for OCI region existence; exact data centers are not public facility evidence. |
| Templus | https://templus.com/ | Malaga, Seville, Ceuta, Barcelona/bitNAP | Spanish regional edge/colo operator; official site plus DCD/Data Center Market. |
| Aire Networks / Grupo Aire / OASIX / Stackscale | https://airetech.es/ ; https://www.stackscale.com/data-centers/ | Madrid, Malaga, Toledo, Canary Islands/Las Palmas, Valencia | Good for smaller regional cloud/colo nodes. Verify addresses with operator pages and directories. |
| ADI Data Center Euskadi | Uptime client page and Basque project pages; search `Atlantic Data Infrastructure ADI Data Center Euskadi` | Bizkaia, Gipuzkoa/Garaia, Basque Country | Regional public-private venture; use Basque tech park and BOPV/local records. |
| Solaria | https://solariaenergia.com/ and CNMV filings | Basque Country/other grid-demand announcements | Grid connection announcements are strong leads but may precede site/permitting. |
| Nostrum Data Centers / Ingenostrum | https://www.ingenostrum.com/ and DCD/Spaindc reports | Badajoz, Caceres, Guadalajara, Galicia | Verify with regional strategic-project status, land, power, and municipal licenses. |
| Sener/Quark, IDOM, AECOM | https://www.group.sener/en/ ; https://www.idom.com/ ; https://aecom.com/ | Design evidence for Altamira, Campus Data Navarra, Nostrum, etc. | Engineering appointment is B/A- for project reality; not construction status alone. |
| Local telecom/ISP operators | Arsys, Sarenet, Kumo, Adam, bitNAP legacy, Infotelecom, IslaLink, Canalink/D-ALiX, Telefonica Tech, Vodafone, Orange, Hispaweb, inAsset/NixMad | Regional facilities, islands, public/enterprise CPDs | Operator page + Uptime/PeeringDB + municipal record is the best validation stack. |

---

## 4. Hyperscaler/cloud region handling

Cloud-region pages are **A for logical region existence and general metro/region**, not exact facility address. Do not create physical facility records only from a logical region unless the cloud provider, operator, incident report, planning file, or public notice identifies a site.

| Provider | Spain signal | URL | Grade |
|---|---|---|---|
| AWS | Europe (Spain) Region in Aragon; official Spain pages describe major investment and expansion through 2035. | https://aws.amazon.com/local/spain/ ; https://www.aboutamazon.eu/news/job-creation-and-investment/amazon-investment-spain-2026 | A region/investment; C facility mapping until PIGA/local evidence |
| Microsoft Azure | Spain Central / Microsoft first Spain cloud region in Community of Madrid; Microsoft local pages for Greater Madrid and Aragon datacenters. | https://news.microsoft.com/source/emea/2024/06/microsoft-opens-its-first-cloud-region-in-spain-to-accelerate-the-development-of-the-ai-economy/ ; https://local.microsoft.com/communities/emea/spain/ ; https://local.microsoft.com/blog/understanding-microsoft-datacenters-in-aragon/ | A region/project; C exact facility |
| Google Cloud | Madrid region `europe-southwest1` opened in 2022; current locations page lists region/zones. | https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-in-madrid-spain-now-open ; https://cloud.google.com/about/locations ; https://docs.cloud.google.com/compute/docs/regions-zones | A region; C facility |
| Oracle Cloud | Spain Central Madrid regions, including `eu-madrid-1` and later Madrid region release notes such as `eu-madrid-3`. | https://www.oracle.com/cloud/public-cloud-regions/ ; https://docs.oracle.com/iaas/releasenotes/changes/590680ed-b19c-43cb-9713-69bf87b09e27/index.htm ; https://docs.oracle.com/iaas/releasenotes/oci/new-region-madrid-3.htm | A region; C facility |
| IBM / local sovereign cloud / Telefonica Tech / Kyndryl / OVHcloud / local clouds | Search current provider region pages and Spanish operator sites. | Provider official pages | A/B depending on source |

Cloud pivot queries:

```text
"{provider}" "Spain" "cloud region" "data center"
"{provider}" "España" "region cloud" "centro de datos"
"{provider}" "Madrid" "cloud region" "data center"
"{provider}" "Aragon" "datacenter" OR "centro de datos"
"{provider}" "{municipio}" "PIGA" OR "licencia de obras"
```

---

## 5. Autonomous-community enumeration method

Run each region as:

1. **Operator/association seed (B/C -> A)**: SpainDC, DCD, Data Center Market, DataCenterMap/Baxtel/PeeringDB, operator pages.
2. **Official strategic-project pass (A)**: regional urbanism/economy/environment portals, regional gazette, BOE, and municipal council/licensing records.
3. **Grid/power pass (A/B)**: BOE/regional public-information notices, Red Electrica, distribution-company references, CNMV notices for listed companies, substation/high-voltage-line terms.
4. **Municipal validation (A)**: once a municipality or industrial estate is known, search town-hall `urbanismo`, `licencia de obras`, `junta de gobierno`, `pleno`, `contratacion`, and `sede electronica`.
5. **Status discipline**: announcements without permit/grid evidence stay `planned/lead`; regional strategic-project approval can be `approved`; construction needs work award/groundbreaking/progress evidence; operational needs operator live page, Uptime/PeeringDB active signal, official inauguration, or cloud GA where logical-only.

### 5.1 Regional query matrix

| Division | Local names / pivots | Major operators/projects to pivot | Query templates |
|---|---|---|---|
| Andalusia | `Andalucia`, `Malaga`, `Sevilla`, `Cordoba`, `Cadiz`, `Algeciras`, `PICA`, `Malaga TechPark` | Templus Malaga/Seville, Aire/OASIX Malaga, cable/edge sites, public-sector CPDs | `site:juntadeandalucia.es "centro de datos" "autorizacion ambiental"`; `site:boja.junta-andalucia.es "centro de datos"`; `site:malaga.eu "centro de datos" "licencia"`; `site:sevilla.org "centro de datos" PICA`; `"Malaga" "data center" Aire OR Templus`; `"Sevilla" "centro de datos" Templus`. |
| Aragon | `Aragon`, `Aragon`, `Zaragoza`, `Huesca`, `Teruel`, `El Burgo de Ebro`, `Villanueva de Gallego`, `San Mateo de Gallego`, `La Muela`, `Calatorao`, `La Puebla de Alfinden`, `La Puebla de Hijar`, `Azaila` | AWS, Microsoft, QTS/Blackstone, Tillion/Azora, Vantage, SAMCA, ACS DC Infra | `site:aragon.es "centro de datos" PIGA`; `site:boa.aragon.es "centro de datos" "Proyecto de Interes General de Aragon"`; `site:boa.aragon.es "campus de centro de datos"`; `site:inaga.aragon.es "centro de datos"`; `"centro de datos" "La Muela" BOA`; `"AWS" Aragon "centro de datos" PIGA`; `"Microsoft" "Villamayor de Gallego" "centro de datos"`; `"QTS" Calatorao "centro de datos"`. |
| Principality of Asturias | `Asturias`, `Oviedo`, `Gijon`, `Aviles`, `Salas`, `Nonaya`, `Digital Valley Asturias` | Digital Valley Asturias / S4U, regional edge/AI projects | `site:asturias.es "centro de datos" "evaluacion ambiental"`; `site:sedemovil.asturias.es "centro de datos"`; `site:ayto-salas.es "centro de datos" licencia`; `"Digital Valley Asturias" Salas "centro de datos"`; `"Nonaya" "data center"`. |
| Cantabria | `Cantabria`, `Santander`, `Marina de Cudeyo`, `Altamira`, `Stoneshield`, `XDC Properties` | Altamira Data Center, Stoneshield/XDC, Sener/Quark | `site:cantabria.es "centro de datos" "informacion publica"`; `site:boc.cantabria.es "centro de datos"`; `"Altamira Data Center" Cantabria`; `"Stoneshield" Cantabria "data center"`; `"centro de datos" Santander "licencia"`. |
| Ceuta | `Ceuta`, `Puerto de Ceuta`, `Puntilla` | Templus CEU01, submarine/edge facilities | `site:ceuta.es "centro de datos" licencia`; `site:boe.es "Ceuta" "centro de datos"`; `site:puertodeceuta.com "centro de datos"`; `"Templus" Ceuta "centro de datos"`; `"CEU01" Ceuta datacenter`. |
| Castile and Leon | `Castilla y Leon`, `Valladolid`, `Torrelobaton`, `Soria`, `Los Royales`, `Leon`, `Burgos`, `Salamanca` | DC Mudarra, Social Security CPD Soria, public/HPC/edge sites | `site:jcyl.es "centro de datos" "evaluacion ambiental"`; `site:bocyl.jcyl.es "centro de datos"`; `site:torrelobaton.ayuntamientosdevalladolid.es "centro de datos"`; `"DC Mudarra" Torrelobaton`; `"Seguridad Social" Soria "centro de procesamiento de datos"`; `"Los Royales" Soria CPD`. |
| Castile-La Mancha | `Castilla-La Mancha`, `Toledo`, `Talavera de la Reina`, `Torrehierro`, `Mora`, `Guadalajara`, `Malpica`, `Azuqueca` | Meta/Zarza Networks, EdgeMode/DC Malpica AI, Nostrum GUA1, Fortinet, OASIX Toledo | `site:urbanismo.castillalamancha.es "Data Center Campus"`; `site:docm.jccm.es "centro de datos"`; `site:castillalamancha.es "centro de datos" "Proyecto de Singular Interes"`; `site:talavera.es "Meta Data Center Campus"`; `"Mora" Toledo "centro de datos" "MOU"`; `"Nostrum" Guadalajara GUA1`. |
| Canary Islands | `Canarias`, `Tenerife`, `Granadilla`, `D-ALiX`, `Las Palmas`, `Gran Canaria`, `Canalink`, `ITER` | D-ALiX/ITER/Canalink, Telefonica Tech VDC node, Aire/OASIX Las Palmas | `site:gobiernodecanarias.org "centro de datos" "evaluacion ambiental"`; `site:boe.es "Canarias" "centro de datos"`; `site:tenerife.es "D-ALiX"`; `site:iter.es "D-ALiX"`; `"Las Palmas" "OASIX" "data center"`; `"Telefonica Tech" "Canary Islands" "Virtual Data Center"`. |
| Catalonia | `Catalunya`, `Catalonia`, `Barcelona`, `L'Hospitalet de Llobregat`, `Terrassa`, `La Maquinista`, `Sant Adria`, `Zona Franca`, `Cerdanyola`, `Mataro` | Equinix BA1/BA2, Nabiax Terrassa, Templus/bitNAP, Merlin/Edged Barcelona, Ark Barcelona, Adam, local Barcelona colo | `site:dogc.gencat.cat "centre de dades" OR "centro de datos"`; `site:gencat.cat "centre de dades" "avaluacio ambiental"`; `site:ajuntament.barcelona.cat "centre de dades" "llicencia"`; `site:l-h.cat "data center" OR "centre de dades"`; `"Equinix" "BA2" Barcelona`; `"Ark Data Centres" "La Maquinista"`; `"bitNAP" Barcelona "Templus"`. |
| Extremadura | `Extremadura`, `Badajoz`, `Caceres`, `Navalmoral de la Mata`, `Valdecaballeros`, `Plataforma Logistica Badajoz` | Nostrum Evergreen/BAZ-01, Ingenostrum CC Green Caceres, Merlin/Edged AI campuses | `site:juntaex.es "centro de datos" "proyecto estrategico"`; `site:doe.juntaex.es "centro de datos"`; `site:aytobadajoz.es "centro de datos" licencia`; `"Nostrum Evergreen" Badajoz`; `"BAZ-01" "centro de datos"`; `"Merlin" Edged Extremadura "data center"`; `"Valdecaballeros" "centro de datos"`. |
| Galicia | `Galicia`, `Santiago de Compostela`, `A Sionlla`, `A Coruna`, `Vigo`, `CESGA`, `Impulsa Galicia` | Nostrum/Ingenostrum Galicia, CESGA datacenter, Xunta CPD | `site:xunta.gal "centro de datos" "A Sionlla"`; `site:xunta.gal "centro de procesamento de datos"`; `site:dog.xunta.gal "centro de datos"`; `site:santiagodecompostela.gal "centro de datos" licencia`; `"CESGA" "nuevo datacenter"`; `"Impulsa Galicia" Ingenostrum "centro de datos"`. |
| Balearic Islands | `Illes Balears`, `Islas Baleares`, `Mallorca`, `Palma`, `Marratxi`, `Son Castello`, `Menorca`, `Mao`, `Ciutadella`, `IslaLink` | Infotelecom, Vodafone Marratxi, IslaLink Palma/Mallorca cable landing colo | `site:caib.es "centre de dades" OR "centro de datos"`; `site:boib.caib.es "centro de datos"`; `site:palma.cat "centro de datos" "licencia"`; `site:marratxi.es "data center" Vodafone`; `"Infotelecom" Palma "centro de datos"`; `"IslaLink" Palma "colocation"`. |
| Region of Murcia | `Murcia`, `Cartagena`, `Espinardo`, `Escombreras`, `Alcantarilla`, `Kumo`, `ITRES` | Grupo Fotones/Casiopeia, Cartagena Data Green, Kumo Murcia, ITRES | `site:carm.es "centro de datos" "evaluacion ambiental"`; `site:borm.es "centro de datos"`; `site:murcia.es "centro de datos" "licencia"`; `site:cartagena.es "centro de datos" "Escombreras"`; `"Grupo Fotones" Murcia "centro de datos"`; `"Cartagena Data Green"`; `"ITRES" Alcantarilla "data center"`. |
| Community of Madrid | `Comunidad de Madrid`, `Madrid`, `Alcala de Henares`, `Alcobendas`, `San Fernando de Henares`, `Getafe`, `San Agustin del Guadalix`, `Julian Camarillo`, `MaDBit`, `Tres Cantos`, `Valdelacasa` | Digital Realty/Interxion, Equinix, DATA4, Nabiax, Iron Mountain, Merlin/Edged, Prime, Microsoft, Google Cloud, Oracle, NTT, Iberdrola/Echelon, Ferrovial | `site:bocm.es "centro de datos"`; `site:comunidad.madrid "centro de datos" "evaluacion ambiental"`; `site:madrid.es "centro de datos" "licencia"`; `site:alcobendas.org "centro de datos"`; `site:ayto-alcaladehenares.es "centro de datos"`; `site:getafe.es "data center" Merlin`; `"Julian Camarillo" "centro de datos"`; `"Madrid Sur" Iberdrola "data center"`; `"Valdelacasa" Ferrovial "data center"`. |
| Melilla | `Melilla` | likely telecom/government server rooms, no major public colo pipeline found in quick industry pass | `site:melilla.es "centro de datos"`; `site:boe.es "Melilla" "centro de datos"`; `site:contrataciondelestado.es Melilla CPD`; `"Melilla" "data center" OR CPD`; `"Melilla" "sala de servidores"`. Treat directory-only leads as C. |
| Chartered Community of Navarre | `Navarra`, `Navarre`, `Pamplona`, `Cendea de Cizur`, `Gazolaz`, `Campus Data Navarra` | Campus Data Navarra, Grupo VDR, Sener/Quark | `site:navarra.es "centro de datos" "informacion publica"`; `site:bon.navarra.es "centro de datos"`; `site:cizur.es "centro de datos"`; `"Campus Data Navarra" Gazolaz`; `"Quark" "Campus Data Navarra"`; `"Sener" Navarra "data center"`. |
| Basque Country | `Euskadi`, `Pais Vasco`, `Bizkaia`, `Gipuzkoa`, `Araba`, `Bilbao`, `Vitoria-Gasteiz`, `Arasur`, `Derio`, `Zamudio`, `Garaia`, `Arrasate`, `Mondragon` | Merlin/Edged Bilbao-Arasur, ADI Data Center Euskadi, Sarenet Derio, Solaria grid-demand lead | `site:euskadi.eus "centro de datos" OR "datu zentro"`; `site:euskadi.eus/bopv2 "centro de datos"`; `site:parke.eus "data centre" Sarenet`; `site:ptgaraia.eus ADI "centro de datos"`; `"Merlin" "Arasur" "data center"`; `"Solaria" "225 MW" "Basque Country" "data centers"`. |
| La Rioja | `La Rioja`, `Logrono`, `Arsys`, `Calahorra` | Arsys Logrono, smaller regional hosting/public CPDs | `site:larioja.org "centro de datos"`; `site:bor.larioja.org "centro de datos"`; `site:logrono.es "centro de datos" licencia`; `"Arsys" Logrono "data center"`; `"La Rioja" CPD "centro de procesamiento de datos"`. |
| Valencian Community | `Comunitat Valenciana`, `Comunidad Valenciana`, `Valencia`, `Paterna`, `Vara de Quart`, `Alicante`, `Castellon`, `NXN`, `Kumo`, `Nethits` | NXN-VLC1/Nethits, Kumo Paterna/Valencia, regional cloud/telecom nodes | `site:gva.es "centro de datos" "evaluacion ambiental"`; `site:dogv.gva.es "centro de datos"`; `site:valencia.es "centro de datos" "licencia"`; `site:paterna.es "data center" OR "centro de datos"`; `"NXN-VLC1" Valencia`; `"Vara de Quart" "centro de datos"`; `"Kumo" Paterna "data center"`. |

---

## 6. Fast validation checklist

1. **Normalize geography**: store the manifest autonomous community/autonomous city, but search Spanish, Catalan, Basque, Galician, and local municipality names where relevant.
2. **Confirm operator identity**: watch rebrands/acquisitions such as Interxion -> Digital Realty, bitNAP -> Templus, XData -> Iron Mountain, Telefonica assets -> Nabiax-style records, local ISP brands under Grupo Aire/OASIX/Stackscale.
3. **Separate logical regions from physical sites**: AWS/Microsoft/GCP/OCI pages prove regions, not facility addresses.
4. **Classify permit maturity**: `PIGA/PSI/declaracion de interes` is not always construction; check final approval, building license, grid access, construction award, and operational evidence.
5. **Grid discipline**: for >20 MW projects, require at least one power-access, substation, BOE/regional-gazette, operator, or investor filing before treating capacity as more than an announcement.
6. **Capacity units**: prefer operator IT MW. Mark `MWe`, total electrical MW, `MVA`, or campus maximum separately and do not convert without noting the caveat.
7. **Avoid double-counting Madrid/Barcelona branding**: Madrid-branded sites may be in Alcobendas, Alcala de Henares, Getafe, San Fernando de Henares, or San Agustin del Guadalix; Barcelona-branded sites may be in L'Hospitalet, Terrassa, Zona Franca, or other metro municipalities.
8. **Use directories as leads only**: DataCenterMap/Baxtel/Datacenters.com can expose small sites and addresses, but need operator, PeeringDB, Uptime, municipal, or official corroboration.
