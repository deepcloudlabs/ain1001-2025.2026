import re

text = "kate                     austen,         e-mail:           kate@example.com"
pattern = "([a-zA-Z]+)\\s+([a-zA-Z]+),\\s+e-mail:\\s+(\\w+@\\w+.\\w{2,5})"
result = re.search(pattern, text)
print("first name: ",result.group(1))
print("last name: ",result.group(2))
print("e-mail: ",result.group(3))