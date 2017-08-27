n = int(input())

result = 0

for i in range(0, n, 3):
    if i % 5 != 0:
        result += i

for j in range(0, n, 5):
    result += j

print(result)
