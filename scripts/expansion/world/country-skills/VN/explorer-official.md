# VN Explorer Official - Viet Nam Datacenter Enumeration via Planning, Energy, Cloud, Colo, and Regulator Sources

Date: 2026-08-12. Country: **VN Viet Nam**. Division model in the world manifest: **63 province / municipality names**. Angle: **official / regulatory / cloud pipeline** focused on Vietnamese investment and construction approvals, industrial/high-tech park authorities, EVN and power evidence, MIC telecom/cloud regulation, official cloud footprint pages, and official colo/operator disclosures.

Reliability grades:
- **A** = primary / official / legally accountable source: Government, ministry, provincial People's Committee, provincial department, high-tech / industrial / export-processing zone management board, EVN / power utility, official cloud-region page, official operator facility page, securities filing, or statutory certification.
- **B** = strong secondary source: state media, reputable trade press, official partner / contractor case study, industry association, or local press that names a project and approval/status.
- **C** = weak lead: directories, market reports, job ads, consultant summaries, unsourced maps, social media, or MoU-only articles with no approval, land, power, or construction trail.

---

## 0. Viet Nam-Specific Structural Facts

- Viet Nam does **not** have a single public national datacenter registry. Enumeration should join: investment-policy approvals (`chấp thuận chủ trương đầu tư`), investment registration certificates (`Giấy chứng nhận đăng ký đầu tư` / `IRC`), construction permits (`giấy phép xây dựng`), high-tech / industrial-zone allocation, EVN power evidence, MIC telecom registration rules, and official operator/cloud facility pages.
- The current repo manifest uses the historical 63 province/municipality divisions. Viet Nam's National Assembly approved a 2025 reorganization reducing the country to 34 provincial-level units, with new local governments operating from **2025-07-01**. For this repo, still bucket output to the manifest's 63 names, but search current official portals under both old and new province/city names. Example: former **Binh Duong** and **Ba Ria - Vung Tau** records may now surface under expanded **Ho Chi Minh City** portals or transition pages.
- Commercial datacenter concentration is strongest in **Ho Chi Minh**, **Ha Noi**, **Binh Duong**, **Da Nang**, and nearby industrial/high-tech zones. Secondary leads appear in **Dong Nai**, **Long An**, **Ba Ria - Vung Tau**, **Binh Dinh**, **Khanh Hoa**, and energy-rich central/southern provinces.
- Public-sector provincial "data centers" (`trung tâm dữ liệu tỉnh`, `trung tâm tích hợp dữ liệu`) are common and usually small civic facilities. Include them only if the expansion goal covers public/government datacenters; do not assign commercial MW unless official sources disclose it.
- Vietnamese sources usually use `trung tâm dữ liệu`, `trung tâm dữ liệu và điện toán đám mây`, `IDC`, `TTDL`, `hạ tầng số`, `khu công nghệ thông tin tập trung`, and `trung tâm tích hợp dữ liệu`. English `data center` / `data centre` appears in operator, hyperscaler, and trade-press material.

---

## 1. Official / Regulatory Query Patterns

Use Vietnamese first, then English. Always combine operator/project terms with the province/city and the likely approval authority.

### 1.1 Investment, Planning, and Construction

```
"trung tâm dữ liệu" "chấp thuận chủ trương đầu tư" "{province}"
"trung tâm dữ liệu" "Giấy chứng nhận đăng ký đầu tư" "{province}"
"trung tâm dữ liệu" "giấy phép xây dựng" "{province}"
"trung tâm dữ liệu" "khởi công" "{province}"
"trung tâm dữ liệu" "nghiệm thu" "{province}"
"trung tâm dữ liệu" "đưa vào vận hành" "{province}"
"data center" "investment registration certificate" "Vietnam" "{province}"
"data center" "construction permit" "Vietnam" "{city}"
site:{province-domain}.gov.vn "trung tâm dữ liệu"
site:{dpi-domain}.gov.vn "trung tâm dữ liệu"
site:{doc-domain}.gov.vn "trung tâm dữ liệu" "giấy phép xây dựng"
```

Key Vietnamese authority terms:
- `UBND` = People's Committee.
- `Sở Kế hoạch và Đầu tư` / `SKHĐT` = Department of Planning and Investment.
- `Sở Xây dựng` = Department of Construction.
- `Ban Quản lý Khu công nghệ cao` = high-tech park management board.
- `Ban Quản lý các khu chế xuất và công nghiệp` / `HEPZA` = export-processing / industrial-zone authority.
- `Khu công nghệ thông tin tập trung` = concentrated IT park; important for future data-center clusters.

