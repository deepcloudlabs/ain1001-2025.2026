for i in range(2,20,3): # i: 2 -> 5 -> 8 -> 11 -> 14
    if i % 4 == 0: # False -> False -> True ->
        continue
    if i % 7 == 0:
        break
    print(i ** 3)