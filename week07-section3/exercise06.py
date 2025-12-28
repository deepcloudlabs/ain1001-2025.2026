for number in range(10, 1_000_000):
    divisor = 0
    for digit in str(number):
        divisor = divisor + int(digit)
    if number % divisor == 0:
        print(number)
