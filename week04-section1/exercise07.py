jack = ("jack", "bauer", "1", 100_000, "TR1", 1967, ["IT", "SALES", "FINANCE"])
kate = ("kate", "austen", "2", 200_000, "TR2", 1985, ["IT"])
james = ("james", "sawyer", "3", 150_000, "TR3", 1982, ["FINANCE"])
ben = ("ben", "linus", "4", 250_000, "TR4", 1958, ["SALES", "IT"])
sun = ("sun", "kwon", "4", 300_000, "TR5", 1976, ["FINANCE", "IT"])
jin = ("jin", "kwon", "4", 400_000, "TR6", 1977, ["SALES"])
employees = [jack, kate, james, ben, sun, jin]
for employee in employees:
    print(employee)

for i in range(len(employees)):
    employee = employees[i]
    print(employee)
print(list(enumerate(employees)))
# [(0, ('jack', 'bauer', '1', 100000, 'TR1', 1967, ['IT', 'SALES', 'FINANCE'])), (1, ('kate', 'austen', '2', 200000, 'TR2', 1985, ['IT'])), (2, ('james', 'sawyer', '3', 150000, 'TR3', 1982, ['FINANCE'])), (3, ('ben', 'linus', '4', 250000, 'TR4', 1958, ['SALES', 'IT'])), (4, ('sun', 'kwon', '4', 300000, 'TR5', 1976, ['FINANCE', 'IT'])), (5, ('jin', 'kwon', '4', 400000, 'TR6', 1977, ['SALES']))]
for i, employee in enumerate(employees):
    print(employee)
