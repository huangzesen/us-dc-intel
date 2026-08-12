# MH Explorer Industry - Marshall Islands Datacenter Enumeration via Industry/Vendor Sources

Date: 2026-08-12. Scope: Republic of the Marshall Islands (MH/RMI), 24 municipality divisions. Angle: **industry/vendor methodology** - telecom operators, colocation/hosting players, satellite/cloud vendors, trade press, and directories. Reliability grades: A = official/primary (operator/vendor official page or announcement, ICANN primary announcement, FCC/USG filing, operator investor/company records, cloud-provider official region page), B = strong secondary/trade press (DCD, Submarine Networks, Subsea Cables News, APNIC, telecoms.com, Marshall Islands Journal, Pacific Island Times, RNZ Pacific, Reuters), C = weak/aggregate (directories, reseller marketing, forum/social posts).

Verified status note (2026-08-12): the only confirmed operational datacenter-class industry asset is **NTA Majuro**, because ICANN states NTA supplied colocation in its datacenter for the L-root instance. NTA Ebeye/Kwajalein is a confirmed telecom/cable-landing lead, not a public colocation/datacenter record without more evidence. IOKWE/Pacific Connect and Central Pacific Cable are planned cable projects; do not count them as operational datacenters.

---

## 0. Industry structural facts (frame every vendor search around these)

- MH has **no confirmed commercial colocation market** and no domestic datacenter vendor. The de facto "datacenter-class" infrastructure is owned by **NTA** (National Telecommunications Authority): published offices/facilities in Majuro and Ebeye, HANTRU-1 landing-related infrastructure, Intelsat/satellite backhaul, national switch/transmission buildings, 4G/mobile systems, and the **ICANN L-root server node in Majuro** (2017). If you are enumerating "data centers" strictly, MH yields: NTA Majuro facility (ICANN-confirmed datacenter colocation for L-root, plus telecom infrastructure), NTA Ebeye/Kwajalein landing-station lead, and future IOKWE landing stations (Majuro + Ebeye). Everything else is satellite-fed telecom or server rooms inside banks/government.
- **Market liberalization is now law**: Bill 66 removed NTA's exclusivity language, and the Telecommunications (Reform) Act 2025 opened the market to authorized telecom operators. First real entrants are satellite providers: **SpaceX Starlink** is confirmed by a World Bank project document as locally launched on 2025-06-10, and Starlink's support page lists kit shipping to Majuro, Ebeye, and Kwajalein Island. **OneWeb/Eutelsat** and **SES O3b mPOWER** remain potential enterprise/backhaul technologies unless an RMI terminal, gateway, or service contract is directly confirmed. Satellite service availability is NOT a datacenter - record as connectivity, not capacity.
- **Google Pacific Connect / Halaihai**: NTA's **IOKWE** branch cable (announced March 2026 in trade coverage) is reported to land in **Majuro and Ebeye** and connect to Google's Halaihai system. Submarine Networks names NTA as owner/operator; DCD confirms the planned branch but should remain Grade B until an NTA/government primary URL is captured. USTDA's Central Pacific Cable feasibility study includes RMI in the route list; landing-station buildings are the most plausible future "datacenter-adjacent" assets, but they are not operational DCs.
- **Hyperscaler presence: none** (no AWS/Azure/GCP/OCI region or local zone found on official region pages as of this pass; CloudFront/Cloudflare/Akamai Majuro PoP claims, if encountered in third-party lists, need provider-official confirmation before citing). Do not promote NTA/Starlink/VPS resellers into hyperscale presence.
- **Market size**: ~36,000-42,000 people; ~39,300 mobile connections; ~24,300 internet users (2025). International bandwidth ~ multiple Gbps on HANTRU-1. No MW-scale power available (diesel island grids). Any claim of a large datacenter build is almost certainly wrong; check for a power/landing-station primary before believing it.
- **Kwajalein special case**: the US Army's Reagan Test Site (Kwajalein island) operates major military IT (range C2, telemetry, DISA-type networking, Army-funded HANTRU-1). This is restricted infrastructure; publicly enumerable only as context (Grade B/C via Army/contract/trade sources). Contractors (e.g., Leidos-type base ops firms) appear in US federal procurement (SAM.gov) for Kwajalein IT/network services - useful for Kwajalein-division leads.
- **Marshallese flag-of-convenience registry** (Trust Company of the Marshall Islands; ~2nd largest ship registry) is a maritime/financial industry, NOT an IT datacenter signal - ignore "Marshall Islands registry" search noise and clarify intent when searching (use country name + IT terms, not registry terms).

