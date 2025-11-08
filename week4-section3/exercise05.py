jack = ("jack", "shephard", "1", 100_000, 1984, "IT")
kate = ("kate", "austen", "2", 200_000, 1987, "SALES")
james = ("james", "sawyer", "3", 300_000, 1985, "FINANCE")
ben = ("ben", "linus", "4", 400_000, 1955, "HR")
jin = ("jin", "kwon", "5", 500_000, 1990, "IT")
sun = ("sun", "kwon", "6", 600_000, 1992, "IT")

employees = [jack, kate, james, ben, jin, sun]

#employees[-2:] = []
#employees[:2] = []
#del employees[0]
#del employees[1]
employees.remove(kate)
print(employees)