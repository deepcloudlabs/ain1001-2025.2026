for i in range(2,20,3):
    if i % 4 == 0:
        continue
    if i % 7 == 0:
        break
    print(i ** 3)