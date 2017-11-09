text = [char for char in input().strip()]

unique = set()

def branch(text, pos):
    if pos == len(text):
        unique.add(''.join(text))
        return None

    if text[pos].isupper():
        without = text.copy()
        without[pos] = ''
        branch(without, pos + 1)

    contain = text.copy()
    branch(contain, pos + 1)

branch(text, 0)

unique_sorted = [x for x in sorted(unique) if x != '']

for item in unique_sorted:
    print(item)
