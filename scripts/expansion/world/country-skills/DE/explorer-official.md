# DE Explorer Official - Germany Datacenter Enumeration via Permits, Energy/Grid, State Portals, Cloud Regions

Date: 2026-08-12. Scope: Germany (DE), 403 divisions at Land + Kreis/kreisfreie Stadt level. Focus angle: official/regulatory/cloud pipeline for enumerating datacenter projects and facilities. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/association source, **C** = weak/aggregate/unverified.

---

## 0. Structural facts that shape Germany enumeration

- Germany has **no single public national building-permit database** for datacenters. Building permission is governed by the 16 state building codes (Landesbauordnungen) and usually administered by municipal/county **Bauaufsicht / Untere Bauaufsichtsbehorde**. For enumeration, treat each Kreis/kreisfreie Stadt as the operational search unit.
- Large German datacenters are usually visible earlier in **Bauleitplanung** than in the final **Baugenehmigung**: look for amendments to **Flachennutzungsplan**, **Bebauungsplan**, **Sondergebiet Rechenzentrum**, **Gewerbegebiet**, **Industriegebiet**, **Abwarme**, **Umspannwerk**, and **Netzanschluss**.
- Official building permit files are often not fully published, but public planning participation documents are. These documents can include site maps, parcels, operator SPVs, target IT load, transformer/substation needs, emergency generators, cooling/water assumptions, and waste-heat commitments.
- The strongest national public energy source is the **Energieeffizienzregister fur Rechenzentren (RZReg)** under the Energy Efficiency Act (**EnEfG**). It is not a building-permit register, but it creates a national reporting route for operational datacenters and should become a high-value validation source.
- Grid capacity is a core bottleneck. Use **Bundesnetzagentur** proceedings and grid-operator materials to find large-load connection projects. The phrase "Netzanschluss Rechenzentrum" is often more revealing than "Baugenehmigung Rechenzentrum".
- The German commercial market is highly clustered in **Frankfurt/Rhein-Main** because of DE-CIX and cloud on-ramps, but the permit pipeline is expanding to **Berlin-Brandenburg**, **Munich/Bavaria**, **Hamburg**, **Dusseldorf/Cologne/NRW**, **Hanover/Lower Saxony**, **Rhineland-Palatinate**, and selected industrial/energy sites.

Key lifecycle vocabulary:

`Standortsuche` < `Aufstellungsbeschluss` / `fruhzeitige Beteiligung` < `Offenlage` / `Auslegung` < `Satzungsbeschluss` / `rechtskraftig` < `Bauantrag` < `Baugenehmigung` < `Baubeginn` / `Spatenstich` < `Richtfest` < `Inbetriebnahme` / `Betriebsaufnahme`

Only count `Baugenehmigung`, `Baubeginn`, or stronger as construction evidence. Treat `Aufstellungsbeschluss`, `Sondergebiet`, or `Bebauungsplan` as planned/permitted-land-use evidence until cross-checked.

---

## 1. German and English query patterns

### 1.1 Core German search terms

Use German first; English mostly finds operator pages and trade press.

```
Rechenzentrum
Datacenter OR Data Center
Cloud Region
Colocation OR Co-Location
Hyperscale
KI-Rechenzentrum OR AI-Rechenzentrum
Sondergebiet Rechenzentrum
Bebauungsplan Rechenzentrum
B-Plan Rechenzentrum
Flachennutzungsplan Rechenzentrum
Bauantrag Rechenzentrum
Baugenehmigung Rechenzentrum
Bauaufsicht Rechenzentrum
Netzanschluss Rechenzentrum
Umspannwerk Rechenzentrum
110-kV Rechenzentrum OR 380-kV Rechenzentrum
Abwarme Rechenzentrum OR Fernwarme Rechenzentrum
Notstromaggregate Rechenzentrum
UVP Rechenzentrum OR Umweltvertraglichkeitsprufung Rechenzentrum
Immissionsschutz Rechenzentrum
```

### 1.2 Discovery queries by division

Substitute `{land}`, `{kreis}`, `{stadt}`, `{operator}`, `{site}`.

Planning and building permits:

```
"{stadt}" "Rechenzentrum" "Bebauungsplan"
"{stadt}" "Sondergebiet Rechenzentrum"
"{stadt}" "B-Plan" "Rechenzentrum"
"{stadt}" "Flachennutzungsplan" "Rechenzentrum"
"{kreis}" "Rechenzentrum" "Baugenehmigung"
"{kreis}" "Bauaufsicht" "Rechenzentrum"
site:{stadt-domain} Rechenzentrum Bebauungsplan
site:{kreis-domain} Rechenzentrum Baugenehmigung
filetype:pdf "Rechenzentrum" "Bebauungsplan" "{stadt}"
filetype:pdf "Rechenzentrum" "Begrundung" "Satzungsbeschluss"
filetype:pdf "Rechenzentrum" "Artenschutz" OR "Schall" OR "Verkehr" OR "Abwarme"
```

