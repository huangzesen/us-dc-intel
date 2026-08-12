# AO Explorer Industry - Angola Datacenter Enumeration via Trade Press, Operator Pages, Colo Directories, and Province Search Patterns

Date: 2026-08-12. Country: **AO Angola**. Scope: industry / press / vendor-led discovery for Angolan data centers, with official verification routes for every lead. Division model: **18 provinces from `world-manifest.jsonl`**: Bengo, Benguela, Bie, Cabinda, Cuando Cubango, Cunene, North Cuanza, South Cuanza, Huambo, Huila, North Lunda, South Lunda, Luanda, Malanje, Moxico, Namibe, Uige, Zaire. Angola's official 2024 reform created 21 provinces; map Icolo e Bengo, Cuando, Cubango, and Moxico Leste evidence back to the manifest divisions until the manifest changes.

Reliability grades:
- **A** = official / primary: operator official page or release, MINTTICS, INFOSI, INACOM/Observatorio TIC, Diario da Republica, Portal Compras Publicas/SNCP, AIPEX/JUI, IRSEA/ENDE/RNTEP/MINEA, official cloud-provider page, Uptime Institute record.
- **B** = strong secondary / trade press: Jornal de Angola, Angop when not simply official record, Expansao, Novo Jornal, Verangola, Macauhub, Agence Ecofin / We Are Tech, TechAfrica News, DCD, The Tech Capital, Capacity, Developing Telecoms, Engineering News, reputable vendor case study with named client/site.
- **C** = weak lead: DataCenterMap, datacenters.com, Baxtel, OCOLO, Inflect, HostDir, colo.exchange, Cloudscene, PeeringDB-only records, DigitalAngola.com aggregator dossiers, market reports, broker pages, LinkedIn/social posts.

---

## 0. Angola market frame

- Angola's data-center landscape is **Luanda-centric**. Confirmed/strong facilities are AngoNAP Luanda (Angola Cables), Raxio Angola AO1 (Cacuaco), Paratus/ITA DC1 and DC2 (Patriota/Benfica), the INFOSI Government Data Center and Cloud (Camama) plus backup at ITEL/Rangel, and Africell's Kings Tower data center. Unitel, Movicel, Angola Telecom, MSTelcom/Startel/Infrasat and banks create additional operator/internal leads that need source-by-source verification.
- The **highest-confidence commercial colo operators** are Angola Cables, Raxio, and Paratus. Raxio's official 2025 opening release gives 3 MW IT power and 800+ racks for AO1. Paratus' official 2023 announcement gives a planned third Angola DC in Luanda with >10 MW IT power and >2,000 cabinets; DCD reports existing Paratus Luanda campus data centers launched in 2017 and 2019.
- The **highest-confidence state project** is INFOSI's Data Center e Cloud do Governo at Camama, inaugurated 2026-04-28 by the government; MINTTICS' 2023 page gives USD 89M project value and identifies both Camama and the backup site at ITEL/Rangel.
- Non-Luanda provinces are **negative-by-default**. The main exception to watch is the 2025 AnyConnect/Visium planned secondary disaster-recovery facility in Lubango, Huila; keep it planned and B/C until a binding official/operator source confirms site, financing, and build status.
- No hyperscaler public cloud region is in Angola as of this methodology date. Check official AWS, Azure, Google Cloud, and OCI region lists before accepting any `cloud region` claim.
- Source spellings vary: `data center`, `datacenter`, `data centre`, `centro de dados`, `centro de processamento de dados`, `cloud nacional`, `cloud soberana`, `hospedagem`, `alojamento`, `sala de servidores`, `servidores`, `Tier III`, `Tier IV`, `Uptime`, `MW`, `MVA`, `racks`, `cabinetes`, `IA`, `inteligencia artificial`, `HPC`.

Core national query set:

