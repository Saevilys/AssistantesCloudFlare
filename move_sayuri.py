import json

# Read both files
with open("data.json") as f:
    main_data = json.load(f)

with open("data-roomservice.json") as f:
    rs_data = json.load(f)

# Find and remove Sayuri from room service
sayuri = None
new_rs = []
for a in rs_data:
    if a["name"] == "Sayuri":
        sayuri = a
    else:
        new_rs.append(a)

if not sayuri:
    print("ERROR: Sayuri not found in room service")
    exit(1)

print(f"Sayuri found: {sayuri['name']}, {sayuri['age']}, {sayuri['origin']}")
print(f"  photos: {len(sayuri['photos'])}")

# Check she's not already in main data
for a in main_data:
    if a["name"] == "Sayuri":
        print("ERROR: Sayuri already in main data.json")
        exit(1)

# Build her main roster entry (L5 format)
sayuri_main = {
    "name": "Sayuri",
    "age": sayuri["age"],
    "origin": sayuri["origin"],
    "city": sayuri["city"],
    "region": "Asie",
    "active": True,
    "flirty": 5,
    "desc": sayuri["desc"],
    "voice": sayuri["voice"],
    "trait": sayuri["trait"],
    "photos": sayuri["photos"]
}

# Add to main data
main_data.append(sayuri_main)

# Write both files
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

with open("data-roomservice.json", "w", encoding="utf-8") as f:
    json.dump(new_rs, f, ensure_ascii=False, indent=2)

print(f"\nSayuri moved to main data.json as L5")
print(f"Main roster: {len(main_data)} assistants")
print(f"Room service: {len(new_rs)} assistants")
print(f"Sayuri photos: {sayuri_main['photos']}")
