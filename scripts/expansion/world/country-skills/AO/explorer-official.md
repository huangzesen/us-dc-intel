# AO Explorer Official - Angola Datacenter Enumeration via INACOM, MINTTICS/INFOSI, Public Procurement, Permitting, Energy, and Official Operator Pages

Date: 2026-08-12. Country: **AO Angola**. Division model for this repo: **18 provinces from `world-manifest.jsonl`**: Bengo, Benguela, Bie, Cabinda, Cuando Cubango, Cunene, North Cuanza, South Cuanza, Huambo, Huila, North Lunda, South Lunda, Luanda, Malanje, Moxico, Namibe, Uige, Zaire. Important caveat: Angola's 2024 administrative reform created a 21-province official map (Icolo e Bengo, Cuando, Cubango, Moxico Leste split from Luanda/Cuando Cubango/Moxico), but this workflow must emit the manifest's 18 division names until the manifest changes. Map new-province evidence back to the legacy manifest division.

Angle: **official / regulatory / government-cloud / procurement / permitting / energy pipeline** for enumerating operational, under-construction, planned, and institutional data-center facilities.

Reliability grades:
- **A** = official / primary source: MINTTICS or INFOSI page, INACOM or Observatorio TIC record, Diario da Republica diploma, official operator facility page, Portal Compras Publicas / SNCP tender or award, AIPEX/JUI decision, IRSEA / ENDE / RNTEP / PRODEL / MINEA page, official cloud-region page, Uptime Institute certification record, or official government news (`governo.gov.ao`, ministry pages, diplomatic mission pages; Angop can be A when carrying official ceremony/ministerial facts).
- **B** = strong secondary source: Jornal de Angola, Expansao, Novo Jornal, Verangola, Macauhub, Agence Ecofin / We Are Tech, TechAfrica News, DCD, The Tech Capital, Capacity, Developing Telecoms, Engineering News, vendor case study with named client/site.
- **C** = weak lead: DataCenterMap / datacenters.com / Baxtel / OCOLO / Inflect / HostDir / Cloudscene / colo.exchange, DigitalAngola.com aggregator dossiers, market reports, LinkedIn/social posts, unverified local blogs.

---

## 0. Angola-specific structural facts

- Angola has **no public national data-center register** and no public national planning-permit search engine comparable to a US county database or the UK planning portal. Enumeration works by joining **government cloud announcements**, **telecom/operator official pages**, **public procurement**, **Diario da Republica decrees**, **municipal construction licensing leads**, **energy/grid context**, and **trade press**.
- The working language is Portuguese. Search both Angolan Portuguese and English variants: `data center`, `datacenter`, `data centre`, `centro de dados`, `centro de processamento de dados`, `centro nacional de dados`, `cloud nacional`, `cloud do governo`, `cloud soberana`, `nuvem`, `colocation`, `alojamento`, `hospedagem`, `sala de servidores`, `computacao em nuvem`, `inteligencia artificial`, `HPC`.
- The Angolan market is **Luanda-centric**. Confirmed/high-confidence facilities are in Luanda province: INFOSI Government Data Center and Cloud at Camama, INFOSI backup/legacy Centro Nacional de Dados at ITEL/Rangel, Angola Cables AngoNAP Luanda, Raxio AO1 at Cacuaco, Paratus/ITA data centers at Patriota/Benfica, Africell Kings Tower, plus telco core facilities from Unitel, Angola Telecom, Movicel, MSTelcom/Startel/Infrasat where named evidence exists. A non-Luanda project should remain negative unless there is named-site evidence, such as the **planned AnyConnect/Visium Lubango DR lead** in Huila.
- **No AWS / Azure / Google Cloud / Oracle OCI public cloud region in Angola** as of this methodology date. Angola's cloud story is sovereign/hosted cloud: INFOSI national cloud, Angola Cables Clouds2Africa, Paratus/telecom clouds, local hosting. Do not treat CDN PoPs, IXPs, direct-connect partners, or marketplace partner pages as physical cloud regions.
- Capacity and rack figures are often absent or conflict. Use only source-supported values. Examples: Raxio's official 2025 opening release states **3 MW IT power and 800+ racks**; Paratus' official 2023 third-DC announcement states **>10 MW IT power and >2,000 cabinets** planned; MINTTICS states the national-cloud project cost and site dimensions but public rack/power figures vary by secondary/vendor source. Leave `capacity_mw` null when the primary source does not state it.

