import re

pattern = "^a[a-z]{8,}n$"
with open("resources/dictionary-eng.txt", mode="rt") as dictionary:
    for word in dictionary:
        if re.fullmatch(pattern, word.strip()):
            print(word,end="")