import json
data = json.load(open('data-roomservice.json', encoding='utf-8'))
for e in data:
    if e['name'] == 'Roksolana':
        raw = open('data-roomservice.json', encoding='utf-8').read()
        idx = raw.find('"Roksolana"')
        if idx >= 0:
            pidx = raw.find('"photos"', idx)
            if pidx >= 0:
                print(raw[pidx:pidx+350])
        break
