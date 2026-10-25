import re
h = open("index.html").read()
hits = set(re.findall(r'(?:src|href)="([^"]*(?:img|r2)[^"]*)"', h)) | set(re.findall(r'"(https://[^"]*r2\.dev[^"]*)"', h))
print(list(hits)[:10])
print([m for m in re.findall(r'img/[a-z]+/', h)[:5]])