Energy, grid, environment:

```
"{stadt}" "Rechenzentrum" "Netzanschluss"
"{stadt}" "Rechenzentrum" "Umspannwerk"
"{stadt}" "Rechenzentrum" "110-kV"
"{stadt}" "Rechenzentrum" "380-kV"
site:bundesnetzagentur.de Rechenzentrum Netzanschluss
site:bundesnetzagentur.de "Rechenzentrum" "Investitionsmaßnahme"
site:uvp-verbund.de Rechenzentrum
site:uvp-portal.de Rechenzentrum
"{stadt}" "Rechenzentrum" "Notstromaggregate"
"{stadt}" "Rechenzentrum" "Abwarme" "Fernwarme"
```

Operator/cloud pivot:

```
"{operator}" "{stadt}" "Rechenzentrum"
"{operator}" "{stadt}" "data center"
"{operator}" "{stadt}" "MW" "Germany"
"{operator}" "{site}" "IT capacity"
"{operator}" "{stadt}" "Spatenstich" OR "Richtfest" OR "Inbetriebnahme"
"AWS" "Frankfurt" "eu-central-1"
"Azure" "Germany West Central" "Frankfurt"
"Google Cloud" "europe-west3" "Frankfurt"
"Oracle Cloud" "eu-frankfurt-1"
```

### 1.3 English query patterns

```
"Germany" "data center" "building permit"
"Frankfurt" "data center" "building permit"
"Germany" "data center" "grid connection"
"Germany" "data center" "substation"
"Germany" "data center" "waste heat"
"Germany" "hyperscale campus" "MW"
"Frankfurt" "data center" "Bebauungsplan"
"Berlin" "data center campus" "building permit"
```

---

## 2. Official/regulatory sources

### 2.1 Bauamt / Baugenehmigung / Bauleitplanung backbone

There is no national "datacenter permit" registry. The practical official chain is:

1. **Municipal Bauleitplanung**: search current and archived public participation for `Bebauungsplan`, `Flachennutzungsplananderung`, `Sondergebiet Rechenzentrum`, `Gewerbegebiet`, `Industriegebiet`.
2. **Council information systems**: search `Ratsinformationssystem`, `Burgerinfo`, `Vorlagen`, `Drucksache`, `Sitzungsvorlage`, `Magistrat`, `Stadtverordnetenversammlung`, `Gemeindevertretung`.
3. **Bauaufsicht / Baugenehmigung**: search building-control press releases and public agenda items. Detailed applications are often non-public, but approvals are sometimes disclosed politically or in council reports.
4. **Regional planning**: for greenfield/out-of-settlement sites, search `Regionalplan`, `Zielabweichung`, `Raumordnungsverfahren`, and the Regierungsprasidium/Bezirksregierung.

Important official examples and portals:

- Frankfurt planning authority datacenter guidance: https://www.stadtplanungsamt-frankfurt.de/facilitating_computer_centers_22137.html. Grade A. Use this as the Frankfurt/Rhein-Main policy frame; it shows Frankfurt actively channels datacenter land use through urban-planning criteria.
- Frankfurt Bebauungsplan PDFs often mention datacenter steering and suitable infrastructure areas; example search result for `Bebauungsplan NW 43c Nr. 2 A` from Frankfurt Stadtplanungsamt. Grade A when hosted by `stadtplanungsamt-frankfurt.de`.
- DiPlanung public participation, used by several states/municipalities: https://bb.beteiligung.diplanung.de/. Grade A for procedures published there. Example active-style query: `site:bb.beteiligung.diplanung.de Rechenzentrum`.
- Brandenburg/DiPlanung example: `Bebauungsplan Sondergebiet "Rechenzentrum 2"` in Nauen: https://bb.beteiligung.diplanung.de/verfahren/e37a84da-6b60-49f5-b20a-258745094bb7/public/detail. Grade A; useful template because it explicitly uses `Sonstiges Sondergebiet` with purpose `Rechenzentrum und rechenzentrumsnahe Technologien`.
- BayernPortal points to the central Bavarian Bauleitplanung portal: https://www.bayernportal.de/dokumente/leistung/47441429650. Grade A. Search by municipality, then `Rechenzentrum`.
- Bavaria DiPlanung program page: https://www.digitale.planung.bayern.de/diplanung/. Grade A.
- Berlin DiPlanung page: https://www.berlin.de/sen/stadtentwicklung/planung/bebauungsplanverfahren/diplan-berlin/. Grade A.
- Hamburg Bauleitplanung Online: https://bauleitplanung.hamburg.de/. Grade A.
- Hessen Bauleitplanung Online instance: https://he.bauleitplanung-online.de/. Grade A for participating Hessian procedures.
- Mecklenburg-Vorpommern Bauleitplanung Online instance: https://mv.bauleitplanung-online.de/. Grade A for participating MV procedures.
- Schleswig-Holstein BOB-SH: https://www.bob-sh.de/. Grade A.
- Sachsen central portal for Raumordnungs- und Bauleitplanung: https://buergerbeteiligung.sachsen.de/portal/bplan/startseite. Grade A.
- Sachsen-Anhalt central portal: https://beteiligung.sachsen-anhalt.de/portal/rbplan/startseite. Grade A.
- NRW Fachportal fur Raumordnungs- und Bauleitplanung: https://beteiligung.nrw.de/portal/rpv/startseite. Grade A.
- Bayern GDI metadata for `Bebauungsplane Bayern`: https://gdk.gdi-de.org/geonetwork/srv/api/records/26d2b2b8-3944-4a49-aec2-59f827d9aa9e. Grade A; note metadata warns data is not complete.

