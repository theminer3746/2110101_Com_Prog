data = input().strip()

if data[0] not in '+-':
    data = '+' + data

all_value = list()
current_value = ''
multiplier = 1

for char in data:
    if char == '+':
        if current_value != '':
            all_value.append(multiplier * int(current_value))
            current_value = ''

        multiplier = 1
    elif char == '-':
        if current_value != '':
            all_value.append(multiplier * int(current_value))
            current_value = ''

        multiplier = -1
    else:
        current_value += char

all_value.append(multiplier * int(current_value))

print(sum(all_value))
