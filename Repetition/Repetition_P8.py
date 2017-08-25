total_length = int(input())

high = 0

for a in range(total_length // 2):
    for b in range(total_length // 2):
        c = total_length - a - b
        if a ** 2 + b ** 2 == c ** 2:
            high = max(a, b, c, high)

print(high)
