# BN Explorer Industry - Brunei Darussalam Datacentre Enumeration via Operators, Trade Press, Directories, IXP/Subsea and Locality Query Patterns

Date: 2026-08-12. Country: **BN Brunei Darussalam**. Scope: all **4 districts**: Brunei-Muara, Belait, Tutong, Temburong. Angle: operator, trade-press, directory, IXP, cable and locality-led discovery. Use `explorer-official.md` to promote or reject every industry lead.

Reliability grades: **A** = operator official page, public-sector page, regulator/permit source, stock-exchange/company filing, or Uptime Institute registry; **B** = reputable trade/local press with named parties and concrete facts; **C** = directory/marketplace/SEO hosting page/partner listing; **U** = unverified. Grade each field independently.

---

## 0. Market Shape

Brunei is a **tiny, state-led datacenter market** with almost all activity in **Brunei-Muara** district. Since the 2019-2020 consolidation, **Unified National Networks (UNN)** owns the national telecom infrastructure, cable landing stations and the country's main datacenter capacity; DST, imagine (ex-TelBru), Progresif and BIG sell services on top of it. The government operates its own shared-services data centres through **EGNC** (Gadong). Tutong hosts the Telisai cable landing station and NiAT's Telisai satellite earth station (infrastructure anchors only). Belait and Temburong have **no confirmed commercial datacenters** - record negative sweeps.

Confirmed or high-confidence public leads as of 2026-08-12: UNN Tungku Prefab Data Centre / `BRUDC4` (200-rack phase 1, Vertiv, at Tungku Submarine Cable Landing Station); UNN `BRUDC2 Sumbiling Telhouse DC`; UNN `BRUDC3 Tungku DC` / Tungku Zone 8; UNN colocation/cloud hosting services (operator ISO 27001 claim, Tier 3 compliance claim); EGNC government/private data centre colocation (Gadong); DST colocation service and UNN-capacity resale (2025-12-02); BIG colocation/cloud marketing; Borneo-IX at Tungku; cable landing stations Tungku and Telisai; Tech Greencloud SME cloud center (directory-led).

**Honest yield expectation**: roughly **3-6 recordable project/facility rows countrywide**, nearly all in Brunei-Muara, plus 2 infrastructure anchors (Telisai CLS/earth station in Tutong) and 2 negative divisions (Belait, Temburong). Do not inflate; Brunei has no hyperscale or regional-hub datacenter market yet.

False-positive controls: local VPS/cloud/hosting marketing is not a datacenter; Borneo-IX, cable landing stations and satellite earth stations are not datacenters unless paired with documented colocation/DC rooms; `cloud` in Brunei marketing means a local hosted service, not a public cloud region; directory entries (DataCenterMap etc.) need operator confirmation; oil-and-gas "data centres" in Belait are internal server rooms unless explicitly offered as commercial colocation.

## 1. Search Vocabulary

```text
English: "data centre", "data center", datacentre, colocation, co-location, "server hosting", "dedicated servers", "cloud services", "disaster recovery", "Tier III", "ISO 27001", IXP, "internet exchange", "submarine cable", "landing station", "cable landing station", racks, MW, substation, generator, UPS
Malay: "pusat data", "pengehosan", "hosting", "kolokasi", "awan", "pengkomputeran awan", "pusat data kerajaan", "pejabat telefon" (telephone house/exchange), "stesen pendaratan kabel"
District/area variants: Brunei-Muara (Bandar Seri Begawan/BSB, Gadong, Berakas, Tungku, Jerudong, Kiulap, Anggerek Desa, Salambigar, Sumbiling, Kampong Ayer), Belait (Kuala Belait, Seria, Lumut, Panaga), Tutong (Tutong town, Telisai, Lamunin), Temburong (Bangar, Pekan Temburong)
Operator names to rotate: UNN, DST, Datastream Digital, imagine, TelBru, Telekom Brunei, Progresif, BIG, Brunei International Gateway, EGNC, NiAT, Tech Greencloud, Borneo-IX, Vertiv, Huawei, Ericsson, Nokia
Cable names: SMW3, SE-ME-WE3, AAG, SJC, LBC, Labuan-Brunei, ALC, Asia Link Cable
```

