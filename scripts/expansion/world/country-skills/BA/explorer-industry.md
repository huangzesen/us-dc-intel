# BA Explorer Industry - Bosnia and Herzegovina Operator, Vendor, Trade-Press, and Division-Level Query Methodology

Date: 2026-08-12. Scope: Bosnia and Herzegovina (BA), division-level datacenter enumeration across the 3 world-manifest.jsonl divisions: **Federation of Bosnia and Herzegovina (FBiH)**, **Republika Srpska (RS)**, and **Brcko District (BD)**. Angle: **industry/vendor-led discovery** for colocation providers, telecom/cloud operators, state/utility projects, cloud-region exclusion, trade press, associations, and local-language query patterns. Reliability grades: **A** = operator official page, government/primary source, public procurement, regulator, corporate announcement; **B** = reputable local/international trade press, contractor case study with named site; **C** = directory/marketplace/SEO listing, unclear reseller page, or unverified aggregate.

> Final review note: key operator, trade-press, directory, and official exclusion URLs were re-checked in August 2026. Dynamic portals and directories can change quickly; use this as a methodology and seed list, not a finished census. Yield estimates below are planning numbers, not census results.

---

## 0. Market Frame

- BiH is a **small, telecom-led market with no hyperscale public-cloud region**. A realistic census is roughly **8-15 records**: a few operator-owned colocation/data-center sites (BH Telecom Sarajevo, HT Eronet Mostar, LANACO Banja Luka, Globalhost Novi Travnik, plus Integra Banja Luka as a lead to verify), telecom internal/network server rooms (m:tel/Telekom Srpske), public-sector/internal micro data centers (IDDEEA, Central Bank of BiH, universities, ministries), and a handful of planned/proposed state projects (RS state datacenter, University of Tuzla, Zenica steelworks proposal, BH Telecom modular DC, BH Telecom-AWS sovereign cloud). Many "data centar" hits are retail computer shops, institutional server rooms, or cloud-service products - grade strictly.
- **Division yields**: FBiH is the highest-yield division (Sarajevo + Mostar + Novi Travnik + Tuzla + Zenica); RS is second (Banja Luka cluster + planned state DC); Brcko District is very low yield (municipal server rooms only). See section 4.
- **Language is essential.** Search both English and BCS variants: `data centar`, `data center`, `centar podataka`, `podatkovni centar`, `kolokacija`, `telehousing`, `server sala`, `serverska sala`, `rezervni data centar`, `DR lokacija`, `disaster recovery`, `agregat`, `UPS`, `ISO 27001`, `Tier III`, plus **Cyrillic** variants for RS content (`центар података`, `колокација`).
- Treat `cloud`, `Virtual Data Center`, `VPS`, `hosting` pages as **service leads only** unless the page names a physical BiH facility, address, municipality, or operator-owned colocation room.
- Hyperscale cloud-region pages reviewed as exclusion sources: AWS, Azure, Google Cloud, and Oracle Cloud do not list a BiH public cloud region/local zone. Use these official vendor lists to rule out cloud-region enumeration, not to find municipal projects. The BH Telecom-AWS "sovereign cloud" MoU (2025) is a local hosting/edge arrangement, not an AWS region.

---

## 1. Priority Operator and Facility Sweep

### 1.1 Confirmed or High-Value Operator Seeds

