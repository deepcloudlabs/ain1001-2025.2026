numbers = (4, 8, 15, 16, 23, 42)
print(numbers[0]) # 4
print(numbers[5]) # 42
print(numbers[-1]) # 42
print(numbers[-6]) # 4
#print(numbers[6]) # IndexError: list index out of range
#print(numbers[-7])
print(16 in numbers) # True
print(numbers.index(16)) # 3
# numbers[3] = 108
# numbers.append(108)
# numbers.remove(42)
# numbers.extend((1,2,3,4))