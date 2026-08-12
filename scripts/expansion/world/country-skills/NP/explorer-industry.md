# NP Explorer Industry - Nepal Datacenter Discovery Methodology

Date: 2026-08-12. Review status: **FINAL**. Scope: industry, trade press, operator-parent, vendor, directory, IXP, connectivity, hyperscaler, certification, and multilingual search methods for Nepal datacenter enumeration. Division model: **single country-level division `-`** per `world-manifest.jsonl`; the 7 provinces are used as a completeness checklist. Reliability grades are field-scoped: **A** = primary operator/government/cloud-region-list/IXP/PeeringDB/certifier record; **B** = credible trade, local, legal, partner, or vendor source with named facts; **C** = directory, broker listing, market report, social post, or weak repost; **U** = unverified after the current check.

## 0. Discovery model

The official starting point is now DoIT's public roster of listed data center and cloud service providers: https://doit.gov.np/pages/details-of-listed-data-center-and-cloud/ . Treat it as A-grade provider evidence and pair it with operator pages, addresses, IXP/PeeringDB, tenders, and press to decide whether a countable physical facility exists.

Discovery inputs:

1. DoIT listed providers: Ncell Axiata Ltd; Access World Tech Pvt. Ltd; Silver Lining Pvt. Ltd; Data Hub Pvt. Ltd; Dish Media Network Ltd; Digital Network Solution (Everest Cloud, cloud only); Times Global Pvt Ltd.
2. Operator-primary pages: Ncell, DataHub, Cloud Himalaya, Nepal Telecom, WorldLink/Data World if an operator page is found, Vianet, Subisu, DishHome/Dish Media Network, Access World, Silver Lining, Times Global, Everest Cloud/Digital Network Solution, NREN.
3. Strong press and trade: DatacenterDynamics, NepaliTelecom, ICT Frame, TechSansar, The Himalayan Times, Republica/MyRepublica, The Kathmandu Post/Kantipur, NepalNews, OnlineKhabar, New Business Age, Developing Telecoms.
4. Connectivity evidence: NPIX, PeeringDB, PCH, bgp.he.net, ISP ASN pages. Connectivity is a pivot, not a facility proof.
5. Directories and market reports: DatacenterMap, Datacenters.com, DC Byte, Baxtel, Inflect, DataCentersList, servers.expert, Mordor/Arizton/6Wresearch-style reports. These are C-grade leads unless matched to primary evidence.
6. Multilingual searches: English and Nepali first; use Chinese/Korean/Indian vendor terms only for Huawei/KOICA/Airtel Nxtra-style leads.

Do not count brands, reseller pages, CDN caches, cloud PoPs, IXP nodes, network exchanges, NOCs, office buildings, or enterprise server rooms without explicit facility evidence.

## 1. Search vocabulary

```text
data center / datacenter / data centre
डाटा सेन्टर / डेटा सेन्टर / डाटासेन्टर / डाटा केन्द्र
IDC / आईडीसी
colocation / co-location / colo / कोलोकेशन / को-लोकेशन
hosting / होस्टिङ / होस्टिंग
cloud / cloud service / क्लाउड / क्लाउड सेवा
server room / server farm / सर्भर / सर्भर रुम / सर्भर फार्म
Internet Exchange / IXP / इन्टरनेट एक्सचेन्ज
listed / enrolled / certified / सूचीकृत / दर्ता / प्रमाणित
opening / launch / inauguration / उद्घाटन / सुरु
construction / tender / award / निर्माण / ठेक्का
investment / लगानी
power / electricity / substation / विद्युत / सबस्टेशन
Tier / Rated / ANSI/TIA-942 / Uptime Institute / टियर
racks / र्याक / MW / मेगावाट
AI / GPU / sovereign compute / एआई
```

Province/city terms:

```text
Koshi कोशी: Biratnagar विराटनगर, Dharan धरान, Itahari इटहरी, Jhapa झापा
Madhesh मधेश: Birgunj वीरगन्ज, Janakpur जनकपुर, Rajbiraj राजविराज
Bagmati बागमती: Kathmandu काठमाडौं/काठमाण्डौ, Lalitpur ललितपुर, Nakkhu नख्खु, Bhaktapur भक्तपुर, Hetauda हेटौडा, Chandragiri चन्द्रागिरि, Syuchatar स्युचाटार, Chitwan चितवन
Gandaki गण्डकी: Pokhara पोखरा, Kaski कास्की
Lumbini लुम्बिनी: Butwal बुटवल, Tilottama तिलोत्तमा, Bhairahawa भैरहवा, Siddharthanagar सिद्धार्थनगर, Nepalgunj नेपालगन्ज, Kohalpur कोहलपुर
Karnali कर्णाली: Surkhet सुर्खेत, Birendranagar वीरेन्द्रनगर, Jumla जुम्ला
Sudurpashchim सुदूरपश्चिम: Dhangadhi धनगढी, Mahendranagar महेन्द्रनगर, Attariya अत्तरिया
```

