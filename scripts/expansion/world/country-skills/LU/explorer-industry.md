# LU Explorer Industry - Operator, Cloud, Trade, Directory, and Canton Discovery for Luxembourg Datacenters

Date: 2026-08-12. Scope: Luxembourg (LU), all 12 cantons and 100 communes. Purpose: industry-facing methodology for seeding Luxembourg datacenter discovery from operator pages, LU-CIX/PeeringDB, cloud-provider region pages, trade/local press, associations, directories, and canton-level query bundles. Reliability grades: **A** = primary/operator/official source for the fact stated; **B** = established trade/local press or association source requiring primary confirmation; **C** = directory, aggregator, or marketing-only lead.

## 0. Market frame and reliability rules

Luxembourg has a small but dense datacenter market concentrated in Bettembourg (Esch-sur-Alzette canton), Bissen (Mersch canton), Luxembourg City/Contern (Luxembourg canton), Windhof/Koerich (Capellen canton), Kayl (Esch-sur-Alzette canton), and Betzdorf (Grevenmacher canton). It does **not** have a public national datacenter registry, so enumeration must be: operator seeds -> LU-CIX/PeeringDB -> directories -> trade/local press -> commune permit/EIE/commodo/LBR/grid confirmation.

Do not use directory totals as authoritative. Snapshot sites such as Data Center Map, Baxtel, DataCenterJournal, and Datacenters.com are useful seed lists but may include aliases, retired facilities, ownership lag, or partial capacity. Grade them C unless corroborated.

No AWS, Microsoft Azure, Google Cloud, or Oracle Cloud public cloud region is currently listed for Luxembourg on their official global-infrastructure pages. Treat any "Luxembourg cloud region" claim as false unless the cloud provider's official region list says otherwise. OVHcloud is different: it has an official **datacentre Luxembourg** page, but that is not the same as AWS/Azure/GCP/OCI launching a Luxembourg region.

## 1. Primary and high-value sources

| Source | URL | Use | Grade |
|---|---|---|---|
| LuxConnect infrastructure | https://www.luxconnect.lu/infrastructure/ | Primary page for DC1.1/DC1.2/DC1.3 Bettembourg and DC2 Bissen, addresses, net/gross area, MVA, cooling, PUE, DCE energy/HVAC JV. | A |
| LU-CIX network map | https://www.lu-cix.lu/infrastructure/network-map/ | Primary/association PoP list that confirms named datacenter locations: BCE, DEEP West, LuxConnect DC1.1/DC2, Portus, DEEP East, DEEP South. | A/B |
| OVHcloud Luxembourg datacentre | https://www.ovhcloud.com/en/datacenter/europe/luxembourg/ | Confirms OVHcloud markets a Luxembourg datacentre. Does not publish a Bissen street address on this page. | A for OVH presence; C for exact physical mapping unless otherwise verified |
| DEEP official site | https://www.deep.eu/ | POST Group B2B ICT/cloud brand; use for current brand names. | A for brand/operator claims |
| DEEP launch note | https://www.deep.eu/en/accueil/a-propos/actualites/lancement-deep | Confirms DEEP combines EBRC, Elgon, Digora Luxembourg, and POST Telecom B2B activities; use current text for merger timing. | A |
| POST Group DEEP launch note | https://www.postgroup.lu/en/home/actualites/a2024/com-post-luxembourg-lance-deep | Same DEEP launch source; sometimes blocks command-line checks but browser/search confirms it. | A |
| Portus Data Centers Luxembourg | https://www.portusdatacenters.com/our-data-centers/luxembourg/ | Primary page for former EDH/Portus Luxembourg underground Tier IV site and new 1 MW IT-load expansion claim. | A for current Portus marketing/existence |
| LuxProvide MeluXina | https://www.luxprovide.lu/meluxina/ | Primary source for MeluXina/LuxProvide; facility is hosted in Luxembourg but this is an HPC anchor load, not public colo. | A |
| Visual Online | https://www.visualonline.lu/ | ISP/hosting lead in Contern; use operator page plus LBR/permit for facility details. | B until facility-specific page found |
| Proximus NXT Luxembourg | https://www.proximusnxt.lu/ | Telindus/Proximus ICT services lead; do not count facilities from brand alone. | B/C |
| Luxembourg Business Registers | https://www.lbr.lu/ | Legal names, ownership, registered offices, SPVs. | A |
| Commune/permit methodology | explorer-official.md | Required official confirmation layer. | A where source is official |

