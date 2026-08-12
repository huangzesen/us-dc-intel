#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

OUT = "/Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/world/results-method/batch-101.jsonl"

R = []
def rec(division, name, status, cap, dev, urls, date, grade, notes):
    R.append({"country_code":"DE","country_name":"Germany","division":division,"name":name,"status":status,"capacity_mw":cap,"developer":dev,"source_urls":urls,"evidence_date":date,"evidence_grade":grade,"notes":notes})

def nop(division, notes):
    R.append({"country_code":"DE","country_name":"Germany","division":division,"no_projects":True,"notes":notes})

rec("North Rhine-Westphalia - Gelsenkirchen", "GELSEN-NET Gerhardstrasse Data Center", "operational", None,
    "GELSEN-NET Kommunikationsgesellschaft mbH",
    ["https://www.datacentermap.com/germany/gelsenkirchen/gelsen-net-data-center/", "https://www.stadtwerke-gelsenkirchen.de/presse-detail/neuer-ruhr-backbone-startet.html", "https://www.gelsen-net.de/geschaeftskunden/cyberrisikocheck.html"],
    "2026-08-12", "B",
    "DataCenterMap lists a GELSEN-NET data center in Gelsenkirchen; Stadtwerke Gelsenkirchen press note describes the Ruhr-Backbone being activated in the Gelsenkirchen data center; GELSEN-NET's own site says it operates its own data centers in the Ruhr area. No public IT load found.")

rec("North Rhine-Westphalia - Gütersloh", "Arvato Systems DC1 and DC3 Gütersloh", "operational", None,
    "Arvato Systems GmbH",
    ["https://www.arvato-systems.de/resource/blob/164858/fdff391c1a6f8e8398eb7732a175e317/din-en-50600-arvato-systems-gt-rz-de-19-94-2025-data.pdf", "https://inflect.com/datacenters/emea/germany/gutersloh"],
    "2025-04-02", "A",
    "TUEV SÜD certificate names Arvato Systems Rechenzentrum DC1 und DC3 at Reinhard-Mohn-Strasse 18, 33333 Gütersloh. Capacity not public.")

rec("North Rhine-Westphalia - Gütersloh", "BITel Business Service Housing / Telehouse Gütersloh", "operational", None,
    "BITel Gesellschaft für Telekommunikation mbH",
    ["https://www.bitel.de/geschaeftskunden/service/rechenzentrum.html", "https://www.bitel.de/ueber-bitel/unternehmen.html"],
    "2026-08-11", "A",
    "BITel describes a certified regional data center and identifies its Business Service Housing (Rechenzentrum Telehouse) in Gütersloh; no public MW disclosed.")

rec("North Rhine-Westphalia - Hagen", "Stadt Hagen replacement secondary data center", "planned", None,
    "Stadt Hagen",
    ["https://www.hagen.de/dateien/aus-dem-rathaus/fachbereiche-und-aemter/f-a-z/umweltamt-2/hochwasser-1/2023-04-04-wap-stadt-hagen-1-aenderungsantrag.pdf"],
    "2023-04-04", "A",
    "City flood-recovery application lists 'Ersatzneubau Zweit-Rechenzentrum' at Rathausstr. 1-11 after the city hall data center was destroyed by flooding; budget shown as EUR 7.65m. No MW public.")

rec("North Rhine-Westphalia - Hamm", "Blackstone / QTS Westfalen Data Center Campus near Hamm-Uentrop and Lippetal", "planned", 200,
    "Blackstone / Quality Technology Services (QTS) with Industriegebiet Westfalen GmbH",
    ["https://www.hamm.de/ob/newsdetail/eines-der-groessten-rechenzentren-deutschlands", "https://www.zeit.de/news/2026-01/15/us-firma-plant-rechenzentrum-in-nrw-fuer-vier-milliarden-euro", "https://www.golem.de/news/blackstone-4-milliarden-euro-fuer-rechenzentrum-in-nordrhein-westfalen-2601-204282.html", "https://www.lw.com/en/news/2026/01/latham-advises-blackstone-on-potential-development-of-major-data-center-campus-in-germany"],
    "2026-01-15", "A",
    "City of Hamm says a conditional purchase agreement enables development of a campus a few hundred meters from the Hamm-Uentrop A2 junction on Lippetal territory (intercommunal Industriegebiet Westfalen), with 200 MW planned IT capacity and about EUR 4bn investment; QTS is Blackstone's operating platform. Cross-boundary project relevant to Hamm division; formal citizen participation started July 2026.")

