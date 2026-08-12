# BD Explorer Industry - Bangladesh Datacenter Discovery Methodology

Date: 2026-08-12. Review status: final methodology after live URL/source checks and fresh web research. Scope: industry, trade press, operator-parent, vendor, directory, IXP, connectivity, hyperscaler, and multilingual search methods for Bangladesh datacenter enumeration. Division model: **division** (8 divisions). Reliability grades are field-scoped: **A** = primary operator/government/cloud-region-list/IXP/PeeringDB record; **B** = credible trade, local, legal, or parent-company source with named facts; **C** = aggregate market report, directory, broker listing, social post, or weak repost; **U** = unverified after the current check.

## 0. Discovery model

Bangladesh has no public datacenter registry. Enumerate by triangulating:

1. Operator-primary pages: BDCCL/Meghna Cloud, BCC NDC, Felicity IDC, Fiber@Home, DhakaColo/BDCOLO, ColoAsia, Rajshahi COLO, CoLoCity, Colocloud, BengalCloud/ADNGateway, XeonBD, Aamra, MNOs, BTCL, BSCCL/BSCPLC.
2. IXP/connectivity evidence: BDIX and PeeringDB for active network/facility signals; SMW-4 Cox's Bazar, SMW-5 Kuakata, and SMW-6 status checks for cable geography.
3. Official support: RJSC, BTRC, BHTPA, BIDA/BEZA/BEPZA, e-GP/BPPA, Planning Commission/IMED, utility/development authorities.
4. High-signal press: DatacenterDynamics, W.Media, The Business Standard, Daily Star, Dhaka Tribune, UNB/BSS, New Age, Financial Express, Prothom Alo, bdnews24, Developing Telecoms.
5. Directories and market reports: DatacenterMap, Datacenters.com, DataCentersList, Baxtel, Inflect, OCOLO, DCPulse, DC Atlas, colocation.bd, Mordor/Arizton/6Wresearch. These are leads unless operator-controlled.
6. Multilingual sweeps: Bengali first, plus English spelling variants and company-country language pivots for Indian/Saudi/Chinese vendors.

Market context is useful but not facility proof. Demand drivers include government e-services and sovereign cloud, fintech/banking, telecom/OTT growth, data-protection/localization signals, Smart Bangladesh policy, CDN/IXP growth, and AI/GPU cloud interest. Risk context includes grid reliability, gas shortage, forex controls, land/power cost, cyclone/flood exposure, and seismic concerns around some sites.

## 1. Search vocabulary

Core terms:

```text
data center / datacenter / data centre
ডেটা সেন্টার / ডাটা সেন্টার / ডেটাসেন্টার
IDC / আইডিসি
colocation / co-location / colo / কোলোকেশন
hosting / হোস্টিং
cloud / ক্লাউড
server / server room / সার্ভার / সার্ভার রুম
server farm / সার্ভার ফার্ম
digital infrastructure / ডিজিটাল অবকাঠামো
Internet Exchange / IXP / ইন্টারনেট এক্সচেঞ্জ
submarine cable / cable landing / সাবমেরিন ক্যাবল / সাবমেরিন কেবল
license / licence / লাইসেন্স
opening / launch / inauguration / উদ্বোধন / চালু
construction / নির্মাণ
investment / বিনিয়োগ
power / electricity / বিদ্যুৎ
Tier / টিয়ার
racks / র্যাক
MW / মেগাওয়াট
```

Division names:

```text
Barishal বরিশাল
Chattogram / Chittagong চট্টগ্রাম
Dhaka ঢাকা
Khulna খুলনা
Rajshahi রাজশাহী
Rangpur রংপুর
Sylhet সিলেট
Mymensingh ময়মনসিংহ
```

General templates:

