import json
d=json.load(open('data.json'))
for c in d:
    if c.get('name','').lower()=='enora':
        print(json.dumps(c.get('photos'),ensure_ascii=False,indent=1))
        break
