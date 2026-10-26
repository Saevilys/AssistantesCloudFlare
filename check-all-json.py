import json, glob
for p in glob.glob('/github/assistantescloudflare/*.json'):
    try:
        data = json.load(open(p, encoding='utf-8'))
    except Exception:
        continue
    if isinstance(data, dict):
        data = data.get('assistants') or data.get('data') or []
    names = [e.get('name','') for e in data if isinstance(e, dict)]
    hits = [n for n in names if n.lower() in ('ximena','yejin','fatou')]
    print(p.split('/')[-1], len(names), hits)
