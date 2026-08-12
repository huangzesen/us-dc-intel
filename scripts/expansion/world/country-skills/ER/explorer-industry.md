# ER Explorer Industry - Eritrea Datacenter Discovery

Date: 2026-08-12. Scope: Eritrea (ER) datacenter discovery from operator pages, telecom and cloud trade press, satellite/connectivity vendors, subsea-cable sources, energy/mining sources, enterprise ICT, aggregators, and regional search patterns. Use this file to find leads; use `explorer-official.md` to verify them against EriTel, Shabait, gazette/legal records, State Department, AfDB/World Bank/ITU, and power evidence.

Repository division model: **Anseba; Southern Red Sea; Southern; Gash-Barka; Central; Northern Red Sea**.

Reliability grades:

- **A**: primary/operator/official source for the exact fact. Examples: EriTel pages, Shabait, official gazette/legal text, US State Department ICS, AfDB/World Bank/ITU records, Uptime certification, or a named operator page.
- **B**: reputable industry/development/press evidence. Examples: Submarine Networks, Carnegie, East African Review, DataReportal, Internet Society Pulse, ICTworks, BuddeComm, Developing Telecoms, Connecting Africa, energy/mining press.
- **C**: aggregator-only listings, directories, forums, social posts, personal blogs, generic VSAT/LEO reseller pages, marketing pages, MoUs, feasibility chatter, or unsupported facility inferences.

## 0. Eritrea-Specific Industry Frame

- Eritrea is a very low-yield datacenter market, but not a zero-signal market. The verified public signal is **EriTel-hosted local email and private-cloud services in EriTel's datacenters**: `https://eritel.com.er/contents.php?id=1045` and `https://eritel.com.er/contents.php?id=1046`.
- Treat that EriTel evidence carefully. It proves an operator-hosted datacenter platform exists, but it does not publish exact facility names, addresses, racks, floorspace, MW, redundancy tier, customer list, or whether the rooms are in one or multiple cities. Asmara/Central is the best location inference because EriTel's headquarters is in Asmara and its direct-connect terms distinguish Asmara from remote cities, but exact site details remain undisclosed.
- Eritrea has no verified public commercial colocation campus, hyperscaler region, carrier-neutral IXP, or public subsea landing station in current public evidence. Submarine Networks says Eritrea is the lone coastal African exception without a subsea landing (`https://www.submarinenetworks.com/en/stations/africa`); Carnegie repeats that no-landing exception in a 2025 analysis.
- Industry context is restrictive: state telecom dominance, no public telecom licence register, very limited fixed/mobile data market, weak power availability, and low internet penetration. DataReportal Digital 2026 reports 726 thousand internet users at end-2025 and 859 thousand cellular mobile connections in late 2025: `https://datareportal.com/reports/digital-2026-eritrea`. Internet Society Pulse reports about 27% of the population as internet users and very poor ISP choice: `https://pulse.internetsociety.org/en/reports/er/`.
- The discovery workflow is: (1) monitor EriTel hosted-service, MPLS, fibre, and rollout pages; (2) sweep Shabait and official/legal sources for named facilities; (3) sweep cable/satellite news for future landing/gateway leads; (4) test banks, mining, UN/embassy, and university ICT for server-room disclosures; (5) run all six division searches and record negatives.
- Spelling variants: `data center`, `data centre`, `datacentre`, `datacenter`; `Asmara`, `Asmera`; `Massawa`, `Mitsiwa`; `Assab`, `Aseb`; `Keren`, `Cheren`; `Mendefera`; `Barentu`; `Gash-Barka`, `Gash Barka`; `Maekel`, `Debub`, `Semienawi Keyih Bahri`, `Debubawi Keyih Bahri`; `hosting`, `private cloud`, `email hosting`, `Nextcloud`, `colocation`, `server room`, `MPLS`, `direct connect`, `VSAT`, `earth station`, `gateway`, `fibre`, `fiber`.

## 1. High-Value Industry Sources

