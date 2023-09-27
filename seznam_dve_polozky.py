hodnoceni = ["Kniha 1", 4, "Kniha 2", 5, "Kniha 3", 3.3]
hodnoceni1 = [
    ["Kniha1", 4], 
    ["Kniha2", 5], 
    ["Kniha3", 3.3]
]

print(hodnoceni1[0][1])
print(hodnoceni1[0][0][0])

for polozka in hodnoceni1:
    print(polozka[0] + " " + str(polozka[1]))