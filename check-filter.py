import re
raw = open("index.html", encoding="utf-8").read()
# Find filter logic
for m in re.finditer(r'(filter|flirty|special|tag|exclude)', raw, re.IGNORECASE):
    start = max(0, m.start()-80)
    end = min(len(raw), m.end()+80)
    print(f"@{m.start()}: ...{raw[start:end]}...")
    print()
