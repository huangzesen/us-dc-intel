#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, sys

OUT = "/Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/world/results-method/batch-100.jsonl"

R = []
def rec(division, name, status, cap, dev, urls, date, grade, notes):
    R.append({"country_code":"DE","country_name":"Germany","division":division,"name":name,"status":status,"capacity_mw":cap,"developer":dev,"source_urls":urls,"evidence_date":date,"evidence_grade":grade,"notes":notes})

def nop(division, notes):
    R.append({"country_code":"DE","country_name":"Germany","division":division,"no_projects":True,"notes":notes})

rec("Mecklenburg-Vorpommern - Schwerin", "DVZ M-V new data center", "construction", None,
    "DVZ Datenverarbeitungszentrum Mecklenburg-Vorpommern GmbH",
    ["https://www.dvz-mv.de/news/startschuss-fuer-neues-rechenzentrum", "https://www.dvz-mv.de/rechenzentrum-service"],
    "2026-01-06", "A",
    "DVZ announced start of site setup for a new data center in Schwerin in January 2026; existing DVZ service page lists Schwerin address. Completion planned for Q2 2027. State-owned IT service provider facility; capacity not public.")

rec("Mecklenburg-Vorpommern - Schwerin", "PLANET IC Schwerin 1", "operational", None,
    "PLANET IC GmbH",
    ["https://datacenterplatform.com/data-centers/planet-ic-gmbh/planet-ic-gmbh-germany/", "https://www.datacentermap.com/germany/schwerin/"],
    "2026-08-11", "C",
    "Aggregator listings identify one PLANET IC colocation facility at Mettenheimer Strasse 9-15, 19061 Schwerin. No public MW capacity found; directory-level source only.")

rec("Mecklenburg-Vorpommern - Vorpommern-Greifswald", "University of Greifswald Data Centre", "operational", None,
    "State of Mecklenburg-Vorpommern / University of Greifswald",
    ["https://foerdermittel.europa-mv.de/project/neubau-rechenzentrum-fuer-die-universitaet-greifswald/", "https://www.uni-greifswald.de/universitaet/information/aktuelles/detail/n/nachhaltiges-rechenzentrum-universitaetsrechenzentrum-greifswald-erhaelt-plakette-nachhaltiges-bauen-192463/", "https://rz.uni-greifswald.de/en/"],
    "2024-04-17", "A",
    "EU/MV project page says a new data center was built at Felix-Hausdorff-Strasse 12, Greifswald, with EUR 12.4m total investment; university release confirms the operational facility and a sustainability award. Institutional data center, capacity not disclosed.")

rec("Mecklenburg-Vorpommern - Vorpommern-Greifswald", "Landkreis Vorpommern-Greifswald technical data center", "operational", None,
    "Landkreis Vorpommern-Greifswald / E-TEC Power Management GmbH",
    ["https://de.e-tecpowerman.com/e-tec-ubergibt-das-technische-rechenzentrum-an-den-landkreis-vorpommern-greifswald/"],
    "2025-09-11", "B",
    "E-TEC reports handover of a secure, energy-efficient technical data center for the district with 12 racks and geothermal integration. District government facility, not commercial colocation.")

rec("Mecklenburg-Vorpommern - Vorpommern-Greifswald", "Pasewalk Berlin-Szczecin Industrial Park data center", "rejected", None,
    "Undisclosed investor / City of Pasewalk",
    ["https://www.ndr.de/nachrichten/mecklenburg-vorpommern/Pasewalk-Mega-Rechenzentrum-wird-nicht-gebaut%2Cdatencenter102.html", "https://www.datacenter-insider.de/800-millionen-euro-projekt-in-pasewalk-gescheitert-neue-chance-fuer-investoren-a-ff9854ef06b3445c36dcf6d910888ea4/"],
    "2025-01-23", "B",
    "NDR reported negotiations for a several-hundred-million-euro data center in Pasewalk had failed after more than three years; Datacenter Insider described the planned investment as about EUR 800m. Recorded as negative evidence (rejected/failed).")

rec("Mecklenburg-Vorpommern - Vorpommern-Rügen", "WIIT Stralsund data centers", "operational", None,
    "WIIT AG",
    ["https://www.wiit.cloud/de/services/cloud-services/colocation/data-center-stralsund/"],
    "2026-08-12", "A",
    "WIIT states it operates two data centers in Stralsund at Zur Schwedenschanze 2 with over 600 m2 of data-center space and 146 racks. Verified against current operator page.")

