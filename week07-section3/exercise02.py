for number in range(100,1_000_000):
    n = len(str(number))
    total = 0
    for digit in str(number):
        total += int(digit) ** n
    if number == total:
        print(number)