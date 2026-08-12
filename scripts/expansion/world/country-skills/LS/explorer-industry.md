# LS Explorer Industry - Lesotho Data-Centre Discovery Methodology

Date: 2026-08-12. Scope: Lesotho (LS) data-centre discovery from industry media, local press, operator/vendor pages, cloud announcements, data-centre directories and district search patterns. Use this file for lead generation; verify every material lead through the official-source workflow in `explorer-official.md`.

District model: Maseru; Berea; Butha-Buthe (also Botha-Bothe); Leribe; Mafeteng; Mohale's Hoek; Mokhotlong; Qacha's Nek; Quthing; Thaba-Tseka.

## Reliability Grades

- A: official/primary source, including operator pages, LCA/LTA records, gov.ls or MICSTI documents, Department of Environment EIA, LEWA/LEC/LHDA/DoE, LAA/council/LNDC land records or official cloud-provider region pages.
- B: strong secondary source, including established local press, trade press, LENA state-news reporting, ISOC/Af-IX material, vendor case studies and tender reposts that reproduce official procurement text.
- C: weak lead, including directories, social posts, old MoU reposts, market reports, scraped pages and unsourced marketing.

Industry discovery can create B/C leads, but an enumerated facility should not be final A unless a primary source names the facility or site.

## Verified Discovery Frame

- Confirmed A-grade operator/institutional seeds: Vodacom Lesotho names two data centres, Maseru West and Lekokoaneng, on its Fixed Solutions page; LIXP says it migrated to the LCA data centre in 2017; gov.ls and the 2021 e-Gov EOI support Mohale's Hoek plus three Government Data Centres.
- ETL/Econet Telecom Lesotho remains a high-value lead because directories and ecosystem evidence point to a Maseru data centre, but directory pages alone are C. Upgrade only with ETL, LCA, land, power or procurement evidence.
- Kobong Hydropower and AI Data Centre Project is an announced Mokhotlong pipeline lead. Convalt's press page and trade press support an approved Memorandum of Agreement/large investment story; facility details, construction and IT-load capacity remain unverified.
- Trade-press statements that Lesotho has """two operational data centers""" should be treated as a market-size floor, not as an exhaustive facility count. They appear to summarize telecom/government services rather than reconcile separate Vodacom, LCA and government sites.

## Industry and Press Sources

| Source | URL / route | Use | Grade |
|---|---|---|---:|
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | Kobong and African data-centre market leads. | B |
| Connecting Africa | https://www.connectingafrica.com/ | Telecom, cloud, Starlink, Kobong and regional digital-infrastructure leads. | B |
| Investment Monitor | https://www.investmentmonitor.ai/ | Kobong investment report and development-finance framing. | B |
| TechAfrica News | https://techafricanews.com/ | Kobong approval, Vodacom/government digitisation and ICT policy leads. | B |
| Business Insider Africa | https://africa.businessinsider.com/ | Early Kobong coverage and investment figures. | B |
| LENA | https://www.lena.gov.ls/ | State-news coverage; useful for ministry quotes and policy direction, e.g. data-centre agenda. | B/A- for direct official quotations |
| Lesotho Times | https://lestimes.com/ | Local political/business/ICT reporting. | B |
| The Post | https://www.thepost.co.ls/ | Local business and government reporting. | B/C |
| Public Eye | https://publiceyenews.com/ | Local connectivity, public-sector and investor stories. | B/C |
| The Reporter | https://www.thereporter.co.ls/ | Local ICT/interconnection stories, including LIXP revamp leads. | B |
| Newsday / Informative / Sunday Express | https://newsdayonline.co.ls/ ; https://lesotho.misa.org/media-directory/ ; https://sundayexpress.co.ls/ | Local discovery sweeps. | C/B |
| Selibeng | https://selibeng.com/ | Tender and GPN aggregator for MICSTI, e-Gov, UPS, LNDC and public procurement leads. | B when official text is reproduced; otherwise C |
| LNDC knowledge base | https://lndc.org.ls/knowledge-base/ | Investor process, EIA, LAA, LCA licensing and estate context. | B/A if LNDC-authored |
| ISOC / Af-IX / PeeringDB | https://af-ix.org/ixps-list ; https://www.peeringdb.com/ix/5015 | IXP and interconnection evidence. | B |
| DataCenterMap / datacenters.com / Baxtel | https://www.datacentermap.com/lesotho/ ; https://www.datacenters.com/locations/lesotho ; https://baxtel.com/map | Discovery only; can reveal names but frequently lacks primary proof. | C |
| Vendor pages | Schneider Electric, Vertiv, Huawei, ZTE, Caterpillar and local UPS/genset contractors | Equipment, UPS, cooling, genset and commissioning leads. | B/C |

