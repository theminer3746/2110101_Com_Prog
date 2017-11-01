file = open('books.txt')

books = {}
books_list = []
for line in file:
    line = line.strip().split(',')
    books[line[0]] = ([x.strip() for x in line[1:]])
    books_list.append(line[0])

needles = input().strip().split(',')
needles = [x.strip() for x in needles]

found = {}

for needle in needles:
    found[needle] = set()
    for book in books:
        if needle in books[book]:
            found[needle].add(book)

results = set.intersection(*found.values())
if len(results) == 0:
    print('Not found')
else:
    for book in books_list:
        if book in results:
            print(book)
