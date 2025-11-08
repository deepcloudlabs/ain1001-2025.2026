numbers = [4, 8, 15, 16, 23, 42]
print(numbers[3]) # read
numbers[3] = 108  # write
print(numbers[3])
numbers.append(549)
numbers.append(3615)
numbers.extend([100,200,300,400])
print(numbers)
del numbers[3]
print(100 in numbers) # True
print(numbers.index(100)) # 7
