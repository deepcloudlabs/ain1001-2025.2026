"""
 A mathematician lives on a street where house numbers are consecutive
 starting from 1. He/She says that the sum of the house numbers less than
 his/her house number is equal to the sum of the house numbers greater
 than his/her house number. Knowing that his house number contains
 3 digits design an algorithm and write a Python script
 to find his house number.
"""
for building_no in range(100000,10000,-1):
    left_sum = 0
    for i in range(1, building_no):
        left_sum += i
    right_sum = 0
    i = building_no+1
    while right_sum < left_sum:
        right_sum += i
        i = i + 1
    if right_sum == left_sum:
        print(f"The mathematician lives on {building_no}.")
        print(f"There are {i-1} buildings at that street.")
        break
