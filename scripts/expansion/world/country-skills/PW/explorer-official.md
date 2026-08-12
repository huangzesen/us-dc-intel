# PW Explorer Official - Palau Datacenter Enumeration via Government, Regulatory, Cable/Telecom, Energy, and Public-Sector Sources

Date: 2026-08-12. Scope: Palau (PW), all 16 state divisions: Aimeliik, Airai, Angaur, Hatohobei, Kayangel, Koror, Melekeok, Ngaraard, Ngarchelong, Ngardmau, Ngatpang, Ngchesar, Ngeremlengui, Ngiwal, Peleliu, Sonsorol. Angle: official/regulatory discovery for operational, under-construction, proposed, and false-positive datacenter candidates.

Reliability grades used by this explorer: **A** = primary government, regulator, state-owned operator, public utility, registry, official cloud/provider page, multilateral lender project document, or stock-exchange filing; **B** = reputable local, regional, or trade press with named parties and dates; **C** = directory, marketplace, SEO hosting page, unverifiable marketing page, or unattributed aggregate. Record Grade C only as a lead or negative-control note; do not use it to establish a facility.

## 0. Verified Country Baseline

- Palau is a compact Pacific island state with 16 state governments. The national PalauGov states page states that the Constitution designates 16 traditional municipalities as states and that the states have their own governments: https://www.palaugov.pw/states/.
- There is no public national planning-permit search portal, no e-permitting database, and no national datacenter association found for Palau. For any new facility, the official-first route is PalauGov/OEK law, Foreign Investment Board (FIB), corporate registry, state government contacts, telecom regulator, PPUC/energy approvals, and then press.
- No verified operational commercial colocation, hyperscale, or cloud-region datacenter in Palau was found in this research pass. The validated infrastructure inventory is mostly telecom/cable assets: BSCC PC1 at Ngeremlengui, BSCC PC2/Echo branch infrastructure at Ngardmau, BSCC customer access in Airai, and PNCC/internal telecom facilities in Koror/Airai.
- The only public commercial datacenter proposal found is the February 2022 DC Alliance / Pacific Blockchain Corporation non-binding MOU for a Tier III-rated facility. The SGX filing says the MOU was non-binding, had a 12-month term from 10 February 2022 unless replaced by a term sheet or binding agreement, and described 1 MW / 200 racks initially with potential expansion to 5 MW / 1,000 racks: https://links.sgx.com/1.0.0/corporate-announcements/3CWI072CXHPQGQJH/701605_FHL%20-%20MOU%20between%20DCA%20and%20PBC.pdf. No verified construction or operational follow-up was found through 2026-08-12, so keep this as `announced_mou` unless new primary evidence appears.
- Palau has no AWS, Azure, Google Cloud, or Oracle Cloud public cloud region in the official region lists checked. Use these absence checks to prevent mistaking resellers, Guam assets, or SEO pages for a Palau hyperscale deployment.
- English is the working language for official records and business reporting. Palauan-language terms do not materially improve datacenter discovery; use English queries with `Palau`, `Belau`, `.pw`, and state names.

## 1. Official Sources To Check First

### 1.1 National And State Government

Primary sources:

- PalauGov national portal: https://www.palaugov.pw/
- PalauGov states index and state contact pages: https://www.palaugov.pw/states/
- Palau National Code Commission / Palau law portal: https://www.palaulaw.gov.pw/palau-national-code-annotated
- RPPL No. 10-17 Telecommunications Regulatory Framework: https://www.palaugov.pw/documents/rppl-no-10-17-telecommunications-regulatory-framework/
- Koror State Government: https://www.kororstategov.com/ and laws page https://www.kororstategov.com/laws.html
- Bureau of Revenue and Taxation business license materials on PalauGov / Ministry pages, including the business license application and renewal notices.

Use:

- Verify state-level jurisdiction, public notices, procurement, business licensing, and any government ICT/server-room procurement.
- Use the PalauGov state pages as the fallback contact source for states with no meaningful independent web presence.
- For state coverage, search all 16 names explicitly; do not infer absence from a country-level query alone.

Government query templates:

```text
site:palaugov.pw "data center" OR "data centre" OR datacenter
site:palaugov.pw "server room" OR "server" OR "hosting" OR "ICT"
site:palaugov.pw "submarine cable" OR "cable landing" OR "fiber optic"
site:palaugov.pw "procurement" "ICT" OR "telecommunications" OR "data"
site:palaugov.pw "business license" "telecommunications" OR "data"
site:palaulaw.gov.pw "telecommunications" OR "Belau Submarine Cable" OR "Foreign Investment"
site:kororstategov.com "business license" OR "permit" OR "telecommunications"
```

