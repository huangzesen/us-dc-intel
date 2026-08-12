# ST Explorer Industry（行业/媒体/供应商侧方法论）— 圣多美和普林西比（Sao Tome and Principe）数据中心枚举

国家：**ST Sao Tome and Principe / São Tomé e Príncipe / 圣普**。范围为行业、运营商、媒体、供应商与目录侧发现。行政覆盖必须匹配 `world-manifest.jsonl` 的 7 个分区：**Agua Grande、Cantagalo、Caue、Lemba、Lobata、Me-Zochi、Principe**；每条记录叠加城镇子层。不要使用清单外拼写作为行政层。

行业侧目标是从运营商、海缆、新闻、设备商、采购和目录中发现种子，再回到官方/一手证据核验。圣普市场很小，诚实预期是 **1 个 A 级政府 Data Center 种子（INIC）+ 少量运营商/银行/海缆/Príncipe PoP lead**，不是商业 colo 市场。

## 0. 行业基线（Verified industry baseline）

- **INIC 是优先种子**：`https://inic.gov.st/ler_mais.php?id=97` 官方服务页列出 Data Center，并列出 Backup、Pasta Partilhada、Alojamento & VPS、Gestão gov.st、Email Institucional、VPN 等。INIC 地址在 São Tomé 市政府/总理府楼宇。行业枚举时应先围绕 INIC、gov.st、Portal Único、World Bank P177158、INE census hosting 查证。
- **CST**：`https://cst.st/` 可访问。DCD 2023 报道 CST 已在全国所有 districts 推出 4G，102 antennas/34 locations 覆盖 90%+ 人口；Developing Telecoms 2022 报道 CST 在固定服务中占 100% 份额并持有 STP Cabo 相关权益。以上证明运营商和网络覆盖，不自动证明商业 DC。
- **Unitel STP**：`https://www.unitel.st/` 可访问。Expansão 2014 报道 Unitel STP 技术启动包括 **Centro de Comutação**，许可证来自 AGER 主导的第二 GSM 运营商流程；DCD 2023 报道 Unitel STP 经 AGER 批准在 São Tomé 推出 4G。该交换中心是电信设施 lead，非 DC，除非一手材料说明托管/服务器数据中心。
- **AGER**：`https://ager.st/` 是当前监管机构。行业媒体提到 telecom regulator 时，应统一映射为 AGER，并回查 AGER 官方公告。
- **ACE/STP Cabo**：ACE 官方页确认 São Tomé and Príncipe landing；World Bank P177158 说明 STP Cabo 是 PPP/SPV，管理 ACE landing station 和国家容量份额，股份最终主要由 CST/Unitel 持有。该信息是连通性和海缆登陆站事实，不是 DC 事实。
- **2Africa**：官方有效站为 `https://www.2africacable.net/`，其首页称 core system complete/landed in most landing countries；`.com` 返回 lander，不可引用。当前文本检索未直接核到 ST landing，因此行业侧只作 C 级 lead/负向控制，直到 TeleGeography、2Africa map 或系统方公告点名 ST。
- **World Bank Digital STP P177158**：说明 Príncipe 依赖两条微波链路、将评估/建设岛际海缆；说明 census data 将托管在 INIC national data center。这使 INIC 为 A 级设施种子，也解释 Principe PoP/edge lead。
- **无超大规模云区域/无公开第三方 colo**：AWS/Azure/GCP/OCI 官方区域页未列出 ST；目录、VPS、代理商页面只给 C 级种子。

## 1. 来源分级（Industry reliability grading）

- **A**：运营商/系统方/认证/政府/多边机构一手材料，如 INIC、CST、Unitel、AGER、ACE、2Africa official `.net`、World Bank、AWS/Azure/GCP/OCI。
- **B**：可靠媒体或行业媒体，有日期、地点、当事方。例如 DCD、Developing Telecoms、Expansão、Lusa、Téla Nón、STP-Press、Capacity Media、TechAfrica News、TeleGeography 新闻。
- **C**：目录、SEO 托管商、承包商作品集、社交账号、地图 POI、无地址/无设施证据报道。C 级不能独立创建 confirmed DC。

## 2. 优先扫描对象（Priority operator and infrastructure sweep）

