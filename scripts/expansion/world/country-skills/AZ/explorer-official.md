# AZ Explorer Official - Azerbaijan Datacenter Enumeration via Regulator, Permits, Energy, Cloud, and Certification Sources

Date: 2026-08-12. Country: **AZ Azerbaijan**. Division model: **rayon / municipality / autonomous republic** from `world-manifest.jsonl`. Angle: **official / regulatory / primary-source methodology** for enumerating operational, under-construction, and planned datacenter projects.

Reliability grades:
- **A** = official / primary source: Ministry of Digital Development and Transport (MINCOM), Information and Communication Technologies Agency (ICTA) operator register, State Committee on Urban Planning and Architecture / e-construction portal, e-procurement record, EIB / IFI financing page, Uptime Institute certificate list, operator official page, presidential / cabinet / state-company announcement, AzerEnergy / Azerishiq / AERA source, official cloud-region page.
- **B** = strong secondary source that quotes named officials/operators or republishes official project facts: AZERTAC, APA, Trend, AzerNews, DCD, Telecompaper, vendor case study.
- **C** = weak lead: directories, marketplace pages, PeeringDB-only / IX-only records, blogs, social posts, market reports without facility-level evidence.

---

## 0. Azerbaijan-specific structure

- Azerbaijan does **not** appear to have a public national datacenter permit register. Enumeration should combine **ICTA registration**, **Uptime certification**, **state cloud / AzInTelecom pages**, **urban-planning permits**, **e-procurement**, **energy connection evidence**, and **operator pages**.
- The state cloud path is unusually important. **AzInTelecom** is a state-owned / state-controlled cloud and telecom infrastructure provider under Azerbaijan's digital-development ecosystem and operates core **Government Cloud** infrastructure. Official and IFI sources identify data centers in **Baku** and **Yevlakh**, plus new green data centers in **Absheron** and **Hajigabul**.
- Uptime Institute is a high-yield primary-adjacent source for Azerbaijan. Its Azerbaijan country list includes facility names and locations for **Azerconnect, AzInTelecom, Central Bank, Delta Telecom, PASHA Technology, and State Customs Committee** projects.
- Azerbaijani public pages may use Azerbaijani, English, Russian, and Turkish-like terminology. Search all of: `data center`, `datacenter`, `data centre`, `data mərkəzi`, `data merkezi`, `verilənlər mərkəzi`, `məlumat mərkəzi`, `hesablama mərkəzi`, `ehtiyat data mərkəzi`, `Hökumət buludu`, `G-cloud`, `bulud xidmətləri`, Russian `дата-центр`, `центр обработки данных`, `ЦОД`.
- Treat **Cloudflare / CDN / IX PoP** locations as edge/network locations unless an underlying facility is identified. Treat **cloud region / availability zone** claims as service evidence, not automatically a standalone datacenter.

Highest-yield divisions:
- **Baku**: AzInTelecom Baku MDC / New Data Protection Center, Delta Telecom, PASHA Technology BMDC, Central Bank, State Customs, Azerconnect, Cloudflare/edge, telecom operator facilities.
- **Yevlakh City**: AzInTelecom Yevlakh Reserve Data Center / availability zone.
- **Absheron / Gobustan**: AzInTelecom Absheron Main Data Center modules; check both because Uptime lists Gobustan while financing/press often says Absheron.
- **Hajigabul / Pirsaat**: AzInTelecom Hajigabul Reserve Data Center modules; check both district and settlement name.
- **Goychay**: PASHA Technology Disaster Recovery Site.
- **Agdash**: Azerconnect Agdash Data Center certification lead.
- **Sumgayit**: STDC / Sumgait Technologies Data Center lead in Sumgayit Chemical Industrial Park.
- **Nakhchivan**: planned state / autonomous-republic datacenter through Nakhchivan state program and tender reporting.

---

## 1. Official telecom / cloud regulator workflow

### 1.1 MINCOM and ICTA

Primary portals:
- Ministry of Digital Development and Transport: https://mincom.gov.az/en
- Registered operators/providers list: https://mincom.gov.az/en/ministry/e-registration/information-on-registered-operators-and-providers
- Telecommunications activity overview: https://mincom.gov.az/en/activity/telecommunications
- ICTA / regulator references appear on MINCOM pages; the operator/provider list is the best public registry entry point.