Core Portuguese vocabulary:

```text
centro de dados
data center
centro de processamento de dados
centro nacional de dados
cloud nacional
cloud do governo
cloud soberana
nuvem
colocation
hospedagem
alojamento
sala de servidores
armazenamento de dados
inteligencia artificial
rede privativa do estado
fibra optica
licenca de construcao
licenca de obras
licenciamento
alvara
certificado de conformidade
concurso publico
contratacao publica
despacho
decreto presidencial
Diario da Republica
```

---

## 1. Grade-A official and regulatory routes

### 1.1 INACOM - communications regulator

Primary source: **Instituto Angolano das Comunicacoes (INACOM)**, https://inacom.gov.ao/. INACOM regulates, supervises, and inspects Angola's electronic-communications and postal-services market. It is not a facility registry, but it is the legal-entity route for telecom operators whose network cores and hosting services generate data-center leads.

High-value official surfaces:

- INACOM main portal: https://inacom.gov.ao/
- Observatorio TIC / INACOM market data: https://www.observatoriotic.gov.ao/ . Search marketplace pages such as `telefonia`, `transferencia_de_dados`, `internet`, and `tv_por_assinatura`; current pages expose operator names including Angola Telecom, Africell, Movicel, Unitel, LMS, MS Telcom, Net One, Multitel, Startel, ITA/Paratus, Infrasat, TV Cabo Angola, DSTV, and ZAP.
- INACOM service pages: `Registo de Empresas`, `Licenca Multiservicos`, `Autorizacao de Comercializacao`.
- Official legal texts may be mirrored at Lex.AO or in Diario da Republica; use mirrors only as B unless the gazette/original is opened.

Use INACOM for:

- Confirming licensed/operator universe and legal names.
- Distinguishing telecom/ISP authorization from physical facility proof.
- Pivoting to official operator pages, procurement, Uptime records, and press for the actual site.

INACOM query templates:

```text
site:inacom.gov.ao "data center"
site:inacom.gov.ao "centro de dados"
site:inacom.gov.ao "Licenca Multiservicos" "{operator}"
site:inacom.gov.ao "Autorizacao" "{operator}"
site:observatoriotic.gov.ao "{operator}"
site:observatoriotic.gov.ao "telefonia" "Unitel" "Africell" "Movicel"
"INACOM" "{operator}" "licenca" Angola
"INACOM" "servico de transferencia de dados" Angola
```

Operator names to sweep: `Angola Telecom`, `Unitel`, `Movicel`, `Africell`, `Paratus Angola`, `ITA`, `Startel`, `MS Telecom`, `MSTelcom`, `Infrasat`, `Multitel`, `Net One`, `TV Cabo Angola`, `ZAP`, `LMS`, `Angola Cables`.

### 1.2 MINTTICS - ministry source for national digital infrastructure

Primary source: **Ministerio das Telecomunicacoes, Tecnologias de Informacao e Comunicacao Social (MINTTICS)**, https://minttics.gov.ao/. MINTTICS is the decisive official source for government digital-infrastructure projects and ministry-supervised telecom/cloud initiatives.

Confirmed high-value pages:

- Government DC/cloud inauguration: https://minttics.gov.ao/ao/noticias/angola-inaugura-data-center-e-cloud-do-governo-e-reforca-soberania-digital/ . Published 2026-04-28; states the Data Center e Cloud do Governo was inaugurated in Luanda-Camama and frames it as strategic infrastructure for digital sovereignty, state data hosting, and public-service modernization.
- National cloud investment/project: https://minttics.gov.ao/ao/noticias/pais-ira-investir-89-milhoes-no-projecto-cloud-nacional/ . Published 2023-02-16; states the government would invest USD 89 million, with a main prefabricated two-storey data center on about 5,320 sqm at Camama, Luanda, and modernization of a backup Data Center at the Centro Nacional de Dados next to ITEL in Rangel, Luanda.
- 2026 inauguration context: https://minttics.gov.ao/ao/noticias/inauguracao-do-novo-data-center-e-cloud-do-governo-em-2026/ . Use for status timing before final inauguration.
- ANGOTIC pages and MINTTICS news for protocols with Huawei, Unitel, Angola Telecom, AI/cloud vendors, and satellite/connectivity projects: https://minttics.gov.ao/ and https://angotic.ao/ .