### 1.2 Telecom Regulator And Telecommunications Law

Primary sources:

- RPPL No. 10-17 Telecommunications Regulatory Framework, PalauGov document page: https://www.palaugov.pw/documents/rppl-no-10-17-telecommunications-regulatory-framework/
- Telecom Equipment Regulation draft, Bureau of Communications / MPIIC: https://www.palaugov.pw/wp-content/uploads/2022/06/Telecom-Equipment-Regulation-Draft-for-APA-Rulemaking.pdf
- World Bank ICT Sector Technical Assistance for Palau (P160504) project records and implementation documents: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/781261526293835086

Verified signals:

- RPPL 10-17 established Palau's modern telecom regulatory framework and the Bureau of Communications as regulator. Treat telecom licenses, authorizations, and equipment approvals as relevant gates for datacenter operators that provide network services, interconnection, hosting, or telecom equipment rooms.
- The World Bank completion documentation is useful for market structure, BoC capacity, and moratoria/license context; it is not facility evidence by itself.

Regulatory query templates:

```text
"Bureau of Communications" Palau telecommunications
"Palau" "RPPL No. 10-17" telecommunications regulator
site:palaugov.pw "Telecom Equipment Regulation" "Palau"
"Palau" "ICT Sector Technical Assistance" P160504
"Palau" telecommunications license "retail service provider"
```

### 1.3 Belau Submarine Cable Corporation (BSCC)

Primary sources:

- BSCC official site: https://belaucable.com/
- BSCC About page: https://belaucable.com/about
- BSCC Business Plan FY 2025-2029: https://belaucable.com/s/BSCC-Business-Plan-2025-2029.pdf
- BSCC Business Plan FY 2022-2026: https://bscc-online.squarespace.com/s/211006-FY-2022-BSCC-Business-Plan-v-31.pdf
- BSCC procurement/public notices: https://belaucable.com/procurement and PalauGov BSCC public notices.

Verified signals:

- BSCC is a state-owned wholesale broadband/cable corporation created to own and manage Palau's submarine fiber network.
- PC1/BSCCnet is the first submarine connection, built with ADB support and ready for service in December 2017. The PC1 landing station / CAP-N is in **Ngeremlengui**.
- BSCC customer access points are CAP-N at Ngeremlengui and CAP-A at **Airai**. The 2022-2026 business plan says BSCC offered CAP-N to Guam connectivity and temporary access at KB Shell corner in Airai, with long-term CAP-A at the airport site targeted for early 2022.
- PC2/Echo Palau Branch is the second international connection. BSCC's 2025-2029 plan says PC2 Ready for Service is expected in **Q3 2026** and describes a final-splice focus in 2025/H1 2025 with RFS in H2/Q3 2026 depending on the document section. Use 2026 as the current official expectation unless later BSCC/AIFFP evidence supersedes it.
- The AIFFP 2026 fact sheet describes the Palau ECHO branch as a dedicated branch off Echo, with a landing station at **Ngardmau**, Palau, and completion in **mid 2026**: https://www.aiffp.gov.au/sites/default/files/2026-05/AIFFP_DSN_Factsheet_%237_Expanding%20digital%20connectivity%20in%20Palau%20via%20a%20submarine%20cable%20system_20260527.pdf.
- Cable landing stations and CAP sites may contain power, cooling, racks, and telecom equipment, but they are not commercial datacenters unless the source says colocation/datacenter services are offered.

BSCC query templates:

```text
site:belaucable.com "data center" OR "data centre" OR datacenter OR "co-location" OR colocation
site:belaucable.com "CAP-N" OR "CAP-A" OR "Customer Access Point"
site:belaucable.com "PC2" OR "Echo" OR "Ngardmau" OR "Ngeremlengui"
site:belaucable.com "procurement" "facility" OR "equipment" OR "landing station"
"Belau Submarine Cable Corporation" "data centre" OR "data center" OR colocation
"BSCC" "Ngeremlengui" "Cable Landing Station"
"BSCC" "Ngardmau" "landing station" OR "Echo"
```

### 1.4 PNCC And Licensed Retail Service Providers

Primary sources and strong context:

- PNCC official site: https://www.pnccpalau.com/
- PNCC visitor/WiFi page and hotspot PDFs: https://www.pnccpalau.com/visitors
- BSCC plans for licensed retail service provider model.
- Island Times reporting on retail service providers and BSCC capacity, used as Grade B context only.

Verified signals:

