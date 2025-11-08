x = "\u20ba"
print(x)
y = "\ud834\udd1e"
print(len(y))
x = "müller"
y = "mueller"
print(y.encode("utf-16","surrogatepass").decode("utf-16"))