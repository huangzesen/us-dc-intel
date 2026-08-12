# LA Explorer Official - Laos Datacenter Enumeration Methodology

Date: 2026-08-12. Scope: official, regulatory, investment, SEZ, utility, state-media, and official-adjacent methods for enumerating datacenter projects in Lao PDR across the 17 manifest provinces, with Vientiane Capital handled as an additional high-priority unit.

Reliability grades:
- **A** = primary or legally accountable source: MTC/MPT/LANIC page, KPL state news, Lao Trade Portal law/regulation page, InvestLaos/MPI/IPMC/SEZ page, provincial government/DPI/SEZA notice, EDL/EDL-Gen utility evidence, official operator page, official hyperscaler region list.
- **B** = strong secondary: Vientiane Times, Xinhua, VietnamPlus, Laotian Times, reputable law-firm/regulatory summaries, listed-company filings, established telecom/datacenter trade press.
- **C** = weak lead: DataCenterMap, generic directories, SEO/vendor blogs, market-report snippets, social posts, uncorroborated Lao-language reposts. Use for discovery only.

---

## 0. Laos-Specific Structure Facts

- Laos has **17 provinces plus Vientiane Capital / Vientiane Prefecture**. The project manifest covers only the 17 provinces: Attapu, Bokeo, Bolikhamxai, Champasak, Houaphan, Khammouan, Louang Namtha, Louangphabang, Oudomxai, Phongsali, Salavan, Savannakhet, Viangchan, Xaignabouli, Xekong, Xiangkhouang, Xaisomboun. Add **Vientiane Capital** manually because nearly every confirmed datacenter/cloud lead is there. Source for administrative framing: Lao official/official-adjacent admin datasets generally describe 17 provinces plus the capital/prefecture; use UN/OCHA COD-AB or Lao Statistics Bureau materials when a manifest cross-check is needed.
- The core regulator is the **Ministry of Technology and Communications (MTC)**. Its live site is `https://mtc.gov.la/`; the footer still says MPT, and legacy references use Ministry of Posts and Telecommunications or Ministry of Science and Technology for older projects. Treat MTC/MPT/MOST as historical aliases and normalize to MTC in notes.
- MTC's home page exposes official service routes for `.la` domain registration through LANIC, server rental/hosting through LANIC, ICT service licensing/import of ICT equipment, and ministry publications including national digital-economy vision/strategy/plans. This makes MTC/LANIC a primary source for government hosting and ICT regulatory context. Source: `https://mtc.gov.la/`.
- There is a **National Data Center** unit under MTC. KPL reported that this unit signed a 2025-05-30 MoU with Silicon Tech Park (Lao) Sole Co., Ltd. for a feasibility study covering AI infrastructure powered by green electricity and an AI SEZ of more than 150 ha in the Vientiane capital area. Source: `https://kpl.gov.la/En/detail.aspx?id=91710`.
- Vientiane Times reported MTC/Phounphonnakhone Co., Ltd. work on a feasibility study for a **National Data Centre and Government Data Exchange System**, with Phounphonnakhone described as an IT company under LA Group / Phongsavanh Group. Source: `https://www.vientianetimes.org.la/freefreenews/freecontent_189_Ministry_y25.php`. Grade this as **B** unless the same agreement is found on MTC/KPL or in a signed official document.
- The most concrete government-operated datacenter precedent is the **Lao PDR Energy Efficient Datacenter Project** in Vientiane. IIJ says Lao PDR's first government-operated eco datacenter was completed in Vientiane on 2016-11-29; Toyota Tsusho says the project was registered as the first Lao-Japan JCM project and used modular datacenter technology. Sources: `https://www.iij.ad.jp/en/news/pressrelease/2016/1130.html`, `https://www.toyota-tsusho.com/english/press/detail/170920_004027.html`, `https://www.jcm.go.jp/jc/projects/la001/`.
- Laos does **not** appear to have a public facility-level datacenter registry or a public national construction-permit database. Build the census from MTC/LANIC, KPL, InvestLaos/MPI/SEZ, provincial DPI/SEZA pages, EDL/EDL-Gen power evidence, official operator pages, and credible trade press.
- Expect a very small market: confirmed or primary-operator-public facilities are concentrated in Vientiane Capital. For the 17 manifest provinces, most searches should return **no confirmed datacenter**; record that absence explicitly instead of inventing provincial rows.