| Source | URL | Best use | Grade |
|---|---|---|---|
| EriTel private cloud | `https://eritel.com.er/contents.php?id=1046` | Primary evidence that EriTel Nextcloud/private cloud is hosted in EriTel datacenters; includes storage/user tiers, direct-connect terms, uptime/RTO. | **A** |
| EriTel email hosting | `https://eritel.com.er/contents.php?id=1045` | Primary evidence that email hosting is locally hosted in EriTel datacenters; lists Axigen, Barracuda, VM replica, weekly backups, direct connect, 99% uptime. | **A** |
| EriTel history/fibre core | `https://eritel.com.er/contents.php?id=1029` | Primary evidence for EriTel restructuring and fibre core in Asmara and Massawa. | **A** |
| EriTel MPLS/SiteConnect | `https://eritel.com.er/contents.php?id=1032` | Enterprise network service context and direct-connect search pivot; not a datacenter by itself. | **A** for service facts |
| Shabait | `https://shabait.com/` | State announcements for telecom, power, ports, mining, ICT. | **A** for named official facts; **B** for background |
| Submarine Networks Africa stations | `https://www.submarinenetworks.com/en/stations/africa` | No-subsea-landing check; identifies Eritrea as the coastal African exception. | **B** |
| Carnegie undersea cable analysis | `https://carnegieendowment.org/research/2025/04/beneath-the-waves-addressing-vulnerabilities-in-africas-undersea-digital-infrastructure` | Independent no-landing corroboration and regional subsea-cable context. | **B** |
| East African Review Red Sea article | `https://eastafricanreview.com/2024/06/11/red-sea-internet-in-peril-cable-companies-turn-to-eritrea-amid-houthi-threats/` | Future lead: cable companies considering Eritrean waters amid Red Sea conflict. No facility/landing commitment. | **B** for report; **C** for any facility inference |
| DataReportal Digital 2026 Eritrea | `https://datareportal.com/reports/digital-2026-eritrea` | Current internet/mobile/social-market context. | **B** |
| Internet Society Pulse Eritrea | `https://pulse.internetsociety.org/en/reports/er/` | Internet penetration, ISP choice, resilience, IXP/cache context. | **B** |
| ICTworks Eritrea internet access | `https://www.ictworks.org/understanding-eritreas-exceptionally-limited-internet-access/` | Ground-level connectivity constraints, internet cafe/community access context. | **B** |
| ts2.tech "Digital Desert" | `https://ts2.tech/en/eritreas-digital-desert-inside-the-worlds-most-isolated-internet-and-the-satellite-lifeline-on-the-horizon/` | Long-form industry overview of isolation, satellite limits, Starlink/VSAT issues. Verify facility claims against primary sources. | **B/C** |
| AfDB 12 MW mini-grid | `https://www.afdb.org/en/news-and-events/press-releases/desert-power-african-development-bank-group-eritrea-sign-agreement-12-mw-mini-grid-project-81778` | Power context for Teseney, Barentu, Kerkebet. Not datacenter evidence. | **A** |
| Africa Energy Portal Eritrea | `https://africa-energy-portal.org/aep/country/eritrea` | Installed/available capacity and electricity-access context. | **B** |
| GlobalTT / VSAT resellers | `https://www.globaltt.com/en/internet-connection/eritrea.html` and city pages | Satellite offer discovery only; do not treat reseller coverage pages as licensed domestic infrastructure. | **C** |
| Aggregators | `https://www.datacentermap.com/eritrea/`, `https://baxtel.com/`, `https://www.datacenters.com/`, `https://www.ocolo.io/data-centers/eritrea/` | Expected zero or weak entries; use as negative checks and spelling discovery only. | **C** |

Trade and industry queries:

```text
"EriTel" "datacenters" OR "data centers" OR "data centres"
"Eritel" "Private Cloud Services" OR Nextcloud OR "Email Hosting Services"
"Eritel" Axigen OR Barracuda OR "VM Replica"
"Eritrea" "data center" OR "data centre" OR datacenter OR datacentre
"Eritrea" "server farm" OR "colocation" OR "cloud region" OR "hosting"
"Eritrea" "submarine cable" OR "landing station" OR "cable landing"
"Eritrea" "earth station" OR gateway OR VSAT OR teleport
site:eastafricanreview.com Eritrea cable OR internet OR telecom
site:connectingafrica.com Eritrea telecom OR data OR cloud
site:developingtelecoms.com Eritrea telecom OR data OR cloud
site:ictworks.org Eritrea internet OR telecom
site:ts2.tech Eritrea internet OR satellite OR Starlink
```

Capture lifecycle wording exactly. `Considering`, `planned`, `prospective`, `feasibility`, `coverage`, and `available by reseller` are not operational facility evidence. `Hosted in datacenters`, `launched`, `commissioned`, `inaugurated`, `certified`, `signed power connection`, and `operational` are stronger, but still grade by source.

## 2. Operator And Project Sweep

| Operator / project | Source route | Eritrea signal | Grade and next joins |
|---|---|---|---|
| EriTel hosted email/private cloud | `https://eritel.com.er/contents.php?id=1045`, `https://eritel.com.er/contents.php?id=1046` | Official pages say services are hosted locally/in EriTel's datacenters. Email tiers include Axigen, Barracuda, VM replica, backups, 99% uptime; private cloud tiers include Nextcloud apps, 100-500 GB storage, 20-100 users, 90% uptime, up to 6-day RTO. | **A** for service/facility existence. Join to Shabait and any EriTel contact/site pages for location; keep exact site undisclosed absent primary evidence. |
| EriTel fibre/MPLS/ADSL network | EriTel history, internet, MPLS pages | Fibre core in Asmara and Massawa; direct-connect/MPLS services; ADSL rollout towns Debaruwa, Adi Quala, Segenetti, Nakfa, Serjeka. | **A** for network/service facts; not datacenter records by themselves. |
| Subsea cable rerouting interest | East African Review 2024; Submarine Networks/Carnegie no-landing checks | Possible future Red Sea routing through Eritrean waters; no landing station, no named consortium commitment, no EriTel/state announcement. | **B/C** monitor lead; do not enumerate. |
| Satellite/LEO offers | GlobalTT, BusinessCom/NTvsat-type pages, Starlink availability coverage | Resellers advertise VSAT/LEO service into Eritrea; Starlink public availability has no reliable licensed Eritrea launch evidence in verified sources. | **C** unless a licence/import/ground-station source appears. |
| State banks | National Bank of Eritrea, Commercial Bank of Eritrea, Housing and Commerce Bank routes | Core-banking/server-room possibility in Asmara. | **C** unless the bank discloses a dedicated datacenter or hosted facility. |
| Mining enterprise IT | Bisha/Zijin, Zara, Danakali/Colluli historical routes | Mine camps likely use enterprise IT/VSAT and substantial power. | **C** context; not a datacenter without primary disclosure. |
| UN/embassies/NGOs | UNDP/mission procurement, embassy pages, field reports | Offices may operate local server rooms or VSAT links. | **C** context; do not count. |
| Universities/government ICT | Eritrea Institute of Technology, ministries, Shabait | Campus/ministry ICT rooms possible. | **C** unless named facility evidence appears. |

Operator queries:

```text
"EriTel" "private cloud" "datacenters"
"EriTel" "email hosting" "datacenters"
"EriTel" "data center" OR "data centre" OR colocation
"EriTel" "Direct Connect" OR MPLS OR SiteConnect
"EriTel" VSAT OR "earth station" OR gateway
"Huawei" Eritrea "data center" OR datacentre OR "cloud"
"GlobalTT" Eritrea Starlink OR OneWeb OR VSAT
"BusinessCom" Eritrea VSAT OR "satellite internet"
"Bisha" Eritrea server OR datacenter OR VSAT OR "IT infrastructure"
"Commercial Bank of Eritrea" "server room" OR "data center"
"National Bank of Eritrea" "server room" OR "data center"
```

