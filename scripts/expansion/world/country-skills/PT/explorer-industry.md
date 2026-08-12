# PT Explorer Industry - Portugal datacenter vendor, trade-press, and district query methodology

Date: 2026-08-12. Scope: Portugal datacenter enumeration methodology focused on Portuguese colo providers, cloud/local-zone signals, trade press, associations, and district-level query patterns. Country code: **PT**. Reliability grades: **A** = official/primary source (operator facility page, cloud official region/local-zone page, public consultation/AIA/procurement record, municipality or government notice), **B** = strong secondary/trade press or market report with named project/operator/location, **C** = directory/aggregator/social/weak lead.

---

## 0. Portugal-specific frame

- Portugal has no single public registry of commercial datacenters. Enumerate by combining **operator pages**, **PortugalDC/industry ecosystem leads**, **DCD + Portuguese business press**, **cloud/local-zone pages**, **municipal announcements**, and **APA/Participa/SIAIA environmental files** for the largest campuses.
- The manifest divisions are districts/autonomous regions. Two division labels are machine-translated: **White Castle = Castelo Branco** and **Royal Town = Vila Real**. Use the Portuguese district names in search.
- Main commercial clusters are **Lisboa/Carnaxide/Prior Velho/Vila Franca de Xira**, **Sines/Setubal**, **Covilha/Castelo Branco**, **Porto/Matosinhos/Leixoes**, **Viseu**, and new energy-led inland/southern projects such as **Pego/Abrantes/Santarem** and **Aljustrel/Beja**.
- Portugal queries must use both English and Portuguese spellings: `data center`, `data centre`, `datacenter`, `centro de dados`, `centro de processamento de dados`, `CPD`, `centro de computacao`, `sala tecnica`, `alojamento`, `colocation`, `housing`, `cloud`, `IA`, `inteligencia artificial`.
- Large projects often surface as **energy, industrial-zone, or environmental-permit** stories before colocation marketing pages exist. Search with `ligacao a rede`, `MVA`, `MW`, `REN`, `EDP`, `subestacao`, `ZILS`, `parque empresarial`, `zona industrial`, `pedido de informacao previa`, `licenciamento`, `AIA`, `RECAPE`, `consulta publica`.
- Treat cable landing stations as leads, not automatically as full colocation datacenters. In Portugal, **Sines** and the **Azores** are critical because subsea cable landing, cloud/AI infrastructure, and datacenter construction overlap.

---

## 1. Associations, market context, and events

| Source | URL | Use | Grade |
|---|---|---|---|
| PortugalDC - Associacao Portuguesa de Centros de Dados | https://portugaldc.pt/en/home/ and https://portugaldc.pt/en/portugaldc/ | National datacenter association; seed list for ecosystem actors, policy, events, sponsors, and government-facing sector messaging. Not a facility registry. | B |
| APDC - Associacao Portuguesa para o Desenvolvimento das Comunicacoes | https://www.apdc.pt/ | Broader telecom/digital association. Use for cloud/connectivity policy events and sector contacts. | B/C |
| Atlantic Convergence / subsea-connectivity events | https://www.atlanticconvergence.com/ | Useful for Sines/Lisbon/Azores cable, cloud, AI, and energy ecosystem leads. Verify facilities elsewhere. | C/B |
| Copenhagen Economics report for Portugal datacenter impact | https://copenhageneconomics.com/wp-content/uploads/2025/07/CE-Report_Economic-contribution-of-data-centres-in-Portugal_EN.pdf | Market/ecosystem context; includes named operators such as Start Campus, Equinix, AtlasEdge, and Edged. | B for context, C for facility details unless independently verified |
| ResearchAndMarkets / Arizton / Business Wire portfolio summaries | Examples: https://www.businesswire.com/news/home/20250626092815/en/Portugal-Data-Center-Portfolio-Report-2025-with-Atlas-Edge-Claranet-DECSIS-Equinix-Merlin-Properties-Edged-Energy-NOS-Portugal-Telecom-Quetta-Data-Centers-REN-Start-Campus-Templus---ResearchAndMarkets.com and https://www.arizton.com/market-reports/portugal-data-center-colocation-market | Paid market-report snippets identify operator universe and locations such as Lisbon, Covilha, Sines, Ermesinde, Riba de Ave, Madeira. Use only as leads. | C/B |

