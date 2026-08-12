# AM Explorer Official - Armenia Datacenter Enumeration via Primary Sources

Date: 2026-08-12. Country: **AM Armenia**. Division model: **10 marzes plus Yerevan city** per the Government of Armenia. Use these 11 first-level units exactly: **Aragatsotn; Ararat; Armavir; Yerevan; Gegharkunik; Kotayk; Lori; Shirak; Syunik; Tavush; Vayots Dzor**.

Reliability grades:
- **A** = primary / official / operator-controlled evidence: Government of Armenia, Ministry of High-Tech Industry, Ministry of Economy, PSRC, Urban Development Committee / construction-permit system, legal acts, state procurement, Uptime Institute, operator official page, official cloud-region page, IFI page.
- **B** = strong secondary evidence: ARKA / ARKATelecom, Armenpress, DCD, Telecompaper, Data Center Frontier, vendor case study, national media quoting named officials or operators.
- **C** = lead only: directories, marketplaces, PeeringDB / IX records, social posts, market reports, blogs, stale address listings.

Do not count a facility unless there is facility-level evidence: name/operator plus locality or address plus status. PSRC telecom authorization alone, cloud resale, CDN/IX presence, or a server-room tender is not enough.

## 1. Country Structure And Source Priorities

Official administrative source:
- Government regions page: `https://www.gov.am/en/regions/` - verifies Armenia has ten marzes and Yerevan city.
- Government system page: `https://www.gov.am/en/gov-system/` - names the ten marzes.

Primary-source order for Armenia:
1. **Government / ministry project evidence**: `https://www.gov.am`, `https://hightech.gov.am`, `https://mineconomy.am`, `https://arlis.am`.
2. **Construction / land / permit evidence**: `https://urban.e-gov.am`, `https://www.minurban.am/en`, `https://azdarar.am`, `https://cadastre.am`, Yerevan Municipality, and marz administrations.
3. **Regulatory / utility evidence**: `https://www.psrc.am`, `https://e-services.psrc.am`, ENA, HVEN, MTAI.
4. **Certification / operator evidence**: Uptime Institute awards, operator facility pages, official cloud-provider region lists.
5. **Secondary confirmation**: ARKA/Armenpress/DCD/vendor articles.

Armenian-language searches are mandatory. Use English `data center`, `datacenter`, `data centre`, `colocation`, `cloud`, `data processing center`, `AI factory`, `supercomputer`; Armenian `տվյալների կենտրոն`, `տվյալների մշակման կենտրոն`, `տվյալների մշակման և պահպանման կենտրոն`, `սերվերային`, `հոսթինգ`, `կոլոկացիա`, `ամպային ծառայություններ`, `գործարկվել է`, `շահագործման է հանձնվել`, `շինարարության թույլտվություն`; Russian `дата-центр`, `ЦОД`, `центр обработки данных`, `облачные услуги`.

## 2. Verified Primary Anchors

