# GQ Explorer Industry - Equatorial Guinea Datacenter Enumeration

Date: 2026-08-12. Scope: industry/operator/vendor methodology for **GQ - Equatorial Guinea / Republic of Equatorial Guinea**. Target division model remains the requested **2 manifest regions**: Continental (Rio Muni mainland); Insular (Bioko + Annobon islands). All results stay keyed to those 2 divisions; province/city names (Malabo, Bata, Luba, Riaba, Annobon, Ebebiyin, Mongomo, Evinayong, Djibloho/Oyala/Ciudad de la Paz, Micomeseng) are search anchors only.

Reliability grades:
- **A** = official operator page (GITGE), official government press, official cloud-region page, ISOC Pulse/PeeringDB structural record, Uptime Institute record.
- **B** = credible trade press (Agence Ecofin / Revista Ecofin EG, AhoraEG, DCD, Telecompaper, Digital Business Africa, Real Equatorial Guinea, guineaInfomarket), local press quoting named officials/operators, GeoCables-type network research, vendor press releases for the vendor's own contract scope.
- **C** = directory (DataCenterMap, DataCenterPlatform, DataCentersList, colo.exchange, Inflect, datacenters.com), PeeringDB user-maintained fields, market report, social post, generic vendor claim, ambiguous POP/hosting/cloud lead.

## 0. Market Assumptions

- The entire public datacenter market is concentrated in **Malabo (Bioko Norte, Insular)**: GITGE Sipopo Datacenter colocation, CNIAPGE / Centro de Datos de la Administración in Malabo II, PAMFP/Hacienda main DC (tender), planned national DC (8 submarine cables), and the announced BCN commercial DC. **Bata (Litoral, Continental)** is the secondary node: ACE landing station, GITGE Bata technical rooms, RNFO metropolitan network, the PAMFP/Hacienda **backup** DC (tender), and SEGESA/Minsait internal-DC supply lead.
- GQ has one international submarine cable system in service (ACE, landing at Bata) plus domestic/regional cables Ceiba-1 and Ceiba-2 (Malabo-Bata; Ceiba-2 to Kribi, Cameroon), Ultramar GE (Annobon-Santo Tome, activated 2023) and Mandji (Corisco-Cabo San Juan). Cable landings are connectivity, not datacenters.
- **There is no active public IXP in Equatorial Guinea** (ISOC Pulse, checked 2026-08-12) and no AWS/Azure/GCP/OCI region. Treat global-cloud references as reseller, CDN, on-ramp, or tenant leads unless an official region page names GQ.
- GITGE (AS37529) is the de-facto national carrier-of-carriers: IP transit, international Ethernet, MetroEthernet, FTTH, port activation, and **coubicacion (colocation)**. Any serious colocation search starts and ends with GITGE plus the government programs (CNIAPGE, PAMFP, BCN agreement).
- Telco POPs (GETESA/Orange-brand legacy, GECOMSA, HITS-EG), tower shelters, landing stations, and offices are not datacenters unless the source names colocation, racks, white space, datacenter rooms, Tier design/certification, or a significant sovereign/enterprise hosting function.
- **Honest yield expectation**: 3-6 records nationwide if internal government/utility facilities are included; fewer if counting only public colocation. Do not inflate with landing stations, telco offices, tower shelters, or cloud resellers.

## 1. Operator and Facility Seeds

