import json
with open('data-roomservice.json') as f:
    rs = json.load(f)
for a in rs:
    if 'sneha' in a.get('name','').lower():
        print(len(a['photos']), 'photos')
        for p in a['photos']:
            print(p)