rec("Mecklenburg-Vorpommern - Vorpommern-Rügen", "Landkreis Vorpommern-Rügen Stralsund data center", "operational", None,
    "Landkreis Vorpommern-Rügen / Data Center Consulting GmbH",
    ["https://www.data-center-consulting.de/referenzen.htm"],
    "2026-08-11", "B",
    "Data Center Consulting reference says it planned and supported completion of a new RZ in Stralsund for Landkreis Vorpommern-Rügen. District facility; no capacity disclosed.")

nop("North Rhine-Westphalia - Aachen (Rural)",
    "Searches returned only Aachen city (kreisfreie Stadt) facilities (regio iT, RelAix, CANCOM) and Kreis-level municipal IT references; no verified data-center project in the rural Staedteregion Aachen area outside the city.")

rec("North Rhine-Westphalia - Aachen (Urban)", "regio iT EURaix Evolution (EVO) data center", "operational", None,
    "regio iT gesellschaft fuer informationstechnologie mbh / Data Center Group",
    ["https://www.regioit.de/nachrichten/spatenstich-fuer-das-neue-klimaneutrale-rechenzentrum-der-regio-it-in-aachen", "https://www.kommune21.de/k21-meldungen/energieeffizientes-rechenzentrum-3/", "https://www.datacenter-insider.de/regio-it-baut-nachhaltiges-rechenzentrum-in-aachen-a-44f1a979d70b9e6610560f03e22c0a68/", "https://www.aachener-zeitung.de/lokales/region-aachen/aachen/innovative-kuehlung-mit-fernwaerme-neues-rechenzentrum-am-schwarzen-weg-startet-durch/158205669.html"],
    "2026-08-12", "B",
    "regio iT broke ground on the climate-neutral 300-kW data center in August 2024; Kommune21 and DataCenter-Insider report it has since entered operation as EURaix Evolution (EVO) on the Schwarzen Weg site. Municipal IT provider facility.")

rec("North Rhine-Westphalia - Aachen (Urban)", "RelAix Networks hex/AC", "operational", None,
    "RelAix Networks GmbH",
    ["https://www.relaix.net/leistungen/datacenter", "https://www.relaix.net/news/hex-ac-das-neue-regionale-rechenzentrum-von-relaix"],
    "2026-08-11", "A",
    "RelAix lists server housing at Data Center hex/AC and gives the Aachen operator address Auf der Huels 172; company news says hex/AC is TUEV-certified. No public MW found.")

rec("North Rhine-Westphalia - Aachen (Urban)", "CANCOM Aachen", "operational", None,
    "CANCOM SE",
    ["https://www.datacentermap.com/germany/aachen/cancom-aachen/", "https://www.datacentermap.com/c/cancom/"],
    "2026-08-11", "C",
    "Data Center Map lists CANCOM Aachen at Im Suesterfeld 6, 52072 Aachen, with event history noting CANCOM acquired Synaix Group in July 2017. Directory-level source; capacity not disclosed.")

rec("North Rhine-Westphalia - Bielefeld", "Stadtwerke Bielefeld / BITel data center (Telehouse 2)", "operational", None,
    "Stadtwerke Bielefeld Gruppe / BITel Gesellschaft fuer Telekommunikation mbH",
    ["https://www.stadtwerke-bielefeld.de/geschaeftskunden/services/mobilitaet-telekommunikation/rechenzentrum/", "https://www.bitel.de/fileadmin/content/documents/zertifikate/Telehouse2_TUEV_Zertifikat_Stadtwerke_Bielefeld_2026.pdf", "https://www.bitel.de/geschaeftskunden/service/rechenzentrum.html"],
    "2026-08-12", "A",
    "Stadtwerke Bielefeld describes a TUEV-certified regional data center with DIN EN 50600 design, ISO 27001 ISMS, dual 10-kV feeds; 2026 TUEV certificate confirms Telehouse 2 at Schweriner Strasse 1-3, Bielefeld. University of Bielefeld servers moving there in 2025.")

rec("North Rhine-Westphalia - Bielefeld", "euNetworks Colocation Bielefeld", "operational", None,
    "euNetworks",
    ["https://www.datacentermap.com/germany/bielefeld/eunetworks-bielefeld/", "https://www.datacenters.com/eunetworks-bielefeld"],
    "2026-08-11", "C",
    "Listings identify euNetworks Colocation Bielefeld at Niederwall 2, 33602 Bielefeld; Datacenters.com reports 3,218 sq ft raised floor and ISO 27001. Directory-level source.")

