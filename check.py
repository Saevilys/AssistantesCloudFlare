import json
rs = json.load(open('data-roomservice.json'))
for a in rs:
    if a['name'].lower() == 'sneha':
        print(len(a['photos']))
        for p in a['photos'][-4:]:
            print(p)
print('total assistants:', len(rs))
