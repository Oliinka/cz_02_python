knihy = ["Temna noc", 450, True, True]
knihy2 = {
    "Nazev": "Ananas na pizzu patri",
    "Cena": 0,
    "Skladem": True
}

print(knihy2)
print(knihy2.keys())
print(knihy2.values())
print(knihy2["Nazev"])
print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}")