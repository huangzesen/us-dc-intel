# LI Explorer Industry - Liechtenstein Datacenter Operators, Directories, Press, and Cloud Proximity

Date: 2026-08-12. Scope: industry-side enumeration for physical datacenter, colocation, hosting, cloud, telecom-room, and server-room leads in Liechtenstein. Reliability grades: **A** = operator-owned/official source for its own services, government/regulator/register source, or official cloud-region page; **B** = established press, association, vendor case study, or trade source requiring primary confirmation; **C** = directory/aggregator/SEO listing, usable only as a lead.

Final review note: Liechtenstein is a very small market. Public evidence supports a cluster of local hosting/colo operators, but many details in directories are inconsistent. Use industry sources to seed leads, then confirm every physical facility through operator pages, commune/AHR permits, LKW/AK records, Handelsregister, and geodata.

---

## 0. Market frame

- The LI datacenter universe is small, local, and mainly colo/hosting/MSP oriented. No public evidence found for hyperscale-owned physical facilities in Liechtenstein.
- Probable facility communes from industry evidence: **Vaduz, Schaan, Eschen, Balzers**. Required negative/low-probability sweeps remain: **Gamprin, Mauren, Planken, Ruggell, Schellenberg, Triesen, Triesenberg**.
- Demand drivers: finance, fiduciary services, regulated outsourcing, fintech/crypto, government digitalization, local data-residency expectations, and cross-border Swiss/Austrian connectivity.
- Connectivity is tightly linked to LKW, Telecom Liechtenstein/FL1, SupraNet/QualityNet, SpeedCom/newsnet, vestra ICT/plus.li, and Swiss/Austrian upstreams. Peering and exchange presence should be checked in PeeringDB and Swiss/Austrian IX contexts, but PeeringDB is not permit evidence.

---

## 1. Operator and facility seeds

Grades below are for the specific claim stated, not for every directory specification.

| Operator / entity | Verified source URLs | Facility / lead | Grade | Notes and required confirmation |
|---|---|---|---:|---|
| vestra ICT AG / plus.li | https://vestra-ict.net/ ; https://www.erlebevaduz.li/mitglied/vestra-ict-plus-li/ | Operator states "Unsere Rechenzentren in Eschen und Vaduz"; Vaduz address lead: Landstrasse 107, 9490 Vaduz; directory lead for Eschen: Hub 37. | A for operator-stated Eschen+Vaduz DC existence; B/C for exact physical addresses and specs | Confirm each site with Vaduz/Eschen Bauverwaltung, Handelsregister, geodata, and any LKW/AK traces. |
| SupraNet AG / QualityNet | https://supra.net/ueber-supranet ; https://supra.net/geschaeftskunden/housing | Operator states jointly operated Rechenzentren in **Schaan and Eschen** and describes a ca. 200 m2 datacenter with racks/cages/footprints, redundant power, UPS, diesel, and redundant fiber. | A for operator-stated Schaan+Eschen DC/service existence and housing service; B for technical details unless datasheet/permit confirmed | Directory entries conflict: Eschen Wirtschaftspark 65 and Schaan Im alten Riet 121 appear. Confirm exact active sites with SupraNet/QualityNet and commune permits. |
| SpeedCom AG / newsnet ag | https://www.speedcom.li/ ; https://wirtschaftskammer.li/directory/listing/speedcom-ag | SpeedCom states it operates two independent datacenters in Liechtenstein; WKL lists SpeedCom at Im alten Riet 153, Schaan. | A for operator-stated two LI datacenters; B for WKL address; C for directory specs | Data Center Map has SpeedCom Schaan/newsnet alias at Im alten Riet 153 and a SpeedCom Ruggell entry. Confirm whether the second site is Ruggell, Schaan, or another LI location before counting. |
| Liechtensteinische Kraftwerke (LKW) | https://www.lkw.li ; https://www.lkw.li/userdata/Alle-Download-Dokumente/Netze-Kommunikation/Kollokation/lkw-kollokation-standortliste-v1.4.pdf ; https://www.llv.li/serviceportal2/amtsstellen/amt-fuer-kommunikation/import/pdf-llv-ak-tal_kupfer_standorte_entbuendelung_v1.0.pdf | LKW Kollokation/access-network locations, especially Eschen Hub/Hubstrasse 37. | A for official telecom colocation/access-network existence; B/C for commercial datacenter interpretation | Count as telecom colocation unless operator/AK/LKW evidence supports datacenter/colo service classification. Extract all listed sites as telecom-infrastructure leads. |
| Kyberna AG | https://www.kyberna.ch/ ; directory seeds at https://www.datacentermap.com/liechtenstein/vaduz/kyberna-balzers/ and https://datacentercatalog.com/liechtenstein/kyberna-balzers | Kyberna DataCenter Balzers, Fabrikstrasse 4, 9496 Balzers. | A for company/operator site existence; C for directory address/spec/opening details unless Kyberna source confirms | Search Kyberna pages/materials for `DataCenter`, `Balzers`, `Fabrikstrasse`, then verify with Balzers Bauverwaltung and geodata. |
| ICT-Center / ICT-Center Vaduz | Directory seeds: https://www.datacentermap.com/liechtenstein/vaduz/ict-center-vaduz/ ; https://inflect.com/datacenters/emea/liechtenstein/vaduz | ICT-Center Vaduz, Schwefelstrasse 5A, 9490 Vaduz. | C until an operator/registry/permit source is found | Search Handelsregister, Vaduz permits, PeeringDB org records, and local press. Do not treat directory MW/sq-ft figures as verified. |
| Telecom Liechtenstein AG / FL1 | https://www.fl1.li/ ; https://telecom.li/ | Hosting/cloud/connectivity lead; HQ Schaanerstrasse 1, Vaduz, but no public physical DC page verified in this review. | B lead only | Do not count as datacenter without facility page, permit, PeeringDB facility, or AK/LKW colocation evidence. |
| Swiss/Austrian providers selling into LI | Provider official pages and LI customer references | Cross-border cloud/hosting sold into LI. | C for LI physical facility claims | Count only if the physical facility is inside LI and supported by A/B evidence. |

