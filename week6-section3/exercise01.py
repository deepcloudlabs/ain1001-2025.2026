def is_distinct_digits(n : int) -> bool:
    digits = set()
    for digit in str(n):
        digits.add(digit)
    return len(digits) == len(str(n))

number = 3364
print(is_distinct_digits(number)) # False
number = 3615
print(is_distinct_digits(number)) # True
