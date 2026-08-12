# CV Explorer Official — Cabo Verde Datacenter Enumeration via Planning, Regulation, ICT-Agency, Energy, Data-Protection, and Public-Finance Sources

Date: 2026-08-12. Country: **CV Cabo Verde**. Division model: **2 geographical regions** from `world-manifest.jsonl` (subnational_type = `geographical region`, not admin2): **Ilhas de Barlavento** (windward: Santo Antão, São Vicente, Santa Luzia, São Nicolau, Sal, Boa Vista) and **Ilhas de Sotavento** (leeward: Maio, Santiago, Fogo, Brava). Because the manifest layer is geographic regions, every facility record must carry the manifest division **and** the island + concelho (municipality) as the natural sub-layer; searches must combine region, island, and concelho names. Angle: **official / regulatory / primary-source methodology** for finding operational, under-construction, planned, and institutional datacentre facilities.

Reliability grades: **A** = official/primary source that proves the relevant claim (BOE/Gazette or legal instrument, ARME licence/decision, NOSi/government page, AfDB/EIB/World Bank project document, operator official page or official operator account, cloud-provider official region page, certification registry). **B** = reputable press/trade source with named parties, dates, and places (Balai, Inforpress, Expresso das Ilhas, A Semana, Voz do Archipelago, DCD, Developing Telecoms, The Tech Capital, TechAfrica News, Submarine Networks when not the cable owner/operator). **C** = directories, marketplaces, SEO hosting pages, contractor portfolios, social posts, event/sponsor profiles not directly controlled by the operator, republished press, or claims without address/facility evidence.

---

## 0. Verified national baseline

