competitor_name = []
all_guess = []

while True:
    datum = input().strip().split()
    #print(datum)

    if datum[0] == 'end':
        break

    #print(datum[1:])

    if datum[0] in competitor_name:
        pos = competitor_name.index(datum[0])
        for guess in datum[1:]:
            if guess not in all_guess[pos]:
                all_guess[pos].append(guess)
        #guess[pos] = list(set(guess[pos]).union(set(datum[1:])))
        #competitor[datum[0]] = competitor[datum[0]].union(set(datum[1:]))
    else:
        competitor_name.append(datum[0])
        all_guess.append([])
        for guess in datum[1:]:
            if guess not in all_guess[-1]:
                all_guess[-1].append(guess)

        #guess.append(sorted(set(datum[1:])))
        #competitor[datum[0]] = set(datum[1:])
        #print(competitor[datum[0]])

#print(competitor_name)
#print(all_guess)

candidate_name = competitor_name.copy()
candidate_guess = all_guess.copy()

#available_guess = all_guess
#print(sorted(zip(candidate_name, candidate_guess), key = lambda x : len(x[1])))

taken = []
result = []

for i in range(len(competitor_name)):
    considering = sorted(zip(candidate_name, candidate_guess), key = lambda x : len(x[1]))[0]
    for guess in considering[1]:
        if guess not in taken:
            result.append((considering[0], guess))
            taken.append(guess)
            pos = candidate_name.index(considering[0])
            candidate_name.pop(pos)
            candidate_guess.pop(pos)
            break

for item in result:
    print(*item)
