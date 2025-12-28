# global variable
z = 42

def sun(x,y):
    global z
    z = x ** 2 + y ** 2
    m = 100
    return x ** y + z

sun(2,2)
print(m)
print(z)