## 2. Priority Operator and Facility Leads

| Lead | Division | URLs | Evidence status |
|---|---|---|---|
| UNN Tungku Prefab Data Centre / `BRUDC4` | Brunei-Muara (Kg Tungku; Tungku Submarine Cable Landing Station) | UNN https://unn.com.bn/unn-invests-in-eco-efficient-data-centre-infrastructure-to-meet-bruneis-increasing-digital-needs ; colocation https://unn.com.bn/colocation-hosting ; cloud https://unn.com.bn/cloud-hosting ; Vertiv https://www.vertiv.com/en-asia/about/news-and-events/news-releases/bruneis-state-owned-unified-national-networks-selects-vertiv-prefabricated-data-centre-solutions-to-achieve-national-digitization-goals/ ; DCD https://www.datacenterdynamics.com/en/news/construction-begins-on-unn-data-center-in-brunei/ ; The Bruneian https://thebruneian.news/2023/08/04/unn-new-data-centre-in-tungku-to-begin-operation-early-2024/ | **A** for UNN-stated project/service facts (51,000 sq ft complex, 200-rack phase 1, construction Apr 2023, `BRUDC4 Tungku Prefab DC` listed on the live colocation page, cloud/colo marketed with ISO 27001 and 99.982% availability claims). **B** for DCD/Vertiv details (second power feed with Berakas Power Company; ALC connection; 10-month build; Tier IV electrical/Tier III mechanical design standards). No MW or Uptime registry certification found. |
| UNN Sumbiling Telephone House / `BRUDC2` | Brunei-Muara (BSB/Sumbiling area) | UNN https://unn.com.bn/colocation-hosting ; The Scoop https://thescoop.co/2025/12/03/dst-unn-expand-partnership-through-data-centre-agreement/ ; LinkedIn https://www.linkedin.com/pulse/dst-expands-strategic-partnership-unn-power-bruneis-qxzne | **A** for UNN listing `BRUDC2 Sumbiling Telhouse DC`; **B** for DST-UNN resale agreement naming Sumbiling Telephone House (2025-12-02). Street address, racks and MW **U**. |
| UNN Tungku DC / Tungku Zone 8 / `BRUDC3` | Brunei-Muara (Tungku complex) | UNN https://unn.com.bn/colocation-hosting ; The Scoop / LinkedIn DST sources | **A** for UNN listing `BRUDC3 Tungku DC`; **B** for "Tungku Zone 8" in the DST-UNN resale agreement. Exact relationship between BRUDC3, Zone 8, cable station and the prefab phase **U**. |
| UNN Colocation Hosting / Cloud Hosting (IaaS) | Brunei-Muara (operator service; facilities listed as BRUDC4/BRUDC2/BRUDC3) | https://unn.com.bn/colocation-hosting ; https://unn.com.bn/cloud-hosting ; UNN LinkedIn post (Tier 3 Uptime Certified Design, 7.5kW high-density racks, dual power, 99.982% uptime) | **A** for official UNN service claims, available DC names, rack product types (42U full rack, 20U half rack), ISO 27001 operator claim and hosted-in-Brunei claim; **C** for LinkedIn-only marketing specifics until mirrored on unn.com.bn or a certificate/technical sheet is captured. |
| EGNC government/private data centres / Data Centre Co-Location | Brunei-Muara (Gadong, Jalan E-Kerajaan, Simpang 69-18, BE1110) | https://www.egnc.gov.bn/ ; https://www.egnc.gov.bn/government-ict-infrastructure/ ; https://www.egnc.gov.bn/data_centre_co-location/ ; service catalogue https://www.egnc.gov.bn/wp-content/uploads/2026/03/Service-Catalogue.pdf ; DCD analysis https://www.datacenterdynamics.com/en/analysis/small-nation-big-vision-brunei-consolidates-its-way-to-digital-resilience/ | **A** for EGNC-stated data centre colocation, government/private service options, 42U APC racks, private suite/shared room options, N+1 UPS, FM-200, VESDA, CCTV, biometric/card access, standby generators and dual rack power sources. Size/MW **U**. |
| DST colocation / resale of UNN capacity | Brunei-Muara (service) | https://dst.com.bn/co-locations/ ; The Scoop (above) | **A** for DST-stated colocation hosting service; **A/B** for Dec-2025 resale of UNN Tungku Zone 8 + Sumbiling capacity. DST is asset-light post-2020; facility = UNN's. |
| BIG (Brunei International Gateway Sdn Bhd) | Brunei-Muara (BSB HQ) | LinkedIn https://www.linkedin.com/company/big-bn ; D&B https://www.dnb.com/business-directory/company-profiles.brunei_international_gateway_sdn_bhd.438d53f0a779da6de02a9e8bce01930c.html ; UNN history https://unn.com.bn/evolution-of-telecommunications | **B** for company existence/history and asset-consolidation context; legacy `www.big.com.bn` is listed by directories but did not resolve in this pass. Facility/service marketing facts **U** unless an archived or live BIG page is captured. |
| Tech Greencloud | Brunei-Muara (BSB, Zainuddin Complex, Spg 11 per DataCenterMap) | https://www.datacentermap.com/brunei/bandar-seri-begawan/tech-greencloud/ ; DCD analysis (SME cloud center) | **C** for directory address/listing; **B** for DCD description. Cloud-center service claims; facility specifics **U**. |
| imagine (ex-TelBru) | Brunei-Muara (nationwide) | https://imagine.com.bn/ ; https://imagine.com.bn/about-us/ | **A** for company/services existence; **U** for any datacenter/colo facility claims (none confirmed on official pages in this pass). Legacy TelBru DC/hosting claims need primary pages. |
| Progresif | Brunei-Muara (nationwide) | https://www.progresif.com/ (verify) | Mobile/consumer operator; no DC claims found in this pass - **U/negative** until evidence appears. |
| NiAT (satellite; Telisai Earth Station) | Tutong (Telisai) | https://niat.com.bn/ ; https://niat.com.bn/about-us/ ; contact https://niat.com.bn/?ae_global_templates=contact-us-telisai-earth-station | **A** for NiAT (est. 2010, AITI-licensed satellite provider) and earth-station address. Satellite infrastructure context, not a DC. |
| Hyperscaler presence (AWS/Azure/GCP/OCI) | None | Official region pages (see explorer-official.md Section 1) | **A negative check** as of 2026-08-12. |