### 1.2 Industrial / High-Tech / Export-Processing Zones

```
"trung tâm dữ liệu" "Khu Công nghệ cao TP.HCM"
"trung tâm dữ liệu" "Saigon Hi-Tech Park"
"trung tâm dữ liệu" "Khu chế xuất Tân Thuận"
"trung tâm dữ liệu" "Khu công nghiệp Tân Phú Trung"
"trung tâm dữ liệu" "Khu Công nghệ cao Hòa Lạc"
"trung tâm dữ liệu" "Khu công nghệ thông tin tập trung"
"data center" "Saigon Hi-Tech Park" "investment"
"data center" "Tan Thuan Export Processing Zone"
"data center" "Tan Phu Trung Industrial Park"
site:shtp.hochiminhcity.gov.vn "trung tâm dữ liệu"
site:hepza.hochiminhcity.gov.vn "trung tâm dữ liệu"
site:hhtp.gov.vn "trung tâm dữ liệu"
```

High-value official zone sources:
- Saigon Hi-Tech Park / SHTP: https://shtp.hochiminhcity.gov.vn/
- HCMC export-processing and industrial zones / HEPZA: https://hepza.hochiminhcity.gov.vn/
- Hoa Lac Hi-Tech Park: https://hhtp.gov.vn/
- National Public Service Portal for administrative procedure metadata: https://dichvucong.gov.vn/
- Ministry of Construction: https://moc.gov.vn/

### 1.3 EVN / Power / Grid

```
"trung tâm dữ liệu" "EVN" "{province}"
"trung tâm dữ liệu" "cấp điện" "{province}"
"trung tâm dữ liệu" "trạm biến áp" "{province}"
"trung tâm dữ liệu" "MW" "điện" "{province}"
"data center" "EVN" "Vietnam" "{operator}"
"data center" "substation" "Vietnam" "{operator}"
site:evn.com.vn "trung tâm dữ liệu"
site:evnhcmc.vn "trung tâm dữ liệu"
site:evnhanoi.vn "trung tâm dữ liệu"
site:npt.evn.vn "trung tâm dữ liệu" OR "trạm biến áp"
```

Use EVN sources as **A** for electricity, substation, and grid facts. They are not a complete datacenter census. Treat a power record as a datacenter only if it names `trung tâm dữ liệu`, the operator, or a project that matches a planning/operator record.

EVN and utility sources:
- EVN group: https://www.evn.com.vn/
- EVN HCMC: https://evnhcmc.vn/
- EVN Hanoi: https://evnhanoi.vn/
- National Power Transmission Corporation: https://www.npt.evn.vn/

### 1.4 MIC / Telecommunications Regulation / Cloud Registration

Primary sources:
- Ministry of Information and Communications / successor official pages: https://mic.gov.vn/ and English mirror https://english.mic.gov.vn/
- MIC legal-policy portal: https://cspl.mic.gov.vn/
- Viet Nam Telecommunications Authority: https://vnta.gov.vn/
- Online public service / procedure portal: https://dichvucong.gov.vn/

Regulatory facts to capture:
- The 2023 Telecommunications Law added `dịch vụ trung tâm dữ liệu` and `dịch vụ điện toán đám mây` to the telecommunications framework.
- MIC materials state the new data-center/cloud/OTT telecom-service provisions took effect from **2025-01-01**.
- MIC legal-policy material describes a "light-touch" model and says the 2023 law does not cap foreign ownership for data-center and cloud services in Viet Nam.
- Decree **163/2024/NĐ-CP** is the key implementing decree for registration / notification of new telecom services. Use official legal/procedure pages where possible; law-firm summaries are **B** only.

Query templates:
```
site:mic.gov.vn "dịch vụ trung tâm dữ liệu"
site:cspl.mic.gov.vn "dịch vụ trung tâm dữ liệu" "Luật Viễn thông"
site:vnta.gov.vn "trung tâm dữ liệu" "đăng ký cung cấp dịch vụ viễn thông"
site:dichvucong.gov.vn "đăng ký cung cấp dịch vụ viễn thông" "trung tâm dữ liệu"
"Nghị định 163/2024/NĐ-CP" "dịch vụ trung tâm dữ liệu"
"Luật Viễn thông 2023" "trung tâm dữ liệu" "điện toán đám mây"
```

