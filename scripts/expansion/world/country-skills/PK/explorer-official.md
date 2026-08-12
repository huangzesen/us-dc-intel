# PK Explorer Official - Pakistan Datacenter Enumeration Methodology

Country: **PK Pakistan**. Review status: **finalized 2026-08-12** after live URL checks and source-grade tightening. This file covers the official/regulatory/government-procurement path for enumerating data centers and data-center-like facilities in Pakistan.

Division model for this expansion manifest: **7 first-level units**: Punjab; Sindh; Khyber Pakhtunkhwa; Balochistan; Islamabad ICT; Gilgit-Baltistan; Azad Kashmir. Pakistan also has lower administrative divisions and districts; record facility city/district exactly as the source states it.

## Reliability Grades

- **A** = primary source for the exact fact: government/regulator page, state operator page, operator-owned page, Uptime Institute award page, official cloud-region page, PeeringDB API for interconnection presence only.
- **B** = credible secondary source: PID/APP where carrying official statements, Dawn, Business Recorder, Express Tribune, ProPakistani, TechJuice, DCD, Developing Telecoms, Capacity, TeleGeography/Submarine Cable Map, APNIC, World Bank/ADB/CGD.
- **C** = directory/aggregator or weak secondary: DataCenterMap, DataCenterCatalog, datacenters.com, OCOLO, Cloudscene, LinkedIn/social reposts, unattributed market blogs.
- **U** = unsupported or not independently confirmed. Keep the field null or explicitly mark it unverified.

Grade each field separately. A source can prove that a facility exists but not its MW, exact address, owner, construction status, or Tier certification.

## Baseline Findings

- Pakistan has **no public national data-center registry**. PTA licenses telecom/data operators, but not data centers as a standalone public facility class.
- Public building-permit portals are not a useful data-center source. CDA, LDA, SBCA/KMC, PDA and Quetta authorities should be treated as address/approval follow-up channels, not discovery registries.
- Uptime Institute has a live Pakistan awards page at `https://uptimeinstitute.com/uptime-institute-awards/country/id/PK`. As of 2026-08-12 it lists: Government of Sindh Board of Revenue Data Center in Karachi; Islamabad (ICT) Safe City Data Center under NADRA; NTC Main Data Centre in Lahore; PTCL Commercial Data Center-1 Lahore; PTCL Commercial Data Center-2 Karachi; Sky47 Karakoram 1 in Islamabad; SBP Main Data Center in Karachi with both Design Documents and Constructed Facility awards; and Transworld KR1 in Karachi. Treat these as **A for award existence and award type only**.
- Official hyperscaler region pages for AWS, Azure, Google Cloud, Oracle Cloud, and Huawei Cloud returned no Pakistan/Karachi/Islamabad/Lahore region match on 2026-08-12. Any Pakistan “cloud region” wording is local/sovereign/partner cloud until the provider's official region page says otherwise.

## Core Official Sources

| Source | URL | Use | Grade notes |
|---|---|---|---|
| Pakistan Telecommunication Authority | `https://www.pta.gov.pk/`; licensing `https://www.pta.gov.pk/en/licensing` | Telecom licensing, CVAS/ISP/LDI/LTIS context, cable/connectivity statements | A for PTA-published facts; not a DC registry |
| MoITT | `https://moitt.gov.pk/`; latest news `https://moitt.gov.pk/LatestNews` | Cloud First, digital policy, AI/cloud MoUs and federal announcements | A for ministry statements; MoUs are intent only |
| SIFC | `https://sifc.gov.pk/`; Data Vault item `https://sifc.gov.pk/news/636`; IT page `https://www.sifc.gov.pk/ITmainPage` | Investment pipeline and official project announcements | A for official publication; B/U for third-party operational claims not independently stated |
| BOI | `https://invest.gov.pk/` | Investment/SEZ leads | A for BOI pages; not a facility registry |
| PPRA/e-PADS | `https://www.ppra.org.pk/`; `https://www.eprocure.gov.pk/` | Tender discovery for server rooms, data centers, cloud migration and DR | A for tender existence; award/outcome requires contract follow-up |
| NEPRA | `https://nepra.org.pk/` | Power-license and grid sanity checks | A for generation/license records; no DC list |
| Uptime Institute | `https://uptimeinstitute.com/uptime-institute-awards/country/id/PK` | Tier award verification | A for listed award type, city and client |
| NTC cloud/NDC | `https://cloud.gov.pk/`; `https://ntc.net.pk/` | Government cloud/NDC leads | A where reachable official service page states the fact |
| PID | `https://pid.gov.pk/site/press_detail/15554` | NTC DRC Lahore official press release | A/B: official press release, verify against NTC if exact service status matters |
| PKIX | `https://pkix.pk/` | Official Pakistan IXP background and participants | A for IXP; not a data center by itself |

