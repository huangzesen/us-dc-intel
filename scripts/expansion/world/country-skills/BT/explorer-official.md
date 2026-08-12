# BT Explorer Official - Bhutan Datacenter Enumeration via Government, Regulatory, Utility, Cloud, and Official Operator Sources

Date: 2026-08-12. Scope: Bhutan (BT). Repo divisions are the 20 dzongkhags: Paro, Chhukha, Haa, Samtse, Thimphu, Tsirang, Dagana, Punakha, Wangdue Phodrang, Sarpang, Trongsa, Bumthang, Zhemgang, Trashigang, Monggar, Pema Gatshel, Lhuentse, Samdrup Jongkhar, Gasa, Trashi Yangtse.

Reliability grades: **A** = official/primary source (government, regulator, utility, operator official page, company filing, official cloud-region page, PeeringDB for IX facts); **B** = strong secondary or trade source with named operator/site/capacity; **C** = weak directory, market report, social post, or promotional article used only as a lead.

---

## 0. Bhutan-specific structural facts

- Bhutan has **no public national datacenter register** and no searchable national planning-permit database for datacenter projects. Enumeration must join GovTech/GDC, DCS/Thimphu TechPark, DHI/Bitdeer official material, Gelephu Mindfulness City Authority announcements, BICMA licensing, BPC/DGPC/BEA energy records, local construction authorities, cloud-region pages, and local/trade press.
- **English is the practical search language.** Government, regulator, telecom, energy, and ICT material is normally published in English. Dzongkha searches are low-yield for this sector.
- **Do not merge asset classes.** Bhutan has government hosting, commercial colocation, internet exchange/network nodes, crypto-mining datacenters, and planned AI/GPU campuses. These are separate records even when the same national energy narrative is used.
- **Confirmed physical anchors as of 2026-08:** Government Data Centre (GDC/Neyduetewa) at Thimphu TechPark; Data Centre Services Pvt. Ltd. (DCS) Tier 2/3 Internet Data Centre inside Thimphu TechPark; btIX at Thimphu TechPark; Bitdeer/DHI crypto-mining datacenters at Gedu (Chhukha, 100 MW online crypto) and Jigmeling (Sarpang, 500 MW online crypto in latest 2026 Bitdeer materials).
- **Planned/proposal anchors:** 21st Century Economic Roadmap / The Bhutanese-reported 40-50 MW, USD 450M national datacenter target with construction aimed at 2027; DHI's 2026 Invest Bhutan AI datacenter proposal; SATO Technologies-GMCA LOI for a hydro-powered AI compute campus in Gelephu Mindfulness City. Treat all three as planned/proposal until land, permit, utility, or construction evidence appears.
- **Power is a gating signal, not facility proof.** Bhutan's hydropower makes the country attractive for digital infrastructure, but winter lean-season imports from India and run-of-river seasonality are material caveats. Keep `gross electrical capacity`, `IT load`, `mining load`, `substation/feed`, and `planned scale` in separate fields.

Key verified anchors:

- GovTech/GDC ITU resilience presentation: https://www.itu.int/en/ITU-D/Regional-Presence/AsiaPacific/Documents/Events/2023/RDF-2023/Presentations%20and%20Relevant%20Reports/Session%209/Speaker%204%20Bhutan%20Session%209%20presentation%20Mr%20Choney.pdf
- GDC support portal: https://support.neyduetewa.gov.bt/
- DCS official site: https://www.dcs.bt/ and https://www.dcs.bt/about-us/
- DCS power/cooling page: https://www.dcs.bt/power-and-cooling/
- DHI 10X roadmap PDF: https://dhi.bt/document/10X-Journey-DHI-Group-Roadmap.pdf
- Bitdeer June 2026 operations update: https://ir.bitdeer.com/news-releases/news-release-details/bitdeer-announces-june-2026-production-and-operations-update/
- Bitdeer Q2 2026 results PDF: https://ir.bitdeer.com/node/9696/pdf
- SATO LOI page: https://www.bysato.com/news/sato-bhutan-sovereign-ai-compute-campus
- BICMA online licensing notice: https://www.bicma.gov.bt/?p=7872
- PeeringDB btIX: https://www.peeringdb.com/ix/2355
- BPC Power Data Book 2023: https://www.bpc.bt/wp-content/themes/bpc/assets/downloads/Power%20Data%20Book%202023.pdf
- MoENR National Energy Policy 2025: https://www.moenr.gov.bt/?p=15033

