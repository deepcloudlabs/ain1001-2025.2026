def get_number_of_digits(n: int) -> int:
    solution = 0 # 1 -> 2 -> 3 -> 4
    while n > 0: # 3615 -> 361 -> 36 -> 3 -> 0
        solution += 1
        n = n // 10
    return solution # 4

number = 3615
print(get_number_of_digits(number))