import json

with open("resources/countries.json", "r",encoding="utf-8") as file:
    countries = json.load(file)
    continents = []
    for country in countries:
        if not country["continent"] in continents:
            continents.append(country["continent"])
    continents.sort()
    print(continents)