---

## 1. Search Language and Core Terms

Use English for state media, operators, investors, and foreign vendors; Lao for ministry/provincial pages; Chinese for China-linked SEZ and railway-corridor leads.

English terms:

```text
"data center"
"data centre"
"datacenter"
"National Data Center"
"National Data Centre"
"government data exchange"
"cloud service"
"server rental"
"hosting"
"colocation"
"IDC"
"AI infrastructure"
"AI Special Economic Zone"
"green energy-powered AI"
```

Lao terms:

```text
ສູນຂໍ້ມູນ
ສູນຂໍ້ມູນແຫ່ງຊາດ
ສູນດາຕ້າ
ດາຕ້າເຊັນເຕີ
ຄລາວ
ເຊົ່າ Server
ບໍລິການ Hosting
ໃບອະນຸຍາດ ICT
ໂຄງການ
ບົດສຶກສາຄວາມເປັນໄປໄດ້
ເຂດເສດຖະກິດພິເສດ
```

Chinese terms:

```text
老挝 数据中心
老挝 国家数据中心
万象 数据中心
老挝 云计算
老挝 人工智能 数据中心
老挝 绿色能源 数据中心
老挝 经济特区 数据中心
磨丁 数据中心
金三角经济特区 数据中心
```

High-yield templates:

```text
site:mtc.gov.la "data center" OR "ສູນຂໍ້ມູນ"
site:mtc.gov.la "ເຊົ່າ Server" OR "Hosting"
site:lanic.gov.la "server" OR "hosting" OR "data center"
site:kpl.gov.la/En "data center" Laos
site:kpl.gov.la/En "National Data Center" "Ministry of Technology and Communications"
site:vientianetimes.org.la "National Data Centre" Laos
site:vientianetimes.org.la "Green AI Data Center" Laos
site:investlaos.gov.la "data center" OR "technology" OR "ICT"
site:investlaos.gov.la "Special Economic Zone" "Post and Telecommunication"
site:laotradeportal.gov.la "Law on Telecommunication" "05/NA"
site:laotradeportal.gov.la "Electronic Data Protection" "25/NA"
site:edl.com.la "data center" OR "server" OR "cloud"
site:edlgen.com.la "data center" OR "server" OR "cloud"
```

---

## 2. Grade A / Official Source Backbone

### 2.1 MTC / MPT / LANIC

Primary routes:
- MTC home/news/publications: `https://mtc.gov.la/`
- LANIC, linked from MTC for domain, server rental, and hosting services: `https://lanic.gov.la/`
- MTC publication route for national digital-economy vision/strategy/plans: linked from `https://mtc.gov.la/`

Use MTC/LANIC for regulator identity, government hosting services, National Data Center unit references, ICT service licensing/import procedures, national digital strategy, and ministry-hosted statistics. Search both Lao and English because many MTC pages are Lao-only and the site still exposes MPT labels.

Grade: **A** for live MTC/LANIC pages and official MTC-hosted PDFs. Caveat: MTC pages are not a facility registry; a ministry strategy or service page should not be converted into a datacenter row unless it identifies a facility, project, location, or operator.

### 2.2 KPL - Khaosan Pathet Lao

Primary route: `https://kpl.gov.la/En/`

KPL is the best official English feed for government digital-infrastructure announcements. It confirmed the 2025-05-30 National Data Center / Silicon Tech Park MoU for green-energy AI infrastructure and an AI SEZ feasibility study in the Vientiane capital area. Search KPL before accepting any MoU or ministerial event from private media.

Queries:

```text
site:kpl.gov.la/En/detail.aspx Laos "data center"
site:kpl.gov.la/En "National Data Center" "Silicon Tech Park"
site:kpl.gov.la/En "AI Special Economic Zone" "Vientiane"
site:kpl.gov.la/En "Ministry of Technology and Communications" "cloud"
```

Grade: **A** for event occurrence, named government unit, named counterparty, date, and official policy statement. Caveat: an MoU/feasibility study is **pipeline only**, not an operational datacenter.

### 2.3 Lao Trade Portal - Laws and ICT Equipment Rules