## Official Search Vocabulary

Use English first, then Urdu for local media/procurement sweeps.

```text
"data center" OR "data centre" OR datacenter
"national data centre" OR "government data center" OR "disaster recovery center"
"cloud first" OR "government cloud" OR "sovereign cloud"
"server room" OR hosting OR colocation OR "co-location"
"Tier III" OR "Tier 3" OR "TIA-942" OR Uptime
"internet exchange" OR IXP OR "landing station" OR "submarine cable"
"ڈیٹا سینٹر" OR "سرور روم" OR "کلاؤڈ" OR "ڈیجیٹل انفراسٹرکچر" OR "ٹینڈر"
```

Prefer quoted phrases and domain filters. Do not rely on bare `OR` expressions inside government-site search boxes; use web search with `site:` or run separate searches.

## Official Query Templates

```text
site:pta.gov.pk ("data center" OR "data centre" OR cloud OR hosting OR CVAS)
site:moitt.gov.pk ("data center" OR "data centre" OR "cloud first" OR "national data centre")
site:sifc.gov.pk ("data center" OR "data centre" OR cloud OR AI OR "digital infrastructure")
site:invest.gov.pk ("data center" OR "data centre" OR "IT park" OR "technology zone")
site:eprocure.gov.pk ("data center" OR "data centre" OR "server room" OR "disaster recovery" OR cloud)
site:ppra.org.pk ("data center" OR "data centre" OR "server" OR "ICT infrastructure")
site:uptimeinstitute.com/uptime-institute-awards/country/id/PK Pakistan
site:cloud.gov.pk OR site:ntc.net.pk ("data center" OR "data centre" OR "cloud" OR NDC)
site:nitb.gov.pk ("data center" OR "data centre" OR cloud OR hosting)
site:pid.gov.pk ("data center" OR "data centre" OR "disaster recovery" OR NTC)
"{division}" "data center" Pakistan government
"{city}" "ڈیٹا سینٹر" Pakistan
```

## Division Coverage