Operator sweep:

```text
site:{operator-domain} (Liechtenstein OR Vaduz OR Schaan OR Eschen OR Balzers OR Ruggell) ("data center" OR Datacenter OR Rechenzentrum OR Kollokation OR Housing)
"{operator}" "{street}" ("data center" OR Datacenter OR Rechenzentrum)
"{operator}" Liechtenstein ("USV" OR Notstrom OR Diesel OR Racks OR Cages OR Footprints OR MW)
"{operator}" "{Gemeinde}" (Baugesuch OR Baubewilligung OR Baufreigabe)
"{operator}" Handelsregister Liechtenstein
site:peeringdb.com "{operator}" Liechtenstein
```

---

## 2. Directory cross-checks

Directory pages are useful for lead discovery but are not final evidence.

| Directory / source | URL / query | Grade | Known issues / use |
|---|---|---:|---|
| Data Center Map - Liechtenstein/Vaduz market | https://www.datacentermap.com/liechtenstein/ and https://www.datacentermap.com/liechtenstein/vaduz/ | C+ | Useful for seed list. It groups LI under a Vaduz market even when physical sites are in Balzers, Eschen, Schaan, or possibly Ruggell. Confirm each address. |
| Data Center Map operator/facility pages | Search operator pages for vestra, SupraNet, SpeedCom/newsnet, Kyberna, ICT-Center | C | Addresses and specs can conflict with operator sites. Treat as candidate aliases only. |
| Data Center Catalog | https://datacentercatalog.com/liechtenstein | C | Good supplemental seed; specs/opening dates need operator/permit confirmation. |
| Inflect | https://inflect.com/datacenters/emea/liechtenstein/vaduz | C | Lists a small set of LI facilities and addresses; some locality labels are imprecise. Use for cross-check only. |
| colo.exchange / PQ.hosting / DCHub | Search `LKW Kollokation TZ Eschen`, `Liechtenstein data center` | C | LKW Eschen details such as network count/IX count are aggregator data. Confirm with LKW/AK/PeeringDB. |
| PeeringDB | https://www.peeringdb.com/ | B-/C | Good for active interconnection leads and aliases. User-maintained; not permit evidence. |
| WKL directory | https://wirtschaftskammer.li/sektionen-und-verbaende/informatik/ and SpeedCom listing | B | Association/member/address confirmation; not facility proof by itself. |
| local.ch / search.ch / yellowpages.li | Search operator name + address | C | Address support only. |

Directory reconciliation rule:

```text
if directory-only:
  status = lead
  source_grade = C
  required_next = operator page + commune/AHR + geodata + LKW/AK
if operator page confirms datacenter in same commune:
  status = operating/service-stated
  source_grade = A for existence, B for details
if commune/AHR permit confirms construction/use:
  status = permit/construction/operating depending on wording
  source_grade = A
```

---

## 3. Industry associations and context sources

| Source | URL | Grade | Use |
|---|---|---:|---|
| proIT - Verband der IT-Profis in Liechtenstein | https://www.pro-it.li/ and https://www.pro-it.li/mitglieder/ | B | IT company universe and leads, not facility registry. |
| Wirtschaftskammer Liechtenstein | https://wirtschaftskammer.li/ ; https://wirtschaftskammer.li/sektionen-und-verbaende/informatik/ | B | Member discovery and address confirmation for IT firms such as SpeedCom. |
| LIHK / Liechtensteinische Industrie- und Handelskammer | https://www.lihk.li/ | B-/C+ | Business context and policy leads. |
| Digital Liechtenstein | https://digital-liechtenstein.li/ | B | Digital economy/sovereign-cloud context; not facility proof. |
| FMA Liechtenstein | https://www.fma-li.li/ | A for regulator / B context | Financial-sector outsourcing/data-residency context; no facility list. |
| Universität Liechtenstein | https://www.uni.li/ | C+ | Possible server/HPC context only. |

