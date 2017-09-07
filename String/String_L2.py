s = input().strip().lower()

longest = 0
current_length = 0
last_char = ''

for i in range(len(s)):
    if s[i] != last_char:
        if current_length > longest:
            longest = current_length
        current_length = 1
        last_char = s[i]
    else:
        current_length += 1

if current_length > longest:
    longest = current_length

print(longest)