MINTTICS query templates:

```text
site:minttics.gov.ao "data center"
site:minttics.gov.ao "centro de dados"
site:minttics.gov.ao "cloud nacional"
site:minttics.gov.ao "Data Center e Cloud do Governo"
site:minttics.gov.ao "Camama" "Rangel"
site:minttics.gov.ao "INFOSI"
site:minttics.gov.ao "{province}" "data center"
site:minttics.gov.ao "{operator}" "data center"
site:minttics.gov.ao "fibra optica" "{province}"
site:minttics.gov.ao "ANGOTIC" "data center"
```

Grade **A** for named project/site/date facts on MINTTICS pages. Do not promote secondary/vendor rack or power numbers to A unless MINTTICS states them.

### 1.3 INFOSI - government cloud and state network operator

Primary source: **INFOSI - Instituto Nacional de Fomento da Sociedade da Informacao**, https://www.infosi.gov.ao/. INFOSI operates state digital infrastructure including the Rede Privativa do Estado and the government data-center/cloud environment. Its statute is **Decreto Presidencial n. 135/21 de 31 de Maio**.

Known INFOSI-linked facilities to verify:

- **Data Center e Cloud do Governo / Cloud Nacional, Camama, Luanda**: operational/inaugurated 2026-04-28 per MINTTICS. Main government cloud facility. MINTTICS 2023 project page gives the USD 89M project, Camama site, and 5,320 sqm building context. Some press/vendor sources report 208 or 336 racks and about 1.04 MW IT load; treat those as B/C unless confirmed by MINTTICS/INFOSI or an official technical document.
- **Centro Nacional de Dados / backup data center at ITEL/Rangel, Luanda**: modernization/backup role per MINTTICS 2023 project page. Count as a government DR/backup facility when the physical site is needed, but keep capacity null unless a primary source states it.

INFOSI query templates:

```text
site:infosi.gov.ao "data center"
site:infosi.gov.ao "centro de dados"
site:infosi.gov.ao "Centro Nacional de Dados"
site:infosi.gov.ao "Cloud Nacional"
site:infosi.gov.ao "Camama"
site:infosi.gov.ao "Rangel"
site:infosi.gov.ao "Rede Privativa do Estado"
"INFOSI" "Data Center e Cloud do Governo"
"INFOSI" "Decreto Presidencial" "135/21"
"Decreto Presidencial" "INFOSI" "centro de dados"
```

### 1.4 Public procurement and gazette routes

Primary sources:

- **Portal Compras Publicas**: https://www.compraspublicas.minfin.gov.ao/ . Search tender notices, awards, and contract records.
- **SNCP - Servico Nacional da Contratacao Publica**: https://www.sncp.minfin.gov.ao/ . Procurement oversight and contract-publication route.
- **Diario da Republica / Imprensa Nacional**: verify current official gazette URL at query time, then search for decrees and authorizations.
- Legal basis: **Lei 41/20 de 23 de Dezembro de 2020 - Lei dos Contratos Publicos**.

Why it matters: INFOSI/MINTTICS, ministries, public universities, state banks, public enterprises, and telecom entities may tender for data-center construction, fit-out, UPS/generator systems, storage, backup, cybersecurity, or cloud platforms. Procurement confirms institutional projects earlier than press.

Query templates:

```text
site:compraspublicas.minfin.gov.ao "data center"
site:compraspublicas.minfin.gov.ao "centro de dados"
site:compraspublicas.minfin.gov.ao "centro de processamento de dados"
site:compraspublicas.minfin.gov.ao "cloud"
site:compraspublicas.minfin.gov.ao "INFOSI"
site:compraspublicas.minfin.gov.ao "UPS" "servidores"
site:sncp.minfin.gov.ao "data center"
site:sncp.minfin.gov.ao "centro de dados"
"concurso publico" "data center" Angola "{year}"
"concurso publico" "centro de dados" "{province}"
"Diario da Republica" "INFOSI" "135/21"
"Diario da Republica" "Janela Unica do Investimento" "167/20"
```

