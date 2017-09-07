text = input().strip()
a1 = input().strip()
a2 = input().strip()

output = ''

for char in text:
    if char == a1:
        output += a2
    elif char == a2:
        output += a1
    else:
        output += char

print(output)
