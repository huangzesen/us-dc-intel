# NP Explorer Official - Nepal Datacenter Enumeration Methodology

Date: 2026-08-12. Review status: **FINAL**. Scope: official, regulator, registry, ministry, budget/planning, e-procurement, government-IT, utility, cloud-region-list, and operator-primary methods for enumerating datacenter facilities and projects in Nepal (NP). Division model: **single country-level division `-`** per `world-manifest.jsonl` (`subnational_type: province`, `divisions: ["-"]`). Nepal's 7 provinces are used only as the internal coverage checklist. Reliability grades are field-scoped: **A** = official government/registry/law/utility/budget/cloud-region-list, primary IXP/PeeringDB, certifier, or operator-owned source for the fact stated; **B** = credible trade/local press, law-firm analysis, or vendor/partner source naming a project fact; **C** = directory, broker listing, market report, social post, or weak repost; **U** = unverified after the current check.

## 0. Administrative model and coverage requirement

The manifest has no province-level rows for NP. A valid run must therefore produce one country-level output division (`-`) while showing that all 7 provinces were swept.

| Province | Priority localities | Expected posture |
|---|---|---|
| Koshi | Biratnagar, Dharan, Itahari, Birtamod/Jhapa, Damak | Low yield. Ncell/network or enterprise-server-room leads only unless a named facility is found. |
| Madhesh | Birgunj, Janakpur, Rajbiraj, Gaur | Sparse. Industrial-corridor and government IT searches usually negative. |
| Bagmati | Kathmandu, Lalitpur/Nakkhu, Bhaktapur, Hetauda, Bharatpur/Chitwan, Banepa/Kavre, Chandragiri/Syuchatar | Main yield. Government, commercial, telecom, cloud, AI, and connectivity hub. |
| Gandaki | Pokhara, Kaski, Lekhnath/Pokhara metro | Low yield. Check Ncell/ISP network DC leads and local enterprise colo claims. |
| Lumbini | Butwal/Tilottama, Bhairahawa/Siddharthanagar, Nepalgunj/Kohalpur, Palpa | Secondary hub. DataHub Butwal, NTC Bhairahawa project, Kohalpur government budget line. |
| Karnali | Birendranagar/Surkhet, Jumla | Negative sweep expected; record no_projects only after English+Nepali searches. |
| Sudurpashchim | Dhangadhi, Mahendranagar, Attariya | Negative sweep expected; record no_projects only after English+Nepali searches. |

Do not infer a datacenter from a head office, telecom exchange, NOC, CDN/cache node, IXP switch, bank server room, reseller page, or cloud brand unless a source names a physical data center, colocation, cloud infrastructure facility, or government data center site.

## 1. Highest-value official sources

