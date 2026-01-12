import re

credit_cards = [
    "1234-1234-1234-1234",
    "1234-1234-1234-1a34",
    "1234-1234-1234",
    "1234-1234-1234-1234-1234",
    "123-123-123-123"
]
pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"
for card in credit_cards:
    if re.fullmatch(pattern, card):
        print(card)