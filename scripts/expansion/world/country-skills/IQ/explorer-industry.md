# IQ Explorer Industry - Iraq Datacenter Operator, Vendor, Press, Directory, and Division Query Methodology

Date reviewed: 2026-08-12. Scope: industry-side enumeration for Iraq datacenters across commercial colo/cloud operators, MNOs, ISPs, state-company facilities, vendor/contractor pages, trade press, cable/connectivity projects, directories, and governorate-level search pivots.

Manifest division model: **16 search divisions**: Anbar, Basra, Babylon, Baghdad, Diyala, Dhi Qar, Karbala, Kirkuk, Kurdistan, Maysan, Muthanna, Najaf, Nineveh, Qadisiya, Saladin, Wasit. The manifest groups Erbil, Sulaymaniyah, and Duhok as **Kurdistan**; do not represent this as Iraq's complete real-world governorate list.

Use `explorer-official.md` for CMC, MoC, NIC, power, planning, and official cloud-region interpretation. This file focuses on discovery and triage from operators, vendors, trade press, and directories.

## Reliability Grades

- **A**: official operator facility page, official vendor/project page, listed-company disclosure, official cloud/region/certification page, or primary government/regulatory page.
- **B**: established trade press or agency reporting: DCD, Iraq Business News, Iraqi News, INA, Shafaq, 964media, Rudaw, Kurdistan24, Capacity, Telecom Review, Developing Telecoms, Reuters, W.Media. If an article says "Source: Ministry of Communications," grade the official fact as **B+** until the primary page is archived.
- **C**: DataCenterMap, Data Center Journal, Baxtel, colocationm, PeeringDB, Cloudscene, LinkedIn/Facebook/X/Instagram, market reports, unverifiable aggregators. Use as leads only.

Grade individual claims separately. Example: T964's existence and Baghdad location are **A** from its official page; its 3 MW IT load is an **A operator claim**; its Tier/Uptime wording remains an **operator claim** until matched to an Uptime certificate page.

## Industry Frame

Iraq's public commercial datacenter market is still small. Baghdad and Kurdistan/Erbil carry the strongest facility evidence. Basra is a rising edge/cable/oil-sector lead, especially around Al-Faw, but cable landings are not datacenters. Most other divisions require negative sweeps plus telco-exchange, university, bank, oil-sector, and government-service checks.

Separate record types:

- commercial colocation/datacenter;
- government datacenter or national cloud;
- telco core/exchange candidate;
- bank/financial-sector datacenter;
- oil-sector or industrial server room;
- cloud region or sovereign cloud;
- edge/POP/IXP/cable landing;
- investment or construction pipeline.

Preserve exact lifecycle verbs: signed, MoU, licensed, registered, land allocation, under construction, customer-ready, inaugurated, launched, operational.

## Operator and Facility Seeds

