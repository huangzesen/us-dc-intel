import sys, urllib.parse, urllib.request
from html.parser import HTMLParser
UA = 'Mozilla/5.0'
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
for u in sys.argv[1:]:
    print('=== PAGE', u, '===')
    try:
        req = urllib.request.Request(u, headers={'User-Agent': UA})
        html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', 'ignore')
    except Exception as e:
        print('FETCH_FAIL', repr(e))
        continue
    p = P()
    p.feed(html)
    for href, text in p.links:
        if href and href.startswith(('http', '/')):
            print(text.strip()[:40], '|', urllib.parse.urljoin(u, href))
