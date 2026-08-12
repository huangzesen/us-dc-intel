# MV Explorer - Industry Angle: Maldives Datacenter Operators, Trade Press and Directory Verification

Date: 2026-08-12. Country: Maldives (MV). Complements `explorer-official.md`. Focus: operator/vendor discovery, trade-press leads, directory de-duplication, and locality queries for the 21 manifest divisions.

Reliability grades: **A** = operator/primary source, Uptime Institute list, public-sector official record, cable owner/consortium record. **B** = established trade/local press with named parties and dates. **C** = directory/marketplace/social-only/SEO lead that needs primary confirmation.

---

## 0. Market shape

- Maldives is a **small telecom-led datacenter market**, not a hyperscale market. The practical census starts with Dhiraagu, Ooredoo Maldives, MVIX, Maldives Digital Service/MINDCo, HDC/Maxcom, Focus Infocom/Raajje Online, and smaller IRSP/ISP operators.
- Confirmed public facility clusters: **Hulhumale / Male Atoll** (Dhiraagu Tier IV DC, OMDC, HDC co-location project/cable landings), **Male city** (MVIX, historical NCIT/MDS government DC lead, telco/ISP server rooms), and **N. Velidhoo / South Miladhunmadulu** (Dhiraagu third DC).
- Important watch locality: **Kulhudhuffushi / South Thiladhunmathi**. Ooredoo landed the PEACE cable there in 2024 and reporting links the landing to managed-services/hyperscaler opportunity, but no confirmed datacenter facility was found.
- Public capacity is sparse. Use Tier/certification, status, address, floor/rack disclosures, and connectivity as proxies. Keep `capacity_mw: null` unless MW is explicitly disclosed.
- Search both `data centre` and `data center`; Maldives operator/public-sector pages usually use English. Add island names because atoll labels are often ambiguous.

---

## 1. Operator and facility seed registry

This is a seed list, not a final census. Re-verify each row during enumeration.

