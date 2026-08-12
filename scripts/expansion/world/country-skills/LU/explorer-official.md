# LU Explorer Official - Luxembourg Datacenter Enumeration via Communal Permits, Energy/Grid, Environment, and Registers

Date: 2026-08-12. Scope: Luxembourg (LU), all 12 cantons and 100 communes. Purpose: official-source methodology for finding datacenter facilities and projects through commune building permits, PAG/PAP planning records, environmental/classified-establishment procedures, energy/grid records, official registers, and cloud-region controls. Reliability grades: **A** = official/primary source; **B** = established trade/local press or operator claim that still needs official confirmation; **C** = directory, aggregator, marketing-only, or unverified lead.

## 0. Administrative and permitting frame

Luxembourg has **no national public datacenter register** and **no single national building-permit portal**. The official public-administration site confirms that Luxembourg is divided into **12 cantons**: Capellen, Clervaux, Diekirch, Echternach, Esch-sur-Alzette, Grevenmacher, Luxembourg, Mersch, Redange, Remich, Vianden, and Wiltz: https://luxembourg.public.lu/en/society-and-culture/territoire-et-climat/territoire.html. The practical permit unit is the **commune**, not the canton. Cantons are routing buckets for coverage control; commune portals, council minutes, public notices, and Gemengebuet bulletins are where project evidence appears.

Official building-permit procedure: Guichet.lu states that construction/transformation/demolition requires an `autorisation de construire`, also called `autorisation de bâtir` or `permis de construire`; the request is filed with the **bourgmestre of the commune concerned**, and the permit is granted only if the project conforms to the PAG/PAP and building regulations: https://guichet.public.lu/fr/citoyens/logement/construction-renovation-transformation/travaux/autorisation-batir.html. Grade A.

Business building-permit procedure: the Guichet enterprise page gives the same rule for companies and is useful because commercial datacenter files are normally filed by legal persons: https://guichet.public.lu/fr/entreprises/gestion-juridique-comptabilite/construction-amenagement-site/construction-transformation-demolition/permis-construire.html. Grade A.

Classified establishments: Guichet.lu confirms that an `établissement classé` needs prior operating authorization; classes 1/3 go to the Administration de l'environnement and/or ITM, while class 2 goes to the bourgmestre. The permit does not replace the building permit: https://guichet.public.lu/fr/entreprises/urbanisme-environnement/commodo-incommodo/autorisations-commodo/commodo.html. Grade A.

Environmental impact: use the Environment portal EIE FAQ and the Administration de l'environnement for screening, motivated conclusions, public inquiries, and commodo files: https://environnement.public.lu/fr/support/faqs/faq-eie-new.html and https://aev.gouvernement.lu/. Grade A.

Planning vocabulary: `PAG` = plan d'amenagement general; `PAP` = plan d'amenagement particulier. A greenfield or industrial-zone datacenter can surface first as land reclassification, PAP adoption, implementation agreement, commodo/EIE notice, then building permit. Do **not** count a PAG/PAP vote as a built facility.

Lifecycle evidence scale:

| Evidence | Count as facility? | Grade rule |
|---|---:|---|
| Existing operator facility page with address | Yes, active/marketed facility | A for operator existence; B for capacity unless independently certified |
| Commune `autorisation de bâtir` issued / permit list / council permit decision | Yes, permitted project | A |
| Commodo/incommodo or EIE decision | Yes for regulated project status, not necessarily built | A |
| PAP/PAG adoption or implementation convention | Lead only until permit or construction evidence | A lead |
| Trade/local press saying permit requested or project planned | Lead only | B |
| Directory entry without operator/official match | Lead only | C |

## 1. Verified official source backbone

