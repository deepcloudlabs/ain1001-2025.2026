for number in range(2, 1_000_000):
    total = 1
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            total += divisor
    if total == number:
        print(number)
