from collections import deque


m, n, k = map(int, input().split(' '))
# 문제 잘 읽자, 여기서는 m이 세로다.
map_list = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    ld_x, ld_y, ru_x, ru_y = map(int, input().split(' '))

    for i in range(ld_y, ru_y):
        for j in range(ld_x, ru_x):
            map_list[i][j] = 1


def solution(y, x):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    q = deque()
    q.append((y, x))
    map_list[y][x] = 1
    count = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < m and 0 <= nx < n and map_list[ny][nx] == 0:
                q.append((ny, nx))
                map_list[ny][nx] = 1
                count += 1

    return count


count = 0
area_count = []

for i in range(m):
    for j in range(n):
        if map_list[i][j] == 0:
            area_count.append(solution(i, j))
            count += 1

area_count.sort()
print(count)
print(*area_count)