Extract exact contracting entity, supplier, contract scope, site/municipality, contract date, value, and whether the work is physical construction versus IT hardware refresh.

### 1.5 Investment and construction licensing routes

- **AIPEX - Agencia de Investimento Privado e Promocao das Exportacoes**: https://www.aipex.co.ao/ and https://investinangola.ao/ . AIPEX/JUI records are A for registered investment/projects, but not necessarily A for the physical status of a site.
- **JUI - Janela Unica do Investimento**: created under Decreto Presidencial 167/20. Use for private data-center investment leads.
- **SEPE - Portal dos Servicos Publicos Electronicos**: https://www.sepe.gov.ao/ . Route for public e-services and licensing information.
- **Municipal construction licensing**: building works require municipal licensing (`licenca de obras`, `licenca de construcao`, `alvara`). For Luanda, search provincial/municipal urban-planning references such as IPGUL and the Luanda provincial government. There is no reliable public searchable database of issued building permits; evidence usually appears in press, AIPEX, municipal notices, or company releases.

Query templates:

```text
site:aipex.co.ao "data center" OR "centro de dados"
site:investinangola.ao "data center" OR "centro de dados"
"AIPEX" "data center" Angola
"Janela Unica do Investimento" "data center" Angola
site:sepe.gov.ao "licenca" "construcao"
site:luanda.gov.ao "data center" OR "centro de dados"
"licenca de construcao" "data center" Luanda
"licenca de obras" "centro de dados" "Cacuaco" OR "Camama" OR "Patriota"
```

### 1.6 Energy and large-consumer context

Primary sources:

- **IRSEA - Instituto Regulador dos Servicos de Electricidade e de Agua**: https://irsea.gov.ao/ . Electricity/water regulator; tariffs, licences, and legislation.
- **MINEA - Ministerio da Energia e Aguas**: https://www.minea.gov.ao/ . Sector policy and large energy projects.
- **ENDE-EP**, **RNTEP/RNT-EP**, **PRODEL-EP**: distribution, transmission, and generation operators. Verify current domains at query time.

Why it matters:

- Angola's grid is hydro-heavy but reliability varies; serious data centers rely on UPS and diesel generation. There is no public register of data-center power connections.
- Grid/substation news can corroborate plausibility near Luanda zones: Camama, Cacuaco, Talatona/Patriota, Benfica, Viana/ZEE Luanda-Bengo, and Lobito corridor.

Query templates:

```text
site:irsea.gov.ao "data center" OR "grande consumidor"
site:minea.gov.ao "data center" OR "centro de dados"
site:minea.gov.ao "energia" "Cacuaco" OR "Camama" OR "Patriota"
"ENDE" "subestacao" "Cacuaco" OR "Camama" OR "Talatona" OR "Viana"
"RNTEP" OR "RNT" "subestacao" "Luanda"
"{operator}" "grupo electrogeneo" "data center" Angola
"{operator}" UPS "data center" Angola
```

Energy evidence is generally supporting context, not facility proof, unless it names the facility or large consumer.

### 1.7 Official cloud-region absence check

Before accepting any Angola public-cloud-region claim, check official lists:

```text
AWS regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
Google Cloud locations: https://cloud.google.com/about/locations
Oracle OCI regions: https://www.oracle.com/cloud/cloud-regions/
```

As of this methodology date, Angola has no public region from AWS, Azure, Google Cloud, or Oracle OCI. South Africa is the usual nearest public-region market; OCI also lists African regional presence outside Angola. Treat `cloud`, `sovereign cloud`, `hosted cloud`, `edge`, `PoP`, `Direct Connect`, `ExpressRoute`, or CDN language as service/network evidence unless the official cloud provider page lists a physical region in Angola.

### 1.8 Data protection and localization context

