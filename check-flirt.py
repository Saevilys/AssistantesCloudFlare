import json

data = json.load(open('data.json', encoding='utf-8'))
for a in data:
    if a["name"].lower() in ("hodan", "danait"):
        print(a["name"], "→", json.dumps(a, ensure_ascii=False)[:300])
