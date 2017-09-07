s = input().strip().lower()

vowel_count = 0
consonant_count = 0

for char in s:
    if 'a' <= char.lower() <= 'z':
        if char.lower() in 'aeiou':
            vowel_count += 1
        else:
            consonant_count += 1

print(vowel_count, consonant_count)
