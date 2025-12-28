def get_evens(numbers: list[int]) -> list[int]:
    print("get_evens() is just started.")
    for number in numbers:
        if number % 2 == 0:
            yield number

print("Application is just started!")
result = get_evens(range(1,1_000))
for even_number in result:
    print(even_number)
print("Application is just completed!")
