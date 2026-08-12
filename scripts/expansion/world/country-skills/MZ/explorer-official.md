# MZ Explorer Official - Mozambique Datacenter Enumeration

Date: 2026-08-12. Country: MZ Mozambique. Division model for this repo: 10 manifest provinces: Niassa; Manica; Gaza; Inhambane; Maputo; Nampula; Cabo Delgado; Zambezia; Sofala; Tete.

Administrative caveat: Mozambique also has Maputo City (Cidade de Maputo) as a separate first-level administrative unit. The repo manifest has only one `Maputo` division. Map evidence from both Maputo City and Maputo Province (Matola, Boane/Beluluane, Namaacha, Manhica, Matalane) to manifest `Maputo`, while preserving the exact official locality in notes.

Angle: official, regulator, government-system, procurement, construction/permitting, energy/utility and official-operator routes for finding operational, licensed, under-construction, planned and institutional data-center facilities in Mozambique.

## Reliability Grades

- A = primary source: INTIC pages or published decrees; INCM legal/operator material; official operator facility page or release; official university/ministry/utility page; Uptime Institute facility record; APIEX/BAU/ARENE/EDM/MIREME/HCB official material; official cloud-region page.
- B = strong secondary: DCD, Club of Mozambique/AIM syndication, Jornal Noticias, Carta de Mocambique, Diario Economico, O Pais, TechCentral, TechAfrica News, Capacity, Developing Telecoms, The Tech Capital, Agence Ecofin/We Are Tech Africa, Macauhub, reputable legal alerts summarizing gazetted law.
- C = weak lead: DataCenterMap, Datacenters.com, Baxtel, Cloudscene, OCOLO, colo.exchange, Inflect, HostDir, PeeringDB, SubmarineNetworks, social posts, market reports, broker pages, unverified blogs.

Do not upgrade a C directory claim unless an A/B source independently confirms the facility, site or accountable operator claim.

## 0. Mozambique-Specific Facts

- There is no public national data-center register. INTIC licensing is now the closest official route: INTIC says it delivered the first licenses to electronic-service providers, digital-platform operators, data-center operators and data centers on 2026-06-08: https://intic.gov.mz/intic-atribui-primeiras-licencas-a-provedores-intermediarios-de-servicos-electronicos-operadores-de-plataformas-digitais-e-centros-de-dados/
- INTIC published the data-center and cloud regime in early 2026. The verified INTIC page says Decretos n.o 71/2025 and n.o 72/2025, both of 2025-12-31, approve the data-center and cloud-computing regulations in Boletim da Republica I Serie n.o 250: https://intic.gov.mz/ja-ha-regras-para-a-construcao-de-centros-de-dados-e-para-a-operacao-de-plataformas-de-computacao-em-nuvem-em-mocambique/ . INTIC also hosts the gazette PDF bundle: https://intic.gov.mz/wp-content/uploads/2026/02/TG_Regulamento-de-Centro-de-Dados_Dec-71_2025_.pdf
- Law-firm summaries are useful but stay B unless quoting the decree text. Verified summaries: DLA Piper Africa, https://www.dlapiperafrica.com/en/mozambique/insights/2026/Approval-of-the-Data-Centre-Regulation ; MLGTS, https://www.mlgts.pt/pt/conhecimento/legal-alerts/Legal-Alert-Novos-regulamentos-de-centro-de-dados-e-computacao-em-nuvem-em-Mocambique/26532/
- Search in Portuguese first. Use `centro de dados`, `centro de processamento de dados`, `data center`, `data centre`, `sala de servidores`, `computacao em nuvem`, `nuvem`, `colocation`, `alojamento`, `hospedagem`, `licenca`, `licenciamento`, `Titulo Unico`, `Uptime`, `Tier III`, `racks`, `MW`.
- Confirmed commercial/operator facilities are Maputo-centric: iColo/Digital Realty MPM1 in Maputo City; Raxio MZ1 in Beluluane/Matola/Boane area, Maputo Province; Vodacom Business Matola Data Center in Tchumene/Matola; plus legacy/operator and institutional leads.
- New official/institutional Maputo leads as of August 2026: UEM/CIUEM inaugurated a new data center in Maputo (official UEM source); EDM's National Control Centre project describes data-center components at Matalane and CTM, with regional control-center/data-collection functions at Chibata and Nampula (source is an EDM-branded 2026 RENMOZ presentation hosted by ALER; treat as A/B depending whether the local repo accepts hosted official slides).
- No AWS, Azure, Google Cloud or Oracle OCI public cloud region is in Mozambique. Check official region lists before accepting a cloud-region claim: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google https://cloud.google.com/about/locations ; Oracle https://www.oracle.com/cloud/cloud-regions/

