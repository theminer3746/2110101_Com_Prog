def B_to_A(working):
    if type(working) is not list:
        return working

    if type(working[0]) is list:
        pass
    else:
        # recurse

        pass

print(B_to_A(eval(input().strip())))
