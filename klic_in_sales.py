sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

for klic in sales:
    print(sales[klic])

for klic, hodnota in sales.items():
    print(f"nazev: {klic}, pocet prodanych kusu: {hodnota}")