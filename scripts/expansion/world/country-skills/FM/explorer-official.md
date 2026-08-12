# FM Explorer Official - Federated States of Micronesia Datacenter Methodology

Date verified: 2026-08-12

Scope: Federated States of Micronesia (FM/FSM). The required state coverage from `world-manifest.jsonl` is complete: Kosrae, Pohnpei, Chuuk, Yap.

Use this file for the official/regulatory pass: TRA, FSM national/state government, FSMTC, FSMTCC/CableCorp/OAE, World Bank, donor-government records, US/FCC records, cloud-provider official region lists, and utility records.

## Bottom Line

No official source verified a live commercial colocation or hyperscale data center in FSM. Enumerate FSM as a very small telecom and government-digital-infrastructure market. The highest-confidence facility universe is:

- Grade A operational telecom facilities: FSMTC international gateway/cable-landing facilities in Pohnpei; FSMTCC/CableCorp submarine cable and FTTP exchange/central-office facilities serving Pohnpei, Chuuk, Yap, and Kosrae; iBoom/Boom network facilities in Yap; CPUC/iSolutions communications facilities in Chuuk where licensed.
- Grade A planned or programmatic data-center leads: Digital FSM's "Secure Government Network and Data Center, Disaster Recovery/Business Continuity and Government Cloud (FSM-Cloud)" component; World Bank P170718 status/results material tracks "New digital services hosted on private sector operated green data centers" with a target of 3 by March 2027.
- Grade A planned/wholesale colocation lead: CableCorp/OAE open-access fiber products include colocation space, power, cooling, and ancillary colocation for retail service providers. Treat this as telecom exchange/PoP colocation unless a later source confirms a standalone data center.
- Grade A absence: official AWS, Azure, Google Cloud, and OCI region lists show no FM cloud region/local region.

Do not count Starlink, Kacific, VSAT terminals, mobile base stations, FTTP rollout, or retail internet service as data centers. Count only dedicated data-center, colocation, landing-station, gateway, central-office, or government-cloud/server-infrastructure evidence, and label telecom facilities separately from data centers.

## Reliability Grades

- Grade A: TRA official pages/registers/determinations; FSM national/state government pages and project documents; FSMTC official pages; FSMTCC/CableCorp official pages and PDFs; World Bank project documents; FCC/US government records; official cloud-provider region pages; state utility official records.
- Grade B: donor/project/trade sources with named parties and dates, including AIFFP, East Micronesia Cable project site, NEC announcements, Submarine Networks, Data Center Dynamics, RNZ Pacific, Pacific Island Times, APNIC.
- Grade C: directories, social media unless it is the operator's own page, LinkedIn, reseller/hosting lists, forums, marketing pages, and inference from enterprise IT job posts.

Apply grades to the specific claim, not the domain. Example: a FSMTCC PDF confirming central-office colocation is Grade A for an OAE telecom-colocation offering, but it is not Grade A proof of an operational commercial data center.

## Verified Official Sources

### TRA - Telecommunication Regulation Authority

- Main site: https://tra.fm/
- Market Entry and Information: https://tra.fm/market-entry-and-information-2/
- Public Register of Licences: https://tra.fm/public-register-of-licences/
- TRA Act: https://tra.fm/tra-act/
- Bottleneck facilities determination: https://tra.fm/wp-content/uploads/2022/05/TRA-Determination-on-Bottleneck-Facilities-Final.pdf
- Licensing guide: https://tra.fm/wp-content/uploads/2023/09/Regulations-and-Licensing-Guide-1.pdf
- National Table of Frequency Allocation: https://tra.fm/wp-content/uploads/2023/10/National-Table-of-Frequency-Allocation.pdf

What TRA verifies:

- TRA is the telecom regulator; there is no data-center license class.
- License classes are Individual Operating License, Class Operating License, and Spectrum/Frequency License.
- FSMTC license IL-001 authorizes terrestrial cable, radio, submarine cable and cable landing station facilities, and international gateway services facilities.
- FSMTCC license IL-002 authorizes submarine cable and cable landing station facilities, terrestrial cable, terrestrial radio, and wholesale connectivity/data transmission.
- Boom! Inc. / iBoom in Yap is licensed for terrestrial cable, international gateway, and satellite earth-station facilities.
- Kacific, CPUC, Starlink, iSolutions, MCS Pohnpei, and FSMtech are licensed telecom/service players; these are connectivity leads, not data-center proof.
- TRA identifies bottleneck facilities: existing submarine cables to Pohnpei, Yap, and Chuuk plus FTTP networks in Pohnpei, Weno, and Yap Proper.
- TRA says CableCorp is building open-access FTTP for the main islands of all four states and will offer ancillary services including colocation.

