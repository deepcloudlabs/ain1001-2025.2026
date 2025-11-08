def gun(x: int=0, y: float=0, z: float=0) -> float:
    return x * y + z

print(gun())  # gun(0,0,0)
print(gun(3)) # gun(3,0,0)
print(gun(z=3.2)) # gun(0,0,3.2)
