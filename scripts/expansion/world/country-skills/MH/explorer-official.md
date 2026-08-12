# MH Explorer Official - Marshall Islands Datacenter Enumeration via Official/Regulatory Sources

Date: 2026-08-12. Scope: Republic of the Marshall Islands (MH/RMI), 24 municipality divisions (atolls/single islands). Angle: official/regulatory methodology for enumerating operational and proposed datacenter-class facilities. Reliability grades: A = official/primary source (RMI government/ministry, Nitijela legislation, NTA official page/announcement, ICANN announcement, World Bank project document, USTDA/State Dept release, US Army/FCC official record, cloud-provider official region page, cable-operator official landing-station record), B = strong secondary/trade press with named parties (DCD, Submarine Networks, Marshall Islands Journal, Pacific Island Times, Reuters, APNIC), C = directory/aggregate/marketing-only evidence.

Verified status note (2026-08-12): keep only one confirmed operational datacenter-class site in the country without further evidence: **NTA Majuro**, because ICANN's 2017 primary announcement states that NTA hosted the L-root node in Majuro and provided colocation in its datacenter plus bandwidth. Treat NTA Ebeye/Kwajalein as a confirmed telecom/cable-landing facility, not a public datacenter, unless a primary source states it has datacenter/colo/server-room services. Treat IOKWE/Pacific Connect and Central Pacific Cable as planned connectivity infrastructure only.

---

## 0. Marshall Islands structural facts (frame every search around these)

