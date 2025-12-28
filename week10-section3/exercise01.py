n = 100_000_000

with open("resources/out.txt", mode="wt" ) as txt_file:
    txt_file.write(f"{n}")

with open("resources/out.bin", mode="wb") as bin_file:
    bin_file.write(n.to_bytes(4,byteorder="big",signed=False))

