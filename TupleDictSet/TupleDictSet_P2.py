amount = int(input())

course = {}

for i in range(amount):
    current = input().strip().split(', ')
    for j in range(1, len(current)):
        if current[j] not in course:
            course[current[j]] = set([current[0]])
        else:
            course[current[j]].add(current[0])

needles = input().strip().split(', ')
for needle in needles:
    if needle in course:
        print(needle, '->', ', '.join(sorted(course[needle])))
    else:
        print(needle, '-> Not found')
