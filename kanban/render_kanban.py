#!/usr/bin/env python3
"""Render US DC county-exploration kanban as a self-contained HTML page.

Reads the exploration state under scripts/expansion/ and writes kanban/index.html.
Pure stdlib; no network. Truthful: every number is derived from on-disk state.

Usage: python3 kanban/render_kanban.py
"""
import json, os, re, html, datetime, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXP = os.path.join(ROOT, 'scripts', 'expansion')
OUT = os.path.join(ROOT, 'kanban', 'index.html')

STATUS_LABEL = {
    'operational': '运营中 / Operational', 'construction': '在建 / Under Construction', 'planned': '规划 / Planned',
    'approved': '已批准 / Approved', 'announced': '已公告 / Announced', 'rejected': '已否决 / Rejected',
    'unknown': '未知 / Unknown', 'no_projects_found': '未发现 / None Found',
}


def load_jsonl(path):
    rows = []
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        rows.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    return rows


def main():
    now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

    # --- county batches ---
    batch_files = sorted(glob.glob(os.path.join(EXP, 'county-batches', 'batch-*.tsv')))
    batches = []
    for bf in batch_files:
        m = re.search(r'batch-(\d+)\.tsv$', bf)
        idx = int(m.group(1)) if m else -1
        counties = []
        with open(bf, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('\t')
                if len(parts) >= 2:
                    counties.append({'state': parts[0], 'county': parts[1]})
        batches.append({'idx': idx, 'file': os.path.basename(bf), 'counties': counties})
    total_counties = sum(len(b['counties']) for b in batches)

    # --- results (done batches) ---
    result_files = sorted(glob.glob(os.path.join(EXP, 'county-results', 'batch-*-results.jsonl')))
    done_idx = set()
    county_projects = []  # rows with project_name
    county_no_proj = []   # rows with no_projects_found
    for rf in result_files:
        m = re.search(r'batch-(\d+)-results\.jsonl$', rf)
        if m:
            done_idx.add(int(m.group(1)))
        for row in load_jsonl(rf):
            if row.get('project_name'):
                county_projects.append(row)
            elif row.get('status') == 'no_projects_found':
                county_no_proj.append(row)

    done_batches = [b for b in batches if b['idx'] in done_idx]
    done_counties = sum(len(b['counties']) for b in done_batches)
    pending_batches = [b for b in batches if b['idx'] not in done_idx]

    # status buckets from county projects
    status_buckets = {}
    for r in county_projects:
        s = r.get('status', 'unknown')
        status_buckets.setdefault(s, []).append(r)

    # --- state projects ---
    state_projects = []
    for sp in sorted(glob.glob(os.path.join(EXP, 'state-projects', '*-projects.jsonl'))):
        state_projects.extend(load_jsonl(sp))

    # --- research sources ---
    research = []
    for rj in sorted(glob.glob(os.path.join(EXP, 'source-research-*.jsonl'))):
        for row in load_jsonl(rj):
            research.append(row)

    pct = (len(done_batches) / len(batches) * 100) if batches else 0
    county_pct = (done_counties / total_counties * 100) if total_counties else 0

    # --- HTML ---
    cards = []
    for b in pending_batches:
        st = b['counties'][0]['state'] if b['counties'] else '?'
        first = b['counties'][0]['county'] if b['counties'] else ''
        cards.append(f'<div class="card pend"><span class="bidx">batch-{b["idx"]:03d}</span> {html.escape(st)} · {html.escape(first)}{f" 等 {len(b["counties"])} 县" if len(b["counties"])>1 else ""}</div>')
    for b in done_batches:
        st = b['counties'][0]['state'] if b['counties'] else '?'
        n = sum(1 for r in county_projects if r.get('state') == st and r.get('county') in {c['county'] for c in b['counties']})
        cards.append(f'<div class="card done"><span class="bidx">batch-{b["idx"]:03d}</span> {html.escape(st)} · {n} 项目</div>')
    done_cards = []
    for b in done_batches:
        st = b['counties'][0]['state'] if b['counties'] else '?'
        n = sum(1 for r in county_projects if r.get('state') == st and r.get('county') in {c['county'] for c in b['counties']})
        done_cards.append(f'<div class="card done"><span class="bidx">batch-{b["idx"]:03d}</span> {html.escape(st)} · {n} 项目</div>')
    cards_html = '\n'.join(cards) if cards else '<div class="card">（暂无批次）</div>'
    done_cards_html = '\n'.join(done_cards) if done_cards else '<div class="card">（暂无）</div>'

    # state project table (top rows)
    sp_rows = []
    for r in state_projects[:400]:
        cap = r.get('capacity_mw')
        cap_s = f'{cap:g} MW' if isinstance(cap, (int, float)) else (cap or '—')
        yr = r.get('year') or '—'
        sp_rows.append(
            f'<tr><td>{html.escape(r.get("state", ""))}</td>'
            f'<td>{html.escape(r.get("county", "") or "")}</td>'
            f'<td class="pn">{html.escape(r.get("project_name", "") or "")}</td>'
            f'<td>{html.escape(r.get("developer", "") or "")}</td>'
            f'<td>{html.escape(STATUS_LABEL.get(r.get("status", ""), r.get("status", "") or ""))}</td>'
            f'<td>{html.escape(cap_s)}</td><td>{html.escape(str(yr))}</td></tr>')
    sp_html = '\n'.join(sp_rows) if sp_rows else '<tr><td colspan="7">暂无</td></tr>'

    # research table
    rs_rows = []
    for r in research:
        rs_rows.append(
            f'<tr><td>{html.escape(r.get("name", "") or "")}</td>'
            f'<td><a href="{html.escape(r.get("url", "") or "")}">{html.escape(r.get("url", "") or "")}</a></td>'
            f'<td>{"✅" if r.get("accessible") else "❌"}</td>'
            f'<td>{"需要" if r.get("auth_required") else "公开"}</td>'
            f'<td>{html.escape(str(r.get("est_projects", "") or ""))}</td>'
            f'<td>{html.escape(r.get("fetch_method", "") or "")}</td></tr>')
    rs_html = '\n'.join(rs_rows) if rs_rows else '<tr><td colspan="6">暂无</td></tr>'

    # status bucket bars
    bucket_html = ''
    order = ['operational', 'construction', 'planned', 'approved', 'announced', 'rejected', 'unknown']
    for s in order:
        rows = status_buckets.get(s, [])
        if rows:
            bucket_html += f'<div class="bucket"><b>{STATUS_LABEL.get(s, s)}</b> <span class="cnt">{len(rows)}</span></div>'

    html_doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>US Data Center County Exploration Kanban · US 数据中心 county 探索看板</title>
<style>
:root {{ --bg:#0f1420; --card:#171e2e; --line:#26304a; --txt:#dbe4ff; --mut:#7f8db3; --acc:#4f8cff; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--txt); font:14px/1.5 -apple-system,'PingFang SC','Microsoft YaHei',sans-serif; }}
.wrap {{ max-width:1200px; margin:0 auto; padding:24px; }}
h1 {{ font-size:22px; margin:0 0 4px; }}
.sub {{ color:var(--mut); margin-bottom:20px; }}
.metrics {{ display:flex; flex-wrap:wrap; gap:12px; margin-bottom:20px; }}
.metric {{ background:var(--card); border:1px solid var(--line); border-radius:12px; padding:14px 18px; min-width:150px; }}
.metric .v {{ font-size:26px; font-weight:700; color:var(--acc); }}
.metric .l {{ color:var(--mut); font-size:12px; }}
.bar {{ height:10px; background:#0b0f1a; border:1px solid var(--line); border-radius:6px; overflow:hidden; margin:6px 0 2px; }}
.bar > div {{ height:100%; background:linear-gradient(90deg,#4f8cff,#63d3ff); }}
.sec {{ margin-top:28px; }}
.sec h2 {{ font-size:16px; border-bottom:1px solid var(--line); padding-bottom:6px; }}
.board {{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }}
.board .col {{ background:var(--card); border:1px solid var(--line); border-radius:12px; padding:12px; }}
.board .col h3 {{ margin:0 0 8px; font-size:13px; color:var(--mut); }}
.card {{ border:1px solid var(--line); border-radius:8px; padding:6px 8px; margin-bottom:6px; font-size:12px; }}
.card.pend {{ color:var(--mut); }}
.card.done {{ color:#9ef0c0; }}
.bidx {{ font-family:ui-monospace,Menlo,monospace; color:var(--acc); margin-right:6px; }}
.buckets {{ display:flex; flex-wrap:wrap; gap:8px; margin:8px 0; }}
.bucket {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:6px 10px; font-size:12px; }}
.bucket .cnt {{ color:var(--acc); font-weight:700; }}
table {{ width:100%; border-collapse:collapse; font-size:12px; }}
th,td {{ border-bottom:1px solid var(--line); padding:6px 8px; text-align:left; vertical-align:top; }}
th {{ color:var(--mut); font-weight:500; }}
td.pn {{ max-width:260px; }}
a {{ color:#63d3ff; text-decoration:none; word-break:break-all; }}
.foot {{ color:var(--mut); font-size:11px; margin-top:30px; }}
</style>
</head>
<body>
<div class="wrap">
  <h1>US Data Center County Exploration Kanban · US 数据中心 county 探索看板</h1>
  <div class="sub">Goal: explore every US county to build the widest data-center superset · 目标：全美 3,000+ county 逐一探索，构建最宽口径数据中心超集清单 · Rendered 渲染于 {html.escape(now)}</div>

  <div class="metrics">
    <div class="metric"><div class="v">{total_counties}</div><div class="l">Total US counties · 全美 county 总数</div></div>
    <div class="metric"><div class="v">{len(batches)}</div><div class="l">Exploration batches (10 per batch) · 探索批次（每批 10 县）</div></div>
    <div class="metric"><div class="v">{len(done_batches)}</div><div class="l">Completed batches · 已完成批次</div><div class="bar"><div style="width:{pct:.1f}%"></div></div><div style="font-size:11px;color:var(--mut)">{pct:.1f}%</div></div>
    <div class="metric"><div class="v">{done_counties}</div><div class="l">Counties explored · 已完成 county</div><div class="bar"><div style="width:{county_pct:.1f}%"></div></div><div style="font-size:11px;color:var(--mut)">{county_pct:.1f}%</div></div>
    <div class="metric"><div class="v">{len(county_projects)}</div><div class="l">Projects found (county) · county 探索发现项目</div></div>
    <div class="metric"><div class="v">{len(state_projects)}</div><div class="l">State-level projects · 州级探索项目</div></div>
    <div class="metric"><div class="v">{len(research)}</div><div class="l">Data sources researched · 数据源调研条目</div></div>
  </div>

  <div class="sec">
    <h2>Status distribution (county finds, first 30 batches) · 探索进度状态分布（county 发现，前 30 批）</h2>
    <div class="buckets">{bucket_html}</div>
  </div>

  <div class="sec">
    <h2>Batch board · 批次看板（Done 已完成 {len(done_batches)} / Total 总 {len(batches)}）</h2>
    <div class="board">
      <div class="col"><h3>⏳ Pending / In progress 待探索 / 探索中（{len(pending_batches)} 批）</h3>{cards_html}</div>
      <div class="col"><h3>✅ Completed 已完成（{len(done_batches)} 批）</h3>{done_cards_html}</div>
    </div>
  </div>

  <div class="sec">
    <h2>State-level projects 州级探索项目（{len(state_projects)} rows 条，showing first 400 显示前 400）</h2>
    <table><thead><tr><th>State 州</th><th>County 县</th><th>Project 项目</th><th>Developer 开发商</th><th>Status 状态</th><th>Capacity 容量</th><th>Year 年份</th></tr></thead><tbody>{sp_html}</tbody></table>
  </div>

  <div class="sec">
    <h2>Data source research 数据源调研（{len(research)} entries 条）</h2>
    <table><thead><tr><th>Name 名称</th><th>URL</th><th>Access 可访问</th><th>Auth 认证</th><th>Est. projects 估计项目数</th><th>Fetch 抓取方式</th></tr></thead><tbody>{rs_html}</tbody></table>
  </div>

  <div class="foot">Rendered by dev4bot · 由 dev4bot 自动渲染 · Data from scripts/expansion/ · 数据来自 scripts/expansion/ · Powered by LingTai AI: https://github.com/Lingtai-AI/lingtai</div>
</div>
</body>
</html>'''

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(html_doc)
    print(f'wrote {OUT}')
    print(f'total_counties={total_counties} batches={len(batches)} done={len(done_batches)} ({pct:.1f}%) done_counties={done_counties} county_projects={len(county_projects)} state_projects={len(state_projects)} research={len(research)}')


if __name__ == '__main__':
    main()
