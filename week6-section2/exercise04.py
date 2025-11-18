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

print(evaluate_move(456,549))
print(evaluate_move(123,549))
print(evaluate_move(549,549))
print(evaluate_move(594,549))
print(evaluate_move(954,549))