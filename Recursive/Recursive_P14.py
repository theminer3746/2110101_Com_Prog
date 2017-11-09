amount, current, target = [int(x) for x in input().split()]

source_list = []
destination_list = []

for i in range(amount):
    source, destination = [int(x) for x in input().split()]
    source_list.append(source)
    destination_list.append(destination)

def travel(current, target, source_list, destination_list):
    if current == target:
        return True
    else:
        possible_ways = source_list.count(current)

        if possible_ways > 1:
            indices = [i for i, x in enumerate(source_list) if x == current]
            for indice in indices:
                if travel(destination_list[indice], target, source_list, destination_list):
                    return True
            else:
                return False
        elif possible_ways == 1:
            indice = source_list.index(current)
            return travel(destination_list[indice], target, source_list, destination_list)
        else:
            return False

if travel(current, target, source_list, destination_list):
    print('yes')
else:
    print('no')
