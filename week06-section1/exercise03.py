def gun(x : int =1, y : int =2, z : int =10) -> int:
    return x * y + z ** 2

gun(10,20,30)
gun(x=10,y=20,z=30)
gun(y=20,x=10)