How to use:
1. Search the registered operators/providers list for candidate operators: `AzInTelecom`, `AzerTelecom`, `Aztelekom`, `Baktelecom`, `Delta Telecom`, `PASHA Technology`, `Azerconnect`, `Azercell`, `Bakcell`, `Azerfon`, `STDC`, `Gcore`, `hosting`.
2. Capture legal name, activity category, services, date, register number, and notes. The MINCOM list explicitly includes provider types such as **operator**, **internet provider**, and **hosting provider**; it is **A** for entity authorization and **C** for a facility unless paired with facility evidence.
3. Pivot each legal name to Uptime, official operator pages, e-procurement, construction portal, and local-language news.

Registry query templates:
```text
site:mincom.gov.az "{operator}" "hosting provider"
site:mincom.gov.az "{operator}" "Internet provider"
site:mincom.gov.az "{operator}" "registered operators and providers"
site:mincom.gov.az "data center" Azerbaijan
site:mincom.gov.az "data mərkəzi"
site:mincom.gov.az "Hökumət buludu"
site:mincom.gov.az "AzInTelecom" "Yevlakh"
site:mincom.gov.az "AzInTelecom" "Baku" "data center"
site:mincom.gov.az "AzInTelecom" "Tier III"
```

Grade guidance:
- MINCOM / ICTA registry = **A** for telecom / internet / hosting registration.
- Registry-only host provider = **C** for datacenter enumeration.
- Registry + Uptime / operator facility page / permit = **A** for facility existence.

### 1.2 Government Cloud / AzInTelecom official pipeline

Primary sources:
- AzInTelecom news and official pages: https://azintelecom.az/en/
- Government Cloud migration articles on AzInTelecom: query `site:azintelecom.az/en/news "Government Cloud" "Baku Data Center"` and `site:azintelecom.az/en/news "Yevlakh" "data centers"`
- Official green datacenter announcement: https://azintelecom.az/en/news/azerbaycanda-yasil-texnologiyalar-esasinda-iki-yeni-data-merkezi-tikilecek
- EIB Global financing page: https://www.eib.org/en/press/all/2024-527-azerbaijan-to-digitise-public-administration-with-eur43-million-loan-from-eib-global

Known official facts to anchor enumeration:
- EIB Global signed a **EUR 43m** loan to state-owned **AzInTelecom LLC** for two new state-of-the-art data centers; EIB says the project is due to complete in **2027** and identifies the planned regions as **Absheron** and **Hajigabul**.
- EIB says AzInTelecom provides cloud services through data centers in **Baku** and **Yevlakh**.
- AzInTelecom's green-technology announcement states two new green technology data centers will be built in Azerbaijan and operated by AzInTelecom. Use it as official project intent, then harden with Uptime, EIB, procurement, construction permits, and regional planning.

AzInTelecom query templates:
```text
site:azintelecom.az/en "data center" "Baku"
site:azintelecom.az/en "data center" "Yevlakh"
site:azintelecom.az/en "Government Cloud" "data centers"
site:azintelecom.az/en "Hökumət buludu" "data mərkəzi"
site:azintelecom.az/en "Absheron" "data center"
site:azintelecom.az/en "Hajigabul" "data center"
site:azintelecom.az/en "LEED" "data center"
site:azintelecom.az/en "solar panels" "data center"
site:azintelecom.az/en "Pirsaat" OR "Gobustan"
```

Extract: named facility, division/settlement, current status, completion year, operator, certification, whether the source says operational vs planned, sustainability attributes, and whether capacity is disclosed. Do not infer MW if only green / cloud / certification language is available.

---

## 2. Uptime and certification workflow

Primary source:
- Uptime Institute Azerbaijan country list: https://uptimeinstitute.com/uptime-institute-awards/country/id/AZ

High-yield Uptime records to enumerate / validate:
- **Azerconnect Baku Data Center** - Baku - Tier IV Certification of Design Documents.
- **Azerconnect Agdash Data Center** - Agdash - Tier III Certification of Design Documents.
- **AzInTelecom Baku Main Data Center (MDC)** - Baku - Tier III Design + Constructed Facility.
- **AzInTelecom Yevlakh Reserve Data Center (RDC)** - Yevlakh - Tier III Design + Constructed Facility.
- **AzInTelecom Baku New Data Protection Center** - Baku - Tier III Design + Constructed Facility.
- **AzInTelecom Absheron Main Data Center, Modules M1-M5** - Uptime location shown as Gobustan - Tier III Design.
- **AzInTelecom Hajigabul Reserve Data Center, Modules M1 and M2** - Uptime location shown as Pirsaat - Tier III Design.
- **Central Bank of Azerbaijan CBAR Main Data Center** - Baku - Tier III Design + Constructed Facility.
- **Delta Telecom Baku Main Data Center (DTMDC)** - Baku - Tier III Design + Constructed Facility.
- **PASHA Technology Baku Main Data Center (BMDC)** - Baku - Tier III Design + Constructed Facility.
- **PASHA Technology Goychay Disaster Recovery Site (GDRS)** - Goychay - Tier III Design + Constructed Facility.
- **State Customs Committee DGK Main Data Center Baku** - Baku - Tier III Design.

