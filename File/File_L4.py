import re

filename = input().strip()
replace_count = int(input())
needle = input()
replace = input()

file = open(filename, 'r')
data = file.read()
file.close()
if replace_count == 0:
    print(data)
else:
    needle = needle.replace('\n', '')
    needle = needle.replace('\r', '')
    print(re.sub(re.escape(needle), replace, data, replace_count, flags=re.IGNORECASE))
