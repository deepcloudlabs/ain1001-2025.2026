for number in range(100,1_000_000):
    numberAsString = str(number)
    sum_of_digits_cubed = 0
    for digit in numberAsString:
        sum_of_digits_cubed += int(digit) ** 3
#    for i in range(len(numberAsString)):
#        digit = numberAsString[i]
#        sum_of_digits_cubed += int(digit) ** 3
    if sum_of_digits_cubed == number:
        print(f"{number} is an Armstrong number!")