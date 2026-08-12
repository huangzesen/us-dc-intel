# KH Explorer Official - Cambodia Datacenter Enumeration Methodology

Date: 2026-08-12. Country: **KH Cambodia**. Scope: official / regulatory / cloud pipeline for enumerating Cambodian datacenter projects across Phnom Penh and the 24 provinces. Focus: MPTC datacenter licensing, TRC telecom-operator records, MLMUPC construction permits, CDC/QIP/SEZ investment evidence, EAC/EDC power evidence, official cloud-region pages, official colo/operator pages, Uptime certification, and trade-press discovery.

Reliability grades:
- **A** = primary / legally accountable source: MPTC datacenter licensing notice or issued license evidence, TRC operator list/statistics, MLMUPC or sub-national construction permit / certificate of occupancy, CDC/QIP or SEZ record, EAC/EDC power record, Ministry of Environment EIA record, official cloud-region page, official operator page, Uptime Institute certificate, listed-company filing.
- **B** = strong secondary: Data Center Dynamics, Khmer Times, Cambodia Investment Review, Construction & Property Cambodia, Knight Frank / CBRE / reputable broker reports, law-firm notes that cite Cambodian regulations, vendor / contractor project pages.
- **C** = weak lead: Baxtel, DataCenterMap, DataCenters.com, PeeringDB, job ads, social posts, market-size reports, SEO directories. Use these for discovery only, then re-verify.

---

## 0. Cambodia-Specific Structure Facts

- Cambodia does **not** appear to have a complete public facility-level datacenter registry. Build the census by joining **MPTC datacenter licensing + TRC telecom operators + construction permits + CDC investment evidence + power/utility evidence + operator/certification pages + trade press**.
- MPTC issued a public notice on **2025-06-09** requiring companies that establish and operate customer-facing datacenters to apply for a license from the Ministry of Post and Telecommunications. Covered services include storage, web/email hosting, location/server rental, managed customer equipment, security, and cloud services including IaaS/PaaS/SaaS. Primary page: https://mptc.gov.kh/2025/06/%E1%9E%9F%E1%9F%81%E1%9E%85%E1%9E%80%E1%9F%92%E1%9E%8F%E1%9E%B8%E1%9E%87%E1%9E%BC%E1%9E%93%E1%9E%8A%E1%9F%86%E1%9E%8E%E1%9E%B9%E1%9E%84-%E1%9E%9F%E1%9F%92%E1%9E%8F%E1%9E%B8%E1%9E%96%E1%9E%B8-68/ and English ODC mirror: https://opendevelopmentcambodia.net/en/announcements/press-release-on-the-application-for-a-license-to-establish-and-operate-a-data-center/
- TRC publishes an active telecommunications-operator list. The live page showed **51 operators**, last updated **2025-08-11**, with downloadable monthly/yearly operator PDFs: https://www.trc.gov.kh/en/resources/active-operator/. TRC statistics also summarize telecom-license categories and internet subscriptions: https://trc.gov.kh/en/resources/telecom-statistics/.
- Planning/building approval is not centralized in a public searchable national planning portal. Treat **MLMUPC** as the national construction authority and route project checks through its online public construction service / One Window Service and the relevant municipal/provincial/district/khan authority. Main MLMUPC site: https://mlmupc.gov.kh/.
- Cambodia's known carrier-neutral/commercial datacenter market is heavily concentrated in **Phnom Penh**, with likely spillover into **Kandal** around Techo International Airport, Phnom Penh Special Economic Zone, National Road corridors, and suburban power/fiber routes. Siem Reap, Battambang, Sihanoukville/Preah Sihanouk, Banteay Meanchey/Poipet, and Svay Rieng/Bavet are secondary checks driven by telco, SEZ, casino/industrial, airport, tourism, border-gateway, or disaster-recovery use cases.
- Search Khmer and English. Core Khmer terms: `មជ្ឈមណ្ឌលទិន្នន័យ` (data center), `អាជ្ញាបណ្ណមជ្ឈមណ្ឌលទិន្នន័យ` (datacenter license), `សេវាក្លោដ` (cloud service), `មជ្ឈមណ្ឌលជាតិទិន្នន័យ` (national data center), `លិខិតអនុញ្ញាតសាងសង់` / `អាជ្ញាបណ្ណសាងសង់` (construction permit), `សំណង់` (construction), `អគ្គិសនី` (electricity), `ស្ថានីយអគ្គិសនី` (substation).

