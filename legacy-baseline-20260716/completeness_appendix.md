# Phase 4 completeness / baseline appendix

Cutoff: **2026-07-16**.

This appendix records the coverage boundary and comparison material for the all-company U.S. construction panorama. It does not claim that confidential, private, unnamed, routine, or sub-threshold work is knowable.

## What “all” means

“All” means all publicly identifiable active new builds and major expansions that produced dated site, approval, permitting, construction, energization, commissioning, phased-service, or current material-proposal evidence under the research brief’s evidence definition. Confidential/private/unnamed/sub-threshold routine additions and private server rooms are unknowable from public records. A zero-result jurisdiction means that no qualifying public record survived the assigned search pass at the cutoff; it is not proof of absence.

Government records outrank company, investor, major-press, local-press, and discovery-aggregator claims. Announcement ≠ vote; approval ≠ permit; permit ≠ construction; construction ≠ energization/live service. Capacity figures remain in source terms and are not silently converted between IT MW, contracted load, compute load, investment, square footage, building count, and site-support potential.

## Mechanical validation

| Check | Result |
|---|---|
| Jurisdictions | 51 rows, 51 unique codes, exact once = **True** |
| National seed | 75 rows; candidate-count sum = 75 |
| Phase 2 / Phase 3 | 186 / 186; ID intersection 186; Phase 2-only 0; Phase 3-only 0; exact set = **True** |
| State-count sums | Phase 2 186; Phase 3 186 |
| HTTPS source check | 643 unique HTTP(S) URL values scanned; non-HTTPS = 0; all project source URLs HTTPS = **True** |
| Comparison-only U.S. rows | Phase 2 IDs from comparison-only U.S. material = 0 |
| Category totals | hyperscalers 64; AI labs 10; developer-role 186; utility/enterprise 84 |

The national seed is a discovery baseline, not an additive register. The four regional Phase 2 registers total 186 rows; the twelve Phase 3 registers reproduce the same 186 canonical IDs exactly.

## 50-state + DC coverage matrix

Candidate count is the count of rows in the 75-row national seed. Verified counts are the canonical regional Phase 2 and Phase 3 rows. The JSON contains every HTTPS source URL; the table shows up to three examples per jurisdiction.

