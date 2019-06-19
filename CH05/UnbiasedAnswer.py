import random

def UnbiasedAnswer():
    while(True):
        x = random.randint(0,1)
        y = random.randint(0,1)
        if x != y:
            return x
