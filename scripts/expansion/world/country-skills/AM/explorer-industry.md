# AM Explorer Industry - Armenia Datacenter Enumeration via Operators, Trade Press, Directories, and Regional Queries

Date: 2026-08-12. Scope: industry, operator, trade-press, and directory methodology for finding Armenia datacenter facilities by first-level division. Division model: **Aragatsotn; Ararat; Armavir; Yerevan; Gegharkunik; Kotayk; Lori; Shirak; Syunik; Tavush; Vayots Dzor**.

Reliability grades:
- **A** = operator / official / certification / IFI / regulator source.
- **B** = strong trade, vendor, or national press source with named operator, location, and status.
- **C** = directory, marketplace, PeeringDB-only, blog, social, or market-report lead requiring confirmation.

## 1. Market Structure After Verification

Armenia is no longer only a small Yerevan colo market. As of this review, the verified market has four high-yield facility clusters:

1. **Kotayk**: Firebird AI Factory in Hrazdan and OVIO / GNC-ALFA Data Center Abovyan.
2. **Gegharkunik**: Eleveight AI Factory in Gagarin, now A-grade operator/ministry confirmed.
3. **Yerevan**: Viva data centers, TeamCloud / Team Telecom Armenia DC, Yerevan State University AI Data Center / supercomputer, plus older ISP/operator leads.
4. **Aragatsotn**: VSData green data center lead, still planned / under-construction unless new commissioning evidence is found.

No official AWS, Azure, Google Cloud, or Oracle Cloud public region was found for Armenia. Cloudflare Yerevan is an edge PoP, not a standalone datacenter unless the host facility is identified.

## 2. Operator And Project Seed List

| Operator / project | Division | Search anchors | Verified handling | Grade seed |
|---|---|---|---|---|
| Firebird AI Factory / DC-1 Hrazdan | Kotayk | `Firebird Hrazdan AI factory`, `Firebird DC-1 Hrazdan`, `Firebird NVIDIA DSX Armenia`, `Firebird 70,000 GPUs 300 MW Armenia` | Operator and NVIDIA confirm operational Hrazdan AI factory. Use Firebird pages for current DC-1 values and NVIDIA/ministry for roadmap. Distinguish 15/18 MW current/phase-one language from 300 MW roadmap. | A |
| Eleveight AI Factory | Gegharkunik | `Eleveight AI Gagarin`, `Eleveight AI data center Gortsaranayin 1`, `NVIDIA B300 Gagarin`, `Գագարին տվյալների կենտրոն` | Operator says first AI Factory in Gagarin, 512 NVIDIA B300 GPUs, first-phase $120m, scaling to 40 MW; contact page gives `Gortsaranayin Street 1, Gagarin, Armenia`. High-Tech Ministry and Armenpress confirm opening in Gagarin, Gegharkunik. | A |
| OVIO / GNC-ALFA Data Center Abovyan | Kotayk | `OVIO Data Center Abovyan`, `GNC-ALFA Data Center Abovyan Uptime`, `OVIO 2 MW 216 racks` | Operator pages and Uptime record confirm Abovyan facility. Use 2 MW / 216 racks from current operator pages; use Uptime record for Tier III Certification of Design Documents only. | A |
| VSData green data center | Aragatsotn | `VSData Armenia 2MW`, `VSData Aragatsotn gorge`, `spring water cooled data center Armenia`, `VSDATA 125 racks` | Operator site plus DCD/Developing Telecoms confirm planned 2 MW / 125-rack green DC outside Yerevan in Aragatsotn with spring-water cooling. No A-grade commissioning found in this review. | B+ |
| Viva Armenia | Yerevan | `Viva colocation Yerevan data centers`, `Viva Data Centers 2N`, `viva.am colocation` | Official Viva pages state data centers in Yerevan with 2N power/cooling, dual HV feeds, diesel generators, UPS, security, fire suppression. | A |
| TeamCloud / Team Telecom Armenia | Yerevan | `TeamCloud colocation`, `Team Telecom Armenia data center`, `TeamCloud cloud servers Armenia` | Official TeamCloud pages state colocation and cloud servers in Team Telecom Armenia data center and Tier III international standards. Facility address needs a separate corroborating source. | A for service; C/B for address |
| Yerevan State University AI Data Center | Yerevan | `YSU supercomputer 64 NVIDIA H100`, `Yerevan State University AI Data Center Legrand`, `գերհամակարգիչ ԵՊՀ` | YSU confirms government-funded 64 NVIDIA H100 supercomputer installed at YSU; Legrand/DCD vendor coverage describes AI data center infrastructure. Count as institutional/research HPC, not commercial colo. | A/B |
| Datacom / ADC Core Network | Yerevan | `ADC Core Network 1 Hrachya Kochar`, `Armenian Datacom Company data center`, `Datacom Armenia colocation` | Directory/trade lead for Yerevan facility. Promote only with current operator page, permit, procurement, or corporate document. | C/B |
| Arminco AIC | Yerevan | `Arminco data center Yerevan`, `Arminco AIC colocation`, `Nikol Duman 62 Arminco` | Historical ISP/directory lead. Treat address and status as stale until reverified. | C |
| Ucom | Yerevan | `Ucom colocation Manandyan 33/8`, `Ucom hosting Armenia`, `Ucom data center Yerevan` | Telecom/hosting lead; SPYUR/directory evidence is insufficient for a standalone facility. | C/B |
| GNC-Alfa Yerevan | Yerevan | `GNC-Alfa Yerevan 4 Tigran Mets`, `GNC-Alfa data center Yerevan` | Historical directory lead; GNC-Alfa/OVIO Abovyan is the verified facility. | C |
| Cloudflare Yerevan #103 | Yerevan | `Cloudflare Yerevan data center 103`, `Cloudflare Armenia network` | Official Cloudflare edge PoP announced 2017. Count only as edge/network location. | A-not-DC |
| Bagratashen / Vanadzor historical leads | Tavush / Lori | `Bagratashen data center GNC-Alfa`, `Vanadzor data center Armenia` | Directory-only historical leads. Use to seed searches, not enumeration. | C |