| Source | URL | Use | Grade |
|---|---|---|---|
| Luxembourg official territory page | https://luxembourg.public.lu/en/society-and-culture/territoire-et-climat/territoire.html | Confirms the 12 cantons; use as division-control source. | A |
| Guichet.lu building permit, citizens | https://guichet.public.lu/fr/citoyens/logement/construction-renovation-transformation/travaux/autorisation-batir.html | Procedure, bourgmestre authority, PAG/PAP conformity, publication/appeal context. | A |
| Guichet.lu building permit, enterprises | https://guichet.public.lu/fr/entreprises/gestion-juridique-comptabilite/construction-amenagement-site/construction-transformation-demolition/permis-construire.html | Same procedure for companies/project owners. | A |
| Guichet.lu commodo/incommodo | https://guichet.public.lu/fr/entreprises/urbanisme-environnement/commodo-incommodo/autorisations-commodo/commodo.html | Classified-establishment operating authorization; authority by class. | A |
| Legilux | https://legilux.public.lu/ | Laws, regulations, Memorial publications. | A |
| Luxembourg Business Registers | https://www.lbr.lu/ | RCS/RBE lookup for operators, SPVs, ownership, registered office. | A |
| Public procurement portal | https://marches.public.lu/ | State/commune procurement for colocation, HPC, cloud, DC construction, backup sites. | A |
| Open Data portal | https://data.public.lu/ | Geodata, administrative boundaries, addresses, cadastre-adjacent datasets. | A |
| Geoportail | https://geoportail.lu/ | Parcel, orthophoto, PAG/PAP map checks. | A |
| STATEC | https://statistiques.public.lu/ | Energy/population/ICT context; not a facility register. | A context |
| Environment portal | https://environnement.public.lu/ | EIE, water, climate, public environmental materials. | A |
| AEV | https://aev.gouvernement.lu/ | Environmental administration, commodo/EIE decision surface. | A |

## 2. Energy, grid, and regulator backbone

Energy is a gate for Luxembourg datacenters. Use official grid sources to verify large-load plausibility and substations before treating a land or press lead as viable.

| Source | URL | Use | Grade |
|---|---|---|---|
| ILR | https://www.ilr.lu/ | Regulator for energy, telecoms, post, transport, radio frequencies, and NIS/cybersecurity. Not a datacenter register. | A |
| ILR energy sector | https://www.ilr.lu/secteurs-activites/energie/ | Electricity/gas market and network regulation. | A |
| ILR plans de developpement dossier | https://www.ilr.lu/secteurs-activites/energie/electricite/reseau-marche/plans-de-developpement/pnec/ | Hosts network development-plan materials and PNEC-related surfaces. | A |
| CEER 2024 Luxembourg national report | https://www.ceer.eu/wp-content/uploads/2024/11/C24_Luxembourg-EN.pdf | Regulator-market context; use only as aggregate load-driver evidence. | A/B context |
| Creos | https://www.creos-net.lu/ | TSO/DSO electricity and gas network operator. | A |
| Creos Network Development Plan 2024-2034 | https://www.creos-net.lu/fileadmin/dokumente/downloads/20240315_Network_Development_Plan_2024-2034_-_Electricity_Transmission_Grid.pdf | Transmission projects, substations, major load planning. | A |
| Ministry energy policy | https://meco.gouvernement.lu/fr/domaines-activites/energie.html | National energy policy context. | A |
| PNEC dossier | https://gouvernement.lu/fr/dossiers/2023/2023-pnec.html | Climate/energy plan. | A |
| PNEC 2024 full PDF | https://gouvernement.lu/dam-assets/documents/actualites/2024/07/17-wilmes-pnec/pnec-document-complet.pdf | Energy/import/renewables policy context. | A |
| Energieauer | https://energieauer.lu/ | Official energy-data portal; use for context, not facility enumeration. | A/B context |

Grid queries:

```text
site:creos-net.lu ("data center" OR "centre de donnees" OR Rechenzentrum OR Rechenzenter)
site:creos-net.lu (raccordement OR Netzanschluss OR Anschlussleistung OR MVA)
site:ilr.lu ("data centres" OR "data centers" OR "centres de donnees" OR Rechenzentrum)
"{operator}" "{commune}" (MW OR MVA OR Creos OR raccordement OR poste OR transformateur)
"{commune}" ("220 kV" OR "380 kV" OR poste) (datacenter OR "centre de donnees")
```

