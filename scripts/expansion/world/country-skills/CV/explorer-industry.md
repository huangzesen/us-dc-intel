# CV Explorer Industry — Cabo Verde Datacenter Enumeration via Operators, Connectivity Infrastructure, Trade Press, and Island Query Patterns

Date: 2026-08-12. Country: **CV Cabo Verde**. Scope: industry/operator-led datacentre discovery across the 2 `world-manifest.jsonl` geographical regions (**Ilhas de Barlavento**, **Ilhas de Sotavento**), using island + concelho sub-layers because the manifest layer is not administrative. Reliability grades: **A** = operator-controlled/certification/cable/cloud/government primary source that proves the claim; **B** = reputable local or trade press with named parties, dates, and places; **C** = directory, marketplace, contractor portfolio, social, event/sponsor profile not directly controlled by the operator, SEO hosting, or unverified aggregate evidence.

---

## 0. Market shape and verified facts

- The Cabo Verde datacentre market is small and state/telecom-led. All confirmed facility activity is in **Praia (Santiago, Sotavento)** with a second pole forming at **Mindelo (São Vicente, Barlavento)** via the TechPark CV second campus.
- **TechPark CV** (Parque Tecnológico Arquipélago Digital de Cabo Verde): AfDB-financed national tech park (≈€51.85M project, AfDB ≈€45.5M; ≈US$57M across both phases per some outlets). Praia campus ~15 ha with five components including a **Data Center managed by NOSi**; second campus in Mindelo with a phase-2 **DR site**; €14M phase-2 loan signed 2023-08-01 for two data centers; campuses inaugurated 2025-05-05 (Praia) and 2025-05-06 (Mindelo); ZEET special economic zone for technologies created 2022 (2.5% corporate tax for qualifying tenants). Companies that expressed interest/attended: Microsoft, Intel, Huawei, Unitel, AfriLabs, Smart Africa.
- **NOSi** (Núcleo Operacional da Sociedade de Informação EPE): government ICT agency and DC operator; legacy AfDB-backed data centre in Praia (<2 km from TechPark per DCD) and manager of the TechPark Praia DC. SVOM hosts its CPV2 satellite station “on the site of the NOSi (DATA CENTER) in Praia” (svom.eu). NOSi address listed as Edifício Business Center, Parque Tecnológico, Praia — resolve legacy-vs-TechPark identity at address level.
- **Cabo Verde Telecom (CVTelecom)** S.A.: state incumbent; associated with a **carrier-neutral data centre** through event/sponsor material and trade coverage (Africa Tech Festival / Atlantic Convergence-style sponsor profiles; CVTelecom PCA statements via AICEP; GCCM West Africa 2024 host). Directories list “Cabo Verde Telecom Data Center in Praia”. Treat the DC service claim as **B/C until confirmed by a CVTelecom-controlled page/account, ARME record, BOE notice, municipal licence, or signed operator filing**; exact address/capacity unverified. CVTelecom also runs the international cable chain (EllaLink branch, domestic cable, inter-island fibre replacement tender) and announced the merger of its three group operating companies.
- **Unitel T+**: second operator (Unitel International Holdings group; commercial launch ~2021); a contractor portfolio (cvnet.cv) lists a “Data Center UNITEL T+” project — lead only.
- **Praia Data Center (MITT)**: NRV/Grupo Norvia supervised construction 2010–2014 for MITT, Praia, Santiago (construction-value share €2.27M) — historical government DC record; match to a specific building before recording.
- No MW/rack/sqm figures are public for any facility. Set `capacity_mw: null` unless a primary source explicitly states a value.
- No independent colocation vendor beyond CVTelecom, and no AWS/Azure/GCP/OCI Cabo Verde region, were confirmed in this pass. Local VPS/hosting/managed-IT/cloud-reseller pages are leads only.
- Cables at Praia (per DCD 2022-09-13): CVT Domestic Submarine Cable, SHARE, WACS, EllaLink (EIB-backed CVT branch); legacy Atlantis-2 (RFS 2000, reported disconnected Jan 2022). They are connectivity infrastructure unless hosting/datacentre evidence appears.
- Honest yield: expect **3–6 facility records** nationwide (Sotavento: TechPark Praia DC, NOSi DC, CVTelecom DC, MITT historic; Barlavento: TechPark Mindelo campus/DR; plus Unitel T+ lead) and connectivity-site records. Do not inflate.

---

## 1. Priority operator and infrastructure sweep

