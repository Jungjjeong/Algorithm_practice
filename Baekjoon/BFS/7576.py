from collections import deque


m, n = map(int, input().split(' '))

field = []
for _ in range(n):
    field.append(list(map(int, input().split(' '))))

count = 1
answer = 0
q = deque()


def solution():
    global count

    while q:
        dy = [0, 0, -1, 1]
        dx = [-1, 1, 0, 0]
        y, x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m or field[ny][nx] == 1 or field[ny][nx] == -1:
                continue
            elif field[ny][nx] == 0:
                q.append((ny, nx))
                field[ny][nx] = field[y][x] + 1


for i in range(n):
    for j in range(m):
        if field[i][j] == 1:
            q.append((i, j))

solution()

for i in field:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer-1)
