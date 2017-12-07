import numpy as np

amount = int(input())

price = []

for i in range(amount):
    price.append(float(input().strip().split()[1]))

price = np.array(price)

sales = []

for j in range(amount):
    sales.append([float(x) for x in input().strip().split()[1:]])

sales = np.array(sales)

for datum in price.dot(sales):
    print(datum)