| Lead | Source route | Locality/district handling | Evidence grade and action |
|---|---|---|---|
| TechPark CV Praia data centre (NOSi-managed) | AfDB project/event pages; NOSi (nosi.cv); Balai, Inforpress, Expresso das Ilhas, Bantumen, RSTP, Voz do Archipelago inauguration coverage; DCD 2022/2023; Tech Africa News; WeAreTech | Sotavento / Santiago / Praia; Praia campus ~15 ha; DC within park campus | **A** for park/DC project and financing; **B** for press dates. Verify DC building operational status at address level; capacity null. |
| NOSi data centre, Praia (legacy) | AfDB (Adesina visit story, “regional ICT hub”); svom.eu CPV2 station page; nosi.cv; IFC CPSD 2024; World Bank Economic Update | Sotavento / Santiago / Praia; <2 km from TechPark; address “Edifício Business Center, Parque Tecnológico” to verify | **A** for existence/role. Do not merge with TechPark DC without parcel evidence. |
| CVTelecom data centre, Praia | CVTelecom official site/accounts and filings; Africa Tech Festival / Atlantic Convergence-style sponsor material; AICEP (PCA statements); GCCM West Africa 2024; directories datacenters.com / colo.exchange / PQ.Hosting | Sotavento / Santiago / Praia; carrier-neutral colocation claim; exact building unverified | **B/C** until confirmed by CVTelecom-controlled, ARME, BOE, or câmara source; **C** for directory address/specs. Check ARME licence and CMP licensing for the building. |
| TechPark CV Mindelo campus + phase-2 DR site | AfDB Mindelo financing release and phase-2 loan docs; Balai; Expresso das Ilhas; CMSV licensing; EDEC/Electra power records | Barlavento / São Vicente / Mindelo | **A** for campus/financing; **B** for press dates; DR/DC build status needs primary proof; capacity null. |
| Unitel T+ data centre | cvnet.cv project page; ARME licence/decisions; uniteltmais.cv; santiagomagazine (network/access disputes); câmara licensing | Sotavento / Santiago / Praia (verify island) | Lead only (**C**) until primary facility proof. |
| Praia Data Center (MITT 2010–2014) | NRV/Grupo Norvia project page (client MITT, Praia, Santiago) | Sotavento / Santiago / Praia | **C+** contractor seed until matched to current building/operator via BOE/câmara/NOSi records. |
| Government cloud / Digital Cabo Verde migration | World Bank P171099 PID & project docs; NOSi; gov.cv; BOE | Sotavento / Santiago / Praia (NOSi-managed) | **A** for project facts; DC scope inside components to verify; record only with facility/tender proof. |
| EllaLink / WACS / SHARE / CVT Domestic / Atlantis-2 landings | EIB; CVTelecom; DCD; TeleGeography/submarinecablemap; Wikipedia (Atlantis-2); Submarine Networks | Praia (verify each landing station); CVT Domestic = inter-island | Cable facts **A/B**; not DCs without hosting/server evidence. |

Operator query templates (EN + PT):
```text
(TechPark OR "Parque Tecnológico") "Cabo Verde" ("data center" OR "centro de dados") (NOSi OR Praia OR Mindelo)
NOSi ("data center" OR "centro de dados") Praia "Cabo Verde"
"Cabo Verde Telecom" ("data center" OR datacenter OR colocation OR "centro de dados" OR "carrier-neutral")
CVTelecom (EllaLink OR "domestic submarine cable" OR fibra)
"Unitel T+" ("data center" OR "centro de dados" OR infraestrutura)
"Cabo Verde" ("data center" OR "centro de dados") ("gerido pelo NOSi" OR DR OR "disaster recovery")
(Praia OR Mindelo) ("data center" OR "centro de dados") ("Cabo Verde" OR "Cape Verde")
```

---

## 2. Industry and press sources

