import json
with open('data.json','r') as f:
    data = json.load(f)

stations = {}
for a in data:
    s = a.get('station','(no station field)')
    stations[s] = stations.get(s,0) + 1

for s,c in sorted(stations.items(), key=lambda x: -x[1]):
    print(f"{s}: {c}")

print(f"\nTotal: {len(data)} entries")
print(f"Has station field: {sum(1 for a in data if 'station' in a)}")

suyin = [a for a in data if a.get('station')=='suyin']
print(f"\nSuyin entries ({len(suyin)}):")
for a in suyin:
    print(f"  - {a.get('name','?')}")