Primary routes:
- Law on Telecommunication (Amended), No. 05/NA, 2021-11-16: `https://www.laotradeportal.gov.la/en-gb/site/display/2570`
- Law on Electronic Data Protection, No. 25/NA, 2017-05-12: `https://www.laotradeportal.gov.la/en-gb/site/display/1718`
- E-Commerce law/regulation index including Electronic Data Protection: `https://www.laotradeportal.gov.la/en-gb/site/display/1714`
- Decision on management of telecommunications and ICT equipment, No. 3583/MoTC, 2022-12-13: `https://www.laotradeportal.gov.la/en-gb/site/display/2634`
- Older Decision on Import and Distribution of ICT Equipment, No. 3201/MPT: `https://www.laotradeportal.gov.la/en-gb/site/display/1158`

Use these for legal/regulatory context, import/type-approval obligations for telecom/ICT equipment, and data-protection context. Do not treat these pages as evidence that a particular datacenter exists.

Grade: **A** for law/decision existence and dates. Use law-firm summaries only as **B** to interpret obligations, then cite the Trade Portal or gazette when possible.

### 2.4 MPI / IPMC / InvestLaos and SEZ Authorities

Primary routes:
- Investment Promotion and Management Committee / InvestLaos: `https://investlaos.gov.la/`
- SEZ list: `https://investlaos.gov.la/where-to-invest/special-economic-zone-sez/`
- SEZ investment mechanism / one-stop service: `https://investlaos.gov.la/starting-a-business/investment-types/special-economic-zone/`
- Lao SEZ page says 12 SEZs are developed and identifies SEZO under MPI plus provincial SEZA approval/facilitation roles: `https://investlaos.gov.la/lo-la/%E0%BA%9A%E0%BB%88%E0%BA%AD%E0%BA%99%E0%BA%97%E0%BA%B5%E0%BB%88%E0%BA%A5%E0%BA%BB%E0%BA%87%E0%BA%97%E0%BA%B6%E0%BA%99/%E0%BB%80%E0%BA%82%E0%BA%94%E0%BB%80%E0%BA%AA%E0%BA%94%E0%BA%96%E0%BA%B0%E0%BA%81%E0%BA%B4%E0%BA%94%E0%BA%9E%E0%BA%B4%E0%BB%80%E0%BA%AA%E0%BA%94-%E0%BA%82%E0%BA%9E%E0%BA%AA/`

High-value official SEZ pages:
- Savan-Seno SEZ, Savannakhet: `https://investlaos.gov.la/where-to-invest/special-economic-zone-sez/savan-seno-special-economic-zone/` - establishment 2003, area 954 ha, government developer, East-West Economic Corridor, land lease/electricity/water rates.
- Boten Beautiful Land Specific Economic Zone, Louang Namtha: `https://investlaos.gov.la/where-to-invest/special-economic-zone-sez/boten-beautiful-land-specific-economic-zone/` - 1,640 ha, private Chinese developer, border/ASEAN+3 corridor, post and telecommunication listed among investment projects.
- Golden Triangle SEZ, Bokeo: `https://investlaos.gov.la/where-to-invest/special-economic-zone-sez/golden-triangle-special-economic-zone/` - post, telecommunication, internet, advertisement and printing listed among project categories.
- Vientiane Capital SEZs on InvestLaos: VITA Park, Saysettha Development Zone, Thatluang Lake, Long-Thanh Vientiane, Dongphosy.
- Additional provincial SEZs on the Lao SEZ page: Luangprabang SEZ, Thakhaek SEZ, Phoukhyo SEZ, Champasak SEZ sub-zones including Pakse-Japan SEZ.

Grade: **A** for official SEZ existence, location, investment process, eligible/project categories, and published utility/lease rates. Caveat: SEZ pages usually show investment potential, not confirmed datacenter tenants; a DC row requires a named tenant/project or additional evidence.

### 2.5 Power and Connectivity Evidence

Primary/near-primary routes:
- EDL: `https://www.edl.com.la/`
- EDL-Gen: `https://www.edlgen.com.la/`
- MTC statistics and telecom publications from `https://mtc.gov.la/`
- Operator network pages for Lao Telecom, Unitel, ETL, T-Plus, Best Telecom, Planet Online.

Use utility evidence to validate high-load projects. Laos markets low-cost/green hydropower, but there is no public datacenter interconnection register. For any claimed facility above normal enterprise/server-room scale, require one of: EDL/EDL-Gen announcement, SEZ utility allocation, grid/substation work, land/permit evidence, or operator construction statement.

