def get_evens(numbers):
    print("get_evens() started")
    for number in numbers:
        print(f"[gen_evens] Working on {number}")
        if number % 2 == 0:
            print(f"[gen_evens] Yielding {number}")
            yield number
    print("get_evens() finishes")

for i in get_evens(range(1,1_000)):
    print(f"[for] consuming {i}")