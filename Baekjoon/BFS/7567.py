from collections import deque


m, n, h = map(int, input().split(' '))

field = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        field[i][j] = list(map(int, input().split(' ')))


count = 1
answer = 0
q = deque()


def solution():
    global count
    global field

    while q:
        dy = [0, 0, -1, 1, 0, 0]
        dx = [-1, 1, 0, 0, 0, 0]
        dh = [0, 0, 0, 0, -1, 1]
        rh, ry, rx = q.popleft()

        for i in range(6):
            nh = rh+dh[i]
            ny = ry+dy[i]
            nx = rx+dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m or nh < 0 or nh >= h or field[nh][ny][nx] == 1 or field[nh][ny][nx] == -1:
                continue
            elif field[nh][ny][nx] == 0:
                q.append((nh, ny, nx))
                field[nh][ny][nx] = field[rh][ry][rx] + 1


for k in range(h):  # 높이
    for i in range(n):  # 세로
        for j in range(m):  # 가로
            if field[k][i][j] == 1:
                q.append((k, i, j))

solution()

for i in field:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))

print(answer-1)