## 3. High-Yield Source List

### Official / operator / certification

| Source | URL / query | Use | Grade |
|---|---|---|---|
| Firebird | `https://www.firebird.ai/`, `https://www.firebird.ai/data-centers.html`, `https://www.firebird.ai/news-firebird-grand-opening.html` | Current Firebird facility and roadmap claims. | A |
| NVIDIA blog | `https://blogs.nvidia.com/blog/firebird-ai-factory-armenia-blackwell-rubin-dsx/` | Official NVIDIA account of Firebird GPUs / MW roadmap. | A |
| Ministry of High-Tech Industry | `https://hightech.gov.am`, old archive `https://old.hightech.gov.am` | Firebird, Eleveight, YSU/HPC policy, government MoUs. | A |
| Eleveight AI | `https://eleveight.ai/en/`, `https://eleveight.ai/en/company/`, `https://eleveight.ai/en/contact/` | Gagarin facility, address, GPUs, scaling target. | A |
| OVIO | `https://ovio.am/en/data-center`, `https://ovio.am/en/about-us`, `https://oviocloud.am/en/about-us`, `https://oviocloud.am/en/colocation` | Abovyan operator claims, 2 MW, racks/cabinets, ISO/PCI, services. | A |
| Uptime Institute | `https://uptimeinstitute.com/uptime-institute-awards/datacenter/data-center-abovyan/2188` | GNC-ALFA Data Center "Abovyan" Tier III Design Documents award. | A |
| Viva | `https://www.viva.am/en/business-solutions/cloud-and-it-solutions/web/colocation`, `https://www.viva.am/en/colocationss` | Viva Yerevan colocation and redundancy details. | A |
| TeamCloud | `https://teamcloud.am/colocation.php`, `https://teamcloud.am/cloud-server.php` | Team Telecom Armenia DC service evidence. | A |
| YSU | `https://www.ysu.am/en/news/90809` | Government-funded 64-H100 supercomputer at YSU. | A |
| VSData | `https://vsdata.org/` | Planned green DC project. Operator site is useful but status must be corroborated. | B+/A for self-claim only |
| Cloud providers | AWS/Azure/GCP/OCI official region pages | Negative controls for public cloud regions. | A |

### Trade / vendor / national press

