numbers = [4, 8, 15, 16, 23, 42]
print(15 in numbers)
print(108 not in numbers)
print(numbers.index(15))
if 108 in numbers: # guard
    print(numbers.index(108))