## 2. Operators and facility pivots

Operator pages are A for the exact facts they publish, usually B for capacity if not independently certified, and C for pipeline/ownership if the page does not cover it.

| Operator / brand | Verified pivots | Canton / place | How to use |
|---|---|---|---|
| LuxConnect S.A. | DC1.1, DC1.2, DC1.3 at 202 Z.A.E. Wolser F, L-3290 Bettembourg; DC2 at 3 op der Poukewiss, ZAC Klengbousbierg, L-7795 Bissen; MVA and area listed on operator page. | Esch-sur-Alzette / Mersch | Seed as operational Grade A from https://www.luxconnect.lu/infrastructure/; cross-check permits only for expansions. |
| DEEP / EBRC legacy | LU-CIX lists DEEP West Windhof, East Betzdorf, South Kayl; search old EBRC names for City/Resilience Centre aliases. | Capellen, Grevenmacher, Esch-sur-Alzette, Luxembourg | Use LU-CIX for PoP existence; use DEEP/operator pages and LBR for legal/current naming. |
| OVHcloud | Official Luxembourg datacentre page. | Mersch/Bissen lead in trade sources | Count Luxembourg presence as A; exact Bissen location remains B/C until operator page, LBR, permit, or strong official address evidence is found. |
| SecureIT S.A. | DCC Luxembourg City; DCB Bettembourg; DCR Bissen are directory/trade/operator-search pivots. | Luxembourg, Esch-sur-Alzette, Mersch | Treat as C/B until current operator page/LBR/permit confirms each site. Search street `8 rue Henri M. Schnadt`. |
| DATA4 | Luxembourg/Bettembourg lead from trade/directories. | Esch-sur-Alzette / Bettembourg | Search DATA4 official site plus Bettembourg permits and LBR; count only confirmed site evidence. |
| Portus Data Centers / European Data Hub | Current Portus Luxembourg page; LU-CIX lists Portus at 9 rue Robert Stumper, L-2557 Luxembourg; older EDH/Drosbach aliases may appear. | Luxembourg | Count current Portus Luxembourg page as A for existence; reconcile address aliases via LBR/commune records. |
| BCE / Broadcasting Center Europe | LU-CIX lists BCE at 43 boulevard Pierre Frieden, L-1543 Luxembourg. | Luxembourg | PoP/colo lead A/B; verify service/facility through BCE/RTL or procurement if counting as commercial colo. |
| Visual Online | ISP/hosting operator; Contern lead. | Luxembourg / Contern | Operator lead B; verify facility-specific address/services. |
| C2D System House | Windhof lead in directories. | Capellen / Koerich-Windhof | Directory lead C until operator/local records confirm datacenter facility details. |
| Datacenter Luxembourg / LuxNetwork | The former Datacenter Luxembourg homepage URL returned 404 in live checks; use LuxNetwork `https://www.luxnetwork.eu/` plus trade sources and LBR instead. | Capellen/Windhof or Bettembourg depending source | Do not rely on stale URL alone; verify active entity, facility and ownership via LBR and current operator pages. |
| LuxProvide / MeluXina | National HPC hosted in LuxConnect ecosystem; MeluXina operational since 2021; AI expansion is a separate procurement/deployment lead. | Mersch / Bissen | Anchor load, not a commercial colo facility. Use for power/HPC context. |
| Verizon legacy | Directory-only entries. | Luxembourg | Treat as retired/unverified until operator or PeeringDB confirms current presence. |

## 3. Cloud-region controls

| Provider | Official URL | Luxembourg conclusion | Grade |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Luxembourg region listed; nearest common region is Frankfurt (`eu-central-1`). | A for region absence |
| Microsoft Azure | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ | No Luxembourg geography/region listed. | A for region absence |
| Google Cloud | https://cloud.google.com/about/locations | No Luxembourg cloud region listed; Google Bissen is a possible datacenter campus pipeline, not a GCP region. | A for region absence; B for pipeline leads |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ | No Luxembourg OCI public cloud region listed. | A for region absence |
| OVHcloud | https://www.ovhcloud.com/en/datacenter/europe/luxembourg/ | Official Luxembourg datacentre page exists; do not convert this into AWS/Azure/GCP-style region evidence. | A for OVH datacentre page |

