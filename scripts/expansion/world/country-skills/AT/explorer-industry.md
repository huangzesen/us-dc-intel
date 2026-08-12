# AT Explorer Industry - Austria Datacenter Discovery via Trade Press, Associations, Operators, IXPs, Aggregators

Date reviewed: 2026-08-12. Scope: Austria (AT), all 9 Bundesländer/states: Burgenland; Carinthia/Kärnten; Lower Austria/Niederösterreich; Upper Austria/Oberösterreich; Salzburg; Styria/Steiermark; Tyrol/Tirol; Vorarlberg; Vienna/Wien.

Purpose: use operator pages, trade press, associations, IXPs, PeeringDB and aggregators to discover Austrian datacenter facilities and projects, then push each lead back to primary evidence where possible. Reliability grades: **A** = operator/official/primary source for the specific fact; **B** = reliable press or industry body; **C** = aggregator/listing/weak source; **U** = unresolved rumor or unsupported claim.

---

## 0. Market frame

- Austria is strongly Vienna-centered for colocation and interconnection. DataCenterMap currently lists 52 Austrian facilities from 36 operators (C seed list only, https://www.datacentermap.com/austria/). Digital Realty, AtlasEdge, A1, BRZ and VIX make Vienna the first search priority.
- Secondary confirmed clusters are Graz/Styria and Linz-Perg/Upper Austria. Graz has Magenta/COOLtec/Nexspace and Citycom evidence; Linz/Perg have LINZ AG TELEKOM, eworx and Technologiezentrum Perg evidence.
- Hyperscaler status: Microsoft Azure **Austria East** is operational/listed by Microsoft in Vienna (A, https://learn.microsoft.com/en-us/azure/reliability/regions-list). Google is building/in development at Kronstorf, Upper Austria (A for Google announcement, https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-data-center-austria/; Google locations page https://datacenters.google/locations). Google Nickelsdorf/Burgenland is a rumor/debate only (U for project status, B for press coverage of speculation, https://burgenland.orf.at/stories/3365457/). No official AWS or OCI Austria region was identified (AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/; OCI: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
- Austria is landlocked. Do not run submarine cable landing-station workflows. Use VIX, PeeringDB, terrestrial routes, carrier PoPs and fiber/broadband maps.
- VIX/Vienna Internet eXchange is a primary interconnection source: VIX says it has operated since 1996 and is present at three Vienna locations (https://www.vix.at/en/; locations https://www.vix.at/en/about-vix/locations). Its member and location pages are high-value discovery inputs for Vienna operators.
- A national DC association does exist: Austrian Data Center Association/ADCA (A/B for its own membership/association facts, https://austriandatacenter.org/). The draft claim that no dedicated Austrian DC association was found is superseded. ADCA is useful for operator/member discovery and for public event breadcrumbs such as Tag der offenen Rechenzentren.
- A1 materially changes low-density-state coverage: A1 Digital states the Vienna datacenter is one of 14 A1 datacenters in Austria and that A1 offers space in every provincial capital (A for A1's own statement, https://www.a1.digital/de/presse/a1-exoscale-public-cloud-zone/). This supports a search lead in all 9 states, but not exact addresses or public colo availability in each city unless separately sourced.

---

## 1. Industry source stack

### 1.1 Operator and primary industry sources

Use these first when a facility name/operator is known:

- Digital Realty Vienna: https://www.digitalrealty.com/data-centers/emea/vienna, including VIE1/VIE2 and VIE13 (A). PeeringDB for VIE1/2 interconnection: https://www.peeringdb.com/fac/67 (C/B for interconnection metadata).
- AtlasEdge Vienna: https://atlasedge.com/data-centres/vienna/ (A). Lists VIE001 and planned VIE002; use its own page for current/planned status, not aggregator MW claims.
- A1 Datacenter Services: https://www.a1.net/business/digitale-loesungen/enterprise-loesungen/it-infrastruktur-loesungen/hybrid-cloud-datacenter/a1-datacenter-services (A). A1/Exoscale Vienna cloud-zone statement: https://www.exoscale.com/datacenters/austria/ (A for Exoscale service location) and A1 Digital press: https://www.a1.digital/de/presse/a1-exoscale-public-cloud-zone/ (A for A1 statement).
- BRZ/Bundesrechenzentrum: https://www.brz.gv.at/ (A).
- VIX: https://www.vix.at/en/ and https://www.vix.at/en/about-vix/locations (A).
- LINZ AG TELEKOM data centers: https://www.linzag-telekom.at/ueber-uns/unsere-it-und-data-center-neu and 2025 press release https://presse.linzag.at/news-pressekonferenz-eroeffnung-neues-it-und-data-center?id=218235&l=deutsch&menueid=32983 (A).
- eworx datacenter: https://www.eworx.at/datacenter/ (A/B for operator statement: Linz and Perg).
- Technologiezentrum Perg / Data Center Perg: https://www.tzperg.at/ (B/A for its own facility/service statement).
- Magenta Graz: https://newsroom.magenta.at/2022/05/23/digitalisierungsstandort-steiermark-neues-magenta-rechenzentrum-in-graz-eroeffnet/ and planning release https://newsroom.magenta.at/2021/03/08/neues-rechenzentrum-in-graz-staerkt-digitale-infrastruktur-der-steiermark/ (A).
- Nexspace Graz: https://www.nexspace.de/data-centers/graz (operator page; A/B for current marketed location).
- Citycom Graz: https://citycom.at/en/home-en/ plus PeeringDB https://www.peeringdb.com/fac/1119 and network page https://www.peeringdb.com/net/16308 (B/C; confirms network/datacenter breadcrumbs, still verify facility details before counting MW).
- Google Kronstorf: Google press corner https://www.googlecloudpresscorner.com/2026-04-23-Google-Breaks-Ground-on-Data-Center-in-Kronstorf%2C-Austria, Google blog https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-data-center-austria/, Google locations https://datacenters.google/locations (A).
- Digital Burgenland/EBRZ: https://www.ebrz.at/ (B/A for public IT provider/self-description; verify facility claims before classing as public colocation).

### 1.2 Associations and member lists

- Austrian Data Center Association (ADCA): https://austriandatacenter.org/ (A/B). Use members/news to seed Austrian DC operators, builders and certifiers. It states it is a nonprofit association representing Austrian datacenter operators and was founded in 2023.
- ISPA Austria: https://www.ispa.at/ (A for own member list/statements). Use ISP/hosting member list as a lead list.
- EuroCloud Austria: https://www.eurocloud.at/ (B). Use for Austrian cloud/sovereign-cloud provider discovery.
- WKO/Wirtschaftskammer: https://www.wko.at/ (A for own guidance; useful EEffG and IT-sector material).
- Österreichs Energie: https://oesterreichsenergie.at/ (B/A for energy-industry materials; useful for DSO net-development-plan breadcrumbs).
- ACOnet / University of Vienna ZID network context: VIX and ACOnet are run through University of Vienna infrastructure; use VIX official pages first.

### 1.3 Press sources by reliability

- B-grade national/regional: ORF regional (`ooe.orf.at`, `steiermark.orf.at`, `burgenland.orf.at`, `wien.orf.at`, `noe.orf.at`, `salzburg.orf.at`, `tirol.orf.at`, `kaernten.orf.at`, `vorarlberg.orf.at`), derStandard (https://www.derstandard.at/), Die Presse (https://www.diepresse.com/), Kurier (https://kurier.at/), Kleine Zeitung (https://www.kleinezeitung.at/), OÖ Nachrichten/nachrichten.at (https://www.nachrichten.at/), Computerwelt (https://computerwelt.at/), itwelt (https://itwelt.at/).
- B-grade international DC press: DataCenterDynamics Austria tag/source pages (https://www.datacenterdynamics.com/en/tags/austria/), datacenter-insider.de.
- C-grade or lead-only: DataCenterMap, Baxtel, Datacenters.com, ocolo, colocationm, datacenterplatform, Herold, Savecall, local sponsored posts and provider directories. Use them to find names/addresses, then upgrade only with primary evidence.

---

## 2. Operator seed list by state

### Vienna/Wien

- Digital Realty Vienna campus/facilities: A for operator-listed facilities at https://www.digitalrealty.com/data-centers/emea/vienna. The page lists three Vienna data centers and direct access to VIX. DCD reported an Interxion/Digital Realty Vienna land acquisition for up to 40 MW IT capacity (B for expansion report; verify current status before counting built capacity: https://www.datacenterdynamics.com/en/news/digital-realtys-interxion-acquires-land-near-vienna-campus-40mw-data-center/).
- AtlasEdge Vienna: A for VIE001 and planned VIE002 from https://atlasedge.com/data-centres/vienna/. DCD confirms acquisition/expansion context (B, https://www.datacenterdynamics.com/en/news/atlasedge-acquires-data-center-in-vienna-austria/). Do not use Baxtel/Datacenters.com MW without labeling C.
- A1 / Exoscale: A1 Datacenter Services (A) and Exoscale Vienna zone in A1 NGDC (A): https://www.a1.net/business/digitale-loesungen/enterprise-loesungen/it-infrastruktur-loesungen/hybrid-cloud-datacenter/a1-datacenter-services; https://www.exoscale.com/datacenters/austria/. A1 Digital states 14 Austrian A1 datacenters and coverage in every provincial capital (A for this statement, https://www.a1.digital/de/presse/a1-exoscale-public-cloud-zone/).
- BRZ: A for federal IT/datacenter operator, https://www.brz.gv.at/.
- VIX/VIX1-3: A for three Vienna IXP locations, https://www.vix.at/en/about-vix/locations.
- T-Systems/T-Center, Raiffeisen/Raitec, S&T/Kapsch/other Vienna enterprise DCs: keep as leads unless current operator pages are found. Herold and DataCenterMap are C only.
- Microsoft Azure Austria East: A for cloud region in Vienna via Microsoft Learn (https://learn.microsoft.com/en-us/azure/reliability/regions-list). Physical addresses and individual AZ municipalities remain undisclosed.

### Lower Austria/Niederösterreich

- Official Rechenzentren-Strategie NÖ is the main lead source (A): press release https://www.noe.gv.at/noe/Niederoesterreich_praesentiert_Rechenzentren-Strategie.html and PDF press release https://www.noe.gv.at/noe/pressAnnouncement/getPdf/119602.
- A1 provincial-capital coverage means St. Pölten should be checked as a likely A1 regional facility lead, but no address should be asserted from the A1 Digital source alone.
- Near-Vienna Microsoft/Azure spillover is plausible but not sourced; keep unassigned unless municipality or operator evidence appears.
- Herold/DataCenterMap listings for Wiener Neustadt or other NÖ locations are C seeds only.

### Upper Austria/Oberösterreich

- Google Kronstorf: A for Google construction/in-development announcement (https://www.googlecloudpresscorner.com/2026-04-23-Google-Breaks-Ground-on-Data-Center-in-Kronstorf%2C-Austria; https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-data-center-austria/; https://datacenters.google/locations). DCD supports extra details such as 70 ha site and 42,000 sqm project scope (B, https://www.datacenterdynamics.com/en/news/google-breaks-ground-on-data-center-in-kronstorf-austria/). ORF supports the UVP/no-UVP controversy and construction context (B, https://ooe.orf.at/stories/3362467/).
- LINZ AG TELEKOM: A for Data Center Linz 1 and Linz 2 from operator/press pages (https://www.linzag-telekom.at/ueber-uns/unsere-it-und-data-center-neu; https://presse.linzag.at/news-pressekonferenz-eroeffnung-neues-it-und-data-center?id=218235&l=deutsch&menueid=32983).
- eworx: A/B for operator-stated datacenter locations Linz and Perg (https://www.eworx.at/datacenter/).
- Data Center Perg / Technologiezentrum Perg: B/A for its own current service statement (https://www.tzperg.at/).
- A1 provincial-capital coverage makes Linz a lead independent of other sources; exact facility details still require A1/operator evidence.

### Salzburg

- A1 provincial-capital coverage makes Salzburg city a lead, but no exact address was verified from reviewed sources.
- Fragmentix AI/datacenter articles are C leads until an operator, permit, grid, or procurement source confirms status.
- Search Salzburg Netz and Salzburg state/city permits before counting any new project.

### Styria/Steiermark

- Magenta Graz: A for opening/inbetriebnahme from Magenta newsroom (https://newsroom.magenta.at/2022/05/23/digitalisierungsstandort-steiermark-neues-magenta-rechenzentrum-in-graz-eroeffnet/). ORF confirms opening and investment level (B, https://steiermark.orf.at/stories/3157595/). derStandard gives useful area/rack/MW details from reporting (B, https://www.derstandard.at/story/2000135968031/magenta-austria-eroeffnete-neues-rechenzentrum-in-graz), but keep technical figures tied to that source.
- COOLtec/Nexspace Graz: Nexspace currently markets Graz data center locations at Alte Poststraße 390 and 376 (A/B, https://www.nexspace.de/data-centers/graz). COOLtec involvement is A/B via Magenta release and COOLtec/project partner pages.
- Citycom Datacenter Graz: C/B via PeeringDB facility/network pages (https://www.peeringdb.com/fac/1119; https://www.peeringdb.com/net/16308). Confirm on operator or customer pages before using as high-confidence facility inventory.
- A1 provincial-capital coverage makes Graz a lead independent of Magenta/Nexspace.

### Tyrol/Tirol

- A1 provincial-capital coverage makes Innsbruck a lead, but no exact current address was verified from reviewed sources.
- Magenta Innsbruck colocation appears in third-party listings only in this review; keep C until an operator page confirms.
- Search TINETZ and Innsbruck/Tirol official pages for grid/permit evidence.

### Vorarlberg

- A1 provincial-capital coverage makes Bregenz a lead, but no exact current address was verified from reviewed sources.
- Historical Vorarlberger Rechenzentrum/Dornbirn items are not current facility evidence. Treat as historical C unless a current operator page, Firmenbuch activity plus services page, or procurement/grid source confirms.
- illwerke vkw / Vorarlberger Energienetze may reveal enterprise IT or grid leads, but neither should be counted as a DC without explicit facility evidence.

### Carinthia/Kärnten

- A1 provincial-capital coverage makes Klagenfurt a lead, but no exact current address was verified from reviewed sources.
- Lakeside Science & Technology Park is a technology/ICT cluster (https://lakeside-scitec.com/) and should not be counted as a datacenter on that basis alone.
- Search Kärnten Netz, Klagenfurt and state permits; expect few public leads.

### Burgenland

- Digital Burgenland/EBRZ: B/A lead for public-sector digital services and possible public IT infrastructure, https://www.ebrz.at/. Confirm specific facility claims before listing a datacenter.
- Nickelsdorf: U for project status. ORF reports speculation/talks around a possible up-to-50 ha datacenter in Nickelsdorf (B for the existence of public speculation only, https://burgenland.orf.at/stories/3365457/). Der Standard/profil add debate context, but no operator or authority confirmation was found in reviewed sources. Do not call this a Google project unless Google or official filings identify Google.
- A1 provincial-capital coverage makes Eisenstadt a lead.

---

## 3. Hyperscaler and cloud status

| Provider | Austria status | Evidence and grade | Enumeration rule |
|---|---|---|---|
| Microsoft Azure | Austria East listed/operational in Vienna with AZ support | A: Microsoft Learn regions list https://learn.microsoft.com/en-us/azure/reliability/regions-list | Record cloud region as Vienna. Do not infer physical addresses or spillover municipalities. |
| Google | Kronstorf datacenter in development/construction; Google locations lists Austria in development | A: Google press/blog/locations https://www.googlecloudpresscorner.com/2026-04-23-Google-Breaks-Ground-on-Data-Center-in-Kronstorf%2C-Austria, https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-data-center-austria/, https://datacenters.google/locations | Record Kronstorf, Upper Austria as in development/construction. Do not equate with live GCP Austria region unless Google Cloud locations confirms. |
| AWS | No Austrian region identified | A for official region list: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | Treat AWS Austria DC claims as false/unsupported unless AWS publishes a region/local zone/facility source. |
| Oracle OCI | No Austrian public cloud region identified | A for OCI region docs: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Treat OCI Austria region claims as unsupported. |
| Exoscale/A1 | Vienna cloud zone in A1 NGDC | A: https://www.exoscale.com/datacenters/austria/ | Count as cloud/DC service in Vienna, not as hyperscaler-owned real estate. |

---

## 4. Network and aggregator workflow

### 4.1 VIX and PeeringDB

- Start with VIX locations and member lists: https://www.vix.at/en/ and https://www.vix.at/en/about-vix/locations. VIX identifies three Vienna locations; these provide strong pointers to facility/operator clusters.
- Use PeeringDB for live interconnection breadcrumbs, not as a sole facility authority. Useful AT examples: Digital Realty VIE1/2 facility (https://www.peeringdb.com/fac/67), Citycom Datacenter Graz (https://www.peeringdb.com/fac/1119), GraX exchange (https://www.peeringdb.com/ix/430).
- For every PeeringDB facility, verify at least one of: operator page, customer-facing colocation page, municipal permit, credible press, procurement, or VIX/location page.

### 4.2 Aggregators

- DataCenterMap Austria (C): https://www.datacentermap.com/austria/. Good for initial count and names; weak for current status and technical details.
- Datacenters.com, Baxtel, ocolo, colocationm, datacenterplatform (C): useful for addresses and MW hints. Never use their power, tier, customer-count or status fields without labeling C unless operator corroborates.
- Herold/local directories (C): business-listing evidence only; often enough to find a company name, not a facility.

### 4.3 Query templates

```text
site:datacenterdynamics.com Austria data center OR datacenter
site:derstandard.at Rechenzentrum Österreich
site:orf.at Rechenzentrum Kronstorf OR Nickelsdorf OR Graz
site:ooe.orf.at Rechenzentrum
site:steiermark.orf.at Rechenzentrum
site:burgenland.orf.at Rechenzentrum
site:austriandatacenter.org Mitglieder Rechenzentrum
site:ispa.at Mitglieder Hosting Rechenzentrum
site:vix.at members OR Mitglieder
site:peeringdb.com Austria Vienna Graz Linz datacenter
site:datacentermap.com/austria "<operator>"
"<operator>" "Rechenzentrum" "Österreich"
"<operator>" "data center" Austria
"<city>" "colocation" Österreich
"<city>" "Serverhousing" OR Housing
```

---

## 5. Known facility/project evidence table

| Facility/project | State | Status | Best reviewed source(s) | Grade |
|---|---|---|---|---|
| Microsoft Azure Austria East | Vienna | Operational/listed cloud region | Microsoft Learn regions list | A for region; U for exact sites |
| Digital Realty Vienna VIE1/VIE2/VIE13 | Vienna | Operational facilities | Digital Realty Vienna page; PeeringDB for VIE1/2 interconnection | A facility; C/B interconnection metadata |
| Digital Realty/Interxion Vienna expansion land | Vienna | Expansion lead | DCD 40 MW land-acquisition report | B for report; verify current build status |
| AtlasEdge VIE001 and planned VIE002 | Vienna | Operational/planned per operator page | AtlasEdge Vienna page; DCD acquisition article | A for operator page |
| A1 Austrian datacenter network / Vienna NGDC | Vienna + all provincial capitals as leads | Operational network/service | A1 Datacenter Services; A1 Digital; Exoscale Vienna | A for A1 statements; addresses need separate proof |
| BRZ | Vienna | Operational federal IT/datacenter | BRZ official site | A |
| VIX/VIX1-3 | Vienna | Operational IXP locations | VIX official pages | A |
| Google Kronstorf | Upper Austria | Construction/in development | Google press/blog/locations; DCD for additional specs; ORF for UVP debate | A for project; B for secondary details |
| LINZ AG TELEKOM Data Center Linz 1/Linz 2 | Upper Austria | Operational | LINZ AG TELEKOM pages and press | A |
| eworx Linz/Perg | Upper Austria | Operational per operator | eworx datacenter page | A/B |
| Data Center Perg | Upper Austria | Operational service lead | Technologiezentrum Perg | B/A |
| Magenta Graz | Styria | Operational/opened 2022 | Magenta newsroom; ORF; derStandard for technical details | A/B |
| Nexspace Graz / COOLtec-origin facility | Styria | Current marketed data center | Nexspace operator page; Magenta/COOLtec context | A/B |
| Citycom Datacenter Graz | Styria | Interconnection/facility lead | PeeringDB facility/network; Citycom page | C/B until operator facility page confirms details |
| Digital Burgenland/EBRZ | Burgenland | Public IT/provider lead | EBRZ official site | B/A for provider; facility specifics need proof |
| Nickelsdorf large DC rumor | Burgenland | Unconfirmed | ORF Burgenland speculation report | U project; B only for public speculation |
| Fragmentix Salzburg AI DC | Salzburg | Announced lead only | Local/trade article found in draft | C until primary confirmation |
| A1 Salzburg/Innsbruck/Bregenz/Klagenfurt/St. Pölten/Eisenstadt/Graz/Linz | Salzburg, Tyrol, Vorarlberg, Carinthia, Lower Austria, Burgenland, Styria, Upper Austria | Provincial-capital lead from A1 network statement | A1 Digital says 14 AT DCs and every provincial capital | A for coverage statement; U/C for exact local facility details until sourced |
| Historical VRZ Dornbirn | Vorarlberg | Historical only | Computerwoche-style historical item from draft | C historical; not current |
| Lakeside Park Klagenfurt | Carinthia | ICT park, not DC proof | Lakeside official site | B for park; U for datacenter |

Negative/guardrail findings:

- Equinix Austria/Vienna claims are usually false positives or third-party marketplace noise; no Austrian IBX was confirmed from Equinix official footprint in this review.
- AWS and OCI have no Austria public cloud region in reviewed official sources.
- Google Nickelsdorf is not confirmed by Google or a public permit in reviewed sources.
- UVP databases are not expected to enumerate Austrian DC projects unless future law changes or a related listed project type is triggered.

---

## 6. Reliability rules and pitfalls

- **A:** operator-owned facility/cloud pages; official government, regulator, procurement, grid or legal sources; association pages only for their own members/statements.
- **B:** ORF, DCD, derStandard, Die Presse, Kurier, Kleine Zeitung, nachrichten.at, datacenter-insider, Computerwelt/itwelt, credible engineering/project pages when they describe their own role but not necessarily facility operation.
- **C:** DataCenterMap, Baxtel, Datacenters.com, PeeringDB, ocolo, colocationm, datacenterplatform, Herold, Savecall and general web directories.
- **U:** rumors, unconfirmed buyer/SPV speculation, exact technical figures copied between aggregators, historical references without current operator proof.

Pitfalls:

- `Vienna` often means Vienna, Virginia. Require Austria, Wien, postal code, `.at`, or Austrian operator context.
- `Austria East` is a cloud region label, not an address.
- `Austrian Cloud`, cloud reseller, managed hosting, or ISP membership does not automatically mean a physical datacenter facility.
- A1's all-provincial-capitals statement is strong for coverage leads but weak for local inventory fields. Use it to force searches in all states, not to invent addresses.
- Large MW numbers often come from aggregators or planning rumors. Keep MW C/U unless an operator, permit, grid document, or credible press article states the figure.
- Historical Austrian mainframe/municipal computing entities are common; mark them historical unless a current page markets DC/colo/hosting operations.

---

## 7. Re-check cadence

- Monthly while Austria is active: Google Kronstorf, Nickelsdorf/Burgenland, DCD Austria tag, ORF regional feeds, ADCA news, Digital Realty/AtlasEdge/A1/Magenta/LINZ AG pages.
- Quarterly: Microsoft/AWS/GCP/OCI official region lists, DataCenterMap/Baxtel/PeeringDB/VIX member refresh, A1/Exoscale, auftrag.at/TED procurement queries.
- Annually: state planning portals, NÖ Rechenzentren strategy updates, APG/DSO grid capacity and net-development documents, EEffG reporting-rule changes.