Association/event queries:

```text
site:portugaldc.pt "centro de dados" Portugal
site:portugaldc.pt "data center" Portugal "{operator}"
site:apdc.pt "data center" OR "centro de dados"
"PortugalDC" "{operator}" "data center"
"Atlantic Convergence" Sines "data center"
```

---

## 2. Trade press and Portuguese business press

Use trade press to discover project names, municipalities, developers, MW/MVA claims, and schedule. Promote to A only after confirming with operator, municipality, APA/Participa/SIAIA, Diario da Republica, or procurement records.

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Dynamics Portugal tag | https://www.datacenterdynamics.com/en/tags/portugal/ | Best English-language running feed for Portugal: Start Campus/Sines, Microsoft/Nscale, FF Ventures/Aljustrel, Guimaraes RNCA, Google Azores/Sines cables, Madeira/NOS, public-sector DR centers. | B |
| DCD Start Campus/Microsoft | https://www.datacenterdynamics.com/en/news/microsoft-to-spend-10bn-on-ai-data-centers-in-portugal/ and https://www.datacenterdynamics.com/en/news/start-campus-launches-sin01-facility-in-sines-portugal/ | Sines AI-campus scale and timeline leads; verify with Start Campus and APA/SIAIA. | B |
| DCD FF Ventures Aljustrel | https://www.datacenterdynamics.com/en/news/renewables-firm-ff-ventures-plans-data-center-in-aljustrel-portugal/ | Beja district lead from municipal announcement; pivot to Aljustrel municipal/licensing records. | B |
| DCD Guimaraes RNCA | https://www.datacenterdynamics.com/en/news/portugal-to-host-new-data-center/ | Braga district public/HPC datacenter lead on University of Minho Azurem campus. | B |
| DCD Google Azores/Sines cables | https://www.datacenterdynamics.com/en/news/google-to-develop-new-cable-landing-stations-in-azores-and-hawaii-for-upcoming-subsea-cable-systems/ and https://www.datacenterdynamics.com/en/news/google-lands-nuvem-cable-in-portugal/ | Azores and Sines cable landing/datacenter leads; verify against Google, municipality, and cable documentation. | B |
| ECO / Sapo | https://eco.sapo.pt/ | Strong Portuguese business press. Good for Sines, Pego/Abrantes, energy, financing, real estate, and government-plan items. | B |
| Jornal de Negocios | https://www.jornaldenegocios.pt/ | Strong on corporate investments, M&A, Altice/Covilha, CTS/Viana do Castelo, Microsoft/Start Campus. | B |
| Portugal News | https://www.theportugalnews.com/ | English-language Portuguese news. Useful for summaries of Sines, PNCD, energy/grid risk, government announcements; often based on Lusa/local press. | B/C |
| IT Channel / Business IT / Computerworld Portugal | https://www.itchannel.pt/ , https://business-it.pt/ , https://www.computerworld.com.pt/ | Portuguese IT trade press for NOS, public-sector, cloud, regional datacenter refreshes. | B |
| AICEP PortugalGlobal | https://portugalglobal.pt/en/news/ | Investment-promotion mirror for foreign investor projects such as FF Ventures. | B when based on municipal/company notice |
| RTP/Lusa/local press | https://www.rtp.pt/ plus local newspapers/radios | Good for older facilities and small municipal projects; pivot to municipality/procurement. | B/C |
| Directories | DataCenterMap https://www.datacentermap.com/portugal/ , Datacenters.com https://www.datacenters.com/locations/portugal , Baxtel https://baxtel.com/data-centers/portugal , Cloudscene, PeeringDB, Inflect | Best for small colo/edge address discovery. Treat capacity/status as C unless the operator page confirms. | C |