| Operator / facility | Division | Evidence | Grade | Action |
|---|---|---|---|---|
| **GITGE Sipopo Datacenter (Malabo)** | Insular (Bioko Norte) | Official colocation page: https://gitge.com/servicios/coubicacion/; brochure: https://gitge.com/wp-content/uploads/2025/08/coubicacion-brochure.pdf; infrastructure page: https://gitge.com/infraestructuras/; PeeringDB fac 9041: https://www.peeringdb.com/fac/9041 (SIPOPO DATACENTER, Malabo, geocode 3.751458, 8.908249); DataCenterMap: https://www.datacentermap.com/equatorial-guinea/malabo/sipopo-datacenter/; DataCenterPlatform: https://datacenterplatform.com/data-centers/gestor-de-infraestructuras-de-telecomunicaciones-de-guinea-ecuatorial/ | A for service offering; C for facility details | Record as the flagship in-country colocation facility. Search GITGE brochure/datasheet for racks, power, Tier, address; PeeringDB customer ASNs; any launch press. Do not merge with CNIAPGE or the planned 8-cable DC without evidence. |
| **CNIAPGE / Centro de Datos de la Administración (Malabo II)** | Insular (Bioko Norte) | Official press: 2014 CNIAPGE tender for passive/active data-center equipment and offices in Malabo II: https://www.guineaecuatorialpress.com/noticias/licitacion_publica_del_proyecto_de_informatizacion_de_la_administracion_publica; 2016 inauguration of the Centro de Datos de la Administración in Malabo II: https://www.guineaecuatorialpress.com/noticias/inauguraciones_de_obras_publicas_en_malabo_ii_para_celebrar_el_natalicio_presidencial; 2025 renewal record: https://www.guineaecuatorialpress.com/index.php/noticias/cniapge_celebra_su_primera_junta_directiva_del_2025 | A for existence, role, Malabo II city/zone location, and renewal | Operational government DC. Exact address/room, capacity, and service scope remain unverified. Likely not a public colocation offering - record accordingly. Keep separate from GITGE Sipopo. |
| **Planned national data center (capacity for 8 submarine cables)** | Unconfirmed | Official press: https://www.guineaecuatorialpress.com/noticias/gitge_conecta_la_fibra_optica_para_annobon (2023-04-04) - GITGE project to attract operators such as Google; go-ahead given pending tender | A for plan | Planned only. Watch for tender, contractor, site (possibly Sipopo/Malabo), and commissioning. Do not count as operational. |
| **PAMFP / Hacienda DCs: Malabo (main) + Bata (backup)** | Insular; Continental | PAMFP official: https://www.pamfp.org/; tender coverage: https://ecofinge.com/guinea-ecuatorial-licita-equipos-para-modernizar-centros-de-datos-de-hacienda-en-malabo-y-bata/ (2026-06-04) - 2 lots, 4 months each, solar energy systems, national tender, PAMFP (AfDB-co-financed) | A for program; B for tender details | Procurement-stage leads. Malabo lot = main DC; Bata lot = backup DC. Follow award and installation; verify whether facilities pre-exist as ministry server rooms. Bata record is the strongest Continental-division datacenter lead. |
| **SEGESA internal data-center supply (Malabo + Bata)** | Insular + Continental | Minsait/Indra official press release: https://www.indragroup.com/es/noticias/minsait-ayudara-electrica-guinea-ecuatorial-reducir-perdidas-comerciales-mejorar-atencion (2019-01-15) - about EUR 5m SEGESA transformation contract, including supply of a new data center in Malabo and Bata; Agenda Empresa mirror: https://www.agendaempresa.com/96276/minsait-ayudara-electrica-guinea-ecuatorial-reducir-perdidas-comerciales/ | B for vendor contract scope | Operator-internal utility IT lead. Search for SEGESA acceptance, exact sites, and whether this means two server rooms or one distributed platform. Do not count as public colocation and do not merge with PAMFP/Hacienda. |
| **Nigeria-BCN commercial data center (agreement)** | Unconfirmed | Official press: https://www.guineaecuatorialpress.com/noticias/guinea_ecuatorial_y_nigeria_estrechan_lazos_con_un_acuerdo_clave_para_la_transformacion_digital (2026-02-08); AhoraEG: https://ahoraeg.com/politica/2026/02/08/guinea-ecuatorial-y-nigeria-estrechan-lazos-con-un-acuerdo-para-la-transformacion-digital/ - BCN (Backbone Connectivity Network, Ibrahim Dikko), submarine cable + commercial data center | A/B agreement-level | Planned/announced. Track BCN, cable landing choice (Bata likely for a new international cable), DC site, and Malabo Convention/cybersecurity framing. |
| **GITGE Bata ACE landing / RNFO Bata metro** | Continental (Litoral) | GITGE infra: https://gitge.com/infraestructuras/; GeoCables: https://geocables.com/research/equatorial-guinea-internet-routing (ACE landing Bata; GITGE AS37529 upstreams Cogent, Hurricane Electric) | A for infrastructure; B for routing | Connectivity leads. Look for carrier rooms, backhaul PoPs, customer equipment at the landing station. Landing station itself is not a DC. |
| **Ultramar GE Annobon station; Mandji Corisco** | Insular (Annobon; Corisco) | GITGE infra: https://gitge.com/infraestructuras/ (Ultramar ~263 km; Mandji 50 km); official press Annobon activation: https://www.guineaecuatorialpress.com/noticias/gitge_conecta_la_fibra_optica_para_annobon (2023-04-03, >EUR 12m, 4.8 Tbps, operator radio links) | A | Connectivity only. Expect no datacenter record; record as no-projects unless facility evidence appears. |
| **GETESA (legacy Orange GQ brand), GECOMSA, HITS-EG** | Multi-division | GETESA: https://getesa.gq/; AS37173: https://bgp.tools/as/37173; GECOMSA profile: https://www.guineainfomarket.com/economia/2016/08/02/gecomsa-guinea-ecuatorial-telecomunicaciones-sociedad-anonima/ | B for existence; no DC evidence found | Operator/POP leads only. Query each for colocation/hosting/datacenter services; require facility language to count. |
| **Vendor/integrator leads** | Unconfirmed | Incubaweb GITGE data-center article: https://incubaweb.com/la-necesidad-de-data-centers-en-africa-un-paso-hacia-la-transformacion-digital/ (GITGE world-class DC ambition); Huawei Marine on SAIL (per GITGE infra page); China Eximbank loan for GECOMSA project: https://china.aiddata.org/projects/30542 | C | Vendor/PR leads. Use to find contractors for GITGE/CNIAPGE/PAMFP/BCN work; do not count as facilities without a facility-level join. |

