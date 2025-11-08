from mpmath import *
mp.dps = 100; mp.pretty = True
x = limit(lambda n: (1+1/n) ** n, inf)
print(x)