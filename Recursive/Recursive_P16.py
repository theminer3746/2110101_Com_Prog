def B_to_A(working, output):
    if type(working) is not list:
        return working

    if type(working[0]) is not list:
        if len(working) > 1:
            if type(working[1][0]) is not list:
                output.append(working[0])
                print('here', output)
                print('working', working[1])
                output.append(B_to_A(working[1], output))

                return output
            else:
                partial_output = []
                for item in working[1]:
                    print(item, 'is', output)
                    partial_output.append(B_to_A(item, output))

                return partial_output
        else:
            output.append(working[0])
            print('xkcd')
            return output
    else:
        pass

data = eval(input().strip())

print(B_to_A(data, []))
