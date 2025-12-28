import json

with open("resources/employees.json", "rt") as file:
    employees = json.load(file)

for employee in employees:
    print(employee)