board = []
zero_set = []
board_c = [[0] * 9 for _ in range(9)]
board_r = [[0] * 9 for _ in range(9)]
board_square = [[0] * 9 for _ in range(9)]

for i in range(9):
    board.append(list(map(int, input())))

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero_set.append((i, j))
        else:
            board_c[i][board[i][j] - 1] = 1
            board_r[j][board[i][j] - 1] = 1
            board_square[3*(i//3) + j//3][board[i][j] - 1] = 1

answer_list = []


def dfs(index):
    if index == len(zero_set):
        for i in range(9):
            print(*board[i], sep='')
        return -1

    for i in range(1, 10):
        if board_c[zero_set[index][0]][i-1] == 0 and board_r[zero_set[index][1]][i-1] == 0 and board_square[3*(zero_set[index][0]//3) + (zero_set[index][1]//3)][i-1] == 0:
            board_c[zero_set[index][0]][i-1] = 1
            board_r[zero_set[index][1]][i-1] = 1
            board_square[3*(zero_set[index][0]//3) +
                         (zero_set[index][1]//3)][i-1] = 1
            board[zero_set[index][0]][zero_set[index][1]] = i
            answer_list.append(i)
            if dfs(index + 1) == -1:
                return -1
            board_c[zero_set[index][0]][i-1] = 0
            board_r[zero_set[index][1]][i-1] = 0
            board_square[3*(zero_set[index][0]//3) +
                         (zero_set[index][1]//3)][i-1] = 0
            board[zero_set[index][0]][zero_set[index][1]] = 0
            answer_list.pop()


dfs(0)
