import re
html=open('index.html').read()
for m in re.finditer(r'photos\[0\]|avatar|idle', html):
    s=max(0,m.start()-120); print(html[s:m.end()+150].replace('\n',' ')); print('---')
