full_name = 'kate austen'
salary = 100_000.56545678
birth_year = 986
x = "full_name: " + full_name + ", salary: " + str(salary)
print(x)
x = f"full_name: {full_name:20s}, salary: {salary:.2f}"
print(x)
x = "full_name: %-20s, salary: %8.2f, birth year: %4d" % (full_name, salary, birth_year )
print(x)
x = "full_name: {0:20s}, salary: {1:8.2f}, birth year: {2:4d}".format(full_name,salary,birth_year)
print(x)