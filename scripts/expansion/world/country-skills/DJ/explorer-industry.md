# DJ Explorer Industry - Djibouti Datacenter Enumeration via Operators, Connectivity, Subsea, Peering, Trade Press and Directories

Date verified: 2026-08-12. Country: **DJ - Djibouti**. Division model from `world-manifest.jsonl`: **6 regions/cities**: **Arta, Ali Sabieh, Dikhil, Djibouti, Obock, Tadjourah**. Scope: industry-side discovery that complements `explorer-official.md`: operator pages, subsea/cable landing records, peering sources, trade press, investor announcements, directories and local market signals.

Reliability grades:
- **A** = primary/operator/official evidence: Wingu, Djibouti Telecom, PAIX/FSD or other operator pages/releases; AMS-IX and PeeringDB for IXP metadata; official cable/operator pages; Uptime Institute certification records; official cloud-region pages.
- **A-** = official operator/investor announcement proving a named site or project, but without a regulator/permit filing; capacity and tier claims remain claim-specific.
- **B** = strong secondary evidence: Data Center Dynamics (DCD), SDxCentral, SubTel Forum news, Capacity/Connecting Africa, African Business, Agence Ecofin, Telecompaper, credible local state/business press.
- **C** = lead only: Baxtel, DataCenterMap, DataCenters.com, Cloudscene, OCOLO, market reports, SEO lists, social posts, vendor pages without a named physical Djibouti site.

Grade each fact separately. A facility can be **A-** for operator existence, **B** for a trade-press launch date, and **C** for directory MW/rack figures.

---

## 0. Djibouti Industry Frame

- Djibouti is a small datacenter market but a major East African subsea landing and interconnection hub. The commercial market is measured in single-digit MW, not regional hyperscale campus sizes.
- All confirmed commercial data-centre activity is in the **Djibouti** division/Djibouti City area.
- Current named facility/project set:
  - **Wingu / Djibouti Data Center (DDC)**: operational older carrier-neutral colocation facility, opened 2013, near Djibouti Telecom's international cable landing infrastructure.
  - **Wingu TO7 Technology Park data centre + carrier-neutral CLS**: launched/inaugurated in November 2024; operator and trade sources describe a Tier 3/Tier III-aligned facility and about 3 MW design capacity.
  - **Djibouti Telecom CLS/data-centre/colocation infrastructure**: official telecom/cable landing infrastructure; treat telco rooms as facility records only when source text names data centre/colocation/server infrastructure.
  - **ANSIE national data center hosting reference**: the Presidency's 2023 tariff-decree summary says ANSIE services include hosting within a national data center; physical site/operator is not named, so do not count as a separate facility until resolved.
  - **AMS-IX Djibouti / DjIX**: operational IXP hosted at Djibouti Data Center SARL.
  - **PAIX JIB1 / PAIX Djibouti**: announced 5 MW project with the Djibouti Sovereign Fund; keep non-operational until construction/commissioning evidence appears.
- No confirmed AWS, Azure, Google Cloud or Oracle public cloud region in Djibouti. Cable consortium participation, PoPs, cloud exchange products and CDN/edge nodes are ecosystem evidence, not cloud-region facilities.
- Directory country counts are unstable and often stale; never use an aggregator count as a census.

---

## 1. Facility and Project Census Seeds

