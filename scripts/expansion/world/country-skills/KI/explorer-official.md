# KI Explorer Official - Kiribati Datacenter Enumeration via Government, Regulatory, Utility, Cable, Cloud, and Official Operator Sources

Date: 2026-08-12. Scope: Kiribati (KI). Repo divisions (world-manifest.jsonl, `subnational_type: geographical unit`): **Gilbert Islands**, **Line Islands**, **Phoenix Islands**.

Reliability grades: **A** = official/primary source (government, regulator, utility, operator official page, company filing, official cloud-region page, donor project document, PeeringDB for interconnection facts); **B** = strong secondary or trade source with named operator/site/status; **C** = weak directory, market report, social post, or promotional article used only as a lead; **U** = unverified / rumor. Rule: an entry's grade covers only the fact actually supported by that source; a single project may have A-grade existence evidence and B/C-grade capacity or timeline evidence.

This is the final reviewed methodology layer. Source URLs listed as evidence were live-checked during review where feasible; blocked or rate-limited sources are explicitly labelled as manual-check leads rather than facility evidence.

---

## 0. Kiribati-specific structural facts

- Kiribati is a **unitary republic of 32 atolls plus Banaba, grouped into three island groups** that map directly onto the repo divisions: the Gilbert Islands (capital atoll South Tarawa; the population, government, and connectivity centre), the Line Islands (Kiritimati/Christmas Island is the division's hub; Teraina and Tabuaeran are low-density), and the Phoenix Islands (Kanton/Abariringa is the only settlement; most of the division is the Phoenix Islands Protected Area). Official languages: **English and Gilbertese (Kiribati / taetae ni Kiribati)**; government, regulator, telecom, and donor material is normally published in English.
- Kiribati has **no public national datacenter register** and no searchable national planning-permit or building-consent database for datacenter projects. Enumeration must join MICT (ICT ministry / Digital Transformation Office), MFED (executing agency for cable and digital projects), BNL (state-cable/infrastructure company), World Bank / ADB / JICA project documents, Vodafone Kiribati and Ocean Link (telecom operators), PUB (electricity), cloud-region pages, and trade press. Expect **low direct yields** from official channels; most official sources are project/policy documents rather than facility registries.
- **Legal/regulatory basis (verified or flagged):**
  - Communications Act 2013 / 2017 amendment - MICT publishes an "Amendment to Communications Act 2017" document; MICT and CCK pages identify CCK as the regulator. Re-check the current consolidated Act text on kiribati.gov.ki/MICT/CCK before legal interpretation.
  - **Data Protection Act 2025** - MICT lists the Act PDF on its publications page and also keeps the earlier Data Protection Bill page/PDF. The Bill page says first reading occurred on 2025-04-01; the Act is now the primary citation for data-protection obligations. The Act strengthens the sovereign-hosting argument behind the planned domestic/containerized data center and government cloud procurement.
  - Older/adjacent instruments: Broadcasting Publication Authority Act (revised 1979, listed on MICT site); Telecom Kiribati Ltd (Special Provisions) Act 1988 (historical state-telco statute, WIPO Lex).
- **Regulator:** telecommunications licensing is handled by the **Communications Commission of Kiribati (CCK)**, formerly the Telecommunications Authority of Kiribati. MICT's SOE page says CCK was established under the Communications Act 2013 and regulates the telecommunications industry; CCK's own About page describes it as the national regulator, and its service menu includes individual/class licences, radiocommunication, numbering, type approval, and `.ki` domain registration. MICT remains the policy ministry and parent oversight channel.
- **Connectivity anchors (as of 2026-08):**
  - **East Micronesia Cable System (EMCS)**: 2,250 km cable linking Tarawa (Kiribati) - Nauru - Kosrae (FSM) - Pohnpei (FSM), onward to Guam. BNL reported the Tarawa landing on 2025-07-25; NEC announced construction completion and handover on 2026-05-15. Re-check current RFS/retail service status before marking it live.
  - **Southern Cross NEXT (SX NEXT) Kiritimati spur**: dedicated 377 km one-fibre-pair branch to **Tabwakea, Kiritimati (Line Islands)**, in service since July 2022 as part of the SX NEXT system (Sydney-Auckland-LA). Landing station operated by **BwebwerikiNet Limited (BNL)**; the station now serves both Vodafone and Ocean Link mobile services on Kiritimati.
  - **South Tarawa fibre backbone / FTTH** (World Bank-funded; BNL to operate the passive network) and **satellite access** (Kacific, Starlink; Lynk sat-to-mobile paired with Vodafone) remain the domestic access context. Cables are **interconnection evidence, not datacenter evidence**.
- **Power is a gating constraint, not facility proof.** South Tarawa's grid is diesel-based and run by the state-owned **Public Utilities Board (PUB)**; the South Tarawa Renewable Energy Project (STREP, ADB/World Bank/CIF) is adding 5 MW solar PV + 13 MWh BESS at Bonriki - the largest renewable installation in Kiribati's history but tiny by datacenter standards. Outer islands run small village grids. There is **no commercial-scale firm power** for a large datacenter anywhere in Kiribati as of 2026-08.
- **Known physical and procurement anchors as of 2026-08:** (1) **planned domestic/containerized government data center + government cloud equipment** under the World Bank-financed **Kiribati Digital Government Project (P176108)**. The World Bank procurement plan lists Phase 2, `KI-MICTTD-470992-GO-RFQ`, "Containerized Data Center and Government Cloud Equipment Phase 2", as `Pending Implementation` with a US$900,000 estimate in the 2026-03-13 revised plan; tender mirrors show publication in March 2026 and a 2026-03-31 submission deadline. (2) **EMCS cable landing station** for Tarawa/South Tarawa, with the landing reported by BNL on 2025-07-25 and construction completion announced by NEC on 2026-05-15. (3) **SX NEXT Tabwakea cable landing station** on Kiritimati. (4) Telco core/network sites of **Vodafone Kiribati (ATHKL)** and **Ocean Link**. No source verified an operational commercial colocation facility or hyperscaler cloud region in Kiribati.
- **Do not merge asset classes.** Planned government cloud/DC procurement, existing ministry/server-room infrastructure, cable landing stations, telco exchanges/server rooms, satellite gateways, planned proposals, and absent cloud regions are separate records.
- **False-positive trap:** Australian **Christmas Island** (Indian Ocean) is NOT Kiribati; Google's reported AI-datacenter plan (Reuters/Australian press, late 2025) concerns the Australian territory. Kiritimati (Kiribati's Christmas Island) must never inherit Australian Christmas Island coverage.