Per-division rule: for each Kreis/kreisfreie Stadt, first query the Land planning portal if one exists; then query the municipality/county site and council system. A Kreis can contain many municipalities, so projects may sit on a small Gemeinde site while the Kreis name never appears in the title.

### 2.2 Environment / UVP / immission control

- UVP-Verbund state/federal search portal: https://www.uvp-verbund.de/. Grade A. Search `Rechenzentrum`, `Datacenter`, `Notstrom`, `Umspannwerk`, operator names, and municipality names.
- Federal UVP portal: https://www.uvp-portal.de/de. Grade A for federal-authority UVP procedures; state procedures are often linked through UVP-Verbund.
- UVP help page explains that the portal covers ongoing procedures and decisions: https://www.uvp-portal.de/de/node/250. Grade A for process understanding.

What to extract:

- Diesel backup generators: count, MW/MVA, fuel tanks, emission controls.
- Cooling systems: water demand, evaporative cooling, noise, heat rejection.
- Electrical infrastructure: transformer/substation size, 110-kV/380-kV connection, cable route.
- Environmental constraints: water, noise, traffic, Natura 2000, species protection.

Some datacenters may not require a full UVP, but associated substations, backup power, district heating, or industrial-park infrastructure can trigger searchable environmental documents.

### 2.3 Energy-efficiency register / EnEfG

- BMWE RZReg page: https://www.bundeswirtschaftsministerium.de/RZReg/rechenzentrums-register.html. Grade A.
- BfEE register page: https://www.bfee-online.de/BfEE/DE/Effizienzpolitik/Energieeffizienzregister_Rechenzentren/energieeffizienzregister_rechenzentren_node.html. Grade A.
- BAFA/BfEE launch note: https://www.bafa.de/SharedDocs/Kurzmeldungen/DE/Energie/20240319_bfee_enefg.html. Grade A.
- Legal basis, EnEfG Section 14: https://www.gesetze-im-internet.de/enefg/__14.html. Grade A. It establishes an energy-efficiency register for datacenters.
- German administrative register map entry for RZReg: https://www.verwaltungsdaten-informationsplattform.de/register/1250. Grade A-/B+; useful for purpose/scope summary.
- Umweltbundesamt publication on building a German datacenter register: https://www.umweltbundesamt.de/publikationen/aufbau-eines-registers-fuer-rechenzentren-in. Grade A-/B+ for policy background.

Use this as validation rather than first-pass discovery until public extract availability is confirmed. Target fields to capture when available:

- operator legal entity;
- facility location;
- non-redundant rated connection power (`nicht redundante elektrische Nennanschlussleistung`);
- annual electricity consumption;
- PUE / ERF / waste-heat metrics;
- reporting year.

### 2.4 Bundesnetzagentur and grid approvals

- Bundesnetzagentur flexible grid connection FAQ: https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/Netzanschluss/FAQ_FCA/FCA_table.html. Grade A; gives regulatory context for constrained connection capacity.
- Bundesnetzagentur construction-cost contribution page: https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/Netzanschluss/Baukostenzuschuesse/start.html. Grade A for Netzanschluss cost context.
- Bundesnetzagentur BK6-24-245 consultation materials mention large-load allocation pressure including datacenters; search `site:bundesnetzagentur.de BK6-24-245 Rechenzentrum`. Grade A.
- Bundesnetzagentur investment-measure proceedings can reveal named grid projects. Example result: `380-kV-Netzanschluss Rechenzentrum Mittenwalde im Umspannwerk Thyrow` under `BK4-20-028` / 50Hertz. Grade A.

