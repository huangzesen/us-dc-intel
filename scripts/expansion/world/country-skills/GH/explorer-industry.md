# GH Explorer Industry - Ghana Datacenter Enumeration via Operators, Connectivity, Peering, Trade Press and Directories

Date: 2026-08-12. Country: **GH Ghana**. Division model: **16 regions**. Angle: **industry and market evidence** that complements `explorer-official.md`: operator pages, Uptime records, colocation directories, subsea/IXP sources, trade press, investor announcements and regional business media.

Reliability grades:
- **A** = official operator facility page, official cloud-region page, Uptime Institute award page, official IXP/subsea/operator page, or regulator record.
- **A-** = official operator/investor press release proving a project or capacity claim where no regulator filing is visible; use `announced_capacity_mw` unless commissioning is also proven.
- **B** = established trade press or reputable Ghanaian/pan-African business press with specific site facts, dates, parties and status.
- **C** = directories, market reports, SEO lists, social posts, unverified rankings and capacity tables. Use as discovery leads only.

Grade each claim separately. Example: Equinix AC1 existence/address is **A** from Equinix; a directory rack count is **C** unless confirmed by Equinix/Uptime/permit evidence.

---

## 0. Ghana market facts

- Ghana's commercial colocation market is **small and Accra-centric**. The verified commercial cluster is in **Greater Accra**: Equinix AC1/MDXi Appolonia, Onix Accra #1, PAIX Accra and the Africa Data Centres/Onix Accra pipeline. Telco and enterprise data rooms exist but are often not retail colocation.
- **Ashanti has an official government DC record**: Uptime Institute lists NITA's **Ghana E-Gov Cloud Data Center** in Kumasi. Do not mark Ashanti as fully empty; mark it as government DC present and commercial colo unconfirmed unless new evidence appears.
- Other regions should generally be negative for commercial colocation after search, but keep government, telco, bank, university, mining, oil/gas and disaster-recovery rooms as possible non-commercial records.
- Ghana is a connectivity hub for West Africa. NCA lists legacy submarine cable providers SAT-3, MainOne, WACS, Glo and ACE; Bayobab/MTN announced the 2Africa landing in Accra. Internet-exchange evidence now includes GIX, Accra-IX and LINX Accra.
- **Equiano is not a Ghana landing**. Google/Equiano route evidence points to Portugal, Togo, Nigeria, St Helena, Namibia and South Africa; do not add Ghana Equiano capacity.
- **No AWS, Azure, Google Cloud or Oracle public region in Ghana** as of 2026-08-12. Treat cloud/edge/CDN presence as ecosystem evidence, not a facility.
- Announced MW is not operational MW. Africa Data Centres' Accra project has been announced as 10 MW initial / 30 MW expandable and later partnered with Onix; keep status as pipeline/construction/partnered unless current operator evidence proves launch.

---

## 1. Verified operator and facility census

