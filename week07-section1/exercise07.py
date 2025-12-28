def is_harshad(n: int) -> bool:
    if n <= 0:
        return False

    digit_sum = sum(int(d) for d in str(n))
    return n % digit_sum == 0


for number in range(10, 100_000):
    if is_harshad(number):
        print(number)
