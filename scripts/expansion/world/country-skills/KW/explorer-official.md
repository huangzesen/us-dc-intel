# KW Explorer Official - Kuwait Datacenter Official/Regulatory Enumeration

Date: 2026-08-12. Scope: State of Kuwait (KW). Repo divisions: Capital; Hawalli; Farwaniya; Ahmadi; Jahra; Mubarak Al-Kabeer. Kuwait has six governorates; use these repo division names in records and keep Arabic/local aliases in notes: Capital / Al Asimah (العاصمة), Hawalli (حولي), Farwaniya / Al Farwaniyah (الفروانية), Ahmadi / Al Ahmadi (الأحمدي), Jahra / Al Jahra (الجهراء), Mubarak Al-Kabeer (مبارك الكبير).

This file is final-review methodology, not a results file. It records verified official and primary-source routes for finding Kuwait data centers, cloud regions, ICT tenders, permits, power leads, and negative sweeps. Do not count a candidate as a physical data center unless the cited source supports a facility, location, and status.

Reliability grades: **A** = official government/regulator/utility/cloud-vendor/operator or operator-investor primary source, but only for the fact directly stated; **B** = established trade press or local press that names a facility, agreement, or status; **C** = aggregators, market reports, directories, social posts, and syndicated PR leads; **U** = claim without a working source. A cloud-vendor announcement is A for intent, not A for an operating region. A directory listing is C even if plausible. A "Tier III-designed" claim is not an Uptime certification.

## 0. Kuwait-Specific Rules

- Kuwait has no public national data-center registry. CITRA regulates telecom/ICT licensing and services, but its public services menu does not expose a data-center register. Kuwait Municipality is the building-permit route; MEW is the electricity/power route; CAPT and e.gov.kw are procurement routes.
- Commercial data-center evidence is concentrated in Kuwait City/Capital and telecom-linked platforms. Treat claims outside Capital as either Syntys/Ooredoo leads, enterprise/government sites, or negative sweeps until a primary source names a facility.
- Hyperscaler announcements remain **planned_or_mou** until an official locations list or operator/government launch/construction source says otherwise. As verified on 2026-08-12, Azure, Google Cloud, AWS, and Oracle official region/location pages had no Kuwait match.
- Syntys is now a major primary-source route. Syntys says it was spun out from Ooredoo in March 2025; Iron Mountain says the Syntys joint venture has Kuwait locations in Kuwait City and Shuaiba; an Ooredoo-hosted Syntys deck lists Kuwait with 2 active data centers and about 2.2 MW active IT load plus 2 MW current capacity in a Kuwait market-position slide. Use this as A for Syntys/Ooredoo platform presence and country-level capacity context, but do not infer exact per-site MW without a site-level source.
- ix.kw and cable landing stations are connectivity evidence, not colocation evidence unless the same source explicitly states data-center service at the site.
- Arabic search is mandatory. Use Arabic data-center terms plus stage verbs: افتتاح, تدشين, إطلاق, وضع حجر الأساس, تخصيص أرض, دخل الخدمة.

## 1. Verified Official / Primary Source Ledger

