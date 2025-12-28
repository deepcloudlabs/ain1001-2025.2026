import json
from functools import reduce

if_asian = lambda country : country["continent"] == "Asia"
to_population = lambda country : country["population"]
to_sum = lambda acc,population: acc + population

with open("resources/countries.json","r",encoding="utf-8") as file:
    countries = json.load(file)
    asian_population = reduce(to_sum,map(to_population,filter(if_asian, countries)),0)
    print(asian_population)