rec("North Rhine-Westphalia - Bochum", "GFR DataCenter Bochum", "operational", None,
    "Glasfaser Ruhr GmbH & Co. KG",
    ["https://www.glasfaser-ruhr.de/rechenzentrum/", "https://www.datacentermap.com/germany/bochum/gfr-datacenter-bochum/", "https://www.peeringdb.com/fac/700"],
    "2026-08-12", "A",
    "Glasfaser Ruhr says it operates data centers directly in Bochum and Herne; Data Center Map lists GFR DataCenter Bochum at Obere Stahlindustrie 4, 44793 Bochum; PeeringDB lists the facility. No public MW found.")

rec("North Rhine-Westphalia - Bonn", "NTT Rhein-Ruhr 1 / CGN1", "operational", None,
    "NTT DATA, Inc. / NTT Global Data Centers",
    ["https://etalytics.com/de/resources/success-stories/ntt-saves-cooling-energy-with-etalytics-ai-optimization", "https://www.datacenter-insider.de/ntt-baut-und-baut-und-baut-seine-basis-in-deutschland-um-mehr-als-40-prozent-aus-a-1032289/", "https://www.datacentermap.com/germany/bonn/ntt-rhein-ruhr-1/"],
    "2026-08-12", "B",
    "etalytics case study confirms NTT Global Data Centers operates Rhein-Ruhr 1 in Bonn with AI-optimized cooling; Datacenter-Insider describes NTT's ongoing expansion at Bonn among other sites; listings place CGN1 at Friedrich-Woehler-Strasse 67, 53117 Bonn.")

rec("North Rhine-Westphalia - Bonn", "ITENOS Data Center Bonn", "operational", None,
    "ITENOS GmbH",
    ["https://itenos.de/en/data-center-provider/data-center-germany/data-center-bonn/"],
    "2026-08-11", "A",
    "ITENOS lists a Bonn data center with 375 m2 floor space, 160 kVA UPS expandable, 24/7 monitoring, and access controls.")

rec("North Rhine-Westphalia - Bonn", "tops.net Data Center", "operational", None,
    "tops.net GmbH",
    ["https://www.datacentermap.com/germany/bonn/topsnet-data-center/", "https://www.datacentermap.com/germany/bonn/"],
    "2026-08-11", "C",
    "Data Center Map lists tops.net Data Center at Holtorfer Strasse 35, 53229 Bonn, offering colocation and 19-inch server rack space. Directory-level source.")

nop("North Rhine-Westphalia - Borken",
    "Searches returned no local colocation/hyperscale facility or announced data-center project in Kreis Borken; only generic IT-service references.")

nop("North Rhine-Westphalia - Bottrop",
    "Searches returned no verified data-center project in Bottrop; only generic IT/colocation marketing pages for other cities.")

rec("North Rhine-Westphalia - Cleves ( Kleve )", "ECHO Datacenter GmbH Kevelaer colocation/data-center services", "operational", None,
    "ECHO Datacenter GmbH",
    ["https://echo-dc.eu/", "https://echo-dc.eu/colocation/", "https://www.kreis-kleve.de/online-dienste-am-wochenende-1314-juni-nicht-erreichbar-rechenzentrum-wartet-die-technik"],
    "2026-08-11", "B",
    "Official ECHO site lists a Kevelaer (Kreis Kleve) registered seat/contact and colocation/data-center services; public pages do not disclose a specific facility address or MW. Kreis Kleve IT operations run from its own data center (maintenance note), but no commercial project verified.")

rec("North Rhine-Westphalia - Coesfeld", "Weiling modular in-house data center", "operational", None,
    "Weiling GmbH",
    ["https://www.it-zoom.de/mittelstand/e/modulares-rechenzentrum-fuer-biogrosshaendler-weiling-9075/", "https://www.cio.de/article/3699797/biohaendler-weiling-spart-strom-mit-all-flash-data-center.html"],
    "2026-08-11", "B",
    "Trade press describes Weiling's modular data center/computer room at its Coesfeld headquarters and later all-flash storage modernization; enterprise/internal facility, not public colocation.")

rec("North Rhine-Westphalia - Cologne ( Köln )", "NetCologne Lövenich sustainable data center", "operational", 5,
    "NetCologne GmbH",
    ["https://netcologne-unternehmen.de/baustart-neues-rechenzentrum-von-netcologne/", "https://www.datacenterdynamics.com/en/news/german-telco-netcologne-breaks-ground-on-data-center/", "https://www.datacentermap.com/germany/cologne/netcologne-lovenich/"],
    "2026-08-12", "B",
    "NetCologne says it built the first sustainable data center for Cologne; construction in Cologne-Lövenich started November 2023 with six data-center rooms, opened September 2024; listings report 5 MW capacity.")