Trade/source queries:

```text
site:datacenterdynamics.com/en/tags/portugal/ "Portugal"
site:datacenterdynamics.com/en/news/ Portugal "data center" "{district OR town OR operator}"
site:eco.sapo.pt ("data center" OR "centro de dados") Portugal "{district OR town}"
site:jornaldenegocios.pt ("data center" OR "centro de dados") "{operator OR town}"
site:itchannel.pt "data center" Portugal
site:business-it.pt "data center" Portugal
site:theportugalnews.com "data centre" Portugal Sines OR Lisbon OR Pego
site:portugalglobal.pt/en/news "data center" Portugal
```

---

## 3. Operator and vendor seed list

Official operator pages are **A** for existence/location and **B** for marketed capacity unless backed by environmental, procurement, or audited documents.

| Operator/developer | Districts/locations to check | Official / strong source | Notes |
|---|---|---|---|
| Start Campus | Setubal - Sines | https://www.startcampus.pt/ and media page https://www.startcampus.pt/pt/media | Flagship SINES DC / Sines 4.0 campus. Official site and releases cite 1.2 GW campus, SIN01 operational, SIN02 planned/under construction. Cross-check APA/SIAIA AIA 3633 and Participa RECAPE. |
| Equinix | Lisboa - Lisbon metro | https://www.equinix.com/data-centers/europe-colocation/portugal-colocation and Lisbon page https://www.equinix.com/data-centers/europe-colocation/portugal-colocation/lisbon-data-centers | LS1 and LS2. Equinix pages confirm two Lisbon data centers and colocation space. |
| AtlasEdge | Lisboa - Carnaxide/Oeiras | https://atlasedge.com/data-centres/lisbon/ and https://atlasedge.com/atlasedge-secures-e253-million-in-green-financing-for-lisbon-campus-expansion/ | LIS001/LIS002/LIS003 campus. Financing release states combined 21.1 MW for LIS001/LIS002 and future 30 MW campus. |
| MERLIN Properties / Edged Energy | Lisboa - Vila Franca de Xira | https://www.edged.es/news/construction-of-new-ai-campus-in-lisbon-portugal and Portuguese page https://pt.edged.es/news/construction-of-new-ai-campus-in-lisbon-portugal | 180 MW AI campus near Lisbon; search Vila Franca de Xira municipality and environmental records for permits. |
| Asterion / Altice / MEO / Portugal Telecom Data Center | Castelo Branco - Covilha; Lisbon/Madeira possible legacy estate | https://www.asterionindustrial.com/asterion-acquires-covilha-data-center-campus-from-altice-portugal-for-e120m/ , https://en.meo.pt/business/solutions/cloud-datacenter/data-centers/covilha , Uptime listing https://uptimeinstitute.com/component/tierachievement/client/portugal-telecom-data-center-sa/212 | Covilha campus is a key existing Portuguese facility; Asterion release says 6.8 MW installed with expansion potential. Uptime confirms tier awards. |
| IP Telecom | Lisboa, Porto, Viseu | https://www.iptelecom.pt/ and https://www.iptelecom.pt/pt-pt/servicos/infraestruturas | Official pages state 3 owned datacenters in Lisbon, Porto, and Viseu, with ISO 27001 and 99.99% monthly availability. |
| Claranet Portugal | Lisboa/Prior Velho/Beato/Parque das Nacoes leads | https://www.claranet.pt/ plus directory leads | Official Portuguese site is useful for services, but facility pages are harder to expose. Use Datacenters.com/DataCenterMap/Inflect as C leads, then verify with Claranet or local permits. |
| NOS | Porto/Matosinhos, Azores/Ponta Delgada, Madeira/Funchal | https://www.nos.pt/empresas/ and press/trade pages | Often appears through IT Channel/Business IT/DCD/local news for island and regional facilities. Verify against NOS pages, local press, and procurement where possible. |
| Decsis | Evora | https://www.decsis.com/ or https://es.decsis.com/en/about-us/ | Company history and directories identify Evora datacenter; RTP/Lusa reported Decsis/HP investment. |
| FF Ventures | Beja - Aljustrel/Rio de Moinhos | https://ffventures.pt/ plus Aljustrel municipality/DCD/AICEP | Renewable-energy developer; DCD/AICEP report planned datacenter at Mancoca Business and Logistics Park. Verify municipal protocol/licensing. |
| EDC One / Pego projects | Santarem - Abrantes/Pego | local/ECO/municipal sources | Large Pego/Abrantes proposals. Search companies, municipal decisions, `pedido de informacao previa`, energy connection, and environmental licensing. |
| Hyperion II Renewables Services | Santarem - Abrantes/Pego | local press/municipal sources | Reported second Pego-area datacenter with 200 MVA connection. Needs A-grade municipal/environmental confirmation before counting. |
| Voltekko | Setubal - Alcochete | https://www.voltekko.com/ plus AICEP/DataCenterMap | Planned AI/HPC eco-responsible datacenter. Directory/AICEP leads require company/municipal verification. |
| Google | Azores - Lagoa, Sao Miguel; Setubal - Sines cable landing | https://cloud.google.com/about/locations and Google cable announcements/blogs, plus DCD/Submarine Networks | No Portugal Google Cloud region in the official cloud-region list, but Google cable landing/datacenter infrastructure is a high-value lead. |
| Public/R&D operators | Braga/Guimaraes, Aveiro, Faro, Coimbra, Leiria, Guarda, Azores, Madeira | FCT/RNCA, university pages, Diario da Republica, regional-government portals | These are not commercial colo, but often real datacenter assets. Use procurement and institutional pages for A-grade evidence. |