rec("North Rhine-Westphalia - Heinsberg", "Gangelt Data Center Industrial Park campus", "planned", None,
    "Unnamed investor / Gemeinde Gangelt",
    ["https://www.datacenterdynamics.com/en/news/thirteen-building-data-center-campus-eyed-in-west-germany-report/", "https://www.datacenter-insider.de/neuer-rechenzentrumscampus-in-gangelt-geplant-a-4277f70388f96d1a30497b24046d4cdc/", "https://www.aachener-zeitung.de/lokales/region-heinsberg/gangelt/investor-plant-gigantisches-rechenzentrum-in-gangelt/30384375.html"],
    "2025-01-08", "B",
    "Reports say Gangelt council approved a 20-hectare special area named Gewerbepark/Data Center Industrial Park on the L47, potentially up to 13 buildings of about 6,300 sqm each plus a substation. Later local reporting noted power-connection uncertainty; MW not public.")

rec("North Rhine-Westphalia - Herford", "DTS DataCenter Herford", "operational", None,
    "DTS Systeme GmbH",
    ["https://www.dts.de/en/cloud/platforms/dts-cloud", "https://www.datacentermap.com/germany/herford/dts-datacenter-herford/"],
    "2026-08-11", "A",
    "DTS states its own high-performance data centers in Herford and Münster are the core of its DTS Cloud services; DataCenterMap lists the Herford site at Schrewestrasse 2. Capacity not public.")

rec("North Rhine-Westphalia - Herne", "YEXIO Herne Data Center at FunkenbergQuartier", "construction", 2,
    "HOCHTIEF PPP Solutions / Palladio Partners / Yorizon",
    ["https://www.hochtief.de/aktuelles-medien/pressemitteilungen/pressemitteilung/spatenstich-im-funkenbergquartier-bau-des-yexio-rechenzentrums-beginnt", "https://www.datacenterdynamics.com/en/news/hochtief-to-build-2mw-wooden-edge-data-center-in-herne-germany/", "https://www.datacenter-insider.de/spatenstich-in-herne-fuer-neues-rechenzentrum-a-11c4536c0324035013ce51ade764551d/"],
    "2026-05-20", "A",
    "HOCHTIEF and Palladio Partners broke ground on 20 May 2026; facility is initially 2 MW IT capacity with expansion potential to 4 MW, timber construction with water cooling, completion scheduled for autumn 2027.")

rec("North Rhine-Westphalia - Herne", "GLASFASER RUHR / TMR Rechenzentrum Herne", "operational", None,
    "Telekommunikation Mittleres Ruhrgebiet GmbH / GLASFASER RUHR",
    ["https://www.glasfaser-ruhr.de/rechenzentrum/", "https://datacenter-group.com/en/news-stories/article/tmr-herne/", "https://www.herne.de/PDF/Finanzen/2018/Beteiligungsbericht-31.12.2018.pdf"],
    "2026-08-11", "A",
    "GLASFASER RUHR describes a TUEV Saarland-audited Herne colocation data center; Herne's 2018 participation report referenced expansion of data center space at the Herne DataCenter location. No public MW found.")

nop("North Rhine-Westphalia - Hochsauerlandkreis",
    "Searches returned no local data-center facility or announced project in the Hochsauerlandkreis; only generic IT-service and district administrative references.")

nop("North Rhine-Westphalia - Höxter",
    "Searches returned no local data-center facility or announced project in Kreis Höxter; only generic IT-service references.")

