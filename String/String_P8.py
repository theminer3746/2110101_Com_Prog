data = input().strip().lower()

last_char = ''
special_string = 'yes'

for char in data:
    if char < last_char:
        special_string = 'no'
        break

    last_char = char

print(special_string)