```text
Angola ("data center" OR datacenter OR "data centre") (Luanda OR Camama OR Cacuaco OR Patriota OR Benfica OR Lubango)
Angola ("centro de dados" OR "centro de processamento de dados") (Camama OR Rangel OR Cacuaco OR Lubango)
"Data Center e Cloud do Governo" OR "Data Center e Cloud Nacional" Angola
"INFOSI" "data center" Camama OR Rangel
"Angola Cables" AngoNAP Luanda colocation
"Raxio" Angola AO1 Cacuaco "3MW" OR "800 racks"
"Paratus" Angola "data center" Luanda OR Patriota OR Benfica
"Africell" "data center" "Kings Tower" Angola
"Unitel" "data center" "Luanda Sul"
"Movicel" "data center" Luanda
"Angola Telecom" "data center" OR "centro de dados"
"AnyConnect" "Lubango" "data center" OR "disaster recovery"
"Visium" "AnyConnect" Angola "data center"
"cloud soberana" Angola
"Angola" "data center" G42 OR Presight OR Huawei
```

---

## 1. High-signal trade and press sources

Use press to discover project names, dates, officials, integrators, and rough status; then verify through official/operator, MINTTICS/INFOSI, INACOM, procurement, Uptime, or energy sources.

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Angola Cables | https://www.angolacables.co.ao/datacenter | Official AngoNAP Luanda data-center services and operator identity. | A for operator facts |
| Raxio Group | https://www.raxiogroup.com/data-centres/angola/ and official news | AO1 status, launch date, capacity, Cacuaco/Luanda positioning. | A |
| Paratus Africa / Paratus Angola | https://paratus.africa/pt/services/data-center-services/ and https://paratus.africa/blog/paratus-announces-its-biggest-data-center-project-yet/ | Existing Angola data centers and planned third Angola DC. | A for operator claims |
| Africell | https://www.africell.com/news/africell-opens-high-tech-data-center-in-angola/ | Kings Tower Luanda data center opening, partners, intended hosting/network use. | A |
| MINTTICS / INFOSI | https://minttics.gov.ao/ ; https://www.infosi.gov.ao/ | Government cloud/data center verification. | A |
| Jornal de Angola | https://www.jornaldeangola.ao/ | National announcements, ministry/operator interviews, official event detail. | B; A only for official facts quoted from state source |
| Angop | https://www.angop.ao/ | State news agency; inaugurations, ANGOTIC, MINTTICS/INFOSI events, protocols. | A/B depending article |
| Expansao | https://expansao.co.ao/ | Business/economy detail, investment amounts, contracts, AIPEX, energy. | B |
| Novo Jornal | https://novojornal.co.ao/ | Politics/infrastructure reporting including national-cloud coverage. | B |
| Verangola | https://www.verangola.net/ | English/Portuguese national infrastructure and digital-economy reporting. | B |
| Macauhub | https://macauhub.com.mo/ | Luso-business wire for infrastructure/telecom project notes. | B |
| Menos Fios | https://www.menosfios.com/ | Angola-focused tech/telecom coverage. | B/C |
| Primeiro IT | https://primeiro-it.com/ | Angolan ICT press; site visits, operator/cloud projects. | B/C |
| Agence Ecofin / We Are Tech Africa | https://www.ecofinagency.com/ ; https://www.wearetech.africa/ | Regional digital-infrastructure coverage. | B |
| TechAfrica News | https://techafricanews.com/ | Africell and state digital-infrastructure coverage. | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | Raxio, Paratus, Angola Cables, Africell, Liquid/market leads. | B |
| The Tech Capital | https://thetechcapital.com/ | Financing/capacity-market coverage, Africell/Dell/Oracle. | B |
| Capacity / Total Telecom / Developing Telecoms | capacitymedia.com, totaltele.com, developingtelecoms.com | Raxio, Paratus, cables/2Africa context. | B |
| Engineering News / World Construction Network | engineeringnews.co.za, worldconstructionnetwork.com | Paratus third-DC construction coverage. | B |
| DigitalAngola.com | https://digitalangola.com/infrastructure/data-centers/ | Facility atlas and capacity dossiers. | C unless it links to primary sources |
| Directories | datacentermap.com/angola, datacenters.com/locations/angola, baxtel.com, ocolo.io, inflect.com, hostdir.net, colo.exchange | Facility names, addresses, power/rack claims. | C unless corroborated |
| PeeringDB / AngonIX | peeringdb.com, AngonIX | Network presence and IX membership. | C for facility enumeration |