rec("North Rhine-Westphalia - Krefeld", "Telekom / T-Systems Krefeld data center", "operational", None,
    "Deutsche Telekom / T-Systems",
    ["https://www.datacenter-insider.de/datacenter-digitalisierungskathedralen-mit-renovierungsbedarf-a-1029109/", "https://www.computerwoche.de/article/2790283/vom-staatsbetrieb-zum-telematik-haus.html"],
    "2021-04-14", "B",
    "DataCenter-Insider describes the Telekom data center in Krefeld, built in the 1980s, using a classic redundant data center layout; older Computerwoche coverage identifies Krefeld among Deutsche Telekom Computer Service Management service/computer centers. No public MW found.")

rec("North Rhine-Westphalia - Leverkusen", "AtlasEdge LEV001 Leverkusen", "operational", None,
    "AtlasEdge",
    ["https://atlasedge.com/de/data-centres/leverkusen/", "https://atlasedge.com/data-centres/"],
    "2026-08-12", "A",
    "AtlasEdge lists LEV001 as an in-operation Leverkusen data centre at Dornierstrasse 10, 51381 Leverkusen; site page describes carrier-neutral, Tier 3-standard operation.")

rec("North Rhine-Westphalia - Leverkusen", "AtlasEdge LEV002 Leverkusen", "construction", 4.4,
    "AtlasEdge",
    ["https://atlasedge.com/atlasedge-accelerates-german-growth-with-second-leverkusen-data-centre/", "https://www.datacenterdynamics.com/en/news/atlasedge-starts-work-on-second-data-center-in-leverkusen-germany/", "https://www.datacenter-insider.de/atlas-edge-baut-zweites-rechenzentrum-in-leverkusen-a-c8317f6181d56c43ed7e6533d25786fd/"],
    "2026-04-16", "A",
    "AtlasEdge says LEV002 is adjacent to LEV001, construction commenced February 2026, 3,400 sqm of data-centre space, 4.4 MW capacity aimed at AI/high-density, ready for service Q2 2027.")

rec("North Rhine-Westphalia - Leverkusen", "ITENOS Leverkusen Data Center", "operational", None,
    "ITENOS GmbH",
    ["https://itenos.de/en/data-center-provider/data-center-germany/data-center-leverkusen/", "https://www.datacentermap.com/germany/cologne/itenos-leverkusen/"],
    "2026-08-11", "A",
    "ITENOS describes its Leverkusen data center as about 2,000 sqm, Level-3 certified, with DE-CIX connectivity.")

nop("North Rhine-Westphalia - Lippe",
    "Searches returned no local colocation/hyperscale facility or announced data-center project in Kreis Lippe; only generic IT-service references.")

rec("North Rhine-Westphalia - Mettmann", "AtlasEdge DUS001 Hilden", "operational", 20,
    "AtlasEdge",
    ["https://atlasedge.com/data-centres/dusseldorf/", "https://www.datacentermap.com/germany/duesseldorf/atlasedge-dus1/"],
    "2026-08-11", "A",
    "AtlasEdge lists DUS001 in operation at Zum Jaegerhof 10, 40724 Hilden (Kreis Mettmann), with over 10,000 sqm of data-centre space and 20 MW of available power.")

rec("North Rhine-Westphalia - Mettmann", "nLighten Duesseldorf DUS1 Hilden", "operational", 4.8,
    "nLighten",
    ["https://www.nlighten.com/en/edge-location/dusseldorf/", "https://www.datacentermap.com/germany/duesseldorf/kpn-dusseldorf/"],
    "2026-08-11", "A",
    "nLighten's Duesseldorf edge data center is located at Ellerstrasse 101, 40721 Hilden, with 1,446 sqm dedicated colocation space and published power of 4,800 kW on the official page.")

rec("North Rhine-Westphalia - Mettmann", "ITENOS Duesseldorf-Hilden DUS2", "planned", 20,
    "ITENOS GmbH",
    ["https://itenos.de/en/data-center-provider/data-center-germany/data-center-duesseldorf-2/"],
    "2026-08-11", "A",
    "ITENOS says its Hilden DUS2 currently offers 3,600 sqm and will expand to 10,000 sqm with 20 MW capacity when completed.")