Important correction: the TRA "S-band spectrum announcement" link visible in the menu currently resolves to an account-suspended page. Do not cite that URL for facts. Use the Public Register for Starlink Pacific Islands LLC's operating license effective 2024-03-19 and Mobile Satellite Frequency License FL-MS-001 effective 2025-10-01.

TRA queries:

```text
site:tra.fm "data center" "Micronesia"
site:tra.fm colocation OR "co-location" CableCorp
site:tra.fm "Public Register of Licences" FSMTC FSMTCC Starlink iBoom iSolutions
site:tra.fm "bottleneck facilities" "Pohnpei" "Weno" "Yap"
site:tra.fm "cable landing station" "international gateway"
```

### FSM Government, DTCI, DFO, DoFA

- FSM government portal: https://gov.fm/
- Department of Transportation, Communications and Infrastructure: https://www.tci.gov.fm/
- DTCI Communications Division: https://www.tci.gov.fm/communications.html
- Digital FSM Office: https://dfo.gov.fm/
- DoFA World Bank projects page: https://dofa.gov.fm/donors/world-bank/
- Digital FSM Project ESMP: https://tci.gov.fm/documents/communications/digitalfsm/digital-fsm-esmp-final-2019.pdf
- Digital FSM Project page: https://dofa.gov.fm/projects/digital-fsm-project/
- FSM Code: https://www.fsmlaw.org/fsm/code/

What government sources verify:

- Digital FSM includes a Secure Government Network and Data Center, Disaster Recovery/Business Continuity, and FSM-Cloud component. This is official evidence of a government data-center/government-cloud workstream, but not a public colocation facility until implementation records name a site/operator.
- DTCI/DoFA are the official route for project implementation, procurement, safeguards, and government-network evidence.
- Use state-government pages only to assign likely state facilities or offices; do not promote ordinary IT offices to data centers without a primary source describing racks, power, hosting, cloud, disaster recovery, or a dedicated facility.

Government queries:

```text
site:gov.fm "data center" OR "data centre" OR "FSM-Cloud" OR "server"
site:tci.gov.fm "Secure Government Network" "Data Center"
site:tci.gov.fm "Digital FSM" "server" OR "cloud"
site:dofa.gov.fm "Digital FSM Project" "data center" OR "green data centers"
site:fsmlaw.org "Title 21" "Telecommunications" "Cable Corporation"
```

### FSMTC - Telecommunications Corporation of the FSM

- Official site: https://fsmtc.fm/
- HANTRU-1 upgrade: https://www.fsmtc.fm/news/fsmtc-announces-completion-hantru-1-upgrade
- Chuuk-Pohnpei cable outage notice: https://www.fsmtc.fm/news/outage-chuuk-pohnpei-submarine-cable-system
- ICANN .fm correspondence: https://www.icann.org/en/system/files/files/fm-icann-letters-24oct07-en.pdf

What FSMTC sources verify:

- FSMTC is headquartered at P.O. Box 1210, Kolonia, Pohnpei FM 96941.
- FSMTC operates as the incumbent retail telecom provider and is licensed by TRA for international gateway and submarine cable/cable-landing facilities.
- FSMTC announced completion of the HANTRU-1 Pohnpei-Guam upgrade in 2021.
- FSMTC outage notices confirm operational dependence on the Chuuk-Pohnpei submarine cable and FSMTCC/OAE maintenance windows.

FSMTC queries:

```text
site:fsmtc.fm "data center" OR "server" OR "hosting" OR "colocation"
site:fsmtc.fm HANTRU OR "Pohnpei and Guam" OR "submarine cable"
site:fsmtc.fm "Chuuk-Pohnpei" OR "cable outage"
site:fsmtc.fm "Dedicated Internet Access" "Pohnpei"
```