| Seed | Locality assignment | Status / evidence | Best source path | Grade |
|---|---|---|---|---|
| Dhiraagu Hulhumale Data Center | Hulhumale / Male Atoll | Operational; Maldives' first/only Tier IV certified facility; Uptime list shows Dhivehi Raajjeyge Gulhun PLC, `Dhiraagu Hulhumale Data Center`, Malé, MV, TCDD/TCCF, TIV. | Uptime list https://uptimeinstitute.com/uptime-institute-awards/list ; Dhiraagu service page https://www.dhiraagu.com.mv/business/products-solutions/data-center-cloud-solution ; DCD/Telecompaper launch coverage. | A |
| Dhiraagu Data Center & Cloud / Cloud IaaS | Hulhumale primarily; check any Male/DR locations separately | Official service offering for colocation/cloud; page names Hulhumale facility and 99.995% uptime. | Dhiraagu official Data Center & Cloud page. | A |
| Dhiraagu Male data centre / legacy core DC | Male | Mentioned in trade summaries as an existing Dhiraagu DC before Hulhumale/Velidhoo; exact address and commercial availability need primary confirmation. | Search Dhiraagu site, annual reports, DCD/dcpulse; do not use directory-only evidence. | B/C |
| Dhiraagu N. Velidhoo data centre | Velidhoo / Noonu / **South Miladhunmadulu** | Third Dhiraagu DC, first in the atolls, launched Nov 2025; described as Tier III-level/ready in press/social/operator snippets. | Dhiraagu media/social, DCD `Dhiraagu launches third data center in Maldives`, MNN, Developing Telecoms. | A/B depending on source captured |
| Ooredoo Maldives Data Centre (OMDC) | Hulhumale / Male Atoll | Launched 2021; Tier-3-ready/Tier III standard; flood-resistant design reported; supports government, corporate and hospitality workloads. | Ooredoo pages, DCD https://www.datacenterdynamics.com/en/news/ooredoo-builds-data-center-in-hulhumal%C3%A9-maldives/ , Telecompaper, Corporate Maldives, Edition. | A/B |
| MVIX Maldives Internet Exchange | Male | Active IXP/peering facility. Official location: H. Bonthi 5th Floor, Hihfaseyha Goalhi, Male. PCH lists MVIX active, established 2022-09-28. | https://mvixp.org/ ; https://mvixp.org/about-us/location/ ; https://www.pch.net/ixp/details/2313 | A |
| NCIT / Maldives Digital Service government DC | Male | Historical government datacenter in NCIT building, built 2005; current operation/ownership must be resolved under MDS after NCIT abolition on 2026-01-15. | President's Office/MDS for institution; DCD 2021 for historical facility lead; MDS pages for current confirmation. | B until current official facility evidence |
| HDC / Maxcom co-location data centre | Hulhumale / Male Atoll | 2021 EOI/agreement lead for co-location DC supporting HDC GPON/open-access infrastructure; current operational status not confirmed in public primary facility pages. | HDC announcements/archive/Gazette; HDC and Maxcom social posts; business registry. | B/C unless HDC/Gazette page captured |
| Syntys Maldives 1 / Ooredoo directory listing | Male or Hulhumale ambiguous | DataCenterMap labels an Ooredoo/Syntys Maldives facility. Syntys is Ooredoo Group's DC platform in other MENA markets; no Syntys official Maldives page found. | DataCenterMap seed only; verify against Ooredoo/Syntys primary pages. | C |
| Focus Infocom / Raajje Online | Male and nationwide ISP context | CAM lists Focus Infocom as ISP licensee; no confirmed public DC/colo facility found. | CAM licence page, rol.net.mv, MVIX membership/peering context. | C for facility |
| SatLink / B-Net / TelNet / other IRSPs | Island-specific | CAM lists many IRSPs by island; likely access/retail infrastructure, not datacenters. | CAM licence page, operator sites. | C for facility unless physical DC page appears |
| Ooredoo PEACE cable / Kulhudhuffushi opportunity | Kulhudhuffushi / South Thiladhunmathi | Cable landing and managed-services/hyperscaler opportunity; no confirmed DC facility. | SubmarineNetworks PEACE landing page, Ooredoo/local press. | B lead, not a facility |
| Resort/private fiber endpoints | Ithaafushi, Maafushi, resorts | Private cable/connectivity to OMDC; not separate DCs. | Hotelier Maldives, Ooredoo/local press. | B lead, exclude from DC count |

---

## 2. Operator query recipes

Use exact operator + island pairs first, then broader Maldives terms.

```text
"Dhiraagu" "Hulhumale" "Tier IV" "data centre"
"Dhiraagu Hulhumale Data Center" "Uptime Institute"
site:dhiraagu.com.mv "data center" OR "data centre" OR "colocation" OR "cloud"
"Dhiraagu" "Velidhoo" "data centre" OR "Tier III"
"Dhiraagu" "Male" "data centre" OR "data center"
"Ooredoo Maldives Data Centre" OR "OMDC" "Hulhumale"
site:ooredoo.mv "data centre" OR "data center" OR "colocation" OR "PEACE Cable"
"Ooredoo" "Kulhudhuffushi" "data centre" OR "managed services" OR "hyperscaler"
"MVIX" "H. Bonthi" OR "Hihfaseyha" OR "Male"
"Maldives Digital Service" OR "NCIT" "data centre" "Male"
"HDC" "Maxcom Technologies" "Co-location Data Centre"
"Raajje Online" OR "Focus Infocom" "data centre" OR "hosting" OR "server"
"Syntys" "Maldives" "data center" OR "data centre"
```

Negative-control queries:
```text
"Maldives cloud region" AWS OR Azure OR Google OR Oracle
"underwater data centre" Maldives
"resort" "data centre" Maldives "server room"
"Syntys Maldives" site:syntys.com
"MMIX" Maldives
```

---

## 3. Trade press and secondary sources

Use trade press to discover, date and interpret leads, then upgrade/downgrade with primary evidence.

