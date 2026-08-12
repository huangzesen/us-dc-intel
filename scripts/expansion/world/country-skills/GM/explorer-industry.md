# GM Explorer Industry - Gambia Datacenter Enumeration via Operators, Colo, Telco, IXP, Vendors, and Trade Press

Layer: **FINAL**. Date: 2026-08-12. Country: **GM - The Gambia**. Division model from `world-manifest.jsonl`: **6 city/divisions**: Banjul; Lower River; Central River; North Bank; Upper River; Western. Angle: **industry/operator-first discovery**, reconciled against official records.

Reliability grades are field-level:
- **A** = operator-owned page, government/regulator page, GPPA/MOCDE/GICTA/NAWEC/PURA record, official cloud-region page, signed government/operator announcement for the exact field.
- **B** = strong named secondary/trade source: The Standard, The Point, Foroyaa, GRTS, GambiaJ, Biometric Update, ITWeb Africa, Developing Telecoms, Connecting Africa, Capacity, Techpoint Africa, DCD, vendor case study, Cloudflare/Internet Society analysis, PeeringDB/IXP records for network presence.
- **C** = lead only: directory entry, social post, generic market report, unsupported capacity/address, aggregator/AI content, regional expansion article with no Gambia site.

Use B/C sources to find candidates, then promote only fields confirmed by A-grade sources. A facility can have A-grade operator existence, B-grade inauguration date, and C-grade address or capacity until each field is independently verified.

---

## 0. Market Structure

The Gambia is a very small, early-stage, **Greater Banjul Area-centred** datacenter market. Honest market picture as of 2026-08-12:

- **One flagship sovereign facility lead**: strong press/vendor reporting says the **Gambia National Data Centre at Abuko, Western division** was inaugurated with NIMS on 2026-07-01 by President Barrow and implemented with **Margins ID Group**. Grade **B** for facility/inauguration until a GICTA/MOCDE/State House source is opened. Grade `ISO-certified` only as **B/C** unless certification evidence is found.
- **State telco colo service**: **GAMTEL** officially sells co-location/facility rental for telecom hardware or servers at its premises/infrastructure and says customers can colocate in any of its **43 sites or towers countrywide**. Grade **A** for the product. Do **not** count 43 datacenters; named sites need site-level proof.
- **Public-sector pipeline**: **WARDIP/DTFA P176932** has official MOCDE/World Bank evidence for second-cable, landing-station, and data-centre/GAMTEL-facility works. Grade **A** for program scope; per-site status remains `planned` or `lead only` until tenders, awards, permits, or operator construction notices identify a facility.
- **No verified commercial open-colo major** was found for Equinix, Digital Realty, Raxio, OADC, Wingu, Liquid, Paratus, Africa Data Centres, Teraco, NTT, or similar. Keep any such Gambia claim at **C** unless an operator page or official record appears.
- **No hyperscale public cloud region** in The Gambia was found on official AWS, Azure, Google Cloud, Oracle OCI, or Huawei Cloud region pages/searches.
- **Connectivity**: ACE lands in/near Banjul and GAMTEL is the national fixed-line infrastructure anchor. SIXP/Serekunda IXP is the domestic exchange point and a strong network clue, not datacenter proof.
- **Power**: NAWEC power reliability, backup generation, fuel, UPS, and solar/captive arrangements are decisive fields. Do not accept `operational` at face value without power notes.

Expected honest yield: **1-3 countable or near-countable facilities**: Abuko National Data Centre; a GAMTEL named exchange/colo if official site evidence is found; WARDIP landing-station/data-centre works when site-level procurement/construction appears. Lower River, Central River, North Bank, and Upper River will usually be `no confirmed facility found`.

---

## 1. Operator and Facility Seed List

