h=open("specials.html").read()
# Voir le sort arrival et la déclaration de currentSort
i=h.find("if(currentSort==='arrival')")
print(repr(h[i-50:i+300]))
print("---")
i=h.find("let currentSort")
if i==-1: i=h.find("var currentSort")
print(repr(h[i:i+60]))
