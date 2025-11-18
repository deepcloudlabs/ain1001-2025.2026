"""
Number Guessing Game
pick a secret number (an integer) which is between 1 and 100
secret: 78
at most 7 moves
player:
1st move: 50
          pick larger number
2nd move: 75
           pick larger number
3rd move: 87
            pick a smaller number
...
"""
import random


def create_secret(low: int = 1, high: int = 100) -> int:
    return random.randint(low, high)


def is_valid(number: int, low: int = 0, high: int = 100) -> (bool, str):
    global moves
    if low <= number <= high:
        for move in moves:
            if move[0] == number:
                return False, "You have already used the number"
        return True, None
    return False, "Please provide an integer between 1 and 100!"


def print_moves(history: [(int, str)]) -> None:
    for move in history:
        print(f"{move[0]}: {move[1]}")


secret: int = create_secret(1, 100)
moves: [(int, str)] = []
tries: int = 0


def game_app():
    global secret, moves, tries
    while True:
        guess = int(input("guess: "))
        validation = is_valid(guess)
        if not validation[0]:
            print(validation[1])
            continue
        if guess == secret:
            print("You win!")
            break
        tries += 1
        if tries > 7:
            print(f"Game Over: {secret}")
            break
        if guess < secret:
            moves.append((guess, "pick a larger number"))
        else:
            moves.append((guess, "pick a smaller number"))
        print_moves(moves)


game_app()