| Source | URL | Use | Grade rule |
|---|---|---|---|
| AfDB | https://www.afdb.org/ (TechPark inauguration event 83348; NOSi DC story 54656; Mindelo release 83646; €14M phase-2 loan release 63363; MapAfrica project pages) | TechPark/NOSi financing and facility facts | A |
| World Bank | https://documents.worldbank.org/ (Digital Cabo Verde P171099 PID/ISDS) | Digital-economy project scope and e-gov hosting | A |
| IFC | https://www.ifc.org/ (Country Private Sector Diagnostic 2024 PDF) | NOSi role, private-sector digital landscape | A for institutional facts |
| EIB | https://www.eib.org/en/press/all/2019-171-eib-backs-high-speed-cabo-verde-internet-and-telecom-connection | EllaLink/Cabo Verde Telecom US$25M financing and US$60M CVT investment program | A for financing facts |
| NOSi | https://www.nosi.cv/ | DC operator, e-gov, address; TechPark DC manager | A for company/facility claims |
| TechPark CV | https://www.techpark.cv/ | Park official claims; may be a thin/stub site — cross-check | A if live and specific; C if stub |
| Cabo Verde Telecom / Alou | https://www.alou.cv/ plus official CVTelecom accounts/filings | Operator identity, DC/colocation claims, cables | A for claims on operator-controlled pages/accounts; otherwise B/C |
| Unitel T+ | https://www.uniteltmais.cv/ | Operator identity, services, network claims | A for company facts on operator-controlled pages; C for DC until primary facility proof |
| CVNet | https://cvnet.cv/ (project pages: NOSi DC, Unitel T+ DC, Banco de Cabo Verde) | Contractor portfolio evidence for DC builds | C unless matched to client primary records |
| NRV / Grupo Norvia | https://www.nrv-norvia.com/en/projects/praia-data-center | MITT Praia Data Center supervision record | C+ contractor seed unless matched to client primary records |
| SVOM | https://www.svom.eu/en/cape-verde-cpv2-station/ | CPV2 hosted at NOSi DC, Praia (coordinates ~14.92N, -23.51W) | A for hosting fact |
| DCD | https://www.datacenterdynamics.com/ (2022-09-13 TechPark DC timeline; 2023-08-01 €14M loan; CVT fibre tender) | TechPark/NOSi/CVT project news and cable list | B; A only when quoting a primary page |
| Balai | https://www.balai.cv/ | Inauguration coverage; “Data Center gerido pelo NOSi”; PM statements | B |
| Inforpress / Expresso das Ilhas | https://inforpress.cv/ ; https://expressodasilhas.cv/ | National agency and press coverage | B |
| A Semana / Santiago Magazine / Voz do Archipelago | https://asemana.cv/ ; Santiago Magazine by source-name search; https://vozdoarchipelago.cv/ | Regulatory/network and TechPark coverage | B; A Semana may return 403 to command-line clients; Santiago Magazine is indexed but did not pass direct curl validation |
| Tech Africa News / WeAreTech / fintechnews.africa | https://techafricanews.com/ ; https://www.wearetech.africa/ ; https://fintechnews.africa/ | Inauguration and financing summaries (incl. US$57M figure) | B |
| The Tech Capital / Developing Telecoms / Africa Business | https://thetechcapital.com/ ; https://www.developingtelecoms.com/ ; https://african.business/ | Regional financing/DC context | B |
| AICEP / Africa Tech Festival / Atlantic Convergence-style sponsor material | https://www.aicep.com/ ; https://africatechfestival.com/ | CVTelecom PCA statements; carrier-neutral DC claim | B/C unless the page is operator-controlled or links to a CVTelecom primary source |
| TeleGeography / Submarine Networks | https://www.submarinecablemap.com/ ; https://www.submarinenetworks.com/ | Cable landings (EllaLink/WACS/SHARE/Atlantis-2/CVT domestic) | A for operator/system primary pages; B for reporting |
| Wikipedia | https://en.wikipedia.org/wiki/Atlantis-2 | Atlantis-2 landing at Praia; disconnect report Jan 2022 | C (verify via TeleGeography/primary) |
| Directories | datacenters.com (CVTelecom DC; TechPark Praia Campus DC), colo.exchange, PQ.Hosting, DataCenterMap (NOSi profile) | Seed discovery only | C until matched to primary |
| Social media | Facebook/LinkedIn (TechPark CV, CVTelecom, NOSi, Unitel T+) | Change feed and marketing claims | C unless official account links a primary document |

Press/trade query templates:
```text
site:balai.cv ("data center" OR "centro de dados" OR TechPark)
site:expressodasilhas.cv ("data center" OR "centro de dados" OR TechPark)
site:inforpress.cv ("data center" OR "centro de dados" OR NOSi)
site:datacenterdynamics.com ("Cape Verde" OR "Cabo Verde") ("data center" OR "centro de dados")
site:thetechcapital.com ("Cape Verde" OR "Cabo Verde")
site:developingtelecoms.com ("Cabo Verde" OR "Cape Verde")
site:techafricanews.com (TechPark OR "Cabo Verde")
site:submarinenetworks.com ("Cabo Verde" OR "Cape Verde" OR EllaLink)
```

