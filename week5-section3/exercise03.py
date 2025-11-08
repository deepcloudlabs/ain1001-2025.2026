years = [2000, 2001, 2002, 2003, 2004, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800]
for year in years:
    if year % 4 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        elif year % 100 == 0:
            print(f"{year} is NOT a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is NOT a leap year")
