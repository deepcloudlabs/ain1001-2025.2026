import pickle

with open("resources/employees.pkl", "rb") as file:
    employees = pickle.load(file)

for employee in employees:
    print(employee)