- RMI is a microstate: 29 atolls + 5 single islands; this repo uses the 24-municipality/local-government layer. The RMI Judiciary local-government constitution page is the best official division cross-check, although it lists available constitutions rather than a clean GIS table and omits some low-population divisions from the downloadable set. Operational ICT infrastructure is concentrated in two settlements: Majuro (capital, Delap-Uliga-Djarrit/Laura corridor) and Ebeye (Kwajalein Atoll). Everything else is low-population outer atolls. There is no public evidence of a commercial colocation market; the realistic facility universe is: (1) NTA telecom/cable-landing facilities, (2) government and donor-funded ICT (Digital Republic project), (3) banks/financial-sector server rooms, (4) US Army Kwajalein military IT (restricted), (5) future subsea-cable landing stations (IOKWE/Pacific Connect/CPC).
- NTA (Marshall Islands National Telecommunications Authority) is the pivotal entity: majority state-owned, historically the sole telecom provider, operator of domestic/international voice, data, internet, and mobile services, with published Majuro and Ebeye addresses. ICANN confirms NTA hosts the L-root node in Majuro and provided datacenter colocation for it (Grade A). NTA/HANTRU-1 facilities at Majuro and Ebeye/Kwajalein are the only high-confidence carrier-grade leads; record them as telecom datacenter/landing-station infrastructure, not retail commercial colo unless a product page or contract says otherwise.
- Connectivity backbone (cable facts anchor every division search): HANTRU-1 submarine cable (in service 2010) links the U.S. Army/Reagan Test Site on Kwajalein to Guam, with RMI/FSM extensions including Majuro and Ebeye. FCC public notice evidence says the base cable had two fiber pairs, initial 20 Gbps protected OC-192 configuration and 160 Gbps final design capacity, and that the Kwajalein cable station was to be owned/operated by USAKA/Reagan Test Site. TeleGeography/Submarine Cable Map lists HANTRU1 landing points including Majuro, Kwajalein, Pohnpei, and Guam. Future: IOKWE branch to Google's Halaihai/Pacific Connect landing Majuro + Ebeye (planned; NTA owner/operator per Submarine Networks, B until NTA primary page is accessible); Central Pacific Cable feasibility also includes RMI in the route list (USTDA Grade A for study scope).
- Regulatory regime (Grade A legislative anchors): National Telecommunications Act 1990 created NTA and vested telecom property/functions in it; Bill 66 (reported by Marshall Islands Journal) removed the exclusive-service language; Telecommunications (Reform) Act 2025 (P.L. 2025-28 / 2025-0028, commencement 2025-04-21) creates a regulated open telecom market and modern licensing. The 2025 public-law list also includes Electronic Transactions Act 2025, Digital Transformation and Identity Verification Act 2025, and Cybersecurity Act 2025, which matter for digital-government/server-hosting context. There is no public datacenter license class and no planning-permit database comparable to EU/US systems; do not search for a national DC registry.
- Government digital agenda: Digital Republic of the Marshall Islands Project (World Bank, 30M USD grant, started 2021; project P171517) funds affordable connectivity, digital government foundations, cybersecurity, digital ID; a Digital Government Office sits under the Chief Secretary. Government ICT/server infrastructure is concentrated in Majuro (Capitol/Uliga-Delap area). World Bank project documents are the best Grade A source for government DC/server-room plans.
- Cloud/hyperscale: no AWS/Azure/GCP/OCI region or local zone in MH. Cloud-region official pages are used to confirm absence and to avoid promoting Starlink/VPS resellers into cloud presence evidence. CDN edge-POP claims for Majuro exist in directories but are unverified in this pass (mark C until confirmed on the provider's official edge-locations page).
- Energy: electricity is diesel-based and island-scoped (Marshall Islands Electricity Company MIEC on Majuro; Kwajalein Atoll Utilities Authority KAJUR on Kwajalein/Ebeye); no interconnected grid, no renewable-DC special regime. Grid/power constraints effectively rule out any MW-scale DC - treat any data center claim that implies utility-scale power with strong skepticism (Grade C until power evidence appears).
- Language: English is the working language for government/telecom; Marshallese terms rarely used for this domain. English-first searching is sufficient; add site:gov.mh / site:rmigov.com / site:nta.mh scoping.

---

## 1. Grade A official/regulatory sources

### 1.1 NTA - National Telecommunications Authority (nta.mh)

- NTA home/contact: https://www.nta.mh/ and https://www.nta.mh/contact-us/ - Grade A for current published addresses: Majuro shipping address `NTA, 1169, Main Street, Delap, Majuro, Marshall Islands 96960`; Ebeye shipping address `NTA, 5025 Main Street, Ebeye, Marshall Islands 96970`.
- ICANN L-root node announcement (2017): https://www.icann.org/en/announcements/details/marshall-islands-national-telecommunications-authority-contributes-to-responsive-and-resilient-internet-with-l-root-instance-in-marshall-islands-6-3-2017-en - Grade A; confirms the L-root instance was installed in Majuro and that NTA supplied equipment, bandwidth, and colocation in its datacenter. This is the strongest primary evidence for an operational datacenter-class facility in MH.
- NTA Facebook (facebook.com/mhnta) - NTA publishes outage/upgrade/service notices here (e.g., 2023 Ebeye voice outage, modem reconfiguration incidents); useful status/incident evidence for facility operations. Grade A for NTA's own posts, B for reposts.
- What to extract from NTA sources: physical addresses of NTA HQ/switch buildings and landing-station sites (Majuro: Uliga area; Ebeye: Kwajalein atoll), transmission/DDF rooms, earth-station locations, cable terminal equipment (CTE) upgrades (2021-2023 HANTRU-1 upgrades), service area = which atolls have NTA equipment huts (outer-island satellite-fed sites).

NTA queries:
```
site:nta.mh "data center" OR "server" OR "hosting" OR "colocation"
site:nta.mh "Contact Us" "5025 Main Street" "Ebeye"
site:nta.mh "Main Street" "Delap" "Majuro"
site:nta.mh "cable" OR "landing" OR "HANTRU" OR "fiber"
site:facebook.com/mhnta "Ebeye" OR "Majuro" OR "outage" OR "upgrade"
"NTA" "L-root" "Majuro"
site:icann.org "Marshall Islands" "root server"
```

### 1.2 Nitijela legislation (rmiparliament.org)

- Legislation portal: https://rmiparliament.org/cms/index.php?option=com_legislation&view=acts_by_tag&Itemid=229
- Telecommunications (Reform) Act 2025: https://rmiparliament.org/cms/images/LEGISLATION/PRINCIPAL/2025/2025-0028/2025-0028_1.pdf - Grade A; published as P.L. 2025-28, commencement 2025-04-21, with an objective to create a regulated open market for authorized telecommunications networks and services. Reading it tells you which license classes exist (none is DC-specific) and who the licensing/regulatory authority is.
- 2025 public-law index: https://www.rmiparliament.org/cms/library/public-laws-by-years/60-2025.html - Grade A for related digital laws (Electronic Transactions, Digital Transformation and Identity Verification, Cybersecurity) and for confirming P.L. 2025-28.
- National Telecommunications Act 1990 (as amended by Bill 66/2022) - use the parliament portal search site:rmiparliament.org telecommunications; the 2022 amendment deleting exclusive is documented in Marshall Islands Journal (B) and World Bank docs (A).
- Marshall Islands Administrative Procedure Act 1979 - referenced by the 2025 Act for regulations; relevant only procedurally.
- What to extract: license classes, operator obligations, regulator name once established (currently reported as Office of the Telecommunications Regulator per National ICT Policy / trade press - B until the office is formally gazetted), any facility/security requirements for cable landing stations.

### 1.3 Ministry of Transportation, Communications & Information Technology (MOTC&IT)

- Government services directory entry: https://www.govserv.org/MH/Majuro/429585256907032/RMI-Ministry-of-Transportation,-Communications-&-Information-Technology (contact info; MOTC&IT works with TCMI, RMI Ports Authority etc.)
- MOTC&IT is the licensing/policy ministry and owner of the ICT portfolio; its formal website is thin - use Nitijela records and government budget documents (Ministry of Finance) for ICT capital projects (e.g., data center / e-government line items). Query: site:gov.mh OR site:rmigov.com MOTC OR "Transportation, Communications" ICT.

### 1.4 RMI Government portal + Digital Government Office

- RMI Government: https://rmigov.com/ (news releases; e.g., President's statements, Digital Republic events). Also legacy gov.mh.
- Digital Republic of the Marshall Islands Project - World Bank project page and documents:
  - Project doc PDF (cited in research pass): https://documents1.worldbank.org/curated/en/099122324225525597/pdf/P1715171fc7d7a02e1b8321f25acb998e53.pdf (P171517). Grade A.
  - Restructuring / implementation document: https://documents1.worldbank.org/curated/en/099072125040537245/pdf/P171517-dd075251-efe4-410b-9bce-2adf01d17e00.pdf - Grade A; confirms the 2025 telecom reform, Starlink local launch on 2025-06-10, and a late-2023 US$40M U.S. Government commitment for fast fiber to all premises in Majuro and Ebeye.
  - Search: site:worldbank.org Marshall Islands digital government P171517 ; site:documents.worldbank.org "Digital Republic" Marshall Islands.
  - Extract: government data center / server-hosting component, digital government platforms, cybersecurity, digital ID, data-protection law plans, telecom liberalization support (PPP for infrastructure).
- Digital Government Office under Chief Secretary - locate via World Bank project reports and RMI budget papers; it is the operational owner of government shared services in Majuro. Query: "Digital Government Office" Marshall Islands Chief Secretary.
- EPPSO (Economic Policy, Planning and Statistics Office) - hosts statistical infrastructure and digital-development reporting: site:rmi-eppso.org OR "EPPSO" digital Marshall Islands.
- Nitijela/parliament news on IOKWE: NTA's IOKWE announcement was covered by DCD (B) and Submarine Networks (B); the underlying announcement is NTA's official channel (A): site:facebook.com/mhnta IOKWE and NTA press releases.

### 1.5 US Government sources (Compact of Free Association partner)

- USTDA - Pacific Connect feasibility: https://www.ustda.gov/ustda-advances-secure-internet-connectivity-in-the-pacific-islands/ - Grade A for the Central Pacific Cable / Pacific Connect program scope including RMI.
- US State Dept - Honolulu Investment Summit (Feb 2026): https://www.state.gov/releases/office-of-the-spokesperson/2026/02/honolulu-investment-summit-connects-u-s-businesses-and-pacific-island-countries - intended Grade A for the 132M USD commitment linking RMI and American Samoa to Pacific Connect, but the page returned a technical-difficulties shell during this verification pass. Until it is directly retrievable, use USTDA as the Grade A Central Pacific Cable source and keep the 132M figure at Grade B via Submarine Networks/DCD/Pacific Island Times.
- US Army Kwajalein Atoll (USAKA) / Reagan Test Site: official pages: https://www.army.mil/kwajalein/ and https://www.smdc.army.mil/ ; MIT Lincoln Laboratory Reagan Test Range: https://www.ll.mit.edu/about/facilities/reagan-test-site ; distributed operations page: https://www.ll.mit.edu/r-d/projects/reagan-test-range-distributed-operations. Grade A/B for existence of major range IT, sensors, telemetry, and command/control; not a public datacenter source. Do not attempt to enumerate restricted military server rooms.
- HANTRU-1 cable official/regulatory anchors: FCC public notice DA-09-1309A1 at https://docs.fcc.gov/public/attachments/DA-09-1309A1.pdf (Grade A for ownership/capacity/cable-station terms); TeleGeography/Submarine Cable Map https://www.submarinecablemap.com/submarine-cable/hantru1-cable-system (Grade B/A for map landing list); APNIC outage article https://blog.apnic.net/2019/04/22/when-the-internet-goes-out-a-marshall-islands-perspective/ (Grade B for operational-dependency context).
- US Government satellite systems on Kwajalein (per CIA/encyclopedic references): legacy Intelsat earth stations + USG SATCOM - context only.

### 1.6 Environmental / energy permitting (thin but checkable)

- RMI Environment Protection Authority (EPA): official site (search RMI Environment Protection Authority). Diesel generators above thresholds may require environmental permits; query site:rmi-eoc.org generator OR "data" OR telecommunications. In practice no public DC generator permits were found in this pass - record nothing without a primary record.
- Marshall Islands Electricity Company (MIEC) - Majuro utility; Kwajalein Atoll Utilities Authority (KAJUR) - Ebeye/Kwajalein utility. No DC-scale connections public. Query: MIEC Majuro electricity large customer (C at best).

### 1.7 Cloud-provider official region pages (absence confirmation)

| Provider | Official page | MH signal |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No MH region; nearest Guam/Oceania region is outside MH. CloudFront edge-POP claim for Majuro unverified - check https://aws.amazon.com/cloudfront/features/ edge-locations list before citing. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No MH region. |
| Google Cloud | https://cloud.google.com/about/locations | No MH region; Google's MH footprint is the Halaihai/Pacific Connect cable branch (IOKWE) - connectivity, not a cloud region. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | No MH region. |

Do not count Starlink availability, VPS resellers, or NTA cloud-like services as a hyperscale region. Do not count Google's IOKWE landing station as a Google data center.

---

## 2. Per-division enumeration workflow (24 municipalities)

Repo divisions (municipalities): Majuro, Kwajalein, Ailinglaplap, Ailuk, Arno, Aur, Ebon, Enewetak & Ujelang, Jabat, Jaluit, Bikini & Kili, Lae, Lib, Likiep, Maloelap, Mejit, Mili, Namdrik, Namu, Rongelap, Ujae, Utrik, Wotho, Wotje.

Generic sweep per division (English):
```
"{Division}" "Marshall Islands" ("data center" OR "datacenter" OR "server room" OR "server" OR "telecom" OR "cable landing" OR "earth station")
"{Division}" atoll NTA (fiber OR satellite OR microwave OR tower)
site:nta.mh "{Division}"
site:intelsat.com OR site:marshallislandsjournal.com "{Division}" connectivity
```

Division routing (who to check first):

| Division | Expected yield | Official-first route | Notes |
|---|---|---|---|
| Majuro | HIGH - the only real cluster | NTA (nta.mh, L-root/ICANN, landing station, earth station), Digital Government Office/World Bank P171517, RMI government, BOMI/CMI (financial/education), EPA (generators) | Assign Delap/Uliga/Rita addresses to Majuro municipality; check NTA HQ, cable landing station, satellite earth station, government data room in Capitol area |
| Kwajalein | MEDIUM-HIGH (two distinct tracks) | Track 1 (civilian): NTA Ebeye landing station + KAJUR power + Ebeye telecom site. Track 2 (military): US Army Kwajalein Atoll / Reagan Test Site IT - context only, Grade B/C | Kwajalein division includes Ebeye; Kwajalein island itself is the US base; Ebadon/Roi-Namur are military sites. Do not double-count HANTRU-1 (one system, two MH landings: Majuro + Ebeye) |
| Jaluit | LOW | NTA outer-island satellite sites; historical admin center (Jaluit) - telecom equipment only | Former colonial capital; only satellite-fed connectivity; no DC evidence found |
| Enewetak & Ujelang, Bikini & Kili, Rongelap, Utrik, Wotje | VERY LOW | Intelsat/NTA small-cell 2G sites (2022-23), school connectivity | Nuclear-test/relocated communities; satellite-fed sites only; log no_projects unless NTA/Intelsat primary record shows a server room |
| Ailinglaplap, Ailuk, Arno, Aur, Ebon, Jabat, Lae, Lib, Likiep, Maloelap, Mejit, Mili, Namdrik, Namu, Ujae, Wotho | VERY LOW | Same Intelsat/NTA sweep + school-internet projects (satellite) | Expect no_projects; a hit only if a donor/telecom primary document names equipment at the atoll |

Workflow per division:
1. Run the generic sweep for the division name + MH context.
2. For Majuro/Kwajalein run NTA + government + cable queries (sections 1.1, 1.4, 1.5).
3. For every division, check Intelsat/NTA outer-island deployment evidence (60 small-cell base stations, satellite hub, and other equipment; mirrored at https://www.broadbandcommission.org/insight/intelsat-connectivity-transforming-lives-and-livelihoods-in-the-marshall-islands/) - if the site is at division X, record only a telecom site, not a DC, unless server-room evidence exists.
4. Record no_projects: true for divisions with no evidence - completeness over precision.
5. Promote to Grade A only with a primary record (NTA page, ICANN, World Bank doc, legislation, USTDA/State, Army official, cable operator official landing-station page).

---

## 3. Confidence grading and pitfalls

Grade A: NTA official page/announcement; ICANN L-root announcement; Nitijela legislation PDF/index; World Bank project document; USTDA/State Department release; US Army/USAKA official page; FCC public notice; cable operator official landing-station record; cloud provider official region page (for absence).

Grade B: DCD, Submarine Networks, Subsea Cables News, APNIC, telecoms.com, Reuters, Marshall Islands Journal, Pacific Island Times, RNZ Pacific, Intelsat/Broadband Commission impact story for outer-island telecom deployments, Wikipedia only for initial lead generation/cross-check.

Grade C: DataCenterMap/Datacenters.com/Cloudscene entries (MH rarely present - absence in directories is a weak signal), dedicated-server marketing pages (e.g., atalnetworks.com Majuro page - reseller marketing, not a facility), unverified CloudFront edge-POP claims, social-media anecdotes.

Pitfalls:
- Do not treat NTA's retail internet service, Starlink availability, or Intelsat cell sites as datacenters. The only facility-grade items are NTA cable-landing/earth-station/root-server installations, government data rooms, and bank/enterprise server rooms.
- HANTRU-1 has two MH landings (Majuro, Kwajalein/Ebeye) - one cable system; do not create two projects without distinguishing landing stations.
- Kwajalein division mixes civilian (Ebeye) and restricted military (base) - military IT is real but non-enumerable publicly; mark honestly.
- IOKWE/Halaihai is a cable branch with planned landing stations in Majuro + Ebeye (~2029 RFS) - record as planned infrastructure, not an operational DC; a future landing station may host small DDF/colo rooms - reassess after construction.
- No planning-permit system: absence of a permit record means nothing; conversely any permit claim needs a primary RMI record.
- Marshallese names: Ebeye (Kwajalein division), Uliga/Delap/Rita (Majuro), Jabor (Jaluit), Enewetak/Ujelang spelling variants - normalize when assigning divisions.

---

## 4. Key sources quick list

- NTA: https://www.nta.mh/ ; contact/addresses: https://www.nta.mh/contact-us/ ; ICANN L-root: https://www.icann.org/en/announcements/details/marshall-islands-national-telecommunications-authority-contributes-to-responsive-and-resilient-internet-with-l-root-instance-in-marshall-islands-6-3-2017-en
- Nitijela: https://rmiparliament.org/cms/index.php?option=com_legislation&view=acts_by_tag&Itemid=229 ; Telecom (Reform) Act 2025 PDF: https://rmiparliament.org/cms/images/LEGISLATION/PRINCIPAL/2025/2025-0028/2025-0028_1.pdf
- World Bank Digital Republic (P171517): https://documents.worldbank.org/en/publication/documents-reports/documentdetail/639311629138295811 ; restructuring PDF: https://documents1.worldbank.org/curated/en/099072125040537245/pdf/P171517-dd075251-efe4-410b-9bce-2adf01d17e00.pdf
- USTDA Pacific Connect: https://www.ustda.gov/ustda-advances-secure-internet-connectivity-in-the-pacific-islands/ ; State Dept (Feb 2026): https://www.state.gov/releases/office-of-the-spokesperson/2026/02/honolulu-investment-summit-connects-u-s-businesses-and-pacific-island-countries
- US Army Kwajalein: https://www.army.mil/kwajalein/ ; MIT LL Reagan Test Site: https://www.ll.mit.edu/about/facilities/reagan-test-site ; MIT LL RDO: https://www.ll.mit.edu/r-d/projects/reagan-test-range-distributed-operations
- HANTRU-1: FCC public notice https://docs.fcc.gov/public/attachments/DA-09-1309A1.pdf ; TeleGeography map: https://www.submarinecablemap.com/submarine-cable/hantru1-cable-system ; APNIC outage context: https://blog.apnic.net/2019/04/22/when-the-internet-goes-out-a-marshall-islands-perspective/
- IOKWE coverage (B): https://www.submarinenetworks.com/en/systems/trans-pacific/iokwe ; https://www.datacenterdynamics.com/en/news/marshall-islands-to-connect-to-googles-halaihai-subsea-cable/
- Intelsat/Broadband Commission outer-island deployment: https://www.broadbandcommission.org/insight/intelsat-connectivity-transforming-lives-and-livelihoods-in-the-marshall-islands/
- RMI Government: https://rmigov.com/

Finalized 2026-08-12 after source verification. Re-run official cloud/cable/regulator pages before any future enumeration refresh.