```text
"{division_en}" Bangladesh ("data center" OR datacenter OR IDC OR colocation OR cloud OR "server room")
"{division_bn}" ("ডেটা সেন্টার" OR "ডাটা সেন্টার" OR সার্ভার OR কোলোকেশন OR ক্লাউড)
"{company}" Bangladesh ("data center" OR IDC OR colocation OR racks OR MW OR Tier)
"{company}" ("ডেটা সেন্টার" OR "সার্ভার" OR "কোলোকেশন")
"{town}" ("data center" OR "ডেটা সেন্টার") (opening OR launch OR উদ্বোধন OR চালু)
"{operator}" (Dhaka OR Chattogram OR Sylhet OR Khulna OR Jashore OR Rajshahi OR Rangpur) (colocation OR server OR NOC OR BDIX)
```

Status mapping:

- **Operational:** active operator service page, official opening, active PeeringDB/facility evidence, or public colocation/cloud price/service page tied to a physical site.
- **Construction:** permit, utility connection, official groundbreaking, EPC/PPP award, or site progress evidence.
- **Approved/planned:** cabinet approval, MoU, tender, investment approval, or announcement without operation/construction proof.
- **Lead only:** directory/social/market-report mention without primary or strong press confirmation.
- **No projects found:** only after logged English+Bengali, operator, official, and connectivity sweeps.

## 2. High-signal sources

| Source | Route | Use | Grade |
|---|---|---|---|
| DatacenterDynamics | https://www.datacenterdynamics.com/en/tags/bangladesh/ ; search `site:datacenterdynamics.com Bangladesh data center` | Meghna launch, GP Sylhet, Yotta, DataVolt, BTCL/ADB, Summit, historical NDC approval. | B |
| W.Media | https://w.media/ ; `site:w.media Bangladesh data center` | Meghna/BDCCL and DataVolt/APAC leads. | B |
| The Business Standard | https://www.tbsnews.net/ ; `site:tbsnews.net "data centre" Bangladesh` | BTCL/ADB green DC, GP Sylhet, Summit plans. | B |
| Daily Star / Dhaka Tribune / Prothom Alo | https://www.thedailystar.net/ ; https://www.dhakatribune.com/ ; https://en.prothomalo.com/ | Launch reports, legal/policy reports, telecom/regulatory risk. | B |
| UNB / BSS / New Age / Financial Express | https://unb.com.bd/ ; https://www.bssnews.net/ ; https://www.newagebd.net/ ; https://thefinancialexpress.com.bd/ | MoUs, wire-level government announcements, telecom launches. | B |
| Developing Telecoms / TelecomTalk | https://developingtelecoms.com/ ; https://telecomtalk.info/ | Telco DC confirmation, especially GP Sylhet. | B/C |
| BDIX / SDNF / PeeringDB | https://bdix.net/ ; https://www.sdnf.org.bd/bdix/ ; https://www.peeringdb.com/ix/2516 | IXP facts, membership, possible facility/network mapping. | A for direct IXP/PeeringDB facts |
| Submarine Networks / Submarine Cable Map | https://www.submarinenetworks.com/en/stations/asia/bangladesh ; https://www.submarinecablemap.com/ | Cable landing and system status. | A/B for cable facts; not DC proof |

Search pack:

```text
site:datacenterdynamics.com Bangladesh ("data center" OR datacenter OR "green data centre" OR submarine)
site:w.media Bangladesh ("data center" OR datacenter OR "digital infrastructure")
site:tbsnews.net Bangladesh ("data centre" OR "data center" OR Summit OR BTCL OR Grameenphone)
site:thedailystar.net OR site:dhakatribune.com Bangladesh ("data centre" OR "data center" OR Meghna OR BTRC)
site:unb.com.bd OR site:bssnews.net Bangladesh ("green data centre" OR "data center" OR submarine)
"{company}" Bangladesh ("data center" OR IDC OR colocation) 2024 2025 2026
```

## 3. Market and directory sources

