def get_evens(numbers: list[int]) -> list[int]:
    print("get_evens() is started.")
    for number in numbers:
        if number % 2 == 0:
            print(f"We got an even number: {number}")
            yield number
    print("get_evens() return the solution.")


values = [4, 8, 15, 16, 23, 42]
for even in get_evens(values):
    print(f"[for] even: {even}")