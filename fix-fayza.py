import json

# Fix Fayza station to 'expat' in data.json
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for c in data:
    if c.get('name') == 'Fayza':
        print('avant:', c['name'], 'station=', repr(c.get('station')))
        c['station'] = 'expat'
        print('après:', c['name'], 'station=', repr(c.get('station')))
        break

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('data.json updated')

# Also update canonical DB
import sqlite3
conn = sqlite3.connect('../citizens/citizens.db')
c2 = conn.cursor()
c2.execute("UPDATE citizens SET station='expat' WHERE name='Fayza'")
conn.commit()
c2.execute("SELECT name, station FROM citizens WHERE name='Fayza'")
print('DB:', c2.fetchone())
conn.close()
