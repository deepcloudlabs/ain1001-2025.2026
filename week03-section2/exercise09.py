numbers = [4, 8, 15, 16, 23, 42, 108, 549]
# slicing
print(numbers[3:6])
# numbers[3:6] = []
del numbers[3:6]
print(numbers)
numbers[::] = []
numbers[:] = []
