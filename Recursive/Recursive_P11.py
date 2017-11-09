def same_row(i,j):
    return (i//9 == j//9)
def same_col(i,j):
    return (i-j) % 9 == 0
def same_block(i,j):
    return (i//27 == j//27 and i%9//3 == j%9//3)
def show(board):
    for i in range(3):
        print('+---+---+---+')
        for j in range(3):
            k = 9*(3*i+j)
            print('|'+board[k:k+3]+'|'+board[k+3:k+6]+'|'+board[k+6:k+9]+'|')
    print('+---+---+---+')
def solve(board):
    if '.' not in board:
        return board

    main_pos = board.find('.')
    s = set()
    for j in range(81):
        if same_row(main_pos, j):
            s.add(board[j])

        if same_col(main_pos, j):
            s.add(board[j])

        if same_block(main_pos, j):
            s.add(board[j])
    T = {'1', '2', '3', '4', '5', '6', '7', '8', '9'} - s

    for e in T:
        newboard = board[:main_pos] + e + board[main_pos + 1:]
        sol = solve(newboard)
        if sol != '' : return sol
    return ''

sol = solve(input().strip())
show(sol)