| Operator/facility | URLs | Location signal | Status and grading |
|---|---|---|---|
| T964 / Tech964 Data Center | https://t964datacenter.com/ ; https://tech964.com/ ; https://www.datacenterdynamics.com/en/news/iraqs-t964-to-build-data-center-with-schneider-electric/ ; https://www.iraq-businessnews.com/2026/07/11/schneider-electric-partners-with-t964-for-new-baghdad-data-centre/ ; https://www.datacentermap.com/iraq/baghdad/ | Baghdad, exact address not public in directory. Official site metadata states Baghdad and markets colocation/enterprise cloud/carrier-neutral connectivity. | Under construction/planned launch end-2026 unless a later launch page exists. Official site claims 3 MW IT load, Tier III, N+1/full redundancy, 24/7 NOC/SOC, carrier-neutral service, and grid-instability mitigation. Treat as **A operator claims**; Schneider/press claims **B**; directory address/capacity **C**. |
| Linkdata.com / Erbil DC 1 | https://linkdata.com/ ; https://www.datacentermap.com/iraq/erbil/linkdatacom/ ; https://colocationm.com/iraq/erbil-dc-1 | Erbil/Kurdistan. Linkdata official page markets VPS, bare metal, Kubernetes, storage, hosting, and "thousands of servers in three different regions." DataCenterMap places the facility near Erbil 44001 and restricts precise address due geopolitical risk. | Operational service provider. Official service presence **A**; datacenter/Tier/address/MW claims **C unless corroborated**. DataCenterMap says commercial Tier 3 and services including private cabinets, bare metal, public cloud; treat as lead. |
| National Data Center / National Cloud Facility | https://www.datacenterdynamics.com/en/news/iraq-govt-launches-national-data-center/ ; https://www.iraq-businessnews.com/2023/08/22/iraq-launches-national-data-center/ ; PMO/Cabinet/INA pages when accessible | Baghdad, General Secretariat of the Council of Ministers. | Operational/inaugurated Aug 2023. Government source **A** when accessible; DCD/IBN **B**. Capacity undisclosed. Government facility, not commercial colo. |
| KRG Government Data Center | https://www.datacenterdynamics.com/en/news/kurdistan-opens-data-center-for-government-services/ ; KRG DIT/gov.krd pages/social when accessible | Kurdistan, likely Erbil government environment. | Operational/inaugurated Sep 2022. KRG Tier III-standard claim; no public size. KRG official **A**; DCD **B**. |
| MoC/Nokia government data centers | https://www.iraq-businessnews.com/2025/09/18/nokia-to-build-first-iraqi-govt-data-centres-for-commercial-use/ ; https://www.datacenterdynamics.com/en/news/iraqs-ministry-of-communications-partners-nokia-for-state-owned-data-center/ ; https://developingtelecoms.com/telecom-technology/data-centres-networks/19088-iraq-to-build-first-data-centres-with-nokia-to-boost-digital-sovereignty.html | Baghdad: Intisar and al-Rashid/al-Sinak exchanges. | Planned/contract from Sep 2025 unless later construction/launch evidence found. IBN cites MoC; grade **B+** until primary MoC page is captured. |
| Ministry of Planning census datacenter | Search Ministry of Planning and Nokia pages | Baghdad likely; exact site unverified. | Candidate until primary confirmation. Do not count solely from passing references in later Nokia/MoC articles. |
| Ooredoo / Asiacell | https://www.asiacell.com/en/personal and Ooredoo Group pages | HQ/service base in Kurdistan/Sulaymaniyah and national MNO footprint. | Telco core candidates. Operator presence **A**; facility existence/specs need named site evidence. |
| Zain Iraq | https://www.iq.zain.com/ar and Zain Group pages | National MNO footprint, likely Baghdad/regional core sites. | Telco core/enterprise candidates only until named DC evidence appears. |
| Korek Telecom | Official Korek pages plus CMC/Rudaw/DCD dispute coverage | KRG-heavy MNO footprint, Erbil HQ. | Telco core candidates; CMC disputes are regulatory context, not DC evidence. |
| Earthlink | https://www.earthlink.iq/ | Large Iraqi ISP with national PoP/fiber footprint. | ISP/edge/server-room candidates. Require official hosting/DC page or facility evidence. |
| ScopeSky | https://scopesky.iq/en/ | Carrier/ISP and connectivity provider. | Network/POP candidates. Do not count PoPs as datacenters. |
| GCCI/GCCIT, ITPC, Al-Salam State Company | MoC/state-company pages, IBN tags, official tenders | Exchanges across divisions, especially Baghdad. | State telecom candidates. Count only named datacenter/cloud/hosting/rack/power evidence. |
| Alamiya Co / Talia / legacy Baghdad listings | https://www.datacenterjournal.com/data-centers/iraq/baghdad/ | Baghdad legacy directory leads. | **C only** until official/current operator evidence is found. |
| IRAQIXP / PeeringDB / Cloudscene | https://www.datacentermap.com/ixp/iraq-internet-exchange-point/ and PeeringDB searches | Baghdad/interconnection context. | IXP/edge only. Do not count as a datacenter. |

## Vendor, Contractor, and Certification Pivots

Vendor pages can be high-value because Iraqi operators often announce through suppliers.

| Vendor/source | Query surface | Use | Grade |
|---|---|---|---|
| Nokia | `site:nokia.com Iraq "data center" OR "data centre" OR census`; press around MoC and Ministry of Planning | MoC/Nokia data centers, Ministry of Planning census DC, possible T964/network work. | A if Nokia official project page; B through trade press. |
| Schneider Electric | `site:se.com Iraq T964 "data center"`; Schneider LinkedIn/PR; DCD/IBN | Power/cooling partner for T964 Baghdad facility. | A if official Schneider page; B for IBN/DCD; social **C/B-** depending source identity. |
| Huawei | `site:huawei.com Iraq 5G "data center" OR cloud` | Equipment/5G/core-network lead, not cloud-region proof. | A for Huawei official contract; facility needs site evidence. |
| Uptime Institute | https://uptimeinstitute.com/ and certificate search | Validate Tier design/facility certifications. | A for certificate status. Business-partner announcements are not facility certification. |
| DIL Technology / Breeze Investments / WorldLink | Reuters/DCD/IBN searches | Cable/AI-infrastructure/edge pipeline around Al-Faw and national routes. | B for consortium/cable; planned/candidate for datacenter unless facility named. |

