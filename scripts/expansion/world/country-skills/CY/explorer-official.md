# CY Explorer Official - Cyprus Datacenter Enumeration via Regulatory, Planning, Energy, Government-IT and Cloud-Region Sources

Date: 2026-08-12. Scope: Cyprus (CY), all 6 districts: Nicosia/Lefkosia, Limassol/Lemesos, Larnaca/Larnaka, Famagusta/Ammochostos, Paphos/Pafos, Kyrenia/Keryneia. Angle: official/regulatory discovery for operational and proposed datacenter, colocation, cloud, government IT, IXP and cable-landing infrastructure.

Reliability grades: **A** = official public-sector/regulator/permit/registry/cloud-provider page, operator official page, listed-company filing, or Uptime Institute registry entry; **B** = reputable trade or local business press with named parties and specific facts; **C** = directories, marketplaces, partner pages, SEO hosting pages, and marketing pages that do not disclose facility-level evidence; **U** = not independently verified. A grade applies only to the supported fact. Example: an operator page proves the operator claims a facility/service; it does not prove MW, Uptime certification, or permits unless it says so or a primary registry confirms it.

---

## 0. Structural Facts and Caveats

- **Administrative coverage is complete at 6 districts.** The Republic of Cyprus District Administration Offices state that Cyprus is divided into Nicosia, Limassol, Pafos, Larnaka in government-controlled areas, plus Famagusta and Keryneia in occupied areas: https://www.moi.gov.cy/moi/da/dadmin.nsf/dmlhistory_en/dmlhistory_en?OpenDocument . This methodology must always log all six rows even when the result is negative.
- **Partition caveat.** The Republic of Cyprus does not exercise effective control in Kyrenia and much of Famagusta. ROC official sources cover the government-controlled part of Famagusta, including Ayia Napa/Agia Napa, Paralimni, Protaras and Deryneia. Kyrenia and occupied Famagusta must be searched through Turkish/TRNC sources and recorded with a `north-cyprus` caveat; do not mix those findings with ROC permit or registry coverage.
- **No single public datacenter registry exists.** Build the inventory from telecom authorisations, radio authorisations, planning/building applications, land records, company registry records, electricity/grid records, procurement notices, official operator pages, Uptime registry records, cloud-region pages, IXPs and cable-landing records.
- **Language.** Greek and English cover ROC official sources. Turkish is required for TRNC/north searches.

## 1. Verified Official Source Map

