# IN Explorer — Industry / Trade Press / Vendor Discovery for India Datacenters

Date: 2026-08-11. Scope: how to enumerate India (IN) datacenter projects through English and Hindi search, trade press, vendor/operator pages, industry bodies, and state/district query patterns. Reliability grades: **A** = primary/official/operator/investor disclosure, **B** = established trade press / industry association / strong market research, **C** = weak secondary / aggregators / social posts / local promotional MoUs.

---

## 0. India-specific frame

- India does **not** have one public datacenter facility registry. Enumeration works by triangulating: operator location pages, hyperscaler region pages, DCD/ET/DataQuest/Voice&Data articles, state investment portals, industrial-development authority allotments, SEIAA/SPCB environment records, fire/building permits where public, power utility tenders, and MCA company/SPV records.
- The main commercial hubs are metro/industrial districts, not all state capitals: **Mumbai/Navi Mumbai/Thane/Rabale/Airoli/Chandivali/Powai/Palava**, **Chennai/Ambattur/Siruseri/SIPCOT/Oragadam**, **Hyderabad/Rangareddy/FAB City/Bharat Future City**, **Noida/Greater Noida/Yamuna Expressway**, **Bengaluru/Whitefield/Electronic City/KIADB Aerospace Park/Hoskote**, **Pune/Hinjewadi/Kharadi**, **Kolkata/New Town/Rajarhat/Hindmotor**, plus emerging **Ahmedabad/GIFT City/Dholera**, **Visakhapatnam**, **Bhubaneswar**, **Jaipur**, **Lucknow**, **Patna**, **Indore/Bhopal**, **Nagpur**, **Mohali/Chandigarh**.
- State policy matters. Dedicated DC or IT/ITES policies exist or are active in: **Maharashtra**, **Tamil Nadu**, **Telangana**, **Uttar Pradesh**, **West Bengal**, **Odisha**, **Karnataka** (policy reported/finalizing), **Gujarat** (2026 policy reported), **Andhra Pradesh**. Use policy pages to find named parks, single-window portals, subsidy approvals, and agency contact pages.
- Indian sources often use **data centre** (British spelling) more than **data center**. Always search both. Also search **datacentre**, **DC park**, **hyperscale**, **colocation**, **AI data centre**, **cloud region**, **server farm**, **digital infrastructure**, **IT load**, **MW**, **MVA**, **substation**, **green data centre**.
- Hindi is useful for local press and district-level project news in North/Central India, but business/trade coverage is mostly English. Search Devanagari variants as leads, then verify with English/official records.

---

## 1. High-signal trade press and industry media

### 1.1 Daily/weekly discovery feeds

| Source | URL / query route | Use | Grade |
|---|---|---|---|
| DCD / Data Center Dynamics India search | `https://www.datacenterdynamics.com/en/news/?term=india` | Best India-specific global DC trade feed. Strong on land leases, construction starts, hyperscaler regions, power/cooling vendors, fires/outages, JV announcements. | B+ |
| ET Telecom data center tag | `https://telecom.economictimes.indiatimes.com/tag/data+center` and `data+centre` | Good on telcos, Nxtra, CtrlS, policy, IndiaAI GPU tenders, operator interviews. | B |
| Economic Times / ET Infra / ET DataCenters | `site:economictimes.indiatimes.com "data centre" "{state}"`, `https://datacenters.economictimes.indiatimes.com/` | Good business/property angle; useful for MoUs and policy changes. Watch paywall and syndicated text. | B |
| DataQuest India | `site:dqindia.com "data centre" India`, `site:dqindia.com "data center" India` | Operator landscape explainers and vendor lists; good for seed universe, not facility proof. | B-/C+ |
| Voice&Data | `site:voicendata.com "data centre" India`, `site:voicendata.com Nxtra Yotta CtrlS` | Telecom/DC operator profiles; helpful on capacity claims and edge strategy. | B- |
| W.Media India | `site:w.media India "data center"` | APAC trade publication; frequent vendor announcements and conference ecosystem. | B |
| Dgtl Infra | `site:dgtlinfra.com India "data center"` | Deal/investment summaries; good for financing and MW pipeline context. | B |
| Data Centre Magazine / Capacity Media / TelecomTalk / CRN India | site-scoped search | Secondary discovery feeds; verify any facility details. | C+/B- |

### 1.2 How to use trade press

Use trade press to discover names, then verify against a primary trail:

```
site:datacenterdynamics.com India "data center" "{operator}"
site:datacenterdynamics.com India "{city}" "MW"
site:telecom.economictimes.indiatimes.com "{operator}" "data center"
site:dqindia.com "data centre" "{operator}"
site:voicendata.com "{operator}" "data centre"
site:w.media "{city}" "data center" India
```

