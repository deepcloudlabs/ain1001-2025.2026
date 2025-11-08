from mpmath import *
mp.pretty = True
mp.dps = 100
x = 4 * atan(1)
print(x)
x = limit(lambda n: (1 + 1/n) ** n, inf)
print(x)
