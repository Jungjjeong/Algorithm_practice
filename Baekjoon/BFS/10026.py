from collections import deque


n = int(input())
field = []
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for _ in range(n):
    field.append(list(map(str, input())))

visited = [[0 for _ in range(n)] for _ in range(n)]
true_visited = [[0 for _ in range(n)] for _ in range(n)]


def true_solution(y, x, ra):
    global dy, dx

    q = deque()
    q.append((y, x, ra))
    true_visited[y][x] = 1

    while q:
        y, x, a = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and true_visited[ny][nx] == 0:
                if ((field[ny][nx] == 'R' or field[ny][nx] == 'G') and (ra == 'R' or ra == 'G')) or field[ny][nx] == 'B' and ra == 'B':
                    q.append((ny, nx, a))
                    true_visited[ny][nx] = 1


def solution(y, x, ra):
    global dy, dx

    q = deque()
    q.append((y, x, ra))
    visited[y][x] = 1

    while q:
        y, x, a = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0 and field[ny][nx] == ra:
                q.append((ny, nx, a))
                visited[ny][nx] = 1


count = 0
true_count = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            solution(i, j, field[i][j])
            count += 1
        if true_visited[i][j] == 0:
            true_solution(i, j, field[i][j])
            true_count += 1

print(count, true_count)
