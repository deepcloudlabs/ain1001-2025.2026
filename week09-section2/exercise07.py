import json
from functools import reduce


def distinct(continents, continent):
    continents.add(continent)
    return continents


to_continent = lambda country: country["continent"]

with open("resources/countries.json", "r", encoding="utf-8") as file:
    countries = json.load(file)
    continents = reduce(distinct, map(to_continent, countries), set())
    print(continents)