| Operator / facility lead | URL / source surface | Municipality / division | Evidence use |
|---|---|---|---|
| BH Telecom Data Centar (colo + DR site) | https://www.bhtelecom.ba/usluge-za-poslovne-korisnike/2019/09/nova-cloud-usluga-kolokacija-u-data-centru-bh-telecoma/ | Sarajevo (FBiH) | Grade A operator/service page: Data Centar described as primary DR site in BiH; colocation incl. racks, cooling, uninterrupted power, direct user links, managed services. |
| BH Telecom modular datacenter tender | https://seenews.com/news/bosnias-bh-telecom-opens-tender-for-works-on-modular-data-centre-1235646 | Sarajevo (FBiH) | Grade B (SeeNews, Sep 2023) - tender for modular DC construction works; seek BH Telecom tender/contract-award pages for Grade A. |
| BH Telecom-AWS sovereign cloud MoU | https://btw.media/en/bh-telecom-and-aws-launch-sovereign-cloud ; https://www.telecomrevieweurope.com/articles/telecom-operators/bh-telecom-aws-to-power-bosnias-digital-future/ ; https://connectingregion.com/news/bosnias-digital-future-with-amazon/ ; https://capacityglobal.com/news/bh-telecom-aws-bosnia/ | Sarajevo (FBiH) | Grade B (Jun 2025): MoU for sovereign cloud for BiH public sector; service/partnership lead, not a new facility. |
| HT Eronet Data Centar (georedundant) | https://www.hteronet.ba/digitalna-rjesenja/ht-eronet-data-centar-pg368 | Mostar (FBiH) | Grade A operator/service page for the data-center service; pair with kolokacija page (https://www.hteronet.ba/poslovni-korisnici/kolokacija-posluzitelja-pg64 and indexed `/digitalna-rjesenja/kolokacija-posluzitelja-s116`). |
| m:tel / Telekom Srpske Virtual Data Center | https://mtel.ba/Poslovni/ICT/Cloud-infrastruktura/Virtual-Data-Center ; https://mtel.ba/Press-centar/a14296-Prezentacija-usluga-u-m-tel-Biznis-centru.html | Banja Luka (RS) | Grade B/C service lead (VPS/NaaS); physical m:tel DC unverified - search `mtel data centar` + Banja Luka permits. |
| Integra Data Centar (Integra Inženjering d.o.o.) | https://integradc.net/ ("Poslovni centar Integra DC") | Banja Luka (RS) | Grade B/C commercial colo lead on company site; confirm address and permits via Grad Banja Luka + e-Nabavke. |
| LANACO Technology Center / Data Center | https://www.tehnoloskicentar.ba/ ; https://tehnoloskicentar.com/ ; https://lanacocloud.com/cloud.php (colo, data in country); https://www.lanaco.com/bs/cloud-i-data-infrastruktura ; profile https://ba.bloombergadria.com/biznis/kompanije/91773/lanaco-prica-od-banjaluke-do-sad-a-australije-i-afrike/news | Banja Luka (RS) | Grade B company/operator evidence for a named data center and cloud/colo offers; promote to Grade A only with permit, procurement, official opening, or audited certification/source document. |
| Globalhost Data Center | https://www.global.ba/dc.php ; https://www.global.ba/kolokacija.php ; https://www.global.ba/en/kolokacija.php | Novi Travnik (FBiH / Central Bosnia Canton) | Grade B company-site evidence: current pages describe colocation in Globalhost's data center located in Novi Travnik; confirm address/permits before Grade A. |
| RS state datacenter (planned) | https://detektor.ba/2026/05/14/republika-srpska-planira-izgadnju-data-centra-po-uzoru-na-srbiju/ ; regional mirrors such as BIRN/N1 | RS (site TBD) | Grade B intent (modeled on Serbia's Kragujevac DC); status `planned`; track `vladars.rs` digitalization ministry + e-Nabavke. |
| University of Tuzla datacenter (concept) | https://www.klix.ba/vijesti/bih/pogledajte-kako-bi-trebao-izgledati-data-centar-u-tuzli-za-digitalno-umrezavanje-svih-institucija/250403114 | Tuzla (FBiH) | Grade B/C concept design (Apr 2025) presented to Tuzla Canton Government; track TK gov + university procurement. |
| Zenica old steelworks datacenter (proposal) | https://www.zenicablog.com/sdp-zenica-stara-zeljezara-zenica-nova-sansa/ | Zenica (FBiH) | Grade C political proposal (Jan 2026); count only after government/planning action. |
| IDDEEA state IT estate | https://iddeea.gov.ba/ | Sarajevo (state level) | Grade B lead for state identity/CIPS/data-exchange infrastructure; probe procurement for server-room/DR projects. |
| BHIX (BiH Internet Exchange) | https://bhix.net/ | Sarajevo area (FBiH) | Grade A for the IXP; participant lists help discover operators/hosting firms. |