General templates:

```text
"{operator}" Nepal ("data center" OR datacenter OR "data centre" OR IDC OR colocation OR cloud OR racks OR MW OR Tier)
"{operator}" ("डाटा सेन्टर" OR "डाटा केन्द्र" OR क्लाउड OR कोलोकेशन OR सर्भर)
"{operator}" (Nakkhu OR Nakhu OR Chandragiri OR Butwal OR Tilottama OR Bhairahawa OR Hetauda OR Pokhara OR Biratnagar OR Kohalpur) (IDC OR colocation OR server OR DC)
"{city}" Nepal ("data center" OR "डाटा सेन्टर") (opening OR launch OR construction OR tender OR उद्घाटन OR निर्माण OR लगानी)
"Nepal" ("data center" OR datacenter OR "data centre") 2025 2026 (launch OR plan OR investment OR AI OR GPU OR certification)
"Nepal" ("ANSI/TIA-942" OR "Uptime Institute" OR "Tier III" OR "Tier 3" OR "Tier-4")
```

## 2. High-signal source map

| Source | Route/search | Use | Grade |
|---|---|---|---|
| DoIT roster | https://doit.gov.np/pages/details-of-listed-data-center-and-cloud/ | Current official provider list; use before directories. | A for provider listing. |
| Ncell | https://www.ncell.com.np/en/business/blogs/ncell-data-center ; https://cloudsuite.ncell.com.np/data-center.html | Nakkhu IDC, Ncell Cloudsuite, certifications and operator claims. | A for operator-owned facts; cert details need certifier or current press. |
| DataHub | https://datahub.com.np/about-us/ ; https://datahub.com.np/services/data-center/our-data-centers/ ; https://datahub.com.np/yeti-cloud/ | Dual Kathmandu/Butwal DCs, colo/cloud, Yeti Cloud. | A for operator-owned facts. |
| Cloud Himalaya | https://www.cloudhimalaya.com/ ; https://www.cloudhimalaya.com/colocation/ | Colocation/cloud provider and Tier marketing claims. | A for existence/offerings; U/B for Tier-4 until certifier proof. |
| DatacenterDynamics | https://www.datacenterdynamics.com/en/tags/nepal/ ; search `site:datacenterdynamics.com Nepal data center` | WorldLink launch, Ncell launch, DataHub/Hosted AI YetiCloud.ai. | B. |
| NepaliTelecom | https://www.nepalitelecom.com/ ; search `site:nepalitelecom.com ("data center" OR "डाटा सेन्टर")` | NTC/Huawei project, Ncell Nakkhu/Tier-3 coverage, WorldLink, Vianet fire, YetiCloud.ai, directive. | B. |
| ICT Frame | https://ictframe.com/ ; search `site:ictframe.com ("data center" OR "डाटा सेन्टर")` | Ncell feature, CG Telecom Satungal lead, Digital Nepal coverage. | B/C depending sourcing. |
| TechSansar | https://techsansar.com/ ; search `site:techsansar.com ("data center" OR AI OR GPU OR budget OR Syuchatar)` | YetiCloud.ai, AI compute center, budget ICT lines. | B. |
| NepalNews / The Himalayan Times / Republica / Kantipur | https://english.nepalnews.com/ ; https://thehimalayantimes.com/ ; https://myrepublica.nagariknetwork.com/ ; https://ekantipur.com/en | AI compute scrutiny, Hetauda DRC, mandatory listing directive. | B. |
| Developing Telecoms / Fast Mode / New Business Age | https://developingtelecoms.com/ ; https://www.thefastmode.com/ ; https://newbusinessage.com/ | Regional telecom/DC coverage, Ncell listed-provider story. | B. |
| NPIX / PeeringDB / PCH | https://www.npix.net.np/ ; https://www.peeringdb.com/ ; https://www.pch.net/ixp/details/159 | IXP and ASN/facility pivots. | A for direct records; not facility proof alone. |
| Directories | https://www.datacentermap.com/nepal/ ; https://www.datacenters.com/locations/nepal ; https://www.dcbyte.com/ ; https://baxtel.com/data-center/nepal ; https://inflect.com/datacenters/asia/nepal | Address/spec leads and dedup hints. | C. |