| Source | URL/search | Use | Grade |
|---|---|---|---|
| DatacenterMap | https://www.datacentermap.com/bangladesh/ and city/facility pages | Seed facilities and addresses; counts vary. | C |
| Datacenters.com | https://www.datacenters.com/locations/bangladesh | Provider/facility leads including DhakaColo, ColoAsia, region pages. | C |
| DataCentersList | https://www.datacenterslist.com/data-centers/country/bd | Active/planned/under-construction leads. | C |
| Baxtel | https://baxtel.com/data-center/bangladesh | Small curated market leads, notably GP Sylhet. | C |
| Inflect | https://inflect.com/datacenters/apac/bangladesh/dhaka and ColoAsia building pages | Building-level leads. | C |
| OCOLO / DC Atlas / DCPulse | https://www.ocolo.io/ ; https://dcatlas.io/ ; https://dcpulse.com/ | Facility/project trackers; good for leads, not final proof. | C |
| colocation.bd | https://colocation.bd/ ; https://colocation.bd/Data_Centers/ | Local aggregator with many BD colo pages. | C unless clearly operator-controlled |
| Mordor/Arizton/6Wresearch/Expert Market Research | `"Bangladesh data center market"` | Market sizing and operator lists only. | C |

Never cite directory counts as authoritative. Use them to generate search targets, then verify via operator page, official record, PeeringDB, press, or procurement.

## 4. Operator and facility seed list

