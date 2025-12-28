import csv

employees = []
with open("resources/employees.csv", "rt") as file:
    reader = csv.reader(file)
    for employee in reader:
        employees.append(employee)

for employee in employees:
    print(employee)