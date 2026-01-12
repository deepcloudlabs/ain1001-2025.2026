import re
pattern = "\\s*,\\s*"
csv_text = "1, 2,        \t\t\t    \n \t 3,       4\n\t\t,       5      ,6\n,   7   "
print(csv_text.split("\\s*,\\s*"))
print([s.strip() for s in re.split(pattern,csv_text)])