Enumeration value: MIC / VTA evidence proves the legal service category and may surface provider registration/notification. It usually does **not** disclose facility address, MW, or construction status, so join it to operator and local approval records.

---

## 2. Grade-A Planning / Approval Pipeline

### Step A - Seed candidates by province/city

For each manifest division, run Vietnamese web search over the provincial portal, Department of Planning and Investment, Department of Construction, Department of Information and Communications, high-tech / industrial-zone management boards, and local state media.

Capture:
- Project name in Vietnamese and English.
- Legal investor / developer / joint venture.
- Authority granting approval: UBND, DPI, zone management board, SHTP, HEPZA, HHTP, etc.
- Approval type: investment-policy approval, IRC, construction permit, land allocation/lease, groundbreaking, completion/acceptance, operation.
- Location: old province/city, current province/city, district/ward/commune if available, industrial park / high-tech park / export-processing zone, lot number.
- Capacity evidence: MW / MVA / racks / sqm / servers / GPUs. Grade capacity separately; MW from official planning/power/operator source is **A**, directory MW is **C**.

### Step B - Search official industrial / technology park authorities

High-yield facilities and clusters:
- **Ho Chi Minh / Thu Duc / District 7 / Cu Chi**: Saigon Hi-Tech Park, Tan Thuan Export Processing Zone, Tan Phu Trung Industrial Park, Quang Trung Software City.
- **Ha Noi / Hoa Lac / Cau Giay**: Hoa Lac Hi-Tech Park, CMC Tower, VNPT IDC Hoa Lac, FPT / Viettel / VNPT / CMC facilities.
- **Binh Duong / Thuận An**: Viettel Binh Duong and wider HCMC-adjacent industrial demand.
- **Da Nang**: Viettel / VNPT / FPT, city digital-government and cloud infrastructure.
- **Dong Nai / Long Thanh**: concentrated IT-zone and southern energy/data-hub policy.
- **Long An, Ba Ria - Vung Tau, Binh Dinh, Khanh Hoa**: investment-seeking or early-stage energy/industrial leads; require approval or power confirmation before counting as firm projects.

### Step C - Construction / completion verification

Use `Sở Xây dựng`, municipal construction departments, and zone-management boards for:
- `giấy phép xây dựng` = construction permit.
- `thông báo khởi công` = construction commencement notice.
- `nghiệm thu hoàn thành công trình` = completion/acceptance.
- `phòng cháy chữa cháy` / `PCCC` = fire prevention and fighting acceptance.
- `đánh giá tác động môi trường` / `ĐTM` = environmental impact assessment when applicable.

Query:
```
site:{construction-domain}.gov.vn "{operator}" "giấy phép xây dựng"
site:{construction-domain}.gov.vn "trung tâm dữ liệu" "nghiệm thu"
site:{province-domain}.gov.vn "trung tâm dữ liệu" "PCCC"
site:{province-domain}.gov.vn "trung tâm dữ liệu" "ĐTM"
site:{zone-domain}.gov.vn "{operator}" "khởi công"
```

Reliability: **A** for official permit/acceptance records; **B** for operator PR or state media saying an official attended a groundbreaking; **C** for MoU-only.

---

## 3. Official Cloud Region / Edge Footprint

Cloud pages are **A** for provider market presence and metro clues, but they are not exact facility registries.

