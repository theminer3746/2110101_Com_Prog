amount, current, target = [int(x) for x in input().split()]

source_list = []
destination_list = []

for i in range(amount):
    source, destination = [int(x) for x in input().split()]
    source_list.append(source)
    destination_list.append(destination)

traversable = []

def travel(current, target, source_list, destination_list, path):
    if current == target:
        traversable.append(path)
    else:
        possible_ways = source_list.count(current)

        if possible_ways > 1:
            indices = [i for i, x in enumerate(source_list) if x == current]
            for pos in indices:
                next_station = destination_list[pos]
                current_path = path.copy()
                current_path.append(next_station)
                travel(next_station, target, source_list, destination_list, current_path)
        elif possible_ways == 1:
            pos = source_list.index(current)
            next_station = destination_list[pos]
            current_path = path.copy()
            current_path.append(next_station)
            return travel(next_station, target, source_list, destination_list, current_path)
        else:
            return False

path = [current]
travel(current, target, source_list, destination_list, path)

if len(traversable) == 0:
    print('no')
else:
    unique_traversable = []
    for option in traversable:
        if option not in unique_traversable:
            unique_traversable.append(option)

    unique_traversable.sort()

    for option in unique_traversable:
        option = [str(x) for x in option]
        print(' -> '.join(option))
