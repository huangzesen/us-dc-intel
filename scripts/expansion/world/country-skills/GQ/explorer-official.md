# GQ Explorer Official - Equatorial Guinea Datacenter Enumeration

Date: 2026-08-12. Country: **GQ - Equatorial Guinea / Republic of Equatorial Guinea** (`Republica de Guinea Ecuatorial`). Target division model for this explorer: the **2 manifest regions**: Continental (Rio Muni mainland); Insular (Bioko + Annobon islands).

Administrative note: the official 8-province structure maps into the 2 manifest regions as follows. **Continental** (Rio Muni) = Litoral (Bata, Machinda, Cogo), Centro Sur (Evinayong, Niefang), Kie-Ntem (Ebebiyin, Micomeseng), Wele-Nzas (Mongomo, Anisok), and Djibloho (Oyala/Ciudad de la Paz). **Insular** = Bioko Norte (Malabo, national capital), Bioko Sur (Luba, Riaba), and Annobon (San Antonio de Pale), plus the Corisco islands (Mandji cable). Store all results under the 2 requested manifest divisions; use province/city names only as search anchors.

Language note: search in Spanish first (only Spanish-speaking country in Africa), then French/English for official and donor documents. High-yield terms: `centro de datos`, `data center`, `datacenter`, `coubicación`, `coubicacion`, `colocation`, `sala de servidores`, `servidores`, `hébergement`, `hebergement`, `centre de données`, `centre de donnees`, `nube soberana`, `soberanía digital`, `fibra óptica`, `cable submarino`, `estación de aterrizaje`, `punto de intercambio`, `IXP`, `Tier III`, `licitación`, `appel d'offres`, `informatización`, `CNIAPGE`, `GITGE`, `ORTEL`, `PAMFP`, `SEGESA`, `Minsait`, `Mandji`, `Ceiba`, `ACE`, `Ultramar GE`, `Annobón`.

Reliability grades used in this file:
- **A** = primary or official for the fact asserted: GITGE official pages/annual reports, government press (guineaecuatorialpress.com), ministry/regulator statements, CNIAPGE board records, official donor project pages (PAMFP, AfDB), official cloud-region pages, ISOC Pulse tracker, Journal Officiel/government legal act.
- **B** = strong secondary or party-primary commercial evidence: Agence Ecofin/Revista Ecofin EG, AhoraEG, guineaInfomarket, Real Equatorial Guinea, Digital Business Africa, DCD, Telecompaper, French Treasury sector note, local press quoting named officials, vendor press releases for that vendor's own contract scope (e.g. Minsait/Indra).
- **C** = lead only: directories (DataCenterMap, DataCenterPlatform, DataCentersList, colo.exchange, Inflect), PeeringDB user-maintained entries, market reports, social posts, unquoted vendor claims, ambiguous hosting/cloud claims, policy-only statements.

## 0. Ground Rules

- There is **no public national datacenter registry** for Equatorial Guinea. Build the inventory by joining official telecom-infrastructure evidence (GITGE), government informatization records (CNIAPGE), donor procurement (PAMFP/AfDB), cable-landing evidence, energy/permit clues, and trade press.
- Disambiguate from Guinea (Conakry), Guinea-Bissau, and the DRC/Congo every time. GQ evidence normally says Malabo, Bata, Bioko, Rio Muni, Annobon, GITGE, GETESA, CNIAPGE, PAMFP, or `Guinea Ecuatorial`. Guinea-Conakry evidence says Conakry or `Guinee`. Do not merge.
- Count physical facilities, not policy objectives, corporate offices, generic cloud services, tower sites, cable landing points, or telco POPs. A facility record needs physical siting or facility language such as data center, racks, technical rooms, white space, colocation/coubicacion, IXP host, Tier design/certification, launch, construction, or commissioning.
- **Be honest about yields**: this is a tiny market (population ~1.9M, one international cable, no public IXP, no hyperscale region). Expect roughly 3-6 records nationwide if internal government/utility facilities are included, and fewer if counting only public colocation; do not inflate with landing stations, operator offices, or ministerial server rooms that are not named as datacenters.

## 1. Official and Regulatory Sources

### 1.1 GITGE - Gestor de Infraestructuras de Telecomunicaciones de Guinea Ecuatorial (state telecom infrastructure manager)