- **Lei 22/11 de 17 de Junho de 2011 - Lei da Proteccao de Dados Pessoais** is the personal-data law. Verify authority/enforcement status at query time through official APD or Diario da Republica sources.
- Financial-sector and government-sector data-hosting requirements are demand drivers. Banco Nacional de Angola (BNA), banks, telecom operators, and ministries may have internal DR/server-room projects; count only when a named site, tender, or official facility claim exists.

---

## 2. Official facility/project watchlist

Use this as a seed list, then verify each run with current sources.

| Facility / project | Manifest division | Status to use when current evidence matches | Primary verification route | Notes |
|---|---:|---|---|---|
| Data Center e Cloud do Governo / Cloud Nacional, Camama | Luanda | Operational | MINTTICS + INFOSI + government news | Inaugurated 2026-04-28. MINTTICS confirms Luanda-Camama and USD 89M project context; keep MW null unless primary technical docs confirm. |
| Centro Nacional de Dados backup / ITEL-Rangel | Luanda | Operational / backup-modernized | MINTTICS + INFOSI | MINTTICS 2023 project says backup DC at Centro Nacional de Dados next to ITEL in Rangel. |
| AngoNAP Luanda | Luanda | Operational | Angola Cables official data-center page | Official page confirms AngoNAP Luanda data-center services; third-party power/rack figures are C unless operator states them. |
| Raxio Angola AO1, Cacuaco | Luanda | Operational | Raxio official Angola page/opening release + Uptime list | Official 2025 opening release: 3 MW IT, 800+ racks, USD 30M, Cacuaco/Luanda. Uptime list should be checked for exact certification type and facility name. |
| Paratus Angola DC1/DC2, Patriota/Benfica | Luanda | Operational | Paratus official data-center services page + Paratus/DCD | Paratus official page markets data centers in Angola; DCD says two Luanda campus facilities launched 2017/2019 with 1,500 and 7,000 server capacities. |
| Paratus Angola third DC / Tier-IV-by-design project | Luanda | Planned unless construction evidence found | Paratus official 2023 announcement + DCD/Developing Telecoms | Official Paratus announcement states third Angola DC, >10 MW IT, >2,000 cabinets, 30,000 sqm plot in Luanda. Re-verify progress before marking under construction/operational. |
| Africell Angola Kings Tower data center | Luanda | Operational | Africell official release | Opened Oct 2021 at Africell Angola HQ in Kings Tower, central Luanda; supports network/cloud/hosting. Capacity not public. |
| Unitel Luanda Sul / Filda DR leads | Luanda | Lead / operational only if official source found | Unitel official pages, INACOM, directories, press | Directories list facilities/power, but require Unitel/press/procurement corroboration. |
| Movicel / Angola Telecom / MSTelcom / Startel core DCs | Luanda or provinces | Lead unless named facility evidence found | Operator pages + INACOM + procurement | Telecom network-core sites are not automatically commercial DCs. |
| AnyConnect / Visium Lubango DR facility | Huila | Planned lead | Visium/AnyConnect official release if available; otherwise datacenters.com/Newswire as B/C | Reported 2025 framework includes secondary DR facility in Lubango and fibre build. Treat as planned until binding project/construction evidence appears. |

---

## 3. Province coverage matrix for the 18-manifest model

Run each manifest division even when official Angola has moved to 21 provinces. Use Portuguese names as aliases.

