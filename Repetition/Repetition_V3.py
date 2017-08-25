from math import sqrt, ceil

n = int(input())

x_list = list()
y_list = list()

# Retrieve all possible x, y combination
for x in range(ceil(sqrt(n)) + 1):
    for y in range(ceil(sqrt(n)) + 1):
        if x**2 + y**2 == n:
            x_list.append(x)
            y_list.append(y)

# Remove duplication
x_to_remove = list()
y_to_remove = list()

for i in range(len(x_list)):
    if y_list.count(x_list[i]) != 0:
        index_to_remove = y_list.index(x_list[i])
        if index_to_remove > i:  # If index_to_remove < i, that mean we already passed it
            x_to_remove.append(x_list[index_to_remove])
            y_to_remove.append(y_list[index_to_remove])

for i in range(len(x_to_remove)):
    x_list.remove(x_to_remove[i])
    y_list.remove(y_to_remove[i])

# Sorting answer
for i in range(len(x_list)):
    if x_list[i] > y_list[i]:
        x_list[i], y_list[i] = y_list[i], x_list[i]

# Print the answer(s)
if len(x_list) == 0:
    print('No solution')
else:
    for i in range(len(x_list)):
        print(x_list[i], y_list[i])
