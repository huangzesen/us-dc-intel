# MW Explorer Industry - Malawi Datacenter Enumeration via Operators, Colo, Telco, IXP, and Trade Press

Date: 2026-08-12. Country: **MW Malawi**. Division model: **3 regions**: Central Region; Northern Region; Southern Region. Angle: **industry/operator-first discovery**, reconciled against official records.

Reliability grades are field-level:
- **A** = operator-owned page, official government/regulator page, council permit, MACRA/MERA/ESCOM/PPPC/DIGMAP/RBM record, official cloud-region page, signed government/operator announcement for the exact claim.
- **B** = strong named secondary/trade source: DCD, ITWeb Africa, Capacity, Developing Telecoms, Connecting Africa, Xinhua, Nyasa Times, The Nation, Maravi Post, Malawi Voice, MANA, vendor case study, PeeringDB/IXP pages for network presence.
- **C** = lead only: directory entry, social media, generic market report, AI-generated/aggregator content, unsupported capacity/address, academic concept paper, regional expansion article with no Malawi site.

Use B/C sources to find candidates, then promote only the specific fields that are confirmed by A-grade sources. A single facility can have A-grade operator existence, B-grade MW/rack data, and C-grade address until each field is independently verified. For Malawi, in practice **no source discloses MW capacity** - record `capacity_mw` as null unless an official figure appears.

---

## 0. Malawi Market Structure