Trade-press queries:

```text
site:jornaldeangola.ao "data center" OR "centro de dados"
site:angop.ao "data center" OR "centro de dados"
site:expansao.co.ao "data center" OR "cloud"
site:novojornal.co.ao "data center" OR "cloud nacional"
site:verangola.net "data center" OR "centro de dados"
site:menosfios.com "data center" OR "centro de dados"
site:primeiro-it.com "data center" OR "cloud"
site:wearetech.africa Angola "data center"
site:techafricanews.com Angola "data center"
site:datacenterdynamics.com/en/news/ Angola "data center"
site:datacenterdynamics.com/en/news/ "Raxio Angola" OR "Paratus" OR "Angola Cables" OR "Africell"
site:thetechcapital.com Angola "data centre"
site:capacitymedia.com Angola "data centre" OR "2Africa"
site:developingtelecoms.com Angola "data centre" OR "data center"
site:engineeringnews.co.za Angola "data centre" Paratus
```

Status-language interpretation:

- `memorando de entendimento`, `protocolo`, `acordo`, `parceria`, `anunciou` = lead/planned unless construction or opening evidence follows.
- `concurso publico`, `aviso de licitacao`, `adjudicacao`, `contrato` = procurement signal. Stronger when Portal Compras Publicas / SNCP / Diario da Republica confirms.
- `obra`, `construcao`, `execucao fisica`, `fase de instalacao`, `terreno`, `plot` = construction/planning lead. Verify with operator/ministry/contractor.
- `inaugurou`, `inauguracao`, `abriu`, `opened`, `launch`, `entrou em funcionamento`, `operacional`, `commissioned` = operational signal. Verify with official/operator page.
- `cloud`, `hospedagem`, `VPS`, `servidores dedicados`, `sovereign cloud` = service evidence only unless a physical site is named.

---

## 2. Operator and vendor sweep

Official operator pages are A for current marketed services and self-claimed facilities, but exact power/rack data remains A only when the operator states the number.