| Operator / platform | URLs | Gambia signal | Likely locations | Grade discipline |
|---|---|---|---|---|
| **GICTA / Gambia National Data Centre / NIMS** | https://gambia.gov.gm/gambia-ict-agency/ ; https://gicta.gov.gm/ ; https://standard.gm/barrow-inaugurates-national-data-centre-digital-identity-system/ ; https://www.biometricupdate.com/202607/the-gambia-launches-sovereign-digital-id-system-built-by-margins-id-group | Press/vendor reports of National Data Centre inauguration with NIMS | Abuko, Western | B for facility/inauguration until official confirmation; A only for fields on government/GICTA/MOCDE pages |
| **GAMTEL** | https://gamtel.gm/ ; https://gamtel.gm/co-location-facility-rental-services/ ; https://gamtel.gm/about-us/ | National fixed operator; official co-location/facility rental service across premises/infrastructure and 43 sites/towers | Banjul HQ; Western exchanges/towers; national tower/site footprint | A for service offering; C for named site details unless GAMTEL/PURA/council records confirm |
| **WARDIP / DTFA P176932** | https://mocde.gov.gm/wardip/ ; https://mocde.gov.gm/wp-content/uploads/2023/11/Environment-and-Social-Management-Framework-ESMF-%E2%80%93-WARDIP-P176932-The-Gambia.pdf ; https://gambia.gov.gm/tenders/ ; https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099061825055573661 | Second cable, landing station, data infrastructure and data-centre/GAMTEL facility works | Landing station likely Banjul/GBA; upgrades may be national | A for program scope; per-facility evidence required |
| **Margins ID Group** | https://www.biometricupdate.com/202607/the-gambia-launches-sovereign-digital-id-system-built-by-margins-id-group | NIMS/sovereign digital ID implementation partner; claims around sovereign infrastructure | Abuko | B for vendor/press fields; promote only if government contract/announcement is opened |
| **SIXP / Serekunda Internet Exchange** | https://www.peeringdb.com/ix/2682 ; https://www.afpif.org/wp-content/uploads/2017/10/Gambia-IXP-Experience-.pdf | Domestic IXP/network concentration | Serekunda, Western | B for IXP/network presence; not a DC |
| **PeeringDB Kairaba Exchange facility lead** | https://www.peeringdb.com/fac/2287 | Directory/network facility entry for Kairaba Exchange | Serekunda/Kanifing, Western | C/B lead; confirm with GAMTEL/PURA/council before counting |
| **Gamcel, Africell, QCell, Comium** | PURA MNO page: https://pura.gm/ict/sub-sectors/mobile-network-operators/ | Mobile operators with core/DR infrastructure needs | GBA and national | A for operator existence; C for facility specifics |
| **Licensed ISPs** | PURA ISP page: https://pura.gm/ict/sub-sectors/internet-service-providers/ | ISPs may provide domain registration/web hosting and business internet | Mostly GBA | A for market structure; C for facility claims until operator pages name sites |
| **Hyperscale/cloud/colo majors** | Official portfolio/region pages | No verified Gambia facility found | Watch GBA only | C until official Gambia source appears |

Operator queries:
```text
"{operator}" Gambia "data centre" OR "data center" OR "colocation" OR "co-location"
"{operator}" Gambia "Tier" OR "ISO" OR "certified"
"{operator}" Gambia "MW" OR "racks" OR "cabinets" OR "servers"
"{operator}" Gambia "cloud" OR "hosting" OR "disaster recovery"
"GICTA" OR "GAMTEL" OR "Margins" "data centre" Gambia
"{operator}" "PURA" OR "GPPA" OR "NAWEC" Gambia
"{operator}" "Banjul" OR "Serekunda" OR "Abuko" "data centre"
```

---

## 2. Trade Press and Industry Media

Use trade press for discovery, dates, partners, and capacity leads. Reconcile against government/operator pages before upgrading.

High-yield sources:
- The Standard, National Data Centre/NIMS inauguration: https://standard.gm/barrow-inaugurates-national-data-centre-digital-identity-system/
- Biometric Update, NIMS/Margins ID: https://www.biometricupdate.com/202607/the-gambia-launches-sovereign-digital-id-system-built-by-margins-id-group
- Biometric Update, data protection bill: https://www.biometricupdate.com/202510/the-gambia-strengthens-digital-trust-with-personal-data-protection-privacy-bill
- National Assembly bill tracker for official current status: https://assembly.gm/bills
- The Point, GAMTEL/privatisation and historical infrastructure context: https://thepoint.gm/
- Cloudflare and Internet Society outage analyses for ACE resilience context: https://blog.cloudflare.com/the-gambia-without-internet/ ; https://pulse.internetsociety.org/blog/the-gambias-internet-outage-through-an-internet-resilience-lens
- Techpoint Africa, WARDIP/subsea-cable context: https://techpoint.africa/
- Developing Telecoms, regional WARDIP context: https://developingtelecoms.com/

Press queries:
```text
site:standard.gm Gambia "data centre" OR "data center" OR GICTA OR WARDIP OR NIMS
site:thepoint.gm Gambia "data centre" OR "data center" OR GAMTEL OR GICTA OR WARDIP
site:foroyaa.net Gambia "data centre" OR "digital"
site:biometricupdate.com Gambia "data centre" OR NIMS OR "digital ID"
site:developingtelecoms.com Gambia "data centre" OR "submarine cable"
site:techpoint.africa Gambia "subsea cable" OR "data centre"
site:datacenterdynamics.com Gambia
"Gambia" "first data centre" OR "national data centre" OR "new data centre"
"Gambia" "tier III" OR "tier 3" OR "ISO certified" "data"
```

