# PT Explorer — Official / Regulatory / Cloud Pipeline for Portugal Datacenter Enumeration

Date: 2026-08-12. Scope: how to enumerate Portugal datacenter projects from official/regulatory sources first, then confirm with cloud/operator pages and trade press. Reliability grades: **A** = official/primary source; **B** = strong secondary/trade press/operator announcement; **C** = weak aggregator, market report, local rumor, or unverified press.

Portugal has no single public national datacenter facility registry. The reliable method is to join five pipelines: (1) national policy / PIN strategic-investment records, (2) environmental assessment and public-consultation files, (3) municipal planning/licensing records, (4) electricity transmission/distribution connection evidence, and (5) cloud/colo/operator official pages.

---

## 0. Structural Facts

- The national policy anchor is the **Plano Nacional de Centros de Dados (PNCD)**, approved by **Resolução do Conselho de Ministros n.º 70/2026, de 13 de abril**. It explicitly says Portugal has low installed capacity versus the European average, an identified project portfolio, and barriers including long bureaucratic processes, unclear procedures, grid access constraints, and dispersed demand. Source: https://diariodarepublica.pt/dr/detalhe/resolucao-conselho-ministros/70-2026-1084345989. **Grade A.**
- PNCD/PAPNCD 2026-2027 is the source to watch for new "green zones", licensing simplification, centralized investor interaction, and national prioritization. Government FAQ: https://portugal.gov.pt/gc25/comunicacao/comunicados/perguntas-e-respostas-plano-nacional-de-dados. **Grade A.**
- **AICEP / Portugal Global** is the investor-facing channel for strategic projects and PIN/Potencial Interesse Nacional status. Example: SINES Data Center / Start Campus is described as PIN and AICEP-supported in AICEP communications. Source: https://portugalglobal.pt/noticias/2025/novembro/investimento-da-microsoft-portugal-como-hub-estrategico-de-ia/. **Grade A-/B+** depending on whether it is restating an official status or a company investment claim.
- **Planning is municipal**. Large DCs need municipal urbanismo records: PIP (`pedido de informação prévia`), `licenciamento urbanístico`, `licença de construção`, `obras de urbanização`, `deliberação de câmara`, and sometimes PDM / unidade de execução amendments. Municipal minutes and agenda PDFs are often the first public sign before national press.
- **Environmental records are central**. Datacenters themselves may not always be a listed EIA project type, but large campuses trigger EIA/RECAPE through industrial-zone works, power lines, substations, water/cooling infrastructure, backup generation, wind/solar supply, or associated grid works. The Start Campus Sines filings are the model case in APA/SIAIA.
- **Power is the limiting evidence**. High-confidence capacity needs REN transmission, E-REDES distribution, DGEG energy licensing, or EIA/RECAPE details for substations/lines. Treat marketing GW claims as design/secured capacity until tied to a phase, substation, or grid connection document.
- **ANACOM is not a datacenter planning-permit registry**, but it is important for the digital-infrastructure layer: electronic communications, submarine cable resilience/connectivity, sectoral cybersecurity role under NIS2, and policy events on `conetividade, espaço, centros de dados e energia`. ANACOM mirrors PNCD legal material and publishes cable/datacenter ecosystem content. Source: https://www.anacom.pt/render.jsp?contentId=1831802. **Grade A** for regulatory/publication facts.

---

## 1. Portuguese and English Query Patterns

Use Portuguese first; English finds operator/trade press but misses municipal records.

### 1.1 Core discovery

```
"centro de dados" "{concelho}" ("pedido de informação prévia" OR PIP OR "licenciamento urbanístico" OR "licença de construção")
"data center" "{concelho}" ("Câmara Municipal" OR "reunião de câmara" OR "deliberação")
"centro de dados" "{distrito}" ("consulta pública" OR "avaliação de impacte ambiental" OR AIA OR RECAPE)
"data center" Portugal ("PIN" OR "Potencial Interesse Nacional" OR AICEP)
"centro de dados" Portugal ("subestação" OR "linha" OR "MVA" OR "MW" OR "ligação à rede")
```

### 1.2 Official source scoping

```
site:diariodarepublica.pt "centro de dados" Portugal
site:portugal.gov.pt "centro de dados" ("Sines" OR "Portugal" OR "IA")
site:portugalglobal.pt "data center" Portugal
site:siaia.apambiente.pt "centro de dados" OR "data center"
site:participa.pt "centro de dados" OR "data center"
site:dgeg.gov.pt "centro de dados" OR "data center"
site:ren.pt ("data center" OR "centro de dados") ("Sines" OR "Pego" OR "Lisboa")
site:e-redes.pt "ligação à rede" "centro de dados"
site:anacom.pt "centros de dados" "cabos submarinos"
site:cm-{municipio}.pt "centro de dados"
site:{municipal-domain} "pedido de informação prévia" "data center"
```

