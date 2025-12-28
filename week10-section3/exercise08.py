import json

with open("resources/circle.json", "rt") as file:
    circle = json.load(file)

print(type(circle["radius"]))
print(circle["x"])
print(circle["y"])
print(circle)