Grid search templates:

```
site:bundesnetzagentur.de "Rechenzentrum" "Netzanschluss"
site:bundesnetzagentur.de "Rechenzentrum" "Umspannwerk"
site:bundesnetzagentur.de "Rechenzentrum" "Investitionsmaßnahme"
site:bundesnetzagentur.de "380-kV-Netzanschluss Rechenzentrum"
site:bundesnetzagentur.de "BK4" "Rechenzentrum"
site:bundesnetzagentur.de "BK6-24-245" "Rechenzentrum"
```

Also query distribution and transmission operators by geography:

- TSO: 50Hertz, TenneT, Amprion, TransnetBW.
- Frankfurt/Rhein-Main DSO examples: NRM Netzdienste Rhein-Main, Syna, Westnetz, e-netz Sudhessen, Mainova-related pages.
- Berlin/Brandenburg: Stromnetz Berlin, E.DIS, 50Hertz.
- NRW: Westnetz, Rheinische NETZGesellschaft, Amprion.
- Bavaria: Bayernwerk Netz, LEW Verteilnetz, N-ERGIE Netz, SWM Infrastruktur, TenneT.

Query:

```
site:{grid-operator-domain} Rechenzentrum Netzanschluss
site:{grid-operator-domain} Rechenzentrum Umspannwerk
site:{grid-operator-domain} "{stadt}" "Rechenzentrum"
```

### 2.5 State and municipal portals - priority routing by Land

Use this routing table for the 16 Länder. For the 403-division manifest, apply the Land row, then drill into the Kreis/city and municipality.

| Land | First official portal route | Second route | Notes |
|---|---|---|---|
| Baden-Wurttemberg | municipal `Bauleitplanung` / `Ratsinformationssystem`; state service portal for authority lookup | regional associations + UVP-Verbund | Stuttgart/Karlsruhe/Mannheim/Ulm searches should include `KI-Rechenzentrum`, `Hochleistungsrechenzentrum`, `Umspannwerk`. |
| Bayern | BayernPortal Bauleitplane + Bayern DiPlanung | municipality planning pages, especially Munich/Nuremberg area | Use `Bauleitplane Bayern`, `digitale.planung.bayern.de`, `Bebauungsplan Rechenzentrum`. |
| Berlin | Berlin DiPlanung + district planning pages | Stromnetz Berlin / UVP | Search district names plus `Bebauungsplan`, `Bauantrag`, `Gewerbegebiet`. |
| Brandenburg | DiPlanung Brandenburg (`bb.beteiligung.diplanung.de`) | municipal pages + 50Hertz/E.DIS | High priority for Berlin-adjacent hyperscale; examples include Nauen/Ahrensfelde/Mittenwalde-type queries. |
| Bremen | city/state planning pages + DiPlaning rollout references | UVP-Verbund | Small state; search `Bremen Rechenzentrum Bebauungsplan`, `Bremerhaven`. |
| Hamburg | https://bauleitplanung.hamburg.de/ | Hamburg district planning + Stromnetz Hamburg | Search `Rechenzentrum`, `Datacenter`, `Umspannwerk`, `Abwarme`. |
| Hessen | `he.bauleitplanung-online.de`, Frankfurt Stadtplanungsamt, municipal portals | Regierungsprasidium Darmstadt/Ratsinfo; NRM/Syna/e-netz | Highest priority. Search Frankfurt, Offenbach, Hanau, Hattersheim, Hofheim, Kelsterbach, Raunheim, Russelsheim, Eschborn, Bad Homburg. |
| Mecklenburg-Vorpommern | `mv.bauleitplanung-online.de` | municipal pages + UVP | Lower density; search coastal/energy sites and industrial parks. |
| Niedersachsen | municipal planning portals + state/geoportal sources | TenneT/Avacon/EWE Netz | Search Hanover/Wolfsburg/Braunschweig/industrial parks; no reliable single B-Plan portal assumed. |
| Nordrhein-Westfalen | https://beteiligung.nrw.de/portal/rpv/startseite | city portals for Dusseldorf, Cologne, Dortmund, Essen, Duisburg | Use `Bauleitplanung NRW`, `Bezirksregierung`, `Ratsinformation`; cloud/colo likely near Rhine-Ruhr fiber/power. |
| Rheinland-Pfalz | municipal/RIS + UVP-Verbund | SGD/Regional planning pages | Watch Nierstein/Ingelheim/Mainz/Rhein-Selz, former military/industrial sites. |
| Saarland | municipal/RIS + UVP-Verbund | state planning pages | Smaller market; search `Rechenzentrum Saarland B-Plan`. |
| Sachsen | https://buergerbeteiligung.sachsen.de/portal/bplan/startseite | municipal/RIS + enviaM/MITNETZ | Leipzig/Dresden/Chemnitz priority. |
| Sachsen-Anhalt | https://beteiligung.sachsen-anhalt.de/portal/rbplan/startseite | municipal/RIS + 50Hertz/Avacon/MITNETZ | Energy/industrial sites may surface via regional planning. |
| Schleswig-Holstein | https://www.bob-sh.de/ | municipal pages + SH Netz/TenneT | Search Hamburg-edge sites and renewable-power-adjacent proposals. |
| Thuringen | municipal/RIS + UVP-Verbund | state planning/geoportal + TEN Thüringer Energienetze | Search Erfurt/Jena/industrial campuses. |