### 1.3 Capacity/status extraction

```
"{project name}" ("MW" OR "MVA" OR "IT capacity" OR "capacidade IT" OR "potência")
"{project name}" ("fase 1" OR "fases 2 a 6" OR RECAPE OR AIA)
"{project name}" ("subestação" OR "linha 150 kV" OR "400/150 kV" OR "ponto de ligação")
"{operator}" "{facility}" ("racks" OR "salas TI" OR "m2" OR "Tier III" OR "PUE")
```

### 1.4 Status vocabulary

- Early intent: `memorando`, `MoU`, `manifestação de interesse`, `anúncio`, `proposta`.
- Planning: `PIP`, `pedido de informação prévia`, `parecer`, `deliberação de câmara`, `licenciamento urbanístico`.
- Environmental: `AIA`, `EIA`, `DIA`, `RECAPE`, `consulta pública`, `proposta de definição de âmbito (PDA)`.
- Construction: `licença de construção`, `empreitada`, `consignação`, `início da obra`, `fase`, `edifício`.
- Operations: `operacional`, `ready for service`, `inaugurado`, `entrada em operação`, `PoP`.

---

## 2. Grade-A Official Sources

### 2.1 National policy / strategic projects

- **Diário da República**: https://diariodarepublica.pt/. Search PNCD, `centro de dados`, `infraestruturas digitais`, `cloud soberana`, and decree-law/resolution numbers. Use for legal force and exact dates. **Grade A.**
- **Portugal.gov.pt**: https://portugal.gov.pt/. Government news, Council of Ministers communiqués, and FAQs. Useful for PNCD, AI strategy, Microsoft/Start Campus public statements, and policy ownership. **Grade A for government statements; B for restated company investment numbers.**
- **AICEP / Portugal Global**: https://portugalglobal.pt/. Search `data center`, `centro de dados`, `PIN`, `Sines`, `Microsoft`, `Nscale`, `Start Campus`. Use for PIN/investor-support status and strategic-investment framing. **Grade A-/B+.**
- **IAPMEI**: https://www.iapmei.pt/. Less productive for named DCs, but check for enterprise incentives/sector classifications and official economic-support records when a project SPV is known. **Grade A for records, low recall.**

### 2.2 Environmental / consultation pipeline

- **APA SIAIA**: https://siaia.apambiente.pt/. Best official repository for EIA/RECAPE PDFs. Search both `data center` and `centro de dados`; also search ancillary projects such as `subestação`, `linha`, `parque eólico`, `fotovoltaico`, `Sines`, `Pego`, `Azambuja`. **Grade A.**
- **Participa**: https://participa.pt/. Public consultations for EIA scoping and related environmental procedures. Watch for power/cooling/renewable projects built to serve DC campuses. **Grade A.**
- Model case: `Data Center Sines 4.0` in APA/SIAIA includes EIA, non-technical summary, public-consultation report, and RECAPE documents for phases. Example search-result URLs include `https://siaia.apambiente.pt/AIADOC/AIA3633/` and `https://siaia.apambiente.pt/AIADOC/RECAPE564/`. **Grade A.**

What to extract from APA/SIAIA:

- Exact proponent/SPV, parcel, industrial-zone unit, municipality, district.
- Phase scope: e.g. `Fase 1` vs `Fases 2 a 6`.
- Area, buildings, substations, generator count, cooling system, water abstraction/discharge, associated transmission line, expected operation date.
- DIA/RECAPE conditions. A positive environmental decision is not an operating status; it is a permitting milestone.

### 2.3 Municipal planning / urbanismo

Every serious enumeration run must search the municipality, not only the district. Municipal evidence often appears in PDF agendas/minutes before a searchable project page exists.

Useful municipal terms:

```
"pedido de informação prévia" OR PIP
"licenciamento urbanístico"
"licença de construção"
"obras de urbanização"
"reunião de câmara"
"ata" OR "deliberação"
"plano de pormenor" OR "unidade de execução" OR PDM
"loteamento" OR "operação urbanística"
```

Examples of municipal portals / patterns:

