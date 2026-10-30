h=open("specials.html").read()
# Voir buildProfile en entier
i=h.find("function buildProfile")
print("=== buildProfile ===")
print(repr(h[i:i+1200]))
print("\n---\n")
# Voir updateSection
i=h.find("function updateSection")
print("=== updateSection ===")
print(repr(h[i:i+500]))
print("\n---\n")
# Voir applyFilters debut
i=h.find("function applyFilters")
print("=== applyFilters ===")
print(repr(h[i:i+600]))
