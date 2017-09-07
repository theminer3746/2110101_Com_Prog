text = input().strip()
a1 = input().strip()
a2 = input().strip()

output = ''

for char in text:
    if char in a1:
        position = a1.find(char)

        output += a2[position]
    elif char in a2:
        position = a2.find(char)

        output += a1[position]
    else:
        output += char

print(output)
