a,b,c = [float(e) for e in input().split()]

if a != 0:
    if b*b >= 4*a*c:
        t = b*b - 4*a*c

        r1 = (-b+t**0.5)/(2*a); tr1 = "{:.2f}".format(r1)
        r2 = (-b-t**0.5)/(2*a); tr2 = "{:.2f}".format(r2)

        if tr1 == tr2:
            print(tr1)
        else:
            print(*sorted([tr1, tr2]))
    else:
        print('Roots are complex numbers')
else:
    if b == 0:
        if c == 0:
            print('Roots are any numbers')
        else:
            print('No roots exists')
    else:
        print(-c / b)
