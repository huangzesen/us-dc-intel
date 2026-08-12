# GR Explorer - Official/Regulatory Methodology for Greece Datacenter Enumeration

Date: 2026-08-12. Scope: Greece (GR), including the 13 first-level administrative regions plus the autonomous monastic polity of Mount Athos as an explicit exclusion/negative-control division. This file covers official and regulatory discovery: transparency decisions, environmental licensing, building permits, energy/grid records, telecom-regulator records, digital-government infrastructure, strategic investments, and official cloud/investor pages.

Reliability grades: **A** = official/primary source for the specific fact; **B** = strong secondary/trade/legal analysis or official source that confirms only part of the fact; **C** = directory, aggregate, local press, or unverified lead. Grade the fact, not the project.

---

## 0. Greece-Specific Enumeration Frame

- **No single public datacenter registry exists.** Build the census by joining Diavgeia transparency decisions, environmental records, e-adeies building permits, grid evidence, telecom-regulator records, strategic-investment decisions, company registry records, and official operator/cloud pages.
- **The new datacenter operating framework is real and should be treated as A-grade for licensing route.** Greece completed a specific data-center operation notification framework through Law 5069/2023 and Joint Ministerial Decision **96038/2024**. The Development Ministry/OpenBusiness announcement is at https://openbusiness-portal.mindev.gov.gr/oloklirothike-to-thesmiko-plaisio-gia-ta-data-centers/ and states that the framework applies from **1 March 2025**. It also gives the notification thresholds: third-party service datacenters at **>=200 kW IT equipment nominal electrical power** and self-use datacenters at **>=1,000 kW**. Use this instead of older generic industrial-licensing assumptions.
- **Environmental approval is still separate.** Law 5069/2023/JMD 96038/2024 do not replace environmental, building, fire-safety, land-use, grid-connection, or other permits. Environmental approvals appear through YPEN/e-PRM and Diavgeia; building permits through e-adeies/TEE; operational notification through OpenBusiness where applicable.
- **Attica is the primary hub but grid-constrained.** Official strategic-investment records confirm Microsoft Operations 4733 Hellas S.M.S.A. has a three-datacenter strategic investment in Attica: Site 6 in Spata-Artemida with 19.2 MW and Sites 27/28 in Koropi/Kropia with 9.6 MW each: https://ependyseis.mindev.gov.gr/en/stratigikes/erga/investment-in-data-centres-in-greece-2. ADMIE/IPTO planning and 2025-2026 Greek energy press describe large connection-request pressure; do not count connection requests as built capacity.
- **Cloud-region pages are seeds, not facility registries.** Microsoft officially announced a Greece datacenter region in 2020: https://news.microsoft.com/europe/2020/10/05/microsoft-announces-plans-for-first-datacenter-region-in-greece-as-part-of-gr-for-growth-digital-transformation-initiative/. Microsoft Local says the region is being introduced in the Attica area: https://local.microsoft.com/communities/emea/greece/. The current Azure regions list at https://learn.microsoft.com/en-us/azure/reliability/regions-list should be checked every run; as reviewed on 2026-08-12, Greece Central is not shown in the public table returned by that page, while Microsoft global-infrastructure pages still show Greece Central/Athens as coming soon. Do not mark it live without current Azure CLI/API or Microsoft GA evidence.
- **Connectivity is a strong siting signal but not facility evidence.** GR-IX, DE-CIX, Grid Telecom, submarine cable landing stations, and telecom PoPs point to likely hosting markets. Cable landing stations are not datacenters unless the source explicitly says they are hosted inside or paired with a datacenter campus.
- **Search Greek first.** Greek public records use `κέντρο δεδομένων`, `κέντρα δεδομένων`, `Κέντρα Δεδομένων`, `data center`, `datacenter`, `υποδομή νέφους`, `φιλοξενία εξοπλισμού`, `οικοδομική άδεια`, `άδεια δόμησης`, `γνωστοποίηση λειτουργίας`, `ΑΕΠΟ`, `ΜΠΕ`, `στρατηγική επένδυση`, `υποσταθμός`, `όροι σύνδεσης`, and `ΑΔΑ`.

---