Trade press is usually reliable for **event existence** (opened, launched, land acquired, MoU signed) but not enough for final capacity accounting. The common failure mode is quoting **full-campus buildout** as current capacity. Capture exact verbs: `announced`, `signed MoU`, `acquired land`, `commenced construction`, `launched/opened`, `operational`, `full build-out`.

---

## 2. Industry associations, policy bodies, and market research

| Body / source | URL | Use | Grade |
|---|---|---|---|
| NASSCOM Community / NASSCOM reports | `https://community.nasscom.in/` search `data centre policy`, `India datacenter hub`; NASSCOM policy PDF: `community.nasscom.in/sites/default/files/report/25264-nasscom-recommendations-data-centre-policy.pdf` | Policy recommendations, industry leader POV, state policy summaries. Good for discovering operator names and policy issues. | B |
| MeitY Draft Data Centre Policy 2020 via NITI for States | `https://nitiforstates.gov.in/policy-viewer?id=PNC510C000384` and PDF `https://www.nitiforstates.gov.in/public-assets/Policy/policy_files/PNC510C000384.pdf` | National policy baseline: clearances, infrastructure status, data centre economic zones, cloud service procurement. Draft, not a live registry. | A- for policy text |
| Invest India / India Investment Grid / state investment portals | `https://www.investindia.gov.in/`, state portals below | Sector pages and policy incentives; sometimes names anchor investors and parks. | A-/B |
| DCAI / Data Center Association of India | `https://www.resiindia.org/dcassociationindia` | Association and event ecosystem; useful for members/speakers/working groups, not a facility list. | B-/C+ |
| ASSOCHAM Data Centre council | `https://www.assocham.org/overview-sector.php?name=data-centre` | Industry council and conference participants; identify active developers and policy asks. | B-/C+ |
| ICRIER Policy Bank | `https://icrier.org/policy_bank/data-centre/` | Curated policy references and commentary. | B |
| Cushman & Wakefield / JLL / CBRE / Colliers / Anarock / CareEdge / CRISIL | site-scoped queries | Market capacity by city, policy comparison, absorption, supply pipeline. Treat as aggregate context; facility names only when stated. | B |

Search templates:

```
site:community.nasscom.in "data centre" India
site:community.nasscom.in "data center policy" "{state}"
site:investindia.gov.in "data centre" "{state}"
site:icrier.org "data centre" India policy
"Data Center Association of India" datacenter
"data centre policy" India "{state}" filetype:pdf
"data centre" "single window" "{state}" India
```

---

## 3. Vendor/operator official pages and primary channels

Official operator pages are **A for claimed presence and current marketed locations**, but **B for capacity** unless backed by an audited filing, bond document, investor presentation, or statutory record.

