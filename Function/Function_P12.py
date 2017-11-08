def eat(q1,q2):
    if q1[0] == q2[0]:
        return True
    elif q1[1] == q2[1]:
        return True
    elif abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return True
    else:
        return False
def all_eat(L):
    eatable = []
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if eat(L[i], L[j]):
                eatable.append((i,j))

    return eatable

print(eval(input().strip()))