## 1. Official Source Spine

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Diavgeia (Διαύγεια) | https://diavgeia.gov.gr and export/API URLs under https://diavgeia.gov.gr/luminapi/api/search/export | Mandatory publication of public decisions: environmental approvals, municipal decisions, procurement, public-sector datacenter projects, sometimes permits and revocations. Search by Greek terms, operator/SPV, municipality, and `ΑΔΑ`. | A |
| National Printing Office / FEK | https://www.et.gr | Laws, JMDs/KYAs, strategic-investment publication, environmental-classification amendments. Search `5069/2023`, `96038/2024`, `κέντρα δεδομένων`, `Κέντρα Δεδομένων`. | A |
| OpenBusiness | https://openbusiness.mindev.gov.gr and announcement page https://openbusiness-portal.mindev.gov.gr/oloklirothike-to-thesmiko-plaisio-gia-ta-data-centers/ | Operating-notification regime under Law 4442/2016 as amended by Law 5069/2023 and JMD 96038/2024. Confirms thresholds and effective date. | A |
| e-adeies / TEE | https://eadeies.gov.gr and support/info at https://web.tee.gr/e-adeies/ | Electronic building permits and pre-approvals. Search facility, municipality, owner/SPV, engineer, and permit year. Public search capability can vary; if not publicly searchable, use Diavgeia municipal references and TEE permit numbers. | A |
| YPEN environmental licensing | https://ypen.gov.gr/perivallon/perivallontiki-adeiodotisi/perivallontiki-adeiodotisi-ergon/ | Environmental-licensing framework and competent-authority routing. | A |
| e-PRM / Electronic Environmental Registry | https://eprm.ypen.gr and service/login surface https://platform.eprm.ypen.gr/ | Environmental study and approval records (`ΜΠΕ`, `ΑΕΠΟ`, `ΠΠΔ`) when public search is available. Pair with Diavgeia AEA/ADA. | A |
| ADMIE / IPTO | https://www.admie.gr and EN TYNDP page https://www.admie.gr/en/grid/development/ten-year-development-plan | Transmission-grid plans, public consultations, high-voltage substations, large-load connection context. Use for grid risk and connection evidence, not operational status. | A |
| HEDNO / DEDDIE | https://www.deddie.gr | Distribution-grid connections for smaller/edge facilities. | A |
| RAEEY | https://www.raaey.gr | Energy/water/waste regulator decisions, grid-code matters, operator restrictions. Not a datacenter registry. | A |
| EETT | https://www.eett.gr | Telecom operator validation, electronic-communications registry, decisions on operators that may host datacenters. Not a facility registry. | A |
| Ministry of Digital Governance | https://mindigital.gr | Cloud-first policy, government cloud, AI/HPC policy. Facility facts need GSIS/GRNET/procurement corroboration. | A/B |
| GSIS / G-Cloud | https://www.gsis.gr/en/public-administration/G-Cloud | Official government cloud page; confirms G-Cloud operates in Tier 3-grade datacenter infrastructure. Physical hosting sites need procurement/operator evidence. | A for program, B for physical sites |
| GRNET / EDYTE | https://grnet.gr and GR-IX page https://grnet.gr/en/gr-ix/ | Research network, GR-IX ownership/neutrality, public/research datacenter and HPC leads. | A |
| GR-IX | https://www.gr-ix.gr | Current Athens/Thessaloniki IXP POP/member evidence; use to validate active interconnection sites and operators. | A/B |
| Enterprise Greece | https://www.enterprisegreece.gov.gr | Investment-promotion and ICT-sector framing. Use as context, not facility proof unless it links to a named official project. | A/B |
| Strategic investments portal | https://ependyseis.mindev.gov.gr/en/stratigikes/erga/investment-in-data-centres-in-greece-2 | Microsoft Attica strategic-investment record with implementation entity, budget, sites, municipalities, and MW. | A |
| ΓΕΜΗ / business registry | https://www.businessregistry.gr | Resolve legal entities/SPVs and corporate relationships. | A/B |

---

## 2. Official Query Templates

### 2.1 Cross-Greece Official Searches

