r, c = map(int, input().split(' '))

board = []
for _ in range(r):
    board.append(list(map(str, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

check_list = [0] * 26
check_list[ord(board[0][0]) - ord('A')] = 1

max_result = 0
current = [0, 0]
alphabet_list = [board[0][0]]


def dfs(index):
    global max_result
    global current

    if max_result < len(alphabet_list):
        max_result = len(alphabet_list)

    if index == 26:
        return

    for i in range(4):
        if current[0] + dx[i] < 0 or current[1] + dy[i] < 0:
            continue

        if current[0] + dx[i] >= r or current[1] + dy[i] >= c:
            continue

        alphabet = board[current[0] + dx[i]][current[1] + dy[i]]
        if check_list[ord(alphabet) - ord('A')] == 0:
            check_list[ord(alphabet) - ord('A')] = 1
            current = [current[0] + dx[i], current[1] + dy[i]]
            alphabet_list.append(alphabet)

            dfs(index + 1)

            check_list[ord(alphabet) - ord('A')] = 0
            current = [current[0] - dx[i], current[1] - dy[i]]
            alphabet_list.pop()


dfs(0)
print(max_result)