| Operator/facility | URLs | Evidence handling |
|---|---|---|
| BDCCL National Data Centre / 4TDC + Meghna Cloud | https://bdccl.gov.bd/ ; https://bdccl.portal.gov.bd/ ; https://www.meghnacloud.com/ ; https://docs.meghnacloud.com/ ; DCD https://www.datacenterdynamics.com/en/news/bangladeshs-first-cloud-data-center-starts-operations/ | State-owned/sovereign-cloud anchor at Bangabandhu Hi-Tech City, Kaliakair, Gazipur. **A** existence/service/location from official pages; **B** launch, size, generators, JV/capex from press; certify Tier claims separately. |
| BCC National Data Center | https://ndc.bcc.gov.bd/ ; https://bcc.gov.bd/ | Government NDC at ICT Tower, Agargaon, Dhaka, with cloud/VPS/colocation/service documents. **A**. |
| Felicity IDC | https://felicity.net.bd/ ; Uptime https://uptimeinstitute.com/component/tierachievement/client/felicity-idc-limited/923 ; PeeringDB org https://www.peeringdb.com/org/40434 | Kaliakair Hi-Tech Park carrier-neutral DC. **A** for operator page and Uptime client/certification existence; operator marketing for sq ft/racks/MW is **A** as claim, **B** as engineering fact unless independently supported. |
| Fiber@Home | https://www.fiberathome.net/co-location | Colocation service from major NTTN/ISP. **A** for service page; site granularity and customer-facing physical location need more evidence. |
| DhakaColo / BDCOLO | https://www.dhakacolo.com/ ; https://www.dhakacolo.com/about-us/ ; https://www.dhakacolo.com/our-data-center/ ; https://bdcolo.net/about ; Cataleya partner note https://cataleya.com/cataleya-and-dhaka-colo-partner-to-launch-orchid-cloud-sbc-node-in-bangladesh/ | Operator claims chain in Dhaka, Chattogram, Jashore, Khulna, Sylhet; own pages also say 3 DCs in places, so reconcile per site. **A** for operator claim; **C** for directory addresses until individually verified. |
| ColoAsia | https://www.coloasiabd.com/ ; https://colocation.bd/Data_Center/ColoAsia.html ; Inflect Jashore https://inflect.com/building/7-r-north-road-jessore/coloasia/datacenter/dc2 | Operator-owned page says 5 DCs; aggregator pages name Dhaka, Jashore, Sylhet, Bogura. Treat operator existence as **A**, individual addresses as **C** until primary page/RJSC/PeeringDB confirms. |
| Rajshahi COLO | https://rajshahicolo.com/ ; https://rajshahicolo.com/colocation/ | Rajshahi city colo/BDIX service. **A** for live operator service; **C/U** for Tier/date/address claims without independent proof. |
| CoLoCity | https://colocity.com.bd/ ; history lead https://industryinsiderbd.com/billions-down-the-drain-as-state-run-data-centers-faltered/ | Mohakhali/Dhaka carrier-neutral colocation. **A** for operator service; **C/B** for historical first/Tier claims. |
| Colocloud | https://colocloud.com.bd/ ; https://colocation.bd/Data_Center/Colocloud.html | Claims multiple Bangladesh Tier-3 DC locations. **C** until individual physical sites are proven. |
| BengalCloud / ADNGateway | https://bengalcloud.com/datacenters/ ; subpages for Dhaka/Khulna/Jashore | Operator page claims carrier-neutral network in Dhaka, Khulna, Jashore; Khulna page gives BDBL Bhaban/KDA area. **A** for operator claim, **C/U** for site independence and underlying host. |
| Aamra Technologies | https://www.aamratechnologies.com/ ; directory https://www.datacenters.com/providers/aamra-technologies-limited | Dhaka-centric infrastructure/hosting leads. **C** until operator page names a physical DC. |
| XeonBD | https://www.xeonbd.com/ ; https://www.xeonbd.com/blog/data-center-bangladesh/ | Local hosting/DC marketing. **C** for facility claims; verify physical site. |
| Grameenphone Super Core DC | DCD https://www.datacenterdynamics.com/en/news/grameenphone-launches-super-core-data-center-in-bangladesh/ ; TBS https://www.tbsnews.net/economy/corporates/gp-unveils-state-art-data-center-sylhet-784674 | Sylhet operational telco DC launched 2024-01-30, 4 MW, GP+ZTE, Tier III standard not Uptime-listed in DCD. **B** until GP primary page found. |
| BTCL/ADB green DC | UNB https://unb.com.bd/category/Business/adb-govt-ink-deal-for-bangladeshs-first-green-data-center/152126 ; TBS https://www.tbsnews.net/bangladesh/bangladesh-establish-first-green-data-centre-adbs-support-1053761 ; DCD https://www.datacenterdynamics.com/en/news/asian-development-bank-and-bangladeshi-govt-plan-green-data-center/ | Planned PPP green data centre near Chattogram on BTCL-owned site. **B** for MoU and announced intent; **U** for construction/operation. |
| BSCCL/BSCPLC landing stations | https://www.bsccl.com.bd/ ; https://www.submarinenetworks.com/en/stations/asia/bangladesh ; Kuakata https://www.submarinenetworks.com/en/stations/asia/bangladesh/kuakata | SMW-4 Cox's Bazar and SMW-5 Kuakata/Patuakhali are cable assets. **A/B** for cable facts; do not count as DCs unless BSCCL names colo/IDC at a landing facility. |
| Yotta Dhaka | DCD https://www.datacenterdynamics.com/en/news/yotta-planning-data-center-park-in-dhaka-bangladesh/ ; DatacenterMap planned page | Announced 2023: two buildings, 4,800 racks, 28.8 MW at Kaliakair with Shamsul Alamin Group. **B/C planned**; no operation found. |
| DataVolt Bangladesh | DCD https://www.datacenterdynamics.com/en/news/datavolt-plans-data-center-in-dhaka-bangladesh/ ; W.Media https://w.media/datavolt-to-invest-100-m-in-data-center-in-bangladeshs-bangabandhu-hi-tech-city/ | Announced 2023: $100m, 3 acres at BHTC. **B/C announced**; construction/operation **U**. |
| Summit Group / Summit Communications DC | Summit https://www.summitcommunications.net/ ; TBS https://www.tbsnews.net/bangladesh/summit-group-plans-first-data-centre-bangladesh-amid-climate-power-challenges-1328186 ; DCD Summit report | 2026 plan near Dhaka using gas/power/fiber assets. **B planned**; no physical facility record yet. |
| Wolast, A Cloud Planet, Nova Colo, ColoBD, Gotipath, SAV, UTSOB, Alpha, HostSeba and other small hosts | DatacenterMap/colocation.bd/operator pages such as https://www.gotipath.com/colocation-bangladesh and https://www.alpha.net.bd/Colocation/ | Treat as **C** leads or reseller services. Do not create separate physical DC records unless facility owner/address/host can be verified. |
| Banglalink / Robi / Teletalk / internal telco DCs | Operator corporate sites | Internal network DCs are plausible but not countable from HQ/service pages alone. **U** until a facility is named. |

