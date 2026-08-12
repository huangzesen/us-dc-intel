# MD Explorer Industry - Moldova Datacenter Enumeration via Operators, IXPs, Trade Press, Cloud/Colo Leads, and Regional Query Patterns

Date: 2026-08-12. Scope: Republic of Moldova (MD). Focus angle: industry/operator/trade-source methodology for identifying datacenter facilities and projects, then validating with official sources. Reliability grades: **A** = official/primary/operator-owned current page, **B** = strong secondary/trade/interconnection source, **C** = weak aggregate, marketplace, SEO page, or unverified lead.

---

## 0. Industry frame

- Moldova is a small Chisinau-centric datacenter market. Public datacenter directories and operator pages point overwhelmingly to **Chisinau**; district searches outside the capital usually return no physical facility evidence.
- Best practical workflow: **operator/directory/IXP lead -> operator-owned page -> PeeringDB/IXP/facility confirmation -> ARCOM legal-entity check -> Chisinau/local permit and environmental searches -> grid/utility checks**.
- Separate commercial colo/hosting, government cloud, telecom network rooms, edge/CDN nodes, and crypto/GPU hosting. Moldova has several hosting/colo claims, but not all are datacenter-grade facilities.
- Major international hyperscale cloud providers do not publish Moldova cloud regions in official AWS/Azure/GCP/OCI lists during this pass. Local "cloud" offerings usually mean VPS/IaaS in Moldovan colo or regional resale.
- The key planned-project theme is sovereign/public-sector infrastructure: STISC/MCloud and a future national datacenter. Treat this separately from commercial colo.

---

## 1. Industry, directories, and trade sources

### 1.1 Facility directories and marketplaces

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Map Moldova | https://www.datacentermap.com/moldova/ and Chisinau https://www.datacentermap.com/moldova/chisinau/ | Best quick seed list for public Chisinau facilities. Lists 6 Moldova datacenters in 1 market and names Data City Moldtelecom, Trabia, MoldData Cloud, AlexHost, IP HOST, AvenaCloud. Verify against operator pages. | C+/B- |
| Datacenters.com Moldova | https://www.datacenters.com/locations/moldova and Chisinau https://www.datacenters.com/locations/moldova/chisinau/chisinau | Seed list for providers including Trabia Network, Wintek, Moldtelecom, Orange Moldova, StarNet, MoldData Cloud. Verify status/address. | C+ |
| Cloudscene Chisinau | https://cloudscene.com/market/data-centers-in-moldova/chisinau | Market overview for colo/cloud/network ecosystem. Useful to find providers but not source-of-record. | C+ |
| Inflect Moldova/Chisinau | https://inflect.com/datacenters/emea/moldova and https://inflect.com/datacenters/emea/moldova/chisinau | Useful for facility/building leads and network presence, including Cogent/Mezon/Trabia leads. Verify with operator/PeeringDB. | C+ |
| ColocationM Moldova | https://www.colocationm.com/moldova/chisinau | Marketplace pages with address/power claims for AvenaCloud, IP HOST, AlexHost, MoldData, etc. Treat MW/power as B-/C+ unless matched to operator or permit data. | C+ |
| DC Hub | Example Moldtelecom Data City: https://dchub.cloud/facilities/moldtelecom-sa-data-city-moldtelecom-7325073a | Useful for coordinates/power/status cross-checks. Verify against operator pages. | C+ |

Directory evidence should start a lead, not close it. In Moldova, directories sometimes list facilities that are actually hosting brands, telecom PoPs, or reseller locations.