| Provider | Official source | Viet Nam footprint signal | Enumeration use |
|---|---|---|---|
| AWS | AWS Local Zones locations: https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ ; Hanoi GA announcement: https://aws.amazon.com/about-aws/whats-new/2026/06/aws-local-zones-hanoi-vietnam/ ; Direct Connect Hanoi: https://aws.amazon.com/about-aws/whats-new/2025/12/aws-direct-connect-hanoi/ | AWS says the **Hanoi Local Zone** is available. AWS also announced a Direct Connect location in **CMC Tower, Hanoi**. | Search CMC Tower / CMC Telecom / Hanoi approval and telecom registration evidence. Do not infer a full AWS Region or dedicated AWS-owned datacenter unless AWS says so. |
| Microsoft Azure | Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Azure geographies: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies ; Azure Front Door POPs: https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-region | No official Azure public cloud region in Viet Nam found in the regions list. Microsoft lists an Azure Front Door POP in **Ho Chi Minh City**. | Treat HCMC as edge/POP evidence only. For datacenter enumeration, search `Microsoft`, `Azure`, `ExpressRoute`, `CMC`, `Viettel`, `VNPT`, and partner colos; do not count an Azure Vietnam region without official Microsoft region-page evidence. |
| Google Cloud | Locations: https://cloud.google.com/about/locations ; Interconnect docs / partner pages | No official Google Cloud region in Viet Nam located in official region list at check date. Local operator pages may mention Google Cloud Interconnect / direct connectivity. | Use as connectivity lead only; search CMC / FPT / Viettel / VNPT partner pages for interconnect locations. |
| Oracle Cloud | OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No official OCI Viet Nam cloud region located in official region list at check date. CMC says it offers OCI FastConnect connectivity. | Connectivity lead only. |
| Viettel Cloud | Viettel Cloud: https://www.viettelcloud.vn/ ; Viettel Cloud ecosystem: https://solutions.viettel.vn/en/vi/chinh-phu-so/he-sinh-thai-viettel-cloud.html ; Viettel IDC: https://viettelidc.com.vn/ | Viettel Cloud is domestic cloud infrastructure operated on Viettel datacenters in Viet Nam. Public pages emphasize local datacenter infrastructure and 99.99% service commitments. | Treat Viettel Cloud pages as **A** for provider existence and domestic-cloud service, then use Viettel IDC / Viettel Group facility pages and local approvals for individual datacenters. |
| CMC Cloud | CMC Telecom: https://cmctelecom.vn/en/ ; CMC Cloud pages on CMC Telecom | CMC operates 3 neutral Tier 3 datacenters in Hanoi and HCMC and offers cloud plus AWS Direct Connect / Google Interconnect / Azure ExpressRoute / OCI FastConnect connectivity. | High-value seed for CMC Tower Hanoi, CMC SHTP, CMC Tan Thuan, and AWS Hanoi Direct Connect. |
| FPT Cloud / Fornix | FPT Fornix: https://fti.fpt.vn/en/services/data-center/ ; Fornix about page: https://fornix.fpt.work/en/about-dc/ | FPT says its datacenters are in Hanoi and Ho Chi Minh City. | Use for FPT Fornix Hanoi / HCM facilities, then verify with FPT Group announcements and SHTP / local permits. |

Cloud search templates:
```
"AWS Local Zone" Hanoi Vietnam "CMC Tower"
"AWS Direct Connect" Hanoi "CMC Tower"
"Azure Front Door" "Ho Chi Minh City" "Vietnam"
"Microsoft Azure" "Vietnam" "data center" "official"
"Viettel Cloud" "data center" "Hà Nội" "Hồ Chí Minh"
"CMC Cloud" "AWS Direct Connect" "CMC Tower" Hanoi
"FPT Cloud" "Fornix" "Hanoi" "Ho Chi Minh"
```

---

## 4. Official / Operator Facility Pages to Seed the Facility Universe

Operator pages are primary for existence and marketed footprint, but planning/power evidence should decide construction status and capacity confidence.

