def get_sum_of_divisors(n: int) -> int:
    total = 1
    for divisor in range(2, n // 2 + 1):
        if n % divisor == 0:
            total += divisor
    return total


for number in range(100, 1_000_000):
    friend_number = get_sum_of_divisors(number)
    total = get_sum_of_divisors(friend_number)
    if total == number:
        print(number, friend_number)
