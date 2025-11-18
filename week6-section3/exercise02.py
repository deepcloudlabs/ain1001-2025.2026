number = 3333
number_as_str = str(number)
for i in range(len(number_as_str)):
    for j in range(i+1,len(number_as_str)):
        if number_as_str[i] == number_as_str[j] and i != j:
            print(f"repeated digit: {number_as_str[i]}")
            break