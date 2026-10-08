"""Dump every visible text fragment and link of a page, in order: python3 inventory.py page.html"""
import sys, re, json
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.rows=[]; s.skip=0; s.stack=[]; s.title=None; s.in_title=False
    def handle_starttag(s, tag, a):
        a=dict(a); s.stack.append(tag)
        if tag in ('style','script','svg'): s.skip+=1
        if tag=='title': s.in_title=True
        if tag=='a' and 'href' in a: s.rows.append(('a href', a['href']))
        if tag=='input' and a.get('type')!='range': s.rows.append((f"input#{a.get('id','')}", f"value={a.get('value','')} min={a.get('min','')} max={a.get('max','')}"))
        if tag=='svg' and 'aria-label' in a: s.rows.append(('svg aria-label', a['aria-label']))
        for k in ('aria-label','data-label'):
            if k in a and tag not in ('svg',): s.rows.append((f'{tag} {k}', a[k]))
        if tag=='meta' and (a.get('name') or a.get('property')): s.rows.append((f"meta {a.get('name') or a.get('property')}", a.get('content','')))
    def handle_endtag(s, tag):
        if tag in ('style','script','svg'): s.skip-=1
        if tag=='title': s.in_title=False
        if s.stack: s.stack.pop()
    def handle_data(s, d):
        if s.in_title: s.rows.append(('title', d.strip())); return
        if s.skip: return
        t=re.sub(r'\s+',' ',d).strip()
        if t: s.rows.append((s.stack[-1] if s.stack else '', t))
p=P(); p.feed(open(sys.argv[1],encoding='utf-8').read())
comp=re.compile(r'ARN|AMFI|SEBI|market risk|not a recommendation|Illustration|does not consider|Demo\.|disclaimer|suitability|Specialized Investment Fund', re.I)
print(f"# Inventory: {sys.argv[1]}\n\n{len(p.rows)} rows (text fragments, links, labels, metadata). Rows marked **C** contain compliance or disclaimer wording.\n\n| # | Element | Exact text |")
print("|---|---|---|")
for i,(el,t) in enumerate(p.rows,1):
    flag=' **C**' if comp.search(t) else ''
    print(f"| {i}{flag} | {el} | {t.replace('|','\\|')} |")
