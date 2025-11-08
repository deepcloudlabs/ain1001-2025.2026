"""
Leap Year
2000 -> Leap Year
2001 -> NOT Leap Year
2002 -> NOT Leap Year
2003 -> NOT Leap Year
2004 -> Leap Year
2005 -> NOT Leap Year
2008 -> Leap Year
2100 -> NOT Leap Year
2200 -> NOT Leap Year
2300 -> NOT Leap Year
2400 -> Leap Year
"""
year = int(input("Enter year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")