### 1.2 Operator Search Templates

```text
"{operator}" "Bosna i Hercegovina" "data centar"
"{operator}" BiH "data center"
"{operator}" "kolokacija" BiH
"{operator}" telehousing "BiH"
"{operator}" "Sarajevo" "data centar"
"{operator}" "Banja Luka" "data centar"
"{operator}" "Mostar" "data centar"
"{operator}" "Tuzla" OR "Zenica" "data centar"
"{operator}" "ISO 27001" "data centar"
"{operator}" "Tier III" "BiH"
"{operator}" "agregat" "UPS" "data centar"
site:{operator-domain} "data centar"
site:{operator-domain} "kolokacija"
site:{operator-domain} "telehousing"
```

Targeted strings:

```text
"BH Telecom" "Data Centar" "Sarajevo"
"BH Telecom" "modular" "data centar"
"HT Eronet" "data centar" "Mostar"
"m:tel" OR "Telekom Srpske" "data centar" "Banja Luka"
"Integra" "data centar" "Banja Luka"
"Lanaco" "data centar"
"Globalhost" "data centar" "Novi Travnik"
"Globalhost" "kolokacija" "Novi Travnik"
("Republika Srpska" "državni data centar") OR ("Republika Srpska" "state data center")
"Univerzitet u Tuzli" "data centar"
"Zenica" "data centar" "Željezara"
"IDDEEA" "data centar" OR "server sala"
"BHIX" participants
```

---

## 2. Trade Press, Associations, and Directories

| Source | URL / query surface | BiH use | Grade |
|---|---|---|---|
| Klix | https://www.klix.ba/ | Best Sarajevo/BiH-wide portal for project announcements (e.g., Tuzla DC concept 2025). | B |
| Dnevni avaz | https://avaz.ba/ | Business/politics coverage incl. Brcko District items. | B |
| Nezavisne novine | https://www.nezavisne.com/ | RS/Banja Luka business and politics coverage. | B |
| Glas Srpske | https://www.glassrpske.com/ | RS regional coverage (search `data centar`). | B |
| Oslobođenje / FENA / Federalna | oslobodjenje.ba ; fena.ba ; https://www.federalna.ba/ | FBiH state agency and government news. | B |
| Capital.ba / Akta.ba / SEEbiz / SeeNews | capital.ba ; akta.ba ; seeebiz.eu ; https://seenews.com/ | Business/finance and regional infrastructure news (e.g., BH Telecom modular DC tender). | B |
| BIRN | https://birn.rs/ (regional) | RS state datacenter plan reporting (2023-2024). | B |
| btw.media / telecomrevieweurope / capacityglobal | btw.media ; telecomrevieweurope.com ; capacityglobal.com | BH Telecom-AWS sovereign cloud MoU coverage (Jun 2025). | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | Regional DC project coverage; low BiH-specific volume. | B |
| US trade.gov country guide | https://www.trade.gov/country-commercial-guides/bosnia-and-herzegovina-telecommunications-industry | Market context and operator structure (BH Telecom / HT Eronet / M:Tel). | B (context) |
| Chamber of Commerce RS | https://komorars.ba/ | RS business ecosystem; member directories; search `data centar`, `IT`. | B/C |
| Chamber of Commerce FBiH | https://kfbih.com/ | FBiH business ecosystem and events. | B/C |
| Foreign Trade Chamber of BiH | https://komorabih.ba/ | Lists BiH chambers incl. Brcko; useful for vendor/ecosystem discovery. | B/C |
| BITO (IT association BiH) | search `BITO udruženje informacione tehnologije BiH` | ICT association/member ecosystem; domain not verified in this pass. | C |
| RAK | https://www.rak.ba/ | Telecom operator universe, market reports; official portal may time out or return gateway errors to automated fetches, so use search/cache fallbacks. | A (regulator data when retrieved) |
| e-Nabavke portal | https://www.ejn.gov.ba/ | All public tenders; search `data centar`, `server sala`, `kolokacija`, `UPS`, `agregat`, `izgradnja`. | A |
| DataCenterMap BiH | https://www.datacentermap.com/bosnia-and-herzegovina/ | Directory seed (~4 facility listings incl. Sarajevo/Banja Luka/telecom entries); verify every listing. | C |
| Datacenters.com BiH | https://www.datacenters.com/locations/bosnia-and-herzegovina | Directory seed for colo/IaaS providers. | C |
| PeeringDB | https://www.peeringdb.com/ | Facility/network seeds; search country BA. | C |
| Cloudscene / Inflect / LinkedIn | cloudscene.com ; inflect.com ; linkedin.com | Address/capacity seeds and company pages; never final proof. | C |

