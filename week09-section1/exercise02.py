from functools import reduce

employees = [
    {"fullname": "jack shephard", "department": "Sales", "salary": 100000, "year": 1978, "fulltime": True},
    {"fullname": "kate austen", "department": "IT", "salary": 200000, "year": 1985, "fulltime": False},
    {"fullname": "ben linus", "department": "Finance", "salary": 150000, "year": 1967, "fulltime": True},
    {"fullname": "james sawyer", "department": "HR", "salary": 70000, "year": 1979, "fulltime": True},
    {"fullname": "kim kwon", "department": "Sales", "salary": 120000, "year": 1986, "fulltime": True},
    {"fullname": "sun kwon", "department": "IT", "salary": 200000, "year": 1984, "fulltime": False},
    {"fullname": "hugo reyes", "department": "IT", "salary": 120000, "year": 1992, "fulltime": True}
]


def is_fulltime(employee: dict) -> bool:
    return employee["fulltime"]


if_fulltime = lambda employee: employee["fulltime"]
if_it_worker = lambda employee: employee["department"] == "IT"
to_salary = lambda employee: employee["salary"]
to_sum = lambda acc,salary: acc + salary
total_salary = reduce(to_sum,map(to_salary,filter(if_it_worker,filter(if_fulltime, employees))),0)
print(total_salary)
