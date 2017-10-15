filename = input().strip()

file = open(filename, 'r')

graded = []
used_student_id = []

for line in file:
    data = line.strip().split(';')

    if data[0] == '':
        continue

    if data[0] in used_student_id:
        continue
    else:
        used_student_id.append(data[0])

    score = float(data[3]) + float(data[4])

    if score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    else:
        grade = 'F'

    graded.append([data[0], data[1] + ' ' + data[2], grade])

while True:
    target_id = input().strip()

    if target_id == '-1':
        break

    if target_id in used_student_id:
        print(graded[used_student_id.index(target_id)])
    else:
        print('Not Found')