| Operator / provider | Main route | Likely geography | Search / verification notes |
|---|---|---|---|
| Angola Cables | https://www.angolacables.co.ao/ ; https://www.angolacables.co.ao/datacenter | AngoNAP Luanda; Av. Pedro de Castro Van-Dunem Loy / Edificio Cellwave lead | Main commercial colo/cloud connectivity operator; also AngoNAP Fortaleza in Brazil, which must not be counted for Angola. Verify rack/MW claims through operator or keep C. |
| Raxio Angola / AO1 | https://www.raxiogroup.com/data-centres/angola/ ; official 2025 opening release | Cacuaco, Luanda | Official release states opened Oct 2, 2025, USD 30M, 3 MW IT power, 800+ racks; some directories report 7 MW as future/planned expansion. |
| Paratus Angola / ITA | https://paratus.africa/pt/services/data-center-services/ ; Paratus 2023 third-DC announcement | Patriota/Benfica Luanda campus; planned third DC in Luanda | Existing two data centers are high-priority commercial colo leads; third DC planned at >10 MW and >2,000 cabinets. Re-verify construction status. |
| INFOSI | https://www.infosi.gov.ao/ ; MINTTICS pages | Camama primary, ITEL/Rangel backup, Luanda | Government cloud operator; not commercial colo. Capacity claims should be source-qualified. |
| Africell Angola | https://www.africell.com/ ; Africell 2021 data-center release | Kings Tower, central Luanda | Official release confirms cloud-based DC at HQ with HP/Nokia/Dell/Oracle and local partners; supports mobile network and local businesses. |
| Unitel | https://www.unitel.ao/ | Luanda Sul and Filda DR leads | Largest mobile operator; directories list data-center/colo power, but official corroboration is needed before A/B. |
| Angola Telecom | http://www.angolatelecom.ao/ | Luanda HQ and provincial network nodes | State incumbent; operator network-core/server rooms in provinces are not automatically data centers. |
| Movicel | https://www.movicel.co.ao/ (verify) | Luanda + provincial switching centres | Operator-grade core facilities; little public technical detail. |
| Startel / MS Telecom / MSTelcom / Infrasat / Multitel / Net One | official domains + INACOM/Observatorio TIC | Mostly Luanda | ISP/enterprise hosting leads. Require site evidence. |
| AFRICLOUD / local VPS hosts | provider pages/directories | Luanda | Service-only unless a physical facility is named. |
| Clouds2Africa | via Angola Cables | AngoNAP-backed service | Cloud service on Angola Cables infrastructure, not a separate facility unless a source names a separate site. |
| AnyConnect / Visium Technologies | official release if found; Newswire/datacenters.com leads | Planned Lubango DR facility, Huila | 2025 $60M digital infrastructure framework lead includes secondary DR in Lubango and fibre deployment. Treat as planned B/C. |
| Presight / G42 / Huawei / ZTE / Dell / Oracle / HP / Nokia | vendor pages and press | Mostly Luanda | Integrators/suppliers. Use named-project references only; vendor social posts can support specs but should not drive A grade alone. |
| Banks and oil/gas operators | BNA, BAI, BFA, BIC, Banco Atlantico, Sonangol, oil majors | Luanda; Soyo/Zaire; Cabinda; Lobito/Benguela | Internal data rooms/DR. Count only with named physical site/tender. |

Vendor/operator queries:

```text
"{operator}" Angola "data center"
"{operator}" Angola "centro de dados" OR "sala de servidores"
"{operator}" "colocation" Angola
"{operator}" "Tier III" OR "Uptime" Angola
"{operator}" "grupo electrogeneo" OR "UPS" "data center"
"{operator}" "cloud" "Luanda"
"{operator}" "protocolo" OR "parceria" "Angola Cables" OR "AngoNAP"
```

Facility-address pivots:

```text
"Edificio Cellwave" "AngoNAP"
"Av. Pedro de Castro Van-Dunem Loy" "data center"
"Estrada de Cacuaco" "data center" OR Raxio
"Cacuaco" "Raxio AO1"
"Kings Tower" Africell "data center"
"Camama" "Data Center e Cloud do Governo"
"Rangel" "Centro Nacional de Dados"
"ITEL" "Centro Nacional de Dados" Angola
"Patriota" Paratus "data center"
"Benfica" Paratus "data center"
"Rua 29" "EPAL 30" Paratus
"Filda" Unitel "data center" OR redundancia
"Lubango" AnyConnect "disaster recovery"
"ZEE" OR "Viana" "parque tecnologico" OR "data center"
```

---

## 3. Directory and aggregator handling

| Directory / lead source | What it can provide | Caveats |
|---|---|---|
| DataCenterMap Angola | Facility/operator names and addresses, including AngoNAP, Raxio, Paratus/ITA, Unitel, MSTelcom, Africell leads. | C by default. Addresses/capacity may be stale or broker-estimated. |
| datacenters.com Angola | Provider/location index, including Angola Cables and AnyConnect Lubango lead. | C; sales/quote-oriented and may list planned facilities. |
| Baxtel | AngoNAP, Angola Cables, Raxio summaries and linked news. | B only for clearly sourced news; C for directory data alone. |
| OCOLO / Inflect / HostDir / colo.exchange / Cloudscene | Rack/power estimates and address hints. | C; reconcile conflicts such as Raxio 3 MW official vs 7 MW future/directory values. |
| DigitalAngola.com | Convenient market atlas. | C unless it cites primary sources; use as a checklist, not final evidence. |
| PeeringDB / AngonIX | ASNs, interconnection, IXP presence. | Network evidence only; not a facility register. |

