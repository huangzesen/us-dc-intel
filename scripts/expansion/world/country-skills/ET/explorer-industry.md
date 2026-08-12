# ET Explorer Industry - Ethiopia Datacenter Discovery

Date: 2026-08-12. Scope: Ethiopia (ET) datacenter discovery from operator pages, trade press, local business/tech media, vendor case studies, cloud and IXP announcements, aggregators, crypto/data-mining coverage, and regional search patterns. Use this industry file to find leads; use `explorer-official.md` to verify them.

Reliability grades:

- **A**: primary/operator/official source. Examples: Raxio/Wingu/Ethio telecom/Safaricom page, ECA/EIC/IPDC/EEP/EEU record, Uptime certification, official cloud-region page.
- **B**: reputable press or vendor evidence. Examples: Data Center Dynamics, Shega, Capital Ethiopia, Addis Fortune, Ethiopian Monitor, The Reporter, ENA/FBC, Connecting Africa, Mobile Europe, CIO Africa, Huawei/Schneider/Vertiv case study.
- **C**: aggregator-only listing, social post, market-report snippet, MoU, feasibility note, unsited crypto-mining claim, or unsupported cloud-region claim.

## 0. Ethiopia-Specific Industry Frame

- Ethiopia's datacenter market is young and Addis-centric. There is no comprehensive public facility registry, so the practical workflow is lead discovery from press/operator pages followed by official joins: ECA licence, EIC investment permit, IPDC/ICT Park/SEZ record, EEP/EEU power evidence, local permit/land lease, or Uptime certification.
- The main commercial cluster is **Ethio ICT Park / ICT Park, Addis Ababa**, where Raxio, Wingu Africa, Redfox, and crypto/data-mining operators are repeatedly reported. Other Addis leads include Ethio telecom's Gola Sefer modular DC, Safaricom Ethiopia's Addis core DC, Dashen Bank's enterprise DC, local cloud services, ADDIX/IXP hosting, Kilinto, and Bole Lemi.
- Non-Addis leads are mostly pipeline or negative: Adama and Dire Dawa for Safaricom expansion; Bahir Dar and Adama for Wingu expansion leads; Oromia ring towns for crypto/data-mining and edge sites; Hawassa/Kombolcha/Debre Berhan/Mekelle/Dire Dawa industrial parks for negative or tenant sweeps.
- Search spelling variants: `data centre`, `data center`, `datacentre`; `Ethiopia`, `Ethiopian`; `Addis Ababa`, `Addis Abeba`; `Amara`, `Amhara`; `Benshangul-Gumaz`, `Benishangul-Gumuz`; `Tigrai`, `Tigray`; `Jigjiga`, `Jijiga`; `Debre Birhan`, `Debre Berhan`.
- Crypto/data-mining is material. Ethiopia Electric Power and ECA statements have made this a real datacenter segment, but many articles do not name the SPV, site, or MW. Keep unnamed mining facilities at C.
- Do not infer hyperscaler presence. AWS, Azure, Google Cloud, and OCI official region pages checked for this methodology date do not list an Ethiopia region.

## 1. High-Value Industry Sources

| Source | URL | Best use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Raxio launch, Wingu inauguration, Ethio telecom Huawei modular DC, Safaricom prefabricated DC, EEU/Wingu lease leads. | **B** unless linking to primary docs. |
| Shega | https://shega.co/ | Ethiopian tech/business reporting: ECA oversight shift, Redfox, Dashen Bank, Ethio telecom DC, cloud/data-centre market, crypto-mining. | **B**. |
| Capital Ethiopia | https://capitalethiopia.com/ | Wingu certification/launch, energy and mining-power context, macro/investment leads. | **B**. |
| Addis Fortune | https://addisfortune.news/ | Safaricom $100m DC and Adama/Dire Dawa expansion plan; telecom liberalisation and regulatory coverage. | **B**. |
| Ethiopian Monitor | https://ethiopianmonitor.com/ | EEP power sales to data miners, Raxio and investment news, energy/business context. | **B**. |
| The Reporter Ethiopia | https://www.thereporterethiopia.com/ | ICT Park, Wingu expansion, investment/industrial policy, permit and construction context. | **B**. |
| ENA | https://www.ena.et/ | Official wire for government, certification, ICT, and industrial-park announcements. | **A/B** depending on whether it directly quotes an official record. |
| Fana Broadcasting Corporate | https://www.fanamc.com/ | State-adjacent announcements, Ethio telecom launch coverage, IPDC/MinT/park news. | **B**, sometimes official-adjacent. |
| Connecting Africa | https://www.connectingafrica.com/ | Pan-African Raxio/Wingu/Safaricom datacenter stories. | **B**. |
| Mobile Europe / CIO Africa / TelcoTitans | https://www.mobileeurope.co.uk/ , https://cioafrica.co/ , https://www.telcotitans.com/ | Safaricom Ethiopia DC and telecom rollout details. | **B/C**, verify with Safaricom/ECA. |
| Aggregators | https://www.datacentermap.com/ethiopia/addis-ababa/ , https://baxtel.com/ , https://www.datacenters.com/ , https://www.ocolo.io/data-centers/ethiopia/ | Facility discovery and nearby-site clues. Never use alone for final grade. | **C**; **B-** only after corroboration. |
| IXP/interconnection indexes | https://www.peeringdb.com/ , https://www.internetexchangemap.com/ | ADDIX and carrier-neutral ecosystem clues. | **C/B**; verify with ECA/operator. |
| Vendor case studies | Huawei, Schneider Electric, Vertiv, Caterpillar, Cummins, Sterling & Wilson sites | Equipment delivery can prove buildout; use for Ethio telecom/Huawei-style cases. | **B/C** depending on specificity. |