| Candidate | Division / location | Status handling | Evidence anchors | Grade guidance |
|---|---|---|---|---|
| **Wingu / Djibouti Data Center (DDC)**, also `Djibouti Data Center SARL`, `Wingu Africa Djibouti 1` | Djibouti - Djibouti City, Haramous/Boulaos area near Djibouti Telecom CLS | Operational carrier-neutral colocation; opened 2013 per DCD. Capacity is not officially verified in this review; directory ~1 MW is C only. | Wingu Djibouti market page: https://www.wingu.africa/markets/djibouti ; DCD 2013 launch: https://www.datacenterdynamics.com/en/news/djibouti-launches-data-center-near-submarine-cable-landing/ ; DCD 2024 context: https://www.datacenterdynamics.com/en/news/wingu-group-launches-data-center-and-cls-in-djibouti-tech-park/ ; Baxtel: https://baxtel.com/data-center/djibouti-data-center-ddc ; DataCenterMap: https://www.datacentermap.com/djibouti/djibouti-city/djibouti-data-center-ddc/ | **A-** for current Wingu/operator service claim; **B** for DCD history; **C** for directory capacity/address details unless corroborated. |
| **Wingu TO7 Technology Park data centre + carrier-neutral CLS** | Djibouti - TO7 Technology Park, Djibouti City | Operational/launched in Nov 2024. Treat 3 MW as design/announced capacity unless an operator technical sheet confirms operational IT load. "Tier 3" is operator/trade wording unless Uptime record is found. | Wingu inauguration page: https://www.wingu.africa/latest-news/djibouti-president-inaugurates-wingu-tier-3-carrier-neutral-data-centre ; DCD launch: https://www.datacenterdynamics.com/en/news/wingu-group-launches-data-center-and-cls-in-djibouti-tech-park/ ; SDxCentral launch: https://www.sdxcentral.com/news/wingu-group-launches-data-center-and-cls-in-djibouti-tech-park/ ; Telecompaper: https://www.telecompaper.com/news/wingu-group-opens-to7-technology-park-in-djibouti-housing-data-centre-and-cable-landing-station--1520399 ; TO7: https://www.to7network.com/ | **A-** for Wingu launch/existence; **B** for trade launch details; **C** for directory-only rack/capacity claims. |
| **PAIX JIB1 / PAIX Djibouti** with Djibouti Sovereign Fund | Djibouti - Djibouti City; Rue de Geneve appears in directory/trade records | Announced/planned. Up to 5 MW and first phase targeted 2026 are announcement facts, not operational capacity. Re-check for construction or launch before coding above `announced`. | DCD: https://www.datacenterdynamics.com/en/news/paix-data-centres-plans-5mw-data-center-in-jv-with-djibouti-sovereign-fund/ ; SubTel Forum: https://subtelforum.com/paix-to-open-data-centre-in-djibouti/ ; W.Media release syndication: https://w.media/paix-partners-with-djiboutis-sovereign-fund-to-build-data-centers/ ; DataCenterMap: https://www.datacentermap.com/djibouti/djibouti-city/paix-djibouti/ ; PAIX LinkedIn announcement may be useful but remains social-source evidence. | **B** for DCD/SubTel announcement and 5 MW/2026 target; **C** for directory racks/floor-area/address unless confirmed by PAIX/FSD. Upgrade to **A-** only with direct PAIX/FSD release. |
| **Djibouti Telecom cable landing and data-centre/colocation infrastructure** | Djibouti - Haramous, YAC, Ras Dika, Siesta/new CLS, Djibouti City | Operational telecom/cable infrastructure. Count as datacenter only when the source names data centre, colocation, server hosting or facility function. Cable landing by itself is not a commercial DC. | Djibouti Telecom international site: https://international.djiboutitelecom.dj/ ; DARE1 page: https://international.djiboutitelecom.dj/dare1/hormuud-telecom-joins-as-new-member-of-dare1/ ; 2Africa landing via SubTel Forum: https://subtelforum.com/2africa-lands-in-djibouti-with-djibouti-telecom/ ; DCD new CLS: https://www.datacenterdynamics.com/en/news/djibouti-to-get-new-data-center-and-cable-landing-stations/ ; DCD 2Africa landing: https://www.datacenterdynamics.com/en/news/worlds-longest-subsea-cable-lands-in-djibouti-east-africa/ | **A** for Djibouti Telecom pages and official cable/operator releases; **B** for DCD/SubTel details; **C** for unsourced "two data centres" counts. |
| **ANSIE / national data center hosting service** | Djibouti - likely Djibouti City, but address/operator not named | Official government hosting-service evidence, not yet a resolved facility. Use as a lead for a government/national data centre; do not count separately until site/operator/address is found. | Presidency Council of Ministers 2023-11-14: https://www.presidence.dj/conseil-des-ministres/2023-11-14 | **A** for existence of ANSIE hosting service in a national data center; **C/unknown** for physical location, operator, capacity and whether it is distinct from Djibouti Telecom/Wingu infrastructure. |
| **AMS-IX Djibouti / DjIX** | Djibouti - hosted at Djibouti Data Center SARL | Operational IXP/interconnection record. Not a datacenter facility by itself, but confirms DDC as an active interconnection site. | AMS-IX market page: https://www.ams-ix.net/dji ; AMS-IX launch/news page: https://www.ams-ix.net/dji/news/the-wingu-groups-partnership-with-ams-ix-in-djibouti-is-now-live-as-the-djibouti-internet-exchange-becomes-ams-ix-djibouti ; PeeringDB IX: https://www.peeringdb.com/ix/967 ; Wingu AMS-IX post: https://www.wingu.africa/latest-news/wingus-partnership-with-ams-ix-in-djibouti-is-now-live | **A** for AMS-IX and PeeringDB IXP metadata; use only as support for DDC, not as capacity. |

