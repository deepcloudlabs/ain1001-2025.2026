import re

text = "kate                austen,        e-mail:              kate@lostisland.org" # semi-structured
print(text)
pattern = "([a-zA-Z]+)\\s+([a-zA-Z]+),\\s+e-mail:\\s+(\\w+)@(\\w+\\.\\w{2,5})"
result = re.search(pattern, text)
print("First Name : ",result.group(1))
print("Last  Name : ",result.group(2))
print("User Name  : ",result.group(3))
print("Domain Name: ",result.group(4))
kate = {
    "first_name": result.group(1),
    "last_name": result.group(2),
    "user_name": result.group(3),
    "domain_name": result.group(4),
}
print(kate) # structured data