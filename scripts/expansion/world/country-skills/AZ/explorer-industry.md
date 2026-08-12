# AZ Explorer Industry - Azerbaijan Datacenter Enumeration via Operators, Trade Press, Directories, and Region Query Patterns

Date: 2026-08-12. Scope: **industry / trade-press / operator-led methodology** for enumerating Azerbaijan datacenter projects at rayon / municipality / autonomous-republic level. Reliability grades: **A** = official/operator/certification/IFI/regulator source; **B** = strong trade press or vendor case study; **C** = directory, marketplace, PeeringDB-only, blog, social, or market-report lead requiring confirmation.

---

## 0. Market structure

- Azerbaijan's public datacenter market is concentrated in **Baku** and state-linked infrastructure. The most repeatable enumeration path is not a generic web crawl; it is an **operator/certification sweep** anchored on AzInTelecom, Uptime Institute, Delta Telecom, PASHA Technology, Azerconnect, state institutions, and telecom providers.
- Known non-Baku leads are sparse but important: **Yevlakh City** (AzInTelecom reserve DC), **Absheron/Gobustan** and **Hajigabul/Pirsaat** (new AzInTelecom green DCs), **Goychay** (PASHA DR site), **Agdash** (Azerconnect design-certified lead), **Sumgayit** (industrial-park STDC lead), and **Nakhchivan** (planned state program / tender lead).
- Large global hyperscalers have no verified Azerbaijan public cloud region in the official AWS/Azure/GCP/OCI region lists checked for this run. Azerbaijan cloud evidence is more likely to be **sovereign cloud, Government Cloud, Gcore/AzInCloud partnership, Cloudflare edge, CDN/IX PoP, or telco-hosted cloud**.
- English-only searches miss material. Always search Azerbaijani, English, Russian, and sometimes Turkish spellings:
  - English: `data center`, `data centre`, `datacenter`, `colocation`, `cloud region`, `sovereign cloud`, `supercomputer center`, `disaster recovery site`.
  - Azerbaijani: `data mərkəzi`, `data merkezi`, `verilənlər mərkəzi`, `məlumat mərkəzi`, `hesablama mərkəzi`, `ehtiyat data mərkəzi`, `server otağı`, `bulud`, `Hökumət buludu`, `tikiləcək`, `tikintisi`, `istismara verilib`.
  - Russian: `дата-центр`, `центр обработки данных`, `ЦОД`, `облачные услуги`, `резервный дата-центр`, `Баку`, `Евлах`.

---

## 1. Industry and trade-press sources

### 1.1 International / English-language trade press

| Source | URL / query | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | `site:datacenterdynamics.com Azerbaijan data center AzInTelecom` | Best English source for EIB-funded AzInTelecom green DCs, Gcore/AzInTelecom sovereign cloud, National Depository Center migration, historic Baku launch. | B |
| Telecompaper | `site:telecompaper.com AzInTelecom Yevlakh data centre` | Useful for older AzInTelecom Yevlakh and telecom infrastructure news. | B |
| PRNewswire / Gcore official release | https://gcore.com/press-releases/azintelecom and PRNewswire mirror | Sovereign-cloud partnership with AzInTelecom; validates cloud-service lead, not necessarily a new physical site. | A/B |
| Lenovo official newsroom | https://news.lenovo.com/pressroom/press-releases/azerbaijan-first-supercomputer-on-lenovo-infrastructure/ | Official vendor evidence for AzInTelecom supercomputer center; needs address/facility pivot. | A |
| EIB / IFI press | https://www.eib.org/en/press/all/2024-527-azerbaijan-to-digitise-public-administration-with-eur43-million-loan-from-eib-global | Financing and timeline for two AzInTelecom DCs in Absheron and Hajigabul. | A |

### 1.2 Azerbaijani / regional press