## 5. Connectivity evidence

Connectivity is a search pivot, not facility proof.

- BDIX: https://bdix.net/ ; SDNF page https://www.sdnf.org.bd/bdix/ ; PeeringDB https://www.peeringdb.com/ix/2516 . PeeringDB/ISOC Pulse showed active BDIX data in August 2026. **A** for IXP facts, **C/B** for facility inference.
- Chattogram BDIX: search BDIX site and press for Chattogram IX launch; use as Chattogram cluster evidence only.
- SMW-4: Cox's Bazar landing, BSCCL/BSCPLC and Submarine Networks. **A/B** for cable facts.
- SMW-5: Kuakata, Patuakhali (Barishal division), BSCCL/BSCPLC. Submarine Networks page confirms Kuakata CLS and SMW-5; **A/B** for cable facts.
- SMW-6: Submarine Networks currently says SMW-6 is going to connect Bangladesh soon. Keep in-service date **U** and re-check official cable maps and BSCCL.
- Terrestrial links: India cross-border fiber and CDN/cache PoPs are useful pivots; not DC records without physical facility evidence.

Queries:

```text
site:bdix.net OR site:peeringdb.com Bangladesh (BDIX OR facility OR member OR Chattogram)
site:submarinenetworks.com Bangladesh ("Cox's Bazar" OR Kuakata OR SMW-4 OR SMW-5 OR SMW-6)
"SMW-6" Bangladesh landing in service BSCCL 2026
"cable landing" Bangladesh ("data center" OR IDC OR colocation)
"Kuakata" ("data center" OR "landing station" OR IDC OR colocation)
```

## 6. Hyperscaler and cloud handling

As of this review, no public Bangladesh region was found in official AWS, Google Cloud, Azure, Alibaba Cloud, OCI, or Huawei Cloud region/location lists. Re-check official lists every run before recording this as current.

Official routes:

- AWS regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and Local Zones https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/
- Google Cloud locations: https://cloud.google.com/about/locations
- Azure geographies/regions: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies and https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Alibaba Cloud regions: https://www.alibabacloud.com/help/en/ecs/product-overview/regions-and-zones
- Oracle/OCI regions: https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
- Huawei Cloud regions: https://www.huaweicloud.com/intl/en-us/about/global-infrastructure.html and https://support.huaweicloud.com/intl/en-us/productdesc-cc/cc_01_0003.html

Do not create a Bangladesh hyperscaler-region facility record. Record in-country cloud/colo evidence separately: Meghna Cloud, BCC NDC cloud, local colos, or private/on-prem cloud deployments. Direct Connect/ExpressRoute/Interconnect partner access through Bangladeshi carriers is foreign-region access unless the hyperscaler names a Bangladesh edge/region/local zone.

Queries:

```text
"Bangladesh" "cloud region" (AWS OR Azure OR "Google Cloud" OR Alibaba OR Oracle OR OCI OR Huawei)
site:aws.amazon.com Bangladesh "Local Zone"
site:cloud.google.com Bangladesh "region"
site:learn.microsoft.com Azure Bangladesh "region"
"Meghna Cloud" ("Tier IV" OR sovereign OR "data center" OR GPU)
"{colo}" Bangladesh ("Direct Connect" OR ExpressRoute OR Interconnect)
```