| Source | URL | Use | Grade |
|---|---|---|---|
| CITRA home | https://www.citra.gov.kw/sites/En/Pages/Home.aspx | Regulator surface; services include ISP & SubISP, Licensing, Tenders, .kw domains; news includes Huawei digital-transformation MoU dated 13 Jul 2026 | A for regulator scope and news surface |
| CITRA IXP launch | https://citra.gov.kw/sites/en/Pages/NewsDetails.aspx?NewsID=68 | CITRA announced ix.kw on 20 Oct 2019 as carrier-neutral IXP connecting local networks/content providers | A for IXP launch and role |
| ix.kw about | https://ix.kw/about.html | Not-for-profit neutral Internet Exchange Point; contact at CITRA / TEC Building | A for IXP identity/location contact; connectivity_only |
| CITRA Data Privacy Protection Regulation | https://www.citra.gov.kw/sites/en/LegalReferences/Resolution-No-42-On-Data-Privacy-Protection-Regulation.pdf | Privacy regulation for telecom/ICT service-provider due diligence | A for regulation text |
| Microsoft Kuwait Azure intent | https://news.microsoft.com/en-xm/2025/03/06/microsoft-strengthens-partnership-with-kuwait-government-announces-intent-to-establish-ai-powered-azure-region-to-accelerate-ai-transformation-and-drive-economic-growth/ | Microsoft, CAIT, and CITRA partnership; intent to establish AI-powered Azure Region; no site/timeline | A for intent only |
| Azure regions list | https://learn.microsoft.com/en-us/azure/reliability/regions-list | Operational Azure region check; no Kuwait match on 2026-08-12 | A for absence/presence at check time |
| Google Cloud locations | https://cloud.google.com/about/locations | Operational Google Cloud region/zone check; no Kuwait match on 2026-08-12 | A for absence/presence at check time |
| AWS regions/AZs | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | AWS region check; no Kuwait match on 2026-08-12 | A for absence/presence at check time |
| Oracle cloud regions | https://www.oracle.com/cloud/data-regions.html | OCI region check; redirected to distributed-cloud availability page; no Kuwait match on 2026-08-12 | A for absence/presence at check time |
| Syntys launch | https://syntys.com/newsroom/syntys-enters-mena-market-poised-to-lead-digital-infrastructure-growth | Syntys launched March 2025, spun out from Ooredoo, specialized in data-center design/construction/management, assets across five markets | A for Syntys corporate/platform facts |
| Iron Mountain Syntys JV | https://www.ironmountain.com/data-centers/locations/syntys-data-center | Iron Mountain minority stake/JV; Syntys locations include Kuwait: Kuwait City and Shuaiba; services include colocation, AI deployment, carrier-neutral connectivity, Tier III data-center designs | A for JV and named location list |
| Ooredoo-hosted Syntys data-centres deck | https://www.ooredoo.com/wp-content/uploads/2025/11/Data-centres_Syntys.pdf | 26 active data centers across platform, 29.6 MW IT capacity; Kuwait shown as 2 active DCs / about 2.2 MW active IT load and 2 MW current capacity | A for Ooredoo/Syntys deck; country-level, not per-site |
| Ooredoo Group NVIDIA collaboration | https://www.ooredoo.com/en/media/news_view/ooredoo-group-pioneers-ai-revolution-in-mena-region-with-nvidia-collaboration/ | Ooredoo plans NVIDIA Tensor Core GPU deployment in AI data centers across Qatar, Algeria, Tunisia, Oman, Kuwait, Maldives | A for regional plan, not a Kuwait facility launch |
| KDIPA incentives | https://kdipa.gov.kw/invest-in-kuwait/guarantees-incentives/ | FDI licensing/incentives route; includes tax/customs exemptions and land/real-estate allocation possibility | A for investment route |
| MEW | https://www.mew.gov.kw/ | Utility/power route; Arabic site includes company/customer portals and investor portal | A for power-agency route; no public DC load register found |
| Kuwait Municipality | https://www.baladia.gov.kw/ | Building/licensing route; public site shows governorate engineering license activity/news, not a searchable DC permit registry | A for permit route |
| Kuwait Government Online governorates | https://e.gov.kw/sites/kgoenglish/Pages/Visitors/AboutKuwait/KuwaitGovernorates.aspx | Official government portal route for administrative governorates | A for governorate coverage check |
| Kuwait Census establishments by governorate | https://census.csb.gov.kw/Census_Establish_EN | Official statistical surface listing all six governorates in establishment distribution | A for division-name cross-check |
| CAPT | https://capt.gov.kw/en/ | Public tender route for high-value state procurement | A for tender route |
| e.gov.kw CAPT open tenders | https://www.e.gov.kw/sites/kgoenglish/Pages/eServices/CTC/Openedtenders.aspx | Government portal route for opened tenders | A for tender route |
| KUNA | https://www.kuna.net.kw/ | Official state news; search Arabic/English for launches, MoUs, ministerial data-center statements | A for official news when result is live |

## 2. Official Query Templates

National/regulator:
```text
site:citra.gov.kw ("data center" OR "data centre" OR "مركز بيانات" OR "مراكز البيانات" OR "cloud" OR "سحابية")
site:citra.gov.kw ("ISP" OR "SubISP" OR "Licensing" OR "Tenders" OR "مزود خدمة الإنترنت") ("data" OR "cloud" OR "مركز")
site:ix.kw ("TEC" OR "landing station" OR "members" OR "peering")
site:moc.gov.kw ("data center" OR "مركز بيانات" OR "cloud" OR "مناقصة")
site:kuna.net.kw ("مركز بيانات" OR "مراكز البيانات" OR "الحوسبة السحابية" OR "سحابة") الكويت
```

Permits, tenders, investment, and power:
```text
site:baladia.gov.kw ("مركز بيانات" OR "مراكز البيانات" OR "رخصة بناء" OR "ترخيص بناء")
site:capt.gov.kw ("data center" OR "cloud" OR "خوادم" OR "استضافة" OR "مركز بيانات")
site:e.gov.kw ("data center" OR "cloud" OR "tender" OR "مناقصة" OR "خوادم")
site:kdipa.gov.kw ("data center" OR "cloud" OR "ICT" OR "technology" OR "مركز بيانات")
site:mew.gov.kw ("مركز بيانات" OR "ميجاواط" OR "محطة تحويل" OR "بوابة المستثمر")
```