## 3. Commune permit surfaces to use first

These verified commune pages are process anchors; they do not by themselves prove a datacenter. Search each commune portal plus agendas, deliberations, public notices, and `Gemengebuet` PDFs.

| Commune / relevance | URL | Use | Grade |
|---|---|---|---|
| Ville de Luxembourg | https://www.vdl.lu/fr/vivre/logement/construire-transformer-et-renover/autorisation-de-batir | Building-permit process for Luxembourg City. | A |
| Helperknapp | https://helperknapp.lu/citoyens/autorisations-de-batir/ | Good example of a commune page publishing issued permits/list surface. | A |
| Strassen | https://www.strassen.lu/fr/urbanisme/construire/autorisation-de-batir | Building-permit procedure. | A |
| Dudelange | https://www.dudelange.lu/index.php/demarches-administratives/autorisation-de-batir/ | Building-permit procedure. | A |
| Clervaux | https://www.clervaux.lu/fr/construire/autorisations-de-construire | Building-permit procedure. | A |
| Wiltz | https://www.wiltz.lu/fr/mediatheque/detail-media/demande-d-autorisation-de-construire | Building-permit form. | A |
| Schieren | https://www.schieren.lu/service-au-citoyen/demarches-administratives/autorisation-de-construire/ | Replaces stale draft URL; building-permit procedure. | A |
| Feulen | https://feulen.lu/autorisation-de-batir/ | Building-permit procedure. | A |
| Lenningen | https://lenningen.lu/guichet-citoyens/formulaires-demande-en-ligne/demande-dautorisation-de-construire/ | Building-permit request surface. | A |
| Troisvierges | https://www.troisvierges.lu/telechargements/27850/ | Building-permit form/download surface. | A |
| Lac de la Haute-Sure | https://lac-haute-sure.lu/vivre-dans-la-commune/guichet-citoyen/arrivee-depart-dans-la-commune-2/ | Form/download surface; verify exact form path when using. | A process / B URL specificity |
| Esch-sur-Alzette | https://administration.esch.lu/service/autorisations-de-batir/ | Building-permit procedure. | A |

Priority commune domains for known or likely datacenter clusters: `bettembourg.lu`, `bissen.lu`, `vdl.lu`, `koerich.lu`, `kayl.lu`, `betzdorf.lu`, `contern.lu`, `mersch.lu`, `sanem.lu`, `roeser.lu`, `leudelange.lu`, `strassen.lu`, `dudelange.lu`, `esch.lu` / `administration.esch.lu`.

## 4. Multilingual query templates

Use French, German, Luxembourgish, and English. Substitute `{commune}`, `{canton}`, `{operator}`, `{locality}`, `{street}`.

```text
"{commune}" ("centre de donnees" OR datacenter OR "data center") ("autorisation de construire" OR "autorisation de batir" OR "permis de construire")
"{commune}" (Rechenzentrum OR Rechenzenter OR Datacenter) (Baugenehmigung OR Baugenehmegung OR Baugesuch)
site:{commune-domain} ("centre de donnees" OR datacenter OR Rechenzentrum OR Rechenzenter) (PAG OR PAP OR autorisation OR permis OR commodo)
site:{commune-domain} ("conseil communal" OR Gemengebuet OR deliberation) (Google OR LuxConnect OR DEEP OR EBRC OR OVHcloud OR SecureIT OR DATA4)
filetype:pdf Luxembourg ("centre de donnees" OR datacenter OR Rechenzentrum) (PAP OR PAG OR commodo OR EIE)
"{street}" Luxembourg (datacenter OR "centre de donnees" OR colocation)
"{operator}" Luxembourg (RCS OR LBR OR "registre de commerce")
```

Terminology:

```text
FR: centre de donnees, centre informatique, salle serveurs, colocation, hebergement, autorisation de construire, autorisation de batir, permis de construire, etablissement classe, commodo/incommodo, evaluation des incidences sur l'environnement, raccordement electrique, poste de transformation, groupes electrogenes, refroidissement, chaleur fatale.
DE: Rechenzentrum, Datenzentrum, Datacenter, Serverhousing, Baugenehmigung, Baugesuch, Bebauungsplan, Betriebsgenehmigung, klassierter Betrieb, Umweltvertraeglichkeitspruefung, Netzanschluss, Umspannwerk, Notstrom, Abwaerme.
LB: Rechenzenter, Baugenehmegung, Gemengebuet, Gemeng, Betribsgenehmegung.
```

## 5. Canton-by-canton official enumeration plan

Coverage checkpoint: the table below includes all 12 official cantons: Capellen; Clervaux; Diekirch; Echternach; Esch-sur-Alzette; Grevenmacher; Luxembourg; Mersch; Redange; Remich; Vianden; Wiltz.

| Canton | Communes / places to prioritize | Official strategy | Known official/primary pivots |
|---|---|---|---|
| Capellen | Koerich/Windhof, Strassen, Mamer, Steinfort, Dippach, Kehlen, Kopstal, Garnich, Habscht | Search Windhof/Koerich and Strassen commune records first; then RCS for C2D/Datacenter Luxembourg/LuxNetwork entities. | LU-CIX lists DEEP Resilience Center Luxembourg West at 3 rue Pierre Flammang, Windhof: https://www.lu-cix.lu/infrastructure/network-map/. |
| Clervaux | Clervaux, Troisvierges, Wincrange, Weiswampach, Parc Hosingen | Low-density canton. Use commune building-permit pages and procurement; expect municipal/enterprise IT rooms more than commercial DCs. | Clervaux and Troisvierges permit pages above. |
| Diekirch | Diekirch, Ettelbruck, Bettendorf, Erpeldange-sur-Sure, Colmar-Berg, Schieren, Feulen, Mertzig, Reisdorf, Bourscheid, Vallee de l'Ernz | Search Nordstad/industrial-zone permits and public procurement. | Schieren/Feulen permit pages above. |
| Echternach | Echternach, Beaufort, Bech, Berdorf, Consdorf, Rosport-Mompach, Waldbillig | Low-density. Search commune portals, `Gemengebuet`, and public procurement for edge/municipal rooms. | Add Bech/Echternach process pages if a lead appears. |
| Esch-sur-Alzette | Bettembourg, Esch/Belval, Sanem, Dudelange, Kayl, Roeser, Schifflange, Mondercange, Differdange, Petange, Rumelange, Leudelange, Reckange-sur-Mess, Frisange | Primary official target. Start with Bettembourg Wolser F campus, Kayl DEEP South, Esch/Belval planning, Dudelange/Roeser spillover, commodo/EIE, and Creos substations. | LuxConnect operator page confirms DC1.1/DC1.2/DC1.3 at 202 Z.A.E. Wolser F, Bettembourg with MVA values: https://www.luxconnect.lu/infrastructure/. LU-CIX also confirms Bettembourg PoP. |
| Grevenmacher | Betzdorf, Grevenmacher, Mertert, Biwer, Flaxweiler, Junglinster, Manternach, Wormeldange | Search Betzdorf/SES area and Mertert logistics/industrial records. | LU-CIX lists DEEP Resilience Center Luxembourg East in Betzdorf: https://www.lu-cix.lu/infrastructure/network-map/. |
| Luxembourg | Luxembourg City, Contern, Hesperange, Bertrange, Niederanven, Sandweiler, Schuttrange, Steinsel, Walferdange, Weiler-la-Tour | Primary official target. Search VDL permits/council, Portus/Drosbach, BCE, SecureIT DCC, DEEP City, Contern/Visual Online. | VDL permit page; LU-CIX lists BCE and Portus addresses. |
| Mersch | Bissen, Mersch, Helperknapp, Lorentzweiler, Lintgen, Fischbach, Heffingen, Nommern | Primary official target. Search Bissen council/PAP/permit files, Helperknapp permit lists, Creos grid reinforcement, AEV EIE/commodo. | LuxConnect confirms DC2 at 3 op der Poukewiss, Bissen; OVHcloud confirms a Luxembourg datacentre; RTL/DCD/Paperjam are leads for Google until permit is issued. |
| Redange | Redange, Rambrouch, Ell, Groussbus-Wal, Beckerich, Saeul, Useldange, Vichten, Wahl, Preizerdaul | Low-density. Search commune permits, industrial zones, public procurement, and edge telecom terms. | No verified commercial DC anchor in current review. |
| Remich | Remich, Mondorf-les-Bains, Schengen, Bous-Waldbredimus, Dalheim, Lenningen, Stadtbredimus | Low-density/cross-border watch. Search Lenningen/Remich process pages, logistics/edge telecom terms. | Lenningen permit page above. |
| Vianden | Vianden, Tandel, Putscheid | Low-density. Treat SEO/Vianden pumped-storage as power-context only, not a datacenter lead. | Search procurement and commune minutes if any DC claim appears. |
| Wiltz | Wiltz, Lac de la Haute-Sure, Esch-sur-Sure, Goesdorf, Kiischpelt, Boulaide, Winseler | Low-density. Search Wiltz/Nord industrial permits, public procurement, and hydro/water constraints separately. | Wiltz and Lac de la Haute-Sure permit pages above. |