| Operator | Official source | Footprint signals | Follow-up joins |
|---|---|---|---|
| Viettel IDC / Viettel Group | Viettel IDC homepage https://viettelidc.com.vn/ ; Viettel data-center info page https://viettelidc.com.vn/tin-tuc/trung-tam-du-lieu ; Viettel Group Tan Phu Trung groundbreaking https://viettel.com.vn/vi/tin-tuc-va-su-kien/tin-tuc/viettel-khoi-cong-trung-tam-du-lieu-tieu-chuan-quy-mo-sieu-lon-dau-tien-tai-viet-nam/ | Existing Viettel IDC portfolio across Hanoi, Da Nang, HCMC, Binh Duong; Tan Phu Trung hyperscale project in HCMC. | HEPZA / Tan Phu Trung Industrial Park / HCMC People's Committee, EVNHCMC power, construction/PCCC records. |
| VNPT / VNPT IDC | VNPT business article https://vnpt.vn/doanh-nghiep/tu-van/vnpt-idc-data-center-giai-phap-luu-tru-du-lieu-toan-dien-cho-doanh-nghiep.html ; VNPT IDC site https://vnptidc.com/ ; Hanoi data-center launch https://vnpt.vn/gioi-thieu/tin-tuc/khai-truong-trung-tam-du-lieu-chinh-thanh-pho-ha-noi.html | VNPT says it owns 8 datacenters; key sites include Hoa Lac, Tan Thuan, Cau Giay, Da Nang, HCMC. | Hoa Lac High-Tech Park, Hanoi city / VNPT contract records, provincial government digital-center tenders. |
| FPT Telecom / FPT Fornix | FPT Fornix service page https://fti.fpt.vn/en/services/data-center/ ; Fornix about page https://fornix.fpt.work/en/about-dc/ ; FPT Group news pages | FPT says datacenters are in Hanoi and HCMC; Fornix HCM02 in Saigon Hi-Tech Park is a major HCMC facility. | SHTP investment/construction records, FPT official announcements, LEED/Uptime certification, EVN power. |
| CMC Telecom / CMC Cloud | CMC Telecom homepage https://cmctelecom.vn/en/ ; CMC DC development article https://cmctelecom.vn/bai-viet/cmc-telecom-becomes-the-leading-data-center-service-provider-in-vietnam-after-15-years-of-development/ ; CMC SHTP approval article https://cmctelecom.vn/bai-viet/cmc-xay-nen-mong-cho-trai-tim-ai-cua-tp-hcm-va-viet-nam/ | CMC operates CMC Tower Hanoi, CMC DC SHTP, CMC DC Tan Thuan; SHTP approved CMC Hyperscale DC in 2025. | SHTP / HEPZA records, AWS Direct Connect Hanoi, MIC security-level articles, EVN / HCMC construction. |
| NTT Global Data Centers / QD.TEK | NTT HCMC1 facility page https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/ho-chi-minh-city-1-data-center ; NTT Group JV release https://group.ntt/en/newsrelease/2022/03/29/220329a.html | HCMC1 at Saigon Hi-Tech Park, 6 MW critical IT load and 3,100 sqm server space, joint venture with QD.TEK. | SHTP investment/land records, construction status, power connection, PCCC. |
| ST Telemedia Global Data Centres / VNG | STT GDC Vietnam pages and factsheets | STT VNG HCMC1 operational in Tan Thuan; second facility announced by JV/trade sources. | Tan Thuan EPZ / HEPZA records, VNG filings, power and construction approvals. |
| MobiFone / other telcos | MobiFone official pages and procurement where available | Smaller national telco/cloud/data-center footprint across several cities. | Confirm via MIC/VTA registration, public procurement, provincial portals, operator pages. |

Operator search templates:
```
site:viettelidc.com.vn "trung tâm dữ liệu" "Hà Nội"
site:viettel.com.vn "trung tâm dữ liệu" "Tân Phú Trung"
site:vnpt.vn "trung tâm dữ liệu" "Hòa Lạc"
site:vnptidc.com "Tân Thuận" "IDC"
site:fpt.vn "Fornix" "Data Center"
site:fti.fpt.vn "Data Center" "Hanoi" "Ho Chi Minh"
site:cmctelecom.vn "Data Center" "Tân Thuận"
site:cmctelecom.vn "CMC Hyperscale" "SHTP"
site:services.global.ntt "Ho Chi Minh City 1 Data Center"
```

---

## 5. Per-Division Enumeration Strategy

### Tier 1: dense commercial/hyperscale sweep

Run full official + operator + power workflow first for:
- **Ho Chi Minh**: SHTP, HEPZA/Tan Thuan, Tan Phu Trung, QTSC, EVNHCMC, HCMC DPI / construction / People's Committee. Operators: Viettel, CMC, FPT, VNPT, NTT/QD.TEK, STT VNG, True IDC, MobiFone, KBC/AIC leads.
- **Ha Noi**: Hoa Lac, Cau Giay, CMC Tower, VNPT IDC Hoa Lac, AWS Direct Connect / AWS Local Zone Hanoi, EVNHANOI. Operators: VNPT, Viettel, CMC, FPT, Hanel/CSF leads, government datacenters.
- **Binh Duong**: Viettel Binh Duong / Thuận An and HCMC-adjacent industrial parks. Because of 2025 administrative changes, search both `Bình Dương` and `TP.HCM`.
- **Da Nang**: local cloud/IDC, Viettel/VNPT/FPT, submarine/fiber and smart-city infrastructure; use city People's Committee, Department of Information and Communications, and power company sources.

