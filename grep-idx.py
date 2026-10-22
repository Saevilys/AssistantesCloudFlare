import re
html = open("index.html").read()
for m in re.finditer(r"[^\n]*(photos|\.png|r2\.dev)[^\n]*", html):
    print(m.group(0)[:200])