Trade-press queries:

```text
site:datacenterdynamics.com/en/news/ Ethiopia "data center" OR "data centre"
site:shega.co Ethiopia "data center" OR "data centre" OR "data-center"
site:capitalethiopia.com Ethiopia "data center" OR "data centre" OR Wingu OR Raxio
site:addisfortune.news Safaricom "data centre" OR "data center"
site:ethiopianmonitor.com "data miner" OR "data mining" OR "data center"
site:thereporterethiopia.com "ICT Park" "data" OR Wingu OR Raxio
site:fanamc.com Ethiopia "data center" OR "modular data center"
site:ena.et Ethiopia "data center" OR "Tier III" OR Wingu
```

Capture lifecycle verbs exactly. `MoU`, `plans`, `targets`, `considering`, `feasibility`, and `seeks investors` are intent. `secured land`, `breaks ground`, `under construction`, `launched`, `inaugurated`, `operational`, `hosts`, `leased`, `certified`, and `PPA signed` are stronger but still need source grading.

## 2. Operator and Project Sweep

| Operator / project | URL / source route | Ethiopia signal | Grade and next joins |
|---|---|---|---|
| Raxio Ethiopia / Raxio Group | https://www.raxiogroup.com/data-centres/ethiopia/ | Addis Ababa, Ethio ICT Park; official page states up to 800 racks and 3 MW IT power. DCD reports Nov 2023 launch: https://www.datacenterdynamics.com/en/news/raxio-launches-data-center-in-addis-ababa-ethiopia/ | **A** for operator page facts; DCD **B** for launch narrative. Join to Uptime, ECA, IPDC/MinT, power. |
| Wingu Africa Ethiopia | https://www.wingu.africa/ ; DCD: https://www.datacenterdynamics.com/en/news/winguafrica-inaugurates-ethiopia-data-center/ | Addis Ababa, ICT Park; DCD reports 10 MW across 800 racks when fully operational and 15,000 sq m plot. | **A** for operator footprint; **B** for detailed capacity if only press/aggregator-backed. Join to Uptime, ECA, ADDIX, EEU tenant evidence. |
| Ethio telecom | https://www.ethiotelecom.et/ ; modular DC lease page: https://www.ethiotelecom.et/ethio-telecom-signs-an-agreement-to-lease-its-modern-modular-data-center-for-five-institutions/ ; cloud services: https://www.ethiotelecom.et/partnership-cloud-solutions/ | State telco operates data-centre/cloud/hosting services; Gola Sefer Huawei modular DC reported by DCD/Fana. | **A** for official service/DC leasing pages; **B** for Gola Sefer/Huawei/cabinet detail when sourced to press. |
| Safaricom Ethiopia | https://safaricom.et/ ; DCD: https://www.datacenterdynamics.com/en/news/safaricom-to-deploy-pre-fab-data-center-in-ethiopia/ ; Addis Fortune: https://addisfortune.news/news-alert/safaricom-sets-up-100m-data-centre | Addis core prefabricated DC reported in 2022; Adama and Dire Dawa planned as expansion sites. | **B** for facility details until official Safaricom/ECA/power records are found. |
| Redfox / Redfox Technologies | Shega: https://shega.co/news/diaspora-owned-it-firm-redfox-opens-first-modular-data-center-in-ict-park | Modular DC at ICT Park, Addis Ababa; DCaaS-style lead. | **B**. Join to ECA licence and MinT/ICT Park lease. |
| Dashen Bank | Shega: https://shega.co/news/dashen-bank-inaugurates-4-4m-tier-iii-ready-data-center | Enterprise/self-use Tier-III-ready DC, Addis Ababa. | **B**. Join to bank annual report, procurement, NBE continuity/DR obligations. |
| Cloud 251 | Zare Journal lead: https://zarejournal.com/cloud-251-takes-off-a-secure-cloud-future-for-ethiopian-businesses/ | Local cloud product launched in Ethiopia; host facility not always explicit. | **C/B** lead. Do not create a facility unless host/site is identified. |
| ADDIX / IXP ecosystem | ECA plus IXP/PeeringDB/operator routes | Interconnection points can identify active carrier-neutral datacenter hosts, especially Wingu. | **A** only for official ECA/operator record; directories **C/B-**. |
| Phoenix Group and other crypto/data-mining operators | Search EEP/ECA/operator/press | Phoenix 80 MW Ethiopia power-purchase lead; ECA/press reports multiple mining DCs at ICT Park. | **B** only if operator + site + MW are named; **C** if unnamed or site is broad. |
| INSA / government cloud | https://insa.gov.et/ | Government data infrastructure and cyber/cloud programmes. | **A** for programme/agency evidence, but do not infer undisclosed physical site. |