| Source | Verified route | Use | Grade guidance |
|---|---|---|---|
| DoIT directive text | https://doit.gov.np/content/12100/data-center-and-claud-service--operations-and/ ; PDF route observed at `https://giwmscdnone.gov.np/media/pdf_upload/data%20center%20translation_bhnhhri.pdf` | Primary text of the Data Center and Cloud Service (Operation and Management) Directives, 2081. Use for registration/listing, rating, and government-data requirements. | **A** for directive text and regulatory requirements. |
| DoIT listed-provider roster | https://doit.gov.np/pages/details-of-listed-data-center-and-cloud/ | Public roster of listed data center and cloud service providers. Verified listed names on 2026-08-12: Ncell Axiata Ltd; Access World Tech Pvt. Ltd; Silver Lining Pvt. Ltd; Data Hub Pvt. Ltd; Dish Media Network Ltd; Digital Network Solution (Everest Cloud, cloud only); Times Global Pvt Ltd. | **A** for provider listing and whether DoIT marks data-center service and/or cloud service. The roster is not by itself a facility address, capacity, or operational status record. |
| IDMC / government data center | https://idmc.gov.np/ ; older NITC root https://nitc.gov.np/ may time out, so use IDMC first | Government Integrated Data Center / Integrated Data Management Center services, government domain/VM/VPS/colocation/backup/replication, and contacts. | **A** for current government data-center operator route and services when named on IDMC pages. |
| NTA telecom regulator | https://nta.gov.np/ ; https://www.nta.gov.np/ ; standing-list portal https://standinglist.nta.gov.np/ may present TLS certificate problems | Telecom-law and ISP/mobile license context for NTC, Ncell, WorldLink, Vianet, Subisu, DishHome, CG, etc. | **A** for telecom licenses/notices; not the DC/cloud roster unless NTA itself publishes one. |
| Nepal Telecom | https://www.ntc.net.np/ | State telco notices, procurement, legacy network/DC references, Kathmandu/Bhairahawa DC project checks. | **A** for NTC-owned statements; **B** for trade press about awards until NTC/PPMO evidence is found. |
| MoCIT | https://www.mocit.gov.np/ | ICT policy, telecom bill, cyber/data-center directives, AI policy context. | **A** for official policy/notices. Use `www` form; non-www may fail certificate validation. |
| MoF / NPC | https://www.mof.gov.np/ ; https://npc.gov.np/ | Budget speeches/red books, national plans, AI compute center and government DC upgrade lines. | **A** for official budget/planning text; **B** for press summaries. |
| PPMO / e-GP | https://www.ppmo.gov.np/ ; https://bolpatra.gov.np/egp/ | Tenders and awards for DC construction, server rooms, cloud, backup, DR, power, cooling, networking. | **A** for tender/award facts; generic ICT procurement is only a lead. |
| OCR / IRD | https://www.ocr.gov.np/ ; https://ird.gov.np/ | Entity and tax identity for operators and SPVs. | **A** for entity facts only. |
| NEA / ERC | https://www.nea.org.np/ ; https://www.erc.gov.np/ | Power, substations, tariff, outages, hydropower surplus/import risk, feeder validation. | **A** for utility/regulator facts; not facility proof by itself. |
| IBN / DoI / SEZ | https://ibn.gov.np/ ; https://www.doind.gov.np/ ; https://seznepal.gov.np/ | Investment approvals, foreign investment, SEZ/industrial land. | **A** only where a record names a DC project/SPV/site. |
| NRB | https://www.nrb.org.np/ | Bank ICT/BCP requirements and demand context. | **A** for NRB directives; bank internal DCs remain **U** unless physically named. |

## 2. Legal and regulatory workflow

1. Start with DoIT's directive page and PDF. Record that the 2081 directives require DC/cloud service providers to be listed with DoIT and require tier/rating evidence; sources summarizing the directive report that government-data-hosting DCs must meet level/tier 3 or higher.
2. Pull the current DoIT listed-provider roster. The roster is now the national A-grade provider list, replacing the older draft assumption that no public list existed.
3. For each listed provider, search exact legal name in OCR/IRD and then search for a physical facility address, operating service page, PeeringDB/IXP record, procurement record, or strong press.
4. Use NTA only for telecom/ISP context unless NTA publishes a DC/cloud roster in a future run.
5. Do not convert a DoIT provider listing into a facility count without address/site evidence. `Digital Network Solution (Everest Cloud)` is currently cloud-only on the roster and should not be counted as a physical data center without more evidence.

DoIT roster queries:

```text
site:doit.gov.np/pages/details-of-listed-data-center-and-cloud "सूचीकृत डाटा केन्द्र"
site:doit.gov.np ("Data Center and Cloud Service" OR "डाटा केन्द्र" OR "क्लाउड सेवा")
"Ncell Axiata Ltd" "Data Center" "DoIT" Nepal
"Access World Tech Pvt. Ltd" Nepal ("data center" OR cloud OR colocation)
"Silver Lining Pvt. Ltd" Nepal ("data center" OR cloud OR colocation)
"Data Hub Pvt. Ltd" Nepal ("data center" OR cloud OR colocation)
"Dish Media Network Ltd" Nepal ("data center" OR cloud OR colocation)
"Digital Network Solution" "Everest Cloud" Nepal
"Times Global Pvt Ltd" Nepal ("data center" OR cloud OR colocation)
```

## 3. Government IT, budget, and procurement workflow

### 3.1 IDMC / GIDC / Hetauda DR

Use https://idmc.gov.np/ first for current government data-center services and contacts. Keep https://nitc.gov.np/ as an older/legacy NITC route when reachable. Press and public records identify the Hetauda Disaster Recovery Center as a backup for GIDC; The Himalayan Times reported it came into operation in Hetauda in May 2019. Use government/IDMC pages for **A** current role and press for **B** inauguration/support details.

