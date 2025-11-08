test_data = [
    {"year": 2000, "is_leap_year": True},
    {"year": 2001, "is_leap_year": False},
    {"year": 2002, "is_leap_year": False},
    {"year": 2003, "is_leap_year": False},
    {"year": 2004, "is_leap_year": True},
    {"year": 2100, "is_leap_year": False},
    {"year": 2200, "is_leap_year": False},
    {"year": 2300, "is_leap_year": False},
    {"year": 2400, "is_leap_year": True},
    {"year": 2500, "is_leap_year": False},
    {"year": 2600, "is_leap_year": False},
    {"year": 2700, "is_leap_year": False},
    {"year": 2800, "is_leap_year": True},
    {"year": 2900, "is_leap_year": False},
    {"year": 3000, "is_leap_year": False},
    {"year": 3100, "is_leap_year": False},
    {"year": 3200, "is_leap_year": True}
]
for data in test_data:
    year = data["year"]
    is_leap_year = data["is_leap_year"]
    leap_year = None
    if year % 4 == 0:
        if year % 400 == 0:
            leap_year = True
        elif year % 100 == 0:
            leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False
    if leap_year == is_leap_year:
        print(f"[SUCCESS] {year} is {'a' if is_leap_year else 'NOT a' } leap year")
    else:
        print(f"[FAIL] {year} is {'a' if is_leap_year else 'NOT a' } leap year")

