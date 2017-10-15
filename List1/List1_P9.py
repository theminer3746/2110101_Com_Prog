data = input().strip().split()
switch = [int(y) for y in input().split()]

arranged = list()

for i in range(len(data)):
    arranged.append(data[switch[i]])

print(*arranged)
