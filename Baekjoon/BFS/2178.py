from collections import deque

n, m = map(int, input().split(' '))
stage = []

for _ in range(n):
    stage.append(list(map(int, input())))


def solution(root):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    q = deque()
    q.append(root)

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if stage[ny][nx] == 1:
                q.append((ny, nx))
                stage[ny][nx] = stage[y][x] + 1

    return stage[n-1][m-1]


print(solution((0, 0)))