Trade and association queries:

```text
site:klix.ba "data centar"
site:avaz.ba "data centar"
site:nezavisne.com "data centar"
site:glassrpske.com "data centar"
site:federalna.ba "data centar"
site:seenews.com Bosnia ("data centre" OR "data center")
site:komorars.ba ("data centar" OR "informacione tehnologije")
site:kfbih.com ("data centar" OR "digitalizacija")
site:rak.ba ("data centar" OR "kolokacija")
site:ejn.gov.ba ("data centar" OR "server sala")
"BITO" "informacione tehnologije" "BiH"
```

---

## 3. Cloud Region and Vendor Exclusion Pass

Use official hyperscale location pages as **A-grade negative evidence** for public cloud regions:

```text
site:aws.amazon.com/about-aws/global-infrastructure/ Bosnia
site:azure.microsoft.com/en-us/explore/global-infrastructure/geographies Bosnia
site:cloud.google.com/about/locations Bosnia
site:oracle.com/cloud/public-cloud-regions/ Bosnia
```

As of this methodology pass, no AWS/Azure/GCP/OCI BiH public cloud region/local zone was identified. BiH projects therefore surface through telecom operator pages, government digitalization contracts, utility-sector ICT, local press, contractor references, and directories.

For non-hyperscale vendors/integrators, search:

```text
"Schneider Electric" "data centar" "BiH"
"Vertiv" "data centar" "BiH"
"Huawei" "data centar" "BiH"
"Cisco" "data centar" "BiH"
"Nutanix" "data centar" "BiH"
"VMware" "data centar" "BiH"
"Rittal" OR "APC" OR "Eaton" "server sala" "BiH"
"protivpožarni sistem" "data centar" "BiH"
"rashladni sistem" "data centar" "BiH"
"integracija" "data centar" "Banja Luka" OR "Sarajevo" OR "Mostar"
```

Use integrator case studies as Grade B/C corroboration for a named site; require operator or permit confirmation before strong enumeration.

---

## 4. Division Enumeration Recipes (world-manifest.jsonl divisions)

### 4.1 Universal sweep (all three divisions)

```text
"{division}" "data centar"
"{division}" "data center"
"{division}" "centar podataka"
"{division}" "kolokacija"
"{division}" "server sala"
"{division}" "rezervni data centar"
"{division}" "disaster recovery"
"{division}" "ISO 27001" "data centar"
"{division}" "Tier III" "data centar"
"{division}" "UPS" "agregat" "data centar"
site:ejn.gov.ba "{division}" ("data centar" OR "server sala")
site:rak.ba "{division}" operator
```

### 4.2 Federation of BiH (FBiH) - 10 cantons

Highest-yield cantons first: **Sarajevo, Herzegovina-Neretva (Mostar), Central Bosnia/Novi Travnik, Tuzla, Zenica-Doboj**; compact sweep for the other five (Una-Sana, Posavina, Bosnian Podrinje, West Herzegovina, Canton 10).