```text
site:idmc.gov.np ("डाटा" OR "data" OR "VM" OR "VPS" OR "कोलोकेसन" OR backup OR replication OR Hetauda)
site:nitc.gov.np (GIDC OR "data center" OR "disaster recovery" OR Hetauda OR "डाटा सेन्टर")
"Government Integrated Data Center" Nepal (Singha Durbar OR Singh Durbar OR Kathmandu OR Hetauda)
"Integrated Data Management Center" Nepal (colocation OR VM OR backup OR replication)
"Disaster Recovery Centre" Hetauda NITC GIDC
```

### 3.2 Budget and national plans

Use MoF/NPC official texts where reachable, with press only as navigational support. Verified press summaries identify FY 2082/83 lines for Integrated National Data Center upgrade, Hetauda DR expansion, Kohalpur data-center construction/upgrade, and a mid-hill DC feasibility study. FY 2083/84 coverage identifies a Sovereign AI Compute Center announced for Syuchatar, Kathmandu. These are **planned/announced** until tender, construction, commissioning, or service evidence appears.

```text
site:www.mof.gov.np ("data center" OR "डाटा सेन्टर" OR "AI compute" OR "Sovereign AI" OR Syuchatar OR Kohalpur OR Hetauda)
site:npc.gov.np ("data center" OR "डाटा सेन्टर" OR cloud OR "AI compute")
"budget" Nepal 2082/83 ("data center" OR Hetauda OR Kohalpur OR "mid-hill")
"budget" Nepal 2083/84 ("Sovereign AI Compute Center" OR Syuchatar OR "AI compute")
"Integrated National Data Center" Nepal (upgrade OR budget OR tender)
"Kohalpur" Nepal ("data center" OR "डाटा सेन्टर") (budget OR tender OR construction)
```

### 3.3 Procurement and tenders

Search PPMO/e-GP and agency notice pages separately; avoid malformed `site:a OR site:b` searches when the engine treats them inconsistently.

```text
site:ppmo.gov.np ("data center" OR "डाटा सेन्टर" OR server OR cloud OR DR OR UPS OR cooling)
site:bolpatra.gov.np/egp ("data center" OR "डाटा सेन्टर" OR server OR cloud OR DR OR UPS OR cooling)
site:www.ntc.net.np ("data center" OR "डाटा सेन्टर" OR Bhairahawa OR Kathmandu OR Huawei OR tender OR award)
"Nepal Telecom" "Huawei" "data center" Bhairahawa Kathmandu
"Nepal Telecom" "Rs 484" "data center"
```

## 4. Province checklist for official coverage

| Province | Required official sweep | Known official/primary seeds |
|---|---|---|
| Bagmati | DoIT roster, IDMC/GIDC, Hetauda DR, MoCIT, MoF/NPC, NTA telecom, PPMO/e-GP, NEA substations, city permits for Kathmandu/Lalitpur/Chandragiri/Syuchatar | IDMC/GIDC Kathmandu; Hetauda DR; Ncell Nakkhu IDC; WorldLink Data World Chandragiri; DataHub Kathmandu; Cloud Himalaya; Vianet Central Business Park incident lead; NTC Kathmandu project; Sovereign AI Compute Center Syuchatar announced. |
| Lumbini | DoIT roster, PPMO/e-GP, NTC, MoF/NPC, Lumbini province notices, Bhairahawa SEZ, NEA power | DataHub Butwal/Tilottama; NTC Bhairahawa project; Kohalpur government DC budget line. |
| Koshi | DoIT roster, NTA/ISP, Koshi province and Biratnagar city searches, NEA | No A-grade official facility confirmed from this review. Treat Ncell/Biratnagar network DC claims as leads unless Ncell/DoIT/press names the site. |
| Madhesh | Province/city notices, Birgunj industrial corridor, NTA/ISP, PPMO/e-GP | No confirmed official/commercial DC from this review. |
| Gandaki | Province/Pokhara notices, NTA/ISP, operator searches, NEA | No A-grade official facility confirmed from this review. Ncell/Pokhara network DC claims need stronger sourcing. |
| Karnali | Province/Birendranagar notices, PPMO/e-GP, NTA/ISP, NEA | No confirmed DC from this review. |
| Sudurpashchim | Province/Dhangadhi/Mahendranagar notices, PPMO/e-GP, NTA/ISP, NEA | No confirmed DC from this review. |