| Source | URL / query | Use | Grade |
|---|---|---|---|
| AZERTAC | `site:azertag.az data center Azerbaijan`, `site:azertag.az "data mərkəzi"` | State news agency; strong for presidential visits, industrial parks, AzInTelecom, supercomputer, Sumgayit, official ceremonies. | B+/A- |
| APA | `site:en.apa.az Azerbaijan "data center" AzInTelecom`, `site:apa.az "data mərkəzi"` | High-yield for exclusive construction/timeline details, including Absheron 2027 and Hajigabul 2029 reporting. | B+ |
| Trend | `site:trend.az AzInTelecom "data centers" Absheron Hajigabul`, `site:trend.az "data mərkəzi"` | Good for state-linked ICT and operator quotes. | B |
| AzerNews | `site:azernews.az Azerbaijan data center AzInTelecom` | Often republishes official/Trend/agency material; good corroboration for EIB and Government Cloud stories. | B |
| Tech.az | `site:tech.az "data center" Azerbaijan`, `site:tech.az "data mərkəzi"` | Local tech media; useful for green DC and Nakhchivan leads. | B/C+ |
| Xeberler.az / FED.az | `site:xeberler.az "Naxçıvan" "data mərkəzi"`, `site:fed.az "Naxçıvan" "data mərkəzi"` | Useful for local tender / Nakhchivan state-program leads; verify against procurement/state documents. | B/C+ |

### 1.3 Directories and network databases

Use these as lead sources, then promote only after operator/Uptime/official confirmation:

- Datacenters.com Azerbaijan: https://www.datacenters.com/locations/azerbaijan/azerbaijan
- DataCenterMap Azerbaijan / Baku: https://www.datacentermap.com/azerbaijan/ and https://www.datacentermap.com/azerbaijan/baku/
- Data Center Catalog Azerbaijan: https://datacentercatalog.com/azerbaijan
- Cloudscene Baku: https://cloudscene.com/market/data-centers-in-azerbaijan/baku
- Inflect Baku: https://inflect.com/datacenters/emea/azerbaijan/baku
- PeeringDB facilities / IX search: https://www.peeringdb.com/
- Uptime Institute country list: https://uptimeinstitute.com/uptime-institute-awards/country/id/AZ

Directory cautions:
- Addresses can conflict. Example: Delta Telecom appears in directory results as **241 Abbas Mirza Sharifzadeh / Sharifzadeh Street** and sometimes **69 Muzaffar Hasanov**. Use official Delta pages, Uptime, and network databases to resolve.
- Marketplace pages may list resellers or service availability rather than owned facilities.
- PeeringDB proves network/interconnection presence when maintained, but not construction status, MW, or whether a facility is purpose-built.

---

## 2. Operator / project seed list

### 2.1 State cloud and government / enterprise facilities

| Operator/project | Search anchor | Notes | Grade seed |
|---|---|---|---|
| AzInTelecom Baku Main Data Center (MDC) | `AzInTelecom Baku Main Data Center Tier III 700 sqm` | Baku operating state cloud facility; Uptime Design + Constructed Facility; DCD/EIB mention Baku/Yevlakh operations. | A |
| AzInTelecom Yevlakh Reserve Data Center | `AzInTelecom Yevlakh Reserve Data Center Tier III`, `Yevlakh availability zone` | Operational reserve/availability-zone facility; Uptime and MINCOM/press corroboration. | A |
| AzInTelecom Baku New Data Protection Center | `Baku New Data Protection Center AzInTelecom Uptime` | Uptime lists Design + Constructed Facility in Baku. | A |
| AzInTelecom Absheron/Gobustan Main Data Center M1-M5 | `Absheron Main Data Center Modules M1-M5 Gobustan`, `AzInTelecom Absheron data center 2027` | EIB/AzInTelecom/APA identify new green primary DC in Absheron; Uptime shows locality Gobustan. | A |
| AzInTelecom Hajigabul/Pirsaat Reserve Data Center M1-M2 | `Hajigabul Reserve Data Center Pirsaat M1 M2`, `AzInTelecom Hajigabul data center 2029` | EIB/AzInTelecom/APA identify new green reserve DC in Hajigabul; Uptime shows locality Pirsaat. | A |
| Central Bank CBAR Main Data Center | `CBAR Main Data Center Baku Uptime` | Uptime-certified state/financial facility in Baku; not necessarily commercial colo. | A |
| State Customs Committee DGK Main Data Center | `DGK Main Data Center Baku`, `State Customs Committee data centre Tier III` | Uptime design-certified; engineering/vendor pages may corroborate implementation. | A/B |
| Nakhchivan Data Center | `Naxçıvan data mərkəzi tikiləcək`, `Nakhchivan Data Center Tier-3` | Local press/state-program lead for planned Nakhchivan state DC; verify via procurement and Nakhchivan government pages. | B |
| AzInTelecom / Lenovo Supercomputer Center | `AzInTelecom Lenovo Supercomputer Center Baku` | Official Lenovo and AZERTAC/Trend evidence; confirm whether it is inside an existing AzInTelecom facility before counting separately. | A/B |

