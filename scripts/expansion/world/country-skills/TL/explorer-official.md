# TL Explorer Official - Timor-Leste Datacenter Enumeration via Government, Procurement, Regulator, Donor, Power, and Connectivity Sources

Date: 2026-08-12. Scope: Timor-Leste (TL), using the repo/requested 13-division frame: Aileu; Ainaro; Baucau; Bobonaro; Cova Lima; Dili; Ermera; Lautem; Liquica; Manatuto; Manufahi; Oe-Cusse Ambeno; Viqueque. Note: Timor-Leste created Atauro as a separate municipality effective 2022; keep Atauro as a Dili/outer-island search variant unless the repo division model is updated.

Reliability grades:

- **A**: primary/official source: Government of Timor-Leste, TIC TIMOR, Ministry of Justice Jornal da Republica, CNA/NPC, Timor-Leste eProcurement, ANC, ADB/World Bank/DFAT project document, EDTL, or an operator-owned page naming a physical facility/project.
- **B**: reputable trade or local/regional press with named parties, or technical industry databases used for context.
- **C**: directories, reseller pages, SEO landing pages, social-only claims, or unverified marketing. Use only as leads.

## 0. Country-Specific Baseline

- Timor-Leste has no practical national planning-permit or building-permit portal for datacenter discovery. The official backbone is **procurement, TIC TIMOR/government announcements, regulator records, donor project documents, and telecom/connectivity releases**.
- Dili is the dominant search target: national government, TIC TIMOR, Ministry of Finance data-center procurement, Timor Telecom/ANC Telecom Building at Caicoli, operator headquarters, and the Bebonuk TLSSC cable landing station are all in Dili.
- Confirmed public evidence points to **government and telecom data rooms/buildings**, not hyperscale or multi-MW commercial campuses. Default `capacity_mw: null` unless a primary source gives electrical/IT load.
- Use four language lanes: English (`data center`, `data centre`, `server`, `ICT`), Portuguese (`centro de dados`, `servidores`, `TIC`), Tetum (`sentru dadus`, `dadus`, `rede fibra optika`, `sistema informasaun`), and Indonesian (`pusat data`, `server`, `jaringan fiber optik`).

## 1. Grade A Official Sources

### 1.1 Government and TIC TIMOR

- Government portal: https://timor-leste.gov.tl/?lang=en
- Administrative divisions reference: https://timor-leste.gov.tl/?lang=en&p=91
- Timor Digital 2032 Council of Ministers approval: https://timor-leste.gov.tl/?lang=en&p=31624&print=1
- TLSSC cable installation at Bebonuk, Dili: https://timor-leste.gov.tl/?lang=en&p=38073&print=1
- Government private fiber network contract to link 12 municipal administrations to the Prime Minister's Office Data Center: https://timor-leste.gov.tl/?lang=en&p=19673&print=1
- TIC TIMOR: https://www.tic.gov.tl/
- TIC TIMOR Data Center role page: https://www.tic.gov.tl/en/tic/sentrudadus/
- TIC TIMOR/ADB coordination meeting, Caicoli, Dili, explicitly describing the Data Center Directorate and Electronic Government Data Center: https://www.tic.gov.tl/en/tic/shownotisia/115/

Official government query templates. When a search engine does not preserve Boolean grouping, run each `OR` alternative as a separate query.

```text
site:timor-leste.gov.tl "data center" OR "data centre" OR "Data Center"
site:timor-leste.gov.tl "centro de dados" OR "sentru dadus" OR "TIC"
site:tic.gov.tl "Data Center" OR "Datacenter" OR "sentru dadus"
site:tic.gov.tl "ADB" "Data Center"
site:timor-leste.gov.tl "Prime Minister's Office Data Center"
site:timor-leste.gov.tl "fiber optic" "municipal" "Data Center"
```

### 1.2 Gazette and Legal Records