## 5. Known official/primary evidence status

| Facility/project/provider | Province | Status and honest grade |
|---|---|---|
| DoIT listed DC/cloud providers roster | National (`-`) | **A** for listed-provider status. Verified provider list on 2026-08-12: Ncell Axiata; Access World Tech; Silver Lining; Data Hub; Dish Media Network; Digital Network Solution/Everest Cloud (cloud only); Times Global. Facility-level facts still require site evidence. |
| IDMC / Government Integrated Data Center, Kathmandu | Bagmati | **Operational. A** for current government data-center route/services via https://idmc.gov.np/; older GIDC/NITC references should be linked but current pages win. |
| Hetauda Disaster Recovery Center | Bagmati | **Operational DR. A/B**: government/IDMC context plus press reporting of 2019 operation at Hetauda. Use **B** for KOICA/cost/inauguration details unless official project documents are retrieved. |
| Ncell Nakkhu IDC, Lalitpur | Bagmati | **Operational. A** for Ncell operator page and DoIT listed-provider status; **A/B** for ANSI/TIA-942-C Rated 3 certification until certifier listing is captured in the run; **B** for launch/capacity values from trade press. |
| Data Hub Pvt. Ltd. | Bagmati; Lumbini | **Operational provider. A** for DoIT listing and operator pages naming dual Kathmandu/Butwal data centers; **B/C** for date/spec claims if sourced only from press/directories. |
| WorldLink/Data World Chandragiri | Bagmati | **Operational. B** from DatacenterDynamics/NepaliTelecom unless an operator-primary Data World page is captured; **C/U** for Tier/Edge certification without certifier proof. |
| Cloud Himalaya | Bagmati | **Operational provider lead. A** for operator-owned existence/colocation pages; **U/B** for "Tier 4" unless Uptime Institute/TIA/certifier evidence is found. |
| NTC Kathmandu/Bhairahawa Huawei DC project | Bagmati; Lumbini | **Planned/construction. B** from trade press. Promote only with NTC, PPMO, e-GP, or award document. |
| Sovereign AI Compute Center, Syuchatar | Bagmati | **Announced/planned. A** only if MoF budget text is captured; otherwise **B** from NepalNews/TechSansar/Sarbatra. Do not mark operational. |
| Kohalpur government DC | Lumbini | **Announced/planned. A** if official FY 2082/83 budget line is captured; **B** via TechSansar/other summaries. Facility details remain **U**. |
| NEA internal DC | Bagmati | **C/U** unless NEA primary evidence is found. Directory claims alone are not enough. |

## 6. Official query pack

```text
"Nepal" ("data center" OR datacenter OR "data centre" OR IDC OR colocation OR cloud) site:gov.np
"Nepal" ("डाटा सेन्टर" OR "डेटा सेन्टर" OR "डाटा केन्द्र" OR क्लाउड OR कोलोकेशन OR सर्भर) site:gov.np
site:doit.gov.np ("data center" OR "डाटा केन्द्र" OR "क्लाउड सेवा" OR "listed")
site:idmc.gov.np ("data" OR "डाटा" OR VM OR VPS OR colocation OR "कोलोकेसन" OR backup OR replication)
site:www.mocit.gov.np ("data center" OR "डाटा सेन्टर" OR cloud OR AI OR "Digital Nepal")
site:nta.gov.np ("data center" OR cloud OR IDC OR ISP OR license OR लाइसेन्स)
site:www.ntc.net.np ("data center" OR "डाटा सेन्टर" OR Bhairahawa OR Kathmandu OR Huawei)
site:ppmo.gov.np ("data center" OR "डाटा सेन्टर" OR server OR cloud OR DR)
site:bolpatra.gov.np/egp ("data center" OR "डाटा सेन्टर" OR server OR cloud OR DR)
site:www.mof.gov.np ("data center" OR "AI compute" OR Syuchatar OR Kohalpur OR Hetauda)
site:npc.gov.np ("data center" OR "AI compute" OR cloud)
site:nea.org.np ("data center" OR substation OR load OR विद्युत OR Syuchatar OR "Mata Tirtha")
site:ocr.gov.np "{company}"
site:ird.gov.np "{company}"
site:ibn.gov.np "{company}" "data center"
site:www.doind.gov.np "{company}" "data center"
site:seznepal.gov.np ("data center" OR ICT OR cloud OR IT)
"{province_en}" Nepal ("data center" OR datacenter OR IDC OR colocation OR "server room")
"{province_ne}" ("डाटा सेन्टर" OR "डेटा सेन्टर" OR सर्भर OR क्लाउड OR कोलोकेशन)
"{city}" Nepal ("data center" OR "डाटा सेन्टर") (opening OR launch OR tender OR निर्माण OR उद्घाटन)
"{operator}" Nepal ("data center" OR IDC OR colocation OR cloud OR racks OR MW OR Tier)
```