- Cabo Verde is a small island market (10 islands, 22 concelhos). Datacentre-relevant infrastructure is concentrated on **Santiago (Praia)** and, secondarily, **São Vicente (Mindelo)**. All other islands (Santo Antão, São Nicolau, Sal, Boa Vista, Maio, Fogo, Brava, Santa Luzia) may host telecom PoPs, cable/coastal infrastructure, or small server rooms but **no public dedicated datacentre evidence was found in this pass**; record leads only where a primary source appears.
- **TechPark CV Praia campus data centre** (Sotavento / Santiago / Praia). The Parque Tecnológico Arquipélago Digital de Cabo Verde (TechPark CV) is an AfDB-financed national technology park with two campuses (Praia and Mindelo). The AfDB original project report defines the park as “construction and equipment of a data center, business center, incubation center and training and qualification center”. The Praia campus (~15 ha) includes a **Data Center managed by NOSi** (Balai/Inforpress, 2025). Campus buildings were ~85% complete in September 2022 with data-centre completion targeted by end-2022; both campuses were officially inaugurated 2025-05-05 (Praia) and 2025-05-06 (Mindelo). Phase 2 (AfDB loan of €14M/≈US$15.3M signed 2023-08) adds **two data centers and a disaster-recovery site on the São Vicente campus**, run on renewable energy. Total park cost ≈€51.85M with AfDB financing ≈€45.5M (some coverage cites ~US$57M across both phases). ZEET (Zona Económica Especial para Tecnologias, created 2022) gives licensed tenants a 2.5% corporate tax rate — an investment-policy signal, not facility evidence.
- **NOSi data centre, Praia** (Sotavento / Santiago / Praia). Núcleo Operacional da Sociedade de Informação EPE (NOSi, nosi.cv) operates the government data centre in Praia, described by AfDB as an AfDB-supported facility located less than 2 km from the TechPark; the SVOM astronomy/space mission officially hosts its CPV2 station “on the site of the NOSi (DATA CENTER) in Praia”. NOSi lists its address as Edifício Business Center, Parque Tecnológico, Praia — confirm during enumeration whether this is the legacy DC site or the TechPark DC site; **do not merge the two records without address-level proof**.
- **Cabo Verde Telecom (CVTelecom) data centre, Praia** (Sotavento / Santiago / Praia). CVTelecom (the state-owned incumbent) is associated with a **carrier-neutral data centre** and colocation/DC services through event/sponsor material and trade coverage (Africa Tech Festival / Atlantic Convergence-style sponsor profiles; AICEP/Expresso coverage of the CVTelecom PCA statement that the data center is one of the country's principal assets; GCCM West Africa 2024 hosted by CVTelecom). Directories (datacenters.com, colo.exchange, PQ.Hosting) list “Cabo Verde Telecom Data Center in Praia”. Treat this as **B/C until a CVTelecom-controlled page/account, ARME record, BOE notice, municipal licence, or signed operator filing confirms the facility**; exact building address and capacity remain unverified.
- **TechPark CV Mindelo (São Vicente) campus** (Barlavento / São Vicente / Mindelo): second campus inaugurated 2025-05-06; planned **DR site** under phase 2; treat as a lead/planned facility until a primary source states a data hall is built and powered.
- **Praia Data Center (MITT)** — historical record: NRV/Grupo Norvia lists construction supervision 2010–2014 for client **MITT (Ministry of Infrastructure, Telecommunications and Transport)**, Praia, Ilha de Santiago, with a construction-value share of €2,267,270. This appears to be an early government data-centre building; identify which building (NOSi/CNPD/ministry server room) before recording — otherwise keep as a dated lead.
- **Unitel T+ data centre** — contractor portfolio (cvnet.cv) lists a “Data Center UNITEL T+” project; Unitel T+ (Unitel International Holdings group) is the second mobile/ISP operator (commercial launch ~2021). Lead only until ARME licensing, operator filings, or municipal records prove a dedicated facility.
- **Capacity is not public for any facility.** Do not infer MW, racks, sqm, or IT load from AfDB loan values, park cost, cable bandwidth, or marketing claims. Use `capacity_mw: null` unless an explicit primary source states capacity.
- **No AWS/Azure/GCP/OCI Cabo Verde cloud region** was confirmed. Recheck official cloud-region pages on each refresh; reseller/VPS/edge pages are common false positives.
- **Cables landing at Praia** (per DCD, Sept 2022): Cabo Verde Telecom Domestic Submarine Cable, SHARE, WACS, and the **EllaLink** branch (EIB agreed US$25M in 2019 for CVT's connection to EllaLink, part of a US$60M CVT investment program incl. 4G, FTTH, solar). Legacy **Atlantis-2** (RFS 2000) also landed at Praia and was reported disconnected in January 2022 pending upgrade. Cable landing stations and cable heads are **connectivity infrastructure**, not datacentres by default — promote only with server/hosting/colo evidence.
- Honest yield expectation: **3–6 facility/DC records nationwide** (Sotavento: TechPark Praia DC, NOSi DC, CVTelecom DC, MITT historical DC; Barlavento: TechPark Mindelo campus/DR lead; plus Unitel T+ lead), plus connectivity sites (cable landings) and government-internal server-room leads. Do not inflate counts.

---

## 1. Official and primary sources

### 1.1 Planning and building permits (municipal licensing)

Primary route:
- Municipal councils issue construction/occupation licences (licenciamento de obras): **Câmara Municipal da Praia** via the live Loja CMP services portal `https://lojacmp.com/` (licenciamento, aprovação de projecto, licença de construção, consulta/submissão de processos), **Câmara Municipal de São Vicente** `https://www.cmsv.cv` (verify), and the other 20 concelhos' câmaras.
- **Boletim Oficial Eletrónico (BOE)**: `https://boe.incv.cv/` — Imprensa Nacional de Cabo Verde; official gazette for laws, regulations, concessions, and public notices. The BOE site hosts full texts (e.g., Lei 41/VIII/2013 at `boe.incv.cv/Bulletins/View/19888`).
- Government portal `https://www.governo.cv/` hosts documents/attachments including BO issues.

Use câmara records for address, parcel/terreno, building use, generators, cooling plant, telecom rooms, substations, approvals/refusals/conditions, and appeal history. BOE notices can confirm statutory instruments, land concessions, and public-interest declarations (including ZEET licensing rules).

Planning query terms (PT + EN). In search engines, keep each OR group in parentheses; otherwise the query will usually return every page containing the last unscoped term.
```text
("data center" OR "data centre" OR datacenter OR "centro de dados" OR "centro de processamento de dados") ("Cabo Verde" OR "Cape Verde")
("sala de servidores" OR servidor OR hospedagem OR colocation OR colocação) ("Cabo Verde" OR Praia OR Mindelo)
("gerador de emergência" OR "gerador de reserva" OR UPS OR subestação OR arrefecimento OR cooling) ("centro de dados" OR datacenter)
("estação de aterragem" OR "cabo submarino" OR "landing station" OR "estação de cabos") Praia "Cabo Verde"
(TechPark OR "Parque Tecnológico" OR ZEET OR Palmarejo OR "Achada Grande" OR Fazenda OR Várzea) ("data center" OR "centro de dados")
(Praia OR Mindelo OR Santiago OR "São Vicente") ("data center" OR datacenter OR "centro de dados") "Cabo Verde"
("licença de construção" OR licenciamento OR obras) ("data center" OR "centro de dados") "Cabo Verde"
```

Extract from each record: application/licence number, applicant/legal entity, parcel/address, concelho + island + region, development description, floor area if stated, generator/substation/cooling details, decision status/date, conditions, appeal history, and source URL/file.

### 1.2 Communications regulator and telecom law

Primary route:
- **ARME — Agência Reguladora Multissectorial da Economia**: `https://www.arme.cv/`. Created by Decreto-lei nº 50/2018 de 20 de Setembro by merging ARE (energy/water) and ANAC (communications); it regulates communications, energy, water, and urban/interurban passenger transport. Legacy ANAC site: `http://anac.cv/` (now largely mirrored into ARME).
- ARME publishes licence frameworks, regulatory decisions, and the **Regulamento de Partilha de Infraestruturas de Comunicações Eletrónicas** (infrastructure-sharing regulation) — a strong lead source for who owns sites/facilities and for new-entrant infrastructure.
- Operator universe to pivot from: **Cabo Verde Telecom S.A.** (state group; merger of its three operating companies announced), **Unitel T+** (Unitel International Holdings subsidiary; second licensee), plus ISP/telecom licensees (CV Multimédia, CV WiFi, CABOCOM, MB Investimentos, TELMAX — legacy ANAC authorisations; recheck current licences).

ARME establishes the authorised-operator universe and licence classes; it is not a complete facility register. Use it to pivot from licensees to facilities.

Queries:
```text
site:arme.cv ("data center" OR "data centre" OR "centro de dados" OR colocation)
site:arme.cv ("partilha de infraestruturas" OR licenças OR operador)
site:arme.cv ("Cabo Verde Telecom" OR Unitel OR "T+") (licença OR autorização)
site:anac.cv "Cabo Verde" ("data center" OR hosting OR servidores)
(ARME OR ANAC) "Cabo Verde" ("data center" OR "centro de dados")
```

### 1.3 Government ICT: NOSi, Digital Cabo Verde, ministries

Primary routes:
- **NOSi** (Núcleo Operacional da Sociedade de Informação EPE): `https://www.nosi.cv/` — government digital agency, e-gov operator, and the confirmed data-centre operator (TechPark Praia DC + its own Praia DC). NOSi project/portfolio pages (cvnet.cv) and tenders reveal DC infrastructure contracts.
- **World Bank “Digital Cabo Verde” Project P171099**: project appraisal document at `https://documents1.worldbank.org/curated/en/933721603977574627/pdf/Cabo-Verde-Digital-Cabo-Verde-Project.pdf`; project documents at `documents.worldbank.org`. Objective: strengthen digital competitiveness foundations and improve digital public services — includes e-government/data-infrastructure components; check component details for data-centre scope.
- Government portal `https://www.governo.cv/` (ministry portfolios have changed: “Ministério da Economia Digital” created ~2021; by Aug 2026 the portfolio sits under the Minister for Economy, Commerce, Industry and Digital Transition — always re-derive the current ministry and minister from gov.cv before citing).
- IFC Country Private Sector Diagnostic, Cabo Verde (2024): `https://www.ifc.org/content/dam/ifc/doc/2024/cabo-verde-country-private-sector-diagnostic-en.pdf` — names NOSi as a key digital-transformation player (Grade A for institutional facts).
- World Bank Economic Update on digital dividends: `https://www.worldbank.org/en/country/caboverde/publication/cabo-verde-potential-digital-dividends-economic-update-2022` — confirms the digital-dividends policy context; use the linked report/downloads for NOSi and ARME institutional details.

Queries:
```text
site:nosi.cv ("data center" OR "centro de dados" OR cloud OR hosting OR "data centre")
site:nosi.cv (TechPark OR "Parque Tecnológico" OR "Business Center")
site:gov.cv ("data center" OR "centro de dados" OR nuvem OR cloud OR digital)
site:governo.cv (concursos OR contrato) ("data center" OR "centro de dados" OR hosting)
"Digital Cabo Verde" P171099 ("data center" OR "data centre" OR infraestrutura)
```

### 1.4 Data protection (demand + processing-authorisation signals)

Primary route:
- **CNPD — Comissão Nacional de Proteção de Dados**, created under Lei nº 41/VIII/2013 de 17 de Setembro (BOE I Série n.º 48, 2013-09-17; full text at the official BOE record `https://boe.incv.cv/Bulletins/View/19888`), which amends the 2001 regime (Lei 133/V/2001); CNPD became effective in practice ~2015 and operates alongside the National Assembly.

Data-protection law creates registration/authorisation duties for processing operations, which can surface who hosts personal data (banks, telecoms, health, government). This is a demand-side and compliance-signal route, not a facility register.

Queries:
```text
(CNPD OR "Comissão Nacional de Proteção de Dados") "Cabo Verde" ("data center" OR servidores OR hosting)
site:redipd.org Cabo Verde CNPD
"Lei 41/VIII/2013" "Cabo Verde" ("data center" OR armazenamento OR servidores)
```

### 1.5 Energy, utilities, and environment

Primary routes:
- **ELECTRA S.A.** (Empresa de Electricidade e Água): `http://www.electra.cv/` — incumbent utility (production/distribution/commercialisation; restructured from 2024-06-01 into new companies, including **EDEC — Empresa de Distribuição de Eletricidade de Cabo Verde** `https://www.edec.cv/`, created 2024-07-01).
- **MICE / DNICE** — Ministério da Indústria, Comércio e Energia and Direcção Nacional de Indústria, Comércio e Energia (government/ministry route via `https://www.governo.cv/` and commerce portal ministry page `https://portaldocomercio.gov.cv/en/web/portal/leis-e-normas/-/asset_publisher/bmgx/content/mice-ministerio-da-industria-comercio-e-energia-1`; recheck the current ministry structure before citing).
- **ARME** energy regulation (tariffs, access to networks, renewable generation) — see 1.2.

Use energy records as corroboration for large electrical loads, substations, standby generation, fuel storage, or EIA conditions. Do not promote a site solely because it has a generator or telecom power connection. TechPark phase 2 is explicitly designed for renewable-energy-powered DCs — energy-project records around the Praia/Mindelo campuses are high-signal.

Queries:
```text
(site:electra.cv OR site:edec.cv) ("data center" OR "centro de dados" OR subestação OR MVA OR kVA)
(site:governo.cv OR site:portaldocomercio.gov.cv) (DNICE OR energia OR renovável OR "grandes clientes")
site:arme.cv eletricidade ("data center" OR "grande consumidor" OR tarifa)
"Cabo Verde" ("data center" OR "centro de dados") ("energia renovável" OR solar OR subestação)
(TechPark OR "Parque Tecnológico") (Praia OR Mindelo) (energia OR eletricidade OR backup)
```

### 1.6 Public procurement, project financing, and concessions

Primary routes (all Grade A for the project/financing claim):
- **AfDB (Banco Africano de Desenvolvimento)**: TechPark CV financing — project/event pages, e.g. `https://www.afdb.org/en/news-and-events/events/inauguration-cabo-verdes-technology-park-praia-and-mindelo-83348`, NOSi DC visit story `https://www.afdb.org/en/news-and-events/african-development-banks-support-propel-cabo-verdes-efforts-become-regional-ict-hub-54656`, Mindelo release `https://www.afdb.org/en/news-and-events/press-releases/african-development-bank-funds-second-tech-park-mindelo-83646`, €14M phase-2 loan release `https://www.afdb.org/en/news-and-events/press-releases/cabo-verde-eu14-million-loan-african-development-bank-will-strengthen-role-regional-tech-hub-63363`, and MapAfrica project pages for the Technology Park and Phase II. AfDB committed ≈€45.5M (park) + €14M (phase 2), cited by some outlets as ≈US$57M across both phases.
- **EIB**: EllaLink/Cabo Verde Telecom connection financing (US$25M, agreed 2019; official press page `https://www.eib.org/en/press/all/2019-171-eib-backs-high-speed-cabo-verde-internet-and-telecom-connection`; EIB says the loan supports a US$60M CVTelecom programme covering 4G, FTTH, solar power for the telecom network, and the EllaLink connection).
- **World Bank**: Digital Cabo Verde P171099 (see 1.3).
- Government procurement: `governo.cv` concursos/notices and BOE contract publications; there is no single confirmed national e-procurement portal in this pass — search `site:governo.cv concursos` and confirm the current portal during enumeration.

Queries:
```text
site:afdb.org Cabo Verde ("data center" OR "technology park" OR TechPark OR NOSi)
site:eib.org Cabo Verde (telecom OR "submarine cable" OR "Cabo Verde Telecom")
site:governo.cv concursos ("data center" OR "centro de dados" OR hosting OR cloud)
(concurso OR contrato) "Cabo Verde" ("data center" OR "centro de dados") (Praia OR Mindelo)
```

### 1.7 Submarine cable primary/connectivity chain

| Cable / system | Best sources | Cabo Verde signal | Enumeration handling |
|---|---|---|---|
| **EllaLink branch** | EIB, CVTelecom official pages, Submarine Networks, DCD | EIB agreed US$25M (2019) for CVT to connect Cabo Verde to EllaLink (Portugal–Brazil system); DCD (2022-09-13) lists EllaLink among Praia landings, launched 2021; CVT's US$60M program covers 4G/FTTH/solar alongside the cable. | Praia landing/connectivity lead. Verify RFS and exact landing-station address via CVTelecom/Submarine Networks. Not a DC. |
| **WACS** | WACS consortium pages, TeleGeography/submarinecablemap, DCD | DCD lists WACS among Praia landings. | Verify against TeleGeography; if confirmed, treat as connectivity site. Not a DC. |
| **SHARE** | DCD (Sept 2022), TeleGeography | DCD lists the SHARE cable at Praia. | Verify; connectivity site unless hosting evidence appears. |
| **CVT Domestic Submarine Cable** | CVTelecom, DCD, BOE | Inter-island domestic cable system operated by CVTelecom; DCD lists it at Praia; CVTelecom launched an international tender to replace inter-island optical fibre (DCD). | Connectivity backbone, not a DC. Its landing stations may host PoP equipment only. |
| **Atlantis-2** | Wikipedia/TeleGeography, cable industry archives | RFS May 2000; landing at **Praia**, Cabo Verde; reported disconnected 2022-01-10 pending upgrade (Wikipedia). | Legacy connectivity record; do not promote to DC without hosting evidence. |

Cable queries:
```text
("Cabo Verde" OR "Cape Verde") Praia ("landing station" OR "cabo submarino" OR "submarine cable")
EllaLink ("Cabo Verde" OR "Cabo Verde Telecom") (Praia OR RFS OR landing)
(WACS OR SHARE) "Cabo Verde" Praia landing
"Cabo Verde Telecom" ("domestic submarine cable" OR fibra OR "fibra inter-ilhas" OR inter-island)
site:submarinenetworks.com ("Cabo Verde" OR "Cape Verde")
```

### 1.8 Official cloud-region absence checks

Check the official pages on every refresh:
- AWS regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

As of this methodology pass, none lists a Cabo Verde cloud region/local zone. Record local reseller/VPS/cloud pages as service evidence only unless a hyperscaler official page names Cabo Verde.

---

## 2. Division coverage workflow

Run the universal workflow for **each of the 2 manifest regions**, then for each island/concelho within the region. The tables below are the coverage checklist; every island/concelho must be either assigned a verified project/lead or explicitly marked no public project found.

### 2.1 Ilhas de Barlavento (windward)

| Island (concelhos) | Priority | Official-first route |
|---|---:|---|
| Santo Antão (Ribeira Grande, Paul, Porto Novo) | Low | Municipal câmaras, BOE, ARME licences; telecom PoPs only unless primary DC evidence appears |
| São Vicente (São Vicente — Mindelo) | High | TechPark CV Mindelo campus + phase-2 DR site; Câmara Municipal de São Vicente licensing; EDEC/Electra power records; ARME |
| Santa Luzia (uninhabited) | None | No concelho/no population; record explicitly as no public project found |
| São Nicolau (Ribeira Brava, Tarrafal de São Nicolau) | Low | Generic câmara/BOE/ARME sweep |
| Sal (Sal — Espargos/Santa Maria) | Medium | Telecom PoPs, airport-zone hosting, cable/coastal records; câmara licensing; no DC without primary evidence |
| Boa Vista (Boa Vista — Sal Rei) | Low | Generic câmara/BOE sweep; tourism-sector server-room leads only |

### 2.2 Ilhas de Sotavento (leeward)

| Island (concelhos) | Priority | Official-first route |
|---|---:|---|
| Santiago (Praia, Ribeira Grande de Santiago, São Domingos, Santa Cruz, São Lourenço dos Órgãos, São Salvador do Mundo, Santa Catarina, **São Miguel**, Tarrafal) | High | **Praia**: TechPark Praia DC (NOSi-managed), NOSi DC, CVTelecom DC, MITT historic DC, cable landings; Câmara Municipal da Praia licensing; ARME; NOSi; BOE; EDEC/Electra; AfDB/World Bank project docs. Other Santiago concelhos: generic sweep |
| Maio (Maio — Vila do Maio) | Low | Generic câmara/BOE sweep; no DC without primary evidence |
| Fogo (São Filipe, Mosteiros, Santa Catarina do Fogo) | Low | Generic câmara/BOE/ARME sweep; telecom PoPs |
| Brava (Brava — Nova Sintra) | Low | Generic câmara/BOE sweep; no DC without primary evidence |

Universal query template (region + island + concelho):
```text
("{island}" OR "{concelho}") "Cabo Verde" ("data center" OR "data centre" OR datacenter OR "centro de dados" OR "sala de servidores")
("{island}" OR "{concelho}") "Cabo Verde" (telecom OR "cabo submarino" OR "landing station" OR "estação de cabos" OR "network operations")
("{island}" OR "{concelho}") "Cabo Verde" (gerador OR UPS OR subestação OR energia OR "backup power")
site:boe.incv.cv "{concelho}" ("data center" OR telecom OR "centro de dados" OR subestação)
site:arme.cv ("{concelho}" OR "{island}") (licença OR autorização OR operador)
site:governo.cv "{island}" ("data center" OR hosting OR "centro de dados" OR cloud)
```

---

## 3. Facility seed list for enumerators

This is a seed list, not the final census. Reverify each record during enumeration and preserve null capacity where no explicit capacity source exists.

| Seed | Preferred assignment (region / island / concelho) | Status | Grade | Best evidence path |
|---|---|---|---|---|
| TechPark CV Praia campus data centre (NOSi-managed) | Sotavento / Santiago / Praia | Operational (campus inaugurated 2025-05-05; DC completed ~end-2022) | A for park/DC project (AfDB docs, NOSi, Balai/Inforpress); verify DC building status at address level | AfDB project docs & event page; NOSi (nosi.cv); Balai/Inforpress/Expresso das Ilhas 2025 inauguration coverage; CMP licensing; ZEET legal instruments (BOE) |
| NOSi data centre, Praia (legacy AfDB-backed) | Sotavento / Santiago / Praia | Operational | A for existence (AfDB, SVOM CPV2 hosting page, NOSi) | AfDB NOSi story; svom.eu CPV2 station page; nosi.cv; verify exact address vs TechPark DC — do not merge |
| Cabo Verde Telecom data centre, Praia | Sotavento / Santiago / Praia | Operational service claim; address/capacity unverified | B/C until confirmed by CVTelecom-controlled, ARME, BOE, or câmara source; C for directory address/specs | CVTelecom official site/filings/accounts; Africa Tech Festival / Atlantic Convergence sponsor material; AICEP/GCCM coverage; CMP licensing; ARME licence |
| TechPark CV Mindelo campus + phase-2 DR site | Barlavento / São Vicente / Mindelo | Planned/under-development (campus inaugurated 2025-05-06; DR under phase 2) | A for campus/phase-2 financing (AfDB); DC/DR build status needs primary proof | AfDB Mindelo release & phase-2 loan docs; CMSV licensing; EDEC/Electra power records; Balai/Expresso das Ilhas |
| Praia Data Center (MITT, 2010–2014) | Sotavento / Santiago / Praia | Historical/institutional | C+ contractor seed until current primary proof | NRV/Grupo Norvia project page; match to NOSi/ministry/central-bank building via BOE/câmara records |
| Unitel T+ data centre | Sotavento / Santiago / Praia (verify island) | Lead | C until primary | cvnet.cv project page; ARME licence/decision; uniteltmais.cv; câmara licensing |
| Government/e-gov hosting (Digital Cabo Verde cloud migration) | Sotavento / Santiago / Praia (NOSi-managed) | Lead | B until facility/tender proof | World Bank P171099 docs; NOSi; gov.cv; BOE contract publications |
| EllaLink / WACS / SHARE / CVT Domestic / Atlantis-2 landings | Praia (verify each) | Connectivity site | A for cable facts where primary; not DC | EIB; CVTelecom; DCD; TeleGeography/submarinecablemap; Wikipedia (Atlantis-2) |

---

## 4. Pitfalls and decision rules

- **Geographic regions are not administrative divisions.** The manifest division is “Ilhas de Barlavento” / “Ilhas de Sotavento”; always attach island + concelho (e.g., “Sotavento / Santiago / Praia”) and record the region exactly as spelled in the manifest. Never invent a division not in the manifest.
- **NOSi DC vs TechPark DC are two records unless proven one site.** Balai says the TechPark Praia DC is NOSi-managed; AfDB and DCD describe a separate legacy NOSi DC <2 km away. Duplicate-risk is real: require address/parcel evidence before merging.
- **Portuguese vs English terminology.** Use “centro de dados”, “datacenter”, “centro de processamento de dados”, “sala de servidores”, “hospedagem”, “coloção”, “estação de aterragem de cabos” alongside “data center”; Cabo Verde sources are predominantly Portuguese-language.
- **Financing ≠ capacity.** AfDB loan values (€14M, €45.5M/€51.85M park, US$57M aggregate), EIB US$25M cable support, and CVT's US$60M program are project-financing facts, not MW/rack figures. Keep `capacity_mw: null` unless an explicit primary source states capacity.
- **Cable landings are not datacentres.** Keep cable records in notes/connectivity unless server/hosting/colo evidence is explicit.
- **Ministry portfolio churn.** Ministry names changed repeatedly (MITT → … → Ministério da Economia Digital → Economy/Commerce/Industry/Digital Transition by 2026). Re-derive the current portfolio from gov.cv before citing a ministry in a record.
- **Directory pollution and false “Cape Verde” results.** Always include “Cabo Verde” or “Cape Verde” plus an island/concelho; bare “CV” matches are noisy. Treat datacenters.com/colo.exchange/PQ.Hosting/DataCenterMap entries as Grade C seeds until matched to a primary.
- **techpark.cv may be a stub.** The official domain exists but content can be thin; cross-check park claims against AfDB/government/press rather than the park site alone.
- **Cloud-region absence is a checked fact, not an assumption.** Re-verify AWS/Azure/GCP/OCI pages each refresh; reseller pages are false positives.
- **No deletion in enumeration.** If an old lead cannot be verified, retain it as a lead with downgraded grade and a note naming the missing evidence rather than silently dropping it.