| 对象 | 来源路线 | Division / town | 当前等级 | 动作 |
|---|---|---|---|---|
| INIC Data Center / government hosting | INIC 官方服务页；World Bank P177158；gov.st/Portal Único；INE census hosting | Agua Grande / São Tomé | **A** | 作为首要设施种子；补地址、服务范围、建设/采购文件；容量 null |
| CST core network / hosting lead | CST 官网、DCD、Developing Telecoms、AGER、World Bank | Agua Grande / São Tomé；全国基站覆盖 | B/C until official DC service | 搜 `hosting/alojamento/centro de dados/NOC`; 不因 4G/光纤自动升级 |
| Unitel STP switching center | Unitel 官网、AGER、Expansão 2014、DCD 2023 | Agua Grande / São Tomé（核实） | B lead | “Centro de Comutação” 标 telecom facility lead；找官方地址/许可 |
| STP Cabo / ACE landing station | ACE official、World Bank P177158、TeleGeography/Submarine Cable Map | Agua Grande / São Tomé | A connectivity | 建连通性记录；只有托管/服务器证据才升级 |
| BCSTP IT/payment systems | BCSTP 官网、采购、年报、World Bank payment-system projects | Agua Grande / São Tomé | C lead | 需要央行一手文件 |
| Commercial bank server rooms | BISTP/other bank sites、BCSTP bank list、procurement | Agua Grande / São Tomé | C lead | 机构机房，不公开时不登记 |
| Príncipe PoP / inter-island endpoint | World Bank P177158、Governo Regional do Príncipe、CST/Unitel | Principe / Santo António | B/C lead | 只记录 telecom/edge lead，非 DC |
| 2Africa possible ST landing | 2Africa official `.net` map/text、TeleGeography、system partner news | 未确认 | C lead | 未点名 ST 前不得确认 |

## 3. 行业与媒体来源（Industry and media roster）

| 来源 | URL/检索途径 | 用途 | 等级 |
|---|---|---|---|
| INIC | `https://inic.gov.st/` | 政府 Data Center、VPS、gov.st、政府网络 | A |
| CST | `https://cst.st/` | 在位运营商、光纤、企业服务、海缆相关 | A for CST claims |
| Unitel STP | `https://www.unitel.st/` | 第二运营商、4G、交换中心 lead | A for Unitel claims |
| AGER | `https://ager.st/` | 许可证、监管公告、运营商验证 | A |
| World Bank | `https://documents.worldbank.org/` | Digital STP、INIC national data center、ACE/STP Cabo、Príncipe connectivity | A |
| ACE | `https://ace-submarinecable.com/en/submarine-cable/` | São Tomé landing and RFS | A |
| 2Africa | `https://www.2africacable.net/` | official system status/map | A where explicit; ST not yet text-verified |
| DCD | `https://www.datacenterdynamics.com/` | CST/Unitel 4G and broader African infra news | B |
| Developing Telecoms | `https://developingtelecoms.com/` | CST ownership, telecom market | B |
| Expansão | `https://expansao.co.ao/` | Unitel STP launch and Centro de Comutação | B |
| Téla Nón / STP-Press / Lusa | search by domain | Local politics, telecom, procurement, power | B |
| Submarine Cable Map / Submarine Networks | `https://www.submarinecablemap.com/`, `https://www.submarinenetworks.com/` | cable status/landing cross-check | B unless system-owner source |
| directories | Datacenters.com, DataCenterMap, PeeringDB, BuiltWith, VPS lists | seed discovery only | C |

## 4. 查询模板（Search templates）

运营商/政府：

```text
INIC ("Data Center" OR "centro de dados" OR "Alojamento" OR VPS OR Backup) ("São Tomé" OR "Sao Tome")
site:inic.gov.st ("Data Center" OR "centro de dados" OR "Alojamento & VPS" OR "Gestão gov.st")
CST OR "Companhia Santomense de Telecomunicações" ("data center" OR "centro de dados" OR hosting OR alojamento OR fibra)
site:cst.st ("data center" OR "centro de dados" OR hosting OR alojamento OR fibra OR "cabo submarino")
"Unitel STP" OR "Unitel São Tomé" ("Centro de Comutação" OR "data center" OR "centro de dados" OR fibra OR 4G)
site:unitel.st ("centro de dados" OR "Centro de Comutação" OR fibra OR cobertura)
site:ager.st (CST OR Unitel OR "STP Cabo" OR licença OR autorização OR telecomunicações)
```

媒体/行业：

```text
site:datacenterdynamics.com ("São Tomé" OR "Sao Tome" OR "CST" OR "Unitel")
site:developingtelecoms.com ("São Tomé" OR "Sao Tome" OR CST OR Unitel)
site:telanon.info ("centro de dados" OR telecom OR CST OR Unitel OR fibra OR "cabo submarino")
site:stp-press.st ("centro de dados" OR telecom OR energia OR concurso OR INIC)
site:expansao.co.ao ("São Tomé" OR "Sao Tome") (Unitel OR telecom OR "Centro de Comutação")
```

海缆/PoP：

```text
"STP Cabo" ("ACE" OR "landing station" OR "cabo submarino" OR capacidade)
ACE ("São Tomé" OR "Sao Tome") (landing OR "cabo submarino" OR "STP Cabo")
2Africa ("São Tomé" OR "Sao Tome" OR "São Tomé e Príncipe") (landing OR "cable landing station" OR planned)
("São Tomé" OR "Sao Tome") ("Príncipe" OR Principe) ("microwave link" OR "inter-island cable" OR "cabo inter-ilhas" OR fibra)
site:submarinenetworks.com ("São Tomé" OR "Sao Tome" OR ACE OR 2Africa)
```

