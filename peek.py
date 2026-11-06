import json, re
raw = open(".nemini.json", encoding="utf-8").read()
urls = sorted(set(re.findall(r"https?://[^\s\"']+", raw)))
for u in urls[:20]:
    print(u)
print("---keys---")
print(list(json.loads(raw).keys())[:20])