Key verified anchor URLs:

- MICT (Ministry of Information, Communications and Transport): https://www.mict.gov.ki/ ; About: https://mict.gov.ki/aboutus ; News page: https://mict.gov.ki/news-page ; KDGP page: https://www.mict.gov.ki/kdgp
- MICT publications page (Data Protection Act 2025, Digital Government Act 2023, Communications amendment): https://www.mict.gov.ki/publications ; Data Protection Bill page: https://www.mict.gov.ki/publications/dpb ; Bill PDF: https://www.mict.gov.ki/sites/default/files/publications/Data%20Protection%20Bill%202025.pdf
- CCK (Communications Commission of Kiribati): https://cck.ki/ ; About: https://cck.ki/about-us ; Individual Licence: https://cck.ki/services/communications-network-services/individual-license ; MICT SOE page: https://www.mict.gov.ki/soess
- MICT example procurement notice (REOI): https://www.mict.gov.ki/node/123
- Government of Kiribati ministries: https://www.president.gov.ki/government-of-kiribati/ministries.html ; legislation portal manual-check lead: https://kiribati.gov.ki/my-government/acts
- BNL (BwebwerikiNet Limited) projects page: https://www.bnl.com.ki/projects ; EMCS landing blog: https://www.bnl.com.ki/blog/east-micronesia-cable-lands-in-first-pacific-location-of-kiribati
- EMCS official project site: https://www.eastmicronesiacable.com/ ; The Project: https://www.eastmicronesiacable.com/the-project ; News: https://www.eastmicronesiacable.com/news
- NEC EMCS construction completion (2026-05-15): https://www.nec.com/en/press/202605/global_20260515_02.html
- World Bank press release, Kiribati Digital Government Project approval (2022-05-25): https://www.worldbank.org/en/news/press-release/2022/05/25/boost-for-digital-services-and-sanitation-in-kiribati
- World Bank procurement plan P176108 (2026-03-13 revised plan): https://documents1.worldbank.org/curated/en/099031326045033591/pdf/P176108-c7747b0b-6787-4232-acf4-2a39d7d284a8.pdf
- Containerized DC / gov cloud tender mirrors (C-grade lead only after World Bank plan): https://www.developmentaid.org/tenders/view/1622456/kiribati-digital-government-project-containerized-data-center-and-government-cloud-equipment-phase-2 ; https://www.kiribatitenders.com/tender/containerized-data-center-and-government-cloud-equipment-phase-2-83846bd.php
- JICA/Yachiyo survey (Feb 2026) - Kiribati section covers CCK/MICT/BNL/PUB, domestic data-center need, planned small container-type data-center design, power constraints, and Google cache/IXP considerations: https://openjicareport.jica.go.jp/pdf/1000057177.pdf ; metadata page: https://openjicareport.jica.go.jp/007/007/007_200_1000057177.html
- UNCTAD Kiribati Rapid eTrade Readiness Assessment (2019): https://unctad.org/system/files/official-document/dtlstict2019d15_en.pdf
- PUB (Public Utilities Board): https://pub.com.ki/ ; STREP: https://pub.com.ki/south-tarawa-renewable-energy-project-strep/
- ADB STREP Project Administration Manual: https://www.adb.org/sites/default/files/project-documents/49450/49450-021-pam-en.pdf
- MLPID (Ministry of Line and Phoenix Islands Development): https://www.mlpid.gov.ki/ (incl. ICT Unit, Energy Planning Division, Kiribati Kiritimati Infrastructure Project)
- Vodafone Kiribati: https://vodafone.com.ki/ ; ATH group structure: https://www.ath.com.fj/our-story/group-structure-2/
- Ocean Link GSMA membership: https://www.gsma.com/get-involved/gsma-membership/gsma_orgs/ocean-link-ltd/
- DCD, EMCS lands at Kiribati (2025-07-28): https://www.datacenterdynamics.com/en/news/east-micronesia-cable-system-lands-at-kiribati/

