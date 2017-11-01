dept_amount = int(input())

dept = {}

for x in range(dept_amount):
    dept_name, maximum_student = input().strip().split()

    dept[dept_name] = [int(maximum_student), []]

student_amount = int(input())

student_data = []

for y in range(student_amount):
    data = input().strip().split()

    student_data.append([data[0], float(data[1]), data[2:]])

student_data.sort(key=lambda student_data:student_data[1], reverse=True)

result = {}

for student in student_data:
    for department in student[2]:
        if len(dept[department][1]) < dept[department][0]:
            dept[department][1].append(student[0])
            result[student[0]] = department
            break

ordered_student_id = list(result.keys())
ordered_student_id.sort()

for student_id in ordered_student_id:
    print(student_id, result[student_id])