```text
"Sarajevo" "data centar" "BH Telecom"
"Novi Travnik" "Globalhost" "data centar"
"Srednjobosanski kanton" "Globalhost" "data centar"
"Sarajevo" "kolokacija" "data centar"
"Mostar" "HT Eronet" "data centar"
"Mostar" "NSoft" "data centar"   (unverified lead - verify)
"Tuzla" "data centar" "Univerzitet"
"Zenica" "data centar" "Željezara"
"Bihać" "data centar"
"Kanton Sarajevo" "urbanistička saglasnost" "data centar"
"{canton}" "građevinska dozvola" "data centar"
"{canton}" "server sala" "javna nabavka"
```

Sarajevo city municipalities (Centar, Stari Grad, Novo Sarajevo, Novi Grad, Ilidža) and Mostar/Tuzla/Zenica municipal services are the permit-level targets.

### 4.3 Republika Srpska (RS)

Banja Luka is the hub (m:tel/Telekom Srpske, Integra DC, Lanaco, RS government). Secondary cities: Bijeljina, Doboj, Prijedor, Istočno Sarajevo, Trebinje.

```text
"Banja Luka" "data centar" ("m:tel" OR "Telekom Srpske")
"Banja Luka" "Integra" "data centar"
"Banja Luka" "Lanaco" "data centar"
"Republika Srpska" "državni data centar"
"Republika Srpska" "data centar" "Vlada"
("Bijeljina" OR "Doboj" OR "Prijedor" OR "Trebinje") "data centar"
"Istočno Sarajevo" "data centar"
"Република Српска" "центар података"
"{rs-municipality}" "server sala" "UPS" "agregat"
```

### 4.4 Brcko District (BD)

Single-district compact sweep; expect internal/municipal server rooms at most.

```text
"Brčko distrikt" "data centar"
"Brcko" "data center"
"Brčko" "server sala"
"Brčko" "informacioni sistem" "Vlada"
"Brčko" "kolokacija"
"JP Komunalno Brčko" "informacioni"
site:vlada.bdcentral.net ("data centar" OR "informaciona tehnologija")
site:ppipo.bdcentral.net ("građevinska dozvola" OR "ekološka dozvola" OR "lokacijski uslovi") "Brčko"
```

### 4.5 Diacritic/variant handling

```text
Brčko OR Brcko
Široki Brijeg OR Siroki Brijeg
Istočno Sarajevo OR Istocno Sarajevo
Željezara OR Zeljezara
Tuzlanski kanton OR TK
Hercegovačko-neretvanski kanton OR HNK
Zeničko-dobojski kanton OR ZDK
Cyrillic: центар података, грађевинска дозвола, колокација
```

---

## 5. Directory-to-Primary Verification Workflow

1. Seed from DataCenterMap BiH, Datacenters.com BiH, PeeringDB, Cloudscene, and contractor/integrator project pages.
2. Search the exact facility/operator string on the operator's official domain (bhtelecom.ba, hteronet.ba, mtel.ba, integradc.net, lanaco.com, global.ba).
3. Search local press (Klix, Avaz, Nezavisne, Glas Srpske, Federalna, Capital, Akta, FENA) for opening/certification/project history.
4. Search e-Nabavke (ejn.gov.ba) and ecjn.gov.ba for construction, colocation, UPS, generator, cooling, fire-suppression, and DR tenders; check telco own tender pages.
5. Search government portals (`fbihvlada.gov.ba`, `vladars.rs` with `vladars.net` redirects, `vlada.bdcentral.net`, `ppipo.bdcentral.net`) and digitalization ministries for state datacenter projects.
6. Search RAK register and telecom market reports to confirm operator identity and active status.
7. If still directory-only, record as Grade C and explicitly name missing proof: current operator page, address, permit/procurement, or opening announcement.

Directory queries:

```text
site:datacentermap.com/bosnia-and-herzegovina ("{operator}" OR "{municipality}")
site:datacenters.com/locations/bosnia-and-herzegovina "{operator}"
site:peeringdb.com Bosnia ("{operator}" OR "{facility}")
site:cloudscene.com Bosnia "{operator}" "data center"
site:inflect.com Bosnia "{operator}" "data center"
```

---

