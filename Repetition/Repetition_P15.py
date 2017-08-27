n = int(input())

# Upper part
upper_line = list()

side_dot_counter = 1
for sharp_counter in range(n - 2, 1, -2):
    upper_line.append('.' * side_dot_counter + '#' * sharp_counter + '.' * (side_dot_counter * 2 + 1) + '#' * sharp_counter + '.' * side_dot_counter)
    side_dot_counter += 1

upper_line.reverse()

# Magic part
magic_line = list()
magic_line.append('#' * n + '.' + '#' * n)

# Middle part
middle_line = list()

full_row_count = (n // 2) - 2
if full_row_count <= 0:
    full_row_count = 1
else:
    full_row_count += 1

for j in range(1, full_row_count + 1):
    middle_line.insert(j, '#' * ((2 * n) + 1))

# Lower part
lower_line = list()

for k in range(0, n):
    lower_line.append('.' * (k + 1) + '#' * (len(middle_line[0]) - ((k + 1 )* 2)) + '.' * (k + 1))

# Print it all out
for upper in range(0, len(upper_line)):
    print(upper_line[upper])

print(magic_line[0])

for middle in range(0, len(middle_line)):
    print(middle_line[middle])

for lower in range(0, len(lower_line)):
    print(lower_line[lower])