- PNCC is Palau's incumbent national communications provider for mobile, internet, telephone, and digital TV services across Palau.
- PNCC WiFi and internet materials confirm broad service distribution, especially Koror/Airai and tourist/commercial locations. They do not establish datacenter inventory.
- Retail ISPs such as PNCC, Palau Telecom/PT Waves, and Palau Wifi are leads for network POPs/server rooms, not datacenter evidence unless a primary source names a facility.

PNCC/ISP query templates:

```text
site:pnccpalau.com "data center" OR "data centre" OR datacenter OR colocation
site:pnccpalau.com "server" OR "hosting" OR "NOC" OR "fiber" OR "fibre"
"PNCC" Palau "Koror" "server" OR "exchange" OR "facility"
"Palau Telecom" OR "PT Waves" "data center" OR "server" OR "facility"
"Palau Wifi" Palau "server" OR "network" OR "facility"
```

### 1.5 Foreign Investment, Corporate Registry, And Business Licensing

Primary sources:

- Foreign Investment Board (FIB), PalauGov: https://www.palaugov.pw/fib/
- FIB GitHub Pages mirror/resources: https://fibpalau.github.io/
- Palau corporate registry / Financial Institutions Commission: https://www.palauregistries.pw/index.aspx
- U.S. State Department Investment Climate Statement for Palau: https://www.state.gov/reports/2025-investment-climate-statements/palau

Verified signals:

- The FIB page publishes laws, FIAC forms, board minutes, office location, and contact details. Because a foreign-backed datacenter would be a high-value investment, FIB minutes and FIAC-related notices are high-yield checks.
- The State Department investment climate statement says foreign-owned businesses need corporate registration and a Foreign Investment Approval Certificate, making FIB/registry checks a procedural gate for foreign datacenter proposals.
- Palauregistries is useful for entity confirmation, but do not assume absence if older or manually handled companies are not easily searchable.

Registry/FIB query templates:

```text
site:palaugov.pw/fib "data" OR "telecommunications" OR "technology" OR "ICT"
site:palaugov.pw/fib "Pacific Blockchain" OR "DC Alliance"
site:palauregistries.pw "Pacific Blockchain Corporation"
site:palauregistries.pw "data" OR "telecom" OR "hosting"
"Foreign Investment Board" Palau "data centre" OR "data center"
"Pacific Blockchain Corporation" Palau registration OR FIAC
```

### 1.6 Energy, Utility, And Major Load Checks

Primary sources and strong context:

- Palau Public Utilities Corporation (PPUC): https://www.ppuc.com/
- Palau Energy and Water Administration (PEWA): https://www.palaugov.pw/executive-branch/ministries/finance/pewa/
- Palau energy / IPP regulations on PalauGov, including independent power producer regulations.
- PCREEE tariff review page for PPUC diesel dependence: https://www.pcreee.org/publication/review-tariff-palau-utility-corporation-final-report
- U.S. DOE Energy Transition Initiative Palau snapshot: https://www.energy.gov/sites/prod/files/2020/09/f79/ETI-Energy-Snapshot-Palau_FY20.pdf

Verified signals:

- Historic Palau tariff and energy documents show very high diesel dependence. The PCREEE tariff review reports 99.3% diesel generation in its period; later snapshots show diesel still dominant with small solar contribution. Treat power cost and fuel adjustment as a major datacenter feasibility constraint.
- A 1-5 MW datacenter in Palau would be a material load and should leave traces in PPUC, PEA/PEWA, IPP, land lease, or press records. Absence of such records supports a conservative status.

Energy query templates:

```text
site:ppuc.com "data center" OR "data centre" OR "industrial" OR "MW"
site:ppuc.com "tariff" OR "fuel" OR "large customer" OR "interconnection"
site:palaugov.pw "Palau Energy Administration" "tariff" OR "IPP" OR "PPUC"
site:palaugov.pw "renewable" "data centre" OR "data center"
"Palau" "PPUC" "data center" OR "large load" OR "industrial"
```

### 1.7 Official Cloud Region Absence Checks

Use these only to confirm whether a named hyperscaler has a Palau public region, local zone, edge zone, or official cloud facility. Do not promote reseller hosting to hyperscale inventory.

| Provider | Official source | Palau result as of 2026-08-12 |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Palau AWS Region or Local Zone found. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No Palau Azure region found. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | No Palau Google Cloud region found. |
| Oracle Cloud Infrastructure | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | No Palau OCI public cloud region found. |

## 2. Division Coverage Matrix

Run the universal query block for each of the 16 states. The table below sets the expected yield and primary official route; it is not a facility census.

