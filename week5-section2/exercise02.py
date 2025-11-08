def is_even(number):
    return number % 2 == 0

x = 42
if is_even(x):
    print(f"{x} is even")
else:
    print(f"{x} is odd")