## 3. Operator and facility seed list

| Operator/facility | Evidence routes | Handling |
|---|---|---|
| Ncell Nakkhu IDC, Lalitpur | Ncell pages; DoIT listed-provider roster; DCD Ncell launch; NepaliTelecom and The Himalayan Times Tier-3 certification coverage; TIA list check https://tiaonline.org/942-datacenters/ | Operational. **A** for operator page and DoIT listing; **B** for launch/specs if only press; certification should be **A** only if TIA/certifier listing is captured, otherwise **B** from press/operator. Ncell marketing now says nationwide multi-site presence; record non-Nakkhu sites only if physically named. |
| DataHub Kathmandu + Butwal/Tilottama | DataHub operator pages; DoIT roster; DCD DataHub/Hosted AI; TechSansar YetiCloud.ai; Datacenters.com/DataCenterMap leads | Operational. **A** for DataHub dual data-center statement and DoIT listing; **B** for YetiCloud.ai launch timing and Hosted AI partnership from DCD/TechSansar; **C** for directory specs. |
| Cloud Himalaya, Kathmandu | Operator homepage/colocation pages; DoIT roster only if exact entity appears indirectly through listed provider search; directory pages | Operational provider lead. **A** for operator-owned colocation/cloud claim; Tier-4/Tier-3 wording is **U/B** until Uptime Institute/TIA or equivalent certifier confirms. |
| WorldLink / Data World, Chandragiri | DCD WorldLink launch; NepaliTelecom; GadgetByte; DC Byte; DatacenterMap; search WorldLink site for Data World page | Operational per trade press. **B** until operator-primary page or DoIT/OCR facility evidence is captured. Treat 3.5 MW, 520 racks, Mata Tirtha-substation adjacency as **B/C** depending source; Tier/Edge certification remains **U/B** without certifier. |
| Nepal Telecom Kathmandu/Bhairahawa DC project | NTC site; NepaliTelecom Jan 2025 Huawei award; PPMO/e-GP searches | Planned/construction. **B** from trade press; promote with NTC/PPMO/e-GP award or commissioning. |
| IDMC/GIDC Kathmandu + Hetauda DRC | https://idmc.gov.np/ ; NITC legacy route; The Himalayan Times 2019 Hetauda DRC | Operational government facility/DR. **A** for IDMC/GIDC current services; **B** for older inauguration/support details unless official document captured. |
| Vianet Central Business Park DC | Vianet site; NepaliTelecom/Laganinews/NepaliICT fire/outage coverage | Physical facility lead. **B** for existence from incident reporting; **C/U** for exact address/capacity unless Vianet names the facility. |
| Access World Tech Pvt. Ltd | DoIT roster; PeeringDB/NPIX; operator/site searches | DoIT-listed data center + cloud provider. **A** for listing; **U** for countable facility until address/operator page found. |
| Silver Lining Pvt. Ltd | DoIT roster; exact-name searches | DoIT-listed data center + cloud provider. **A** for listing; **U** for facility without physical site proof. |
| Dish Media Network Ltd | DoIT roster; DishHome/Dish Media searches | DoIT-listed data center + cloud provider. **A** for listing; **U** for facility unless a site is named. |
| Digital Network Solution / Everest Cloud | DoIT roster marks cloud service only | **A** for cloud-only listing; do not count as physical DC without additional evidence. |
| Times Global Pvt Ltd | DoIT roster; exact-name searches | DoIT-listed data center + cloud provider. **A** for listing; **U** for facility without address/site proof. |
| Subisu / CG / NREN / bank DCs | Operator searches, PeeringDB/NPIX, NRB/press | Leads only unless physical DC named. CG Satungal construction reports are **B/C** until company/permit/procurement evidence. |
| NEA internal DC | NEA searches; directory pages | **U/C** unless NEA primary evidence names it. |

## 4. Status mapping

- **Operational:** operator service page tied to a physical site, official roster plus site evidence, commissioning/opening evidence, active public colocation/cloud page, or confirmed government service page.
- **Construction:** official permit, tender/award, EPC contract, utility connection, contractor record, or credible construction reporting.
- **Planned/announced:** budget line, MoU, policy statement, cabinet/ministerial announcement, or press statement without construction/operation.
- **Lead only:** directory/social/market-report/operator-office hint without facility evidence.
- **No projects found:** only after logged English+Nepali province, official, operator, procurement, and connectivity sweeps.

## 5. Connectivity evidence