Malawi is a small, early-stage, **two-pole datacenter market**: government/colo density in **Lilongwe (Central Region)** and telco/bank/backup density in **Blantyre (Southern Region)**. The Northern Region has no verified facility. The market is dominated by: (a) government data centres (Lilongwe primary + Blantyre backup) built under the World Bank-funded DIGMAP project and the 2022 Huawei national facility; (b) telco/enterprise facilities (TNM, Airtel Malawi, MTL) that are mostly closed or internal; and (c) a thin layer of commercial colo/cloud (OCL in Kanengo, Lilongwe; MTL; plus new AI-flavoured announcements: CTN micro data centre and Korena/1nga's claimed Blantyre campus).

Verified industry-grade seeds (from this review and the prior batch-480 exploration):
- **Government Data Centre, Lilongwe** - primary national DC under PPPC/DIGMAP (World Bank); completion implied by Jun 2025 World Bank brief; no MW. Grade A for existence (digmap.pppc.mw; worldbank.org).
- **National Data Centre, Blantyre** - Huawei-built, commissioned 21-22 Jul 2022 by President Chakwera; hosts government-wide systems; secondary/backup role. Grade A for launch (Xinhua; gov statements), B for Tier 3 wording (ML.mw blog, datacentermap).
- **National Data Centre Expansion, Lilongwe** - PPPC RFB/PDF (ref MW-PPPC-494042-GO-RFB) for expansion of the National Data Centre under the Digital Malawi Acceleration Project. The RFB places the project site off/along Paul Kagame Road in Lilongwe, states the existing Production Site is a Tier-III facility, and gives UPS/HCI details without IT MW or facility MW. Grade A (PPPC procurement). Status: planned/procurement until award/commissioning evidence appears.
- **OCL Enterprise Data Center, Kanengo, Lilongwe** - operator page (ocl.mw) claims world-class DC, 99.982% uptime, redundant power/cooling/network, colo from 1 Dec 2023. Grade A for operator/facility claim; capacity/address fields need verification.
- **MTL Data Centre / DataCENTRE service** - MTL's operator page advertises colocation with rack/floor space, dedicated internet/VPN, fire suppression, air conditioning, UPS, biometric access, CCTV, and continuous traffic monitoring. Grade A for operator-owned service/facility claim; note that normal TLS validation failed on 2026-08-12 and local verification required `curl -k`, so keep a fetch caveat rather than downgrading the content itself.
- **Airtel Malawi Data Centre, Blantyre** - DCD (3 Dec 2013): new DC opened in Blantyre, doubled capacity, over US$1m invested, MD Saulos Chilima. Grade B; **2013 record - verify current status**.
- **TNM data centres** - TNM operates two DCs (implied by its 5 Mar 2026 announcement of a planned **third** datacentre, ITWeb Africa; VoLTE launch in Lilongwe) and built a private cloud on Canonical Charmed OpenStack (Canonical blog). Grade B for the announcement; existing DCs have little public documentation.
- **Converged Technology Networks (CTN) Micro Data Centre, Lilongwe** - ITWeb Africa (Feb 2026): plans for Malawi's first AI-focused micro data centre, GPU-as-a-Service. Grade B for announcement; no site/capacity disclosed. Status: announced.
- **Korena / 1nga Solutions, Blantyre** - korena.mw claims a Tier III+ sovereign AI cloud/data-centre campus in Blantyre, Mawatt waste-to-energy power, NVIDIA A100/H100 GPU cloud. **Caution**: contact phone on the page is a placeholder-style number; no independent/third-party confirmation found. Grade A only for the marketing claim's existence; physical status U/unverified. Status: announced/claim.
- **Reserve Bank of Malawi Corporate Data Centre, Blantyre Branch** - ITB RBM/ICT/BT/01/2025 (issued 13 Nov 2025, bids due 3 Dec 2025 at 10:00) for design and construction. Grade A (RBM primary). Status: planned/procurement.
- **ESCOM data centre** - ML.mw blog (Sep 2022) names ESCOM among entities with data centres. Grade C lead only; verify on escom.mw.
- **Mzuzu University data centre concept** - 2021 academic/academic-blog materials only. Grade C; treated as concept, not a facility.

Market watch: **no hyperscale public cloud region** in Malawi (AWS/Azure/GCP/OCI/Huawei all absent as of 2026-08-12). Regional colo players (Raxio, Africa Data Centres, Teraco/Digital Realty, Equinix/iColo, Wingu, Paratus, Liquid Intelligent Technologies) have **no verified Malawi data centre**; Liquid operates Malawi fibre/network but no confirmed public DC facility was found in this review.

## 1. Operator and Facility Seed List

| Operator / platform | URLs | Malawi signal | Likely location | Grade discipline |
|---|---|---|---|---|
| **Government Data Centre (PPPC/DIGMAP)** | https://digmap.pppc.mw/government-data-center-making-progress/ ; https://www.worldbank.org/en/results/2025/06/23/digitalizing-afe-malawi-to-improve-access-to-education-public-services-and-income-opportunities | Primary national DC; HCI; World Bank-funded; complements Blantyre DC | Lilongwe (Central) | A for project existence/role; capacity null; completion date unverified |
| **National Data Centre (Gov of Malawi / Huawei)** | https://www.datacenterdynamics.com/en/news/malawi-launches-national-data-center/ ; https://english.news.cn/20220723/4f40a51b98244c7f97c5b70469dd8992/c.html ; https://capacityglobal.com/news/malawi-government-sets-up-national-data-centre-with-huawei/ ; https://ml.mw/2022/09/07/the-national-data-center-blantyre-blog-post/ | First national DC; commissioned 21 Jul 2022; hosts gov-wide systems; secondary/backup to Lilongwe per DIGMAP | Blantyre (Southern) | B+/A for launch event from Xinhua/DCD and DIGMAP role statement; B/C for Tier 3 and ESCOM involvement from ML.mw; capacity null |
| **National Data Centre Expansion** | https://www.pppc.mw/procurement/reports-notices/request-for-bids-goods-two-envelope-bidding-process-procurement-of-expansion-of-national-data-centre ; https://api.pppc.mw/api/download/722 ; https://www.pppc.mw/procurement/reports-notices/invitation-to-early-market-engagement-expansion-of-the-national-data-centre | RFB MW-PPPC-494042-GO-RFB; project site off/along Paul Kagame Road; existing Production Site is Tier-III; expansion adds modules/compute to existing DC | Lilongwe (Central) | A for procurement/site/tier wording in PPPC PDF; planned/procurement status; capacity_mw null |
| **OCL Enterprise Data Center** | https://www.ocl.mw/tier3.html ; https://www.ocl.mw/ | World-class enterprise DC; 99.982% uptime; redundant power/cooling/network; enterprise colo from 1 Dec 2023; OCL HQ Robins Rd, Blantyre | Kanengo, Lilongwe (Central) | A for operator/facility claim; C for details not on the page (capacity, rack counts) |
| **MTL Data Centre / DataCENTRE** | https://www.mtl.mw/hosted-services/datacentre/ ; https://www.datacenters.com/malawi-telecommunications-mtl-data-centre | Operator advertises rack/floor-space colocation, dedicated internet/VPN, fire suppression, AC, UPS, biometric access, CCTV, and traffic monitoring | Malawi; directory places MTL Data Centre in Lilongwe | A for MTL operator-owned service/facility claims; C for third-party location detail unless operator/council source confirms; TLS-chain caveat from 2026-08-12 |
| **TNM (Telekom Networks Malawi)** | https://www.tnm.co.mw/ ; https://itweb.africa/article/tnm-malawi-mulls-third-datacentre-as-it-rolls-out-launches-volte-service/KzQenMjy9zY7Zd2r ; https://canonical.com/blog/malawis-tnm-selects-canonicals-charmed-openstack-to-help-lead-virtualisation-charge | Two existing DCs + third announced 5 Mar 2026 (VoLTE launch, Lilongwe); private cloud on Charmed OpenStack | Blantyre HQ (Southern); Lilongwe (Central) presence | B for 3rd-DC announcement and OpenStack build; DC count/locations C unless operator discloses |
| **Airtel Malawi** | https://www.datacenterdynamics.com/en/news/airtel-malawi-establishes-new-data-center/ | New DC opened Blantyre Dec 2013; doubled capacity; >US$1m; cloud launch followed | Blantyre (Southern) | B (2013 record); current status/address unverified - do not count MW |
| **Korena / 1nga Solutions** | https://korena.mw/ | Tier III+ sovereign AI cloud/DC campus claim; Mawatt waste-to-energy; GPU cloud (A100/H100); government hosting pitch | Blantyre (Southern) | A for claim existence (operator page); U for physical operation; placeholder-style phone noted |
| **Converged Technology Networks (CTN)** | https://itweb.africa/article/malawi-plans-to-launch-micro-data-centre/KzQenqjy9NlMZd2r ; https://mw.linkedin.com/company/converged-technology-networks | AI-focused Micro Data Centre; GPU-as-a-Service; HQ Lilongwe | Lilongwe (Central) | B for announcement (ITWeb Africa); no site/capacity |
| **Reserve Bank of Malawi CDC** | https://www.rbm.mw/Home/GetContentFile/?ContentID=62075 ; https://www.malawitenders.com/tender/design-and-construction-modern-corporate-data-centre-cdc-reserve-bank-malawi-blantyre-branch-7c2b7ce.php | Design+construction of modern CDC at RBM Blantyre branch; ITB RBM/ICT/BT/01/2025, issued 13 Nov 2025; bids due 3 Dec 2025 | Blantyre (Southern) | A for tender (RBM); planned/procurement status |
| **ESCOM** | https://www.escom.mw/ ; https://ml.mw/2022/09/07/the-national-data-center-blantyre-blog-post/ | ESCOM named as having its own data centre; utility power context | Blantyre (Southern), national | C lead only until escom.mw confirms |
| **MIX (Malawi Internet Exchange, MIX-BT)** | http://www.mispa.org.mw/mix.html ; https://www.peeringdb.com/ix/727 | Neutral IXP at College of Medicine, Blantyre; op since 4 Dec 2008; ~10 peers/46G | Blantyre (Southern) | A/B for network presence; not DC proof |
| **SimbaNet** | https://www.simbanet.co.mw/ ; https://www.simbanet.net/ | ISP/network operator (AS327941) with Lilongwe/Blantyre presence; peers at MIX; hosting services | Lilongwe/Blantyre | A for operator; C for DC specifics unless a facility page appears |
| **Raxio, Africa Data Centres, Teraco/Digital Realty, Equinix/iColo, Wingu, Paratus, Liquid, Vantage, NTT** | Official portfolio pages | No verified Malawi facility found in this review | Watch Lilongwe/Blantyre only | C until official Malawi project/source appears |

Operator queries:
```text
"{operator}" Malawi "data centre" OR "data center" OR "colocation"
"{operator}" Malawi "Tier III" OR "Tier 3" OR "by design"
"{operator}" Malawi "MW" OR "MVA" OR "racks" OR "cabinets"
"{operator}" Malawi "cloud" OR "hosting" OR "DR site"
"{operator}" "MACRA" OR "ESCOM" OR "PPPC" Malawi
"{operator}" "Lilongwe" OR "Blantyre" "data centre"
"{operator}" "MoU" OR "expansion" "data centre" Malawi
```

---

## 2. Trade Press and Industry Media

Use trade press for discovery and date/capacity leads, then reconcile against operator/government sources. Verified high-yield examples from this review:
- DCD: Malawi launches national data center (28 Jul 2022) - Huawei-built Blantyre facility, hosts government-wide systems: https://www.datacenterdynamics.com/en/news/malawi-launches-national-data-center/
- DCD: Airtel Malawi establishes new data center (3 Dec 2013) - Blantyre DC, doubled capacity, >US$1m: https://www.datacenterdynamics.com/en/news/airtel-malawi-establishes-new-data-center/
- ITWeb Africa: TNM Malawi mulls third datacentre (6 Mar 2026) - announced at VoLTE launch in Lilongwe: https://itweb.africa/article/tnm-malawi-mulls-third-datacentre-as-it-rolls-out-launches-volte-service/KzQenMjy9zY7Zd2r ; related roadmap: https://itweb.africa/article/tnm-outlines-malawi-growth-roadmap/6GxRKMYQpmaMb3Wj
- ITWeb Africa: Malawi plans to launch micro data centre (Feb 2026) - CTN AI micro-DC, GPU-as-a-Service: https://itweb.africa/article/malawi-plans-to-launch-micro-data-centre/KzQenqjy9NlMZd2r
- Capacity: Malawi government sets up national data centre with Huawei (26 Jul 2022): https://capacityglobal.com/news/malawi-government-sets-up-national-data-centre-with-huawei/
- Xinhua (official wire, B+/A for the commissioning event): https://english.news.cn/20220723/4f40a51b98244c7f97c5b70469dd8992/c.html
- Machine Learning Malawi blog (B/C): National Data Centre Blantyre as Tier 3 by Huawei with ESCOM; names TNM, ESCOM, ISPs (MRL, Inq/Skyband), banks and Ministry of Health as DC operators: https://ml.mw/2022/09/07/the-national-data-center-blantyre-blog-post/
- Canonical (vendor case study, B): TNM builds private cloud on Charmed OpenStack: https://canonical.com/blog/malawis-tnm-selects-canonicals-charmed-openstack-to-help-lead-virtualisation-charge

Local/national press to search (B/C discovery surface):
- Nyasa Times: https://www.nyasatimes.com/
- The Nation: https://mwnation.com/
- Maravi Post: https://www.maravipost.com/
- Malawi Voice: https://www.malawivoice.com/
- MANA (Malawi News Agency): https://www.manaonline.gov.mw/

Regional/international trade:
- DCD: https://www.datacenterdynamics.com/
- ITWeb Africa: https://itweb.africa/
- Capacity: https://capacityglobal.com/
- Developing Telecoms: https://developingtelecoms.com/
- Connecting Africa: https://www.connectingafrica.com/

---

## 3. Network, Peering, and CDN Evidence

Malawi is landlocked; all international capacity is terrestrial or via third-country landings (no submarine cable lands in Malawi). International routes run through Zambia, Tanzania, and Mozambique; the National Fiber Backbone and MTL's backbone carry domestic traffic, and MACRA licences international gateway/carrier services. Fibre/gateway evidence is a viability input, **not** datacenter proof.

Verified network anchors:
- **MIX-BT (Malawi Internet Exchange)**: operated by MISPA; located at the College of Medicine, Blantyre; operational since 4 Dec 2008; ~10 peers / 46G capacity per PeeringDB (ix 727). Use PeeringDB membership lists to discover operators that co-locate equipment in Blantyre. https://www.peeringdb.com/ix/727 ; http://www.mispa.org.mw/mix.html
- **Datacentermap Malawi**: lists 1 data centre facility (Malawi National Data Center, Blantyre) across 3 operators - a C-grade directory baseline, not authoritative: https://www.datacentermap.com/malawi/ ; https://www.datacentermap.com/malawi/blantyre/
- **Datacenters.com MTL listing**: C-grade directory confirmation that MTL offers colocation infrastructure: https://www.datacenters.com/malawi-telecommunications-mtl-data-centre
- Local ASNs for cross-checks: SimbaNet Malawi (AS327941), MTL (MTL-AS). CDN PoP claims (Cloudflare/Akamai edge nodes in Lilongwe) should be verified on PeeringDB/network maps and treated as edge presence, not DCs.

Query templates:
```text
site:peeringdb.com/ix "Malawi" OR "Blantyre"
"Malawi Internet Exchange" "member" OR "peer"
site:datacentermap.com Malawi
site:datacenters.com "Malawi"
"{operator}" "Malawi" "fibre" OR "backbone" OR "gateway"
"{operator}" AS{number} Malawi
```

---

## 4. Enterprise, Financial, Government, and University Leads

- **Banks and financials**: RBM's own CDC tender (Blantyre) is the strongest financial-sector lead. ML.mw (C) states banks run their own datacenters; only count named facilities confirmed by primary/strong secondary sources. Watch RBM ITBs and annual reports for CDC awards; watch commercial banks (e.g., NBS, Standard Bank, FMB/First Capital, CDH/Illovo) for DR-site announcements.
- **Utilities**: ESCOM's own DC is a C-grade lead (ML.mw). Any ESCOM/Huawei collaboration around the National Data Centre (ML.mw mentions ESCOM under the national fibre backbone initiative) should be re-verified against escom.mw.
- **Government agencies**: Ministry of Health server rooms and other MDA in-house ICT rooms are leads only (ML.mw, C). The e-Government Department and PPPC/DIGMAP pages are the A-grade surfaces for real government facilities.
- **Universities**: Mzuzu University data-centre concept (2021, C - academic materials only, https://ralphphall.com/2021/01/11/establishing-data-centre-at-mzuzu-university/ and ResearchGate paper 357339171) - no later completion evidence found. Malawi University of Science and Technology (MUST, Ndata/Thyolo, Southern) - no DC evidence found. Treat both as `lead only`.
- **Checked-and-empty leads (honest note)**: "Kukula" (Kukula Capital is a Zambia investment firm - unrelated) and "2090" (no Malawian DC entity) produced no DC evidence; regional colo firms (Raxio, Wingu, Africa Data Centres, Teraco, Equinix/iColo, Paratus, Liquid) have no verified Malawi DC as of 2026-08-12.
- **Hosting/ISPs**: SimbaNet, Inq Digital (formerly Skyband), Globe Internet, Afrimax, and MRL offer hosting/connectivity; none has a documented public colo DC beyond MTL/OCL. Check each operator's page for "data centre" claims before counting.

Query templates:
```text
"{bank}" "data centre" OR "disaster recovery" Malawi
site:rbm.mw "data centre" OR "CDC"
site:escom.mw "data centre" OR "data center"
"Malawi University of Science and Technology" "data centre"
"Mzuzu" "data centre" 2022 OR 2023 OR 2024 OR 2025
"{isp}" Malawi "data centre" OR "colocation"
```

---

## 5. Associations and Events

- **MISPA** (Malawi Internet Service Providers' Association): operates the MIX; membership and peering records reveal who co-locates where: http://www.mispa.org.mw/
- **ICTAM** (Information and Communication Technology Association of Malawi): industry advocacy; useful for company directories and events: referenced on https://ict.gov.mw/index.php/home
- Industry events (Malawi ICT/innovation summits, e-Government conferences) occasionally announce DC/AI projects; monitor local press coverage rather than assuming attendance.

---

## 6. Per-Region Industry Strategy

| Region | Industry anchors | Strategy and honest expected yield |
|---|---|---|
| **Central Region** | OCL (Kanengo); MTL; CTN; Government Data Centre; NDC expansion; TNM 3rd-DC announcement (Lilongwe, Mar 2026); MIX peers with Lilongwe presence | **Highest yield.** Confirm OCL/MTL/CTN operator pages; reconcile government DC status against PPPC/DIGMAP; search Lilongwe hosting providers and CDN/edge claims. Expected **4-6 records**. |
| **Southern Region** | National Data Centre Blantyre; RBM CDC; Airtel DC; TNM existing DCs (Blantyre HQ); Korena/1nga claim; ESCOM lead; MIX-BT | **Medium-high yield.** Verify 2022 launch + current government use; track RBM CDC tender award; re-verify Airtel 2013 DC; treat Korena as announced/unverified until independent confirmation. Expected **3-5 records**. |
| **Northern Region** | Mzuzu University concept only | **Very low yield.** Re-check Mzuzu/Karonga for university or provincial-government ICT infrastructure; otherwise record `no_projects`. Expected **0-1 records**. |

---

## 7. Confirmation Workflow

For each candidate facility, run this loop and record per-field grades:
1. **Discover** via trade press, directories, procurement, or operator marketing.
2. **Anchor** on the operator/government page for existence and role (A). If a page has transport/TLS issues, record the fetch caveat separately; do not downgrade an operator page that can be opened and read with a reproducible method such as `curl -k` unless identity/content is uncertain.
3. **Independently confirm** with a second source (government, regulator, procurement, or strong trade press) before marking a field A.
4. **Grade each field separately**: existence, role, tier, capacity, address, status. Never let an A-grade existence claim lift a C-grade address to A.
5. **Status discipline**: `operational` (launched + continued evidence), `under construction`, `planned` (procurement/tender), `announced` (public commitment without site/permit), `MoU/intent`, `lead only` (no named facility), `unverified` (marketing-only claim such as Korena).
6. **Capacity**: Malawi sources disclose no MW figures for any DC; record `null` and note the absence rather than estimating from MVA or rack counts.
7. **Coverage**: complete all three regions; if a region yields nothing, say so explicitly in the results line (no_projects) rather than dropping it.

---

## 8. Source Notes From This Review

Honest record of what was verified on 2026-08-12:
- **A-grade/operator pages opened**: ocl.mw/tier3.html (full), mtl.mw/hosted-services/datacentre/ (full via `curl -k`; TLS-chain caveat), korena.mw (full; placeholder-style contact phone noted), digmap.pppc.mw (full), PPPC RFB page/PDF (full enough via HTML/PDF text extraction), ict.gov.mw (full), rbm.mw ITB PDF (full enough via PDF text extraction). DCD/ITWeb/Xinhua/Canonical pages were also opened for B-grade industry/vendor confirmation.
- **Fetch caveats**: mtl.mw/hosted-services/datacentre/ returned HTTP 200 only when TLS verification was bypassed locally on 2026-08-12; keep the operator facts, but note the certificate issue. The older PPPC early-market URL is real but its visible body is sparse/noisy; use the PPPC RFB page and `https://api.pppc.mw/api/download/722` PDF for expansion details.
- **Old records needing re-validation**: Airtel Malawi DC (2013, DCD); TNM DC count/locations (2026 announcement says a third datacentre is planned but does not list the first two). National Data Centre Blantyre has 2022 launch evidence and a 2024 DIGMAP role statement as the secondary/backup site, but still lacks public MW/certification detail.
- **Marketing-only claims**: Korena/1nga (Tier III+ campus, GPU cloud) - no third-party confirmation, placeholder phone; CTN micro-DC - press announcement only.
- **Checked-and-empty**: no hyperscale cloud region in Malawi; no Paratus/Liquid/Raxio/ADC/Teraco/Equinix/iColo/Wingu/Vantage/NTT Malawi DC; no Kukula/2090 DC; no Mzuzu/MUST facility; no MW figures anywhere.
- **Prior exploration**: batch-480 results (see scripts/expansion/world/results/batch-480.jsonl) align with this review; new additions here: Korena/1nga claim, TNM third-DC announcement, MIX-BT details, power-crisis context.