供应商/采购：

```text
(Huawei OR ZTE OR Ericsson OR Nokia) "São Tomé e Príncipe" (telecom OR rede OR "core network" OR fibra OR 4G OR 5G)
(Schneider OR Vertiv OR ABB OR Caterpillar OR Cummins OR Siemens) "São Tomé e Príncipe" (gerador OR UPS OR energia OR "data center" OR "centro de dados")
"São Tomé e Príncipe" ("fornecimento e montagem" OR "chave na mão" OR empreitada) (servidores OR "centro de dados" OR telecom OR fibra)
"São Tomé e Príncipe" (concurso público OR licitação) (informática OR servidores OR hosting OR "centro de dados" OR energia)
```

负向控制：

```text
"São Tomé e Príncipe" (AWS OR Azure OR "Google Cloud" OR OCI) ("data center" OR region OR região)
"Sao Tome" "data center" -"São Tomé e Príncipe"
"STP" "data center" -"São Tomé"
"São Tomé e Príncipe" ("cloud hosting" OR VPS OR "dedicated server") -"inic.gov.st"
```

## 5. 分区枚举矩阵（Enumeration matrix）

| Manifest division | 官方/监管 | 运营商/海缆 | 媒体/供应商 | 预期产量 |
|---|---|---|---|---|
| **Agua Grande** | INIC, gov.st, AGER, BCSTP, EMAE | CST, Unitel, ACE/STP Cabo | DCD, Developing Telecoms, Expansão, suppliers | 1 confirmed seed + 0-2 lead + connectivity |
| **Lobata** | EMAE, county permits | CST/Unitel coverage | local media | 0 DC unless direct source |
| **Lemba** | EMAE, county permits | coverage/PoP lead | local media | 0 DC |
| **Me-Zochi** | government/education/health IT lead | coverage/PoP lead | procurement | 0-1 institutional lead only |
| **Cantagalo** | county permits | coverage lead | low | 0 DC |
| **Caue** | county permits | coverage lead | low | 0 DC |
| **Principe** | regional government, World Bank inter-island project | CST/Unitel microwave/PoP; future cable endpoint | local/media lead | 0 DC; PoP/edge lead |

## 6. 目录到一手证据流程（Directory-to-primary workflow）

1. 目录只取种子：Datacenters.com、DataCenterMap、PeeringDB、BuiltWith、VPS/hosting lists、LinkedIn/company pages。
2. 对每个种子回查 `inic.gov.st`、`cst.st`、`unitel.st`、`ager.st`、`stp.gov.st`、`bcstp.st`、World Bank、ACE/2Africa official。
3. 要求至少一个一手证据落到设施/服务/地址/状态；否则保留 C 级 lead。
4. 海缆、PoP、交换中心、基站、发电机、变电站默认不是 DC。
5. 字段中始终记录 `division` 的 manifest spelling；城镇写在 locality/town 字段。
6. 无一手容量时：`capacity_mw: null`、`racks: null`、`area_sqm: null`、`tier: null`。

## 7. 葡语术语表（Portuguese terminology）

| 中文 | 葡语 | 英语 |
|---|---|---|
| 数据中心 | centro de dados / centro de processamento de dados / Data Center | data center / datacenter / data centre |
| 服务器机房 | sala de servidores | server room |
| 托管/主机服务 | alojamento / hospedagem / VPS | hosting / VPS |
| 主机托管 | colocação | colocation / colo |
| 政府门户管理 | gestão gov.st | government domain management |
| 备份 | cópia de segurança / backup | backup |
| 光纤 | fibra óptica | fiber / fibre |
| 海缆 | cabo submarino | submarine cable |
| 登陆站 | estação de aterragem / estação de cabos | landing station |
| 交换中心 | centro de comutação | switching center |
| 网络运营中心 | centro de operações de rede | NOC |
| 发电机 | gerador / grupo gerador | generator |
| 不间断电源 | UPS / fonte de alimentação ininterrupta | UPS |
| 变电站 | subestação | substation |
| 招标 | concurso público / licitação | tender |
| 交钥匙 | chave na mão | turnkey |

## 8. 行业侧判断规则（Decision rules）

- INIC 官方 Data Center 服务可作 A 级设施种子；但容量、Tier、机柜数必须留空，除非找到明确文件。
- Unitel “Centro de Comutação”、CST 核心网、Príncipe 微波/PoP 是 telecom facility lead，不自动等于 DC。
- ACE landing / STP Cabo 是 connectivity record；只有同一站点托管服务器、colo 或 data center 服务时才升级。
- 2Africa ST landing 未经当前文本来源核实；用 `.net` 官方地图、TeleGeography 或系统方公告确认前保持 C 级。
- AWS/Azure/GCP/OCI 只引用官方区域列表；本地客户、转售商和 CDN 页面不证明本地云区域。
- 分区覆盖要完整：7 个 manifest divisions 均需记录已查来源和未发现公开 DC 的负向结论。
