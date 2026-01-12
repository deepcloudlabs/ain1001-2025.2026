import re

empty_line_pattern = "^$"
with open("resources/dictionary-eng.txt", mode="rt") as dictionary:
    empty_lines = 0
    for word in dictionary:
        if re.fullmatch(empty_line_pattern, word.strip()):
            empty_lines += 1
    print(empty_lines)