| Source | URL | Maldives use | Grade |
|---|---|---|---|
| Data Center Dynamics | https://www.datacenterdynamics.com/en/ | OMDC Hulhumale launch; Dhiraagu Hulhumale launch; Dhiraagu Velidhoo launch; DSCoM and SMW6 coverage; historical NCIT mention. | B |
| Telecompaper | https://www.telecompaper.com/ | Dhiraagu Tier IV launch; Ooredoo OMDC launch; CAM/ISP licence context. | B |
| Developing Telecoms | https://developingtelecoms.com/ | MSC landing and Dhiraagu/Ooredoo cable/facility summaries. | B |
| Edition / Mihaaru | https://edition.mv/ | Local business/telecom details, cable meetings, DC launches. | B |
| Raajje.mv | https://raajje.mv/ | Dhiraagu colocation/SMW6/Hulhumale lease stories. | B |
| PSM News | https://psmnews.mv/ | SMW6 landing-station lease and government/utility announcements. | B |
| Corporate Maldives | https://corporatemaldives.com/ | OMDC hospitality/cloud framing; local business announcements. | B |
| Adhadhu / Sun / Avas / Atoll Times / See.mv | respective sites | Local cable landing, utility, council and operator news; use to chase official pages. | B/C |
| SubmarineNetworks / SubTel Forum / CableStatus / TeleGeography | https://www.submarinenetworks.com/ ; https://subtelforum.com/ ; https://cablestatus.com/ | MSC, DSCoM, PEACE, IAX, SMW6 facts and landing points. | B unless owner announcement linked |
| PCH | https://www.pch.net/ixp/details/2313 | MVIX active status and establishment date. | B/A-support |
| DataCenterMap | https://www.datacentermap.com/maldives/ | Directory seed for Ooredoo/Syntys and Dhiraagu entries; not source-of-record. | C |
| Cloudscene / Datacenters.com / Baxtel | respective sites | Cross-check for hidden/duplicate facility names. | C |

Trade queries:
```text
site:datacenterdynamics.com/en/news/ Maldives "data center" OR "data centre"
site:telecompaper.com Maldives "data centre" OR "data center" Dhiraagu Ooredoo
site:developingtelecoms.com Maldives "data centre" OR "submarine cable"
site:edition.mv "data centre" Maldives OR Dhiraagu OR Ooredoo
site:raajje.mv Dhiraagu "data centre" OR "landing station"
site:psmnews.mv "SEA-ME-WE 6" Hulhumale Dhiraagu
site:corporatemaldives.com "Ooredoo Maldives Data Centre" OR OMDC
site:submarinenetworks.com Maldives Kulhudhuffushi OR Hulhumale OR Velidhoo
site:datacentermap.com/maldives/ Maldives "Syntys" OR "Dhiraagu"
```

---

## 4. Directory-to-primary workflow

1. Capture exact directory name, address, operator, coordinates, and claimed services.
2. Search exact name plus operator official domain.
3. Search address/plot plus `HDC`, `Maavehi`, `Gazette`, `ERA`, and the relevant island/city council.
4. Search Uptime Institute for exact facility/country/client if a Tier certification is claimed.
5. Search CAM for the operator/legal entity but keep that separate from facility existence.
6. If no primary/operator record appears, keep the row as Grade C and mark `facility_unverified: true`.

Directory examples:
```text
"Syntys Maldives 1" "Ooredoo"
"Kuredhimaa Hingun" "data centre" Maldives
"Lot 21563" "Dhunburigas Magu" Dhiraagu
"21563" "Hulhumale" "Dhiraagu" "data center"
"DataCenterMap" Maldives Dhiraagu Ooredoo Syntys
```

---

## 5. Locality search matrix

Run the high-yield rows first, then one-shot sweeps for low-yield divisions.

