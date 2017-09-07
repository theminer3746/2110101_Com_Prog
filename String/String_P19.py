long_word = input().strip()
short_word = input().strip()

if len(short_word) > len(long_word):
    short_word, long_word = long_word, short_word

common_alphabet = long_word

for alphabet in common_alphabet:
    if alphabet not in short_word:
        common_alphabet = common_alphabet.replace(alphabet, '')

upper = list()
lower = list()
for a in common_alphabet:
    if a not in upper and a.isupper():
        upper.append(a)
    elif a not in lower and not a.isupper():
        lower.append(a)

if upper == list() and lower == list():
    print('NONE')
else:
    upper.sort()
    lower.sort()
    print(*lower, *upper)