- Ministry of Justice Jornal da Republica official page: https://www.mj.gov.tl/jornal/
- Government publications mirror: https://timor-leste.gov.tl/?cat=32&lang=en
- Use Jornal da Republica for decree-laws and resolutions affecting TIC TIMOR, ANC, public procurement, environmental licensing, and RAEOA/ZEESM procurement. The older `jornal.gov.tl` domain appears in archives but the verified official route is now the Ministry of Justice page above.
- Useful legal anchors to search: Decree-Law No. 29/2017 (TIC TIMOR public institute), Decree-Law No. 46/2023 (government organic placement of TIC TIMOR), Decree-Law No. 15/2012 (telecommunications), Decree-Law No. 31/2024 (ANC statute), Decree-Law No. 5/2011 and Decree-Law No. 39/2022 (environmental licensing).

Gazette query templates. Run spelling/accent variants separately where needed.

```text
site:mj.gov.tl/jornal "TIC TIMOR" "Data Center"
site:mj.gov.tl/jornal "Autoridade Nacional de Comunicações"
site:mj.gov.tl/jornal "Decreto-Lei n.o 31/2024"
site:mj.gov.tl/jornal "licenciamento ambiental" "telecomunicações"
site:timor-leste.gov.tl/?cat=32 "Jornal da República" "TIC"
```

### 1.3 Procurement Backbone

- CNA/NPC portal: https://www.cna.gov.tl/
- CNA Ministry of Finance DC upgrade post-qualification, TENDER/13/MOF-2024: https://www.cna.gov.tl/pt/2024/09/02/postqualification-for-the-upgrade-of-equipment-of-/
- Timor-Leste eProcurement portal: https://www.eprocurement.gov.tl/
- eProcurement record 1219650, `Fornesimentu ekipamentu ICT ba Data Centre MdF`, Ministry of Finance, published 2023-06-21, awarded to VISIMITRA UNIPESSOAL LDA for USD 884,375: https://www.eprocurement.gov.tl/publishedDocuments/show/1219650
- eProcurement record 979880, `Commit of Supply Hard Disk and Ram Memory for Upgrade data center Ministry of Finance`, published 2021-11-17, awarded to BANNILA, UNIPESSOAL LDA for USD 191,780: https://www.eprocurement.gov.tl/publishedDocuments/show/979880
- eProcurement record 1133403, `Commitment for Data Center Recovery for Ministry of Finance`, reference ICB/063/MOF-2022: https://www.eprocurement.gov.tl/publishedDocuments/show/1133403

Procurement extraction fields: tender/procurement ID; buyer; department; title and language; award status; vendor; award amount; location; whether scope is facility, IT equipment, power/cooling, disaster recovery, network, or managed service.

Procurement query templates. Prefer exact strings first, then broader ICT/fiber sweeps.

```text
site:cna.gov.tl "data center" OR "data centre" OR "Data Center"
site:cna.gov.tl "centro de dados" OR "Data Centre" OR "sentru dadus"
site:eprocurement.gov.tl "Data Centre" OR "data center"
site:eprocurement.gov.tl "MdF" "Data Centre"
site:eprocurement.gov.tl "Ministry of Finance" "data center"
site:eprocurement.gov.tl "disaster recovery" OR "Data Center Recovery"
site:eprocurement.gov.tl "{division}" "ICT" OR "servidor" OR "fibra"
```

### 1.4 Regulator: ANC

- ANC home: https://anc.tl/
- ANC about/contact pages: https://anc.tl/about-us/index.html and https://anc.tl/contact-us/index.html
- ANC address: Ground floor, Telecom Building, Avenida Xavier do Amaral No. 8, Caicoli, Dili.
- ANC technical adviser/TOR for national IXP deployment, including route server, IXP Manager, DNS, virtualization and infrastructure setup: https://anc.tl/media/2025/08/TOR-for-ANC-Technical-Adviser.pdf
- ANC vacancy page linking the TOR: https://anc.tl/advertisement-vacancy-for-technical-adviser/index.html

