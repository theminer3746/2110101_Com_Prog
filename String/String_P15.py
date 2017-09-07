data = input().strip()

duplicate_alphabet = ''
duplicate_alphabet_count = list()

for char in data:
    if data.count(char) > 1 and char not in duplicate_alphabet:
        duplicate_alphabet += char
        duplicate_alphabet_count.append(0)

output = ''

for char in data:
    if char in duplicate_alphabet:
        position = duplicate_alphabet.find(char)
        duplicate_alphabet_count[position] += 1
        if duplicate_alphabet_count[position] == 2:
            output += char
    else:
        output += char

print(output)