| Jurisdiction | Seed candidates | Phase 2 | Phase 3 | Negative result / regional finding | Access caveat | Sources |
|---|---:|---:|---:|---|---|---|
| Alabama | 1 | 2 | 2 | qualifying found | Company announcement is accessible; no linked city or county approval packet was identified.<br>State report is an economic-development record, not a city site-plan or building record. | [1](https://investors.corescientific.com/news-events/press-releases/detail/107/core-scientific-announces-expansion-into-auburn-alabama-with-new-high-performance-computing-facility) [2](https://www.auburnal.gov/planning/development-services/) [3](https://www.jacksoncountyal.gov/DocumentCenter/View/1414/DRAFT_HMPG-26) +3 more in JSON |
| Alaska | 0 | 3 | 3 | STAK North Slope proposal; TA Infrastructure/Hilcorp North Slope pilot application; Air Force solicitation for possible facilities. No energized hyperscale build verified. | Local reporting; not a lease, land-use, building, air, water, or utility permit.<br>The cited page is a nonprofit/local analysis of state lease documents; the underlying final DNR disposition was not retrieved. | [1](https://alaskapublic.org/news/economy/energy/2026-05-26/alaskas-north-slope-proposed-as-home-for-massive-ai-data-center) [2](https://aws.state.ak.us/OnlinePublicNotices/Notices/) [3](https://aws.state.ak.us/OnlinePublicNotices/Notices/View.aspx?id=217467) +3 more in JSON |
| Arizona | 3 | 7 | 7 | qualifying projects found; ACC, Maricopa/Mesa/Pima records, operators, and local queries | Official state page accessible; it does not expose the Port lease, parcel-level permit register, inspections, or energization record.<br>Non-government report; no associated Muskogee permit or utility filing was located. | [1](https://azcc.gov/news/home/2026/02/06/vice-chair-walden-releases-statement-on-project-baccara) [2](https://bealeinfra.com/beale-infrastructure-works-with-tep-to-pursue-additional-carbon-free-energy-resources-to-serve-future-growth-in-southern-arizona/) [3](https://bealeinfra.com/location/pima-county/) +12 more in JSON |
| Arkansas | 0 | 1 | 1 | qualifying found | Company announcement is accessible; no linked city or county approval packet was identified.<br>State report is an economic-development record, not a city site-plan or building record. | [1](https://www.arkansasedc.com/news-events/newsroom/detail/2026/01/12/avaio-digital-announces-new-large-scale-ai-ready-data-center-and-power-campus-in-little-rock--arkansas) [2](https://www.entergy.com/datacenters/arkansas) [3](https://www.pulaskicounty.net/) |
| California | 0 | 4 | 4 | Microsoft Alviso; Prime Sacramento; Imperial IVCM; CoreSite SV9 expansion. | The official meeting record exposes the action summary but not a complete roll-call tally in the reviewed extract.<br>The city page says its list is updated monthly and may not reflect every current permit status; it is not a certificate-of-occupancy record. | [1](https://agendanet.saccounty.gov/OnBaseAgendaOnline/Meetings/ViewMeetingAgenda?meetingId=10380&type=AGENDATYPEVALUE) [2](https://imperialcounty.org/2025/12/plancommlotmerger/) [3](https://planning.saccounty.gov/PlansandProjectsIn-Progress/Design%20Review%20Committee/07.24.25%20DRAC%20Agenda.pdf) +14 more in JSON |
| Colorado | 0 | 2 | 2 | qualifying projects found | Company announcement does not publish a Denver permit, inspection, or CO number.<br>Operator page is not a governmental inspection or energization record. | [1](https://coloradosprings.gov/developmenttracker) [2](https://coloradosprings.gov/node/163450) [3](https://gazette.com/2026/06/22/appeals-filed-against-project-taurus-data-center-development-whats-next/) +6 more in JSON |
| Connecticut | 0 | 0 | 0 | No qualifying new build or major expansion verified after targeted searches of CT DECD, CEQ, Hartford and planning material; Hartford AI-center references do not establish data-center construction. | Government portals, imaged packets, and live search systems may not expose every permit or inspection record in the retrieved pass.<br>Company, trade, and local-press sources are retained as evidence but are not treated as a vote, permit, energization, occupancy, or live-service record without that record. | No qualifying HTTPS project-source URL carried forward; see the regional search ledger. |
| Delaware | 0 | 0 | 0 | Rumor/withdrawn leads lacked current site-specific evidence. | Government portals, imaged packets, and live search systems may not expose every permit or inspection record in the retrieved pass.<br>Company, trade, and local-press sources are retained as evidence but are not treated as a vote, permit, energization, occupancy, or live-service record without that record. | No qualifying HTTPS project-source URL carried forward; see the regional search ledger. |
| Florida | 0 | 0 | 0 | Operational/ordinary colo references lacked current major expansion evidence. | Government portals, imaged packets, and live search systems may not expose every permit or inspection record in the retrieved pass.<br>Company, trade, and local-press sources are retained as evidence but are not treated as a vote, permit, energization, occupancy, or live-service record without that record. | No qualifying HTTPS project-source URL carried forward; see the regional search ledger. |
| Georgia | 2 | 7 | 7 | qualifying found | Notice is a construction-activity notice and does not publish the underlying permit number.<br>Agenda/staff request is not substituted for minutes or a vote tally. | [1](https://dca.georgia.gov/developments-regional-impact-dri-faqs) [2](https://dca.georgia.gov/document/document/2025-515brdghrwllms/download) [3](https://dca.georgia.gov/document/document/2025-545vrbnastredevms/download) +20 more in JSON |
| Hawaii | 0 | 1 | 1 | Servpac MTP Building 2. | Local reporting; not a lease, land-use, building, air, water, or utility permit.<br>The cited page is a nonprofit/local analysis of state lease documents; the underlying final DNR disposition was not retrieved. | [1](https://buildingindustryhawaii.com/2026/03/servpac-inc-breaks-ground-on-mtp-data-centers-building-2/) [2](https://servpac.com/mtp-groundbreaking/) [3](https://wpc-viewer.doh.hawaii.gov/) +2 more in JSON |
| Idaho | 0 | 2 | 2 | qualifying projects found | Company announcement does not publish a Denver permit, inspection, or CO number.<br>Operator page is not a governmental inspection or energization record. | [1](https://adacounty.id.gov/developmentservices/permitting-division/) [2](https://boisedev.com/news/2025/04/03/kuna-data-center-diode-ventures/) [3](https://datacenters.atmeta.com/2022/02/hello-kuna/) +7 more in JSON |
| Illinois | 2 | 4 | 4 | qualifying projects found | The primary accessible record is Alliant's official announcement rather than a City packet; no municipal vote sheet was located in the reviewed search.<br>Company/utility announcement; local approval details are not attached. | [1](https://edged.us/news/edged-us-expands-chicagoland-campus) [2](https://morrisil.org/data-center-resources/) [3](https://www.datacenterdynamics.com/en/news/tract-expands-into-illinois-with-plans-for-1gw-data-center-park-outside-chicago/) +10 more in JSON |
| Indiana | 8 | 9 | 9 | qualifying projects found | Official state page accessible; it does not publish a county/town vote tally or a building-by-building completion register.<br>IDEM PDF is public and searchable; the meeting is an agency permitting proceeding, not a local zoning vote. | [1](https://about.fb.com/news/2026/02/metas-new-data-center-lebanon-indiana-marks-milestone-ai-investment/amp/) [2](https://apnews.com/article/a27bac9f20de516dbe35f9242174e888) [3](https://apnews.com/article/ccdad82728a72025f37383e3811f13f6) +25 more in JSON |
| Iowa | 2 | 3 | 3 | qualifying projects found | The primary accessible record is Alliant's official announcement rather than a City packet; no municipal vote sheet was located in the reviewed search.<br>Company/utility announcement; local approval details are not attached. | [1](https://www.alliantenergy.com/news/news-center/2025/02/021225-qtsannouncementcr) [2](https://www.axios.com/local/des-moines/2025/02/20/norwalk-data-center-project-west-meta-microsoft) [3](https://www.axios.com/local/des-moines/2026/01/16/microsoft-west-des-moines-data-center-water-zero) +5 more in JSON |
| Kansas | 1 | 1 | 1 | qualifying project found | Company announcement; it does not establish a city/county approval, building permit, actual groundbreaking, or energized service.<br>Company infrastructure claim; no municipal, KDHE, EPA, or Evergy permit/interconnection closeout was retrieved. | [1](https://bealeinfra.com/beale-infrastructure-announces-hyperscale-kansas-data-center-campus-advancing-3-billion-infrastructure-investment/) [2](https://bealeinfra.com/beale-infrastructure-upgrades-critical-water-infrastructure-to-secure-long-term-water-resiliency-for-de-soto/) [3](https://bealeinfra.com/location/de-soto/) +1 more in JSON |
| Kentucky | 0 | 2 | 2 | qualifying found | Company announcement is accessible; no linked city or county approval packet was identified.<br>State report is an economic-development record, not a city site-plan or building record. | [1](https://calvertcityky.gov/community/) [2](https://corescientific.com/high-density-data-centers/calvert-city-ky/) [3](https://investors.corescientific.com/sec-filings/all-sec-filings/content/0001628280-24-010544/0001628280-24-010544.pdf) +9 more in JSON |
| Louisiana | 1 | 1 | 1 | qualifying found | Company announcement is accessible; no linked city or county approval packet was identified.<br>State report is an economic-development record, not a city site-plan or building record. | [1](https://about.fb.com/news/2025/12/metas-richland-parish-data-center-supports-louisiana-economy-875-million-in-contracts/) [2](https://lpscpubvalence.lpsc.louisiana.gov/portal/PSC/DocketDetails?docketId=32146) [3](https://lpscpubvalence.lpsc.louisiana.gov/portal/PSC/DocumentDetails?documentId=176967) +5 more in JSON |
| Maine | 0 | 4 | 4 | Jay on hold; Lewiston rejected; Nautilus Millinocket canceled; Scarborough incomplete proposal. | Local reporting; not a lease, land-use, building, air, water, or utility permit.<br>The cited page is a nonprofit/local analysis of state lease documents; the underlying final DNR disposition was not retrieved. | [1](https://apnews.com/article/352ad4fbd531d905b9415258692b318f) [2](https://www.bangordailynews.com/2025/04/09/mainefocus/mainefocus-business/300m-data-center-former-millinocket-paper-mill-canceled/) [3](https://www.datacenterdynamics.com/en/news/nautilus-cancels-flagship-maine-data-center/) +10 more in JSON |
| Maryland | 1 | 2 | 2 | qualifying found | County summary is the accessible official record; the agenda packet is separately linked in the official Agenda Center.<br>County project page reports the action; a separate EDA minutes packet was not located. | [1](https://frederickcountymd.gov/Archive.aspx?AMID=128) [2](https://frederickcountymd.gov/ArchiveCenter/ViewFile/Item/14901) [3](https://frederickcountymd.gov/m/newsflash/home/detail/5845) +9 more in JSON |
| Massachusetts | 0 | 2 | 2 | Servistar Westfield proposal; Markley Lowell contested expansion. | Local reporting; not a lease, land-use, building, air, water, or utility permit.<br>The cited page is a nonprofit/local analysis of state lease documents; the underlying final DNR disposition was not retrieved. | [1](https://apnews.com/article/5607b4ea8ef9776b28268561060752a8) [2](https://malegislature.gov/Laws/SessionLaws/Acts/2024/Chapter238) [3](https://westfielddevelopment.com/m/newsflash/Home/Detail/1724) +8 more in JSON |
| Michigan | 1 | 2 | 2 | qualifying projects found | The primary accessible record is Alliant's official announcement rather than a City packet; no municipal vote sheet was located in the reviewed search.<br>Company/utility announcement; local approval details are not attached. | [1](https://openai.com/index/stargate-michigan-data-center/) [2](https://salinetownship.org/uploads/minutes/1763385582_September%202025%20minutes.pdf) [3](https://salinetownship.org/uploads/notices/SalineDataCenterConsentJudgmentFinalExecutionCopy492124804975v1.pdf) +3 more in JSON |
| Minnesota | 2 | 6 | 6 | qualifying projects found | Company announcement; it does not establish a city/county approval, building permit, actual groundbreaking, or energized service.<br>Company infrastructure claim; no municipal, KDHE, EPA, or Evergy permit/interconnection closeout was retrieved. | [1](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/data-center-pine-island/) [2](https://datacenters.google/discover-more/faq/) [3](https://hermantownmn.com/community/community-highlights/google-announces-plans-for-hermantown-data-center/) +13 more in JSON |
| Mississippi | 3 | 5 | 5 | qualifying found | Company announcement is accessible; no linked city or county approval packet was identified.<br>State report is an economic-development record, not a city site-plan or building record. | [1](https://apnews.com/article/433691ace945708a04762b4791602f3d) [2](https://buildportal.madisonal.gov/eSuite.Permits/WelcomePage.aspx) [3](https://governorreeves.ms.gov/amazon-continues-mississippi-expansion-announcing-plans-to-invest-a-total-of-25-billion-across-the-magnolia-state/) +20 more in JSON |
| Missouri | 0 | 4 | 4 | qualifying projects found | Company announcement; it does not establish a city/county approval, building permit, actual groundbreaking, or energized service.<br>Company infrastructure claim; no municipal, KDHE, EPA, or Evergy permit/interconnection closeout was retrieved. | [1](https://datacenters.google/) [2](https://datacenters.google/discover-more/faq/) [3](https://ded.mo.gov/press-room/google-deepens-missouri-roots-15-billion-community-investment-montgomery-county) +13 more in JSON |
| Montana | 0 | 1 | 1 | one public proposal found but stalled/paused | Company announcement does not publish a Denver permit, inspection, or CO number.<br>Operator page is not a governmental inspection or energization record. | [1](https://live.web.missoula.co/) [2](https://missoulacountyvoice.com/data-center-interim-zoning) [3](https://www.missoulacounty.gov/news/missoula-county-commissioners-to-consider-interim-zoning-for-data-centers/) +2 more in JSON |
| Nebraska | 0 | 0 | 0 | No stable, named new-build/major-expansion record with current 2024-2030 construction/approval evidence survived search; this is not proof of absence. | Government portals, imaged packets, and live search systems may not expose every permit or inspection record in the retrieved pass.<br>Company, trade, and local-press sources are retained as evidence but are not treated as a vote, permit, energization, occupancy, or live-service record without that record. | No qualifying HTTPS project-source URL carried forward; see the regional search ledger. |
| Nevada | 1 | 4 | 4 | qualifying projects found; Nevada Legislature, county action, state publication, and local queries | Company announcement does not publish a Denver permit, inspection, or CO number.<br>Operator page is not a governmental inspection or energization record. | [1](https://epubs.nsla.nv.gov/statepubs/epubs/62184-2024.pdf) [2](https://nevadacurrent.com/2026/06/18/las-vegas-data-center-expansion-approved-as-officials-ponder-need-for-future-regulations/) [3](https://www.clarkcountynv.gov/government/board_of_county_commissioners/county-meeting-agendas) +11 more in JSON |
| New Hampshire | 0 | 2 | 2 | FirstLight Bedford expansion; Nottingham proposal. | Local reporting; not a lease, land-use, building, air, water, or utility permit.<br>The cited page is a nonprofit/local analysis of state lease documents; the underlying final DNR disposition was not retrieved. | [1](https://www.bedfordnh.org/agendacenter) [2](https://www.bedfordnh.org/quicklinks.aspx?CID=35) [3](https://www.firstlight.net/firstlight-expands-bedford-nh-data-center/) +2 more in JSON |
| New Jersey | 0 | 4 | 4 | Nebius/DataOne Vineland; CoreWeave Kenilworth; QTS East Windsor; NJFX Wall AI hall. | Official SRBC docket is directly indexed; it is a water approval, not a building permit or energization approval.<br>The FERC case page summarizes the order and related appellate record; the docket record was not fully enumerated here. | [1](https://investors.coreweave.com/news/news-details/2025/CoreWeave-Reports-Strong-Second-Quarter-2025-Results) [2](https://kenilworthborough.com/AgendaCenter/ViewFile/Minutes/_09172025-259) [3](https://nebius.com/newsroom/nebius-accelerates-us-expansion-adding-up-to-300-mw-capacity-at-new-data-center-in-new-jersey) +15 more in JSON |
| New Mexico | 1 | 1 | 1 | one major qualifying project found | Company announcement does not publish a Denver permit, inspection, or CO number.<br>Operator page is not a governmental inspection or energization record. | [1](https://aqb-cpaur.env.nm.gov/) [2](https://kvia.com/news/top-stories/2026/04/14/dona-ana-county-commissioners-adopt-resolution-on-communication-about-project-jupiter/) [3](https://sourcenm.com/2026/07/16/new-mexico-land-commissioner-blocks-project-jupiter-related-pipeline-from-building-on-state-land/) +4 more in JSON |
| New York | 0 | 4 | 4 | Stream STAMP/Genesee; North East Data Niagara Falls; Niagara Digital Campus; TeraWulf Lake Mariner CB-5. | Official SRBC docket is directly indexed; it is a water approval, not a building permit or energization approval.<br>The FERC case page summarizes the order and related appellate record; the docket record was not fully enumerated here. | [1](https://cms3.revize.com/revize/niagarafallsny/Documents/Government/City%20Council/2025/0604/0%20-%20CORRECTED%20DRAFT%20AGENDA%20for%20REGULAR%20MTG%2006.04.25.pdf) [2](https://cms3.revize.com/revize/niagarafallsny/Documents/Government/Department/Planning_And_Environmental/PlanningBoard/2025/PB%20Packet%20FOR%20WEB%2020250409.pdf) [3](https://dec.ny.gov/news/environmental-notice-bulletin/2022-02-16/seqr/niagara-county-the-town-of-somerset-as-lead) +10 more in JSON |
| North Carolina | 1 | 4 | 4 | qualifying found | Notice is a construction-activity notice and does not publish the underlying permit number.<br>Agenda/staff request is not substituted for minutes or a vote tally. | [1](https://datacenters.google/locations/north-carolina/) [2](https://local.microsoft.com/blog/boyd-farms-datacenter-construction-update/) [3](https://spectrumlocalnews.com/nc/charlotte/news/2026/01/13/stokes-county-approves-rezoning-for-ai-data-center) +6 more in JSON |
| North Dakota | 2 | 4 | 4 | qualifying projects found | Company announcement; it does not establish a city/county approval, building permit, actual groundbreaking, or energized service.<br>Company infrastructure claim; no municipal, KDHE, EPA, or Evergy permit/interconnection closeout was retrieved. | [1](https://deq.nd.gov/PublicNotice.aspx) [2](https://www.commerce.nd.gov/power-partnerships/applied-digital-advancing-digital-infrastructure-north-dakota) [3](https://www.datacenterdynamics.com/en/news/applied-digital-completes-second-building-at-north-dakota-data-center-campus/) +7 more in JSON |
| Ohio | 3 | 10 | 10 | qualifying projects found | Official state page accessible; it does not publish a county/town vote tally or a building-by-building completion register.<br>IDEM PDF is public and searchable; the meeting is an agency permitting proceeding, not a local zoning vote. | [1](https://apnews.com/article/4667fa1442ec1c652228337ab4eb68ee) [2](https://columbusregion.com/press-release/cologix-expands-in-central-ohio/) [3](https://dam.assets.ohio.gov/image/upload/development.ohio.gov/about/taxcreditminutes/Meeting_Minutes_10.8.2025.pdf) +26 more in JSON |
| Oklahoma | 2 | 8 | 8 | qualifying projects found; state commerce, city packets, utility, company, and local queries | Official state page accessible; it does not expose the Port lease, parcel-level permit register, inspections, or energization record.<br>Non-government report; no associated Muskogee permit or utility filing was located. | [1](https://bealeinfra.com/beale-infrastructure-announces-new-data-center-campus-in-tulsa-county/) [2](https://bealeinfra.com/location/tulsa-county/) [3](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/oklahoma-energy-affordability-agreement/) +13 more in JSON |
| Oregon | 2 | 4 | 4 | Google The Dalles; AWS Boardman; CoreSite Hillsboro; STACK Hillsboro. | The official meeting record exposes the action summary but not a complete roll-call tally in the reviewed extract.<br>The city page says its list is updated monthly and may not reflect every current permit status; it is not a certificate-of-occupancy record. | [1](https://apnews.com/article/0f148f7d22c0ed054c18090adbbd233d) [2](https://datacenters.google/locations/oregon/) [3](https://hillsboro-or-us.avolvecloud.com/) +14 more in JSON |
| Pennsylvania | 3 | 6 | 6 | AWS Susquehanna and Fairless Hills; CoreWeave Lancaster; PAX-1; Homer City; TECfusions Keystone Connect. | Official SRBC docket is directly indexed; it is a water approval, not a building permit or energization approval.<br>The FERC case page summarizes the order and related appellate record; the docket record was not fully enumerated here. | [1](https://apnews.com/article/31f705d035069279b70fa27a5dc71596) [2](https://apnews.com/article/450534992fab8dd3527b64b92614259e) [3](https://coreweave.com/blog/building-pennsylvania-into-the-mid-atlantic-ai-hub) +24 more in JSON |
| Rhode Island | 0 | 1 | 1 | Hanton City/Revity Smithfield proposal, locally blocked; no construction verified. | Local reporting; not a lease, land-use, building, air, water, or utility permit.<br>The cited page is a nonprofit/local analysis of state lease documents; the underlying final DNR disposition was not retrieved. | [1](https://ecori.org/energy-intensive-data-center-proposed-for-woods-of-smithfield/) [2](https://www.oceanstatemedia.org/technology/proposed-data-center-still-looms-over-smithfield-even-after-town-council-enacts-ban) [3](https://www.smithfieldri.gov/Home/Components/News/News/472/57) +2 more in JSON |
| South Carolina | 2 | 4 | 4 | qualifying found | Notice is a construction-activity notice and does not publish the underlying permit number.<br>Agenda/staff request is not substituted for minutes or a vote tally. | [1](https://apnews.com/article/3ae6420a90b546e525b5f04ed6326453) [2](https://datacenters.google/locations/south-carolina/) [3](https://dms.psc.sc.gov/Attachments/Matter/0515fd97-b3e1-4f67-83ff-dde6a0f2dd38) +9 more in JSON |
| South Dakota | 0 | 3 | 3 | qualifying projects found | Company announcement; it does not establish a city/county approval, building permit, actual groundbreaking, or energized service.<br>Company infrastructure claim; no municipal, KDHE, EPA, or Evergy permit/interconnection closeout was retrieved. | [1](https://amv.siouxfalls.gov/OnBaseAgendaOnline/Documents/DownloadFileBytes/Planning_Commission_Meeting_4175_Agenda_Packet_12_3_2025_6_00_00_PM.pdf?documentType=5&isAttachment=True&meetingId=4175) [2](https://amv.siouxfalls.gov/OnBaseAgendaOnline/Meetings/ViewMeeting?doctype=2&id=4182) [3](https://ir.applieddigital.com/news-events/press-releases/detail/148/applied-digital-reports-fiscal-third-quarter-2026-results) +6 more in JSON |
| Tennessee | 2 | 2 | 2 | qualifying found | Company announcement is accessible; no linked city or county approval packet was identified.<br>State report is an economic-development record, not a city site-plan or building record. | [1](https://assessment.cot.tn.gov/TPAD/) [2](https://engage.zencity.io/mcminnville-tn/en-US/projects/high-impact-developments) [3](https://memphistn.gov/wp-content/uploads/2025/01/Committee-Agenda-July-9-2024-v2-Revised-782024-245-pm.pdf) +7 more in JSON |
| Texas | 17 | 17 | 17 | qualifying projects found; broad search included Texas Comptroller, TCEQ, governor, county/city, company, utility, and trade queries | Official county agenda; this is not minutes and does not prove approval.<br>The TCEQ technical-review record gives the received date; the linked public record is a review document, not a local vote. | [1](https://abilenetx.gov/2476/Tax-Abatements) [2](https://apnews.com/article/f4f74c3a4617d8cfab5b933fc31ccc6e) [3](https://blog.google/company-news/inside-google/company-announcements/google-american-innovation-texas/) +59 more in JSON |
| Utah | 3 | 11 | 11 | qualifying projects found; Utah government inventory and county/state records used | Official state page accessible; it does not expose the Port lease, parcel-level permit register, inspections, or energization record.<br>Non-government report; no associated Muskogee permit or utility filing was located. | [1](https://business.utah.gov/tax-credits/creekstone-energy-llc-commits-17-billion-to-millard-county-data-center-project/) [2](https://duchesne.utah.gov/wp-content/uploads/2026/03/Findings-Report-Nine-Mile-Data-LLC-040226.pdf) [3](https://duchesne.utah.gov/wp-content/uploads/2026/03/Nine-Mile-Data-Center-LLC-Data-Center_PublicNotice_040226.pdf) +15 more in JSON |
| Vermont | 0 | 0 | 0 | No large-scale project proposed or sited found; Vermont Public and VNRC explicitly report no AI/crypto or large-scale project. | Government portals, imaged packets, and live search systems may not expose every permit or inspection record in the retrieved pass.<br>Company, trade, and local-press sources are retained as evidence but are not treated as a vote, permit, energization, occupancy, or live-service record without that record. | No qualifying HTTPS project-source URL carried forward; see the regional search ledger. |
| Virginia | 3 | 5 | 5 | qualifying found | County summary is the accessible official record; the agenda packet is separately linked in the official Agenda Center.<br>County project page reports the action; a separate EDA minutes packet was not located. | [1](https://cardinalnews.org/2026/05/19/a-data-center-project-in-pittsylvania-was-approved-monday-with-higher-investment-and-jobs-than-previously-announced/) [2](https://corscale.com/press-releases/corscale-begins-construction-on-its-second-building-at-gainesville-crossing-campus/) [3](https://danvilleva.gov/calendar.aspx?CID=0&month=5&view=list&year=2026) +36 more in JSON |
| Washington | 1 | 5 | 5 | Microsoft MWH08 Quincy; Bitfarms Moses Lake; Wallula/Walla Walla; Seattle five-site approach cluster; Microsoft Malaga/East Wenatchee portfolio. | Official SRBC docket is directly indexed; it is a water approval, not a building permit or energization approval.<br>The FERC case page summarizes the order and related appellate record; the docket record was not fully enumerated here. | [1](https://apps.ecology.wa.gov/facilitysite/FacilitySite/FacilitySiteReport/100002672) [2](https://apps.ecology.wa.gov/paris/FacilitySummary.aspx?FacilityId=100002672) [3](https://apps.ecology.wa.gov/separ/Main/SEPA/Record.aspx?SEPANumber=202403581) +11 more in JSON |
| West Virginia | 1 | 2 | 2 | qualifying found | County summary is the accessible official record; the agenda packet is separately linked in the official Agenda Center.<br>County project page reports the action; a separate EDA minutes packet was not located. | [1](https://apnews.com/article/b33c051439bd3694ee3f2b04981f4555) [2](https://apps.dep.wv.gov/Documents/DAQ/NSRPermits/093-00034/Final/093-00034_PERM_13-3713%202025-08-15.pdf) [3](https://apps.dep.wv.gov/Documents/DAQ/NSRPermits/093-00034/Final/2026.02.05.%2025-02-AQB.%20Memorandum%20of%20Decision%20and%20Final%20Order.pdf) +10 more in JSON |
| Wisconsin | 2 | 6 | 6 | qualifying projects found | The primary accessible record is Alliant's official announcement rather than a City packet; no municipal vote sheet was located in the reviewed search.<br>Company/utility announcement; local approval details are not attached. | [1](https://blogs.microsoft.com/on-the-issues/2025/09/18/made-in-wisconsin-the-worlds-most-powerful-ai-datacenter/) [2](https://datacenters.atmeta.com/2025/11/hello-beaver-dam/) [3](https://dnr.wisconsin.gov/topic/EIA/Portwashington.html) +21 more in JSON |
| Wyoming | 2 | 4 | 4 | qualifying projects found; state business council, Microsoft, and trade queries | Company announcement does not publish a Denver permit, inspection, or CO number.<br>Operator page is not a governmental inspection or energization record. | [1](https://local.microsoft.com/blog/cheyenne-datacenter-update/) [2](https://news.microsoft.com/source/2026/04/14/microsoft-announces-intent-to-expand-datacenter-operations-in-cheyenne-accelerating-innovation-and-economic-growth/) [3](https://www.cheyennecity.org/Your-Government/Departments/Planning-and-Development-Department/Data-Centers) +6 more in JSON |
| District of Columbia | 0 | 0 | 0 | No new-build campus identified inside District boundaries. | Government portals, imaged packets, and live search systems may not expose every permit or inspection record in the retrieved pass.<br>Company, trade, and local-press sources are retained as evidence but are not treated as a vote, permit, energization, occupancy, or live-service record without that record. | No qualifying HTTPS project-source URL carried forward; see the regional search ledger. |

Zero-result jurisdictions in the supplied regional matrices are Connecticut, Delaware, District of Columbia, Florida, Nebraska, and Vermont. Their worker findings are preserved in the matrix and JSON. The six zeros are search outcomes, not exhaustive absence claims.

## Active construction scope versus baseline

The active U.S. scope is the 186-row Phase 2/3 canonical set. Existing operational facilities appear here only when the supplied evidence also describes an active expansion or phased build. Live-only facilities below are appendix-only and must never be placed on the Gantt.

### Baseline live facilities with no active expansion

| ID | Facility / service record | Status | Scope treatment |
|---|---|---|---|
| my-kulai-oci-west2 | OCI Malaysia West 2 (Kulai) | live_service | Live/service record or hosted deployment; no active U.S. construction row and no Gantt entry. |
| id-batam-oci-north | OCI Indonesia North (Batam) | live_service_hosted_physical_status_partial | Live/service record or hosted deployment; no active U.S. construction row and no Gantt entry. |
| sg-singapore-west2 | OCI Singapore West 2 | live_service | Live/service record or hosted deployment; no active U.S. construction row and no Gantt entry. |
| es-madrid3 | OCI Madrid 3 | live_service_hosted | Live/service record or hosted deployment; no active U.S. construction row and no Gantt entry. |
| it-turin | OCI Turin | live_service_hosted | Live/service record or hosted deployment; no active U.S. construction row and no Gantt entry. |
| ma-casablanca-settat | Oracle Morocco cloud expansion: Casablanca and Settat | casablanca_live_settat_planned | Casablanca live-service component is baseline-only; Settat is a separate planned component without site evidence. Neither is a U.S. construction row or Gantt entry. |
| sa-riyadh-neom | Oracle Saudi Arabia expansion: Riyadh live component / NEOM planned component | Riyadh live; NEOM planned | Riyadh live-service component is baseline-only; NEOM is a separate plan without site/construction evidence. Neither is a U.S. construction row or Gantt entry. |
| ORCL-BR-NETSUITE-VINHEDO-SP | Oracle NetSuite Brazil customer data-center deployment | Announced as inaugurated/operational by Vinhedo municipal government; not proven greenfield construction. Included as a named customer-driven regional deployment with low-to-medium physical-build confidence. | Operational/customer deployment comparison record; greenfield construction not proven; no Gantt entry. |

Named ordinary/existing context supplied by the comparison artifact: Singapore East, Jeddah, Madrid 1, Milan, Tokyo, Osaka, London, Newport, Frankfurt, Amsterdam, ordinary U.S. OCI regions. **This is not an exhaustive legacy-facility count.** Ordinary U.S. OCI regions remain an aggregate label because no site-by-site legacy inventory was supplied.

## Excluded, duplicate, non-U.S., and comparison-only material

The seed-only list has 60 IDs. These are not silently declared nonexistent; they are discovery IDs that did not survive as the same canonical ID in the regional register. They are not additive to the validated count.

### Seed-only discovery IDs (not additive)

- US-AL-META-MONTGOMERY-2024 (AL): Meta Montgomery Data Center
- US-AZ-EDGECORE-MESA-EXPANSION-2024 (AZ): EdgeCore Mesa data-center campus expansion
- US-GA-QTS-FAYETTEVILLE-2025 (GA): QTS Fayetteville data-center campus
- US-GA-PROJECT-SAIL-COWETA-2025 (GA): Project Sail data-center campus
- US-IL-CYRUSONE-AURORA-2024 (IL): CyrusOne Aurora data center
- US-IL-YORKVILLE-TRACT-2024 (IL): Yorkville data-center campus
- US-IN-AWS-NEW-CARLISLE-2024 (IN): AWS New Carlisle / Project Rainier campus
- US-IN-AWS-NORTHERN-INDIANA-2026 (IN): AWS Northern Indiana AI/cloud campuses
- US-IN-GOOGLE-FORT-WAYNE-2024 (IN): Google Fort Wayne data center
- US-IN-GOOGLE-MICHIGAN-CITY-2026 (IN): Google Michigan City data center
- US-IN-GOOGLE-MORGAN-2025 (IN): Google Morgan County data center
- US-IN-META-JEFFERSONVILLE-2024 (IN): Meta Jeffersonville data center
- US-IN-META-LEBANON-2026 (IN): Meta Lebanon AI data-center campus
- US-IA-MICROSOFT-WEST-DES-MOINES-OSMIUM-2024 (IA): Microsoft Project Osmium data center
- US-IA-SNA-CEDAR-RAPIDS-2024 (IA): SNA Data Center Cedar Rapids phases
- US-KS-PROJECT-KESTREL-KANSAS-CITY-2026 (KS): Project Kestrel data-center campus
- US-LA-META-HYPERION-RICHLAND-2024 (LA): Meta Richland Parish / Hyperion AI campus
- US-MD-QUANTUM-LOOPHOLE-FREDERICK-2025 (MD): Quantum Loophole Frederick campus
- US-MI-STARGATE-SALINE-2025 (MI): Stargate Michigan / Related Digital Saline Township campus
- US-MN-META-ROSEMOUNT-2024 (MN): Meta Rosemount data center
- US-MN-PROJECT-COSMO-EAGAN-2024 (MN): Project Cosmo data center
- US-MS-AWS-MADISON-2024 (MS): AWS Madison County campuses
- US-MS-AWS-WARREN-2025 (MS): AWS Warren County next-generation campus
- US-MS-AWS-HINDS-2026 (MS): AWS Hinds County / former Delphi campus conversion
- US-MS-XAI-COLOSSUS-MEMPHIS-2025 (TN): xAI Colossus Memphis/Southaven expansion
- US-NV-COREWEAVE-LAS-VEGAS-2025 (NV): CoreWeave Las Vegas AI campus
- US-NC-META-CATAWBA-2024 (NC): Meta Catawba County data-center expansion
- US-ND-APPLIED-DIGITAL-ELLENDALE-2024 (ND): Applied Digital Ellendale AI data center
- US-ND-APPLIED-DIGITAL-POLARIS-2024 (ND): Applied Digital Polaris Forge campus
- US-OH-META-PROMETHEUS-NEW-ALBANY-2025 (OH): Meta Prometheus New Albany AI campus
- US-OH-VANTAGE-NEW-ALBANY-2024 (OH): Vantage New Albany data-center campus
- US-OH-SB-ENERGY-PORTS-PIKETON-2025 (OH): SB Energy PORTS Technology Campus
- US-OK-CORE-SCIENTIFIC-MUSKOGEE-2025 (OK): Core Scientific Port Muskogee HPC data center
- US-PA-HOMER-CITY-AI-2025 (PA): Homer City Energy + AI campus
- US-PA-AWS-SALEM-NUCLEAR-2025 (PA): AWS Salem Township nuclear campus
- US-PA-NEBIUS-GIGAWATT-2026 (PA): Nebius Pennsylvania gigawatt-scale campus
- US-SC-GOOGLE-DAWSON-RIDGEVILLE-2024 (SC): Google Project Dawson
- US-SC-META-AIKEN-2024 (SC): Meta Aiken County data center
- US-TN-XAI-COLOSSUS-MEMPHIS-2024 (TN): xAI Colossus original Memphis facility
- US-TX-STARGATE-ABILENE-2025 (TX): Stargate I Abilene AI campus
- US-TX-GOOGLE-TEXAS-ARMSTRONG-HASKELL-ELLIS-2025 (TX): Google Texas cloud and AI infrastructure expansion
- US-TX-GOOGLE-MEITNER-2026 (TX): Google/Intersect Meitner Energy Center
- US-TX-META-EL-PASO-2025 (TX): Meta El Paso AI/data-center campus
- US-TX-FERMI-MATADOR-AMARILLO-2025 (TX): Fermi America Project Matador HyperGrid
- US-TX-COREWEAVE-PLANO-2025 (TX): CoreWeave Plano AI data center
- US-TX-QTS-FORT-WORTH-2024 (TX): QTS Fort Worth data center
- US-TX-KDC-IRVING-2024 (TX): KDC Irving data-center campus
- US-TX-POWERHOUSE-IRVING-2024 (TX): PowerHouse Irving data center
- US-UT-JOULE-HOLDEN-2026 (UT): Joule Energy and Data Center Campus
- US-UT-DELTA-GIGASITE-2026 (UT): Delta Gigasite data-center campus
- US-VA-GOOGLE-NOVA-EXPANSION-2024 (VA): Google Virginia data-center campus expansion
- US-VA-DULLES-DIGITAL-BUILDINGS-2024 (VA): Dulles Digital Data Center Buildings 6 and 8
- US-VA-CONVERGENT-REMINGTON-2024 (VA): Convergent Technology Park
- US-WA-WALLA-WALLA-CAMPUS-2024 (WA): Walla Walla 16-building data-center campus
- US-WV-MONARCH-Nscale-MICROSOFT-2026 (WV): Monarch Compute Campus / Nscale-Microsoft
- US-WI-MICROSOFT-MOUNT-PLEASANT-2024 (WI): Microsoft Mount Pleasant Fairwater campus
- US-WI-STARGATE-PORT-WASHINGTON-2025 (WI): Stargate Port Washington / Vantage Wisconsin campus
- US-WY-GOOGLE-TEMBO-CHEYENNE-2025 (WY): Google Project Tembo
- US-IN-MICROSOFT-LAPORTE-2024 (IN): Microsoft Radius Industrial Park data center
- US-TX-MICROSOFT-SAT82-CASTROVILLE-2024 (TX): Microsoft SAT82 data center

### Comparison crosswalks (no extra U.S. rows)

- ORCL-US-TX-ABILENE-FLAGSHIP → US-TX-ABILENE-LANCIUM-STARGATE-2024 — active all-company row; no extra row.
- ORCL-US-TX-SHACKELFORD-FRONTIER → US-TX-STARGATE-FRONTIER-SHACKELFORD-2025 — active all-company row; no extra row.
- ORCL-US-NM-DONA_ANA-JUPITER → US-NM-STARGATE-JUPITER-SANTA-TERESA-2025 — active all-company row; no extra row.
- ORCL-US-MI-SALINE-THE-BARN → MI-SALINE-BARN-STARGATE — active all-company row; no extra row.
- ORCL-US-WI-PORT-WASHINGTON-Lighthouse → WI-PORT-WASHINGTON-VANTAGE-LIGHTHOUSE — active all-company row; no extra row.
- ORCL-US-TX-MILAM-FREEBIRD → US-TX-STARGATE-MILAM-2025 — active all-company row; no extra row.
- ORCL-US-OH-LORDSTOWN-STARGATE → OH-LORDSTOWN-STARGATE — active all-company row; no extra row.
- county/vote abilene_taylor_tx_lancium_project_radiance → US-TX-ABILENE-LANCIUM-STARGATE-2024 — County/vote comparison record; no additional row.
- county/vote shackelford_tx_vantage_frontier → US-TX-STARGATE-FRONTIER-SHACKELFORD-2025 — County/vote comparison record; no additional row.
- county/vote dona_ana_nm_project_jupiter → US-NM-STARGATE-JUPITER-SANTA-TERESA-2025 — County/vote comparison record; no additional row.
- county/vote saline_mi_the_barn → MI-SALINE-BARN-STARGATE — County/vote comparison record; no additional row.
- county/vote port_washington_wi_vantage_lighthouse → WI-PORT-WASHINGTON-VANTAGE-LIGHTHOUSE — County/vote comparison record; no additional row.

Lordstown and Milam are excluded from the Oracle-specific county-vote comparison’s Oracle-developed subset, but remain in the all-company U.S. count because the governing scope includes SoftBank/OpenAI and all companies.

### Non-U.S. and other comparison-only material

The international/non-Stargate records, OCI Kenya without site evidence, ordinary existing OCI labels, and adjacent unattributed SB Energy leads are comparison material only. They are not U.S. construction rows. The supplied U.S. comparison artifacts also contribute no comparison-only project to the Phase 2 construction count.

**global_inventory_non_us_or_service_only:**
- ORCL-UAE-ABUDHABI-STARGATE-UAE — Non-U.S. or service-only comparison record; not in U.S. construction count.
- ORCL-SG-SINGAPORE-OCI-REGION-2 — Non-U.S. or service-only comparison record; not in U.S. construction count.
- ORCL-SAUDI-RIYADH-OCI-REGION — Non-U.S. or service-only comparison record; not in U.S. construction count.
- ORCL-ID-BATAM-INDONESIA-NORTH — Non-U.S. or service-only comparison record; not in U.S. construction count.
- ORCL-BR-NETSUITE-VINHEDO-SP — Non-U.S. or service-only comparison record; not in U.S. construction count.

**international_and_nonstargate_non_us:**
- my-kulai-oci-west2 — Non-U.S./international comparison material; excluded from the U.S. construction count.
- id-batam-oci-north — Non-U.S./international comparison material; excluded from the U.S. construction count.
- sg-singapore-west2 — Non-U.S./international comparison material; excluded from the U.S. construction count.
- sa-riyadh-neom — Non-U.S./international comparison material; excluded from the U.S. construction count.
- es-madrid3 — Non-U.S./international comparison material; excluded from the U.S. construction count.
- it-turin — Non-U.S./international comparison material; excluded from the U.S. construction count.
- ma-casablanca-settat — Non-U.S./international comparison material; excluded from the U.S. construction count.
- jp-program-alloy — Non-U.S./international comparison material; excluded from the U.S. construction count.
- uk-de-expansion-programs — Non-U.S./international comparison material; excluded from the U.S. construction count.
- ae-abu-dhabi-stargate-oci — Non-U.S./international comparison material; excluded from the U.S. construction count.

**ordinary_existing_live_regions:**
- Singapore East
- Jeddah
- Madrid 1
- Milan
- Tokyo
- Osaka
- London
- Newport
- Frankfurt
- Amsterdam
- ordinary U.S. OCI regions

**upcoming_without_site_evidence:**
- OCI Kenya — available_soon_undated

**adjacent_unattributed_leads:**
- SB Energy Borden County Data Center Campus — 1 GW+ and early construction reported without Oracle/OpenAI/OCI attribution.
- SB Energy PORTS Technology Campus — Up to 10 GW reported without Oracle/OpenAI/OCI attribution.

**oracle_comparison_exclusions:**
- Lordstown, Ohio — OpenAI identifies it as developed through SoftBank/OpenAI, not Oracle-developed.
- Milam County, Texas — OpenAI identifies it as developed through SoftBank/OpenAI, not Oracle-developed.
- Other non-Stargate Oracle U.S. capacity — No separately named new-build or major expansion with a public site-specific local-government trail was found in the stated searches; generic OCI-region and unnamed colocation references were excluded rather than inferred into sites.

## Announced proposals lacking siting evidence

This is a deterministic evidence-gap subset of Phase 2 rows: status signals an announcement/proposal/planning stage while the record also contains an unresolved or absent site-specific permit, approval, construction, or comparable siting trail. These remain in the public-identifiable scope as proposals, not as verified construction.
- AL-001 — Core Scientific Auburn HPC facility (AL): announced/early development; no building permit, energization, or service record located
- AL-002 — Google Jackson County data-center expansion (AL): announced major expansion; permit, construction and energization not verified
- AR-001 — AVAIO Digital Leo (AR): announced/utility-contracted; physical construction not validated
- GA-006 — Pine Ridge Tech Park (GA): rezoned/proposed; no permit or construction record located
- GA-007 — Microsoft Tyrone data center (GA): announced/proposed; approvals and construction not verified
- MS-002 — AVAIO East Metropolitan Center (MS): announced/early development; construction not validated
- SC-001 — Meta Aiken County data center (SC): announced/under development; construction not verified
- SC-003 — Cielo Cherokee County project (SC): selected/announced; no permit or groundbreaking found
- VA-003 — Danville–Pittsylvania regional data-center development (VA): approved early development; site/tenant/building program unresolved
- VA-005 — Powhatan County data-center campus (VA): approved/early development; no permit or construction evidence located
- WV-001 — Google Putnam County high-impact data center (WV): early approved/high-impact proposal; no construction evidence
- WV-002 — Fundamental Data high-impact Tucker–Grant campus (WV): proposed/air-review; no construction verified; local control constrained by WV high-impact law
- IL-MORRIS-TRACT-TECHPARK — — (IL): announced/entitled; no construction or permit evidence located
- IN-MORGAN-GOOGLE — — (IN): announced/early site development; city and permit not pinned
- IN-PLAINFIELD-RADIUS-INDY1 — — (IN): announced/pre-construction; construction date and permits not found
- MO-NEW-FLORENCE-GOOGLE-SPADE — — (MO): announced/planned; no permit or construction evidence located
- MN-PINE-ISLAND-GOOGLE — — (MN): announced/locally processed; construction halted by court order; not energized
- WI-RACINE-MICROSOFT-FAIRWATER2 — — (WI): announced/planned expansion; site-specific construction not independently verified
- OH-FAYETTE-AWS — — (OH): announced/planned; construction start not verified in this pass
- OH-PORTS-PIKE-SBENERGY — — (OH): federal/private announced; pre-construction/permit pathway unresolved
- OH-LORDSTOWN-STARGATE — — (OH): announced/claimed groundbreaking; current construction/live status unresolved
- OH-VAN-WERT-QTS — — (OH): discovery lead only; not validated as approved or under construction
- ND-HARWOOD-UNNAMED-AI — — (ND): announced/early-stage; company, permit and construction not confirmed
- ND-HANOVER-APPLIED-OLIVER — — (ND): county agreement/early development; construction not verified
- SD-RAPID-CITY-SEQUITOR — — (SD): announced/permit stage; no construction or energization found
- US-TX-STARGATE-FRONTIER-SHACKELFORD-2025 — Stargate Frontier / Vantage Shackelford County campus (TX): Announced/under development; construction status remains provisional because the surviving public source is a tracker/aggregate attribution.
- US-TX-STARGATE-MILAM-2025 — Stargate Milam County campus (TX): Announced/provisional; no verified physical start.
- US-TX-GOOGLE-MEITNER-GRAY-ROBERTS-2026 — Google/Intersect Meitner Energy Center (TX): Announced/under development; site/building and approval record not verified.
- US-TX-MICROSOFT-PECOS-2026 — Microsoft Pecos AI/cloud data-center campus (TX): Announced/planned; construction and local approvals not established in the announcement.
- US-OK-BEALE-MUSTANG-CLAREMORE-2026 — Beale Project Mustang (OK): Proposed; public hearing/project-plan stage, not verified approved or under construction.
- US-OK-ANTHEM-TULSA-2024 — Anthem Data Centers Tulsa (OK): Provisional planned project; no primary record found.
- US-AZ-BEALE-MARANA-2025 — Beale Marana data-center campus (AZ): Planned/under development; local approval path unresolved.
- US-AZ-TRACT-YUMA-2024 — Tract Yuma data center (AZ): Provisional planned lead; no primary record found.
- US-UT-NINE-MILE-UINTA-2026 — Nine Mile / Uinta Basin data center (UT): Approved/proposed; construction not verified.
- US-NV-COPIA-MONARCH-YERINGTON-2025 — Copia Power Monarch Data Campus (NV): Planned/proposed; no construction verification found.
- US-ID-DIODE-GEMSTONE-KUNA-2025 — Gemstone Technology Park (ID): Locally approved/re-zoned; early development, construction not verified.
- US-WY-MICROSOFT-CHEYENNE-2026 — Microsoft Cheyenne datacenter expansion (WY): Announced/planned; no construction evidence found.
- US-AK-STAK-NORTH-SLOPE-2026 — STAK Energy Campus (AK): proposed/lease review; construction not verified
- US-ME-SCARBOROUGH-TECH-PARK-2026 — Scarborough Technology Park data-center proposal (ME): early proposal/incomplete; no construction
- US-MA-SERVISTAR-WESTFIELD-2021 — Servistar Westfield data-center campus (MA): proposed/under development; construction not verified
- US-NH-FIRSTLIGHT-BEDFORD-2026 — FirstLight Bedford data-center expansion (NH): announced expansion; construction not verified
- US-NH-NOTTINGHAM-PROPOSAL-2026 — Nottingham Route 4 data-center proposal (NH): proposal only; no approval or construction
- US-NJ-QTS-EAST-WINDSOR-2026 — QTS East Windsor second data-center building (NJ): proposed/approval unresolved
- US-NY-STREAM-STAMP-2025 — Stream Data Centers Western New York/STAMP (NY): proposed/under regulatory review; construction pause/funding reports conflict
- US-NY-NFR-NIAGARA-DIGITAL-CAMPUS-2024 — Niagara Falls Redevelopment Niagara Digital Campus (NY): proposed/approval pathway
- US-PA-AWS-FAIRLESS-HILLS-2025 — AWS Falls Township/Keystone Trade Center campus (PA): announced/planned; site-level construction not verified
- US-PA-COREWEAVE-LANCASTER-2025 — CoreWeave Lancaster AI data center (PA): announced/under development; construction start not verified
- US-PA-HOMER-CITY-2025 — Homer City AI/HPC campus (PA): announced/early development; construction not independently verified
- US-PA-TECFUSIONS-KEYSTONE-CONNECT-2025 — TECfusions Keystone Connect (PA): announced/adaptive reuse; construction/customer not verified
- US-RI-REVITY-HANTON-CITY-SMITHFIELD-2026 — Hanton City Business Park / Revity data-center concept (RI): proposed/locally blocked; construction not verified
- US-WA-BITFARMS-MOSES-LAKE-2026 — Bitfarms Moses Lake cryptomine-to-AI data-center conversion (WA): proposed/conversion construction; permit disposition unresolved
- US-WA-ADVANCE-PHASE-WALLULA-2024 — Wallula Gap/Walla Walla data-center campus (WA): proposal/land acquired; permits/construction not verified
- US-WA-SEATTLE-CITY-LIGHT-5-SITES-2026 — Seattle large-load data-center approach cluster (WA): proposals/withdrawals/moratorium; no construction

## Company and region coverage

Category counts below are multi-label project-row signals over the 186 canonical Phase 2 rows; they do not sum to 186.

| Coverage class | Project-row signal count | Rule | Named coverage |
|---|---:|---|---|
| Hyperscalers | 64 | case-insensitive text match for Google, Microsoft, Amazon, AWS, or Meta in the structured project record. | Google/Alphabet/Google Cloud, Microsoft/Azure, Amazon/AWS, Meta |
| AI labs | 10 | case-insensitive text match for OpenAI, xAI, or SpaceXAI. | OpenAI, xAI/SpaceXAI |
| Cloud / colo / developers | 186 | at least one non-empty owner/developer/operator/company role field in the structured project record. | QTS, Core Scientific, Vantage, STACK, CoreWeave, CoreSite, Compass Datacenters, Applied Digital, Beale Infrastructure, Tract, Novva, EdgeCore, Prime, CyrusOne, Switch, Cologix, Nebius, DataBank/colo and specialist developers as named in project rows |
| Utilities / enterprise | 84 (utility/power 53; customer/tenant 61) | at least one non-empty utility/power or customer/tenant/enterprise field; overlap is allowed. | TVA, Entergy, Georgia Power, Duke Energy, AEP/AES Ohio, Xcel, DTE, WE Energies, Black Hills Energy, BPA, PPL, Talen, MLGW and other named utility/host/customer partners |

The coverage spans hyperscalers (Google/Alphabet, Microsoft/Azure, Amazon/AWS, Meta), AI labs (OpenAI, xAI/SpaceXAI), cloud/colo/developers (including QTS, Core Scientific, Vantage, STACK, CoreWeave, CoreSite, Applied Digital, Beale, Tract, Novva, EdgeCore, Prime, CyrusOne, Switch, Cologix, Nebius and others), and utilities/enterprise/customer partners. The counts are evidence-field signals, not a market-share estimate.

## Input artifact hashes

Hashes are SHA-256 over the exact supplied input bytes read for this appendix. The JSON contains the same inventory with byte sizes.

| Input | Bytes | SHA-256 |
|---|---:|---|
| research_brief.md | 4130 | 1e5770c3a072026eef7ad9ed03fb2a8d96228c68c105d74f99b9ef56b88bdac3 |
| phase2/national_all_company_seed.json | 93144 | 30d34a113377ff80bfb5a55d1299420b9e6dd74f7b782c808c6c028fdf37a699 |
| phase2/national_all_company_seed.md | 7315 | bcd7c2a38092da547a02d9540409ac506a8f723d1f564942e2c44c7738a6bf38 |
| phase2/region_midatlantic_southeast.json | 61537 | 860d7f0767153f5cf8db10959615a73694ba0c07bea3084e3255f66646be10d5 |
| phase2/region_midwest_greatlakes.json | 105757 | 2dfb0467930a8c9cfdb1b79a70577cc1b429ac6935b72d2a62da7b719ee53213 |
| phase2/region_southwest_mountain.json | 94492 | dc542cc2f57000c502c45ecf22d77d687e0e710823f552a3239aad3b6ef3e760 |
| phase2/region_west_northeast_remaining.json | 72780 | d30fb209cd2b94629ab558779a225bbe79fa5ea60e8e687a7dfea8ae4c8cf761 |
| phase2/region_midatlantic_southeast.md | 22468 | 27ee266672fee3ded01e9525be732fe748e9c9801670025a666abdf1c63a4739 |
| phase2/region_midwest_greatlakes.md | 95493 | fe814152f9c9e581d5be7b31869501f53aa87cd5c8fd186b157b86a6b406e309 |
| phase2/region_southwest_mountain.md | 16049 | b40610e44f0b382d18344e08cacb5a8fbd34e8a660be16523d2a223f64d5369c |
| phase2/region_west_northeast_remaining.md | 27674 | 75baf65cfc5e5fc6f2977f977094dd311fb81231148e42bdfd065c3544ce58b3 |
| phase3/county_ak_hi_me_ma_nh_ri.json | 54124 | 6176a047977262d2757d81ff2f1b19e4a487621809bd625a5c9affe8f52b8252 |
| phase3/county_ca_or.json | 57114 | fe2871511350314fc6def703a4dcfb0781525253e99993206673f60edd1b1257 |
| phase3/county_co_id_mt_nv_nm_wy.json | 78052 | 80e8fe8fe4a263e4f039d18e89fcb2b43ad692026fff14294df99b90edee3062 |
| phase3/county_ga_nc_sc.json | 62371 | a3ec5aa7247580c397759f16b740ce81841350d3b640e81feef503625741aac9 |
| phase3/county_ia_il_mi_wi.json | 64403 | 717bc9940df202f270e9c0fa0c32f448d962b772d39f348360a741ddcc84fe0d |
| phase3/county_ks_mn_mo_nd_sd.json | 93488 | 82d517cf404f8afec1a3a5d9f3e41720b8b9bd6bc8d264ef1a4ba8f7376480bf |
| phase3/county_ms_al_la_ar_tn_ky.json | 55962 | 0bd7d74de0673dc5b5af0e64821bdee1ad5ae8d97dbe876582107b6c6d6b8962 |
| phase3/county_oh_in.json | 55764 | 408cb9aef20a0fc637bec7c4b5f25badc1c171e36d818b164af2f93b85e03256 |
| phase3/county_ok_az_ut.json | 89443 | 86dacb6b374387c6efa95a02f295163300c5298a50d2dd0ee0947d1b840f2329 |
| phase3/county_pa_nj_ny_wa.json | 68946 | 4ed724673394fb9b66cfdb913449c8b64a3e2dac3a61029214a8c1d1fbdf42d0 |
| phase3/county_tx.json | 50975 | 1752d2751d0777649002dcb98a24b153de1ea826afc6a469bd9cdc3ce1d018fe |
| phase3/county_va_md_wv.json | 59359 | d0411dcdb39a06773cccceca146bc311700ed6cde2d00bc20c05ea51969186bd |
| phase3/county_ak_hi_me_ma_nh_ri.md | 45394 | 358c58382c8f00ed6ee820d3895f3c8ec3b228f26beb0b48c918c0d69fff3178 |
| phase3/county_ca_or.md | 35983 | 63d93dd102bdaa7519828d287df4b35079fbfb9fc4ecd5848ddbaf3d49df697e |
| phase3/county_co_id_mt_nv_nm_wy.md | 66121 | 3699086fe1925d491215e4c92cdc8a2d4c493d14e8614ba3306a572bf4afc9cd |
| phase3/county_ga_nc_sc.md | 26832 | ac4c1277f3f2fba7129382d44a63dde293736ba11fe2012b5e950553c5e20619 |
| phase3/county_ia_il_mi_wi.md | 43512 | 51f53c508e210aa1b9f505ba525cea93f326fe5cb58952c0dfc44eabe601e1b9 |
| phase3/county_ks_mn_mo_nd_sd.md | 78790 | d9300ab4887a9705020901c7a08d7f8f666fb09feb31deec5c96293e7ee76c50 |
| phase3/county_ms_al_la_ar_tn_ky.md | 28693 | 702a67ac87571455e1f2419c8619f118fdc5c14810f9911ea8893e97427ea2f1 |
| phase3/county_oh_in.md | 32692 | 4e3712fb7c34c436a0df858d578200907f0f5aff5a1f0e651df561e8b4399178 |
| phase3/county_ok_az_ut.md | 67004 | 5076d2c23ddc4c9bb95d0186c1d34d9a46231ba6a6b4de86cb4b58962379e759 |
| phase3/county_pa_nj_ny_wa.md | 66248 | af076e3aa2a8ba7aae81221f0be7e95b4364a064ec157beb33c0c44d63598e15 |
| phase3/county_tx.md | 26974 | 8f318ee95764a7a11941d378684d069c3bbc7439a188ecfe4f745255a066160f |
| phase3/county_va_md_wv.md | 34753 | 5501346bf28eeaf972d730704079b3f322b252141d06d460354cb79c053af873 |
| phase1/global_site_inventory.json | 52901 | 5ec71ec88265e62c3b235ecad7efcd6af462ecf6b2ad030775cefe46ce47557b |
| us_county_vote_map.json | 29750 | ae1dfd57114af450e11cc0dd87db75b4e1abd2100ef4362ed7cb10f9eceef77f |
| phase1/international_and_nonstargate.json | 63693 | bab0bad98ff23aea240a6be733f01249566f89f6d57c0226dd15319808ce28a3 |

No new web research was used: every jurisdiction had a supplied regional coverage field. No deletion, cleanup, Git/config/runtime mutation, or external contact was performed.

