n = int(input())

result = 0
for i in range(n+1):
    for j in range(i+1):
        for k in range(j, 0, -1):
            result += ((-1) ** i) * j * k

print(result)
