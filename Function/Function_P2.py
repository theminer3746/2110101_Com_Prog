import math

def nextEven(f):
    num = math.ceil(f)

    if num % 2 == 0:
        return num
    else:
        return num + 1

def nextOdd(f):
    num = math.ceil(f)

    if num % 2 == 1:
        return num
    else:
        return num + 1

while True:
    x = float(input())
    if x < 0:
        break
    even = nextEven(x)
    odd = nextOdd(x)
    print( (even, odd) )