| Priority | Division/locality | Query anchors |
|---|---|---|
| 1 | Male Atoll / Hulhumale | `Hulhumale data centre`, `Dhiraagu Hulhumale Tier IV`, `OMDC Hulhumale`, `HDC co-location data centre`, `SMW6 landing station Hulhumale`, `MSC Hulhumale`, `IAX Hulhumale` |
| 1 | Male | `MVIX Bonthi Hihfaseyha`, `NCIT data centre Male 2005`, `Maldives Digital Service data centre`, `Dhiraagu Male data centre`, `Focus Infocom hosting Male` |
| 1 | South Miladhunmadulu / Noonu / Velidhoo | `Dhiraagu Velidhoo data centre`, `N. Velidhoo Tier III`, `Velidhoo Dhuvaafaru submarine cable`, `Fenaka Velidhoo generator` |
| 2 | South Thiladhunmathi / Kulhudhuffushi | `Ooredoo PEACE Cable Kulhudhuffushi data centre`, `Kulhudhuffushi managed services hyperscaler`, `Kulhudhuffushi council data centre` |
| 2 | South Ari / Dhangethi / Maamigili | `Dhangethi Maamigili submarine cable data`, `ADh data centre generator`, `Ooredoo Dhiraagu Dhangethi Maamigili` |
| 2 | South Nilandhe / Kudahuvadhoo | `Kudahuvadhoo submarine cable data centre`, `Dh. Kudahuvadhoo generator data` |
| 2 | Raa / Dhuvaafaru and Baa / Eydhafushi | `Dhuvaafaru Eydhafushi submarine cable`, `Raa Baa data centre`, `Fenaka Dhuvaafaru Eydhafushi generator` |
| 3 | Addu City | `Addu Hithadhoo data centre`, `Xpower Maldives Hithadhoo server`, `Addu City council ICT data centre` |
| 3 | Fuvammulah / Fuvahmulah | `Fuvahmulah data centre`, `Fuvammulah server room`, `Gnaviyani ICT hosting` |
| 3 | All other divisions | `{division} Maldives data centre`, `{capital island} server room`, `{atoll code} Dhiraagu Ooredoo data centre` |

Universal templates:
```text
"{division}" Maldives "data centre" OR "data center" OR datacentre
"{island}" Maldives "data centre" OR "server room" OR "server farm" OR colocation
"{island}" Dhiraagu OR Ooredoo "cloud" OR "hosting" OR "data"
"{island}" "submarine cable" OR "landing station"
"{island}" "generator" OR "UPS" OR "substation" "data"
site:{council-domain} "data centre" OR "server" OR "ICT"
```

---

## 6. Known leads to carry into enumeration

| Candidate | Count as facility? | Locality | Grade discipline |
|---|---|---|---|
| Dhiraagu Hulhumale Data Center | Yes | Male Atoll | A with Uptime + Dhiraagu. |
| Dhiraagu N. Velidhoo Data Centre | Yes if Dhiraagu/operator source captured | South Miladhunmadulu | A/B; ensure Noonu mapping. |
| OMDC Hulhumale | Yes | Male Atoll | A/B; distinguish Tier III standard/ready from certified. |
| MVIX | Count as IXP/colo/peering facility, not commercial wholesale DC | Male | A. |
| NCIT/MDS government DC | Count only with date-stamped current status or historical status flag | Male | B historical; A only if MDS confirms. |
| HDC/Maxcom co-location DC | Pipeline/watch unless operational evidence is found | Male Atoll | B/C. |
| Syntys Maldives 1 | No unless primary confirms | Male/Male Atoll ambiguous | C. |
| Kulhudhuffushi PEACE cable data-centre opportunity | No | South Thiladhunmathi | B lead; watch-list only. |
| Resort/private cable endpoints | No | Male Atoll/resort islands | B lead; not standalone DC. |

---

## 7. Capacity extraction

Search capacity proxies before leaving fields blank, but do not infer MW:

```text
"{facility}" "MW" OR "MVA" OR "kW"
"{facility}" rack OR racks OR sqm OR "m2" OR "square feet"
"{facility}" "Tier IV" OR "Tier III" OR "Uptime"
"{facility}" generator OR UPS OR "2N" OR "N+1"
"{facility}" investment OR USD OR MVR
```

Rules:
- Tier IV certification is a reliability/design/constructed-facility signal, not an IT-load figure.
- Cable capacity is a demand/connectivity signal, not DC capacity.
- Generator/UPS mentions support resiliency but do not define IT load.
- If a field is not public, write `capacity_mw: null` and put the proxy in notes.

---

END OF MV/explorer-industry.md
