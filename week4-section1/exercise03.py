jack = ("jack", "bauer", "1", 100_000, "TR1", 1967, ["IT", "SALES", "FINANCE"])
kate = ("kate", "austen", "2", 200_000, "TR2", 1985, ["IT"])
james = ("james", "sawyer", "3", 150_000, "TR3", 1982, ["FINANCE"])
ben = ("ben", "linus", "4", 250_000, "TR4", 1958, ["SALES", "IT"])
sun = ("sun", "kwon", "4", 300_000, "TR5", 1976, ["FINANCE", "IT"])
jin = ("jin", "kwon", "4", 400_000, "TR6", 1977, ["SALES"])
employees = [jack, kate, james, ben, sun, jin]
print(employees)
employees.sort(reverse=True, key=lambda employee: len(employee[6]))
print(employees)
print(employees)
print(employees)

