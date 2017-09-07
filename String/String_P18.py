line_amount = int(input())

first_word = input().strip()

current_prefix = first_word
current_suffix = first_word[::-1]

for i in range(line_amount - 1):
    current_word = input().strip()

    for j in range(len(current_prefix)):
        if current_word[j] != current_prefix[j]:
            current_prefix = current_prefix[:j]
            break

    for k in range(len(current_suffix)):
        if current_word[::-1][k] != current_suffix[k]:
            current_suffix = current_suffix[:k]
            break

if current_prefix == '':
    print('NO COMMON PREFIX')
else:
    print(current_prefix)

if current_suffix == '':
    print('NO COMMON SUFFIX')
else:
    print(current_suffix[::-1])