---

## 4. Trade press and vendor case studies

Use press to identify expansions, upgrades, modernization, customers, and permitting milestones. Press is rarely sufficient for final facility records without a matching operator/permit source.

| Source | URL / query | Grade | Use |
|---|---|---:|---|
| Liechtensteiner Vaterland | https://www.vaterland.li/ ; `site:vaterland.li Rechenzentrum OR Datacenter OR Kollokation` | B | Main local business/energy/government sweep. |
| Liechtensteiner Volksblatt archive | https://www.eliechtensteinensia.li/viewer/toc/000476564/1/ and https://www.llv.li/de/medienmitteilungen/volksblatt-archiv-bleibt-bei-landesbibliothek-und-landesarchiv-zugaenglich | B historical | Defunct newspaper; useful for pre-2023 archive searches and older official/business notices, not current monitoring. |
| lie:zeit | https://www.lie-zeit.li/ ; `site:lie-zeit.li Rechenzentrum OR Datacenter OR Baugesuch` | B | Local company/commune coverage. |
| Landesspiegel | https://landesspiegel.li/ ; `site:landesspiegel.li Rechenzentrum OR Energie` | B-/C+ | Policy and energy context. |
| radio.li | https://www.radio.li/ | C+ | Short business/infrastructure leads. |
| Regional CH/AT press | Sarganserlaender, St. Galler Tagblatt, NZZ, Vorarlberger Nachrichten | B-/C+ | Cross-border coverage of LI companies and infrastructure. |
| Vendor case studies | Example query: `SupraNet Rechenzentrum Modernisierung`, `Schaefer IT Systems SupraNet` | B | Can confirm equipment/upgrade details; still verify location and permit separately. |

Press query bundle:

```text
site:vaterland.li Liechtenstein Rechenzentrum OR Datacenter OR Kollokation
site:eliechtensteinensia.li Liechtenstein Rechenzentrum OR Datacenter
site:lie-zeit.li SpeedCom OR SupraNet OR Kyberna OR vestra OR "ICT-Center"
site:landesspiegel.li Energieeffizienz Rechenzentrum Liechtenstein
"SupraNet" Rechenzentrum Modernisierung
"SpeedCom" Datacenter Liechtenstein
"Kyberna" DataCenter Balzers
"vestra" Rechenzentrum Vaduz Eschen
```

---

## 5. Per-division industry strategy

| Commune | Industry priority | Seeds | Search bundle |
|---|---|---|---|
| Vaduz | High | vestra Vaduz; ICT-Center Vaduz; FL1/Telecom lead; banks/government demand | `"Vaduz" Rechenzentrum`; `"Schwefelstrasse 5A" Datacenter`; `"Landstrasse 107" vestra`; `"FL1" Rechenzentrum Vaduz`; `site:datacentermap.com/liechtenstein/vaduz Vaduz` |
| Schaan | High | SpeedCom/newsnet; SupraNet Schaan; LKW HQ; industrial/telecom belt | `"Schaan" Datacenter`; `"Im alten Riet 153" SpeedCom`; `"Im alten Riet 121" SupraNet`; `"newsnet" Schaan Datacenter`; `site:speedcom.li Datacenter` |
| Eschen | High | LKW Hub/Hubstrasse 37; SupraNet/QualityNet Eschen; vestra Eschen; Nendeln locality | `"Eschen" Rechenzentrum`; `"Hub 37" Kollokation`; `"Hubstrasse 37" LKW`; `"Wirtschaftspark 65" SupraNet`; `"vestra" Eschen Rechenzentrum` |
| Balzers | Medium | Kyberna Balzers | `"Balzers" Datacenter`; `"Fabrikstrasse 4" Kyberna`; `"Kyberna" Rechenzentrum`; `site:kyberna.ch Balzers Datacenter` |
| Ruggell | Medium-low | SpeedCom Ruggell directory lead is unconfirmed; industrial/logistics context | `"Ruggell" Datacenter`; `"Speedcom Ruggell Data Center"`; `"Industriering 14" SpeedCom`; `site:ruggell.li Rechenzentrum` |
| Gamprin | Low | Bendern/Unterbendern telecom/industrial leads only | `"Gamprin" Rechenzentrum`; `"Bendern" Kollokation`; `"Unterbendern" Datacenter` |
| Mauren | Low | Schaanwald/Mauren AK/LKW telecom colocation leads | `"Mauren" Rechenzentrum`; `"Schaanwald" Datacenter`; `"Saegenstrasse 11" Kollokation`; `"Weiherring 10" Kollokation` |
| Planken | Very low | No known industry lead | `"Planken" Datacenter`; `"Planken" Rechenzentrum`; `"Planken" Serverraum` |
| Schellenberg | Very low | No known industry lead | `"Schellenberg" Datacenter`; `"Schellenberg" Rechenzentrum`; `"Schellenberg" Serverraum` |
| Triesen | Low | Industrial/service context only | `"Triesen" Rechenzentrum`; `"Triesen" Datacenter`; `"Triesen" Serverraum` |
| Triesenberg | Very low | Telecom/public-building/server-room only | `"Triesenberg" Rechenzentrum`; `"Triesenberg" Datacenter`; `"Malbun" Serverraum` |

