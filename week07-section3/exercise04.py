def is_happy(n: int) -> bool:
    visited_numbers = set()
    while n > 1 and n not in visited_numbers:
        visited_numbers.add(n)
        total = 0
        for digit in str(n):
            total += int(digit) ** 2
        n = total
    return n == 1


for number in range(1, 1_000_001):
    if is_happy(number):
        print(number)