rec("North Rhine-Westphalia - Cologne ( Köln )", "nLighten Cologne CGN1 edge data center", "operational", 4.8,
    "nLighten",
    ["https://www.nlighten.com/en/edge-location/cologne/", "https://www.nlighten.com/en/edge-location/germany/"],
    "2026-08-11", "A",
    "Official nLighten page states 1,960 m2 dedicated colocation space and 4,800 kW power, near Cologne city center.")

rec("North Rhine-Westphalia - Cologne ( Köln )", "Penta Infra Cologne data center", "operational", None,
    "Penta Infra",
    ["https://penta-infra.com/data-centers/cologne/", "https://penta-infra.com/"],
    "2026-08-11", "A",
    "Official Penta Infra pages list Cologne as an operating carrier-neutral colocation site on the Amsterdam-Frankfurt fiber route; public page does not show MW capacity.")

rec("North Rhine-Westphalia - Dortmund", "DOKOM21 Dortmund data-center sites (Huckarde / Hörde)", "operational", None,
    "DOKOM21 (DOKOM Gesellschaft fuer Telekommunikation mbH)",
    ["https://www.dokom21.de/geschaeftskunden/rechenzentrum/infrastruktur-sicherheit/standorte-redundanz", "https://www.dokom21.de/geschaeftskunden/rechenzentrum/zertifizierung/entstehung-reliable-data-center", "https://www.dokom21.de/geschaeftskunden/rechenzentrum/"],
    "2026-08-12", "A",
    "Official DOKOM21 pages state it operates geographically separated Dortmund/Ruhr-area data centers with over 4,600 m2 of data-center area, including Hörde and newer Huckarde capacity (groundbreaking May 2017).")

rec("North Rhine-Westphalia - Dortmund", "EXA Dortmund data center", "operational", None,
    "EXA Infrastructure",
    ["https://www.datacentermap.com/germany/dortmund/interoute-dortmund/", "https://www.datacenters.com/exa-infrastructure-dortmund"],
    "2026-08-11", "C",
    "Data-center directories list EXA Dortmund at Stockholmer Allee 24 / 44269 Dortmund-Aplerbeck; capacity not publicly supplied.")

rec("North Rhine-Westphalia - Dortmund", "euNetworks Colocation Dortmund", "operational", None,
    "euNetworks",
    ["https://www.datacentermap.com/germany/dortmund/eunetworks-dortmund/", "https://www.datacenters.com/locations/germany/north-rhine-westphalia/dortmund"],
    "2026-08-11", "C",
    "Data-center directories list an euNetworks colocation facility at Im Spaehenfelde 51 in Dortmund; capacity not disclosed.")

rec("North Rhine-Westphalia - Dortmund", "Knipp Dortmund data center", "operational", None,
    "Knipp Medien und Kommunikation GmbH",
    ["https://www.knipp.de/company/career?set-language=en", "https://colomap.com/facilities/knipp-data-center/", "https://www.datacentermap.com/germany/dortmund/knipp-data-center/"],
    "2026-08-11", "B",
    "Knipp states it operates its own data center in Dortmund; directories place the facility at Martin-Schmeisser-Weg 9.")

rec("North Rhine-Westphalia - Duisburg", "DU-IT main data center", "operational", None,
    "DU-IT Gesellschaft fuer Informationstechnologie Duisburg mbH",
    ["https://datacenter-group.com/en/news-stories/article/du-it-gmbh/", "https://datacenter-group.com/de/news-stories/artikel/du-it-gmbh/"],
    "2026-08-11", "A",
    "Data Center Group case study says Stadtwerke Duisburg provided a hall that was gutted to plan and build DU-IT's new main data center, about 750 m2 including technical areas, TUEV Level 3 basis.")

rec("North Rhine-Westphalia - Duisburg", "Rhine Cloud hosted by DU-IT in Duisburg", "operational", None,
    "DU-IT / Huawei",
    ["https://www.datacenterdynamics.com/en/news/cebit-2018-huawei-du-it-launch-smart-city-cloud-service-in-duisburg-germany/", "https://www.golem.de/news/du-it-duisburg-und-huawei-starten-die-rhine-cloud-1806-134892.html"],
    "2018-06-12", "B",
    "2018 launch of Duisburg smart-city/public-services cloud; sources state Rhine Cloud IaaS/SaaS is hosted in Duisburg by DU-IT in a BSI/TUEV Level 3 data center.")