Uptime workflow:
```text
site:uptimeinstitute.com/uptime-institute-awards/country/id/AZ Azerbaijan
site:uptimeinstitute.com "Azerbaijan" "Data Center" "Tier"
site:uptimeinstitute.com "{operator}" "{division}"
site:uptimeinstitute.com "{facility name}"
```

Grade:
- Uptime = **A** for certification existence, facility name, operator/client, and city/locality shown.
- Uptime Design-only certification does **not** prove operational status. Treat as `approved` or `planned/construction` until operator, constructed-facility certificate, press, permit, or commissioning source confirms.
- Uptime city/locality can conflict with administrative division naming. Record both: e.g. **Absheron project with Uptime locality Gobustan**, **Hajigabul project with Uptime locality Pirsaat**.

---

## 3. Urban planning, permits, and procurement

### 3.1 State Committee on Urban Planning and Architecture

Primary portals:
- State Committee on Urban Planning and Architecture: https://www.arxkom.gov.az/en/
- Electronic Construction Portal / single-window references: `e-tikinti.gov.az`, `birpencere.arxkom.gov.az`, and State Committee service/news pages.
- State Committee news on electronic permits: https://www.arxkom.gov.az/en/media/xeberler/butun-nov-tikinti-obyektlerinin-istismarina-icazelerin-elektron-sistem-vasitesile-verilmesine-baslanilib

Method:
- Use State Committee / e-construction pages to identify whether construction and occupancy permits are handled through the electronic system. Public search may not expose all permit files, so use the portal as a validation layer and search the Committee site for announcements, master plans, interactive maps, and regional plans.
- For large datacenters, also search district executive authority pages, industrial park pages, and environmental / energy documents. In Azerbaijan, project facts often surface through state news and IFI financing before detailed permit material is public.

Permit query templates:
```text
site:arxkom.gov.az "data center"
site:arxkom.gov.az "data mərkəzi"
site:arxkom.gov.az "məlumat mərkəzi"
site:arxkom.gov.az "tikintiyə icazə" "data"
site:arxkom.gov.az "istismara icazə" "data"
site:arxkom.gov.az "AzInTelecom"
site:arxkom.gov.az "Absheron" "AzInTelecom"
site:arxkom.gov.az "Hajigabul" "AzInTelecom"
site:e-tikinti.gov.az "data mərkəzi"
site:birpencere.arxkom.gov.az "data mərkəzi"
"{division}" "data mərkəzi" "tikintiyə icazə"
"{division}" "data center" "construction permit" Azerbaijan
"{operator}" "tikintiyə icazə"
"{facility}" "istismara icazə"
```

Extract: permit type (construction vs operation), application/client, parcel/address, project function, gross area, expert assessment requirement, occupancy/commissioning date, and local executive authority.

### 3.2 Public procurement

Primary portal:
- Azerbaijan public procurement portal: https://etender.gov.az/

Search for public-sector data-center construction, server-room modernization, UPS, cooling, fire suppression, backup generators, and Nakhchivan state-program tenders.

Procurement query templates:
```text
site:etender.gov.az "data mərkəzi"
site:etender.gov.az "verilənlər mərkəzi"
site:etender.gov.az "məlumat mərkəzi"
site:etender.gov.az "server otağı"
site:etender.gov.az "Hökumət buludu"
site:etender.gov.az "AzInTelecom"
site:etender.gov.az "UPS" "data"
site:etender.gov.az "soyutma" "server"
site:etender.gov.az "Naxçıvan" "data mərkəzi"
```

Grade:
- Award / tender document = **A** for procurement event and buyer.
- Tender alone = **B/C** for final facility existence unless the award/contract and later commissioning are found.

---

## 4. Energy, grid, and sustainability validation

Primary sources:
- Azerbaijan Energy Regulatory Agency (AERA): https://regulator.gov.az/en/
- AERA electricity market structure: https://regulator.gov.az/en/elektrik/elektrik-enerjisi-sebekesi-ve-daxili-topdansatis-bazari
- Ministry of Energy: https://minenergy.gov.az/
- AzerEnergy OJSC: https://azerenerji.gov.az/
- Azerishiq OJSC: https://www.azerishiq.az/
- Azerbaijan Renewable Energy Agency (AREA): https://area.gov.az/

