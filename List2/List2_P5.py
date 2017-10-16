amount = int(input())

data = []

for i in range(amount):
    data.append(int(input()))

data.sort(reverse=True)

for bit in data:
    print(bit)
