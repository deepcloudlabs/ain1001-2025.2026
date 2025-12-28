n = 100_000_000

with open("resources/out.txt",mode="wt") as file:
    file.write(f"{n}")
    
with open("resources/out.bin",mode="wb") as file:
    file.write(n.to_bytes(4))