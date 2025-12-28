numbers = [4, 8, 15, 16, 23, 42]
with open("resources/numbers.txt", mode="wt") as file:
    for number in numbers:
        file.write(f"{number}")