Use first for every national backbone, cable, and colocation question. GITGE is the state company that owns/manages the public telecom infrastructure (created by Decreto Presidencial 44/2011, 26 Jan 2011) and is the operator of record behind the Sipopo datacenter and all submarine landings.

Verified URLs:
- Homepage: https://gitge.com/
- Infrastructure overview (ACE, SAIL, Ceiba-1, Ceiba-2, Ultramar GE, Mandji, RNFO): https://gitge.com/infraestructuras/
- Colocation service page (`Coubicacion`): https://gitge.com/servicios/coubicacion/
- Colocation service brochure PDF: https://gitge.com/wp-content/uploads/2025/08/coubicacion-brochure.pdf
- Annual report 2024 (PDF, large): https://gitge.com/wp-content/uploads/2025/09/informe-anual-2024.pdf
- Contact: https://gitge.com/contacto/
- PeeringDB org 17440 / AS37529: https://www.peeringdb.com/org/17440

Use GITGE pages as **A** for: existence of state infrastructure, cable systems and landing points, the colocation service offering, IP transit/Ethernet/FTTH services, and GITGE's role. Do not use the colocation page alone to claim a specific datacenter address or capacity; join with the Sipopo directory/PeeringDB records and GITGE press before recording capacity.

Queries:

```text
site:gitge.com "centro de datos"
site:gitge.com coubicacion
site:gitge.com Sipopo
site:gitge.com "data center"
site:gitge.com infraestructuras Ceiba OR ACE OR Mandji OR Ultramar
site:gitge.com "informe anual"
"GITGE" "centro de datos" Malabo
"GITGE" "data center" Sipopo
"GITGE" colocation OR coubicacion Guinea Ecuatorial
"GITGE" Bata "estacion de aterrizaje"
```

Extract: facility name, city/province/region, build status, opening target, contractor, intended tenants (operators, Google-type platforms), funding, and whether the page proves a facility or only a service/policy.

### 1.2 Ministry of Transport, Telecommunications and AI Systems + official government press

Verified URLs:
- Official government press (Oficina de Informacion y Prensa de Guinea Ecuatorial): https://www.guineaecuatorialpress.com/
- GITGE Annobon fiber activation + planned national data center (capacity for 8 submarine cables) + Mandji: https://www.guineaecuatorialpress.com/noticias/gitge_conecta_la_fibra_optica_para_annobon (2023-04-04)
- Nigeria-BCN digital transformation agreement incl. commercial data center: https://www.guineaecuatorialpress.com/noticias/guinea_ecuatorial_y_nigeria_estrechan_lazos_con_un_acuerdo_clave_para_la_transformacion_digital (2026-02-08)
- GITGE bandwidth increase / ORTEL DG quote: https://www.guineaecuatorialpress.com/noticias/el_gitge_otorgara_un_30%25_mas_de_capacidad_de_ancho_de_banda_a_las_operadoras
- SEGESA tender announcements: https://www.guineaecuatorialpress.com/noticias/anuncio_de_licitacion_de_la_empresa_segesa

Use as **A** for government programme status, official project descriptions, and named officials. The current ministry name seen in 2026 sources is `Ministerio de Transportes, Telecomunicaciones y Sistemas de Inteligencia Artificial` (minister Honorato Evita Oma); older sources use `Ministerio de Transportes, Correos y Telecomunicaciones`. Both names should be queried.

Queries:

```text
site:guineaecuatorialpress.com "centro de datos"
site:guineaecuatorialpress.com datacenter OR "data center"
site:guineaecuatorialpress.com GITGE fibra OR cable OR datos
site:guineaecuatorialpress.com CNIAPGE
site:guineaecuatorialpress.com "Honorato Evita Oma" telecomunicaciones
site:guineaecuatorialpress.com licitacion "centro de datos"
"Guinea Ecuatorial" "centro de datos" Ministerio OR Gobierno 2026
"cable submarino" "Guinea Ecuatorial" "centro de datos"
```

Extract: project name, division/province/city, status, contractor, financing, tenants, and whether the source proves a physical facility or only an agreement/policy.

### 1.3 ORTEL / OERT - telecom regulator

