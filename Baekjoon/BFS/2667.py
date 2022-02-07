from collections import deque

n = int(input())
map_list = []
for _ in range(n):
    map_list.append(list(map(int, input())))

result = []
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def solution(y, x):
    q = deque()
    q.append((y, x))
    map_list[y][x] = 0
    count = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n or map_list[ny][nx] == 0:
                continue
            else:
                map_list[ny][nx] = 0
                count += 1
                q.append((ny, nx))

    result.append(count)


for i in range(n):
    for j in range(n):
        if map_list[i][j] == 1:
            solution(i, j)

result.sort()
print(len(result))
for i in result:
    print(i)