---

## 1. Core Search Terms

Use both American and British spellings plus operator, Khmer, and district/province names.

```text
"Cambodia" "data center" "{operator_or_project}"
"Cambodia" "data centre" "{operator_or_project}"
"Phnom Penh" "data center" "MW" OR "racks" OR "Tier III"
"Kandal" "data center" "Techo International Airport"
"Cambodia" "cloud" "data center license"
"Cambodia" "National Data Center" "MPTC"
"Cambodia" "data center" "construction permit"
"Cambodia" "data center" "QIP" OR "CDC" OR "SEZ"
"Cambodia" "data center" "Electricite du Cambodge" OR "EDC"
"Cambodia" "data center" "Uptime Institute"
```

Khmer queries:

```text
"មជ្ឈមណ្ឌលទិន្នន័យ" "កម្ពុជា"
"មជ្ឈមណ្ឌលទិន្នន័យ" "ភ្នំពេញ"
"មជ្ឈមណ្ឌលទិន្នន័យ" "ខេត្តកណ្តាល"
"អាជ្ញាបណ្ណ" "មជ្ឈមណ្ឌលទិន្នន័យ"
"លិខិតអនុញ្ញាតសាងសង់" "មជ្ឈមណ្ឌលទិន្នន័យ"
"សំណង់" "មជ្ឈមណ្ឌលទិន្នន័យ"
"អគ្គិសនី" "មជ្ឈមណ្ឌលទិន្នន័យ"
"មជ្ឈមណ្ឌលជាតិទិន្នន័យ" "ក្រសួងប្រៃសណីយ៍"
```

Search engines and tactics:
- Google/Bing with `site:` work better than most local site search boxes.
- Use Khmer exact-match queries for government pages; English for operator pages, trade press, and foreign investor filings.
- Search Facebook only as a last-mile discovery channel for provincial administrations and local operators; grade social-only evidence **C** unless it is an official ministry/province page and includes a document image.

---

## 2. Grade A Regulatory / Licensing Sources

### 2.1 MPTC - Datacenter Operating License

Primary sources:
- MPTC home / news: https://mptc.gov.kh/en/
- 2025 Khmer datacenter license notice: https://mptc.gov.kh/2025/06/%E1%9E%9F%E1%9F%81%E1%9E%85%E1%9E%80%E1%9F%92%E1%9E%8F%E1%9E%B8%E1%9E%87%E1%9E%BC%E1%9E%93%E1%9E%8A%E1%9F%86%E1%9E%8E%E1%9E%B9%E1%9E%84-%E1%9E%9F%E1%9F%92%E1%9E%8F%E1%9E%B8%E1%9E%96%E1%9E%B8-68/
- ODC English mirror of the same notice: https://opendevelopmentcambodia.net/en/announcements/press-release-on-the-application-for-a-license-to-establish-and-operate-a-data-center/
- Cambodia Digital Government Policy 2022-2035: https://mptc.gov.kh/en/2022/04/cambodia-digital-government-policy-2022-2035/

Use MPTC as the first regulatory filter for any customer-facing colocation, hosting, managed infrastructure, or cloud facility. The 2025 notice is a rule/existence anchor, not a license register. For every operator lead, search MPTC for the legal name and Khmer spelling plus `អាជ្ញាបណ្ណ`.

Query templates:

```text
site:mptc.gov.kh "data center" "license"
site:mptc.gov.kh "Data Center" "Cambodia"
site:mptc.gov.kh "អាជ្ញាបណ្ណ" "មជ្ឈមណ្ឌលទិន្នន័យ"
site:mptc.gov.kh "{operator}" "អាជ្ញាបណ្ណ"
site:mptc.gov.kh "{operator}" "data center"
site:mptc.gov.kh "National Data Center"
site:mptc.gov.kh "មជ្ឈមណ្ឌលជាតិទិន្នន័យ"
```

