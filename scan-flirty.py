import re

raw = open("specials.html", encoding="utf-8").read()

# Find all references to flirty, currentFlirtLvl, flirtBannerLabel, flirt-desc, flirt-asc
patterns = [
    r'flirty',
    r'currentFlirtLvl',
    r'flirtBannerLabel',
    r'flirt-desc',
    r'flirt-asc',
    r'flirtLvl',
]

for p in patterns:
    matches = [(m.start(), raw[max(0,m.start()-60):m.end()+60]) for m in re.finditer(p, raw)]
    if matches:
        print(f"\n=== {p} ({len(matches)} hits) ===")
        for pos, ctx in matches:
            print(f"  @{pos}: ...{ctx}...")
    else:
        print(f"{p}: clean ✅")
