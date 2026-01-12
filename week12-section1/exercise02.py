import re

names = [
    "şule", "Şima", "ümit"
]
pattern = "[a-zA-ZüşÜŞİığĞçÇöÖ]+"
for name in names:
    if re.fullmatch(pattern, name):
        print(name)