| Facility / project | Division | Official source chain | Current handling | Grade |
|---|---|---|---|---|
| Firebird AI Factory / DC-1 Hrazdan | Kotayk | `https://www.firebird.ai/news-firebird-grand-opening.html`; `https://www.firebird.ai/data-centers.html`; NVIDIA blog `https://blogs.nvidia.com/blog/firebird-ai-factory-armenia-blackwell-rubin-dsx/`; High-Tech Ministry `https://hightech.gov.am/en/articles/news/firebird-06-1` | Operational Hrazdan AI factory. Operator page names DC-1 Hrazdan and 6,144 NVIDIA B200 GPUs / 15 MW on the home page; ministry page says near Hrazdan, 200,000 sq m, launch scheduled July 2026, >6,000 Blackwell GPUs, 18 MW; Firebird/NVIDIA pages state roadmap to >70,000 GPUs and 300 MW in Armenia by end-2027. Treat 300 MW and later DC-2/DC-3 values as announced roadmap, not commissioned capacity. | A |
| Eleveight AI Factory | Gegharkunik | High-Tech Ministry `https://old.hightech.gov.am/en/tegekatvakan-kentron/ayl/norutyunner/eleveight-ai`; Eleveight `https://eleveight.ai/en/company/`; Eleveight contact `https://eleveight.ai/en/contact/`; Armenpress `https://armenpress.am/en/article/1251654` | Operational AI data center in **Gagarin, Gegharkunik Province**. Operator states first AI Factory in Gagarin, 512 NVIDIA B300 GPUs, first-phase investment $120m, capacity scaling to 40 MW; contact page gives data center address `Gortsaranayin Street 1, Gagarin, Armenia`. Ministry page confirms opening, MoU, NVIDIA Blackwell B300, natural cooling / zero chemical footprint claims. | A |
| OVIO / GNC-ALFA Data Center Abovyan | Kotayk | Uptime `https://uptimeinstitute.com/uptime-institute-awards/datacenter/data-center-abovyan/2188`; OVIO `https://ovio.am/en/data-center`; OVIO Cloud `https://oviocloud.am/en/about-us`; investment support page `https://investin.am/news/gnc-alfa-is-set-to-invest-28000000-to-launch-a-data-center-in-the-city-of-abovyan/` | Operational commercial colo/cloud DC in Abovyan. Uptime confirms GNC-ALFA CJSC, Data Center "Abovyan", location Abovyan, Armenia, Tier III Certification of Design Documents. Operator pages state Tier III, 2 MW, 216 server racks/cabinets, commercial operation May 2024. Investment-support source says government would support the project with two substations and access roads. | A for existence/location; A for TCDD only; do not claim constructed-facility Uptime certification unless a current Uptime record says so. |
| Viva Data Centers | Yerevan | `https://www.viva.am/en/business-solutions/cloud-and-it-solutions/web/colocation`; `https://www.viva.am/en/colocationss` | Official Viva pages state colocation services at advanced data centers in Yerevan, 2N power and cooling, dual high-voltage feeds, diesel generators, UPS, fire suppression, security. Treat as operational Yerevan colo facilities. | A |
| TeamCloud / Team Telecom Armenia DC | Yerevan | `https://teamcloud.am/colocation.php`; `https://teamcloud.am/cloud-server.php` | TeamCloud states colocation and cloud servers are hosted in Team Telecom Armenia data center and describes Tier III international-standard design. Address is not fully facility-confirmed by this page; use TeamCloud contact address only as business contact unless another source names the DC address. | A for operator/service; B/C for exact address. |
| Yerevan State University AI Data Center / Supercomputer | Yerevan | YSU `https://www.ysu.am/en/news/90809`; Legrand case study `https://www.legrand.com/datacenter/gb-en/reference-projects/yerevan-state-university-of-armenia-legrand-powering-future-ready-ai-supercomputing-hub`; DCD sponsored/vendor coverage | Government-funded academic HPC / AI data center at YSU, 64 NVIDIA H100 GPUs. Count as institutional / research DC, not commercial colo. | A for YSU supercomputer; B/A for Legrand infrastructure depending on accessible case-study page. |
| VSData green DC | Aragatsotn | `https://vsdata.org/`; DCD `https://www.datacenterdynamics.com/en/news/2mw-data-center-planned-in-armenia/`; Developing Telecoms `https://developingtelecoms.com/telecom-technology/data-centres-networks/18177-vsdata-plans-spring-water-cooled-data-centre-for-armenia.html` | Planned / under-construction lead in Aragatsotn, outside Yerevan: 2 MW, 125 racks, Tier-3 specifications, spring-water / gorge cooling, 25 km fiber to Yerevan, target go-live end-2025 in 2025 sources. Because the operator site is investment-oriented and no official commissioning source was found in this run, status remains planned/under construction unless new permit/operator evidence proves operational. | B+ lead; promote to A only with permit, commissioning, utility, or operator operations evidence. |
| Cloudflare Yerevan #103 | Yerevan | `https://blog.cloudflare.com/yerevan-armenia-cloudflare-data-center-103/`; `https://www.cloudflare.com/network/` | Edge PoP / CDN location. Do not count as standalone datacenter unless host facility is identified. | A for edge presence; not a DC enumeration item. |
| AWS / Azure / GCP / OCI public cloud regions | National negative control | AWS `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`; Azure `https://learn.microsoft.com/en-us/azure/reliability/regions-list`; GCP `https://cloud.google.com/about/locations`; OCI `https://www.oracle.com/cloud/public-cloud-regions/` | No official Armenia public cloud region or Local Zone found in this run. Treat Armenia partner-cloud news separately. | A negative control. |

