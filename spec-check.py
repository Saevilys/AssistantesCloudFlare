import re
h=open("specials.html").read()
# Find where cnt-demones count is set
for m in re.finditer(r'cnt-demones', h):
    i=m.start()
    print(repr(h[i-100:i+100]))
    print("---")
