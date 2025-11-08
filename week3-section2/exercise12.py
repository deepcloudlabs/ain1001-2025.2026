employees = [
    ("jack bauer", 100_000, 1965, "IT", True),
    ("kate austen", 200_000, 1988, "FINANCE", True),
    ("james sawyer", 75_000, 1986, "SALES", False),
    ("ben linus", 120_000, 1963, "IT", True)
]
print(employees)
employees.sort(key = lambda emp : emp[2])
print(employees)