### 1.2 Interconnection and IX sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| PeeringDB | https://www.peeringdb.com/ | Facility/network/IX validation. Data City - Moldtelecom facility page: https://www.peeringdb.com/fac/15521 ; MD-IX page: https://www.peeringdb.com/ix/392 ; Moldtelecom org/network pages. | B |
| Packet Clearing House (PCH) | MD-IX page: https://www.pch.net/ixp/details/1237 | Confirms Moldova Internet Exchange / MD-IX in Chisinau, managed by Moldtelecom, active status. | B |
| Internet Society Pulse IXP Tracker | https://pulse.internetsociety.org/en/ixp-tracker/ixp/222/ | Member and port-capacity context for MD-IX; useful for operator discovery. | B/C |
| Trabia KIVIX | https://www.trabia.com/kivix.html | Operator-owned page for KIVIX, described as Chisinau's second-largest Internet Exchange in Moldova. Useful for Trabia ecosystem and connected networks. | A/B |
| Euro-IX IXPDB | https://ixpdb.euro-ix.net/en/explore/ixp/278/ | Supplemental MD-IX metadata; may be stale. | C+ |

Interconnection records prove active network presence, not necessarily datacenter ownership. Use them to confirm that a site is a live connectivity facility and to identify tenants/peers.

### 1.3 Trade press and market context

Moldova has limited datacenter-specific trade coverage. Use local business/technology press primarily for planned public-sector projects and investment context.

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Government of Moldova | https://gov.md/en/press-releases/pm-meets-ambassador-latvia-moldova | Official confirmation that Latvia supports STISC with methodological assistance for a future national datacenter. | A |
| STISC activity/procurement reports | https://stisc.gov.md/ro/achizitii and 2025 report PDF | Best source for national datacenter feasibility/site-search progress, MCloud modernization, and government IT infrastructure procurement. | A |
| eGov/MCloud | https://www.egov.md/en/content/mcloud-platform | Official government cloud platform context; not necessarily a new standalone facility. | A |
| Moldova1 | https://moldova1.md/p/66418 | Public broadcaster article echoing Latvia support for future national datacenter; useful secondary lead. | B |
| IPN | query `site:ipn.md Moldova national data center STISC Latvia` | Secondary reporting on digitization/cybersecurity cooperation and national datacenter objectives. | B |
| Logos Press | https://logos-pres.md/en/article/the-digital-economy-needs-data-centers/ | Local business press commentary; useful for market narrative, not facility verification. | C+/B- |
| UNECE IT sector review | https://unece.org/sites/default/files/2025-03/Sector%20Review%20IT%20Moldova%20Report%202023.pdf | Good public-sector digital economy/MCloud context. Not a facility registry. | B |
| SeeNews / regional business press | query `site:seenews.com Moldova data center Chisinau` | Good for construction/economy signals, but datacenter coverage appears sparse. | B/C |

---

## 2. Operator and facility seed list

Operator-owned pages are **A for marketed service/facility existence** when they directly describe a datacenter/colo service. Exact capacity still needs spec sheet, permit, or strong facility database corroboration.

### 2.1 Chisinau commercial and telecom facilities

- **Moldtelecom Data City** - official page: https://www.moldtelecom.md/ro/business/data-centru/ . The page markets Data City as a Tier 3-standard datacenter with colocation/hosting for companies. Use PeeringDB Data City page https://www.peeringdb.com/fac/15521 and DC Hub for address/power cross-check. **Grade A/B**.
- **MoldData Cloud / Host.md** - official page: https://host.md/en/?pag=datacenter . Markets MoldData Cloud as a Moldovan datacenter offering colocation and dedicated servers. **Grade A/B**.
- **Trabia Network** - main site https://www.trabia.com/ and technology/KIVIX pages including https://www.trabia.com/kivix.html . DataCenterMap places Trabia at Vlaicu Pircalab St 52/2012. **Grade A for operator existence, B/C for directory address/capacity**.
- **AlexHost** - colocation page: https://alexhost.com/colocation-in-moldova/ . Describes Moldovan colocation with autonomous power, cooling/ventilation, video surveillance, and high-speed channels. Cross-check with marketplace address/power. **Grade B**.
- **IP HOST / Inovare-Prim** - directory and IXP evidence; search official IP HOST/Inovare-Prim pages and ARCOM/PeeringDB. Use DataCenterMap/ColocationM only as leads for Uzinelor Street and MW claims. **Grade B/C until operator page found**.
- **AvenaCloud / Infotech-Grup SRL** - marketplace/directory lead for Chisinau facility at Muncesti 364. Search operator official pages and ARCOM. **Grade C+/B- until operator facility page found**.
- **Cogent Moldova / Chisinau CNDC** - Cogent official location search: https://www.cogentco.com/en/component/content/article?action=search&city=&continent=&country=Moldova&id=40&metro=&site_type=&state= . Cross-check Inflect/PeeringDB for Decebal/Trabia locations. **Grade B**.
- **Orange Moldova** - appears in Chisinau directory/provider lists and MD-IX ecosystem. Search Orange Moldova/Orange Business official pages for local datacenter or colocation claims; do not assume a Moldovan Orange datacenter from generic Orange Business global pages. **Grade B/C until local official page found**.
- **StarNet Moldova** - appears in Datacenters.com/IXP ecosystem. Search official StarNet business/cloud pages and ARCOM. **Grade B/C until local facility page found**.
- **Mezon Business Park DC** - appears in Inflect/DataCenterPlatform-style listings. Treat as a weak lead until operator-owned documentation or interconnection evidence is found. **Grade C**.