| Operator / facility | Region / location | Status and capacity handling | Primary evidence | Grade |
|---|---|---|---|---|
| **Equinix AC1 Accra** / MainOne MDXi Appolonia | Greater Accra - Plot No. 1, Benin Boulevard, Appolonia Industrial Park, Appolonia City | Operational carrier-neutral colocation/IBX. Equinix official page gives address and facility space; Uptime/trade records support Tier III history. Use operator page for existence/address; use Uptime or operator-certified materials for tier. | https://www.equinix.com/data-centers/europe-colocation/ghana-colocation/accra-data-centers/ac1 ; https://www.equinix.com/data-centers/europe-colocation/ghana-colocation/accra-data-centers ; https://www.peeringdb.com/fac/1965 | A for existence/address; B/C for third-party capacity details |
| **Onix Accra #1** / Onix Data Centres Ghana / Ngoya Etix DC (Ghana) Ltd | Greater Accra - Accra/Amrahia area | Operational carrier-neutral Tier IV facility. Onix official site states Tier IV colocation in Accra; Uptime lists ONIX Accra #1; AIIM case study states 170 racks expandable to 680 and partial solar. DCD reported 12 MW at opening. Keep rack and MW fields source-tagged. | https://onixdatacentres.com/ ; https://uptimeinstitute.com/uptime-institute-awards/client/onix-data-centres-ghana-limited/1060 ; https://aiimafrica.com/media/case-study-detail/case-study-onix-accra-1/ ; https://www.datacenterdynamics.com/en/news/ghanas-vice-president-opens-onix-tier-iv-data-center/ | A for existence/tier; A-/B for capacity depending source |
| **PAIX Accra** / RackAfrica legacy | Greater Accra - 42 Ring Road Central, Accra | Operational carrier-neutral colocation. PAIX official site confirms Ghana/Accra presence; Africa50 reported expansion to 1.2 MW. Directories preserve RackAfrica alias but are lead-only. | https://www.paix.io/ ; https://www.paix.io/contact-us ; https://www.africa50.com/media/news/article/paix-data-centres-expands-capacity-in-ghana-to-12-mw/ | A for operator presence; B for expansion capacity; C for directory details |
| **Africa Data Centres Accra** / Cassava Technologies, partnered with Onix | Greater Accra - Central Business District / Accra | Pipeline/construction/partnered unless an operator source confirms operational launch. ADC/Cassava announced initial 10 MW expandable to 30 MW; DCD reported Onix partnership in 2024. Store as `announced_capacity_mw`, not operational capacity. | https://www.africadatacentres.com/africa-data-centres-announces-that-it-will-start-construction-on-a-new-facility-in-accra-ghana/ ; https://www.cassavatechnologies.com/africa-data-centres-will-start-construction-on-a-new-facility-in-accra/ ; https://www.datacenterdynamics.com/en/news/africa-data-centres-and-onix-partner-for-data-center-build-in-accra-ghana/ | A-/B for announced project and capacity; status needs recheck |
| **NITA Primary Ghana National Data Center Accra** | Greater Accra - Accra | Operational government data centre / e-government infrastructure. Uptime lists the Accra project under NITA; NITA has a data-centre project page. | https://nita.gov.gh/projects/datacentre/ ; https://uptimeinstitute.com/uptime-institute-awards/datacenter/primary-ghana-national-data-center-accra-/2056 ; https://uptimeinstitute.com/uptime-institute-awards/client/national-information-technology-agency-nita/1008 | A |
| **NITA Ghana E-Gov Cloud Data Center Kumasi** | Ashanti - Kumasi | Official government DC record. Uptime lists this separate Kumasi project under NITA. Treat as government/non-commercial unless NITA shows commercial colocation. | https://uptimeinstitute.com/uptime-institute-awards/datacenter/ghana-egov-cloud-data-center/1684 ; https://uptimeinstitute.com/uptime-institute-awards/client/national-information-technology-agency-nita/1008 | A |
| **MTN Ghana / Bayobab / Telecel Ghana / AT / NGIC enterprise and network facilities** | Mainly Greater Accra, with regional exchanges | Connectivity and enterprise hosting leads. Usually not public retail colocation; verify each site through operator pages, NCA licences, PeeringDB/IXP records, or official enterprise product pages. | https://nca.org.gh/ ; https://bayobab.africa/ ; operator domains | A for official records; C for capacity unless documented |

Operator census queries:
```text
"Ghana" "data centre" "{operator}" launch OR inaugurated OR operational OR "Tier III" OR "Tier IV"
"Accra" "data centre" colo OR colocation OR "carrier-neutral" -Nigeria -Kenya
"{operator}" Ghana facility MW racks "data centre"
"{operator}" "Accra" "Uptime Institute"
"{operator}" "Ghana" "environmental permit" OR "bulk customer"
```

Alias rules:
- Equinix AC1 = MainOne MDXi Appolonia = MDXi Appolonia Data Center.
- Onix Accra #1 = Onix Data Centres Ghana = Ngoya Etix DC (Ghana) Ltd / Etix Accra #1 in older records.
- PAIX Accra = RackAfrica legacy.
- NITA Accra = Primary Ghana National Data Center Accra; NITA Kumasi = Ghana E-Gov Cloud Data Center.

---

## 2. Hyperscaler and cloud-provider status

Official pages to check every run:
- AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ and https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud: https://cloud.google.com/about/locations
- Oracle Cloud: https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

As of this methodology date, none lists a Ghana public cloud region. Do not create a Ghana hyperscale/cloud-region facility from:
- Google office or AI/research centre in Accra.
- CDN/cache/edge nodes.
- Partner cloud, managed hosting or reseller presence.
- Claims that customer data can be served in Ghana without an official cloud-region page.

