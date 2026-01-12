import re
pattern= "\\d{3}-\\d{3}-\\d{4}"
text = "Ben Linus, Home: 555-555-5555, Business: 444-444-4444"
phones = re.findall(pattern, text)
for phone in phones:
    print(phone)