# SN Explorer - Industry / Press / Vendor Discovery for Senegal Datacentres

Date: 2026-08-12. Scope: Senegal (SN) datacenter enumeration from industry media, local press, operator/vendor pages, cloud-region announcements, aggregators, and per-region search patterns. This file complements `explorer-official.md`; every press lead should be promoted only after operator, Uptime, commune, DEEC/DIREC, Senelec/CRSE, ARTP, APIX, or Senegal Numerique evidence is found.

Reliability grades:

- **A** = primary source for the specific claim: official operator page, official press release, Uptime record, government/regulator/utility/investment page, official cloud-provider region list.
- **B** = reputable industry or business press: DCD, DCmag, Connecting Africa, Developing Telecoms, Agence Ecofin, CIO Mag, RFI, Le Soleil/major local press, Africa50/project-finance pages, vendor case studies.
- **C** = lead-only source: DataCenterMap, Baxtel, Neocloud, SEO market pages, social posts, old MoUs, unclear local blogs, unlinked certification/capacity claims.

---

## 0. Senegal-specific industry frame

- Senegal has no complete public facility register. Practical discovery is a triangle: **operator/Uptime pages** for named facilities, **press/vendor pages** for project timing and capacities, and **official files** for permit/environment/power/regulatory confirmation.
- The current verified market is Dakar-heavy. Confirmed or strong leads are in Dakar department, Rufisque/Diamniadio, Almadies, Les Mamelles, Rufisque, Pikine/Technopole, and state/utility locations. Thies is a nearby watchlist; Kaolack is an unverified historical plan; the remaining regions are negative-search territory.
- Search in French first: `centre de donnees`, `datacenter`, `data center`, `salle de serveurs`, `hebergement`, `colocation`, `cloud souverain`, `souverainete numerique`, `Tier III`, `Uptime`, `MW`, `racks`, `baies`, `salles techniques`, `station d'atterrissage`, `cable sous-marin`, `Diamniadio`, `Rufisque`, `Almadies`, `Les Mamelles`, `Technopole`, `Orana`.
- Diamniadio is in Rufisque department, Dakar region. Do not put Diamniadio facilities in Thies because of airport-corridor wording.
- Edge/cloud caution: AWS Wavelength with Orange/Sonatel, Oracle/Orange planning stories, CDN PoPs, IXPs, cable landing stations, and sovereign-cloud websites are leads; they are not automatically standalone data centers.

---

## 1. High-value industry and press sources

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/?tag=senegal | Senegal DC trade coverage: PAIX Dakar, Onix Dakar, Tigo/Millicom, national DC, AWS Wavelength/Sonatel context. | **B** |
| DCmag | https://dcmag.fr/ | Francophone DC coverage, useful for PAIX/Onix/StellarIX. | **B** |
| Connecting Africa | https://www.connectingafrica.com/ | PAIX, Avanti/Free, telecom-infrastructure updates. | **B** |
| Developing Telecoms | https://developingtelecoms.com/ | PAIX Dakar, national DC, telecom projects. | **B** |
| Agence Ecofin | https://www.agenceecofin.com/ and English https://www.ecofinagency.com/ | Telecom/regulatory, Sonatel, cable and data-center context. | **B** |
| CIO Mag | https://cio-mag.com/ | Francophone IT policy and national DC coverage. | **B** |
| RFI / Financial Afrik / Dakaractu / Le Soleil / Le Quotidien | rfi.fr, financialafrik.com, dakaractu.com, lesoleil.sn, lequotidien.sn | National DC inauguration, government programs, local announcements. | **B/C** depending on detail and source links |
| Africa50 | https://www.africa50.com/our-funds/projects/ | Financing/strategic backing for PAIX/Africa digital infrastructure leads. | **B/A-** if a project page names Senegal |
| Operator press-release mirrors | Telecom Ramblings/APO, AXIAN, Avanti, Orange/Sonatel, PAIX | Use when the source is the operator and the page is stable; mirror is secondary but content may be operator-issued. | **A/B** |
| Uptime Institute | https://uptimeinstitute.com/uptime-institute-awards/country/id/SN | Certification/location verification for Sonatel, Senelec, Millicom/Tigo, Douanes. | **A** |
| Aggregators | DataCenterMap, Baxtel, Neocloud, datacenters.com, OCOLO | Lead index for facility names, geocodes, market counts. | **C** unless corroborated |
| Vendor/build suppliers | Schneider, Vertiv, Huawei, Siemon, BlueSun DC West Africa, local EPCs | Construction/equipment leads, often good for dates and scope but rarely enough alone. | **B/C** |

