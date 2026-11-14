import json

with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

e = data[527]
print(json.dumps(e, indent=2, ensure_ascii=False))