---

## 3. Official cloud-region and network seeds

Cloud regions confirm city-level demand and interconnection anchors, but they normally hide exact buildings. Use them as seed records and then pivot to colo/on-ramp operators, DE-CIX enabled sites, ExpressRoute/Direct Connect partner locations, and planning/grid evidence.

### 3.1 Hyperscaler official regions

| Provider | Germany region(s) to seed | Official source | Reliability |
|---|---|---|---|
| AWS | `eu-central-1` Europe (Frankfurt); watch announced European Sovereign Cloud Germany as separate future infrastructure | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | A for region/city; not facility-level |
| Microsoft Azure | `germanywestcentral` Germany West Central, physical location Frankfurt; paired with restricted Germany North/Berlin | https://learn.microsoft.com/en-us/azure/reliability/regions-list | A for region/city; not facility-level |
| Google Cloud | `europe-west3` Frankfurt | https://docs.cloud.google.com/compute/docs/regions-zones and https://cloud.google.com/about/locations | A for region/city; not facility-level |
| Oracle Cloud Infrastructure | Germany Central (Frankfurt), `eu-frankfurt-1`, FRA, 3 availability domains per current Oracle region table | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | A for region/city; not facility-level |
| IBM Cloud | Frankfurt (`eu-de`) | IBM Cloud global availability pages / cloud endpoint docs | A for region/city when on IBM docs |
| Alibaba Cloud / Tencent Cloud / other on-ramps | Frankfurt connectivity/region/on-ramp pages where official | vendor official docs | A for cloud presence; not facility-level |

Extraction rule: create a cloud seed record with `division=Frankfurt am Main / Hessen` unless the official source states another city. Do not infer the physical datacenter owner without a second source.

### 3.2 DE-CIX and interconnection

- DE-CIX Frankfurt official page: https://www.de-cix.net/en/locations/frankfurt. Grade A. It states Frankfurt is a leading Internet Exchange with very high peak traffic and more than 1,000 networks; use this to prioritize Frankfurt/Rhein-Main.
- DE-CIX `Where to connect`: https://www.de-cix.net/en/services/where-to-connect. Grade A for enabled/connected site discovery; filter Germany/Frankfurt/Hamburg/Munich/Dusseldorf as applicable.
- DE-CIX global locations: https://www.de-cix.net/en/locations. Grade A for IX market list.

Use DE-CIX enabled sites as a facility seed list, then verify each facility against the operator page and planning/permit evidence if it is new or expanding.

---

## 4. Official operator/vendor seed list

Use operator pages as A-/B evidence: A for the operator's own claimed existence/location, B for capacity unless independently confirmed by filings/permits/grid documents. For exact facility address and MW, prefer operator official facility pages, then cross-check with planning/grid.

### 4.1 Frankfurt / Rhein-Main priority operators

