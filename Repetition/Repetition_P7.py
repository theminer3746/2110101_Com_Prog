line_count, needle = [int(x) for x in input().split()]

counter = 0
for i in range(line_count):
    value = int(input())

    if value == needle:
        counter += 1

print(counter)
