import sqlite3, shutil, re
DB='datacenters.db'
shutil.copy(DB, DB+'.bak-20260813-status-norm')
conn=sqlite3.connect(DB); cur=conn.cursor()
rows=cur.execute('SELECT status, COUNT(*) FROM centers GROUP BY status').fetchall()

def norm(s):
    if s is None: return None
    t=str(s).strip(); tl=t.lower()
    canon={'operational','planned','construction','approved','announced','unknown','rejected','coverage'}
    if tl in canon: return tl
    if tl in ('operating','operational_phase1','operational_partial','partial_operational','construction_completed','completed','existing_campus'): return 'operational'
    if tl=='under_construction': return 'construction'
    if tl in ('coverage_note','none_found','no_direct_evidence','no_projects_found','rumor'): return 'unknown'
    # completion markers
    if any(k in tl for k in ['已建成','已投','已投产','建成投运','已启用','已投用','建成运营','已开通','开服','已交付']): return 'operational'
    if any(k in tl for k in ['在建','建设中','施工','开工','封顶','土建','破土','under_construction','construction']): return 'construction'
    if any(k in tl for k in ['运营','投运','投产','启用','operational','operating','completed']): return 'operational'
    if any(k in tl for k in ['批准','批复','核准','许可','签约','备案','approved','greenlit']): return 'approved'
    if any(k in tl for k in ['宣布','公布','公告','announced']): return 'announced'
    if any(k in tl for k in ['规划','计划','拟建','前期','储备','招标','采购','planned','proposed','procurement','pipeline']): return 'planned'
    if any(k in tl for k in ['排除','未发现','无','no_','none','rejected','拒绝','否决','搁置','moratorium']): return 'unknown'
    return 'unknown'

mapping={}; changed=0
for s,cnt in rows:
    n=norm(s)
    mapping[s]=n
    if n!=s:
        cur.execute('UPDATE centers SET status=? WHERE status=?',(n,s))
        changed+=cnt
conn.commit()
# report counts by NEW status
print('=== normalized counts (by new status) ===')
for r in cur.execute('SELECT status, COUNT(*) FROM centers GROUP BY status ORDER BY COUNT(*) DESC'): print(' ',r)
print('=== rows changed:', changed)
# show free-text -> mapped
print('=== free-text mappings (non-canonical) ===')
for s,n in sorted(mapping.items()):
    if s not in {'operational','planned','construction','approved','announced','unknown','rejected','coverage'}:
        print(f'  {s!r} -> {n}')