NPIX/PeeringDB/PCH can confirm networks, IXP presence, and sometimes site hints, but an IXP node is not a datacenter record. Verified routes include PeeringDB IX `npIX DH` at https://www.peeringdb.com/ix/241 and PCH Putalisadak at https://www.pch.net/ixp/details/159 . Use these as pivots for operators on the DoIT roster and major ISPs.

```text
site:peeringdb.com Nepal (NPIX OR npIX OR facility OR "Access World" OR DataHub OR Ncell OR WorldLink OR Cloud Himalaya)
site:pch.net/ixp/details Nepal NPIX Putalisadak
site:bgp.he.net "npIX"
"Nepal Internet Exchange" (Jawalakhel OR Putalisadak OR Kathmandu OR Lalitpur)
"{operator}" PeeringDB (facility OR IXP OR ASN) Nepal
"Nepal" "China" "India" ("optical fiber" OR cross-border OR transit OR bandwidth) ("data center" OR hosting)
"Nepal" submarine cable landing "no direct"
```

## 6. Hyperscaler and cloud handling

As of this review, no official AWS, Google Cloud, Azure, Alibaba Cloud, OCI, or Huawei Cloud region/local-zone list was found naming a Nepal region. Re-check official lists each run before recording this as current.

Official routes:

- AWS regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; Local Zones: https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/
- Google Cloud locations: https://cloud.google.com/about/locations
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Alibaba Cloud regions: https://www.alibabacloud.com/help/en/ecs/product-overview/regions-and-zones
- OCI regions: https://www.oracle.com/cloud/public-cloud-regions/
- Huawei Cloud regions: https://www.huaweicloud.com/intl/en-us/about/global-infrastructure.html

Do not create a Nepal hyperscaler-region facility record from partner access, CDN caches, or foreign Direct Connect/ExpressRoute/Interconnect access. Count local cloud/colo separately: Ncell Cloudsuite/Nakkhu, DataHub/Yeti Cloud/YetiCloud.ai, IDMC/GIDC government cloud, Cloud Himalaya, and any DoIT-listed provider with physical proof.

## 7. Complete division playbook (`-`, organized by province)

| Province | Search posture |
|---|---|
| Bagmati | Highest priority. Confirm Ncell Nakkhu, DataHub Kathmandu, IDMC/GIDC, Hetauda DRC, WorldLink Chandragiri, Cloud Himalaya, Vianet DC/fire lead, NTC Kathmandu project, CG Satungal lead, Syuchatar AI compute announcement. Search Kathmandu/Lalitpur/Bhaktapur/Hetauda/Chandragiri/Syuchatar in English and Nepali. |
| Lumbini | Confirm DataHub Butwal/Tilottama, NTC Bhairahawa, Kohalpur government budget line, Nepalgunj/Bhairahawa enterprise leads, SEZ/industrial-power context. |
| Koshi | Search Biratnagar/Dharan/Jhapa with Ncell/NTC/WorldLink/Vianet/Subisu/DataHub and official province terms. Do not count Ncell network claims without physical source. |
| Gandaki | Search Pokhara/Kaski with Ncell/NTC/ISPs and local business/permits. Likely low yield. |
| Madhesh | Search Birgunj/Janakpur/industrial corridor. Negative expected unless named facility appears. |
| Karnali | Search Surkhet/Birendranagar/Jumla in English and Nepali; negative expected. |
| Sudurpashchim | Search Dhangadhi/Mahendranagar/Attariya in English and Nepali; negative expected. |

Per-province query pack:

```text
"{province_en}" Nepal ("data center" OR datacenter OR IDC OR colocation OR cloud OR "server room")
"{province_ne}" ("डाटा सेन्टर" OR "डेटा सेन्टर" OR सर्भर OR क्लाउड OR कोलोकेशन)
"{city}" Nepal ("data center" OR "डाटा सेन्टर") (opening OR launch OR construction OR tender OR उद्घाटन OR निर्माण)
"{province_en}" Nepal (Ncell OR NTC OR WorldLink OR Vianet OR Subisu OR DataHub OR Cloud Himalaya OR DishHome OR "Access World" OR "Silver Lining" OR "Times Global")
"{province_en}" Nepal (NPIX OR "Internet Exchange" OR PeeringDB OR transit OR substation)
```

## 8. Evidence rules and pitfalls