### 2.2 Commercial / telecom / financial operators

| Operator/project | Search anchor | Notes | Grade seed |
|---|---|---|---|
| Delta Telecom Baku Main Data Center / Alatava | `Delta Telecom Baku Main Data Center DTMDC`, `datacenter.az Delta Telecom Data Center`, `Delta Telecom co-location` | Official Delta/DataCenter.az pages market colo; Uptime lists Tier III Design + Constructed Facility. | A |
| PASHA Technology Baku Main Data Center | `PASHA Technology Baku Main Data Center BMDC`, `PASHA Technology data center services` | PASHA official pages and Uptime validate Baku BMDC; DataCenterMap may provide capacity hints. | A |
| PASHA Technology Goychay Disaster Recovery Site | `PASHA Technology Goychay Disaster Recovery Site GDRS` | Uptime and PASHA service pages validate non-Baku DR site. | A |
| Azerconnect Baku Data Center | `Azerconnect Baku Data Center Tier IV`, `Azerconnect data center 2000 kW` | Uptime Design certification; contractor/engineering pages may mention 2,000 kW. Confirm operational status separately. | A/B |
| Azerconnect Agdash Data Center | `Azerconnect Agdash Data Center Tier III` | Uptime Design certification; needs operator/commissioning status validation. | A/B |
| STDC / Sumgait Technologies Data Center | `STDC Sumgayit data processing registration transmission center`, `Sumgayit Chemical Industrial Park data center` | AZERTAC presidential visit report is strong; identify operator and whether it is a commercial DC vs industrial digital center. | A/B |
| AzerTelecom / Azerfon / Nar Baku facility | `AZRT Datacenter Baku`, `Azerfon 106A Heydar Aliyev PeeringDB`, `AzerTelecom Bakı data center` | PeeringDB/directory lead; requires official operator or certification corroboration. | C/B |
| Aztelekom / Baktelecom | `Aztelekom data center Baku`, `Baktelecom data center`, `Aztelekom hosting` | State telecom providers may operate hosting/server rooms; validate with MINCOM register and official pages. | C/B |
| Azercell / Bakcell | `Azercell data center`, `Bakcell data center`, `Azerconnect data center` | Mobile operators / group infrastructure leads; many hits are network-core rather than datacenters. | C/B |

---

## 3. Query patterns

### 3.1 Broad discovery

Use `{division}` as manifest spelling and `{az}` as local spelling / alias.

```text
"{division}" "data center" Azerbaijan
"{division}" "datacenter" Azerbaijan
"{az}" "data mərkəzi"
"{az}" "verilənlər mərkəzi"
"{az}" "məlumat mərkəzi"
"{az}" "server otağı"
"{az}" "Hökumət buludu"
"{az}" "bulud xidmətləri"
"{az}" "дата-центр"
"{az}" "центр обработки данных"
"{az}" "ЦОД"
"{division}" "Tier III" "Azerbaijan"
"{division}" "Uptime Institute" "Azerbaijan"
"{division}" "colocation" Azerbaijan
"{division}" "disaster recovery site" Azerbaijan
```

### 3.2 Status / construction terms

```text
"{az}" "data mərkəzi" "tikiləcək"
"{az}" "data mərkəzi" "tikintisi"
"{az}" "data mərkəzi" "istismara verilib"
"{az}" "data mərkəzi" "açılış"
"{az}" "data mərkəzi" "layihə"
"{az}" "data mərkəzi" "tender"
"{az}" "data mərkəzi" "LEED"
"{az}" "data mərkəzi" "günəş panelləri"
"{az}" "data mərkəzi" "MW"
"{az}" "data mərkəzi" "MVA"
"{operator}" "{division}" "data center"
"{operator}" "{az}" "data mərkəzi"
```

