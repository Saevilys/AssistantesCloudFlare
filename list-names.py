import json
# Main roster
data = json.load(open('data.json'))
names = sorted([a['name'].lower() for a in data])
print(f"Main roster: {len(data)} assistants")
for n in names:
    print(f"  {n}")

# Room service
rs = json.load(open('data-roomservice.json'))
rs_names = sorted([a['name'].lower() for a in rs])
print(f"\nRoom service: {len(rs)} assistants")
for n in rs_names:
    print(f"  {n}")
