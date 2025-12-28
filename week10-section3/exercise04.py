employees = []
with open("resources/employees.txt", "rt") as file:
    # file.readlines()
    for line in file:
        full_name, department, salary, birth_year, full_time = line.strip().split(",")
        salary = float(salary.strip())
        birth_year = int(birth_year.strip())
        full_time = bool(full_time.strip())
        employees.append((full_name, department, salary, birth_year, full_time))

for employee in employees:
    print(employee)