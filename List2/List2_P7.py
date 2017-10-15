file = open('score.txt')

student_id = []

for line in file:
    student_id.append(line.strip().split()[0])

student_id.sort()

for id in student_id:
    print(id)
