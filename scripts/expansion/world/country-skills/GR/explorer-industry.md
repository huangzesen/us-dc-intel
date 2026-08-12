# GR Explorer Industry - Greece Datacenter Market and Operator Methodology

Date: 2026-08-12. Scope: Greece datacenter enumeration from operator pages, cloud-region pages, colocation providers, IXPs, cable systems, trade press, market reports, and region-level industry search patterns. Pair every industry lead with the official workflow in `explorer-official.md` before counting it as a facility.

Reliability grades: **A** = operator/cloud/IX official page for the specific fact; **B** = strong trade press, legal analysis, contractor page, or company press release that does not itself prove permitting/operation; **C** = directories, market reports, local promotional articles, and speculative press.

---

## 0. Market Frame

- Greece has no complete industry-run datacenter registry or mature national datacenter association. Enumerate by triangulating official operator pages, cloud-region pages, DCD/Greek trade press, GR-IX/DE-CIX/PeeringDB, submarine cable announcements, and official permitting.
- Main hub: **Attica**, especially eastern Attica/Mesogeia: Koropi/Kropia, Spata-Artemida, Paiania, Markopoulo, and nearby Athens metro facilities. Secondary hubs: **Thessaloniki/Central Macedonia** and **Crete**. **Volos/Thessaly** appears in market-report pipeline lists but requires primary confirmation.
- Connectivity drivers are material: GR-IX operates Athens and Thessaloniki exchanges; Digital Realty, OTE/Cosmote, Lancom, Synapsecom, Sparkle, Grid Telecom, Vodafone, and cable landing systems all create siting leads. Connectivity evidence alone does not prove a datacenter facility.
- Market-report numbers are leads only. Arizton, DataCenterMap, Baxtel, Datacenters.com, Mordor, and similar sources can identify operators and cities, but their counts, capacity, and opening dates must be verified against operator or official records.
- Search in both languages: `data center`, `datacenter`, `data centre`, `κέντρο δεδομένων`, `κέντρα δεδομένων`, `colocation`, `φιλοξενία`, `cloud`, `νέφος`, `hyperscale`, `υποδομή δεδομένων`, `subsea`, `cable landing station`, `CLS`.

---

## 1. Source Grades and URLs

### 1.1 Industry / Trade Sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics, Greece tag/search | https://www.datacenterdynamics.com/en/tags/greece/ | Best English feed for Greek DC announcements: EDGNEX/Data In Scale, DATA4 Paiania, Digital Realty HER1, Lamda Hellix/Digital Realty expansions, Grid Telecom/Quadrivium. | B |
| Kathimerini / eKathimerini | https://www.kathimerini.gr and https://www.ekathimerini.com | Greek business reporting on permitting, grid constraints, Microsoft, Dromeus/Apto, and policy. | B |
| Naftemporiki | https://www.naftemporiki.gr | Greek business coverage of Digital Realty/Lamda Hellix, Microsoft, energy and investment context. | B |
| OT.gr | https://www.ot.gr | ICT/telco/business reporting on Microsoft, OTE, EDGNEX/PPC, DATA4, cloud policy. | B |
| Business Daily | https://www.businessdaily.gr | Greek economy/ICT reporting and project announcements. | B |
| energypress / energymag | https://www.energypress.gr and https://www.energymag.gr | Grid-demand and ADMIE/energy-policy context for datacenters. | B |
| Insider, newmoney, tovima, protothema, iefimerida | site searches | Greek-language leads, public reactions, local project details. Use carefully and back-resolve. | B/C |
| The Tech Capital, Capacity Media, TeleGeography, Submarine Networks | site searches | International investment/subsea coverage. | B |
| Cushman & Wakefield reports | https://www.cushmanwakefield.com | Regional market context only. | B/C |
| Arizton Greece DC portfolio | https://www.arizton.com/market-reports/greece-data-center-portfolio | Facility counts and city pipeline leads; verify each named facility. | C |
| Mordor Intelligence Greece market report | https://www.mordorintelligence.com/industry-reports/greece-data-center-market | Market sizing and share estimates; not facility proof. | C |