Operator query templates:

```text
"{operator}" Portugal "data center" OR "centro de dados"
"{operator}" "{district}" "data center" OR "datacenter"
"{operator}" "{town}" MW OR MVA OR "capacidade"
"{operator}" "{town}" "licenciamento" OR "pedido de informacao previa" OR "consulta publica"
site:{operator-domain} Portugal "data center"
site:{municipality-domain} "{operator}" "centro de dados"
```

---

## 4. Cloud and hyperscale region/local-zone sweep

Portugal currently has stronger **local-zone, edge, subsea, and dedicated AI-campus** signals than standard public-cloud region signals. Cloud pages prove cloud-region/local-zone existence, not exact buildings.

| Provider | Official page | Portugal signal | Grade |
|---|---|---|---|
| AWS | Local Zones page https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ ; AWS launch post https://press.aboutamazon.com/aws/2026/1/aws-launches-aws-european-sovereign-cloud-and-announces-expansion-across-europe ; AWS ESC FAQ https://aws.eu/faq/ | AWS lists announced Lisbon, Portugal sovereign Local Zone `eusc-de-east-1-lis-1a` under AWS European Sovereign Cloud Germany. No ordinary Portugal AWS Region. | A for local-zone announcement |
| Microsoft Azure | Azure region list https://learn.microsoft.com/en-us/azure/reliability/regions-list and geographies https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No standard Azure Portugal region in official list; Portugal signal comes from Microsoft/Nscale/Start Campus AI infrastructure commitments at Sines. | A for no/yes region list; B for physical Sines mapping unless Microsoft/operator source |
| Google Cloud | Google locations https://cloud.google.com/about/locations and Google data center locations https://datacenters.google/locations | No standard Google Cloud Portugal region listed. Separate Google cable landing/data infrastructure in Azores/Sines is a project lead, not a GCP region. | A for region list; B for cable-project leads |
| Oracle Cloud | Oracle public cloud regions https://www.oracle.com/cloud/public-cloud-regions/ | No Portugal OCI public region found; nearest Iberian/EU signals are Spain/France/Italy/others. | A for official region list |
| DE-CIX / interconnection | Start Campus release/media, DE-CIX pages | DE-CIX PoP at SINES DC is a useful carrier-neutral interconnection lead; not a separate datacenter. | B/A depending on source |

