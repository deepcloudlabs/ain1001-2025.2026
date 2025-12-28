for number in range(100,1_000_000):
    best_friend = 1
    for divisor in range(2,number//2+1):
        if number % divisor == 0:
            best_friend += divisor
    total = 1
    for divisor in range(2,best_friend//2+1):
        if best_friend % divisor == 0:
            total += divisor
    if total == number:
        print(number,best_friend)