Press query templates:

```text
site:datacenterdynamics.com/en/news/ Senegal ("data center" OR "data centre" OR datacenter)
site:dcmag.fr Senegal (datacenter OR "centre de donnees" OR Dakar OR Diamniadio)
site:connectingafrica.com Senegal (datacenter OR "data center" OR Avanti OR PAIX OR Sonatel)
site:developingtelecoms.com Senegal (datacenter OR "data centre" OR "centre de donnees")
site:agenceecofin.com Senegal (datacenter OR "centre de donnees" OR Sonatel OR ARTP)
site:cio-mag.com Senegal (datacenter OR "centre de donnees" OR Diamniadio)
site:financialafrik.com Senegal datacenter Diamniadio
site:dakaractu.com "Datacenter national" Diamniadio
"PAIX Dakar" "data centre" Senegal
"Onix" Dakar "2Africa" "data centre"
"Tigo Senegal" Diamniadio "Tier III" datacenter
```

Status verbs to capture exactly:

- `announces`, `plans`, `MoU`, `will build`, `purchased land` = planned or early construction, usually **B/C**.
- `breaks ground`, `construction started`, `extension`, `phase` = pipeline/construction, **B** unless operator/government official.
- `inaugurated`, `operational`, `go-live`, `available`, current order/service page = operational signal; verify with operator/Uptime for **A**.
- `Tier III`, `Tier 3`, `certified` = verify against Uptime. Marketing claims stay A for marketing text but not A for certification unless Uptime confirms.

---

## 2. Operator/developer sweep and source grades

