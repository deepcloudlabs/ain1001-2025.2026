def is_automorphic(n: int) -> bool:
    if n < 0:
        n = -n
    k = len(str(n))
    mod = 10 ** k
    return (n * n) % mod == n % mod

for number in range(1, 100_000):
    if is_automorphic(number):
        print(number)