No official regulator website was found in this review (checked 2026-08-12); the regulator appears in press under two acronyms: `ORTEL` (Organo Regulador de las Telecomunicaciones) in older and some current sources, and `OERT`/`Organo Regulador de Telecomunicaciones` in others. Verify the current official name and URL before citing it as A; use press quoting the regulator as **B**.

Verified URLs:
- Regulator profile (directory): https://www.guineainfomarket.com/agencias-oficiales-guinea-ecuatorial/2014/08/16/oficiana-reguladora-de-las-telecomunicaciones-ortel/
- ORTEL DG Hermogenes Nzang Esono quoted on GITGE bandwidth plan (official press): https://www.guineaecuatorialpress.com/noticias/el_gitge_otorgara_un_30%25_mas_de_capacidad_de_ancho_de_banda_a_las_operadoras
- Telecoms sector legal overview (law firm note): https://clarenceabogados.com/guest-column/las-telecomunicaciones-en-guinea-ecuatorial/

Use the regulator for licence/operator facts and CEMAC roaming policy; it is not a datacenter register. Treat any `Tier` claims attributed to the regulator as operator/vendor claims until Uptime or an official datasheet confirms.

Queries:

```text
"ORTEL" OR "OERT" "Guinea Ecuatorial" telecomunicaciones licencia OR operador
"Organo Regulador de las Telecomunicaciones" "Guinea Ecuatorial" datacenter OR "centro de datos"
"Hermogenes Nzang Esono" telecomunicaciones
site:guineaecuatorialpress.com ORTEL OR OERT
"Ley General de Telecomunicaciones" "Guinea Ecuatorial" centros de datos
```

### 1.4 CNIAPGE - Centro Nacional para la Informatizacion de la Administracion Publica

CNIAPGE (under the Presidencia del Gobierno) is the government body running the public-administration informatization project and its **data center** - officially described as the heart of the project. This is the strongest A-grade evidence of an operational government datacenter in GQ. Official press ties the administration data center to **Malabo II**; treat the division as **Insular / Bioko Norte**. Do not infer an exact street address or merge it with GITGE Sipopo unless a source says so.

Verified URLs:
- Public tender for administration informatization, including passive and active equipment lots for the data center and CNIAPGE offices at Malabo II, Bloque E19-C 6th floor: https://www.guineaecuatorialpress.com/noticias/licitacion_publica_del_proyecto_de_informatizacion_de_la_administracion_publica (2014-07-12)
- Inauguration of the Centro de Datos de la Administración in Malabo II: https://www.guineaecuatorialpress.com/noticias/inauguraciones_de_obras_publicas_en_malabo_ii_para_celebrar_el_natalicio_presidencial (2016-06-06; event on 2016-06-04)
- First 2025 board meeting (data center equipment renewal, data custody/continuity mandate): https://www.guineaecuatorialpress.com/index.php/noticias/cniapge_celebra_su_primera_junta_directiva_del_2025 (2025-04-15)

Use as **A** for CNIAPGE existence, the Malabo II administration data center, its 2014 equipment tender, its 2016 inauguration, its 2025 renewal programme, and its role. The exact room/building relationship between the 2014 CNIAPGE office address and the inaugurated data center still needs confirmation; keep location granularity at Malabo II unless a source gives a finer address.

Queries:

```text
site:guineaecuatorialpress.com CNIAPGE "centro de datos"
"CNIAPGE" Malabo OR Bata OR sede OR edificio
"Centro de Datos de la Administración" "Malabo II"
"CNIAPGE" licitacion equipos OR servidores OR racks
"centro de datos" "informatizacion de la administracion" "Guinea Ecuatorial"
"CNIAPGE" direccion OR contacto
```

Extract: address, division, equipment scope (active/passive), power/cooling, UPS/generator, contractor, and commissioning history.

### 1.5 Ministry of Finance (Hacienda) / PAMFP - procurement channel for government datacenters

