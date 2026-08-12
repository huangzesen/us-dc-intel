import json, collections
base = '/Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/world/results-method/'
for f in ['batch-276.jsonl', 'batch-277.jsonl']:
    recs = [json.loads(l) for l in open(base+f) if l.strip()]
    bydiv = collections.OrderedDict()
    for r in recs:
        d = r['division']
        bydiv.setdefault(d, []).append(r)
    print('='*20, f, 'total', len(recs))
    for d, rs in bydiv.items():
        proj = [r['name'] for r in rs if 'no_projects' not in r]
        np_ = any('no_projects' in r for r in rs)
        print(f'  {d}: {len(proj)} projects' + (' (no_projects)' if np_ else '') + (' | ' + '; '.join(proj[:4]) + ('...' if len(proj)>4 else '') if proj else ''))