Chisinau operator query bundle:

```text
"Moldtelecom" "Data City" "centru de date"
"Data City Moldtelecom" "Alba Iulia 77"
"MoldData Cloud" "Armeneasca 37/1"
"Host.md" "MoldData Cloud" "colocation"
"Trabia" "Vlaicu Pircalab" "data center"
"Trabia" "KIVIX" "Chisinau"
"AlexHost" "colocation in Moldova"
"IP HOST" "Uzinelor" "data center" Moldova
"Inovare-Prim" "data center" Chisinau
"AvenaCloud" "Muncesti 364"
"Infotech-Grup" "AvenaCloud" "data center"
"Cogent" "Chisinau" "CNDC"
"StarNet" "data center" Chisinau
"Orange Moldova" "data center" OR "colocation"
```

### 2.2 Government and public-sector infrastructure

- **MCloud** - official eGov page: https://www.egov.md/en/content/mcloud-platform . This is a government cloud/consolidation platform; enumerate as public-sector cloud infrastructure only when physical facility evidence is present.
- **STISC / future national datacenter** - STISC procurement/activity pages and the 2025 activity report are the main source. The report mentions a `Centrul de Date TIER III, AI-Ready`, feasibility-study procurement, and land-identification travel to Ungheni, Falesti, and Balti. Store as planned/site-search, not a selected facility.
- **Moldova HiTech Park / Stauceni** - public coverage ties Moldova HiTech Park to Stauceni and future advanced-technology development. Only count a national datacenter there if official STISC/government or permit records name the site.

Public-sector queries:

```text
"MCloud" "centru de date" Moldova
"MCloud" "data center" Moldova
site:egov.md "MCloud" "data centers"
site:stisc.gov.md "Modernizarea infrastructurii centrelor de date"
site:stisc.gov.md "Centrul de Date TIER III"
site:stisc.gov.md "AI-Ready"
"national data center" Moldova STISC Latvia
"centru national de date" Moldova STISC
"Moldova HiTech Park" "centru de date"
"Stauceni" "centru de date"
```

### 2.3 Transnistria / left-bank hosting and mining leads

Left-bank sources often have weaker official validation and may be outside normal Moldova regulatory visibility.

- **Imperial Hosting / Tiraspol** - operator-style pages and hosting/mining directory evidence indicate Tiraspol activity, but public permit/capacity evidence is weak. Treat as **C/B-** depending on source.
- Search Tiraspol, Bender, Rybnitsa/Ribnita, and Transnistria terms in Russian and English. Distinguish real physical hosting/colo/mining sites from VPS company addresses.

Templates:

```text
"Imperial Hosting" "Tiraspol"
"Tiraspol" "data center" Moldova
"Tiraspol" "colocation"
"Тирасполь" "дата центр"
"Тирасполь" "ЦОД"
"Приднестровье" "майнинг" "дата центр"
"Бендеры" "дата центр"
"Рыбница" "хостинг" "сервер"
```

