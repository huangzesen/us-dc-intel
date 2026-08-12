# MV Explorer - Official/Regulatory Angle: Maldives Datacenter Enumeration

Date: 2026-08-12. Country: Maldives (MV). Scope: the manifest's 21 Maldives divisions: Male, Addu City, and the historical/administrative atoll rows used by this dataset. Modern Maldives local government now also treats Fuvahmulah, Kulhudhuffushi and Thinadhoo as cities; for this manifest, keep them under `Fuvammulah`, `South Thiladhunmathi`, and `South Huvadhu Atoll` unless the manifest is updated.

Reliability grades: **A** = primary/official source (CAM licence/register, operator official page, Uptime Institute certification list, Maldives Digital Service/President's Office/MINDCo official page, HDC/council/gazette land or tender record, ERA EIA decision, STELCO/FENAKA/MEA official record, cable owner/consortium/operator announcement, official cloud-region page). **B** = reputable trade or local press with named parties and dates. **C** = directory, marketplace, SEO hoster page, social-only lead, or unverified aggregate.

---

## 0. Structural facts that control the search

- There is **no public Maldives datacenter register**. Enumeration has to join telecom licensing, operator pages, land/tender notices, environmental decisions, energy records, and cable-landings.
- The market is **telecom-led and very small**. Confirmed public-facing facility evidence clusters in **Male city**, **Hulhumale / Male Atoll (Kaafu)**, and **Velidhoo / South Miladhunmadulu (Noonu)**. No public MW capacity figures were found; use `capacity_mw: null` unless a primary source publishes load.
- **Critical manifest mapping correction**: `North Miladhunmadulu` = Shaviyani (Sh.); `South Miladhunmadulu` = Noonu (N.). Dhiraagu's N. Velidhoo datacenter is therefore `South Miladhunmadulu`, not `North Miladhunmadulu`.
- **Male vs Male Atoll**: `Male` is the city. `Male Atoll` is Kaafu and includes Hulhumale, Maafushi, Guraidhoo and other islands. Put Dhiraagu Hulhumale DC, OMDC, HDC co-location project, MSC/SMW6/IAX landings in `Male Atoll`; put MVIX, the historical government NCIT/MDS data centre, and any confirmed Male-city telco/server facilities in `Male`.
- **Institutional churn**: the President's Office established **Maldives Digital Service (MDS)** and abolished **NCIT** on 2026-01-15 under Presidential Directive No. 4/2026. Historical NCIT data-centre references must be resolved to MDS/current owner before a current operating claim is made. Source: https://presidency.gov.mv/Press/Article/36043 and https://www.mds.gov.mv/.
- **Environmental regulator**: the Environmental Regulatory Authority (ERA) now hosts environmental regulation/EIA channels at https://www.era.gov.mv/. Older EIA records and citations may still refer to EPA.
- **Connectivity is a location proxy, not facility proof**. Cable landings raise the priority of an island search but do not prove a datacenter unless a facility/operator record exists.

---

## 1. Grade-A source backbone

### 1.1 Communications Authority of Maldives (CAM)

- Main site: https://www.cam.gov.mv/
- Telecom Service Provider Licensees page: https://www.cam.gov.mv/splicence.htm
- Verified CAM signals: Dhiraagu and Ooredoo Maldives have Unified Telecommunications Licences; Focus Infocom and Starlink Services Maldives have ISP licences; WARF Telecom International and Ocean Connect Maldives have international submarine optical-fibre licences; HDC has a telecommunication infrastructure licence for Hulhumale. CAM's page was last updated 2024-10-16.
- Use CAM to define the licensed operator universe. Do **not** treat a licence as a physical datacenter record.

Queries:
```text
site:cam.gov.mv "Telecom Service Provider Licensees" Maldives
site:cam.gov.mv "Dhiraagu" "Ooredoo Maldives" "Focus Infocom"
site:cam.gov.mv "Internet Retail Service Provider Licence" "Velidhoo" OR "Maafushi" OR "Kudahuvadhoo"
site:cam.gov.mv "Telecommunication Infrastructure Licence" "Housing Development Corporation"
```

Extraction fields: licensee legal name, licence class, island/group coverage, date updated, and whether the record supports only entity/operator existence or a physical facility.

### 1.2 Government digital infrastructure: MDS / NCIT / MINDCo

- President's Office MDS establishment: https://presidency.gov.mv/Press/Article/36043
- Maldives Digital Service: https://www.mds.gov.mv/
- DMADD stakeholder page: https://dmadd.gov.mv/en/stakeholders
- MINDCo: https://www.mindco.mv/

Known official-grade lead:
- A historical government datacenter was reported in the NCIT building in Male, built in 2005 to host e-government workloads. Current ownership/operation must be checked through MDS because NCIT no longer exists after 2026-01-15.

Queries:
```text
site:mds.gov.mv "data centre" OR "data center" OR "hosting" OR "infrastructure"
site:presidency.gov.mv "Maldives Digital Service" "NCIT" "Directive No. 4/2026"
site:dmadd.gov.mv "Maldives Digital Service" "National Centre for Information Technology"
site:mindco.mv "data centre" OR "cloud" OR "hosting" OR "digital infrastructure"
"NCIT" "Male" "data centre" "2005" Maldives
"Maldives 2.0" "data centre" OR "data infrastructure" OR "National Data Exchange"
```

Grade rule: MDS/President's Office/MINDCo pages are A for institution and programme ownership; a trade article about the 2005 NCIT facility is B until a current MDS/official facility page confirms live status.

### 1.3 Planning, land and procurement

- HDC main site: https://www.hdc.mv/ and announcements: https://www.hdc.mv/announcements
- HDC old announcements archive: https://oldweb.hdc.mv/announcements/
- HDC bid portal: https://bids.hdc.mv/
- Government Gazette: https://www.gazette.gov.mv/
- Male City Council: https://malecity.gov.mv/
- Maavehi e-permit portal: https://maavehi.gov.mv/
- Local Government Authority councils directory: https://www.lga.gov.mv/en/councils
- Finance tenders: https://www.finance.gov.mv/tenders/
- Business Registry: https://business.egov.mv/

Known Grade-A/B leads:
- HDC issued an EOI for **Development of Co-Location Data Centre in Hulhumale** in 2021; HDC social/announcement search snippets preserve the title, but the current HDC page is JavaScript/ID-based and should be re-opened through the HDC announcements archive or Gazette before final facility entry.
- HDC and Maxcom Technologies signed an agreement for development of a co-location data centre to support GPON/open-access infrastructure in Hulhumale. Current operating status needs HDC/Maxcom/operator confirmation; keep as pipeline/watch-list if no facility page is found.

Queries:
```text
site:hdc.mv/announcements "data centre" OR "data center" OR "co-location" OR "colocation"
site:oldweb.hdc.mv/announcements "data centre" OR "co-location" "Hulhumale"
site:gazette.gov.mv "data centre" OR "data center" OR "co-location" OR "colocation"
site:bids.hdc.mv "data centre" OR "colocation" OR "digitalization"
site:maavehi.gov.mv "data centre" OR "server" OR "generator"
site:malecity.gov.mv "data centre" OR "server room" OR "building permit"
"HDC" "Maxcom Technologies" "Co-location Data Centre"
"HDC" "Development of Co-Location Data Centre" "Hulhumale"
"{island council}" "data centre" OR "server room" OR "generator"
```

Extraction fields: applicant/SPV, plot/lot, island, council/HDC authority, announcement number, tender/lease status, land-use class, floor area, generator/fuel conditions, EIA reference, current status.

### 1.4 Environmental and energy

- ERA: https://www.era.gov.mv/ and downloads: https://www.era.gov.mv/downloads.html
- STELCO: https://stelco.com.mv/
- FENAKA: https://fenaka.mv/
- Maldives Energy Authority / energy ministry pages: verify current URL during sweep.

Datacenters are likely to appear in environmental/power records through diesel generators, fuel storage, substations, cooling plant, cable landing stations, coastal works, or reclaimed-land development, not always through the phrase `data centre`.

Queries:
```text
site:era.gov.mv "data centre" OR "data center" OR "server farm" OR "generator" OR "fuel storage"
site:epa.gov.mv "data centre" OR "data center" OR "server farm" OR "generator"
"EIA" "Maldives" "data centre" OR "colocation" OR "landing station"
site:stelco.com.mv "data centre" OR "substation" OR "MVA" OR "bulk supply" OR "Hulhumale"
site:fenaka.mv "data centre" OR "generator" OR "Velidhoo" OR "Kulhudhuffushi"
"Maldives Energy Authority" "data centre" OR "captive" OR "generator"
```

Grade rule: ERA/STELCO/FENAKA records are A for the project element they document. A generator permit or substation notice is supporting evidence only; it is not a datacenter existence claim unless tied to a named datacenter project.

### 1.5 Connectivity official/primary sources

| Asset | Primary / strong source | Locality impact | Use |
|---|---|---|---|
| Dhiraagu Hulhumale Data Center certification | Uptime Institute awards list: https://uptimeinstitute.com/uptime-institute-awards/list | Male Atoll / Hulhumale | A for Tier IV TCDD/TCCF certification of `Dhiraagu Hulhumale Data Center` by Dhivehi Raajjeyge Gulhun PLC. |
| Dhiraagu Data Center & Cloud | https://www.dhiraagu.com.mv/business/products-solutions/data-center-cloud-solution | Male Atoll / Hulhumale | A for marketed cloud/colo service and Tier IV claim; use Uptime list to independently verify certification. |
| MVIX | https://mvixp.org/ and https://mvixp.org/about-us/location/ | Male | A for active IXP/data-center room at H. Bonthi 5th Floor, Hihfaseyha Goalhi, Male. |
| Maldives-Sri Lanka Cable (MSC) | Dhiraagu announcement: https://www.dhiraagu.com.mv/about-us/investor-relations/announcements-disclosures/dhiraagu-has-joined-a-multi-party-agreement-to-connect-the-maldives-to-sri-lanka-through-a-second-fiber-optic-submarine-cable ; Dialog announcement: https://dialog.lk/news/dialog-axiata-connects-srilanka-and-maldives-with-high-speed-submarine-cable ; SubmarineNetworks MSC: https://www.submarinenetworks.com/en/systems/intra-asia/msc | Hulhumale | A/B for 840 km, four-fiber-pair system with Dhiraagu, Ooredoo Maldives and Dialog; cable landing is not DC proof. |
| Domestic Submarine Cable expansion | Dhiraagu official: https://www.dhiraagu.com.mv/about-us/investor-relations/announcements-disclosures/domestic-submarine-cable-system-expansion-project | Hulhumale, Maafushi, Dhangethi, Maamigili, Velidhoo, Dhuvaafaru, Eydhafushi | A for node-points in the 2022 expansion announcement. |
| SEA-ME-WE 6 | Dhiraagu/PSM/DCD/submarine-cable sources; PSM: https://psmnews.mv/en/107112 | Hulhumale | B/A depending on source; Dhiraagu is Maldives landing partner. |
| PEACE cable | Ooredoo/SubmarineNetworks: https://www.submarinenetworks.com/en/systems/asia-europe-africa/peace/ooredoo-maldives-lands-peace-cable-in-kulhudhuffushi-city | Kulhudhuffushi / South Thiladhunmathi | B for landing and managed-services/hyperscaler opportunity; do not count a DC until an operator/facility record appears. |
| Ooredoo private resort cable | Ooredoo/local hospitality press | Ithaafushi/Maafushi to OMDC Hulhumale | B; resort connectivity use-case, not separate DC. |

### 1.6 Hyperscaler absence check

Use official region lists to confirm absence of an MV public cloud region. Re-check quarterly and before publication:

```text
AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
Azure: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies
Google Cloud: https://cloud.google.com/about/locations
Oracle OCI: https://www.oracle.com/cloud/public-cloud-regions/
Alibaba Cloud: https://www.alibabacloud.com/global-locations
Huawei Cloud: https://www.huaweicloud.com/intl/en-us/about/global-locations/
```

As of this pass, no AWS/Azure/GCP/OCI public cloud region in Maldives was found. Treat local `cloud`, VPS and hosting offers as reseller/local-telco services unless a hyperscaler official page says otherwise.

---

## 2. Division coverage matrix

Every run must produce a searched/not-searched note for all 21 manifest divisions. Use the atoll code and anchor islands below for locality assignment.

| Manifest division | Code / modern local unit | Anchor islands / localities | DC yield and required checks |
|---|---|---|---|
| Male | Male City | Male, Henveiru/Maafannu/Galolhu/Machchangolhi, Villingili | **High**: MVIX (A), historical NCIT/MDS government DC lead (B until current A), Dhiraagu/Focus/Raajje/SatLink server-room leads. Search Maavehi/Male Council/MDS/MVIX. |
| Male Atoll | Kaafu (K.); Male Atholhu | Hulhumale, Maafushi, Guraidhoo, Thulusdhoo, Himmafushi, Kaashidhoo | **Highest**: Dhiraagu Hulhumale Tier IV DC (A), OMDC Hulhumale (A/B), HDC/Maxcom co-location project, MSC/SMW6/IAX/DSCoM landings. Search HDC, CAM, Dhiraagu, Ooredoo, ERA. |
| North Thiladhunmathi | Haa Alif (HA) | Dhidhdhoo, Uligam | Low: telecom retail/server-room only unless CAM/FENAKA/council record appears. |
| South Thiladhunmathi | Haa Dhaalu (HDh); includes Kulhudhuffushi City in modern administration | Kulhudhuffushi, Nolhivaramfaru, Kurinbi | Medium watch: PEACE cable landed at Kulhudhuffushi in 2024 and reporting mentions future data-centre/managed-service opportunities. No confirmed DC; search Ooredoo, council, ERA, FENAKA. |
| North Miladhunmadulu | Shaviyani (Sh.) | Funadhoo, Komandoo, Maroshi | Low: do not assign Noonu/Velidhoo here. Search CAM IRSP and island councils. |
| South Miladhunmadulu | Noonu (N.) | Velidhoo, Manadhoo, Maafaru | **High**: Dhiraagu third datacenter in N. Velidhoo (A/B), DSCoM Velidhoo node. Search Dhiraagu, CAM, Fenaka, council. |
| North Maalhosmadulu | Raa (R.) | Dhuvaafaru, Ungoofaaru | Low-medium: DSCoM Dhuvaafaru node; CAM retail ISPs. No confirmed DC. |
| South Maalhosmadulu | Baa (B.) | Eydhafushi, Dharavandhoo, Hithaadhoo | Low-medium: DSCoM Eydhafushi node; CAM retail ISPs. No confirmed DC. |
| Faadhippolhu | Lhaviyani (Lh.) | Naifaru, Kurendhoo | Low: CAM retail ISPs and resort/server-room noise. |
| North Ari Atoll | Alif Alif (AA) | Rasdhoo, Ukulhas, Himandhoo | Low: CAM retail ISPs; no known DC. |
| South Ari Atoll | Alif Dhaalu (ADh) | Mahibadhoo, Dhangethi, Maamigili | Low-medium: DSCoM Dhangethi-Maamigili segment; search cable/generator records. |
| Felidhu Atoll | Vaavu (V.) | Felidhoo | Low: one-shot official/operator sweep. |
| Mulaku Atoll | Meemu (M.) | Muli | Low: one-shot official/operator sweep. |
| North Nilandhe Atoll | Faafu (F.) | Nilandhoo | Low: one-shot official/operator sweep. |
| South Nilandhe Atoll | Dhaalu (Dh.) | Kudahuvadhoo | Low-medium: DSCoM/CAM retail connectivity; no confirmed DC. |
| Kolhumadulu | Thaa (Th.) | Veymandoo | Low: CAM retail ISP entries; no confirmed DC. |
| Hahdhunmathi | Laamu (L.) | Fonadhoo, Gan | Low: CAM retail ISP entries; no confirmed DC. |
| North Huvadhu Atoll | Gaafu Alif (GA) | Villingili | Low: one-shot official/operator sweep. |
| South Huvadhu Atoll | Gaafu Dhaalu (GDh); includes Thinadhoo City in modern administration | Thinadhoo | Low: city/telecom server-room search; no confirmed DC. |
| Fuvammulah | Gnaviyani (Gn.); Fuvahmulah City | Fuvahmulah | Low: spell both `Fuvammulah` and `Fuvahmulah`; no confirmed DC. |
| Addu City | Seenu (S.) | Hithadhoo, Maradhoo, Feydhoo, Gan | Low-medium watch: city status, southern redundancy potential, CAM Xpower island coverage; no confirmed DC. |

---

## 3. Official enumeration workflow

1. Start with CAM licensees and define the operator universe: Dhiraagu, Ooredoo Maldives, Focus Infocom/Raajje Online, Starlink Services Maldives, WARF, OCM, HDC telecom infrastructure, IRSP licensees by island.
2. Run the facility search against official/operator domains: Dhiraagu, Ooredoo, MVIX, MDS, MINDCo, HDC, Gazette, Maavehi, Male City Council, ERA, STELCO/FENAKA.
3. Assign locality by island first, then atoll/manifest division. Do not rely on directory city labels.
4. Use Uptime Institute and operator pages for Tier claims. Distinguish `Tier IV certified` (Dhiraagu Hulhumale, A) from `Tier III ready/standard` marketing or trade claims (OMDC/Velidhoo until independently certified).
5. Use cable records to prioritize islands: Hulhumale, Maafushi, Dhangethi, Maamigili, Velidhoo, Dhuvaafaru, Eydhafushi, Kudahuvadhoo, Kulhudhuffushi. Promote only when a separate facility record exists.
6. For each candidate, capture: name, operator/legal entity, island, manifest division, address/plot if public, status, source URLs, reliability grade, capacity_mw, capacity proxy, evidence notes, and unresolved questions.

---

## 4. Reliability and pitfalls

- Grade A facility examples: Uptime Institute entry for Dhiraagu Hulhumale Data Center; Dhiraagu official Data Center & Cloud page; MVIX official location page; CAM licence page for operator identity; President's Office/MDS pages for NCIT-to-MDS succession.
- Grade B examples: Data Center Dynamics, Telecompaper, Developing Telecoms, Edition/Mihaaru, Raajje.mv, PSM News, Corporate Maldives, Adhadhu, Sun, Atoll Times, SubTel Forum/SubmarineNetworks where they summarize operator announcements.
- Grade C examples: DataCenterMap/Cloudscene/Baxtel/datacenters.com without primary corroboration; generic VPS/hosting pages; Facebook/social-only posts unless they are the only mirror of an official HDC/operator notice and are explicitly marked as social evidence.

Common traps:
- Do not put N. Velidhoo under `North Miladhunmadulu`; it belongs to Noonu / `South Miladhunmadulu` in this manifest.
- Do not count Kulhudhuffushi PEACE cable as a datacenter. It is a high-priority pipeline/watch locality only.
- Do not count resort server rooms or private resort fiber endpoints as datacenters.
- Do not merge OMDC Hulhumale with the directory-only `Syntys Maldives 1` entry unless Ooredoo/Syntys confirms the same facility/address.
- Do not infer MW from Tier level, cable capacity, generator presence, or flood-resilience claims.

---

END OF MV/explorer-official.md
