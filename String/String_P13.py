data = input().strip().lower()

vowel_group_count = 0
last_char_is_vowel = False

for char in data:
    if char in 'aeiou' and not last_char_is_vowel:
        vowel_group_count += 1
        last_char_is_vowel = True
    elif char not in 'aeiou':
        last_char_is_vowel = False

print(vowel_group_count)
