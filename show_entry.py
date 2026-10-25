import json
d = json.load(open("data.json"))
if isinstance(d, dict):
    print(list(d.keys())[:5])
    for k, v in d.items():
        if isinstance(v, list) and v:
            print("LIST:", k, len(v))
            print(json.dumps(v[0], ensure_ascii=False, indent=1)[:1500])
            break
elif isinstance(d, list):
    print(len(d)); print(json.dumps(d[0], ensure_ascii=False, indent=1)[:1500])