## 2. Cloud, CDN, and On-Ramp Checks

Official public-region sources, used as A-grade negative controls (checked 2026-08-12):

| Provider | Official URL | Current GQ finding |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Equatorial Guinea region. The official AWS list checked on 2026-08-12 shows Africa (Cape Town / `af-south-1`) and does not list GQ. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Equatorial Guinea region. Africa regions are South Africa North/West; GQ not listed. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | No Equatorial Guinea region. `africa-south1` is Johannesburg; GQ not listed. |
| Oracle OCI | https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm | No Equatorial Guinea region. `af-johannesburg-1` (South Africa) and `af-marrakech-1` (Morocco); GQ not listed. |

On-ramp/CDN searches (the planned 8-cable DC explicitly names Google as a target tenant):

```text
"Malabo" OR "Bata" ("AWS Direct Connect" OR ExpressRoute OR "Cloud Interconnect" OR FastConnect OR CDN OR edge)
"GITGE" (Google OR AWS OR Azure OR Oracle OR Cloudflare OR Akamai OR CDN OR peering)
"Guinea Ecuatorial" "centro de datos" Google OR "plataformas ciberneticas"
"Equatorial Guinea" "direct connect" OR "edge location" OR cache
site:cloud.google.com "Equatorial Guinea"
```

## 3. Industry Sources by Type

