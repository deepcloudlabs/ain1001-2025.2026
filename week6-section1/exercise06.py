import random


def create_secret(number_of_digits: int = 2) -> int:
    return random.randint(1, 10 ** number_of_digits)

for i in range(100):
    print(create_secret(2))