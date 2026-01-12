import re

print("The dictionary module is loaded")
with open("dictionary/resources/dictionary-eng.txt", mode="rt", encoding="utf-8") as dictionary_file:
    words = dictionary_file.readlines()

def search_word(regular_expression: str):
    for word in words:
        if re.fullmatch(regular_expression, word):
            yield word.strip()