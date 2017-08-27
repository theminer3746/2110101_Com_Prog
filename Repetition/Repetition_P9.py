a, b, c, x1, d = [float(q) for q in input().split()]

current_x = x1
counter = 0
while True:
    next_x = current_x - ((a * (current_x ** 2) + b * current_x + c) / (2 * a * current_x + b))
    counter += 1

    if abs(next_x - current_x) < d:
        break

    current_x = next_x

print(counter)
