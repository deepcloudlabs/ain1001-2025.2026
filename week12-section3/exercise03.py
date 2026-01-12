import re

names = [
    "Ayşe",
    "Şule",
    "Şima"
]
pattern1 = "\\w{5,7}"
pattern2 = "[a-zA-Z0-9_İışŞçÇüÜöÖğĞ]+"
pattern3 = "[3-7]"
pattern4 = "\\d"
pattern6 = "[0-9]"
pattern5 = "[f-OF-O]+"
for name in names:
    if re.fullmatch(pattern2, name):
        print(name)