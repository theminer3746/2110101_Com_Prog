amount = int(input())

data = {}
order = []

for i in range(amount):
    current = input().strip().split(':')
    user = current[0]
    cities = current[1]
    cities = set(x.strip() for x in cities.split(','))

    data[user] = cities
    order.append(user)

needle = input().strip()

keys = list(data.keys())
keys.remove(needle)

found = []

for key in keys:
    intersect = data[key] & data[needle]

    if len(intersect) != 0:
        found.append(key)

sorted_found = []

for user in order:
    if user in found:
        sorted_found.append(user)

if len(sorted_found) != 0:
    for item in sorted_found:
        print(item)
else:
    print('Not Found')
