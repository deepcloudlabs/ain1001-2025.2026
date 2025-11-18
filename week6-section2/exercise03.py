import random


def create_random_digit(min_digit: int = 0, max_digit: int = 9) -> int:
    if max_digit == min_digit:
        return min_digit
    elif max_digit < min_digit:
        return random.randint(max_digit, min_digit)
    return random.randint(min_digit, max_digit)


def create_secret(number_of_digits: int) -> int:
    if number_of_digits > 10:
        number_of_digits = 10
    digits: [int] = [create_random_digit(1, 9)]
    while len(digits) < number_of_digits:
        digit = create_random_digit(0, 9)
        if digit not in digits:
            digits.append(digit)
    number = 0
    # [5,4,9] -> number: 549
    for digit in digits:
        number = 10 * number + digit
    return number


for i in range(10):
    print(create_secret(111))