rec("North Rhine-Westphalia - Düren", "SOCO Data Center Düren-Birkesdorf", "operational", None,
    "SOCO Network Solutions GmbH",
    ["https://www.datacentermap.com/germany/cologne/soco-data-center/", "https://www.datacentermap.com/germany/cologne/soco-data-center/specs/", "https://www.eco.de/mitglieder/soco-network-solutions-gmbh/"],
    "2026-08-12", "C",
    "Directories list SOCO Data Center at Nordstrasse 102, 52353 Düren-Birkesdorf; eco member page confirms SOCO Network Solutions address in Düren. No MW capacity supplied.")

rec("North Rhine-Westphalia - Düren", "Jülich Supercomputing Centre JUPITER modular data center", "operational", None,
    "Forschungszentrum Jülich / EuroHPC JU",
    ["https://www.fz-juelich.de/en/jsc/jupiter", "https://www.ecmwf.int/en/about/media-centre/news/2025/reaching-jupiter-ecmwf-celebrates-first-european-exascale", "https://blogs.nvidia.com/blog/jupiter-exascale-supercomputer-live/"],
    "2025-09-05", "A",
    "Forschungszentrum Jülich hosts JUPITER; ECMWF and NVIDIA report the exascale system went into operation on 5 September 2025 at Jülich, with NVIDIA noting the modular data center housing it. Research/HPC facility, not colocation.")

rec("North Rhine-Westphalia - Düsseldorf", "Digital Realty Düsseldorf DUS1", "operational", None,
    "Digital Realty",
    ["https://www.digitalrealty.com/data-centers/emea/dusseldorf/dus1", "https://www.digitalrealty.com/data-centers/emea/dusseldorf"],
    "2026-08-11", "A",
    "Official Digital Realty page lists DUS1 at In der Steele 25-45 as a network-neutral Düsseldorf data center; page gives 35,000 ft2 / 3,284 m2 building size but no MW in accessible text.")

rec("North Rhine-Westphalia - Düsseldorf", "Digital Realty Düsseldorf DUS2", "operational", None,
    "Digital Realty",
    ["https://www.digitalrealty.com/data-centers/emea/dusseldorf/dus2", "https://www.digitalrealty.com/data-centers/emea/dusseldorf"],
    "2026-08-11", "A",
    "Official Digital Realty page lists DUS2 at In der Steele 39-45; page gives 26,000 ft2 / 2,404 m2 building size but no MW in accessible text.")

rec("North Rhine-Westphalia - Düsseldorf", "Digital Realty Düsseldorf DUS3", "operational", 6.6,
    "Digital Realty",
    ["https://www.digitalrealty.com/data-centers/emea/dusseldorf/dus3", "https://www.datacentermap.com/germany/duesseldorf/digital-realty-dusseldorf-dus3/"],
    "2026-08-11", "B",
    "Official Digital Realty page confirms DUS3; DataCenterMap reports 6.6 MW at In der Steele 27-43.")

rec("North Rhine-Westphalia - Düsseldorf", "NorthC Düsseldorf data center (ex-Colt asset)", "operational", None,
    "NorthC Datacenters",
    ["https://www.northcdatacenters.com/de/northc-datacenters/duesseldorf/", "https://www.artfiles.de/en/colocation/rechenzentrum-technik/lumen-rechenzentrum/"],
    "2026-08-12", "A",
    "NorthC lists its Düsseldorf data center at Suederstrasse 198 (built 2000, ISO 27001 certified since 2016), acquired from the Colt portfolio. Capacity not public.")

rec("North Rhine-Westphalia - Düsseldorf", "nLighten Düsseldorf edge data center", "operational", 4.8,
    "nLighten",
    ["https://www.nlighten.com/en/edge-location/dusseldorf/", "https://www.nlighten.com/en/edge-location/germany/"],
    "2026-08-11", "A",
    "Official nLighten page states 1,446 m2 dedicated colocation space and 4,800 kW power in the Düsseldorf metro area (facility address Ellerstrasse 101, 40721 Hilden, Kreis Mettmann). Kept under Düsseldorf because the marketed location is Düsseldorf; cross-listed under Mettmann in batch-101.")

