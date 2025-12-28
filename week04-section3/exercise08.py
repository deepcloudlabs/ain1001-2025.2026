numbers = [4, 8, 15, 16, 23, 15, 42, 15, 74, 82, 103]

print(numbers.index(15, 0))
print(numbers.index(15, 3))
print(numbers.index(15, 6))
if 15 in numbers[8:]: # guard
    print(numbers.index(15, 8))
