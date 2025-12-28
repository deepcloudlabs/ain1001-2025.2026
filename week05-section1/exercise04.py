"""
 A mathematician lives on a street where house numbers are consecutive
 starting from 1. He/She says that the sum of the house numbers less than
 his/her house number is equal to the sum of the house numbers greater
 than his/her house number. Knowing that his house number contains
 3 digits design an algorithm and write a Python script
 to find his house number.
"""
for building_number in range(100000-1,10000,-1):
    left_sum = 0
    for house_number in range(1,building_number):
        left_sum += house_number
    right_sum = 0
    house_number = building_number + 1
    while right_sum < left_sum:
        right_sum += house_number
        house_number += 1
    if left_sum == right_sum:
        print(building_number,house_number-1)

