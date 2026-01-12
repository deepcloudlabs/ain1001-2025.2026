import re
fruits = ["Apple", "pEAr", "cheRRy", "pomegraNAte", "pEAch", "BANANA",
          "waterMElon", "melON", "kiWi", "blackbeRRy", "sOUr cherry", "black mulbeRRy",
          "strawBErry", "cornELian cherry", "Fig", "cURrant", "raspbeRRy", "12345"
          ]
pattern1="....."
pattern2="[a-z ]{5}"
pattern3="[a-z ]{5,7}"
pattern4="[a-z ]{5,}"
pattern5=".....+"
pattern6="[a-zA-Z ]*"
pattern7="[^a-z ]*"
pattern8="[0-9]+"
pattern9="\\d+" # digits
pattern10="\\w+" # alphabet letters + digits + underscore
pattern11="\\D+" # non-digit
pattern12="\\W+" #
for fruit in fruits:
    if re.fullmatch(pattern6, fruit):
        print(fruit,len(fruit))