| Operator | Official source | German seed locations / notes |
|---|---|---|
| Equinix | Frankfurt metro page: https://www.equinix.com/data-centers/europe-colocation/germany-colocation/frankfurt-data-centers | FR series including central, west, northeast and xScale facilities. Facility pages such as FR8 show addresses like Lärchenstrasse 141, 65933 Frankfurt. |
| Digital Realty / Interxion | Frankfurt metro page: https://www.digitalrealty.com/data-centers/emea/frankfurt | Large Frankfurt portfolio; page reports 20+ facilities. Facility pages include FRA5, FRA8, FRA14, FRA18, FRA20, FRA32. FRA20 press release: https://www.digitalrealty.com/about/newsroom/press-releases/19811/digital-realty-begins-construction-of-its-latest-state-of-the-art-data-center-in-frankfurt. |
| NTT Global Data Centers | Frankfurt page: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/emea/frankfurt-data-centers | Frankfurt 1-4. Frankfurt 1 official page gives 52,200+ sq m IT space and 77.4 MW max IT load: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/emea/frankfurt-1-data-center. |
| maincubes | main site: https://www.maincubes.com/en/ and datacenters: https://www.maincubes.com/en/data-centers/ | Frankfurt FRA01/FRA03 and Berlin BER01. FRA01: https://www.maincubes.com/en/data-centers/frankfurt-01/. BER01: https://www.maincubes.com/en/data-centers/berlin-01/. |
| Vantage Data Centers | EMEA locations: https://vantage-dc.com/data-center-locations/emea/ | Frankfurt and Berlin campuses. Frankfurt I official page: https://vantage-dc.com/data-center-locations/emea/frankfurt-i-germany/. EMEA page lists Berlin total 88 MW and Frankfurt total 112 MW. |
| CyrusOne | Germany/Frankfurt facility pages under https://www.cyrusone.com/data-centers/emea/ | FRA1/FRA5/FRA6/FRA7 etc. FRA7 page: https://www.cyrusone.com/data-centers/emea/frankfurt-germany-fra7; FRA5: https://www.cyrusone.com/data-centers/emea/frankfurt-germany-fra5; FRA6: https://www.cyrusone.com/data-centers/emea/frankfurt-germany-fra6. |
| Telehouse / KDDI | Telehouse official site and DE-CIX enabled-site filters | Frankfurt legacy carrier-neutral site; verify current page before counting. |
| NorthC, Global Switch, Iron Mountain, Colt DCS, EdgeCore/Edged, STACK, Data4, Green Mountain-type entrants | operator official pages + planning portals | Include only if Germany page or official planning evidence exists. Search by operator + city + `Bebauungsplan` and `Netzanschluss`. |

### 4.2 Berlin-Brandenburg and other non-Frankfurt anchors

- Vantage Berlin campuses: official EMEA page lists Berlin, Germany; drill into BER1/BER2 from https://vantage-dc.com/data-center-locations/emea/.
- maincubes BER01 official page: https://www.maincubes.com/en/data-centers/berlin-01/.
- NTT planned Berlin/Nierstein-type projects should be verified through municipal planning and public tender/contract announcements; do not count as operational until permit/build status is confirmed.
- Munich/Bavaria, Hamburg, Dusseldorf/Cologne/NRW, and Stuttgart/Karlsruhe/Mannheim should be searched by `cloud on-ramp`, `DE-CIX enabled sites`, `Bauleitplanung`, and operator pages. Many are enterprise/edge colo rather than hyperscale.

---

## 5. Per-division enumeration workflow for DE-403

For each division record (Land, Landkreis, kreisfreie Stadt):

1. **Normalize the division**: identify Land, Kreis/kreisfreie Stadt, major municipalities, and industrial parks. Germany projects are often named by municipality, not Kreis.
2. **Run official planning queries**:
   - Land planning portal query: `Rechenzentrum`, `Datacenter`, `Sondergebiet`, `Umspannwerk`, operator names.
   - Municipality/county site query: `site:{domain} Rechenzentrum Bebauungsplan`, `site:{domain} Rechenzentrum Baugenehmigung`.
   - Council system query: `{stadt} Ratsinformationssystem Rechenzentrum`, `{stadt} Burgerinfo Rechenzentrum`, `{stadt} Drucksache Rechenzentrum`.
3. **Run environmental/grid queries**:
   - UVP-Verbund and federal UVP for `Rechenzentrum`, `Notstromaggregate`, `Umspannwerk`.
   - Bundesnetzagentur for `Netzanschluss Rechenzentrum`, `Investitionsmaßnahme`, `380-kV`.
   - TSO/DSO websites for the division.
4. **Cloud/operator pivot**:
   - If division is Frankfurt/Rhein-Main or Berlin-Brandenburg, query every major operator above.
   - For other divisions, use DE-CIX where-to-connect plus cloud connectivity pages to seed facilities.
5. **Extract fields**:
   - `name`: official plan/facility/campus name.
   - `operator`: ultimate parent plus SPV if shown.
   - `division`: Kreis/kreisfreie Stadt and municipality.
   - `status`: planned, land-use-planning, permitted, under-construction, operational.
   - `capacity_mw`: IT MW if explicit; otherwise connection MW/MVA with note.
   - `source_urls`: planning + operator + grid/energy references.
   - `evidence_grade`: A/B/C per source.
   - `notes`: lifecycle verb, plan number, parcel/site, substation/waste heat, aliases.
