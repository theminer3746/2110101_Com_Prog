def read_data():
    docs = {}
    n = int(input().strip())
    for i in range(n):
        tokens = input().strip().split()
        doc_name = tokens[0]
        doc_keywords = tokens[1:]
        for kword in doc_keywords:
            if kword in docs.keys():
                docs[kword].add(doc_name)
            else:
                docs[kword] = {doc_name}
    return docs

def search(docs, condition, search_keywords):
    match = []
    for keyword in search_keywords:
        if keyword in docs.keys():
            match.append(docs[keyword])
        else:
            match.append(set())

    if match == []:
        return []

    if condition == 'and':
        return list(set.intersection(*match))
    elif condition == 'or':
        return list(set.union(*match))
    else:
        return []

docs = read_data()
tokens = input().split()
print(sorted(search(docs, tokens[0], tokens[1:])))