rec("North Rhine-Westphalia - Mettmann", "YEXIO Heiligenhaus Data Center", "operational", 4,
    "HOCHTIEF PPP Solutions / Palladio Partners",
    ["https://www.hochtief.com/news-media/stories-and-interviews/opening-yexio-heiligenhaus", "https://www.hochtief.com/activities/selected-projects/yexio-data-center-heiligenhaus-germany", "https://www.datacentermap.com/germany/duesseldorf/yexio-heiligenhaus/"],
    "2025-09-11", "A",
    "HOCHTIEF says Germany's first YEXIO data centre in Heiligenhaus (Kreis Mettmann) entered operation on 11 September 2025; DataCenterMap lists the facility at 4 MW.")

rec("North Rhine-Westphalia - Mettmann", "NETMOUNTAINS VEL1 & VEL2 Velbert", "operational", 8,
    "NETMOUNTAINS Group GmbH",
    ["https://netmountains.de/", "https://www.datacenterdynamics.com/en/news/germanys-netmountains-launches-data-center-in-velbert/", "https://www.datacentermap.com/germany/duesseldorf/netmountains-velbert-vel1/"],
    "2025-10-06", "B",
    "NETMOUNTAINS says its modern Velbert data center has opened with direct liquid cooling; DCD reports VEL1/VEL2 at Industriestrasse 76 with first-phase capacity for 100 racks. DataCenterMap lists 8 MW.")

rec("North Rhine-Westphalia - Mettmann", "Heinrich-Hertz-Strasse 21 Erkrath Data Center", "planned", None,
    "Unknown",
    ["https://www.datacenterdynamics.com/en/news/new-data-center-planned-in-erkrath-germany/", "https://www.datacentermap.com/germany/duesseldorf/heinrich-hertz-strasse-21/"],
    "2025-01-13", "B",
    "DCD reports a planned data center in Erkrath's Unterfeldhaus commercial area on Heinrich-Hertz-Strasse, with details and timeline not yet shared.")

nop("North Rhine-Westphalia - Minden-Lübbecke",
    "Searches returned no local colocation/hyperscale facility or announced data-center project in Kreis Minden-Lübbecke; only generic IT-service references.")

rec("North Rhine-Westphalia - Märkischer Kreis", "Telemark Rechenzentrum Luedenscheid", "operational", 0.5,
    "TeleMark Telekommunikationsgesellschaft Mark mbH",
    ["https://www.datacentermap.com/germany/ludenscheid/telemark-rechenzentrum-ludenscheid/", "https://www.datacenters.com/providers/telemark-telekommunikationsgesellschaft", "https://www.wjl.de/tag/telemark/"],
    "2026-08-12", "C",
    "Aggregator listings identify Telemark Rechenzentrum Luedenscheid as an operational colocation facility in Luedenscheid with 0.5 MW; Wirtschaftsjunioren describe Telemark operating the Rechenzentrum Märkischer Kreis 24x7.")

rec("North Rhine-Westphalia - Märkischer Kreis", "INDUSYS Cloud/Rechenzentrum Luedenscheid", "operational", None,
    "INDUSYS GmbH",
    ["https://www.indusys.de/cloud/", "https://www.indusys.de/"],
    "2026-08-12", "A",
    "INDUSYS advertises colocation/cloud services from a German data center for Luedenscheid, Iserlohn, Maerkischer Kreis and Suedwestfalen; no MW capacity disclosed.")

