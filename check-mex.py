import json
targets = {'rosalia','renata','dayana','sofia','mariana','lupita','dulce','itzel','nayeli'}
data = json.load(open('data-roomservice.json', encoding='utf-8'))
if isinstance(data, dict):
    data = data.get('assistants') or data.get('data') or []
rs = set(e.get('name','').lower() for e in data if isinstance(e, dict))
data2 = json.load(open('data.json', encoding='utf-8'))
main = set(e.get('name','').lower() for e in data2 if isinstance(e, dict))
for c in sorted(targets):
    st = 'TAKEN rs' if c in rs else ('TAKEN main' if c in main else 'FREE')
    print(st, c)
