for number in range(100, 100_000_000):
    n = len(str(number))
    total = 0
    for digit in str(number):
        total += int(digit) ** n
    if total == number:
        print(number)