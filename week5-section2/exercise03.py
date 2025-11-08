def is_even(number: int) -> bool:
    return number % 2 == 0

def get_evens(values: [int]) -> [int]:
    evens = []
    for value in values:
        if is_even(value):
            evens.append(value)
    return evens

numbers = [4, 8, 15, 16, 23, 42]
for even in get_evens(numbers):
    print(even)

def get_evens2(values: [int]) -> [int]:
    return [n for n in values if n % 2 == 0]