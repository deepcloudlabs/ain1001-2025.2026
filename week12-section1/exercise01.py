import re

fruits = ["Apple", "pEAr", "cheRRy", "pomegraNAte", "pEAch", "BANANA",
          "waterMElon", "melON", "kiWi", "blackbeRRy", "sOUr cherry", "black mulbeRRy",
          "strawBErry", "cornELian cherry", "Fig", "cURrant", "raspbeRRy", "12345"
          ]
pattern1 = "....."
pattern2 = "[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]"
pattern3 = "[a-zA-Z]{5}"
pattern4 = "[a-zA-Z ]{8,}"
pattern5 = "[a-zA-Z ]{,5}"
pattern6 = "[a-zA-Z ]+"  # at least one
pattern7 = "[a-zA-Z ]{1,}"
pattern8 = "[a-zA-Z ]*"  # any number of times
pattern9 = "[a-zA-Z ]{0,}"
pattern10 = "[a-zA-Z ]?"  # none or one
pattern11 = "[a-zA-Z ]{0,1}"
pattern12 = "[^a-zA-Z ]+"
pattern13 = "[0-9]+"
pattern14 = "\\d+"
pattern15 = r"\d+"
pattern16 = r"\w+"
patterns17 = "[3-7]+"
patterns18 = "[f-oM-T]+"
for fruit in fruits:
    if re.fullmatch(pattern16, fruit):
        print(fruit, len(fruit))