---

## 3. Network, Peering, CDN, and Directory Evidence

Network evidence identifies likely facilities; it rarely proves a datacenter by itself.

- **SIXP**: use PeeringDB and AfPIF for IXP status, ASN/member clues, and Serekunda location.
- **Kairaba Exchange**: PeeringDB/datacenter directories are leads for a GAMTEL exchange/colo site. Promote only after GAMTEL, PURA, GPPA, NAWEC, or council evidence confirms the facility.
- **Directories**: datacentermap, colo.exchange, inflect, datacenters.com, and similar sites are C unless they link to operator-owned evidence.
- **CDN/cache clues**: Google Global Cache, Meta, Akamai, Netflix OCA, Cloudflare, or similar caches show network/edge deployment only. Count a DC only if the hosting facility is named and corroborated.
- **ACE/landing station**: connectivity and resilience evidence, not a commercial datacenter by itself.

Queries:
```text
"SIXP" OR "Serekunda Internet Exchange" members OR peers Gambia
site:peeringdb.com Gambia OR Serekunda OR Banjul
"Kairaba Exchange" Serekunda colocation
"Google Global Cache" OR "Akamai" OR "Netflix OCA" OR "Meta CDN" Gambia
"ACE cable" Gambia "landing station" Banjul
"Gambia" "internet exchange" OR "IXP" 2024 OR 2025 OR 2026
```

Extract: ASN, network name, IXP/facility status, address/town/division, source date, evidence type (`facility`, `network`, `cache-only`, `directory lead`), grade.

---

## 4. Enterprise, Financial, Government, and Vendor Leads

These reveal demand and private server rooms more often than public colo supply.

- Government/sovereign: GICTA, MOCDE, Ministry of Interior, NIMS, GRA, SSFA, National Assembly, health/education systems, WARDIP/GPPA tenders.
- Financial sector: Central Bank of The Gambia, Trust Bank, GTBank, Access Bank, Ecobank, mobile money and fintech operators. DR/server-room references are C unless site details are public.
- Telecoms/ISPs: GAMTEL/Gamcel, Africell, QCell, Comium, QuantumNet, Netpage, Airtip, GamNet. Count only explicit hosting/DC products or named facilities.
- Vendors/integrators: Margins ID Group, Huawei, Presight, SYSROAD and other network integrators. Network upgrades are not DCs unless the source says data centre/facility.
- Universities/research: University of The Gambia and colleges may have server rooms; count only public facility evidence.

Queries:
```text
"Central Bank of The Gambia" "data centre" OR "disaster recovery" OR "server room"
"{bank}" Gambia "data centre" OR "DR site" OR "business continuity"
"GRA" OR "SSFA" OR "National Assembly" Gambia "data centre" OR "server"
"{vendor}" Gambia "data centre" OR "digital government"
"Gambia" "cloud" OR "hosting" "{bank}" OR "fintech"
"UTG" OR "University of The Gambia" "server" OR "data centre"
"SYSROAD" OR "Huawei" OR "Presight" Gambia "data" OR "ICT infrastructure"
```

---

## 5. Associations and Events

- PURA-licensed operator community: use PURA for official operator lists and service classes.
- Gambia Chamber of Commerce and Industry and local digital-economy events: useful for leads, normally B/C.
- AfPIF: useful for SIXP and peering history.
- Africa Tech Festival/AfricaCom and vendor events: announcements are B until operator or government pages confirm.
- AU/PIDA and World Bank project pages: useful for official regional-program context; per-site facility claims still need Gambia site evidence.

Queries:
```text
"Gambia" "GCCI" OR "chamber of commerce" "data centre" OR "digital"
"AfPIF" Gambia IXP OR peering
"AfricaCom" OR "Africa Tech Festival" GAMTEL Gambia "data centre" OR "cloud"
"PIDA" Gambia IXP OR digital infrastructure
"Gambia" "digital economy" summit OR conference "data centre"
```

---

## 6. Per-Division Industry Strategy