---

## 1. Evidence and grading rules

Minimum positive evidence:

1. **Operational government/commercial facility:** official operator/government page or ITU/government presentation, plus site/location evidence where available.
2. **Operational crypto-mining datacenter:** company filing/IR release or official DHI/Bitdeer release with named site and MW. Record as `crypto/mining`, not commercial colocation.
3. **IX or network node:** PeeringDB, btIX official page, or PCH/btIX listing. Record as interconnection evidence, not a datacenter unless a colocated datacenter is separately verified.
4. **Planned/proposed AI or national datacenter:** official authority/operator announcement or official policy/roadmap, with status verb captured exactly (`LOI`, `proposal`, `feasibility study`, `construction target`).
5. **Hyperscaler cloud:** official cloud-region pages only. In Bhutan these verify absence of local AWS/Azure/GCP/OCI regions.

Grade guidance:

- **A:** GovTech, GDC/Neyduetewa, DCS, DHI, GMCA, SATO official LOI page, Bitdeer IR/SEC materials, BICMA, BPC, DGPC, BEA, MoIT/BCTA, MoENR/MoICE, official cloud-region pages, PeeringDB for btIX.
- **B:** Data Center Dynamics, The Bhutanese, Kuensel, BBS, Business Bhutan, GovInsider, CoinDesk/The Block/Cointelegraph when citing named mining filings or official statements.
- **C:** Baxtel, DataCenterMap, Cloudscene, market-report PR, social media, directory listings, generic vendor pages.

Status mapping:

- `operational/online`: GDC, DCS, btIX, Bitdeer Gedu and Jigmeling when backed by current Bitdeer materials.
- `planned/proposal`: DHI AI datacenter, national 40-50 MW roadmap datacenter, SATO/GMC AI campus.
- `lead only`: telco exchange/server room, bank/government server room, industrial park, hydropower project, fiber route, cloud service availability without facility evidence.

---

## 2. Planning, construction, and land sources

Bhutan has no public datacenter planning register. Use these official sources to identify authority, process, and parcel context; expect low direct project yield.

- **Ministry of Infrastructure and Transport (MoIT):** https://moit.gov.bt/. National infrastructure/construction authority context.
- **Bhutan Construction and Transport Authority (BCTA):** https://moit.gov.bt/bhutan-construction-transport-authority/. Building-permit and contractor-regulation context. Grade A for process, not a project register.
- **Thimphu Thromde construction approval:** https://thimphucity.bt/construction-approval/. Grade A for Thimphu construction process; useful for GDC/DCS/TechPark context.
- **Citizen Services Portal:** https://www.citizenservices.gov.bt/. Licensing/building-service route; BICMA online licensing is also accessed through citizen services.
- **National Land Commission:** https://www.nlc.gov.bt/. Parcel/Thram/land-administration context if a candidate site has a named parcel.
- **Dzongkhag and thromde administrations:** use official dzongkhag domains and Facebook pages for local construction notices outside Thimphu. Relevant authorities include Sarpang for Jigmeling/Gelephu and Chhukha for Gedu.
- **Gelephu Mindfulness City Authority (GMCA):** https://gmc.bt/ and https://gmc.bt/news/. Grade A for GMC zone/investment announcements. The SATO AI datacenter item remains LOI/planned unless GMCA publishes land lease, construction, or power-allocation evidence.

Planning/land query templates:

```text
site:moit.gov.bt ("data center" OR "data centre" OR datacenter OR "server room")
site:thimphucity.bt ("construction approval" OR "building permit" OR "data centre")
site:nlc.gov.bt ("Gelephu" OR "Jigmeling" OR "Gedu" OR "TechPark") ("lease" OR "land" OR "Thram")
site:gmc.bt ("data center" OR "data centre" OR "AI" OR "Green Technology Valley" OR "SATO")
"{dzongkhag}" "dzongkhag administration" ("building permit" OR "construction" OR "industrial")
"Gelephu" OR "Jigmeling" ("land lease" OR "building permit" OR "construction") "data"
"Gedu" ("building permit" OR "construction" OR "substation") ("Bitdeer" OR "data center")
```

---

## 3. Regulator, policy, and digital-government sources

- **GovTech Agency:** https://tech.gov.bt/. Successor to the Department of IT and Telecom (DITT). Official anchor for GDC, GovNet, cloud services, government hosting, AI policy, and digital-government platforms. The ITU 2023 presentation states GovTech/DITT operationalized the GDC in 2017, colocated 1,000 sq ft GDC space with 2,500 sq ft leased to DCS, and hosted 200+ government systems at that time.
- **Neyduetewa/GDC support:** https://support.neyduetewa.gov.bt/. Confirms GDC/GovNet support and new server request channel.
- **BICMA:** https://www.bicma.gov.bt/. Telecom/ICT/media regulator. Its 2023 online licensing notice is Grade A for licensing workflow; its 2024 Starlink ISP license notice is a good example of connectivity licensing, not datacenter evidence.
- **DHI:** https://dhi.bt/. State holding/investment company. Grade A for DHI strategy, Green Digital/Bitdeer partnership, TechPark ecosystem, and AI datacenter investment framing. The DHI 10X roadmap calls for feasibility pathways for green AI datacenters, but this is strategic intent rather than a site record.
- **21st Century Economic Roadmap:** official policy source; The Bhutanese provides detailed reporting on the 40-50 MW / USD 450M datacenter target and 2027 construction aim. Treat as national project pipeline until a site is selected and permitted.
- **Data/privacy context:** Data Protection Act 2018 and National Digital Identity/NDI materials can explain sovereign hosting demand, but they are not facility records.

Regulator/policy query templates:

```text
site:tech.gov.bt ("Government Data Centre" OR "Government Data Center" OR "GDC" OR "cloud" OR "GovNet")
site:neyduetewa.gov.bt OR site:support.neyduetewa.gov.bt ("server request" OR "Government Data Center")
site:bicma.gov.bt ("ISP License" OR "online licensing" OR "ICT" OR "cloud")
site:dhi.bt ("data center" OR "data centre" OR "AI data" OR "Green Digital" OR "Bitdeer")
site:dhi.bt filetype:pdf ("AI Data Centers" OR "digital infrastructure" OR "dark fiber")
"21st Century Economic Roadmap" "data center" Bhutan
"National AI Strategy" Bhutan ("compute" OR "data center" OR "GPU")
"Fiscal Incentives Act 2021" Bhutan "ICT"
```

---

## 4. Utility, grid, and energy evidence

Large Bhutan projects should be checked against power-sector evidence before status is upgraded.

- **Bhutan Power Corporation (BPC):** https://www.bpc.bt/. Distribution/transmission-service context, substations, OPGW/fiber over power infrastructure, annual reports, and Power Data Book. DCS states it has dual feeders from Olakha and Semtokha substations via separate routes.
- **Druk Green Power Corporation (DGPC):** https://www.drukgreen.bt/. Generation company and official hydropower source. Use for plant/project capacity and winter import context, not as datacenter evidence.
- **Bhutan Electricity Authority (BEA):** https://www.bea.gov.bt/. Regulator for electricity licensing/tariffs.
- **MoENR / Department of Energy:** https://www.moenr.gov.bt/. National Energy Policy 2025 targets 25,000 MW installed capacity by 2040, including 20,000 MW hydro and 5,000 MW solar. Use this as power-market context.

Power caveats to record:

- Bhutan's hydro fleet is strongly seasonal; winter lean months can require power imports from India.
- Do not equate hydropower generation capacity with datacenter IT load.
- For Bitdeer and SATO, preserve whether the source states `firm power`, `electrical capacity`, `IT MW`, or `mining capacity`.

Utility query templates:

```text
site:bpc.bt ("data center" OR "data centre" OR "industrial load" OR "substation" OR "OPGW")
site:bpc.bt ("Gedu" OR "Jigmeling" OR "Gelephu" OR "TechPark" OR "Olakha" OR "Semtokha")
site:drukgreen.bt ("data center" OR "AI" OR "mining" OR "power purchase")
site:bea.gov.bt ("data center" OR "tariff" OR "large industry" OR "license")
site:moenr.gov.bt ("data center" OR "AI" OR "hydropower" OR "National Energy Policy")
"Bhutan Power Corporation" ("Jigmeling" OR "Gedu" OR "Gelephu") ("MW" OR "substation" OR "energized")
"Druk Green" ("AI data center" OR "Bitdeer" OR "Green Digital")
```

---

## 5. Official cloud and operator seed list

### 5.1 Hyperscale cloud regions - absence check

Use current official region pages to verify that Bhutan does **not** have an AWS, Azure, Google Cloud, or Oracle OCI public cloud region. Do not create a Bhutan facility from SaaS availability, partner hosting, edge cache, or customer-country support.

| Provider | Official source | Bhutan handling |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Bhutan region. Nearest practical regions are India/Singapore. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Bhutan region. Treat Microsoft/365/Azure usage as out-of-country or partner-hosted unless Microsoft says otherwise. |
| Google Cloud | https://cloud.google.com/about/locations | No Bhutan region. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Bhutan public cloud region. |

Cloud queries:

```text
"AWS" "Bhutan" ("region" OR "availability zone" OR "local zone")
"Azure" "Bhutan" ("region" OR "data center" OR "datacenter")
"Google Cloud" "Bhutan" ("region" OR "data center")
"Oracle Cloud" "Bhutan" ("region" OR "data center")
"cloud region" "Bhutan" ("GovTech" OR "DHI" OR "DCS")
```

### 5.2 Official operator/platform seeds

| Operator/platform | Official source | Division | Status and method notes |
|---|---|---:|---|
| GovTech Agency / GDC / Neyduetewa | https://tech.gov.bt/ ; https://support.neyduetewa.gov.bt/ ; ITU PDF above | Thimphu | **Operational government DC.** ITU says operationalized in 2017, colocated at TechPark, 200+ government systems in 2023. Capacity fields: use the ITU resource stats only with source/date; MW not public. |
| Data Centre Services Pvt. Ltd. (DCS) | https://www.dcs.bt/ ; https://www.dcs.bt/about-us/ ; https://www.dcs.bt/power-and-cooling/ | Thimphu | **Operational commercial colo/IDC.** Operator says Tier 2/3 Internet Data Centre inside Thimphu TechPark, dual Olakha/Semtokha feeds, ABB transformers, carrier-neutral services. |
| Thimphu TechPark Ltd (TTPL) | https://thimphutechpark.bt/ | Thimphu | IT park/host site for GDC/DCS/btIX. Useful for tenant and campus context; not itself a DC record unless a facility is named. |
| btIX / Bhutan Internet Exchange | https://www.btix.bt/ ; https://www.peeringdb.com/ix/2355 | Thimphu | IX at Thimphu TechPark. Grade A for interconnection/location; not a datacenter by itself. |
| DHI / Green Digital | https://dhi.bt/ | National; site-specific in Chhukha/Sarpang when named | Official investment/partnership source for Bitdeer and green digital-asset mining. Do not infer unnamed sites from "across Bhutan." |
| Bitdeer Technologies | https://www.bitdeer.com/ ; https://ir.bitdeer.com/ | Chhukha, Sarpang | **Operational crypto datacenters.** Latest public 2026 materials list Gedu 100 MW online crypto and Jigmeling 500 MW online crypto. |
| GMCA / GMC | https://gmc.bt/ | Sarpang | Special administrative region and Green Technology Valley context. SATO is LOI/planned unless construction evidence appears. |
| SATO Technologies | https://www.bysato.com/news/sato-bhutan-sovereign-ai-compute-campus | Sarpang | LOI effective 2026-06-20, announced 2026-07-06, for phased renewable AI datacenter campus in GMC. Initial 5 MW, target 100 MW firm hydro, possible 500 MW pathway are planning claims, not operating capacity. |
| Bhutan Telecom | https://www.bhutan-telecom.bt/ | National; likely Thimphu for core | Telecom/fiber/enterprise services. Facility-level server rooms require explicit evidence. |
| Tashi InfoComm / TashiCell | https://www.tashicell.bt/ | National; likely Thimphu for core | Telecom operator. Treat exchange/core-network facilities as leads unless named as datacenter/colo. |

