jack = ("jack","bauer", "11111111110", 100_000, "TR1", 1967, ["IT", "SALES"])
print(jack[3])
# Error: jack[3] *= 1.2
#jack[6] = ["IT"]
jack[6].remove("IT")
print(jack[6])
# unpacking
first_name, last_name, identity,salary,iban,birth_year,departments = jack
salary *= 2
jack = (first_name, last_name, identity, salary, iban, birth_year, departments)
print(jack[3])