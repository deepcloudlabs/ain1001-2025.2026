def take_sum_of_proper_divisor(n: int) -> int:
    total = 1
    for divisor in range(2, n // 2 + 1):
        if n % divisor == 0:
            total += divisor
    return total


amicable_numbers: [(int, int)] = []
for number in range(100, 100_000):
    found = False
    for pair in amicable_numbers:
        if number in pair:
            found = True
            break
    if found:
        continue
    best_friend = take_sum_of_proper_divisor(number)
    total = take_sum_of_proper_divisor(best_friend)
    if total == number:
        amicable_numbers.append((number, best_friend))
        print(number, best_friend)