---

## 3. Cloud, CDN, and edge-provider handling

Use official hyperscale pages to verify absence/presence:

```text
site:docs.aws.amazon.com "Moldova" "Local Zone"
site:aws.amazon.com/wavelength "Moldova"
site:learn.microsoft.com "Azure regions list" "Moldova"
site:cloud.google.com/about/locations "Moldova"
site:oracle.com/cloud/public-cloud-regions "Moldova"
```

Likely interpretation:

- No official AWS/Azure/GCP/OCI public region in Moldova during this pass.
- CDN/edge nodes may appear through MD-IX/KIVIX, Cloudflare, Bunny CDN, Google cache, or other networks. Record these as `edge_node` or `network_pop`, not as full datacenters, unless a facility address and operator relationship are shown.
- Chisinau local VPS providers may market "cloud" but usually operate from local colo/hosting facilities. Use their legal entity, facility address, and power/cooling evidence before adding a datacenter row.

---

## 4. Per-division industry query patterns

### 4.1 Chisinau

Chisinau gets a full operator + official validation pass.

```text
"Chisinau" "data center" "Moldtelecom" OR "Trabia" OR "MoldData" OR "AlexHost"
"Chisinau" "colocation" Moldova
"Chișinău" "centru de date"
"Chișinău" "colocare servere"
"Кишинев" "дата центр"
"Кишинев" "колокация"
site:peeringdb.com Chisinau Moldova facility
site:datacentermap.com/moldova/chisinau "Data Center"
site:inflect.com/building Chisinau Moldova datacenter
```

Validation pivots:

```text
site:chisinau.md "{operator}" "autorizatie de construire"
site:am.gov.md "{operator}" "Chisinau"
site:anrceti.md "{operator}"
site:moldelectrica.md "{operator}" "racordare"
```

### 4.2 Balti

Balti is important because of STISC national-datacenter land-identification travel, not because of confirmed commercial colo.

```text
"Balti" "data center" Moldova
"Bălți" "centru de date"
"Бельцы" "дата центр"
"Centrul de Date TIER III" "Bălți"
site:balti.md "centru de date" OR "servere"
site:balti.md "autorizatie de construire" "servere"
site:stisc.gov.md "Bălți" "Centrul de Date"
site:mtender.gov.md "Bălți" "servere" OR "centru de date"
```

### 4.3 Ungheni and Falesti

These are STISC site-search watchlist districts. Treat any "smart city data center" or data-platform language carefully unless it names physical infrastructure.

```text
"Ungheni" "centru de date" Moldova
"Ungheni" "data center" Moldova
"Falesti" "centru de date" OR "Fălești" "centru de date"
"Centrul de Date TIER III" "Ungheni"
"Centrul de Date TIER III" "Fălești"
site:ungheni.md "centru de date" OR "servere"
site:falesti.md "centru de date" OR "servere"
site:stisc.gov.md "Ungheni" "Fălești" "Centrul de Date"
site:mtender.gov.md "Ungheni" "studiu de fezabilitate"
```

### 4.4 Chisinau spillover: Ialoveni, Straseni, Anenii Noi, Criuleni

These districts are plausible for future suburban Chisinau facilities because of land, logistics, and power corridors, but current public evidence is weak.

```text
"Ialoveni" "centru de date" OR "data center"
"Straseni" "centru de date" OR "data center"
"Anenii Noi" "centru de date" OR "data center"
"Criuleni" "centru de date" OR "data center"
"Stauceni" "centru de date" "HiTech Park"
"Moldova HiTech Park" "Stauceni" "data center"
site:{local-domain} "autorizatie de construire" "centru de date"
site:{local-domain} "statie de transformare" "servere"
```

### 4.5 Regional development/free-zone districts: Cahul, Gagauzia, Taraclia, Orhei

Search for digital-infrastructure or industrial-park announcements, but expect mostly no-project results unless an operator is named.