Grade: **A** for licensing requirement, issued license evidence, national-policy statements, and MPTC-owned government datacenter projects. Caveat: an MPTC notice alone does not prove a facility exists; it proves a licensing requirement and helps identify non-compliant operators to verify.

### 2.2 TRC - Telecom Operator Census

Primary sources:
- TRC active operators: https://www.trc.gov.kh/en/resources/active-operator/
- TRC telecom statistics: https://trc.gov.kh/en/resources/telecom-statistics/
- TRC laws/regulations / prakas: https://trc.gov.kh/en/laws-and-regulations/prakas/2/

TRC is a company-level telecom-operator census, not a datacenter facility register. Download the newest operator PDF and search for known datacenter / ISP / fiber operators. The web page and statistics expose operator totals and license categories; individual operator rows may need PDF extraction.

High-value operator names to seed from TRC/operator/trade evidence:
- ByteDC / Bytedc (KH) Co., Ltd / Urban Data Center Co., Ltd
- Chaktomuk Data Center Co., Ltd
- Daun Penh Data Center / DPDC
- SINET / S.I Group Co., Ltd
- Ezecom / Telcotech
- Seatel / South East Asia Telecom
- MekongNet / Angkor Data Communication Group
- NeocomISP / NTC
- Global Cloud Xchange / GCX, if a local facility or POP is claimed
- Angkor Data Infrastructure Co., Ltd, visible in the TRC active-operator search snippet

Query templates:

```text
site:trc.gov.kh "{operator}" "Telecommunications Operators List"
site:trc.gov.kh "Operators List" "Data"
site:trc.gov.kh "ISP" "Cambodia" "{operator}"
site:trc.gov.kh "Value Added Network" "{operator}"
site:trc.gov.kh "អាជ្ញាបណ្ណ" "{operator}"
"Telecommunications Operators List" "Cambodia" "data center"
```

Grade: **A** for legal operator/license presence. Caveat: TRC licensing does not give rack count, MW, construction status, or exact facility address; join to operator pages, MPTC license, Uptime, and permit/power evidence.

---

## 3. Planning, Construction, EIA, and Investment Evidence

### 3.1 MLMUPC / Sub-National Construction Permits

Primary sources:
- Ministry of Land Management, Urban Planning and Construction: https://mlmupc.gov.kh/
- MLMUPC public services include electronic construction services / `សេវាសំណង់តាមប្រព័ន្ធអេឡិចត្រូនិក`.
- Construction Law / Prakas / Sub-Decree mirrors are often easier to search through ODC, EuroCham, DFDL, BNG Legal, and Construction & Property Cambodia; use them only to understand routing, then look for primary issuing authority evidence.

Method:
1. For every lead, identify city/khan/district/commune and land setting. Phnom Penh leads route to the Phnom Penh Capital Administration and the relevant khan, but large/high-rise/special projects may sit with MLMUPC.
2. Search MLMUPC, Phnom Penh Capital Administration, provincial administration, district/khan, and One Window Service (`OWSO`) terms by legal owner, project name, land lot, street, and Khmer project terms.
3. Extract construction permit, occupancy certificate, building height/floor count, land title/lot, applicant, address, authority, and date.
4. Treat consultant/legal summaries as **B** unless they reproduce permit numbers or official forms.

Construction query templates:

```text
site:mlmupc.gov.kh "{operator}" "data center"
site:mlmupc.gov.kh "មជ្ឈមណ្ឌលទិន្នន័យ"
site:mlmupc.gov.kh "សេវាសំណង់" "មជ្ឈមណ្ឌលទិន្នន័យ"
site:phnompenh.gov.kh "data center" OR "មជ្ឈមណ្ឌលទិន្នន័យ"
site:phnompenh.gov.kh "{operator}" "សំណង់"
"{operator}" "construction permit" "Cambodia"
"{operator}" "លិខិតអនុញ្ញាតសាងសង់"
"{district_or_khan}" "មជ្ឈមណ្ឌលទិន្នន័យ" "សំណង់"
```

Grade: **A** for MLMUPC/province/municipal/district/khan permit records. Caveat: public online search coverage is incomplete; absence is not evidence that a project lacks permits.