Grade: **A** for utility/operator-primary statements; **B/C** for press claims about cheap power or hydro advantage unless tied to a specific tariff, site, or agreement.

---

## 3. Official Enumeration Workflow

1. **Start with Vientiane Capital**: MTC/LANIC, KPL, Vientiane Times, Unitel Cloud, LaoDC, GDMS, the 2016 government eco datacenter, and Vientiane Capital SEZs. This is the only location with confirmed public datacenter/cloud evidence.
2. **Separate row types**: operational facility, operator cloud/hosting service, government datacenter, MoU/feasibility study, SEZ opportunity, telecom/server-room lead, crypto/scam/mining compute lead. Do not merge these into a single operational count.
3. **For each lead, capture minimum fields**: source URL, source grade, operator/project, legal entity if available, admin division, district/village/address if available, status, date, evidence type, capacity if published, and caveats.
4. **Check official source chain**: MTC/LANIC or KPL -> InvestLaos/MPI/SEZ -> provincial DPI/SEZA -> EDL/EDL-Gen -> operator page -> trade press. Promote a row to Grade A only when the evidence is primary for the fact being asserted.
5. **Sweep all 17 manifest provinces** using province-specific templates below. Record `no confirmed DC found in public sources` when searches return only telecom coverage, generic SEZ promotion, or unrelated IT projects.

---

## 4. Division Coverage and Search Plan

Use the official English and variant spellings shown here. Pair every English query with Lao and, where relevant, Chinese terms.

| Manifest division | Priority | Official route | Query pivots | Expected result |
|---|---:|---|---|---|
| Attapu / Attapeu | Low | provincial DPI + MTC + EDL | `Attapu data center`, `Attapeu cloud`, `ອັດຕະປື ສູນຂໍ້ມູນ` | likely none |
| Bokeo | Medium | Golden Triangle SEZ + provincial DPI/SEZA + MTC | `Bokeo Golden Triangle data center`, `金三角经济特区 数据中心`, `Bokeo crypto mining` | SEZ/telecom/crypto leads only unless named facility appears |
| Bolikhamxai / Bolikhamsai | Low | provincial DPI + EDL | `Bolikhamxai data center`, `Paksan cloud`, `ບໍລິຄໍາໄຊ ສູນຂໍ້ມູນ` | likely none |
| Champasak | Medium | Champasak SEZ/Pakse-Japan SEZ + DPI | `Pakse data center`, `Champasak SEZ ICT`, `ຈໍາປາສັກ ດາຕ້າເຊັນເຕີ` | possible small hosting/edge/SEZ lead; no confirmed DC yet |
| Houaphan / Huaphanh | Low | provincial DPI + MTC | `Houaphan data center`, `Sam Neua cloud`, `ຫົວພັນ ສູນຂໍ້ມູນ` | likely none |
| Khammouan / Khammouane | Medium | Thakhaek SEZ + DPI + EDL | `Khammouan data center`, `Thakhek SEZ data center`, `ຄໍາມ່ວນ ສູນຂໍ້ມູນ` | SEZ/industrial leads; no confirmed DC yet |
| Louang Namtha / Luang Namtha | Medium | Boten Beautiful Land SEZ + DPI/SEZA | `Boten data center`, `Louang Namtha cloud`, `磨丁 数据中心` | China-border digital/telecom leads; no confirmed DC yet |
| Louangphabang / Luang Prabang | Medium-low | Luangprabang SEZ + DPI + MTC | `Luang Prabang data center`, `Luangprabang SEZ technology`, `ຫຼວງພະບາງ ສູນຂໍ້ມູນ` | possible government/tourism ICT; no confirmed DC yet |
| Oudomxai / Oudomxay | Low | provincial DPI + railway corridor sources | `Oudomxai data center`, `Muang Xay cloud`, `ອຸດົມໄຊ ສູນຂໍ້ມູນ` | likely none |
| Phongsali / Phongsaly | Low | provincial DPI + border connectivity | `Phongsali data center`, `Phongsaly cloud`, `ຜົ້ງສາລີ ສູນຂໍ້ມູນ` | likely none |
| Salavan / Saravan | Low | provincial DPI + EDL | `Salavan data center`, `Saravan cloud`, `ສາລະວັນ ສູນຂໍ້ມູນ` | likely none |
| Savannakhet | Medium-high | Savan-Seno SEZ + DPI/SEZA + EDL | `Savan-Seno data center`, `Savannakhet IDC`, `ສະຫວັນນະເຂດ ດາຕ້າເຊັນເຕີ` | strongest province outside capital; no confirmed DC tenant yet |
| Viangchan / Vientiane Province | Medium | provincial DPI + EDL + proximity to capital | `Vientiane Province data center`, `Phonhong cloud`, `ວຽງຈັນ ແຂວງ ສູນຂໍ້ມູນ` | possible spillover; distinguish from Vientiane Capital |
| Xaignabouli / Xayabury / Sainyabuli | Low | provincial DPI + EDL | `Xayabury data center`, `Xaignabouli cloud`, `ໄຊຍະບູລີ ສູນຂໍ້ມູນ` | likely none |
| Xekong / Sekong | Low | provincial DPI + EDL | `Xekong data center`, `Sekong cloud`, `ເຊກອງ ສູນຂໍ້ມູນ` | likely none |
| Xiangkhouang / Xiengkhouang | Low | provincial DPI + MTC | `Xiengkhouang data center`, `Phonsavan cloud`, `ຊຽງຂວາງ ສູນຂໍ້ມູນ` | likely none |
| Xaisomboun / Saysomboun | Low | provincial DPI + EDL | `Xaisomboun data center`, `Saysomboun cloud`, `ໄຊສົມບູນ ສູນຂໍ້ມູນ` | likely none |