## 3. Trade Press and Secondary Sources

| Source | URL | Brunei use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/tags/brunei/ | UNN DC construction, Brunei digital-infrastructure analysis (2026-01-16), ALC coverage. | B |
| The Scoop | https://thescoop.co/ | DST-UNN data centre agreement (2025-12-03), Borneo-IX launch (2021-02-09), policy news. | B |
| Borneo Bulletin | https://borneobulletin.com.bn/ | UNN Tungku DC groundbreaking coverage, government/tech news. | B |
| The Bruneian | https://thebruneian.news/ | UNN DC (2023-08-04), DST-UNN pact (2025-12-03), Digital Brunei 2030. | B |
| Biz Brunei | https://www.bizbrunei.com/ | Local business/economy/ICT. | B |
| BruDirect | https://brudirect.com/ | Local news briefs. | B |
| Everything Brunei | https://www.everythingbrunei.com/ | Mirrors of local press (UNN DC, DST-UNN). | B/C (mirror) |
| Vertiv (vendor) | https://www.vertiv.com/en-asia/about/news-and-events/news-releases/ | Vendor-stated UNN project facts. | B (vendor primary for its own work) |
| Submarine Networks | https://www.submarinenetworks.com/en/stations/asia/brunei | Landing stations Tungku/Telisai, cable systems. | B |
| SubTel Forum / Capacity Media / Telecompaper | https://subtelforum.com/ ; https://www.capacitymedia.com/ ; https://www.telecompaper.com/ | Subsea and telecom coverage incl. ALC. | B |
| 6Wresearch Brunei colocation market report | https://www.6wresearch.com/industry-report/brunei-data-center-colocation-market | Market sizing/marketing context only. | C |
| ResearchAndMarkets / BusinessWire (Brunei telecoms market reports) | https://www.businesswire.com/news/home/20200423005680/en/ | Historical market context (TelBru rebrand to imagine). | C/B |