| Source | URL | How to use | Grade scope |
|---|---|---|---|
| District Administration Offices | https://www.moi.gov.cy/moi/da/dadmin.nsf/dmlhistory_en/dmlhistory_en?OpenDocument | Confirms the 6-district frame and occupied-area caveat. | A for division structure. |
| OCECPR / GERHET registers page | https://ocecpr.ee.cy/mitroa | Links to `iris.cy/search-organization` for registered electronic communications providers and to numbering-plan search. | A for provider authorisation/name; not a DC inventory. |
| IRIS electronic communications register | https://iris.cy/search-organization | Search authorised electronic-communications entities such as Cyta, PrimeTel, Cablenet, Epic, Logosnet, NetShop. | A for authorisation if found. |
| DEC radio authorisation register | https://dec.dmrid.gov.cy/dmrid/dec/ws_dec.nsf/register_en/register_en?OpenDocument= | Radio/frequency authorisations; useful for wireless backhaul and spectrum-linked infrastructure. | A for radio authorisation. |
| Digital Security Authority laws | https://dsa.cy/en/legislation/laws | Confirms NIS law N.89(I)/2020 consolidated with Law 60(I)/2025; use for CII/essential-entity context. | A for cybersecurity-law status. |
| CERA transmission/distribution page | https://www.cera.org.cy/en-gb/ilektrismos/details/transmission-system | Confirms CTSO role, EAC as transmission owner, EAC/DSO split, and connection thresholds. Customers above 12 MVA file connection requests with CTSO; customers up to 12 MVA use EAC/DSO. | A for grid route and threshold. |
| CERA competitive market announcement | https://www.cera.org.cy/en-gb/anakoinoseis/details/anakoinwsi-2025-27 and https://www.cera.org.cy/en-gb/anakoinoseis/details/anakoinwsi-aah | Commercial operation / first trading day is 1 October 2025, not 2024. | A for market date. |
| EAC | https://www.eac.com.cy/EN/Pages/default.aspx | Distribution connection and district electricity works; search for substations and large loads near candidate sites. | A when a filing/page states a project. |
| Great Sea Interconnector | https://www.great-sea-interconnector.com/en | Official project page: 1,000 MW, 1,208 km, 500 kV, Greece-Cyprus first and Israel later; Cyprus-Greece part under construction per project site. | A for project sponsor claims/current page status. |
| Department of Town Planning and Housing | https://www.moi.gov.cy/moi/tph/tph.nsf/home_en/home_en?openform= | Planning authority pages, planning forms, development-control contacts and Hippodamos link. | A for planning route. |
| Hippodamos planning portal | https://hippodamus.tph.moi.gov.cy/ and info page https://www.moi.gov.cy/moi/tph/tph.nsf/ishippodamos_en/ishippodamos_en?opendocument= | Electronic planning applications/map browsing. Search by parcel/address/operator where possible. | A for application/permit metadata if retrieved. |
| Department of Lands and Surveys | https://portal.dls.moi.gov.cy/en/ | Ownership/title and parcel checks for candidate addresses; often requires account/fee. | A for land-record facts retrieved. |
| eProcurement System e-PPS | https://www.eprocurement.gov.cy/epps/home.do?OpenElement | Search tenders/awards for data centre, colocation, cloud, hosting, disaster recovery, WAN, UPS, generators. | A for public tender/award facts. |
| EU TED | https://ted.europa.eu/ | Above-threshold Cyprus procurement notices. | A for tender notices. |
| DMRID / gov.cy | https://www.gov.cy/dmrid/en/ and https://www.gov.cy/en/ | Digital policy, cloud policy, government IT and data-sovereignty signals. Gov.cy search pages may return 403 to crawlers, so keep URLs and evidence dates. | A for accessible official pages/PDFs. |
| Digital Services Factory cloud guidance | https://dsf.dmrid.gov.cy/2022/05/17/guidance-for-cloud-computing/ | Government cloud/on-prem guidance; use as government IT context, not a facility address. | A if accessible; otherwise record as official URL requiring manual browser check. |
| Uptime Institute registry | https://uptimeinstitute.com/tier-certification/tier-certification-list | Search Cyprus/CL8. Confirmed entry: `CL8 LIM Data Center, Phase 1`, Limassol, Cyprus, Cloudlayer8 Limited. | A for Uptime-listed certification only. |
| Cloud provider region pages | AWS: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; Azure: https://learn.microsoft.com/en-us/azure/reliability/regions-list ; GCP: https://cloud.google.com/about/locations ; OCI: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Check for public cloud regions/local zones. As of 2026-08-12, no AWS/Azure/GCP/OCI Cyprus public region was found. | A for region presence/absence on check date. |

## 2. Legal and Regulatory Anchors

- Electronic communications: OCECPR operates registers under the Regulation of Electronic Communications and Postal Services Law, N.112(I)/2004, as amended. Use OCECPR/IRIS to confirm telecom/ISP authorisation, but do not treat authorisation as a facility record.
- Radio/frequency: DEC maintains the public authorisation register under the Radiocommunications framework. Use for operators with wireless access/backhaul or private-network claims.
- Cybersecurity/NIS: DSA lists the Security of Networks and Information Systems Laws of 2020 and 2025, N.89(I)/2020 consolidated with Law 60(I)/2025. Datacenters may be relevant as digital infrastructure/essential entities, but DSA pages should not be expected to publish site addresses.
- Planning: Town and Country Planning Law is Law 90/1972. TPH and Hippodamos are the official route for planning applications and planning-permit records.
- Land: DLS operates the land/title portal. It is a verification source for specific parcels/addresses after industry discovery.
- Electricity: CERA says customers above 12 MVA submit connection requests to CTSO; up to 12 MVA goes to EAC/DSO. This matters because many Cyprus facilities are below hyperscale size and may only appear in EAC/DSO traces.

## 3. Official Query Templates

Greek and English templates for ROC sources:
```text
site:ocecpr.ee.cy "Μητρώο" "Ηλεκτρονικών Επικοινωνιών" "{operator}"
site:iris.cy "{operator}" "Ηλεκτρονικών Επικοινωνιών"
site:dec.dmrid.gov.cy "{operator}" OR "{area}" "Authorization Register"
site:dsa.cy "critical information infrastructure" OR "essential entity" OR "ΦΚΥΠ"
site:cera.org.cy "data centre" OR "κέντρο δεδομένων" OR "connection" OR "12 MVA"
site:eac.com.cy "substation" OR "υποσταθμός" "{area}"
site:moi.gov.cy/moi/tph "κέντρο δεδομένων" OR "data centre" OR "πολεοδομική άδεια"
site:hippodamus.tph.moi.gov.cy "{operator}" OR "{address}"
site:eprocurement.gov.cy "data centre" OR "data center" OR "κέντρο δεδομένων" OR colocation OR hosting
site:ted.europa.eu Cyprus "data centre" OR "data center" OR colocation
site:gov.cy/dmrid "data centre" OR "cloud" OR "κυβερνητικό νέφος"
"κέντρο δεδομένων" "{district}" "Κύπρος"
"πολεοδομική άδεια" "κέντρο δεδομένων" "{district}"
"ηλεκτροδότηση" OR "υποσταθμός" "κέντρο δεδομένων" "Κύπρος"
```