Additional enumeration unit:

| Extra division | Priority | Official route | Query pivots | Expected result |
|---|---:|---|---|---|
| Vientiane Capital / Vientiane Prefecture / Nakhon Louang Vientiane | Very high | MTC/LANIC, KPL, Vientiane Times, InvestLaos Vientiane SEZs, operator pages, EDL | `Vientiane Capital data center`, `MTC National Data Center`, `LANIC server hosting`, `Unitel Cloud Nongbone`, `LaoDC Vientiane`, `GDMS National Cloud`, `ວຽງຈັນ ສູນຂໍ້ມູນ` | confirmed government/operator/cloud rows and 2025 feasibility pipeline |

---

## 5. Official Source Grading Rules for Registry Rows

- **A operational facility**: official operator page or government/utility/SEZ document identifies a facility and location. Examples: LaoDC's own page says it has its own datacenter in Vientiane Capital; IIJ/Toyota/JCM identify the 2016 government eco datacenter in Vientiane.
- **A government project/MoU event**: KPL or MTC confirms an MoU or feasibility study. Status must be `MoU`, `feasibility`, or `planned`; do not mark operational.
- **A legal/regulatory context**: Lao Trade Portal law/decision pages. Useful for methodology, not facility proof.
- **A SEZ opportunity**: InvestLaos/SEZ page confirms the zone, location, utilities, or eligible sectors. It is not a datacenter project unless a named DC tenant exists.
- **B project lead**: Vientiane Times/Xinhua/VietnamPlus or established trade press names parties and status but no primary document was found.
- **C discovery lead**: directories, social posts, SEO pages, stale aggregators, or generic market reports. Never publish as a confirmed facility without primary/operator/official corroboration.

---

## 6. Open Verification Checklist

1. Re-run MTC/KPL/Vientiane Times searches for follow-ups to the 2025 Silicon Tech Park AI infrastructure/AI SEZ MoU and the Phounphonnakhone national data-centre feasibility study.
2. Search MTC/LANIC for a public ICT/hosting/datacenter license list; as of this rewrite, no facility-level register was found.
3. Confirm whether the 2016 government eco datacenter is one of the two National Data Centers referenced by GDMS, and whether both sites have public locations.
4. For any claimed provincial site, require province/DPI/SEZA, utility, operator, or construction evidence before adding a facility row.
5. Re-check official cloud-region pages quarterly for Laos. As of this rewrite, there is no confirmed AWS, Azure, Google Cloud, Oracle Cloud, Alibaba Cloud, Tencent Cloud, or Huawei Cloud public region in Laos.
6. Keep crypto-mining, online-scam infrastructure, telecom tower/backhaul, and normal enterprise server rooms out of the operational datacenter count unless the registry has a separate `non_standard_compute` or `telecom_internal` row type.