## 3. Industry-To-Official Verification Pivots

For every press, vendor, or aggregator lead, run these joins before enumeration:

```text
site:eritel.com.er "{operator}" OR "{service}" OR "{town}"
site:eritel.com.er "Datacenters" "{service}"
site:shabait.com "{operator}" OR "{project}" OR "{town}"
"{operator}" "Eritrean Investment Center" OR EFZA OR "free zone"
"{operator}" EEC Eritrea MW OR power OR substation
site:state.gov Eritrea "{operator}" OR "{project}"
site:afdb.org Eritrea "{town}" OR "{project}"
site:peeringdb.com AS30987 OR EriTel
site:uptimeinstitute.com Eritrea OR EriTel
```

Use these official joins:

- EriTel: `https://eritel.com.er/`
- Email hosting: `https://eritel.com.er/contents.php?id=1045`
- Private cloud: `https://eritel.com.er/contents.php?id=1046`
- Fibre/history: `https://eritel.com.er/contents.php?id=1029`
- Shabait: `https://shabait.com/`
- US State Dept ICS: `https://www.state.gov/reports/2025-investment-climate-statements/eritrea`
- UNCTAD investment law: `https://investmentpolicy.unctad.org/investment-laws/laws/255/eritrea-investment-proclamation-`
- EEC Proclamation 142/2004: `https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-142-2004/eritrean-proc-142-2004.pdf`
- EFZA Proclamation 115/2001: `https://leap.unep.org/en/countries/er/national-legislation/eritrean-free-zones-proclamation-no-115-2001`
- AfDB mini-grid project: `https://www.afdb.org/en/news-and-events/press-releases/desert-power-african-development-bank-group-eritrea-sign-agreement-12-mw-mini-grid-project-81778`

## 4. Regional Search Playbook

Use each row as a checklist and mark negative searches explicitly.

| Manifest division | Towns/sites | Industry strategy | Expected yield |
|---|---|---|---|
| Central | Asmara, Asmera, Ghala Nefhi, Serejaka/Serjeka, airport/industrial areas | EriTel datacenters-hosted email/private cloud, HQ, MPLS/direct connect, banks, ministries, internet cafes, `server room`, `hosting`, `gateway`, `VSAT`, `racks`, `Tier`, `Uptime`. | **Low-medium.** Best national seed is EriTel; exact site undisclosed. |
| Northern Red Sea | Massawa, Hirgigo, Nakfa, Ghinda, Foro, Afabet | EriTel Massawa fibre core, Nakfa rollout, port/free-zone ICT, cable landing/rerouting checks, Hirgigo power context. | **Low/negative.** No verified subsea landing or DC tenant. |
| Southern | Mendefera, Debaruwa, Adi Quala, Segenetti, Dekemhare, Adi Keyh, Mai Nefhi/EIT | ADSL rollout towns, EIT/campus ICT, Dekemhare solar, regional government server-room searches. | **Negative/low.** Telecom/power/campus context only. |
| Anseba | Keren, Hamelmalo, Elabered, Kerkebet | Regional telecom node, university/agriculture ICT, AfDB Kerkebet mini-grid, `VSAT`, `server room`. | **Negative.** |
| Gash-Barka | Barentu, Teseney/Tessenei, Agordat, Bisha mine area | Mining ICT/VSAT, AfDB Barentu/Teseney mini-grids, regional telecom, power/MW searches. | **Negative/low.** Mining IT is not DC evidence. |
| Southern Red Sea | Assab/Aseb, Beilul, Denkalia plain | Assab free zone, port ICT, wind/power context, regional telecom, satellite/VSAT. | **Negative.** |

Reusable regional queries:

```text
"{division}" Eritrea "data center"
"{division}" Eritrea "data centre"
"{town}" Eritrea "data center" OR "data centre" OR datacenter
"{town}" Eritrea "server room" OR colocation OR hosting
"{town}" Eritrea "private cloud" OR "email hosting" OR Nextcloud
"{town}" Eritrea "VSAT" OR "earth station" OR gateway OR satellite
"{town}" Eritrea "fibre" OR fiber OR ADSL OR broadband OR exchange
"{town}" Eritrea "free zone" OR "industrial park" OR port OR tenant
"{town}" Eritrea mining OR power OR MW OR substation
"EriTel" "{town}" Eritrea
site:shabait.com "{town}" EriTel OR internet OR electricity OR port
```

Tigrinya/local-language secondary queries:

```text
"{town}" "መረጃ ማእከል" OR "ሰርቨር" OR "ኣገልግሎት ኢንተርነት"
site:shabait.com "ሰርቨር" OR "መረጃ"
"{town}" Eritrea Tigrinya internet OR computer
```

## 5. Aggregator Handling

Aggregators are expected to return zero or weak Eritrea entries. Use them for negative checks and alternate spelling discovery only.

```text
site:datacentermap.com/eritrea Eritrea
site:baxtel.com Eritrea datacenter OR "data center"
site:datacenters.com Eritrea datacenter OR "data center"
site:ocolo.io "Eritrea" "data centers"
"Eritrea" "colocation" "Data Center Map" OR Baxtel OR datacenters.com
```

Rules:

- Aggregator-only facility: **C**, even if it appears to name a city.
- Aggregator plus EriTel official hosted-service pages: grade only the EriTel facts as **A**; keep aggregator-only fields such as address, racks, or tier at **C**.
- Nearby-country listings in Djibouti, Sudan, Ethiopia, Kenya, Saudi Arabia, or UAE must not be imported into Eritrea.

## 6. Hyperscaler, Certification, And Connectivity Checks

Recheck official pages before each major refresh:

```text
site:aws.amazon.com/about-aws/global-infrastructure/regions_az Eritrea
site:learn.microsoft.com/en-us/azure/reliability/regions-list Eritrea
site:cloud.google.com/about/locations Eritrea
site:oracle.com/cloud/public-cloud-regions Eritrea
site:uptimeinstitute.com Eritrea EriTel
site:submarinenetworks.com Eritrea "landing"
site:eastafricanreview.com Eritrea cable 2025 OR 2026
site:starlink.com Eritrea availability
```

If official provider pages still do not list Eritrea, record a negative hyperscaler/certification check. If a new cable, LEO licensing, or sovereign-cloud story appears, grade it **B/C** until a primary EriTel/state/named-operator source identifies the physical site.

## 7. Final Evidence Rules

- Final facility records need a named operator/project, division/city or explicit "undisclosed", source URL, source date/access date, lifecycle stage, and grade.
- For Eritrea, the likely final inventory is **EriTel hosted-services datacenters, exact site undisclosed**, plus negative records in most divisions. That is a valid outcome.
- Do not promote an EriTel fibre core, MPLS/direct-connect route, ADSL rollout, port/free zone, power plant, mine camp, bank system, university server room, or VSAT sales page to datacenter status without a source naming a datacenter/server-hosting facility.
- Do not convert Red Sea cable-rerouting interest into a Massawa landing station. Do not use contradictory EASSy snippets as proof of a landing where Submarine Networks and Carnegie show no Eritrean landing.
- Do not label EriTel private cloud as AWS/Azure/GCP/OCI, sovereign cloud, carrier-neutral colocation, or Tier-certified unless a primary source says so.
- Keep reliability grades honest: **A** for official EriTel hosted-service facts; **B** for market/cable/power context; **C** for exact-location inference, directories, and marketing-only satellite/cloud pages.
- Re-verify quarterly: EriTel service pages, Shabait announcements, cable/landing sources, Starlink/LEO licensing, EFZA tenants, EEC/AfDB power projects, Uptime awards, and hyperscaler region pages.