## 6. Google Bissen handling

Google Bissen is a **pipeline**, not an operating facility and not an announced Google Cloud region. Treat status as fluid. Verified public leads:

- DCD reported the 33.7 ha land reclassification/regulatory hurdle in 2019 and later reclassification context; grade B lead until matched to current commune/permit files: https://www.datacenterdynamics.com/en/news/googles-11-billion-bissen-luxembourg-data-center-clears-regulatory-hurdle/.
- RTL Today reported on 2025-11-18 that Google had submitted a building-permit application in mid-August 2025 and that approval had not yet been granted in that report: https://today.rtl.lu/news/luxembourg/google-data-centre-in-bissen-scaled-down-but-far-from-shelved-2355533. Grade B.
- RTL Today reported on 2025 PAP implementation-agreement completion and said Google had not yet applied for construction permission at that point: https://today.rtl.lu/news/luxembourg/bissen-council-approves-key-agreements-for-google-data-centre-2266926. Grade B.
- Environmental/energy numbers such as 950 GWh/year from the Oeko-Institut/Mouvement Ecologique debate are opposition-study/local-press leads; grade B/C unless the EIE or government decision file publishes the figure.

Operational rule: for Google Bissen, record exact stage as `PAG/PAP/permit application/EIE/commodo/construction` with date and source. Do not mark `under construction` without a commune permit issuance or construction-start evidence.

## 7. Extraction schema

For each candidate, capture:

```text
country=LU
canton=
commune=
locality_or_quarter=
street_address=
operator_legal_name=
brand_or_facility_name=
source_url=
source_grade=A/B/C
source_type=commune_permit | operator_page | EIE | commodo | grid | LBR | procurement | trade_press | directory
status=operational | permitted | permit_applied | PAP/PAG_only | planned | retired | unverified
permit_reference=
permit_date=
PAG_PAP_reference=
commodo_or_EIE_reference=
MW_or_MVA=
water_or_cooling_notes=
grid_notes=
ownership_notes=
last_checked=2026-08-12
```

## 8. Validation rules

- Count only issued permits, operating authorization, operator pages with addresses, or physically existing facilities as positive records.
- A canton with no verified facility still needs a negative search note naming the communes searched.
- Never infer a Luxembourg hyperscale cloud region from customer availability-zone wording.
- Use LBR for legal-entity/ownership claims and do not rely on directory ownership history without confirmation.
- Use directory counts only as leads; they are not authoritative facility totals.
