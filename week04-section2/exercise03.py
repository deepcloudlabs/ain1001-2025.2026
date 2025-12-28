"""
 A mathematician lives on a street where house numbers are consecutive
 starting from 1. He/She says that the sum of the house numbers less than
 his/her house number is equal to the sum of the house numbers greater
 than his/her house number. Knowing that his house number contains
 3 digits design an algorithm and write a Python script
 to find his house number.
"""
for house_number in range(1000000-1, 100000):
    sum_left = 0
    for building_number in range(1, house_number):
        sum_left += building_number
    sum_right = 0
    building_number = house_number + 1
    while sum_right < sum_left:
        sum_right += building_number
        building_number += 1
    if sum_right == sum_left:
        print(f"Mathematician lives at the building: {house_number}.")
        print(f"There are {building_number-1} buildings in the street.")
        break