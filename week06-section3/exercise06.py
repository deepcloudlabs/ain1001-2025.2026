"""
Number Guessing Game
game level: 2
secret= pick a random number between 1 .. 10 ** game level
max number of moves =
secret: 42
player -> 50 -> pick a smaller one
         25 -> pick larger one
         37 -> pick larger
         log2(100) -> 7
"""
import math
import random


def create_secret(game_level: int = 2) -> int:
    return random.randint(1, 10 ** game_level)


# Model
level = 3
secret = create_secret(level)
max_number_of_moves = math.ceil(math.log2(10 ** level))
print(max_number_of_moves)
tries = 0
while True:
    guess = int(input("Enter your guess: "))
    if guess == secret:
        level += 1
        if level > 5:
            print("You win the game! Tokens are transferred to your account")
            break
        print(f"Moved to the next level: {level}")
        secret = create_secret(level)
        tries = 0
        max_number_of_moves = math.ceil(math.log2(10 ** level))
    else:
        tries += 1
        if tries > max_number_of_moves:
            print("You lost! Try again later")
            break
        if  guess < secret:
            print("Guess too low")
        else:
            print("Guess too high")