```text
site:diavgeia.gov.gr "κέντρο δεδομένων" OR "data center"
site:diavgeia.gov.gr "Κέντρα Δεδομένων" "ΑΕΠΟ"
site:diavgeia.gov.gr "data center" "οικοδομική άδεια"
site:diavgeia.gov.gr "data center" "γνωστοποίηση λειτουργίας"
site:diavgeia.gov.gr "{SPV or operator}" "data center"
site:diavgeia.gov.gr "{municipality}" "κέντρο δεδομένων"
site:eprm.ypen.gr "data center" OR "κέντρο δεδομένων"
site:eadeies.gov.gr "data center" "{municipality}"
site:et.gr "5069/2023" "κέντρα δεδομένων"
site:et.gr "96038/2024" "Κέντρα Δεδομένων"
site:openbusiness-portal.mindev.gov.gr "data centers" "96038/2024"
site:admie.gr "data center" OR "κέντρα δεδομένων" OR "όροι σύνδεσης"
site:raaey.gr "data center" OR "κέντρα δεδομένων"
site:eett.gr "{operator}" "μητρώο" OR "πάροχος"
site:gsis.gr "G-Cloud" "data center"
site:grnet.gr "data center" OR "Daidalos" OR "GR-IX"
```

### 2.2 Project-Level Official Searches

```text
"{operator}" "{SPV}" "ΑΔΑ"
"{operator}" "{municipality}" "ΑΕΠΟ"
"{operator}" "{municipality}" "ΜΠΕ"
"{operator}" "{municipality}" "οικοδομική άδεια"
"{operator}" "{municipality}" "γνωστοποίηση λειτουργίας"
"{project name}" "στρατηγική επένδυση" "data center"
"{site name}" "ισχύς" "MW" "data center"
```

Known SPV/operator pivots to seed: `MICROSOFT OPERATIONS 4733 HELLAS`, `DATA IN SCALE`, `EDGNEX`, `DAMAC`, `PPC`, `ΔΕΗ`, `LAMDA HELLIX`, `Digital Realty`, `DATA4`, `Dromeus`, `Apto`, `Serverfarm`, `Grid Telecom`, `Quadrivium`, `Lancom`, `Synapsecom`, `OTE`, `COSMOTE`, `Vodafone`, `Nova`, `GRNET`, `ΓΓΠΣΨΔ`.

### 2.3 Greek Lifecycle Terms

```text
μνημόνιο συνεργασίας / πρόθεση / ανακοίνωση = intent only
προέγκριση οικοδομικής άδειας = pre-approval; not a final building permit
ΜΠΕ / μελέτη περιβαλλοντικών επιπτώσεων = environmental study submitted
ΑΕΠΟ / έγκριση περιβαλλοντικών όρων = environmental terms approved
οικοδομική άδεια / άδεια δόμησης = building permit
γνωστοποίηση λειτουργίας = operating notification under Law 4442/2016/Law 5069/2023/JMD 96038/2024
άδεια εγκατάστασης / άδεια λειτουργίας = installation / operation permit where still applicable
έναρξη εργασιών / κατασκευή / εργοτάξιο = construction started
παράδοση / θέση σε λειτουργία / λειτουργεί = operational
```

---

## 3. Per-Division Official Strategy (13 Regions + Mount Athos)

For every division, run the national official queries plus the Greek/English division names. Regions do not maintain complete datacenter registries; use regional and municipal searches mainly to locate environmental files, building-permit references, public consultations, and council decisions.