### 3.2 CDC / QIP / SEZ Investment Pipeline

Primary sources:
- Council for the Development of Cambodia: https://cdc.gov.kh/
- CDC incentives page: https://cdc.gov.kh/incentives-and-schemes/
- CDC SEZ Smart Search: https://cdc.gov.kh/sez-smart-search/
- CDC laws/regulations and investor services pages: https://cdc.gov.kh/laws-and-regulations/ and https://cdc.gov.kh/investment-services/

Use CDC where a datacenter is foreign-invested, import-heavy, high-tech, digital-industry, SEZ-based, or tax-incentive seeking. CDC states that digital industries are among investment-incentive sectors, QIPs can receive tax/customs incentives, and SEZs provide on-site one-stop services and utilities.

Query templates:

```text
site:cdc.gov.kh "data center"
site:cdc.gov.kh "data centre"
site:cdc.gov.kh "digital industries" "QIP"
site:cdc.gov.kh "{operator}" "QIP"
site:cdc.gov.kh "{province}" "data center"
site:cdc.gov.kh "Special Economic Zone" "data center"
"Cambodia" "QIP" "data center" "{operator}"
"Phnom Penh SEZ" "data center"
"Kandal" "SEZ" "data center"
"Bavet" "data center" "SEZ"
"Sihanoukville SEZ" "data center"
```

Grade: **A** for CDC/QIP/SEZ records naming the project/company; **B** for investment-promotion articles that say CDC facilitated a project without listing a registration certificate or QIP detail.

### 3.3 Ministry of Environment / EIA Trail

Primary sources:
- Ministry of Environment: https://www.moe.gov.kh/
- NCSD/MoE environment and climate pages: https://ncsd.moe.gov.kh/
- ODC EIA topic summary: https://opendevelopmentcambodia.net/en/topics/environmental-impact-assessments/
- ODC EIA dataset: https://opendevelopmentcambodia.net/dataset/?id=environmental-impacts-assessments-
- EIA legal reference, Sub-Decree 72 mirror: https://lpr.adb.org/sites/default/files/resource/%5Bnid%5D/sub-decree-72-on-eia-process-1999.pdf

Datacenters may not appear under a clean `data center` category. Search EIA records by company, landowner, SEZ/industrial park, backup generator, fuel storage, cooling/water, transmission line, and roadworks. ODC notes that EIA documentation is incomplete but provides a useful public-data supplement.

Query templates:

```text
site:moe.gov.kh "data center" Cambodia
site:moe.gov.kh "មជ្ឈមណ្ឌលទិន្នន័យ"
site:opendevelopmentcambodia.net "data center" "EIA" Cambodia
site:opendevelopmentcambodia.net "មជ្ឈមណ្ឌលទិន្នន័យ" "EIA"
"{operator}" "EIA" "Cambodia"
"{SEZ_or_airport_or_campus}" "environmental impact assessment" "Cambodia"
"data center" "generator" "Cambodia" "EIA"
```

Grade: **A** for MoE approval or EIA report; **B** for ODC/legal mirrors if they reproduce official documents; **C** for general environmental commentary.

---

## 4. Energy and Utility Evidence

Primary sources:
- Electricite du Cambodge / EDC: https://www.edc.com.kh/
- Electricity Authority of Cambodia / EAC: https://eac.gov.kh/
- EAC annual power-sector report mirror for 2024: https://data.opendevelopmentcambodia.net//dataset/report-on-power-sector-of-the-kingdom-of-cambodia-for-year-2024
- Ministry of Mines and Energy: https://www.mme.gov.kh/
- U.S. International Trade Administration energy guide, useful secondary context: https://www.trade.gov/country-commercial-guides/cambodia-energy-power-generation-equipment

Use power evidence to validate large projects and to prioritize likely provinces. EAC annual reports provide licensee/service-area context, while EDC/MME procurement and project pages reveal grid/transmission/substation upgrades. Large datacenters should leave one or more of these traces: high-voltage connection, substation expansion, dedicated feeder, transformer import, power-purchase/industrial tariff issue, backup-generator permit/EIA, or SEZ utility upgrade.

Query templates:

```text
site:edc.com.kh "data center" OR "data centre"
site:edc.com.kh "មជ្ឈមណ្ឌលទិន្នន័យ"
site:edc.com.kh "{operator}" "Phnom Penh"
site:eac.gov.kh "{operator}" "license"
site:eac.gov.kh "Annual Report" "Kandal" "Distribution"
site:eac.gov.kh "Special Purpose Transmission" "Cambodia"
site:mme.gov.kh "data center" "electricity"
"{operator}" "Electricite du Cambodge" "data center"
"{project}" "substation" "Cambodia"
"{province}" "data center" "MW" "Cambodia"
```

Grade: **A** when EDC/EAC/MME names the customer, grid project, service area, licensee, tariff, or interconnection. **B** when an operator or trade source claims power capacity without utility confirmation. Caveat: EAC/EDC sources are better for feasibility and large-load validation than for complete project discovery.

---

## 5. Official Cloud-Region and Hyperscaler Seeds

As of the 2026-08-12 research pass, the major global cloud providers' official region lists do **not** show a Cambodia cloud region. Treat this as a negative-control step: if a source claims `AWS Cambodia region` or `Azure Cambodia region`, verify against the official region list before adding a facility.

| Provider | Official source | Cambodia signal |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/ and https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Cambodia Region found in official global infrastructure pages. Nearby region signals are Singapore, Thailand, Malaysia, Indonesia, Hong Kong/Taiwan/Japan/Korea depending provider. |
| Microsoft Azure | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies and https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Cambodia geography/region found in official region lists. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | No Cambodia region found in official cloud locations/Compute regions. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Cambodia commercial region found in official OCI region list. |
| Alibaba / Tencent / Huawei | Use official global region docs only | Search for Cambodia partner/edge/cloud resale separately; do not infer a physical hyperscale region from reseller presence. |

Cloud query templates:

```text
"Cambodia" "cloud region" site:aws.amazon.com
"Cambodia" "Azure region" site:learn.microsoft.com OR site:azure.microsoft.com
"Cambodia" "Google Cloud region" site:cloud.google.com
"Cambodia" "OCI region" site:oracle.com OR site:docs.oracle.com
"Cambodia" "availability zone" "cloud"
"Cambodia" "local zone" "cloud"
```

Grade: **A** for official cloud-region existence/status. Grade **C** for partner/reseller pages that imply local cloud without proving a Cambodian datacenter.

---

## 6. Operator / Facility Seeds to Verify

Use these as facility seeds, then verify against MPTC/TRC/permit/power evidence.

| Operator / facility | Best source(s) | Method notes |
|---|---|---|
| **National Data Center / MPTC** | MPTC 2025 site visit: https://mptc.gov.kh/en/2025/07/he-minister-chea-vandeth-and-he-japanese-ambassador-ueno-atsushi-visited-the-digital-park-and-national-data-center-project-site/ ; DCD construction article: https://www.datacenterdynamics.com/en/news/cambodia-breaks-ground-on-national-data-center/ | Government project in Phnom Penh/Digital Park pipeline. Use MPTC as **A** for project/site visits; DCD/Khmer Times as **B** for $30m, 12-story, target completion/Tier IV claims unless MPTC page states them. |
| **ByteDC Phnom Penh / Urban Data Center** | Uptime award: https://uptimeinstitute.com/uptime-institute-awards/client/urban-data-center-co-ltd/1032 ; DCD launch article: https://www.datacenterdynamics.com/en/news/bytedc-launches-cambodia-data-center/ ; ASX/Kingsland filing on Urban Data Center sale | Uptime is **A** for certified project name/location and Tier award; DCD is **B** for launch/3MW/81,040 sq ft claims; listed-company filings are **A** for ownership/building history. Search legal aliases: `Urban Data Center Co., Ltd`, `Bytedc (KH) Co., Ltd`, `ByteDC Solutions`. |
| **Chaktomuk Data Center - PNH1** | Official site: https://www.chaktomuk-dc.com.kh/ ; Uptime award: https://uptimeinstitute.com/uptime-institute-awards/datacenter/chaktomuk-data-center--pnh1/1911 ; IBC listing: https://ibccambodia.com/member/chaktomuk-data-center-co-ltd/ | Official/Uptime sources are **A** for facility identity and Phnom Penh location; IBC gives address/contact as **B/A-** chamber evidence. Verify MPTC license after 2025 notice. |
| **SINET / S.I Group data centre** | Official SINET service page: https://www.sinet.com.kh/enterprise-solution/data-centre/ ; Archetype project page: https://www.archetype-group.com/projects/sinet-data-center/ | SINET is **A** for service offering; consultant page is **B** for 3,000 sqm Phnom Penh project details. Verify TRC ISP license and physical facility address. |
| **Kepstar Data Centre Management** | DCD mentions Kepstar planned projects; W.Media launch/planning article: https://w.media/kepstar-launches-cambodias-1st-tier-iii-data-center/ ; Baxtel/DataCenterMap pages | Mostly **B/C** unless official Kepstar, permit, TRC/MPTC, or Uptime evidence is found. Search address `216 Norodom Blvd` and legal company name. |
| **Daun Penh Data Center / DPDC** | DataCenterMap/Baxtel discovery pages | Treat as **C** until official site, MPTC/TRC, permit, or Uptime evidence is found. Search `Daun Penh Data Center`, `DPDC`, and Khmer variants. |
| **Ezecom / Telcotech, Seatel, MekongNet, NeocomISP/NTC** | Operator official service pages, TRC operator PDFs, DataCenterMap/Baxtel/Knight Frank report | These are likely telecom/ISP datacenter or hosting operators. Grade official operator pages **A** for service existence, but facility-level facts need address/certification/permit/power proof. |