rec("North Rhine-Westphalia - Düsseldorf", "Penta Infra Düsseldorf DUS01/DUS campus", "operational", 2.4,
    "Penta Infra",
    ["https://penta-infra.com/data-centers/duesseldorf/"],
    "2026-08-11", "A",
    "Official Penta Infra page states 2.4 MW IT capacity and planned expansion into a 9.5 MW IT-capacity Düsseldorf data-center campus together with DUS02.")

rec("North Rhine-Westphalia - Düsseldorf", "Equinix Düsseldorf DU1", "operational", 4,
    "Equinix",
    ["https://www.equinix.com/data-centers/europe-colocation/germany-colocation/dusseldorf-data-centers/du1", "https://www.ocolo.io/colocation/equinix/dusseldorf-du1/"],
    "2026-08-11", "B",
    "Equinix official page lists DU1 at Albertstrasse; OCOLO reports 4.00 MW power capacity and 58,738 ft2.")

rec("North Rhine-Westphalia - Ennepe-Ruhr-Kreis", "RZV DC1 Wetter", "operational", None,
    "RZV Rechenzentrum Volmarstein GmbH",
    ["https://www.rzv.de/", "https://www.rzv.de/ueber-rzv/", "https://www.datacentermap.com/germany/dortmund/rzv-dc1/"],
    "2026-08-12", "B",
    "RZV official pages describe certified cloud data centers (ISO 27001); DataCenterMap lists DC1 at Grundschoetteler Str. 21, 58300 Wetter (Ennepe-Ruhr-Kreis). Capacity not disclosed.")

rec("North Rhine-Westphalia - Ennepe-Ruhr-Kreis", "RZV DC2 Wetter", "operational", None,
    "RZV Rechenzentrum Volmarstein GmbH",
    ["https://www.rzv.de/", "https://www.rzv.de/ueber-rzv/", "https://www.datacentermap.com/germany/dortmund/rzv-dc2/"],
    "2026-08-12", "B",
    "RZV official pages describe certified cloud data centers; DataCenterMap lists DC2 at Am Gruenewald 10, 58300 Wetter. Capacity not disclosed.")

rec("North Rhine-Westphalia - Essen", "Ruhrallee 80 / Ruhrturm2 Essen data center project", "planned", None,
    "FAKT AG / DOKOM21",
    ["https://www.datacenter-insider.de/essen-bekommt-ein-rechenzentrum-mit-internet-knoten-a-1006549/", "https://www.presse-blog.com/2021/03/04/neues-rechenzentrum-an-der-ruhrallee-im-herzen-von-essen/", "https://www.eon.com/de/ueber-uns/presse/pressemitteilungen/2021/eon-entwickelt-nachhaltige-energiekonzepte.html"],
    "2021-03-04", "B",
    "2021 sources announced a 700 m2 data center with an internet exchange at Ruhrallee 80/RUHRTURM2; later completion status not confirmed in reviewed public sources.")

rec("North Rhine-Westphalia - Essen", "euNetworks Essen data center", "operational", None,
    "euNetworks",
    ["https://baxtel.com/data-center/eunetworks-essen", "https://inflect.com/building/hachestrasse-essen/eunetworks-group/datacenter/eunetworks-group-lnc-colocentre-essen-1"],
    "2026-08-11", "C",
    "Baxtel/Inflect list an operational euNetworks data center at Hachestrasse 8 in Essen; MW capacity not reported.")

rec("North Rhine-Westphalia - Essen", "MTI/GLH ESS01 data center", "operational", 2.8,
    "MTI / GLH",
    ["https://inflect.com/building/28-teilungsweg-essen/mti-glh/datacenter/ess01", "https://inflect.com/datacenters/emea/germany/ruhr-area"],
    "2026-08-11", "C",
    "Inflect lists ESS01 at 28 Teilungsweg, Essen with 2.8 MW total power capacity and N+1 cooling; aggregate/directory source only.")

rec("North Rhine-Westphalia - Essen", "Skaylink Essen data center", "operational", None,
    "Skaylink GmbH",
    ["https://www.datacentermap.com/germany/essen/skaylink-datacenter/"],
    "2026-08-11", "C",
    "DataCenterMap lists Skaylink Datacenter at Natorpstrasse 36, Essen; capacity not disclosed.")

nop("North Rhine-Westphalia - Euskirchen",
    "Searches found telecom/broadband providers and references to external municipal data centers, but no public evidence of a local colocation/hyperscale/data-center facility or announced project in Kreis Euskirchen.")

with open(OUT, "w", encoding="utf-8") as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote", len(R), "records")
