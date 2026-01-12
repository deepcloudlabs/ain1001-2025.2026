import re
pattern1 = "^[a-zA-Z]{5}$"
pattern2 = "^d[a-zA-Z]*n$"
pattern3 = "^[^aeiou]*$"
pattern4 = "^$"
with open("resources/dictionary-eng.txt", mode="rt") as dictionary:
    number_of_empty_lines = 0
    for word in dictionary:
        if re.match(pattern4,word):
            number_of_empty_lines += 1
    print(number_of_empty_lines)