Regulator query templates. Keep `ANC Timor-Leste` in broader searches to avoid ANATEL/ANACOM results.

```text
site:anc.tl "IXP" OR "Internet Exchange"
site:anc.tl "data center" OR "data centre" OR "datacenter"
site:anc.tl "licence" OR "licensa" OR "licença"
site:anc.tl "Starlink"
site:anc.tl "Vanov Technology"
"Autoridade Nacional de Comunicações" "Timor-Leste" "Data Center"
```

### 1.5 Donor and Development-Bank Sources

- ADB e-Government Development and Infrastructure Project 55338-001: https://www.adb.org/projects/55338-001/main
- ADB PDS mirror confirms status `Proposed`, USD 50 million OCR loan, executing agency `Council for Administration of the Infrastructure Fund`, and outputs including `National data center and disaster recovery facilities established`: https://ewsdata.rightsindevelopment.org/files/documents/01/ADB-55338-001.pdf
- ADB Power Distribution Modernization Project 49177-002: https://www.adb.org/projects/49177-002/main
- ADB project summary/approval context for 140,000 smart meters, distribution automation, and Dili distribution control/warehouse components: https://events.development.asia/energyforall/power-distribution-modernization-project-timor-leste-approved
- World Bank July 28, 2026 energy investment: 73.7 MWac solar PV and 80.2 MWh BESS, useful power-readiness context, not a DC record: https://www.worldbank.org/en/news/press-release/2026/07/28/development-partners-power-timor-leste-s-energy-future-with-landmark-investment
- UNDP Timor-Leste programme pages can support digital-government context but must not be used as facility evidence without a named data-center site: https://www.undp.org/timor-leste

Donor query templates. Search the project number separately because ADB pages may not include all facility terms in snippets.

```text
site:adb.org "Timor-Leste" "data center" OR "data centre"
site:adb.org "55338-001" OR "e-Government Development and Infrastructure Project"
site:adb.org "Timor-Leste" "disaster recovery"
site:adb.org "Timor-Leste" "ICT" "procurement"
site:worldbank.org "Timor-Leste" "digital" OR "ICT" OR "data"
site:ungm.org "Timor-Leste" "data center" OR "ICT"
```

### 1.6 Power and Grid

- EDTL official production/renewable-energy page: https://edtl-ep.tl/department/en/2979994931093398343150/
- Wartsila 2025 O&M renewal for Hera and Betano, combined 255 MW supporting the national grid: https://www.wartsila.com/media/news/26-11-2025-wartsila-s-operation-and-maintenance-capabilities-provide-critical-support-to-timor-leste-s-national-power-supply-3688519
- ADB Power Distribution Modernization Project 49177-002: https://www.adb.org/projects/49177-002/main
- World Bank 2026 solar/BESS investment: https://www.worldbank.org/en/news/press-release/2026/07/28/development-partners-power-timor-leste-s-energy-future-with-landmark-investment

Use power sources as siting context only. They do not prove a datacenter unless tied to an ICT building, tender, interconnection, or operator record.

Power query templates. Treat hits as siting context until tied to an ICT facility.

```text
"EDTL" "Data Center" OR "data centre"
"EDTL" "substation" "Dili" "ICT"
"Hera" "Dili" "data center"
"Betano" "data center" OR "ICT"
"Timor-Leste" "MVA" "Data Center"
```

### 1.7 Connectivity and Cable-Landing Sources

- Government TLSSC installation at Bebonuk, Dili: https://timor-leste.gov.tl/?lang=en&p=38073&print=1
- Submarine Networks TLSSC technical record: https://www.submarinenetworks.com/en/systems/asia-australia/png-national/tlssc
- DCD June 2024 cable landing report: https://www.datacenterdynamics.com/en/news/timor-leste-south-submarine-cable-system-lands-in-dili/
- DCD August 2026 commercial launch report: https://www.datacenterdynamics.com/en/news/timor-leste-launches-commercial-operations-of-first-international-subsea-cable/
- Tatoli landing-station report: https://en.tatoli.tl/2024/06/24/timor-leste-begins-installation-of-southern-submarine-cable/19/

