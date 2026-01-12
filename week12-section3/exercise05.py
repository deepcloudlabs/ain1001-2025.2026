import re
#un/semi-structured data
line = "kate         austen,        email:              kate.austen@example.com"
pattern = "([a-zA-Z]+)\\s+([a-zA-Z]+),\\s*email:\\s+(\\w+\\.?\\w*)@(\\w+\\.\\w{2,5})"
result = re.search(pattern, line)
# structured data
kate = {
    "first_name": result.group(1),
    "last_name": result.group(2),
    "user_name": result.group(3),
    "domain_name": result.group(4)
}
print(kate)