Cloud queries:

```text
site:aws.amazon.com/about-aws/global-infrastructure Luxembourg
site:azure.microsoft.com "Luxembourg" "region"
site:cloud.google.com/about/locations Luxembourg
site:oracle.com/cloud/public-cloud-regions Luxembourg
site:ovhcloud.com/en/datacenter/europe/luxembourg Luxembourg datacentre
"Google" "Bissen" ("building permit" OR PAP OR EIE OR commodo OR "permis de construire")
```

## 4. Associations, press, and directories

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| ICT Luxembourg | https://www.ictluxembourg.lu/ | Cluster/member universe; not a facility registry. | B |
| Luxinnovation | https://www.luxinnovation.lu/ | Digital/HPC/innovation context. | B |
| FEDIL | https://fedil.lu/ | Energy/digital infrastructure policy positions. | B |
| LU-CIX | https://www.lu-cix.lu/ and https://www.lu-cix.lu/infrastructure/network-map/ | PoP/facility existence cross-check. | A/B |
| Cloud Community Europe Luxembourg | https://cloudcommunityeurope.lu/ | Sovereign-cloud/DEEP-OVH ecosystem leads. | B/C |
| Data Center Dynamics | https://www.datacenterdynamics.com/ | Strong DC trade source, especially Google Bissen/LuxConnect. Some command-line checks return 403; browser/search verifies site availability. | B |
| Paperjam | https://paperjam.lu/ and https://en.paperjam.lu/ | Business/local reporting, Google Bissen/company news. | B |
| Delano | https://delano.lu/ | English business reporting. | B |
| ITnation | https://itnation.lu/ | Luxembourg IT trade press, EBRC/DEEP/SecureIT/company deals. | B |
| Luxembourg Times | https://www.luxtimes.lu/ | Local reporting; command-line checks may return 403/paywall. | B |
| RTL Today | https://today.rtl.lu/ | Useful public English coverage of Google Bissen and local status. | B |
| Chronicle.lu | https://chronicle.lu/ | English local news; use as secondary lead. | B/C |
| Data Center Map | https://www.datacentermap.com/luxembourg/ | Seed list only; command-line rate limits (429) are not proof of bad source. | C |
| Baxtel | https://baxtel.com/data-center/luxembourg | Seed/alias/ownership leads. | C |
| DataCenterJournal Luxembourg | https://www.datacenterjournal.com/data-centers/luxembourg/luxembourg/ | Market snapshot and facility count lead. | C/B context |
| Datacenters.com Luxembourg | https://www.datacenters.com/locations/luxembourg/ | Seed list only; may rate-limit. | C |
| PeeringDB | https://www.peeringdb.com/ | Network/facility cross-check; not a permit source. | B/C |

## 5. Google Bissen industry handling

Use Google Bissen as a live pipeline lead only. Do not count it as operational or as a Google Cloud region.

| Source | URL | Fact to extract | Grade |
|---|---|---|---|
| RTL Today, 2025-11-18 | https://today.rtl.lu/news/luxembourg/google-data-centre-in-bissen-scaled-down-but-far-from-shelved-2355533 | Permit application reportedly submitted mid-August 2025; not approved in that report; project scaled down and air-cooling mentioned. | B |
| RTL Today, PAP agreements | https://today.rtl.lu/news/luxembourg/bissen-council-approves-key-agreements-for-google-data-centre-2266926 | PAP implementation process complete at that stage; no construction permit yet in that report. | B |
| DCD 2019 | https://www.datacenterdynamics.com/en/news/googles-11-billion-bissen-luxembourg-data-center-clears-regulatory-hurdle/ | Land reclassification/regulatory hurdle; still required more approvals. | B |
| DCD 2022 | https://www.datacenterdynamics.com/en/news/land-in-bissen-luxembourg-classified-as-data-center-delayed-google-project-may-finally-begin-construction/ | Reclassification context and caveats. | B |
| Mouvement Ecologique / Oeko-Institut debate | https://www.meco.lu/en/blog/documentcenter/google-data-centre-lacking-transparency-in-environmental-impact-assessment-best-available-technology-disregarded/ | Environmental opposition/study claims; useful for issues and numbers, not final project status. | B/C |

Pipeline query bundle:

```text
"Google" "Bissen" ("permis de construire" OR "autorisation de batir" OR "building permit")
site:bissen.lu Google (PAP OR PAG OR "centre de donnees" OR Rechenzenter)
site:environnement.public.lu Google Bissen EIE
site:aev.gouvernement.lu Google Bissen commodo
"Google" "Bissen" (Creos OR MVA OR MW OR "raccordement")
```

## 6. Canton-by-canton industry recipes

Coverage checkpoint: all 12 cantons are included below: Capellen, Clervaux, Diekirch, Echternach, Esch-sur-Alzette, Grevenmacher, Luxembourg, Mersch, Redange, Remich, Vianden, Wiltz.

| Canton | Priority places | Industry/operator pivots | Query bundle |
|---|---|---|---|
| Capellen | Koerich/Windhof, Strassen, Mamer, Steinfort, Dippach, Kehlen, Kopstal, Garnich, Habscht | DEEP West, C2D, Datacenter Luxembourg/LuxNetwork legacy | `"Windhof" (datacenter OR "data center" OR "centre de donnees")`; `"DEEP Resilience Center Luxembourg West"`; `"C2D System House" Windhof`; `"Datacenter Luxembourg" LuxNetwork LBR`; `site:koerich.lu datacenter` |
| Clervaux | Clervaux, Troisvierges, Wincrange, Weiswampach, Parc Hosingen | No verified commercial anchor; edge/telecom/municipal IT only until proven | `"Clervaux" (datacenter OR Rechenzentrum OR colocation)`; `"Troisvierges" server`; `site:clervaux.lu (Rechenzentrum OR "centre de donnees")` |
| Diekirch | Diekirch, Ettelbruck, Colmar-Berg, Schieren, Feulen, Nordstad | Enterprise/industrial-zone hosting leads | `"Ettelbruck" ("data center" OR colocation)`; `"Diekirch" Rechenzentrum`; `site:marches.public.lu Diekirch (colocation OR "centre de donnees")` |
| Echternach | Echternach, Consdorf, Beaufort, Bech, Rosport-Mompach | No verified commercial anchor; municipal/edge leads | `"Echternach" (datacenter OR Rechenzentrum OR colocation)`; `site:echternach.lu "centre de donnees"`; `site:bech.lu "autorisation de batir"` |
| Esch-sur-Alzette | Bettembourg/Wolser F, Kayl, Esch/Belval, Sanem, Dudelange, Roeser, Leudelange | LuxConnect DC1.x, DATA4 lead, SecureIT DCB lead, DEEP South, LU-CIX | `"202 Z.A.E. Wolser F"`; `"LuxConnect" Bettembourg MVA`; `"DATA4" Luxembourg Bettembourg`; `"SecureIT" DCB Bettembourg`; `"DEEP Resilience Center Luxembourg South"`; `"Kayl" "210 rue de Noertzange"` |
| Grevenmacher | Betzdorf, Grevenmacher, Mertert, Junglinster, Biwer | DEEP East/SES area, industrial/logistics edge | `"DEEP Resilience Center Luxembourg East"`; `"Betzdorf" datacenter`; `"Z.A. audiovisuelle et de communications" Betzdorf`; `"Mertert" "data center"` |
| Luxembourg | Luxembourg City, Cloche d'Or/Drosbach, Kirchberg, Hamm, Contern, Hesperange, Bertrange | Portus/EDH, BCE, SecureIT DCC, DEEP City, Visual Online, Proximus NXT/Telindus | `"Portus Data Centers" Luxembourg`; `"9 rue Robert Stumper"`; `"Impasse Drosbach" datacenter`; `"Broadcasting Center Europe" colocation`; `"SecureIT" DCC`; `"Visual Online" Contern`; `"Telindus" "data center" Luxembourg` |
| Mersch | Bissen/Klengbousbierg, Mersch, Helperknapp, Lorentzweiler, Lintgen | LuxConnect DC2, OVHcloud Luxembourg, SecureIT DCR lead, LuxProvide/MeluXina, Google Bissen pipeline | `"3 op der Poukewiss"`; `"LuxConnect DC 2" Bissen`; `"OVHcloud" Luxembourg datacentre`; `"MeluXina" Bissen`; `"Google" Bissen "building permit"`; `"Klengbousbierg" datacenter` |
| Redange | Redange, Rambrouch, Groussbus-Wal, Beckerich, Ell | No verified commercial anchor; industrial/edge watch | `"Redange" (datacenter OR Rechenzentrum OR colocation)`; `"Rambrouch" "data center"`; `site:redange.lu "centre de donnees"` |
| Remich | Remich, Mondorf-les-Bains, Schengen, Lenningen, Dalheim | No verified commercial anchor; cross-border edge watch | `"Remich" (datacenter OR Rechenzentrum)`; `"Mondorf" colocation`; `"Schengen" "data center"`; `site:lenningen.lu "centre de donnees"` |
| Vianden | Vianden, Tandel, Putscheid | No verified commercial anchor; SEO pumped-storage is context only | `"Vianden" "data center"`; `"Vianden" Rechenzentrum`; `"Vianden" pumped storage datacenter` |
| Wiltz | Wiltz, Lac de la Haute-Sure, Esch-sur-Sure, Goesdorf, Kiischpelt | No verified commercial anchor; industrial/municipal IT watch | `"Wiltz" (datacenter OR Rechenzentrum OR colocation)`; `"Esch-sur-Sure" datacenter`; `site:wiltz.lu "centre de donnees"` |