High-value sources:
- **Operator official pages (A)**: GITGE (services + annual report), GETESA, PAMFP, ministry/government press.
- **Peering/network records (A/B/C)**: PeeringDB org 17440 / fac 9041 (C for user-maintained detail), AS37529 routing (bgp.he.net / bgp.tools), ISOC Pulse GQ (A: no IXP, 3% local cache), GeoCables research (B).
- **Government project pages (A)**: guineaecuatorialpress.com, CNIAPGE board records, PAMFP official site, AfDB pages for PAMFP financing.
- **Trade press (B)**: Revista Ecofin EG / Agence Ecofin, AhoraEG, Real Equatorial Guinea, guineaInfomarket, La Gaceta de Guinea, Diario Rombe, DCD, Telecompaper, Digital Business Africa, We Are Tech Africa, EquaCom News.
- **Directories (C)**: DataCenterMap, DataCenterPlatform, DataCentersList, colo.exchange, Inflect, datacenters.com, empresasguinea.com. Use for aliases/addresses only until joined to A/B sources.

Directory URLs to check as leads:

```text
https://www.datacentermap.com/equatorial-guinea/
https://www.datacentermap.com/equatorial-guinea/malabo/sipopo-datacenter/
https://www.peeringdb.com/fac/9041
https://datacenterplatform.com/data-centers/gestor-de-infraestructuras-de-telecomunicaciones-de-guinea-ecuatorial/
https://www.datacenterslist.com/data-centers/country/gq
https://inflect.com/datacenters/emea/equatorial-guinea  (checked 2026-08-12: HTTP 404; keep only as a historical search lead, not a verified URL)
```

## 4. Query Library

Core disambiguated queries (Spanish first):

```text
("Guinea Ecuatorial" OR Malabo OR Bata) (datacenter OR "data center" OR "centro de datos" OR coubicacion OR colocation) -Conakry -"Guinea-Bissau"
("Guinea Ecuatorial" OR Malabo OR Bata) ("Tier III" OR "Tier 3" OR "Uptime Institute")
("Guinea Ecuatorial") ("nube soberana" OR "soberania digital" OR "cofre digital" OR "centro de datos nacional")
("Guinea Ecuatorial") (IXP OR "punto de intercambio" OR "intercambio de trafico")
"GITGE" (centro de datos OR datacenter OR coubicacion OR "data center")
"centro de datos" "Guinea Ecuatorial" -Guinee -Conakry
```

Vendor pivots:

```text
"GITGE" Sipopo datacenter OR coubicacion OR racks OR Tier
"GITGE" "centro de datos" licitacion OR contrato OR adjudicacion
"CNIAPGE" servidores OR racks OR "centro de datos" OR licitacion
"Centro de Datos de la Administración" "Malabo II"
"PAMFP" Malabo "centro de datos" OR Bata "centro de datos"
"Hacienda" "Guinea Ecuatorial" "centro de datos principal" OR "centro de datos de respaldo"
"Minsait" SEGESA "centro de datos" Malabo Bata
"BCN" OR "Backbone Connectivity Network" "Guinea Ecuatorial" cable OR "centro de datos"
"Huawei" OR "ZTE" OR "Sumec" OR "DatacenterDynamics" "Guinea Ecuatorial" datacenter OR fibra
"GETESA" OR "GECOMSA" colocation OR hosting OR "sala de servidores" OR datacenter
"Google" "centro de datos" "Guinea Ecuatorial"
"Annobon" fibra OR "estacion" GITGE
"Mandji" cable Corisco "Guinea Ecuatorial"
```

Trade-source scoped queries:

```text
site:ecofinge.com "Guinea Ecuatorial" "centro de datos" OR datacenter
site:ahoraeg.com "Guinea Ecuatorial" datacenter OR "centro de datos"
site:realequatorialguinea.com datacenter OR "centro de datos"
site:guineainfomarket.com datacenter OR "centro de datos" OR GITGE
site:guineaecuatorialpress.com "centro de datos" OR datacenter OR GITGE
site:lagdeguinea.com "centro de datos" OR datacenter OR GITGE
site:datacenterdynamics.com "Equatorial Guinea" "data center"
site:agenceecofin.com "Guinee equatoriale" datacenter OR "centre de donnees"
```