Vendor queries:

```text
site:nokia.com Iraq "data center" OR "data centre" OR "census"
site:se.com Iraq "data center" OR T964 OR Baghdad
site:huawei.com Iraq "5G" OR "data center" OR cloud
site:uptimeinstitute.com Iraq OR Baghdad OR Erbil OR T964 OR Linkdata
"T964" "Uptime Institute" "certificate" OR "Tier"
"Schneider Electric" T964 Baghdad "data centre" OR "data center"
"WorldLink" Iraq "data center" OR "AI infrastructure" OR cable
"DIL Technology" Iraq "data center" OR "WorldLink"
```

## Trade Press and Directory Triage

| Source | URL/query | Use | Grade |
|---|---|---|---|
| DCD Iraq tag | https://www.datacenterdynamics.com/en/tags/iraq/ | Best English DC/connectivity feed: National Data Center, KRG DC, MoC/Nokia, T964/Schneider, cable projects, CMC/Korek. | B |
| Iraq Business News communications/data-centres | https://www.iraq-businessnews.com/category/communications/ ; https://www.iraq-businessnews.com/tag/data-centres/ | Iraqi business coverage, often sourced to ministries/operators. | B/B+ |
| Iraqi News / INA / Shafaq / 964media | https://www.iraqinews.com/ ; https://ina.iq/eng/ ; https://shafaq.com/en ; https://en.964media.com/ | Official-statement coverage and Arabic local search. | B; A only for official agency text if primary enough. |
| Rudaw / Kurdistan24 | https://www.rudaw.net/english ; https://www.kurdistan24.net/en | KRG digital, KRG DC, Korek/Starlink context. | B |
| Capacity / Telecom Review / Developing Telecoms / W.Media | site-scoped searches | Regional telco/DC/cable/vendor coverage. | B |
| Reuters | site/news searches | Consortium, investment, sanctions, telecom/cable context. | B+ |
| US ITA | https://www.trade.gov/country-commercial-guides/iraq-telecommunications | Dated telecom-market background. | A-/B+ background only. |
| Directories | https://www.datacentermap.com/iraq/ ; https://www.datacentermap.com/iraq/baghdad/ ; https://www.datacentermap.com/iraq/erbil/ ; https://www.datacenterjournal.com/data-centers/iraq/baghdad/ ; Baxtel; colocationm | Aliases, approximate city, services, operator names. | C |

Trade queries:

```text
site:datacenterdynamics.com/en/news Iraq "data center" OR "data centre" OR cable OR Nokia OR T964
site:iraq-businessnews.com "data centre" OR "data center" OR "T964" OR "Nokia" OR "Uptime"
site:iraqinews.com "data center" OR "مركز بيانات" OR Nokia OR cloud
site:ina.iq "مركز بيانات" OR "الخدمات السحابية" OR "الاستضافة"
site:shafaq.com "مركز بيانات" OR "داتا سنتر" OR "الحوسبة السحابية"
site:rudaw.net "data center" OR "Kurdistan" "digital" OR Korek
site:capacitymedia.com Iraq "data centre" OR cable OR Nokia
site:developingtelecoms.com Iraq "data centre" OR "data center" OR Nokia OR T964
"Iraq" "data center" "MW" "Tier III" -market -forecast -jobs
```

## English and Arabic Search Vocabulary

English terms:

```text
"Iraq" ("data center" OR "data centre" OR datacenter OR datacentre)
"Iraq" (colocation OR hosting OR "cloud services" OR "sovereign cloud" OR "government cloud")
"Iraq" ("Tier III" OR Uptime OR racks OR "IT load" OR MW OR MVA)
"Baghdad" "data center" OR "T964" OR "National Data Center" OR "Al-Sinak"
"Erbil" OR "Kurdistan" "data center" OR Linkdata OR Korek
"Al-Faw" OR "Faw" OR Basra "submarine cable" "data center"
"Rabia" OR Nineveh "fiber" OR "transit route" OR GBI
```