| Operator / developer | Primary/strong URL | Senegal locality/status signal | Grade and notes |
|---|---|---|---|
| **Sonatel / Orange Business Senegal** | https://www.orangebusiness.sn/digitaliser/datacenter ; Uptime https://uptimeinstitute.com/uptime-institute-awards/datacenter/data-center-sonatel-rufisque/984 | Rufisque, Dakar region. Orange page says Sonatel's datacenter is based at Rufisque; Uptime lists Data Center Sonatel Rufisque. | **A** for facility/location/certification record. Press mentions extra rooms/expansions should be separate dated facts. |
| **Senegal Numerique SA / ADIE** | https://senegalnumeriquesa.sn/fr/senegal-numerique-moteur-de-la-transformation-digitale-de-letat | Current page lists three operational datacenters: Orana, Technopole, Diamniadio; national cloud development. | **A** for operator claim. Use press for 2021 Diamniadio inauguration and capacity when official technical sheet is absent. |
| **Senelec** | Uptime https://uptimeinstitute.com/uptime-institute-awards/datacenter/senelec-datacenter-diamniadio-/1245 | Senelec Datacenter Diamniadio. | **A** Uptime record. Treat as a distinct utility/internal DC until linked otherwise. |
| **Direction Generale des Douanes** | Uptime https://uptimeinstitute.com/uptime-institute-awards/list/datacenter/douanes-bdm-datacenter-/1202 | Douanes, BdM Datacenter, Dakar. | **A** certification/location record; likely internal government/customs facility. |
| **Millicom/Tigo/SenConnect / Yas legacy** | Uptime https://uptimeinstitute.com/uptime-institute-awards/list/datacenter/tigo-senegal-dakar-dc-phase1a/767 ; DCD 2017 Tigo article | Uptime names Tigo Senegal, Dakar DC, Phase-1A; DCD reports a Diamniadio facility built by SenConnect for Tigo. | **A** for Uptime; **B** for DCD location narrative. Current Yas branding from aggregators remains **C** unless Yas/Free/ARTP/Uptime source confirms. |
| **Free Senegal** | AXIAN/Free release https://www.axian-telecom.com/2022/05/23/avanti-communications-and-free-in-senegal-sign-landmark-agreement-to-build-and-host-new-hylas-4-satellite-gateway-in-senegal/ | Free has a Tier III data centre facility in Diamniadio and hosts/builds Avanti gateway. | **A/B** operator-group press release. Verify exact facility name and Uptime/current owner. |
| **Avanti Communications** | https://www.avanti.space/news/avanti-secures-authorisation-for-hylas-4-satellite-gateway-in-senegal/ plus AXIAN/Free release | HYLAS 4 gateway station at/with Free in Diamniadio. | **A/B** for gateway authorization/tenant lead. Not a separate DC unless separate site evidence appears. |
| **Onix Data Centres Senegal** | https://onixdatacentres.com/2023/05/11/tier-3-facility-in-dakar-2023-completion/ ; contact https://onixdatacentres.com/o-home/senegal/contact-us/ | Almadies 2Africa Cable Landing Station, Dakar; Tier 3 carrier-neutral facility, expected Q4 2023 completion in older update. | **A** for operator location and facility claim. Recheck current service/status page before marking operational based only on 2023 target. |
| **PAIX Data Centres Dakar** | Operator-issued release mirror https://newswire.telecomramblings.com/2025/01/paix-data-centres-announces-the-construction-of-a-new-ultra-modern-data-centre-in-dakar-senegal/ ; DCD https://www.datacenterdynamics.com/en/news/paix-data-centres-breaks-ground-on-facility-in-dakar-senegal/ | Les Mamelles, Dakar; about 918-900 sqm usable/colo space, 1.2 MW IT load/critical power, 330 bays; first phase scheduled operational in 2026. | **B/A-** for source-issued announcement and trade press. Until PAIX posts go-live, status remains under construction/planned operational 2026. |
| **StellarIX Senegal** | https://www.stellar-ix.com/senegal/ ; brochure https://www.stellar-ix.com/wp-content/uploads/2026/05/BROCHURE%20STELLARIX%20SN.pdf | Diamniadio colocation/cloud; claims Tier III Design & Facility, PCI-DSS, ISO 27001. | **A** for operator service/location claim; certification details need Uptime lookup under parent/client entity before recording as A certification. |
| **Jokko / Dariss Consulting** | https://jokko.africa/ | Senegal sovereign cloud, hosted in a Tier III+ Dakar datacenter. | **A** for provider claim; **C/B** for unnamed facility/Tier III+ until the host DC and certification source are identified. |
| **MainOne / Equinix** | https://mainone.net/ and cable/Orange press | Dakar cable/PoP/office/branch presence. | **B lead**. No confirmed Equinix colocation DC in Senegal from official region pages. |
| **WIOCC/OADC** | https://www.wiocc.net/ and OADC official pages | No confirmed Senegal facility in current evidence. | Negative watchlist; recheck official announcements. |
| **Africa Data Centres (Cassava/ADC)** | https://www.africadatacentres.com/ | No confirmed Senegal facility in current evidence. | Negative watchlist. |
| **APIX unnamed project / Kaolack plan** | APIX PDF and 2021 local-government intent stories | APIX PDF describes an unnamed data-center project; Kaolack stories are old intent. | **A/B lead** for APIX project; **C** for Kaolack until current official proof. |
| **N+ONE Senegal SEO page / BlueSun DC West Africa** | https://nplusone.africa/senegal-datacenter/ ; https://bluesun-dc.com/en/locations/bluesun-dc-west-africa/ | Market-entry/construction-service leads, not facility proof. | **C lead** unless project/customer/site is named. |

