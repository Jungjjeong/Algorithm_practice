from collections import deque


test_num = int(input())


def solution(ry, rx, field):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    q = deque()
    q.append((ry, rx))
    field[ry][rx] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= len(field) or nx < 0 or nx >= len(field[0]) or field[ny][nx] == 0:
                continue
            elif field[ny][nx] == 1:
                q.append((ny, nx))
                field[ny][nx] = 0


for _ in range(test_num):
    m, n, k = map(int, input().split(' '))
    field = [[0] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split(' '))
        field[y][x] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                solution(i, j, field)
                count += 1

    print(count)
