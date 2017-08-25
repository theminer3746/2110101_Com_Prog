base2 = input()

base10 = 0

for i in range(len(base2)):
    base10 += int(base2[i]) * (2 ** (len(base2) - i - 1))

print(base10)
