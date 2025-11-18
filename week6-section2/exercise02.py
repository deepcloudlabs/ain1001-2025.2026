"""
Mastermind
level: 3
secret: 3-digit integer with all digits are distinct
549
max number of moves: 10 +2
lives: 3
Player -> 123 -> No match!
          456 -> -2
          574 -> -1+1
          548 -> +2
          549 -> level: 4
"""
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


def print_moves(history: [(int, int, int, str)]) -> None:
    for move in history:
        print(f"Guess: {move[0]} -> {move[3]}")


def evaluate_move(guess: int, secret: int) -> (int, int, int, str):
    guess_as_str = str(guess)
    secret_as_str = str(secret)
    perfect_match = 0
    partial_match = 0
    for i in range(len(guess_as_str)):
        g = guess_as_str[i]
        for j in range(len(secret_as_str)):
            s = secret_as_str[j]
            if g == s:
                if i == j:
                    perfect_match += 1
                else:
                    partial_match += 1
    if perfect_match == 0 and partial_match == 0:
        return guess, 0, 0, "No Match"
    message = ""
    if partial_match > 0:
        message = f"-{partial_match}"
    if perfect_match > 0:
        message = f"{message}+{perfect_match}"
    return guess, partial_match, perfect_match, message


# Game Model
game_level: int = 3
max_moves: int = 10
lives: int = 3
moves: [(int, int, int, str)] = []
tries: int = 0
secret = create_secret(game_level)

while True:
    guess = int(input("Guess a number: "))
    if guess == secret:
        game_level += 1
        if game_level > 10:
            print("You win!")
            break
        tries = 0
        secret = create_secret(game_level)
        max_moves = max_moves + 2
        moves = []
        print(f"You got it. Move to the next level: {game_level}")
    else:
        tries = tries + 1
        if tries > max_moves:
            print("You lose!")
            break
        else:
            moves.append(evaluate_move(guess, secret))
        print_moves(moves)