Verified URLs:
- PAMFP official site: https://www.pamfp.org/
- PAMFP tender coverage (June 2026) for Hacienda main DC in Malabo + backup DC in Bata (2 lots, 4 months each, solar equipment, national tender, bids in French with Spanish copy): https://ecofinge.com/guinea-ecuatorial-licita-equipos-para-modernizar-centros-de-datos-de-hacienda-en-malabo-y-bata/ (2026-06-04)
- PAMFP financing context (AfDB + GQ Government): https://realequatorialguinea.com/economia/guinea-ecuatorial-aprueba-en-el-marco-del-pamfp-el-plan-2026-para-reforzar-la-transparencia-y-la-gestion-de-las-finanzas-publicas/
- PAMFP 2022 tender batch: https://www.guineainfomarket.com/gobierno/2022/03/11/el-proyecto-de-apoyo-a-la-modernizacion-de-las-finanzas-publicas-pamfp-lanza-tres-concursos-de-licitacion-de-interes-publico/

Use PAMFP/official pages as **A** for project existence and financing (AfDB-co-financed). Use tender coverage as **B** for the specific Malabo/Bata datacenter equipment lots until an award notice appears on pamfp.org or in official press.

Queries:

```text
site:pamfp.org "centro de datos" OR "data center" OR licitacion
"PAMFP" "centro de datos" Malabo OR Bata OR Hacienda
"PAMFP" licitacion 2026 equipos servidores
"Hacienda" "Guinea Ecuatorial" "centro de datos"
"Ministerio de Hacienda" "Guinea Ecuatorial" datacenter OR servidores
site:afdb.org "Guinea Ecuatorial" "finanzas publicas"
```

Extract: lot scope, site (Malabo/Bata), budget, solar/generator scope, execution window, awardee, and commissioning evidence.

### 1.6 Energy, grid, and permit sources

Verified URLs:
- SEGESA (Sociedad de Electricidad de Guinea Ecuatorial) profile: https://www.guineainfomarket.com/agencias-oficiales-guinea-ecuatorial/2015/01/10/segesa-sociedad-de-electricidad-de-guinea-ecuatorial/
- SEGESA tender announcements (official press): https://www.guineaecuatorialpress.com/noticias/anuncio_de_licitacion_de_la_empresa_segesa
- Minsait/Indra official press release for SEGESA transformation contract including supply of a new data center in Malabo and Bata: https://www.indragroup.com/es/noticias/minsait-ayudara-electrica-guinea-ecuatorial-reducir-perdidas-comerciales-mejorar-atencion (2019-01-15)
- SEGESA X account: @Segesa_Energia (per La Gaceta de Guinea reporting, 2025)

No searchable national building-permit registry was found. Construction/permits are expected at municipality level (Malabo/Bata city councils); environmental/energy studies may surface through donor documents. Treat named permits/EIES as **A/B** depending on issuer; generic construction mentions remain leads. Treat the Minsait/SEGESA item as **B** for vendor contract scope and as an operator-internal data-center lead, not public colocation, until SEGESA or government commissioning evidence appears.

Queries:

```text
site:guineaecuatorialpress.com SEGESA electricidad Malabo OR Bata OR planta
"SEGESA" "centro de datos" OR datacenter OR "sala de servidores"
"Minsait" SEGESA "centro de datos" Malabo Bata
"Guinea Ecuatorial" datacenter electricidad OR "grupo electrogeno" OR UPS OR MW OR MVA
"permiso de construccion" OR "licencia de obras" "centro de datos" "Guinea Ecuatorial"
"SEGESA" cortes OR estabilidad energia Malabo
```

Extract exact power meaning: grid connection, substation, site load, IT load, MW/MVA, generator/fuel, cooling/water, permit dates, commissioning.

### 1.7 Official cloud-region negative controls

Use these as **A** only for cloud-region existence/non-existence. No AWS, Azure, Google Cloud, or OCI public region exists in GQ in the checked public lists (checked 2026-08-12); any GQ cloud claim is reseller/CDN/on-ramp/tenant evidence, not a regional facility.

- AWS Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Microsoft Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones
- Oracle OCI regions: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm

Queries:

```text
"Malabo" OR "Bata" ("AWS Direct Connect" OR ExpressRoute OR "Cloud Interconnect" OR FastConnect)
"Guinea Ecuatorial" "cloud region" OR "regiones de nube"
"Google" "centro de datos" "Guinea Ecuatorial"
"Equatorial Guinea" AWS OR Azure OR GCP OR Oracle region
```

### 1.8 IXP, peering, and Uptime Institute negative controls