Operator query templates:

```text
"ByteDC" "Phnom Penh" "data center"
"Urban Data Center Co., Ltd" "Cambodia"
"Bytedc (KH) Co., Ltd" "Cambodia"
"Chaktomuk Data Center" "PNH1"
"SINET" "Data Centre" "Phnom Penh"
"Kepstar" "data center" "Cambodia"
"Daun Penh Data Center" OR "DPDC" Cambodia
"Telcotech" "data center" Cambodia
"Ezecom" "data center" Cambodia
"Seatel" "cloud data center" Cambodia
"MekongNet" "data center" Cambodia
"NeocomISP" "data center" Cambodia
site:uptimeinstitute.com "Cambodia" "Data Center"
```

---

## 7. Trade Press and Secondary Sources

High-yield secondary sources:
- Data Center Dynamics: https://www.datacenterdynamics.com/ - best international trade source for Cambodia launch/construction articles.
- Khmer Times: https://www.khmertimeskh.com/ - often covers MPTC, CDC, and national infrastructure announcements.
- Cambodia Investment Review: https://cambodiainvestmentreview.com/ - useful for ByteDC, Knight Frank summaries, and investment context.
- Construction & Property Cambodia: https://construction-property.com/ - useful for construction-permit regime, construction starts, and real estate/infrastructure projects.
- Open Development Cambodia: https://opendevelopmentcambodia.net/ - mirrors government notices, legal documents, EIA datasets, power-sector reports, and local news.
- Knight Frank Cambodia data-centre report, December 2024: https://content.knightfrank.com/research/2946/documents/en/data-centres-the-cambodia-report-december-2024-11773.pdf - useful market/operator list; grade **B** and verify each facility.
- Baxtel/DataCenterMap/DataCenters.com/PeeringDB - discovery only; grade **C** unless linked to primary proof.

Trade-press query templates:

```text
site:datacenterdynamics.com Cambodia "data center"
site:khmertimeskh.com "data center" "Cambodia"
site:cambodiainvestmentreview.com "data centre" Cambodia
site:construction-property.com "data center" Cambodia
site:opendevelopmentcambodia.net "National Data Center"
site:opendevelopmentcambodia.net "data center" "license"
site:content.knightfrank.com "Cambodia" "data centres"
```

Grade: **B** for named projects from reputable trade/market press. Use these to find operator aliases and dates, not as final proof of operational status when official/certification evidence is missing.

---

## 8. Province-by-Province Enumeration Strategy

Cambodia has Phnom Penh capital plus 24 provinces. Start with the high-probability belt, then run low-yield sweeps for the rest.