- Lisbon: https://www.lisboa.pt/temas/urbanismo/gestao-urbanistica/licenciamentos and Lisboa open-data urbanism dataset pages. Query `site:lisboa.pt "centro de dados"` plus `site:dados.gov.pt "Processos de Urbanismo" Lisboa`. **Grade A, but facility recall low because most DCs are in Greater Lisbon municipalities rather than Lisboa city.**
- Porto: https://portaldomunicipe.cm-porto.pt/ has `Consulta online de processos`. Query `site:cm-porto.pt "centro de dados"` and `site:portaldomunicipe.cm-porto.pt "data center"`. **Grade A.**
- Sines: https://www.sines.pt/. Query `site:sines.pt "Data Center"`, `site:sines.pt "NEST"`, `site:sines.pt "Sines 4.0"`, `site:sines.pt "Unidade de Execução"`. Sines municipal PDFs are essential for Start Campus urbanistic status. **Grade A.**
- Azambuja: https://www.cm-azambuja.pt/. Query `site:cm-azambuja.pt "data center"`, `site:cm-azambuja.pt "Alcoentre"`, `site:cm-azambuja.pt "PIP"`. Recent press indicates a Neoen/Azambuja DC planning path; verify through meeting minutes before counting. **A if municipal record, B if press only.**
- Abrantes: https://cm-abrantes.pt/. Query `site:cm-abrantes.pt "centro de dados" "Pego"` and `site:cm-abrantes.pt "pedido de informação prévia" "centro de dados"`. Press reports a second DC PIP near Pego; verify in Câmara minutes. **A if municipal record, B if local press only.**

### 2.4 Electricity / grid / energy regulators

- **REN** (transmission system operator): https://www.ren.pt/. Search `data center`, `Sines`, `Pego`, `subestação`, `linha`, `MVA`, `rentelecom`, `EllaLink`. REN pages and reports can establish transmission-linked projects and connectivity. **Grade A for REN-owned facts; B for management commentary about third-party projects.**
- **E-REDES** (distribution grid): https://www.e-redes.pt/ and open data portal https://e-redes.opendatasoft.com/pages/homepage/. Use for distribution connection processes, local grid capacity context, and open data; not a simple facility registry. **Grade A for grid data/process.**
- **DGEG**: https://www.dgeg.gov.pt/. Energy and geology directorate; check `Serviços Online`, `Energia Elétrica`, `Eficiência Energética`, `Atos`, `Editais`, and GIS (`Informação Geográfica`) for power, generation, and energy-efficiency records tied to a DC or captive renewables. **Grade A.**
- **ERSE**: https://www.erse.pt/. Energy regulator. Use for electricity-market rules, connection/regulatory context, tariffs, outage/value-of-lost-load studies, and distribution/transmission regulation. Less likely to name individual DCs. **Grade A for regulatory context.**

### 2.5 Telecom / digital-infrastructure regulator

- **ANACOM**: https://www.anacom.pt/. Search `centros de dados`, `cabos submarinos`, `conetividade`, `NIS2`, `autoridade setorial`, `infraestruturas digitais`. ANACOM should be used to frame Portugal's cable/datacenter attractiveness and regulatory responsibilities, not as a planning-permit database. **Grade A.**
- **CNCS / MyCiber**: https://www.cncs.gov.pt/ and NIS2/RJC materials. Datacenter operators can fall into essential/important digital-infrastructure obligations. Use for cybersecurity compliance context and operator self-registration duties where public. **Grade A for cybersecurity rules; low facility-discovery value.**

---

## 3. Cloud and Colo Operator Seeds

Official operator pages provide existence/location evidence but usually hide exact addresses and phase capacities. Use them as seed lists, then verify through municipal or environmental records.

### 3.1 Hyperscale cloud regions / edge

- **AWS**: no Portugal full AWS Region found on the official Regions/AZ page as of this research. Official AWS Local Zones page lists **Lisbon, Portugal** as an **announced** Local Zone, zone name `eusc-de-east-1-lis-1a`, parent region AWS European Sovereign Cloud (Germany): https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/. AWS also announced a Direct Connect location at Equinix LS1 near Lisbon in 2025: search `AWS Direct Connect Lisbon Portugal Equinix LS1`. **Grade A for AWS service-location status.**
- **Microsoft Azure**: no Portugal geography/region appears on the official Azure geography/product-by-region pages checked; nearest strategic regions are usually Spain/West Europe. However Microsoft has public investment statements tied to Start Campus/Nscale in Sines; treat those as customer/AI infrastructure commitments, not proof of an Azure Portugal region unless Microsoft region docs list one. Official regions: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/. **Grade A for region absence/presence; B for investment press unless official Microsoft/AICEP.**
- **Google Cloud**: official locations page checked does not list a Portugal cloud region. Google is relevant for submarine cable connectivity (e.g. Nuvem/Equiano routes touching Portugal/Azores) but not a Portugal GCP region unless the locations page changes. Source: https://cloud.google.com/about/locations. **Grade A.**
- **Oracle Cloud**: official public-cloud regions list has Spain Central/Madrid and EU Sovereign South/Madrid, but no Portugal public region in the table checked. Source: https://www.oracle.com/cloud/public-cloud-regions/. **Grade A.**

