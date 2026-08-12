import sys, urllib.parse, urllib.request
from html.parser import HTMLParser
UA = 'Mozilla/5.0'
KW = ['数据', '智算', '算力', '环评', '备案', '节能', '发改委', '生态环境', '云计算']
class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.cur = None
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            d = dict(attrs)
            self.cur = [d.get('href'), '']
    def handle_data(self, data):
        if self.cur:
            self.cur[1] += data
    def handle_endtag(self, tag):
        if tag == 'a' and self.cur:
            self.links.append(tuple(self.cur))
            self.cur = None
def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    return urllib.request.urlopen(req, timeout=10).read().decode('utf-8', 'ignore')
for u in sys.argv[1:]:
    print('=== PAGE', u, '===')
    try:
        html = fetch(u)
    except Exception as e:
        print('FETCH_FAIL', repr(e))
        continue
    p = P()
    p.feed(html)
    for href, text in p.links:
        if not href:
            continue
        j = urllib.parse.urljoin(u, href)
        hit = [k for k in KW if k in text or k in href]
        if hit:
            print('HIT', ' '.join(hit), '|', text.strip()[:50], '|', j)
