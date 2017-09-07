mode = input().strip()
s = input().strip()
find_string = input().strip()
replace_string = input().strip()

out = ""

found_index = s.lower().find(find_string.lower())
while found_index >= 0:
    out += s[0:found_index] + replace_string

    s = s[found_index + len(find_string):]

    if mode == "R":
        break
    found_index = s.lower().find(find_string.lower())

print(out + s)
