jack = ("jack", "shephard", "1", 100_000, 1984, "IT")
kate = ("kate", "austen", "2", 200_000, 1987, "SALES")
james = ("james", "sawyer", "3", 300_000, 1985, "FINANCE")
ben = ("ben", "linus", "4", 400_000, 1955, "HR")
jin = ("jin", "kwon", "5", 330_000, 1990, "IT")
sun = ("sun", "kwon", "6", 250_000, 1992, "IT")

employees = {
    "1": jack,
    "2": kate,
    "3": james,
    "4": ben,
    "5": jin,
    "6": sun
}

for id in employees.keys():
    employee = employees[id]
    print(employee)

for employee in employees.values():
    id = employee[2]
    print(employee)

for id, employee in employees.items():
    print(id, employee)
