import json

with open("resources/countries.json", "r", encoding="utf-8") as file:
    countries = json.load(file)
    continents = []
    for country in countries:
        continent = country["continent"]
        if continent not in continents:
            continents.append(continent)
    continents.sort()
    print(continents)