Alias and dedupe rules:
- `DDC`, `Djibouti Data Center`, `Djibouti Data Center SARL`, `Wingu Africa Djibouti`, and `Wingu Africa Djibouti 1` may describe the same older Djibouti City facility. Dedupe before counting.
- `Wingu TO7`, `TO7 Technology Park`, `Djibouti's second carrier-neutral data center`, and `Djibouti City 2` may describe the newer Wingu/TO7 facility.
- `PAIX JIB1`, `PAIX Djibouti`, and `PAIX/FSD Djibouti` are the announced PAIX project.
- `DjIX` and `AMS-IX Djibouti` are the same IXP brand transition/operation after the 2024 AMS-IX/Wingu partnership.

---

## 2. Operator and Facility Queries

```text
"Djibouti" "data center" OR "data centre" OR datacenter OR "centre de donnees" colocation OR colo
"Wingu" Djibouti "TO7" OR "Technology Park" OR "carrier-neutral" OR "CLS" OR "3 MW"
site:wingu.africa Djibouti "data centre" OR "data center" OR colocation OR "TO7"
"Djibouti Data Center" OR "Djibouti Data Centre" Wingu OR "Djibouti Telecom"
"PAIX" Djibouti JIB1 OR "5MW" OR "5 MW" OR "Sovereign Fund"
"Djibouti Telecom" "data centre" OR "data center" OR colocation OR "cable landing station"
ANSIE Djibouti "centre de donnees national" OR "DATA CENTER" OR hebergement
site:ams-ix.net Djibouti OR "Djibouti Internet Exchange"
site:peeringdb.com Djibouti "Djibouti Data Center" OR "AMS-IX"
```

Lifecycle queries:
```text
"Djibouti" "data center" announced OR launched OR inaugurated OR commissioned OR operational
"Djibouti" "centre de donnees" annonce OR inaugure OR "mise en service" OR operationnel
"Djibouti" "data center" construction OR groundbreaking OR "under construction"
```

---

## 3. Connectivity, Subsea and IXP Evidence

Connectivity records are high-value leads, but cable landings and PoPs must not be counted as datacenters without separate facility/hosting evidence.

Verified/high-value anchors:
- 2Africa landed in Djibouti with Djibouti Telecom in May 2022; SubTel Forum carries the Djibouti Telecom release: https://subtelforum.com/2africa-lands-in-djibouti-with-djibouti-telecom/
- DCD covered the 2Africa landing and Djibouti Telecom's new cable landing station: https://www.datacenterdynamics.com/en/news/worlds-longest-subsea-cable-lands-in-djibouti-east-africa/
- Djibouti Telecom DARE1 page: https://international.djiboutitelecom.dj/dare1/hormuud-telecom-joins-as-new-member-of-dare1/
- AMS-IX Djibouti is live as an IXP with Wingu/DDC context: https://www.ams-ix.net/dji

Cable and IXP queries:
```text
"landing station" Djibouti Haramous OR "Ras Dika" OR YAC OR Siesta
"2Africa" Djibouti landing "Djibouti Telecom"
"DARE1" "Djibouti Telecom" Somtel OR Hormuud
"PEACE" cable Djibouti "Haramous" OR "Djibouti Telecom"
"IEX" cable Djibouti OR "Africa-1" Djibouti
"Djibouti" "cable landing station" "data center" OR colocation
"Djibouti" "internet exchange" OR DjIX OR "AMS-IX Djibouti"
```