## 5. Division-by-Division Industry Pattern

For each division use:

```text
("{division}" OR "{city}" OR "{alias}") (datacenter OR "data center" OR "centro de datos" OR colocation OR coubicacion OR hosting OR "sala de servidores") "Guinea Ecuatorial"
("{city}" OR "{division}") ("fibra optica" OR backbone OR POP OR "punto de presencia" OR IXP OR "estacion de aterrizaje") (GITGE OR GETESA OR GECOMSA OR datacenter)
("{operator}") ("{city}" OR "{division}") (datacenter OR colocation OR coubicacion OR hosting OR "sala de servidores")
```

| Manifest division | Industry aliases | Priority | Industry strategy |
|---|---|---:|---|
| **Continental** (Rio Muni) | Bata, Machinda, Cogo, Evinayong, Niefang, Bicurga, Nkimi, Nkue, Ebebiyin, Micomeseng, Bidjabijan, Mongomo, Anisok, Ayene, Mongomeyen, Djibloho/Oyala/Ciudad de la Paz | High (Bata); low-medium (others) | Seed PAMFP/Hacienda backup DC (Bata, tender), SEGESA/Minsait Bata internal-DC lead, GITGE ACE landing station + RNFO Bata metro technical rooms, operator POPs. Oyala (Ciudad de la Paz) is the new administrative capital - check government server rooms. Other RNFO cities: backbone/POP leads only; expect no colocation. |
| **Insular** (Bioko + Annobon) | Malabo, Malabo II, Sipopo, Luba, Riaba, San Antonio de Pale, Corisco, Annobon | Very high (Malabo); low (elsewhere) | Seed GITGE Sipopo DC, CNIAPGE / Centro de Datos de la Administración in Malabo II, PAMFP/Hacienda main DC (Malabo, tender), SEGESA/Minsait Malabo internal-DC lead, planned 8-cable national DC, BCN commercial DC (location TBD). Luba/Riaba and Annobon/Corisco: landing/backbone only. Malabo is the national colocation market. |

## 6. Verification and Dedupe Rules

1. **Operator page beats directory.** GITGE confirms the colocation service (A); PeeringDB/DataCenterMap supply the Sipopo address and identity (C) - grade each fact separately and keep directory-only capacity as C until a GITGE datasheet or official launch record matches.
2. **Landing station is connectivity, not colocation.** ACE Bata, Ceiba-1/2, Ultramar GE Annobon and Mandji Corisco are network leads; do not count them as datacenters without adjacent rack/facility evidence.
3. **Keep the government DCs separate.** GITGE Sipopo DC, CNIAPGE DC, PAMFP/Hacienda Malabo DC, the planned 8-cable national DC, and the BCN commercial DC are distinct records until official evidence proves identity (same building/contract).
4. **Do not upgrade agreements/tenders to construction.** The BCN data center is an agreement (2026-02); the PAMFP lots are a tender (2026-06); the 8-cable DC was a 2023 proposal with go-ahead pending tender. Each needs award/site/construction evidence before promotion.
5. **CNIAPGE is Malabo II at city/zone level, not Sipopo by default.** Official press supports the administration data center in Malabo II and a 2025 renewal programme; it does not publish capacity or prove identity with GITGE Sipopo.
6. **No IXP, no Tier certification shortcuts.** ISOC Pulse reports no active GQ IXP (A); any `Tier III` claim needs the Uptime Institute list or an official datasheet (none found).
7. **Keep status dates explicit.** Examples: Sipopo DC record updated in PeeringDB 2025-09-26; CNIAPGE tender 2014-07-12, inauguration 2016-06-04/06, and renewal 2025-04-15; SEGESA/Minsait contract 2019-01-15; Annobon fiber activated 2023-04-03; PAMFP tender 2026-06-04; BCN agreement 2026-02-09; 8-cable DC proposal 2023-04-04.
