import re

full_name = "JAMES SAWYER"
result = re.search("james", full_name, flags=re.IGNORECASE)
print("found" if result else "not found")