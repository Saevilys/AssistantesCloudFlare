import re
with open('station-suyin.html') as f:
    html = f.read()
scripts = re.findall(r'<script>(.*?)</script>', html, re.S)
s = scripts[0]
lines = s.split('\n')
for i in range(90, 125):
    print(i+1, lines[i])
