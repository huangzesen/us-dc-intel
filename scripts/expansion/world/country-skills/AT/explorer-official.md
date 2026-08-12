# AT Explorer Official - Austria Datacenter Enumeration via Regulation, Energy/Grid, Planning Permits, Government IT, Cloud Regions

Date reviewed: 2026-08-12. Scope: Austria (AT), all 9 Bundesländer/states: Burgenland; Carinthia/Kärnten; Lower Austria/Niederösterreich; Upper Austria/Oberösterreich; Salzburg; Styria/Steiermark; Tyrol/Tirol; Vorarlberg; Vienna/Wien.

Purpose: use official, regulator, planning, procurement, grid and cloud-region evidence to find and verify Austrian datacenter facilities and projects. Reliability grades are intentionally narrow: **A** = official/primary/operator-owned source for the specific fact; **B** = reliable press, industry body, or regulator-adjacent source; **C** = aggregator/listing/weak source; **U** = unresolved rumor or unsupported claim. Never let one A-grade source upgrade facts it does not actually state.

---

## 0. Austria facts that control the workflow

- Austria is a federal republic with 9 states. Vienna is both a municipality and a state. Enumeration must explicitly cover: Burgenland; Carinthia; Lower Austria; Upper Austria; Salzburg; Styria; Tyrol; Vorarlberg; Vienna.
- There is no national public building-permit register for datacenters. Building and spatial-planning law is state law and implementation is municipal/district level. Look for **Baubewilligung**, **Bauverfahren**, **Bauanzeige**, **Einreichplanung**, **Flächenwidmung**, **Bebauungsplan**, **Raumordnung**, **Betriebsanlage** and **Gewerbeordnung** at state/municipal sources.
- Datacenters are not a named UVP/EIA project type in Austria as of this review. The federal environment ministry explains that UVP applies to project types listed in Annex 1 of UVP-G 2000 (https://www.bmluk.gv.at/themen/klima-und-umwelt/betrieblich_umweltschutz/umweltvertraeglichkeitspruefung-uvp/uvp.html), and the consolidated act is on RIS (https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10010767). ORF reported that the Google Kronstorf construction does not require a UVP, while NGOs and parties are seeking reform (https://ooe.orf.at/stories/3362467/, https://ooe.orf.at/stories/3362857/). Use UVP searches as a negative/control check, not as the primary discovery source.
- Austria has a datacenter energy reporting obligation, but not a public facility register suitable for enumeration. § 72a EEffG requires owners/operators of datacenters with installed IT electrical power of at least 500 kW to publish and report minimum KPIs annually, except protected information. Primary/legal sources: RIS § 72a (https://ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008914&Paragraf=72a), Energieeffizienz-Monitoringstelle page (https://www.energieeffizienzmonitoring.at/rechenzentren/), WKO explainer (https://www.wko.at/noe/industrie/neue-meldepflich-zu-rechenzentren), USP legal-change note (https://www.usp.gv.at/aktuelles/gesetzliche-neuerungen/archiv-fuer-gesetzliche-neuerungen/archiv-bgbl-2024/bundes-energieeffizienzgesetz.html).
- Large-load grid evidence is often more useful than environmental evidence. APG is the transmission system operator; its grid-connection page is real and usable (https://markt.apg.at/en/power-grid/grid-connection/), and APG states no free unrestricted transmission-grid connection capacity is currently available (https://markt.apg.at/netz/netzanschluss/netzanschlusskapazitaeten/). E-Control is the regulator (https://www.e-control.at/) and hosts/links regulatory material.
- Distribution system operators by state are real and should be searched directly: Wiener Netze (Vienna, https://www.wienernetze.at/stromanschluss); Netz Niederösterreich (https://netz-noe.at/); Netz Oberösterreich (https://www.netzooe.at/); Salzburg Netz (https://www.salzburgnetz.at/); Energienetze Steiermark (https://www.e-netze.at/) and Graz Netze/Stromnetz Graz for city-level Graz checks; Kärnten Netz (https://kaerntennetz.at/); TINETZ-Tiroler Netze (https://www.tinetz.at/); Vorarlberger Energienetze (https://www.vorarlbergnetz.at/); Netz Burgenland (https://netzburgenland.at/).
- Broadband/telecom context: RTR is the telecom regulator service organization (https://www.rtr.at/). The Austrian Breitbandatlas is at https://breitbandatlas.gv.at/ and is described by the responsible ministry as the central public broadband-availability platform (https://www.bmwkms.gv.at/themen/telekommunikation-post/breitband/breitbandatlas.html). Use it for fiber/connectivity prioritization, not as a DC source.
- National registers for entity checks: JustizOnline Firmenbuch search (https://justizonline.gv.at/jop/web/firmenbuchabfrage), GISA trade-information system (https://www.gisa.gv.at/), RIS legal database (https://www.ris.bka.gv.at/), Datenschutzbehörde (https://www.dsb.gv.at/).
- Austria is landlocked. Submarine cable landing-station search is not applicable. Replace it with terrestrial backbone, IXP and PeeringDB checks.

Lifecycle vocabulary:

`Standortsuche` < `Widmung` / `Flächenwidmung` < `Bauverfahren` / `Baubewilligung` < `Bauausführung` / `Baubeginn` / `Spatenstich` < `Inbetriebnahme` / `Betriebsaufnahme` < `EEffG-Meldung` for >=500 kW IT power.

Count only **Baubewilligung**, **Baubeginn/Spatenstich**, **Inbetriebnahme**, operator facility page, or direct procurement/grid evidence as strong project evidence. Treat strategy documents, land purchases, rumors and zoning-only materials as planned/lead evidence.

---

## 1. Official source stack

### 1.1 Federal legal and regulatory sources

- RIS (A): https://www.ris.bka.gv.at/. Use for UVP-G 2000, EEffG, ElWOG 2010, TKG 2021, DSG and state-law searches. Query inside RIS and with web search, because RIS URLs can be parameter-heavy.
- Energieeffizienz-Monitoringstelle (A for reporting rules): https://www.energieeffizienzmonitoring.at/rechenzentren/ and electronic platform https://www.energieeffizienzmonitoring.at/elektronische-meldeplattform/.
- E-Control (A): https://www.e-control.at/ and https://portal.e-control.at/. Use for electricity regulation, grid tariffs and market-participant context; do not expect facility names unless there is a grid/regulatory proceeding.
- APG (A): https://www.apg.at/ and market/grid portal https://markt.apg.at/. Search APG for `Netzanschluss`, `Netzentwicklungsplan`, `große Last`, `Umspannwerk`, `Rechenzentrum`.
- RTR (A): https://www.rtr.at/. Use telecom market data and links to central information points; combine with Breitbandatlas (https://breitbandatlas.gv.at/).
- Datenschutzbehörde (A): https://www.dsb.gv.at/. Use only for data-protection context; it is not a DC siting source.

### 1.2 Planning, building and state sources

Primary pattern: start at the state government site and RIS state-law pages, then move to the municipality/district authority named in press or land records. Useful national starting points include the state homepages below and RIS state-law search.

| State | Official portals to start | Permit/planning notes |
|---|---|---|
| Burgenland | https://www.burgenland.at/ | Search `Baugesetz Burgenland`, `Raumplanung`, municipality records, especially Nickelsdorf and Eisenstadt. |
| Carinthia/Kärnten | https://www.ktn.gv.at/ | Search `Kärntner Bauordnung`, `Klagenfurt Rechenzentrum`, `Betriebsanlage`. |
| Lower Austria/Niederösterreich | https://www.noe.gv.at/ and https://www.raumordnung-noe.at/ | Strongest official DC policy source: NÖ Rechenzentren-Strategie press release (https://www.noe.gv.at/noe/Niederoesterreich_praesentiert_Rechenzentren-Strategie.html) and PDF release (https://www.noe.gv.at/noe/pressAnnouncement/getPdf/119602). Use municipality-level zoning/permit follow-up. |
| Upper Austria/Oberösterreich | https://www.land-oberoesterreich.gv.at/ | Google Kronstorf is the key project; search Land OÖ, Bezirk Linz-Land and Marktgemeinde Kronstorf. |
| Salzburg | https://www.salzburg.gv.at/ | Search `Baupolizei`, `Raumordnung`, `Fragmentix`, `Rechenzentrum Salzburg`. |
| Styria/Steiermark | https://www.verwaltung.steiermark.at/ | Graz projects require city and operator cross-checks. Search Graz building/planning plus Energienetze/Graz Netze. |
| Tyrol/Tirol | https://www.tirol.gv.at/ | Search Innsbruck/Tirol building and commercial-operating permits; expect few public DC permit hits. |
| Vorarlberg | https://www.vorarlberg.at/ | Search `Baugesetz`, Dornbirn/Feldkirch/Bregenz, and illwerke/vkw; expect few hits. |
| Vienna/Wien | https://www.wien.gv.at/ | Building authority is MA 37/Baupolizei. Search `site:wien.gv.at Rechenzentrum Baubewilligung`, `Baupolizei Rechenzentrum`, `Flächenwidmung Rechenzentrum`. |

### 1.3 Procurement and government IT

- BRZ/Bundesrechenzentrum (A): https://www.brz.gv.at/. BRZ states it operates one of Austria's largest datacenter environments and is the federal public-sector IT provider. Use BRZ only for federal-government DC/IT infrastructure, not as a list of commercial colocations.
- USP procurement guidance and publication-media list (A): https://www.usp.gv.at/en/themen/betrieb-und-umwelt/laufender-betrieb/weitere-informationen-laufender-betrieb/vergaberecht/ausschreibungsdatenbanken-und-publikationsmedien.html.
- Auftrag.at/app.auftrag.at (A for notices): https://www.auftrag.at/ and https://app.auftrag.at/. Search `Rechenzentrum`, `Colocation`, `Housing`, `Serverraum`, `Cloud`, `Datacenter`, `Betriebsführung`.
- BBG/Bundesbeschaffung (A): https://www.bbg.gv.at/ and BMF description https://www.bmf.gv.at/en/the-ministry/internal-organisation/Procurement-Service-Provider-%28BBG%29-.html. Useful for framework contracts and public-sector cloud/IT demand.
- TED eTendering / EU procurement (A): use https://ted.europa.eu/ for above-threshold Austrian notices; include country filter Austria and CPV filters for IT services/facility construction.

### 1.4 Cloud-region official pages

- Microsoft Azure (A): Microsoft Learn lists **Austria East** with physical location Vienna, Austria, availability-zone support and programmatic name `austriaeast` (https://learn.microsoft.com/en-us/azure/reliability/regions-list). This verifies the cloud region, not exact datacenter addresses. Treat physical location as Vienna / greater Vienna only unless Microsoft publishes more.
- Google (A for company datacenter, A for GCP status when using Google pages): Google announced construction of its Kronstorf datacenter on 2026-04-23 (https://www.googlecloudpresscorner.com/2026-04-23-Google-Breaks-Ground-on-Data-Center-in-Kronstorf%2C-Austria; Google blog: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-data-center-austria/). Google Data Centers locations lists Austria as in development (https://datacenters.google/locations). Do not infer a live Google Cloud region from this; check Google Cloud locations separately before coding any GCP region claim.
- AWS (A): AWS official global infrastructure pages list current regions/AZs (https://aws.amazon.com/about-aws/global-infrastructure/regions_az/; documentation: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html). No Austrian AWS region was identified in official lists during this review.
- Oracle Cloud (A): OCI regions are listed in Oracle documentation (https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). No Austrian OCI public cloud region was identified during this review.
- Equinix (A for its own footprint): Equinix EMEA page states it operates in 20 EMEA countries (https://www.equinix.com/data-centers/europe-colocation); Austria was not identified as an Equinix IBX country in official footprint checks during this review. Beware `Vienna, VA` false positives.

---

## 2. Search vocabulary

### 2.1 Core facility terms

```text
Rechenzentrum
Datenzentrum
Data Center OR Datacenter OR Data Centre
Serverfarm
Colocation OR Co-Location
Housing
Hosting
Cloud-Region OR Cloud Region
Hyperscale OR Hyperscaler
KI-Rechenzentrum OR AI-Rechenzentrum
Digitale Infrastruktur
Internetknoten OR IXP
```

### 2.2 Planning, construction and authority terms

```text
Baugenehmigung OR Baubewilligung Rechenzentrum
Bauverfahren Rechenzentrum
Bauanzeige Rechenzentrum
Einreichplan Rechenzentrum
Flächenwidmung Rechenzentrum
Widmung Rechenzentrum
Bebauungsplan Rechenzentrum
Raumordnung Rechenzentrum
Betriebsanlage Rechenzentrum
Gewerbeordnung Rechenzentrum
Spatenstich Rechenzentrum
Baubeginn Rechenzentrum
Inbetriebnahme Rechenzentrum
```

### 2.3 Energy/grid terms

```text
Netzanschluss Rechenzentrum
Anschlussleistung Rechenzentrum
Umspannwerk Rechenzentrum
110-kV Rechenzentrum
220-kV Rechenzentrum
380-kV Rechenzentrum
Notstromaggregate Rechenzentrum
USV Rechenzentrum
Abwärme Rechenzentrum
Fernwärme Rechenzentrum
Kühlung Rechenzentrum
Energieeffizienzgesetz Rechenzentrum
EEffG Rechenzentrum
```

---

## 3. Query templates that work in Austria

### 3.1 Official/planning

```text
site:<state-domain> Rechenzentrum
site:<state-domain> Rechenzentrum Baubewilligung
site:<municipality-domain> Rechenzentrum
"Rechenzentrum" "<municipality>" "Baubewilligung"
"Rechenzentrum" "<municipality>" "Flächenwidmung"
"Rechenzentrum" "<district>" "Bauverfahren"
"Betriebsanlage" "Rechenzentrum" "<state>"
filetype:pdf "Rechenzentrum" "<state>" "Baubewilligung"
filetype:pdf "Rechenzentrum" "<municipality>" "Gemeinderat"
```

### 3.2 Grid/energy

```text
site:markt.apg.at Rechenzentrum OR Netzanschluss
site:apg.at Rechenzentrum OR "große Last" OR Umspannwerk
site:e-control.at Rechenzentrum OR Netzanschluss
site:<dso-domain> Rechenzentrum
"Netzanschluss" "Rechenzentrum" "<state>"
"Umspannwerk" "Rechenzentrum" "<municipality>"
"Anschlussleistung" "Rechenzentrum" "<operator>"
"Abwärme" "Rechenzentrum" "Fernwärme" "<city>"
```

### 3.3 Procurement/government IT

```text
site:auftrag.at Rechenzentrum
site:app.auftrag.at Rechenzentrum
site:bbg.gv.at Rechenzentrum OR Cloud OR Housing
site:brz.gv.at Rechenzentrum
site:ted.europa.eu Austria Rechenzentrum
"Rechenzentrum" "Ausschreibung" "<state>"
"Colocation" "Ausschreibung" "Österreich"
"Serverraum" "Betriebsführung" "Ausschreibung" "Österreich"
```

### 3.4 Cloud/hyperscaler

```text
"Austria East" "Azure" "Vienna"
site:learn.microsoft.com "Austria East" "austriaeast"
site:datacenters.google "Kronstorf" Austria
site:blog.google "Kronstorf" "data center"
"Google" "Kronstorf" "Baubewilligung" OR "Baugenehmigung"
"Google" "Nickelsdorf" "Rechenzentrum"
site:aws.amazon.com Austria "Region"
site:docs.oracle.com OCI Austria region
```

---

## 4. Division-by-division official workflow

### Vienna/Wien - major hub

Known official/primary anchors: Microsoft Azure Austria East is listed by Microsoft with physical location Vienna (A); Digital Realty has three Vienna data centers in its own location page, including Louis-Häfliger-Gasse facilities and Siemensstraße VIE13 (A, https://www.digitalrealty.com/data-centers/emea/vienna); AtlasEdge operates VIE001 and lists VIE002 planned in Vienna (A, https://atlasedge.com/data-centres/vienna/); A1 markets Austrian datacenter services and its NGDC/Vienna cloud zone relationship with Exoscale (A, https://www.a1.net/business/digitale-loesungen/enterprise-loesungen/it-infrastruktur-loesungen/hybrid-cloud-datacenter/a1-datacenter-services; https://www.exoscale.com/datacenters/austria/); BRZ is in Vienna and operates federal datacenter infrastructure (A, https://www.brz.gv.at/); VIX is at three Vienna locations (A, https://www.vix.at/en/about-vix/locations).

Workflow: search MA 37 / wien.gv.at for permits and zoning; search Wiener Netze and Wien Energie for grid/heat leads; use VIX and PeeringDB only as interconnection evidence; avoid `Vienna, VA` false positives.

Queries:

```text
site:wien.gv.at Rechenzentrum Baubewilligung
site:wien.gv.at Rechenzentrum Baupolizei
"Louis-Häfliger-Gasse" Rechenzentrum Wien
"Siemensstraße" OR "Siemensstrasse" "Rechenzentrum" Wien
"Austria East" "Wien" "Azure"
site:wienernetze.at Rechenzentrum OR Netzanschluss
```

### Lower Austria/Niederösterreich - policy-active, near-Vienna spillover likely

The state published an official Rechenzentren strategy in April 2026 (A, https://www.noe.gv.at/noe/Niederoesterreich_praesentiert_Rechenzentren-Strategie.html; PDF release https://www.noe.gv.at/noe/pressAnnouncement/getPdf/119602). Use it as the best official lead source, then verify each municipality separately. Microsoft Austria East may involve the greater Vienna area, but exact sites are not public; do not assign Azure facilities to Lower Austria without a source naming the municipality.

Queries:

```text
site:noe.gv.at Rechenzentrum
site:raumordnung-noe.at Rechenzentrum
"Rechenzentren-Strategie" "Niederösterreich"
"Rechenzentrum" "Niederösterreich" "Baubewilligung"
"Rechenzentrum" "St. Pölten" OR "Wiener Neustadt" OR Krems
site:netz-noe.at Rechenzentrum OR Netzanschluss
```

### Upper Austria/Oberösterreich - Google Kronstorf plus Linz regional DCs

Google Kronstorf is official construction/in-development evidence (A from Google; B for press details). Google announced the Kronstorf datacenter construction on 2026-04-23 and says it is its first Austrian datacenter, with about 100 direct jobs and heat-recovery readiness (https://www.googlecloudpresscorner.com/2026-04-23-Google-Breaks-Ground-on-Data-Center-in-Kronstorf%2C-Austria; https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/google-data-center-austria/). DCD reports planning-permission and site/area details (B, https://www.datacenterdynamics.com/en/news/google-breaks-ground-on-data-center-in-kronstorf-austria/). ORF and regional press are useful for UVP/debate follow-up.

Other primary anchors: LINZ AG TELEKOM operates IT- und Data Center Linz 1 and Linz 2 (A, https://www.linzag-telekom.at/ueber-uns/unsere-it-und-data-center-neu; press release https://presse.linzag.at/news-pressekonferenz-eroeffnung-neues-it-und-data-center?id=218235&l=deutsch&menueid=32983); eworx states datacenter locations in Linz and Perg (B/A for operator statement, https://www.eworx.at/datacenter/); Technologiezentrum Perg markets Data Center Perg (B, https://www.tzperg.at/).

Queries:

```text
"Google" "Kronstorf" "Rechenzentrum" "Baubewilligung"
site:land-oberoesterreich.gv.at Kronstorf Rechenzentrum
site:kronstorf.at Rechenzentrum
site:netzooe.at Rechenzentrum OR Netzanschluss
"IT- und Data Center Linz" "LINZ AG"
"Data Center Perg" Rechenzentrum
```

### Salzburg - thin market, verify announced projects carefully

No official hyperscale or major state strategy was confirmed. Treat Fragmentix/AI datacenter items as leads until operator, permit or grid evidence is found. A1 states it offers datacenter area in every Austrian provincial capital through its Austrian DC network (A1 Digital press, A, https://www.a1.digital/de/presse/a1-exoscale-public-cloud-zone/), which supports checking Salzburg as an A1 regional site, but does not provide an address in the reviewed source.

Queries:

```text
site:salzburg.gv.at Rechenzentrum
"Rechenzentrum" "Salzburg" "Baubewilligung"
"KI-Rechenzentrum" Salzburg Fragmentix
site:salzburgnetz.at Rechenzentrum OR Netzanschluss
"A1" "Rechenzentrum" Salzburg
```

### Styria/Steiermark - Graz-centered

Primary anchors: Magenta opened a new Graz datacenter in 2022; its own newsroom states opening/inbetriebnahme, double-digit million investment and COOLtec planning/build/operation (A, https://newsroom.magenta.at/2022/05/23/digitalisierungsstandort-steiermark-neues-magenta-rechenzentrum-in-graz-eroeffnet/; earlier planning release https://newsroom.magenta.at/2021/03/08/neues-rechenzentrum-in-graz-staerkt-digitale-infrastruktur-der-steiermark/). ORF confirms the opening (B, https://steiermark.orf.at/stories/3157595/). Nexspace markets a Graz datacenter at Alte Poststraße 390/376 (operator page, B/A for its own current offering, https://www.nexspace.de/data-centers/graz). Citycom has Graz network/datacenter evidence via PeeringDB and its own site (C/B, https://www.peeringdb.com/fac/1119; https://citycom.at/en/home-en/).

Queries:

```text
site:verwaltung.steiermark.at Rechenzentrum
site:graz.at Rechenzentrum Baubewilligung
"Rechenzentrum" "Graz" "Alte Poststraße"
"Magenta" "Rechenzentrum" Graz
site:e-netze.at Rechenzentrum OR Netzanschluss
"Graz Netze" Rechenzentrum
```

### Tyrol/Tirol - low-density, Innsbruck checks

No hyperscale or major official DC project was confirmed. A1's all-provincial-capitals statement makes Innsbruck worth checking, but do not record a named facility without an operator/permit source. Use Innsbruck city, Tirol state, TINETZ and A1/Magenta searches.

Queries:

```text
site:tirol.gv.at Rechenzentrum
site:innsbruck.gv.at Rechenzentrum
"Rechenzentrum" Innsbruck OR Tirol
"A1" "Rechenzentrum" Innsbruck
"Magenta" "Rechenzentrum" Innsbruck
site:tinetz.at Rechenzentrum OR Netzanschluss
```

### Vorarlberg - low-density, historical leads only until re-verified

No current major DC project was confirmed. Historical Vorarlberger Rechenzentrum/Dornbirn references are not enough for current facility status. Search state, municipal, illwerke/vkw, A1 and Vorarlberger Energienetze sources.

Queries:

```text
site:vorarlberg.at Rechenzentrum
"Rechenzentrum" Vorarlberg OR Dornbirn OR Bregenz OR Feldkirch
"Vorarlberger Rechenzentrum" current OR aktuell
site:vorarlbergnetz.at Rechenzentrum OR Netzanschluss
"A1" "Rechenzentrum" Vorarlberg OR Bregenz
```

### Carinthia/Kärnten - low-density, Klagenfurt checks

No major DC project was confirmed. Lakeside Science & Technology Park is an ICT cluster, not a datacenter proof by itself (https://lakeside-scitec.com/). Use Klagenfurt, Kärnten Netz, A1 and municipal IT searches.

Queries:

```text
site:ktn.gv.at Rechenzentrum
site:klagenfurt.at Rechenzentrum
"Rechenzentrum" Kärnten OR Klagenfurt
"A1" "Rechenzentrum" Klagenfurt
site:kaerntennetz.at Rechenzentrum OR Netzanschluss
```

### Burgenland - low-density, one live rumor plus public IT

Digital Burgenland/EBRZ is a public/municipal IT lead (operator/public source, B/A for its own services: https://www.ebrz.at/). Nickelsdorf is a significant but unconfirmed datacenter lead: ORF reported on 2026-08-03 that a datacenter up to 50 ha could be discussed in Nickelsdorf and that talks over business-park use were running (B for the existence of speculation/talks only, https://burgenland.orf.at/stories/3365457/). Der Standard and profil also report the rumor/debate, but no operator confirmation was found in reviewed sources. Grade project status **U** until municipality, Land, grid operator, buyer/SPV or operator confirms.

Queries:

```text
site:burgenland.at Rechenzentrum
site:nickelsdorf.at Rechenzentrum
"Nickelsdorf" "Rechenzentrum"
"Mönchhof" "Rechenzentrum" "Nickelsdorf"
site:netzburgenland.at Rechenzentrum OR Netzanschluss
"Digital Burgenland" Rechenzentrum OR EBRZ
```

---

## 5. Reliability grading rules

- **A - official/primary/operator-owned:** government/state/municipal pages; RIS statutes; APG/E-Control/RTR/Monitoringstelle pages; DSO-owned pages; procurement notices on official portals; cloud provider official region/location lists; operator-owned facility pages such as Digital Realty, AtlasEdge, A1, BRZ, LINZ AG, Magenta, Google, Exoscale, Nexspace.
- **B - reliable secondary:** ORF regional, DataCenterDynamics, derStandard, Die Presse, Kurier, Kleine Zeitung, nachrichten.at/OÖN, datacenter-insider.de, Computerwelt/itwelt where reporting is specific and attributable; Österreichs Energie and association pages when not primary for the operator fact.
- **C - aggregator/weak:** DataCenterMap, Baxtel, datacenters.com, PeeringDB facility pages, ocolo, colocationm, datacenterplatform, herold.at listings, savecall, blogs and unverifiable local trade snippets. PeeringDB is useful for interconnection, but it is not enough alone for construction status, ownership or MW.
- **U - unverified:** rumors, land-use speculation, exact addresses copied across aggregators without operator confirmation, MW figures with no primary planning/operator source, historical facilities not confirmed current.

Rules:

- Grade the exact fact, not the entity. Example: Digital Realty's Vienna facilities are A from Digital Realty; a third-party MW figure remains C unless Digital Realty or a permit states it.
- Do not assign hyperscaler physical addresses from region names. Azure Austria East verifies a region in Vienna, not site addresses.
- Do not count an ICT park, hosting provider, office, cloud reseller or IXP node as a datacenter unless a facility, server-room/colocation, or datacenter operation is explicitly stated.
- For construction, require at least one of: permit decision, operator construction announcement, municipality/district record, groundbreaking, tender award, or grid-connection evidence.

---

## 6. Minimum validation checklist for an AT enumeration run

1. Confirm all 9 states were searched and mark states with no confirmed facility/project as `no_confirmed_project_found`, not omitted.
2. Run official searches first: state/municipality, APG/DSO, EEffG/Monitoringstelle, procurement, BRZ.
3. Cross-check every industry or aggregator facility against an operator page, PeeringDB/VIX, procurement, permit or press source.
4. Re-check cloud status on official Microsoft/AWS/Google/Oracle pages before any run dated after this file.
5. Record uncertainty at field level: source grade, fact supported, date, URL, and what remains unknown.