### 3.2 Portugal colo / carrier-neutral / telecom DC players

- **Start Campus / SINES DC**: https://www.startcampus.pt/. Flagship campus in Sines, AI-ready, marketed at up to 1.2 GW secured IT grid capacity. Verify every phase via APA/SIAIA, Sines municipal records, REN/grid records, and operator press. **A- for official operator existence; B for marketing capacity until regulatory/power record is linked.**
- **Equinix Lisbon LS1/LS2**: https://www.equinix.com/data-centers/europe-colocation/portugal-colocation/lisbon-data-centers. Equinix lists LS1 and LS2 in Lisbon/Prior Velho. LS1 also hosts AWS Direct Connect per AWS announcement. **A- for operator facility list.**
- **MEO / Altice Portugal**: https://en.meo.pt/business/solutions/cloud-datacenter/data-centers and Covilhã page https://en.meo.pt/business/solutions/cloud-datacenter/data-centers/covilha. MEO describes the largest national DC network, with Lisbon, Porto, Azores, Madeira, and Covilhã; Covilhã page gives facility size/IT-room data. **A- for operator list and facility specs.**
- **NOS / Sonaecom / Bright Pixel ecosystem**: search official NOS enterprise pages and annual reports for `data center`, `cloud`, `colocation`, `Sonaecom`. NOS is a connectivity/cloud player, but facility-level public detail is thinner than MEO/Equinix. **B unless official facility page is found.**
- **Claranet Portugal**: managed hosting/cloud/security provider; search `site:claranet.com/pt "data center"` and `site:claranet.pt "datacenter"`. May be more service/provider than facility owner. **B unless a facility page or permit is found.**
- **DE-CIX**: https://www.de-cix.net/ and Start Campus press for PoP at SINES DC. Use IX PoP announcements as operational/connectivity evidence, not construction permits. **B+.**
- **IP Telecom / Infraestruturas de Portugal**: search `site:iptelecom.pt "data center"` and `site:infraestruturasdeportugal.pt "centro de dados"`. Important for public-sector cloud/connectivity and PNCD stakeholder mapping. **B/A depending on official record.**
- Aggregator seeds only: DataCenterMap, Baxtel, PeeringDB, Datacenters.com, Cloudscene. Use to identify candidate facility names/addresses, then verify via operator/municipal records. **C to B depending on record freshness.**

---

## 4. District-by-District Enumeration Strategy

Portugal's practical search unit is **concelho/municipality**, grouped by district or autonomous region. Run national portals first, then municipal searches for the high-probability municipalities in each district.

