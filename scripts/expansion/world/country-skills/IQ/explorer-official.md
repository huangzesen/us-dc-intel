# IQ Explorer Official - Iraq Datacenter Enumeration Methodology

Date reviewed: 2026-08-12. Country: **IQ Iraq**. Manifest division model: **16 search divisions**: Anbar, Basra, Babylon, Baghdad, Diyala, Dhi Qar, Karbala, Kirkuk, Kurdistan, Maysan, Muthanna, Najaf, Nineveh, Qadisiya, Saladin, Wasit.

Important boundary: Iraq's real administrative geography has more federal governorates than this manifest model. The manifest groups Erbil, Sulaymaniyah, and Duhok under **Kurdistan**; it also omits some federal governorate names used in Iraqi sources. Do not call the manifest list "all Iraqi governorates" in outputs. For this workflow, coverage is complete only when all 16 manifest divisions above have been swept.

Use this file for official, regulatory, public-sector, investment, utility, and cloud-region evidence. Use `explorer-industry.md` for operator, vendor, trade-press, directory, and per-division query execution.

## Reliability Grades

Grade each data point, not just each project.

- **A**: primary official/legal/facility evidence: CMC pages or PDFs, Ministry of Communications (MoC), PMO/Council of Ministers, state-company announcements, NIC or governorate investment commission licences, Ministry of Electricity/utility records, KRG official pages, official operator facility pages, official cloud-region pages, official vendor/project pages, Uptime Institute certificate pages.
- **B**: strong secondary evidence: DCD, Iraq Business News, Iraqi News, INA, Shafaq, 964media, Rudaw, Kurdistan24, Capacity, Telecom Review, Developing Telecoms, Reuters, W.Media, development-bank or investor releases. Upgrade only the quoted official fact, not the whole article.
- **C**: lead-only evidence: DataCenterMap, Data Center Journal, Baxtel, colocationm, PeeringDB, Cloudscene, social posts, market-report snippets, and vendor marketing without physical scope/location.

Status rules:

- **Operational** requires launch/customer-ready evidence from a government, operator, vendor, or certification source.
- **Under construction** requires site-work, equipment award, or operator/vendor build progress evidence.
- **Planned/contract** covers signed contracts, MoUs, investment licences, land allocation, and announced project pipelines without construction proof.
- **Candidate** covers exchanges, POPs, cable landings, CMC registrations, cloud-service availability, and directory-only leads.

## Verified Source Surface

These URLs were checked for reachability or discoverability during review. Re-check every run because Iraqi government domains and anti-bot controls change frequently.

| Source | URL | Grade/use | Review note |
|---|---|---|---|
| Communications and Media Commission (CMC) | https://cmc.iq/ | A for regulator identity, official notices, licence/service frameworks | Reachable. Arabic-first. Home page exposes services for IT/digital services, media, telecoms, and CMC contact/address. |
| CMC digital-platform licence request PDF | https://cmc.iq/wp-content/uploads/2026/03/license-request-1.pdf | A for digital-platform licensing process | Reachable PDF. Refers to Articles 5 and 6 of the 2025 digital platforms/services framework and lists `it.licenses@cmc.iq`. It is not a datacenter licence. |
| CMC 2025 framework PDF | https://cmc.iq/ar/wp-content/uploads/2025/03/Framework-regulations-for-digital-platforms-and-services-en.pdf | A if accessible; A- when only linked from CMC PDF | Direct browser fetch may show verification interstitial, but the 2026 CMC PDF links to it. Use with caution and archive if accessible. |
| National Investment Commission | https://investpromo.gov.iq/ | A for national investment-promotion surface | Reachability varies by crawler. Use for ICT/data-centre investment opportunities and investor-guide pivots. |
| Council of Ministers / General Secretariat | https://cabinet.iq/ | A for National Data Center if page accessible | Some pages render as JavaScript `Loading...`; use PMO/Cabinet pages when accessible and corroborate with INA/DCD/IBN. |
| Ministry of Communications | https://moc.gov.iq/ | A when reachable | Domain exists but command-line fetch can be blocked. Search Arabic name `وزارة الاتصالات العراقية` and MoC statements mirrored by agencies. |
| Ministry of Electricity | https://moelc.gov.iq/ | A for grid/substation/power evidence | Domain responds but command-line fetch may be Cloudflare-blocked. Use browser/search plus official social/utility company pages. |
| KRG portal | https://gov.krd/english/ | A for Kurdistan Region government facilities | Use for Erbil/Sulaymaniyah/Duhok planning, digital-transformation, and government data center follow-up. |
| IraqGov portal | https://iraqgov.com/ | A/B directory to institutions | Use to find official governorate and ministry domains, not as facility evidence by itself. |
| AWS regions | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | A for AWS public-region existence | Checked; no Iraq region indicated in public region list. |
| AWS Local Zones | https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | A for AWS Local Zone existence | Checked; use to confirm no Iraq Local Zone before rejecting AWS local-facility claims. |
| Azure regions | https://learn.microsoft.com/en-us/azure/reliability/regions-list | A for Azure region existence | Checked; no Iraq Azure region found. |
| Google Cloud locations | https://cloud.google.com/about/locations | A for Google Cloud region/zone existence | Checked; no Iraq public region found. |
| Oracle Cloud regions | https://www.oracle.com/cloud/public-cloud-regions/ | A for OCI region existence | Checked; no Iraq public region found. |