### FSMTCC / CableCorp / OAE

- Official site: https://fsmcable.com/
- State pages: https://fsmcable.com/states/
- Chuuk page: https://fsmcable.com/states/chuuk/
- Kosrae page: https://fsmcable.com/states/kosrae/
- Pohnpei page: https://fsmcable.com/states/pohnpei/
- Yap page: https://fsmcable.com/states/yap/
- OAE wholesale overview PDF: https://fsmcable.com/wp-content/uploads/2020/11/High-level-OAE-overview-for-RSP-2020.pdf
- OAE interstate/international services PDF: https://fsmcable.com/wp-content/uploads/2020/11/OAE-Interstate-and-International-Connectivity-Services-November-2020.pdf
- Capital Projects Fund 2024 report: https://fsmcable.com/all-states/capital-projects-fund-2024-report/

What FSMTCC sources verify:

- FSMTCC/CableCorp is the government-owned open-access/wholesale entity, also referred to as OAE.
- FSMTCC gives its headquarters as Ocean View Plaza (East Wing), Suite 15, Pohnpei, FM 96941.
- Pohnpei has HANTRU-1 connectivity and the Pohnpei side of the C-P cable landing.
- Chuuk's C-P cable to Pohnpei became operational on 2019-04-27 and has a Chuuk landing station.
- Yap's spur to SEA-US has been in service since late June 2018.
- Kosrae was expected by FSMTCC to receive EMC service by late 2025; later NEC official material says EMCS construction was completed and handed over in 2026.
- OAE wholesale material explicitly designs for colocation space, power, and cooling at central offices/exchanges and describes future co-location/backhaul products.

FSMTCC queries:

```text
site:fsmcable.com colocation OR "co-location" OR "central office" OR exchange
site:fsmcable.com "Pohnpei" "landing station"
site:fsmcable.com "Chuuk" "landing station"
site:fsmcable.com "Yap" "in service" "June 2018"
site:fsmcable.com "Kosrae" "EMC" OR "East Micronesia Cable"
```

### World Bank and Donor-Government Records

- FSM Connectivity Project P130592: https://projects.worldbank.org/en/projects-operations/project-detail/P130592
- Digital FSM Project P170718 press release: https://www.worldbank.org/en/news/press-release/2020/03/29/new-digital-project-to-connect-federated-states-of-micronesia-to-global-economic-opportunities
- World Bank documents detail for Digital FSM P170718: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099072326232021244
- World Bank results story: https://www.worldbank.org/en/results/2026/07/07/connecting-islands-creating-opportunity-digital-transformation-expands-jobs-in-the
- AIFFP EMC investment page: https://www.aiffp.gov.au/investments/investment-list/improving-digital-connectivity-in-the-federated-states-of-micronesia-kiribati-and-naoero-via-submarine-cable
- AIFFP Kosrae landing: https://www.aiffp.gov.au/news/east-micronesia-cable-lands-third-and-final-pacific-location-kosrae-fsm
- NEC EMCS completion: https://www.nec.com/en/press/202605/global_20260515_02.html
- East Micronesia Cable project: https://www.eastmicronesiacable.com/ and https://www.eastmicronesiacable.com/the-project

What these verify:

- Digital FSM Project ID is P170718. The 2020 World Bank release states a US$30.8 million project.
- World Bank P170718 status material shows the original IDA-D5560 financing and later IDA-E5020 additional financing, with a revised closing date in 2027.
- World Bank P170718 status/results material includes a target of three new digital services hosted on private-sector-operated green data centers by March 2027. This is a project target, not a list of live facilities.
- The East Micronesia Cable System spans about 2,250 km and connects Tarawa, Nauru, Kosrae, and Pohnpei. NEC says construction was completed and handed over to FSMTCC/BNL/Cenpac on 2026-05-15.
- The East Micronesia Cable project page says cable landing stations house optical transmission equipment and power feed equipment. That is telecom landing-station evidence, not general-purpose colocation.

World Bank/donor queries:

```text
site:worldbank.org Micronesia "P170718" "green data centers"
site:documents.worldbank.org "Digital Federated States of Micronesia Project" "data center"
site:tci.gov.fm "FSM-Cloud" "Data Center"
site:aiffp.gov.au "East Micronesia Cable" "Kosrae"
site:nec.com "East Micronesia Cable System" "FSMTCC"
```

