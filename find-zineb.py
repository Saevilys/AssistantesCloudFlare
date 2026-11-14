#!/usr/bin/env python3
import json
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

# Find Zineb station entries
zineb = [e for e in data if "zineb" in (str(e.get("city", "") or "") + str(e.get("station", "") or "")).lower()]
print(f"Total entries: {len(data)}")
print(f"Zineb entries: {len(zineb)}")
if zineb:
    # Show first Zineb entry as example
    import json as j
    print(j.dumps(zineb[0], indent=2, ensure_ascii=False)[:3000])
    print("\n--- Last Zineb entry ---")
    print(j.dumps(zineb[-1], indent=2, ensure_ascii=False)[:3000])
