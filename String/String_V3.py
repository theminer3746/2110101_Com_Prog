import pprint

haystack = input().lower()
needle = input().lower()

haystack_processed = ''

for i in haystack:
    if i in '\"\'’,.()':
        haystack_processed += ' '
    else:
        haystack_processed += i

if needle in haystack_processed.split():
    print('Found')
else:
    print('Not Found')