| Operator / developer | Primary URL(s) | India location signals | Grade notes |
|---|---|---|---|
| STT GDC India | `https://www.sttelemediagdc.com/in-en`, locations `https://www.sttelemediagdc.com/in-en/locations` | 30+ facilities / 10 cities language appears in press pages; cities include Mumbai, Noida, Pune, Chennai, Hyderabad, Bengaluru, Kolkata, Jaipur, Ahmedabad, Delhi/Gurugram. | A for portfolio presence; B for MW unless facility page/press release gives exact IT load. |
| CtrlS | `https://www.ctrls.in/`, services `https://www.ctrls.in/data-center-services.php` | Mumbai, Chennai, Hyderabad, Noida, Bangalore, Kolkata; edge DCs Lucknow, Patna, Ahmedabad, Bhubaneswar, Bhopal. | A for city list; B for "Rated-4" and MW claims until certified/filing confirmed. |
| Nxtra by Airtel | `https://www.nxtra.in/` | Hyperscale locations published by cluster: Mumbai (Chandivali, Airoli, Mahape), Pune (Kharadi, Hinjewadi), Kolkata, Bhubaneswar, Bengaluru (Whitefield, Hoskote), plus Noida/Chennai/Hyderabad pages. 120+ edge DCs often cited. | A for own site; Bharti Airtel annual report is better for capacity and capex. |
| Sify / Sify Infinit Spaces | `https://www.sifytechnologies.com/data-center/`, `https://sifyinfinitspaces.com/` | Hyperscale campuses: Noida, Mumbai Rabale, Chennai; footprint pages list Mumbai Rabale/Airoli/Vashi, Bengaluru, Hyderabad FAB City, Chennai Siruseri/Tidel, Noida, Kolkata. | A for locations; NASDAQ/SEC filings are A for financial/capacity detail if available. |
| NTT Global Data Centers India / Netmagic | `https://services.global.ntt/en-us/services-and-products/global-data-centers` plus India facility pages | Large footprint in Mumbai, Bengaluru, Delhi NCR/Noida, Chennai; DCD/trade reports for new Mumbai/Noida phases. | A for NTT official pages; B for market articles. |
| Yotta Data Services | `https://yotta.com/`, colo page `https://colocation.yotta.com/data-center/` | Operational: NM1 Navi Mumbai, D1 Greater Noida, G1 GIFT City; planned/announced: Chennai, Delhi/NCR expansion, Bengal/Kolkata, Gujarat, Pune/Powai. | A for Yotta pages; B/C for future city pipeline. |
| AdaniConneX | `https://www.adaniconnex.com/`, data centers `https://www.adaniconnex.com/data-centers` | Chennai, Hyderabad, Navi Mumbai, Noida, Pune on current official site; earlier JV release also listed Vizag. | A for official current list; treat 1GW/5GW national platform as long-term plan unless phase-specific. |
| Digital Connexion (Digital Realty/Brookfield/Jio) | `https://digitalconnexion.com/`, `https://digitalconnexion.com/india/maa10` | Chennai MAA10 operational; Mumbai BOM10/Chandivali planned/under construction reported. | A for own facility pages; B for JV/interview pipeline. |
| Equinix India | Mumbai page `https://www.equinix.com/data-centers/asia-pacific-colocation/india-colocation/mumbai-data-centers`; MB1/MB2/MB3/MB4 pages; Chennai CN1 press page | Mumbai Chandivali campus (MB1/MB2/MB3) and Navi Mumbai MB4; Chennai CN1. | A for IBX pages and specs. |
| Web Werks / Iron Mountain Data Centers | `https://www.ironmountain.com/data-centers` and Web Werks pages | Mumbai, Pune, Noida/Delhi NCR, Bengaluru; verify exact current branding after Iron Mountain JV/acquisition. | A for current official page; C for old Web Werks-only lists. |
| CapitaLand India Trust / Ascendas | `https://www.capitaland.com/` and investor releases | Navi Mumbai, Chennai, Hyderabad, Bengaluru development pipeline; REIT filings can be high-grade. | A for SGX/CapitaLand disclosures; B for press. |
| Princeton Digital Group (PDG) | `https://www.princetondg.com/` | Mumbai/Navi Mumbai and Chennai projects reported; official pages and LinkedIn announcements needed. | A if official; B via DCD. |
| Pi DATACENTERS / ESDS / NxtGen / E2E / NeevCloud / RackBank / NetForChoice | own sites + IndiaAI procurement news | Smaller regional/AI/edge facilities; strong leads for non-metro enumeration. | A for own location pages, but capacity often marketing. |
| Jio / Reliance / Digital Connexion | Reliance annual reports, Digital Connexion | Jio cloud/AI and DC JV activity; local land allotments in WB/Chennai/Mumbai need separate proof. | A for filings, B for interviews. |

Vendor query templates:

```
site:{vendor-domain} India "data center" "{city}"
site:{vendor-domain} India "data centre" "{city}"
"{operator}" "{city}" ("MW" OR "IT load" OR "MVA" OR "racks" OR "sq ft")
"{operator}" "{city}" ("launched" OR "opened" OR "commenced construction" OR "foundation stone" OR "land")
"{operator legal name}" "data centre" "MCA"
"{operator}" "annual report" "data center" India
```

---

## 4. Hyperscaler official region pages

These prove operational cloud-region presence at city/region granularity, not facility address. Use them as **A for region existence** and pivot to vendor/land/permit records for physical sites.

| Provider | Official URL | India regions / locations to map |
|---|---|---|
| AWS | India page `https://aws.amazon.com/local/india/`; region docs `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html` | `ap-south-1` Asia Pacific (Mumbai), 3 AZs; `ap-south-2` Asia Pacific (Hyderabad), 3 AZs. |
| Microsoft Azure | Region list `https://learn.microsoft.com/en-us/azure/reliability/regions-list`; 2026 Hyderabad launch `https://news.microsoft.com/source/asia/features/microsofts-newest-india-datacenter-region-goes-live-to-power-the-countrys-ai-economy-and-enable-frontier-firms/` | Central India (Pune), South India (Chennai), West India (Mumbai), India South Central (Hyderabad). Also Jio India West / Jio India Central are partner regions. |
| Google Cloud | Locations `https://cloud.google.com/about/locations`; compute regions `https://docs.cloud.google.com/compute/docs/regions-zones`; Google DC communities `https://datacenters.google/locations` | `asia-south1` Mumbai, `asia-south2` Delhi/NCR; Andhra Pradesh, India appears as in-development Google data center location. |
| Oracle Cloud | `https://www.oracle.com/cloud/public-cloud-regions/` | India West (Mumbai), India South (Hyderabad). |
| IBM Cloud / SAP / Zoom / Salesforce / Akamai / Cloudflare | official region/location pages + DCD/ET articles | Often colocated in Equinix/STT/NTT/Sify; use as operational demand signals, not facility owners. |