## Iraq-Specific Official Research Frame

Iraq has no public national datacenter facility register. Enumeration must join CMC licensing, MoC/state-company announcements, PMO/Cabinet e-government evidence, NIC and governorate investment licences, municipal/planning notices, utility and substation evidence, KRG sources, official cloud-region lists, and operator/vendor pages.

Do not infer a datacenter from:

- a CMC digital-platform registration;
- a mobile, ISP, VSAT, Starlink, or satellite licence;
- a fiber route, IXP, exchange, or submarine cable landing;
- an ordinary `مركز معلومات` government information office;
- a public-cloud sales page or regional service availability;
- a generator/substation project not tied to a facility.

Iraq's fixed backbone and exchanges are state-heavy. MoC/state companies such as the General Company for Communications and Informatics/Information Technology (GCCI/GCCIT), ITPC, and Al-Salam State Company may operate exchange buildings with server rooms in many governorates. Count them only when evidence says datacenter, hosting, cloud, racks, Tier, power/cooling, or customer services.

Electricity is a core validation axis. Capture grid MW/MVA, generator capacity, redundancy design, fuel storage, and renewable/PPA evidence separately. Never convert site power or PR capacity into IT load.

Arabic and English are both mandatory. Use Arabic for CMC/MoC/NIC/governorate pages and Iraqi agencies; use English for cloud providers, vendor pages, investment press, cable/connectivity, and international trade press.

## Official Portals and Query Templates

### CMC - Communications and Media Commission

Primary URLs:

- https://cmc.iq/
- https://cmc.iq/wp-content/uploads/2026/03/license-request-1.pdf
- https://cmc.iq/ar/wp-content/uploads/2025/03/Framework-regulations-for-digital-platforms-and-services-en.pdf

Use for MNO/ISP licences, spectrum and 5G decisions, digital-platform/services registrations, satellite broadband notices, interconnection disputes, and any future hosting/cloud/datacenter licence category. Current CMC digital-platform forms regulate services and platforms; they do not prove local physical infrastructure.

Queries:

```text
site:cmc.iq "مركز بيانات" OR "مراكز البيانات" OR "استضافة" OR "خدمات سحابية"
site:cmc.iq "data center" OR "data centre" OR hosting OR cloud
site:cmc.iq "ترخيص" OR "رخصة" OR "التراخيص" "انترنت" OR "بيانات"
site:cmc.iq "منصات رقمية" OR "الخدمات الرقمية" OR "الخدمات السحابية"
site:cmc.iq "5G" OR "الجيل الخامس" OR "الطيف الترددي"
"هيئة الإعلام والاتصالات" "مركز بيانات" OR "مراكز بيانات" OR "الاستضافة"
"CMC" Iraq "ISP license" OR "ISP licensing" OR "digital platforms"
"{operator}" "هيئة الإعلام والاتصالات" "رخصة" OR "تسجيل"
```

### MoC, PMO, State Companies, and Government Data Centers

Primary URLs and anchors:

- MoC: https://moc.gov.iq/ (also search `وزارة الاتصالات العراقية`)
- Cabinet/General Secretariat: https://cabinet.iq/
- IraqGov institution directory: https://iraqgov.com/
- INA English: https://ina.iq/eng/ and Arabic: https://ina.iq/

Confirmed public-sector facility seeds:

| Facility | Division | Status | Evidence and grade |
|---|---|---|---|
| National Data Center / National Cloud Facility, General Secretariat of the Council of Ministers | Baghdad | Operational/inaugurated Aug 2023 | PMO/Cabinet/INA when accessible **A**; DCD https://www.datacenterdynamics.com/en/news/iraq-govt-launches-national-data-center/ **B**; IBN https://www.iraq-businessnews.com/2023/08/22/iraq-launches-national-data-center/ **B**. Capacity not public. |
| MoC/Nokia government data centers at Intisar and al-Rashid/al-Sinak exchanges | Baghdad | Planned/contract as of Sep 2025 unless later site-work evidence found | IBN article citing Ministry of Communications https://www.iraq-businessnews.com/2025/09/18/nokia-to-build-first-iraqi-govt-data-centres-for-commercial-use/ **B+**; IraqiNews/DCD/Developing Telecoms corroboration **B**. Treat exact exchange names as named sites; do not mark operational without later launch evidence. |
| Ministry of Planning census datacenter | Baghdad likely, verify site | Candidate/operational lead | Mentioned in Nokia/MoC coverage as a prior Nokia-built data center supporting the 2024 census. Requires Ministry of Planning or Nokia primary confirmation before counting. |
| KRG Government Data Center | Kurdistan (Erbil) | Operational/inaugurated Sep 2022 | KRG official pages/social when accessible **A**; DCD https://www.datacenterdynamics.com/en/news/kurdistan-opens-data-center-for-government-services/ **B**. DCD reports KRG Tier III-standard claim but no size. |

MoC/state queries:

```text
site:moc.gov.iq "مركز بيانات" OR "مراكز البيانات" OR "الحوسبة السحابية"
site:moc.gov.iq "data center" OR "data centre" OR cloud OR hosting
"وزارة الاتصالات" "مركز بيانات" OR "مراكز البيانات" OR "السحابة الحكومية"
"Ministry of Communications" Iraq Nokia "data center" OR "data centre"
"General Company for Communications and Informatics" OR "GCCI" OR "GCCIT" "data center"
"Informatics and Telecommunications Public Company" OR "ITPC" Iraq "data center"
"Al-Salam State Company" Iraq "data center" OR "exchange" OR "مركز بيانات"
"مركز البيانات الوطني" "الأمانة العامة لمجلس الوزراء"
"National Data Center" Iraq "General Secretariat of the Council of Ministers"
"Ministry of Planning" Iraq census "data center" Nokia
```

### NIC and Governorate Investment Commissions

Primary URLs:

- NIC: https://investpromo.gov.iq/
- Investor guide: https://investpromo.gov.iq/investor-guide/
- Investment Law No. 13 of 2006 reference: https://investmentpolicy.unctad.org/investment-laws/laws/205/iraq-investment-law

Investment licences and opportunities are useful for large ICT projects because they can name land, investor, sector, and governorate. Grade NIC and governorate commission postings **A** for licence/existence of an investment decision, but only **planned** until construction/operation evidence appears.

Queries:

```text
site:investpromo.gov.iq "data center" OR "data centre" OR "ICT" OR "communications"
site:investpromo.gov.iq "مركز بيانات" OR "مراكز بيانات" OR "الاتصالات" OR "تقنية المعلومات"
"الهيئة الوطنية للاستثمار" "مركز بيانات" OR "البنية التحتية الرقمية"
"National Investment Commission" Iraq "data center" OR "data centre"
"Iraq Investment Forum" "data centre" OR "data center" OR "digital infrastructure"
"{governorate} Investment Commission" "data center" OR ICT OR digital
"هيئة استثمار {governorate_ar}" "مركز بيانات" OR "تخصيص أرض" OR "اتصالات"
```

### Planning, Municipal, and Environment Evidence

No national public e-permitting database was found. Use governorate municipalities, Amanat Baghdad, KRG municipal/planning bodies, and investment commissions for land allocations, building permits, and project approvals.

Queries:

```text
"{governorate}" "data center" "building permit" OR "land allocation"
"{governorate_ar}" "مركز بيانات" "إجازة بناء" OR "رخصة بناء" OR "تخصيص أرض"
"أمانة بغداد" "مركز بيانات" OR "تخصيص أرض" OR "رخصة بناء"
site:gov.krd "data center" OR "مركز بيانات" OR "داتا سنتر"
"وزارة البيئة" "مركز بيانات" OR "تقييم الأثر البيئي" OR "مولدات"
"Ministry of Environment" Iraq "data center" OR EIA OR generators
"{project}" Iraq "Environmental Impact Assessment" OR "تقييم الأثر البيئي"
```

### Power and Utility Evidence

Primary URL: https://moelc.gov.iq/ . Search the Ministry portal, official social channels, transmission/distribution companies, and KRG electricity sources.

Queries:

```text
site:moelc.gov.iq "مركز بيانات" OR "data center" OR "الخدمات الرقمية"
"وزارة الكهرباء" "مركز بيانات" OR "استضافة" OR "اتصالات"
"Ministry of Electricity" Iraq "data center" OR "digital"
"شركة نقل الطاقة الكهربائية" "مركز بيانات" OR "محطة تحويل"
"{operator}" "{division}" "ميجاواط" OR "MW" "محطة تحويل" OR "مولدات"
"{project}" Iraq substation OR feeder OR MVA OR MW
"{project}" Iraq solar OR renewable "data center"
"Kurdistan" electricity "data center" MW OR substation
```

Record: utility connection MW/MVA, voltage, substation/feeder, generator count/rating, fuel storage, renewable/PPA MW, energisation date, and whether the power evidence is committed, installed, or contextual.

## Cloud-Region and Edge Checks

Official cloud pages are **A** for public-region/Local-Zone/edge existence, not for physical building addresses. As of this review, no AWS, Azure, Google Cloud, Oracle OCI, or Huawei Cloud public region in Iraq was found in official lists.

| Provider | Official check | Iraq interpretation |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | No Iraq public region or Local Zone found. Outposts/partner deployments are tenant leads only. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-region | No Iraq Azure region found. Edge POPs, if listed, are not datacenters. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | No Iraq public region found. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Iraq public region found. |
| Huawei Cloud | https://www.huaweicloud.com/intl/en-us/about/global-infrastructure.html | No Iraq public cloud region found; Huawei remains an equipment/5G/vendor lead. |
| Starlink/satellite | CMC notices and Starlink availability/licence coverage | Connectivity only; never count as datacenter infrastructure. |

Cloud queries:

```text
site:aws.amazon.com Iraq "region" OR "Local Zone" OR "Outposts"
site:learn.microsoft.com Iraq "region" OR "availability zone" OR "Baghdad" OR "Erbil"
site:cloud.google.com Iraq "region" OR "Baghdad" OR "Erbil"
site:oracle.com Iraq "cloud region" OR "OCI"
site:huaweicloud.com Iraq OR Baghdad OR Erbil "region"
"{hyperscaler}" Iraq "data center" -jobs -training
```

## Division Coverage Strategy

For every manifest division, run this seven-step sweep and record negative results with date and query strings:

1. CMC: `site:cmc.iq` plus licensing/service terms and the division name.
2. MoC/state companies: `وزارة الاتصالات`, GCCI/GCCIT, ITPC, Al-Salam plus datacenter/cloud/hosting terms.
3. Investment: NIC and governorate investment commission terms in English and Arabic.
4. Power: MOE, transmission/distribution companies, substation, feeder, MW/MVA, generator terms.
5. Planning: municipality, Amanat Baghdad, KRG planning, building permit, land allocation terms.
6. Local press: INA, Shafaq, 964media, Rudaw/Kurdistan24, Iraqi News, Iraq Business News.
7. Connectivity context: cable landings, terrestrial fiber corridors, IXPs, MNO core sites. Mark as candidate/edge unless facility evidence exists.