Cloud queries:

```text
site:aws.amazon.com Portugal "Local Zone"
site:aws.eu Portugal "Local Zones"
site:learn.microsoft.com azure regions Portugal
site:cloud.google.com/about/locations Portugal
site:oracle.com/cloud/public-cloud-regions Portugal
"Microsoft" "Start Campus" Sines "data center"
"Nscale" "Start Campus" "Microsoft" Sines GPU
"Google" Nuvem Sol Sines Azores "cable landing station" "data center"
```

---

## 5. Official verification channels useful to industry leads

Even for an industry/vendor explorer, these sources are necessary to convert B/C leads into A-grade records.

| Source | URL | Use | Grade |
|---|---|---|---|
| Participa public consultations | https://participa.pt/ | Search public consultations by project. Example Sines: https://participa.pt/pt/consulta/verificacao-do-relatorio-de-conformidade-ambiental-do-projeto-de-execucao-do-data-center-sines-40 | A |
| APA/SIAIA environmental documents | https://siaia.apambiente.pt/ | AIA/RECAPE/EIA PDFs for large projects. Example Sines AIA 3633 PDFs appear under `siaia.apambiente.pt/AIADOC/AIA3633/`. | A |
| Diario da Republica / public procurement | https://diariodarepublica.pt/ | Best source for public/university/regional-government datacenter procurement and maintenance. Search exact Portuguese terms plus district. | A |
| Base.gov public contracts | https://www.base.gov.pt/ | Contract notices/awards after Diario da Republica lead. Useful for datacenter works, cooling, UPS, generators, disaster recovery. | A |
| Municipal portals | `https://www.cm-{municipio}.pt/` or municipality-specific domains | Protocols, prior-information requests (`pedido de informacao previa`), tax exemptions, urban planning, public notices. Critical for Aljustrel, Abrantes/Pego, Vila Franca de Xira, Sines, Alcochete. | A/B |
| REN / E-REDES / DGEG energy portals | https://www.ren.pt/ , https://www.e-redes.pt/ , https://www.dgeg.gov.pt/ | Grid-connection and substation leads for 100+ MW projects. Search by project/operator/town plus `MVA`, `subestacao`, `ligacao a rede`. | A/B |

Official-verification queries:

```text
site:participa.pt ("data center" OR "centro de dados" OR datacenter) Portugal
site:siaia.apambiente.pt ("Data Center" OR "Centro de Dados" OR datacenter)
site:diariodarepublica.pt ("Centro de Dados" OR Datacenter OR "Data Center") "{district}"
site:base.gov.pt ("centro de dados" OR datacenter) "{operator OR municipality}"
site:cm-{municipality}.pt ("centro de dados" OR "data center" OR datacenter)
"{project}" "AIA" OR "RECAPE" OR "Estudo de Impacte Ambiental"
"{project}" "pedido de informacao previa" OR "licenciamento"
"{project}" "MVA" OR "REN" OR "subestacao" OR "ligacao a rede"
```

---

## 6. District-level enumeration recipes

For every district, run three passes: **vendor/trade**, **municipal/energy**, and **official procurement/environmental**. Use Portuguese district and municipality names. The manifest's division names are shown in parentheses where different.

### 6.1 High-priority commercial and hyperscale districts