Operator queries:

```text
site:dcs.bt ("data centre" OR "colocation" OR "Tier" OR "TechPark" OR "Olakha" OR "Semtokha")
site:tech.gov.bt OR site:support.neyduetewa.gov.bt ("GDC" OR "Government Data Center" OR "GovNet")
site:thimphutechpark.bt ("data centre" OR "DCS" OR "btIX" OR "BITC")
site:btix.bt ("launch" OR "Thimphu TechPark" OR "members")
site:ir.bitdeer.com Bhutan ("Gedu" OR "Jigmeling" OR "MW" OR "Online")
site:dhi.bt ("Bitdeer" OR "Green Digital" OR "AI Data Centers")
site:bysato.com Bhutan ("AI data centre" OR "Gelephu" OR "100 MW" OR "500 MW")
site:gmc.bt ("SATO" OR "AI data center" OR "Green Technology Valley")
site:bhutan-telecom.bt ("data center" OR "colocation" OR "cloud" OR "fiber")
site:tashicell.bt ("data center" OR "cloud" OR "enterprise" OR "fiber")
```

---

## 6. Division coverage workflow

Run the same four-pass workflow for every dzongkhag:

1. **National seed pass:** GovTech/GDC, DCS, DHI/Bitdeer, GMCA/SATO, BICMA, BPC/DGPC/BEA, MoIT/BCTA, cloud-region pages.
2. **Named-site pass:** GDC, Neyduetewa, DCS, Thimphu TechPark, btIX, Gedu, Jigmeling, Gelephu, GMC, Green Technology Valley, BITC, Olakha, Semtokha.
3. **Division pass:** run dzongkhag templates below. Map a hit only when town/park/landmark evidence places it in that dzongkhag.
4. **Validation pass:** classify as government DC, commercial colo, crypto/mining, planned AI/GPU, IX/network, telco exchange, or false positive.

### Priority dzongkhags

**Thimphu** - GDC, DCS, Thimphu TechPark, btIX, telco/enterprise core.

```text
"Thimphu" ("data center" OR "data centre" OR "server room" OR colocation)
"Thimphu TechPark" ("DCS" OR "data centre" OR "GDC" OR "btIX")
"Government Data Centre" OR "Government Data Center" OR "Neyduetewa" Thimphu
site:tech.gov.bt "Thimphu" ("GDC" OR "cloud" OR "GovNet")
site:dcs.bt ("Thimphu" OR "TechPark" OR "Olakha" OR "Semtokha")
"Thimphu" ("Bhutan Telecom" OR "TashiCell") ("exchange" OR "data center" OR "cloud")
```

**Sarpang** - Jigmeling/Bitdeer, Gelephu/GMC, SATO LOI.

```text
"Sarpang" ("data center" OR "data centre" OR "AI" OR "mining")
"Jigmeling" ("Bitdeer" OR "500 MW" OR "data center" OR "mining" OR "energized")
"Gelephu" ("data center" OR "AI" OR "GMC" OR "Green Technology Valley")
site:gmc.bt ("Sarpang" OR "Gelephu" OR "SATO" OR "AI data")
"Sarpang dzongkhag" ("building permit" OR "industrial" OR "construction")
```