### 1.2 Directories / Aggregators

| Source | URL | Use | Grade |
|---|---|---|---|
| DataCenterMap Greece | https://www.datacentermap.com/greece/ and https://www.datacentermap.com/greece/athens/ | Seed facility names, rough addresses, operators, nearby facilities. | C+ |
| Datacenters.com Greece | https://www.datacenters.com/locations/greece | Seed operator/facility pages. | C+ |
| Baxtel Greece | https://baxtel.com/data-center/greece and Athens market page https://baxtel.com/data-center/athens | Expansion leads such as Microsoft Koropi, Digital Realty ATH5, DATA4, EDGNEX. | C+ |
| PeeringDB GR-IX::Athens | https://www.peeringdb.com/ix/347 | Active interconnection evidence, local facilities, peers, capacity. As reviewed, GR-IX Athens lists Digital Realty ATH1/2/3 as a local facility. | B/C |
| TeleGeography Submarine Cable Map | https://www.submarinecablemap.com | Cable landings and CLS leads; not datacenter proof. | B/C |

### 1.3 Official Sources to Pair With Industry Leads

| Source | URL | Use | Grade |
|---|---|---|---|
| Microsoft strategic investment | https://ependyseis.mindev.gov.gr/en/stratigikes/erga/investment-in-data-centres-in-greece-2 | Confirms Microsoft Operations 4733 Hellas three-site Attica strategic investment, budget, municipalities, and site power. | A |
| Microsoft announcement | https://news.microsoft.com/europe/2020/10/05/microsoft-announces-plans-for-first-datacenter-region-in-greece-as-part-of-gr-for-growth-digital-transformation-initiative/ | Official announcement of first Greece datacenter region. | A |
| Microsoft Local Greece | https://local.microsoft.com/communities/emea/greece/ | Current Microsoft community/project page; Attica region framing and local updates. | A/B |
| Azure regions list | https://learn.microsoft.com/en-us/azure/reliability/regions-list | Current public Azure region status. Re-check every run before marking Greece Central live. | A |
| OpenBusiness datacenter framework | https://openbusiness-portal.mindev.gov.gr/oloklirothike-to-thesmiko-plaisio-gia-ta-data-centers/ | Law 5069/JMD 96038 operational-notification thresholds and effective date. | A |
| PPC/EDGNEX announcement | https://www.ppcgroup.com/en/investor-relations/announcements/stock-news/stock-news-2024/edgnex-data-centers-by-damac-and-ppc-group-announce-new-data-center-in-attica-greece/ and media mirror https://www.ppcgroup.com/en/ppc-group/media-center/press-releases/recent/press-releases-2024/december-2024/dei-edgnex-data-center-atiki/ | Official company announcement of Data In Scale JV and Attica datacenter project. | A/B |
| Digital Realty HER1 page | https://www.digitalrealty.com/data-centers/emea/heraklion/her1 | Official facility page for Heraklion HER1. | A |
| Digital Realty HER1 press | https://www.digitalrealty.com/about/newsroom/press-releases/123317/digital-realty-unveils-first-data-center-in-crete-enhancing-eastern-mediterranean-connectivity | Official launch announcement for HER1. | A/B |
| Digital Realty Athens campus / Lamda Hellix legacy | https://www.digitalrealty.com/data-centers/emea/athens and legacy page https://lamdahellix.com/data-centers/athens-data-center-campus | Official Athens campus seed. | A/B |
| Digital Realty acquisition of Lamda Hellix | https://www.digitalrealty.com/about/newsroom/press-releases/123079/interxion-a-digital-realty-company-establishes-presence-in-greece-with-acquisition-of-lamda-hellix | Confirms ownership history and dedupe relationship. | A |
| DATA4 Athens/Peania | https://www.data4group.com/en/data-center-athens-greece/ | Official DATA4 campus page with address at Agiou Louka 33, Peania/Paiania. | A/B |
| GR-IX official | https://www.gr-ix.gr and GRNET page https://grnet.gr/en/gr-ix/ | Official IXP locations and members. | A |
| Grid Telecom / Quadrivium CLS | https://www.grid-telecom.com/nea/anakoinoseis/i-grid-telecom-kai-i-quadrivium-enonoyn-tis-dynameis-toys | Official Grid Telecom announcement of Chania CLS hosted in Quadrivium 20 MW Interconnection DC campus. | A/B |
| Lancom datacenter page | https://lancom.gr/data-center/ | Operator seed for Athens, Thessaloniki, Heraklion connectivity/DC services. | A/B |
| Synapsecom official | https://synapsecom.gr and https://synapsecom.gr/data-centers/thessaloniki-data-center | Operator seed for Athens/Thessaloniki datacenters. | A/B |
| GSIS G-Cloud | https://www.gsis.gr/en/public-administration/G-Cloud | Government cloud Tier 3-grade infrastructure. | A for program, B for physical site |
| Uptime Institute awards | https://uptimeinstitute.com/component/tierachievement/datacenter/rentis-data-center/644 | OTE/Cosmote Rentis Data Center certification/award evidence. | A/B |
| Aktor OTE Renti project | https://aktor.gr/en/projects/reconstruction-of-ote-data-center/ | Contractor evidence for OTE Renti conversion: 1,500 sqm, 124 racks, 500 sqm data center. | B |

