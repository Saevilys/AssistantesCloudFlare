import json
data = json.load(open('data.json', encoding='utf-8'))
print(f'Total: {len(data)}')
last = data[-1]
print(json.dumps(last, indent=2, ensure_ascii=False)[:2000])
