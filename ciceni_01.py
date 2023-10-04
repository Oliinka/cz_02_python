
# ------------------------------- TASK 02 -----------------------------------
# Proměnná medal_table tentokrát obsahuje zisky jednotlivých druhů medailí států
# na olympiádě 2020.
medal_table = {
    "Cuba": { "gold": 7, "silver": 3, "bronze": 5 },
    "Spain": { "gold": 3, "silver": 8, "bronze": 6 },
    "Uganda": { "gold": 2, "silver": 1, "bronze": 1 },
    "Bahamas": { "gold": 2, "silver": 0, "bronze": 0 },
    "Ukraine": { "gold": 1, "silver": 6, "bronze": 12 },
    "San Marino": { "gold": 0, "silver": 1, "bronze": 2 },
}

for state in medal_table:
    print(state, medal_table [state]["bronze"])

bronze_medals = []
for state in medal_table:
    bronze_medals.append(medal_table[state]["bronze"])
print(bronze_medals)
print(max(bronze_medals))

bronze_medals_slovnik = {}

for state in medal_table:
    bronze_medals_slovnik[state] = medal_table [state]["bronze"]
print(bronze_medals_slovnik)
print(max(bronze_medals_slovnik, key=bronze_medals_slovnik.get))

max_pocet = 0
max_state = ""
for state in bronze_medals_slovnik:
    if bronze_medals_slovnik[state] > max_pocet:
        max_pocet = bronze_medals_slovnik[state]
        max_state = state
print (max_state, max_pocet)


min_pocet = 10000
min_state = ""
for state in bronze_medals_slovnik:
    if bronze_medals_slovnik[state] > min_pocet:
        min_pocet = bronze_medals_slovnik[state]
        min_state = state
print (min_state, max_pocet)