---

## 2. Operator / Project Seed List

| Operator / project | Regions / places | Current evidence and how to use it | Grade |
|---|---|---|---|
| **Microsoft Azure / Microsoft Operations 4733 Hellas** | Attica: Spata-Artemida, Koropi/Kropia; possible broader Attica area | Official strategic-investment page confirms three datacenters in two Attica installation areas, with 19.2 MW at Spata Site 6 and 9.6 MW each at Koropi Sites 27/28. Microsoft announcement and Local page confirm the region plan. Current Azure public-region status must be verified before marking live; as reviewed, use planned/under-development unless Azure list/API shows GA. | A for investment/sites; A for region announcement; not live without GA proof |
| **Digital Realty / Lamda Hellix Athens campus** | Attica: Koropi/Kropia, wider Athens | Official Lamda Hellix/Digital Realty pages seed ATH campus. Dedupe Lamda Hellix legacy names with Digital Realty current branding. Verify ATH1/2/3/4/5 names and capacities against operator pages, permits, or PeeringDB. | A/B |
| **Digital Realty HER1** | Crete: Heraklion | Official facility page and 2025 Digital Realty press release confirm HER1. DCD reports initial 1 MW IT load expandable to 5 MW; Hill reports up to 6.5 MW installed IT load. Treat capacity by source and field. | A existence; B capacity unless operator page states exact MW |
| **DATA4 Athens / Peania-Paiania campus** | Attica: Paiania/Peania | DATA4 official page lists `Campus of Data Centers @ Athens - Peania`, Agiou Louka 33. DCD reports groundbreaking; Hill reports DC1 at 5,200 sqm and 15 MW. Verify permits before under-construction/future-phase capacity. | A/B |
| **EDGNEX Data Centers by DAMAC + PPC / Data In Scale** | Attica: Spata | PPC official press release confirms Data In Scale JV (DAMAC 55%, PPC 45%) and new Attica/Spata datacenter project. DCD reports 12.5-15.5 MW. Verify Diavgeia/e-adeies/OpenBusiness before counting construction/operation. | A/B |
| **Dromeus Capital + Apto** | Attica: Spata industrial zone | Strong Greek/international press lead for hyperscale DC and environmental/permitting process. Needs Diavgeia/e-PRM/e-adeies confirmation before A-grade count. | B |
| **Serverfarm + ADMIE/IPTO** | Attica / Greece unspecified | ADMIE official announcement at https://www.admie.gr/kentro-typoy/nea/synergasia-admie-kai-serverfarm-gia-tin-anaptyxi-kai-leitoyrgia-ypersyghronon-data confirms cooperation intent for hyperscale-ready datacenters. Track cautiously because regulated TSO participation may be subject to RAEEY limits/approvals. | A/B for announcement; C for facility until sited/permitted |
| **OTE / COSMOTE** | Attica: Renti, Acharnon/Athens; Central Macedonia: Thessaloniki | Uptime Institute lists Rentis Data Center for OTE/Cosmote; Aktor describes OTE Renti conversion. Datacenters.com/DataCenterMap list additional OTE/Cosmote locations; verify against OTE/Cosmote, permits, Uptime, and EETT. | A/B for Rentis; C+ for directory-only sites |
| **Lancom** | Attica: Athens/Marousi; Central Macedonia: Thessaloniki/Balkan Gate; Crete: Heraklion lead | Official Lancom datacenter page and directories seed facilities. Verify exact addresses/capacity through operator pages, GR-IX/PeeringDB, and permits. | A/B |
| **Synapsecom Telecoms** | Attica: Ano Liosia; Central Macedonia: Kalochori/Thessaloniki | Official website lists Athens HQ and Thessaloniki branch; official Thessaloniki DC page confirms colocation. Directories and LinkedIn say two DCs in Athens/Thessaloniki; verify facility details. | A/B |
| **Grid Telecom + Quadrivium Digital** | Crete: Chania | Official Grid Telecom announcement says the new Chania CLS will be hosted within Quadrivium's 20 MW Interconnection Data Centre campus. Count CLS and datacenter campus separately; verify campus status through permits/operator pages. | A/B |
| **Sparkle / TIM Group** | Crete: Chania; Attica connectivity | BlueMed/cable landing and Chania data-center/connectivity leads. Verify facility-grade claims against Sparkle pages and permits. | B |
| **Vodafone Greece** | Crete: Tympaki landing; Attica/Milos cable route | 2Africa/Thetis Express connectivity leads and telco DC estate. Cable landing is not datacenter evidence. | B |
| **Nova / United Group** | Attica/Thessaloniki likely telco estate | Telco hosting leads; validate via EETT and official/operator pages. | B/C |
| **GRNET / EDYTE, G-Cloud, Daidalos/Faros** | Attica: Lavrio/Athens; Central Macedonia: Thessaloniki; national research network | Public/research infrastructure, not commercial colocation unless census includes government/HPC. Use GSIS/GRNET official pages and procurement. | A for program/operator; B for physical hosting if indirect |
| **Small hosters / edge providers** | Mostly Attica and Thessaloniki | Webhosting, managed-hosting, and enterprise server-room providers are often directory-only. Count only if facility-grade evidence exists. | C |