Pivot query:

```
"AWS" Hyderabad "data center" Telangana land
"Microsoft" "Hyderabad" "data center" "Bharat Future City"
"Google" "Andhra Pradesh" "data center" "Visakhapatnam"
"Oracle Cloud" Mumbai Hyderabad "data center" India
"{cloud provider}" "{city}" "STT" OR "NTT" OR "Sify" OR "Equinix"
```

---

## 5. English and Hindi query patterns

### 5.1 English discovery templates

Use both spellings and status verbs:

```
"{state}" "{district}" ("data centre" OR "data center") ("MW" OR "MVA" OR "IT load" OR "racks")
"{city}" ("hyperscale data centre" OR "data center park" OR "colocation") India
"{city}" ("data centre" OR "data center") ("foundation stone" OR "groundbreaking" OR "commenced construction")
"{city}" ("data centre" OR "data center") ("launched" OR "inaugurated" OR "operational" OR "goes live")
"{city}" ("data centre" OR "data center") ("land" OR "leased" OR "allotted" OR "industrial plot")
"{city}" ("data centre" OR "data center") ("substation" OR "220 kV" OR "400 kV" OR "power evacuation")
"{operator}" "{district}" ("data centre" OR "data center") ("MW" OR "IT load")
"{state industrial agency}" "data centre" "{operator}"
```

Permit/official trail:

```
site:environmentclearance.nic.in "data centre" "{state}"
site:parivesh.nic.in "data centre" "{state}"
site:{state-spcb-domain} "data centre" "Consent to Establish"
site:{state-spcb-domain} "data center" "CTE"
site:{state-fire-domain} "data centre" NOC
site:{state-investment-domain} "data centre" "{operator}"
site:{state-industrial-development-domain} "data centre" "land allotment"
site:mca.gov.in "{operator legal name}" "data"
site:ibbi.gov.in "{operator}" "data centre"      # distress/asset sales
```

Trade-press scoped:

```
site:datacenterdynamics.com/en/news India "{city}" "data center"
site:telecom.economictimes.indiatimes.com "{city}" "data center"
site:dqindia.com "{operator}" "data centre"
site:voicendata.com "{city}" "data centre"
site:w.media "{operator}" "{city}" "data center"
```

### 5.2 Hindi / Devanagari templates

Hindi coverage is strongest for Uttar Pradesh, Delhi NCR, Rajasthan, Madhya Pradesh, Bihar, Jharkhand, Chhattisgarh, Haryana, Uttarakhand, Himachal Pradesh, and local Maharashtra/Gujarat press that republishes Hindi wire copy. Use Hindi for discovery, not final proof.

Core nouns:

- data centre: `डेटा सेंटर`, `डाटा सेंटर`, `डेटा केंद्र`, `डाटा केंद्र`
- data center park: `डेटा सेंटर पार्क`, `डाटा सेंटर पार्क`
- AI data center: `एआई डेटा सेंटर`, `कृत्रिम बुद्धिमत्ता डेटा सेंटर`
- cloud / server: `क्लाउड`, `सर्वर फार्म`, `सर्वर केंद्र`
- land/allotment: `भूमि आवंटन`, `जमीन आवंटित`, `औद्योगिक भूखंड`
- construction/opening: `शिलान्यास`, `भूमिपूजन`, `निर्माण शुरू`, `उद्घाटन`, `लोकार्पण`, `चालू`, `संचालित`
- investment/capacity: `निवेश`, `करोड़`, `मेगावाट`, `एमडब्ल्यू`, `रैक`, `क्षमता`

Templates:

```
"{जिला}" "डेटा सेंटर" ("शिलान्यास" OR "निर्माण शुरू" OR "उद्घाटन")
"{शहर}" "डाटा सेंटर" ("मेगावाट" OR "करोड़" OR "रैक" OR "क्षमता")
"{राज्य}" "डेटा सेंटर नीति" ("निवेश" OR "सब्सिडी" OR "छूट")
"{जिला}" "डेटा सेंटर पार्क" "भूमि आवंटन"
"{operator}" "डेटा सेंटर" "{शहर}"
site:amarujala.com "{जिला}" "डेटा सेंटर"
site:jagran.com "{जिला}" "डेटा सेंटर"
site:bhaskar.com "{शहर}" "डाटा सेंटर"
site:livehindustan.com "{जिला}" "डेटा सेंटर"
```

