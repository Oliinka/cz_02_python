import json

data = {
    '1. místo': "Olga",
    '2. místo': "Zanet",
    "3. místo": "Letadlo",
    "4. místo": "Kozí bobky",
     }

with open("vyherci.json", mode = "w", encoding="utf-8") as soubor:
    json.dump(data, soubor, ensure_ascii=False)

