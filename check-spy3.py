import json
with open('data.json') as f:
    data = json.load(f)
names = [d['name'] for d in data]
for n in ['Soomin','Ryunhee','Xueli','Saki','Ayame','Natsuki','Rina','Koharu','Tsukasa','Hinata','Yui','Mai','Shiori','Kotone']:
    print(f"{n}: {'TAKEN' if n in names else 'FREE'}")
print(f"Total: {len(names)}")