| Manifest division | Portuguese search geography | Priority operators/projects | District query seeds |
|---|---|---|---|
| Lisbon | Lisboa, Oeiras/Carnaxide, Loures/Prior Velho, Parque das Nacoes, Vila Franca de Xira | Equinix LS1/LS2, AtlasEdge LIS001/2/3, MERLIN/Edged 180 MW, Claranet, IP Telecom, Altice/MEO legacy | `"Lisboa" ("data center" OR "centro de dados" OR datacenter)`, `"Carnaxide" AtlasEdge`, `"Vila Franca de Xira" Edged OR Merlin "centro de dados"`, `site:cm-vfxira.pt "centro de dados"`, `"Prior Velho" Claranet datacenter`, `"Loures" "data center"` |
| Setubal | Setubal, Sines, Santiago do Cacem, Alcochete, Barreiro, Palmela | Start Campus SINES DC/Sines 4.0, Google/Nuvem Sines cable landing, Voltekko Alcochete, Online.pt Barreiro | `"Sines" "Data Center Sines 4.0"`, `site:participa.pt Sines "data center"`, `site:siaia.apambiente.pt AIA3633`, `"SINES DC" "SIN01" "SIN02"`, `"Alcochete" Voltekko "data center"`, `"Barreiro" "centro de dados"` |
| Porto | Porto, Matosinhos, Leixoes, Ermesinde, Maia, Vila Nova de Gaia | IP Telecom Porto, NOS Matosinhos, NFSI Telecom, APDL campus, MEO/Porto cable/interconnection leads | `"Porto" "data center" colocation`, `"Matosinhos" NOS "data center"`, `"APDL Data Center Campus"`, `"Leixoes" "data center"`, `"Ermesinde" "centro de dados"`, `site:cm-matosinhos.pt "centro de dados"` |
| Castelo Branco (White Castle) | Castelo Branco, Covilha, Fundao | Asterion/Altice/MEO Covilha campus | `"Covilha" "data center"`, `"Covilha Data Center Campus" Asterion Altice`, `site:cm-covilha.pt "centro de dados"`, `site:uptimeinstitute.com Covilha "Portugal Telecom Data Center"` |
| Santarem | Santarem, Abrantes, Pego, Tomar, Cartaxo | EDC One Pego, Hyperion II Renewables Services Pego, power-station redevelopment | `"Abrantes" Pego "data center"`, `"Pego" "centro de dados"`, `"Hyperion II" "200 MVA" Pego`, `"EDC One" Abrantes "data center"`, `site:cm-abrantes.pt "centro de dados" OR "pedido de informacao previa"` |
| Beja | Beja, Aljustrel, Rio de Moinhos, Sines-adjacent Alentejo energy corridors | FF Ventures Aljustrel | `"Aljustrel" "centro de dados"`, `"FF Ventures" Aljustrel "data center"`, `"Mancoca" "data center"`, `site:mun-aljustrel.pt "centro de dados"`, `"Rio de Moinhos" "data center"` |
| Azores | Acores, Sao Miguel, Lagoa, Ponta Delgada, Terceira | Google Azores CLS/Nuvem/Sol, Azores Cloud, NOS Ponta Delgada | `"Acores" "data center"`, `"Lagoa" "Google" "Nuvem" "Sol"`, `"Tecnoparque da Lagoa" "data center"`, `"Ponta Delgada" NOS "data center"`, `site:portal.azores.gov.pt "centro de dados"` |
| Madeira | Madeira, Funchal, Virtudes, Machico/Agua de Pena | NOS Madeira/Funchal, EMACOM/EEM Tier III, CTM/MEO Madeira | `"Madeira" "data center"`, `"Funchal" "centro de dados"`, `"EMACOM" "Data Center"`, `"Virtudes" "data center"`, `site:madeira.gov.pt datacenter`, `site:diariodarepublica.pt EMACOM "Data Center"` |

### 6.2 Secondary districts with public/R&D, regional edge, or supply-chain leads