### 3.3 Source-scoped searches

```text
site:datacenterdynamics.com Azerbaijan "data center"
site:datacenterdynamics.com AzInTelecom Baku Yevlakh
site:azertag.az "data center" Azerbaijan
site:azertag.az "data mərkəzi"
site:en.apa.az "Azerbaijan" "data center"
site:apa.az "data mərkəzi"
site:trend.az "AzInTelecom" "data centers"
site:azernews.az "Azerbaijan" "data center"
site:tech.az "data center" Azerbaijan
site:xeberler.az "data mərkəzi"
site:fed.az "data mərkəzi"
site:gcore.com "AzInTelecom" "sovereign cloud"
site:news.lenovo.com "AzInTelecom" "Supercomputer Center"
```

### 3.4 Directory / network checks

```text
site:datacenters.com Azerbaijan "{division}"
site:datacentermap.com/azerbaijan "{division}"
site:datacentercatalog.com Azerbaijan "{operator}"
site:cloudscene.com Azerbaijan Baku "data center"
site:inflect.com Azerbaijan Baku "data center"
site:peeringdb.com/fac Azerbaijan Baku
site:peeringdb.com "{operator}" "Baku"
```

Promote a directory lead only after at least one of:
- Uptime certification.
- Official operator page.
- MINCOM/ICTA entity registration + independent facility page.
- State / IFI / procurement / construction source.
- Strong trade article with named operator, facility, location, and status.

---

## 4. Per-division industry workflow

### 4.1 Tier 1 divisions

Run full operator + press + directory + official validation:
- **Baku**: search every major operator and Uptime facility name. Include district/address terms: `Alibey Huseynzadeh`, `Sharifzadeh`, `Alatava`, `Heydar Aliyev ave`, `Azadlyg Ave`, `Tbilisi Prospekti`.
- **Yevlakh City**: query `Yevlakh`, `Yevlax`, `Reserve Data Center`, `RDC`, `availability zone`, `AzInTelecom`.
- **Absheron / Gobustan**: query both region and locality; include `M1-M5`, `green technology`, `2027`, `LEED`, `EIB`.
- **Hajigabul / Pirsaat**: query both district and settlement; include `M1 M2`, `reserve`, `2029`, `EIB`, `Pirsaat`.
- **Goychay**: query `Göyçay`, `Goycay`, `PASHA GDRS`, `Disaster Recovery Site`.
- **Agdash**: query `Ağdaş`, `Agdas`, `Azerconnect Agdash`.
- **Sumgayit**: query `Sumqayıt`, `Sumqayit`, `STDC`, `Sumgait Technologies`, `Chemical Industrial Park`.
- **Nakhchivan**: query `Naxçıvan`, `Naxcivan`, `Nakhchivan data center`, `Tier-3`, `state program`, `Nakhchivan City Communication Department`.

### 4.2 Tier 2 divisions

Run local-language no-project sweeps plus smart-city / government cloud checks:
- **Ganja, Mingachevir, Shirvan, Lankaran City, Shaki City, Naftalan**: city-scale public infrastructure might produce `server otağı` or municipal data-center leads, but many are not commercial DCs.
- **Fuzuli, Shusha, Zangilan, Aghdam, Lachin, Kalbajar, Jabrayil, Gubadli, Khojaly, Khojavend, Khankendi**: search reconstruction / smart-city programs, but require physical facility evidence; broadband/base-station/smart-village references are false positives.
- **Astara, Lankaran, Salyan, Khizi, Khachmaz, Guba, Gabala, Shaki, Zagatala**: tourism/agriculture/open-data results are common false positives; look for named operators only.

### 4.3 Tier 3 divisions

For all remaining rayons, use the compact negative-control set:

```text
"{division}" "data center" Azerbaijan
"{az}" "data mərkəzi"
"{az}" "verilənlər mərkəzi"
"{az}" "server otağı"
"{az}" "Hökumət buludu"
"{az}" "дата-центр"
site:uptimeinstitute.com "{division}" Azerbaijan
site:mincom.gov.az "{division}" "data mərkəzi"
site:azertag.az "{az}" "data mərkəzi"
site:apa.az "{az}" "data mərkəzi"
site:trend.az "{az}" "data mərkəzi"
```