---

## 3. Industry Query Templates

### 3.1 Facility Discovery

```text
"{operator}" "data center" Greece "{city}"
"{operator}" "κέντρο δεδομένων" "{πόλη ή δήμος}"
"{operator}" Greece colocation MW OR MVA OR racks OR sqm
"{operator}" "Athens" "data center" "opened" OR "launched" OR "groundbreaking"
"{operator}" "Αθήνα" "data center" "κατασκευή" OR "εγκαινιάστηκε"
"{company}" "{municipality}" "data center" "ΑΕΠΟ" OR "οικοδομική άδεια"
"Greece" "data center" pipeline "Athens" OR "Thessaloniki" OR "Crete" OR "Volos"
```

### 3.2 Cloud Region / Hyperscaler Pivot

```text
"Azure" "Greece Central" "coming soon" OR "available" OR "GA"
site:learn.microsoft.com "Greece Central" "Azure regions list"
site:azure.microsoft.com "Greece Central" "Coming soon"
"Microsoft Operations 4733 Hellas" "data center"
"AWS" Greece "data center" "region" OR "local zone" OR "edge"
"Google Cloud" Greece "region" OR "Athens" "PoP"
"Oracle Cloud" Greece "public cloud region"
"IBM Cloud" Greece "data center"
```

### 3.3 Connectivity / IXP / Cable Pivot