Directory upgrade workflow:

1. Capture exact name, address, operator, claimed power/racks, and source date.
2. Search exact name plus operator official domain.
3. Search MINTTICS / INFOSI / INACOM / compraspublicas for legal entity or project.
4. Search Angop / Jornal de Angola / DCD / TechAfrica / The Tech Capital / Developing Telecoms for opening or tender news.
5. Search Uptime Institute by legal entity and facility name for Tier claims.
6. If no primary or strong secondary support appears, keep as **C** with an explicit caveat or do not count.

Directory query templates:

```text
site:datacentermap.com/angola "{operator}"
site:datacenters.com/locations/angola "{operator}"
site:baxtel.com "{facility}" Angola
site:ocolo.io "{facility}" Angola
site:inflect.com "{facility}" Angola
site:digitalangola.com "{facility}"
site:peeringdb.com Angola "{operator}"
"{facility name}" "{operator}" Angola
```

---

## 4. Known lead grading guidance

| Lead | Initial grade | How to finalize |
|---|---:|---|
| Raxio Angola AO1 | A for operator release; B for DCD; C for directories | Use official Raxio for 3 MW/800 racks/opened Oct 2025. Use Uptime only for exact certification status. |
| Angola Cables AngoNAP Luanda | A for existence/services on Angola Cables; C for directory MW/rack | Official operator page confirms AngoNAP Luanda; use DCD/operator for any rack count if found. |
| Paratus Angola DC1/DC2 | A for operator services page; B for DCD launch/server counts | Count as operational if official service page remains current; capacity_mw null unless official. |
| Paratus third Angola DC | A for planned operator announcement; B for trade reposts | Keep planned unless construction/opening evidence exists. Official plan: >10 MW IT, >2,000 cabinets, 30,000 sqm Luanda plot. |
| INFOSI Camama government cloud | A for MINTTICS/INFOSI facts | Operational from 2026-04-28. Keep capacity null unless primary technical doc confirms. |
| INFOSI ITEL/Rangel backup | A for MINTTICS project description | Backup/DR facility; capacity null unless official. |
| Africell Kings Tower | A for Africell release | Operational since Oct 2021; capacity null. |
| Unitel Luanda Sul / Filda | C unless Unitel/press confirms | Search Unitel official and local press before counting as facility. |
| Movicel / Angola Telecom / MSTelcom core sites | C/B leads | Do not infer all provincial nodes are data centers. Need named facility or tender. |
| AnyConnect / Visium Lubango DR | B/C planned lead | Use only as Huila planned lead if official/Newswire source names Lubango; capacity null and status planned. |
| Liquid Angola DC leads | B if only DCD/reporting | Search for official Liquid/Paratus/Angola source and site; do not count without location. |

---

## 5. Province-by-province industry search matrix

Use all 18 manifest divisions. Search province aliases in Portuguese, English, and city/municipality names.

### 5.1 Luanda - highest priority

Known/expected leads: AngoNAP Luanda, Raxio AO1 Cacuaco, Paratus/ITA DC1/DC2 Patriota/Benfica, Paratus third DC, INFOSI Camama, ITEL/Rangel backup, Africell Kings Tower, Unitel Luanda Sul/Filda, Movicel, Angola Telecom, MSTelcom, AFRICLOUD, banks, oil majors' Luanda offices, ZEE Viana, Talatona.

```text
"Luanda" "data center" (colocation OR racks OR MW OR "Tier III" OR "Tier IV")
"Luanda" "centro de dados" (colocation OR alojamento OR servidores)
"Talatona" OR "Camama" OR "Cacuaco" OR "Patriota" OR "Benfica" OR "Viana" "data center"
"Luanda" "sala de servidores" banco OR "instituicao financeira"
"ZEE" Viana "tecnologia" OR "data center"
"{bank}" Angola "data center" OR "backup" OR "disaster recovery"
```