Hindi stage mapping:

- `MoU / समझौता / करार` = intent only, **C unless followed by land/permit/construction**.
- `भूमि आवंटन / भूखंड आवंटित` = land signal, **B/A- if from authority**.
- `शिलान्यास / भूमिपूजन / foundation stone` = construction-start ceremony, **B unless authority/operator confirms**.
- `उद्घाटन / लोकार्पण / चालू / operational` = operational claim, verify with operator page or customer/cloud region.

---

## 6. State and district enumeration matrix

Use this workflow for every state/UT:

1. Search state investment portal and industrial agency for `data centre`, `data center`, Hindi variants where applicable.
2. Search major DC districts/cities below with operator names and status verbs.
3. Search SEIAA/SPCB/OCMMS/Parivesh for CTE/CTO/environment records. Data centres may not require standalone EC, but large building/construction projects, DG sets, cooling plants, and industrial-park approvals leave records.
4. Search DISCOM/transmission tenders for `data centre`, `MVA`, `substation`, `HT connection`, `EHV`.
5. Search local authority minutes/land allotment pages: MIDC/MMRDA/CIDCO, SIPCOT/ELCOT/Guidance TN, TSIIC/TG-iPASS, NOIDA/GNIDA/YEIDA/Invest UP, HIDCO/Webel, IDCO/Invest Odisha, GIDC/iNDEXTb/GIFT, KIADB/Karnataka Udyog Mitra, APIIC/APEDB, RIICO/BIP Rajasthan.

### 6.1 Priority commercial states

| State / UT | Hot districts / localities | Operator/developer seeds | Official portals / agency query targets | Grade notes |
|---|---|---|---|---|
| Maharashtra | Mumbai, Navi Mumbai, Thane, Airoli, Rabale, Mahape, Chandivali, Powai, Palava, Pune, Hinjewadi, Kharadi, Nagpur | Equinix, STT, NTT, Sify, CtrlS, Nxtra, Yotta, Web Werks/Iron Mountain, CapitaLand, Digital Connexion, PDG, AdaniConneX, Lodha/Palava | `midcindia.org`, `cidco.maharashtra.gov.in`, `mmrda.maharashtra.gov.in`, Maharashtra single window/MAITRI, MPCB, SEIAA Maharashtra, MSEDCL/MSETCL tenders | Highest-density market. Official land/power records and operator pages are better than press. Watch "green integrated data centre park" MoUs; count only phase-specific builds. |
| Tamil Nadu | Chennai, Ambattur, Siruseri, Taramani, Oragadam, Sriperumbudur, Chengalpattu, Thiruvallur, Coimbatore | STT, NTT, Sify, CtrlS, Equinix CN1, Digital Connexion MAA10, AdaniConneX, Nxtra, Yotta planned, CapitaLand | Guidance TN `investingintamilnadu.com/sectors/data-centre`, SIPCOT, ELCOT, TIDCO, TANGEDCO/TANTRANSCO, TNPCB, SEIAA TN | Subsea cable and policy hub. District terms matter: Ambattur (Chennai), Siruseri (Chengalpattu/Kanchipuram legacy), Oragadam/Sriperumbudur. |
| Telangana | Hyderabad, Rangareddy, Shamshabad, Elkatta, FAB City, Bharat Future City, Maheshwaram | CtrlS, Sify, STT, Nxtra, AdaniConneX, AWS Hyderabad, Microsoft Hyderabad, Oracle Hyderabad, CapitaLand | Invest Telangana `invest.telangana.gov.in/data-centres/`, TG-iPASS, TSIIC, TSSPDCL/TSTRANSCO, TSPCB | Cloud-region evidence is strong. Query old/new state naming: Telangana, TG, Hyderabad, Rangareddy. |
| Uttar Pradesh | Noida, Greater Noida, Yamuna Expressway, Dadri, Jewar, Lucknow | Yotta D1/Dx, NTT, Sify, STT, Nxtra, CtrlS, AdaniConneX, Web Werks/Iron Mountain, Google Noida/Delhi region leads | Invest UP `invest.up.gov.in/up-data-centre-policy-2021/`, UPLC `uplc.up.gov.in/en/page/uttar-pradesh-data-center-policy`, NOIDA Authority, GNIDA, YEIDA, UPPCB, UPPCL/UPPTCL | UP policy page reports proposed investment/capacity; use as pipeline, not facility list. Land allotments by authorities are high-grade. |
| Karnataka | Bengaluru, Whitefield, Electronic City, KIADB Aerospace Park, Hoskote, Devanahalli, Mysuru | Nxtra, Sify, STT, NTT, CtrlS, CapitaLand, Web Werks/Iron Mountain, ESDS, NxtGen | KIADB, Karnataka Udyog Mitra, KSPCB, BESCOM/KPTCL, Karnataka Digital Economy Mission | Policy was reported as finalizing in 2026; before final notification use investment/industrial agency and vendor records. |
| West Bengal | Kolkata, New Town/Rajarhat, Salt Lake/Sector V, Hindmotor/Uttarpara, Hooghly, Kalyani | STT Kolkata, Sify, Nxtra, NTT reported, Adani land, Yotta/Hiranandani Bengal plan, Jio/Reliance land leads | Webel, HIDCO, WBIDC, Invest Bengal/BGWS, WBPCB, WBSEDCL/WBSETCL | High MoU/land-allotment noise. Need HIDCO/WBIDC/land plus operator confirmation. |
| Odisha | Bhubaneswar, Infovalley, Khordha, Cuttack, Gopalpur | CtrlS edge, Nxtra Bhubaneswar, HCLTech/Sarvam AI DC leads, state DC policy investors | Invest Odisha `investodisha.gov.in/datacentre-policy`, IDCO, OCAC, Odisha single window GO SWIFT, OSPCB, OPTCL/TPCODL | Policy exists; many leads tied to AI/IT parks. Verify with IDCO allotment or tender. |
| Gujarat | GIFT City/Gandhinagar, Ahmedabad, Dholera, Sanand, Vadodara, Surat | Yotta G1 GIFT City, CtrlS Ahmedabad edge, AdaniConneX/Gujarat links, NeevCloud/RackBank leads | GIFT City, GIDC, iNDEXTb/Invest Gujarat, Gujarat single window, GPCB, GETCO/UGVCL/DGVCL | 2026 Gujarat policy reported with very large GW target; use official notification when available. Treat target numbers as policy ambition. |
| Andhra Pradesh | Visakhapatnam, Madhurawada, Kapuluppada, Vijayawada, Amaravati, Tirupati | Google AP in-development, AdaniConneX Vizag legacy, Colt/RMZ Vizag reports, Pi DATACENTERS, state/IT park leads | APIIC, APEDB, AP single desk, APPCB, APTRANSCO, Visakhapatnam urban authority | Vizag has many hyperscale headlines. Environmental clearance currently nuanced: standalone AI DC may not need EC, but project components still leave permits. |

