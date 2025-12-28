x = "\u20ba"
print(len(x))
print(x)
y = "\ud834\udd1e"
print(len(y))
print(y.encode("utf-16", "surrogatepass").decode("utf-16"))
x = "müller"
y = "mueller"
print(x == y)
