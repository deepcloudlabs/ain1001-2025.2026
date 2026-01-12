import re

fruits = ["Apple", "pAEr", "cheRRy", "pomegraNAte", "pEAch", "BANANA",
          "waterMElon", "melON", "kiWi", "blackbeRRy", "sOUr cherry", "black mulbeRRy",
          "strawBErry", "cornELian cherry", "Fig", "cURrant", "raspbeRRy", "12345"
          ]

pattern1 = "[a-zA-Z]{5}"
pattern2 = "[a-zA-Z]{1,}"
pattern3 = "[a-zA-Z]+" # at least once
pattern4 = "[a-zA-Z]{0,}"
pattern5 = "[a-zA-Z]*"  # any number of times
pattern6 = "[a-zA-Z]{0,1}"
pattern7 = "[a-zA-Z]?"  # none or one
for fruit in fruits:
    if re.fullmatch(pattern2, fruit):
        print(fruit, len(fruit))
