from collections import deque

n, m = map(int, input().split(' '))
graph = []
result = False

for _ in range(n):
    graph.append(list(map(int, input())))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def solution(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 1

    while q:
        y, x = q.popleft()

        if y == n-1:
            return True

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m or graph[ny][nx] == 1:
                continue
            else:
                graph[ny][nx] = 1
                q.append((ny, nx))


for j in range(m):
    if solution(0, j) == True:
        result = True
        break

if result:
    print('YES')
else:
    print('NO')