| Manifest division | Portuguese aliases and new-map caveat | Baseline expectation | Official queries |
|---|---|---|---|
| Bengo | Bengo; Caxito; Icolo e Bengo evidence maps to Bengo unless manifest changes | Negative except connectivity/government IT | `"Bengo" "centro de dados"`, `"Caxito" "data center"`, `site:gov.ao Bengo TIC` |
| Benguela | Benguela; Lobito; Catumbela; Lobito Corridor | Oil/logistics/telecom lead only | `"Benguela" "data center"`, `"Lobito" "centro de dados"`, `"Corredor do Lobito" digital` |
| Bie | Bie; Bié; Kuito/Cuito | Negative except public-sector ICT | `"Bie" OR "Bié" "centro de dados"`, `"Kuito" servidores` |
| Cabinda | Cabinda | Oil/internal IT lead only | `"Cabinda" "data center"`, `"Cabinda" servidores Sonangol` |
| Cuando Cubango | Cuando Cubango; Cuando; Cubango; Menongue; Mavinga | Negative; split evidence maps here | `"Cuando Cubango" "centro de dados"`, `"Menongue" data center`, `"Cubango" TIC` |
| Cunene | Cunene; Ondjiva | Negative | `"Cunene" "centro de dados"`, `"Ondjiva" servidores` |
| North Cuanza | Cuanza Norte; Kwanza Norte; N'dalatando | Negative | `"Cuanza Norte" "data center"`, `"N'dalatando" servidores` |
| South Cuanza | Cuanza Sul; Kwanza Sul; Sumbe | Negative | `"Cuanza Sul" "centro de dados"`, `"Sumbe" TIC servidores` |
| Huambo | Huambo | University/telecom lead only | `"Huambo" "data center"`, `"Huambo" "inteligencia artificial"`, `"Universidade Jose Eduardo dos Santos" servidores` |
| Huila | Huila; Huíla; Lubango | Watch AnyConnect/Visium DR lead | `"Lubango" "data center"`, `"Huila" "centro de dados"`, `"AnyConnect" Lubango` |
| North Lunda | Lunda Norte; Dundo | Mining/internal IT lead only | `"Lunda Norte" "data center"`, `"Dundo" servidores` |
| South Lunda | Lunda Sul; Saurimo | Mining/internal IT lead only | `"Lunda Sul" "centro de dados"`, `"Saurimo" servidores` |
| Luanda | Luanda; Camama; Rangel; Cacuaco; Patriota; Benfica; Talatona; Viana; Icolo e Bengo split caveat | Highest priority; known facilities | `"Luanda" "data center"`, `"Camama" INFOSI`, `"Cacuaco" Raxio`, `"Patriota" Paratus` |
| Malanje | Malanje | Negative except public-sector ICT | `"Malanje" "data center"`, `"Malanje" servidores TIC` |
| Moxico | Moxico; Luena; Moxico Leste; Cazombo | Negative; split evidence maps here | `"Moxico" "centro de dados"`, `"Luena" data center`, `"Moxico Leste" TIC` |
| Namibe | Namibe; Mocamedes/Moçâmedes | Port/energy/telecom lead only | `"Namibe" "data center"`, `"Mocamedes" servidores` |
| Uige | Uige; Uíge | Negative | `"Uige" OR "Uíge" "centro de dados"`, `"Uíge" TIC` |
| Zaire | Zaire; Mbanza Kongo; M'banza-Kongo; Soyo | Oil/gas/internal IT lead only | `"Soyo" "data center"`, `"Zaire" servidores Sonangol` |

Promotion rule: A non-Luanda lead becomes a project entry only with official/operator naming of the physical site, a named tender/award, or strong press with a named site and accountable source. Otherwise keep it as negative/no-project or C lead.

---

## 4. Extraction and grading rules

For every candidate, extract:

```text
name
operator / developer / owner
status: planned | under_construction | operational | decommissioned | unknown
manifest division
city / municipality / bairro / address
capacity_mw (null unless source-supported)
racks / cabinets / sqm (null unless source-supported)
source_urls
evidence_date
evidence_grade
notes: why counted, what remains unverified
```

Grade upgrades:

- **A**: official opening, operator-owned facility page, regulator/procurement/gazette record, Uptime certification naming the facility, or official cloud-region page.
- **B**: reputable trade/local press with named facility/site/date/capacity, especially where quoting operator/ministry officials.
- **C**: directories, aggregators, broker pages, social media, vague market-report snippets, or service-only pages.

Do not count:

- AngoNAP Fortaleza in Brazil.
- AngonIX/IXPs, PeeringDB presences, CDN PoPs, submarine-cable landing stations, or satellite ground stations unless a data center facility is independently named.
- Generic cloud/hosting/VPS service pages with no Angola physical site.
- Provincial telecom exchanges/server rooms unless the source explicitly frames them as a data center and gives a site.

Final confidence language for Angola should be conservative: Luanda has confirmed commercial/government facilities; most other provinces are negative-by-default with occasional DR, university, bank, oil/gas, or telecom-internal leads requiring hard verification.
