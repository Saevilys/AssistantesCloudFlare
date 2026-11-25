import sqlite3

conn = sqlite3.connect("citizens.db")
c = conn.cursor()
c.execute("UPDATE citizens SET station='expat' WHERE name='Fayza'")
conn.commit()
c.execute("SELECT name, station FROM citizens WHERE name='Fayza'")
print('DB:', c.fetchone())
conn.close()
