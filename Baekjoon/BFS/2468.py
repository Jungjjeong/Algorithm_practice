from collections import deque


n = int(input())
stage = []

max_num = 0

for _ in range(n):
    s_list = list(map(int, input().split(' ')))
    max_num = max(max_num, max(s_list))
    stage.append(s_list)

visited = [[0] * n for _ in range(n)]


def solution(ry, rx, w):
    if visited[ry][rx] == 1:
        return False

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque()
    q.append((ry, rx))
    visited[ry][rx] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and stage[ny][nx] > w and visited[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = 1

    return True


answer = 0

for w in range(max_num):
    count = 0
    for i in range(n):
        for j in range(n):
            if stage[i][j] > w and solution(i, j, w):
                count += 1
    answer = max(answer, count)
    visited = [[0] * n for _ in range(n)]

print(answer)