| State | Coverage status | Expected yield / official route |
|---|---:|---|
| Aimeliik | Covered | Rural Babeldaob state on the Ngeremlengui-Airai fiber route. Check PalauGov state page, BSCC local fiber references through Ngatpang/Aimeliik/Airai, PPUC notices, and local press. Low DC yield. |
| Airai | Covered | Airport, industrial/commercial corridor, BSCC CAP-A airport access point, PNCC service locations. Search BSCC plans, PNCC, airport/land notices, and state contacts. Medium yield for telecom POP, not commercial DC. |
| Angaur | Covered | Remote southern state. Check PalauGov state page, PNCC/USO and satellite/backhaul mentions, and press. Very low DC yield. |
| Hatohobei | Covered | Remote Southwest Islands state with administrative contact in Koror. Check PalauGov, PNCC/USO, satellite/emergency communications. Very low DC yield. |
| Kayangel | Covered | Northern outer island. Check PalauGov, PNCC/USO, port and emergency communications. Very low DC yield. |
| Koror | Covered | Commercial center and likely PNCC/internal enterprise server-room concentration. Check PNCC, Koror State, PalauGov procurement, FIB, registry, banks, and press. Highest non-cable yield, but no confirmed commercial DC. |
| Melekeok | Covered | Ngerulmud capital/government campus. Check PalauGov ministries, OEK/procurement, national ICT, and energy/government server-room mentions. Do not confuse Ngerulmud with Ngeremlengui. |
| Ngaraard | Covered | Rural Babeldaob. Check PalauGov state contact, PPUC, PNCC service, press. Low DC yield. |
| Ngarchelong | Covered | Rural northern Babeldaob. Check PalauGov, PNCC, local fiber/road/port mentions. Low DC yield. |
| Ngardmau | Covered | PC2/Echo branch landing station at Ngardmau. Check BSCC, AIFFP, Blue Dot Network, NEC/DXN, and PalauGov/press. High yield for cable infrastructure, not commercial DC. |
| Ngatpang | Covered | Rural Babeldaob on Ngeremlengui-Airai fiber route. Check BSCC local fiber mentions, PalauGov, PPUC, press. Low-to-medium yield for fiber route evidence. |
| Ngchesar | Covered | Rural Babeldaob/east coast. Check PalauGov, PNCC, press. Low DC yield. |
| Ngeremlengui | Covered | PC1 cable landing station / CAP-N. Check BSCC, ADB, Submarine Networks, NEC, land lease notices, and PalauGov. High yield for cable infrastructure. |
| Ngiwal | Covered | Rural Babeldaob/east coast. Check PalauGov, PNCC, press. Low DC yield. |
| Peleliu | Covered | Remote island state. Check PalauGov, PNCC/USO, satellite/emergency communications. Very low DC yield. |
| Sonsorol | Covered | Remote Southwest Islands state. Check PalauGov, PNCC/USO, satellite/emergency communications. Very low DC yield. |

Universal per-state query block:

```text
"{state}" Palau "data centre" OR "data center" OR datacenter
"{state}" Palau "server room" OR "server" OR hosting OR colocation
"{state}" Palau "cable landing" OR "submarine cable" OR "fiber" OR "fibre"
"{state}" Palau telecom OR telecommunications OR internet OR wifi
site:palaugov.pw "{state}" "communications" OR "ICT" OR "data"
site:islandtimes.org "{state}" internet OR cable OR ICT OR telecommunications
```

High-yield locality variants:

```text
"Koror" OR "Malakal" Palau "PNCC" OR "server" OR "telecom" OR "data center"
"Airai" Palau "CAP-A" OR "airport" "fiber" OR "fibre" OR "BSCC"
"Ngeremlengui" Palau "CAP-N" OR "cable landing station" OR "BSCC"
"Ngardmau" Palau "Echo" OR "PC2" OR "cable landing station" OR "DXN"
"Ngerulmud" OR "Melekeok" Palau "government" "ICT" OR "server" OR "data"
"Hatohobei" OR "Sonsorol" OR "Kayangel" Palau satellite OR "internet" OR "PNCC"
```

## 3. Official Enumeration Workflow