Cloud queries:
```text
site:aws.amazon.com Ghana "Region" "Availability Zone"
site:learn.microsoft.com/azure Ghana "region"
site:cloud.google.com/about/locations Ghana "region"
site:oracle.com/cloud Ghana "cloud region"
"Ghana" "AWS region" OR "Azure region" OR "Google Cloud region" OR "Oracle Cloud region"
```

---

## 3. Connectivity, subsea and IXP evidence

Connectivity records are **DC adjacency leads**. They can identify landing stations, meet-me sites and operator candidates, but they do not automatically create a commercial data-centre record.

Verified sources and facts:
- NCA submarine-cable landing page: https://nca.org.gh/submarine-cable-landing/. It confirms the licence scope for submarine cable landing stations and lists legacy providers SAT-3, MainOne, WACS, Glo and ACE.
- Bayobab official 2Africa Ghana landing: https://bayobab.africa/bayobab-lands-2africa-subsea-cable-in-ghana-further-strengthening-internet-connectivity-in-africa/. Use this for the 2Africa Accra landing, then check NCA for licence evidence.
- GIX - Ghana Internet Exchange: https://gixa.org.gh/ and PCH entry https://www.pch.net/ixp/details/93. Use member lists and facility hints as ISP/network pivots.
- Accra-IX: https://www.accra-ix.net/. It describes a Ghana colocation/peering/interconnection non-profit; verify members and locations before creating facility links.
- LINX Accra: https://www.linx.net/network/linx-accra/ and https://www.linx.net/about/african-connectivity-solutions/. LINX states it is available across Onix, PAIX and Digital Realty data centres in Accra; verify the Digital Realty naming/host mapping before ingesting as a separate Ghana facility.
- Google Equiano official launch and route material: https://cloud.google.com/blog/products/infrastructure/introducing-equiano-a-subsea-cable-from-portugal-to-south-africa. Route evidence does not include Ghana.

Connectivity queries:
```text
"landing station" Ghana Accra OR Tema submarine cable
site:nca.org.gh "Submarine Cable Landing" "{operator}"
site:bayobab.africa Ghana 2Africa Accra landing
"Ghana Internet Exchange" OR GIX members Accra
"Accra-IX" Ghana colocation peering
"LINX Accra" Onix PAIX "Digital Realty"
"Equiano" Ghana site:cloud.google.com OR site:submarinenetworks.com
```

---

## 4. Trade press and market-monitoring feeds

Use these to detect new builds, financing, acquisitions and commissioning. They are not substitutes for official/operator evidence.

| Source | URL | Use | Grade |
|---|---|---|---|
| DatacenterDynamics (DCD) | https://www.datacenterdynamics.com/ | Ghana DC launches, ADC/Onix updates, acquisitions | B+ |
| Capacity Media | https://www.capacitymedia.com/ | subsea, carrier and data-centre market news | B |
| Connecting Africa | https://www.connectingafrica.com/ | ADC Ghana, telecom/cloud/connectivity | B |
| tech.africa / TechAfrica News | https://tech.africa/ ; https://techafricanews.com/ | African tech/DC/IXP announcements | B |
| Telecom Review Africa, Developing Telecoms, ITWeb Africa | outlet domains | telecom and infrastructure updates | B |
| Business & Financial Times Ghana | https://thebftonline.com/ | local ICT/investment coverage | B |
| Graphic Business / Daily Graphic | https://www.graphic.com.gh/business/ | Ghana business/government project notices | B |
| GhanaWeb, MyJoyOnline, Citi News, GNA | outlet domains | local launch/inauguration coverage; verify facts | B-/C |
| Africa50, AIIM, Cassava, ADC investor/operator sites | official domains | financing, capacity and ownership changes | A-/B depending claim |
| Baxtel, Data Center Map, DataCenters.com, PeeringDB, PCH | directory/peering domains | lead discovery, aliases, network ecosystem | C except PeeringDB/PCH for peering metadata |
| Xalam/D4D Hub, Arizton, Mordor and other market reports | vendor/report domains | market sizing only | C |