| Division | Capital / core towns | Industry anchors | Strategy and expected yield |
|---|---|---|---|
| **Banjul** | Banjul | GAMTEL HQ; ACE/landing-station evidence; ministries; banks; GPPA | **Medium-low.** Query GAMTEL HQ, ACE landing-station works, ministries/banks, GPPA/WARDIP. Do not count HQ/server-room references without facility evidence. |
| **Western** | Serekunda, Kanifing, Abuko, Bakau, Brikama, Yundum | National Data Centre Abuko; GAMTEL/Kairaba leads; SIXP; ISPs; PURA; NAWEC; GIEPA; airport/industrial corridor | **Primary cluster.** Start with NDC/NIMS, then GAMTEL colo, SIXP/PeeringDB, PURA/GPPA/NAWEC/council checks. Expected 1-3 countable or near-countable facilities plus leads. |
| **Lower River** | Mansakonko | Telco/backbone nodes; area council; public-service ICT | **Very low watch.** Search Mansakonko for government ICT rooms and telco nodes; record `no confirmed facility found` if no evidence. |
| **Central River** | Janjanbureh, Kuntaur | Telco/backbone nodes; area councils; public-service ICT | **Very low watch.** Search Janjanbureh/Kuntaur for e-government/telco facilities; count unlikely. |
| **North Bank** | Kerewan | Telco/backbone nodes; ferry/corridor systems; area council | **Very low watch.** Search Kerewan/corridor for telco or DR nodes; count only named facilities. |
| **Upper River** | Basse Santa Su | Telco/backbone nodes; border/trade systems; area council | **Very low watch.** Search Basse for government ICT, border systems, and telco nodes; count unlikely. |

Division query block:
```text
"{capital}" "data centre" OR "data center" OR "server room" OR "hosting" Gambia
"{division}" "cloud" OR "ICT" OR "digital" Gambia
"{capital}" "GAMTEL" OR "GICTA" OR "WARDIP" OR "QuantumNet" OR "Netpage"
"{division}" "disaster recovery" OR "business continuity" Gambia
"{capital}" "substation" OR "generator" "data" Gambia
site:standard.gm "{division}" "ICT" OR "digital"
site:thepoint.gm "{division}" "ICT" OR "digital"
"{division}" "NBN" OR "fiber" Gambia
```

---

## 7. Confirmation Workflow

1. Seed from operator/government pages: GICTA/government directory, GAMTEL, MOCDE/WARDIP/G-Cloud/Open Data PDFs, GPPA/government tenders, PURA, NAWEC, World Bank.
2. Use press and trade sources to identify dates, partners, and capacity leads; keep them B until official/operator confirmation.
3. Use directories and PeeringDB only for leads; keep facility details C unless reconciled.
4. Cross-check every candidate with at least two of: operator page, PURA licence, GPPA tender/award, NAWEC power record, GICTA/MOCDE document, council record, World Bank/MOCDE project document.
5. Run all six divisions and explicitly record `no confirmed facility found` for divisions with no hits.
6. Store field-level grades and exact source wording. Never upgrade `inaugurated` to A without an official page; never upgrade `ISO-certified` without certification evidence; never count GAMTEL's 43-site offering as 43 datacenters.

Master query bank:
```text
"Gambia" "national data centre" OR "data center" Abuko OR GICTA
"Gambia National Data Centre" NIMS Margins ISO
"GAMTEL" "co-location" OR "colocation" Gambia
"Kairaba Exchange" Serekunda
"WARDIP" Gambia "data centre" OR "landing station"
"SIXP" OR "Serekunda Internet Exchange" Gambia
"ACE" "Gambia" "landing" Banjul
"Gambia" "data centre" "Banjul" OR "Serekunda" OR "Abuko"
"Gambia" "data center" "MW"
"{operator}" "PURA" OR "GPPA" OR "NAWEC" Gambia
```

---

## 8. Source Notes From This Review

Verified or usable A-grade surfaces include MOCDE WARDIP/G-Cloud/Open Data PDFs, MOCDE WARDIP page, government directory/GICTA page, PURA ICT pages, GAMTEL co-location page, GPPA/government tenders, GIEPA media/resources page, National Assembly bill tracker, World Bank WARDIP project pages, and official cloud-provider region pages.

Honest downgrades: Abuko National Data Centre is **B** until an official facility/inauguration page is opened; `ISO-certified` is not A without certification evidence; GAMTEL's 43-site colocation language is an A-grade service claim but not 43 datacenters; Kairaba Exchange is a C/B network/directory lead until operator or official site evidence confirms it; WARDIP is A-grade program scope but per-site works are not countable without site-level evidence; telco/ISP core sites and private DR rooms are leads; hyperscale Gambia region claims are false unless official provider pages change.