## Operator and Developer Sweep

| Operator/developer | Primary URL | Lesotho signal | Grade handling |
|---|---|---|---|
| Vodacom Lesotho | https://www.vodacom.co.ls/business/fixed-solutions/ | Officially names two data centres: Maseru West and Lekokoaneng; markets colocation and fixed business services. | A for existence/name/location; search for capacity, power and parcel proof. |
| Econet Telecom Lesotho / ETL | https://www.etl.co.ls/ | Licensed incumbent and LIXP peer; directories list a Maseru data-centre lead. | C from directories; B/A only with ETL, LCA, LEC, LAA or tender evidence. |
| LCA | https://lca.org.ls/ | Regulator and host institution for LCA data centre per LIXP official page. | A for LCA data-centre existence via LIXP; B for specs unless LCA source found. |
| LIXP | https://lixp.org.ls/about/ | IXP moved to LCA data centre; hosts content/cache/root-server ecosystem. | Interconnection evidence, not a standalone facility. |
| MICSTI / Government Data Centres | https://communications.gov.ls/ ; https://www.gov.ls/ | e-Government programme, Mohale's Hoek data centre, three Government Data Centres. | A via gov.ls/EOI; resolve exact locations before district assignment. |
| Convalt Energy / Kobong | https://convalt.com/press_releases | U.S. Embassy/Convalt announcement says Kobong project includes hydropower, solar and a large-scale AI data centre. | B for announced project; C for facility details until permits/construction. |
| Starlink | https://www.starlink.com/ | Lesotho connectivity/ISP lead only. | Not a data centre. |
| Liquid Intelligent Technologies / Africa Data Centres | https://liquid.tech/ ; https://www.africadatacentres.com/ | Regional operators with South African footprint; no verified Lesotho facility found. | Require Lesotho-specific primary evidence. |
| Cloud hyperscalers | AWS/Azure/Google/Oracle official region pages | No public Lesotho cloud region found; nearest regions in South Africa. | Negative official check. |

Queries:
```text
"Vodacom Lesotho" "Maseru West" "Lekokoaneng"
"Vodacom Lesotho" "colocation" OR "data centres"
"Econet Telecom Lesotho" "data centre" OR "data center" OR hosting
"LIXP" "LCA data centre" OR "data center"
"Mohale's Hoek" "data centre" OR "data center"
"three Government Data Centres" Lesotho
"Kobong" "Convalt" "AI Data Centre" Lesotho
"{operator}" Lesotho "racks" OR "MW" OR "UPS" OR "Tier III"
"{operator}" "Uptime Institute" Lesotho
```

## Kobong Pipeline Handling

Use industry press to monitor Kobong, but keep status conservative.

Known public lead set:
- Convalt press releases: https://convalt.com/press_releases
- DCD Kobong report: https://www.datacenterdynamics.com/en/news/us-energy-company-plots-12gw-hydropower-plant-and-ai-data-center-in-lesotho-report/
- Investment Monitor Kobong report: https://www.investmentmonitor.ai/news/lesotho-signs-6-2bn-hydropower-deal/
- TechAfricaNews approval report: https://techafricanews.com/2026/08/03/lesotho-approves-us6-2-billion-kobong-hydropower-and-ai-data-centre-project/

