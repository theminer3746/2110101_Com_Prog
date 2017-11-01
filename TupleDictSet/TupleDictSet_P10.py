amount = int(input())

data = []

for i in range(amount):
    data.append(input().strip() + ' ')

queries = input().strip().split()

results = []

for query in queries:
    current = set()

    for student in data:
        if ' ' + query + ' ' in student:
            current.add(student)

    results.append(current)

result_set = set.intersection(*results)

result_list = []

for student in result_set:
    result_list.append(student.strip())

result_list.sort()

if len(result_list) != 0:
    for student in result_list:
        print(student)
else:
    print('Not Found')
