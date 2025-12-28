def get_evens(numbers: list[int]) -> list[int]:
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

for i in get_evens(range(1,1_000)):
    print(i)