---

## 1. Evidence and grading rules

Minimum positive evidence:

1. **Government datacenter / sovereign hosting:** official ministry/government page or donor project document (World Bank PAD/procurement plan, JICA survey, MICT notice) naming the facility and its function. For Kiribati, the reviewed evidence supports a **planned/procurement-stage** domestic/containerized government data center, not an operational national data center.
2. **Procurement-stage datacenter/cloud:** official WB/MFED/MICT notice or World Bank procurement plan (notice number + bid reference), e.g. `KI-MICTTD-470992-GO-RFQ`. Status verbs are mandatory: `pending implementation`, `RFQ published`, `closed`, `awarded`, `delivered`, `commissioned`.
3. **Cable landing station:** operator/government page (BNL, EMCS project site, NEC release, Submarine Networks/GeoCables for geography) with named site (Nanikai, Tabwakea). Record as interconnection evidence, not a datacenter, unless a co-located datacenter is separately verified.
4. **Telco core/network facility:** operator page or TeleGeography/LogCluster reference naming a site; record as `telco/server-room lead` unless named as colocation.
5. **Hyperscaler cloud:** official cloud-region pages only. In Kiribati these verify **absence** of local AWS/Azure/GCP/OCI regions.

Grade guidance:

- **A:** MICT/DTO, CCK, MFED, BNL, MLPID, PUB, MTCIC/IPD, kiribati.gov.ki/president.gov.ki official pages and notices, World Bank project documents and procurement notices, ADB project documents, JICA report (for the Kiribati-specific statements quoted), NEC press release, official cloud-region pages, EMCS official site, Vodafone Kiribati and Ocean Link official pages, PeeringDB (for IX/network facts).
- **B:** Data Center Dynamics, Submarine Networks, GeoCables, TeleGeography (via press), UNCTAD, commsupdate, Islands Business, content-technology.com, ZDNET, sapt.news (for the April 2025 parliamentary reading), reputable local media quoting officials.
- **C:** DevelopmentAid/GlobalTenders aggregator listings (lead to the A-grade primary notice), DataCenterMap, Cloudscene, market reports (BuddeCom, Arizton, Mordor), social posts, promotional/advertorial pages.
- **U:** anything not confirmable in a second independent source, or where the live page could not be opened.

Status mapping:

- `operational/in service`: SX NEXT Kiritimati spur (since Jul 2022); EMCS landing station built, construction completed May 2026, live RFS/service handover should still be re-checked before marking retail services live.
- `procurement/planned`: domestic/containerized government data center + government cloud (KDGP Phase 2 listed as pending implementation in the 2026-03-13 World Bank procurement plan), South Tarawa fibre backbone/FTTH, Kiritimati spur retail rollout, possible Tarawa-Kiritimati domestic submarine-cable concept from JICA/BNL discussions.
- `lead only`: telco exchange/server room, bank/government server room, satellite gateway, fibre route, cloud SaaS availability without facility evidence.

---

## 2. Planning, construction, and land sources

Kiribati has no public datacenter planning register. Use these official sources for authority, process, and site context; expect low direct project yield.

