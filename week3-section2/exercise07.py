x = 3
y = 5
print(x, y)
x = x ^ y # ^ : xor
y = x ^ y
x = x ^ y
print(x, y)
""" or
  False False False
  False True  True
  True  False True
  True  True  True
"""
""" xor
  False False False
  False True  True
  True  False True
  True  True  False
"""