Handling:
- Create/update a data-centre record from a CLS only if the source says the building includes colocation/data-centre/server-hosting space.
- Record cable systems as connectivity context on the nearest facility; do not inflate facility counts.
- For cable counts, use current operator/cable records. Counts vary by year and by whether planned/under-construction systems are included.

---

## 4. Trade Press and Monitoring Feeds

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Dynamics | https://www.datacenterdynamics.com/ | DDC history, Wingu TO7, PAIX JIB1, Djibouti Telecom CLS/cables | B/B+ |
| SDxCentral | https://www.sdxcentral.com/ | Wingu TO7 launch and cable/connectivity context | B |
| SubTel Forum | https://subtelforum.com/ | 2Africa landing, PAIX announcement, cable-system news | B |
| Capacity / Connecting Africa | https://www.capacitymedia.com/ ; https://www.connectingafrica.com/ | PoP, subsea, operator partnerships | B |
| African Business | https://african.business/ | PAIX/FSD and market context | B |
| Agence Ecofin | https://www.agenceecofin.com/ | French telecom/regulator/cable market reporting | B |
| Telecompaper | https://www.telecompaper.com/ | Wingu TO7 launch corroboration | B |
| Wingu / TO7 / PAIX / Djibouti Telecom | https://www.wingu.africa/ ; https://www.to7network.com/ ; https://paix.io/ ; https://international.djiboutitelecom.dj/ | Operator-side facts and announcements | A/A- |
| ADI / La Nation / RTD | https://adi.dj ; https://www.lanation.dj ; https://rtd.dj/ | Local official/state event coverage | B; A only for reproduced official documents |

Feed queries:
```text
site:datacenterdynamics.com Djibouti "data center" OR "data centre" OR cable OR Wingu OR PAIX
site:sdxcentral.com Djibouti Wingu OR "data center" OR "cable landing"
site:subtelforum.com Djibouti 2Africa OR PAIX OR cable
site:connectingafrica.com Djibouti Wingu OR Omantel OR "data center" OR PoP
site:agenceecofin.com Djibouti "data center" OR datacenter OR telecoms OR cables
site:african.business Djibouti "data centre" OR PAIX OR Wingu
site:telecompaper.com Djibouti Wingu "data centre" OR "TO7"
```

---

## 5. Directories and Aggregators

Use directories for aliases, addresses and nearby-facility checks. Do not use them as final facility evidence without operator, official or strong press corroboration.

High-yield directory pages:
- Baxtel DDC: https://baxtel.com/data-center/djibouti-data-center-ddc
- DataCenterMap DDC: https://www.datacentermap.com/djibouti/djibouti-city/djibouti-data-center-ddc/
- DataCenterMap PAIX Djibouti: https://www.datacentermap.com/djibouti/djibouti-city/paix-djibouti/
- DataCenters.com Wingu: https://www.datacenters.com/wingu-africa-djibouti
- Cloudscene Djibouti market: https://cloudscene.com/market/data-centers-in-djibouti/djibouti
- OCOLO Wingu Djibouti City 2: https://www.ocolo.io/colocation/winguafrica/djibouti-city-2-djibouti/

Directory rules:
- Treat Baxtel/DataCenterMap/DataCenters.com/Cloudscene/OCOLO as **C** unless they link to or reproduce operator-source facts.
- Directory MW, rack, sqft and count fields stay `claimed_*` or notes until verified.
- Watch stale counts: aggregator country pages may omit PAIX, TO7 or newer changes.
- Do not create a record for "Wingu Data Center Djibouti" and "DDC" separately unless source text proves two separate physical sites. The separate newer Wingu/TO7 facility is distinguishable by TO7 Technology Park/CLS wording.

