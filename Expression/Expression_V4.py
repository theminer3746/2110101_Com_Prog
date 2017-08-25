import math

weight = float(input())
height = float(input())

Mosteller = math.sqrt(weight * height) / 60
Haycock = 0.024265 * (weight ** 0.5378) * (height ** 0.3964)
Boyd = 0.0333 * (weight ** (0.6157 - (0.0188 * math.log10(weight)))) * (height ** 0.3)

print(str(Mosteller))
print(str(Haycock))
print(str(Boyd))