6. **De-duplicate**:
   - Same campus can appear as operator brand, German SPV, street address, B-Plan name, and industrial-park name.
   - Cluster by `(operator ultimate parent, municipality, street/parcel, campus name, plan number)`.

Recommended status rules:

| Evidence | Status |
|---|---|
| Operator page says live/in operation; cloud/colo listing active | operational |
| `Inbetriebnahme`, `Betriebsaufnahme`, `eroffnet` from operator/gov | operational |
| `Baubeginn`, `Spatenstich`, `Richtfest`, EPC contract with schedule | under-construction |
| `Baugenehmigung erteilt`, approved Bauantrag | permitted |
| `Satzungsbeschluss`, rechtskraftiger B-Plan, special-use zoning | land-use-approved |
| `Offenlage`, `fruhzeitige Beteiligung`, draft B-Plan | land-use-planning |
| `Absichtserklarung`, `Prufung`, `Standortsuche`, political announcement | planned / C unless backed by official procedure |

---

## 6. High-value German clusters and search notes

### 6.1 Frankfurt / Rhein-Main (Hessen)

Priority municipalities and divisions:

- Frankfurt am Main (kreisfreie Stadt)
- Offenbach am Main / Landkreis Offenbach
- Hanau / Main-Kinzig-Kreis
- Hattersheim, Hofheim, Kelsterbach, Raunheim, Russelsheim, Eschborn, Bad Homburg, Neu-Isenburg, Maintal
- Darmstadt / Landkreis Darmstadt-Dieburg for grid/tech spillover

Queries:

```
"Frankfurt" "Rechenzentrum" "Bebauungsplan"
"Frankfurt" "Rechenzentren" "Leitlinien"
"Frankfurt" "Gwinnerstraße" "Rechenzentrum"
"Frankfurt" "Friesstraße" "Rechenzentrum"
"Frankfurt Westside" "Rechenzentrum"
"Hanau" "Rechenzentrum" "Bebauungsplan"
"Hattersheim" "Rechenzentrum" "Bebauungsplan"
"Hofheim" "Rechenzentrum Marxheim"
"Kelsterbach" "Rechenzentrum Kornweg"
"Raunheim" "Vantage" "Rechenzentrum"
"Russelsheim" "NTT" "Rechenzentrum"
site:stadtplanungsamt-frankfurt.de Rechenzentrum
site:he.bauleitplanung-online.de Rechenzentrum
```

Reason: Frankfurt has DE-CIX, AWS/Azure/GCP/OCI cloud-region anchors, and the densest official/operator evidence. Many projects are in neighboring municipalities but marketed as Frankfurt.

### 6.2 Berlin-Brandenburg

Priority municipalities/divisions:

- Berlin districts
- Ludwigsfelde / Teltow-Flaming
- Nauen / Havelland
- Ahrensfelde / Barnim
- Mittenwalde / Dahme-Spreewald
- Potsdam-Mittelmark, Oberhavel, Oder-Spree for industrial/power sites

Queries:

```
"Berlin" "Rechenzentrum" "Bebauungsplan"
"Brandenburg" "Sondergebiet Rechenzentrum"
"Nauen" "Rechenzentrum"
"Ahrensfelde" "Rechenzentrum Eiche"
"Mittenwalde" "380-kV-Netzanschluss Rechenzentrum"
site:bb.beteiligung.diplanung.de Rechenzentrum
site:berlin.de Rechenzentrum Bebauungsplan
site:bundesnetzagentur.de Mittenwalde Rechenzentrum
```

### 6.3 NRW / Rhine-Ruhr

Priority cities: Dusseldorf, Cologne, Bonn, Dortmund, Essen, Duisburg, Monchengladbach, Neuss, Aachen, Munster.

Queries:

```
site:beteiligung.nrw.de Rechenzentrum
"Dusseldorf" "Rechenzentrum" "Bebauungsplan"
"Koln" "Rechenzentrum" "Bauleitplanung"
"Dortmund" "Rechenzentrum" "Baugenehmigung"
"NRW" "Rechenzentrum" "Netzanschluss"
```

### 6.4 Bavaria / Munich-Nuremberg

Priority cities: Munich, Nuremberg, Erlangen, Regensburg, Augsburg, Ingolstadt.

Queries:

```
site:bayernportal.de Rechenzentrum Bauleitplanung
"Munchen" "Rechenzentrum" "Bebauungsplan"
"Nurnberg" "Rechenzentrum" "Baugenehmigung"
"Bayern" "Rechenzentrum" "Umspannwerk"
site:bauleitplanung.muenchen.de Rechenzentrum
```