```text
"GR-IX" Athens "Digital Realty" OR "facility"
"GR-IX" Thessaloniki members facility
"DE-CIX" Athens "data center" OR "enabled site"
"Greece" "cable landing station" "data center"
"Chania" "data center" "cable landing station"
"Heraklion" "HER1" "Digital Realty"
"Tympaki" "2Africa" "Vodafone"
"Thetis Express" Crete Milos Athens
"BlueMed" Chania "data center"
```

### 3.4 Status Words

- Intent/land only: `MoU`, `memorandum`, `exploring`, `plans`, `πρόθεση`, `μνημόνιο`, `ανακοίνωση`, `συμφωνία`.
- Permit evidence: `ΑΕΠΟ`, `ΜΠΕ`, `οικοδομική άδεια`, `γνωστοποίηση λειτουργίας`, `pre-approval`, `environmental approval`.
- Construction: `groundbreaking`, `breaking ground`, `under construction`, `έναρξη εργασιών`, `κατασκευή`, `εργοτάξιο`.
- Operational: `opened`, `launched`, `operational`, `live`, `in service`, `λειτουργεί`, `θέση σε λειτουργία`, facility page accepting colocation orders, active PeeringDB local facility.

---

## 4. Cloud Regions and Cloud-Adjacent Signals

| Provider | Official source | Greece signal | Enumeration rule |
|---|---|---|---|
| Microsoft Azure | Announcement: https://news.microsoft.com/europe/2020/10/05/microsoft-announces-plans-for-first-datacenter-region-in-greece-as-part-of-gr-for-growth-digital-transformation-initiative/; Microsoft Local: https://local.microsoft.com/communities/emea/greece/; strategic investment: https://ependyseis.mindev.gov.gr/en/stratigikes/erga/investment-in-data-centres-in-greece-2; regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list | Greece Central/Athens announced and under Attica buildout. Strategic-investment page confirms three Attica DC sites and MW. | Do not mark cloud region operational unless current Azure list/API shows Greece Central available. Count physical projects by official permit/status evidence. |
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No official AWS Greece region identified in current methodology. | Press about Amazon/hyperscale interest is C until AWS or permitting evidence appears. |
| Google Cloud | https://cloud.google.com/about/locations | No official Google Cloud Greece region identified; PoP/CDN/network presence may exist. | Track as connectivity/cloud-edge lead only. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No official Greece public cloud region identified. | Re-check current official region list every run. |
| IBM Cloud | https://www.ibm.com/cloud/data-centers/ | No official Greece cloud region identified. | Directory-only entries are C. |

---

## 5. Per-Division Industry Routing (13 Regions + Mount Athos)

