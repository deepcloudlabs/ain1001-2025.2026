import re

credit_cards = [
    "1234-1234-5678-9088",
    "123-1234-5678-9088",
    "1234-1234-5678",
    "1234-1234-56a8-9088",
    "1234-1234-5678-1234-1234",
]
pattern = "\\d{4}-\\d{4}-\\d{4}-\\d{4}"
for credit_card in credit_cards:
    if re.fullmatch(pattern, credit_card):
        print(credit_card, " is valid.")
    else:
        print(credit_card, " is NOT valid.")