| Manifest division | Arabic/city anchors | Official strategy | Expected yield |
|---|---|---|---|
| Anbar | الأنبار; الرمادي; الفلوجة; القائم | Sweep CMC/MoC/ITPC exchanges, fiber corridors toward Jordan/Syria, Anbar Investment Commission, universities/government IT. | Low; mostly negative except exchange/fiber leads. |
| Basra | البصرة; الفاو; أم قصر; خور الزبير | Search Al-Faw cable landings, port/oil-sector digital infrastructure, Basra Oil/South Gas, Basra Investment Commission, MOE/substation evidence. | Medium for edge/cable and oil-sector candidates; facility proof still needed. |
| Babylon | بابل; الحلة | Sweep Babylon Investment Commission/NIC, government e-services, universities, industrial zones, MoC exchanges. | Low. |
| Baghdad | بغداد; الكرخ; الرصافة; المنصور; الكرادة; الانتصار; السنك | Highest priority: National Data Center, MoC/Nokia Intisar and al-Rashid/al-Sinak sites, T964, Ministry of Planning census DC lead, CBI/state banks, MoC/GCCI/ITPC exchanges, Amanat Baghdad permits, MOE power joins. | High. |
| Diyala | ديالى; بعقوبة | Search Diyala State Company fiber manufacturing, telco exchanges, university/government IT, investment commission. | Low; avoid counting fiber factory as DC. |
| Dhi Qar | ذي قار; الناصرية | Search government services, Gharraf/oil-sector IT, Dhi Qar Investment Commission, MoC exchanges. | Low. |
| Karbala | كربلاء | Search religious-tourism digital services, smart-city/e-services, Karbala Investment Commission, renewables/power, MoC exchanges. | Low. |
| Kirkuk | كركوك | Search oil/energy IT rooms, disputed-area telecom/core sites, transit corridor and MoC exchanges. | Low to medium candidate leads; verify KRG/federal attribution by physical site. |
| Kurdistan | إقليم كردستان; أربيل; السليمانية; دهوك | KRG government DC, Linkdata Erbil, Korek/Asiacell/Tishknet core/hosting, KRG DIT and Ministry of Transport & Communications, KRG electricity/planning. | Medium-high. |
| Maysan | ميسان; العمارة | Search oil-sector IT, Maysan Investment Commission, government e-services, MoC exchanges. | Low. |
| Muthanna | المثنى; السماوة | Search renewables/solar investment, government IT, Muthanna Investment Commission, MoC exchanges. | Low. |
| Najaf | النجف | Search investment/tourism/university IT, airport/religious-tourism digital services, Najaf Investment Commission, MoC exchanges. | Low. |
| Nineveh | نينوى; الموصل; ربيعة | Search Mosul reconstruction, universities, MoC exchanges, Rabia/Turkey fiber transit, GBI/Civilisations Route leads. | Medium-low for transit/context. |
| Qadisiya | القادسية; الديوانية | Search government e-services, university IT, Qadisiya Investment Commission, MoC exchanges. | Low. |
| Saladin | صلاح الدين; تكريت; سامراء; بيجي | Search industrial/oil/refining IT, government services, investment commission, MoC exchanges. | Low. |
| Wasit | واسط; الكوت | Search government services, university IT, Wasit Investment Commission, MoC exchanges. | Low. |

Per-division copy-paste template:

```text
"{division}" Iraq ("data center" OR "data centre" OR datacenter OR colocation OR "cloud services")
"{division}" Iraq ("MW" OR MVA OR racks OR "Tier III" OR Uptime) "data center"
"{division_ar}" "مركز بيانات" OR "مراكز البيانات" OR "داتا سنتر" OR "الاستضافة"
"{division_ar}" "وزارة الاتصالات" OR "هيئة الإعلام والاتصالات" "مركز بيانات" OR "رخصة"
"{division_ar}" "الهيئة الوطنية للاستثمار" OR "هيئة استثمار" "مركز بيانات" OR "تخصيص أرض"
"{division_ar}" "وزارة الكهرباء" OR "شركة توزيع كهرباء" "ميجاواط" OR "محطة تحويل" OR "مولدات"
site:iraqinews.com "{division}" "data center" OR "مركز بيانات"
site:ina.iq "{division_ar}" "مركز بيانات" OR "الحوسبة السحابية"
site:shafaq.com "{division_ar}" "مركز بيانات" OR "داتا سنتر"
site:iraq-businessnews.com "{division}" "data centre" OR "data center"
```

## Minimum Record Schema

Capture these fields before promotion into the facility inventory:

```text
country=IQ
division=<one of 16 manifest divisions>
city_district_exchange=<as stated>
facility_name=<canonical + aliases>
owner_operator=<legal entity>
facility_type=<commercial colo | government | telco core | cloud | bank | oil-sector | exchange candidate | edge/connectivity>
status=<operational | under construction | planned/contract | candidate | retired/unknown>
source_grade=<A/B/C per data point>
source_urls=<URLs>
evidence_date=<publication or access date>
capacity_claims=<IT load, site power, racks, sqm, Tier, redundancy, only verbatim>
regulatory_relation=<CMC licence/registration if any>
investment_relation=<NIC/governorate licence/land if any>
power_relation=<grid/generator/solar/substation evidence if any>
notes=<false-positive checks and unresolved joins>
```

## Anti-False-Positive Checklist

- `مركز معلومات` usually means information center/office, not datacenter.
- CMC digital-platform registration is service regulation, not physical infrastructure.
- Starlink/satellite licensing is connectivity only.
- Al-Faw cable landings and IRAQIXP/PeeringDB records are edge/connectivity leads only.
- MoC/GCCI/ITPC exchanges need hosting/cloud/Tier/rack/power evidence before counting.
- Operator PR capacity is not audited capacity unless supported by certification, utility, or commissioning evidence.
- KRG records belong to the manifest `Kurdistan` division only when physically in Erbil/Sulaymaniyah/Duhok; do not merge Kirkuk or Nineveh disputed-area records without location proof.
