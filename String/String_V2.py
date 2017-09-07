s = input()

output = ''

for i in s:
    if i in '\"\'’,.()':
        output += ' '
    else:
        output += i

print(output)
