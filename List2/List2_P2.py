data = input().strip()

pos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
counter = [0] * len(pos)

for char in data:
    counter[pos.index(char)] += 1

print(*counter)