Verified URLs:
- ISOC Pulse IXP tracker GQ: https://pulse.internetsociety.org/en/ixp-tracker/country/GQ/ - states: **no active Internet Exchange Points in Equatorial Guinea**; only ~3% of the top 1000 websites reachable via in-country cache (checked 2026-08-12). Use as **A** negative control for IXP existence.
- Uptime Institute awards list: https://uptimeinstitute.com/uptime-institute-awards/list - no GQ facility surfaced in this review. Treat `Tier III` language as design/compliance/operator claim unless the Uptime list confirms the exact facility and certification type.

Queries:

```text
site:uptimeinstitute.com "Equatorial Guinea" OR "Guinea Ecuatorial"
site:uptimeinstitute.com Malabo OR Bata
"Guinea Ecuatorial" "punto de intercambio" IXP
"GQIX" OR "GEIX" OR "IXP" "Guinea Ecuatorial"
site:peeringdb.com GQ facility OR exchange
```

## 2. Verified Facility and Lead Seeds

| Facility / project | Division | Evidence and grade | Status and handling |
|---|---|---|---|
| **GITGE Sipopo Datacenter, Malabo (Bioko Norte)** | Insular | GITGE official colocation service page + brochure **A**: https://gitge.com/servicios/coubicacion/ and https://gitge.com/wp-content/uploads/2025/08/coubicacion-brochure.pdf. PeeringDB facility 9041 (SIPOPO DATACENTER, Malabo, Bioko Norte, org GITGE, AS37529, geocode 3.751458, 8.908249; updated 2025-09-26) **C**: https://www.peeringdb.com/fac/9041. DataCenterMap **C**: https://www.datacentermap.com/equatorial-guinea/malabo/sipopo-datacenter/ (address Carretera Malabo-Sipopo, Sipopo). DataCenterPlatform **C**: https://datacenterplatform.com/data-centers/gestor-de-infraestructuras-de-telecomunicaciones-de-guinea-ecuatorial/ | Operator-confirmed colocation service (coubicacion: physical equipment location, casetas space, power access, interconnection) with a directory/PeeringDB-named facility at Sipopo. Grade service/location as **A** (service exists) but keep capacity, Tier, and rack counts as **C** until GITGE datasheet/brochure details or an official launch record is read. Do not assume this is the same site as the planned 8-cable national DC (see below). |
| **CNIAPGE / Centro de Datos de la Administración, Malabo II** | Insular (Bioko Norte) | Official government press **A**: 2014 CNIAPGE tender for passive/active data-center equipment and offices in Malabo II: https://www.guineaecuatorialpress.com/noticias/licitacion_publica_del_proyecto_de_informatizacion_de_la_administracion_publica; 2016 inauguration of the Centro de Datos de la Administración in Malabo II: https://www.guineaecuatorialpress.com/noticias/inauguraciones_de_obras_publicas_en_malabo_ii_para_celebrar_el_natalicio_presidencial; 2025 board record: https://www.guineaecuatorialpress.com/index.php/noticias/cniapge_celebra_su_primera_junta_directiva_del_2025 - data center described as the heart of the informatization project, guaranteeing availability, custody and continuity; active/passive equipment renewal requested. | Operational government datacenter with an ongoing renewal programme. Location is confirmed to Malabo II at city/zone level; exact address, size and capacity are not public. Keep separate from GITGE Sipopo unless official records prove they are the same room. |
| **Planned national data center with capacity for 8 submarine cables** | Unconfirmed (presented to Vice-Presidency; likely Malabo/Sipopo area but verify) | Official government press **A**: https://www.guineaecuatorialpress.com/noticias/gitge_conecta_la_fibra_optica_para_annobon (2023-04-04) - GITGE presented the data center project (capacity for 8 submarine cables, to attract operators such as Google and other cyber platforms); Vice-President gave the go-ahead pending tender. | Planned/approved project, expected to go through public tender. No public award/construction/commissioning evidence found in this review. Do **not** record as under construction or operational. Identity vs Sipopo DC unresolved - keep as a separate lead until tender/construction evidence appears. |
| **PAMFP / Hacienda main data center - Malabo** | Insular (Bioko Norte) | PAMFP official **A** for project: https://www.pamfp.org/. Tender coverage **B**: https://ecofinge.com/guinea-ecuatorial-licita-equipos-para-modernizar-centros-de-datos-de-hacienda-en-malabo-y-bata/ (2026-06-04) - Centro de Datos Principal in Malabo, lot 1, 4-month execution, solar equipment, national tender under PAMFP (AfDB-co-financed) counterpart funds. | Tender/planned. Modernization/equipment procurement for an existing or new ministry server facility; record as procurement-stage unless award/inauguration appears. Verify whether the Malabo Hacienda DC is an existing room being upgraded or a new build. |
| **PAMFP / Hacienda backup data center - Bata** | Continental (Litoral) | Same tender coverage **B** (Centro de Datos de Respaldo in Bata, lot 2). | Tender/planned. This is the main Continental-division datacenter lead. Do not count the ACE landing station or GITGE Bata technical rooms as this facility. |
| **SEGESA internal data-center supply - Malabo and Bata** | Insular + Continental | Minsait/Indra official press release **B**: https://www.indragroup.com/es/noticias/minsait-ayudara-electrica-guinea-ecuatorial-reducir-perdidas-comerciales-mejorar-atencion (2019-01-15) - SEGESA transformation contract of about EUR 5m, including supply of a new data center in Malabo and Bata. Agenda Empresa mirror **B/C**: https://www.agendaempresa.com/96276/minsait-ayudara-electrica-guinea-ecuatorial-reducir-perdidas-comerciales/ | Operator-internal utility IT lead, not public colocation. Search for SEGESA acceptance/commissioning, whether there are two sites or one distributed solution, and whether these are server rooms inside SEGESA offices. Do not merge with PAMFP/Hacienda or CNIAPGE. |
| **Nigeria-BCN commercial data center** | Unconfirmed (cable+DC agreement, location TBD) | Official press **A**: https://www.guineaecuatorialpress.com/noticias/guinea_ecuatorial_y_nigeria_estrechan_lazos_con_un_acuerdo_clave_para_la_transformacion_digital (2026-02-08); local press **B**: https://ahoraeg.com/politica/2026/02/08/guinea-ecuatorial-y-nigeria-estrechan-lazos-con-un-acuerdo-para-la-transformacion-digital/ | Signed strategic agreement between the GQ Government and Nigerian company BCN (Backbone Connectivity Network, led by Ibrahim Dikko) covering a submarine fiber cable and construction of a **commercial data center**. Agreement-level evidence only; record as planned/announced with no division assignment until site/tender evidence appears. |
| **GITGE Bata landing station / ACE + Ceiba-1/2 technical rooms** | Continental (Litoral) | GITGE infrastructure page **A**: https://gitge.com/infraestructuras/ (ACE international cable; Ceiba-1 287 km Malabo-Bata; Ceiba-2 in service since March 2017 Malabo-Bata-Kribi; RNFO metropolitan networks in Malabo and Bata incl. ACE and Ceiba-1 locations). GeoCables routing research **B**: https://geocables.com/research/equatorial-guinea-internet-routing (ACE landing at Bata; GITGE AS37529 upstreams Cogent and Hurricane Electric). | Connectivity infrastructure, **not** datacenters. Search the Bata station for technical/server rooms; do not count the landing station itself. Expected yield: POP/server-room leads only. |
| **Ultramar GE Annobon station + Mandji Corisco cable** | Insular (Annobon; Corisco) | GITGE infra page **A** (Ultramar GE ~263 km Annobon-Santo Tome; Mandji 50 km Corisco-Cabo San Juan). Official press **A**: https://www.guineaecuatorialpress.com/noticias/gitge_conecta_la_fibra_optica_para_annobon (266 km per press; activation 2023-04-03; >EUR 12m; 4.8 Tbps; described as self-sustaining station; operator radio links). | Connectivity only. Annobon station is a landing station with technical rooms; no public colocation evidence. Expect no datacenter record for Annobon; record as no-projects unless facility evidence appears. |
| **GETESA (Orange GQ legacy brand), GECOMSA, HITS-EG operators** | Multi-division | Operator/company records: https://getesa.gq/; GETESA AS37173 via https://bgp.tools/as/37173; GECOMSA profile https://www.guineainfomarket.com/economia/2016/08/02/gecomsa-guinea-ecuatorial-telecomunicaciones-sociedad-anonima/ | Operator existence is **A/B**; **no public evidence of public datacenter/colocation services** was found in this review. Treat as POP/server-room leads only; require facility language to count. |

