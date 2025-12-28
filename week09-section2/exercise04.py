def get_evens(numbers: list[int]) -> list[int]:
    print("get_evens() is started.")
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            print(f"We got an even number: {number}")
            even_numbers.append(number)
    print("get_evens() return the solution.")
    return even_numbers


values = [4, 8, 15, 16, 23, 42]
for even in get_evens(values):
    print(even)