Official grid structure to remember:
- AERA describes Azerbaijan as having a vertically integrated electricity market.
- **AzerEnergy** is state-owned and performs producer/transmission-system functions, including 110 kV and above transmission lines/substations.
- **Azerishiq** performs distribution and supply functions for distribution lines up to 110 kV.

Energy query templates:
```text
site:regulator.gov.az "data center"
site:regulator.gov.az "data mərkəzi"
site:azerenerji.gov.az "data center"
site:azerenerji.gov.az "data mərkəzi"
site:azerishiq.az "data mərkəzi"
site:azerishiq.az "AzInTelecom"
site:minenergy.gov.az "data center" Azerbaijan
site:area.gov.az "data center"
site:area.gov.az "AzInTelecom"
"{facility}" "MW" Azerbaijan
"{facility}" "MVA" Azerbaijan
"{facility}" "solar panels" "data center"
"{division}" "yarımstansiya" "data mərkəzi"
"{division}" "substation" "data center"
"{operator}" "LEED" "data center" Azerbaijan
```

What to extract:
- Contracted electrical demand, transformer / substation name, MVA / MW values, backup generator count, solar / renewable component, natural cooling / water efficiency language, and whether the energy evidence belongs to the datacenter itself or only to a nearby infrastructure project.

Capacity rules:
- Do not convert MVA to IT MW without an explicit source.
- Do not assign project-wide financing (e.g. EUR 43m for two sites) to one site unless the source splits it.
- LEED / green-technology claims validate sustainability intent, not datacenter capacity.

---

## 5. Official cloud / edge source checks

Check these official pages every run because cloud regions and edge locations change:

| Provider | Official source | Azerbaijan signal / use |
|---|---|---|
| AWS | Regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Local Zones: https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | No official Azerbaijan AWS Region or Local Zone found in searched official pages. Use as negative control; do not count partner hosting as AWS-owned DC. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No official Azure public cloud region in Azerbaijan found in searched region list. Search partner cloud / sovereign cloud separately. |
| Google Cloud | https://cloud.google.com/about/locations | No official Google Cloud region in Azerbaijan found in searched locations page. |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ | No official OCI public region in Azerbaijan found in searched region list. |
| Cloudflare | https://www.cloudflare.com/network/ and https://www.cloudflarestatus.com/locations | Official network pages list Baku / Azerbaijan locations in recent search results. Count as **edge PoP / network location**, not a standalone DC unless facility host is known. |
| Gcore / AzInCloud | https://gcore.com/press-releases/azintelecom and https://azincloud.az/en/about | Sovereign / regional cloud lead with AzInTelecom. Use as cloud-service evidence and pivot to AzInTelecom Baku/Yevlakh/Absheron/Hajigabul facilities. |
| Lenovo / AzInTelecom HPC | https://news.lenovo.com/pressroom/press-releases/azerbaijan-first-supercomputer-on-lenovo-infrastructure/ | Official vendor evidence for Azerbaijan's first Supercomputer Center with AzInTelecom; needs site/address confirmation before treating as separate facility. |

Cloud query templates:
```text
"Azerbaijan" "AWS Region" site:aws.amazon.com
"Azerbaijan" "Azure region" site:learn.microsoft.com
"Azerbaijan" "Google Cloud region" site:cloud.google.com
"Azerbaijan" "Oracle Cloud region" site:oracle.com
"Baku" "Cloudflare" "data center" site:cloudflare.com
"AzInTelecom" "Gcore" "sovereign cloud"
"AzInCloud" "Regional Accessibility Zone"
"Lenovo" "AzInTelecom" "Supercomputer Center"
```

---

## 6. Per-division official enumeration workflow

### 6.1 Division tiering

1. **Tier 1 - exhaustive official sweep**: Baku, Yevlakh City, Absheron, Gobustan, Hajigabul, Goychay, Agdash, Sumgayit, Nakhchivan. Run MINCOM/ICTA, Uptime, AzInTelecom, e-construction, energy, procurement, and official operator searches.
2. **Tier 2 - state infrastructure / regional validation**: Ganja, Mingachevir, Shirvan, Lankaran City, Shaki City, Naftalan, Yevlakh district, Lankaran, Khizi, Salyan, Astara, Fuzuli, Shusha, Zangilan, Aghdam. Search government cloud migration, smart-city / reconstruction, local executive authorities, e-procurement, and energy substations. Expect many no-project outcomes.
3. **Tier 3 - negative-control sweep**: all remaining rayons. Use local-language aliases plus national operator/certification checks; record no-project if only general broadband, smart village, CCTV, school server-room, or unrelated `data` hits appear.

