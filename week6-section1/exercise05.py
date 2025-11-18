import math
import random


def create_secret(number_of_digits: int = 2) -> int:
    return random.randint(1, 10 ** number_of_digits)

# secret: 42
# 50 -> pick smaller -> 25 -> pick larger -> 37 -> pick larger
level=2
secret=create_secret(level)
max_number_of_moves = math.ceil(math.log2(10 ** level))
max_level = 5
tries = 0

while True:
    guess = int(input("Guess a number: "))
    if guess == secret:
        level += 1
        print(f"Move to the next level: {level}")
        if level > max_level:
            print(f"You win!")
            break
        secret = create_secret(level)
        max_number_of_moves = math.ceil(math.log2(10 ** level))
    else:
        tries += 1
        if tries > max_number_of_moves:
            print(f"You lose: {secret}")
            break
        if guess > secret:
            print("Pick smaller number")
        else:
            print("Pick larger number")