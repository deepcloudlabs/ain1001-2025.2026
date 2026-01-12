import re

dictionary_path = "dictionary/resources/dictionary-eng.txt"
with open(dictionary_path,mode="rt",encoding="utf-8") as dictionary_file:
    words = [line.strip() for line in dictionary_file.readlines()]

def search_word(search_text: str):
    regexp = re.compile(search_text)
    for word in words:
        if regexp.fullmatch(word):
            yield word