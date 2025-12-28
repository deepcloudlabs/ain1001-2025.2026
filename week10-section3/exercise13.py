import pandas as pd

df = pd.read_excel("resources/employees.xlsx")
print(df)
df = pd.read_xml("resources/employees.xml")
print(df)
df = pd.read_json("resources/employees.json")
print(df)