| District / Region | Priority municipalities and why | Official query pattern |
|---|---|---|
| **Setúbal** | **Sines** is the national hyperscale anchor; also Santiago do Cacém for wind/energy supply, Setúbal/Palmela for industrial/logistics spillover. | `site:sines.pt ("data center" OR "centro de dados" OR "Sines 4.0" OR NEST)`, `site:siaia.apambiente.pt "Data Center Sines"`, `site:participa.pt "Sines" "centro de dados"`, `site:ren.pt Sines "data center"`, `site:santiagocacem.pt "centro de dados" "parque eólico"`. |
| **Lisbon / Lisboa** | Lisbon city, Loures/Prior Velho, Oeiras, Sintra, Amadora, Cascais, Vila Franca de Xira, Azambuja. Equinix LS1/LS2 in Greater Lisbon; many carrier hotels/edge facilities; Azambuja/Alcoentre emerging. | `site:lisboa.pt "centro de dados"`, `site:cm-loures.pt ("data center" OR "centro de dados" OR Prior Velho)`, `site:cm-oeiras.pt "data center"`, `site:cm-azambuja.pt ("Alcoentre" OR "data center" OR PIP)`, plus Equinix/AWS Direct Connect pages. |
| **Porto** | Porto, Maia, Matosinhos, Vila Nova de Gaia, Ermesinde/Valongo. MEO lists Porto; aggregators mention Ermesinde. | `site:cm-porto.pt "centro de dados"`, `site:portaldomunicipe.cm-porto.pt "data center"`, `site:cm-maia.pt "centro de dados"`, `site:cm-valongo.pt ("Ermesinde" "data center")`, `site:meo.pt "Porto" "Data Centers"`. |
| **Braga** | Braga, Vila Nova de Famalicão/Riba de Ave, Guimarães. REN had a Riba de Ave data-center building reference historically; northern industrial demand may support enterprise DCs. | `site:cm-braga.pt "centro de dados"`, `site:famalicao.pt ("Riba de Ave" "data center")`, `site:ren.pt "Riba de Ave" "Data Center"`, `site:cm-guimaraes.pt "centro de dados"`. |
| **Castelo Branco** | **Covilhã** is a major MEO/Altice facility; also Castelo Branco for municipal/public-sector backup facilities. | `site:cm-covilha.pt ("Data Center" OR "centro de dados")`, `site:meo.pt "Covilhã" "Data Center"`, `site:cm-castelobranco.pt "Data Center"`. |
| **Santarém** | **Abrantes/Pego** is emerging due to former power-plant/grid capacity; Santarém and Cartaxo as industrial/logistics alternatives. | `site:cm-abrantes.pt ("Pego" "centro de dados" OR "pedido de informação prévia")`, `site:participa.pt "Pego" "centro de dados"`, `site:ren.pt Pego "data center"`, `site:cm-santarem.pt "centro de dados"`. |
| **Aveiro** | Aveiro, Ílhavo, Santa Maria da Feira, Ovar: industrial/cable/fiber corridors; lower known DC density but worth annual sweep. | `site:cm-aveiro.pt "centro de dados"`, `site:cm-feira.pt "data center"`, `site:cm-ovar.pt "centro de dados"`, `site:siaia.apambiente.pt "Aveiro" "centro de dados"`. |
| **Leiria** | Leiria, Marinha Grande, Porto de Mós: industrial land and central location; likely smaller enterprise DCs. | `site:cm-leiria.pt "centro de dados"`, `site:municipio-portodemos.pt "Urbanismo Digital" "centro de dados"`, `site:siaia.apambiente.pt "Leiria" "data center"`. |
| **Coimbra** | Coimbra/Figueira da Foz: university/research and coastal industrial sites; expect smaller HPC/public-sector nodes. | `site:cm-coimbra.pt "centro de dados"`, `site:uc.pt "data center"`, `site:cm-figfoz.pt "centro de dados"`. |
| **Faro** | Algarve has solar and cable/landing potential but grid constraints; check Faro/Loulé/Portimão/Lagos. | `site:cm-faro.pt "centro de dados"`, `site:cm-loule.pt "data center"`, `site:participa.pt Algarve "centro de dados"`, `site:erse.pt Algarve "centros de dados"`. |
| **Beja / Évora / Portalegre** | Alentejo has land/renewables; Beja and Évora may appear as renewable-backed campuses, but verify grid and water. | `site:cm-beja.pt "centro de dados"`, `site:cm-evora.pt "data center"`, `site:participa.pt Alentejo "centro de dados"`, `site:dgeg.gov.pt Alentejo "centro de dados"`. |
| **Viana do Castelo / Vila Real / Bragança / Guarda / Viseu** | Lower probability for large hyperscale except hydro/renewable or municipal/public-sector facilities; run light sweeps. | `site:{municipal-domain} ("centro de dados" OR "processamento de dados" OR "cloud")`, plus DGEG/APA for energy-linked proposals. |
| **Azores / Madeira** | MEO lists Azores and Madeira DC network nodes; islands matter for resilience/subsea cables and public-sector continuity. | `site:azores.gov.pt "centro de dados"`, `site:madeira.gov.pt "centro de dados"`, `site:anacom.pt Açores "cabos submarinos"`, `site:meo.pt "Açores" "Data Centers"`, `site:meo.pt "Madeira" "Data Centers"`. |

For each district, also run:

```
"{district}" "centro de dados" "consulta pública"
"{district}" "data center" "Câmara Municipal"
"{municipality}" ("subestação" OR "linha 150 kV" OR "400 kV") "centro de dados"
```

---

## 5. Verification and Evidence Grading

### 5.1 Evidence hierarchy