### US/FCC Sources

- FCC HANTRU-1 public notice DA-09-1309A1: https://docs.fcc.gov/public/attachments/DA-09-1309A1.pdf
- US Embassy in FSM: https://fm.usembassy.gov/
- US DOI Office of Insular Affairs FSM page: https://www.doi.gov/oia/islands/fsm

Use FCC for HANTRU-1 ownership/IRU and landing facts. Use US Embassy/DOI for Compact and donor-context confirmation. Do not infer a US military or federal data center in FSM; none was verified.

### Cloud-Provider Official Absence Checks

- AWS regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle OCI regions: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm

Current result: no FM region/local cloud region was found on the official pages. Re-check these pages before making time-sensitive claims.

## Per-State Official Workflow

| State | Official coverage status | Official-first route | What to record |
|---|---|---|---|
| Kosrae | Complete; new cable state | FSMTCC Kosrae page; East Micronesia Cable; AIFFP Kosrae landing; NEC completion; KUA for power; Kosrae state government only if a named ICT/server facility appears | EMC cable landing station and Kosrae FTTP plans as telecom infrastructure; Digital FSM/green-DC target as a national lead if no local site is named. Before EMC, treat Kosrae as satellite-only for facility purposes. |
| Pohnpei | Complete; highest-yield state | TRA register; FSMTC; FSMTCC Pohnpei page; DTCI/DFO/DoFA; World Bank P170718; FCC HANTRU-1 | FSMTC gateway/HANTRU-1, FSMTCC Pohnpei C-P/EMCS landing, CableCorp HQ/central-office colocation lead, national government data-center/FSM-Cloud lead in Palikir/Kolonia only if project documents name the site. |
| Chuuk | Complete; Weno-focused | FSMTCC Chuuk page; TRA register for CPUC/iSolutions; FSMTC outage notices; CPUC official site | C-P landing station in Chuuk/Weno, FSMTC Weno FTTP bottleneck facility, licensed CPUC/iSolutions communications infrastructure. Do not count outer-island satellite links as data centers. |
| Yap | Complete; cable plus competitor | FSMTCC Yap page; TRA register for Boom/iBoom; iBoom official site if needed; YSPSC official site | Yap Spur/SEA-US cable landing and open-access infrastructure, iBoom/Boom licensed network/gateway/earth-station facilities, FSMTC Yap Proper FTTP bottleneck facility. |

State sweep template:

```text
"{State}" "Federated States of Micronesia" "data center" OR "data centre" OR "server room"
"{State}" "Federated States of Micronesia" "cable landing station" OR "international gateway"
site:tra.fm "{State}" "license" OR "bottleneck" OR "FTTP"
site:fsmcable.com/states "{State}" "landing station" OR "FTTH" OR "FTTP"
site:tci.gov.fm "{State}" "Digital FSM" OR "FSM-Cloud" OR "server"
```

## Enumeration Rules

1. Start with TRA Public Register and Market Entry to identify licensed operators and allowed facility types.
2. Cross-check every physical telecom facility against FSMTC/FSMTCC primary records, World Bank/donor records, FCC records, or state utility/government records.
3. Classify landing stations, gateways, central offices, and FTTP head-ends as telecom infrastructure unless a source explicitly offers colocation/data-center/server-hosting services.
4. Classify CableCorp/OAE colocation as planned or wholesale telecom colocation until a current tariff, service order form, or operations manual confirms live availability.
5. Classify Digital FSM data-center/FSM-Cloud and green-data-center targets as official project leads until procurement, award, or commissioning documents identify locations/operators.
6. For divisions without a verified facility beyond telecom connectivity, record `no_projects: true` and preserve the search trail.
7. Use official cloud-provider region pages to document absence; do not use reseller availability pages as cloud-region evidence.

## Noise Filters

```text
-ship -vessel -registry -"Micronesia International Ship Registry" -Guam -Palau -Saipan -Marshall -Kiribati -Nauru
```

"Micronesia" often refers to the wider region. Keep searches anchored to "Federated States of Micronesia", "FSM", and the state names.