- **MICT** (https://www.mict.gov.ki/): ICT ministry; publishes news, REOIs/tenders, policies (National ICT Policy 2019, Digital Government Master Plan 2021), the Data Protection Act 2025, and project pages (KDGP). Grade A for process and policy; the primary hunting ground for government-IT procurement.
- **MFED (Ministry of Finance, Economics and Development)**: https://www.mfed.gov.ki/ ; procurement, budget, and executing-agency context for WB/donor projects. The site was live during review; use it as a policy/procurement context source, but use World Bank STEP/procurement-plan records for WB contract status.
- **World Bank procurement sources:** World Bank documents/procurement plan for P176108 is the best primary source found during review: https://documents1.worldbank.org/curated/en/099031326045033591/pdf/P176108-c7747b0b-6787-4232-acf4-2a39d7d284a8.pdf. Search World Bank procurement notices and STEP by `P176108`, `KI-MICTTD-470992-GO-RFQ`, and `Containerized Data Center and Government Cloud Equipment Phase 2`; tender mirrors are leads only.
- **MLPID (Ministry of Line and Phoenix Islands Development)** (https://www.mlpid.gov.ki/): official division-level source for Line and Phoenix Islands; has ICT Unit, Energy Planning Division/Power Unit, and the Kiribati Kiritimati Infrastructure Project (KKIP). Grade A for Line/Phoenix island infrastructure and investment framing ("world-class investment hub").
- **Land/planning context**: Ministry of Environment, Lands and Agricultural Development (MELAD) for land administration; island councils (Tarawa Urban Council, Betio Town Council) for local building/consent notices; donor project documents (ADB PAM, WB procurement/PAD documents, JICA) carry the most reliable site-level detail. Treat council/Facebook pages as manual-check leads unless loaded and archived.
- **MTCIC / Invest in Kiribati** (http://mtcic.gov.ki/ ; https://mtcic.gov.ki/investment-promotion-office/ ; https://www.investinkiribati.mtcic.gov.ki/): foreign-investment registration (Foreign Investment Certificate) and FDI framework - the correct channel if a private datacenter proposal ever appears.

Planning/land query templates:

```text
site:mict.gov.ki ("data center" OR "data centre" OR datacenter OR "server" OR "cloud" OR REOI OR RFQ)
site:mict.gov.ki ("containerized" OR "containerised" OR "government cloud" OR "Digital Government")
site:mlpid.gov.ki ("data" OR "ICT" OR "internet" OR "cable" OR "Kiritimati" OR "investment")
site:mlpid.gov.ki ("building" OR "construction" OR "land" OR "lease") ("Kiritimati" OR "Tabwakea" OR "Kanton")
site:melad.gov.ki ("lease" OR "land" OR "crown land") ("Tarawa" OR "Kiritimati" OR "Betio")
"Kiribati" ("land lease" OR "building permit" OR "construction") ("data center" OR "cloud" OR "cable landing")
"Tarawa Urban Council" OR "Betio Town Council" ("building" OR "consent" OR "development application")
"Nanikai" OR "Tabwakea" ("cable landing station" OR "land" OR "lease" OR "site")
```

---

## 3. Regulator, policy, and digital-government sources

- **MICT / Digital Transformation Office (DTO)**: https://www.mict.gov.ki/ ; DTO drives government digital transformation; ICT Policy and Development Division coordinates ICT policy/projects and cyber-security. MICT is the policy ministry and parent oversight channel; do not use it as a substitute for CCK licence evidence.
- **Communications Commission of Kiribati (CCK)**: https://cck.ki/ ; https://cck.ki/about-us ; https://cck.ki/services/communications-network-services/individual-license. CCK is the telecom regulator under the Communications Act 2013; it handles communications licences, spectrum, type approval, numbering, and `.ki`. Use CCK first for operator/licensing checks.
- **Data Protection Act 2025**: https://www.mict.gov.ki/publications ; Bill page: https://www.mict.gov.ki/publications/dpb ; Bill PDF: https://www.mict.gov.ki/sites/default/files/publications/Data%20Protection%20Bill%202025.pdf. Relevant as a sovereign-hosting demand driver and for any commercial hosting operator's compliance obligations. Re-check commencement/regulations before legal conclusions.
- **National ICT Policy 2019** (Dig Watch summary: https://dig.watch/resource/the-kiribati-national-ict-policy-2019) and **Digital Government Master Plan (2021)** (referenced by WB P176108): policy backbones; not facility records.
- **UNCTAD Rapid eTrade Readiness Assessment (2019)**: https://unctad.org/system/files/official-document/dtlstict2019d15_en.pdf - ICT market structure, regulator amendments, cable projects; good B/A-grade background.
- **World Bank Kiribati Digital Government Project (P176108)**: press release https://www.worldbank.org/en/news/press-release/2022/05/25/boost-for-digital-services-and-sanitation-in-kiribati ; MICT project page https://www.mict.gov.ki/kdgp ("Location: Tarawa, Kiribati"); procurement plan https://documents1.worldbank.org/curated/en/099031326045033591/pdf/P176108-c7747b0b-6787-4232-acf4-2a39d7d284a8.pdf. The plan lists the original C2.2 supply/installation of containerized data center and government cloud equipment and the 2026 Phase 2 RFQ (`KI-MICTTD-470992-GO-RFQ`) as `Pending Implementation`.
- **Pacific Regional Connectivity Program Phase 4 - KI Connectivity Project** (WB/IDA, regional program with FSM and Nauru): financing context for Kiribati connectivity work. Use the World Bank project record as a lead (https://documents.worldbank.org/en/publication/documents-reports/documentdetail/822111494852547471) and prefer live EMCS/BNL/NEC pages for current cable status.
- **JICA/Yachiyo survey (Feb 2026)**: "Data collection survey for improving digital connectivity and cybersecurity in the Pacific island countries" - Kiribati section documents CCK/MICT/DTO/BNL/PUB roles, government recognition that a domestic data center is needed, the planned small container-type design, South Tarawa power constraints, Google cache/IXP considerations, and a Tarawa-Kiritimati domestic-cable concept. Do **not** cite the report's Samoa national-data-center dysfunction caption as Kiribati evidence. PDF: https://openjicareport.jica.go.jp/pdf/1000057177.pdf

Regulator/policy query templates:

```text
site:mict.gov.ki ("Telecommunications Act" OR "Communications Act" OR "licence" OR "license" OR "regulation")
site:cck.ki ("Individual License" OR "Class License" OR "Vodafone" OR "Ocean Link" OR Starlink)
site:cck.ki ("frequency" OR spectrum OR "type approval" OR numbering OR ".ki")
site:mict.gov.ki ("Data Protection Act" OR "data protection" OR "privacy")
site:mict.gov.ki ("Digital Government" OR "master plan" OR "cloud" OR "data center")
site:kiribati.gov.ki ("Telecommunications Act" OR "Data Protection Act 2025" OR "Digital Government")
"Kiribati" "Telecommunications Act" "2017" amendment
"Kiribati" "Data Protection Act 2025" (commencement OR gazette OR regulations)
"Kiribati Digital Government Project" ("data center" OR "cloud" OR "procurement" OR "container")
"Pacific Regional Connectivity Program" Kiribati ("EMCS" OR "cable" OR "connectivity")
```

---

## 4. Utility, grid, and energy evidence

Kiribati's power sector is the strongest structural argument against near-term commercial datacenters; use it to grade feasibility claims, not to find facilities.

- **PUB (Public Utilities Board)**: https://pub.com.ki/ - state-owned utility; electricity, water, sewerage for South Tarawa. Grid-connected generation is diesel-based; STREP adds 5 MW solar + 13 MWh BESS at Bonriki (https://pub.com.ki/south-tarawa-renewable-energy-project-strep/ ; https://pub.com.ki/projects/).
- **ADB STREP documents**: PAM https://www.adb.org/sites/default/files/project-documents/49450/49450-021-pam-en.pdf and sector assessment https://www.adb.org/sites/default/files/linked-documents/49450-021-ssa.pdf - confirm PUB structure, diesel generation, tariff/expansion context.
- **MLPID Energy Planning Division / Power Unit**: https://www.mlpid.gov.ki/ - energy context for Line and Phoenix Islands (village grids, solar + storage programs; e.g., Kiritimati solar/diesel projects).

Power caveats to record:

- South Tarawa's grid cannot support a multi-MW datacenter today; any announced datacenter MW figure must be checked against PUB connection/feed evidence.
- Outer islands (incl. Kiritimati) run small diesel/solar hybrid grids; a cable landing station's small power draw is not evidence of datacenter capacity.
- Keep `gross electrical capacity`, `IT load`, `substation/feed`, and `planned scale` in separate fields; PUB data is A-grade for tariff/generation context, not a project register.

Utility query templates:

```text
site:pub.com.ki ("solar" OR "diesel" OR "STREP" OR "grid" OR "tariff" OR "data")
"Public Utilities Board" Kiribati ("substation" OR "feeder" OR "capacity" OR "MW")
"South Tarawa" ("data center" OR "server" OR "cloud") ("power" OR "electricity" OR "diesel")
site:mlpid.gov.ki ("solar" OR "power" OR "energy") ("Kiritimati" OR "Kanton" OR "Tabuaeran")
"Kiribati" ("data center") ("MW" OR "power purchase" OR "substation")
```

---

## 5. Official cloud and operator seed list

### 5.1 Hyperscale cloud regions - absence check

Use current official region pages to verify that Kiribati has **no** AWS, Azure, Google Cloud, or Oracle OCI public cloud region. Do not create a KI facility from SaaS availability, partner hosting, edge cache, or customer-country support.

| Provider | Official source | Kiribati handling |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No KI region. Nearest practical regions: Sydney, Singapore, Tokyo. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No KI region. Azure/M365 usage by KI customers is served from outside the country. |
| Google Cloud | https://cloud.google.com/about/locations | No KI region. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No KI public cloud region. |

Cloud queries:

```text
"AWS" "Kiribati" ("region" OR "availability zone" OR "edge" OR "Local Zone")
"Microsoft Azure" "Kiribati" ("region" OR "data center")
"Google Cloud" "Kiribati" ("region" OR "data center")
"Oracle Cloud" "Kiribati" ("region" OR "data center")
"cloud region" "Kiribati" OR "Tarawa"
"sovereign cloud" Kiribati
"data residency" Kiribati ("cloud" OR "data center" OR "government")
```

### 5.2 Official operator/platform seeds

| Operator/platform | Official source | Division | Status and method notes |
|---|---|---:|---|
| Planned domestic/containerized government data center | JICA survey PDF (2026-02); https://www.mict.gov.ki/kdgp ; World Bank P176108 procurement plan | Gilbert Islands (Tarawa/South Tarawa) | **Procurement/planned**: JICA describes a small container-type domestic DC need/design; World Bank plan lists Phase 2 `KI-MICTTD-470992-GO-RFQ` as `Pending Implementation`. Not operational until commissioned. |
| Containerized DC + government cloud (KDGP P176108) | https://www.mict.gov.ki/kdgp ; World Bank procurement plan; tender mirrors for notice metadata | Gilbert Islands (Tarawa) | **Procurement/planned**: record exact phase, process status, award, delivery, and commissioning once published. A-grade for World Bank plan; C-grade for tender mirrors. |
| BNL (BwebwerikiNet Limited) | https://www.bnl.com.ki/projects | Gilbert Islands (Tarawa); Line Islands (Kiritimati) | State cable/infrastructure company; implementing agency for Kiritimati Cable Project and EMCS; operator of passive networks (outer islands, South Tarawa fibre backbone). Grade A for cable/network facts; not a datacenter operator. |
| EMCS Tarawa/Nanikai CLS | https://www.eastmicronesiacable.com/ ; https://www.bnl.com.ki/blog/east-micronesia-cable-lands-in-first-pacific-location-of-kiribati ; NEC release 2026-05-15 | Gilbert Islands (South Tarawa, Nanikai/Tarawa landing site) | **Cable landing station**, landed 2025-07-25; construction completed and handed over 2026-05-15. Re-check RFS/retail service status. Record as interconnection anchor. |
| SX NEXT Kiritimati spur / Tabwakea CLS | https://www.bnl.com.ki/projects ; https://www.submarinenetworks.com/en/systems/trans-pacific/southern-cross-next/southern-cross-next-cable-system-overview ; https://geocables.com/location/tabwakea-kiribati | Line Islands (Kiritimati, Tabwakea) | **Cable landing station / submarine spur**: BNL and Submarine Networks confirm the Kiritimati spur to Tabwakea; use operator/project pages for status and treat directories as geography/status cross-checks. |
| Vodafone Kiribati (ATHKL) | https://vodafone.com.ki/ ; https://www.ath.com.fj/our-story/group-structure-2/ ; JICA survey | Gilbert Islands (South Tarawa core; Kiritimati presence) | ATH acquired TSKL assets in 2015 and operates Vodafone Kiribati. JICA says South Tarawa sites upgraded to 4G+ and 5G core readiness is being prepared. Treat core/network sites as leads unless named as colocation. |
| Ocean Link Ltd | https://www.gsma.com/get-involved/gsma-membership/gsma_orgs/ocean-link-ltd/ ; JICA survey | Gilbert Islands (South Tarawa); Line Islands (Kiritimati/remote-island rollout) | Second mobile/ISP operator. JICA identifies Ocean Link as a competitor to Vodafone and active in remote-island mobile projects. Core sites = leads, not colocation. |
| PUB | https://pub.com.ki/ | Gilbert Islands (South Tarawa) | Power utility; energy context only (see Section 4). |

Operator queries:

```text
site:mict.gov.ki ("cloud" OR "data center" OR "container" OR "server")
site:bnl.com.ki ("cable" OR "landing station" OR "data" OR "EMCS" OR "SX NEXT")
site:eastmicronesiacable.com ("ready for service" OR "landing" OR "Kiribati" OR "Tarawa")
site:vodafone.com.ki ("enterprise" OR "business" OR "hosting" OR "cloud" OR "data")
"Vodafone Kiribati" ("data center" OR "cloud" OR "hosting" OR "colocation")
"Ocean Link" Kiribati ("data center" OR "server" OR "hosting" OR "network")
"Ocean Link" ("Tarawa" OR "Kiritimati") ("LTE" OR "4G" OR "fibre" OR "fiber")
site:nec.com Kiribati OR EMCS ("complete" OR "ready for service")
```

---

## 6. Division coverage workflow

Run the same four-pass workflow for every division:

1. **National seed pass:** MICT/DTO (KDGP, DPA 2025), MFED, WB notices (P176108, PRCP Phase 4), JICA survey, BNL (EMCS, SX NEXT), Vodafone Kiribati, Ocean Link, PUB, MTCIC/IPD, MLPID, cloud-region pages.
2. **Named-site pass:** South Tarawa, Betio, Bairiki, Ambo, Nanikai, Bonriki, Bikenibeu, Eita, Teaoraereke (Gilbert); Kiritimati, Tabwakea, London, Banana, Teraina, Tabuaeran (Line); Kanton/Abariringa (Phoenix).
3. **Division pass:** run division templates below; map a hit only when town/islet/site evidence places it in that division.
4. **Validation pass:** classify as government DC, procurement-stage gov cloud/DC, cable landing station, telco exchange/server room, satellite gateway, planned proposal, or false positive.

### Gilbert Islands (priority: South Tarawa)

South Tarawa hosts essentially all of Kiribati's real datacenter-adjacent infrastructure: KDGP containerized DC/government cloud procurement, EMCS Nanikai/Tarawa CLS, and telco cores (Vodafone Kiribati, Ocean Link). Outer Gilbert atolls (Abaiang, Marakei, Butaritari, Makin, Nonouti, Tabiteuea, Onotoa, Beru, Nikunau, Aranuka, Kuria, Abemama, Arorae, Tamana) are negative-expectation; watch for island-council/health/bank server rooms and satellite/Starlink gateways only.

```text
"South Tarawa" OR "Tarawa" ("data center" OR "data centre" OR "server room" OR "cloud" OR "container")
"Betio" OR "Bairiki" OR "Ambo" OR "Nanikai" OR "Bonriki" ("data" OR "server" OR "cable landing")
"Kiribati" ("national data center" OR "government data center" OR "government cloud")
"containerized data center" Kiribati OR Tarawa
"EMCS" OR "East Micronesia Cable" ("Tarawa" OR "Nanikai" OR "ready for service")
"Vodafone Kiribati" ("exchange" OR "core" OR "server" OR "data")
"{outer atoll}" Kiribati ("server room" OR "data center" OR "telecom" OR "Starlink" OR "satellite")
```

### Line Islands (priority: Kiritimati)

Kiritimati is the strategic watch division: SX NEXT Tabwakea CLS in service since 2022, MLPID's stated ambition to make Kiritimati a "world-class investment hub", cheap land, and one of the best connected points in the central Pacific - but diesel/solar power limits and no datacenter proposal verified as of 2026-08. Teraina and Tabuaeran: no expected activity.

```text
"Kiritimati" OR "Christmas Island Kiribati" ("data center" OR "data centre" OR "server" OR "cloud" OR "compute")
"Kiritimati" ("SX NEXT" OR "Southern Cross NEXT" OR "Tabwakea" OR "landing station")
"Tabwakea" OR "London" OR "Banana" ("cable" OR "internet" OR "data" OR "power")
site:mlpid.gov.ki ("Kiritimati" OR "Line Islands") ("investment" OR "ICT" OR "data" OR "cable" OR "solar")
"Kiritimati" ("solar" OR "diesel" OR "power") ("MW" OR "plant" OR "grid")
"Kiritimati" ("satellite" OR "Starlink" OR "Kacific" OR "gateway")
"Line Islands" Kiribati ("data center" OR "internet exchange" OR "IXP")
```

Watch list: any MLPID/BNL/government announcement pairing SX NEXT capacity with land, power, or investment promotion on Kiritimati; any satellite-gateway campus with server-room claims.

### Phoenix Islands (expected no activity)

Only Kanton (Abariringa) has a permanent settlement; the Phoenix Islands Protected Area (PIPA) covers most of the division. Record negative searches rather than skipping; watch for government/coastguard satellite/telecom equipment only.

```text
"Kanton" OR "Abariringa" OR "Phoenix Islands" ("data" OR "server" OR "internet" OR "telecom")
"Phoenix Islands" ("satellite" OR "radio" OR "communications") Kiribati
"Phoenix Islands Protected Area" ("data" OR "telemetry" OR "communications")
```

---

## 7. Output normalization

For each candidate, capture:

- `name`, `aliases`, `operator`, `ultimate_parent`, `asset_class` (government-DC | gov-cloud-procurement | cable-landing | telco-core | satellite-gateway | planned-proposal)
- `division`, `islet/town/site`, `address_or_landmark`, `coordinates` if reliable
- `status`, `status_date`, `source_status_verb` (e.g., "landed 2025-07-25", "RFQ closed", "in service since 2022-07")
- `capacity_it_mw`, `capacity_electrical_mw`, `racks`, `floor_area` (rare in KI; use null and say so)
- `power_sources` (diesel/solar/BESS), `grid_connection` (PUB South Tarawa vs village grid), `power_caveat`
- `connectivity` (EMCS/SX NEXT/satellite; ISPs Vodafone Kiribati, Ocean Link, Speed Wave, Tentanini, TeniCom)
- `evidence_grade_by_field` and `source_urls`

Known current seed records (as of 2026-08):

| Name | Division | Asset class | Status | Grade |
|---|---|---|---|---|
| Planned domestic/containerized government data center / KDGP government cloud | Gilbert Islands (Tarawa/South Tarawa) | Procurement-stage gov cloud/DC | Phase 2 `KI-MICTTD-470992-GO-RFQ` listed as pending implementation in World Bank 2026-03 plan; tender mirrors show Mar 2026 notice and 2026-03-31 deadline | A for World Bank plan and MICT project context; C for mirrors |
| KDGP containerized DC + gov cloud (P176108) | Gilbert Islands (Tarawa) | Procurement-stage gov cloud/DC | Phase 2 `KI-MICTTD-470992-GO-RFQ` pending implementation in the 2026-03-13 World Bank procurement plan; tender mirrors show Mar 2026 notice and 2026-03-31 deadline | A for World Bank procurement plan; C for mirrors |
| EMCS Tarawa/Nanikai cable landing station | Gilbert Islands (South Tarawa) | Cable landing station | Landed 2025-07-25; construction complete and handed over 2026-05-15; RFS/retail service to re-check | A |
| SX NEXT Kiritimati spur - Tabwakea CLS | Line Islands (Kiritimati) | Cable landing station | SX NEXT branch to Tabwakea; in-service status cross-checked through BNL/Submarine Networks/GeoCables rather than a DC source | A/B for cable evidence, not datacenter evidence |
| Vodafone Kiribati (ATHKL) core/network sites | Gilbert Islands; Kiritimati presence | Telco core | Operational telecom network; no colocation claim verified | A for operator existence; C for facilities |
| Ocean Link core/network sites | Gilbert Islands; Line Islands | Telco core | Operational since 2018/2019 | A (GSMA/TeleGeography); C for facilities |
| South Tarawa fibre backbone / FTTH (WB) | Gilbert Islands | Network infrastructure | Planned/rolling out; BNL passive O&M | B until government/BNL confirmation |

---

## 8. Update/re-check cadence

- **Monthly:** MICT news + tenders (mict.gov.ki/news-page, REOI node), WB procurement notices for P176108 (containerized DC award/status), EMCS official site (RFS), BNL pages (Kiritimati spur retail rollout), MLPID news, PUB project pages.
- **Quarterly:** hyperscaler region pages (absence re-check), PeeringDB/PCH manual check (any KI IX/facility entry; none surfaced in reviewed searches), DataCenterMap/Cloudscene/Baxtel KI directory checks as C-grade leads, DCD and Submarine Networks KI keyword sweeps.
- **Event-driven:** Data Protection Act 2025 commencement/regulations; Telecommunications Act consolidation; any cable RFS/outage news; any MLPID/MTCIC investment announcement naming Kiritimati or Tarawa digital infrastructure; any containerized DC award/delivery news.
- **On every pass:** re-check time-sensitive statuses: EMCS RFS/retail service, WB/STEP award and completion fields for `KI-MICTTD-470992-GO-RFQ`, CCK licence lists, Ocean Link official domain/contact details, PeeringDB absence, and any MICT/MFED/BNL announcement that changes the planned DC from procurement to delivered/commissioned.
