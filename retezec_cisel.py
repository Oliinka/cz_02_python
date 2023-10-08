leva_mez_1 = int(input("Zadejte levou mez 1. intervalu: "))
prava_mez_1 = int(input("Zadejte pravou mez 1. intervalu: "))
leva_mez_2 = int(input("Zadejte levou mez 2. intervalu: "))
prava_mez_2 = int(input("Zadejte pravou mez 2. intervalu: "))
# rozložení dlouhého textu
text = ("Dvojice čísel, jejichž součet leží alespoň v jednom z intervalů: ")
print(text)
for i in range(leva_mez_1, prava_mez_1 + 1):
    for j in range(leva_mez_2, prava_mez_2 + 1):
        soucet = i + j
        if (leva_mez_1 <= soucet <= prava_mez_1 or
            leva_mez_2 <= soucet <= prava_mez_2):
            retezec = "[" + str(i) + ";" + str(j) + "]"
            print(retezec)