| Division | Industry approach |
|---|---|
| **Mount Athos / Άγιο Όρος** | Negative control. Search only for false positives; exclude monastery ICT rooms and telecom shelters unless the census explicitly includes non-commercial edge rooms. |
| **Eastern Macedonia and Thrace / Ανατολική Μακεδονία και Θράκη** | Sweep Alexandroupoli, Kavala, Komotini, Xanthi, Drama for energy-hub and edge announcements. Use terms `Alexandroupoli data center`, `Αλεξανδρούπολη κέντρο δεδομένων`, `Kavala datacenter`. Count nothing from energy/security narratives alone. |
| **Central Macedonia / Κεντρική Μακεδονία** | High-priority Thessaloniki market. Start with Lancom, Synapsecom, OTE/Cosmote, GR-IX::Thessaloniki, Balkan Gate, Kalochori/Ionia/Sindos/Thessaloniki metro. Verify hyperscale rumors through permits. |
| **Western Macedonia / Δυτική Μακεδονία** | Watch power-transition, brownfield industrial, and cheap-power narratives in Kozani/Ptolemaida/Florina. Require official records; most leads are speculative. |
| **Epirus / Ήπειρος** | Ioannina/university/edge sweep. Use operator plus `Ioannina`, `Ιωάννινα`, `University of Ioannina`, `GRNET`. Usually public/edge rather than commercial colo. |
| **Thessaly / Θεσσαλία** | Medium-priority because Volos appears in market-report pipeline. Search Volos, Larissa, Trikala, Karditsa with operator/permit terms. Treat Trikala smart-city/server-room material as edge unless facility-grade. |
| **Ionian Islands / Ιόνια Νησιά** | Cable/edge sweep for Corfu, Kefalonia, Zakynthos, Lefkada. Use subsea maps only as leads. |
| **Western Greece / Δυτική Ελλάδα** | Patras research/telecom/science-park sweep plus Agrinio/Pyrgos. Validate through GRNET, university procurement, operator pages, and permits. |
| **Central Greece / Στερεά Ελλάδα** | Attica spillover sweep around Oinofyta, Thiva, Chalkida, Lamia. Industrial land and grid capacity are siting leads, not facilities. Search Greek municipality names. |
| **Attica / Αττική** | Core market. Start with Microsoft Spata/Koropi, Digital Realty/Lamda Hellix Koropi, DATA4 Paiania, EDGNEX/Data In Scale Spata, Dromeus/Apto Spata, Serverfarm/ADMIE, OTE/Cosmote Rentis/Acharnon, Lancom Athens, Synapsecom Athens, GR-IX Athens, DE-CIX Athens. Deduplicate brand/SPV/campus names aggressively. |
| **Peloponnese / Πελοπόννησος** | Corinth and Megalopolis are the main speculative pivots; Kalamata/Tripoli secondary. Require operator page or permits. |
| **North Aegean / Βόρειο Αιγαίο** | Edge-only sweep for Lesbos/Mytilene, Chios, Samos, Lemnos, Ikaria. Count telecom shelters/server rooms only if scope allows. |
| **South Aegean / Νότιο Αιγαίο** | Cable-node and island-edge sweep. Milos is relevant for Thetis Express; Rhodes/Kos/Syros/Santorini for edge demand. Cable node is not a datacenter. |
| **Crete / Κρήτη** | Medium/high. Start with Digital Realty HER1 Heraklion, Chania Grid Telecom/Quadrivium CLS and 20 MW Interconnection DC campus, Sparkle/BlueMed, Vodafone/2Africa Tympaki, Thetis Express Crete-Milos-Athens, Lancom Heraklion lead, FORTH/GRNET research infrastructure. Verify island power/interconnector assumptions before counting capacity. |

---

## 6. Verification and Deduplication Rules

- **Always back-resolve industry leads to official records** where possible: Diavgeia, e-PRM, e-adeies, OpenBusiness, strategic-investment portal, ADMIE/HEDNO/RAEEY, EETT, ΓΕΜΗ.
- **Grade per data point.** Example: Microsoft Attica sites are A for strategic-investment existence and site powers from the ministry page, B for contractor progress unless permit-backed, and not operational unless Microsoft/Azure or official operating evidence says so.
- **Separate capacity fields:** `IT load`, `installed electrical power`, `grid connection`, `total campus capacity`, and `future expansion`. Directories often mix them.
- **Deduplicate by:** legal SPV + municipality + campus/site name + operator facility code + permit/AEO/AEEP/ADA. Record former names such as Lamda Hellix under Digital Realty.
- **Do not count these as datacenters by themselves:** Azure region announcement, ExpressRoute/Front Door PoP, GR-IX/DE-CIX node, submarine cable landing, grid connection request, land acquisition, investment budget, MoU, or public-sector server-room procurement.
- **Operational requires live evidence:** operator facility page offering service, commissioning/launch announcement, Uptime/PeeringDB active-facility evidence, operating notification/license, or cloud-region GA status.
- **Re-check fast-changing sources every run:** Azure/AWS/Google/Oracle official region lists, GR-IX/PeeringDB facilities, Digital Realty/DATA4 operator pages, and ADMIE grid/connection-request reporting.
