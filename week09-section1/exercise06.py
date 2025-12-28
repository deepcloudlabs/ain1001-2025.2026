import json
from functools import reduce

to_continent = lambda country: country["continent"]


def distinct(continents, continent):
    continents.add(continent)
    return continents


with open("resources/countries.json", "r", encoding="utf-8") as file:
    countries = json.load(file)
    continents = reduce(distinct, map(to_continent, countries), set())
    print(continents)