```text
"Cahul" "centru de date" Moldova
"Comrat" "centru de date" OR "data center"
"Gagauzia" "data center" Moldova
"Taraclia" "centru de date"
"Orhei" "centru de date" Moldova
"free economic zone" Moldova "data center"
"zona economica libera" "centru de date"
site:mtender.gov.md "Cahul" "servere"
site:mtender.gov.md "Gagauzia" "servere"
```

### 4.6 North and small districts

For Briceni, Donduseni, Drochia, Edinet, Glodeni, Ocnita, Riscani, Singerei, Soroca, Soldanesti, Telenesti, Floresti, Rezina, Calarasi, Nisporeni, Hincesti, Leova, Cimislia, Basarabeasca, Cantemir, Causeni, Stefan Voda, Dubasari, and similar districts, use fast negative screening:

```text
"{division}" "centru de date"
"{division}" "data center" Moldova
"{division}" "colocare servere"
"{division}" "camera servere"
"{division}" "autorizatie de construire" "servere"
"{division}" "statie de transformare" "servere"
site:mtender.gov.md "{division}" "servere"
site:mtender.gov.md "{division}" "cloud"
site:{local-domain} "centru de date"
```

Escalate only if the result names a physical facility, operator, large power connection, industrial-park site, or government project. Otherwise record a no-project result with Chisinau-only national directory evidence.

### 4.7 Bender and Stinga Nistrului

Use Russian/English and separate confidence grading:

```text
"Bender" "data center" Moldova
"Bender" "colocation" Moldova
"Бендеры" "дата центр"
"Тирасполь" "дата центр"
"Приднестровье" "дата центр"
"Transnistria" "data center"
"Rybnitsa" "hosting" "data center"
```

For any left-bank claim, capture source jurisdiction, operator address, physical evidence, and whether the source is a hosting offer, mining offer, or telecom facility.

---

## 5. Moldova-specific deduplication rules

- Moldtelecom may appear as Data City, MD-IX manager, COLO-54, and telecom-provider pages. Keep facility records distinct only when addresses or PeeringDB facility IDs differ.
- Directory pages may list "MoldData Cloud / S.E. MoldData", "Host.md", and "MoldData" as separate provider labels. Treat as same ecosystem unless a second facility is proven.
- `Chisinau CNDC`, Cogent Chisinau, Trabia Data Center, and carrier PoPs may overlap. Do not double count a carrier PoP as a separate datacenter without facility/address evidence.
- Orange Moldova and StarNet may have network rooms or service nodes; count only if a datacenter/colo service page, facility record, or permit exists.
- "MCloud" should not be merged automatically with STISC's future national datacenter. One is an operational government cloud platform; the other is a planned/new datacenter workstream unless documents say otherwise.

---

## 6. Recommended enumeration order

1. **Chisinau operator census**: Moldtelecom Data City, MoldData/Host.md, Trabia, AlexHost, IP HOST, AvenaCloud, Cogent, Orange, StarNet, Mezon, MivoCloud and any PeeringDB facilities.
2. **Interconnection pass**: MD-IX, KIVIX, PeeringDB networks/facilities, PCH, Internet Society Pulse.
3. **Official validation**: ARCOM provider register, Chisinau/DGAURF permits, Environmental Agency notices, Moldelectrica/ANRE/Premier Energy power evidence.
4. **Government cloud pass**: MCloud, STISC reports/procurements, future national datacenter, Moldova HiTech Park/Stauceni, Balti/Ungheni/Falesti site-search traces.
5. **Regional negative screens**: run local-language district templates; escalate only if physical or official evidence appears.
6. **Transnistria pass**: Russian-language hosting/colo/mining searches with cautious grading.

Minimum fields to capture for each candidate:

```text
facility_name
operator_brand
legal_entity
division
city/locality
address_or_cadastral_reference
status
evidence_grade
source_urls
operator_source
interconnection_source
permit_or_environment_source
capacity_mw_or_power_claim
notes_on_duplicate_risk
```