## 7. Complete division playbook

| Division | Priority localities | Seeds and search posture |
|---|---|---|
| **Dhaka** | Dhaka city; Gazipur/Kaliakair; Narayanganj; Savar | Highest priority. Confirm BDCCL/Meghna, BCC NDC, Felicity IDC, Fiber@Home, DhakaColo/BDCOLO, ColoAsia Dhaka, CoLoCity, Aamra, XeonBD, BengalCloud/ADNGateway, Gotipath, Wolast, ACP, Nova Colo/ColoBD, Yotta, DataVolt, Summit. |
| **Chattogram** | Chattogram city/Agrabad/Nasirabad; Cox's Bazar; Mirsarai; Cumilla | Verify BTCL/ADB green DC near Chattogram, DhakaColo Chattogram, ColoAsia/NRB leads, Colocloud claims, BDIX Chattogram, Cox's Bazar SMW-4 landing. |
| **Khulna** | Khulna city/KDA area; Jashore; Mongla | Verify DhakaColo Jashore/Khulna, ColoAsia Jashore, BengalCloud Khulna/Jashore, Jashore Software Technology Park. |
| **Rajshahi** | Rajshahi city; Bogura; Pabna | Verify Rajshahi COLO, ColoAsia Bogura claim, Rajshahi hi-tech park. |
| **Rangpur** | Rangpur city; Dinajpur | Verify Colocloud Rangpur and any BHTPA/STP record. Current posture: sparse, likely 0-1 lead only. |
| **Sylhet** | Sylhet city; Moulvibazar/Habiganj | Confirm GP Super Core DC; verify DhakaColo/ColoAsia Sylhet claims and Sylhet hi-tech park/STP. |
| **Mymensingh** | Mymensingh city; Jamalpur; Netrokona; Sherpur | Current sweep found no named commercial DC, only generic directory geography. Run Bengali and English negative sweep; do not count generic provider-map pages as facilities. |
| **Barishal** | Barishal city; Patuakhali/Kuakata; Bhola | Confirm Kuakata SMW-5 cable landing; search for BSCCL/ISP hosting around landing station. Current posture: cable asset, no confirmed commercial DC. |

Per-division query pack:

```text
"{division_en}" ("data center" OR datacenter OR IDC OR colocation OR cloud OR "server room") Bangladesh
"{division_bn}" ("ডেটা সেন্টার" OR "ডাটা সেন্টার" OR সার্ভার OR কোলোকেশন OR ক্লাউড)
"{division_en}" (BDIX OR "Internet Exchange" OR "cable landing" OR submarine)
"{division_en}" (BTRC OR RJSC OR BIDA OR BHTPA) ("data center" OR ICT OR license)
"{division_en}" (Grameenphone OR GP OR Banglalink OR Robi OR Teletalk OR BTCL OR Summit OR "Fiber@Home") ("data center" OR NOC OR server OR colocation)
```

## 8. Evidence rules and pitfalls

- Count physical facilities, not brands, resellers, IXP nodes, CDN caches, cloud PoPs, telecom offices, or cable landing stations.
- Match duplicate brands by address, city, operator, ASN/PeeringDB, customer-facing service page, and directory cross-listing before creating multiple records.
- Treat `Dhaka` marketing as Dhaka division unless a page names another city. DhakaColo/BDCOLO, ColoAsia, BengalCloud, Colocloud, and Rajshahi COLO are the main non-Dhaka operator leads.
- Treat Tier/MW/rack/SLA claims as source claims unless a certifier, procurement spec, or engineering filing supports them. Use Uptime Institute for certification checks.
- Yotta, DataVolt, Summit, and BTCL/ADB remain planned/announced until construction or operation evidence appears.
- Directory pages for Mymensingh/Sherpur or other empty geographies are not evidence of facilities.
- Cable landing stations in Cox's Bazar and Kuakata are telecom infrastructure; record as datacenters only if a source names commercial colocation, server hosting, or a datacenter building at the station.
- Legal/data-localization changes are demand signals, not construction proof.

