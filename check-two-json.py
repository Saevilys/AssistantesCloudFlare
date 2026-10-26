import json
targets = {'ximena','yejin','fatou'}
for p in ['data.json','data-roomservice.json']:
    data = json.load(open(p, encoding='utf-8'))
    if isinstance(data, dict):
        data = data.get('assistants') or data.get('data') or []
    names = [e.get('name','') for e in data if isinstance(e, dict)]
    hits = [n for n in names if n.lower() in targets]
    print(p, len(names), hits)