Cloud-region status checks:
```text
site:learn.microsoft.com/en-us/azure/reliability/regions-list Kuwait
site:cloud.google.com/about/locations Kuwait
site:aws.amazon.com/about-aws/global-infrastructure/regions_az/ Kuwait
site:oracle.com/cloud/data-regions Kuwait
site:news.microsoft.com/en-xm Kuwait ("Azure Region" OR "AI powered Azure Region")
"Google Cloud" Kuwait region (launch OR opened OR operational OR construction)
```

Operator-primary checks:
```text
site:syntys.com Kuwait ("data center" OR "data centre" OR "Kuwait City" OR Shuaiba)
site:ironmountain.com/data-centers/locations/syntys-data-center Kuwait
site:ooredoo.com Kuwait ("NVIDIA" OR "GPU" OR "data centre" OR "Syntys")
site:kw.zain.com ("Zain Business Data Center" OR ZBDC OR "cloud")
site:stc.com.kw ("Data Center 1" OR "Data Center 2" OR "data center" OR "cloud")
"Zajil" OR "Kalaam" Kuwait ("data center" OR "Tier III" OR VESDA)
```

Arabic launch/permitting terms:
```text
("افتتاح" OR "تدشين" OR "إطلاق" OR "دخل الخدمة" OR "وضع حجر الأساس") ("مركز بيانات" OR "مراكز البيانات") الكويت
("تخصيص أرض" OR "ترخيص بناء" OR "رخصة بناء") "مركز بيانات" الكويت
("هيئة الاتصالات" OR "وزارة المواصلات" OR "بلدية الكويت" OR "وزارة الكهرباء") ("مركز بيانات" OR "الحوسبة السحابية")
```

## 3. Status and Evidence Discipline

Use these statuses consistently:

- `operational`: operator/owner, government, or strong trade source says the facility is live/opened/operational.
- `under_construction`: construction or fit-out is explicitly underway.
- `land_or_permit`: land, permit, grid request, or license only.
- `planned_or_mou`: MoU, intent, announcement, or partnership without site/construction/launch. Azure Kuwait and Google Kuwait are here until upgraded by official evidence.
- `cloud_edge_or_dedicated_region`: cloud node/edge/ExpressRoute/local zone; record separately from colocation.
- `connectivity_only`: IXP, submarine cable landing, PoP, exchange, or terrestrial system with no data-center evidence.
- `negative_sweep`: named governorate searched with no facility found; keep query log.

Capacity fields remain separate: `it_mw`, `facility_power_mw`, `grid_connection_mva`, `racks`, `white_space_sqm`, `land_area_sqm`, `announced_campus_mw`. Do not merge GPU/cloud-region language into colocation MW.

## 4. Official / Primary Seeds to Carry Forward

| Seed | Division | Location handling | Status | Grade and handling |
|---|---|---|---|---|
| Microsoft AI-powered Azure Region intent | Undisclosed / Kuwait-wide | No site, no timeline, no launch in Azure regions list | `planned_or_mou` | A for Microsoft/CAIT/CITRA intent only |
| Google Cloud Kuwait region announcement | Undisclosed / Kuwait-wide | No site/timeline in DCD/Reuters coverage; absent from Google locations check | `planned_or_mou` | A/B for announcement only; re-check Google official locations |
| Syntys Kuwait City | Capital | Kuwait City; exact district/address not primary-sourced in official page | `operational` | A for Syntys/Iron Mountain named location; C for directory address details such as Al-Soor St |
| Syntys Shuaiba | Ahmadi | Shuaiba industrial area | `operational` | A for Syntys/Iron Mountain named location; use as Ahmadi-positive coverage; no per-site MW unless sourced |
| Syntys/Ooredoo Kuwait platform capacity | Capital + Ahmadi / country-level | 2 active Kuwait DCs; about 2.2 MW active IT load in deck | `operational` platform context | A for Ooredoo-hosted deck; do not allocate MW by site |
| Ooredoo Kuwait sovereign AI data-center claim | Likely Syntys/Ooredoo Kuwait, exact site not public | Press says H200 GPUs/local data center; official Ooredoo regional NVIDIA page supports Kuwait in regional plan | `operational` if press accepted; `operator_lead` until official Kuwait launch page found | B for launch press; A only for regional plan |
| Zain Business Data Center / ZBDC | Capital likely; directory address may conflict | Zain business site navigation exposes Zain Business Data Center; local press cites ZBDC services | `operational` | A for Zain product existence; B/C for facility/address details |
| stc Kuwait / solutions by stc data centers | Capital likely | stc 2024 sustainability report names Data Center 1 and Data Center 2 in assessed critical locations | `operational` | A for stc data-center existence; C for public directory address such as Liberation Tower |
| Zajil / Kalaam Kuwait DC | Capital likely | DCD and Submarine Networks report Kalaam acquired Zajil; DCD specifically names the Kuwait data center; DCD says single-story built to Tier III standards per company website | `operational` | B for acquisition/facility; Tier III = design claim, not certification |
| ix.kw at TEC Building | Capital | TEC Building, CITRA/IXP contact | `connectivity_only` | A for IXP; not a DC |
| Submarine cable landings and MEETS/EIG connectivity | Capital / Kuwait City | FALCON, FOG, GBI, Kuwait-Iran, MEETS/EIG leads | `connectivity_only` | B/C unless landing-party primary source is found |
| PACI systems | Hawalli lead | PACI HQ / Mishref lead only | `enterprise/government lead` | A for agency role if sourced; U/C for data-center inference |