## 1. Highest-Value Official Routes

### 1.1 INTIC - Data-Center and Cloud Regulator

Primary URL: https://intic.gov.mz/

Use INTIC for license and regulatory evidence, not just market leads.

Verified official routes:

- First licensing announcement, 2026-06-08: https://intic.gov.mz/intic-atribui-primeiras-licencas-a-provedores-intermediarios-de-servicos-electronicos-operadores-de-plataformas-digitais-e-centros-de-dados/
- Rules for data-center construction and cloud-platform operation: https://intic.gov.mz/ja-ha-regras-para-a-construcao-de-centros-de-dados-e-para-a-operacao-de-plataformas-de-computacao-em-nuvem-em-mocambique/
- Data-center/cloud decree PDF bundle: https://intic.gov.mz/wp-content/uploads/2026/02/TG_Regulamento-de-Centro-de-Dados_Dec-71_2025_.pdf
- Sector legislation page, including cyber laws: https://intic.gov.mz/sectorial/

Queries:

```text
site:intic.gov.mz "centro de dados"
site:intic.gov.mz "Operadores de Centros de Dados"
site:intic.gov.mz "licencas" "centros de dados"
site:intic.gov.mz "Titulo Unico"
site:intic.gov.mz "computacao em nuvem"
site:intic.gov.mz "{operator}" "licenca"
"INTIC" "centro de dados" "{province}"
"Decreto 71/2025" "centro de dados" Mocambique
"Decreto 72/2025" "computacao em nuvem" Mocambique
```

Grade A for INTIC facts, license categories, dates and named licensees. If a licensee is a cloud/platform operator only, do not count it as a physical data center unless the source names a facility.

### 1.2 INCM - Communications Regulator

Primary URL: https://www.incm.gov.mz/

INCM is the telecom/postal regulator, useful for legal names and operator universe. It is not a data-center facility register.

Verified routes:

- Main portal: https://www.incm.gov.mz/
- Telecom legislation page: https://www.incm.gov.mz/legislacao-telecomunicacoes/

Queries:

```text
site:incm.gov.mz "data center"
site:incm.gov.mz "centro de dados"
site:incm.gov.mz "licenca" "{operator}"
site:incm.gov.mz "5G" OR "espectro" "{operator}"
"INCM" "Mocambique Telecom" OR Tmcel
"INCM" Vodacom Movitel licenca Mocambique
```

Use INCM to confirm the operator universe: Tmcel/Mocambique Telecom, Vodacom Mocambique, Movitel, TV Cabo, Internet Solutions/Dimension Data/BCX, Webmasters, Moztel, TeleData, Paratus, WIOCC, SEACOM and other licensed telecom/ISP entities. Operator licenses are A for telecom authority, but only a lead for physical facilities.

### 1.3 Government Systems and Institutional Data Centers

Primary routes:

- CEDSIF: https://www.cedsif.gov.mz/ . CEDSIF/e-SISTAFE product pages confirm the state financial-management platform, but are not yet a public physical data-center record. Product page: https://www.cedsif.gov.mz/cedsifportal/productos/
- UEM official data-center page: https://uem.mz/uem-inaugura-centro-de-dados/ . This is A for the UEM/CIUEM Maputo institutional data center. It states the facility supports UEM systems and strategic national services including `.mz` and MOZIX, and replaces/upgrades the former server room.
- Portal do Governo and ministry pages: verify current URLs at run time. Use only when they name a physical site.
- Boletim da Republica: use official gazette or INTIC-hosted gazette PDF where available. Third-party mirrors are B unless the official text is opened.

Queries:

```text
site:cedsif.gov.mz "centro de dados" OR "data center"
site:cedsif.gov.mz "e-SISTAFE" "servidores"
site:uem.mz "centro de dados"
site:uem.mz CIUEM MOZIX ".mz"
"Centro de Dados do Governo de Mocambique"
"Portal do Governo" "centro de dados" Mocambique
"Boletim da Republica" "centro de dados" Mocambique
"concurso publico" "centro de dados" Mocambique
"sala de servidores" "Mocambique" "ministerio"
```

### 1.4 Investment, Business and Construction Licensing

Primary routes:

- APIEX: https://apiex.gov.mz/ and investment route https://apiex.gov.mz/invest/ . Use for registered investments, special economic zones and large ICT projects. APIEX records are A for investment approval, not for operational data-center status.
- BAU/e-BAU: https://www.bau.gov.mz/ and e-BAU page https://www.bau.gov.mz/e-bau/ . Use for economic-activity licensing leads. BAU is not a searchable building-permit database.
- Municipal/district works licenses: Maputo City council for Maputo City; Matola/Boane/Namaacha/Manhica and district/provincial authorities elsewhere. Public records are sparse; rely on operator releases, procurement, municipal notices and press.

Queries:

```text
site:apiex.gov.mz "data center" OR "centro de dados"
site:apiex.gov.mz "Beluluane" OR "MozParks"
site:bau.gov.mz "licenciamento" "actividades economicas"
"licenca de construcao" "data center" Maputo OR Matola OR Boane
"licenca de obras" "centro de dados" Mocambique
"Zona Franca" OR "ZEE" OR "Beluluane Industrial Park" "data center"
```

### 1.5 Energy and Utility Route

Primary routes:

- ARENE: https://arene.org.mz/ ; electricity legislation page: https://arene.org.mz/electricidade/legislacao/
- EDM: https://www.edm.co.mz/
- MIREME (correct acronym; not MIRENA): https://mireme.gov.mz/
- HCB: https://www.hcb.co.mz/

Energy evidence is usually supporting context. Count it only when a source explicitly names a data-center, control-center or data-collection facility.

Verified utility lead:

- EDM-branded RENMOZ 2026 presentation hosted by ALER describes the National Control Centre project with data-center components at Matalane and CTM in Maputo, and regional control/data-collection sites at Chibata and Nampula: https://www.aler-energia.org/contents/activitieseventsspeakersdocuments/1--renmoz-edm-tsate-and-mavuzi-ii_final.pdf . Treat Matalane and CTM as utility/SCADA institutional data-center leads; Chibata and Nampula as control/data-collection leads unless later EDM procurement or commissioning documents explicitly name data centers.

Queries:

```text
site:edm.co.mz "centro de dados" OR "data center"
site:edm.co.mz "Centro Nacional de Controlo" OR "National Control Center"
"EDM" "Matalane" "data center"
"EDM" "CTM" "data center"
"EDM" "Chibata" "Data Collection Centre"
"EDM" "Nampula" "Regional Control Center"
site:arene.org.mz "grandes consumidores" "data center"
site:mireme.gov.mz "data center" OR "centro de dados"
"Central Termica de Temane" SCADA servidores
"HCB" "centro de dados" OR servidores
```

## 2. Official Facility and Project Watchlist

