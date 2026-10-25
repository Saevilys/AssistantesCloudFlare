import json
with open('data.json') as f:
    data = json.load(f)
names = [d['name'] for d in data]
for n in ['Ksenia','Sloane','Minji','Valka','Sable','Roza','Mina','Katya','Mila','Anya','Daria','Vera','Tasha','Nina','Seraphine','Naamah','Estrie','Mircalla','Brunhild','Hecate']:
    print(f"{n}: {'TAKEN' if n in names else 'FREE'}")
print(f"Total: {len(names)}")
