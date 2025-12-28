for number in range(1, 1_000_000):
    number_of_digits = len(str(number))
    mod = 10 ** number_of_digits # mod: 100
    automorphic_number = number ** 2 # 625 % 100 => 25
    if number % mod == automorphic_number % mod:
        print(number)