Directory queries:
```text
site:baxtel.com Djibouti "data center" OR "data centre" OR Wingu OR PAIX
site:datacentermap.com/djibouti Djibouti "data center" OR PAIX OR Wingu
site:datacenters.com Djibouti Wingu OR PAIX OR "data center"
site:cloudscene.com Djibouti "data center"
site:ocolo.io Djibouti Wingu OR "data center"
site:peeringdb.com/fac Djibouti OR "Djibouti City"
```

---

## 6. Hyperscaler and Cloud-Provider Status

Official provider pages to check every run:
- AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ and https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud: https://cloud.google.com/about/locations
- Oracle Cloud: https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

As of 2026-08-12, no Djibouti public cloud region appears on these official pages. Do not create a cloud-region facility from:
- Meta/2Africa cable participation.
- CDN/cache/edge/PoP references.
- Omantel/Wingu or other point-of-presence partnerships.
- Wingu Cloud Exchange or cloud-connect products unless they name a physical facility already counted.
- Reseller/partner claims that workloads can be served in Djibouti.

Cloud queries:
```text
site:aws.amazon.com Djibouti "Region" "Availability Zone"
site:learn.microsoft.com/azure Djibouti "Azure region"
site:cloud.google.com/about/locations Djibouti "region"
site:oracle.com/cloud Djibouti "cloud region"
"Djibouti" "AWS region" OR "Azure region" OR "Google Cloud region" OR "Oracle Cloud region"
```

---

## 7. Industry Bodies, Certification and Events

- **AMS-IX** is the most important industry-body signal for Djibouti because AMS-IX Djibouti confirms active interconnection at DDC.
- **Uptime Institute**: no Djibouti award/certification record surfaced during this review. Treat "Tier 3" or "Tier III" wording for Wingu/TO7/DDC as operator/trade wording unless an Uptime page is found.
- **Smart Africa, AfPIF, Datacloud Africa and regional telecom events** can reveal operators and partnerships, but they are usually B/C unless they point to facility pages or official documents.
- **Africa Data Centres Association / market roundups** are market context, not facility proof.

Queries:
```text
site:uptimeinstitute.com Djibouti "Data Center" OR "Data Centre" OR Wingu OR PAIX
site:ams-ix.net Djibouti members OR participants OR news
"Smart Africa" Djibouti cloud OR "economie numerique" OR "data center"
"AfPIF" Djibouti Wingu OR peering OR "Djibouti Telecom"
"Datacloud Africa" Djibouti Wingu OR PAIX OR "data centre"
```

---

## 8. Per-Division Industry Discovery Map

| Division | Industry search set | Expected result / coding guidance |
|---|---|---|
| **Djibouti** | `"Djibouti City" "data center" OR "data centre" OR colocation OR "Tier III" OR MW`; `"Haramous" OR "Boulaos" OR "Siesta" OR "Ras Dika" Djibouti "data center" OR CLS`; `"Wingu" TO7 Djibouti`; `"PAIX" Djibouti JIB1`; `"Djibouti Telecom" "cable landing station"`; AMS-IX/PeeringDB/directories | Positive cluster. Count DDC/Wingu, Wingu TO7, Djibouti Telecom data-centre/CLS records only with facility wording, AMS-IX as IXP context, and PAIX as announced/planned. |
| **Arta** | `"Arta" Djibouti "data center" OR "data centre" OR "centre de donnees" OR "server room" OR "salle serveur"`; `"Arta" Djibouti colocation OR hebergement OR fibre` | Expected negative for commercial colo. Keep telco/NGO/government rooms out unless facility-level evidence exists. |
| **Ali Sabieh** | `"Ali Sabieh" Djibouti "data center" OR "centre de donnees" OR "salle serveur"`; `"Ali Sabieh" Djibouti ICT OR customs OR fibre` | Expected negative; customs/logistics ICT is not a datacenter without hosting/colo evidence. |
| **Dikhil** | `"Dikhil" Djibouti "data center" OR "centre de donnees"`; `"Dikhil" Djibouti geothermal OR fibre OR ICT` | Expected negative; geothermal/power leads are context only. |
| **Obock** | `"Obock" Djibouti "data center" OR "centre de donnees" OR "salle serveur"`; `"Obock" Djibouti port ICT OR fibre OR telecom` | Expected negative; port/telco rooms need explicit evidence. |
| **Tadjourah** | `"Tadjourah" Djibouti "data center" OR "centre de donnees" OR "salle serveur"`; `"Tadjourah" Djibouti port ICT OR fibre OR telecom` | Expected negative; port ICT and backbone PoPs are not commercial DCs by default. |