Feed queries:
```text
site:datacenterdynamics.com Ghana "data center" OR "data centre"
site:capacitymedia.com Ghana "data centre" OR submarine
site:connectingafrica.com Ghana "data centre" OR "cloud"
site:tech.africa Ghana "data centre" OR "LINX Accra"
site:thebftonline.com Ghana "data centre" OR "digital infrastructure"
site:graphic.com.gh Ghana "data centre" OR "cloud data"
"Ghana" "data centre" announced OR launched OR inaugurated OR commissioned OR groundbreaking
"Ghana" "data center" "MW" "Accra"
```

---

## 5. Directories and how to use them

Directories are useful for alias discovery and nearby-facility checks, but Ghana has a high risk of duplicated or stale entries.

Directory rules:
- Use Baxtel/DataCenterMap/DataCenters.com/Data Center Platform as **C** unless they link to an official operator page or Uptime record.
- Never ingest a directory-only facility without at least one operator, regulator, Uptime, permit or strong press source.
- Watch for alias duplication: MDXi vs Equinix AC1, RackAfrica vs PAIX Accra, Ngoya Etix vs Onix.
- Treat directory MW/rack values as `claimed_capacity` until official confirmation.
- For NITA, use Uptime/NITA first; directories may list additional or foreign records incorrectly.

Directory queries:
```text
site:baxtel.com Ghana "data center" OR "data centre"
site:datacentermap.com/ghana Accra "data center"
site:datacenters.com Ghana Accra "data center"
site:datacenterplatform.com Ghana NITA "data center"
site:peeringdb.com/fac Ghana Accra
```

---

## 6. Industry bodies and events

- Uptime Institute country/client search is a core certification source. Current Ghana records include Onix Accra #1 and NITA Accra/Kumasi; also check older MainOne/MDXi Appolonia certification history.
- GIX, Accra-IX and LINX Accra member lists identify network operators that may host or lease DC space.
- GISPA and the Ghana Chamber of Telecommunications can provide ISP/telco member pivots. Verify current domains before relying on them.
- AfPIF and Datacloud Africa event materials can identify Ghana operators and peering participants, but are **B/C** unless tied to official facility pages.
- No dedicated Ghana Data Centre Association was verified in this pass; do not invent one.

Queries:
```text
site:uptimeinstitute.com Ghana "Accra" "Data Center"
site:uptimeinstitute.com Ghana "Kumasi" "Data Center"
"Ghana" "Uptime Institute" "Tier III" "data centre"
"Ghana" "Uptime Institute" "Tier IV" "data centre"
"AfPIF" Accra MainOne Equinix Ghana
"Datacloud Africa" Accra Ghana data centre
"GISPA" Ghana members ISP data centre
"Chamber of Telecommunications" Ghana "data centre"
```

---

## 7. Per-region industry discovery map

| Region | Industry search set | Expected result / coding guidance |
|---|---|---|
| **Greater Accra** | `"Accra" "data centre" colo OR colocation OR "Tier III" OR "Tier IV" OR MW`; `"Appolonia" "data centre"`; `"Amrahia" "data centre"`; `"Ring Road Central" PAIX`; `"Tema" "landing station" Ghana`; directory cross-checks | Positive commercial and government cluster. Create facility records only after dedupe and official/operator confirmation. |
| **Ashanti** | `"Kumasi" "data centre" Ghana`; `"Ghana E-Gov Cloud Data Center" Kumasi`; `site:uptimeinstitute.com Ghana Kumasi`; `"KNUST" HPC OR "data centre"` | NITA government DC present in Kumasi. Commercial colo unconfirmed unless new operator evidence appears. |
| **Bono** | `"Sunyani" "data centre" Ghana`; `"Bono Region" "server room" Ghana`; `"Sunyani" colocation Ghana` | Expected negative for commercial colo; keep enterprise/telco leads separate. |
| **Bono East** | `"Techiman" "data centre" Ghana`; `"Bono East" "ICT hub" "data centre"` | Expected negative. |
| **Ahafo** | `"Ahafo" "data centre" Ghana`; `"Kenyasi" "server room" Ghana` | Expected negative except mining/enterprise ICT. |
| **Central** | `"Cape Coast" "data centre" Ghana`; `"Winneba" "server room" Ghana`; university ICT searches | Expected negative for commercial colo. |
| **Eastern** | `"Koforidua" "data centre" Ghana`; `"Eastern Region" Ghana "server room"` | Expected negative. |
| **North East** | `"Nalerigu" "data centre" Ghana`; `"North East Region" Ghana ICT server` | Expected negative. |
| **Northern** | `"Tamale" "data centre" Ghana`; `"Tamale" colocation Ghana`; `"Northern Region" Ghana "server room"` | Expected negative for commercial colo; government/UN/telco rooms possible. |
| **Oti** | `"Oti Region" "data centre" Ghana`; `"Dambai" "server room" Ghana` | Expected negative. |
| **Savannah** | `"Savannah Region" Ghana "data centre"`; `"Damongo" "server room" Ghana` | Expected negative. |
| **Upper East** | `"Bolgatanga" "data centre" Ghana`; `"Upper East" Ghana "server room"` | Expected negative. |
| **Upper West** | `"Wa" "data centre" Ghana`; `"Upper West" Ghana "server room"` | Expected negative. |
| **Volta** | `"Ho" "data centre" Ghana`; `"Volta Region" Ghana "data centre"`; `"Hohoe" "server room" Ghana` | Expected negative for commercial colo. |
| **Western** | `"Takoradi" "data centre" Ghana`; `"Sekondi" "server room" Ghana`; `"Western Region" Ghana "oil" "data centre"` | Enterprise/oil/gas ICT rooms possible; commercial colo unconfirmed. |
| **Western North** | `"Western North" Ghana "data centre"`; `"Sefwi Wiawso" "server room" Ghana` | Expected negative. |

