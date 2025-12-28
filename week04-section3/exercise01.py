# tuple -> vector
jack = ("jack", "bauer", "1", 100_000, 1968, "IT")
print(jack[3])
# jack[3] *= 1.2
print(jack[3])
first_name, last_name, id, salary, birth_year, department = jack
# salary = salary * 1.2
print(jack[3])
jack = (first_name, last_name, id, 1.2 * salary, birth_year, department)
print(jack[3])
