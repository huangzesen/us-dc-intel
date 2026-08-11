# GRIDWATCH · 项目结构导航 ANATOMY

> 约定：本文件是项目导航图（仿灵台 ANATOMY 体系）。找模块/代码/契约先看这里；每个文件夹有自己的 `SKILL.md` 说明职责，`SKILL.md` 是行为契约，`ANATOMY.md` 是结构地图。

## 顶层结构

```
us-dc-intel/
├── SKILL.md                 # 顶层方法论：项目是什么/怎么更新/边界（先读这个）
├── ANATOMY.md               # 本文件：结构导航
├── README.md                # 人读的欢迎页
├── dc/<slug>/               # 每个数据中心一个目录（240 baseline + 32 discovery + 候选）
│   ├── SKILL.md             #   看护契约（数据源/字段/验证）
│   ├── data.json            #   结构化基线
│   └── NOTES.md             #   历次更新记录
├── scripts/                 # 数据管线（探索/合并/导出）
│   ├── generate_skeleton.py #   从 baseline 生成 dc/ 骨架
│   ├── merge_all_sources.py #   幂等合并全源 → centers.jsonl + datacenters.db
│   ├── export_astro_data.py #   导出 Astro 数据包（构建时）
│   ├── discovery-brief.md   #   补漏发现契约
│   ├── refresh-brief.md     #   刷新契约
│   └── expansion/           #   探索批次输入/结果/清单
│       ├── county-batches/  #   美国 county 批次（323 批）
│       ├── county-results/  #   美国 county 结果（323 文件）
│       ├── state-projects/  #   州级项目
│       └── americas/        #   美洲二级行政区清单（探索中）
├── merge-output/            # 合并产物 centers.jsonl
├── datacenters.db           # SQLite：centers + source_urls（2,731 中心）
├── kanban/                  # 静态看板（当前线上版）
│   ├── render_kanban.py     #   renderer → index.html
│   └── index.html           #   自包含单文件看板
├── design/                  # GRIDWATCH 设计
│   ├── design-proposal.md   #   设计提案（配色/排版/组件）
│   └── design-mockup.html   #   已批准的可交互 mockup（设计规格）
├── astro/                   # 正式站（Astro 静态站，GRIDWATCH 实现）
│   ├── SKILL.md             #   站点维护契约
│   └── src/                 #   组件/数据/样式
├── legacy-baseline-20260716/# 7/16 冻结基线（codex 衡枢 208 masters）
└── taskcard/                # 本地探索追踪（daemon 派发脚本/状态）
```

## 数据流

```
探索 daemon（每行政区）
  → scripts/expansion/**/ 结果 JSONL
  → scripts/merge_all_sources.py（去重/规范）
  → merge-output/centers.jsonl + datacenters.db
  → scripts/export_astro_data.py → astro/src/data/datacenters.json
  → astro/ npm run build → dist/
  → 部署（GitHub Pages 路径 /datacenters/）
```

## 契约与责任矩阵

| 模块 | 责任 | 契约文件 |
|---|---|---|
| `SKILL.md`（顶层） | 项目方法论/更新流程/边界 | 自身 |
| `dc/<slug>/` | 单中心数据真源 | 每中心 `SKILL.md` |
| `scripts/` | 探索/合并/导出管线 | `scripts/SKILL.md` |
| `kanban/` | 静态看板渲染 | `kanban/SKILL.md` |
| `design/` | 视觉设计规格 | `design/SKILL.md` |
| `astro/` | 正式站实现与构建 | `astro/SKILL.md` |
| `legacy-baseline-20260716/` | 冻结基线（只读） | `legacy-baseline-20260716/SKILL.md` |

## 变更纪律

- 跨模块改动先读目标 `SKILL.md` 与相关 `ANATOMY.md` 引用；不重复造轮子
- 结构事实（文件/目录/调用）以本 ANATOMY 为准；若代码与文档不符，更新文档并记录偏差
- 新增模块时必须同时补：目录 `SKILL.md` + 本文件条目 + 顶层 `SKILL.md` 路由表

## 维护契约

- 本文件是项目结构事实的准；任何文件/目录/调用变动后必须同步更新，代码与文档不符时以代码为准并更新本文件且记录偏差。
- 新增/移除模块、改变数据流、调整责任矩阵时，此处为必更项（跟顶层 `SKILL.md` 一起）。

## 相关文件

- `SKILL.md`（顶层方法论/路由）
- `scripts/SKILL.md`、`kanban/SKILL.md`、`design/SKILL.md`、`astro/SKILL.md`、`legacy-baseline-20260716/SKILL.md`（各模块手册）
- `README.md`（公开入口）
- `scripts/expansion/americas/explore-brief.md` + `americas-manifest.jsonl`（探索契约/清单）