| Division | Coverage status | Official discovery method | Known official/institutional leads |
|---|---|---|---|
| **Sindh** | Complete; primary commercial hub | SIFC/MoITT/PTA + Sindh procurement + Uptime + safe city + cable landing checks | Data Vault Karachi; PTCL Commercial DC-2 Karachi; SBP MDC Karachi; Government of Sindh Board of Revenue DC; Transworld KR1; Sindh Safe Cities Authority; Karachi cable landing stations |
| **Punjab** | Complete; second hub | Punjab PPRA/PITB/PSCA + Uptime + NTC/PID | PTCL Commercial DC-1 Lahore; NTC Main Data Centre/DRC Lahore; PSCA PPIC3 Lahore; PITB/government systems; Rawalpindi/Lahore follow-up for Sky47-related claims if source gives city outside ICT |
| **Khyber Pakhtunkhwa** | Complete; institutional pipeline, limited commercial evidence | KPITB, KP Digital Transformation Strategy, KPPRA, safe-city/police/university sweeps | KP strategy states a modern Tier-III Government Data Centre; KPITB projects/STPs; no verified commercial colo hub found in official sources |
| **Balochistan** | Complete; minimal | Balochistan Police, provincial tenders, university queries | Balochistan Police D3C on Gulistan Road Quetta; University of Turbat data centre from credible press; no official commercial colo evidence |
| **Islamabad ICT** | Complete; federal cluster | MoITT, NTC, NITB, NADRA, PTA, PKIX, Uptime, operator official pages | Zong CICC; Jazz Digital Park; Sky47 Karakoram 1; Islamabad ICT Safe City DC; NTC/NITB/NADRA facilities; PKIX/PERN; federal AI/cloud initiatives |
| **Gilgit-Baltistan** | Complete; negative-search default | GBIT downloads, GB Cloud First Policy, GB tenders | GB Cloud First Policy 2024 supports cloud adoption and procurement; no confirmed local DC facility found |
| **Azad Kashmir** | Complete; negative-search default | AJK IT Board, AJK government and procurement searches | AJK IT Board/e-government only; no confirmed local DC facility found |

## Official Seed Evidence

| Facility/project | Division | Status to record | Best evidence | Grade |
|---|---|---|---|---|
| PTCL Commercial Data Center-1 Lahore | Punjab | Operational facility with Uptime Design Documents award | Uptime PK awards; PTCL cloud/DC pages | A for award; A for PTCL service; capacity U unless PTCL discloses |
| PTCL Commercial Data Center-2 Karachi | Sindh | Operational facility with Uptime Design Documents award | Uptime PK awards; PTCL cloud/DC pages | A for award; A for PTCL service |
| SBP Main Data Center | Sindh | Operational institutional DC; Uptime Design Documents and Constructed Facility awards | Uptime PK awards; SBP site for entity | A for awards; facility details U unless SBP publishes |
| Board of Revenue Data Center | Sindh | Government DC; Uptime Design Documents award | Uptime PK awards | A for award; specs U |
| Transworld KR1 | Sindh | Project/facility with Uptime Design Documents award | Uptime PK awards; TWA official site; cable/DC press | A for award; B for construction/launch timing unless TWA official page confirms |
| Data Vault Pakistan AI data centre | Sindh | Launched in Karachi per SIFC | SIFC item `https://sifc.gov.pk/news/636`; company site `https://datavault.com.pk/` | A for SIFC launch statement and company existence; GPU/solar/superlative details only if primary source states them |
| Quantum Global Data Center | Sindh | Announced Karachi project, not operational by default | QGDC `https://quantumdc.com/about-us/`; Dawn/Business Recorder/DCD on $230m Huawei partnership | A for company existence; B for project economics/status |
| Zong Cloud Intelligent Computing Center | Islamabad ICT | Inaugurated at Zong HQ Islamabad; Tier-III wording per company | Zong PR URL in source log; Zong cloud page | A for launch and company wording; Uptime registry not listed under Zong as of this review |
| Jazz Digital Park | Islamabad ICT | Operational; TIA Tier-III wording; 300+ racks/3MW from VEON/Jazz | VEON PR and Jazz media room | A for operator claim; not Uptime unless Uptime lists it |
| Sky47 Karakoram 1 | Islamabad ICT | Uptime Design Documents award; inaugurated/AI cloud claims require separate current source | Uptime PK awards; ZTE/Sky47/official press where available | A for award; B/A per opened launch source; claims such as largest/Tier IV U unless certified |
| NTC National Data Centre and Lahore DRC | Islamabad ICT/Punjab | Government cloud/NDC + Lahore DRC | `https://cloud.gov.pk/`; PID press release `https://pid.gov.pk/site/press_detail/15554`; NTC site | A for official service/press wording; current capacity U |
| NADRA data centers | Islamabad ICT and undisclosed DR site(s) | Operational institutional DC estate | NADRA site for entity; CGD NADRA Story for two DCs 150 miles apart and third planned | B for count/distance; locations U unless NADRA publishes |
| Islamabad ICT Safe City Data Center | Islamabad ICT | Uptime Design Documents award | Uptime PK awards | A for award; operational/spec details need authority source |
| KP Government Data Centre | Khyber Pakhtunkhwa | Tier-III Government Data Centre stated in KP Digital Transformation Strategy | `https://digital.kpitb.gov.pk/`; KPITB site | A for KPITB statement; city/specs U |
| Balochistan Police D3C | Balochistan | Operational command/data center in Quetta | `https://balochistanpolice.gov.pk/d3c` and tenders page | A for D3C existence; not commercial colo |
| University of Turbat data centre | Balochistan | Operational institutional facility | Express Tribune `https://tribune.com.pk/story/2420867/data-centre-opens-at-university-of-turbat` | B |
| PKIX/PERN | Islamabad ICT; Lahore/Karachi IXP nodes in secondary data | IXP, not DC | `https://pkix.pk/`; PeeringDB/APNIC for nodes | A for official IXP; PeeringDB A for interconnection presence only |