| Source | Query | Use | Grade |
|---|---|---|---|
| Data Center Dynamics | `site:datacenterdynamics.com Armenia data center`, `site:datacenterdynamics.com Firebird Hrazdan`, `site:datacenterdynamics.com Eleveight Gagarin`, `site:datacenterdynamics.com VSData` | Best English trade index for Firebird, Eleveight, OVIO, VSData, YSU. | B |
| Armenpress | `site:armenpress.am Eleveight Gagarin`, `site:armenpress.am "տվյալների կենտրոն"`, `site:armenpress.am Firebird Hrazdan` | State news agency, useful for ministry-backed announcements. | B+/A when directly reporting government action |
| ARKA / ARKATelecom | `site:arka.am OVIO data center`, `site:arkatelecom.am OVIO`, `site:arka.am Firebird Hrazdan` | Armenian business/telecom wire; good for launch, financing, ownership, certificates. | B |
| Legrand / Data Center Frontier | `Legrand Yerevan State University AI data center`, `site:datacenterfrontier.com Armenia Yerevan State University AI Data Center` | Vendor case-study evidence for YSU facility build-out. | B/A depending source page |
| Developing Telecoms | `site:developingtelecoms.com VSData Armenia` | VSData spring-water/gorge design summary. | B |
| Data Center Knowledge / The Tech Capital / Data Centre Central | `VSData Armenia data centre` | VSData secondary corroboration. | B |
| Telecompaper | `site:telecompaper.com Armenia data centre` | Older OVIO/GNC-Alfa/telecom project history. | B |
| Kommersant / regional business press | `GNC-Alfa Fedilco Viva Armenia` | Ownership context only; do not use for facility status by itself. | B |

### Directories and network databases

Use only as lead sources:
- `https://www.datacentermap.com/armenia/` and `https://www.datacentermap.com/armenia/yerevan/`
- `https://www.datacenterjournal.com/data-centers/armenia/`
- `https://www.datacenters.com/locations/armenia`
- `site:inflect.com Armenia data center`
- `site:cloudscene.com Armenia`
- `https://www.peeringdb.com`
- `site:whtop.com Armenia hosting colocation`
- `site:spyur.am "co-location" Armenia`

Directory cautions:
- Some directories place non-Yerevan facilities under the Yerevan metro. Preserve actual locality/division from primary sources: Hrazdan = Kotayk, Abovyan = Kotayk, Gagarin = Gegharkunik, VSData = Aragatsotn lead.
- Directory "operational" tags for VSData or other planned projects need primary confirmation.
- PeeringDB proves network/facility presence, not MW, construction, or commercial DC status.

## 4. Query Patterns

### Broad discovery

```text
"{division}" "data center" Armenia
"{division}" "datacenter" Armenia
"{division}" "data centre" Armenia
"{division}" "colocation" Armenia
"{division}" "AI factory" Armenia
"{division}" "supercomputer" Armenia
"{am_alias}" "տվյալների կենտրոն"
"{am_alias}" "տվյալների մշակման կենտրոն"
"{am_alias}" "սերվերային սենյակ"
"{am_alias}" "կոլոկացիա"
"{ru_alias}" "дата-центр"
"{ru_alias}" "ЦОД"
"{ru_alias}" "центр обработки данных"
```

### Status and capacity

```text
"{facility}" "opened" Armenia
"{facility}" "launched" Armenia
"{facility}" "commissioned" Armenia
"{facility}" "under construction" Armenia
"{facility}" "MW" Armenia
"{facility}" "MVA" Armenia
"{facility}" "racks" Armenia
"{facility}" "cabinets" Armenia
"{am_alias}" "տվյալների կենտրոն" "գործարկվել է"
"{am_alias}" "տվյալների կենտրոն" "շահագործման է հանձնվել"
"{am_alias}" "տվյալների կենտրոն" "կառուցվում է"
"{am_alias}" "գերհամակարգիչ"
```

### Source-scoped

```text
site:hightech.gov.am "data center" Armenia
site:old.hightech.gov.am "data center" Armenia
site:gov.am "տվյալների կենտրոն"
site:mineconomy.am "Infrastructure in Exchange for Investment" "data center"
site:arlis.am "տվյալների կենտրոն"
site:firebird.ai Hrazdan
site:eleveight.ai Gagarin
site:ovio.am Abovyan data center
site:oviocloud.am Abovyan data center
site:viva.am colocation data center
site:teamcloud.am colocation
site:ysu.am supercomputer NVIDIA H100
site:vsdata.org Armenia data center
site:uptimeinstitute.com Armenia Abovyan
site:datacenterdynamics.com Armenia "data center"
site:armenpress.am "data center" Armenia
site:arka.am "data center" Armenia
```

