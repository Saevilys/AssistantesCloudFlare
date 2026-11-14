with open('data.json') as f:
    txt = f.read()
head = txt[:40362]
print("station in first 40k:", '"station"' in head)
import json
# find where entries with station appear
idx = txt.find('"station"')
print("first station idx:", idx)
# last name visible in first 40k
print(head[-200:])
