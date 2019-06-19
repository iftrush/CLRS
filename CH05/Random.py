import math, random
from math import floor, ceil

def Random(a,b):

    if a == b:
        return a
    mid = (a+b)/2
    r = random.randint(0,1)
    if r == 0:
        return Random(a, floor(mid))
    else:
        return Random(ceil(mid), b)

# DRIVER
print(Random(0,1))