## 5. Per-Governorate Official Strategy

### Capital - primary hub
Expected positives: Syntys Kuwait City/Ooredoo, Zain Business Data Center, stc Data Center 1/2 or solutions by stc, Zajil/Kalaam, ix.kw/TEC connectivity, cable landing leads. Search Kuwait City, Sharq, Mirqab, Qibla, Shuwaikh, Al-Soor Street, Liberation Tower, Abdulla Al-Salem Street, Fahad Al-Salem Street. Treat addresses from directories as C until operator/official corroboration.

### Hawalli - enterprise/government sweep
Districts: Hawalli, Salmiya, Bayan, Mishref, Jabriya, Salwa, Rumaithiya. Search PACI/Mishref and Arabic terms. Expected result is 0 public colo unless a government/enterprise site is explicitly named. Record `negative_sweep` if no source names a facility.

### Farwaniya - logistics/airport sweep
Districts: Farwaniya, Al Rai, Sabhan, Ardhiya, Khaitan, Jleeb Al-Shuyoukh, Kuwait International Airport. Search CAPT, airport, customs/logistics, and Arabic terms. Expected result is negative or enterprise-only; do not infer from data/ICT offices.

### Ahmadi - Syntys Shuaiba plus oil-sector leads
Districts/areas: Ahmadi city, Shuaiba, Mina Abdullah, Al Zour, Fahaheel, Mangaf, Fintas, Mahboula, Wafra, Al Khiran / Sea City. Carry Syntys Shuaiba as a verified positive. Search KOC/KNPC/KIPIC and CAPT for enterprise data-center tenders; keep Omniva/Sea City as historical industry lead only.

### Jahra - negative-expected
Districts/areas: Jahra city, Sulaibiya, Abdali, Kabd, Mutlaa, Subiya/Silk City, Boubyan/Mubarak Al-Kabeer Port. Search mega-project ICT, land allocation, and Arabic launch verbs. Expected public-colo result: negative sweep.

### Mubarak Al-Kabeer - negative-expected
Districts/areas: Mubarak Al-Kabeer, Sabah Al-Salem, Qurain, Funaitees, Messila, Abu Al-Hasaniya. Search residential/new-city IT and bank DR terms. Expected public-colo result: negative sweep.

## 6. Validation Workflow

1. Verify the source URL resolves and still supports the exact claim.
2. Normalize division to one of the six repo divisions; keep district and Arabic alias separately.
3. Assign one status per candidate; never upgrade cloud-intent to operational without official region launch or physical facility evidence.
4. For Syntys/Ooredoo, distinguish country/platform capacity from site-level capacity.
5. Check official cloud-region lists every run: Azure, Google Cloud, AWS, Oracle.
6. Check CITRA, ix.kw, KUNA, CAPT/e.gov.kw, KDIPA, baladia, and MEW for official events, permits, tenders, investment, and power leads.
7. Check Uptime Institute certification separately before recording certified Tier level.
8. Complete all six governorates with either a positive seed or a documented negative sweep.

## 7. Re-check Cadence

- Monthly: Azure/GCP/AWS/Oracle region lists; Microsoft Kuwait newsroom; Google Cloud Kuwait searches; CITRA news; KUNA Arabic searches.
- Quarterly: Syntys/Ooredoo, Zain, stc, Kalaam/Zajil operator pages; CAPT/e.gov.kw tender scans; KDIPA/KAPP/baladia/MEW searches.
- Semi-annual: aggregator reconciliation (DataCenterMap, datacenters.com, Baxtel, datacenterHawk, PeeringDB), Uptime certification list, full per-governorate negative sweeps.
- Event-triggered: hyperscaler launch, Syntys expansion, government cloud award, land/power tender, or new cable landing.