### 5.2 Huila / Lubango - watch planned DR lead

```text
"Huila" OR "Huíla" OR "Lubango" "data center" OR "centro de dados"
"Lubango" "disaster recovery" Angola
"AnyConnect" "Lubango" "data center"
"Visium" "AnyConnect" Angola "Lubango"
"Lubango" "fibra optica" "centro de dados"
```

### 5.3 Benguela and Zaire - oil/logistics secondary

```text
"Benguela" OR "Lobito" "data center" OR "centro de dados" OR "servidores"
"Corredor do Lobito" "digital" OR "data"
"Soyo" OR "Mbanza Kongo" OR "Zaire" "data center" OR "servidores" OR "telemetria"
"Sonangol" "Soyo" "data center" OR "backup"
"{oil operator}" Angola "data center" OR "centro de dados" OR "backup"
```

### 5.4 Cabinda, Lunda Norte, Lunda Sul, Namibe - extractive/port/internal leads only

```text
"Cabinda" "data center" OR "centro de dados" OR "servidores"
"Lunda Norte" OR "Dundo" "data center" OR "servidores"
"Lunda Sul" OR "Saurimo" "centro de dados" OR "servidores"
"Namibe" OR "Mocamedes" OR "Moçâmedes" "data center" OR "servidores"
"mining" OR "diamantes" Angola "data center" "Lunda"
```

### 5.5 Huambo, Bie, Malanje - university/institutional

```text
"Huambo" OR "Kuito" OR "Cuito" OR "Malanje" "data center" OR "servidores" OR "TIC"
"Universidade" "Huambo" "centro de dados" OR "servidores"
"Huambo" "inteligencia artificial" OR "HPC"
"Malanje" "governo provincial" "TIC" "servidores"
```

### 5.6 Remaining manifest provinces - negative-by-default

Divisions: Bengo, Cuando Cubango, Cunene, North Cuanza, South Cuanza, Moxico, Uige. Include new-map names in aliases: Icolo e Bengo -> Bengo/Luanda depending site; Cuando and Cubango -> Cuando Cubango; Moxico Leste -> Moxico.

```text
"{province}" "data center" OR "centro de dados" OR "sala de servidores"
"{province}" "fibra optica" OR "banda larga"
"{province}" "governo provincial" "digital" OR "TIC"
"{province}" "servidores" "backup"
"Icolo e Bengo" "data center" OR "centro de dados"
"Cuando" OR "Cubango" OR "Menongue" "data center"
"Moxico Leste" OR "Cazombo" "centro de dados"
"Uige" OR "Uíge" "data center" OR "TIC"
```

Promotion rule: a non-Luanda lead becomes a project entry only with official/operator naming of the physical site, named procurement, or strong trade press with accountable details. Otherwise record as `no_projects: true` or keep only as a C lead in notes.

---

## 6. Confidence and honesty rules

- Angola has no public DC register; every entry needs explicit sourcing and a stated reason for being counted.
- Do not count AngoNAP Fortaleza (Brazil), CDN PoPs, AngonIX/IXPs, PeeringDB presences, satellite teleports, or cable landing stations as Angola data centers unless a separate data-center facility is named.
- Treat `Tier III`, `Tier IV`, `Uptime`, `carrier-neutral`, `largest`, and `first` claims carefully. Use Uptime Institute for certification type; operator/trade pages may mean design target or marketing claim.
- Capacity conflicts are common. Prefer official operator releases; otherwise leave `capacity_mw` null and put estimates in notes with C-grade caveat.
- Date-sensitive status must be re-verified: INFOSI Camama became operational on 2026-04-28; Raxio AO1 opened on 2025-10-02 per official release; Paratus third Angola DC remained planned in the sources checked unless newer evidence appears.
- Use the manifest's 18 province names in outputs, but preserve official place names and aliases in notes.