Arabic terms:

```text
"مركز بيانات" OR "مركز البيانات" OR "مراكز بيانات" OR "مراكز البيانات" OR "داتا سنتر"
"الحوسبة السحابية" OR "الخدمات السحابية" OR "السحابة الحكومية"
"الاستضافة" OR "الخوادم" OR "استضافة المواقع"
"التحول الرقمي" OR "البنية التحتية الرقمية"
"ترخيص" OR "رخصة" OR "تسجيل" OR "إجازة بناء" OR "تخصيص أرض"
"الكهرباء" OR "ميجاواط" OR "محطة تحويل" OR "مولدات"
"افتتح" OR "أطلق" OR "دشن" OR "قيد الإنشاء" OR "وقّع عقد"
```

Arabic warning: `مركز معلومات` often means an administrative information office. Reject unless racks, hosting, cloud, power/cooling, or facility terms are present.

## Division-by-Division Industry Strategy

Run English, Arabic, operator, vendor, trade, directory, and power/investment pivots for every division. Record negative sweeps so future runs do not keep promoting market-report noise.

| Division | Arabic/city anchors | Industry route |
|---|---|---|
| Anbar | الأنبار; الرمادي; الفلوجة; القائم | Search fiber routes toward Jordan/Syria, ISP PoPs, MoC exchanges, universities, Anbar Investment Commission. Expect exchange/edge candidates only. |
| Basra | البصرة; الفاو; أم قصر; خور الزبير | Search Al-Faw submarine cable projects, WorldLink, GBI/Civilisations Route, port authority, Basra Oil Company, South Gas, Elsafeer/VSAT, Basra Investment Commission. Treat cable landing as edge unless datacenter building named. |
| Babylon | بابل; الحلة | Search NIC/Babylon investment licences, ISPs, universities, government-services centers, MoC exchanges. Mostly negative. |
| Baghdad | بغداد; الكرخ; الرصافة; المنصور; الكرادة; الانتصار; السنك | Highest priority: T964, National Data Center, MoC/Nokia Intisar and al-Rashid/al-Sinak sites, Ministry of Planning census DC lead, DataCenterMap Baghdad, Data Center Journal legacy listings, IRAQIXP, CBI/state banks, MNO core facilities. |
| Diyala | ديالى; بعقوبة | Search Diyala State Company fiber cable factory as manufacturing context, ScopeSky/Earthlink PoPs, government IT, investment commission. Do not count factory/exchange alone. |
| Dhi Qar | ذي قار; الناصرية | Search oil-field IT (Gharraf), local ISPs, university/government IT, investment commission. Mostly negative. |
| Karbala | كربلاء | Search pilgrimage/religious-tourism digital services, smart-city vendors, ISPs, power/renewables, investment commission. Mostly negative. |
| Kirkuk | كركوك | Search oil/energy operators, MNO cores, transit routes, ISPs, disputed-area KRG/federal sources. Assign by physical site only. |
| Kurdistan | إقليم كردستان; أربيل; السليمانية; دهوك | Search KRG DC, Linkdata, Korek, Asiacell/Ooredoo, Tishknet, KRG DIT, KRG Ministry of Transport & Communications, Erbil/Sulaymaniyah/Duhok investment/planning, DataCenterMap Erbil. |
| Maysan | ميسان; العمارة | Search oil-sector IT, local ISP PoPs, government services, investment commission. Mostly negative. |
| Muthanna | المثنى; السماوة | Search solar/renewable investment, edge/ISP PoPs, government IT, investment commission. Mostly negative. |
| Najaf | النجف | Search airport/tourism/religious-services IT, university hosting, ISPs, Najaf Investment Commission. Mostly negative. |
| Nineveh | نينوى; الموصل; ربيعة | Search Mosul reconstruction, universities, ISPs, MoC exchanges, Rabia border transit, GBI/Civilisations Route. Medium candidate/context yield. |
| Qadisiya | القادسية; الديوانية | Search university/government IT, local ISPs, investment commission. Mostly negative. |
| Saladin | صلاح الدين; تكريت; سامراء; بيجي | Search refinery/industrial IT, government services, MoC exchanges, investment commission. Mostly negative. |
| Wasit | واسط; الكوت | Search government/university IT, ISPs, investment commission, MoC exchanges. Mostly negative. |