## 7. Query bundles

Broad discovery:

```text
("centre de donnees" OR datacenter OR "data center" OR Rechenzentrum OR Rechenzenter) Luxembourg (colocation OR "Tier IV" OR MW OR MVA)
site:datacenterdynamics.com Luxembourg ("data center" OR "data centre") (Google OR LuxConnect OR Bissen OR Bettembourg)
site:paperjam.lu OR site:delano.lu OR site:itnation.lu OR site:siliconluxembourg.lu Luxembourg (datacenter OR "data center" OR "centre de donnees")
site:lu-cix.lu/infrastructure/network-map Luxembourg datacenter
site:peeringdb.com Luxembourg (LuxConnect OR DEEP OR EBRC OR Portus OR BCE)
site:baxtel.com/data-center/luxembourg Luxembourg {operator}
site:datacentermap.com/luxembourg {operator OR city}
```

Operator/address confirmation:

```text
site:{operator-domain} Luxembourg (datacenter OR "data center" OR "centre de donnees" OR colocation)
"{facility alias}" "{street}" Luxembourg
"{operator}" "{commune}" ("autorisation de construire" OR "permis de construire" OR PAP OR commodo OR EIE)
"{operator}" Luxembourg (MW OR MVA OR "Tier IV" OR racks OR "m2")
"{operator}" Luxembourg (RCS OR LBR OR "registre de commerce")
```

Ownership/transaction sweep:

```text
"SecureIT" Luxembourg (acquired OR acquisition OR Colony OR Genii)
"European Data Hub" OR "Portus Data Centers" Luxembourg Arcus
"Proximus" Luxembourg datacenter sale
"POST" DEEP EBRC Elgon Digora "31 December 2024"
"Datacenter Luxembourg" LuxNetwork (acquisition OR partnership OR capital)
site:lbr.lu ("Data Center" OR Datacenter OR LuxConnect OR SecureIT OR Portus OR DATA4)
```

Government/procurement sweep:

```text
site:marches.public.lu ("centre de donnees" OR "data center" OR colocation OR Rechenzentrum OR cloud OR HPC)
site:marches.public.lu (MeluXina OR supercomputer OR "AI Factory")
site:legilux.public.lu ("centre de donnees" OR datacenter OR "data center")
site:data.public.lu (datacenter OR "centre de donnees" OR communes OR cantons)
```

## 8. Confidence notes

- Grade A does not mean "complete"; it means the specific fact comes from a primary source. A commune permit page is A for procedure, not for any datacenter unless it names one.
- LU-CIX is strong evidence that a named site hosts an exchange PoP; it is not automatically evidence of total datacenter capacity or all commercial services.
- LuxConnect capacity/address facts are primary and can be recorded directly from the operator page, but expansions still require current permits.
- Google Bissen is a pipeline lead with changing status. Re-check Bissen commune, AEV/EIE, RTL Today, Paperjam, DCD, and Creos before every extraction run.
- Use both old and new brand names: EBRC/DEEP, EDH/Portus, Telindus/Proximus NXT, Datacenter Luxembourg/LuxNetwork.
- The negative-search requirement matters: for Clervaux, Diekirch, Echternach, Redange, Remich, Vianden, and Wiltz, record searches even when no facility is found, because the country is small and clustered.
