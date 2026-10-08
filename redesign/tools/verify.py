import sys, html, json, re
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.texts=[]; self.hrefs=[]; self.attrs=[]; self.meta=[]; self.skip=0; self.cur=[]; self.jsonld=None; self.in_ld=False; self.title=None; self.in_title=False
    def handle_starttag(self, tag, a):
        a=dict(a)
        if tag in ('style','script','svg'):
            self.skip+=1
            if tag=='script' and a.get('type')=='application/ld+json': self.in_ld=True
        if tag=='svg' and 'aria-label' in a: self.attrs.append(('svg aria-label',a['aria-label']))
        if tag=='a':
            if 'href' in a: self.hrefs.append(a['href'])
            if 'aria-label' in a: self.attrs.append(('a aria-label',a['aria-label']))
        if tag=='nav' and 'aria-label' in a: self.attrs.append(('nav aria-label',a['aria-label']))
        if tag=='meta':
            k=a.get('name') or a.get('property')
            if k: self.meta.append((k,a.get('content')))
        if tag=='link' and a.get('rel')=='canonical': self.meta.append(('canonical',a.get('href')))
        if tag=='html': self.meta.append(('lang',a.get('lang')))
        if tag=='title': self.in_title=True
        if tag in ('p','h1','h2','li','a','span','b','dt','dd','div','nav','footer','header','main','section','ul','dl','svg'):
            pass
    def handle_endtag(self, tag):
        if tag in ('style','script','svg'):
            self.skip-=1; self.in_ld=False
        if tag=='title': self.in_title=False
    def handle_data(self, d):
        if self.in_title: self.title=d.strip(); return
        if self.in_ld: self.jsonld=json.loads(d); return
        if self.skip: return
        t=re.sub(r'\s+',' ',d).strip()
        if t: self.texts.append(t)

def parse(path):
    p=P(); p.feed(open(path,encoding='utf-8').read()); return p

def joined(texts):
    # merge adjacent fragments into one stream for word-level comparison
    return ' '.join(texts)

a=parse(sys.argv[1]); b=parse(sys.argv[2])
ok=True
def cmp(name,x,y):
    global ok
    if x==y: print(f"MATCH  {name}")
    else:
        ok=False; print(f"DIFF   {name}\n   original: {x!r}\n   new:      {y!r}")

cmp('<title>',a.title,b.title)
cmp('meta/lang/canonical',a.meta,[m for m in b.meta if m[0]!='theme-color'])
cmp('JSON-LD',a.jsonld,b.jsonld)
cmp('aria-labels (svg, a, nav)',a.attrs,b.attrs)
cmp('hrefs in order',a.hrefs,b.hrefs)
# text stream: compare as one normalised string (ignores how fragments are split by tags)
ja,jb=joined(a.texts),joined(b.texts)
cmp('full visible text stream',ja,jb)
# per-string set check for a readable report
sa,sb=set(a.texts),set(b.texts)
print(f"\noriginal text fragments: {len(a.texts)}  new: {len(b.texts)}")
missing=[t for t in a.texts if t not in jb]
print("fragments from original not found in new:", missing or "none")
extra=[t for t in b.texts if t not in ja]
print("fragments in new not found in original:", extra or "none")
print("\nRESULT:", "100% MATCH" if ok and not missing and not extra else "MISMATCH")
