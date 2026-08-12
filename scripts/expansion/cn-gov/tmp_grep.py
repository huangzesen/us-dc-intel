import sys, re, urllib.request
UA = 'Mozilla/5.0'
PAT = re.compile('数据中心|智算中心|算力中心|云计算|机架|智算|算力')
def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    return urllib.request.urlopen(req, timeout=15).read().decode('utf-8', 'ignore')
def text(html):
    html = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.S)
    html = re.sub(r'<style[^>]*>.*?</style>', ' ', html, flags=re.S)
    html = re.sub(r'<[^>]+>', ' ', html)
    html = re.sub(r'\s+', ' ', html)
    return html
for u in sys.argv[1:]:
    print('=== PAGE', u, '===')
    try:
        t = text(fetch(u))
    except Exception as e:
        print('FETCH_FAIL', repr(e))
        continue
    for m in PAT.finditer(t):
        s = max(0, m.start() - 80)
        print('HIT:', t[s:m.end() + 120])
        print('---')
