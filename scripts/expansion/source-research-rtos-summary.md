# RTO/ISO 互联队列组调研摘要

范围：brief #6-10，覆盖 ERCOT、PJM、MISO、SPP，以及 NYISO / ISO-NE / CAISO / SERC。所有可访问性判断均基于本轮 `curl` 实测；ERCOT GIS 报告已优先测试到文件下载层。

## 结论

可直接作为 planned 层高优先级项目级来源：

- ERCOT GIS Report：公开页面、报告列表 JSON、XLSX 下载均可用；最新实测文件为 `GIS_Report_July2026`，工作簿显示截至 2026-07-31 跟踪 1906 个 generation interconnection/change requests。
- PJM Service Request Status：旧 brief URL 已失效，但当前页面和 Planning API 可用；需从页面 JS 取得公开 `api-subscription-key` 并带 Referer/Origin 调用 API。实测 `totalRows=9263`。
- MISO GI Interactive Queue：旧 brief URL 已失效；当前 JSON API `https://www.misoenergy.org/api/giqueue/getprojects` 可直接全量获取，实测 3806 条。
- SPP GI Active Requests：`opsportal.spp.org/Studies/GIActive` 返回单个大型 HTML 表，实测约 1029 条项目行。
- NYISO Interconnection Queue：直链 XLSX 可下载，含 active/withdrawn/in-service 三张表，实测 301 + 1487 + 153 行。需要在生产抓取中监控文件 freshness，因为 HEAD 文件名/Last-Modified 显示为 2024。
- CAISO Public Queue Report：直链 `publicqueuereport.xlsx` 可下载，Last-Modified 为 2026-08-11，含 active/completed/withdrawn 三张表，实测 273 + 255 + 1765 行。
- ISO-NE IRTT Public Queue：公开可取，但需要 cookie jar 处理 ASP.NET cookie 探测；`curl -L -c cookies -b cookies` 后返回 200，HTML 内含项目表和 Excel export 链接，实测 1751 条项目行。

不建议作为统一队列源：

- SERC：官网公开可访问，但 SERC 是区域可靠性实体，不运营统一项目级 interconnection queue。SERC 区域内 planned 项目应转向成员 utility / TO / OASIS 队列。

## 抓取优先级

1. ERCOT、CAISO、NYISO：优先实现 XLSX 下载解析。字段完整，包含名称、位置、容量、状态/阶段、日期；ERCOT 和 CAISO freshness 较好。
2. MISO、PJM：优先实现 API 抓取。MISO 是直接 JSON；PJM 需要页面 JS 中的公开 key 和正确 headers，建议把 key 发现步骤自动化而不是硬编码。
3. SPP、ISO-NE：HTML 表可解析；ISO-NE 另有 Excel export，生产实现建议优先测试 export，失败时回退 HTML 表解析。
4. SERC：从 RTO/ISO 统一源清单中降级为“区域提示/覆盖缺口”，后续另开 utility queue 组补齐。

## 实测访问方式

- ERCOT：`curl -L https://www.ercot.com/mp/data-products/data-product-details?id=PG7-200-ER`，解析 `reportTypeID=15933`；随后 `curl -L https://www.ercot.com/misapp/servlets/IceDocListJsonWS?reportTypeId=15933`；最后用 `doclookupId=1258020955` 下载 `GIS_Report_July2026`。
- PJM：`curl -L https://www.pjm.com/planning/service-requests/serial-service-request-status`，解析 JS 中 API base/key；调用 `https://services.pjm.com/PJMPlanningApi/api//Queue/GetFilteredQueues?`。
- MISO：`curl -L https://www.misoenergy.org/api/giqueue/getprojects`。
- SPP：`curl -L https://opsportal.spp.org/Studies/GIActive`。
- NYISO：`curl -L https://www.nyiso.com/documents/20142/1407078/NYISO-Interconnection-Queue.xlsx/f615d83e-eea6-ccf6-ec07-b4ecbe78d8ef`。
- ISO-NE：`curl -L -c cookies.txt -b cookies.txt https://irtt.iso-ne.com/reports/external`。
- CAISO：`curl -L https://www.caiso.com/documents/publicqueuereport.xlsx`。
- SERC：`curl -L https://www.serc.org/`，未发现统一项目级队列入口。

## 主要注意事项

- 多个 XLSX 源使用 Excel serial date，需要统一日期归一化。
- PJM 的旧 URL 和 MISO 的旧 URL 已失效，应在源清单中记录 current URL 与 stale URL 的替换关系。
- PJM API 的 key 看起来是页面内公开订阅 key，但仍建议生产抓取动态解析页面 JS，减少 key 轮换风险。
- ISO-NE 的普通 `curl -L` 会因 `AspxAutoDetectCookieSupport` 重定向卡住；抓取器必须启用 cookie jar。
- SERC 不应强行标为项目级 planned source；否则会引入空源或误导覆盖率。