## 5. Per-Division Industry Workflow

| Division | Aliases / localities | Workflow | Current expectation |
|---|---|---|---|
| Aragatsotn | `Արագածոտն`, `Арагацотн`, Ashtarak, Talin, North-South Hwy, VSData | Start with VSData, then check DCD/DevelopingTelecoms/directories, then permits/ENA/cadastre for commissioning. | One B+ planned/under-construction lead. |
| Ararat | `Արարատ`, `Арарат`, Artashat, Masis, Vedi | Run negative sweep across press, marz governor, procurement, permit, server-room terms. | No verified DC. |
| Armavir | `Արմավիր`, `Армавир`, Armavir, Vagharshapat, Metsamor | Watch energy/NPP false positives; search server-room and procurement terms. | No verified DC. |
| Yerevan | `Երևան`, `Ереван`, Viva, TeamCloud, YSU, Datacom, ADC, Arminco, Ucom, GNC-Alfa, Cloudflare | Full operator sweep, then directories for stale address leads, then Yerevan permits and procurement. Separate commercial colo, institutional HPC, and edge PoPs. | Viva A; TeamCloud A for service; YSU A/B; Cloudflare edge only; older ISP leads C/B. |
| Gegharkunik | `Գեղարքունիք`, `Гегаркуник`, Gagarin, Sevan, Gavar, Eleveight | Search Eleveight first, then ministry/Armenpress, DCD, operator contact/address, permits/energy. | Eleveight Gagarin A-grade operational AI factory. |
| Kotayk | `Կոտայք`, `Котайк`, Hrazdan, Abovyan, Gagarin false-positive check, Firebird, OVIO, GNC-Alfa | Highest-yield marz: verify Firebird and OVIO each run; check Hrazdan power station / substations and Abovyan permits. | Firebird A; OVIO Abovyan A. |
| Lori | `Լոռի`, `Лори`, Vanadzor, Alaverdi | Recheck old Vanadzor directory lead; search local press/procurement. | No verified DC; historical lead only. |
| Shirak | `Շիրակ`, `Ширак`, Gyumri | Search tech-center/HPC claims carefully; suppress TUMO/education-only facilities unless a compute facility is named. | No verified DC. |
| Syunik | `Սյունիք`, `Сюник`, Kapan, Goris, Meghri | Search Iran-border fiber and disaster-recovery claims; suppress telecom corridor evidence unless facility named. | No verified DC. |
| Tavush | `Տավուշ`, `Тавуш`, Ijevan, Dilijan, Bagratashen | Recheck Bagratashen border/GNC-Alfa historical lead; use only as C until primary evidence appears. | No verified DC. |
| Vayots Dzor | `Վայոց Ձոր`, `Вайоц-Дзор`, Yeghegnadzor, Jermuk | Negative sweep; beware tourism/smart-city false positives. | No verified DC. |

## 6. Extraction Rules

For every candidate extract:
- Facility name as stated.
- Operator / legal entity / developer.
- Division and locality/address. Do not let metro-area directory pages override actual division.
- Status: operational, under construction, planned, design-certified only, institutional, edge PoP, unknown.
- Capacity exactly as stated: MW, IT MW, racks/cabinets, GPUs, sq m, sq ft, MVA. Preserve units and source wording.
- Facility type: commercial colo/cloud, AI/GPU factory, institutional/research HPC, enterprise/government internal, disaster recovery, edge/network PoP, server room.
- Source chain: primary first, then B/C corroboration.

Promotion rules:
- **A**: operator page, ministry/government page, Uptime record, permit/commissioning, regulated utility/energy source directly tied to the facility.
- **B**: DCD, Armenpress, ARKA, vendor case study, Telecompaper, or equivalent with named operator and location.
- **C**: DataCenterMap, DataCenterJournal, datacenters.com, Inflect, Cloudscene, PeeringDB, whtop, SPYUR, social, or market reports without corroboration.

False positives:
- CDN/edge/IX location without host facility.
- Generic cloud resale or VPS plans without a named data center.
- Education centers, TUMO, smart village, smart city, digitization portals.
- Bank/government server-room modernization unless described as a data center.
- Hrazdan TPP, Metsamor NPP, substations, solar projects unless tied to a compute facility.
- `AM` as an abbreviation unrelated to Armenia in cloud/global-region pages.