## 3. Regulator Workflow - PSRC

Primary portal: `https://www.psrc.am`.

Use PSRC for electricity, grid, tariff, and telecommunications authorization context, not as a standalone datacenter registry. Relevant sections may move; verify from the homepage each run.

Seed URLs / sections:
- Electric energy licensed companies: `https://psrc.am/contents/fields/electric_energy/el_energy_licensed_companies`
- Electric energy tariffs: `https://psrc.am/contents/fields/electric_energy/el_energy_tariffs`
- Electricity market: `https://psrc.am/contents/fields/electric_energy/electricity-market`
- Electronic communications regulated persons: `https://psrc.am/contents/fields/communications/com_regulated-personss`
- Electronic communications statistical indicators: `https://psrc.am/contents/fields/communications/com_statistical-indicators`
- Licensing info: `https://psrc.am/contents/info/for_investors/licensing-info`
- PSRC e-services: `https://e-services.psrc.am`

PSRC query templates:
```text
site:psrc.am "տվյալների կենտրոն"
site:psrc.am "data center"
site:psrc.am "Էլեկտրոնային հաղորդակցություն" "{operator}"
site:psrc.am "Էլեկտրական էներգիա" "{operator}"
site:psrc.am "Հրազդան" "լիցենզիա"
site:psrc.am "Գագարին" "լիցենզիա"
site:psrc.am "Աբովյան" "ենթակայան"
site:psrc.am "Ցանցին միացման կանոններ"
"ՀԾԿՀ" "{operator}" "տվյալների կենտրոն"
```

Grade guidance:
- PSRC register = **A** for licensed/regulated status.
- PSRC energy decision + facility source = **A** for grid/utility context.
- PSRC register only = **C** for datacenter existence.

## 4. Permits, Land, Environmental Review, Procurement

Construction / urban planning:
- Urban Development Committee: `https://www.minurban.am/en`
- Building-permit platform: `https://urban.e-gov.am`
- Alternative permit host seen in Armenian workflows: `https://urban-permits.e-gov.am`
- Official announcements: `https://azdarar.am`
- Cadastre: `https://cadastre.am`
- General government request portal: `https://e-request.am`

Permit queries:
```text
site:urban.e-gov.am "տվյալների կենտրոն"
site:urban.e-gov.am "data center"
site:minurban.am "data center" Armenia
site:minurban.am "Հրազդան"
site:minurban.am "Գագարին"
site:minurban.am "Աբովյան"
site:azdarar.am "տվյալների կենտրոն"
site:azdarar.am "շինարարության թույլտվություն" "տվյալների"
"{facility}" "շինարարության թույլտվություն"
"{facility}" "շահագործման թույլտվություն"
"{operator}" "construction permit" Armenia
site:yerevan.am "տվյալների կենտրոն"
```

Extract applicant, parcel/address, permit type, project function, area, expert-review requirement, issuing authority, date, and commissioning/operation status.

Environmental review:
- Ministry of Environment: `https://www.env.am`
```text
site:env.am "data center"
site:env.am "տվյալների կենտրոն"
"{facility}" "շրջակա միջավայրի վրա ազդեցության գնահատում"
"{operator}" "environmental impact" Armenia data center
```

Procurement:
- Armenian Electronic Procurement System: `https://armeps.am`
```text
site:armeps.am "տվյալների կենտրոն"
site:armeps.am "սերվերային"
site:armeps.am "UPS"
site:armeps.am "հովացման համակարգ"
site:armeps.am "supercomputer"
site:armeps.am "գերհամակարգիչ"
```

Grade: procurement award = **A** for buyer/procurement; it is **B/C** for final facility existence until commissioning or operator evidence appears.

## 5. Energy And Grid Validation

Primary energy sources:
- PSRC: `https://www.psrc.am`
- Electric Networks of Armenia tariffs: `https://www.ena.am/Info.aspx?id=11&lang=2`
- Ministry of Territorial Administration and Infrastructures: `https://www.mtad.am`
- IEA Armenia energy profile: `https://www.iea.org/reports/armenia-energy-profile`
- World Bank Armenia projects for grid/digital public infrastructure context.