## Certification Rules

- Uptime Institute awards are A-grade only for the award displayed. Most Pakistan entries are **Tier III Certification of Design Documents**, not constructed-facility certification. SBP MDC is listed with both Design Documents and Constructed Facility.
- TIA-942/Tier-III marketing from Jazz, Zong, PTCL, Sky47, or others must be recorded as the source's wording unless matched to Uptime/TIA certification records.
- Do not convert `designed to Tier III`, `Tier III compliant`, or `Tier III certified` into operational resilience claims.

## Procurement and Power Pass

Use PPRA/e-PADS plus provincial procurement portals for `data center`, `server room`, `DR site`, `cloud migration`, `UPS`, `generator`, `precision cooling`, `rack`, and Urdu `ڈیٹا سینٹر`. Tenders prove procurement intent only. Follow award documents, contract notices, and completion reports before adding a facility.

Use NEPRA/DISCO/NTDC only to sanity-check power feasibility. Record MW/kVA/kW only when the exact facility source states it. Do not infer capacity from a company's generation assets or grid connection.

## Cloud Region Absence Check

Re-check these every quarter:

```text
https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
https://learn.microsoft.com/en-us/azure/reliability/regions-list
https://cloud.google.com/about/locations
https://www.oracle.com/cloud/public-cloud-regions/
https://www.huaweicloud.com/intl/en-us/global/
```

On 2026-08-12 all returned HTTP 200 and no Pakistan/Karachi/Islamabad/Lahore match in fetched text. This is absence evidence only; it can change.

## Update Cadence

- Monthly while active projects are moving: Data Vault, QGDC, Transworld KR1/Tier III DC, Sky47, GO AI Hub and any SIFC/MoITT cloud project.
- Quarterly: full official-source sweep, Uptime PK awards page, cloud-region absence check, PeeringDB PK facilities/IXPs, PPRA/e-PADS and provincial PPRAs.
- Semiannual: negative sweep for KP, Balochistan, Gilgit-Baltistan and Azad Kashmir; check provincial IT-board domains and policy downloads.
- Annual: legal/policy refresh for data protection, cloud-first policy, PTA licensing changes, SIFC/BOI structure and procurement portals.

## Source Status Log

Validation status on 2026-08-12: PTA, MoITT, SIFC, BOI, PPRA/e-PADS, NEPRA, Uptime PK, Zong, Jazz/VEON, NTC, PID, PKIX, digital KP/KPITB, GBIT, QGDC, Transworld and the five official cloud-region pages returned usable HTTP results. Data Vault and AJK IT Board were bot-blocked but search-indexed/site-present. Cloud.gov.pk and Balochistan Police timed out from curl during validation but were retained because search results and prior source discovery identify the official pages; open them in browser/search before extracting new fields.
