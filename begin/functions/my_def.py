def funct1(x, y, z):
    value = x + 2*y + z**2
    if value > 0:
        return x + 2*y + z**2
    else:
        return 0


u, v = 3, 4

funct1(u, v, 2) # 15

funct1(u, z=v, y=2) # 23

def funct2(x, y=1, z=1):
    return x + 2 * y + z ** 2

funct2(3, z=4) # 21

def funct3(x, y=1, z=1, *tup):
    print((x, y, z) + tup)

funct3(2) # (2, 1, 1)
funct3(1, 2, 3, 4, 5, 6, 7, 8, 9) # (1, 2, 3, 4, 5, 6, 7, 8, 9)

def funct4(x, y=1, z=1, **kwargs):
    print(x, y, z, kwargs)


funct4(1, 2, m = 5, n=9, z=3) # 1 2 3 {'n': 9, 'm': 5}