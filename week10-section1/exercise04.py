employees = []

with open("resources/employees.txt",mode="rt") as file:
    for line in file:
        full_name,department,salary,birth_year,full_time = line.strip().split(",")
        employees.append((full_name,department,salary,birth_year,full_time))

for employee in employees:
    print(employee)