For every negative division, output a dated search note and `no_projects: true`; do not omit the division.

---

## 9. Output and Verification Workflow

1. Start from primary/operator sources: Wingu, Djibouti Telecom, AMS-IX/PeeringDB, PAIX/FSD if available, official cable releases.
2. Dedupe aliases and separate physical facilities before counting.
3. Assign physical division by location. Haramous, Boulaos, Rue de Geneve, Ras Dika, Siesta and TO7 Technology Park are all in the **Djibouti** division/city.
4. Split operating and announced capacity:
   - DDC: capacity unknown unless operator source found; directory ~1 MW is C.
   - Wingu TO7: use `announced_capacity_mw` or `design_capacity_mw` for 3 MW unless operator technical evidence confirms live IT load.
   - PAIX JIB1: use `announced_capacity_mw: 5`; status `announced/planned`.
5. Treat IXP, cable landing, PoP and CDN/cache records as adjacency/context unless there is explicit data-centre/colocation wording.
6. Escalate each surviving candidate through `explorer-official.md` for regulator, legal, land, power and government evidence.
7. Re-run hyperscaler exclusion and all six division searches each batch.

Recommended record shape:
```json
{
  "country_code": "DJ",
  "country_name": "Djibouti",
  "division": "Djibouti",
  "name": "Wingu TO7 Technology Park Data Centre",
  "status": "operational",
  "operator": "Wingu Africa / Wingu Group",
  "developer": "Wingu Africa with TO7 Network",
  "capacity_mw": null,
  "announced_capacity_mw": 3,
  "racks": null,
  "source_urls": ["https://www.wingu.africa/latest-news/djibouti-president-inaugurates-wingu-tier-3-carrier-neutral-data-centre"],
  "evidence_date": "2026-08-12",
  "evidence_grade": "A-",
  "notes": "Launched/inaugurated Nov 2024; 3 MW and Tier 3 wording should remain claim-specific unless confirmed by an independent certification or technical sheet."
}
```

Status ladder: rumour < MoU < announced < land acquired < permit applied < permit granted < construction started < commissioned/inaugurated < operational.

---

## 10. Common False Positives

- DIFTZ/free-zone marketing treated as a datacenter.
- 2Africa, PEACE, DARE1 or other submarine cables counted as datacenters.
- Omantel/Wingu and other PoP/edge/CDN/cloud-connect announcements counted as facilities.
- `DjIX`/`AMS-IX Djibouti` counted as a separate data centre instead of an IXP hosted at/associated with DDC.
- Multiple directory aliases for DDC counted as multiple facilities.
- PAIX JIB1 5 MW treated as operational before construction/commissioning evidence.
- Wingu TO7 "Tier 3" wording upgraded to Uptime-certified without an Uptime Institute record.
- Directory rack/MW/sqft values treated as official capacity.
- Telco exchanges/server rooms outside Djibouti City counted as commercial colocation without explicit service evidence.

## 11. URL Validation Notes From This Review

- Current useful primary/operator URLs: Wingu https://www.wingu.africa/markets/djibouti and https://www.wingu.africa/latest-news/djibouti-president-inaugurates-wingu-tier-3-carrier-neutral-data-centre ; AMS-IX https://www.ams-ix.net/dji ; PeeringDB https://www.peeringdb.com/ix/967 ; Djibouti Telecom international site https://international.djiboutitelecom.dj/
- The old Djibouti Telecom `/data-centre-colocation/` path under `international.djiboutitelecom.dj` returned 404 in this review and should not be used as a live primary source.
- DCD, SDxCentral, African Business, Capacity and some directory pages may return 403/429 to curl/HEAD but are real pages discoverable in web search. Record them as trade/directory evidence, not as official proof.
- Search result snippets confirmed live/current Wingu Djibouti and TO7 pages; use those over stale directory claims whenever possible.