### 6.2 Secondary / edge states and UTs

| State / UT | Query localities | Likely leads | Query notes |
|---|---|---|---|
| Delhi / NCR | Delhi, Gurugram, Manesar, Faridabad, Bahadurgarh | STT Delhi/Gurugram, Nxtra Manesar, legacy enterprise DCs | Delhi itself has land/power constraints; many "Delhi" results are Noida/Gurugram. Query `Delhi NCR`, `Gurugram`, `Manesar`, `Noida` separately. |
| Haryana | Gurugram, Manesar, Panchkula, Sonipat | STT/Nxtra/enterprise DCs, edge sites | HSIIDC, Invest Haryana, HSPCB, DHBVN/HVPNL. Hindi searches useful. |
| Rajasthan | Jaipur, Bhiwadi, Neemrana, Jodhpur | STT Jaipur 1, RIICO data park leads | RIICO, BIP Rajasthan, RSPCB, Jaipur DISCOM/RVPN. Search Hindi `जयपुर डेटा सेंटर उद्घाटन`. |
| Madhya Pradesh | Indore, Bhopal, Pithampur | CtrlS Bhopal edge, RackBank/Indore, state IT park leads | MPIDC, Invest MP, MPPCB, MPPTCL. Hindi searches strong. |
| Bihar | Patna | CtrlS Patna edge, state e-gov DC | Bihar Industries, BIP, BSPCB, NBPDCL/SBPDCL. Hindi search is essential. |
| Jharkhand | Ranchi, Jamshedpur | state DC/edge, enterprise/telco | JIADA, JSPCB, JBVNL. Mostly small/edge unless new policy appears. |
| Chhattisgarh | Raipur, Naya Raipur | state DC, enterprise/telco | CSIDC, CHiPS, CECB, CSPTCL. Query `Naya Raipur data centre`. |
| Punjab / Chandigarh | Mohali, Chandigarh, Ludhiana | enterprise/edge, telecom DCs | Invest Punjab, PSIEC, PPCB, PSPCL; also query Hindi/Punjabi transliterations. |
| Kerala | Kochi, Thiruvananthapuram, Infopark, Technopark | Sify/enterprise, subsea/edge, state DC | KSIDC, KINFRA, Kerala Startup Mission/Technopark, KSPCB, KSEB. |
| Goa | Verna, Panaji | DR/edge only | Goa-IDC, GSPCB. Low priority. |
| Assam / Northeast | Guwahati, Assam Electronics City | state DC, edge/telco | AIDC, AMTRON, ASPCB, AEGCL. Use `data centre` and Hindi/Assamese only as broad leads. |
| Uttarakhand | Dehradun, Pantnagar | DR/edge, government DC | SIIDCUL, UKPCB, UPCL/PTCUL. Hindi searches strong. |
| Himachal Pradesh | Shimla, Baddi | DR/edge | HP Industries, HPSPCB, HPSEBL. Low priority. |
| Jammu & Kashmir / Ladakh | Jammu, Srinagar | government/edge | JK Industries, JKPCB, power development department. Mostly state DC/edge. |
| Puducherry / Andaman / Lakshadweep / Dadra & Nagar Haveli and Daman & Diu | UT capitals/industrial estates | government/edge only | Query for `state data centre`, `NIC`, `disaster recovery`; hyperscale unlikely. |

