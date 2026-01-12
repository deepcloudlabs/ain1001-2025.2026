from dictionary import search_word

for word in search_word("^[a-zA-Z]{12,}\n$"):
    print(word)