## 3. Division Coverage and Strategy

Generic query block (run per division):

```text
("{division}" OR "{city}" OR "{alias}") (datacenter OR "data center" OR "centro de datos" OR "sala de servidores" OR coubicacion OR colocation) "Guinea Ecuatorial"
("{city}") ("fibra optica" OR backbone OR IXP OR "punto de intercambio" OR "estacion de aterrizaje") (datacenter OR "centro de datos" OR GITGE OR CNIAPGE)
site:gitge.com "{city}"
site:guineaecuatorialpress.com "{city}" "centro de datos"
site:guineaecuatorialpress.com "{city}" CNIAPGE OR GITGE OR PAMFP
"{operator}" "{city}" (datacenter OR colocation OR coubicacion OR POP OR "punto de presencia")
```

| Manifest division | Provinces / anchors | Priority | Concrete strategy |
|---|---|---:|---|
| **Continental** (Rio Muni) | Litoral (Bata, Machinda, Cogo); Centro Sur (Evinayong, Niefang, Bicurga, Nkimi); Kie-Ntem (Ebebiyin, Micomeseng, Nkue, Bidjabijan); Wele-Nzas (Mongomo, Anisok, Ayene, Mongomeyen); Djibloho (Oyala/Ciudad de la Paz) | High for Bata; low elsewhere | Seed PAMFP/Hacienda backup DC (Bata, tender), SEGESA/Minsait Bata internal-DC lead, GITGE Bata ACE landing station technical rooms, RNFO city POPs. For the 16 RNFO continental cities run only broad operator/backbone searches; expect POP/server-room leads, not colocation. Oyala (Ciudad de la Paz) is the new administrative capital - check for government server rooms there. |
| **Insular** (Bioko + Annobon) | Bioko Norte (Malabo, Malabo II, Sipopo); Bioko Sur (Luba, Riaba); Annobon (San Antonio de Pale); Corisco (Mandji) | Very high for Malabo; low elsewhere | Seed GITGE Sipopo DC, CNIAPGE / Centro de Datos de la Administración in Malabo II, PAMFP/Hacienda main DC (Malabo, tender), SEGESA/Minsait Malabo internal-DC lead, planned 8-cable national DC, BCN commercial DC (location TBD). Malabo is where the national market concentrates. Luba/Riaba: RNFO termination + port/oil services; Annobon: Ultramar GE landing only; Corisco: Mandji landing only. |