rec("North Rhine-Westphalia - Mönchengladbach", "WIIT / myLoc MGL 1 Moenchengladbach", "operational", None,
    "WIIT AG",
    ["https://www.wiit.cloud/en/services/cloud/colocation/data-center-moenchengladbach/", "https://www.wfmg.de/wiit-ag-in-moenchengladbach-rechenzentrum-neu-eroeffnet/", "https://www.datacenter-insider.de/die-neuen-rechenzentren-der-wiit-ag-a-e54c8fe2b34826f55a9e4ea2a7a291f3/", "https://www.datacentermap.com/germany/duesseldorf/wiit-mgl1/specs/"],
    "2024-03-20", "A",
    "WIIT's official page lists a Moenchengladbach data center at Dieselstrasse 34 with 440 sqm and 176 racks (Tier III); local economic development reported the newly opened facility and ISO certification; Datacenter-Insider covered the WIIT grand opening including the Moenchengladbach backup data center.")

rec("North Rhine-Westphalia - Mönchengladbach", "ucs datacenter Moenchengladbach", "operational", None,
    "ucs datacenter GmbH",
    ["https://www.ucs.cloud/"],
    "2026-08-11", "A",
    "ucs datacenter GmbH lists its headquarters and data center in 41199 Moenchengladbach and describes itself as a German mid-market data center provider.")

nop("North Rhine-Westphalia - Mülheim an der Ruhr",
    "Searches returned no local colocation/hyperscale facility or announced data-center project in Mülheim an der Ruhr; only generic IT references.")

rec("North Rhine-Westphalia - Münster", "DTS DataCenter Muenster", "operational", None,
    "DTS Systeme Muenster GmbH",
    ["https://www.dts-it-ag.de/en/gesellschaften/dts-systeme-muenster-gmbh.html", "https://www.datacentermap.com/germany/munster/dts-datacenter-munster/"],
    "2026-08-11", "A",
    "DTS says its Muenster IT service provider has its own datacenter; DataCenterMap places DTS DataCenter Muenster at Soester Strasse 13.")

rec("North Rhine-Westphalia - Münster", "GLOBE Development Datacenter Muenster", "operational", None,
    "GLOBE Development GmbH",
    ["https://www.globe.de/", "https://www.peeringdb.com/fac/9109", "https://whois.ipip.net/AS12470"],
    "2026-08-12", "A",
    "GLOBE advertises colocation, servers and hosting operated from its own datacenter in Muenster with reported platform availability above 99.99%; PeeringDB lists the facility and AS12470.")

rec("North Rhine-Westphalia - Münster", "Telehaus Muenster", "operational", None,
    "1&1 Versatel",
    ["https://www.datacentermap.com/germany/munster/telehaus-munster/", "https://www.peeringdb.com/fac/12653"],
    "2026-08-11", "C",
    "DataCenterMap and PeeringDB list Telehaus Muenster at Willy-Brandt-Weg 37A, operated by 1&1 Versatel, with about 900 sqm of data center space.")

nop("North Rhine-Westphalia - Oberbergischer Kreis",
    "Searches returned no local colocation/hyperscale facility or announced data-center project in the Oberbergischer Kreis; only generic IT-service references.")

rec("North Rhine-Westphalia - Oberhausen", "KAMP Rechenzentrum Oberhausen", "operational", None,
    "KAMP Netzwerkdienste GmbH",
    ["https://www.kamp.de/kamp-rechenzentrum.html", "https://www.datacentermap.com/germany/oberhausen/kamp-rechenzentrum/", "https://datacenterplatform.com/data-centers/kamp/kamp-germany/kamp-oberhausen/"],
    "2026-08-12", "A",
    "KAMP's official site describes its certified NRW data center for server housing/IT outsourcing; DataCenterMap and DatacenterPlatform locate KAMP Oberhausen at Vestische Strasse 89-91.")

rec("North Rhine-Westphalia - Oberhausen", "RITTER Technologie Oberhausen Data Center", "operational", None,
    "RITTER Technologie GmbH",
    ["https://www.rittec.de/en/infrastruktur/rechenzentrum/"],
    "2026-08-11", "A",
    "RITTER Technologie states it plans and operates dedicated infrastructure environments at its data center in Oberhausen, Germany; no public MW disclosed.")

with open(OUT, "w", encoding="utf-8") as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote", len(R), "records")