Trade-query examples:
```text
site:datacenterdynamics.com/en/ Brunei ("data center" OR "data centre" OR UNN OR Tungku OR ALC)
site:thescoop.co ("data centre" OR "data center" OR UNN OR Borneo-IX OR DST OR Sumbiling)
site:borneobulletin.com.bn ("data centre" OR "pusat data" OR UNN OR Tungku)
site:thebruneian.news ("data centre" OR UNN OR "Digital Brunei" OR "sovereign cloud")
site:bizbrunei.com ("data centre" OR cloud OR UNN)
site:brudirect.com ("data centre" OR UNN OR telco)
"UNN" "Tungku" "data centre" "racks"
"Sumbiling Telephone House" "data centre" OR colocation
"Berakas Power" "data centre" OR "power feed" OR Tungku
"Asia Link Cable" Brunei "ready for service" OR RFS OR "go live"
```

## 4. Directories and Aggregators

Use directories to seed names and addresses, then confirm through operator/EGNC/UNN official pages, AITI, or reputable press. DataCenterMap listings are C-grade leads even when the address is plausible; UNN's own colocation page is now the better source for BRUDC facility names.

| Directory | URL | Brunei signal | Grade |
|---|---|---|---|
| DataCenterMap | https://www.datacentermap.com/brunei/ | UNN Tungku SCLS entry (address "Jalan Universiti, Tungku Submarine Cable Landing Station, BE2119, Jerudong"), Tech Greencloud (Zainuddin Complex, Spg 11), and other Brunei leads. Use only after checking UNN/EGNC/operator pages. | C |
| Datacenters.com | https://www.datacenters.com/locations/brunei | Facility/provider leads. | C |
| Inflect | https://inflect.com/datacenters/apac/brunei | Colocation leads. | C |
| Cloudscene | https://cloudscene.com/ | Interconnect/colo market pages. | C |
| OCOLO / ColocationM / UpStack | various | Marketplace/SEO pages. | C |
| Dun & Bradstreet / LinkedIn | https://www.dnb.com/ ; linkedin.com | Company existence/HQ facts for BIG, DST, UNN, EGNC. | B for company facts, C for facility claims |

Directory-query examples:
```text
site:datacentermap.com/brunei/ "{operator}" OR "data center"
site:datacenters.com "Brunei" "{operator}" "Data Center"
site:inflect.com/datacenters/apac/brunei "{operator}"
site:cloudscene.com "Brunei" "{operator}"
"Brunei" "data center" "colocation" "Tier"
```

## 5. IXP, Peering and Subsea Pipeline

