import re

text = "Jack Shephard, Home: 555-555-5555, Business: 444-444-4444, Mobile: 333-333-3333"
pattern = "\\d{3}-\\d{3}-\\d{4}"
phones = re.findall(pattern, text)
for phone in phones:
    print(phone)