### Tier 2: industrial / energy / growth leads

Use investment + industrial park + EVN searches for:
- **Dong Nai**: Long Thanh concentrated IT zone, southern energy/data-hub policy, industrial parks, potential hyperscale spillover from HCMC.
- **Long An**: Saigontel / P&G Tech and HCMC-edge industrial land.
- **Ba Ria - Vung Tau**: Digital Hub / energy-rich southern coastal leads.
- **Binh Dinh**: Quy Nhon / Nhon Hoi economic zone, submarine cable landing, Korean-investor data-center leads.
- **Khanh Hoa**: Nha Trang / Cam Ranh policy leads and data-hub positioning.
- **Quang Ninh, Hai Phong, Bac Ninh, Hai Duong, Hung Yen, Vinh Phuc, Thai Nguyen**: northern industrial/electronics belt and government/integrated datacenter records; search industrial park and power sources heavily.

### Tier 3: provincial government datacenter sweep

For all remaining manifest divisions, first distinguish small government digital-infrastructure facilities from commercial colocation/hyperscale projects:

```
"trung tâm dữ liệu tỉnh {province}"
"trung tâm tích hợp dữ liệu {province}"
"trung tâm dữ liệu" "Sở Thông tin và Truyền thông" "{province}"
"nâng cấp trung tâm dữ liệu" "{province}" "đấu thầu"
"trung tâm dữ liệu" "{province}" "chính quyền điện tử"
site:{province-domain}.gov.vn "trung tâm tích hợp dữ liệu"
site:muasamcong.mpi.gov.vn "trung tâm dữ liệu" "{province}"
```

Use public procurement for equipment upgrades, firewalls, servers, UPS, generators, and security assessments:
- National bidding portal: https://muasamcong.mpi.gov.vn/
- Search terms: `trung tâm dữ liệu`, `trung tâm tích hợp dữ liệu`, `máy chủ`, `tường lửa`, `UPS`, `máy phát điện`, `điều hòa chính xác`, `nâng cấp TTDL`.

Grade public procurement as **A** for buyer, package, and civic datacenter evidence. It is usually **not** a commercial MW source.

---

## 6. Evidence Rules and Common Pitfalls

- **Do not count "cloud region" as a building**. AWS Hanoi Local Zone and Azure HCMC POP are cloud/edge infrastructure signals; they need local operator / facility / approval evidence before becoming datacenter records.
- **Separate service registration from facility approval**. MIC / VTA registration rules prove the provider/service category, while provincial planning and construction sources prove the physical project.
- **Separate investment MoU from approved project**. `ký kết hợp tác`, `MOU`, `đề xuất`, and `xúc tiến đầu tư` are **C/B** leads until an official approval, IRC, land allocation, construction start, or power connection appears.
- **Use 2025 administrative aliases**. For every old manifest division, search old and new names. Record the old manifest division for output, but keep the current official province/city name in notes.
- **Vietnamese diacritics matter**. Search with and without diacritics: `trung tâm dữ liệu`, `trung tam du lieu`, `Hòa Lạc`, `Hoa Lac`, `Tân Thuận`, `Tan Thuan`, `Tân Phú Trung`, `Tan Phu Trung`.
- **Capacity confidence is separate from existence confidence**. An operator page may be **A** for existence but **B/C** for future MW if the number is marketed roadmap rather than approved design or power capacity.
- **Industrial-park location is often the best exact locator**. Lot numbers and zones such as `Lô VA02C-03A`, `SHTP`, `Khu chế xuất Tân Thuận`, and `Khu công nghiệp Tân Phú Trung` are more reliable than generic city names.

---

## 7. Minimal Record Checklist

For each candidate, store:
- Manifest division and current official province/city alias.
- Project name, Vietnamese name, and operator / legal entity.
- Status: planned / approved / construction / operational / retired / no-project.
- Source chain: at least one A-grade source where possible; otherwise mark B/C and state missing proof.
- Location: city/province, ward/commune/district if old source uses it, industrial/high-tech park, lot/address.
- Capacity fields: MW/MVA/racks/sqm/servers/GPUs, each with source and confidence.
- Approval trail: investment approval/IRC, construction permit, commencement, PCCC, environmental, EVN/power, completion.
- Cloud/colo role: AWS Local Zone / Direct Connect, Azure POP, domestic cloud, colocation, government integrated datacenter, hyperscale AI/GPU campus.