| Division | Priority | Official route | Target places / known official pivots | Query notes |
|---|---:|---|---|---|
| **Mount Athos / Άγιο Όρος** | Exclude / negative control | No normal regional permitting route; autonomous monastic polity under Greek sovereignty. Check only if a source claims a site. | Karyes, Dafni. | Do not include monastery IT rooms as commercial datacenters. Search `Άγιο Όρος "κέντρο δεδομένων"` once as a negative-control sweep. |
| **Eastern Macedonia and Thrace / Ανατολική Μακεδονία και Θράκη** | Low/medium | Region environmental decisions, Diavgeia, e-adeies, ADMIE energy-hub material. | Alexandroupoli, Kavala, Komotini, Xanthi, Drama. | Watch energy/security-hub narratives around Alexandroupoli; require permits or grid terms before counting. |
| **Central Macedonia / Κεντρική Μακεδονία** | High | Region/municipal decisions, e-adeies Thessaloniki metro, EETT operator validation, GR-IX Thessaloniki. | Thessaloniki, Kalochori/Ionia, Sindos, Thermi, Pylaia, Kalamaria. Operators: Lancom, Synapsecom, OTE/Cosmote; GR-IX::Thessaloniki. | Search `Θεσσαλονίκη data center`, `Κεντρική Μακεδονία κέντρο δεδομένων`, operator + municipality. Hyperscale interest remains B/C until official records. |
| **Western Macedonia / Δυτική Μακεδονία** | Low/medium | Region environmental files, ADMIE grid studies, Just Transition materials, Diavgeia. | Kozani, Ptolemaida, Florina, Kastoria, Grevena. | Power-transition narrative is real, but facility evidence is usually weak. Search `Δυτική Μακεδονία data center`, `Πτολεμαΐδα κέντρο δεδομένων`, `Κοζάνη data center`. |
| **Epirus / Ήπειρος** | Low | Region environmental files, e-adeies, university/public-sector procurement. | Ioannina, Arta, Preveza, Igoumenitsa. | Mostly edge, university, and enterprise server-room leads. Do not count without facility-grade evidence. |
| **Thessaly / Θεσσαλία** | Medium | Region/municipal files, Diavgeia, e-adeies, DEDDIE/ADMIE. | Volos, Larissa, Trikala, Karditsa. | Volos appears in market-report pipeline lists; verify with `Βόλος data center ΑΕΠΟ`, `Λάρισα κέντρο δεδομένων`, and permits. |
| **Ionian Islands / Ιόνια Νησιά** | Low | Region environmental files, municipal permits, cable context. | Corfu, Kefalonia, Zakynthos, Lefkada. | Greece-Italy connectivity can create leads; treat as edge/telecom until a facility source appears. |
| **Western Greece / Δυτική Ελλάδα** | Low/medium | Region environmental files, Diavgeia, Patras university/science-park procurement. | Patras, Agrinio, Pyrgos, Mesolongi, Aigio. | Patras has research/telecom potential; require permits/operator pages for commercial census. |
| **Central Greece / Στερεά Ελλάδα** | Medium | Region environmental files, e-adeies, Diavgeia, ADMIE substations. | Chalkida, Oinofyta, Thiva, Lamia, Livadeia. | Search as Attica spillover: `Οινόφυτα data center`, `Θήβα κέντρο δεδομένων`, `Στερεά Ελλάδα data center`. Industrial land and grid access are leads, not proof. |
| **Attica / Αττική** | Very high | Diavgeia/e-PRM for AEO/AEEP, e-adeies for Spata/Koropi/Paiania/Koropi permits, strategic investments portal, municipal decisions, ADMIE. | Spata-Artemida, Koropi/Kropia, Paiania, Markopoulo, Keratea, Lavrio, Athens, Marousi, Renti, Metamorfosi, Aspropyrgos, Elefsina, Mandra. Official anchors: Microsoft Operations 4733 Hellas strategic investment; OpenBusiness/Law 5069 framework; GRNET/G-Cloud public infrastructure. | Highest risk of duplicates and speculative capacity. Separate Microsoft strategic-investment sites from Digital Realty Koropi, DATA4 Paiania, EDGNEX/Data In Scale Spata, Dromeus/Apto Spata, OTE/Cosmote, Lancom, Synapsecom, and government/research facilities. |
| **Peloponnese / Πελοπόννησος** | Low | Region environmental files, e-adeies, Diavgeia, grid/cable context. | Corinth, Tripoli, Kalamata, Nafplio, Megalopolis. | Corinth proximity to Attica and Megalopolis power-transition stories are leads only. Search `Κόρινθος data center`, `Τρίπολη κέντρο δεδομένων`, `Μεγαλόπολη data center`. |
| **North Aegean / Βόρειο Αιγαίο** | Low | Region environmental files, DEDDIE island-grid context, municipal procurement. | Mytilene/Lesbos, Chios, Samos, Lemnos, Ikaria. | Edge/public-sector IT rooms only unless operator evidence appears. |
| **South Aegean / Νότιο Αιγαίο** | Low | Region environmental files, cable and island interconnection context, municipal permits. | Syros, Rhodes, Kos, Santorini, Naxos, Milos. | Milos is a cable-node lead for Vodafone Thetis Express; cable node does not equal datacenter. Search `Μήλος data center`, `Ρόδος κέντρο δεδομένων`. |
| **Crete / Κρήτη** | Medium/high | Region of Crete environmental files, e-adeies Heraklion/Chania, Diavgeia, ADMIE Crete-mainland interconnector, official operator pages. | Heraklion, Chania, Tympaki, Sitia, Rethymno, Agios Nikolaos. Official anchors: Digital Realty HER1 page at https://www.digitalrealty.com/data-centers/emea/heraklion/her1 and press release at https://www.digitalrealty.com/about/newsroom/press-releases/123317/digital-realty-unveils-first-data-center-in-crete-enhancing-eastern-mediterranean-connectivity; Grid Telecom/Quadrivium Chania CLS within a 20 MW interconnection datacenter campus. | Strong cable-driven pipeline. Verify power and interconnector assumptions before counting MW; separate Heraklion DCs, Chania CLS/datacenter campus, and Tympaki cable landing. |

