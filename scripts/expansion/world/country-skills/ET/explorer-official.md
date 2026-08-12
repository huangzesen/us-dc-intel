# ET Explorer Official - Ethiopia Datacenter Enumeration

Date: 2026-08-12. Country: **ET Ethiopia**. Division model for this repository: **13 manifest divisions**: Addis Ababa; Afar; Amara (Amhara); Benshangul-Gumaz (Benishangul-Gumuz); Dire Dawa; Gambela Peoples (Gambela); Harari People (Harari); Oromia; Sidama; Somali; Southern Nations, Nationalities and Peoples (legacy SNNPR bucket); Southwest Ethiopia Peoples; Tigrai (Tigray).

Administrative caution: Ethiopia's current official subnational structure has changed since the old SNNPR model. South West Ethiopia Peoples Region was created in 2021, and South Ethiopia and Central Ethiopia were split from SNNPR in 2023. This repo still asks for the 13 manifest divisions above, so keep SNNPR as the manifest bucket but search the newer names (`South Ethiopia`, `Central Ethiopia`, `Wolaita`, `Gamo`, `Gofa`, `Hadiya`, `Gurage`, etc.) when clearing that bucket.

Reliability grades:

- **A**: primary/official evidence for a named facility, permit, licence, registration, park allocation, power connection, PPA, operator location, or certification. Examples: ECA service/licence record; EIC investment/SEZ record; IPDC park page; EEP/EEU document; Addis Ababa or regional permit/land record; operator facility page; Uptime Institute certification record; official cloud-provider region list.
- **B**: strong secondary evidence from reputable trade/local press, vendor case studies, official-wire articles, or two mutually consistent independent press accounts. Use for lifecycle/capacity leads unless a primary source confirms the facility.
- **C**: weak lead only. Examples: aggregators, social posts, market-report snippets, MoUs, feasibility announcements, unnamed crypto-mining claims, or unsupported "cloud region" marketing.

## 0. Operating Facts

