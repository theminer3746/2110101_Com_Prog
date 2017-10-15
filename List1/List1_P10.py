data = [int(x) for x in input().strip().split(', ')]

puddle_count = 0
in_puddle = False

for x in data:
    if x < 0 and not in_puddle:
        puddle_count += 1
        in_puddle = True
    elif x >= 0:
        in_puddle = False

print(puddle_count)
