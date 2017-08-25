import math

x = float(input())

base = 1 + x

third = x**2 / math.factorial(2)
forth = x**3 / math.factorial(3)
fifth = x**4 / math.factorial(4)

print(third)
print(forth)
print(fifth)
print(base + third + forth + fifth)