Turkish/TRNC templates for occupied areas:
```text
site:bthk.org "veri merkezi" OR "barındırma" OR "bulut"
site:edevlet.gov.ct.tr "Bilgi Teknolojileri ve Haberleşme Kurumu"
"KKTC" "veri merkezi" "Girne" OR "Gazimağusa"
"Kuzey Kıbrıs" "veri merkezi" "fiziksel adres"
"Kıb-Tek" "veri merkezi" OR "trafo" OR "bağlantı"
```

Cloud/edge templates:
```text
site:docs.aws.amazon.com/global-infrastructure "Cyprus"
site:aws.amazon.com/cloudfront/features "Cyprus"
site:learn.microsoft.com/en-us/azure/reliability/regions-list "Cyprus"
site:azure.microsoft.com "ExpressRoute" "Cyprus"
site:cloud.google.com/about/locations "Cyprus"
site:docs.oracle.com/iaas "Cyprus"
```

## 4. Official Verification Workflow

1. Start with a candidate name/address from industry sources.
2. Confirm the operator in OCECPR/IRIS or DEC if telecom/radio-related.
3. Search TPH/Hippodamos by operator, parcel/address, municipality and Greek keywords. For high-load projects, search EIA/Department of Environment notices as well.
4. Check CERA/CTSO/EAC for connection route. Above 12 MVA should have a CTSO trail; smaller colo facilities may only have EAC/DSO or no public load trace.
5. Check DLS only after an address is known; record parcel/ownership facts separately from facility facts.
6. Search e-PPS/TED for government colocation, cloud, hosting, backup, UPS, generator and disaster-recovery tenders.
7. Check cloud-provider official pages for region/local-zone/edge claims.
8. Grade every field independently; do not promote directory rack counts, MW, or addresses unless operator/official/Uptime evidence supports them.

## 5. District Coverage and Official-First Expectations

| District | Expected pattern | Official-first route | Current verified official status |
|---|---|---|---|
| Nicosia / Lefkosia | Main hub: Cyta Aglantzia, RedMax/Latsia, Logosnet DataFort, Cablenet Engomi lead, PrimeTel service, CyIX, government IT. | Cyta official pages; OCECPR/IRIS; TPH/Hippodamos in Aglantzia, Latsia-Geri, Engomi/Strovolos; DLS; e-PPS; CERA/EAC for high-load traces. | Cyta confirms two DCs including Nicosia/Aglantzia; Cyta confirms RedMax agreement in Latsia Industrial Area. Logosnet official page confirms Nicosia DataFort. Cablenet address is directory/office-supported only unless Cablenet official page is found. |
| Limassol / Lemesos | Secondary hub: Cyta Amathounta, CL8 Limassol, JumboIX/IPTP Kermia, fintech/iGaming demand. | Cyta official; CL8 official + Uptime registry; CERA/EAC for Agios Athanasios/Mesa Geitonia/Amathounta; PeeringDB for JumboIX; TPH/Hippodamos. | CL8 is confirmed by operator and Uptime registry in Limassol. Cyta confirms Limassol/Amathounta. PeeringDB confirms JumboIX/IPTP facility in Limassol as IXP/facility context. |
| Larnaca / Larnaka | Medium: Cyta/Simplex LCA1, Pentaskhinos cable landing, NetShop/hosting leads. | Cyta official LCA1 press; DLS/TPH for LCA1 address; Cytaglobal/Submarine Networks for Pentaskhinos; EAC Aradippou/Larnaca searches. | Cyta official press confirms Simplex LCA1 acquisition in Larnaca; DCD/CBN provide size/power context. Cytaglobal/Submarine Networks confirm Pentaskhinos cable landing. |
| Famagusta / Ammochostos | Low in ROC-controlled area: Ayia Napa cable landing; Paralimni/Deryneia/Protaras negative sweep. Occupied north handled separately. | Cytaglobal/Submarine Networks for Ayia Napa; TPH/Hippodamos in Ayia Napa/Paralimni-Deryneia; Turkish/TRNC searches for occupied Famagusta with caveat. | Ayia Napa cable landing is infrastructure context, not a DC. No ROC-part DC facility confirmed in this review. |
| Paphos / Pafos | Low: Yeroskipos cable landing and possible small colo/hosting; PrimeTel/NetShop directory claims need proof. | Cytaglobal/Submarine Networks for Yeroskipos; TPH/Hippodamos Yeroskipou; EAC Paphos district; OCECPR/IRIS for operators. | Yeroskipos cable landing confirmed. No operator/official datacenter facility confirmed beyond directory/marketing leads. |
| Kyrenia / Keryneia | No ROC-controlled registry coverage; TRNC only. Expect very limited verifiable DC activity. | BTHK, edevlet.gov.ct.tr, Kıb-Tek, Turkish-language searches, TRNC press. | BTHK official site verified as telecom authority. No Kyrenia commercial datacenter confirmed by primary source in this review. |