---

## 1. Key industry players and their official pages

### 1.1 NTA - the only real facility owner/operator

- **Official site**: https://www.nta.mh/ ; contact page: https://www.nta.mh/contact-us/ (Majuro: `NTA, 1169, Main Street, Delap`; Ebeye: `NTA, 5025 Main Street`). NTA sells consumer/business broadband, mobile, phone, TV, IP PBX, and related services; no public colo product page was found - treat any NTA hosting as internal/telecom unless a primary service page says otherwise.
- **Facility evidence**: ICANN L-root node at NTA Majuro (https://www.icann.org/en/announcements/details/marshall-islands-national-telecommunications-authority-contributes-to-responsive-and-resilient-internet-with-l-root-instance-in-marshall-islands-6-3-2017-en, Grade A). This is a direct datacenter-colocation statement, not merely an inference. HANTRU-1 landing stations: Majuro + Kwajalein/Ebeye (Grade A via FCC public notice https://docs.fcc.gov/public/attachments/DA-09-1309A1.pdf for Kwajalein/Reagan Test Site station and cable capacity; Grade B/A via TeleGeography https://www.submarinecablemap.com/submarine-cable/hantru1-cable-system for map landing list).
- **Status/ops channel**: NTA Facebook https://www.facebook.com/mhnta (outages: 2017 cable fault 3-week national outage; 2022 five-day nationwide disruption; 2023 Ebeye voice outage; CTE upgrades 2021-2023).
- **CEO signal**: Dr. Yukiko Muller, President & CEO (quoted in IOKWE announcement) - search her name + NTA for announcements.

### 1.2 Satellite vendors (connectivity, not DCs - but they anchor outer-atoll "sites")

| Vendor | MH role | Official page / signal | DC relevance |
|---|---|---|---|
| SpaceX Starlink | Confirmed local launch 2025-06-10; official support lists kit shipping to Majuro, Ebeye, and Kwajalein Island | https://www.starlink.com/ (support/availability article); World Bank P171517 restructuring PDF | None - do not count as DC; useful as demand/competitive signal |
| Intelsat | GEO backhaul; 60 small-cell base stations plus satellite hub/equipment across outer islands; future 3G/4G phases | https://www.broadbandcommission.org/insight/intelsat-connectivity-transforming-lives-and-livelihoods-in-the-marshall-islands/ | None - but names the network type to look for in outer-atoll telecom evidence |
| SES (O3b mPOWER) | Potential enterprise/backhaul; no confirmed RMI terminals as of pass | https://www.ses.com/ | None until terminals confirmed |
| OneWeb | Potential enterprise/government LEO; no confirmed RMI deployment | https://oneweb.net/ | None until confirmed |

### 1.3 Google / Pacific Connect (future landing-station infrastructure)

- **Halaihai cable** (Google Pacific Connect; Guam-French Polynesia): Google official infrastructure blog https://cloud.google.com/blog/products/infrastructure/introducing-bulikula-and-halaihai-subsea-cables-to-connect-the-central-pacific (A for Google system existence; not a MH landing by itself).
- **IOKWE branch** (NTA; Majuro + Ebeye landings): https://www.submarinenetworks.com/en/systems/trans-pacific/iokwe (B), https://www.datacenterdynamics.com/en/news/marshall-islands-to-connect-to-googles-halaihai-subsea-cable/ (B), https://cablestatus.com/cables/iokwe (C aggregate - treat RFS dates carefully), GeoCables https://geocables.com/cable/iokwe (C)
- **Central Pacific Cable** (Guam-American Samoa feasibility; RMI included in route list): https://www.ustda.gov/ustda-advances-secure-internet-connectivity-in-the-pacific-islands/ (A)
- Google Cloud official regions (absence check): https://cloud.google.com/about/locations - no MH region. Google's MH footprint = cable, not compute.

### 1.4 Hyperscaler/CDN official absence checks (industry angle)

| Provider | Official page to check | MH status |
|---|---|---|
| AWS | Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; CloudFront edge locations: https://aws.amazon.com/cloudfront/features/ | No MH region/local zone; CloudFront Majuro POP unverified in this pass (provider-official confirmation required) |
| Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No region |
| GCP | https://cloud.google.com/about/locations | No region |
| OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No region |
| Akamai/Cloudflare | https://www.cloudflare.com/network/ ; Akamai edge map | No confirmed MH PoP in this pass - verify before citing |

### 1.5 Local IT / enterprise server-room players (Grade C unless primary evidence)

- **Pacific International Inc. (PII)** - Majuro IT services firm (referenced in local tech-ecosystem listings); verify via LinkedIn/company site before recording any facility.
- **Majuro Digital Solutions** - local IT/development shop; same verification rule.
- **Bank of Marshall Islands (BOMI)** - national bank; core-banking server room in Majuro (plausible but unverified; query BOMI annual reports / RMI Financial Institutions Commission).
- **College of the Marshall Islands (CMI)** - campus network/server room in Majuro (query CMI IT pages).
- **Marshall Islands Development Bank / RMI Social Security** - server rooms, unverified.
- General rule: enterprise server rooms are NOT datacenters for this pipeline unless a primary source describes a dedicated facility with power/racks; otherwise record as Grade C leads only, or skip with no_projects.

### 1.6 Kwajalein military-industrial IT (context only)

- US Army Kwajalein Atoll (USAKA): https://www.army.mil/kwajalein/ ; Reagan Test Site: https://www.ll.mit.edu/about/facilities/reagan-test-site ; range C2 with Huntsville AL (MIT Lincoln Laboratory description).
- Federal procurement leads: search SAM.gov / USAspending for Kwajalein IT/network/data-center service contracts (e.g., base operations support contractors) - Grade B/C; military server rooms not enumerable publicly.
- HANTRU-1 is Army/Reagan Test Site-linked infrastructure; FCC public notice says the Kwajalein cable station was to be owned and operated by USAKA/Reagan Test Site. The Kwajalein landing is a real telecom facility but should not be expanded into a public datacenter record.

---

## 2. Trade press and directories

High-value trade press (Grade B, fact-bearing):
- **Data Center Dynamics (DCD)**: https://www.datacenterdynamics.com/ - search `site:datacenterdynamics.com "Marshall Islands"` (IOKWE/Halaihai coverage 2026).
- **Submarine Networks**: https://www.submarinenetworks.com/ - `site:submarinenetworks.com IOKWE OR "Marshall Islands"` (system pages list landings, ownership, RFS).
- **Subsea Cables News / SSCC Samoa / cablestatus / GeoCables**: aggregate cable trackers - Grade C for facts, useful for landing-station cross-check.
- **telecoms.com, Reuters, Pacific Island Times, RNZ Pacific**: regional telecom/cable policy coverage (e.g., East Micronesia Cable, CPC funding).
- **Marshall Islands Journal** (marshallislandsjournal.com): local paper of record - NTA reform (Bill 66), outages, Digital Republic coverage; Grade B for named local facts.
- **Marshall Islands Government / rmigov.com**: national announcements (Digital Republic, IOKWE) - Grade A when directly sourced.

Directories (Grade C only - MH almost always absent; absence is a weak negative signal, not proof):
```
site:datacentermap.com Marshall Islands OR Majuro
site:datacenters.com Marshall Islands OR Majuro
site:cloudscene.com Majuro
site:atalnetworks.com Majuro  <- reseller marketing page; ignore as facility evidence
```

Search templates (industry angle):
```
"Marshall Islands" ("data center" OR datacenter OR colocation OR "server hosting") -registry
"Majuro" ("data center" OR "server" OR hosting OR colocation)
"Ebeye" ("data center" OR "server" OR telecom)
"NTA" ("landing station" OR "earth station" OR "L-root" OR "data center") Marshall Islands
"IOKWE" OR "Halaihai" OR "Central Pacific Cable" Marshall Islands
site:datacenterdynamics.com "Marshall Islands"
site:submarinenetworks.com IOKWE
"Kwajalein" ("data center" OR "network operations" OR "IT services") Army contract
"Starlink" "Marshall Islands" availability
```

---

## 3. Per-division industry enumeration

Divisions: Majuro, Kwajalein, Ailinglaplap, Ailuk, Arno, Aur, Ebon, Enewetak & Ujelang, Jabat, Jaluit, Bikini & Kili, Lae, Lib, Likiep, Maloelap, Mejit, Mili, Namdrik, Namu, Rongelap, Ujae, Utrik, Wotho, Wotje.

| Division | Expected industry findings | Vendor route |
|---|---|---|
| Majuro | NTA Majuro landing station + L-root + earth station; government/bank server rooms; IOKWE Majuro landing (planned) | NTA site/Facebook, ICANN, TeleGeography, DCD/Submarine Networks (IOKWE), World Bank P171517 |
| Kwajalein | NTA Ebeye landing station; US Army Reagan Test Site IT (restricted); IOKWE Ebeye landing (planned); KAJUR power | TeleGeography landing list, USAKA/army.mil, SAM.gov contracts, DCD |
| Jaluit | Satellite-fed telecom site only | Intelsat blog, NTA service notices |
| Enewetak & Ujelang / Bikini & Kili / Rongelap / Utrik / Wotje | Intelsat 2G small-cell sites; no DC | Intelsat blog (names atolls) |
| Remaining 15 atolls | Intelsat/NTA satellite sites, school connectivity; no DC expected | Intelsat blog, donor news |

Practical notes:
- For each division, one sweep of the generic industry template + the vendor-route source is sufficient; MH is tiny - do not over-search. Log `no_projects: true` for divisions without facility evidence.
- Cross-check cable landing claims against FCC/USG filings and TeleGeography (https://www.submarinecablemap.com/submarine-cable/hantru1-cable-system) - it lists HANTRU-1 landing stations at Majuro and Kwajalein; IOKWE is listed as planned by trackers/trade sites (treat RFS dates from trackers as Grade C unless NTA/USG/Google confirms).
- Satellite-vendor "deployments" (Starlink dishes, Intelsat small cells) are connectivity assets, not datacenter capacity - keep them out of the DC registry or mark clearly as telecom infrastructure.

---

## 4. Pitfalls and grading (industry angle)

- **Pitfall 1 - registry noise**: Marshall Islands' ship registry is a major offshore industry; searches mixing "Marshall Islands registry" with IT terms return maritime junk. Add `-registry` or scope to `Majuro/Ebeye/NTA/cable`.
- **Pitfall 2 - reseller marketing as facilities**: pages like atalnetworks.com "Majuro dedicated servers" are offshore-reseller marketing with no physical MH facility; ignore as facility evidence (Grade C/ignore).
- **Pitfall 3 - satellite = DC**: Starlink availability (2025), Intelsat cell sites, and NTA retail internet are connectivity, not datacenters.
- **Pitfall 4 - hyperscale misattribution**: Google's Halaihai/IOKWE is a cable project; no Google Cloud region in MH. AWS CloudFront Majuro POP unverified - do not cite until the official AWS edge-locations list confirms it.
- **Pitfall 5 - military double-counting**: Kwajalein base IT is real but non-public; record only context. HANTRU-1 is one cable with two MH landings - one system, two stations.
- **Grading**: A = vendor/official page (NTA, ICANN, FCC, USTDA, Army, Google cloud/cable official pages, cloud-provider official region pages), B = DCD/Submarine Networks/APNIC/Reuters/MIJ/PIT/RNZ, C = cable trackers (cablestatus, GeoCables, SSCC), directories, reseller pages.

---

## 5. Key sources quick list (industry angle)

- NTA: https://www.nta.mh/ ; contact/addresses: https://www.nta.mh/contact-us/ ; Facebook: https://www.facebook.com/mhnta
- ICANN L-root (Majuro): https://www.icann.org/en/announcements/details/marshall-islands-national-telecommunications-authority-contributes-to-responsive-and-resilient-internet-with-l-root-instance-in-marshall-islands-6-3-2017-en
- HANTRU-1: FCC public notice https://docs.fcc.gov/public/attachments/DA-09-1309A1.pdf ; TeleGeography map: https://www.submarinecablemap.com/submarine-cable/hantru1-cable-system ; APNIC outage context: https://blog.apnic.net/2019/04/22/when-the-internet-goes-out-a-marshall-islands-perspective/
- IOKWE: https://www.submarinenetworks.com/en/systems/trans-pacific/iokwe ; DCD: https://www.datacenterdynamics.com/en/news/marshall-islands-to-connect-to-googles-halaihai-subsea-cable/
- USTDA Pacific Connect: https://www.ustda.gov/ustda-advances-secure-internet-connectivity-in-the-pacific-islands/
- Starlink availability: https://www.starlink.com/ (search "Marshall Islands"); World Bank restructuring PDF confirms local service launch on 2025-06-10: https://documents1.worldbank.org/curated/en/099072125040537245/pdf/P171517-dd075251-efe4-410b-9bce-2adf01d17e00.pdf
- Intelsat/Broadband Commission outer-island program: https://www.broadbandcommission.org/insight/intelsat-connectivity-transforming-lives-and-livelihoods-in-the-marshall-islands/
- US Army Kwajalein: https://www.army.mil/kwajalein/ ; Reagan Test Site: https://www.ll.mit.edu/about/facilities/reagan-test-site
- Marshall Islands Journal: https://marshallislandsjournal.com/ ; RMI Gov: https://rmigov.com/

Finalized 2026-08-12 after source verification. Re-run official cloud/cable/operator pages before any future enumeration refresh.