Collection rule: record as Mokhotlong announced pipeline only. Upgrade lifecycle when one of these appears: official feasibility award/completion, Environment Act EIA documents, LEWA generation licence/PPA, LAA lease/plot, EPC/construction procurement, site works or commissioning evidence.

## District Industry Search Guidance

Base press sweep for every district:
```text
"{district}" Lesotho "data centre" OR "data center" OR datacentre
"{district}" Lesotho colocation OR hosting OR "server farm" OR "server room"
"{district}" Lesotho UPS OR generator OR substation "data"
site:lena.gov.ls "{district}" "data centre" OR "digital infrastructure"
site:lestimes.com "{district}" "data centre" OR "ICT"
site:thepost.co.ls "{district}" "data centre" OR "ICT"
site:selibeng.com "{district}" "UPS" OR "data centre" OR "e-Government"
```

- Maseru: highest yield. Search Maseru West, LCA data centre, LIXP, ETL/Econet, Vodacom Park, Kingsway Road, Old Europa, Mabille Road, Thetsane, Ha Tikoe/Tikoe, Moposo, LNDC Centre. Press leads should be joined to LCA, operator, LAA/council and LEC evidence.
- Berea: search Lekokoaneng, Teyateyaneng/TY, Malimong, Berea District Council and Vodacom. Main verified seed is Vodacom Lekokoaneng; district attribution should be checked with land/council records.
- Leribe: search Hlotse, Maputsoe, Ha Nyenye, Peka, Leribe District Council, LNDC estate, border fibre and industrial power. No confirmed DC seed; likely negative unless a telco/industrial lead appears.
- Butha-Buthe / Botha-Bothe: search both spellings plus Belo, 'Muela, LHDA, LNDC and industrial site. Energy/hydro stories are infrastructure context, not DC evidence.
- Mafeteng: search Mafeteng town, Likhoele tower, Ha Ramarothole solar, LEGCO/LEWA and LNDC. Treat power/solar as lead context only.
- Mohale's Hoek: high-priority government search. Search Mohale's Hoek data centre, power house, e-Government Phase I/II, commissioning, UPS, LEC and council approvals.
- Mokhotlong: high-priority pipeline search. Search Kobong, Convalt, Polihali, Senqunyane, Letseng, hydropower, AI data centre, LEWA and EIA. Keep all non-permitted material as announced.
- Qacha's Nek: search Qacha's Nek and Thamathu tower with data-centre/cloud/UPS terms. Likely negative-search district.
- Quthing: search Quthing, Moyeni, southern border connectivity, council/EIA/telecom terms. Likely negative-search district.
- Thaba-Tseka: search Thaba-Tseka, Katse adjacency, public-sector connectivity, council/EIA/telecom terms. Likely negative-search district.

## Negative-Search Protocol

For districts without a seed, record a defensible negative only after checking:
1. local/trade press using data-centre variants;
2. LCA licence and public-consultation notices;
3. gov.ls/MICSTI/e-Government records;
4. Department of Environment/EIA terms;
5. LEWA/LEC/LHDA/DoE power terms;
6. LAA/council/LNDC land or industrial-estate terms;
7. named operators: Vodacom, ETL/Econet, LCA, LIXP, LECC, Comnet, Jenny, Starlink, Liquid, Huawei, Schneider, Vertiv.

Do not record cyber cafes, computer labs, bank server rooms, tower shelters or routine telecom exchange rooms unless the source explicitly describes a data centre, colocation, cloud, hosting or comparable facility.

## De-Duplication and Capacity Rules

- Do not merge Vodacom Maseru West and Vodacom Lekokoaneng; the official page names two data centres.
- Do not count LIXP separately from the LCA data centre; it is hosted inside the facility.
- Do not assign the two non-Mohale's Hoek government data centres to a district until a primary document identifies their sites.
- Treat data-centre directory entries as leads to resolve, not as final truth.
- Separate power-generation capacity from IT load. Kobong's hydropower/solar figures are generation claims, not data-centre MW.
- Lifecycle wording matters: MoU/approved/planned/feasibility = announced; tender/EPC/site works = pipeline; commissioned/operational/operator-marketed = operational, subject to primary evidence.
