# USDC-0027 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Beale announced a phased campus in April 2026 and describes site preparation, power, water, sewer, and a public Evergy substation
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：由 announcement/local-process 表述提升为 `site work-construction`。De Soto 官方 Beale project page 载明 Phase 1（Buildings 1 and 2）site plan 已获 City conditional approval，grading 和 early site preparation underway；同页列出 Flint Commerce Center（103rd & Edgerton Rd.）、up to four buildings、约 $3.1B private investment、2026 construction target、约 2035 phased buildout。来源：https://www.desotoks.us/496/Beale-Data-Center
- 增补 2025-08-21 市政动作：De Soto project page 称 City Council approved Development Agreement with Mount Sunflower, LLC and IRB intent；执行版 Development Agreement 载明该协议于 2025-08-21 presented to and approved by City Council，协议 made as of 2025-09-23。该动作证明 development agreement / incentive framework，不等同于 building permit、CO 或 energized service。来源：https://www.desotoks.us/496/Beale-Data-Center ；https://www.desotoks.us/DocumentCenter/View/3805/Final-Development-Agreement-De-Soto---Mount-Sunflower
- 增补 site-work 媒体佐证：KCUR / Johnson County Post 于 2026-07-09 报道 work officially underway、construction began in April、Planning Commission approved scope changes in April and May，并称项目由四栋楼扩大至 nearly 2.9M sq ft；该来源佐证施工/范围变化，但 official city page 仍为控制性状态来源。来源：https://www.kcur.org/housing-development-section/2026-07-09/de-soto-data-center-complaints-beale-infrastructure
- owner 字段补为 Beale Infrastructure / Mount Sunflower Properties, LLC（developer/project entity）；tenant/operator 仍未公开。De Soto 官方 FAQ 仍称 operator 是 single large U.S.-based technology company and will be announced at groundbreaking；本次未找到公开 tenant/operator 披露。来源：https://www.desotoks.us/496/Beale-Data-Center
- capacity_mw 保持 `null`：De Soto 官方页、Development Agreement、Beale 项目页和检索到的本地媒体均未给出可核实 campus MW 容量；只确认 Evergy service / public substation / LLPS rate context / square footage。Beale 项目页称 electric service provided by Evergy and new public Evergy substation; KCC 2025-11-06 announcement confirms LLPS applies to customers requiring greater than 75 MW peak power, but that is tariff eligibility context, not this project's confirmed capacity。来源：https://bealeinfra.com/location/de-soto/ ；https://www.kcc.ks.gov/news-11-6-25
- 冲突/不足：官方 city page 的 Phase 1 completion target 为 2027，但 Beale project page timeline shows Phase 1 Completion at 2029 and local reporting cites 2028/2029 variants; 未写入硬性 completion date。未找到 building permit number、inspection、certificate of occupancy、energization、commissioning、live-service 或 confirmed MW record。