Per-division template:

```text
"{division}" Iraq ("data center" OR "data centre" OR datacenter OR colocation OR "cloud computing")
"{division}" Iraq ("MW" OR MVA OR racks OR "Tier III" OR Uptime) "data center"
"{division}" Iraq "{operator}" "data center" OR "مركز بيانات"
"{division_ar}" "مركز بيانات" OR "مراكز البيانات" OR "داتا سنتر" OR "الاستضافة"
"{division_ar}" "الخدمات السحابية" OR "الخوادم" OR "التحول الرقمي"
site:cmc.iq "{division}" OR "{division_ar}"
site:investpromo.gov.iq "{division}" OR "{division_ar}"
site:iraq-businessnews.com "{division}" "data centre" OR "data center"
site:datacenterdynamics.com "{division}" Iraq "data center" OR cable
site:iraqinews.com "{division}" "data center" OR "مركز بيانات"
site:ina.iq "{division_ar}" "مركز بيانات" OR "الحوسبة السحابية"
site:shafaq.com "{division_ar}" "مركز بيانات" OR "داتا سنتر"
```

Operator-specific template:

```text
"{operator}" Iraq ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR "cloud services")
"{operator}" Iraq ("MW" OR "IT load" OR racks OR "Tier III" OR Uptime OR redundancy)
"{operator}" "{division}" "مركز بيانات" OR "الاستضافة" OR "خوادم"
"{operator}" "CMC" OR "هيئة الإعلام والاتصالات" "رخصة" OR "تسجيل"
"{operator}" "وزارة الكهرباء" OR "Ministry of Electricity" "ميجاواط" OR "محطة تحويل"
"{operator}" "تخصيص أرض" OR "قطعة أرض" OR "إجازة بناء"
```

## Directory Reconciliation Rules

Use directories for candidate creation only, then backfill.

- DataCenterMap currently lists Baghdad/T964 and Erbil/Linkdata but with restricted exact location data. Capture only city/proximity, not precise addresses, unless the operator publishes them.
- DataCenterMap's T964 description says Tier III+, 3 MW IT load, 2N power redundancy, ASHRAE cooling, and carrier-neutral connectivity. Treat as **C** unless matched to T964 official text or certification/utility evidence.
- DataCenterMap's Linkdata page says commercial Tier 3, Erbil proximity, services, PCI/ISO27001 tags. Treat as **C** until corroborated by Linkdata or certification bodies.
- Data Center Journal legacy Baghdad listings (GCCIT, Alamiya, Talia) are **C** and may be stale. Promote only with current official/operator evidence.
- PeeringDB/Cloudscene/IXP records prove interconnection/POP presence, not facility type.

## Final Enumeration Pipeline

1. Pull all confirmed seeds from official methodology: National Data Center, KRG DC, MoC/Nokia x2, T964, Linkdata, Ministry of Planning census lead.
2. Verify operator pages and extract only directly stated claims: facility name, city, service type, MW/racks/Tier, redundancy, launch status.
3. Search vendor/certification pages for Nokia, Schneider, Huawei, Uptime.
4. Search DCD/IBN/Iraqi News/INA/Shafaq/964/Rudaw/Kurdistan24/Developing Telecoms/Capacity for status changes.
5. Run the 16-division table and record negative sweeps.
6. Reconcile directories and IXPs as candidate records only.
7. Join every candidate to official/regulatory, investment, power, planning, or operator evidence before promotion.
8. Dedupe by `(operator, facility/campus, physical division, phase)`, not by article headline.
9. Assign lifecycle status from the strongest current verb and grade every URL/data point.

## Pitfalls

- Do not mark T964 operational until an opening/customer-ready source exists; as of reviewed public evidence it is under construction/planned for end-2026.
- Do not treat MoC/Nokia signed-contract sites as operational before launch/site-work evidence.
- Do not convert T964 site-power or PR expansion claims into IT load; preserve each claim verbatim with source grade.
- Do not count Al-Faw, Rabia, WorldLink, GBI routes, IRAQIXP, Starlink, or MNO spectrum as datacenters.
- Do not count every exchange, ISP PoP, or government information center.
- Do not let the `Kurdistan` manifest bucket hide physical city evidence; record Erbil/Sulaymaniyah/Duhok in `city_district_exchange`.
- Avoid market-report snippets unless they reveal a named operator, site, status, and source trail.