Operator queries:

```text
"Raxio" Ethiopia "ICT Park" "800 racks" "3MW"
"Wingu" Ethiopia "ICT Park" "10MW" "800 racks"
"Wingu" Ethiopia "ADDIX" OR "Internet Exchange"
"Ethio telecom" "Gola Sefer" "modular data center"
"Ethio telecom" "cloud" "data center"
"Safaricom Ethiopia" "data centre" "Adama" OR "Dire Dawa"
"Redfox" "ICT Park" "modular data center" Ethiopia
"Dashen Bank" "Tier III" "data center"
"Phoenix Group" Ethiopia "80 MW" "power purchase agreement"
```

## 3. Industry-to-Official Verification Pivots

For every press or aggregator lead, run these joins before final enumeration:

```text
site:eca.et "{operator}" "Data Center Service Provider License"
site:eca.et "{operator}" "Hosting Service Provider License"
site:investethiopia.gov.et "{operator}" "investment permit"
site:ipdc.gov.et "{operator}" OR "{park}" "data"
site:mint.gov.et "{operator}" OR "ICT Park"
site:eep.com.et "{operator}" MW OR MVA
site:eeu.gov.et "{operator}" "data center"
site:uptimeinstitute.com "{operator}" Ethiopia
"{operator}" "Ethiopian Communications Authority" licence
"{operator}" "Ethiopian Electric Power" MW Ethiopia
"{operator}" "Uptime Institute" Ethiopia
```

Official URLs to use as joins:

- ECA: https://www.eca.et/ and https://www.eca.et/services/
- EIC: https://investethiopia.gov.et/
- IPDC: https://www.ipdc.gov.et/ and https://www.ipdc.gov.et/service/parks/
- EEP: https://www.eep.com.et/
- EEU: https://eeu.gov.et/
- INSA: https://insa.gov.et/
- Addis Ababa city: https://www.addisababa.gov.et/
- Uptime awards/certification search route: https://uptimeinstitute.com/uptime-institute-awards/

## 4. Regional Search Playbook

Use each row as a checklist. Mark negative searches explicitly.

| Manifest division | Towns/sites | Industry strategy | Expected yield |
|---|---|---|---|
| Addis Ababa | ICT Park/Tulu Dimtu, Kilinto, Bole Lemi, Gola Sefer, Bole/Airport Road, CMC, Summit/Lemi Kura, Kazanchis | Run all operator names, `carrier-neutral`, `Tier III`, `cloud`, `IXP`, `crypto mining`, `data mining`, `MW`, `racks`, `substation`. Check aggregators only as lead indexes. | **High**: Raxio, Wingu, Redfox, Ethio telecom, Safaricom, Dashen, local cloud, ADDIX, crypto/data mining. |
| Afar | Semera, Logiya, Awash corridor | Search IPDC Semera and power/transmission/mining terms. | **Negative** unless mining/power customer appears. |
| Amara (Amhara) | Bahir Dar, Gondar, Dessie, Kombolcha, Debre Berhan | Search Wingu expansion, parks, universities, bank/government DCs, `server room`, `cloud`, `Tier III`. | **Low**; mostly planned/negative. |
| Benshangul-Gumaz | Assosa, GERD area | Search GERD only as power context; avoid false positives from electricity stories. | **Negative**. |
| Dire Dawa | Dire Dawa city, industrial park, rail/airport corridor | Search Safaricom, telco edge, industrial park ICT, `server room`, `data centre`. | **Low**; Safaricom planned DC lead. |
| Gambela Peoples | Gambela town | Search government, university, server-room procurement, regional cloud. | **Negative**. |
| Harari People | Harar, Harari | Search both `Harari` and `Harar`; university/government/telecom edge. | **Negative**. |
| Oromia | Adama/Nazret, Bishoftu/Debre Zeit, Burayu, Sebeta, Dukem, Modjo, Sululta, Holeta, Jimma | Search Safaricom Adama, Wingu Adama, crypto/data mining near Addis, industrial zones, power/PPA. | **Low-medium**; best non-Addis target. |
| Sidama | Hawassa, Hawassa Industrial Park | Search park tenants, university ICT, government edge, `server room`. | **Low/negative**. |
| Somali | Jigjiga/Jijiga | Search regional government, university ICT, telco edge, server room. | **Negative**. |
| Southern Nations, Nationalities and Peoples (legacy SNNPR) | Arba Minch, Wolaita Sodo, Dilla, Hosanna/Hosaena; also South Ethiopia and Central Ethiopia names | Search legacy and current region names. File results to the repo's SNNPR bucket unless the manifest changes. | **Negative/minor**. |
| Southwest Ethiopia Peoples | Bonga, Mizan Teferi, Tepi, Bench Sheko, Dawro, West Omo | Search new-region names plus government/university/server-room terms. | **Negative**. |
| Tigrai (Tigray) | Mekelle, Adigrat, Axum, Shire | Search Mekelle Industrial Park, universities, telecom edge, and conflict/status updates. | **Negative/low**; verify operational status. |

