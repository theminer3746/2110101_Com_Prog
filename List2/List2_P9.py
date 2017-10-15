data = [int(x) for x in input().strip().split()]

odd = []
even = []

for bit in data:
    if bit % 2 == 0:
        even.append(bit)
    else:
        odd.append(bit)

even.sort()
odd.sort(reverse=True)

print(*(even + odd))
