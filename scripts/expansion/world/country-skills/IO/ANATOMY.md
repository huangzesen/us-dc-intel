# IO · Country Anatomy

Datacenter-country knowledge layer for British Indian Ocean Territory (IO).

## Files

| Path | Status | Note |
|---|---|---|
| SKILL.md | present | Country-level skill: 双线方法论（官方/监管/云管线 + 行业/厂商/媒体发现），预期产出 0（军事/基地通信与 .io TLD 均排除），由两份 explorer 合并而来 |
| explorer-official.md | present | 官方/监管/云管线：GOV.UK BIOT、BIOT Administration、FCDO travel advice、UK legislation、UK/Mauritius treaty、U.S. Navy NSF Diego Garcia、云厂商区域负表、`.io` ccTLD IANA 排除、海缆/IXP/公用事业负核 |
| explorer-industry.md | present | 行业/厂商/媒体发现：DCD/Reuters/BBC、TeleGeography/Submarine Cable Map、目录（Data Center Map、datacenters.com、Cloudscene、PeeringDB、IXPDB）、云/CDN/边缘负核、海缆军事连接性背景、承包商/国防 IT 排除、`.io` TLD 误判过滤 |
| divisions/ | — | division 层未建；IO 为单一 division 领地，规划在 divisions/british-indian-ocean-territory/ 下建 sub-location 笔记 |

## Division layer (future)

- manifest 已核验：`subnational_type: country`，`divisions: ["British Indian Ocean Territory"]`；IO 按整个领地枚举，不拆分环礁或岛礁。
- 已确认记录使用 `division: British Indian Ocean Territory`；Diego Garcia 仅作 locality/背景字段（公开有人活动集中地），永远不作 division。
- 规划：创建 `divisions/british-indian-ocean-territory/` 时，在子层笔记中沉淀负向核验纪律（军事/基地通信与 `.io` TLD 排除、0 产出模板、UK/Mauritius treaty 状态监控）。