- Ethiopia has **no public national datacenter registry** and no comprehensive public planning-permit search. Enumeration must join multiple official routes: telecom/data-centre licence, investment permit, industrial park/SEZ allocation, power evidence, local construction/land records, and operator facility pages.
- **ECA now explicitly lists Data Center Service Provider License and Hosting Service Provider License categories** on its [services page](https://www.eca.et/services/). Treat this as the key official route for commercial data-centre/hosting operators.
- The main physical cluster is **Addis Ababa**, especially Ethio ICT Park / ICT Park on the south-east edge of the city. Verified high-value Addis seeds include Raxio Ethiopia, Wingu Africa, Redfox, Ethio telecom's Gola Sefer modular DC, Safaricom Ethiopia's Addis core DC, Dashen Bank's enterprise DC, local cloud services, and crypto-mining/data-mining facilities.
- Secondary searches should cover **Oromia** (Adama, Bishoftu, Burayu, Sebeta, Dukem, Modjo, Sululta, Holeta, Jimma), **Amhara** (Bahir Dar, Kombolcha, Debre Berhan, Gondar, Dessie), **Dire Dawa**, and **Sidama/Hawassa**. Other divisions are usually negative searches unless a telco edge, government/university, mining, or power-linked facility appears.
- Search both spellings: `data centre`, `data center`, `datacentre`. Also search `colocation`, `hosting`, `cloud`, `carrier-neutral`, `Tier III`, `Uptime`, `MW`, `MVA`, `racks`, `server room`, `modular data center`, `crypto mining`, `bitcoin mining`, `data mining`, `PPA`, `substation`, `ICT Park`, `industrial park`, and `SEZ`.
- Amharic secondary terms: `ዳታ ሴንተር`, `የውሂብ ማዕከል`, `የሰርቨር ክፍል`, `ኢሲቲ`, `ክላውድ`, `ግንባታ`, `ተመርቋል`, `ተጀምሯል`.
- No AWS, Azure, Google Cloud, or Oracle OCI public cloud region is listed for Ethiopia on official region/location pages checked for this methodology date. Recheck official provider pages before recording any hyperscaler Ethiopia facility.

## 1. Official Sources

### 1.1 Ethiopian Communications Authority (ECA)

Primary URL: https://www.eca.et/  
Services/licence categories: https://www.eca.et/services/

Use ECA first for commercial telecom, data-centre, hosting, IXP, VISP, and PDPP-related evidence. ECA's services page is real and lists Data Center Service Provider License and Hosting Service Provider License categories. Commercial colocation/cloud facilities should be joined to ECA where possible. ECA also matters for ADDIX and for Personal Data Protection Proclamation No. 1321/2024 controller/processor registration.

Queries:

```text
site:eca.et "Data Center Service Provider License"
site:eca.et "Hosting Service Provider License"
site:eca.et "data center" OR "data centre" Ethiopia
site:eca.et "{operator}" licence OR license
site:eca.et "internet exchange" OR ADDIX
"Ethiopian Communications Authority" "{operator}" "data center"
"Ethiopian Communications Authority" "data controller" "processor registration"
```

Grade: **A** when a licence, registration, directive, or ECA announcement names the operator or service. **B** when press quotes ECA but no underlying ECA record is public.

### 1.2 Ethiopian Investment Commission (EIC)

Primary URL: https://investethiopia.gov.et/  
Investment guide / SEZ context: https://investethiopia.gov.et/wp-content/uploads/2025/02/EIC%20Investment%20Guide%20Final%20Version22.pdf

Use EIC for investment permits, one-stop-shop records, investment incentives, and SEZ context. Datacenter projects may be described under ICT services, data processing, cloud/hosting, telecom infrastructure, or special economic zones. The public site is real, but searchable facility-level permit data is limited, so use EIC as a join source rather than the only discovery route.

Queries:

```text
site:investethiopia.gov.et "data center" OR "data centre"
site:investethiopia.gov.et "cloud" "ICT"
site:investethiopia.gov.et "special economic zone" "ICT"
site:investethiopia.gov.et "investment permit" "{operator}"
"Ethiopian Investment Commission" "{operator}" "data center"
"Ethiopian Investment Commission" "ICT Park" "data"
```

Grade: **A** for EIC records or PDFs naming the project/operator/location. **B** for press describing EIC permits without a public permit document.

### 1.3 Industrial Parks and SEZs

IPDC primary URL: https://www.ipdc.gov.et/  
IPDC parks route: https://www.ipdc.gov.et/service/parks/

IPDC's park list is real and includes high-value search anchors such as Bole Lemi, Kilinto, Adama, Hawassa, Dire Dawa, Kombolcha, Debre Birhan, Mekelle, Bahir-Dar, Jimma, and Semera. Use IPDC pages to place industrial parks in the correct manifest division and to verify whether a data-centre claim is inside an IPDC park/SEZ. IPDC park evidence is not enough by itself to infer a datacenter tenant.

Ministry of Innovation and Technology (MinT): https://mint.gov.et/  
Use MinT for Ethio ICT Park, Digital Ethiopia, government cloud, and innovation-park announcements. The current ministry site can change path behavior; if indexed pages fail, search the domain and government social/press releases, then corroborate with operator/ECA evidence.

Queries:

```text
site:ipdc.gov.et "data center" OR "data centre" OR "ICT"
site:ipdc.gov.et "Kilinto" "ICT" OR "data"
site:ipdc.gov.et "Bole Lemi" "{operator}"
site:ipdc.gov.et "Adama" "data" OR "ICT"
site:ipdc.gov.et "Dire Dawa" "ICT" OR "data"
site:mint.gov.et "ICT Park" "data center"
"Ethio ICT Park" "{operator}"
"ICT Park" Ethiopia "data center" "ECA"
```

Grade: **A** for IPDC/MinT records naming park allocation or facility. **B** for official-wire/press articles quoting ministers or park officials. **C** for tenant rumors.

### 1.4 Power and Utility Evidence

EEP primary URL: https://www.eep.com.et/  
EEU primary URL: https://eeu.gov.et/

Ethiopia's cheap hydropower and direct power sales make energy evidence critical, especially for large colocation, telecom, and crypto/data-mining facilities. Extract MW/MVA, voltage, substation, feeder, connection date, PPA customer, tariff/currency terms, and whether the site is an industrial-park or direct EEP customer.

Queries:

```text
site:eep.com.et "data center" OR "data centre" OR "data miner" OR "crypto"
site:eep.com.et "{operator}" "MW" OR "MVA"
site:eeu.gov.et "data center" OR "data centre" OR "{operator}"
"Ethiopian Electric Power" "data mining" Ethiopia MW
"Ethiopian Electric Power" "Phoenix Group" "80 MW"
"Ethiopian Electric Utility" "Wingu" "data center"
"{site}" Ethiopia "substation" "data center"
```

Grade: **A** for EEP/EEU source material. **B** for DCD/Capital/Monitor/Shega power reports with named operator, site, and MW. **C** for unnamed mining-capacity claims.

### 1.5 Government, Cybersecurity, and Local Permits

INSA primary URL: https://insa.gov.et/  
Addis Ababa city portal: https://www.addisababa.gov.et/

Use INSA for government cloud, cybersecurity infrastructure, national ID/Fayda infrastructure, and procurement hints. Physical government datacenter locations may be undisclosed; do not invent them from programme-level evidence.

Use Addis Ababa and regional/city administrations for building permits, land leases, land auctions, and construction-control notices. Public search is weak; combine web-indexed notices with operator and ECA/IPDC evidence.

Queries:

```text
site:insa.gov.et "data center" OR "data centre" OR cloud
site:addisababa.gov.et "data center" OR "data centre" OR "server"
"Addis Ababa" "Building Permit" "{operator}"
"{city}" Ethiopia "land lease" "ICT" OR "data center"
"{region}" "urban development" "{operator}" "permit"
"Fayda" Ethiopia "data center" OR "data centre"
```

Grade: **A** for official permits/procurement/agency pages. **B** for press describing official permit or procurement. Programme-level government cloud evidence is **A for programme existence**, not A for a named physical site unless the source gives a site.

## 2. Official/Primary Facility Seeds

Use these as starting points. Do not stop at the seed; join each to ECA, EIC/IPDC/MinT, power, local permit, or Uptime evidence where available.

| Facility / operator | Division and locality | Primary / strongest URL | What is verified | Grade guidance |
|---|---|---|---|---|
| Raxio Ethiopia ET1 | Addis Ababa, Ethio ICT Park | https://www.raxiogroup.com/data-centres/ethiopia/ | Raxio's official page states Ethiopia facility, up to 800 racks and 3 MW IT power. | **A** for operator/site existence and current marketed specs; use Uptime/ECA/IPDC for independent joins. |
| Wingu Africa Ethiopia | Addis Ababa, Ethio ICT Park | https://www.wingu.africa/ plus DCD article https://www.datacenterdynamics.com/en/news/winguafrica-inaugurates-ethiopia-data-center/ | Operator has Ethiopia facilities; DCD reports ICT Park site, 10 MW and 800 racks when fully operational. | **A** for operator country footprint; **B** for DCD-reported detailed capacity unless confirmed on an operator/cert page. |
| Ethio telecom modular DC | Addis Ababa, Gola Sefer | https://www.ethiotelecom.et/ethio-telecom-signs-an-agreement-to-lease-its-modern-modular-data-center-for-five-institutions/ and https://www.ethiotelecom.et/partnership-cloud-solutions/ | Official Ethio telecom page confirms modern modular DC leasing; official service pages confirm cloud/hosted services. | **A** for Ethio telecom DC/cloud services; use press/vendor articles for Gola Sefer/Huawei detail if the official launch page is unavailable. |
| Safaricom Ethiopia core DC | Addis Ababa; planned Adama and Dire Dawa leads | https://safaricom.et/ plus DCD https://www.datacenterdynamics.com/en/news/safaricom-to-deploy-pre-fab-data-center-in-ethiopia/ and Addis Fortune https://addisfortune.news/news-alert/safaricom-sets-up-100m-data-centre | Official operator site verifies Ethiopia operator; press reports Addis prefabricated DC and Adama/Dire Dawa expansion plans. | **B** for facility/capacity until Safaricom/ECA/power evidence is found. |
| Redfox modular DC | Addis Ababa, Ethio ICT Park | https://shega.co/news/diaspora-owned-it-firm-redfox-opens-first-modular-data-center-in-ict-park | Local tech press reports modular DC at ICT Park. | **B** unless ECA/MinT/operator evidence is located. |
| Dashen Bank enterprise DC | Addis Ababa | https://shega.co/news/dashen-bank-inaugurates-4-4m-tier-iii-ready-data-center | Local tech press reports bank-owned Tier-III-ready facility. | **B** unless bank annual report/procurement confirms. |
| ADDIX IXP / interconnection | Addis Ababa, Wingu-hosted lead | https://www.eca.et/ and press/IXP records | ECA regulates IXP category; ADDIX can identify active data-centre interconnection sites. | **A** only for ECA/IXP official records; **B/C** for directory-only locations. |
| Crypto/data-mining DCs | Addis Ababa / ICT Park and possible Oromia ring | EEP/ECA primary route; Phoenix press lead | Large power purchases and ECA statements indicate a real segment, but many operators/sites are unnamed. | **B** only when operator + site + MW are named by EEP/ECA/operator; otherwise **C**. |

## 3. Hyperscaler and Cloud Region Guardrails

Official region pages to recheck:

- AWS regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/

As of this methodology date, these official pages do **not** list Ethiopia as a public cloud region. Local cloud or sovereign-cloud services should be enumerated under their local operator or host facility, not as AWS/Azure/GCP/OCI infrastructure.

Queries:

```text
site:aws.amazon.com Ethiopia "region" "AWS"
site:learn.microsoft.com/en-us/azure Ethiopia "region"
site:cloud.google.com Ethiopia "region" "Google Cloud"
site:oracle.com/cloud Ethiopia "region" "Oracle"
"Ethio telecom" "cloud" "data center"
"Wingu Cloud Exchange" Ethiopia
"Cloud 251" Ethiopia "data center" OR "cloud"
```

## 4. Per-Division Official Strategy

Run four passes for every division: official/licence, industrial-park/SEZ, power/utility, and operator/local-permit. Record negative searches explicitly.

| Manifest division | Priority towns/sites | Official routes | Expected yield and cautions |
|---|---|---|---|
| Addis Ababa | Ethio ICT Park/Tulu Dimtu-Goro road, Kilinto, Bole Lemi, Gola Sefer, Bole/Airport Road, CMC, Summit/Lemi Kura, Kazanchis | ECA; EIC; MinT ICT Park; IPDC Kilinto/Bole Lemi; Addis Ababa permits; EEP/EEU; operator pages | **High**. Enumerate Raxio, Wingu, Redfox, Ethio telecom, Safaricom, Dashen, Cloud 251 host, ADDIX, and crypto/data-mining sites. |
| Afar | Semera, Logiya, Awash corridor | IPDC Semera; Afar investment/urban bureau; EEP transmission; EEU connections | **Negative/energy context**. Do not treat power corridor or Semera park as DC evidence without operator/site. |
| Amara (Amhara) | Bahir Dar, Gondar, Dessie, Kombolcha, Debre Berhan | IPDC Bahir-Dar/Kombolcha/Debre Birhan; Amhara investment/urban bureaus; EEP/EEU; universities | **Low**. Wingu Bahir Dar expansion is a press lead; parks are manufacturing-heavy unless tenant evidence appears. |
| Benshangul-Gumaz (Benishangul-Gumuz) | Assosa, GERD area | Regional bureau; EEP/GERD context; EEU | **Negative**. GERD is power-generation context, not a datacenter location by itself. |
| Dire Dawa | Dire Dawa city, Dire Dawa Industrial Park, airport/rail corridor | Dire Dawa administration; IPDC Dire Dawa; ECA; EEP/EEU; Safaricom joins | **Low**. Safaricom planned DC is a B lead; verify with operator/ECA/power records. |
| Gambela Peoples | Gambela town | Regional bureau; EEU; government/university procurement | **Negative**. Look for government edge/server-room only. |
| Harari People | Harar | Harari regional/city administration; EEU; university/government procurement | **Negative**. Search both Harari and Harar. |
| Oromia | Adama/Nazret, Bishoftu, Burayu, Sebeta, Dukem/Eastern Industry Zone, Modjo, Sululta, Holeta, Jimma | Oromia investment/urban bureaus; IPDC Adama/Jimma; EEP/EEU; ECA; Safaricom/Wingu joins | **Low-medium**. Best non-Addis target: planned Adama DCs, crypto/data-mining near Addis ring, industrial-zone edge sites. |
| Sidama | Hawassa, Hawassa Industrial Park | IPDC Hawassa; Sidama bureaus; Hawassa city; EEU; universities | **Low/negative**. Manufacturing park and university ICT leads only unless a named operator appears. |
| Somali | Jigjiga, Dire Dawa corridor edge | Somali regional bureau; EEU; university/government procurement | **Negative**. Search Jigjiga/Jijiga spelling variants. |
| Southern Nations, Nationalities and Peoples (legacy SNNPR) | Arba Minch, Wolaita Sodo, Dilla, Hosanna/Hosaena; also current South Ethiopia and Central Ethiopia region names | Regional/city administrations; EEU; universities; EIC | **Negative/minor**. Because this is a legacy manifest bucket, include searches for `South Ethiopia` and `Central Ethiopia` but file records under the repo's SNNPR bucket unless the manifest changes. |
| Southwest Ethiopia Peoples | Bonga, Mizan Teferi, Jimma corridor edge | SWEP regional bureau; EEU; universities/government procurement | **Negative**. New region; use `South West Ethiopia`, `Southwest Ethiopia Peoples`, `SWEPR`, `Kaffa`, `Bench Sheko`, `Dawro`, `West Omo`. |
| Tigrai (Tigray) | Mekelle, Adigrat, Axum, Shire | Tigray regional/city bureaus; IPDC Mekelle; EEP/EEU; university/government procurement | **Negative/low**. Conflict impacts make old leads stale; verify operational status carefully. |

## 5. Per-Division Query Templates

Use the manifest division plus towns. Keep parentheses and `OR` groups simple so they work in Google/Bing.

```text
"{division}" Ethiopia ("data center" OR "data centre" OR datacentre)
"{town}" Ethiopia ("data center" OR "data centre" OR "server room")
"{town}" Ethiopia ("colocation" OR hosting OR cloud OR "Tier III" OR Uptime)
"{town}" Ethiopia ("crypto mining" OR "bitcoin mining" OR "data mining") (MW OR MVA OR EEP)
"{industrial park}" Ethiopia ("data center" OR ICT OR cloud OR server)
"{operator}" "{town}" Ethiopia (data OR cloud OR colocation OR server OR mining)
site:eca.et "{operator}" OR "{town}" "data center"
site:ipdc.gov.et "{industrial park}" "{operator}" OR ICT
site:eep.com.et "{operator}" OR "{town}" MW OR MVA
site:eeu.gov.et "{operator}" OR "{town}" "data"
```

Specific high-yield official queries:

```text
"Ethio ICT Park" Ethiopia ("data center" OR "data centre" OR "crypto mining")
"Raxio" "Ethio ICT Park" "Ethiopia"
"Wingu" "Ethio ICT Park" "Ethiopia"
"Redfox" "ICT Park" "data center" Ethiopia
"Safaricom Ethiopia" "data centre" Addis Ababa
"Safaricom Ethiopia" Adama "data centre"
"Safaricom Ethiopia" "Dire Dawa" "data centre"
"Ethio telecom" "Gola Sefer" "data center"
"Ethiopian Electric Power" "data mining" Ethiopia
```

## 6. Extraction Fields

For each candidate, capture:

```text
division; city/town; sub-city/woreda; exact locality; parcel/lease number if available;
operator/SPV legal name; parent company; owner nationality; sector (colo/cloud/telco/government/crypto/enterprise);
source URL; source grade; source date; lifecycle stage;
floorspace; rack count; IT load MW; utility import MVA; voltage; substation/feeder;
PPA/connection terms; backup generation; fibre/carriers/IXP; ECA licence/registration;
EIC permit; IPDC/SEZ/ICT Park link; Uptime certification; notes and contradictions.
```

## 7. Confidence Rules

- Upgrade to **A** only when a primary source names the facility/operator and the relevant fact. Example: operator page for existence/capacity, ECA licence for service authorization, IPDC record for park location, EEP record for MW/PPA, Uptime record for certification.
- Keep **B** when the best evidence is DCD, Shega, Capital Ethiopia, Addis Fortune, ENA/FBC, Ethiopian Monitor, vendor case study, or press quoting officials.
- Keep **C** when the source is an aggregator, social post, market report, unnamed statement, or an announced plan with no site and no permit/power evidence.
- For crypto/data-mining, require **operator + site + MW** to exceed C. ECA/EEP/operator records can make it A; reputable press with all three fields is B.
- Do not count a cloud product as a physical datacenter unless the host facility or operator-owned DC is identified.
- Re-verify quarterly: ECA licence categories and lists, PDPP registration portal, IPDC park list, hyperscaler region pages, EEP/EEU PPA policy, Ethio ICT Park tenant announcements, and Safaricom/Wingu/Raxio expansion pages.
