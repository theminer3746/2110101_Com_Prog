dna = input().strip()
command = input().strip()

dna = dna.upper()

for protein in dna:
    if protein not in 'ATGC':
        print('Invalid DNA')
        exit(0)

if command == 'R':
    reverse = dna.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
    reverse = reverse.upper()[::-1]
    print(reverse)
elif command == 'F':
    A = 0
    T = 0
    G = 0
    C = 0

    for protein in dna:
        if protein == 'A':
            A += 1
        elif protein == 'T':
            T += 1
        elif protein == 'G':
            G += 1
        elif protein == 'C':
            C += 1

    print('A='+ str(A) +', T='+ str(T) +', G='+ str(G) +', C=' + str(C))
elif command == 'D':
    needle = input().strip().upper()
    count = 0
    for pos in range(len(dna)):
        if dna[pos:pos + 2] == needle:
            count += 1
    print(count)