1. Run DoIT roster first, then resolve each provider to physical facilities. DoIT-listed provider does not automatically equal one facility.
2. Deduplicate Kathmandu/Thapathali/Central Business Park-type leads by operator, address, ASN, service page, and incident reporting before creating separate facilities.
3. Treat `Kathmandu` marketing as Bagmati unless another city is named. DataHub Butwal, NTC Bhairahawa, Hetauda DRC, Kohalpur, and possible Ncell network DCs are the main non-Valley leads.
4. Treat Tier, MW, racks, uptime, "first", "largest", and "sole" as claims unless a certifier, official procurement spec, or engineering document supports them.
5. The Ncell ANSI/TIA-942-C Rated 3 story is strong, but prefer the TIA certified-data-center list or certificate as A-grade certification proof.
6. WorldLink/Data World's Tier-3/Edge-certified language is not A-grade until the certifier is identified.
7. Budget and AI announcements remain planned until a tender, construction, commissioning, or operating service page appears.
8. Social-media and market-report claims about Google/JV/Bichuten-style Nepal DCs remain **U** until primary or strong press evidence appears.
9. Landlocked transit, CDN caches, and NPIX nodes are connectivity context, never DC records.

## 9. Minimal workflow

1. Pull DoIT listed-provider roster and directive.
2. Search each listed provider exactly; classify provider listing, physical site evidence, cloud-only status, and province.
3. Add operator-primary pages for Ncell, DataHub, Cloud Himalaya, NTC, WorldLink, Vianet, DishHome/Dish Media, Access World, Silver Lining, Times Global, Everest Cloud.
4. Search DCD, NepaliTelecom, ICT Frame, TechSansar, NepalNews, Himalayan Times, Republica/Kantipur, New Business Age, Developing Telecoms for launches, certifications, fires, awards, and AI/cloud announcements.
5. Search PPMO/e-GP/NTC for construction and procurement.
6. Run NPIX/PeeringDB/PCH pivots for connectivity corroboration.
7. Run and log 7-province English+Nepali sweeps.
8. Assign field-level grades and statuses. Use `no_projects` only with logged negative sweeps.

## 10. Verified URL index

- DoIT listed providers: https://doit.gov.np/pages/details-of-listed-data-center-and-cloud/
- DoIT directive: https://doit.gov.np/content/12100/data-center-and-claud-service--operations-and/
- Ncell: https://www.ncell.com.np/en/business/blogs/ncell-data-center ; https://cloudsuite.ncell.com.np/data-center.html
- DataHub: https://datahub.com.np/about-us/ ; https://datahub.com.np/services/data-center/our-data-centers/ ; https://datahub.com.np/yeti-cloud/
- Cloud Himalaya: https://www.cloudhimalaya.com/ ; https://www.cloudhimalaya.com/colocation/
- DatacenterDynamics Nepal: https://www.datacenterdynamics.com/en/tags/nepal/
- WorldLink DCD launch: https://www.datacenterdynamics.com/en/news/wordlink-launches-35mw-data-center-in-chandragiri-nepal/
- DataHub/Hosted AI DCD: https://www.datacenterdynamics.com/en/news/datahub-launches-ai-cloud-in-nepal-in-partnership-with-hosted-ai/
- NepaliTelecom: https://www.nepalitelecom.com/ ; https://www.nepalitelecom.com/huawei-build-data-center-of-nepal-telecom ; https://www.nepalitelecom.com/ncell-data-center-nakkhu ; https://www.nepalitelecom.com/worldlink-builds-nepals-largest-data-center-in-chandragiri ; https://www.nepalitelecom.com/directive-for-operation-of-data-center-and-cloud-service-in-nepal
- TechSansar YetiCloud/AI: https://techsansar.com/computing/yeticloud-ai-nepal-sovereign-compute/ ; https://techsansar.com/featured/nepal-sovereign-ai-compute-center-syuchatar-technical-explainer/
- NepalNews AI scrutiny: https://english.nepalnews.com/s/feature/nepals-ai-compute-center-plan-draws-scrutiny-over-feasibility-and-risks/
- Himalayan Times Hetauda/Ncell searches: https://thehimalayantimes.com/
- NPIX/Peering: https://www.npix.net.np/ ; https://www.peeringdb.com/ix/241 ; https://www.pch.net/ixp/details/159 ; https://bgp.he.net/exchange/npIX
- Directories/leads: https://www.datacentermap.com/nepal/ ; https://www.datacenters.com/locations/nepal ; https://www.dcbyte.com/
- Hyperscaler lists: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ ; https://cloud.google.com/about/locations ; https://learn.microsoft.com/en-us/azure/reliability/regions-list ; https://www.alibabacloud.com/help/en/ecs/product-overview/regions-and-zones ; https://www.oracle.com/cloud/public-cloud-regions/ ; https://www.huaweicloud.com/intl/en-us/about/global-infrastructure.html