## 6. Officially Confirmed / High-Confidence Facility and Infrastructure Leads

| Lead | District | Evidence | Grade and notes |
|---|---|---|---|
| Cyta Data Centers: Nicosia/Aglantzia and Limassol/Amathounta | Nicosia, Limassol | Cyta business data-center/services pages: https://www.cyta.com.cy/business-datacenter-services and https://www.cyta.com.cy/business-server-hosting/en | A for Cyta-operated DC service, locations, Tier III-standard claim and ISO 27001 claim. Not an Uptime certificate. |
| Cyta / RedMax Data Centre, Latsia Industrial Area | Nicosia | Cyta press release https://www.cyta.com.cy/pr/2026-jul-15?postid=383 ; DCD https://www.datacenterdynamics.com/en/news/cyta-acquires-redmax-data-center-in-cyprus/ ; Cyprus Mail https://cyprus-mail.com/2026/07/07/cyta-invests-in-biggest-privately-owned-data-centre-in-cyprus | A for Cyta signing agreement/acquisition and Latsia Industrial Area. B for DCD/Cyprus Mail details such as 193 Giannou Kranidioti Avenue, 1,300 sqm white space, 420 racks, 2 MW substation, 640 kWp PV/battery, early-2027 commercial phase. |
| Cyta / Simplex LCA1 | Larnaca | Cyta press release https://www.cyta.com.cy/pr/2025-may-7?postid=357 ; Cyta Annual Report 2024 https://www.cyta.com.cy/mp/informational/docs/annualreports/AnnualReport_2024_en.pdf ; DCD https://www.datacenterdynamics.com/en/news/cyta-acquires-data-center-in-cyprus/ | A for Cyta acquisition and Larnaca/LCA1; A for Cyta annual-report claim of nearly 1 MW and Tier III specifications. B for DCD size/power summary. |
| CloudLayer8 / CL8 LIM Data Center, Phase 1 | Limassol | CL8 official https://cl8.com/ and https://cl8.com/about-us/ ; Uptime registry https://uptimeinstitute.com/component/tierachievement/datacenter/cl8-lim-data-center-phase-1/713 | A for operator existence, Limassol location, colocation/cloud services, and Uptime-listed Tier certification for CL8 LIM Phase 1. Use Uptime registry for certification, not only CL8 marketing. |
| Logosnet DataFort | Nicosia | Logosnet official https://logosnet.cy.net/data-centre-services | A for operator-stated Nicosia DataFort, colo features, 500 kVA diesel backup generator statement, and address at 15 Patriarchi Petrou Z, Strovolos/Nicosia. |
| PrimeTel colocation | Multiple Cyprus locations; districts unresolved from operator page | PrimeTel official https://business.primetel.com.cy/server-colocation or https://primetel.com.cy/wholesale-collocation-hosting-services | A for PrimeTel-stated colocation/data-center services, ISO/IEC 27001 and four Cyprus locations. U for exact per-site addresses until primary records are found. |
| Cablenet Engomi/Nicosia lead | Nicosia | Cablenet official contact address https://cablenet.com.cy/en/ ; DataCenterMap lead https://www.datacentermap.com/cyprus/nicosia/cablenet-data-center/ | A for Cablenet company office/address only; C for datacenter listing/address unless Cablenet official facility page or permit confirms it. |
| Logicom data-centre services | Nicosia company/service | Logicom Solutions official https://solutions.logicom.net/offerings/infrastructure-solutions-and-services/data-centre/ | A for data-centre design/integration service offering; **not a confirmed owned/operated datacenter**. |
| CyIX | Nicosia | PeeringDB https://www.peeringdb.com/ix/487 ; ISOC Pulse Cyprus https://pulse.internetsociety.org/en/ixp-tracker/country/CY/ | A/B for IXP existence via PeeringDB/ISOC; not a datacenter facility by itself. |
| JumboIX Cyprus / IPTP Kermia | Limassol | PeeringDB IX https://www.peeringdb.com/ix/3541 ; PeeringDB facility https://www.peeringdb.com/fac/3055 ; IPTP pricing page https://www.iptp.net/connectivity-services/jumbix/jumboix-cyprus-pricing-plans/ | B for PeeringDB/IXP facts; C/A only if IPTP primary pages confirm facility details. Not a DC census entry unless treated as facility/IXP context. |
| Cyta cable landing stations | Larnaca, Famagusta ROC part, Paphos | Cytaglobal https://cytaglobal.com/en/submarine-cables ; Submarine Networks https://www.submarinenetworks.com/en/stations/europe/cyprus | A for Cytaglobal claims; B for Submarine Networks summary. Stations: Pentaskhinos, Ayia Napa, Yeroskipos. CLS is not a datacenter. |
| KIMONAS | Larnaca/Pentaskhinos | Cytaglobal https://cytaglobal.com/en/submarine-cables ; Submarine Networks https://www.submarinenetworks.com/en/systems/asia-europe-africa/kimonas | A/B for cable-system context. |
| Medusa cable | Cyprus landing district must be rechecked | Medusa official https://medusascs.com/ ; Submarine Networks https://www.submarinenetworks.com/en/systems/asia-europe-africa/medusa | A/B for cable-system context; not a DC. |
| UGARIT 2 announcement | Larnaca/Pentaskhinos | BusinessWire mirror https://markets.businessinsider.com/news/stocks/unifi-communications-syrian-telecom-and-cyta-sign-landmark-ugarit-2-submarine-cable-agreement-the-first-major-international-infrastructure-deal-of-post-sanctions-syria-1036439310 ; SubTel Forum https://subtelforum.com/ugarit-2-cable-agreement-advances-syria-connectivity/ | B until Cyta or project primary page is found; 2026-08-11 announcement says Pentaskhinos-Tartous. |
| TRNC/BTHK authority | North Cyprus / occupied areas | BTHK https://www.bthk.org/ ; e-devlet profile https://edevlet.gov.ct.tr/bilgi-teknolojileri-ve-haberlesme-kurumu-bthk | A for de facto telecom authority existence/contact; does not establish a DC. |