| Facility / project | Manifest division | Status | Grade | Verification route | Notes |
|---|---:|---|---:|---|---|
| Raxio MZ1, Beluluane Industrial Park / Matola-Boane area | Maputo | Operational | A | Raxio official page https://www.raxiogroup.com/data-centres/mozambique/ ; Uptime Mozambique country record https://uptimeinstitute.com/uptime-institute-awards/country/id/MZ | Raxio states up to 400 racks, 2,000 sqm white space and 3 MW IT power. Uptime lists Raxio MZ1 with Tier III design and constructed-facility certification. |
| iColo / Digital Realty Maputo One MPM1, Maputo City | Maputo | Operational | A | iColo location https://www.icolo.io/location/mpm1/ ; iColo opening https://www.icolo.io/news/icolo-announces-opening-of-mpm1-data-center-in-maputo/ ; Digital Realty https://www.digitalrealty.com/data-centers/emea/maputo/mpm1 | 80 racks, 350 sqm IT space, 9,500 sqm campus from iColo. Digital Realty lists MPM1 in Maputo. |
| Vodacom Business Matola Data Center, Tchumene/Matola | Maputo | Operational | A/B | Uptime country record https://uptimeinstitute.com/uptime-institute-awards/country/id/MZ ; DCD https://www.datacenterdynamics.com/en/news/vodacom-opens-data-center-in-maputo-mozambique/ ; Club of Mozambique https://clubofmozambique.com/news/mozambique-prime-minister-opens-vodacom-data-centre-photos/ | Uptime lists Vodacom Mocambique, S.A. / Vodacom Business Matola Data Center with Tier III design and constructed-facility certification. DCD reports USD 25m, Tchumene, construction began Oct 2023, carrier-neutral and 2Africa access. Leave capacity_mw null unless Vodacom publishes it. |
| Vodacom modular data center, Matola | Maputo | Operational legacy lead | B | DCD 2025 article references prior 2013 modular data center | Keep separate only if inventory policy distinguishes legacy modular facility from the 2025 Matola DC. |
| UEM / CIUEM data center, Maputo | Maputo | Operational institutional | A | UEM official page https://uem.mz/uem-inaugura-centro-de-dados/ | Inaugurated Aug 2026; supports UEM systems, research, AI/data science, `.mz` and MOZIX. Institutional, not commercial colo unless service offering is documented. |
| CEDSIF / e-SISTAFE infrastructure, Maputo | Maputo | Institutional lead | A/C | CEDSIF portal https://www.cedsif.gov.mz/ ; products https://www.cedsif.gov.mz/cedsifportal/productos/ | CEDSIF confirms e-SISTAFE platform and official address; count only if a physical data-center/source names the facility. |
| INTIC-licensed data-center operators/facilities | Any, likely Maputo-heavy | Licensed | A | INTIC first license page | Harvest exact licensee names from INTIC pages and license notices each run. License category matters: DC operator/facility can count as licensed lead; cloud/platform-only cannot. |
| Bubble Cloud Mozambique | Maputo, verify exact site | Licensed cloud/service lead | B/C until facility source | Carta https://cartamz.com/empresas-marcas-e-pessoas/51499/novo-regime-bubble-e-a-primeira-provedora-de-servicos-cloud-a-receber-licenciamento/ ; Bubble https://www.bubble.co.mz/ ; LinkedIn/company material | Licensed cloud provider with data residency in Mozambique. AIM reports two data centers; verify operator or INTIC facility names before counting as two physical DCs. |
| EDM National Control Centre - Matalane and CTM | Maputo | Planned/under procurement utility DC components | A/B | EDM-branded RENMOZ slides hosted by ALER | Use as utility/SCADA data-center leads. Construction start and commissioning dates in the slide deck should be rechecked in EDM tender/award documents. |
| EDM Central Regional Control Center - Chibata | Manica/Sofala boundary, verify exact division | Planned utility control/data-collection lead | A/B | EDM-branded RENMOZ slides hosted by ALER | Do not count as commercial DC. Verify Chibata locality before division assignment; likely central grid site. |
| EDM Northern Regional Control Center - Nampula | Nampula | Planned utility control/data-collection lead | A/B | EDM-branded RENMOZ slides hosted by ALER | Lead for Nampula institutional/utility infrastructure. Count only if data-center component is explicit in later procurement. |
| Tmcel, Movitel, TV Cabo, Webmasters, TeleData, Paratus, Dimension Data/BCX, WIOCC | Mostly Maputo | Operator leads | A/C | Official operator pages + INCM + iColo/Raxio ecosystem lists | Network/core/hosting presence is not enough. Require named facility, license or tender. |

## 3. Province Coverage Matrix

Run all 10 manifest divisions. `Maputo` includes Maputo City and Maputo Province.

