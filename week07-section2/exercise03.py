# perfect numbers
# 6 = 1 + 2 + 3
# 28 = 1 + 2 + 4 + 7 + 14
for n in range(2, 1_000_000):
    sum_of_proper_divisors = 1
    for divisor in range(2, n // 2 + 1):
        if n % divisor == 0:
            sum_of_proper_divisors += divisor
    if sum_of_proper_divisors == n:
        print(f"{n} is a perfect number!")