Operator queries:

```text
"{operator}" Senegal (datacenter OR "data center" OR "data centre" OR "centre de donnees")
"{operator}" Dakar (colocation OR hebergement OR cloud OR racks OR baies OR MW)
"{operator}" Diamniadio (datacenter OR "centre de donnees" OR Tier III OR Uptime)
"{operator}" Senegal ("mise en service" OR inauguration OR "go live" OR operational OR construction)
"{operator}" Senegal (ARTP OR Senelec OR "autorisation de construire" OR EIES OR "installations classees")
site:uptimeinstitute.com/uptime-institute-awards "{operator}" Senegal
```

---

## 3. Cloud, edge, cable, and IXP handling

Official cloud-region pages show no Senegal public cloud region as of 2026-08-12:

- AWS regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/

Industry handling:

- AWS Wavelength with Orange/Sonatel in Senegal is an edge-zone/service lead, not an AWS region. If the physical host is implied to be Sonatel, record the Sonatel facility relationship only when AWS/Orange/Sonatel states it.
- Oracle/Orange West Africa cloud-region planning stories from 2021 are not operational Senegal-region evidence.
- Cable landing stations (ACE, MainOne, SAT-3, SHARE, 2Africa) are strong interconnection leads. Count a data center only when the landing station includes a colocation/data-center facility, as with Onix at the Almadies 2Africa landing station.
- SENIX/IXP and CDN nodes may be in data centers; they are not themselves data centers.

Queries:

```text
"AWS Wavelength" Senegal Orange Sonatel data center
"Oracle" Orange Senegal cloud region data center
"2Africa" Almadies Dakar Onix "data centre"
"ACE" "MainOne" "SAT-3" SHARE Dakar datacenter
"SENIX" Dakar datacenter OR "centre de donnees"
"cloud souverain" Senegal (Jokko OR StellarIX OR SENUM OR Sonatel)
```

---

## 4. Region-level industry enumeration method

Run four passes for each region:

1. Press/vendor pass: region + towns + French/English DC terms.
2. Operator pass: Sonatel, Free, Expresso, Senegal Numerique/SENUM/ADIE, Senelec, Onix, PAIX, StellarIX, Jokko, Yas/Tigo/Millicom, Avanti, MainOne, WIOCC/OADC, ADC.
3. Certification/aggregator pass: Uptime, DataCenterMap, Baxtel, Neocloud, datacenters.com, OCOLO.
4. Official pivot pass: urbanisme, DEEC/DIREC, Senelec/CRSE, ARTP, APIX, Senegal Numerique.

### 4.1 Exact 14-region strategy