---

## 4. Reliability Rules

| Evidence | Grade | Use |
|---|---|---|
| Diavgeia/FEK decisions, e-PRM records, e-adeies building permits, OpenBusiness operating notifications | A | Facility/project existence, legal proponent, location, permit stage, statutory route. |
| Strategic investments portal / official ministry project page | A | Strategic-investment status, implementation entity, budget, official site/municipality and stated power where listed. |
| ADMIE/HEDNO/RAEEY official material | A | Grid route, connection constraints, energy-regulatory context. Do not infer built datacenter from connection demand. |
| EETT operator registry/decisions | A | Company/operator status; not facility count or capacity. |
| Cloud provider official pages | A for region announcement/status; B for physical facility count/location unless site-specific public records exist. |
| Operator official facility pages and press releases | A- for existence when page is facility-specific; B for capacity/timing unless commissioned or licensed. |
| Strong trade/legal press | B | Leads, project status, legal interpretation; back-resolve to official records. |
| Directories and market reports | C | Lead generation only. |

Status rules:
- Count **operational** only with an operating notification/license, operator live facility page, Uptime/certification evidence tied to a live site, active PeeringDB/IX evidence for colocation use, or cloud-region GA evidence.
- Count **under construction** only with building permit plus contractor/operator start-of-works evidence.
- Count **approved/planned** with strategic-investment approval, AEPO, building permit/pre-approval, or official operator announcement; keep separate from live capacity.
- Treat `μνημόνιο`, `πρόθεση`, `αναμένεται`, investment totals, and aggregate GW requests as non-operational pipeline.

Capacity rules:
- Keep separate fields for `IT load MW`, `installed electrical power`, `grid connection MVA/MW`, `total site power`, and `marketing campus capacity`.
- Never convert euros, hectares, racks, or square meters into MW.
- For islands and Crete, cross-check grid/interconnector capacity and local environmental approvals before accepting large MW claims.

Deduplication keys:

```text
legal SPV/proponent + municipality + campus/site name + permit/AEO/AEEP number + Diavgeia ADA + operator facility code
```

Duplicate traps: Microsoft cloud region vs three Attica sites; `Microsoft` vs `Microsoft Operations 4733 Hellas`; EDGNEX vs DAMAC vs PPC vs `Data In Scale`; Lamda Hellix vs Digital Realty vs ATH1/ATH2/ATH3/ATH4/ATH5; cable landing station vs datacenter; government/research infrastructure vs commercial colocation; DEDDIE/ADMIE connection requests vs built facilities.

---

## 5. Recommended Official Workflow

1. Seed named projects from official cloud/operator pages and the strategic-investment portal.
2. Resolve the legal proponent/SPV through the strategic-investment page, FEK/Diavgeia, and ΓΕΜΗ.
3. Search Diavgeia for the SPV, municipality, Greek lifecycle terms, and `ΑΔΑ`.
4. Search e-PRM/YPEN for environmental records and match them to Diavgeia AEO/AEEP decisions.
5. Search e-adeies/TEE and municipal pages for building permits and pre-approvals.
6. Search OpenBusiness for operating notification evidence for facilities above the Law 5069/JMD 96038 thresholds.
7. Check ADMIE/HEDNO/RAEEY for connection and grid constraints; record requested/approved connection separately.
8. Check EETT for telco operator legitimacy and GR-IX/PeeringDB for active interconnection evidence.
9. Backfill with industry/trade press only after official surfaces have been exhausted, and downgrade any unverified fact to B or C.
10. Run the 14-division table explicitly, even if the result for Mount Athos or low-priority island regions is “no facility-grade evidence found.”