| Manifest division | Portuguese search geography | Known/likely lead type | District query seeds |
|---|---|---|---|
| Aveiro | Aveiro, Gloria e Vera Cruz, Ilhavo | University of Aveiro datacenter reinforcement, IT Aveiro | `"Aveiro" "Centro de Dados" Universidade`, `site:diariodarepublica.pt "Centro de Dados da Universidade de Aveiro"`, `"Datacenter" "Gloria e Vera Cruz"`, `"Instituto de Telecomunicacoes" Aveiro datacenter` |
| Braga | Braga, Guimaraes, Azurem, Riba de Ave | RNCA/CNCA Guimaraes HPC datacenter, possible Riba de Ave/edge leads | `"Guimaraes" "data center"`, `"Azurem" "centro de dados"`, `"RNCA" Guimaraes "data center"`, `"DST" "centro de supercomputacao" Guimaraes`, `"Riba de Ave" "data center"` |
| Braganca | Braganca | Polytechnic/institutional datacenter lead | `"Braganca" "datacenter"`, `"Instituto Politecnico de Braganca" "Datacenter"`, `site:ipb.pt "centro de dados"` |
| Coimbra | Coimbra | AIBILI certified clinical data centre; university/HPC leads | `"Coimbra" "data centre" AIBILI`, `"Coimbra" "centro de dados"`, `site:uc.pt "centro de dados"`, `site:diariodarepublica.pt Coimbra datacenter` |
| Evora | Evora, Parque Industrial e Tecnologico de Evora | Decsis Evora, smaller colo/enterprise | `"Evora" "data center" Decsis`, `"Parque Industrial e Tecnologico de Evora" "centro de dados"`, `site:cm-evora.pt datacenter` |
| Faro | Faro, Algarve, Campus da Penha | University of Algarve TECH HUB datacenter, RNCA visualization center | `"Faro" "data center"`, `"Universidade do Algarve" "Data Center" "Campus da Penha"`, `"TECH HUB Data Center" UAlg`, `site:ualg.pt "centro de dados"` |
| Guarda | Guarda | ULS Guarda/Hospital Sousa Martins public datacenter maintenance | `"Guarda" "Data Center" "Hospital Sousa Martins"`, `site:diariodarepublica.pt Guarda "Data Center"`, `"ULS Guarda" "centro de dados"` |
| Leiria | Leiria, Campus 2 | Polytechnic Leiria datacenter container | `"Leiria" "Datacenter"`, `"Politecnico de Leiria" "datacenter"`, `"Rittal" "Leiria" "data center"`, `site:ipleiria.pt "centro de dados"` |
| Portalegre | Portalegre, Elvas, Alto Alentejo | CIMAA shared-services datacenter | `"Portalegre" "centro de dados" CIMAA`, `"Alto Alentejo" "centro de dados informatico"`, `"Elvas" "centro de dados" "CIMAA"` |
| Viana do Castelo | Viana do Castelo, Neiva, Darque | CTS Group datacenter production/supply-chain campus; APDL Leixoes/Viana port org leads | `"Viana do Castelo" "data center"`, `"CTS" "centro de producao" "data centers"`, `"Viana do Castelo" EPOD "data center"`, `site:cm-viana-castelo.pt "centro de dados"` |
| Vila Real (Royal Town) | Vila Real, Vila Pouca de Aguiar, Sabroso de Aguiar | MTGREEN zero-carbon datacenter lead | `"Vila Real" "data center"`, `"Vila Pouca de Aguiar" datacenter`, `"Sabroso de Aguiar" "centro de dados"`, `"MTGREEN" datacenter Portugal` |
| Viseu | Viseu | IP Telecom Viseu, AR Telecom/Viseu directory leads | `"Viseu" "data center" "IP Telecom"`, `"Viseu" "centro de dados"`, `"Av. Cap. Homem Ribeiro" "data center"`, `site:iptelecom.pt Viseu DataCenter` |

### 6.3 Low-signal districts: run broad energy/municipal sweeps

For districts without strong known commercial leads, focus on municipal industrial parks, public procurements, hospitals/universities, and renewables-grid projects:

```text
"{district}" ("centro de dados" OR datacenter OR "data center")
"{district}" ("colocation" OR housing OR alojamento) "servidores"
"{district}" ("parque empresarial" OR "zona industrial") ("centro de dados" OR "data center")
"{district}" ("MW" OR MVA OR "subestacao" OR "ligacao a rede") ("data center" OR "centro de dados")
site:diariodarepublica.pt "{district}" ("Centro de Dados" OR Datacenter)
site:base.gov.pt "{district}" ("centro de dados" OR datacenter)
site:cm-{main_municipality}.pt ("centro de dados" OR datacenter OR "data center")
```

Apply that broad sweep especially to **Coimbra, Braganca, Guarda, Portalegre, Viana do Castelo, Vila Real, Faro, Leiria**, and any inland district where a renewable developer, substation, former power station, or logistics park appears in press.

---

## 7. Capacity/status extraction and grading

Capture these fields per lead:

- facility/project name, operator/developer, municipality, district, exact site/address if public;
- evidence URL(s), evidence date, evidence grade;
- status: announced/protocol, prior information request, licensing/AIA, approved, construction, ready for service, operational, expansion, decommissioned;
- capacity evidence: IT MW, grid MW/MVA, gross area, white space, number of buildings, phases, RFS dates, backup generator count, cooling method;
- whether it is commercial colocation/hyperscale, enterprise/public-sector datacenter, cable landing station, or supply-chain site.

Evidence hierarchy:

1. **A** - operator facility pages, cloud official pages, APA/SIAIA/Participa, Diario da Republica/Base.gov, municipal resolutions/protocols, Uptime Institute awards for named facility existence.
2. **B** - DCD, ECO, Jornal de Negocios, IT Channel, Business IT, RTP/Lusa, AICEP, Portugal News when they name operator + municipality + project details.
3. **C** - DataCenterMap, Datacenters.com, Baxtel, Cloudscene, Inflect, LinkedIn, market-report snippets, conference materials.

Status sanity rules:

- `protocolo`, `memorando`, `investimento anunciado`, and `manifestacao de interesse` = announced/planned only.
- `pedido de informacao previa`, `licenciamento`, `AIA`, `RECAPE`, `consulta publica` = permitting; do not mark construction unless work has started.
- `obra`, `construcao`, `empreitada`, `adjudicacao`, `inicio da construcao` = construction if from municipality/operator/procurement.
- `inaugurado`, `operacional`, `ready for service`, `clientes instalados`, `em funcionamento` = operational.
- MVA is not IT MW. Record it as grid/import capacity unless the source explicitly gives IT load.
- Avoid double counting: Start Campus/SINES DC/Data Center Sines 4.0/SIN01-SIN06 are campus and phase aliases; Altice/MEO/Portugal Telecom Data Center Covilha/Asterion Covilha are owner/operator aliases; RNCA/CNCA/University of Minho Guimaraes/DST are the same public HPC facility.

---

## 8. Recommended workflow

1. Seed the database from official operator pages: Start Campus, Equinix, AtlasEdge, Edged/MERLIN, Asterion/MEO Covilha, IP Telecom, Claranet, NOS, Decsis, FF Ventures, Voltekko, Google cable infrastructure.
2. Sweep DCD Portugal tag, ECO, Jornal de Negocios, IT Channel, Business IT, RTP/Lusa, Portugal News, and AICEP for the same operator/town names.
3. For every large or planned project, pivot to municipality + APA/Participa/SIAIA + Diario da Republica/Base.gov using Portuguese terms.
4. For every manifest district, run the district recipes in Section 6 and add municipality-specific searches for the largest cities and industrial parks.
5. Use directories only to fill gaps in small colo/edge facilities; promote records only after operator or independent source confirmation.
6. Re-check cloud official pages quarterly: Portugal currently has an announced AWS sovereign Local Zone in Lisbon, but no standard AWS/Azure/GCP/OCI public cloud region found in official region lists.