### 6.5 Hamburg / North

Priority divisions: Hamburg, Schleswig-Holstein Hamburg-edge municipalities, Bremen, Hanover, Wolfsburg/Braunschweig.

Queries:

```
site:bauleitplanung.hamburg.de Rechenzentrum
site:bob-sh.de Rechenzentrum
"Hamburg" "Rechenzentrum" "Abwarme"
"Hamburg" "Rechenzentrum" "Netzanschluss"
"Hannover" "Rechenzentrum" "Bebauungsplan"
```

---

## 7. Reliability grading for German sources

| Source type | Grade | Use |
|---|---|---|
| Municipal B-Plan/FNP documents, council resolutions, Bauaufsicht notices | A | Best source for land-use status, parcel, lifecycle, sometimes MW. |
| Bundesnetzagentur proceedings and official grid-operator planning documents | A | Best source for grid connection/substation and large-load signal. |
| RZReg / BfEE / BMWE / EnEfG sources | A | Best national validation path for operational datacenter energy reporting, when public data is available. |
| UVP-Verbund / UVP portal documents | A | Best for environmental, backup power, cooling, and ancillary infrastructure. |
| Operator official facility pages | A- for existence/location; B for marketing capacity | Good seed and capacity source; cross-check new/large claims. |
| Cloud provider region docs | A for city-level cloud-region existence | Not facility-level; do not infer exact owner/address. |
| DE-CIX official enabled-site/location pages | A for interconnection site/market | Good seed for colo facilities and connectivity hubs. |
| German Datacenter Association, Bitkom, UBA/BMWK/BMWE studies | A-/B+ | Useful market/policy context; not a facility census. |
| DCD, DataCenter-Insider, heise, local newspapers | B | Good discovery and lifecycle hints; verify with official/operator sources. |
| Data Center Map, Baxtel, PeeringDB, Cloudscene, datacenters.com | B/C depending field | Good seed/alias/address source; verify before final count. |
| Local political statements, investor MoUs, marketing brochures | C | Intent only unless matched to official planning/permit. |

---

## 8. Pitfalls and validation rules

- **Baugenehmigung is local and often non-public**: absence from a search result does not mean absence of a permit. Use council, B-Plan, UVP, grid, and operator evidence together.
- **Frankfurt naming inflation**: many "Frankfurt" campuses are in Offenbach, Hanau, Hattersheim, Raunheim, Russelsheim, Hofheim, Eschborn, or other Rhein-Main municipalities. Store both marketed metro and legal municipality.
- **Connection MW is not IT MW**: distinguish `Netzanschlussleistung`, transformer MVA, building power, and IT load.
- **Planned total vs phase 1**: German planning documents may describe ultimate campus buildout; operator pages may list campus total. Record phase and status separately.
- **Waste heat commitments are status signals**: `Abwarme`, `Fernwarme`, and municipal heat-planning documents can reveal new facilities and startup schedules.
- **Emergency-generator documents can reveal hidden projects**: search UVP/immission/noise filings for `Notstromaggregat`, `Diesel`, `BHKW`, `Schornstein`, `Schalltechnische Untersuchung`.
- **Operator SPVs**: permits may use German legal entities such as `... Germany GmbH`, real-estate SPVs, or project companies, not the global brand. Pivot from address/parcel back to brand.
- **Cloud regions are not addresses**: AWS/Azure/GCP/OCI official pages prove Frankfurt region presence, not individual datacenters.

---

## 9. Recommended DE official/cloud pipeline

1. **Seed national anchors**: cloud regions (AWS, Azure, GCP, OCI), DE-CIX Frankfurt/where-to-connect, major operator official Germany pages.
2. **Prioritize clusters**: Frankfurt/Rhein-Main first; Berlin-Brandenburg second; NRW, Bavaria, Hamburg/North next.
3. **Run per-division official planning search**: Land portal -> municipality Bauleitplanung -> council/RIS -> Bauaufsicht.
4. **Run energy/grid search**: Bundesnetzagentur, TSO/DSO pages, UVP-Verbund, RZReg/BfEE/BMWE.
5. **Extract capacity/status conservatively**: prefer IT MW from operator official pages only when facility-specific; otherwise tag as connection MW/MVA.
6. **Verify with at least two evidence channels for large projects**: planning/permit + operator, or planning/permit + grid/UVP, or operator + RZReg when available.
7. **Write records at Kreis/municipality granularity**: preserve `Land`, `Kreis/kreisfreie Stadt`, `Gemeinde`, marketed metro, and source URLs to avoid double counting.

