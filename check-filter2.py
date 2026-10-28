import re
raw = open("index.html", encoding="utf-8").read()
# Find the fetch and filter area around the data loading
for m in re.finditer(r'(fetch|\.json|filter\(|special|flirty|tag\b|\.tag)', raw, re.IGNORECASE):
    start = max(0, m.start()-100)
    end = min(len(raw), m.end()+150)
    print(f"@{m.start()}: ...{raw[start:end]}...")
    print("---")