## 9. Minimal workflow

1. Seed from operator-primary pages and BDIX/PeeringDB.
2. Search RJSC for every operator and SPV variant.
3. Search BTRC/LIMS and e-GP/BPPA for licences, tenders, and government procurements.
4. Search BDCCL/BCC/BHTPA/BIDA/Planning/IMED for official project records.
5. Search DCD, W.Media, TBS, Daily Star, Dhaka Tribune, UNB/BSS, New Age, Financial Express, Prothom Alo, and Developing Telecoms for openings, MoUs, and construction.
6. Run cable and IXP pivots: BDIX Dhaka/Chattogram, SMW-4 Cox's Bazar, SMW-5 Kuakata, SMW-6.
7. Run English+Bengali sweeps for all 8 divisions and log negative searches.
8. Assign field-level grades and status. Use **no_projects** only where the negative sweep is logged.

## 10. Quick URL index

- DCD Bangladesh: https://www.datacenterdynamics.com/en/tags/bangladesh/
- DCD Meghna: https://www.datacenterdynamics.com/en/news/bangladeshs-first-cloud-data-center-starts-operations/
- DCD GP Sylhet: https://www.datacenterdynamics.com/en/news/grameenphone-launches-super-core-data-center-in-bangladesh/
- DCD Yotta: https://www.datacenterdynamics.com/en/news/yotta-planning-data-center-park-in-dhaka-bangladesh/
- DCD DataVolt: https://www.datacenterdynamics.com/en/news/datavolt-plans-data-center-in-dhaka-bangladesh/
- DCD BTCL/ADB: https://www.datacenterdynamics.com/en/news/asian-development-bank-and-bangladeshi-govt-plan-green-data-center/
- TBS BTCL/ADB: https://www.tbsnews.net/bangladesh/bangladesh-establish-first-green-data-centre-adbs-support-1053761
- UNB BTCL/ADB: https://unb.com.bd/category/Business/adb-govt-ink-deal-for-bangladeshs-first-green-data-center/152126
- TBS Summit: https://www.tbsnews.net/bangladesh/summit-group-plans-first-data-centre-bangladesh-amid-climate-power-challenges-1328186
- Felicity: https://felicity.net.bd/ ; Uptime https://uptimeinstitute.com/component/tierachievement/client/felicity-idc-limited/923
- DhakaColo/BDCOLO: https://www.dhakacolo.com/ ; https://www.dhakacolo.com/about-us/ ; https://www.dhakacolo.com/our-data-center/ ; https://bdcolo.net/about
- ColoAsia: https://www.coloasiabd.com/ ; https://colocation.bd/Data_Center/ColoAsia.html
- Rajshahi COLO: https://rajshahicolo.com/
- CoLoCity: https://colocity.com.bd/
- Fiber@Home colo: https://www.fiberathome.net/co-location
- BengalCloud: https://bengalcloud.com/datacenters/
- BDIX/PeeringDB: https://bdix.net/ ; https://www.peeringdb.com/ix/2516
- Submarine Networks Bangladesh: https://www.submarinenetworks.com/en/stations/asia/bangladesh ; Kuakata https://www.submarinenetworks.com/en/stations/asia/bangladesh/kuakata
- Hyperscaler official lists: AWS https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; Google https://cloud.google.com/about/locations ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Alibaba https://www.alibabacloud.com/help/en/ecs/product-overview/regions-and-zones ; OCI https://www.oracle.com/cloud/public-cloud-regions/ ; Huawei https://www.huaweicloud.com/intl/en-us/about/global-infrastructure.html