If these produce only schools, local executive authority IT rooms, statistics/open-data pages, or broadband coverage, record no-project with the query scope.

---

## 5. Alias table

| Manifest division | Also query | Notes |
|---|---|---|
| Baku | `Bakı`, `Baki`, `Баку` | Main market; use address and facility-name searches. |
| Absheron | `Abşeron`, `Abseron`, `Апшерон`, `Gobustan`, `Qobustan` | New AzInTelecom primary/green DC; Uptime locality may be Gobustan. |
| Gobustan | `Qobustan`, `Absheron Main Data Center` | Possible assignment conflict with Absheron project. |
| Hajigabul | `Hacıqabul`, `Haciqabul`, `Pirsaat`, `Пирсаат` | New AzInTelecom reserve/green DC; Uptime locality may be Pirsaat. |
| Yevlakh City | `Yevlax`, `Евлах`, `RDC`, `Reserve Data Center` | Separate from Yevlakh district in manifest. |
| Yevlakh | `Yevlax rayonu`, `Yevlakh District` | Avoid duplicating Yevlakh City facility. |
| Goychay | `Göyçay`, `Goycay`, `Гёйчай`, `GDRS` | PASHA DR site. |
| Agdash | `Ağdaş`, `Agdas`, `Агдаш` | Azerconnect design-certified lead. |
| Sumgayit | `Sumqayıt`, `Sumqayit`, `Сумгайыт`, `STDC`, `Sumgait` | Industrial park / STDC lead. |
| Nakhchivan | `Naxçıvan`, `Naxcivan`, `Нахчыван` | Autonomous republic planned DC; search local state-program/tender terms. |
| Ganja | `Gəncə`, `Gence`, `Гянджа` | Major city but no strong public DC lead in current sweep. |
| Lankaran City / Lankaran | `Lənkəran`, `Lenkeran`, `Ленкорань` | Split city/district carefully. |
| Shaki City / Shaki | `Şəki`, `Sheki`, `Шеки` | Split city/district carefully. |
| Khachmaz | `Xaçmaz`, `Xacmaz` | Negative-control / local ISP checks. |
| Shamakhi | `Şamaxı`, `Samaxi` | Negative-control / open-data false positives. |
| Shusha | `Şuşa`, `Susa` | Reconstruction/smart-city false positives likely. |
| Zangilan | `Zəngilan`, `Zengilan` | Smart village false positives likely. |
| Khankendi | `Xankəndi`, `Stepanakert` | Search both names; require post-2023 physical facility evidence. |

---

## 6. Facility extraction and grading rules

For every candidate, extract:
- Facility name exactly as source states it.
- Operator / client / developer and legal entity.
- Division plus locality/address, preserving source wording.
- Status: operational, construction, planned, design-certified only, unknown.
- Capacity: MW / kW / MVA / racks / sqm only if explicitly stated; record units.
- Source chain: operator/official/certification first, then trade/directories.
- Whether it is commercial colo/cloud, enterprise/government DC, DR site, edge PoP, supercomputer/HPC center, or server room.

Promotion rules:
- **A**: Uptime constructed-facility certification, official operator page naming the facility, IFI/state financing naming location/status, presidential/state agency source, or regulator/permit record.
- **B**: DCD/APA/AZERTAC/Trend/AzerNews/vendor case study with named operator and location, especially if quoting operator/official.
- **C**: Datacenters.com/DataCenterMap/Cloudscene/Inflect/PeeringDB/market reports without corroboration.

False positives:
- Generic open-data / statistics portals.
- Broadband expansion under `Online Azerbaijan`.
- Smart village / smart city / telecom restoration in liberated territories without a physical compute facility.
- CDN/Cloudflare/Gcore edge service claims without facility host details.
- Bank/government `server otağı` modernization that is not described as a data center.
- The country code `AZ` in AWS/Azure contexts; it usually means Availability Zone, not Azerbaijan.
