import re

credit_cards = [
    "1234-1234-1234-1234",
    "1234-1234-1234-12a4",
    "1234-1234-1234-123",
    "1234-1234-1234-1234-1234",
    "1234-1234-1234",
]

pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"
for card in credit_cards:
    if not re.fullmatch(pattern, card):
        print(card)