## 6. Capacity and Status Extraction

- BiH sources rarely disclose MW. Preserve disclosed proxies instead of inventing capacity: square meters, rack count, certified standards, redundancy tier, ISO certificates, UPS/generator/fire-suppression scope, project value (KM or EUR), and tender scope.
- BH Telecom describes its Data Centar as the primary DR site in BiH with managed colocation services (Grade A service evidence); capacity numbers should come from tenders/annual reports, not press.
- For Integra/LANACO/Globalhost, company-site claims are Grade B unless supported by a primary permit/procurement/opening/certification document; seek permits, annual reports, or press with numbers.
- For RS state DC, University of Tuzla DC, and Zenica proposal, status stays `planned/proposed` until procurement, government acceptance, operator opening, or site-specific construction evidence appears.
- For m:tel Virtual Data Center, treat as a cloud service; count a physical facility only with address/permit/opening evidence.

Capacity queries:

```text
"{facility}" "MW" OR "MVA" OR "kW"
"{facility}" "m2" OR "kvadrata"
"{facility}" "rack" OR "ormar"
"{facility}" "Tier III" OR "TIER 3"
"{facility}" "ISO 27001" OR "ISO 27701"
"{facility}" "UPS" OR "agregat" OR "dizel agregat"
"{facility}" "protivpožarni" OR "protivpozarni"
"{facility}" "investicija" "KM" OR "EUR" OR "miliona"
```

---

## 7. Known Seed List for Later Validation

This is a methodology seed list, not a final census. Re-check every item during enumeration.

| Seed | Municipality / division | Status tendency | Best evidence path |
|---|---|---|---|
| BH Telecom Data Centar (colo + DR) | Sarajevo (FBiH) | Operational | BH Telecom colocation page (A) + tender records + modular DC tender (B) |
| HT Eronet Data Centar (georedundant) | Mostar (FBiH) | Operational | HT Eronet official pages (A) + permits |
| Globalhost Data Center | Novi Travnik (FBiH / Central Bosnia Canton) | Operational (company site) | global.ba DC/kolokacija pages (B) + address/permit confirmation |
| m:tel / Telekom Srpske DC | Banja Luka (RS) | Service lead, physical unverified | mtel.ba VDC pages (B/C) + permits/tenders |
| Integra Data Centar | Banja Luka (RS) | Operational (company site) | integradc.net (B/C) + Grad Banja Luka permits + e-Nabavke |
| LANACO Technology Center / Data Center | Banja Luka (RS) | Operational (company site) | tehnoloskicentar.ba/.com + lanaco.com/lanacocloud.com (B) + Bloomberg Adria profile |
| RS state datacenter | RS, site TBD | Planned | Detektor/BIRN/N1 (B) + `vladars.rs` digitalization + e-Nabavke tenders |
| University of Tuzla DC | Tuzla (FBiH) | Concept | Klix (B/C) + TK government + university procurement |
| Zenica steelworks DC | Zenica (FBiH) | Political proposal | zenicablog (C) + ZDK planning action |
| BH Telecom modular DC | Sarajevo (FBiH) | Tender (2023) | SeeNews (B) + BH Telecom tender pages |
| BH Telecom-AWS sovereign cloud | Sarajevo (FBiH) | MoU/service | btw.media etc. (B) + BH Telecom official announcement |
| IDDEEA state IT estate | Sarajevo (state) | Operational internal | iddeea.gov.ba (A/B) + e-Nabavke |
| Central Bank of BiH / UIO / ministries server rooms | Sarajevo and entity seats | Internal | e-Nabavke + gazette decisions (A when named) |
| BHIX peering participants | Sarajevo area (FBiH) | Operational | bhix.net (A) + PeeringDB |
| NSoft data center (Mostar) | Mostar (FBiH) | Unverified in this pass | Verify via company site/press before counting |
| Old directory-era leads (e.g., historical Comping/other Sarajevo listings) | Sarajevo (FBiH) | Unverified/inactive likely | Directory entries only (C); require primary confirmation |