## 4. Evidence Capture Rules

For every candidate record capture:

```text
facility_name:
operator_or_owner:
division_manifest_2: Continental | Insular
province_city_address:
status: operational | commissioned | under construction | planned | tender | agreement | lead-only | rejected
source_grade_by_fact:
source_urls:
physical_evidence: racks | rooms | MW/MVA | Tier | IXP host | landing station | POP | office
capacity:
power_cooling:
connectivity:
tenant_or_service_scope:
dedupe_notes:
country_disambiguation:
```

Status hierarchy: official/operator operational page or inauguration > commissioning coverage > under-construction official/donor page > contract award > tender > agreement/MoU > policy. Capacity hierarchy: official datasheet > operator statement > trade press quoting operator > directory. Do not promote a C-grade directory lead without a non-directory join.

## 5. Rejection Patterns

- Guinea-Conakry (`Guinee`, Conakry) or Guinea-Bissau sources unless they explicitly describe a cross-border GQ facility.
- Hyperscale region claims for AWS/Azure/GCP/OCI in GQ unless the provider region page names Equatorial Guinea (none do as of 2026-08-12).
- Submarine landing stations (ACE Bata, Ceiba-1/2 Malabo-Bata, Ultramar GE Annobon, Mandji Corisco) counted as datacenters without adjacent facility evidence.
- `cloud`, `hosting`, `hebergement`, or `alojamiento web` services with no GQ physical site (e.g., foreign hosting resellers).
- Ministerial/ministry server rooms unless named as a significant data center, disaster-recovery site, or colocation facility (CNIAPGE DC and PAMFP/Hacienda DCs are the exceptions with official naming).
- Tier/ISO claims without Uptime Institute listing or official datasheet.
- The 2023 Annobon fiber project and the 8-cable national DC must not be merged; the latter is planned and the former is connectivity.