**Chhukha** - Gedu/Bitdeer, Chukha hydro corridor, Phuentsholing industrial/connectivity leads.

```text
"Chhukha" OR "Chukha" ("data center" OR "data centre" OR "mining" OR "Bitdeer")
"Gedu" ("Bitdeer" OR "100 MW" OR "data center" OR "mining")
"Phuentsholing" ("data center" OR "IT park" OR "colocation" OR "server room")
"Chukha" ("substation" OR "hydropower" OR "industrial load") ("data" OR "mining")
```

### Low-probability dzongkhags

For Paro, Haa, Samtse, Tsirang, Dagana, Punakha, Wangdue Phodrang, Trongsa, Bumthang, Zhemgang, Trashigang, Monggar, Pema Gatshel, Lhuentse, Samdrup Jongkhar, Gasa, and Trashi Yangtse, record negative searches rather than skipping. Watch for telecom exchanges, bank/government server rooms, university/HPC, industrial estates, and hydro-adjacent proposals. Power plants alone are **not** datacenters.

```text
"{dzongkhag}" ("data center" OR "data centre" OR datacenter OR "server room" OR cloud)
"{dzongkhag}" ("thromde" OR "dzongkhag administration") ("building permit" OR "construction")
"{dzongkhag}" ("BPC" OR "DGPC" OR "substation" OR "hydropower")
"{dzongkhag}" ("Bhutan Telecom" OR "TashiCell" OR "Tashi InfoComm") ("exchange" OR "fiber" OR "data")
"{dzongkhag}" ("AI" OR "GPU" OR "HPC" OR "supercomputer" OR "mining")
"{dzongkhag}" ("industrial park" OR "FDI" OR "digital infrastructure")
```

Hydro/industrial watch notes:

- Wangdue Phodrang/Punakha: Punatsangchhu and Sephu solar context; count only if tied to named digital infrastructure.
- Trongsa: Mangdechhu/Nikachhu power context; no known DC from official sources.
- Trashi Yangtse: Kholongchhu power context; no known DC from official sources.
- Samdrup Jongkhar/Samtse/Paro: industrial/connectivity candidates; no confirmed DC from official sources.

---

## 7. Output normalization

For each candidate, capture:

- `name`, `aliases`, `operator`, `ultimate_parent`, `asset_class`
- `division`, `town/site`, `address_or_landmark`, `coordinates` if reliable
- `status`, `status_date`, `source_status_verb`
- `capacity_it_mw`, `capacity_electrical_mw`, `mining_mw`, `racks`, `floor_area`, `site_area`
- `power_sources`, `substations/feeders`, `seasonal_power_caveat`
- `connectivity` (ISPs, fiber, btIX/PeeringDB, satellite/Starlink if relevant)
- `evidence_grade_by_field` and `source_urls`

Known current seed records:

| Name | Division | Asset class | Status | Grade |
|---|---|---|---|---|
| Government Data Centre / Neyduetewa | Thimphu | Government/sovereign hosting | Operational since 2017 | A |
| Data Centre Services Pvt. Ltd. / DCS | Thimphu | Commercial colo/IDC | Operational | A |
| btIX | Thimphu | Internet exchange | Operational | A |
| Bitdeer Gedu | Chhukha | Crypto-mining datacenter | 100 MW online crypto in 2026 Bitdeer materials | A |
| Bitdeer Jigmeling | Sarpang | Crypto-mining datacenter | 500 MW online crypto in 2026 Bitdeer materials | A |
| National 40-50 MW datacenter | TBD | Planned national/AI-ready datacenter | Roadmap/feasibility; construction target 2027 per local reporting | B until official site/permit |
| DHI AI datacenter proposal | TBD | Planned AI/GPU infrastructure | Proposal/strategy | A for DHI strategy, B for facility details |
| SATO-GMCA AI compute campus | Sarpang | Planned AI datacenter campus | LOI; initial 5 MW, target 100 MW, possible 500 MW pathway | A for LOI, B for scale/timing |