1. Start with a national sweep: PalauGov, Palau National Code, BoC/RPPL 10-17, FIB, corporate registry, PPUC/PEWA, BSCC, PNCC.
2. Run the 16-state query block. Mark each state `covered` even when the result is negative; record why the state is low-yield.
3. For every positive lead, classify the asset type before assigning datacenter status: `commercial_datacenter`, `government_server_room`, `telecom_exchange`, `cable_landing_station`, `customer_access_point`, `office_only`, or `seo_false_positive`.
4. Require at least one Grade A source for operational status. If only trade press exists, cap status at announced/proposed unless the press quotes or links a primary document.
5. Check FIB minutes and registry for any foreign-backed technology/datacenter entity. Use the SGX filing for DC Alliance/PBC as Grade A evidence of a non-binding MOU only.
6. Check PPUC/PEA/PEWA for major load, IPP, renewable, or tariff proceedings tied to a datacenter. A multi-MW facility should produce official or press-visible power evidence.
7. Check official cloud-region pages and directory sites as negative controls.
8. Record capacity only when the source states IT load, rack count, building area, or telecom capacity. Never convert cable bandwidth or utility generation into datacenter MW.

## 4. Current Facility And Project Seeds

Use this seed list to validate enumeration output; re-check every item before recording it in an inventory.

| Seed | State | Type | Current status as of 2026-08-12 | Best evidence | Reliability |
|---|---|---|---|---|---|
| BSCC PC1 / BSCCnet Cable Landing Station, CAP-N | Ngeremlengui | Cable landing station / telecom equipment room | Operational; PC1 RFS Dec 2017 | BSCC official pages/business plans; ADB; Submarine Networks | A for BSCC/ADB, B for trade map/articles |
| BSCC CAP-A airport access point | Airai | Customer access point / potential colocated telecom equipment | Operational or late-stage access infrastructure; verify current CAP-A terms in BSCC docs | BSCC official About and business plans | A |
| BSCC PC2 / Echo Palau Branch landing station | Ngardmau | Cable landing station / modular CLS | Under construction / pre-service; current official expectation mid/Q3 2026 | BSCC 2025-2029 plan; AIFFP 2026 fact sheet; Blue Dot Network; NEC/DXN trade coverage | A for BSCC/AIFFP, B for trade |
| PNCC internal exchange/server facilities | Koror, Airai | Telecom exchange / internal server room | Operational telecom infrastructure; no public MW/rack data | PNCC official site; PNCC WiFi/service materials | A for operator existence; facility details often unverified |
| DC Alliance / Pacific Blockchain Tier III datacenter | Unspecified Palau; likely Koror/Airai/Melekeok corridor until a site is named | Proposed commercial datacenter | Announced non-binding MOU in Feb 2022; MOU term 12 months; no verified build/operation found | SGX filing; DCD/Island Times/w.media coverage | A for MOU terms, B for press, not A for operational status |
| Government/Ngerulmud server rooms | Melekeok | Government server room | Plausible but unverified; do not record without procurement/source | PalauGov/OEK procurement and ICT searches | Not recordable without evidence |
| Guam colocation used by Palau customers | n/a | Regional fallback | Operational in Guam only; never count as Palau | GTA, Guam Exchange, Baxtel/Cloudscene Guam pages | A/B for Guam context only |

## 5. Reliability Rules And Pitfalls

- Grade A source does not automatically mean Grade A facility status. Example: the SGX announcement is Grade A for the existence and terms of the MOU, but only supports `announced_mou`, not `operational`.
- Cable landing stations are telecommunications infrastructure. Include them in infrastructure notes when the broader project tracks datacenter-adjacent assets, but do not classify them as commercial datacenters unless colocation or datacenter service is explicitly offered.
- PNCC offices, BSCC corporate offices, hotspots, and retail shops are not datacenters. They are leads for possible network operations or exchange rooms.
- PC1 belongs in Ngeremlengui; PC2/Echo branch belongs in Ngardmau; CAP-A belongs in Airai. Do not assign these to Koror because Koror is the business center.
- Ngerulmud is in Melekeok. Ngeremlengui and Ngardmau are separate states.
- Digital residency, blockchain, fintech, and cybersecurity stories are only datacenter leads when they name a facility, site, capacity, power approval, or procurement.
- SEO pages advertising Palau VPS, Ngerulmud dedicated servers, or generic `.pw hosting` without an address/operator/registry source are Grade C false positives.
- Guam is regional context, not Palau inventory. Use Guam only to explain where nearby colocation/interconnection exists.

## 6. Summary Expected Outcome

A careful Palau enumeration should produce a very small, conservative result set: PC1/CAP-N in Ngeremlengui, PC2/Echo branch infrastructure in Ngardmau, CAP-A/customer-access infrastructure in Airai, PNCC/internal telecom leads in Koror/Airai, and the DC Alliance/Pacific Blockchain proposal as an expired or unproven MOU-stage lead unless fresh primary evidence is found. All 16 states must still be queried and marked covered so low-yield rural and outer-island divisions are not silently skipped.
