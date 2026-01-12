import re

full_name = "JACK SHEPHARD"
result = re.search("jack", full_name, flags=re.IGNORECASE)
print("found" if result else "not found")
