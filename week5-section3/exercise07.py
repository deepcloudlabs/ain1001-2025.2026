"""
7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16
  -> 8 -> 4 -> 2 -> 1
"""
longest = 0
for n in range(10_000_000, 100_000_000):
    sequence = [n]
    p = n
    while p > 1:
        if p % 2 == 0:
            p = p // 2
        else:
            p = 3 * p + 1
        sequence.append(p)
    if longest < len(sequence):
        longest = len(sequence)
        print(f"n: {n}, length: {len(sequence)}")