Reusable region queries:

```text
"{division}" Ethiopia ("data center" OR "data centre" OR datacentre)
"{town}" Ethiopia ("data center" OR "data centre" OR "server room")
"{town}" Ethiopia ("colocation" OR hosting OR "carrier-neutral" OR "Tier III" OR Uptime)
"{town}" Ethiopia ("cloud" OR "sovereign cloud" OR "local cloud")
"{town}" Ethiopia ("crypto mining" OR "bitcoin mining" OR "data mining") (MW OR EEP)
"{industrial park}" Ethiopia ("data center" OR ICT OR cloud OR server)
"{operator}" "{town}" Ethiopia ("data center" OR cloud OR server OR mining)
```

Amharic/local-language secondary queries:

```text
"{town}" "ዳታ ሴንተር"
"{town}" "የውሂብ ማዕከል"
"{town}" "የሰርቨር ክፍል"
"{town}" "ኢሲቲ" "ፓርክ"
site:fanamc.com "ዳታ ሴንተር" OR "የውሂብ ማዕከል"
site:ena.et "ዳታ ሴንተር" OR "የውሂብ ማዕከል"
```

## 5. Aggregator Handling

Aggregators are useful for finding misspelled names and nearby facilities, but do not trust capacity or operational status without corroboration.

Aggregator checks:

```text
site:datacentermap.com/ethiopia Addis Ababa Raxio OR Wingu OR Safaricom
site:baxtel.com "Ethiopia" "data center" Raxio OR Wingu
site:datacenters.com "Ethiopia" "Wingu" OR "Raxio"
site:ocolo.io "Ethiopia" "data centers"
site:peeringdb.com ADDIX Ethiopia
```

Rules:

- Aggregator-only facility: **C**.
- Aggregator plus matching operator page: use operator page as **A** for facts it states; keep aggregator-only fields at **C**.
- Aggregator plus reputable press: usually **B-** for existence only, unless capacity/site are independently confirmed.
- Treat nearby-facility claims as leads, not proof of exact campus boundary.

## 6. Hyperscaler Checks

Recheck official pages before every major refresh:

```text
site:aws.amazon.com/about-aws/global-infrastructure Ethiopia region
site:learn.microsoft.com/en-us/azure/reliability/regions-list Ethiopia
site:cloud.google.com/about/locations Ethiopia
site:oracle.com/cloud/public-cloud-regions Ethiopia
```

If official provider pages still do not list Ethiopia, record a negative hyperscaler check. Do not treat Cloud 251, Ethio telecom cloud, Wingu Cloud Exchange, or an AWS/Azure/GCP partner as a hyperscaler facility.

## 7. Final Evidence Rules

- Final facility records need at least one named operator/project, a physical division/city, a source URL, a lifecycle stage, and a grade.
- Do not promote a plan to operational without launch, lease, customer, energisation, certification, or operator-service evidence.
- For enterprise DCs, confirm the facility is more than a generic `server room` before counting it as a datacenter.
- For government cloud/INSA/Fayda, record programme evidence separately from physical-site evidence.
- For crypto/data-mining, require operator + site + MW for B; require EEP/ECA/operator evidence for A.
- Re-verify fast-moving items quarterly: Raxio/Wingu expansions, Safaricom Adama/Dire Dawa, ECA licensing/PDPP portal, IPDC SEZ status, EEP mining-power policy, and hyperscaler region pages.
