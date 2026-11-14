import json, os
print("size:", os.path.getsize('data.json'))
with open('data.json') as f:
    data = json.load(f)
names = [a['name'] for a in data]
print("total:", len(names))
print("last 5:", names[-5:])
print("has Yumi:", 'Yumi' in names)