| Manifest division | Aliases / cities | Baseline expectation | Official strategy |
|---|---|---|---|
| Niassa | Niassa; Lichinga; Cuamba; Chimbonila | Negative by default; public ICT and off-grid energy leads only | Search INTIC/BAU/INCM plus `"Niassa" "centro de dados"`, `"Lichinga" "data center"`, `"Chimbonila" servidores`. Do not confuse generic "Joint Data Center" or development datasets with facilities. |
| Manica | Manica; Chimoio; Chibata; Beira Corridor | Negative by default, but EDM Chibata control/data-collection lead and corridor telecom leads | Search `"Manica" "centro de dados"`, `"Chimoio" "data center"`, `"Chibata" "data center" EDM`, `"Beira Corridor" servidores`. Verify whether Chibata belongs to Manica or Sofala before assigning. |
| Gaza | Gaza; Xai-Xai; Chokwe; Chibuto; Macia | Negative by default | Search `"Gaza" "centro de dados"`, `"Xai-Xai" "data center"`, `"Chokwe" servidores`, `"Kuvaninga" SCADA servidores`. Treat energy/control rooms as leads only. |
| Inhambane | Inhambane; Maxixe; Vilankulo; Pande; Temane; Inhassoro | Gas/energy internal-IT lead only | Search `"Inhambane" "centro de dados"`, `"Temane" servidores SCADA`, `"Sasol" Pande Temane "data center"`, `"Central Termica de Temane" servidores`. |
| Maputo | Maputo City; Matola; Tchumene; Boane; Beluluane; Namaacha; Manhica; Matalane; CTM | Highest priority; confirmed commercial/operator and institutional facilities | Verify Raxio, iColo/Digital Realty, Vodacom/Uptime, UEM, CEDSIF, INTIC licenses, EDM Matalane/CTM, APIEX/Beluluane, municipal works. |
| Nampula | Nampula; Nacala; Nacala Corridor | Negative by default, now EDM northern control-center/data-collection lead | Search `"Nampula" "centro de dados"`, `"Nacala" "data center"`, `"EDM" Nampula "Regional Control Center"`, `"UniLurio" servidores`. |
| Cabo Delgado | Cabo Delgado; Pemba; Palma; Afungi; Mocimboa da Praia | LNG/security/telecom internal leads only | Search `"Cabo Delgado" "centro de dados"`, `"Pemba" "data center"`, `"Palma" servidores`, `"TotalEnergies" Afungi servidores`. Count only named sites. |
| Zambezia | Zambezia; Zambézia; Quelimane; Mocuba | Negative by default; energy/education leads only | Search both spellings: `"Zambezia" "centro de dados"`, `"Zambézia" "centro de dados"`, `"Quelimane" "data center"`, `"Mocuba" SCADA servidores`. |
| Sofala | Sofala; Beira; Dondo; Chibata if locally confirmed | Port/rail/university and EDM central control lead | Search `"Sofala" "centro de dados"`, `"Beira" "data center"`, `"CFM" Beira servidores`, `"UniZambeze" servidores`, `"Chibata" EDM`. |
| Tete | Tete; Moatize; Songo; Cahora Bassa; Mphanda Nkuwa | Mining/hydro internal leads only | Search `"Tete" "centro de dados"`, `"Moatize" servidores`, `"HCB" "centro de dados"`, `"Cahora Bassa" servidores`, `"Mphanda Nkuwa" TIC`. |

Promotion rule: outside Maputo, a lead becomes an inventory row only with official/operator naming of a physical facility, a named tender/award, Uptime/certification evidence, or strong press with accountable site details. Otherwise record as negative or C lead.

## 4. Extraction Rules

Extract for every candidate:

```text
name
operator / owner / developer
status: planned | under_construction | operational | licensed | decommissioned | unknown
manifest division
official locality and address
facility type: commercial colo | telecom/operator | government | university | utility/SCADA | enterprise/internal | cloud-service lead
capacity_mw: null unless source-supported
racks / cabinets / sqm: null unless source-supported
source_urls
evidence_date
evidence_grade
notes: why counted, what remains unverified
```

Do not count:

- Cable landing stations, IXPs, PeeringDB presences, CDN PoPs, cloud on-ramps, satellite ground stations or ISP points of presence without a named data-center facility.
- Generic VPS/cloud/hosting pages without a Mozambique physical site.
- Provincial telecom exchanges or server rooms unless a source explicitly calls them a data center or equivalent facility.
- The Prime Minister's 2025 "17/18 data centers" statement as a registry. Use it only as market-size context, noting the source discrepancy: Club of Mozambique reports 17; DCD reports 18.

Final confidence language should be conservative: Mozambique has a real and growing Maputo-centric DC market, an emerging INTIC licensing regime, and a small number of institutional/utility facilities outside pure commercial colo. Non-Maputo provinces remain negative-by-default until named physical evidence appears.
