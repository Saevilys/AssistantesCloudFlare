#!/usr/bin/env python3
import json

with open("data.json", "r") as f:
    main = json.load(f)

# Remove Liezel and Mayaris
before = len(main)
main = [e for e in main if e.get("name") not in ("Liezel", "Mayaris")]
after = len(main)
print(f"Before: {before}, After: {after}, Removed: {before - after}")

# Verify they're gone
names = [e.get("name") for e in main]
assert "Liezel" not in names, "Liezel still there!"
assert "Mayaris" not in names, "Mayaris still there!"
print(f"Last 3: {names[-3:]}")

with open("data.json", "w") as f:
    json.dump(main, f, ensure_ascii=False, indent=2)
print("Written OK")