- **Borneo-IX** (Brunei's first and only international internet exchange): located at the Tungku Cable Landing Station; partnership between UNN and DE-CIX ("DE-CIX in a box" / DE-CIX-as-a-Service). PeeringDB https://www.peeringdb.com/ix/3440 ; PCH https://www.pch.net/ixp/details/2342 (established 2021-02-04; Nokia 7750 SR; managed by UNN); DE-CIX press release https://www.de-cix.net/en/about-de-cix/media/press-releases/establishing-borneo-ix-a-new-interconnection-hub-for-southeast-asia-brunei-national-telecommunications-provider-unn-and-de-cix-form-strategic-partnership ; The Scoop https://thescoop.co/2021/02/09/brunei-launches-first-internet-exchange-point/ . Also check PeeringDB facility records for UNN Tungku and any DST/imagine facilities (`site:peeringdb.com Brunei`). IXP context, not a DC.
- **Cable landing stations**: Tungku (Brunei-Muara) and Telisai (Tutong). Submarine Networks lists Brunei landing sites and cable systems including Tungku Submarine Cable Station and Telisai Submarine Cable Station; TeleGeography is the current map cross-check. Treat RFS/retirement dates as cable-system facts requiring a current primary or specialist source before entering them as hard dates. CLS context is useful because Tungku is co-located with UNN/IXP infrastructure, but the CLS itself is not a DC row.
- **NiAT Telisai Earth Station** (Tutong): NiAT satellite teleport/earth station address on the Sultan Haji Hassanal Bolkiah Highway, Telisai, Tutong (https://niat.com.bn/?ae_global_templates=contact-us-telisai-earth-station). Satellite infrastructure, not a DC.

Cable/IXP queries:
```text
"Tungku" "cable landing" Brunei
"Telisai" "landing" Brunei SJC
"Asia Link Cable" Brunei UNN "Tungku"
"Borneo-IX" UNN DE-CIX
site:peeringdb.com Brunei UNN OR Borneo
"AAG" Brunei "Tungku" "data centre"
"Labuan-Brunei Cable" Brunei
```

## 6. Per-District Industry Sweep

| Division | Realistic expectation | Industry-first route | Current status (2026-08-12) |
|---|---|---|---|
| Brunei-Muara | Main cluster: UNN Tungku (`BRUDC4` prefab, `BRUDC3` Tungku DC, CLS + Borneo-IX), UNN Sumbiling Telephone House (`BRUDC2`), EGNC Gadong, DST colocation resale, BIG, Tech Greencloud, imagine/progresif service leads. Expect 3-6 recordable rows. | UNN official pages; DST co-locations page; EGNC pages/service catalogue; DataCenterMap/Datacenters.com; DCD/The Scoop/Borneo Bulletin/The Bruneian; then AITI/DES/BPC for verification. | Confirmed: UNN Tungku project + available colocation/cloud sites; Sumbiling and Tungku Zone 8 via DST resale; EGNC government/private DC colocation; DST colocation service; Borneo-IX. |
| Tutong | Telisai CLS (SJC) + NiAT Telisai Earth Station; no commercial DC. Record infrastructure anchors, no DC rows. | Submarine Networks/TeleGeography for Telisai; NiAT pages; local press; negative DC sweep. | Telisai CLS + NiAT earth station confirmed as infrastructure; no DC. |
| Belait | Negative for commercial DCs; oil/gas industry (BSP) runs internal enterprise IT; Lumut Cogen power station is energy context only. | Negative sweep: "pusat data" + Belait/Kuala Belait/Seria/Lumut/Panaga; check energy press. | Negative. |
| Temburong | Negative; no DC demand (exclave, protected rainforest). | Negative sweep: Temburong/Bangar + data centre terms. | Negative. |

## 7. Known Facilities and Evidence Status

| Seed | Division | Status | Best evidence | Grade now |
|---|---|---|---|---|
| UNN Tungku Prefab Data Centre / BRUDC4 | Brunei-Muara | Project announced 2023; listed on UNN live colocation page as available data centre; no MW/Uptime registry entry found | UNN official news/pages; Vertiv; DCD; The Bruneian | A for project/service claims and 200-rack phase-1 sizing; B for vendor/press details; U for MW/certification |
| UNN Sumbiling Telephone House / BRUDC2 | Brunei-Muara | Existing UNN colocation facility listed by UNN and named in DST resale deal | UNN colocation page; The Scoop/LinkedIn | A for UNN listing; B for DST resale context; U for street address/racks/MW |
| UNN Tungku DC / Tungku Zone 8 / BRUDC3 | Brunei-Muara | UNN listed facility; Zone 8 named in DST resale deal | UNN colocation page; The Scoop et al. | A for BRUDC3 name; B for Zone 8 name; U for exact site relationship/details |
| EGNC government/private data centres / colocation | Brunei-Muara (Gadong) | Operational shared-services and private co-location offerings | EGNC official pages and 2026 service catalogue; DCD analysis | A for existence/services/features; U for total size/MW |
| DST colocation service | Brunei-Muara | Operational service (reselling UNN capacity) | DST official; The Scoop | A for service; U for own facility |
| BIG services | Brunei-Muara | Legacy cable/company lead; no live official website resolved | LinkedIn; D&B; UNN history | B for history; U for facility/service claims |
| Tech Greencloud | Brunei-Muara (BSB) | SME cloud center | DataCenterMap; DCD analysis | C (address); B (DCD mention) |
| Borneo-IX | Brunei-Muara (Tungku) | Operational IXP since 2021-02-04 | UNN; DE-CIX; PeeringDB; PCH; The Scoop | A/B context |
| Tungku CLS (SMW3/AAG/LBC/ALC) | Brunei-Muara | Operational landing station; ALC pending RFS | UNN; Submarine Networks; TeleGeography; DCD | A/B infrastructure |
| Telisai CLS | Tutong | Operational landing-station lead, not a DC | Submarine Networks/TeleGeography | B infrastructure unless confirmed by current operator primary source |
| NiAT Telisai Earth Station | Tutong | Operational satellite earth station | NiAT official | A infrastructure |
| Level 3 Tungku CLS (historical) | Brunei-Muara | Historical commercial CLS + basic DC services; pre-UNN | DCD analysis; Data Center Journal | B historical |
| imagine (ex-TelBru) DC claims | Brunei-Muara | No confirmed own DC on official pages | imagine.com.bn | U/negative |
| Progresif DC | none | No claims found | - | U/negative |
| Public cloud region | none | No BN region | Provider official region pages | A negative check |
| Uptime certification | none | No registry entry found | Uptime Institute registry | A negative check |

## 8. Reliability and Promotion Rules

- Promote an industry lead to **A** only when operator, government, regulator, permit, land, procurement, listed-company filing, cloud-provider official page, or Uptime registry evidence supports the specific fact.
- Keep address, rack count, white space, MW, certification and operational status as separate fields with separate grades. No public MW figures exist for most BN facilities - do not invent them.
- Keep cable landing stations, Borneo-IX and the NiAT earth station in infrastructure tables unless they are physically part of a documented colocation/datacenter facility.
- Record negative searches: Belait and Temburong negatives matter for complete division coverage; the results schema wants `no_projects: true` rows there.
- Be honest about UNN Tungku DC status: project/claims (A), construction (2023), UNN live colocation listing (A), DST resale context (B), MW and formal Uptime certification (not verified).
- Use `evidence_date=2026-08-12` for this reviewed pass; refresh dates when rechecked.

## 9. Update Cadence

- **Monthly:** UNN news/services; DST; imagine; BIG; The Scoop; Borneo Bulletin; The Bruneian; Biz Brunei; BruDirect; DCD Brunei tag; Vertiv releases.
- **Quarterly:** AITI licences/guidelines; EGNC; MTIC/Digital Brunei; PeeringDB/PCH (Borneo-IX peers); Submarine Networks/TeleGeography (ALC status); Uptime registry; directories (DataCenterMap, Datacenters.com, Inflect, Cloudscene); cloud-provider region pages.
- **Semi-annual:** BDEB/InvestBrunei announcements; government procurement; data.gov.bn.
- **Event-driven:** ALC ready-for-service (Tungku), formal UNN Tungku DC launch, DST-UNN colocation milestones, Borneo-IX expansion, Digital Brunei 2030 implementation, any foreign-investment datacenter MOU, new cable landing or power-connection announcements.