For negative regions, store query/date notes. Do not omit a region from the output just because no facility is found.

---

## 8. Verification workflow

1. Seed from **A/A-** sources: Equinix, Onix, PAIX, NITA/Uptime, ADC/Cassava and IXP/subsea operator pages.
2. Dedupe aliases before counting facilities.
3. For each site, assign `division` by physical location, not by headquarters. Appolonia, Amrahia, Ring Road/CBD and Tema-area sites are Greater Accra; NITA Kumasi is Ashanti.
4. Split status and capacity: `operational_capacity_mw`, `announced_capacity_mw`, `racks`, `certification`, `source_date`, `source_grade`.
5. Escalate each facility to official verification through `explorer-official.md`: EPA, MMDA, Energy Commission, NCA, DPC, NITA/ministry, GIPC/GFZA/RGD.
6. Re-run cloud-region and Equiano exclusions each batch.
7. Sweep all 16 regions and explicitly output `no_projects: true` where appropriate.

Recommended output schema:
```json
{
  "country_code": "GH",
  "country_name": "Ghana",
  "division": "Greater Accra",
  "name": "Equinix AC1 Accra",
  "status": "operational",
  "operator": "Equinix",
  "developer": "Equinix / MainOne MDXi legacy",
  "capacity_mw": null,
  "announced_capacity_mw": null,
  "racks": null,
  "source_urls": [],
  "evidence_date": "2026-08-12",
  "evidence_grade": "A",
  "notes": "Dedupe with MainOne MDXi Appolonia."
}
```

---

## 9. Common false positives

- Market-report counts that list Ghana facilities without names or sources.
- Systalink or SEO rankings that mention a large Ghana facility such as `Data Cloud DC` without primary evidence.
- `Digital Realty Accra` mentions from LINX or third-party sites: verify whether this means a current operating facility, a naming/partner error, or another operator-hosted access point before adding a separate record.
- Google Accra office, Google AI research centre, Google Global Cache, Cloudflare/Akamai nodes and other edge/CDN references.
- Equiano cable claims for Ghana.
- Telco exchanges described as `data centres` without commercial colocation service or facility-level source.
- Africa Data Centres 30 MW treated as fully operational before a commissioning/launch source.

## Final confidence notes

- **High confidence**: division model is 16 regions; Greater Accra is the commercial DC core; NITA has Accra and Kumasi Uptime records; no Ghana public cloud region appears on official hyperscaler pages; Equiano does not land in Ghana.
- **Medium confidence**: exact operational capacity for Onix/PAIX/Equinix without permit or operator technical sheet; ADC Accra current construction/commissioning state should be rechecked in each batch.
- **Low confidence**: directory-only facilities, unverified telco/private enterprise rooms, and any regional non-commercial server room outside Accra/Kumasi.