Energy query templates:
```text
site:psrc.am "Ցանցին միացման կանոններ"
site:psrc.am "միացում" "ենթակայան"
site:psrc.am "Հրազդան" "ենթակայան"
site:psrc.am "Գագարին" "ենթակայան"
site:ena.am "տվյալների կենտրոն"
site:ena.am "միացում"
site:mtad.am "data center"
site:mtad.am "տվյալների կենտրոն"
"{facility}" "MW" Armenia
"{facility}" "MVA" Armenia
"{facility}" "220 kV" Armenia
"{operator}" "ենթակայան" Armenia
```

Rules:
- Do not convert MVA to MW unless the source does.
- Separate IT load, total facility power, grid connection, and roadmap capacity.
- Firebird: treat DC-1/phase-one power as operator/ministry-stated current or near-current values; treat 300 MW / 70,000+ GPUs / 2 GW as roadmap.
- OVIO: use 2 MW and 216 cabinets/racks from operator pages; older 218-rack investment pages are useful history but should not override current operator pages.
- Eleveight: use operator 512 B300 GPUs and 40 MW scaling language; use third-party 35 MW claims only as B until reconciled.

## 6. Per-Division Official Strategy

| Division | Official strategy | Known status after this review |
|---|---|---|
| Aragatsotn | Search VSData, Ashtarak, North-South highway, gorge/spring-water cooling; check urban.e-gov.am, azdarar.am, cadastre, ENA connection. | VSData planned / under-construction lead; no A-grade commissioning found. |
| Ararat | Search Artashat, Masis, Ararat marz governor, permits, procurement, server-room terms. | No verified DC found; negative-control division. |
| Armavir | Search Armavir city, Metsamor, Vagharshapat, energy/NPP context, permits/procurement. | No verified DC found; energy context only. |
| Yerevan | Search Viva, TeamCloud, YSU, Datacom/ADC, Arminco, Ucom, GNC-Alfa Yerevan, Cloudflare, e-government hosting, Yerevan permits. | Multiple A/B/C leads: Viva A, TeamCloud A for service, YSU A institutional, Cloudflare edge A-not-DC; older ISP addresses need corroboration. |
| Gegharkunik | Search Gagarin, Sevan, Gavar, Eleveight AI, Blackwell, NVIDIA B300, `Գագարին տվյալների կենտրոն`. | Eleveight AI Factory is A-grade operational in Gagarin; this division is no longer a negative control. |
| Kotayk | Search Hrazdan, Abovyan, Firebird, OVIO, GNC-Alfa, Hrazdan power station, substations, permits. | Highest-yield division: Firebird Hrazdan A; OVIO Abovyan A. |
| Lori | Search Vanadzor, Alaverdi, historical directory leads, marz governor permits/procurement. | Only old directory leads found; no verified DC. |
| Shirak | Search Gyumri, Shirak marz, tech centers, server rooms, procurement. | No verified DC; watch future AI/HPC announcements. |
| Syunik | Search Kapan, Goris, Meghri, Iran fiber corridor, border infrastructure. | No verified DC; telecom/fiber context only. |
| Tavush | Search Ijevan, Dilijan, Bagratashen, Georgia border, GNC-Alfa historical lead. | Bagratashen remains C-grade historical/network lead only. |
| Vayots Dzor | Search Yeghegnadzor, Jermuk, marz procurement, server rooms. | No verified DC. |

## 7. Final Grading Rules

Promote to **A** only when at least one primary source names the facility/project and at least one of location/status/capacity. Uptime Design Documents are A-grade for the design award, not proof of constructed Tier certification. Operator pages are A-grade for the operator's own facility claims but still reconcile conflicts with government, permit, and certification records.

Keep as **B** when a strong press/vendor source names the operator, location, and status but no primary source is available. Keep as **C** when evidence is directory-only, PeeringDB-only, marketplace-only, social-only, or a generic cloud/hosting page without facility details.

False positives to suppress: open-data portals, school / TUMO / smart-city IT rooms, broadband rollouts, CDN/IX PoPs without host facility, bank/ministry server-room modernization, energy plants without compute facility evidence, and AWS/Azure/GCP/OCI pages where `AM` is not Armenia.