---

## 3. Directory-to-primary workflow

1. Seed only from directories/marketplaces: datacenters.com, colo.exchange, PQ.Hosting, DataCenterMap, Baxtel, PeeringDB, CDN PoP lists, hosting-provider pages.
2. Search exact facility/operator/address against primary domains: `arme.cv`, `nosi.cv`, `techpark.cv`, `cvtelecom.cv`, `uniteltmais.cv`, `governo.cv`, `boe.incv.cv`, `afdb.org`, `eib.org`, `documents.worldbank.org`.
3. Verify location through municipal licensing (Câmara Municipal da Praia / São Vicente), parcel/address, ARME licence, operator official address, or a certification/project document. Always record region + island + concelho.
4. Verify status with launch/inauguration/certification/operational-service evidence (e.g., 2025-05-05/06 TechPark inauguration; CVTelecom DC service pages). Use `announced` or `lead` if only a planned project or press statement exists.
5. Keep directory-only entries as Grade C; do not merge them into confirmed facilities unless name/address/operator line up.

Negative-control queries:
```text
"Cabo Verde" (colocation OR "co-location" OR provider OR "carrier-neutral")
"Cabo Verde" ("cloud hosting" OR VPS OR "dedicated server" OR hospedagem)
"Cabo Verde" (AWS OR Azure OR "Google Cloud" OR OCI) ("data center" OR region)
"Cape Verde" "data center" -"Cabo Verde" -Praia
"CV" "data center" -"Cabo Verde"
```

---

## 4. Island/division recipes for the 2 manifest regions

Use the exact manifest spellings in records (“Ilhas de Barlavento”, “Ilhas de Sotavento”); add island/concelho names in queries.

Universal island query:
```text
"{island}" "Cabo Verde" ("data center" OR "data centre" OR datacenter OR "centro de dados" OR colocation OR "sala de servidores")
"{island}" "Cabo Verde" ("network operations" OR telecom OR "cabo submarino" OR "landing station" OR "estação de cabos")
"{island}" "Cabo Verde" (gerador OR UPS OR subestação OR cooling OR "backup power" OR energia)
site:balai.cv "{island}" ("data center" OR telecom OR servidores)
site:expressodasilhas.cv "{island}" ("data center" OR telecom)
site:arme.cv ("{island}" OR "{concelho}") (licença OR operador OR telecomunicações)
site:governo.cv "{island}" ("data center" OR "centro de dados" OR hosting)
site:boe.incv.cv "{concelho}" ("data center" OR telecom OR subestação)
```

High-yield variants:
```text
Praia (TechPark OR "Parque Tecnológico") ("data center" OR "centro de dados") NOSi
Praia "Cabo Verde Telecom" (datacenter OR colocation OR "carrier-neutral" OR "centro de dados")
Praia NOSi ("data center" OR "centro de dados" OR SVOM)
(Mindelo OR "São Vicente") (TechPark OR "data center" OR "centro de dados" OR "disaster recovery" OR DR)
"Unitel T+" ("data center" OR "centro de dados")
Praia ("landing station" OR "cabo submarino") (EllaLink OR WACS OR SHARE OR "Atlantis-2")
("Santo Antão" OR "São Nicolau" OR Sal OR "Boa Vista" OR Maio OR Fogo OR Brava) ("data center" OR "centro de dados" OR servidores)
```

Region checklist and expected handling:

| Manifest division | Islands / concelhos | Expected yield | Notes |
|---|---|---|---|
| Ilhas de Barlavento | Santo Antão (Ribeira Grande, Paul, Porto Novo); São Vicente (Mindelo); Santa Luzia (uninhabited); São Nicolau (Ribeira Brava, Tarrafal de São Nicolau); Sal; Boa Vista | Medium (São Vicente high) | Mindelo: TechPark campus + DR lead. Other islands: PoPs/fibre only; no DC without primary proof. Santa Luzia: record explicitly as no public project found. |
| Ilhas de Sotavento | Santiago (Praia + 8 other concelhos: Ribeira Grande de Santiago, São Domingos, Santa Cruz, São Lourenço dos Órgãos, São Salvador do Mundo, Santa Catarina, São Miguel, Tarrafal); Maio; Fogo (São Filipe, Mosteiros, Santa Catarina do Fogo); Brava | High (Praia) / low elsewhere | Praia: TechPark DC, NOSi DC, CVTelecom DC, MITT historic DC, Unitel T+ lead, cable landings. Other concelhos/islands: generic sweep; no DC without primary proof. |

