import re

text = "1, 2,          3,\t\t\t\t    \t \t4,   \t \t\t   5,                6,    7"
pattern = "\\s*,\\s*"
print(text.split(","))
print(text.split(pattern))
print(re.split(pattern, text))