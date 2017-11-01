course = {}
while True:
    data = input().strip()

    if data == '-1':
        break

    data = data.split()

    student_id = data[0]

    for i in range(1, len(data)):
        if data[i] not in course:
            course[data[i]] = set([student_id])
        else:
            course[data[i]].add(student_id)

needle = input().strip().split()

if needle[0] not in course:
    element0 = set()
else:
    element0 = course[needle[0]]

if needle[1] not in course:
    element1 = set()
else:
    element1 = course[needle[1]]

intersect = element0 & element1
xor = element0 ^ element1
union = element0 | element1

print(len(intersect), len(xor), len(union))