### 8.1 Tier 1 - Phnom Penh Capital

Targets: Daun Penh, Srah Chak, Boeung Kak / PPCC, Russey Keo, Toul Sangke, Mean Chey, Sen Sok, Chamkar Mon, Toul Kork, Chroy Changvar, airport/CBD corridors.

Workflow:
1. Seed with known facilities: National Data Center, ByteDC/Urban Data Center, Chaktomuk PNH1, SINET, Kepstar, Daun Penh/DPDC, Ezecom/Telcotech, Seatel, MekongNet, NeocomISP.
2. For each legal name, search MPTC license pages and TRC operator PDFs.
3. Search MLMUPC and Phnom Penh Capital Administration/khan pages for construction permit, occupancy, and building inspection records.
4. Search EDC/EAC for Phnom Penh supply upgrades, substations, and high-load customer evidence.
5. Verify Uptime certifications and operator pages for facility status and names.

Queries:

```text
"Phnom Penh" "data center" "Tier III"
"ភ្នំពេញ" "មជ្ឈមណ្ឌលទិន្នន័យ"
"Daun Penh" "National Data Center" "MPTC"
"Srah Chak" "National Data Center"
"Boeung Kak" "ByteDC" OR "PPCC" "data center"
"Russey Keo" "Chaktomuk Data Center"
site:phnompenh.gov.kh "មជ្ឈមណ្ឌលទិន្នន័យ"
site:mlmupc.gov.kh "ភ្នំពេញ" "មជ្ឈមណ្ឌលទិន្នន័យ"
```

### 8.2 Tier 1 Spillover - Kandal

Targets: Techo International Airport / KTI area, Takhmao, Kandal Stueng, Ang Snuol, Kien Svay, Muk Kampul, Khsach Kandal, National Roads 2/3/4/5/6 corridors, Phnom Penh suburban industrial land.

Workflow:
1. Search Kandal + airport/logistics/SEZ terms because new large campuses may choose lower-cost suburban land while marketing themselves as Phnom Penh.
2. Search CDC/QIP, SEZ Smart Search, local provincial administration, MLMUPC, EAC/EDC, and MPTC/TRC by legal company.
3. Validate any KTI/airport-area investment marketing against CDC/QIP and construction-permit evidence.

Queries:

```text
"Kandal" "data center" Cambodia
"ខេត្តកណ្តាល" "មជ្ឈមណ្ឌលទិន្នន័យ"
"Techo International Airport" "data center"
"KTI" "data center" Cambodia
"Kandal Stueng" "data center"
"Ang Snuol" "data center"
site:cdc.gov.kh "Kandal" "data center"
site:eac.gov.kh "Kandal" "data center"
```

### 8.3 Tier 2 - Siem Reap, Battambang, Preah Sihanouk, Banteay Meanchey, Svay Rieng

Use these provinces for edge, disaster-recovery, border, SEZ, tourism/casino, and connectivity searches.

- **Siem Reap**: tourism/government edge, airport, fiber routes, disaster recovery from Phnom Penh. Search `Siem Reap data center`, `សៀមរាប មជ្ឈមណ្ឌលទិន្នន័យ`, `EDC Siem Reap substation data center`, `SINET Siem Reap data center`.
- **Battambang**: western regional hub and Thailand corridor. Search `Battambang data center`, `បាត់ដំបង មជ្ឈមណ្ឌលទិន្នន័យ`, `EDC Battambang data center`.
- **Preah Sihanouk / Sihanoukville**: port, SEZ, casino/industrial, submarine/landing connectivity possibilities. Search `Sihanoukville data center`, `Preah Sihanouk data center`, `ក្រុងព្រះសីហនុ មជ្ឈមណ្ឌលទិន្នន័យ`, `Sihanoukville SEZ data center`.
- **Banteay Meanchey / Poipet**: Thailand border trade and Poipet SEZ. Search `Poipet data center`, `Banteay Meanchey data center`, `បន្ទាយមានជ័យ មជ្ឈមណ្ឌលទិន្នន័យ`.
- **Svay Rieng / Bavet**: Vietnam border and SEZ/manufacturing corridor. Search `Bavet data center`, `Svay Rieng data center`, `ស្វាយរៀង មជ្ឈមណ្ឌលទិន្នន័យ`, `Tai Seng Bavet data center`.