1. **A — Official permitting / legal / regulatory evidence**: Diário da República, PNCD/PAPNCD, APA/SIAIA EIA/RECAPE/DIA, Participa consultation, municipal PIP/licensing/minutes, REN/E-REDES/DGEG grid/energy documents, ERSE rules, ANACOM/CNCS regulatory publications.
2. **A- — Operator official pages**: Equinix, MEO/Altice, Start Campus, AWS/Azure/GCP/OCI region pages. Strong for existence and service availability; capacity often marketing.
3. **B — Strong trade press**: DatacenterDynamics, Data Center Frontier, Capacity Media, TeleGeography, ECO/Lusa, Jornal de Negócios, SAPO TEK, IT Insight, Jornal Económico, APDC. Good for leads and event dates; re-check official evidence.
4. **C — Aggregators/market reports**: DataCenterMap, Baxtel, PeeringDB, Datacenters.com, Mordor, paid database press releases, LinkedIn posts. Useful for seeds; do not count without confirmation.

### 5.2 Status rules

- Count as **planned** only when there is a named project + named proponent + municipality + official planning/environmental/strategic-investment record.
- Count as **permitted/approved** when PIP/licensing/EIA/DIA/RECAPE or equivalent official decision exists. Record which permit type.
- Count as **under construction** only with construction license, contractor/EPC notice, municipal construction record, operator construction update, or credible site imagery.
- Count as **operational** only with operator page, customer/PoP ready-for-service announcement, official inauguration, or service availability.
- Do not count total design GW as live MW. Store `design_capacity_mw`, `secured_grid_mw`, `phase_capacity_mw`, and `live_capacity_mw` separately when possible.

### 5.3 Common pitfalls

- `Centro de dados municipal` often means a small public IT/server room. Keep but classify separately from commercial/colo/hyperscale DCs.
- Portuguese press may use `data center`, `datacenter`, and `centro de dados` interchangeably; search all spellings.
- PIN status accelerates coordination; it does **not** replace municipal, environmental, or grid permits.
- Sines-related renewable or grid projects may mention the datacenter only as an offtaker. Link them as supporting infrastructure, not a separate DC.
- Greater Lisbon facilities often sit outside Lisboa municipality; search Loures/Prior Velho, Oeiras, Sintra, Amadora, Cascais, Vila Franca de Xira, and Azambuja.
- Cloud regions are not the same as colo facilities. AWS Local Zone / Direct Connect in Lisbon proves cloud edge/connectivity, not a full AWS Portugal Region.

---

## 6. Recommended Official-First Workflow

1. **National seed sweep**: search Diário da República, Portugal.gov.pt, AICEP, ANACOM for `Plano Nacional de Centros de Dados`, `PIN`, `centro de dados`, `Sines`, `cloud soberana`, `infraestruturas digitais`.
2. **APA/SIAIA + Participa sweep**: search `data center`, `centro de dados`, `Sines`, `Pego`, `Azambuja`, `Alcoentre`, `subestação`, `parque eólico`, `linha 150 kV`, `400/150 kV`. Extract proponent, phase, MW/MVA, and dates from PDFs.
3. **Municipal sweep by district**: prioritize Setúbal/Sines, Greater Lisbon, Porto, Braga/Famalicão, Castelo Branco/Covilhã, Santarém/Abrantes. Search municipal site, minutes, agenda, urbanismo portal, and open-data portal.
4. **Power validation**: for every >10 MW claim, search REN/E-REDES/DGEG/ERSE with project name, municipality, substation, voltage, MVA, and associated renewable assets.
5. **Operator/cloud sweep**: Equinix, MEO/Altice, Start Campus, DE-CIX, AWS/Azure/GCP/OCI official locations. Use these to mark operational/service status.
6. **Trade-press lead pass**: DCD, Data Center Frontier, ECO/Lusa, SAPO TEK, Jornal Económico, IT Insight, Capacity/TeleGeography. Promote leads to the registry only after one official or operator source confirms them.
7. **Record output fields**: `{country_code: PT, district_or_region, municipality, facility_or_project_name, proponent/operator, status, design_capacity_mw, phase_capacity_mw, live_capacity_mw, grid_evidence, planning_evidence, environmental_evidence, source_urls, evidence_grade, evidence_date, notes}`.

Minimum source package for a high-confidence large Portuguese DC record:

- Municipality/PIP/licensing or APA/SIAIA/Participa record (**A**).
- Operator or AICEP/Portugal.gov source identifying proponent and project (**A-/B+**).
- REN/E-REDES/DGEG or EIA power evidence for MW/MVA (**A**).
- Trade press only as date/context support (**B**).
