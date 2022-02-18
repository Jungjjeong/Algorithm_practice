from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split(' '))

field = []
empty = []
answer = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
    f = list(map(int, input().split(' ')))
    field.append(f)
    for j in range(m):
        if f[j] == 0:
            empty.append((i, j))  # 0이어서 벽을 놓을 수 있어

c_empty = list(combinations(empty, 3))
# 벽을 놓는 경우의 수


def solution(ry, rx, tmp_field):
    global dx, dy

    q = deque()
    q.append((ry, rx))
    tmp_field[ry][rx] = 2

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and tmp_field[ny][nx] == 0:
                q.append((ny, nx))
                tmp_field[ny][nx] = 2


for c in c_empty:
    tmp_answer = 0
    tmp_field = copy.deepcopy(field)

    for i in range(3):
        tmp_field[c[i][0]][c[i][1]] = 1

    for i in range(n):
        for j in range(m):
            if tmp_field[i][j] == 2:
                solution(i, j, tmp_field)

    for i in range(n):
        for j in range(m):
            if tmp_field[i][j] == 0:
                tmp_answer += 1

    answer = max(answer, tmp_answer)


print(answer)
