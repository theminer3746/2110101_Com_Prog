list1 = input().strip().split()
list2 = input().strip().split()

crypter1 = {}
crypter2 = {}

for i in range(len(list1)):
    crypter1[list1[i]] = list2[i]
    crypter2[list2[i]] = list1[i]

sentence = input().strip().split()

cryptic = ''

for word in sentence:
    if word in list1:
        cryptic += crypter1[word]
    elif word in list2:
        cryptic += crypter2[word]
    else:
        cryptic += word

    cryptic += ' '

print(cryptic)