Connectivity query templates. Use locality terms (`Bebonuk`, `Dili`) as well as cable names.

```text
"TLSSC" "data center" OR "data centre"
"Bebonuk" "Data Center" OR "Cable Landing Station"
"Dili" "cable landing station" "data"
"Timor-Leste South Submarine Cable" "DXN" "landing station"
"North-West Cable System" "Timor-Leste" "Dili"
```

### 1.8 Hyperscale Cloud Absence Check

Use only official provider pages for cloud-region absence:

| Provider | Official page | Timor-Leste handling |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No TL region found; nearest practical Asia-Pacific regions include Singapore, Jakarta, Sydney. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No TL public region found. |
| Google Cloud | https://cloud.google.com/about/locations | No TL region found. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No TL public region found. |

Do not treat a reseller selling AWS/Azure/GCP/OCI services in Timor-Leste as a local hyperscale region or local datacenter.

## 2. Per-Division Official Search Strategy

Run the universal sweep for every division:

```text
site:timor-leste.gov.tl "{division}" "data center" OR "centro de dados" OR "sentru dadus"
site:tic.gov.tl "{division}" "data" OR "TIC" OR "fibra"
site:cna.gov.tl "{division}" "Data Center" OR "ICT" OR "fibra"
site:eprocurement.gov.tl "{division}" "Data Center" OR "ICT" OR "servidor"
site:anc.tl "{division}" "IXP" OR "licence" OR "internet"
site:adb.org "Timor-Leste" "{division}" "ICT" OR "digital"
```

| Division | Main place variants | Yield / strategy |
|---|---|---|
| Aileu | Aileu; Laulara; Remexio; Liquidoe | Low. Search for municipal fiber, EDTL substation routing, TIC awareness/municipal-network work, and disaster-recovery site mentions. Do not record a DC without tender/operator evidence. |
| Ainaro | Ainaro; Maubisse; Hato-Udo; Hatu-Udo | Low. Search municipal administration fiber, south-coast network resilience, and public-service ICT tenders. |
| Baucau | Baucau; Baukau; Venilale; Vemasse; Laga | Medium. Second city and plausible DR candidate. Prioritize ADB 55338 follow-up docs, CNA/eProcurement, EDTL reliability works, government cloud/backup references, and operator backbone nodes. |
| Bobonaro | Bobonaro; Maliana; Balibo; Batugade | Low/medium because of border and transit routes. Search border digitalization, customs/immigration ICT, municipal fiber, and operator backbone. |
| Cova Lima | Cova Lima; Covalima; Suai; Zumalai; Tilomar | Low/medium. Search south-coast connectivity, Suai public administration, border/customs ICT, and EDTL/fiber tenders. |
| Dili | Dili; Dili Municipality; Caicoli; Bebonuk; Comoro; Bidau; Taibesi; Vila Verde; Fatuhada; Cristo Rei; Metinaro | High. Search TIC TIMOR, MoF, Prime Minister's Office Data Center, Telkomcel DC, Timor Telecom/ANC Telecom Building, TLSSC Bebonuk landing station, IXP, operator HQs, and all procurement records. |
| Ermera | Ermera; Gleno; Atsabe; Letefoho; Railaco | Low. Search municipal fiber and public-administration ICT only. Beware agricultural/coffee "data" false positives. |
| Lautem | Lautem; Lospalos; Los Palos; Com; Tutuala; Iliomar | Low. Search municipal fiber, eastern backbone extension, and any future cable/landing speculation; no current DC evidence found. |
| Liquica | Liquica; Likisa; Maubara; Bazartete | Low/medium due west-of-Dili corridor. Search Dili spillover, fiber route, EDTL substations, and coastal/industrial site terms. |
| Manatuto | Manatuto; Laclo; Laleia; Soibada; Natarbora | Low/medium. World Bank 2026 energy project makes this a power-readiness watch area, but not a DC lead without ICT/facility evidence. |
| Manufahi | Manufahi; Same; Betano; Alas; Fatuberliu; Turiscai | Low/medium. Betano power station is major grid context. Search for backup/DR, power-adjacent ICT, and south-coast resilience. |
| Oe-Cusse Ambeno | Oe-Cusse; Oecusse; Oekusi; Oecussi-Ambeno; RAEOA; ZEESM; Pante Macassar | Medium because special-region procurement may sit outside generic ministry patterns. Search RAEOA/ZEESM procurement, Jornal da Republica, border/digital services, local power plant, and operator backbone. |
| Viqueque | Viqueque; Vikeke; Ossu; Uatolari; Uatucarbau; Lacluta | Low. Search municipal fiber, government service digitization, and operator backbone. |