### 6.2 Copy-paste official workflow

```text
1. Convert division to Azerbaijani/Russian aliases:
   Baku/Baki/Bakı/Баку; Absheron/Abseron/Abşeron/Апшерон; Yevlakh/Yevlax/Евлах;
   Hajigabul/Haciqabul/Hacıqabul; Gobustan/Qobustan; Goychay/Goycay/Göyçay;
   Agdash/Agdas/Ağdaş; Sumgayit/Sumqayit; Nakhchivan/Naxcivan/Naxçıvan.

2. Certification sweep:
   site:uptimeinstitute.com "Azerbaijan" "{division}"
   site:uptimeinstitute.com "{operator}" "{division}"

3. Regulator/entity sweep:
   site:mincom.gov.az "{division}" "data center"
   site:mincom.gov.az "{division}" "data mərkəzi"
   site:mincom.gov.az "{operator}" "hosting provider"

4. State cloud/operator sweep:
   site:azintelecom.az "{division}" "data center"
   site:azintelecom.az "{division}" "Hökumət buludu"
   site:azintelecom.az "{division}" "data mərkəzi"

5. Permit/procurement/energy sweep:
   site:arxkom.gov.az "{division}" "data mərkəzi"
   site:etender.gov.az "{division}" "data mərkəzi"
   site:azerenerji.gov.az "{division}" "data mərkəzi"
   site:azerishiq.az "{division}" "data mərkəzi"

6. Validate administrative assignment:
   If source says locality (Gobustan/Pirsaat/Yevlakh town) that differs from project-region language
   (Absheron/Hajigabul/Yevlakh district), record the source wording in notes and assign to the manifest
   division that best matches the locality, unless an official source explicitly assigns the project region.
```

### 6.3 Alias table for known leads

| Manifest division | Also query | Official rationale |
|---|---|---|
| Baku | `Bakı`, `Baki`, `Баку`, `MDC`, `BMDC`, `DTMDC`, `DGK`, `CBAR`, `Azerconnect Baku`, `Baku New Data Protection Center` | Most certified and enterprise/state facilities are in Baku. |
| Yevlakh City | `Yevlax`, `Yevlakh town`, `Reserve Data Center`, `RDC`, `availability zone` | AzInTelecom Yevlakh RDC / availability zone. |
| Yevlakh | `Yevlax rayonu` | Check separately from Yevlakh City; avoid duplicate assignment. |
| Absheron | `Abşeron`, `Abseron`, `Gobustan`, `Qobustan`, `Absheron Main Data Center` | EIB/AzInTelecom say Absheron; Uptime lists Gobustan locality. |
| Gobustan | `Qobustan`, `Absheron Main Data Center`, `M1-M5` | Uptime locality for Absheron Main Data Center modules. |
| Hajigabul | `Hacıqabul`, `Haciqabul`, `Pirsaat`, `Hajigabul Reserve Data Center` | EIB/AzInTelecom say Hajigabul; Uptime lists Pirsaat locality. |
| Goychay | `Göyçay`, `Goycay`, `GDRS`, `Disaster Recovery Site` | PASHA Technology Goychay DR site. |
| Agdash | `Ağdaş`, `Agdas`, `Azerconnect Agdash` | Uptime Tier III design lead. |
| Sumgayit | `Sumqayıt`, `Sumqayit`, `STDC`, `Sumgait Technologies Data Center`, `Chemical Industrial Park` | Presidential/AZERTAC industrial-park lead. |
| Nakhchivan | `Naxçıvan`, `Naxcivan`, `Nakhchivan City Communication Department`, `Tier-3 data mərkəzi` | Planned autonomous-republic state datacenter; use procurement/state program confirmation. |

---

## 7. Common false positives

- `data` as generic statistics/open-data pages; require `mərkəzi`, `center`, `cloud`, `server`, `hosting`, `Tier`, or operator context.
- `AzDataCom` network project: useful telecom backbone context, but not every AzDataCom node is a datacenter.
- Cloudflare / CDN / IX locations: count as edge/network only unless the host facility is identified.
- Institutional `server otağı` / server room tenders: record only if the project is explicitly a datacenter or materially datacenter-like and public-facing enough for the dataset.
- Nagorno-Karabakh / post-conflict reconstruction hits: smart-city, telecom restoration, e-government office, or base-station work is not a datacenter without facility evidence.
