import json
with open('data.json') as f:
    data = json.load(f)
names = [d['name'] for d in data]
for n in ['Ksenia','Mina','Mila','Tasha','Nina','Daria','Sable','Roza','Valka','Seraphine','Naamah','Estrie','Mircalla','Brunhild','Hecate','Reyna','Yuki','Suki','Mika','Nika','Dalia','Liana','Sable','Kira','Zara','Nova','Echo','Raven','Iris']:
    print(f"{n}: {'TAKEN' if n in names else 'FREE'}")
print(f"Total: {len(names)}")