## 3. Known Official Facility/Project Seeds

| Seed | Division | Status | Grade | Evidence and handling |
|---|---|---:|---:|---|
| TIC TIMOR / Electronic Government Data Center | Dili, Caicoli / MTC area | Operational government function | A | TIC TIMOR Data Center role page and 2024 ADB coordination article name a Data Center Directorate and Electronic Government Data Center managed by TIC TIMOR. Treat as government DC function; physical specs unknown. |
| Prime Minister's Office Data Center | Dili | Operational anchor | A | 2018 government release says 12 municipal administrations would connect through EDTL substations into the Prime Minister's Office Data Center. |
| Ministry of Finance Data Center | Dili | Existing / repeatedly upgraded | A | CNA TENDER/13/MOF-2024 plus eProcurement records 1219650, 979880, and 1133403. Extract vendor/award amounts per record; physical room and MW not disclosed. |
| National Data Center and disaster recovery facilities | Nation-wide, likely Dili plus DR site TBD | Proposed | A | ADB 55338-001 PDS says status Proposed and lists this as an output. Do not mark under construction until ADB RRP/procurement or government release confirms. |
| TL-IXP | Dili likely | Deployment / interconnection anchor | A | ANC TOR covers IXP infrastructure components. It is not a colo facility by itself; use as a network anchor. |
| TLSSC Bebonuk Cable Landing Station | Dili, Bebonuk | Operational connectivity anchor | A for government release; B for trade technical detail | Government says landing at Bebonuk, Dili, 607 km and 27 Tbps. Use as site-selection context, not as a DC unless colocation/service evidence appears. |
| Telkomcel Data Center Building | Dili | Operational operator DC | A in industry file | Operator/parent official page confirms first Telkomcel Data Center Building in Timor-Leste; include in official workflow as cross-source target. |

## 4. Reliability Rules and Pitfalls

- Grade A records still need status honesty: an ADB project output can be **A/proposed**, not operational.
- Use Grade B trade sources to identify leads and dates, then cross-check against official/procurement/operator pages.
- Keep TLSSC capacity separate from DC capacity. `27 Tbps` is cable capacity, not datacenter IT load.
- Telecom offices and regulator addresses are not automatically datacenters. Record a facility only when the page says data center/data centre/datacenter, server room, DR facility, IXP infrastructure site, or equivalent.
- Starlink/VSAT/mobile towers are connectivity context only.
- Avoid regulator confusion: Timor-Leste is ANC, not Brazil ANATEL or Portugal ANACOM.
- Avoid operator confusion: Timor Telecom, Telemor/Viettel Timor, and Telkomcel/Telin-Telkom Indonesia are separate.
- Treat Atal-style "Tier III Dili" reseller pages as C until a Dili facility address and operator evidence are found.
- For capacity, use disclosed proxies: award amount, project budget, Tier target, rack/sqm count, generator rating, or phase. Leave MW null when absent.