---

## 5. Seed records to validate during enumeration

| Seed | Status | Capacity | Developer/operator | Grade | Sources to use |
|---|---|---|---|---|---|
| TechPark CV Praia campus data centre | Operational (campus inaugurated 2025-05-05) | null | TechPark CV / NOSi (operator); AfDB-financed | A for project; verify building status | AfDB, NOSi, Balai/Inforpress/Expresso das Ilhas, CMP licensing, ZEET legal instruments |
| NOSi data centre, Praia (legacy) | Operational | null | NOSi EPE; AfDB-supported | A | AfDB, svom.eu CPV2, nosi.cv; address-level split from TechPark DC |
| Cabo Verde Telecom data centre, Praia | Operational service claim; address/capacity unverified | null | Cabo Verde Telecom S.A. | B/C until confirmed by CVTelecom-controlled, ARME, BOE, or câmara source; C for directory specs | cvtelecom.cv/accounts, Africa Tech Festival / Atlantic Convergence-style material, AICEP, ARME, CMP licensing |
| TechPark CV Mindelo campus / phase-2 DR site | Planned/under-development | null | TechPark CV; AfDB phase-2 financing | A for financing; B for dates | AfDB releases, CMSV licensing, EDEC/Electra, Balai/Expresso das Ilhas |
| Praia Data Center (MITT) | Historical/institutional | null | MITT client; NRV supervision | C+ | NRV project page; BOE/câmara/NOSi matching |
| Unitel T+ data centre | Lead | null | Unitel T+ (Unitel International Holdings group) | C until primary | cvnet.cv, ARME, uniteltmais.cv, câmara licensing |
| Government cloud / Digital Cabo Verde hosting | Lead | null | NOSi / Government of Cabo Verde | B until tender/facility proof | World Bank P171099, NOSi, gov.cv, BOE |
| EllaLink / WACS / SHARE / CVT Domestic / Atlantis-2 landings | Connectivity sites | null | CVTelecom (EllaLink branch; domestic cable); consortium/carriers for WACS/SHARE; Atlantis-2 consortium | A/B for cable; not DC | EIB, CVTelecom, DCD, TeleGeography, Wikipedia (Atlantis-2) |

---

## 6. Capacity and reliability extraction

Record these fields when available: operator, facility name, address, island/concelho/region, status, inauguration/launch dates, financing (loan values, park cost), certification if any, connectivity/cable adjacency, tenant types (government, banks, telecoms), and ZEET/park-zone affiliation.

Do not derive capacity from:
- AfDB loan values (€14M phase 2; €45.5M/€51.85M park; US$57M aggregate claims).
- EIB US$25M cable financing or CVT's US$60M program.
- WACS/SHARE/EllaLink/Atlantis-2 bandwidth or cable capex.
- Marketing claims such as “carrier-neutral”, “world-class”, “Tier III”, “state-of-the-art” without a registry entry (no TIA/Uptime certification entries were found for CV in this pass — treat any such claim as unverified until a certification registry appears).

Capacity query templates:
```text
(TechPark OR "centro de dados") "Cabo Verde" (rack OR racks OR sqm OR MW OR MVA OR kVA OR capacidade)
NOSi "data center" Praia (rack OR racks OR MW OR capacidade OR Tier)
"Cabo Verde Telecom" datacenter (rack OR MW OR capacidade OR Tier)
"Cabo Verde" "data center" (capacidade OR MW OR potência OR racks)
"Unitel T+" "data center" (capacidade OR racks OR MW)
```

Reliability grading rules:
- **A**: AfDB/EIB/World Bank/government/operator-controlled/NOSi/ARME/BOE source proves the facility, address, status, or financing.
- **B**: press/trade source supports dates, financing figures, inauguration, or cable events but does not independently prove a facility/address.
- **C**: directory/social/hosting/event-sponsor page only, or a contractor portfolio page not matched to a client primary record.

Pitfalls: do not merge NOSi legacy DC with the TechPark DC; do not treat ZEET tax status, park financing, or cable landings as datacentre capacity; keep both manifest regions in the sweep even where prior passes found no projects; always include an island/concelho plus “Cabo Verde” in searches (bare “CV”/“Cape Verde” cause false positives); record Santa Luzia as explicitly no public project found.
