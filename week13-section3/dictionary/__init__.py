import re

dictionary_path = "dictionary/resources/dictionary-eng.txt"
with open(dictionary_path, mode="rt", encoding="utf-8") as dictionary_file:
    words = [word.strip() for word in dictionary_file.readlines()]


def search_dictionary(regexp: str):
    search_regexp = re.compile(regexp)
    for word in words:
        if search_regexp.fullmatch(word):
            yield word