District-level template:

```
"{district}" "{state}" ("data centre" OR "data center" OR "डेटा सेंटर")
"{district}" "{industrial estate/IT park}" "data centre"
"{district}" "{operator}" "MW"
"{district}" "Consent to Establish" "data centre"
"{district}" "fire NOC" "data centre"
"{district}" "substation" "data centre"
```

---

## 7. Official and semi-official records to pair with industry leads

These are not the main angle, but they are needed to upgrade trade/vendor leads.

| Channel | URL / route | What it proves | Grade |
|---|---|---|---|
| MCA company records | `https://www.mca.gov.in/` company/LLP master data | Legal existence of SPV, registered office, directors; not facility existence. | A for entity |
| SEIAA / Parivesh / MoEFCC | `https://parivesh.nic.in/`, `https://environmentclearance.nic.in/` | EC proposals for large building/construction/industrial parks. AI/DC standalone EC may not always be required; absence is not absence of project. | A when present |
| State Pollution Control Boards / OCMMS | state SPCB sites, search `Consent to Establish data centre` | CTE/CTO for DG sets, HVAC, construction, water/air consents. | A |
| Industrial development authorities | MIDC, CIDCO, SIPCOT, TSIIC, NOIDA/GNIDA/YEIDA, HIDCO, IDCO, GIDC, KIADB, APIIC, RIICO | Land allotment, tender, plot auction, park master plan. | A |
| DISCOM / transmission tenders | MSETCL/MSEDCL, TANGEDCO/TANTRANSCO, TSTRANSCO, UPPTCL, GETCO, APTRANSCO, etc. | Large power connection/substation often reveals real MW/MVA before launch. | A/B |
| State single-window portals | MAITRI, Guidance TN, TG-iPASS, Nivesh Mitra UP, GO SWIFT Odisha, Invest Gujarat, Karnataka Udyog Mitra, AP Single Desk | Project approvals and incentive applications when public. | A/B |
| Stock exchange / investor filings | NSE/BSE, SEC for Sify, SGX/CapitaLand, Bharti Airtel annual report, listed real estate developers | Audited capex, MW under construction, land banking. | A |
| Tender portals | GeM, CPPP, state e-procurement, utility tenders | EPC, cooling, electrical, DG, substation awards. | A/B |

Search examples:

```
site:parivesh.nic.in "data centre" "Maharashtra"
site:environmentclearance.nic.in "data center" "Tamil Nadu"
site:mpcb.gov.in "data centre" "Consent to Establish"
site:tnpcb.gov.in "data centre"
site:uppcb.com "data center" Noida
site:gem.gov.in "data centre" "MW"
site:eprocure.gov.in "data centre" "substation"
site:bseindia.com "{operator}" "data centre"
site:airtel.in "annual report" "Nxtra" "data center"
```

---

## 8. Reliability grading rules for India

### 8.1 Source grades

| Grade | India examples |
|---|---|
| **A** | Operator official facility page; cloud provider official region/AZ page; MCA master data for entity; SEIAA/Parivesh EC record; SPCB CTE/CTO; industrial authority land allotment; DISCOM/transmission tender/connection; audited annual report/investor filing; stock exchange release. |
| **B** | DCD, ET Telecom, ET DataCenters/ET Infra, DataQuest, Voice&Data, W.Media, Dgtl Infra, NASSCOM/ASSOCHAM/DCAI policy/event material, major real-estate consultant reports when they name cities/MW. |
| **C** | Local newspaper MoU articles, LinkedIn posts, aggregator maps (Baxtel/DataCenterMap/DataCenters.com), conference brochures, broker posts, generic "top 10" articles, social media. |