| Region | Main localities | Industry strategy | Expected result |
|---|---|---|---|
| **Dakar** | Dakar Plateau/CBD, Almadies, Ouakam, Les Mamelles, Fann, Mermoz, Pikine, Technopole, Guediawaye, Keur Massar, Rufisque, Diamniadio, Bargny | Search each named facility/operator plus cable landing terms and Uptime. | Highest yield: Sonatel, Onix, PAIX, SENUM Diamniadio/Technopole, Senelec, Douanes, Tigo/Millicom/Yas, Free/Avanti, StellarIX, Jokko. |
| **Diourbel** | Diourbel, Touba, Mbacke | Add `Touba`, `Mbacke`, telecom exchange, `salle serveurs`, local government ICT. | Low; likely telecom rooms only. |
| **Fatick** | Fatick, Foundiougne, Sokone, Saloum | Add fisheries/admin ICT, local digital projects, Senelec/telecom. | Low. |
| **Kaffrine** | Kaffrine, Birkelane, Koungheul, Malem Hoddar | Add agropole/rural connectivity and operator infrastructure. | Low; watch satellite/telecom technical-room stories. |
| **Kaolack** | Kaolack city, Medina Baye, Nioro | Search `datacenter de Kaolack`, old national-DC plan, SENUM/APIX/ministry refresh. | Historical plan only unless current evidence appears. |
| **Kedougou** | Kedougou, Saraya, Salemata | Add mining/gold operators, `data room`, `salle serveurs`, EIES. | Low; require explicit compute/hosting function. |
| **Kolda** | Kolda, Velingara, Medina Yoro Foulah | Add Casamance ICT and administration/university terms. | Low. |
| **Louga** | Louga, Linguere, Kebemer, Dahra | Add agropole, rural connectivity, Sonatel/Free. | Low. |
| **Matam** | Matam, Ourossogui, Kanel, Ranerou, Ogo | Add border/rural coverage and satellite/technical-room terms. | Low; Ogo appears in connectivity context, not DC evidence by itself. |
| **Saint-Louis** | Saint-Louis, UGB/Gaston Berger, Richard Toll, Dagana, Podor | Add university, fisheries, research, administrative server-room terms. | Possible institutional server-room leads; grade carefully. |
| **Sedhiou** | Sedhiou, Bounkiling, Goudomp | Add Casamance digital services and administration terms. | Low. |
| **Tambacounda** | Tambacounda, Bakel, Goudiry, Koumpentoum | Add east-corridor, transit, Senelec/telecom infrastructure. | Low. |
| **Thies** | Thies, Mbour, Saly, Tivaouane, Diass, Ndiass, Blaise Diagne airport | Search airport/SEZ/industrial corridor and `zone economique`; distinguish from Diamniadio. | Watchlist only; no confirmed commercial DC in verified set. |
| **Ziguinchor** | Ziguinchor, Bignona, Oussouye | Add Casamance, university/admin ICT, SENUM regional service points. | Low; government/university rooms possible. |

Exact copy/paste seeds:

```text
Dakar Senegal (Onix OR PAIX OR Sonatel OR Free OR StellarIX OR Jokko OR SENUM OR Senelec OR Douanes OR Tigo OR Millicom) datacenter
Diourbel Senegal ("centre de donnees" OR datacenter OR "data center" OR "salle de serveurs")
Fatick Senegal ("centre de donnees" OR datacenter OR "data center" OR "salle de serveurs")
Kaffrine Senegal ("centre de donnees" OR datacenter OR "data center" OR "salle de serveurs")
Kaolack Senegal (datacenter OR "centre de donnees") (projet OR inauguration OR SENUM OR APIX)
Kedougou Senegal (mine OR or OR Saraya OR Salemata) (datacenter OR "salle de serveurs" OR "data room")
Kolda Senegal ("centre de donnees" OR datacenter OR "data center" OR "salle de serveurs")
Louga Senegal ("centre de donnees" OR datacenter OR "data center" OR "salle de serveurs")
Matam Senegal ("centre de donnees" OR datacenter OR "data center" OR "salle de serveurs" OR Ogo)
Saint-Louis Senegal (UGB OR "Gaston Berger" OR universite OR administration) (datacenter OR "salle de serveurs")
Sedhiou Senegal ("centre de donnees" OR datacenter OR "data center" OR "salle de serveurs")
Tambacounda Senegal ("centre de donnees" OR datacenter OR "data center" OR "salle de serveurs")
Thies Senegal (Diass OR Mbour OR Saly OR "Blaise Diagne" OR "zone economique") (datacenter OR "centre de donnees" OR "data center")
Ziguinchor Senegal (universite OR administration OR Casamance) (datacenter OR "salle de serveurs" OR "centre de donnees")
```

Universal region query block:

```text
"{region}" Senegal ("centre de donnees" OR datacenter OR "data center" OR "salle de serveurs" OR colocation OR hebergement OR "cloud souverain")
"{main town}" Senegal ("centre de donnees" OR datacenter OR "salle de serveurs")
"{region}" (Sonatel OR Free OR Expresso OR SENUM OR ADIE OR Senelec OR Onix OR PAIX OR StellarIX OR Jokko OR Tigo OR Yas) datacenter
site:datacenterdynamics.com/en/news/ Senegal "{region}"
site:dcmag.fr Senegal "{region}" datacenter
site:agenceecofin.com Senegal "{region}" "centre de donnees"
site:uptimeinstitute.com/uptime-institute-awards Senegal "{region}"
site:datacentermap.com/senegal "{region}"
```

---

## 5. Facility lead sheet for researchers

Use this as the first-pass lead list, then verify every open field with the official methodology file.

| Lead | Status to record now | Next verification |
|---|---|---|
| Sonatel Rufisque | Operational/certified facility; **A** location/certification via Orange/Uptime. | Expansion dates, exact rooms/PODs, power, Senelec connection. |
| Senegal Numerique Diamniadio | Operational state DC; **A** SENUM name plus **B** inauguration/capacity press. | Official technical sheet, EIES, Senelec power, whether private-sector hosting is active. |
| Senegal Numerique Orana | Official state-operator DC name; **A lead**. | Locality, function, whether true DC vs server room. |
| Senegal Numerique Technopole | Official state-operator DC name; **A lead**. | Confirm Technopole/Pikine site and function. |
| Senelec Datacenter Diamniadio | Uptime-certified facility; **A**. | Internal/utility function, relationship to SENUM if any, physical parcel. |
| Douanes BdM Datacenter | Uptime-certified Dakar facility; **A**. | Internal government/customs function, exact location, whether commercial services exist. |
| Millicom/Tigo/SenConnect / Yas lead | Uptime + DCD support legacy facility; **A/B**. | Current operator/brand (Yas/Free/other), exact Diamniadio/Dakar assignment, Uptime current record. |
| Free Senegal Diamniadio | Operator-group release supports Tier III DC; **A/B**. | Uptime/permit/current facility name and exact location. |
| Avanti gateway | Tenant/gateway hosted with Free; **A/B**. | Authorization document, separate civil works if any. |
| Onix Dakar | Operator page supports Almadies/2Africa facility; **A**. | Current operational go-live/Uptime status, capacity. |
| PAIX Dakar | Under construction/planned operational 2026; **B/A-**. | Current go-live, permits, EIES, Senelec connection, exact Route/parcel in Les Mamelles. |
| StellarIX Senegal | Operator claims Diamniadio colocation/cloud; **A** for service/location. | Uptime record under exact owner/client, physical facility relationship. |
| Jokko | Sovereign cloud hosted in Dakar; **A** for provider claim. | Identify host datacenter and certification source. |
| APIX unnamed project | Investment-promotion lead; **A/B**. | Operator, site, current status. |
| Kaolack planned DC | Historical intent only; **C**. | Current ministry/SENUM/APIX proof before recording. |

---

## 6. Common pitfalls

- Do not count cable landing stations, IXPs, CDNs, satellite gateways, telecom exchanges, or government server rooms as data centers unless the source names a hosting/colocation/compute facility or Uptime/operator page supports it.
- Do not let DataCenterMap/Baxtel/Neocloud create authoritative capacity, certification, or operator fields. They are useful for search seeds.
- Do not merge Dakar-region facilities because sources say `Diamniadio` or `near Dakar`; keep operator/site-specific records.
- Do not mark PAIX Dakar operational solely because first phase was scheduled for 2026; find a 2026 go-live/current services page first.
- Do not record a Senegal AWS/Azure/GCP/OCI public cloud region. Current official region lists do not support it.
- Treat `Tier III+` as marketing language unless Uptime has a matching record; Uptime records in Senegal currently expose specific named projects such as Sonatel Rufisque, Senelec Diamniadio, Tigo Dakar DC Phase-1A, and Douanes BdM.
