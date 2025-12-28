def fun(a, b):
    s = 0 # 3 -> 1
    for i in range(a): # i:0, i:1
        if i % 2 == 0: # True
            s = s + b + i
        else:
            s = s - 2
    return s
print("fun(2, 3):", fun(2, 3))
print("fun(3, 1):", fun(3, 1))
print("fun(4, 2):", fun(4, 2))