Nepali variants: `डाटा सेन्टर`, `डेटा सेन्टर`, `डाटासेन्टर`, `डाटा केन्द्र`, `क्लाउड`, `क्लाउड सेवा`, `कोलोकेशन`, `को-लोकेशन`, `सर्भर`, `सर्भर रुम`, `आईडीसी`, `राष्ट्रिय डाटा सेन्टर`, `सरकारी डाटा सेन्टर`, `लाइसेन्स`, `अनुमति`, `निर्माण`, `उद्घाटन`, `विद्युत`, `भूकम्प`, plus city/province spellings: कोशी, मधेश, बागमती, गण्डकी, लुम्बिनी, कर्णाली, सुदूरपश्चिम, काठमाडौं/काठमाण्डौ, ललितपुर, भक्तपुर, पोखरा, विराटनगर, बुटवल, भैरहवा, नेपालगन्ज, वीरगन्ज, हेटौडा, कोहलपुर, स्युचाटार.

## 7. Reliability rules

1. Grade each field separately. A provider roster can prove listing, but not address, capacity, certification, or uptime.
2. DoIT roster entries are A-grade provider evidence. They are not facility counts unless a physical site is separately named.
3. Operator pages are A for existence and operator claims; Tier/MW/rack/SLA claims need certifier, procurement, or engineering evidence for A.
4. Directories and market reports are C leads. Never use DatacenterMap, Datacenters.com, Baxtel, DC Byte, or market reports as the sole proof for an official record.
5. Budget, MoU, cabinet, and press-announcement items are planned until procurement, construction, commissioning, or service availability is found.
6. CDN caches, IXP nodes, NOCs, telecom exchanges, and bank server rooms are not datacenters without explicit facility evidence.
7. `no_projects` for a province requires logged English+Nepali official, operator, procurement, and connectivity searches.

## 8. Re-check cadence

- **Monthly:** DoIT listed-provider roster; DoIT directive updates; IDMC/GIDC pages; NTA notices; NTC/PPMO/e-GP tenders; NTC Huawei project; Syuchatar AI compute center; Kohalpur/Hetauda budget lines.
- **Quarterly:** OCR/IRD entity refresh for listed providers; NEA/ERC power facts; PeeringDB/NPIX; certification bodies; hyperscaler official region/local-zone lists.
- **Annual or after legal change:** full 7-province sweep, Digital Nepal/telecom bill/data-protection status, and revalidation of empty-province `no_projects` notes.

## 9. Verified URL index

- DoIT directive: https://doit.gov.np/content/12100/data-center-and-claud-service--operations-and/
- DoIT listed providers: https://doit.gov.np/pages/details-of-listed-data-center-and-cloud/
- IDMC/GIDC current route: https://idmc.gov.np/
- NTA: https://nta.gov.np/ ; https://www.nta.gov.np/
- NTA standing-list route with TLS caution: https://standinglist.nta.gov.np/
- MoCIT: https://www.mocit.gov.np/
- NTC: https://www.ntc.net.np/
- PPMO/e-GP: https://www.ppmo.gov.np/ ; https://bolpatra.gov.np/egp/
- OCR/IRD: https://www.ocr.gov.np/ ; https://ird.gov.np/
- NEA/ERC: https://www.nea.org.np/ ; https://www.erc.gov.np/
- NRB: https://www.nrb.org.np/
- Ncell data center: https://www.ncell.com.np/en/business/blogs/ncell-data-center ; https://cloudsuite.ncell.com.np/data-center.html
- DataHub: https://datahub.com.np/about-us/ ; https://datahub.com.np/services/data-center/our-data-centers/
- Cloud Himalaya: https://www.cloudhimalaya.com/ ; https://www.cloudhimalaya.com/colocation/