Aggregator note: Baxtel/DataCenterMap/DataCenters.com are useful for address discovery and alternate names. They are **C leads** unless the same fact is verified on an operator page, authority record, or filing.

### 8.2 Evidence-grade by fact

- **Existence of operator in city**: operator official page = A; trade article = B; aggregator = C.
- **Exact address / campus boundary**: industrial authority/SPCB/EC/operator facility PDF = A; Equinix/retail colocation page = A; aggregator = C.
- **Capacity MW / IT load**: audited filing or operator facility spec = A; DCD/ET quoting operator = B; consultant aggregate = B; local MoU = C.
- **Status**: `operational/opened/launched` by operator/cloud = A; DCD/ET opening report = B; local ceremony = B/C; MoU = C.
- **Pipeline full buildout**: always store as `planned_full_buildout_mw`, not current MW.
- **AI/GPU capacity**: IndiaAI tender/official empanelment = A for GPU procurement; operator PR = B; social claims = C.

### 8.3 Common India pitfalls

- **"Data centre policy target" is not project capacity.** Maharashtra/Gujarat/UP targets can be tens of GW or hundreds of MW; do not count them as pipeline without named investor/site.
- **"Delhi" may mean Noida or Gurugram.** Normalize to state/district: Noida/Greater Noida = Uttar Pradesh; Gurugram/Manesar = Haryana; Delhi = NCT Delhi.
- **"Mumbai" may mean Navi Mumbai/Thane/Rabale/Airoli/Palava/Powai/Chandivali.** Normalize to district and locality.
- **MoUs are weak.** Count only after land allotment, CTE/EC, construction, operator page, or power connection evidence.
- **IT load vs facility power vs MVA.** Store unit verbatim. `400 MW campus` may be eventual utility capacity; `critical IT load` is closer to usable capacity.
- **Old brands persist.** Netmagic = NTT; GPX Mumbai = Equinix MB1/MB2; Web Werks assets may be Iron Mountain-branded; BAM Digital Realty = Digital Connexion.
- **State Data Centre (SDC) is often government e-governance infrastructure**, not commercial colo. Include only if the enumeration target includes public sector DCs; otherwise mark category `government_sdc`.

---

## 9. Recommended pipeline for India

1. **Seed operators:** scrape/manual-capture official location pages for STT, CtrlS, Nxtra, Sify, NTT, Yotta, AdaniConneX, Digital Connexion, Equinix, Web Werks/Iron Mountain, CapitaLand, PDG, Pi, ESDS, NxtGen, E2E, NeevCloud.
2. **Seed cloud regions:** AWS Mumbai/Hyderabad; Azure Pune/Chennai/Mumbai/Hyderabad plus Jio partner regions; Google Mumbai/Delhi and Andhra Pradesh in-development; Oracle Mumbai/Hyderabad.
3. **Trade press sweep:** DCD India, ET Telecom/DataCenters, DataQuest, Voice&Data, W.Media, Dgtl Infra with `{operator} + {city} + MW/status` queries.
4. **State portal sweep:** run the state matrix in section 6, prioritizing Maharashtra, Tamil Nadu, Telangana, Uttar Pradesh, Karnataka, West Bengal, Odisha, Gujarat, Andhra Pradesh.
5. **Permit/power validation:** for every discovered project, search SPCB/Parivesh/SEIAA plus transmission/DISCOM tenders and land allotments.
6. **Entity resolution:** map brand → legal SPV through MCA and filings; dedupe by locality + operator parent + campus/phase.
7. **Status resolution:** record lifecycle as `MoU`, `land_allotted`, `permitted`, `under_construction`, `launched`, `operational`, `expanded`; never collapse planned and live capacity.
8. **Standing monitoring:** weekly DCD/ET/W.Media, monthly operator pages, quarterly state single-window/policy pages, and annual filings/ESG reports.

Quick-start query set for a new analyst:

```
site:datacenterdynamics.com/en/news India "data center" "Mumbai" "MW"
site:telecom.economictimes.indiatimes.com "data center" "Noida"
site:sttelemediagdc.com/in-en "data centre" "India" "MW"
site:ctrls.in "data center" "Kolkata"
site:nxtra.in "Hyperscale Locations"
site:sifytechnologies.com "data center footprint"
site:adaniconnex.com "Data Centres" India
site:equinix.com "India colocation" "MB"
"Greater Noida" "data centre" "land allotment"
"डेटा सेंटर" "शिलान्यास" "नोएडा"
site:parivesh.nic.in "data centre" "Maharashtra"
site:midcindia.org "data centre" "MW"
```

