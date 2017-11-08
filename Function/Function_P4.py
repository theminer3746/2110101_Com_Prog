def det3(m):
    a = m[0][0]*m[1][1]*m[2][2]
    b = m[0][1]*m[1][2]*m[2][0]
    c = m[0][2]*m[1][0]*m[2][1]
    d = m[0][2]*m[1][1]*m[2][0]
    e = m[0][0]*m[1][2]*m[2][1]
    f = m[0][1]*m[1][0]*m[2][2]
    return a + b + c - d - e - f

def det4(m):
    n1 = matrix[0][0] * det3([
         [matrix[1][1], matrix[1][2], matrix[1][3]],
         [matrix[2][1], matrix[2][2], matrix[2][3]],
         [matrix[3][1], matrix[3][2], matrix[3][3]]
    ])

    n2 = matrix[0][1] * det3([
         [matrix[1][0], matrix[1][2], matrix[1][3]],
         [matrix[2][0], matrix[2][2], matrix[2][3]],
         [matrix[3][0], matrix[3][2], matrix[3][3]]
    ])

    n3 = matrix[0][2] * det3([
         [matrix[1][0], matrix[1][1], matrix[1][3]],
         [matrix[2][0], matrix[2][1], matrix[2][3]],
         [matrix[3][0], matrix[3][1], matrix[3][3]]
    ])

    n4 = matrix[0][3] * det3([
         [matrix[1][0], matrix[1][1], matrix[1][2]],
         [matrix[2][0], matrix[2][1], matrix[2][2]],
         [matrix[3][0], matrix[3][1], matrix[3][2]]
    ])

    return n1 - n2 + n3 - n4

matrix = []
for i in range(4):
    matrix.append([int(e) for e in input().split()])

print(det4(matrix))