---

## 6. Cloud-region handling

Cloud provider pages are A for the logical regions they list. They are C for physical facility inference because exact datacenter sites are not disclosed and none are listed in LI.

| Provider | Official source | Nearest relevant regions | Grade/use |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | Zurich `eu-central-2`, Frankfurt `eu-central-1`, Milan `eu-south-1` | A for region existence. No LI region. No official AWS Vienna/Austria region found in current official region table. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | Switzerland North/West, Austria East `austriaeast` | A for region existence. No LI region. |
| Google Cloud | https://cloud.google.com/about/locations | Zurich `europe-west6`, Milan `europe-west8`, Frankfurt `europe-west3` | A for region existence. No LI region. |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Zurich `eu-zurich-1`, Frankfurt `eu-frankfurt-1` | A for region existence. No LI region. |

Do not create a LI facility from `cloud`, `availability zone`, or `region` marketing unless a physical LI site is explicitly evidenced by operator/regulator/permit records.

Cloud pivots:

```text
"Liechtenstein" "cloud region" OR "availability zone"
"Liechtenstein" ("AWS" OR Azure OR "Google Cloud" OR Oracle) ("datacenter" OR Rechenzentrum)
site:fl1.li Cloud Rechenzentrum
site:vestra-ict.net Cloud Rechenzentrum
site:supra.net Cloud Rechenzentrum
site:speedcom.li Cloud Datacenter
```

---

## 7. Status vocabulary and grading controls

- **Lead only**: `Absicht`, `Planung`, `Projekt`, `Standortsuche`, `Machbarkeit`, `Konzept`, `angekuendigt`, directory-only listing.
- **Permit evidence**: `Baugesuch`, `Auflage`, `Bauverhandlung`, `Baubewilligung`, `Bewilligungsbescheid`, `Baufreigabe`, confirmed by AHR/commune.
- **Construction/operation**: `Baustart`, `Spatenstich`, `Bauabnahme`, `Inbetriebnahme`, `eroeffnet`, active operator service page naming a LI datacenter.
- **Rejected/canceled/retired**: `abgelehnt`, `zurueckgezogen`, `sistiert`, `Beschwerde`, `Einsprache`, `stillgelegt`, `geschlossen`.

Honest grading notes:

- `7 facilities / 5 operators` is a **directory-derived C claim**. Use it only as a reconciliation target, not as an authoritative count.
- Operator pages reviewed support local datacenter/service claims for vestra, SupraNet, and SpeedCom, but exact physical addresses and permits still need commune/AHR confirmation.
- LKW/AK colocation lists are official telecom colocation evidence; classify carefully as telecom colocation/access-network sites unless commercial datacenter evidence exists.
- ICT-Center Vaduz remains directory-led until a direct operator/register/permit source is attached.
- Telecom Liechtenstein/FL1 remains a hosting/cloud/connectivity lead, not a counted datacenter, unless a facility-specific source is found.
- Rural commune negatives are "no public evidence found" findings, not confirmed absence.

---

## 8. Recommended enumeration loop

1. Build seed table from operator pages, Data Center Map, Data Center Catalog, Inflect, PeeringDB, AK/LKW colocation PDFs, WKL/proIT, and local press.
2. Normalize every seed to one of the 11 communes and capture aliases/localities (`Nendeln`, `Schaanwald`, `Bendern`, `Malbun`).
3. For each seed, run operator-domain, commune-domain, AHR/llv.li, LKW, AK, Handelsregister, geodata, and press searches.
4. Promote only when evidence supports the normalized status:
   - C directory -> lead
   - A operator page -> service-stated/operating lead
   - A permit or official colocation/grid record -> official evidence for that exact function
5. Re-run cloud-region pages quarterly and remove any stale assumptions about provider regions.

Final confidence: operator universe B+; official/commune source coverage A; facility addresses/specifications mixed B/C pending permit/geodata confirmation; no-hyperscale-region finding A for current official region pages, B for physical-market negative claim.
