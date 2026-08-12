import json, sys

def check(path, divisions):
    print('==', path)
    lines = open(path, encoding='utf-8').read().split('\n')
    lines = [l for l in lines if l.strip()]
    seen = set()
    problems = 0
    for i, l in enumerate(lines, 1):
        try:
            o = json.loads(l)
        except Exception as e:
            problems += 1
            print('  LINE', i, 'JSON ERROR:', e)
            print('  snippet:', repr(l[:300]))
            continue
        seen.add(o.get('division'))
        if o.get('country_code') != 'IN':
            problems += 1; print('  LINE', i, 'bad country_code')
        if 'no_projects' in o:
            if 'name' in o:
                problems += 1; print('  LINE', i, 'no_projects with name')
        else:
            for k in ('name','status','capacity_mw','developer','source_urls','evidence_date','evidence_grade'):
                if k not in o:
                    problems += 1; print('  LINE', i, 'missing key', k)
            if o.get('status') not in ('announced','planned','approved','construction','operational','rejected','unknown'):
                problems += 1; print('  LINE', i, 'bad status', o.get('status'))
            if o.get('evidence_grade') not in ('A','B','C','U'):
                problems += 1; print('  LINE', i, 'bad grade', o.get('evidence_grade'))
    missing = [d for d in divisions if d not in seen]
    extra = sorted(seen - set(divisions))
    print('  records:', len(lines), 'divisions seen:', len(seen))
    print('  missing:', missing)
    print('  extra:', extra)
    print('  problems:', problems)

check('scripts/expansion/world/results-method/batch-184.jsonl', ['Maharashtra - '+x for x in ['Jalgaon','Jalna','Kolhapur','Latur','Mumbai','Mumbai Suburban','Nagpur Division','Nanded','Nandurbar','Nashik Division','Osmanabad','Palghar','Parbhani','Pune Division','Raigarh','Ratnagiri','Sangli','Satara Division','Sindhudurg','Solapur']])
check('scripts/expansion/world/results-method/batch-185.jsonl', ['Maharashtra - '+x for x in ['Thane','Wardha','Washim','Yavatmal']] + ['Manipur - '+x for x in ['Bishnupur','Chandel','Churachandpur','Imphal East','Imphal West','Jiribam','Kakching','Kamjong','Kangpokpi','Noney','Pherzawl','Senapati','Tamenglong','Tengnoupal','Thoubal','Ukhrul']])