Workflow:
1. Start from TRC operator presence and ISP POPs, not global cloud pages.
2. Search CDC SEZ pages and province/district pages for construction/investment.
3. Search EAC annual report by province for distribution licensee/service-area evidence, then EDC/MME for substations and transmission upgrades.
4. Treat branch POPs, network rooms, and telco exchanges separately from commercial datacenters unless they sell colocation/hosting/cloud or have facility-grade evidence.

### 8.4 Tier 3 - Remaining Province Sweep

Provinces: Kampong Cham, Kampong Chhnang, Kampong Speu, Kampong Thom, Kampot, Kep, Koh Kong, Kratie, Mondulkiri, Oddar Meanchey, Pailin, Preah Vihear, Prey Veng, Pursat, Ratanakiri, Stung Treng, Takeo, Tboung Khmum.

Use a lightweight sweep unless a lead appears:

```text
"{province_en}" "data center" Cambodia
"{province_en}" "data centre" Cambodia
"{province_kh}" "មជ្ឈមណ្ឌលទិន្នន័យ"
"{province_en}" "cloud" "Cambodia" "ISP"
"{province_en}" "SEZ" "data center"
"{province_en}" "substation" "data center"
site:cdc.gov.kh "{province_en}" "digital"
site:eac.gov.kh "{province_en}" "licensee"
site:edc.com.kh "{province_en}" "substation"
```

Prioritization notes:
- **Kampong Speu**: Phnom Penh industrial spillover and National Road 4 corridor.
- **Koh Kong / Kampot / Kep**: coastal power/industrial/tourism checks; watch for green-power or SEZ marketing claims.
- **Kampong Cham / Tboung Khmum / Prey Veng / Takeo**: Phnom Penh/Vietnam corridor edge checks.
- **Kratie / Stung Treng / Ratanakiri / Mondulkiri / Preah Vihear / Oddar Meanchey / Pailin**: low-probability for large commercial DCs; search only for government/telecom edge facilities, mining/energy-linked compute claims, or suspicious AI/hydro announcements.

---

## 9. Verification and Pitfalls

1. **Do not count cloud reseller offices as datacenters.** Cambodia has many cloud/IT service companies but no official AWS/Azure/GCP/OCI Cambodia region found in the official lists.
2. **Separate telecom POP/exchange from datacenter.** TRC/ISP evidence is an operator lead. Count a facility only when there is colocation/hosting/cloud service, Uptime/certification, a named facility page, permit, or credible project evidence.
3. **MPTC 2025 license notice changes the compliance baseline.** Any operator active before June 2025 may need new MPTC authorization. Track license evidence separately from facility existence.
4. **Watch Phnom Penh aliasing.** A facility may appear as `ByteDC`, `Urban Data Center`, `Global IT Media Hub`, `PPCC`, and `G-Tech`. Key by legal owner + facility/campus + address.
5. **Use construction and power sanity checks.** Claims of 5-10+ MW should usually have EDC/EAC/substation, generator, EIA, import, or construction traces.
6. **Directories overcount.** Baxtel/DataCenterMap/DataCenters.com may list the same operator with slightly different names or include POPs. Grade these as **C** until verified.
7. **Government National Data Center is separate from private colo.** It may serve public and private institutions, but treat it as an MPTC/government facility unless commercial terms/license evidence show otherwise.

Suggested final pipeline:
1. Download latest TRC operator PDF and extract all ISP/value-added/network operators.
2. Build a Phnom Penh facility seed list from Uptime + official operator pages + DCD/Khmer Times/Knight Frank.
3. Search MPTC licensing notice/follow-up pages by every legal name and Khmer name.
4. Search MLMUPC/Phnom Penh/Kandal permitting plus CDC/QIP/SEZ for construction/investment evidence.
5. Search EAC/EDC/MME for power/service-area validation.
6. Run province sweeps for Kandal, Siem Reap, Battambang, Preah Sihanouk, Banteay Meanchey, and Svay Rieng; then lightweight all-province negative sweeps.