## 7. Reliability Rules Specific to Cyprus

- Treat `Tier III standard`, `Tier III specifications`, `Tier III design`, and `Tier III Constructed Facility` as different claims. Only Uptime Institute registry entries prove Uptime certification.
- Treat `cloud` as a local service unless an AWS/Azure/GCP/OCI official region page says otherwise. No Cyprus public cloud region was found on 2026-08-12.
- Treat cable landing stations and IXPs as digital-infrastructure anchors, not datacenters.
- Treat directory counts (DataCenterMap, Datacenters.com, Cloudscene, OCOLO, Data Center Platform, UpStack, ColocationM) as discovery leads only.
- Treat north-Cyprus claims as U unless BTHK/Kıb-Tek/TRNC procurement or a named operator page gives a physical facility/address.
- For addresses, prefer: operator official page > permit/DLS/e-PPS/registry > PeeringDB for IXP/facility > reputable trade press > directories.

## 8. Recheck Cadence

- Monthly: Cyta press releases, CL8 news, DCD, Cyprus Mail, CBN, KNews, SubTel Forum, Telecompaper, Capacity Media for RedMax, LCA1, Medusa and UGARIT 2 milestones.
- Quarterly: OCECPR/IRIS authorised-operator register, DEC register, PeeringDB/ISOC Pulse, Uptime registry, hyperscaler region pages, PrimeTel/Cablenet/Logosnet/NetShop/CL8 operator pages.
- Semi-annually: TPH/Hippodamos, DLS for known parcels, EAC/CERA/CTSO for grid connection signals, e-PPS/TED for public-sector hosting/DR/cloud procurement.
- Event-driven: any announced large-load connection, new cable landing, hyperscaler local-zone/edge announcement, Khazna/G42 or other foreign-investment datacenter MOU, TRNC e-government/datacenter procurement.
