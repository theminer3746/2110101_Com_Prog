s = input().strip()

capital_letter_count = 0

for i in s:
    if 'A' <= i <= 'Z':
        capital_letter_count += 1

print(capital_letter_count)
